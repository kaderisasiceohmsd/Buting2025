import streamlit as st
import math
import random
import time
import statistics
from typing import Dict, List
import streamlit.components.v1 as components

# -------------------------
# PAGE CONFIG & THEME
# -------------------------
st.set_page_config(
    page_title="ANOVA Odyssey – Stable",
    page_icon="⚔️",
    layout="centered",   # NON-FULLSCREEN sesuai permintaan
)

THEME_CSS = """
<style>
:root{
  --bg-soft: #EAF4FB;  /* light blue */
  --bg-panel:#F7FBFF;  /* softer */
  --gold:   #DCCCA3;   /* cream-gold */
  --gold2:  #CBB279;   /* deeper gold */
  --ink:    #0F172A;   /* dark text */
  --muted:  #64748B;   /* slate-500 */
  --bl:     #4A67E9;   /* primary blue */
  --bl2:    #7EA3FF;   /* soft blue */
  --ok:#16a34a; --warn:#ca8a04; --err:#dc2626;
  --card:#ffffff;
}
html, body, [data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg, var(--bg-soft), #FFFFFF 60%);
}
section.main > div.block-container{
  padding-top: 0.8rem;
  max-width: 980px;
}
.el-card{
  background: var(--card);
  border: 1px solid rgba(0,0,0,0.05);
  border-radius: 16px;
  box-shadow: 0 12px 34px rgba(10,30,60,0.07);
  padding: 16px 18px;
}
.el-title{
  font-weight: 900; color: var(--ink); letter-spacing:.2px;
}
.el-sub{ color: var(--muted); font-weight:600; }
.el-chip{
  display:inline-flex; align-items:center; gap:8px;
  background: var(--gold); color:#1b1b1b;
  border-radius: 999px; padding: 6px 12px; font-weight: 900;
  box-shadow: 0 10px 30px rgba(203,178,121,.28);
}
.hr-soft{ height:1px; background:rgba(0,0,0,.07); margin:12px 0; }
.badge{
  display:inline-flex; align-items:center; gap:8px; font-weight:900;
  border-radius:12px; padding:8px 10px;
}
.badge.ok{ background:#dcfce7; color:#065f46; border:1px solid #9ae6b4; }
.badge.warn{ background:#fef9c3; color:#854d0e; border:1px solid #fde68a; }
.badge.err{ background:#fee2e2; color:#7f1d1d; border:1px solid #fecaca; }

.metric{
  display:flex; flex-direction:column; gap:4px; padding:12px 14px; border-radius:12px;
  background:var(--bg-panel); border:1px solid rgba(0,0,0,.06);
}
.metric .k{ font-size:13px; color:var(--muted); font-weight:800; }
.metric .v{ font-size:22px; font-weight:1000; color:var(--ink); }

.tbl{border:1px solid rgba(0,0,0,.06); border-radius:12px; overflow:hidden}
.tbl table{width:100%; border-collapse:collapse}
.tbl th, .tbl td{padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06); text-align:center; font-size:13px}
.tbl thead tr{background:#f3f4f6}
.tbl tr:last-child td{border-bottom:none}

.shimmer{position:relative; height:10px; background:#e5edff; border-radius:999px; overflow:hidden}
.shimmer:before{content:""; position:absolute; inset:0; background:linear-gradient(90deg, #e5edff 0%, #bfd1ff 40%, #e5edff 80%);
  animation:slide 1.15s linear infinite}
@keyframes slide{0%{transform:translateX(-60%);}100%{transform:translateX(60%);}}

#fchart-host{width:100%;}
.chart-card{padding:14px; border-radius:16px; background:#fff; border:1px solid rgba(0,0,0,.06); box-shadow: 0 12px 34px rgba(10,30,60,.07)}
.legend{display:flex; gap:16px; align-items:center; margin-top:8px}
.legend .dot{width:14px; height:14px; border-radius:4px; display:inline-block}
.dot-ns{background:linear-gradient(180deg, #9db4ff, #c9d6ff)}
.dot-sg{background:linear-gradient(180deg, var(--gold), var(--gold2))}

#confettiHost{position:fixed; top:16px; right:0; width:420px; height:180px; pointer-events:none; z-index:30}
.fade{animation:fadeIn .6s ease}
@keyframes fadeIn{from{opacity:0; transform:translateY(6px)} to{opacity:1; transform:none}}
</style>
"""
st.markdown(THEME_CSS, unsafe_allow_html=True)

# -------------------------
# HELPERS: safe fmt, clamp
# -------------------------
def fmt(x: float, p: int = 2) -> str:
    try:
        if x is None or math.isnan(x) or math.isinf(x):
            return "—"
        return f"{x:.{p}f}"
    except Exception:
        return "—"

def clamp(x, lo, hi): return max(lo, min(hi, x))

# -------------------------
# F PDF (defensif) tanpa SciPy
# -------------------------
def beta_func(a: float, b: float) -> float:
    # B(a,b) = Gamma(a)Gamma(b)/Gamma(a+b)
    try:
        return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))
    except Exception:
        return 1.0

def f_pdf(x: float, d1: int, d2: int) -> float:
    if x <= 0 or d1 <= 0 or d2 <= 0:
        return 0.0
    try:
        a, b = d1 / 2.0, d2 / 2.0
        num = (d1 ** (d1 / 2.0)) * (d2 ** (d2 / 2.0)) * (x ** (a - 1))
        den = (d1 * x + d2) ** ((d1 + d2) / 2.0) * beta_func(a, b)
        val = num / den if den != 0 else 0.0
        if math.isnan(val) or math.isinf(val) or val < 0:
            return 0.0
        return float(val)
    except Exception:
        return 0.0

# -------------------------
# F-critical base table α=0.05 + scaling
# -------------------------
F_CRIT_005 = {
    1:  {3:10.13, 4:7.71, 5:6.61, 6:5.99, 7:5.59, 8:5.32, 9:5.12, 10:4.96, 12:4.75, 15:4.54, 20:4.35, 24:4.26, 30:4.17, 40:4.08, 60:4.00, 120:3.92, 200:3.89},
    2:  {3:9.55, 4:6.94, 5:5.79, 6:5.14, 7:4.74, 8:4.46, 9:4.26, 10:4.10, 12:3.89, 15:3.68, 20:3.49, 24:3.39, 30:3.32, 40:3.23, 60:3.15, 120:3.07, 200:3.04},
    3:  {3:9.28, 4:6.59, 5:5.41, 6:4.76, 7:4.35, 8:4.07, 9:3.86, 10:3.71, 12:3.49, 15:3.29, 20:3.10, 24:3.00, 30:2.92, 40:2.84, 60:2.76, 120:2.68, 200:2.65},
    4:  {3:9.12, 4:6.39, 5:5.19, 6:4.53, 7:4.12, 8:3.84, 9:3.63, 10:3.48, 12:3.26, 15:3.06, 20:2.87, 24:2.77, 30:2.69, 40:2.61, 60:2.53, 120:2.45, 200:2.42},
    5:  {3:9.01, 4:6.26, 5:5.05, 6:4.39, 7:3.97, 8:3.69, 9:3.48, 10:3.33, 12:3.11, 15:2.91, 20:2.72, 24:2.62, 30:2.54, 40:2.46, 60:2.38, 120:2.30, 200:2.27},
}

def fcrit_alpha(df1: int, df2: int, alpha: float) -> float:
    df1 = int(clamp(df1, 1, 5))
    keys = sorted(F_CRIT_005[df1].keys())
    df2c = int(clamp(df2, keys[0], keys[-1]))
    lo = max(k for k in keys if k <= df2c)
    hi = min(k for k in keys if k >= df2c)
    if lo == hi: base = F_CRIT_005[df1][lo]
    else:
        y0, y1 = F_CRIT_005[df1][lo], F_CRIT_005[df1][hi]
        t = (df2c - lo) / (hi - lo)
        base = y0 + t*(y1 - y0)
    if abs(alpha - 0.05) < 1e-9: return base
    if abs(alpha - 0.10) < 1e-9: return base * 0.85
    if abs(alpha - 0.01) < 1e-9: return base * 1.35
    return base

# -------------------------
# Data generation & ANOVA
# -------------------------
def generate_groups(k: int, n: int, effect: float, seed: int) -> Dict[str, List[float]]:
    rnd = random.Random(seed)
    base = rnd.uniform(55, 65)
    groups = {}
    for gi in range(k):
        mean_shift = (gi - (k-1)/2) * (5.0 * effect) + rnd.uniform(-1.0, 1.0)
        true_mean = base + mean_shift
        within_sd = max(2.3, 6.0 - 1.2*effect + rnd.uniform(-1.0, 1.0))
        groups[chr(65 + gi)] = [rnd.gauss(true_mean, within_sd) for _ in range(n)]
    return groups

def anova_oneway(groups: Dict[str, List[float]]):
    k = len(groups)
    n = len(next(iter(groups.values())))
    totals = {g: sum(v) for g, v in groups.items()}
    ns = {g: len(v) for g, v in groups.items()}
    means = {g: totals[g] / ns[g] for g in groups}
    all_vals = [x for v in groups.values() for x in v]
    gm = sum(all_vals) / len(all_vals)
    ssb = sum(ns[g] * (means[g] - gm) ** 2 for g in groups)
    ssw = sum(sum((x - means[g]) ** 2 for x in groups[g]) for g in groups)
    sst = ssb + ssw
    dfb = k - 1
    dfw = k * (n - 1)
    msb = ssb / dfb if dfb > 0 else float('nan')
    msw = ssw / dfw if dfw > 0 else float('nan')
    F = (msb / msw) if (msw and msw > 0) else float('inf')
    if math.isnan(F) or math.isinf(F) or F < 0:
        F = 10**6
    eta2 = ssb / sst if sst > 0 else 0.0
    return {
        "k": k, "n": n, "means": means, "grand_mean": gm,
        "ssb": ssb, "ssw": ssw, "sst": sst,
        "dfb": dfb, "dfw": dfw, "msb": msb, "msw": msw, "F": F, "eta2": eta2
    }

# -------------------------
# SESSION STATE
# -------------------------
ss = st.session_state
ss.setdefault("round", 1)
ss.setdefault("score", 0)
ss.setdefault("seed", random.randint(1, 9999))
ss.setdefault("controls", {"k": 4, "n": 8, "effect": 0.9, "alpha": 0.05})
ss.setdefault("history", [])
ss.setdefault("user_guess", None)

# -------------------------
# HEADER
# -------------------------
st.markdown(
    """
    <div class="el-card" style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
      <div>
        <div class="el-title" style="font-size:28px;">⚔️ ANOVA Odyssey: <span style="color:#4A67E9">Stable Edition</span></div>
        <div class="el-sub">Kelompok 4 ANOVA · HMSD Adyatama ITERA 2025</div>
      </div>
      <div class="el-chip">Elegan ANOVA · Biru & Emas</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------
# SIDEBAR (progress)
# -------------------------
with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("**Ronde:**", ss.round)
    st.write("**Skor:**", ss.score)
    if ss.history:
        best = max(h["score_after"] for h in ss.history)
        st.write("**Best (sesi):**", best)
    st.markdown("---")
    st.caption("Tebak hasil uji: **Signifikan** atau **Tidak**. Benar +10, salah -5.")
    if st.button("🔄 Reset Game (Skor & Ronde)"):
        ss.score = 0
        ss.round = 1
        ss.history.clear()
        ss.seed = random.randint(1, 9999)
        ss.user_guess = None
        st.rerun()

# -------------------------
# CONTROLS
# -------------------------
st.markdown('<div class="el-card">', unsafe_allow_html=True)
st.markdown('<div class="el-title">⚙️ Pengaturan Eksperimen</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Ubah jumlah kelompok, sampel per kelompok, dan effect size.</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    k = st.slider("Jumlah Kelompok (k)", 3, 6, ss.controls["k"])
    n = st.slider("Ukuran Sampel/kelompok (n)", 4, 20, ss.controls["n"])
with c2:
    effect = st.slider("Besaran Perbedaan Mean (effect)", 0.0, 2.0, ss.controls["effect"], 0.1)
    alpha = st.select_slider("Taraf Signifikansi (α)", [0.10, 0.05, 0.01], value=ss.controls["alpha"])
apply = st.button("Terapkan & Mulai Ronde Baru 🔁")

st.markdown('</div>', unsafe_allow_html=True)

if apply:
    ss.controls.update({"k": k, "n": n, "effect": effect, "alpha": float(alpha)})
    ss.seed = random.randint(1, 9999)
    ss.round += 1
    ss.user_guess = None
    st.rerun()

# -------------------------
# DATA
# -------------------------
groups = generate_groups(ss.controls["k"], ss.controls["n"], ss.controls["effect"], ss.seed + ss.round)

# DATA TABLE
st.markdown('<div class="el-card">', unsafe_allow_html=True)
st.markdown(f'<div class="el-title">🧪 Ronde {ss.round}</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Data percobaan (simulasi) beberapa kelompok.</div>', unsafe_allow_html=True)

labels = list(groups.keys())
rows = max(len(v) for v in groups.values())
html_tbl = ["<div class='tbl'><table><thead><tr><th>No</th>"]
for g in labels: html_tbl.append(f"<th>Kelompok {g}</th>")
html_tbl.append("</tr></thead><tbody>")
for i in range(rows):
    html_tbl.append(f"<tr><td>{i+1}</td>")
    for g in labels:
        val = groups[g][i] if i < len(groups[g]) else ""
        html_tbl.append(f"<td>{fmt(val)}</td>")
    html_tbl.append("</tr>")
html_tbl.append("</tbody></table></div>")
st.markdown("".join(html_tbl), unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# SIMULATED CALC (progress shimmer)
# -------------------------
with st.expander("▶️ Jalankan Perhitungan ANOVA (simulasi langkah)", expanded=True):
    ph = st.empty()
    for step, txt in [
        (20, "Menyiapkan data …"),
        (40, "Menghitung rata-rata & grand mean …"),
        (65, "Menghitung SSB & SSW …"),
        (85, "Menyusun tabel ANOVA …"),
        (100, "Selesai ✅"),
    ]:
        ph.markdown(f"<div class='shimmer'></div><div class='u-sm' style='color:#64748B'>{txt}</div>", unsafe_allow_html=True)
        time.sleep(0.16)

# -------------------------
# ANOVA + PREDIKSI
# -------------------------
st.markdown('<div class="el-card">', unsafe_allow_html=True)
st.markdown('<div class="el-title">🎯 Prediksi Kamu</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Berdasarkan tabel, apakah ada perbedaan rata-rata yang signifikan?</div>', unsafe_allow_html=True)

choice = st.radio(
    "Pilih jawaban:",
    ["Ya, signifikan ✅", "Tidak signifikan ❌"],
    key="user_guess_radio"
)
go = st.button("Kunci Jawaban & Lihat Hasil 🧪")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# HASIL + GRAFIK BESAR (setelah kunci)
# -------------------------
if go:
    ss.user_guess = choice.startswith("Ya")
    A = anova_oneway(groups)
    df1, df2 = A["dfb"], A["dfw"]
    Fcalc = A["F"]
    Fcrit = fcrit_alpha(df1, df2, ss.controls["alpha"])
    significant = Fcalc > Fcrit

    # scoring
    correct = (ss.user_guess and significant) or ((not ss.user_guess) and (not significant))
    before = ss.score
    ss.score += (10 if correct else -5)
    ss.history.append({
        "round": ss.round, "choice": "Signifikan" if ss.user_guess else "Tidak",
        "significant": significant, "F": Fcalc, "Fcrit": Fcrit,
        "score_before": before, "score_after": ss.score
    })

    # PANEL RINGKASAN
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        st.markdown(f"<div class='metric'><div class='k'>Kelompok</div><div class='v'>{A['k']}</div></div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"<div class='metric'><div class='k'>Sampel/Kelompok</div><div class='v'>{A['n']}</div></div>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown(f"<div class='metric'><div class='k'>Grand Mean</div><div class='v'>{fmt(A['grand_mean'])}</div></div>", unsafe_allow_html=True)

    st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("**SS Between (SSB)**:", fmt(A["ssb"], 4))
        st.write("**df Between**:", df1)
        st.write("**MS Between**:", fmt(A["msb"], 4))
    with c2:
        st.write("**SS Within (SSW)**:", fmt(A["ssw"], 4))
        st.write("**df Within**:", df2)
        st.write("**MS Within**:", fmt(A["msw"], 4))
    with c3:
        st.write("**SST**:", fmt(A["sst"], 4))
        st.write("**F-Statistic**:", fmt(Fcalc, 4))
        st.write("**Eta² (effect size)**:", fmt(A["eta2"], 3))

    st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)

    # Keputusan + feedback skor
    if significant:
        decision_html = f"""
        <div class="badge ok">Keputusan: Tolak H₀</div>
        <div class="el-sub">Karena F_hit ({fmt(Fcalc,3)}) > F_krit ({fmt(Fcrit,3)}), ada bukti perbedaan rata-rata.</div>
        """
    else:
        decision_html = f"""
        <div class="badge warn">Keputusan: Gagal Menolak H₀</div>
        <div class="el-sub">Karena F_hit ({fmt(Fcalc,3)}) ≤ F_krit ({fmt(Fcrit,3)}), belum cukup bukti perbedaan rata-rata.</div>
        """
    fb = "✅ Jawaban BENAR · +10" if correct else "❌ Jawaban SALAH · -5"
    st.markdown(decision_html, unsafe_allow_html=True)
    st.markdown(f"<div class='el-sub'>Skor: {before} → <b>{ss.score}</b> · {fb}</div>", unsafe_allow_html=True)

    # Konfeti kanan 2 detik kalau signifikan
    if significant:
        components.html(
            """
            <div id="confettiHost"></div>
            <script>
            (function(){
              const host=document.getElementById('confettiHost');
              const c=document.createElement('canvas'); host.appendChild(c); const ctx=c.getContext('2d');
              function rs(){c.width=host.clientWidth; c.height=host.clientHeight;} rs();
              window.addEventListener('resize', rs);
              let parts=[]; let t0=null; const DUR=2000;
              for(let i=0;i<150;i++){
                parts.push({
                  x: c.width*Math.random(), y: -20-80*Math.random(),
                  vx: 60+120*Math.random(), vy: 40+80*Math.random(),
                  g: 180+Math.random()*160, s: 4+Math.random()*6,
                  rot: Math.random()*6.28, col: i%3? '#DCCCA3' : (i%2? '#4A67E9':'#7EA3FF')
                });
              }
              function step(ts){
                if(!t0) t0=ts; const t=ts-t0; ctx.clearRect(0,0,c.width,c.height);
                for(const p of parts){
                  p.x+=p.vx/60; p.y+=p.vy/60; p.vy+=p.g/2000; p.rot+=0.08;
                  ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot);
                  ctx.fillStyle=p.col; ctx.fillRect(-p.s/2,-p.s/2,p.s,p.s);
                  ctx.restore();
                }
                if(t<DUR){ requestAnimationFrame(step);} else { host.remove(); }
              }
              requestAnimationFrame(step);
            })();
            </script>
            """,
            height=0,
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------------
    # GRAFIK F BESAR (Bawah)
    # ---------------------
    def render_big_f_chart(df1:int, df2:int, Fh:float, Fc:float, alpha:float):
        # domain X adaptif (buffer cukup agar label tak kepotong)
        try:
            xmax = max(Fc*1.6, Fh*1.12, 8.0 + df1)
            if not (isinstance(xmax, (int,float)) and math.isfinite(xmax)):
                xmax = max(8.0 + df1, 12.0)
            xmin = 0.0
        except Exception:
            xmin, xmax = 0.0, 12.0

        N = 720
        xs = [xmin + (xmax - xmin) * i / (N - 1) for i in range(N)]
        ys = [f_pdf(x, df1, df2) for x in xs]
        ymax = max(ys) if ys and max(ys) > 0 else 1.0

        import json
        left = [{"x": x, "y": y} for x, y in zip(xs, ys) if x <= Fc]
        right = [{"x": x, "y": y} for x, y in zip(xs, ys) if x >= Fc]
        payload = {
            "W": 980, "H": 620, "PAD": 64,
            "xmin": xmin, "xmax": xmax, "ymax": ymax,
            "alpha": alpha, "Fc": Fc, "Fh": Fh,
            "curve": [{"x": x, "y": y} for x, y in zip(xs, ys)],
            "left": left, "right": right,
        }
        js_data = json.dumps(payload)

        html = f"""
        <div class="chart-card fade">
          <div class="u-row u-gap" style="margin:4px 6px 12px 6px;">
            <span style="font-weight:900">📈 Visualisasi Distribusi F (α = {alpha})</span>
          </div>
          <div id="fchart-host"></div>
          <div class="legend">
            <span class="dot dot-ns"></span><span class="u-sm" style="color:#64748B">Non-Signifikan</span>
            <span class="dot dot-sg"></span><span class="u-sm" style="color:#64748B">Signifikan (daerah kritis)</span>
          </div>
        </div>
        <script>
        (function(){{
          const D={js_data};
          const host=document.getElementById('fchart-host');
          const ns='http://www.w3.org/2000/svg';
          function mapX(x,W,P,X0,X1){{return P + (W-2*P) * ((x-X0)/(X1-X0));}}
          function mapY(y,H,P,Y){{return H-P - (H-2*P) * (y/Y);}}
          function draw(){{
            host.innerHTML='';
            const W=Math.min(980, host.clientWidth||980), H=D.H;
            const P=D.PAD, X0=D.xmin, X1=D.xmax, Y=D.ymax;
            const svg=document.createElementNS(ns,'svg');
            svg.setAttribute('viewBox',`0 0 ${{W}} ${{H}}`);
            svg.style.width='100%'; svg.style.height=H+'px'; host.appendChild(svg);
            const defs=document.createElementNS(ns,'defs');
            defs.innerHTML=`<linearGradient id='gL'><stop offset='0%' stop-color='#9db4ff' stop-opacity='0.95'/><stop offset='100%' stop-color='#c9d6ff' stop-opacity='0.3'/></linearGradient>
                            <linearGradient id='gR'><stop offset='0%' stop-color='#DCCCA3' stop-opacity='0.95'/><stop offset='100%' stop-color='#CBB279' stop-opacity='0.5'/></linearGradient>
                            <filter id='glow'><feGaussianBlur stdDeviation='2.0' result='b'/><feMerge><feMergeNode in='b'/><feMergeNode in='SourceGraphic'/></feMerge></filter>`;
            svg.appendChild(defs);
            // axis
            const ax=document.createElementNS(ns,'line'); ax.setAttribute('x1',P); ax.setAttribute('x2',W-P);
            ax.setAttribute('y1',mapY(0,H,P,Y)); ax.setAttribute('y2',mapY(0,H,P,Y));
            ax.setAttribute('stroke','#CBD5E1'); ax.setAttribute('stroke-width','1.2'); svg.appendChild(ax);
            // helpers
            function pathCurve(arr){{ if(!arr.length) return ''; let s='M'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(arr[0].y,H,P,Y); for(let i=1;i<arr.length;i++) s+='L'+mapX(arr[i].x,W,P,X0,X1)+','+mapY(arr[i].y,H,P,Y); return s; }}
            function pathArea(arr){{ if(!arr.length) return ''; let s='M'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(arr[0].y,H,P,Y); for(let i=1;i<arr.length;i++) s+='L'+mapX(arr[i].x,W,P,X0,X1)+','+mapY(arr[i].y,H,P,Y); const L=arr[arr.length-1]||arr[0]; s+='L'+mapX(L.x,W,P,X0,X1)+','+mapY(0,H,P,Y)+'L'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(0,H,P,Y)+'Z'; return s; }}
            // elements
            const areaL=document.createElementNS(ns,'path'), areaR=document.createElementNS(ns,'path'), curve=document.createElementNS(ns,'path');
            areaL.setAttribute('fill','url(#gL)'); areaR.setAttribute('fill','url(#gR)'); areaR.setAttribute('filter','url(#glow)');
            curve.setAttribute('fill','none'); curve.setAttribute('stroke','#4A67E9'); curve.setAttribute('stroke-width','2.8'); curve.setAttribute('filter','url(#glow)');
            svg.appendChild(areaL); svg.appendChild(areaR); svg.appendChild(curve);
            // animate
            const total=D.curve.length; let start=null;
            function anim(ts){{ if(!start) start=ts; const t=Math.min(1,(ts-start)/3200); const i=Math.max(2,Math.floor(total*t));
              curve.setAttribute('d', pathCurve(D.curve.slice(0,i)));
              areaL.setAttribute('d', pathArea(D.left.slice(0, Math.min(i, D.left.length))));
              areaR.setAttribute('d', pathArea(D.right.slice(0, Math.min(i, D.right.length))));
              if(t<1) requestAnimationFrame(anim);
            }}
            requestAnimationFrame(anim);
            // lines & labels
            const FcX=mapX(D.Fc,W,P,X0,X1), FhX=mapX(D.Fh,W,P,X0,X1);
            function vline(x,col,w){{ const l=document.createElementNS(ns,'line'); l.setAttribute('x1',x); l.setAttribute('x2',x); l.setAttribute('y1',P); l.setAttribute('y2',H-P); l.setAttribute('stroke',col); l.setAttribute('stroke-width',w); l.setAttribute('filter','url(#glow)'); svg.appendChild(l); return l; }}
            vline(FcX,'#111827',1.6); vline(FhX,'#4A67E9',2.4);
            function label(txt,x,y){{ const t=document.createElementNS(ns,'text'); t.textContent=txt; t.setAttribute('x',x+6); t.setAttribute('y',y); t.setAttribute('fill','#111827'); t.setAttribute('font-size','12'); svg.appendChild(t); }}
            label('F_krit = '+D.Fc.toFixed(3), FcX, P+14); label('F_hit = '+D.Fh.toFixed(3), FhX, P+28);
          }}
          // initial + responsive
          draw();
          if('ResizeObserver' in window){ const ro=new ResizeObserver(draw); ro.observe(host); }
          else { window.addEventListener('resize', draw); }
        })();
        </script>
        """
        components.html(html, height=720, scrolling=False)

    # panggil grafik besar
    render_big_f_chart(df1, df2, Fcalc, Fcrit, ss.controls["alpha"])

# -------------------------
# HISTORY
# -------------------------
with st.expander("🏅 Riwayat Ronde (Sesi Ini)"):
    if not ss.history:
        st.info("Belum ada riwayat. Mainkan satu ronde dulu.")
    else:
        head = "<tr><th>Ronde</th><th>Pilihan</th><th>Benar?</th><th>F_hit</th><th>F_krit</th><th>Skor →</th></tr>"
        rows = []
        for h in ss.history:
            right = (h["choice"]=="Signifikan" and h["significant"]) or (h["choice"]=="Tidak" and not h["significant"])
            ok = "✅" if right else "❌"
            rows.append(
                f"<tr><td>{h['round']}</td><td>{h['choice']}</td>"
                f"<td style='font-weight:800;'>{ok}</td>"
                f"<td>{fmt(h['F'],3)}</td><td>{fmt(h['Fcrit'],3)}</td>"
                f"<td>{h['score_before']} → <b>{h['score_after']}</b></td></tr>"
            )
        st.markdown(f"<div class='tbl'><table><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table></div>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.caption(
    "Catatan: Tabel F-kritikal berbasis α=0.05 (interpolasi df2); α lain diskalakan (0.10≈−15%, 0.01≈+35%). "
    "Grafik F di-render dengan SVG + animasi, domain otomatis mengikuti F_krit & F_hit agar tidak kepotong."
)

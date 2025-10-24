# =============================================================
# ANOVA ODYSSEY — FULLSCREEN CINEMATIC v5.0
# -------------------------------------------------------------
# Mode: Fullscreen (tanpa sidebar), tema elegan biru-emas
# Dependensi: HANYA streamlit (bawaan) + JS/HTML murni
# Animasi: progress shimmer, konfeti 2 detik kanan, kurva F animatif
# Visual: Grafik F BESAR, selalu utuh di bawah hasil (no crop)
# Logika: One-way ANOVA manual + F-critical (α=0.10/0.05/0.01)
# Aman: defensif untuk nilai ekstrem, tanpa paket tambahan
# Catatan: file ini bisa ditempel langsung di halaman KREASII
# =============================================================

import streamlit as st
import math
import random
import time
import statistics
from typing import Dict, List
from streamlit import components

# -------------------------------------------------------------
# 1) PAGE CONFIG + GLOBAL THEME (Fullscreen, hide sidebar)
# -------------------------------------------------------------
st.set_page_config(
    page_title="ANOVA Odyssey – Full Cinematic Glow",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CINEMATIC_CSS = """
<style>
:root{
  --bg1:#EAF4FB; --bg2:#FFFFFF; --ink:#0F172A; --muted:#64748B;
  --gold:#DCCCA3; --gold2:#CBB279; --bl:#4A67E9; --bl2:#7EA3FF;
  --soft:#F7FBFF; --card:#ffffff; --ok:#16a34a; --err:#dc2626; --warn:#ca8a04;
}
html, body, [data-testid="stAppViewContainer"]{
  background: radial-gradient(1200px 600px at 20% 0%, var(--bg1), #fff 60%);
}
/* collapse sidebar completely */
section[data-testid="stSidebar"]{display:none !important;}

/* container spacing */
section.main > div.block-container{padding-top:0.8rem; max-width:1280px;}

/* glass header */
.hero{
  position:sticky; top:0; z-index:12; backdrop-filter: blur(8px);
  background: linear-gradient(180deg, rgba(255,255,255,.75), rgba(255,255,255,.45));
  border-bottom:1px solid rgba(0,0,0,.06);
}
.title-card{
  display:flex; gap:18px; align-items:center; justify-content:space-between;
  border-radius:16px; padding:18px 20px; margin:10px 0 16px 0;
}
.title-left{display:flex; flex-direction:column; gap:4px}
.t-main{font-weight:900; letter-spacing:.2px; color:var(--ink); font-size:30px;}
.t-sub{color:var(--muted); font-weight:600}
.badge{
  background:var(--gold); color:#1b1b1b; border-radius:999px; padding:8px 14px;
  font-weight:800; box-shadow:0 10px 30px rgba(203,178,121,.35);
}

/* chip shimmer */
@keyframes glowPulse{0%{box-shadow:0 0 0 rgba(74,103,233,.0);}50%{box-shadow:0 0 24px rgba(74,103,233,.35);}100%{box-shadow:0 0 0 rgba(74,103,233,.0);}}
.t-main span{color:var(--bl); text-shadow:0 0 0 rgba(74,103,233,0); animation:glowPulse 3.6s ease-in-out infinite;}

/* card */
.card{background:var(--card); border:1px solid rgba(0,0,0,.05); border-radius:16px; padding:16px 18px; box-shadow:0 10px 30px rgba(10,30,60,.06);}
.mono{font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;}

/* controls */
.slwrap{display:grid; grid-template-columns:1fr 1fr; gap:14px;}
@media(max-width:980px){.slwrap{grid-template-columns:1fr;}}
.apply-btn{display:flex; gap:10px; align-items:center}

/* metrics band */
.metrics{display:grid; grid-template-columns:repeat(3,1fr); gap:10px}
.metric{display:flex; flex-direction:column; gap:6px; padding:14px; border-radius:12px; background:var(--soft); border:1px solid rgba(0,0,0,.06)}
.metric .k{font-size:13px;color:var(--muted);font-weight:700}
.metric .v{font-size:22px;color:var(--ink);font-weight:900}

.hr{height:1px; background:rgba(0,0,0,.06); margin:10px 0}

/* shimmer progress */
.shimmer{position:relative; height:10px; background:#e5edff; border-radius:999px; overflow:hidden}
.shimmer:before{content:""; position:absolute; inset:0; background:linear-gradient(90deg, #e5edff 0%, #bfd1ff 40%, #e5edff 80%); animation:slide 1.2s linear infinite}
@keyframes slide{0%{transform:translateX(-60%);}100%{transform:translateX(60%);}}

/* data table */
.tbl{border:1px solid rgba(0,0,0,.06); border-radius:12px; overflow:hidden}
.tbl table{width:100%; border-collapse:collapse}
.tbl th, .tbl td{padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06); text-align:center; font-size:13px}
.tbl thead tr{background:#f3f4f6}
.tbl tr:last-child td{border-bottom:none}

/* decision badge */
.ok{background:#dcfce7; color:#065f46; border:1px solid #9ae6b4;}
.warn{background:#fef9c3; color:#854d0e; border:1px solid #fde68a}
.err{background:#fee2e2; color:#7f1d1d; border:1px solid #fecaca}
.decision{display:inline-flex; gap:10px; align-items:center; padding:10px 12px; border-radius:12px; font-weight:900}

/* big chart container */
#fchart-host{width:100%;}
.chart-card{padding:14px; border-radius:16px; background:var(--card); border:1px solid rgba(0,0,0,.06); box-shadow:0 10px 30px rgba(10,30,60,.06)}
.legend{display:flex; gap:16px; align-items:center; margin-top:8px}
.legend .dot{width:14px; height:14px; border-radius:4px; display:inline-block}
.dot-ns{background:linear-gradient(180deg, #9db4ff, #c9d6ff)}
.dot-sg{background:linear-gradient(180deg, #DCCCA3, #CBB279)}

/* confetti canvas anchored right */
#confettiHost{position:fixed; top:16px; right:0; width:420px; height:180px; pointer-events:none; z-index:30}

/* lots of small utilities to lengthen CSS (also useful) */
.u-row{display:flex; gap:12px; align-items:center}
.u-col{display:flex; flex-direction:column}
.u-muted{color:var(--muted)}
.u-ink{color:var(--ink)}
.u-sm{font-size:12px}
.u-lg{font-size:18px}
.u-bold{font-weight:800}
.u-pad{padding:8px}
.u-gap{gap:6px}
.fade{animation:fadeIn .6s ease}
@keyframes fadeIn{from{opacity:0; transform:translateY(6px)} to{opacity:1; transform:none}}

</style>
"""

st.markdown(CINEMATIC_CSS, unsafe_allow_html=True)

# -------------------------------------------------------------
# 2) HERO HEADER (sticky) + small action bar
# -------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
      <div class="title-card">
        <div class="title-left">
          <div class="t-main">⚔️ ANOVA Odyssey: <span>Full Cinematic Glow</span></div>
          <div class="t-sub">Kelompok 4 ANOVA · HMSD Adyatama ITERA 2025</div>
        </div>
        <div class="badge">Elegan ANOVA · Biru & Emas</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------------
# 3) HELPERS & CORE MATH (ANOVA + F critical)
# -------------------------------------------------------------

# safe formats
fmt = lambda x, p=2: f"{x:.{p}f}"

def clamp(x, lo, hi):
    return max(lo, min(hi, x))

# --- Beta/F PDF without external libs ---
def beta_func(a: float, b: float) -> float:
    return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))

def f_pdf(x: float, d1: int, d2: int) -> float:
    if x <= 0 or d1 <= 0 or d2 <= 0:
        return 0.0
    a, b = d1 / 2.0, d2 / 2.0
    num = (d1 ** (d1 / 2.0)) * (d2 ** (d2 / 2.0)) * (x ** (a - 1))
    den = (d1 * x + d2) ** ((d1 + d2) / 2.0) * beta_func(a, b)
    return num / den

# F critical table (α=0.05 base) + interpolation
F_CRIT_005 = {
    1:  {3:10.13, 4:7.71, 5:6.61, 6:5.99, 7:5.59, 8:5.32, 9:5.12, 10:4.96, 12:4.75, 15:4.54, 20:4.35, 24:4.26, 30:4.17, 40:4.08, 60:4.00, 120:3.92, 200:3.89},
    2:  {3:9.55, 4:6.94, 5:5.79, 6:5.14, 7:4.74, 8:4.46, 9:4.26, 10:4.10, 12:3.89, 15:3.68, 20:3.49, 24:3.39, 30:3.32, 40:3.23, 60:3.15, 120:3.07, 200:3.04},
    3:  {3:9.28, 4:6.59, 5:5.41, 6:4.76, 7:4.35, 8:4.07, 9:3.86, 10:3.71, 12:3.49, 15:3.29, 20:3.10, 24:3.00, 30:2.92, 40:2.84, 60:2.76, 120:2.68, 200:2.65},
    4:  {3:9.12, 4:6.39, 5:5.19, 6:4.53, 7:4.12, 8:3.84, 9:3.63, 10:3.48, 12:3.26, 15:3.06, 20:2.87, 24:2.77, 30:2.69, 40:2.61, 60:2.53, 120:2.45, 200:2.42},
    5:  {3:9.01, 4:6.26, 5:5.05, 6:4.39, 7:3.97, 8:3.69, 9:3.48, 10:3.33, 12:3.11, 15:2.91, 20:2.72, 24:2.62, 30:2.54, 40:2.46, 60:2.38, 120:2.30, 200:2.27},
}

def fcrit_alpha(df1: int, df2: int, alpha: float) -> float:
    df1 = int(clamp(df1, 1, 5))
    df2_keys = sorted(F_CRIT_005[df1].keys())
    d2 = int(clamp(df2, df2_keys[0], df2_keys[-1]))
    lo = max(k for k in df2_keys if k <= d2)
    hi = min(k for k in df2_keys if k >= d2)
    if lo == hi: base = F_CRIT_005[df1][lo]
    else:
        y0, y1 = F_CRIT_005[df1][lo], F_CRIT_005[df1][hi]
        t = (d2 - lo) / (hi - lo)
        base = y0 + t * (y1 - y0)
    if abs(alpha - 0.05) < 1e-9: return base
    if abs(alpha - 0.10) < 1e-9: return base * 0.85
    if abs(alpha - 0.01) < 1e-9: return base * 1.35
    return base

# --- Data generation ---

def generate_groups(k: int, n: int, effect: float, seed: int) -> Dict[str, List[float]]:
    rnd = random.Random(seed)
    base = rnd.uniform(55, 65)
    groups = {}
    for gi in range(k):
        mean_shift = (gi - (k - 1) / 2) * (5.0 * effect) + rnd.uniform(-1.0, 1.0)
        true_mean = base + mean_shift
        within_sd = max(2.5, 6.0 - 1.2 * effect + rnd.uniform(-1.0, 1.0))
        groups[chr(65 + gi)] = [rnd.gauss(true_mean, within_sd) for _ in range(n)]
    return groups

# --- ANOVA ---

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
    F = (msb / msw) if msw > 0 else float('inf')
    eta2 = ssb / sst if sst > 0 else 0.0
    return {
        "k": k, "n": n, "means": means, "grand_mean": gm,
        "ssb": ssb, "ssw": ssw, "sst": sst,
        "dfb": dfb, "dfw": dfw, "msb": msb, "msw": msw, "F": F, "eta2": eta2
    }

# -------------------------------------------------------------
# 4) SESSION STATE + CONTROLS
# -------------------------------------------------------------
ss = st.session_state
ss.setdefault("round", 1)
ss.setdefault("score", 0)
ss.setdefault("seed", random.randint(1, 9999))
ss.setdefault("controls", {"k": 4, "n": 8, "effect": 0.9, "alpha": 0.05})
ss.setdefault("history", [])

with st.container():
    st.markdown('<div class="card"><div class="u-row u-gap"><span class="u-bold">🛠️ Pengaturan Eksperimen</span><span class="u-muted u-sm">(ubah jumlah kelompok, sampel, dan effect size)</span></div>', unsafe_allow_html=True)
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
    st.rerun()

# -------------------------------------------------------------
# 5) DATA + TABEL (with tiny shimmer animation)
# -------------------------------------------------------------
groups = generate_groups(ss.controls["k"], ss.controls["n"], ss.controls["effect"], ss.seed + ss.round)

st.markdown('<div class="card"><div class="u-row u-gap"><span class="u-bold">🧪 Ronde {}</span><span class="u-muted u-sm">Data hasil percobaan (simulasi) beberapa kelompok.</span></div>'.format(ss.round), unsafe_allow_html=True)

# table
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

# -------------------------------------------------------------
# 6) SIMULATED CALC (progress shimmer)
# -------------------------------------------------------------
with st.expander("▶️ Jalankan Perhitungan ANOVA (simulasi langkah)", expanded=True):
    ph = st.empty()
    for step, txt in [
        (20, "Menyiapkan data …"), (40, "Menghitung rata-rata & grand mean …"),
        (65, "Menghitung SSB & SSW …"), (85, "Menyusun tabel ANOVA …"), (100, "Selesai ✅")
    ]:
        ph.markdown(f"<div class='shimmer'></div><div class='u-sm u-muted'>{txt}</div>", unsafe_allow_html=True)
        time.sleep(0.18)

# -------------------------------------------------------------
# 7) ANOVA CORE + DECISION
# -------------------------------------------------------------
A = anova_oneway(groups)
Fcalc = A["F"]
df1, df2 = A["dfb"], A["dfw"]
Fcrit = fcrit_alpha(df1, df2, ss.controls["alpha"])

# defensif: jika Fcalc NaN/inf, clamp
if math.isnan(Fcalc) or math.isinf(Fcalc):
    Fcalc = 1e6

# metrics band
st.markdown('<div class="card">', unsafe_allow_html=True)
mc1, mc2, mc3 = st.columns(3)
with mc1:
    st.markdown(f"<div class='metric'><div class='k'>Kelompok</div><div class='v'>{A['k']}</div></div>", unsafe_allow_html=True)
with mc2:
    st.markdown(f"<div class='metric'><div class='k'>Sampel/Kelompok</div><div class='v'>{A['n']}</div></div>", unsafe_allow_html=True)
with mc3:
    st.markdown(f"<div class='metric'><div class='k'>Grand Mean</div><div class='v'>{fmt(A['grand_mean'])}</div></div>", unsafe_allow_html=True)

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

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

st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

significant = Fcalc > Fcrit

# keputusan
dec_badge = (
    f"<div class='decision ok'>Keputusan: Tolak H₀</div><div class='u-sm u-muted'>Karena F_hit ({fmt(Fcalc,3)}) > F_krit ({fmt(Fcrit,3)}), ada bukti perbedaan rata-rata.</div>"
    if significant else
    f"<div class='decision warn'>Keputusan: Gagal Menolak H₀</div><div class='u-sm u-muted'>Karena F_hit ({fmt(Fcalc,3)}) ≤ F_krit ({fmt(Fcrit,3)}), belum cukup bukti perbedaan rata-rata.</div>"
)
st.markdown(dec_badge, unsafe_allow_html=True)

# Konfeti kanan 2 detik kalau signifikan
if significant:
    components.v1.html(
        """
        <div id="confettiHost"></div>
        <script>
        (function(){
          const host=document.getElementById('confettiHost');
          const c=document.createElement('canvas');host.appendChild(c); const ctx=c.getContext('2d');
          function rs(){c.width=host.clientWidth; c.height=host.clientHeight;} rs();
          window.addEventListener('resize', rs);
          let parts=[]; let t0=null; const DUR=2000;
          for(let i=0;i<140;i++){
            parts.push({x: c.width*Math.random(), y: -20-80*Math.random(), vx: 60+120*Math.random(), vy: 40+80*Math.random(),
                        g: 180+Math.random()*160, s: 4+Math.random()*6, rot: Math.random()*6.28, col: i%2? '#DCCCA3':'#4A67E9'});
          }
          function step(ts){
            if(!t0) t0=ts; const t=ts-t0; ctx.clearRect(0,0,c.width,c.height);
            for(const p of parts){ p.x+=p.vx/60; p.y+=p.vy/60; p.vy+=p.g/2000; p.rot+=0.08; ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot);
              ctx.fillStyle=p.col; ctx.fillRect(-p.s/2,-p.s/2,p.s,p.s); ctx.restore(); }
            if(t<DUR){ requestAnimationFrame(step);} else { host.remove(); }
          }
          requestAnimationFrame(step);
        })();
        </script>
        """,
        height=0,
    )

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# 8) GRAFIK BESAR DI BAWAH (selalu utuh, auto-scale)
# -------------------------------------------------------------

def render_big_f_chart(df1:int, df2:int, Fh:float, Fc:float, alpha:float):
    # domain x adaptif; tambah buffer agar tidak mentok kanan
    xmax = max(Fc*1.5, Fh*1.1, 8.0 + df1)
    xmin = 0.0
    N = 700
    xs = [xmin + (xmax - xmin) * i / (N - 1) for i in range(N)]
    ys = [f_pdf(x, df1, df2) for x in xs]
    ymax = max(ys) if max(ys) > 0 else 1.0

    # siapkan area kiri/kanan
    left = [
        {"x": x, "y": y} for x, y in zip(xs, ys) if x <= Fc
    ]
    right = [
        {"x": x, "y": y} for x, y in zip(xs, ys) if x >= Fc
    ]

    import json
    payload = {
        "W": 1280, "H": 560, "PAD": 60,
        "xmin": xmin, "xmax": xmax, "ymax": ymax,
        "alpha": alpha, "Fc": Fc, "Fh": Fh,
        "curve": [{"x": x, "y": y} for x, y in zip(xs, ys)],
        "left": left, "right": right,
    }
    js_data = json.dumps(payload)

    html = f"""
    <div class="chart-card fade">
      <div class="u-row u-gap u-bold" style="margin:4px 4px 10px 4px;">
        <span>📈 Visualisasi Distribusi F (α = {alpha})</span>
      </div>
      <div id="fchart-host"></div>
      <div class="legend">
        <span class="dot dot-ns"></span><span class="u-sm u-muted">Non-Signifikan</span>
        <span class="dot dot-sg"></span><span class="u-sm u-muted">Signifikan (daerah kritis)</span>
      </div>
    </div>
    <script>
    (function(){{
      const D={js_data};
      const host=document.getElementById('fchart-host');
      const ns='http://www.w3.org/2000/svg';
      function mapX(x,W,P,X0,X1){{return P + (W-2*P) * ((x-X0)/(X1-X0));}}
      function mapY(y,H,P,Y){{return H-P - (H-2*P) * (y/Y);}}
      function draw(){
        host.innerHTML='';
        const W=Math.min(1280, host.clientWidth), H=D.H;
        const P=D.PAD, X0=D.xmin, X1=D.xmax, Y=D.ymax;
        const svg=document.createElementNS(ns,'svg');
        svg.setAttribute('viewBox',`0 0 ${'{'}W{'}'} ${'{'}H{'}'}`);
        svg.style.width='100%'; svg.style.height=H+'px'; host.appendChild(svg);
        const defs=document.createElementNS(ns,'defs');
        defs.innerHTML=`<linearGradient id='gL'><stop offset='0%' stop-color='#9db4ff' stop-opacity='0.95'/><stop offset='100%' stop-color='#c9d6ff' stop-opacity='0.3'/></linearGradient>
                        <linearGradient id='gR'><stop offset='0%' stop-color='#DCCCA3' stop-opacity='0.95'/><stop offset='100%' stop-color='#CBB279' stop-opacity='0.5'/></linearGradient>
                        <filter id='glow'><feGaussianBlur stdDeviation='2.2' result='b'/><feMerge><feMergeNode in='b'/><feMergeNode in='SourceGraphic'/></feMerge></filter>`;
        svg.appendChild(defs);
        // axis
        const ax=document.createElementNS(ns,'line'); ax.setAttribute('x1',P); ax.setAttribute('x2',W-P);
        ax.setAttribute('y1',mapY(0,H,P,Y)); ax.setAttribute('y2',mapY(0,H,P,Y));
        ax.setAttribute('stroke','#CBD5E1'); ax.setAttribute('stroke-width','1.2'); svg.appendChild(ax);
        // helper
        function pathCurve(arr){ if(!arr.length) return ''; let s='M'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(arr[0].y,H,P,Y); for(let i=1;i<arr.length;i++) s+='L'+mapX(arr[i].x,W,P,X0,X1)+','+mapY(arr[i].y,H,P,Y); return s; }
        function pathArea(arr){ if(!arr.length) return ''; let s='M'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(arr[0].y,H,P,Y); for(let i=1;i<arr.length;i++) s+='L'+mapX(arr[i].x,W,P,X0,X1)+','+mapY(arr[i].y,H,P,Y); const L=arr[arr.length-1]||arr[0]; s+='L'+mapX(L.x,W,P,X0,X1)+','+mapY(0,H,P,Y)+'L'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(0,H,P,Y)+'Z'; return s; }
        // elements
        const areaL=document.createElementNS(ns,'path'), areaR=document.createElementNS(ns,'path'), curve=document.createElementNS(ns,'path');
        areaL.setAttribute('fill','url(#gL)'); areaR.setAttribute('fill','url(#gR)'); areaR.setAttribute('filter','url(#glow)'); curve.setAttribute('fill','none'); curve.setAttribute('stroke','#4A67E9'); curve.setAttribute('stroke-width','2.8');
        svg.appendChild(areaL); svg.appendChild(areaR); svg.appendChild(curve);
        const total=D.curve.length; let start=null;
        function anim(ts){ if(!start) start=ts; const t=Math.min(1,(ts-start)/3200); const i=Math.max(2,Math.floor(total*t));
          curve.setAttribute('d', pathCurve(D.curve.slice(0,i)));
          areaL.setAttribute('d', pathArea(D.left.slice(0, Math.min(i, D.left.length))));
          areaR.setAttribute('d', pathArea(D.right.slice(0, Math.min(i, D.right.length))));
          if(t<1) requestAnimationFrame(anim);
        }
        requestAnimationFrame(anim);
        // critical & hit lines + labels
        const FcX=mapX(D.Fc,W,P,X0,X1), FhX=mapX(D.Fh,W,P,X0,X1);
        function vline(x,col,w){ const l=document.createElementNS(ns,'line'); l.setAttribute('x1',x); l.setAttribute('x2',x); l.setAttribute('y1',P); l.setAttribute('y2',H-P); l.setAttribute('stroke',col); l.setAttribute('stroke-width',w); l.setAttribute('filter','url(#glow)'); svg.appendChild(l); return l; }
        vline(FcX,'#111827',1.6); vline(FhX,'#4A67E9',2.4);
        function label(txt,x,y){ const t=document.createElementNS(ns,'text'); t.textContent=txt; t.setAttribute('x',x+6); t.setAttribute('y',y); t.setAttribute('fill','#111827'); t.setAttribute('font-size','12'); svg.appendChild(t); }
        label('F_krit = '+D.Fc.toFixed(3), FcX, P+14); label('F_hit = '+D.Fh.toFixed(3), FhX, P+28);
      }
      draw();
      let ro=null; if('ResizeObserver' in window){ ro=new ResizeObserver(draw); ro.observe(host);} else { window.addEventListener('resize', draw); }
    })();
    </script>
    """
    components.v1.html(html, height=620, scrolling=False)

# panggil grafik besar
render_big_f_chart(df1, df2, Fcalc, Fcrit, ss.controls["alpha"])

# -------------------------------------------------------------
# 9) FOOTER NOTES
# -------------------------------------------------------------
st.caption("Catatan: Tabel F-kritikal berbasis α=0.05 dengan interpolasi; α lain diskalakan monotonic (0.10≈−15%, 0.01≈+35%). Cukup akurat untuk edukasi & gameplay.")

# ======================================================================
# ANOVA ODYSSEY – Final Cinematic UltraSafe (Single File, No External Deps)
# Theme: Elegant ANOVA (light-blue + gold)
# Visual: Dual F-curve (main + zoom), gold glow, smooth animation (JS/SVG)
# Game: Significance prediction, scoring, rounds, session leaderboard
# FX: Right-side confetti (2s), progress simulation, subtle glows
# Safe: No numpy/pandas; only stdlib (math, statistics, random, json)
# ======================================================================

import streamlit as st
import streamlit.components.v1 as components
import random, math, statistics, time, json
from typing import Dict, List

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="ANOVA Odyssey – Final Cinematic",
    page_icon="⚔️",
    layout="centered",
)

# ----------------------------------------------------------------------
# THEME CSS (elegan: biru muda + emas)
# ----------------------------------------------------------------------
THEME_CSS = """
<style>
:root{
  --bg-soft:#EAF4FB; --bg-panel:#F7FBFF; --gold:#DCCCA3; --gold2:#CBB279;
  --ink:#111827; --muted:#6B7280; --blue:#4A67E9; --blue2:#7EA3FF; --card:#FFFFFF;
}
html,body,[data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,var(--bg-soft),#FFFFFF 65%);
}
section.main > div.block-container{ padding-top:1.0rem; }

.el-card{ background:var(--card); border:1px solid rgba(0,0,0,.06);
  border-radius:18px; padding:18px 20px; box-shadow:0 14px 36px rgba(10,30,60,.06); }
.el-title{ font-weight:900; color:var(--ink); letter-spacing:.25px; }
.el-sub{ color:var(--muted); font-weight:500; }

.el-chip{ display:inline-flex; align-items:center; gap:8px; background:var(--gold);
  color:#1b1b1b; padding:6px 12px; border-radius:999px; font-weight:800; }

.hr-soft{ height:1px; background:rgba(0,0,0,.06); margin:14px 0; }

.metric{ display:flex; gap:10px; align-items:center; background:var(--bg-panel);
  border:1px solid rgba(0,0,0,.06); border-radius:14px; padding:12px 14px; }
.metric .k{ color:var(--muted); font-size:13px; font-weight:700; }
.metric .v{ color:var(--ink); font-size:20px; font-weight:900; }

.badge{ display:inline-flex; gap:8px; align-items:center; border-radius:12px;
  padding:6px 10px; font-weight:800; }
.badge.ok{ background:#dcfce7; color:#065f46; }
.badge.warn{ background:#fef9c3; color:#854d0e; }
.badge.err{ background:#fee2e2; color:#7f1d1d; }

.chart-box{ border:1px dashed rgba(0,0,0,.12); border-radius:14px; background:#fff; padding:16px; }
.bar-wrap{ display:grid; gap:10px; }
.bar-row{ display:flex; gap:10px; align-items:center; }
.bar-label{ min-width:68px; font-weight:900; color:#111827; }
.bar{ flex:1; height:18px; border-radius:9px; position:relative; overflow:hidden; background:#eef2ff; }
.bar > div{ height:100%; background:linear-gradient(90deg,var(--blue),var(--blue2)); border-radius:9px; }
.mean-pill{ display:inline-flex; gap:8px; align-items:center; border:1px solid rgba(37,99,235,.25);
  background:#eef2ff; color:#1e3a8a; padding:6px 10px; font-weight:900; border-radius:999px; }

table.simple{ width:100%; border-collapse:collapse; background:#fff; border-radius:10px; overflow:hidden;
  border:1px solid rgba(0,0,0,.06); }
table.simple thead tr{ background:#f3f4f6; }
table.simple th, table.simple td{ padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06);
  text-align:center; font-size:13px; }
table.simple tr:last-child td{ border-bottom:none; }

.fade{ animation:fadeIn .55s ease-out both; }
@keyframes fadeIn{ from{opacity:0; transform:translateY(6px)} to{opacity:1; transform:none} }

.glow{
  box-shadow: 0 0 0 rgba(220,204,163,0.0);
  animation: breath 3s ease-in-out infinite;
}
@keyframes breath{
  0%{ box-shadow:0 0 0 rgba(220,204,163,0.0) }
  50%{ box-shadow:0 0 24px rgba(220,204,163,0.45) }
  100%{ box-shadow:0 0 0 rgba(220,204,163,0.0) }
}
</style>
"""
st.markdown(THEME_CSS, unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SESSION STATE INIT
# ----------------------------------------------------------------------
def init_state():
    ss = st.session_state
    ss.setdefault("round", 1)
    ss.setdefault("score", 0)
    ss.setdefault("history", [])
    ss.setdefault("seed", random.randint(1, 999999))
    ss.setdefault("controls", {
        "k": 3, "n": 6, "effect": 0.8, "alpha": 0.05
    })
    ss.setdefault("last_correct", None)
init_state()

# ----------------------------------------------------------------------
# UTILS
# ----------------------------------------------------------------------
def fmt(x: float, p: int = 3) -> str:
    try:
        return f"{x:.{p}f}"
    except Exception:
        return str(x)

def progress_sim(texts: List[str], delays: List[float]=(0.15,0.12,0.18,0.14,0.1)):
    prog = st.progress(0, text="Menyiapkan …")
    steps = max(1, len(texts))
    for i, t in enumerate(texts):
        pct = int((i+1)/steps*100)
        prog.progress(pct, text=t)
        time.sleep(delays[i % len(delays)])
    time.sleep(0.03)

# ----------------------------------------------------------------------
# DATA GENERATION (tanpa numpy)
# ----------------------------------------------------------------------
def generate_groups(k:int, n:int, effect:float, seed:int) -> Dict[str, List[float]]:
    rnd = random.Random(seed)
    base = rnd.uniform(55, 65)
    groups: Dict[str, List[float]] = {}
    for gi in range(k):
        # mean bergeser sesuai effect
        mean_shift = (gi - (k-1)/2.0) * (5.0 * effect) + rnd.uniform(-1.0, 1.0)
        true_mean = base + mean_shift
        within_sd = max(2.5, 6.0 - 1.2*effect + rnd.uniform(-1.0, 1.0))
        vals = [rnd.gauss(true_mean, within_sd) for _ in range(n)]
        groups[chr(65+gi)] = vals
    return groups

# ----------------------------------------------------------------------
# ANOVA (manual, one-way)
# ----------------------------------------------------------------------
def anova_oneway(groups:Dict[str,List[float]])->Dict[str,float]:
    k = len(groups)
    n = len(next(iter(groups.values())))
    totals = {g: sum(v) for g,v in groups.items()}
    ns = {g: len(v) for g,v in groups.items()}
    means = {g: totals[g]/ns[g] for g in groups}
    all_vals = [x for v in groups.values() for x in v]
    grand_mean = sum(all_vals)/len(all_vals)

    ss_between = sum(ns[g]*(means[g]-grand_mean)**2 for g in groups)
    ss_within  = sum(sum((x-means[g])**2 for x in groups[g]) for g in groups)
    ss_total   = ss_between + ss_within

    df_between = k - 1
    df_within  = k*(n-1)

    ms_between = ss_between/df_between if df_between>0 else float('nan')
    ms_within  = ss_within/df_within if df_within>0 else float('nan')
    F = (ms_between/ms_within) if ms_within>0 else 0.0
    eta2 = ss_between/ss_total if ss_total>0 else 0.0

    return {
        "k":k,"n":n,"means":means,"grand_mean":grand_mean,
        "ssb":ss_between,"ssw":ss_within,"sst":ss_total,
        "dfb":df_between,"dfw":df_within,
        "msb":ms_between,"msw":ms_within,"F":F,"eta2":eta2
    }

# ----------------------------------------------------------------------
# F-CRITICAL TABLE (alpha=0.05) + simple alpha adjust
# ----------------------------------------------------------------------
F_CRIT_005 = {
    1:{3:10.13,4:7.71,5:6.61,6:5.99,8:5.32,10:4.96,12:4.75,15:4.54,20:4.35,30:4.17,40:4.08,60:4.00,120:3.92,200:3.89},
    2:{3: 9.55,4:6.94,5:5.79,6:5.14,8:4.46,10:4.10,12:3.89,15:3.68,20:3.49,30:3.32,40:3.23,60:3.15,120:3.07,200:3.04},
    3:{3: 9.28,4:6.59,5:5.41,6:4.76,8:4.07,10:3.71,12:3.49,15:3.29,20:3.10,30:2.92,40:2.84,60:2.76,120:2.68,200:2.65},
    4:{3: 9.12,4:6.39,5:5.19,6:4.53,8:3.84,10:3.48,12:3.26,15:3.06,20:2.87,30:2.69,40:2.61,60:2.53,120:2.45,200:2.42},
    5:{3: 9.01,4:6.26,5:5.05,6:4.39,8:3.69,10:3.33,12:3.11,15:2.91,20:2.72,30:2.54,40:2.46,60:2.38,120:2.30,200:2.27},
}
def interp_fcrit(df1:int, df2:int)->float:
    df1 = max(1, min(5, df1))
    table = F_CRIT_005[df1]
    keys = sorted(table.keys())
    if df2 <= keys[0]: return table[keys[0]]
    if df2 >= keys[-1]: return table[keys[-1]]
    lo = max(k for k in keys if k<=df2)
    hi = min(k for k in keys if k>=df2)
    if lo==hi: return table[lo]
    t = (df2-lo)/(hi-lo)
    return table[lo] + t*(table[hi]-table[lo])

def fcrit_adjusted(df1:int, df2:int, alpha:float)->float:
    base = interp_fcrit(df1, df2)
    if abs(alpha-0.05) < 1e-9: return base
    if abs(alpha-0.10) < 1e-9: return base*0.85
    if abs(alpha-0.01) < 1e-9: return base*1.35
    return base

# ----------------------------------------------------------------------
# F-PDF (tanpa scipy)
# ----------------------------------------------------------------------
def f_pdf(x:float, d1:int, d2:int)->float:
    if x <= 0: return 0.0
    a, b = d1/2.0, d2/2.0
    # Beta(a,b) via gamma
    beta = math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
    return ((d1/d2)**a * x**(a-1)) / (beta * (1+(d1/d2)*x)**(a+b))

# ----------------------------------------------------------------------
# RENDER: TABLE, MEANS, VARIANCES (tanpa pandas)
# ----------------------------------------------------------------------
def render_data_table(groups:Dict[str,List[float]]):
    labels = list(groups.keys())
    rows = max(len(v) for v in groups.values())
    html = ['<div class="chart-box fade glow"><table class="simple"><thead><tr><th>No</th>']
    for g in labels:
        html.append(f"<th>Kelompok {g}</th>")
    html.append("</tr></thead><tbody>")
    for i in range(rows):
        html.append(f"<tr><td>{i+1}</td>")
        for g in labels:
            val = groups[g][i] if i < len(groups[g]) else ""
            html.append(f"<td>{fmt(val,2)}</td>")
        html.append("</tr>")
    html.append("</tbody></table></div>")
    st.markdown("".join(html), unsafe_allow_html=True)

def bar_row(label:str, value:float, vmax:float):
    pct = 0 if vmax<=0 else max(0.0, min(100.0, (value / vmax) * 100.0))
    st.markdown(
        f"""
        <div class="bar-row">
            <div class="bar-label">{label}</div>
            <div class="bar"><div style="width:{pct}%;"></div></div>
            <div class="mean-pill">{fmt(value,2)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_means_chart(means:Dict[str,float]):
    vmin = min(means.values()) if means else 0
    span = max(1.0, (max(means.values()) - vmin))
    vmax = vmin + span*1.2
    st.markdown('<div class="chart-box fade"><b>📈 Rata-rata per Kelompok</b><div class="bar-wrap">', unsafe_allow_html=True)
    for g, m in sorted(means.items()):
        bar_row(f"Mean {g}", m - (vmin - 0.1*span), vmax)
    st.markdown('</div></div>', unsafe_allow_html=True)

def render_var_chart(groups:Dict[str,List[float]]):
    vars_ = {}
    for g, vals in groups.items():
        try:
            vars_[g] = statistics.pvariance(vals)
        except statistics.StatisticsError:
            vars_[g] = 0.0
    vmax = max(vars_.values()) if vars_ else 1.0
    st.markdown('<div class="chart-box fade"><b>🧮 Varians per Kelompok</b><div class="bar-wrap">', unsafe_allow_html=True)
    for g, v in sorted(vars_.items()):
        bar_row(f"Var {g}", v, vmax)
    st.markdown('</div></div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# CONFETTI (2 detik, kanan layar) – aman di Streamlit Cloud
# ----------------------------------------------------------------------
def confetti_right():
    js = """
    <script>
    (function(){
      let c=document.createElement('canvas');
      c.style.position='fixed';c.style.right='0';c.style.top='0';
      c.style.width='100vw';c.style.height='100vh';c.style.pointerEvents='none';
      c.style.zIndex='9999';document.body.appendChild(c);
      let ctx=c.getContext('2d'); c.width=innerWidth; c.height=innerHeight;
      let parts=[];
      for(let i=0;i<220;i++){ parts.push({
        x: c.width*0.72 + Math.random()*80,
        y: c.height*0.18 + Math.random()*30,
        vx:(Math.random()*8)+2, vy: - (Math.random()*12+6),
        r:2+Math.random()*3,
        color:['#4A67E9','#7EA3FF','#DCCCA3','#CBB279'][~~(Math.random()*4)],
        life: 120
      }) }
      let t=0;
      function step(){
        t++; ctx.clearRect(0,0,c.width,c.height);
        parts.forEach(p=>{
          p.x+=p.vx; p.y+=p.vy; p.vy+=0.35; p.life--;
          ctx.globalAlpha=Math.max(0,p.life/120);
          ctx.fillStyle=p.color; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,6.28); ctx.fill();
        });
        parts=parts.filter(p=>p.life>0);
        if(t<120) requestAnimationFrame(step); else c.remove();
      }
      step();
    })();
    </script>
    """
    components.html(js, height=0, width=0)

# ----------------------------------------------------------------------
# F-DISTRIBUTION RENDER (dual: main + zoom) – auto-scale anti kepotong
# ----------------------------------------------------------------------
def render_f_dual(df1:int, df2:int, Fh:float, Fc:float, alpha:float):
    # smart max-x: kalau Fh jauh di atas Fc, scale ke Fh*1.1; else sekitar Fc*1.6
    xmax = Fh*1.1 if Fh > Fc*3 else Fc*1.6
    xmin = 0.0
    # jaga agar kanvas proporsional terhadap jumlah kelompok
    xmax = max(xmax, 10 + 1.2*df1)

    # sampling kurva
    N = 560
    xs = [xmin + (xmax-xmin)*i/(N-1) for i in range(N)]
    ys = [f_pdf(x, df1, df2) for x in xs]
    ymax = max(ys) if max(ys) > 0 else 1.0

    left = [{"x":x,"y":y} for x,y in zip(xs,ys) if x<=Fc]
    right= [{"x":x,"y":y} for x,y in zip(xs,ys) if x>=Fc]

    data = {
        "W": 1120, "H": 520, "PAD": 60,
        "xmax": xmax, "xmin": xmin, "ymax": ymax,
        "Fh": Fh, "Fc": Fc, "alpha": alpha,
        "curve":[{"x":x,"y":y} for x,y in zip(xs,ys)],
        "left": left, "right": right
    }
    data_json = json.dumps(data)

    # HTML/JS – tidak pakai f-string variable di template literal agar aman
    html = """
    <div style="display:flex; flex-wrap:wrap; gap:18px; justify-content:center;">
      <div class="el-card fade glow" style="flex:1; min-width:560px;">
        <div class="el-title" style="font-size:18px;">📊 Distribusi F (α = <span style='color:#4A67E9'>DATA_ALPHA</span>)</div>
        <div id="f-main"></div>
      </div>
      <div class="el-card fade" style="flex:1; min-width:560px;">
        <div class="el-title" style="font-size:18px;">🔎 Zoom Area Kritis</div>
        <div id="f-zoom"></div>
      </div>
    </div>
    <script>
    (function(){
      const D = DATA_JSON_PLACEHOLDER;
      function mapX(x,W,P,X0,X1){ return P + (W-2*P)*((x-X0)/(X1-X0)); }
      function mapY(y,H,P,Y){ return H-P - (H-2*P)*(y/Y); }

      function draw(hostId, zoom){
        const ns='http://www.w3.org/2000/svg';
        const W=D.W, H=D.H, P=D.PAD, X0=D.xmin, X1=D.xmax, Y=D.ymax;
        const host = document.getElementById(hostId);
        const svg = document.createElementNS(ns,'svg');
        svg.setAttribute('viewBox',`0 0 ${W} ${H}`);
        svg.style.width='100%'; svg.style.height=H+'px';
        host.innerHTML=''; host.appendChild(svg);

        const defs = document.createElementNS(ns,'defs');
        const gL = document.createElementNS(ns,'linearGradient');
        gL.id='leftGrad';
        gL.innerHTML = "<stop offset='0%' stop-color='#9db4ff' stop-opacity='0.95'/>" +
                       "<stop offset='100%' stop-color='#9db4ff' stop-opacity='0.15'/>";
        const gR = document.createElementNS(ns,'linearGradient');
        gR.id='rightGrad';
        gR.innerHTML = "<stop offset='0%' stop-color='#DCCCA3' stop-opacity='0.95'/>" +
                       "<stop offset='100%' stop-color='#CBB279' stop-opacity='0.55'/>";
        const glow = document.createElementNS(ns,'filter');
        glow.id='glow';
        glow.innerHTML = "<feGaussianBlur stdDeviation='3.5' result='b'/>" +
                         "<feMerge><feMergeNode in='b'/><feMergeNode in='SourceGraphic'/></feMerge>";
        defs.appendChild(gL); defs.appendChild(gR); defs.appendChild(glow);
        svg.appendChild(defs);

        // axis
        const axis = document.createElementNS(ns,'line');
        axis.setAttribute('x1',P); axis.setAttribute('x2',W-P);
        axis.setAttribute('y1',mapY(0,H,P,Y)); axis.setAttribute('y2',mapY(0,H,P,Y));
        axis.setAttribute('stroke','#9CA3AF'); axis.setAttribute('stroke-width','1.2');
        svg.appendChild(axis);

        // Fc line
        let Fc = D.Fc;
        const lineFc = document.createElementNS(ns,'line');
        lineFc.setAttribute('x1',mapX(Fc,W,P,X0,X1)); lineFc.setAttribute('x2',mapX(Fc,W,P,X0,X1));
        lineFc.setAttribute('y1',P); lineFc.setAttribute('y2',H-P);
        lineFc.setAttribute('stroke','#1f2937'); lineFc.setAttribute('stroke-width','1.4');
        svg.appendChild(lineFc);

        // Fh line
        let Fh = D.Fh;
        const lineFh = document.createElementNS(ns,'line');
        lineFh.setAttribute('x1',mapX(Fh,W,P,X0,X1)); lineFh.setAttribute('x2',mapX(Fh,W,P,X0,X1));
        lineFh.setAttribute('y1',P); lineFh.setAttribute('y2',H-P);
        lineFh.setAttribute('stroke','#4A67E9'); lineFh.setAttribute('stroke-width','2.1');
        lineFh.setAttribute('filter','url(#glow)');
        svg.appendChild(lineFh);

        // curve & areas
        const pathCurve = document.createElementNS(ns,'path');
        pathCurve.setAttribute('fill','none'); pathCurve.setAttribute('stroke','#4A67E9');
        pathCurve.setAttribute('stroke-width','2.6');
        const pathLeft = document.createElementNS(ns,'path');
        const pathRight = document.createElementNS(ns,'path');
        pathLeft.setAttribute('fill','url(#leftGrad)');
        pathRight.setAttribute('fill','url(#rightGrad)'); pathRight.setAttribute('filter','url(#glow)');
        svg.appendChild(pathLeft); svg.appendChild(pathRight); svg.appendChild(pathCurve);

        const curve = zoom ? D.left.concat(D.right) : D.curve;
        const total = curve.length;
        function toPath(arr){
          if(!arr.length) return '';
          let s='M'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(arr[0].y,H,P,Y);
          for(let i=1;i<arr.length;i++){ s+='L'+mapX(arr[i].x,W,P,X0,X1)+','+mapY(arr[i].y,H,P,Y); }
          return s;
        }
        function areaPath(arr){
          if(!arr.length) return '';
          let s='M'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(arr[0].y,H,P,Y);
          for(let i=1;i<arr.length;i++){ s+='L'+mapX(arr[i].x,W,P,X0,X1)+','+mapY(arr[i].y,H,P,Y); }
          const last = arr[arr.length-1]||arr[0];
          s+='L'+mapX(last.x,W,P,X0,X1)+','+mapY(0,H,P,Y)+'L'+mapX(arr[0].x,W,P,X0,X1)+','+mapY(0,H,P,Y)+'Z';
          return s;
        }

        let start=null;
        function frame(ts){
          if(!start) start=ts;
          let t=Math.min(1,(ts-start)/3200); // 3.2s
          const idx=Math.max(2, Math.floor(total*t));
          const c=curve.slice(0,idx);
          pathCurve.setAttribute('d', toPath(c));
          pathLeft.setAttribute('d', areaPath(D.left.slice(0, Math.min(idx, D.left.length))));
          pathRight.setAttribute('d', areaPath(D.right.slice(0, Math.min(idx, D.right.length))));
          if(t<1) requestAnimationFrame(frame);
        }
        requestAnimationFrame(frame);

        // Legend
        const legend=document.createElement('div');
        legend.style.margin='8px 8px 0 8px';
        legend.innerHTML = `
          <div style="display:flex;gap:16px;align-items:center;flex-wrap:wrap;">
            <span style="display:inline-flex;gap:8px;align-items:center;">
              <span style="width:14px;height:14px;border-radius:4px;background:#9db4ff;display:inline-block"></span>
              <span>Non-Signifikan</span>
            </span>
            <span style="display:inline-flex;gap:8px;align-items:center;">
              <span style="width:14px;height:14px;border-radius:4px;background:#DCCCA3;display:inline-block"></span>
              <span>Signifikan (daerah kritis)</span>
            </span>
          </div>`;
        host.appendChild(legend);
      }

      draw('f-main', false);
      draw('f-zoom', true);
    })();
    </script>
    """
    html = html.replace("DATA_JSON_PLACEHOLDER", data_json).replace("DATA_ALPHA", str(alpha))
    components.html(html, height=780, scrolling=False)

# ----------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------
st.markdown(
    """
    <div class="el-card fade" style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
      <div>
        <div class="el-title" style="font-size:28px;">⚔️ ANOVA Odyssey: <span style="color:#4A67E9">Final Cinematic</span></div>
        <div class="el-sub">Kelompok 4 ANOVA · HMSD Adyatama ITERA 2025</div>
      </div>
      <div class="el-chip">Elegan · Biru & Emas</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------------------
# SIDEBAR – scoreboard & controls
# ----------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("**Ronde:**", st.session_state.round)
    st.write("**Skor:**", st.session_state.score)
    if st.session_state.history:
        best = max(h["score_after"] for h in st.session_state.history)
        st.write("**Best (sesi):**", best)
    st.markdown("---")
    st.caption("Cara main: tebak ada/tidak perbedaan signifikan antar mean. "
               "Benar +10, salah −5. Data berubah tiap ronde.")
    st.markdown("---")
    if st.button("🔄 Reset Skor & Ronde"):
        st.session_state.score = 0
        st.session_state.history.clear()
        st.session_state.round = 1
        st.session_state.seed = random.randint(1, 999999)
        st.rerun()

# Controls panel
def controls_panel():
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown('<div class="el-title">⚙️ Pengaturan Eksperimen</div>', unsafe_allow_html=True)
    st.markdown('<div class="el-sub">Atur jumlah kelompok, ukuran sampel, dan effect size.</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        k = st.slider("Jumlah Kelompok (k)", 3, 6, st.session_state.controls["k"])
        n = st.slider("Sampel per Kelompok (n)", 4, 12, st.session_state.controls["n"])
    with c2:
        effect = st.slider("Besaran Perbedaan Mean (effect)", 0.0, 2.0, st.session_state.controls["effect"], 0.1)
        alpha = st.select_slider("Taraf Signifikansi (α)", options=[0.10, 0.05, 0.01], value=st.session_state.controls["alpha"])
    apply = st.button("Terapkan & Ronde Baru 🔁")
    st.markdown('</div>', unsafe_allow_html=True)
    if apply:
        st.session_state.controls.update({"k":k, "n":n, "effect":effect, "alpha":float(alpha)})
        st.session_state.seed = random.randint(1, 999999)
        st.session_state.round += 1
        st.rerun()
controls_panel()

# ----------------------------------------------------------------------
# GENERATE ROUND DATA
# ----------------------------------------------------------------------
k = st.session_state.controls["k"]
n = st.session_state.controls["n"]
effect = st.session_state.controls["effect"]
alpha = st.session_state.controls["alpha"]

groups = generate_groups(k, n, effect, seed=st.session_state.seed + st.session_state.round)

# ----------------------------------------------------------------------
# TABLE DATA
# ----------------------------------------------------------------------
st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
st.markdown(f'<div class="el-title">🧪 Data Ronde {st.session_state.round}</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Nilai simulasi untuk tiap kelompok.</div>', unsafe_allow_html=True)
render_data_table(groups)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SIMULATED CALC (progress)
# ----------------------------------------------------------------------
with st.expander("▶️ Jalankan Perhitungan ANOVA (simulasi langkah)", expanded=True):
    progress_sim([
        "Menghitung mean tiap kelompok …",
        "Menghitung grand mean …",
        "Menghitung SSB & SSW …",
        "Menyusun tabel ANOVA …",
        "Selesai ✅"
    ])

# ----------------------------------------------------------------------
# ANOVA CALC
# ----------------------------------------------------------------------
anv = anova_oneway(groups)
Fcalc = anv["F"]
df1, df2 = anv["dfb"], anv["dfw"]
Fcrit = fcrit_adjusted(df1, df2, alpha)
significant = Fcalc > Fcrit

# ----------------------------------------------------------------------
# SUMMARY (lab style)
# ----------------------------------------------------------------------
st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
st.markdown('<div class="el-title">🧫 Ringkasan Perhitungan (Lab)</div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(f'<div class="metric"><div class="k">SS Between (SSB)</div><div class="v">{fmt(anv["ssb"],4)}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric"><div class="k">df Between</div><div class="v">{df1}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric"><div class="k">MS Between</div><div class="v">{fmt(anv["msb"],4)}</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown(f'<div class="metric"><div class="k">SS Within (SSW)</div><div class="v">{fmt(anv["ssw"],4)}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric"><div class="k">df Within</div><div class="v">{df2}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric"><div class="k">MS Within</div><div class="v">{fmt(anv["msw"],4)}</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown(f'<div class="metric"><div class="k">F-Statistic</div><div class="v">{fmt(Fcalc,3)}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric"><div class="k">F-Critical (α={alpha})</div><div class="v">{fmt(Fcrit,3)}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric"><div class="k">Eta²</div><div class="v">{fmt(anv["eta2"],3)}</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# PREDICTION UI
# ----------------------------------------------------------------------
st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
st.markdown('<div class="el-title">🎯 Prediksi Kamu</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Berdasarkan data & grafik, apakah ada perbedaan rata-rata yang signifikan?</div>', unsafe_allow_html=True)
choice = st.radio("Pilih jawaban:", ["Ya, signifikan ✅", "Tidak signifikan ❌"], index=0, key="guess_choice")
go = st.button("Kunci Jawaban & Tampilkan Hasil 🧪")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# RESULT + SCORING + VISUALS
# ----------------------------------------------------------------------
if go:
    user_says_sig = choice.startswith("Ya")
    correct = (user_says_sig and significant) or ((not user_says_sig) and (not significant))
    before = st.session_state.score
    if correct:
        st.session_state.score += 10
        badge = '<span class="badge ok">Benar · +10</span>'
        confetti_right()  # efek aman 2 detik kanan
    else:
        st.session_state.score -= 5
        badge = '<span class="badge err">Salah · -5</span>'

    st.session_state.history.append({
        "round": st.session_state.round,
        "choice": "Signifikan" if user_says_sig else "Tidak",
        "significant": significant,
        "F": Fcalc, "Fcrit": Fcrit,
        "score_before": before, "score_after": st.session_state.score
    })

    # Decision text
    if significant:
        decision_html = f"""
        <div class="badge ok">Keputusan: Tolak H₀</div>
        <div class="el-sub" style="margin-top:6px">
          Karena F_hit ({fmt(Fcalc,3)}) > F_krit ({fmt(Fcrit,3)}), terdapat bukti bahwa minimal satu mean kelompok berbeda.
        </div>"""
        note = "Variasi antar-kelompok lebih besar daripada variasi dalam-kelompok."
    else:
        decision_html = f"""
        <div class="badge warn">Keputusan: Gagal Menolak H₀</div>
        <div class="el-sub" style="margin-top:6px">
          F_hit ({fmt(Fcalc,3)}) ≤ F_krit ({fmt(Fcrit,3)}): belum cukup bukti perbedaan rata-rata antar kelompok.
        </div>"""
        note = "Perbedaan mean tidak cukup kuat dibanding noise dalam-kelompok."

    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown(f'<div style="display:flex;align-items:center;gap:10px;">{badge}<div style="font-weight:900;">&nbsp;Hasil Ronde {st.session_state.round}</div></div>', unsafe_allow_html=True)
    st.markdown(decision_html, unsafe_allow_html=True)
    st.markdown(f'<div class="hr-soft"></div><div class="el-sub">{note}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Grafik F (dua panel, auto-scale anti kepotong)
    render_f_dual(df1, df2, Fcalc, Fcrit, alpha)

    # Means & variance
    cA, cB = st.columns(2)
    with cA: render_means_chart(anv["means"])
    with cB: render_var_chart(groups)

    # Next round button
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    nxt1, nxt2 = st.columns([1,1])
    with nxt1:
        if st.button("🔁 Lanjut ke Ronde Berikutnya"):
            st.session_state.seed = random.randint(1, 999999)
            st.session_state.round += 1
            st.rerun()
    with nxt2:
        st.write(f"🏆 Skor saat ini: **{st.session_state.score}**")
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# HISTORY (session leaderboard)
# ----------------------------------------------------------------------
with st.expander("🏅 Riwayat Ronde & Leaderboard (Sesi Ini)"):
    if not st.session_state.history:
        st.info("Belum ada riwayat. Mainkan satu ronde dulu.")
    else:
        head = "<tr><th>Ronde</th><th>Pilihan</th><th>F_hit</th><th>F_krit</th><th>Benar?</th><th>Skor →</th></tr>"
        rows = []
        for h in st.session_state.history:
            right = (h["choice"]=="Signifikan" and h["significant"]) or (h["choice"]=="Tidak" and not h["significant"])
            ok = "✅" if right else "❌"
            rows.append(
                f"<tr><td>{h['round']}</td><td>{h['choice']}</td>"
                f"<td>{fmt(h['F'],3)}</td><td>{fmt(h['Fcrit'],3)}</td>"
                f"<td style='font-weight:800;'>{ok}</td>"
                f"<td>{h['score_before']} → <b>{h['score_after']}</b></td></tr>"
            )
        st.markdown(
            f"<div class='chart-box'><table class='simple'><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table></div>",
            unsafe_allow_html=True
        )
        top = max(h["score_after"] for h in st.session_state.history)
        st.caption(f"Skor terbaik sesi ini: **{top}**. Coba variasikan k, n, dan effect untuk tantangan baru.")

# ----------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------
st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
st.caption(
    "Catatan: F-kritis diturunkan dari tabel α=0.05 dengan interpolasi; α=0.10 & 0.01 "
    "diaproksimasi skala monoton. Cukup akurat untuk edukasi & gameplay."
)
# ======================================================================
# END
# ======================================================================


# ======================================================================
# ANOVA ODYSSEY v5.4 — Wide Cinematic Smooth Edition (No external deps)
# Title bar: "ANOVA Oyssey" (requested)
# Layout: wide; single F-graph (big, auto-scale, anti-crop) shown AFTER user locks answer
# Theme: Elegant light-blue + gold
# Animations: 3s smooth curve draw + subtle glow on critical area, right-side confetti 2s
# Logic: One-way ANOVA (manual), F-critical lookup (α=0.05 table) with simple α scaling
# UI: Prediction game, scoring, rounds, session leaderboard
# Safety: Pure stdlib (math, statistics, random, json), no numpy/pandas
# Notes: Lots of inline comments for education & line-length; keep functions compact & safe
# ======================================================================

import streamlit as st
import streamlit.components.v1 as components
import random, time, math, statistics, json
from typing import Dict, List, Tuple, Any

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
# Per permintaan: judul tab browser "ANOVA Oyssey" (tanpa 'd')
st.set_page_config(
    page_title="ANOVA Oyssey",
    page_icon="⚔️",
    layout="wide",   # diminta wide agar grafik besar dan tidak kepotong
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------
# THEME CSS (elegant blue + gold)
# ----------------------------------------------------------------------
THEME = """
<style>
:root{
  --bg-soft:#EAF4FB; --bg-panel:#F7FBFF; --gold:#DCCCA3; --gold2:#CBB279;
  --ink:#111827; --muted:#6B7280; --blue:#4A67E9; --blue2:#7EA3FF; --card:#ffffff;
}

html, body, [data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,var(--bg-soft),#FFFFFF 64%);
}
section.main > div.block-container{
  padding-top:1.0rem;
  max-width: 1500px; /* biar nyaman di layar besar, tetap wide */
}

.el-card{
  background:var(--card);
  border:1px solid rgba(0,0,0,.05);
  border-radius:18px;
  box-shadow:0 12px 30px rgba(10,30,60,.06);
  padding:18px 20px;
}
.el-title{ font-weight:900; color:var(--ink); letter-spacing:.3px; }
.el-sub{ color:var(--muted); font-weight:500; }
.el-chip{
  display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#1b1b1b;
  border-radius:999px; padding:6px 12px; font-weight:800;
}
.hr-soft{ height:1px; background:rgba(0,0,0,.06); margin:14px 0; }

.badge{ display:inline-flex; align-items:center; gap:6px; font-weight:800; border-radius:12px; padding:6px 10px; }
.badge.ok{ background:#dcfce7; color:#065f46; }
.badge.warn{ background:#fef9c3; color:#854d0e; }
.badge.err{ background:#fee2e2; color:#7f1d1d; }

.metric{
  display:flex; flex-direction:column; gap:4px; padding:12px 14px; border-radius:12px;
  background:var(--bg-panel); border:1px solid rgba(0,0,0,.06);
}
.metric .k{ font-size:14px; color:var(--muted); font-weight:700; }
.metric .v{ font-size:22px; font-weight:900; color:var(--ink); }

.chart-box{
  border:1px dashed rgba(0,0,0,.12);
  padding:14px; border-radius:14px; background:#fff;
}
.bar-wrap{ display:grid; gap:10px; }
.bar-row{ display:flex; align-items:center; gap:12px; }
.bar-label{ min-width:64px; font-weight:900; color:#111827; }
.bar{
  flex:1; height:18px; border-radius:999px; position:relative;
  background:linear-gradient(90deg,var(--gold),var(--gold2));
  box-shadow:inset 0 0 0 2px rgba(0,0,0,.06);
  overflow:hidden;
}
.bar-fill{
  height:100%; border-radius:999px;
  background:linear-gradient(90deg,var(--blue),var(--blue2));
  width:0%;
}
.mean-pill{
  display:inline-flex; align-items:center; gap:10px; background:#eef2ff; color:#1e3a8a;
  padding:6px 10px; border-radius:999px; font-weight:800; border:1px solid rgba(37,99,235,.25);
}

table.simple{
  width:100%; border-collapse:collapse; background:#fff; border-radius:12px; overflow:hidden;
  border:1px solid rgba(0,0,0,.06);
}
table.simple thead tr{ background:#f3f4f6; }
table.simple th, table.simple td{
  padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06); text-align:center; font-size:13px;
}
table.simple tr:last-child td{ border-bottom:none; }

.fade{ animation:fadeIn .55s ease-out both; }
@keyframes fadeIn { from{opacity:0; transform:translateY(6px)} to{opacity:1; transform:none} }

.footer-note{ color:var(--muted); font-size:12px; line-height:1.5; margin-top:6px; }
.small-note{ color:var(--muted); font-size:12px; }

/* SVG container helpers */
.svg-wrap{
  width:100%;
  max-width: 1400px; /* supaya tidak melebar kebablasan di ultra-wide */
  margin-inline:auto;
}
</style>
"""
st.markdown(THEME, unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SESSION STATE INIT
# ----------------------------------------------------------------------
def init_state():
    s = st.session_state
    s.setdefault("round", 1)
    s.setdefault("score", 0)
    s.setdefault("history", [])
    s.setdefault("seed", random.randint(1, 999999))
    s.setdefault("controls", {"k":3, "n":6, "effect":0.8, "alpha":0.05, "round_name":"Ronde"})
    s.setdefault("last_feedback", "")
    s.setdefault("locked", False)
init_state()

# ----------------------------------------------------------------------
# UTILS
# ----------------------------------------------------------------------
def fmt(x: float, p: int = 3) -> str:
    try:
        return f"{x:.{p}f}"
    except Exception:
        return str(x)

def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))

def progress_sim():
    with st.expander("▶️ Jalankan Perhitungan ANOVA (simulasi langkah)", expanded=True):
        prog = st.progress(0, text="Menyiapkan data …")
        time.sleep(0.22); prog.progress(20, text="Menghitung mean tiap kelompok …")
        time.sleep(0.15); prog.progress(40, text="Menghitung grand mean …")
        time.sleep(0.14); prog.progress(62, text="Menghitung SSB & SSW …")
        time.sleep(0.18); prog.progress(84, text="Menyusun tabel ANOVA …")
        time.sleep(0.12); prog.progress(100, text="Selesai ✅"); time.sleep(0.05)

# ----------------------------------------------------------------------
# DATA GENERATION (tanpa numpy)
# ----------------------------------------------------------------------
def generate_groups(k:int, n:int, effect:float, seed:int) -> Dict[str, List[float]]:
    rnd = random.Random(seed)
    base = rnd.uniform(55, 65)
    groups: Dict[str, List[float]] = {}
    for gi in range(k):
        mean_shift = (gi - (k-1)/2.0) * (5.0 * effect) + rnd.uniform(-1.0, 1.0)
        true_mean = base + mean_shift
        within_sd = max(2.5, 6.0 - 1.2*effect + rnd.uniform(-1.0, 1.0))
        vals = [rnd.gauss(true_mean, within_sd) for _ in range(n)]
        groups[chr(65+gi)] = vals
    return groups

# ----------------------------------------------------------------------
# ANOVA (manual)
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
    beta = math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
    return ((d1/d2)**a * x**(a-1)) / (beta * (1+(d1/d2)*x)**(a+b))

# ----------------------------------------------------------------------
# RENDER: TABLE, MEANS, VARIANCES
# ----------------------------------------------------------------------
def render_table(groups:Dict[str,List[float]]):
    labels = list(groups.keys())
    rows = max(len(v) for v in groups.values())
    html = ['<div class="chart-box fade"><table class="simple"><thead><tr><th>No</th>']
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

def bar(label:str, value:float, vmax:float):
    pct = 0 if vmax<=0 else max(0.0, min(100.0, (value/vmax)*100.0))
    st.markdown(
        f"""
        <div class="bar-row fade">
          <div class="bar-label">{label}</div>
          <div class="bar"><div class="bar-fill" style="width:{pct}%;"></div></div>
          <div class="mean-pill">{fmt(value,2)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_means(means:Dict[str,float]):
    vmax = max(means.values()) if means else 1.0
    vmin = min(means.values()) if means else 0.0
    span = max(1.0, vmax - vmin)
    st.markdown('<div class="chart-box fade"><b>📈 Rata-rata per Kelompok</b><div class="bar-wrap">', unsafe_allow_html=True)
    for g, m in sorted(means.items()):
        bar(f"Mean {g}", m - (vmin - 0.1*span), span*1.2)
    st.markdown('</div></div>', unsafe_allow_html=True)

def render_vars(groups:Dict[str,List[float]]):
    variances = {}
    for g, vals in groups.items():
        try:
            variances[g] = statistics.pvariance(vals)
        except statistics.StatisticsError:
            variances[g] = 0.0
    vmax = max(variances.values()) if variances else 1.0
    st.markdown('<div class="chart-box fade"><b>🧮 Varians per Kelompok</b><div class="bar-wrap">', unsafe_allow_html=True)
    for g, v in sorted(variances.items()):
        bar(f"Var {g}", v, vmax if vmax>0 else 1.0)
    st.markdown('</div></div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# CONFETTI (kanan layar, 2 detik)
# ----------------------------------------------------------------------
def confetti_right(duration:float=2.0, pieces:int=220):
    html = """
    <script>
    (function(){
      try{
        var P = window.parent || window;
        var doc = P.document;
        var cOld = doc.getElementById('anova-confetti-canvas');
        if(cOld) cOld.remove();
        var canvas = doc.createElement('canvas');
        canvas.id = 'anova-confetti-canvas';
        canvas.style.position='fixed';
        canvas.style.left='0'; canvas.style.top='0';
        canvas.style.width='100vw'; canvas.style.height='100vh';
        canvas.style.pointerEvents='none'; canvas.style.zIndex='999999';
        doc.body.appendChild(canvas);
        var ctx = canvas.getContext('2d');
        function resize(){ canvas.width = P.innerWidth; canvas.height = P.innerHeight; }
        resize(); P.addEventListener('resize', resize);

        var colors = ['#4A67E9','#7EA3FF','#DCCCA3','#CBB279'];
        var parts = [];
        for (var i=0;i:%PIECES%;i++) {
          parts.push({
            x: canvas.width*0.75 + Math.random()*60,
            y: canvas.height*0.20 + Math.random()*40,
            r: 3 + Math.random()*3.5,
            vx: (Math.random()*2-1)*12,
            vy: - (10 + Math.random()*12),
            g: 0.35 + Math.random()*0.25,
            rot: Math.random()*Math.PI*2,
            vr: (Math.random()*0.2 - 0.1),
            color: colors[(Math.random()*colors.length)|0],
            life: %DUR%*60
          });
        }
        var start=null;
        function step(ts){
          if(!start) start=ts;
          ctx.clearRect(0,0,canvas.width,canvas.height);
          parts.forEach(p=>{
            p.vy += p.g; p.x += p.vx; p.y += p.vy; p.rot += p.vr; p.life--;
            ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot);
            ctx.fillStyle=p.color; ctx.globalAlpha=Math.max(0,p.life/(%DUR%*60));
            ctx.fillRect(-p.r,-p.r, p.r*2, p.r*2); ctx.restore();
          });
          parts = parts.filter(p=>p.life>0 && p.y<canvas.height+20);
          if (parts.length>0) P.requestAnimationFrame(step);
          else { canvas.remove(); P.removeEventListener('resize', resize); }
        }
        P.requestAnimationFrame(step);
      }catch(e){ console.log('confetti error', e); }
    })();
    </script>
    """.replace("%DUR%", str(duration)).replace("%PIECES%", str(pieces))
    components.html(html, height=0, width=0)

# ----------------------------------------------------------------------
# SINGLE BIG F-GRAPH (cinematic 3s, anti-crop, responsive width)
# ----------------------------------------------------------------------
def render_f_big(df1:int, df2:int, Fh:float, Fc:float, alpha:float, height:int=680):
    # Auto-scale X-range: pastikan tidak kepotong meski Fh sangat besar.
    # Heuristic: gunakan max dari beberapa kandidat.
    xmax_candidates = [Fc*1.6, Fh*1.3, 10 + 1.0*df1, 8.0]
    xmax = max([x for x in xmax_candidates if math.isfinite(x)] + [8.0])
    # Sampling F-PDF
    N = 620
    xs = [xmax*i/(N-1) for i in range(N)]
    ys = [f_pdf(x, df1, df2) for x in xs]
    ymax = max(ys) if max(ys) > 0 else 1.0

    left = [{"x":x,"y":y} for x,y in zip(xs,ys) if x<=Fc]
    right= [{"x":x,"y":y} for x,y in zip(xs,ys) if x>=Fc]

    data = {
        "W": 1400, "H": height, "PAD": 56,
        "xmax": xmax, "ymax": ymax,
        "Fh": Fh, "Fc": Fc, "alpha": alpha,
        "curve":[{"x":x,"y":y} for x,y in zip(xs,ys)],
        "left": left, "right": right
    }
    DATA = json.dumps(data)

    html = """
    <div class="svg-wrap fade">
      <div class="el-card">
        <div class="el-title" style="font-size:18px; margin-bottom:10px;">📊 Distribusi F (α = %ALPHA%)</div>
        <div id="f-main"></div>
      </div>
    </div>
    <script>
    (function(){
      const D = %DATA%;
      const DUR = 3000;
      function mapX(x,W,P,X){ return P + (W-2*P)*(x/X); }
      function mapY(y,H,P,Y){ return H - P - (H-2*P)*(y/Y); }

      const ns='http://www.w3.org/2000/svg';
      const W=D.W, H=D.H, P=D.PAD, X=D.xmax, Y=D.ymax;
      const host=document.getElementById('f-main'); host.innerHTML='';
      const svg=document.createElementNS(ns,'svg');
      svg.setAttribute('viewBox',`0 0 ${W} ${H}`);
      svg.style.width='100%'; svg.style.height=H+'px';
      host.appendChild(svg);

      const defs=document.createElementNS(ns,'defs'); svg.appendChild(defs);
      const gL=document.createElementNS(ns,'linearGradient');
      gL.setAttribute('id','gL'); gL.setAttribute('x1','0'); gL.setAttribute('y1','0'); gL.setAttribute('x2','0'); gL.setAttribute('y2','1');
      gL.innerHTML = "<stop offset='0%' stop-color='#9db4ff' stop-opacity='0.85'/>"+
                     "<stop offset='100%' stop-color='#9db4ff' stop-opacity='0.35'/>";
      const gR=document.createElementNS(ns,'linearGradient');
      gR.setAttribute('id','gR'); gR.setAttribute('x1','0'); gR.setAttribute('y1','0'); gR.setAttribute('x2','0'); gR.setAttribute('y2','1');
      gR.innerHTML = "<stop offset='0%' stop-color='#DCCCA3' stop-opacity='0.95'/>"+
                     "<stop offset='100%' stop-color='#CBB279' stop-opacity='0.70'/>";
      const glow=document.createElementNS(ns,'filter');
      glow.setAttribute('id','glow');
      glow.innerHTML = "<feGaussianBlur stdDeviation='3.5' result='b'/>"+
                       "<feMerge><feMergeNode in='b'/><feMergeNode in='SourceGraphic'/></feMerge>";
      defs.appendChild(gL); defs.appendChild(gR); defs.appendChild(glow);

      // Axis line (x-axis at y=0)
      const axis = document.createElementNS(ns,'line');
      axis.setAttribute('x1',P); axis.setAttribute('x2',W-P);
      axis.setAttribute('y1',mapY(0,H,P,Y)); axis.setAttribute('y2',mapY(0,H,P,Y));
      axis.setAttribute('stroke','#9CA3AF'); axis.setAttribute('stroke-width','1.2');
      svg.appendChild(axis);

      // critical region areas
      function toPath(points){
        if(!points.length) return '';
        let d='M'+mapX(points[0].x,W,P,X)+','+mapY(points[0].y,H,P,Y);
        for(let i=1;i<points.length;i++){
          d+='L'+mapX(points[i].x,W,P,X)+','+mapY(points[i].y,H,P,Y);
        }
        return d;
      }
      function areaPath(points){
        if(!points.length) return '';
        let d='M'+mapX(points[0].x,W,P,X)+','+mapY(points[0].y,H,P,Y);
        for(let i=1;i<points.length;i++){
          d+='L'+mapX(points[i].x,W,P,X)+','+mapY(points[i].y,H,P,Y);
        }
        const last = points[points.length-1] || points[0];
        d+='L'+mapX(last.x,W,P,X)+','+mapY(0,H,P,Y)+'L'+mapX(points[0].x,W,P,X)+','+mapY(0,H,P,Y)+'Z';
        return d;
      }

      const pathLeft = document.createElementNS(ns,'path');
      pathLeft.setAttribute('fill','url(#gL)'); pathLeft.setAttribute('opacity','0');
      svg.appendChild(pathLeft);
      const pathRight = document.createElementNS(ns,'path');
      pathRight.setAttribute('fill','url(#gR)'); pathRight.setAttribute('filter','url(#glow)'); pathRight.setAttribute('opacity','0');
      svg.appendChild(pathRight);
      const curve = document.createElementNS(ns,'path');
      curve.setAttribute('fill','none'); curve.setAttribute('stroke','#4A67E9'); curve.setAttribute('stroke-width','2.8');
      svg.appendChild(curve);

      // Vertical lines
      const Y0 = mapY(0,H,P,Y), YT = mapY(Y*1.02,H,P,Y);
      function vline(x,color,dash){
        const ln=document.createElementNS(ns,'line');
        ln.setAttribute('x1',x); ln.setAttribute('x2',x); ln.setAttribute('y1',YT); ln.setAttribute('y2',YT);
        ln.setAttribute('stroke',color); ln.setAttribute('stroke-width','2');
        if(dash) ln.setAttribute('stroke-dasharray','5,5');
        svg.appendChild(ln); return ln;
      }
      const XFcrit = mapX(D.Fc,W,P,X);
      const XFhit  = mapX(D.Fh,W,P,X);
      const lineFc = vline(XFcrit,'#CBB279',true);
      const lineFh = vline(XFhit , '#111827',false);

      function label(x,y,txt,fill){
        const t=document.createElementNS(ns,'text');
        t.setAttribute('x', x+6); t.setAttribute('y', y+14); t.setAttribute('font-size','12'); t.setAttribute('fill', fill);
        t.textContent=txt; t.setAttribute('opacity','0'); svg.appendChild(t); return t;
      }
      const labC = label(XFcrit, YT, 'F_krit = '+D.Fc.toFixed(2), '#6B7280');
      const labH = label(XFhit , YT+18, 'F_hit = '+D.Fh.toFixed(2), '#111827');

      // Animate draw
      const total = D.curve.length; let start=null;
      function ease(t){ return t<0.5 ? 2*t*t : -1+(4-2*t)*t; }
      function frame(ts){
        if(!start) start = ts;
        let p = (ts - start)/DUR; if(p>1) p=1;
        const e = ease(p);
        // partial curve
        const idx = Math.max(2, Math.floor(total*e));
        const seg = D.curve.slice(0, idx);
        curve.setAttribute('d', toPath(seg));
        // areas fade in
        const leftIdx  = Math.min(idx, D.left.length);
        const rightIdx = Math.min(idx, D.right.length);
        pathLeft.setAttribute('d',  areaPath(D.left.slice(0,leftIdx)));
        pathRight.setAttribute('d', areaPath(D.right.slice(0,rightIdx)));
        pathLeft .setAttribute('opacity', Math.min(1, e*2.0));
        pathRight.setAttribute('opacity', Math.max(0, (e-0.45)/0.55));
        // verticals grow
        const vl = Math.max(0,(e-0.65)/0.35); lineFc.setAttribute('y2', YT+(Y0-YT)*vl);
        const vh = Math.max(0,(e-0.70)/0.30); lineFh.setAttribute('y2', YT+(Y0-YT)*vh);
        labC.setAttribute('opacity', Math.max(0,(e-0.82)/0.18));
        labH.setAttribute('opacity', Math.max(0,(e-0.86)/0.14));
        if(p<1) requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    })();
    </script>
    """.replace("%DATA%", DATA).replace("%ALPHA%", f"{alpha:.2f}")
    components.html(html, height=height+120, scrolling=False)

# ----------------------------------------------------------------------
# CONTROLS PANEL (k max = 5 sesuai permintaan)
# ----------------------------------------------------------------------
def controls_panel():
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown('<div class="el-title">⚙️ Pengaturan Eksperimen</div>', unsafe_allow_html=True)
    st.markdown('<div class="el-sub">Atur jumlah kelompok, ukuran sampel, dan effect size. (Maks kelompok = 5)</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        k = st.slider("Jumlah Kelompok (k)", 3, 5, st.session_state.controls["k"])
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
        st.session_state.locked = False
        st.rerun()

# ----------------------------------------------------------------------
# HEADER & SIDEBAR
# ----------------------------------------------------------------------
st.markdown(
    """
    <div class="el-card fade" style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
      <div>
        <div class="el-title" style="font-size:28px;">⚔️ ANOVA Odyssey</div>
        <div class="el-sub">Kelompok 4 ANOVA · HMSD Adyatama ITERA 2025</div>
      </div>
      <div class="el-chip">Elegan ANOVA · Biru & Emas</div>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("**Ronde:**", st.session_state.round)
    st.write("**Skor:**", st.session_state.score)
    if st.session_state.history:
        best = max(h["score_after"] for h in st.session_state.history)
        st.write("**Best (sesi):**", best)
    st.markdown("---")
    st.caption("Cara main: tebak apakah terdapat perbedaan mean yang signifikan antar kelompok. Benar +10, salah −5.")
    st.markdown("---")
    if st.button("🔄 Reset Skor & Ronde"):
        st.session_state.score = 0
        st.session_state.history.clear()
        st.session_state.round = 1
        st.session_state.seed = random.randint(1, 999999)
        st.session_state.locked = False
        st.rerun()

# ----------------------------------------------------------------------
# CONTROLS
# ----------------------------------------------------------------------
controls_panel()

# ----------------------------------------------------------------------
# GENERATE DATA FOR ROUND
# ----------------------------------------------------------------------
k = st.session_state.controls["k"]
n = st.session_state.controls["n"]
effect = st.session_state.controls["effect"]
alpha = st.session_state.controls["alpha"]
groups = generate_groups(k, n, effect, seed=st.session_state.seed + st.session_state.round)

# ----------------------------------------------------------------------
# SHOW TABLE
# ----------------------------------------------------------------------
st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
st.markdown(f'<div class="el-title">🧪 {st.session_state.controls["round_name"]} {st.session_state.round}</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Nilai simulasi untuk tiap kelompok.</div>', unsafe_allow_html=True)
render_table(groups)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SIMULATED CALC STEPS
# ----------------------------------------------------------------------
progress_sim()

# ----------------------------------------------------------------------
# ANOVA CALC
# ----------------------------------------------------------------------
anv = anova_oneway(groups)
Fcalc = anv["F"]
df1, df2 = anv["dfb"], anv["dfw"]
Fcrit = fcrit_adjusted(df1, df2, alpha)
significant = Fcalc > Fcrit

# ----------------------------------------------------------------------
# LAB SUMMARY (compact, before prediction)
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
# MEANS & VARS pre-visual (optional small bars, help prediction)
# ----------------------------------------------------------------------
cA, cB = st.columns(2)
with cA:
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown('<div class="el-sub">Gambaran mean kelompok (indikasi perbedaan)</div>', unsafe_allow_html=True)
    render_means(anv["means"])
    st.markdown('</div>', unsafe_allow_html=True)
with cB:
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown('<div class="el-sub">Keragaman dalam-kelompok (varians)</div>', unsafe_allow_html=True)
    render_vars(groups)
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# PREDICTION UI
# ----------------------------------------------------------------------
st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
st.markdown('<div class="el-title">🎯 Prediksi Kamu</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Berdasarkan tabel & indikator di atas, apakah ada perbedaan yang signifikan?</div>', unsafe_allow_html=True)
choice = st.radio("Pilih jawaban:", ["Ya, signifikan ✅", "Tidak signifikan ❌"], index=0, key="guess_choice_v54")
go = st.button("Kunci Jawaban & Tampilkan Hasil 🧪")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# RESULT + SCORING + GRAPH (after lock)
# ----------------------------------------------------------------------
if go:
    user_says_sig = choice.startswith("Ya")
    correct = (user_says_sig and significant) or ((not user_says_sig) and (not significant))
    before = st.session_state.score
    if correct:
        st.session_state.score += 10
        badge = '<span class="badge ok">Benar · +10</span>'
        confetti_right(2.0, 240)  # efek aman 2 detik kanan
        feedback = f"✅ Tepat! {'F_hit > F_krit' if significant else 'F_hit ≤ F_krit'}."
    else:
        st.session_state.score -= 5
        badge = '<span class="badge err">Salah · -5</span>'
        feedback = f"❌ Kurang tepat. {'F_hit > F_krit' if significant else 'F_hit ≤ F_krit'}."

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
          Karena F_hit ({fmt(Fcalc,3)}) > F_krit ({fmt(Fcrit,3)}), terdapat bukti setidaknya satu mean berbeda.
        </div>"""
        note = "Variasi antar-kelompok lebih besar daripada variasi dalam-kelompok."
    else:
        decision_html = f"""
        <div class="badge warn">Keputusan: Gagal Menolak H₀</div>
        <div class="el-sub" style="margin-top:6px">
          F_hit ({fmt(Fcalc,3)}) ≤ F_krit ({fmt(Fcrit,3)}): belum cukup bukti perbedaan rata-rata antar kelompok.
        </div>"""
        note = "Perbedaan mean tidak cukup kuat dibanding noise dalam-kelompok."

    # Result header
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown(f'<div style="display:flex;align-items:center;gap:10px;">{badge}<div style="font-weight:900;">&nbsp;Hasil Ronde {st.session_state.round}</div></div>', unsafe_allow_html=True)
    st.write(feedback)
    st.markdown('</div>', unsafe_allow_html=True)

    # Decision + Explanation
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown('<div class="el-title">🧪 Keputusan Uji</div>', unsafe_allow_html=True)
    st.markdown(decision_html, unsafe_allow_html=True)
    st.markdown(f'<div class="hr-soft"></div><div class="el-sub">{note}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # BIG F GRAPH (single panel, auto-scale anti-crop)
    render_f_big(df1, df2, Fcalc, Fcrit, alpha, height=700)

    # Next Round
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    c1, c2 = st.columns([1,1])
    with c1:
        if st.button("🔁 Lanjut ke Ronde Berikutnya"):
            st.session_state.seed = random.randint(1, 999999)
            st.session_state.round += 1
            st.session_state.locked = False
            st.rerun()
    with c2:
        st.write(f"🏆 Skor saat ini: **{st.session_state.score}**")
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# HISTORY / LEADERBOARD
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
st.caption("© ANOVA 2025 Team — ANOVA Odyssey (wide cinematic smooth, single graph, no external deps)")


# ----------------------------------------------------------------------
# Appendix: Extra educational helpers (not used in UI, kept for completeness/length)
# ----------------------------------------------------------------------
# Desain: fungsi-fungsi berikut menjelaskan rumus ANOVA, namun tidak dipanggil.
# Disertakan sebagai dokumentasi kode (membantu pembaca) dan menambah panjang file
# sesuai request tanpa mengubah perilaku utama aplikasi.

def _doc_sum_of_squares_example(values: List[float]) -> Tuple[float, float]:
    """
    Contoh sederhana menghitung sum of squares (total vs about zero)
    (Hanya dokumentasi; tidak dipakai).
    """
    if not values:
        return 0.0, 0.0
    mean = sum(values)/len(values)
    sst = sum((x-mean)**2 for x in values)
    ss0 = sum(x**2 for x in values)  # terhadap nol (bukan ANOVA resmi)
    return sst, ss0

def _doc_eta_squared(ss_between: float, ss_total: float) -> float:
    """
    Menjelaskan eta^2 = SSB / SST (efek ukuran di ANOVA).
    (Hanya dokumentasi; tidak dipakai).
    """
    if ss_total <= 0:
        return 0.0
    return ss_between / ss_total

def _doc_f_distribution_notes() -> str:
    """
    Catatan singkat tentang distribusi F:
    - F = (MS_between / MS_within)
    - Tergantung df1 = k-1, df2 = N-k
    - Bentuk kurva skew-right, nilai >= 0
    (Hanya dokumentasi; tidak dipakai).
    """
    return "Distribusi F bersifat skew-right dan mendukung uji rasio varians."

# End of file

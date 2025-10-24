# =========================
# 🎬 ANOVA ODYSSEY v4.2 – Smooth Cinematic Edition (No external deps)
# Theme : Elegan ANOVA (Light-Blue + Gold)
# FX    : Confetti victory (2s, kanan) + Dual F-Graph Cinematic (3s SVG+JS)
# Logic : One-way ANOVA (manual), Fcritical table (α=0.05) + scale 0.10/0.01
# Visual: Tabel data, bar means & variances, dual animated F-graph (utama + zoom)
# Game  : Prediksi signifikan/tidak, skor, ronde, riwayat
# Deps  : HANYA streamlit
# =========================

import streamlit as st
import streamlit.components.v1 as components
import random, time, math, statistics
from typing import Dict, List

# -------------------------
# PAGE CONFIG & THEME
# -------------------------
st.set_page_config(page_title="ANOVA Odyssey v4.2 – Smooth Cinematic", page_icon="⚔️", layout="centered")

THEME = """
<style>
:root{
  --bg-soft:#EAF4FB; --bg-panel:#F7FBFF; --gold:#DCCCA3; --gold2:#CBB279;
  --ink:#111827; --muted:#6B7280; --blue:#4A67E9; --blue2:#7EA3FF; --card:#ffffff;
}
html, body, [data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,var(--bg-soft),#FFFFFF 60%);
}
section.main > div.block-container{ padding-top:1.0rem; }

.el-card{ background:var(--card); border:1px solid rgba(0,0,0,.05); border-radius:18px;
  box-shadow:0 12px 30px rgba(10,30,60,.06); padding:18px 20px; }
.el-title{ font-weight:900; color:var(--ink); letter-spacing:.3px; }
.el-sub{ color:var(--muted); font-weight:500; }
.el-chip{ display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#1b1b1b;
  border-radius:999px; padding:6px 12px; font-weight:800; }
.hr-soft{ height:1px; background:rgba(0,0,0,.06); margin:14px 0; }

.badge{ display:inline-flex; align-items:center; gap:6px; font-weight:800; border-radius:12px; padding:6px 10px; }
.badge.ok{ background:#dcfce7; color:#065f46; } .badge.warn{ background:#fef9c3; color:#854d0e; } .badge.err{ background:#fee2e2; color:#7f1d1d; }

.metric{ display:flex; flex-direction:column; gap:4px; padding:12px 14px; border-radius:12px;
  background:var(--bg-panel); border:1px solid rgba(0,0,0,.06); }
.metric .k{ font-size:14px; color:var(--muted); font-weight:700; }
.metric .v{ font-size:22px; font-weight:900; color:var(--ink); }

.chart-box{ border:1px dashed rgba(0,0,0,.12); padding:14px; border-radius:14px; background:#fff; }
.bar-wrap{ display:grid; gap:10px; }
.bar-row{ display:flex; align-items:center; gap:12px; }
.bar-label{ min-width:64px; font-weight:900; color:#111827; }
.bar{ flex:1; height:18px; border-radius:999px; position:relative; background:linear-gradient(90deg,var(--gold),var(--gold2));
  box-shadow:inset 0 0 0 2px rgba(0,0,0,.06); overflow:hidden; }
.bar-fill{ height:100%; border-radius:999px; background:linear-gradient(90deg,var(--blue),var(--blue2)); width:0%; }
.mean-pill{ display:inline-flex; align-items:center; gap:10px; background:#eef2ff; color:#1e3a8a;
  padding:6px 10px; border-radius:999px; font-weight:800; border:1px solid rgba(37,99,235,.25); }

table.simple{ width:100%; border-collapse:collapse; background:#fff; border-radius:12px; overflow:hidden; border:1px solid rgba(0,0,0,.06); }
table.simple thead tr{ background:#f3f4f6; }
table.simple th, table.simple td{ padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06); text-align:center; font-size:13px; }
table.simple tr:last-child td{ border-bottom:none; }

.fade{ animation:fadeIn .55s ease-out both; }
@keyframes fadeIn { from{opacity:0; transform:translateY(6px)} to{opacity:1; transform:none} }

/* Agar overlay konfeti terlihat */
.stApp iframe{ overflow:visible !important; }
</style>
"""
st.markdown(THEME, unsafe_allow_html=True)

# -------------------------
# STATE
# -------------------------
def init_state():
    s = st.session_state
    s.setdefault("round", 1)
    s.setdefault("score", 0)
    s.setdefault("history", [])
    s.setdefault("seed", random.randint(1, 10_000))
    s.setdefault("last_feedback", "")
    s.setdefault("controls", {"k":3, "n":6, "effect":0.8, "alpha":0.05, "round_name":"Ronde"})
init_state()

# -------------------------
# F-critical table (α=0.05) + interpolation + alpha adjust
# -------------------------
F_CRIT_005 = {
    1:{3:10.13,4:7.71,5:6.61,6:5.99,7:5.59,8:5.32,9:5.12,10:4.96,12:4.75,15:4.54,20:4.35,24:4.26,30:4.17,40:4.08,60:4.00,120:3.92,200:3.89},
    2:{3:9.55,4:6.94,5:5.79,6:5.14,7:4.74,8:4.46,9:4.26,10:4.10,12:3.89,15:3.68,20:3.49,24:3.39,30:3.32,40:3.23,60:3.15,120:3.07,200:3.04},
    3:{3:9.28,4:6.59,5:5.41,6:4.76,7:4.35,8:4.07,9:3.86,10:3.71,12:3.49,15:3.29,20:3.10,24:3.00,30:2.92,40:2.84,60:2.76,120:2.68,200:2.65},
    4:{3:9.12,4:6.39,5:5.19,6:4.53,7:4.12,8:3.84,9:3.63,10:3.48,12:3.26,15:3.06,20:2.87,24:2.77,30:2.69,40:2.61,60:2.53,120:2.45,200:2.42},
    5:{3:9.01,4:6.26,5:5.05,6:4.39,7:3.97,8:3.69,9:3.48,10:3.33,12:3.11,15:2.91,20:2.72,24:2.62,30:2.54,40:2.46,60:2.38,120:2.30,200:2.27},
}
def interp_fcrit(df1:int, df2:int)->float:
    df1 = max(min(df1, max(F_CRIT_005.keys())), min(F_CRIT_005.keys()))
    row = F_CRIT_005[df1]
    keys = sorted(row.keys())
    if df2 <= keys[0]: return row[keys[0]]
    if df2 >= keys[-1]: return row[keys[-1]]
    lo = max(k for k in keys if k <= df2); hi = min(k for k in keys if k >= df2)
    if lo == hi: return row[lo]
    t = (df2 - lo) / (hi - lo)
    return row[lo] + t*(row[hi]-row[lo])

def adj_alpha(fcrit005:float, alpha:float)->float:
    if abs(alpha-0.05)<1e-9: return fcrit005
    if abs(alpha-0.10)<1e-9: return fcrit005*0.85
    if abs(alpha-0.01)<1e-9: return fcrit005*1.35
    return fcrit005

# -------------------------
# DATA & ANOVA
# -------------------------
def generate_groups(k:int, n:int, effect:float, seed:int)->Dict[str,List[float]]:
    rnd = random.Random(seed)
    base = rnd.uniform(55, 65)
    groups = {}
    for gi in range(k):
        shift = (gi - (k-1)/2) * (5.0*effect) + rnd.uniform(-1.0, 1.0)
        m = base + shift
        sd = max(2.5, 6.0 - 1.2*effect + rnd.uniform(-1.0,1.0))
        groups[chr(65+gi)] = [rnd.gauss(m, sd) for _ in range(n)]
    return groups

def anova_oneway(groups:Dict[str,List[float]])->Dict[str,float]:
    k = len(groups); n = len(next(iter(groups.values())))
    totals = {g: sum(v) for g,v in groups.items()}
    ns = {g: len(v) for g,v in groups.items()}
    means = {g: totals[g]/ns[g] for g in groups}
    all_vals = [x for v in groups.values() for x in v]
    grand = sum(all_vals)/len(all_vals)
    ssb = sum(ns[g]*(means[g]-grand)**2 for g in groups)
    ssw = sum(sum((x-means[g])**2 for x in groups[g]) for g in groups)
    sst = ssb + ssw
    dfb = k-1; dfw = k*(n-1)
    msb = ssb/dfb if dfb>0 else float("nan")
    msw = ssw/dfw if dfw>0 else float("nan")
    F = (msb/msw) if msw>0 else float("inf")
    eta2 = ssb/sst if sst>0 else 0.0
    return {"k":k,"n":n,"grand_mean":grand,"ssb":ssb,"ssw":ssw,"sst":sst,"dfb":dfb,"dfw":dfw,
            "dft":dfb+dfw,"msb":msb,"msw":msw,"F":F,"eta2":eta2,"means":means}

# -------------------------
# RENDER HELPERS
# -------------------------
def fmt(x:float, p:int=2)->str: return f"{x:.{p}f}"

def render_table(groups:Dict[str,List[float]]):
    labels = list(groups.keys()); rows = max(len(v) for v in groups.values())
    html = ['<div class="fade"><table class="simple"><thead><tr><th>No</th>'] + [f"<th>Kelompok {g}</th>" for g in labels]
    html.append("</tr></thead><tbody>")
    for i in range(rows):
        html.append(f"<tr><td>{i+1}</td>")
        for g in labels: html.append(f"<td>{fmt(groups[g][i])}</td>")
        html.append("</tr>")
    html.append("</tbody></table></div>")
    st.markdown("".join(html), unsafe_allow_html=True)

def bar(label:str, value:float, vmax:float):
    pct = 0 if vmax<=0 else max(0.0, min(100.0, (value/vmax)*100))
    st.markdown(
        f"""<div class="bar-row fade">
               <div class="bar-label">{label}</div>
               <div class="bar"><div class="bar-fill" style="width:{pct}%;"></div></div>
               <div class="mean-pill">{fmt(value)}</div>
            </div>""", unsafe_allow_html=True)

def render_means(means:Dict[str,float]):
    vmax = max(means.values()); vmin = min(means.values()); span = max(1.0, vmax-vmin)
    st.markdown('<div class="chart-box fade"><div class="bar-wrap">', unsafe_allow_html=True)
    for g,m in sorted(means.items()):
        bar(f"Mean {g}", m-(vmin-0.1*span), span*1.2)
    st.markdown('</div></div>', unsafe_allow_html=True)

def render_vars(groups:Dict[str,List[float]]):
    vars_ = {g: (statistics.pvariance(v) if len(v)>1 else 0.0) for g,v in groups.items()}
    vmax = max(vars_.values()) if vars_ else 1
    st.markdown('<div class="chart-box fade"><div class="bar-wrap">', unsafe_allow_html=True)
    for g,v in sorted(vars_.items()):
        bar(f"Var {g}", v, vmax if vmax>0 else 1.0)
    st.markdown('</div></div>', unsafe_allow_html=True)

# -------------------------
# CONFETTI (Victory Explosion 2s)
# -------------------------
def victory_confetti_js(pieces:int=200, duration:float=2.0):
    html = f"""
    <div id="__confetti_mount"></div>
    <script>
    (function(){{
      try{{
        var P = window.parent || window;
        var doc = P.document;
        var old = doc.getElementById('anova-confetti-canvas');
        if(old) old.remove();
        var canvas = doc.createElement('canvas');
        canvas.id = 'anova-confetti-canvas';
        canvas.style.position='fixed';
        canvas.style.left='0'; canvas.style.top='0';
        canvas.style.width='100vw'; canvas.style.height='100vh';
        canvas.style.pointerEvents='none';
        canvas.style.zIndex='999999';
        doc.body.appendChild(canvas);
        var ctx = canvas.getContext('2d');
        function resize(){{ canvas.width = P.innerWidth; canvas.height = P.innerHeight; }}
        resize(); P.addEventListener('resize', resize);

        var colors = ['#4A67E9','#7EA3FF','#DCCCA3','#CBB279'];
        var parts = [];
        for (var i=0;i<{pieces};i++) {{
          parts.push({{
            x: canvas.width*0.7, y: canvas.height*0.25,
            r: 4 + Math.random()*3.5,
            vx: (Math.random()*2-1)*14,
            vy: - (10 + Math.random()*12),
            g: 0.35 + Math.random()*0.25,
            rot: Math.random()*Math.PI*2,
            vr: (Math.random()*0.2 - 0.1),
            color: colors[(Math.random()*colors.length)|0],
            life: {duration}*60
          }});
        }}
        var start=null;
        function step(ts){{
          if(!start) start=ts;
          var t=(ts-start)/1000.0;
          ctx.clearRect(0,0,canvas.width,canvas.height);
          parts.forEach(p=>{{
            p.vy += p.g; p.x += p.vx; p.y += p.vy; p.rot += p.vr; p.life--;
            ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot);
            ctx.fillStyle=p.color; ctx.globalAlpha=Math.max(0,p.life/({duration}*60));
            ctx.fillRect(-p.r,-p.r, p.r*2, p.r*2); ctx.restore();
          }});
          parts = parts.filter(p=>p.life>0 && p.y<canvas.height+20);
          if (t<{duration} || parts.length>0) P.requestAnimationFrame(step);
          else {{ canvas.remove(); P.removeEventListener('resize', resize); }}
        }}
        P.requestAnimationFrame(step);
      }} catch(e){{ console.log('Confetti error:',e); }}
    }})();
    </script>
    """
    components.html(html, height=0, width=0)

# -------------------------
# ANIMATED DUAL F-GRAPH (Smooth Cinematic 3s)
# -------------------------
def f_pdf(x:float, d1:int, d2:int)->float:
    if x<=0: return 0.0
    a,b=d1/2,d2/2
    # Beta function via lgamma
    beta = math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
    return ((d1/d2)**a * (x**(a-1))) / (beta * (1+(d1/d2)*x)**(a+b))

def render_f_animated(df1:int, df2:int, Fcalc:float, Fcrit:float, alpha:float, height:int=580):
    W, H, PAD = 1000, height, 50
    xmax = max(8.0, Fcrit*1.45, Fcalc*1.30, 6 + 0.6*df1)
    N = 520
    xs = [xmax*i/(N-1) for i in range(N)]
    ys = [f_pdf(x, df1, df2) for x in xs]
    ymax = max(ys) if max(ys)>0 else 1.0

    # data dict
    data = {
        "W": W, "H": H, "PAD": PAD,
        "xmax": xmax, "ymax": ymax,
        "alpha": alpha,
        "Fcalc": Fcalc, "Fcrit": Fcrit,
        "curve": [{"x":x,"y":y} for x,y in zip(xs,ys)]
    }

    html = """
    <div style="padding:10px 0;">
      <svg id='anova_svg' width='100%' height='{H}'></svg>
      <script>
      const data = {data};
      const svg = document.getElementById('anova_svg');
      const ns = 'http://www.w3.org/2000/svg';
      const W = data.W, H = data.H, PAD=data.PAD;
      function mapX(x){{return PAD+(W-2*PAD)*(x/data.xmax);}}
      function mapY(y){{return H-PAD-(H-2*PAD)*(y/data.ymax);}}
      const path = document.createElementNS(ns,'path');
      path.setAttribute('stroke','#4A67E9');
      path.setAttribute('stroke-width','2.5');
      path.setAttribute('fill','none');
      svg.appendChild(path);
      let i=0;
      function draw(){{
        const seg=data.curve.slice(0,i);
        let d='M '+mapX(seg[0].x)+','+mapY(seg[0].y);
        for(let j=1;j<seg.length;j++)d+=' L '+mapX(seg[j].x)+','+mapY(seg[j].y);
        path.setAttribute('d',d);
        if(i<data.curve.length){{i+=5;requestAnimationFrame(draw);}}
      }}
      draw();
      </script>
    </div>
    """.format(H=height, data=data)
    components.html(html, height=height+100, scrolling=False)

    """Dual graph: main + zoom, animated with JS (3s). Fully responsive width."""
    # Precompute curve points in Python (smooth)
    W, H, PAD = 1000, height, 50
    xmax = max(8.0, Fcrit*1.45, Fcalc*1.30, 6 + 0.6*df1)
    N = 520
    xs = [xmax*i/(N-1) for i in range(N)]
    ys = [f_pdf(x, df1, df2) for x in xs]
    ymax = max(ys) if max(ys)>0 else 1.0

    # split areas for fill
    left_idx = [i for i,x in enumerate(xs) if x <= Fcrit]
    right_idx= [i for i,x in enumerate(xs) if x >= Fcrit]
    def to_path_points():
        return [{"x": x, "y": y} for x,y in zip(xs,ys)]
    def to_area(points_idx):
        return [{"x": xs[i], "y": ys[i]} for i in points_idx]

    # Prepare data for JS
    data = {
        "W": W, "H": H, "PAD": PAD,
        "xmax": xmax, "ymax": ymax,
        "alpha": alpha,
        "Fcalc": Fcalc, "Fcrit": Fcrit,
        "curve": to_path_points(),
        "leftArea": to_area(left_idx),
        "rightArea": to_area(right_idx),
    }

    # HTML + JS animator (draw path gradually, glow on critical area, slide-in vertical lines)
    html = f"""
    <div class="fade" style="display:flex;flex-wrap:wrap;gap:20px;justify-content:center;align-items:flex-start;">
      <div class="el-card" style="flex:1;min-width:520px;padding:18px 22px;max-width:none;">
        <div style="font-weight:900;color:#111827;margin-bottom:8px;">📊 Distribusi F – Visual Utama (α = {alpha:.2f})</div>
        <div id="f-main"></div>
      </div>
      <div class="el-card" style="flex:1;min-width:520px;padding:18px 22px;">
        <div style="font-weight:900;color:#111827;margin-bottom:8px;">🔍 Zoom Area Kritis</div>
        <div id="f-zoom"></div>
      </div>
    </div>

    <script>
    (function(){{
      const D = {data};
      const DUR = 3000; // 3s cinematic
      function mapX(x, W, PAD, xmax) {{ return PAD + (W-2*PAD)*(x/xmax); }}
      function mapY(y, H, PAD, ymax) {{ return H - PAD - (H-2*PAD)*(y/ymax); }}

      function makeSVG(containerId, zoom=false){{
        const W = D.W, H = D.H, PAD = D.PAD, xmax = D.xmax, ymax = D.ymax;
        const host = document.getElementById(containerId);
        host.innerHTML = "";
        const svg = document.createElementNS("http://www.w3.org/2000/svg","svg");
        svg.setAttribute("viewBox", `0 0 ${{W}} ${{H}}`);
        svg.setAttribute("width","100%"); svg.setAttribute("height", H);
        host.appendChild(svg);

        // defs
        const defs = document.createElementNS(svg.namespaceURI,"defs");
        svg.appendChild(defs);
        function addGrad(id, c1, a1, c2, a2){{
          const lg = document.createElementNS(svg.namespaceURI,"linearGradient");
          lg.setAttribute("id", id); lg.setAttribute("x1","0"); lg.setAttribute("x2","0"); lg.setAttribute("y1","0"); lg.setAttribute("y2","1");
          const s1 = document.createElementNS(svg.namespaceURI,"stop");
          s1.setAttribute("offset","0%"); s1.setAttribute("stop-color", c1); s1.setAttribute("stop-opacity", a1);
          const s2 = document.createElementNS(svg.namespaceURI,"stop");
          s2.setAttribute("offset","100%"); s2.setAttribute("stop-color", c2); s2.setAttribute("stop-opacity", a2);
          lg.appendChild(s1); lg.appendChild(s2); defs.appendChild(lg);
        }}
        addGrad("gradL", "#9db4ff", zoom?0.70:0.85, "#9db4ff", zoom?0.25:0.35);
        addGrad("gradR", "#DCCCA3", 0.95, "#CBB279", 0.75);

        // axes
        const axis = document.createElementNS(svg.namespaceURI,"line");
        axis.setAttribute("x1", PAD); axis.setAttribute("y1", mapY(0,H,PAD,ymax));
        axis.setAttribute("x2", W-PAD); axis.setAttribute("y2", mapY(0,H,PAD,ymax));
        axis.setAttribute("stroke","#9CA3AF"); axis.setAttribute("stroke-width","1");
        svg.appendChild(axis);

        // areas
        function pathFrom(points){{
          if(!points.length) return "";
          let d = `M ${{mapX(points[0].x,W,PAD,xmax)}},${{mapY(points[0].y,H,PAD,ymax)}}`;
          for(let i=1;i<points.length;i++) d += ` L ${{mapX(points[i].x,W,PAD,xmax)}},${{mapY(points[i].y,H,PAD,ymax)}}`;
          return d;
        }}
        function closedArea(points){{
          if(!points.length) return "";
          const start = `M ${{mapX(points[0].x,W,PAD,xmax)}},${{mapY(points[0].y,H,PAD,ymax)}}`;
          const lines = points.slice(1).map(p=>`L ${{mapX(p.x,W,PAD,xmax)}},${{mapY(p.y,H,PAD,ymax)}}`).join(" ");
          const base  = `L ${{mapX(points[points.length-1].x,W,PAD,xmax)}},${{mapY(0,H,PAD,ymax)}} L ${{mapX(points[0].x,W,PAD,xmax)}},${{mapY(0,H,PAD,ymax)}} Z`;
          return start + " " + lines + " " + base;
        }}

        const leftArea = document.createElementNS(svg.namespaceURI,"path");
        leftArea.setAttribute("fill", "url(#gradL)"); leftArea.setAttribute("opacity","0");
        leftArea.setAttribute("d", closedArea(D.leftArea));
        svg.appendChild(leftArea);

        const rightArea = document.createElementNS(svg.namespaceURI,"path");
        rightArea.setAttribute("fill", "url(#gradR)"); rightArea.setAttribute("opacity","0");
        rightArea.setAttribute("d", closedArea(D.rightArea));
        svg.appendChild(rightArea);

        // curve
        const curve = document.createElementNS(svg.namespaceURI,"path");
        curve.setAttribute("fill","none"); curve.setAttribute("stroke","#4A67E9"); curve.setAttribute("stroke-width","2.8");
        curve.setAttribute("stroke-linecap","round");
        svg.appendChild(curve);

        // vertical lines (hidden first)
        const XFc = mapX(D.Fcrit,W,PAD,xmax), XF = mapX(D.Fcalc,W,PAD,xmax);
        const Y0 = mapY(0,H,PAD,ymax), YT = mapY(ymax*1.02,H,PAD,ymax);

        function vline(x, color, dash){
          const ln = document.createElementNS(svg.namespaceURI,"line");
          ln.setAttribute("x1", x); ln.setAttribute("y1", YT); ln.setAttribute("x2", x); ln.setAttribute("y2", YT);
          ln.setAttribute("stroke", color); ln.setAttribute("stroke-width", "2.2");
          if(dash) ln.setAttribute("stroke-dasharray","5,5");
          svg.appendChild(ln);
          return ln;
        }
        const lineCrit = vline(XFc, "#CBB279", true);
        const lineHit  = vline(XF,  "#111827", false);

        // labels
        function label(x,y,text,fill){
          const t = document.createElementNS(svg.namespaceURI,"text");
          t.setAttribute("x", x+6); t.setAttribute("y", y+16);
          t.setAttribute("font-size","12"); t.setAttribute("fill", fill);
          t.textContent = text; svg.appendChild(t); return t;
        }
        const labCrit = label(XFc, YT, `F_krit = ${{D.Fcrit.toFixed(2)}}`, "#6B7280"); labCrit.setAttribute("opacity","0");
        const labHit  = label(XF,  YT+16, `F_hit = ${{D.Fcalc.toFixed(2)}}`, "#111827"); labHit.setAttribute("opacity","0");

        // Animate curve drawing
        const total = D.curve.length;
        let start=null;
        function ease(t){{ return t<0.5 ? 2*t*t : -1+(4-2*t)*t; }} // smooth ease-in-out

        function frame(ts){
          if(!start) start=ts;
          let p = (ts - start) / DUR;
          if(p>1) p=1;
          const eased = ease(p);

          const idx = Math.max(2, Math.floor(total * eased));
          const seg = D.curve.slice(0, idx);
          curve.setAttribute("d", pathFrom(seg));

          // fade left area first 40%
          leftArea.setAttribute("opacity", Math.min(1, eased*2.2));
          // show right area after 45%
          const rightAlpha = Math.max(0, (eased-0.45)/0.55);
          rightArea.setAttribute("opacity", rightAlpha);

          // slide-in verticals after 65%
          const vl = Math.max(0, (eased-0.65)/0.35);
          const yCrit = YT + (Y0-YT)*vl;
          lineCrit.setAttribute("y2", yCrit);
          const yHit = YT + (Y0-YT)*Math.max(0, (eased-0.70)/0.30);
          lineHit.setAttribute("y2", yHit);

          // labels fade-in near end
          labCrit.setAttribute("opacity", Math.max(0, (eased-0.82)/0.18));
          labHit.setAttribute("opacity", Math.max(0, (eased-0.86)/0.14));

          if(p<1) requestAnimationFrame(frame);
        }
        requestAnimationFrame(frame);

        // Return svg in case caller needs
        return svg;
      }}

      // Render both
      makeSVG("f-main", false);
      makeSVG("f-zoom", true);
    }})();
    </script>
    """
    components.html(html, height=height+220, scrolling=False)

# -------------------------
# CONTROLS
# -------------------------
def controls_panel():
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown('<div class="el-title">⚙️ Pengaturan Eksperimen</div>', unsafe_allow_html=True)
    st.markdown('<div class="el-sub">Ubah jumlah kelompok, sampel, dan besaran perbedaan mean (effect size).</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        k = st.slider("Jumlah Kelompok (k)", 3, 6, st.session_state.controls["k"])
        n = st.slider("Ukuran Sampel/kelompok (n)", 4, 12, st.session_state.controls["n"])
    with c2:
        effect = st.slider("Besaran Perbedaan Mean (effect)", 0.0, 2.0, st.session_state.controls["effect"], 0.1)
        alpha  = st.select_slider("Taraf Signifikansi (α)", options=[0.10,0.05,0.01], value=st.session_state.controls["alpha"])
    apply = st.button("Terapkan & Mulai Ronde Baru 🔁")
    st.markdown('</div>', unsafe_allow_html=True)
    if apply:
        st.session_state.controls.update({"k":k,"n":n,"effect":effect,"alpha":float(alpha)})
        st.session_state.seed = random.randint(1,10_000)
        new_round(False)

def new_round(reset:bool):
    if reset:
        st.session_state.score = 0
        st.session_state.history.clear()
        st.session_state.round = 1
    else:
        st.session_state.round += 1
    st.session_state.last_feedback = ""
    st.rerun()

# -------------------------
# HEADER
# -------------------------
st.markdown("""
<div class="el-card fade" style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
  <div>
    <div class="el-title" style="font-size:28px;">⚔️ ANOVA Odyssey: <span style="color:#4A67E9">Smooth Cinematic Edition</span></div>
    <div class="el-sub">Kelompok 4 ANOVA · HMSD Adyatama ITERA 2025</div>
  </div>
  <div class="el-chip">Elegan ANOVA · Biru & Emas</div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("**Level/Ronde:**", st.session_state.round)
    st.write("**Skor:**", st.session_state.score)
    if st.session_state.history:
        best = max(h["score_after"] for h in st.session_state.history); st.write("**Best (sesi):**", best)
    st.markdown("---")
    st.caption("Tebak benar apakah ada perbedaan signifikan. Skor +10 bila benar, -5 bila salah.")
    st.markdown("---")
    if st.button("🔄 Reset Game (Skor & Ronde)"):
        st.session_state.seed = random.randint(1,10_000); new_round(True)

# -------------------------
# CONTROLS
# -------------------------
controls_panel()

# -------------------------
# DATA
# -------------------------
k = st.session_state.controls["k"]; n = st.session_state.controls["n"]
effect = st.session_state.controls["effect"]; alpha = st.session_state.controls["alpha"]
groups = generate_groups(k, n, effect, st.session_state.seed + st.session_state.round)

# -------------------------
# TABLE
# -------------------------
st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
st.markdown(f'<div class="el-title">🧪 {st.session_state.controls["round_name"]} {st.session_state.round}</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Data hasil percobaan (simulasi) untuk beberapa kelompok.</div>', unsafe_allow_html=True)
render_table(groups)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# SIMULATED STEPS
# -------------------------
with st.expander("▶️ Jalankan Perhitungan ANOVA (simulasi langkah)", expanded=True):
    prog = st.progress(0, text="Menyiapkan data …")
    time.sleep(0.25); prog.progress(22, text="Menghitung rata-rata tiap kelompok …")
    time.sleep(0.16); prog.progress(44, text="Menghitung Grand Mean …")
    time.sleep(0.13); prog.progress(66, text="Menghitung SSB & SSW …")
    time.sleep(0.18); prog.progress(88, text="Menyusun tabel ANOVA …")
    time.sleep(0.12); prog.progress(100, text="Selesai ✅"); time.sleep(0.05)

# -------------------------
# ANOVA CORE
# -------------------------
anv = anova_oneway(groups)
df1, df2, Fcalc = anv["dfb"], anv["dfw"], anv["F"]
Fcrit = adj_alpha(interp_fcrit(max(1,min(5,df1)), max(3,min(200,df2))), alpha)
significant = Fcalc > Fcrit

# -------------------------
# PREDICTION
# -------------------------
st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
st.markdown('<div class="el-title">🎯 Prediksi Kamu</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Berdasarkan tabel & grafik batang, apakah mean berbeda signifikan?</div>', unsafe_allow_html=True)
choice = st.radio("Pilih jawaban:", ["Ya, signifikan ✅","Tidak signifikan ❌"], key="guess_v42")
go = st.button("Kunci Jawaban & Lihat Hasil 🧪")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# RESULT + LAB + DUAL CINEMATIC F-GRAPH
# -------------------------
def lab_panel(anv:Dict[str,float], alpha:float, decision_html:str, note:str):
    c0,c1,c2 = st.columns(3)
    with c0: st.markdown(f'<div class="metric"><div class="k">Kelompok</div><div class="v">{anv["k"]}</div></div>', unsafe_allow_html=True)
    with c1: st.markdown(f'<div class="metric"><div class="k">Sampel/Kelompok</div><div class="v">{anv["n"]}</div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="metric"><div class="k">Grand Mean</div><div class="v">{fmt(anv["grand_mean"])}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
    st.subheader("Ringkasan Perhitungan (Lab)")
    a,b,c = st.columns(3)
    with a:
        st.write("**SS Between (SSB)**:", fmt(anv["ssb"],4))
        st.write("**df Between**:", anv["dfb"])
        st.write("**MS Between**:", fmt(anv["msb"],4))
    with b:
        st.write("**SS Within (SSW)**:", fmt(anv["ssw"],4))
        st.write("**df Within**:", anv["dfw"])
        st.write("**MS Within**:", fmt(anv["msw"],4))
    with c:
        st.write("**SST**:", fmt(anv["sst"],4))
        st.write("**F-Statistic**:", fmt(anv["F"],4))
        st.write("**Eta² (effect size)**:", fmt(anv["eta2"],3))

    st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
    st.subheader(f"Keputusan Uji (α = {alpha:.2f})")
    st.markdown(decision_html, unsafe_allow_html=True)
    if note: st.caption(note)

    st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
    st.subheader("Rata-rata per Kelompok"); render_means(anv["means"])
    st.subheader("Varians per Kelompok (indikasi keragaman)"); render_vars(groups)

if go:
    correct = (choice.startswith("Ya") and significant) or (choice.startswith("Tidak") and not significant)
    before = st.session_state.score
    if correct:
        st.session_state.score += 10
        st.session_state.last_feedback = (
            f"✅ Tepat! F_hit = {fmt(Fcalc,3)} > F_krit = {fmt(Fcrit,3)}"
            if significant else f"✅ Tepat! F_hit = {fmt(Fcalc,3)} ≤ F_krit = {fmt(Fcrit,3)}"
        )
        victory_confetti_js(220, 2.0)
        badge = '<span class="badge ok">Benar · +10</span>'
    else:
        st.session_state.score -= 5
        st.session_state.last_feedback = f"❌ Kurang tepat. F_hit = {fmt(Fcalc,3)} {'>' if significant else '≤'} F_krit = {fmt(Fcrit,3)}"
        badge = '<span class="badge err">Salah · -5</span>'

    st.session_state.history.append({
        "round": st.session_state.round,
        "choice": "Signifikan" if choice.startswith("Ya") else "Tidak",
        "significant": significant, "F": Fcalc, "Fcrit": Fcrit,
        "score_before": before, "score_after": st.session_state.score
    })

    if significant:
        decision_html = f"""
        <div class="badge ok">Keputusan: Tolak H₀</div>
        <div class="el-sub">F_hit ({fmt(Fcalc,3)}) > F_krit ({fmt(Fcrit,3)}): setidaknya satu mean berbeda.</div>
        """
        note = "Variasi antar-kelompok lebih besar daripada variasi dalam-kelompok."
    else:
        decision_html = f"""
        <div class="badge warn">Keputusan: Gagal Menolak H₀</div>
        <div class="el-sub">F_hit ({fmt(Fcalc,3)}) ≤ F_krit ({fmt(Fcrit,3)}): belum cukup bukti perbedaan mean.</div>
        """
        note = "Perbedaan mean tidak cukup kuat dibanding noise dalam-kelompok."

    # Hasil ringkas
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown(f'<div style="display:flex; align-items:center; gap:10px;">{badge}<div style="font-weight:900;">&nbsp;Hasil Ronde {st.session_state.round}</div></div>', unsafe_allow_html=True)
    st.write(st.session_state.last_feedback)
    st.markdown('</div>', unsafe_allow_html=True)

    # Layout: Lab panel + Dual Animated F Graph
    left, right = st.columns([1.08, 1])
    with left:
        st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
        lab_panel(anv, alpha, decision_html, note)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        # Dual animated F-graph (utama + zoom) — smooth cinematic 3s
        render_f_animated(df1, df2, Fcalc, Fcrit, alpha, height=600)

    # Next round
    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        if st.button("🔁 Lanjut ke Ronde Berikutnya"):
            st.session_state.seed = random.randint(1,10_000); new_round(False)
    with c2:
        st.write(f"🏆 Skor Kamu Sekarang: **{st.session_state.score}**")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# HISTORY
# -------------------------
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
              f"<td style='font-weight:900;'>{ok}</td>"
              f"<td>{h['score_before']} → <b>{h['score_after']}</b></td></tr>"
            )
        st.markdown(f"<table class='simple fade'><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table>", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
st.caption("Animasi kurva F digambar bertahap (3 detik) menggunakan SVG + requestAnimationFrame; area kritis glow emas, garis F_krit dan F_hit slide-in. "
           "Konfeti overlay via canvas parent, otomatis hilang setelah 2 detik. Tabel F α=0.05 diinterpolasi; α=0.10/0.01 memakai skala pendekatan edukatif.")

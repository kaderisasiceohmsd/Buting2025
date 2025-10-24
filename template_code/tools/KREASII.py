# =========================
# ANOVA ODYSSEY v4.3 – Full Cinematic Glow (No external deps)
# =========================
import streamlit as st
import streamlit.components.v1 as components
import random, time, math, statistics, json
from typing import Dict, List

# -------------------------
# PAGE CONFIG & THEME
# -------------------------
st.set_page_config(page_title="ANOVA Odyssey", page_icon="⚔️", layout="centered")

THEME = """
<style>
:root{
  --bg-soft:#EAF4FB; --bg-panel:#F7FBFF; --gold:#DCCCA3; --gold2:#CBB279;
  --ink:#111827; --muted:#6B7280; --blue:#4A67E9; --blue2:#7EA3FF; --card:#ffffff;
}
html, body, [data-testid="stAppViewContainer"]{ background:linear-gradient(180deg,var(--bg-soft),#FFFFFF 60%); }
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
# CONFETTI (Victory Explosion 2s – kanan)
# -------------------------
def victory_confetti_js(pieces:int=220, duration:float=2.0):
    html = """
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
        canvas.style.pointerEvents='none'; canvas.style.zIndex='999999';
        doc.body.appendChild(canvas);
        var ctx = canvas.getContext('2d');
        function resize(){{ canvas.width = P.innerWidth; canvas.height = P.innerHeight; }}
        resize(); P.addEventListener('resize', resize);

        var colors = ['#4A67E9','#7EA3FF','#DCCCA3','#CBB279'];
        var parts = [];
        for (var i=0;i<{pieces};i++) {{
          parts.push({{
            x: canvas.width*0.72, y: canvas.height*0.25,
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
          ctx.clearRect(0,0,canvas.width,canvas.height);
          parts.forEach(p=>{{
            p.vy += p.g; p.x += p.vx; p.y += p.vy; p.rot += p.vr; p.life--;
            ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot);
            ctx.fillStyle=p.color; ctx.globalAlpha=Math.max(0,p.life/({duration}*60));
            ctx.fillRect(-p.r,-p.r, p.r*2, p.r*2); ctx.restore();
          }});
          parts = parts.filter(p=>p.life>0 && p.y<canvas.height+20);
          if (parts.length>0) P.requestAnimationFrame(step);
          else {{ canvas.remove(); P.removeEventListener('resize', resize); }}
        }}
        P.requestAnimationFrame(step);
      }} catch(e){{ console.log('Confetti error:',e); }}
    }})();
    </script>
    """.format(pieces=pieces, duration=duration)
    components.html(html, height=0, width=0)

# -------------------------
# F pdf
# -------------------------
def f_pdf(x:float, d1:int, d2:int)->float:
    if x<=0: return 0.0
    a,b=d1/2,d2/2
    beta = math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
    return ((d1/d2)**a * (x**(a-1))) / (beta * (1+(d1/d2)*x)**(a+b))

# -------------------------
# ANIMATED DUAL F-GRAPH (Cinematic 3s + Glow)
# SAFE BUILD: embed data via json.dumps + format, escape braces in JS with {{ }}
# -------------------------
def render_f_animated(df1:int, df2:int, Fcalc:float, Fcrit:float, alpha:float, height:int=600):
    W, H, PAD = 1000, height, 50
    xmax = max(8.0, Fcrit*1.45, Fcalc*1.30, 6 + 0.6*df1)
    N = 520
    xs = [xmax*i/(N-1) for i in range(N)]
    ys = [f_pdf(x, df1, df2) for x in xs]
    ymax = max(ys) if max(ys)>0 else 1.0

    left = [{"x":x,"y":y} for x,y in zip(xs,ys) if x<=Fcrit]
    right= [{"x":x,"y":y} for x,y in zip(xs,ys) if x>=Fcrit]
    data = {
        "W": W, "H": H, "PAD": PAD, "xmax": xmax, "ymax": ymax,
        "alpha": alpha, "Fcalc": Fcalc, "Fcrit": Fcrit,
        "curve": [{"x":x,"y":y} for x,y in zip(xs,ys)],
        "leftArea": left, "rightArea": right
    }
    DATA = json.dumps(data)  # safe embed

    html = """
    <div class="fade" style="display:flex;flex-wrap:wrap;gap:20px;justify-content:center;align-items:flex-start;">
      <div class="el-card" style="flex:1;min-width:520px;padding:18px 22px;max-width:none;">
        <div style="font-weight:900;color:#111827;margin-bottom:8px;">📊 Distribusi F – Visual Utama (α = {alpha})</div>
        <div id="f-main"></div>
      </div>
      <div class="el-card" style="flex:1;min-width:520px;padding:18px 22px;">
        <div style="font-weight:900;color:#111827;margin-bottom:8px;">🔍 Zoom Area Kritis</div>
        <div id="f-zoom"></div>
      </div>
    </div>

    <script>
    (function(){{
      const D = {DATA};
      const DUR = 3000;
      function mapX(x,W,P,X){{ return P + (W-2*P)*(x/X); }}
      function mapY(y,H,P,Y){{ return H - P - (H-2*P)*(y/Y); }}

      function makeSVG(id, zoom){{
        const W=D.W,H=D.H,P=D.PAD,X=D.xmax,Y=D.ymax;
        const host=document.getElementById(id); host.innerHTML="";
        const ns="http://www.w3.org/2000/svg";
        const svg=document.createElementNS(ns,"svg");
        svg.setAttribute("viewBox",`0 0 ${{
          W}} ${{H}}`); svg.setAttribute("width","100%"); svg.setAttribute("height",H);
        host.appendChild(svg);

        // defs: gradients + glow
        const defs=document.createElementNS(ns,"defs"); svg.appendChild(defs);
        function grad(id,c1,a1,c2,a2){{const g=document.createElementNS(ns,"linearGradient");
          g.setAttribute("id",id); g.setAttribute("x1","0"); g.setAttribute("y1","0"); g.setAttribute("x2","0"); g.setAttribute("y2","1");
          const s1=document.createElementNS(ns,"stop"); s1.setAttribute("offset","0%"); s1.setAttribute("stop-color",c1); s1.setAttribute("stop-opacity",a1);
          const s2=document.createElementNS(ns,"stop"); s2.setAttribute("offset","100%"); s2.setAttribute("stop-color",c2); s2.setAttribute("stop-opacity",a2);
          g.appendChild(s1); g.appendChild(s2); defs.appendChild(g);
        }}
        grad("gL","#9db4ff", zoom?0.70:0.85, "#9db4ff", zoom?0.25:0.35);
        grad("gR","#DCCCA3",0.95,"#CBB279",0.75);

        const filt=document.createElementNS(ns,"filter");
        filt.setAttribute("id","glow"); filt.innerHTML = `
          <feGaussianBlur stdDeviation="3.5" result="b"/> 
          <feMerge>
            <feMergeNode in="b"/> <feMergeNode in="SourceGraphic"/>
          </feMerge>`;
        defs.appendChild(filt);

        // axis
        const axis=document.createElementNS(ns,"line");
        axis.setAttribute("x1",P); axis.setAttribute("y1", mapY(0,H,P,Y));
        axis.setAttribute("x2",W-P); axis.setAttribute("y2", mapY(0,H,P,Y));
        axis.setAttribute("stroke","#9CA3AF"); axis.setAttribute("stroke-width","1");
        svg.appendChild(axis);

        // helpers
        function toPath(points){{ if(!points.length) return ""; 
          let d=`M ${{mapX(points[0].x,W,P,X)}},${{mapY(points[0].y,H,P,Y)}}`;
          for(let i=1;i<points.length;i++) d+=` L ${{mapX(points[i].x,W,P,X)}},${{mapY(points[i].y,H,P,Y)}}`;
          return d; }}
        function closeArea(points){{ if(!points.length) return "";
          const start=`M ${{mapX(points[0].x,W,P,X)}},${{mapY(points[0].y,H,P,Y)}}`;
          const lines=points.slice(1).map(p=>`L ${{mapX(p.x,W,P,X)}},${{mapY(p.y,H,P,Y)}}`).join(" ");
          const base=`L ${{mapX(points[points.length-1].x,W,P,X)}},${{mapY(0,H,P,Y)}} L ${{mapX(points[0].x,W,P,X)}},${{mapY(0,H,P,Y)}} Z`;
          return start+" "+lines+" "+base; }}

        const leftA=document.createElementNS(ns,"path");
        leftA.setAttribute("fill","url(#gL)"); leftA.setAttribute("opacity","0");
        leftA.setAttribute("d", closeArea(D.leftArea)); svg.appendChild(leftA);

        const rightA=document.createElementNS(ns,"path");
        rightA.setAttribute("fill","url(#gR)"); rightA.setAttribute("opacity","0.0");
        rightA.setAttribute("filter","url(#glow)");
        rightA.setAttribute("d", closeArea(D.rightArea)); svg.appendChild(rightA);

        // pulse animation (glow)
        const style=document.createElementNS(ns,"style");
        style.textContent = `
          @keyframes glowPulse {{ 0%{{opacity:.55}} 50%{{opacity:.95}} 100%{{opacity:.55}} }}
          .pulseGold {{ animation: glowPulse 2.6s ease-in-out infinite; }}
        `;
        svg.appendChild(style);

        // curve
        const curve=document.createElementNS(ns,"path");
        curve.setAttribute("fill","none"); curve.setAttribute("stroke","#4A67E9");
        curve.setAttribute("stroke-width","2.8"); curve.setAttribute("stroke-linecap","round");
        svg.appendChild(curve);

        // verticals
        const XFc=mapX(D.Fcrit,W,P,X), XF=mapX(D.Fcalc,W,P,X);
        const Y0=mapY(0,H,P,Y), YT=mapY(Y*1.02,H,P,Y);
        function vline(x,color,dash){{ const ln=document.createElementNS(ns,"line");
          ln.setAttribute("x1",x); ln.setAttribute("y1",YT); ln.setAttribute("x2",x); ln.setAttribute("y2",YT);
          ln.setAttribute("stroke",color); ln.setAttribute("stroke-width","2.2");
          if(dash) ln.setAttribute("stroke-dasharray","5,5");
          svg.appendChild(ln); return ln; }}
        const lineC=vline(XFc,"#CBB279",true); const lineH=vline(XF,"#111827",false);

        function label(x,y,txt,fill){{ const t=document.createElementNS(ns,"text");
          t.setAttribute("x", x+6); t.setAttribute("y", y+16);
          t.setAttribute("font-size","12"); t.setAttribute("fill", fill);
          t.textContent=txt; t.setAttribute("opacity","0"); svg.appendChild(t); return t; }}
        const labC=label(XFc,YT,`F_krit = ${{D.Fcrit.toFixed(2)}}`,"#6B7280");
        const labH=label(XF, YT+16,`F_hit = ${{D.Fcalc.toFixed(2)}}`,"#111827");

        // animate
        const total=D.curve.length; let start=null;
        function ease(t){{ return t<0.5 ? 2*t*t : -1+(4-2*t)*t; }}
        function frame(ts){{
          if(!start) start=ts; let p=(ts-start)/{dur}; if(p>1) p=1; const e=ease(p);
          const idx=Math.max(2, Math.floor(total*e)); const seg=D.curve.slice(0,idx);
          curve.setAttribute("d", toPath(seg));
          leftA.setAttribute("opacity", Math.min(1, e*2.2));
          const rA = Math.max(0, (e-0.45)/0.55);
          rightA.setAttribute("opacity", rA); if(rA>0.05) rightA.setAttribute("class","pulseGold");
          const vl=Math.max(0,(e-0.65)/0.35); lineC.setAttribute("y2", YT+(Y0-YT)*vl);
          const vh=Math.max(0,(e-0.70)/0.30); lineH.setAttribute("y2", YT+(Y0-YT)*vh);
          labC.setAttribute("opacity", Math.max(0,(e-0.82)/0.18));
          labH.setAttribute("opacity", Math.max(0,(e-0.86)/0.14));
          if(p<1) requestAnimationFrame(frame);
        }}
        requestAnimationFrame(frame);
      }}

      makeSVG("f-main", false);
      makeSVG("f-zoom", true);
    }})();
    </script>
    """.format(alpha=f"{alpha:.2f}", DATA=DATA, dur=3000)
    components.html(html, height=height+240, scrolling=False)

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
# HEADER & SIDEBAR
# -------------------------
st.markdown("""
<div class="el-card fade" style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
  <div>
    <div class="el-title" style="font-size:28px;">⚔️ ANOVA Odyssey: <span style="color:#4A67E9">Full Cinematic Glow</span></div>
    <div class="el-sub">Kelompok 4 ANOVA · HMSD Adyatama ITERA 2025</div>
  </div>
  <div class="el-chip">Elegan ANOVA · Biru & Emas</div>
</div>
""", unsafe_allow_html=True)

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
choice = st.radio("Pilih jawaban:", ["Ya, signifikan ✅","Tidak signifikan ❌"], key="guess_v43")
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

    st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
    st.markdown(f'<div style="display:flex; align-items:center; gap:10px;">{badge}<div style="font-weight:900;">&nbsp;Hasil Ronde {st.session_state.round}</div></div>', unsafe_allow_html=True)
    st.write(st.session_state.last_feedback)
    st.markdown('</div>', unsafe_allow_html=True)

    left, right = st.columns([1.05, 1])
    with left:
        st.markdown('<div class="el-card fade">', unsafe_allow_html=True)
        lab_panel(anv, alpha, decision_html, note)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        render_f_animated(df1, df2, Fcalc, Fcrit, alpha, height=620)

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
st.caption("Build aman (no SyntaxError): data JS ditanam pakai json.dumps + .format(); kurva F dianimasikan 3 detik, area kritis glow emas berdenyut, dan garis F_krit/F_hit slide-in. Konfeti overlay 2 detik di sisi kanan.")

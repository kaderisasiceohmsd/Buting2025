# ======================================================================
# ANOVA Oyssey – v5.5 (Wide, Final Stable, No External Deps)
# - One-way ANOVA (manual)
# - F-crit lookup (α=0.05) + alpha adjust (0.10 / 0.05 / 0.01)
# - Responsive dual F-curve (main + zoom), no clipping (auto height)
# - Victory confetti (2s, right), smooth SVG animations
# - Gameplay: prediction + scoring + session leaderboard
# - Max groups = 5 (as requested)
# - Footer: "© ANOVA 2025 Team"
# ======================================================================

import streamlit as st
import streamlit.components.v1 as components
import random, time, math, statistics, json
from typing import Dict, List

# -------------------------
# PAGE CONFIG (wide)
# -------------------------
st.set_page_config(page_title="ANOVA Oyssey", page_icon="⚔️", layout="wide")

# -------------------------
# THEME (soft blue + gold, minimal)
# -------------------------
THEME = """
<style>
:root{
  --bg-soft:#EAF4FB; --bg-panel:#F7FBFF; --card:#FFFFFF;
  --ink:#111827; --muted:#6B7280; --blue:#4A67E9; --blue2:#7EA3FF;
  --gold:#DCCCA3; --gold2:#CBB279;
}
html, body, [data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,var(--bg-soft),#FFFFFF 60%);
}
section.main > div.block-container{ padding-top: 0.8rem; }

.el-card{ background:var(--card); border:1px solid rgba(0,0,0,.06); border-radius:18px;
  box-shadow:0 12px 36px rgba(10,30,60,.06); padding:18px 20px; }
.el-title{ font-weight:900; color:var(--ink); letter-spacing:.2px; }
.el-sub{ color:var(--muted); font-weight:500; }

.el-chip{ display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#1b1b1b;
  border-radius:999px; padding:6px 12px; font-weight:800; }

.hr-soft{ height:1px; background:rgba(0,0,0,.06); margin:14px 0; }

.metric{ display:flex; flex-direction:column; gap:4px; padding:12px 14px; border-radius:12px;
  background:var(--bg-panel); border:1px solid rgba(0,0,0,.06); }
.metric .k{ font-size:13px; color:var(--muted); font-weight:700; }
.metric .v{ font-size:20px; font-weight:900; color:var(--ink); }

.badge{ display:inline-flex; align-items:center; gap:8px; font-weight:800;
  border-radius:12px; padding:6px 10px; }
.badge.ok{ background:#dcfce7; color:#065f46; }
.badge.warn{ background:#fef9c3; color:#854d0e; }
.badge.err{ background:#fee2e2; color:#7f1d1d; }

.table-box{ border:1px dashed rgba(0,0,0,.12); padding:12px; border-radius:14px; background:#fff; }
table.simple{ width:100%; border-collapse:collapse; background:#fff; border-radius:12px; overflow:hidden;
  border:1px solid rgba(0,0,0,.06); }
table.simple thead tr{ background:#f3f4f6; }
table.simple th, table.simple td{ padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06);
  text-align:center; font-size:13px; }
table.simple tr:last-child td{ border-bottom:none; }

.bar-wrap{ display:grid; gap:10px; }
.bar-row{ display:flex; align-items:center; gap:10px; }
.bar-label{ min-width:64px; font-weight:900; color:#111827; }
.bar{ flex:1; height:18px; border-radius:999px; background:linear-gradient(90deg,var(--gold),var(--gold2));
  box-shadow:inset 0 0 0 2px rgba(0,0,0,.06); overflow:hidden; }
.bar>div{ height:100%; background:linear-gradient(90deg,var(--blue),var(--blue2)); border-radius:999px; }

.mean-pill{ display:inline-flex; gap:8px; align-items:center; border:1px solid rgba(37,99,235,.25);
  background:#eef2ff; color:#1e3a8a; padding:6px 10px; border-radius:999px; font-weight:900; }

.fade{ animation:fadeIn .55s ease-out both; }
@keyframes fadeIn{ from{opacity:0; transform:translateY(6px)} to{opacity:1; transform:none} }
</style>
"""
st.markdown(THEME, unsafe_allow_html=True)

# -------------------------
# SESSION STATE
# -------------------------
def init_state():
    s = st.session_state
    s.setdefault("round", 1)
    s.setdefault("score", 0)
    s.setdefault("history", [])
    s.setdefault("seed", random.randint(1, 999_999))
    s.setdefault("controls", {"k":3, "n":6, "effect":0.8, "alpha":0.05})
    s.setdefault("last_feedback", "")
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
    df1 = max(min(df1, 5), 1)
    row = F_CRIT_005[df1]
    keys = sorted(row.keys())
    if df2 <= keys[0]: return row[keys[0]]
    if df2 >= keys[-1]: return row[keys[-1]]
    lo = max(k for k in keys if k<=df2); hi = min(k for k in keys if k>=df2)
    if lo==hi: return row[lo]
    t = (df2-lo)/(hi-lo)
    return row[lo] + t*(row[hi]-row[lo])

def adjust_alpha(base:float, alpha:float)->float:
    if abs(alpha-0.05)<1e-9: return base
    if abs(alpha-0.10)<1e-9: return base*0.85
    if abs(alpha-0.01)<1e-9: return base*1.35
    return base

# -------------------------
# DATA + ANOVA
# -------------------------
def generate_groups(k:int, n:int, effect:float, seed:int)->Dict[str,List[float]]:
    rnd = random.Random(seed)
    base = rnd.uniform(55, 65)
    groups = {}
    for gi in range(k):
        shift = (gi - (k-1)/2.0) * (5.0*effect) + rnd.uniform(-1.0, 1.0)
        m = base + shift
        sd = max(2.5, 6.0 - 1.2*effect + rnd.uniform(-1.0, 1.0))
        groups[chr(65+gi)] = [rnd.gauss(m, sd) for _ in range(n)]
    return groups

def anova_oneway(groups:Dict[str,List[float]])->Dict[str,float]:
    k = len(groups); n = len(next(iter(groups.values())))
    totals = {g: sum(v) for g,v in groups.items()}; ns = {g: len(v) for g,v in groups.items()}
    means = {g: totals[g]/ns[g] for g in groups}
    all_vals = [x for v in groups.values() for x in v]
    grand = sum(all_vals)/len(all_vals)

    ssb = sum(ns[g]*(means[g]-grand)**2 for g in groups)
    ssw = sum(sum((x-means[g])**2 for x in groups[g]) for g in groups)
    sst = ssb + ssw

    dfb = k-1; dfw = k*(n-1)
    msb = ssb/dfb if dfb>0 else float("nan")
    msw = ssw/dfw if dfw>0 else float("nan")
    F = (msb/msw) if msw>0 else 0.0
    eta2 = ssb/sst if sst>0 else 0.0

    return {"k":k,"n":n,"means":means,"grand":grand,
            "ssb":ssb,"ssw":ssw,"sst":sst,"dfb":dfb,"dfw":dfw,"msb":msb,"msw":msw,"F":F,"eta2":eta2}

# -------------------------
# HELPERS
# -------------------------
def fmt(x:float, p:int=3)->str:
    try: return f"{x:.{p}f}"
    except: return str(x)

def progress_sim():
    prog = st.progress(0, text="Menyiapkan …")
    seq = [
        ("Menghitung mean tiap kelompok …", 22, .16),
        ("Menghitung grand mean …",       44, .12),
        ("Menghitung SSB & SSW …",        68, .18),
        ("Menyusun tabel ANOVA …",        90, .14),
        ("Selesai ✅",                   100, .06),
    ]
    for txt, pct, d in seq:
        prog.progress(pct, text=txt); time.sleep(d)

# -------------------------
# TABLE & BAR CHARTS (HTML/CSS)
# -------------------------
def table_html(groups:Dict[str,List[float]]):
    labels = list(groups.keys())
    rows = max(len(v) for v in groups.values())
    html = ['<div class="table-box fade"><table class="simple"><thead><tr><th>No</th>']
    for g in labels: html.append(f"<th>Kelompok {g}</th>")
    html.append("</tr></thead><tbody>")
    for i in range(rows):
        html.append(f"<tr><td>{i+1}</td>")
        for g in labels: html.append(f"<td>{fmt(groups[g][i],2)}</td>")
        html.append("</tr>")
    html.append("</tbody></table></div>")
    st.markdown("".join(html), unsafe_allow_html=True)

def bar_row(label:str, value:float, vmax:float):
    pct = 0 if vmax<=0 else max(0.0, min(100.0, (value/vmax)*100.0))
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

def means_chart(means:Dict[str,float]):
    if not means: return
    vmin = min(means.values()); vmax = max(means.values()); span = max(1.0, vmax-vmin)
    scale_max = vmin + span*1.2
    st.markdown('<div class="table-box fade"><b>📈 Rata-rata per Kelompok</b><div class="bar-wrap">', unsafe_allow_html=True)
    for g,m in sorted(means.items()):
        bar_row(f"Mean {g}", m-(vmin-0.1*span), scale_max)
    st.markdown('</div></div>', unsafe_allow_html=True)

def vars_chart(groups:Dict[str,List[float]]):
    vars_ = {g:(statistics.pvariance(v) if len(v)>1 else 0.0) for g,v in groups.items()}
    vmax = max(vars_.values()) if vars_ else 1.0
    st.markdown('<div class="table-box fade"><b>🧮 Varians per Kelompok</b><div class="bar-wrap">', unsafe_allow_html=True)
    for g,v in sorted(vars_.items()):
        bar_row(f"Var {g}", v, vmax if vmax>0 else 1.0)
    st.markdown('</div></div>', unsafe_allow_html=True)

# -------------------------
# CONFETTI (2s, right; robust in Streamlit Cloud)
# -------------------------
def confetti_right(duration_s:float=2.0, pieces:int=220):
    html = """
    <script>
    (function(){
      try{
        var P = window.parent || window, doc = P.document;
        var prior = doc.getElementById('anova-confetti'); if(prior) prior.remove();
        var c = doc.createElement('canvas'); c.id='anova-confetti';
        c.style.position='fixed'; c.style.left='0'; c.style.top='0';
        c.style.width='100vw'; c.style.height='100vh';
        c.style.pointerEvents='none'; c.style.zIndex='999999';
        doc.body.appendChild(c);
        var ctx=c.getContext('2d');
        function rs(){ c.width=P.innerWidth; c.height=P.innerHeight; }
        rs(); P.addEventListener('resize', rs);

        var cols=['#4A67E9','#7EA3FF','#DCCCA3','#CBB279'];
        var parts=[], life=%LIFE%;
        for(var i=0;i<%PIECES%;i++){
          parts.push({
            x: c.width*0.72 + Math.random()*20,
            y: c.height*0.18 + Math.random()*10,
            vx: (Math.random()*2-1)*13,
            vy: -(8 + Math.random()*12),
            g: 0.35 + Math.random()*0.25,
            rot: Math.random()*Math.PI*2, vr:(Math.random()*0.2-0.1),
            r: 2 + Math.random()*3.5,
            color: cols[(Math.random()*cols.length)|0],
            life: life
          });
        }
        function step(){
          ctx.clearRect(0,0,c.width,c.height);
          parts.forEach(p=>{
            p.vy+=p.g; p.x+=p.vx; p.y+=p.vy; p.rot+=p.vr; p.life--;
            ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot);
            ctx.globalAlpha=Math.max(0,p.life/life);
            ctx.fillStyle=p.color; ctx.fillRect(-p.r,-p.r,p.r*2,p.r*2); ctx.restore();
          });
          parts = parts.filter(p=>p.life>0 && p.y < c.height+30);
          if(parts.length>0) requestAnimationFrame(step);
          else { c.remove(); P.removeEventListener('resize', rs); }
        }
        requestAnimationFrame(step);
      }catch(e){ console.log('confetti err',e); }
    })();
    </script>
    """.replace("%LIFE%", str(int(duration_s*60))).replace("%PIECES%", str(int(pieces)))
    components.html(html, height=0, width=0)

# -------------------------
# F-pdf (no scipy)
# -------------------------
def f_pdf(x:float, d1:int, d2:int)->float:
    if x <= 0: return 0.0
    a, b = d1/2.0, d2/2.0
    beta = math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
    return ((d1/d2)**a * x**(a-1)) / (beta * (1+(d1/d2)*x)**(a+b))

# -------------------------
# F DISTRIBUTION RENDER (dual; responsive, anti-clipping)
# -------------------------
def render_f_dual(df1:int, df2:int, Fcalc:float, Fcrit:float, alpha:float):
    # Smart domain: ensure full visibility even for extreme F
    base_max = max(10.0, Fcrit*1.55)
    if Fcalc > base_max: base_max = Fcalc*1.15
    xmax = max(base_max, 6 + 0.8*df1)

    # Auto-height: grow with df2 and ratio Fcalc/Fcrit (but clamp to 460..920)
    height = int(min(920, max(460, 380 + df2*3 + (max(1.0, Fcalc/(Fcrit+1e-9))-1.0)*90)))

    # Sample curve
    N = 640
    xs = [xmax*i/(N-1) for i in range(N)]
    ys = [f_pdf(x, df1, df2) for x in xs]
    ymax = max(ys) if max(ys)>0 else 1.0

    left = [{"x":x,"y":y} for x,y in zip(xs,ys) if x<=Fcrit]
    right= [{"x":x,"y":y} for x,y in zip(xs,ys) if x>=Fcrit]

    data = {
        "W": 1200, "H": height, "PAD": 56,
        "xmax": xmax, "ymax": ymax, "alpha": alpha,
        "Fcalc": Fcalc, "Fcrit": Fcrit,
        "curve": [{"x":x,"y":y} for x,y in zip(xs,ys)],
        "left": left, "right": right
    }
    DATA = json.dumps(data)

    # Use placeholders to avoid f-string/template collisions
    html = """
    <div style="display:flex;flex-wrap:wrap;gap:18px;justify-content:center;">
      <div class="el-card" style="flex:1;min-width:560px;">
        <div class="el-title" style="font-size:18px;">📊 Distribusi F (α = __ALPHA__)</div>
        <div id="f-main"></div>
      </div>
      <div class="el-card" style="flex:1;min-width:560px;">
        <div class="el-title" style="font-size:18px;">🔎 Zoom Area Kritis</div>
        <div id="f-zoom"></div>
      </div>
    </div>
    <script>
    (function(){
      const D = __DATA__;
      function mapX(x,W,P,X1){ return P + (W-2*P)*(x/X1); }
      function mapY(y,H,P,Y){ return H-P - (H-2*P)*(y/Y); }

      function draw(hostId, zoom){
        const ns='http://www.w3.org/2000/svg';
        const W=D.W, H=D.H, P=D.PAD, X=D.xmax, Y=D.ymax;
        const host=document.getElementById(hostId);
        const svg=document.createElementNS(ns,'svg');
        svg.setAttribute('viewBox',`0 0 ${W} ${H}`);
        svg.style.width='100%'; svg.style.height=H+'px';
        host.innerHTML=''; host.appendChild(svg);

        const defs=document.createElementNS(ns,'defs');
        const gL=document.createElementNS(ns,'linearGradient'); gL.id='gLeft';
        gL.innerHTML="<stop offset='0%' stop-color='#9db4ff' stop-opacity='0.85'/>"+
                     "<stop offset='100%' stop-color='#9db4ff' stop-opacity='0.25'/>";
        const gR=document.createElementNS(ns,'linearGradient'); gR.id='gRight';
        gR.innerHTML="<stop offset='0%' stop-color='#DCCCA3' stop-opacity='0.95'/>"+
                     "<stop offset='100%' stop-color='#CBB279' stop-opacity='0.65'/>";
        const glow=document.createElementNS(ns,'filter'); glow.id='glow';
        glow.innerHTML="<feGaussianBlur stdDeviation='3.5' result='b'/>"+
                       "<feMerge><feMergeNode in='b'/><feMergeNode in='SourceGraphic'/></feMerge>";
        defs.appendChild(gL); defs.appendChild(gR); defs.appendChild(glow); svg.appendChild(defs);

        // Axis
        const axis=document.createElementNS(ns,'line');
        axis.setAttribute('x1',P); axis.setAttribute('x2',W-P);
        axis.setAttribute('y1',mapY(0,H,P,Y)); axis.setAttribute('y2',mapY(0,H,P,Y));
        axis.setAttribute('stroke','#9CA3AF'); axis.setAttribute('stroke-width','1.1');
        svg.appendChild(axis);

        function toPath(arr){
          if(!arr.length) return '';
          let d='M'+mapX(arr[0].x,W,P,X)+','+mapY(arr[0].y,H,P,Y);
          for(let i=1;i<arr.length;i++){ d+='L'+mapX(arr[i].x,W,P,X)+','+mapY(arr[i].y,H,P,Y); }
          return d;
        }
        function areaPath(arr){
          if(!arr.length) return '';
          let s='M'+mapX(arr[0].x,W,P,X)+','+mapY(arr[0].y,H,P,Y);
          for(let i=1;i<arr.length;i++){ s+='L'+mapX(arr[i].x,W,P,X)+','+mapY(arr[i].y,H,P,Y); }
          const last = arr[arr.length-1] || arr[0];
          s+='L'+mapX(last.x,W,P,X)+','+mapY(0,H,P,Y)+'L'+mapX(arr[0].x,W,P,X)+','+mapY(0,H,P,Y)+'Z';
          return s;
        }

        const pathCurve=document.createElementNS(ns,'path');
        pathCurve.setAttribute('fill','none'); pathCurve.setAttribute('stroke','#4A67E9');
        pathCurve.setAttribute('stroke-width','2.6'); pathCurve.setAttribute('stroke-linecap','round');
        svg.appendChild(pathCurve);

        const left=document.createElementNS(ns,'path'); left.setAttribute('fill','url(#gLeft)'); left.setAttribute('opacity','0');
        const right=document.createElementNS(ns,'path'); right.setAttribute('fill','url(#gRight)'); right.setAttribute('opacity','0'); right.setAttribute('filter','url(#glow)');
        svg.appendChild(left); svg.appendChild(right);

        const Fc = D.Fcrit, Fh = D.Fcalc, Y0 = mapY(0,H,P,Y), YT = mapY(Y*1.04,H,P,Y);
        function vline(x,color,wd, dash){
          const ln=document.createElementNS(ns,'line');
          ln.setAttribute('x1',x); ln.setAttribute('x2',x);
          ln.setAttribute('y1',YT); ln.setAttribute('y2',YT);
          ln.setAttribute('stroke',color); ln.setAttribute('stroke-width',wd);
          if(dash) ln.setAttribute('stroke-dasharray','5,5');
          svg.appendChild(ln); return ln;
        }
        const xFc=mapX(Fc,W,P,X), xFh=mapX(Fh,W,P,X);
        const lnC=vline(xFc,'#CBB279',2.1,true), lnH=vline(xFh,'#111827',2.2,false);

        function label(x,txt,fill,dy){
          const t=document.createElementNS(ns,'text');
          t.setAttribute('x',x+6); t.setAttribute('y', YT+dy);
          t.setAttribute('font-size','12'); t.setAttribute('fill',fill);
          t.setAttribute('opacity','0'); t.textContent=txt; svg.appendChild(t); return t;
        }
        const labC=label(xFc, 'F_krit = '+D.Fcrit.toFixed(2), '#6B7280', 14);
        const labH=label(xFh, 'F_hit = '+D.Fcalc.toFixed(2), '#111827', 28);

        const curve = zoom ? D.left.concat(D.right) : D.curve;
        const total = curve.length;

        function ease(t){ return t<.5 ? 2*t*t : -1+(4-2*t)*t; }
        let start=null;
        function frame(ts){
          if(!start) start=ts;
          let p=(ts-start)/3200; if(p>1) p=1; const e=ease(p);
          const k=Math.max(2, Math.floor(total*e));
          const seg = curve.slice(0,k);
          pathCurve.setAttribute('d', toPath(seg));
          left.setAttribute('d', areaPath(D.left.slice(0, minInt(k, D.left.length))));
          right.setAttribute('d', areaPath(D.right.slice(0, minInt(k, D.right.length))));
          left.setAttribute('opacity', Math.min(1, e*1.6));
          right.setAttribute('opacity', Math.max(0, (e-0.45)/0.55));
          const r = Math.max(0,(e-0.65)/0.35);
          lnC.setAttribute('y2', YT+(Y0-YT)*r);
          lnH.setAttribute('y2', YT+(Y0-YT)*Math.max(0,(e-0.72)/0.28));
          labC.setAttribute('opacity', Math.max(0,(e-0.82)/0.18));
          labH.setAttribute('opacity', Math.max(0,(e-0.86)/0.14));
          if(p<1) requestAnimationFrame(frame);
        }
        function minInt(a,b){ return a<b?a:b; }
        requestAnimationFrame(frame);

        // Legend
        const legend=document.createElement('div');
        legend.style.margin='8px 4px 0 4px';
        legend.innerHTML = "<div style='display:flex;gap:16px;flex-wrap:wrap;align-items:center;'>\
          <span style='display:inline-flex;gap:8px;align-items:center;'><span style='width:14px;height:14px;border-radius:4px;background:#9db4ff;display:inline-block'></span>Non-Signifikan</span>\
          <span style='display:inline-flex;gap:8px;align-items:center;'><span style='width:14px;height:14px;border-radius:4px;background:#DCCCA3;display:inline-block'></span>Signifikan (daerah kritis)</span>\
        </div>";
        host.appendChild(legend);
      }

      draw('f-main', false);
      draw('f-zoom', true);
    })();
    </script>
    """.replace("__DATA__", DATA).replace("__ALPHA__", f"{alpha:.2f}")
    components.html(html, height=height+240, scrolling=False)

# -------------------------
# HEADER
# -------------------------
st.markdown(
    """
    <div class="el-card fade" style="display:flex;align-items:center;justify-content:space-between;gap:16px;">
      <div>
        <div class="el-title" style="font-size:26px;">⚔️ ANOVA Oyssey</div>
        <div class="el-sub">Kelompok 4 • HMSD Adyatama ITERA 2025</div>
      </div>
      <div class="el-chip">Biru & Emas</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------
# SIDEBAR (scoreboard & reset)
# -------------------------
with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("**Ronde:**", st.session_state.round)
    st.write("**Skor:**", st.session_state.score)
    if st.session_state.history:
        best = max(h["score_after"] for h in st.session_state.history)
        st.write("**Best (sesi):**", best)
    st.markdown("---")
    st.caption("Tebak apakah ada perbedaan rata-rata yang signifikan. Benar +10, salah −5.")
    if st.button("Reset Skor & Ronde"):
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.history.clear()
        st.session_state.seed = random.randint(1, 999_999)
        st.rerun()

# -------------------------
# CONTROLS
# -------------------------
def controls_panel():
    st.markdown('<div class="el-card">', unsafe_allow_html=True)
    st.markdown('<div class="el-title">⚙️ Pengaturan Eksperimen</div>', unsafe_allow_html=True)
    st.markdown('<div class="el-sub">Atur jumlah kelompok (maks 5), sampel/kelompok, dan effect size.</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        k = st.slider("Jumlah Kelompok (k)", 3, 5, st.session_state.controls["k"])
        n = st.slider("Sampel per Kelompok (n)", 4, 12, st.session_state.controls["n"])
    with c2:
        effect = st.slider("Effect Size (perbedaan mean)", 0.0, 2.0, st.session_state.controls["effect"], 0.1)
        alpha  = st.select_slider("Taraf Signifikansi (α)", options=[0.10,0.05,0.01], value=st.session_state.controls["alpha"])
    apply = st.button("Terapkan & Mulai Ronde Baru 🔁")
    st.markdown('</div>', unsafe_allow_html=True)
    if apply:
        st.session_state.controls.update({"k":k,"n":n,"effect":effect,"alpha":float(alpha)})
        st.session_state.seed = random.randint(1, 999_999)
        st.session_state.round += 1
        st.rerun()
controls_panel()

# -------------------------
# DATA & TABLE
# -------------------------
k = st.session_state.controls["k"]
n = st.session_state.controls["n"]
effect = st.session_state.controls["effect"]
alpha = st.session_state.controls["alpha"]

groups = generate_groups(k, n, effect, st.session_state.seed + st.session_state.round)

st.markdown('<div class="el-card">', unsafe_allow_html=True)
st.markdown(f'<div class="el-title">🧪 Data Ronde {st.session_state.round}</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Nilai simulasi untuk tiap kelompok.</div>', unsafe_allow_html=True)
table_html(groups)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# PROGRESS (simulasi langkah)
# -------------------------
with st.expander("▶️ Jalankan Perhitungan ANOVA (simulasi langkah)", expanded=True):
    progress_sim()

# -------------------------
# ANOVA CALC & SUMMARY
# -------------------------
anv = anova_oneway(groups)
df1, df2, Fcalc = anv["dfb"], anv["dfw"], anv["F"]
Fcrit = adjust_alpha(interp_fcrit(df1, df2), alpha)
significant = Fcalc > Fcrit

st.markdown('<div class="el-card">', unsafe_allow_html=True)
st.markdown('<div class="el-title">🧪 Ringkasan Perhitungan (Lab)</div>', unsafe_allow_html=True)
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
    st.markdown(f'<div class="metric"><div class="k">F-hit</div><div class="v">{fmt(Fcalc,3)}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric"><div class="k">F-krit (α={alpha:.2f})</div><div class="v">{fmt(Fcrit,3)}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric"><div class="k">Eta²</div><div class="v">{fmt(anv["eta2"],3)}</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# PREDICTION UI
# -------------------------
st.markdown('<div class="el-card">', unsafe_allow_html=True)
st.markdown('<div class="el-title">🎯 Prediksi Kamu</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Berdasarkan data & grafik batang, apakah mean berbeda signifikan?</div>', unsafe_allow_html=True)
choice = st.radio("Pilih jawaban:", ["Ya, signifikan ✅", "Tidak signifikan ❌"], key="guess_final_v55")
go = st.button("Kunci Jawaban & Tampilkan Hasil 🧪")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# RESULT + DECISION + GRAPH (always visible, full width, not clipped)
# -------------------------
if go:
    user_sig = choice.startswith("Ya")
    correct = (user_sig and significant) or ((not user_sig) and (not significant))
    before = st.session_state.score
    if correct:
        st.session_state.score += 10
        badge = '<span class="badge ok">Benar · +10</span>'
        confetti_right(2.0, 240)
    else:
        st.session_state.score -= 5
        badge = '<span class="badge err">Salah · -5</span>'

    st.session_state.history.append({
        "round": st.session_state.round,
        "choice": "Signifikan" if user_sig else "Tidak",
        "significant": significant, "F": Fcalc, "Fcrit": Fcrit,
        "score_before": before, "score_after": st.session_state.score
    })

    st.markdown('<div class="el-card">', unsafe_allow_html=True)
    st.markdown(f'<div style="display:flex;align-items:center;gap:10px;">{badge}<div style="font-weight:900;">&nbsp;Hasil Ronde {st.session_state.round}</div></div>', unsafe_allow_html=True)

    if significant:
        st.markdown(
            f'<div class="badge ok">Keputusan: Tolak H₀</div>'
            f'<div class="el-sub" style="margin-top:6px;">F_hit ({fmt(Fcalc,3)}) > F_krit ({fmt(Fcrit,3)}): minimal satu mean berbeda.</div>',
            unsafe_allow_html=True
        )
        st.caption("Variasi antar-kelompok lebih besar daripada variasi dalam-kelompok.")
    else:
        st.markdown(
            f'<div class="badge warn">Keputusan: Gagal Menolak H₀</div>'
            f'<div class="el-sub" style="margin-top:6px;">F_hit ({fmt(Fcalc,3)}) ≤ F_krit ({fmt(Fcrit,3)}): belum ada bukti perbedaan mean.</div>',
            unsafe_allow_html=True
        )
        st.caption("Perbedaan mean tidak cukup kuat dibanding noise dalam-kelompok.")
    st.markdown('</div>', unsafe_allow_html=True)

    # GRAPH – ditempatkan DI BAWAH hasil, lebar penuh, anti kepotong
    render_f_dual(df1, df2, Fcalc, Fcrit, alpha)

    # Means & Variances (tambahan visual edukasi)
    colA, colB = st.columns(2)
    with colA: means_chart(anv["means"])
    with colB: vars_chart(groups)

    # Next round
    st.markdown('<div class="el-card">', unsafe_allow_html=True)
    nx1, nx2 = st.columns([1,1])
    with nx1:
        if st.button("🔁 Lanjut ke Ronde Berikutnya"):
            st.session_state.seed = random.randint(1, 999_999)
            st.session_state.round += 1
            st.rerun()
    with nx2:
        st.write(f"🏆 Skor saat ini: **{st.session_state.score}**")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# HISTORY / LEADERBOARD
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
        st.markdown(
            f"<div class='table-box'><table class='simple'><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table></div>",
            unsafe_allow_html=True
        )
        top = max(h["score_after"] for h in st.session_state.history)
        st.caption(f"Skor terbaik sesi ini: **{top}**")

# -------------------------
# FOOTER
# -------------------------
st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
st.write("© ANOVA 2025 Team")
# ======================================================================

# =============================================================
# ANOVA ODYSSEY — CINEMATIC+ ANIMATIONS v5.3 (Sidebar ON)
# Dependensi: HANYA streamlit + HTML/JS murni (tanpa paket lain)
# Animasi: shimmer, count-up metrics, kurva F menulis, area fill,
#          bounce F_hit, tooltip interaktif, konfeti 2 detik
# Visual: Grafik F BESAR di bawah hasil (no crop)
# =============================================================

import math, random, time, json
import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------------------
# PAGE CONFIG (sidebar TETAP ADA)
# -------------------------------------------------------------
st.set_page_config(
    page_title="ANOVA Odyssey – Cinematic+",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",  # ← bukan fullscreen
)

# -------------------------------------------------------------
# CSS TEMA (tanpa menyembunyikan sidebar)
# -------------------------------------------------------------
st.markdown("""
<style>
:root{
  --bg1:#F6FAFF; --ink:#0F172A; --muted:#64748B; --bl:#4A67E9; --bl2:#7EA3FF;
  --gold:#CBB279; --soft:#F8FAFF; --card:#ffffff;
}
body, [data-testid="stAppViewContainer"]{background:radial-gradient(900px 420px at 12% -10%, var(--bg1), #fff 60%);}
.block{background:var(--card);border:1px solid rgba(0,0,0,.06);border-radius:16px;padding:16px 18px;box-shadow:0 10px 30px rgba(10,30,60,.06);}
.title{font-weight:900;color:var(--ink);font-size:28px;letter-spacing:.2px}
.badge{background:var(--gold);color:#1b1b1b;border-radius:999px;padding:6px 12px;font-weight:800}
.sub{color:var(--muted);font-weight:600}
.hr{height:1px;background:#e5e7eb;margin:8px 0 14px}
.tbl{border:1px solid #e5e7eb;border-radius:12px;overflow:hidden}
.tbl table{width:100%;border-collapse:collapse}
.tbl th,.tbl td{padding:8px 10px;border-bottom:1px solid #eef2f7;text-align:center;font-size:13px}
.tbl thead tr{background:#f3f4f6}
.tbl tr:last-child td{border-bottom:none}

/* shimmer bar */
.shimmer{position:relative;height:10px;background:#e5edff;border-radius:999px;overflow:hidden}
.shimmer:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#e5edff 0%,#bfd1ff 40%,#e5edff 80%);animation:slide 1.15s linear infinite}
@keyframes slide{0%{transform:translateX(-60%)}100%{transform:translateX(60%)}}

/* custom metric tiles (biar bisa count-up) */
.metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.metric{background:var(--soft);border:1px solid #eef2f7;border-radius:12px;padding:14px}
.metric .k{font-size:12px;color:var(--muted);font-weight:700}
.metric .v{font-size:24px;font-weight:900;color:var(--ink)}

/* decisions */
.ok{background:#dcfce7;border:1px solid #86efac;color:#065f46;border-radius:12px;padding:10px 12px;font-weight:800}
.warn{background:#fef9c3;border:1px solid #fde68a;color:#854d0e;border-radius:12px;padding:10px 12px;font-weight:800}

/* chart card */
.chart-card{padding:14px;border-radius:16px;background:var(--card);border:1px solid rgba(0,0,0,.06);box-shadow:0 10px 30px rgba(10,30,60,.06)}
.legend{display:flex;gap:16px;align-items:center;margin-top:6px}
.dot{width:14px;height:14px;border-radius:4px;display:inline-block}
.dot-ns{background:linear-gradient(180deg,#9db4ff,#c9d6ff)}
.dot-sg{background:linear-gradient(180deg,#DCCCA3,#CBB279)}
.tooltip{position:absolute;pointer-events:none;background:#111827;color:#fff;font-size:12px;padding:6px 8px;border-radius:8px;opacity:0;transform:translate(-50%,-140%);transition:opacity .12s ease}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# HELPERS (ANOVA & F-PDF)
# -------------------------------------------------------------
fmt = lambda x, p=2: f"{x:.{p}f}"
def clamp(x,a,b): return max(a,min(b,x))
def beta_func(a,b): return math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
def f_pdf(x,d1,d2):
    if x<=0: return 0.0
    a,b=d1/2,d2/2
    num=(d1**(d1/2))*(d2**(d2/2))*(x**(a-1))
    den=(d1*x+d2)**((d1+d2)/2)*beta_func(a,b)
    v=num/den
    return v if math.isfinite(v) and v>=0 else 0.0

F_CRIT_005={
 1:{3:10.13,5:6.61,10:4.96,20:4.35,40:4.08,60:4.00,120:3.92,200:3.89},
 2:{3:9.55,5:5.79,10:4.10,20:3.49,40:3.23,60:3.15,120:3.07,200:3.04},
 3:{3:9.28,5:5.41,10:3.71,20:3.10,40:2.84,60:2.76,120:2.68,200:2.65},
 4:{3:9.12,5:5.19,10:3.48,20:2.87,40:2.61,60:2.53,120:2.45,200:2.42},
 5:{3:9.01,5:5.05,10:3.33,20:2.72,40:2.46,60:2.38,120:2.30,200:2.27},
}
def fcrit_alpha(df1,df2,alpha):
    df1=int(clamp(df1,1,5))
    keys=sorted(F_CRIT_005[df1])
    lo=max(k for k in keys if k<=df2); hi=min(k for k in keys if k>=df2)
    base = F_CRIT_005[df1][lo] if lo==hi else F_CRIT_005[df1][lo] + (df2-lo)/(hi-lo)*(F_CRIT_005[df1][hi]-F_CRIT_005[df1][lo])
    if alpha==0.10: return base*0.85
    if alpha==0.01: return base*1.35
    return base

def generate_groups(k,n,effect,seed):
    rnd=random.Random(seed); base=rnd.uniform(55,65)
    groups={}
    for gi in range(k):
        shift=(gi-(k-1)/2)*(5.0*effect)+rnd.uniform(-1,1)
        m=base+shift; sd=max(2.5,6.0-1.2*effect+rnd.uniform(-1,1))
        groups[chr(65+gi)]=[rnd.gauss(m,sd) for _ in range(n)]
    return groups

def anova_oneway(groups):
    k=len(groups); n=len(next(iter(groups.values())))
    totals={g:sum(v) for g,v in groups.items()}
    means={g:totals[g]/len(groups[g]) for g in groups}
    allv=[x for arr in groups.values() for x in arr]
    gm=sum(allv)/len(allv)
    ssb=sum(len(groups[g])*(means[g]-gm)**2 for g in groups)
    ssw=sum(sum((x-means[g])**2 for x in groups[g]) for g in groups)
    sst=ssb+ssw; dfb=k-1; dfw=k*(n-1)
    msb,msw=ssb/dfb,ssw/dfw
    F=msb/msw if msw>0 else float("inf")
    eta2=ssb/sst if sst>0 else 0.0
    return {"k":k,"n":n,"means":means,"gm":gm,"ssb":ssb,"ssw":ssw,"sst":sst,"dfb":dfb,"dfw":dfw,"msb":msb,"msw":msw,"F":F,"eta2":eta2}

# -------------------------------------------------------------
# SIDEBAR (biar enak kontrol)
# -------------------------------------------------------------
sb = st.sidebar
sb.title("⚙️ Pengaturan")
k = sb.slider("Jumlah Kelompok (k)", 3, 6, 4)
n = sb.slider("Ukuran Sampel per Kelompok (n)", 4, 20, 8)
effect = sb.slider("Besaran Perbedaan Mean (effect)", 0.0, 2.0, 0.9, 0.1)
alpha = sb.select_slider("Taraf Signifikansi (α)", [0.10, 0.05, 0.01], value=0.05)
seed = sb.number_input("Seed (opsional)", min_value=1, max_value=99999, value=random.randint(1,99999), step=1)

if sb.button("🔁 Terapkan & Simulasikan"):
    st.session_state["_go"] = True
    st.session_state["_seed"] = int(seed)
    st.experimental_rerun()

seed = st.session_state.get("_seed", seed)

# -------------------------------------------------------------
# DATA + TABEL
# -------------------------------------------------------------
groups = generate_groups(k, n, effect, int(seed))
A = anova_oneway(groups)
df1, df2 = A["dfb"], A["dfw"]
Fcalc = A["F"];  Fcrit = fcrit_alpha(df1, df2, alpha)
signif = Fcalc > Fcrit

st.markdown(f"""
<div class="block">
  <div class="title">⚔️ ANOVA Odyssey — <span style="color:#4A67E9">Cinematic+</span></div>
  <div class="sub">One-way ANOVA (manual) dengan animasi interaktif.</div>
  <div class="hr"></div>
  <div class="tbl">
    <table>
      <thead><tr><th>No</th>{''.join(f'<th>Kelompok {g}</th>' for g in groups.keys())}</tr></thead>
      <tbody>
""", unsafe_allow_html=True)

rows = max(len(v) for v in groups.values())
for i in range(rows):
    st.markdown(
        "<tr><td>"+str(i+1)+"</td>"+"".join(f"<td>{fmt(groups[g][i])}</td>" for g in groups.keys())+"</tr>",
        unsafe_allow_html=True
    )

st.markdown("</tbody></table></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SIMULATED CALC (shimmer)
# -------------------------------------------------------------
with st.expander("▶️ Jalankan Perhitungan ANOVA (simulasi langkah)"):
    ph = st.empty()
    for txt in ["Menyiapkan data …","Menghitung rata-rata & grand mean …","Menghitung SSB & SSW …","Menyusun tabel ANOVA …","Selesai ✅"]:
        ph.markdown("<div class='shimmer'></div><div class='sub' style='font-size:12px;margin-top:6px'>"+txt+"</div>", unsafe_allow_html=True)
        time.sleep(0.16)

# -------------------------------------------------------------
# METRICS + KEPUTUSAN (count-up animasi via HTML)
# -------------------------------------------------------------
metric_payload = {
    "k": A["k"], "n": A["n"], "gm": float(A["gm"]),
    "ssb": float(A["ssb"]), "ssw": float(A["ssw"]), "sst": float(A["sst"]),
    "msb": float(A["msb"]), "msw": float(A["msw"]),
    "Fh": float(Fcalc), "Fc": float(Fcrit), "eta2": float(A["eta2"])
}
components.html("""
<div class="block">
  <div class="metrics">
    <div class="metric"><div class="k">Kelompok</div><div id="m1" class="v">0</div></div>
    <div class="metric"><div class="k">Sampel/Kelompok</div><div id="m2" class="v">0</div></div>
    <div class="metric"><div class="k">Grand Mean</div><div id="m3" class="v">0</div></div>
  </div>
  <div class="hr"></div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px">
    <div>
      <b>Between</b><br>
      SSB: <span id="ssb">0</span><br>df: <span id="dfb">0</span><br>MSB: <span id="msb">0</span>
    </div>
    <div>
      <b>Within</b><br>
      SSW: <span id="ssw">0</span><br>df: <span id="dfw">0</span><br>MSW: <span id="msw">0</span>
    </div>
    <div>
      <b>Total</b><br>
      SST: <span id="sst">0</span><br>F: <span id="fh">0</span><br>Eta²: <span id="eta">0</span>
    </div>
  </div>
  <div class="hr"></div>
  <div id="decision"></div>
</div>
<script>
const D = """ + json.dumps(metric_payload) + """;
function up(el, target, dur=800, fmt=val=>val.toString()){
  const start=performance.now(), from=0;
  function step(t){
    const p=Math.min(1,(t-start)/dur);
    el.textContent = fmt(from + (target-from)*p);
    if(p<1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}
const nfmt=(x)=> (Math.round(x*100)/100).toFixed(2);
up(document.getElementById('m1'), D.k, 600, v=>Math.round(v));
up(document.getElementById('m2'), D.n, 600, v=>Math.round(v));
up(document.getElementById('m3'), D.gm, 900, v=>nfmt(v));
document.getElementById('dfb').textContent = """ + str(df1) + """;
document.getElementById('dfw').textContent = """ + str(df2) + """;
up(document.getElementById('ssb'), D.ssb, 700, nfmt);
up(document.getElementById('ssw'), D.ssw, 700, nfmt);
up(document.getElementById('sst'), D.sst, 700, nfmt);
up(document.getElementById('msb'), D.msb, 700, nfmt);
up(document.getElementById('msw'), D.msw, 700, nfmt);
up(document.getElementById('fh'), D.Fh, 900, nfmt);
up(document.getElementById('eta'), D.eta2, 700, v=> (Math.round(v*1000)/1000).toFixed(3));
const sig = D.Fh > D.Fc;
const box = document.getElementById('decision');
box.innerHTML = sig
 ? "<div class='ok'>Keputusan: Tolak H₀ — F_hit ("+nfmt(D.Fh)+") > F_krit ("+nfmt(D.Fc)+")</div>"
 : "<div class='warn'>Keputusan: Gagal Menolak H₀ — F_hit ("+nfmt(D.Fh)+") ≤ F_krit ("+nfmt(D.Fc)+")</div>";
// konfeti 2 detik di kanan atas jika signifikan
if(sig){
  const host=document.body, c=document.createElement('canvas'); c.style.position='fixed'; c.style.top='12px'; c.style.right='0'; c.style.width='420px'; c.style.height='180px'; c.style.pointerEvents='none'; c.style.zIndex='9999'; host.appendChild(c);
  c.width=420; c.height=180; const ctx=c.getContext('2d'); let t0=null; const parts=[];
  for(let i=0;i<140;i++){ parts.push({x: 420*Math.random(), y: -20-60*Math.random(), vx: 60+120*Math.random(), vy: 40+80*Math.random(), g: 180+Math.random()*160, s: 4+Math.random()*6, rot: Math.random()*6.28, col: i%2? '#CBB279':'#4A67E9'}); }
  function step(ts){ if(!t0) t0=ts; const t=ts-t0; ctx.clearRect(0,0,420,180);
    for(const p of parts){ p.x+=p.vx/60; p.y+=p.vy/60; p.vy+=p.g/2000; p.rot+=0.08; ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot); ctx.fillStyle=p.col; ctx.fillRect(-p.s/2,-p.s/2,p.s,p.s); ctx.restore(); }
    if(t<2000) requestAnimationFrame(step); else host.removeChild(c);
  }
  requestAnimationFrame(step);
}
</script>
""", height=320)

# -------------------------------------------------------------
# GRAFIK F BESAR (animasi menulis, area fill, bounce, tooltip)
# -------------------------------------------------------------
# siapkan data kurva
xmax = max(Fcrit*1.6, Fcalc*1.2, 10+df1)
xs   = [i*xmax/900 for i in range(901)]
ys   = [f_pdf(x, df1, df2) for x in xs]
chart_payload = {
    "xmax": xmax, "xs": xs, "ys": ys,
    "Fcrit": Fcrit, "Fcalc": Fcalc,
}
components.html("""
<div class="chart-card">
  <div style="display:flex;gap:10px;align-items:center;margin:2px 4px 8px 4px">
    <b>📈 Distribusi F (α=""" + str(alpha) + """)</b>
  </div>
  <div id="fchart-host" style="position:relative"></div>
  <div class="legend"><span class="dot dot-ns"></span> Non-Signifikan <span class="dot dot-sg"></span> Signifikan</div>
</div>
<script>
const D = """ + json.dumps(chart_payload) + """;
const host = document.getElementById('fchart-host');
const ns='http://www.w3.org/2000/svg';
const W=(host.clientWidth||1100), H=520, P=60;
const svg=document.createElementNS(ns,'svg');
svg.setAttribute('viewBox','0 0 '+W+' '+H); svg.style.width='100%'; svg.style.height=H+'px'; host.appendChild(svg);
// tooltip
const tip=document.createElement('div'); tip.className='tooltip'; host.appendChild(tip);

const maxY = Math.max(...D.ys) || 1;
function mapX(x){return P+(W-2*P)*(x/D.xmax);}
function mapY(y){return H-P-(H-2*P)*(y/maxY);}

// axis
const ax=document.createElementNS(ns,'line'); ax.setAttribute('x1',P); ax.setAttribute('x2',W-P); ax.setAttribute('y1',mapY(0)); ax.setAttribute('y2',mapY(0));
ax.setAttribute('stroke','#CBD5E1'); ax.setAttribute('stroke-width','1.2'); svg.appendChild(ax);

// gradients & glow
const defs=document.createElementNS(ns,'defs');
defs.innerHTML =
 "<linearGradient id='gL'><stop offset='0%' stop-color='#9db4ff' stop-opacity='0.95'/>"+
 "<stop offset='100%' stop-color='#c9d6ff' stop-opacity='0.3'/></linearGradient>"+
 "<linearGradient id='gR'><stop offset='0%' stop-color='#DCCCA3' stop-opacity='0.95'/>"+
 "<stop offset='100%' stop-color='#CBB279' stop-opacity='0.5'/></linearGradient>"+
 "<filter id='glow'><feGaussianBlur stdDeviation='2.0' result='b'/>"+
 "<feMerge><feMergeNode in='b'/><feMergeNode in='SourceGraphic'/></feMerge></filter>";
svg.appendChild(defs);

// paths
const areaL=document.createElementNS(ns,'path'), areaR=document.createElementNS(ns,'path'), curve=document.createElementNS(ns,'path');
areaL.setAttribute('fill','url(#gL)'); areaR.setAttribute('fill','url(#gR)'); areaR.setAttribute('filter','url(#glow)');
curve.setAttribute('fill','none'); curve.setAttribute('stroke','#4A67E9'); curve.setAttribute('stroke-width','2.6'); curve.setAttribute('filter','url(#glow)');
svg.appendChild(areaL); svg.appendChild(areaR); svg.appendChild(curve);

// critical & hit lines + labels
function vline(x,col,w,id){
  const l=document.createElementNS(ns,'line'); l.id=id; l.setAttribute('x1',x); l.setAttribute('x2',x); l.setAttribute('y1',P); l.setAttribute('y2',H-P);
  l.setAttribute('stroke',col); l.setAttribute('stroke-width',w); l.setAttribute('filter','url(#glow)'); svg.appendChild(l); return l;
}
const FcX = mapX(D.Fcrit), FhX = mapX(D.Fcalc);
const lFc = vline(FcX,'#111827',1.6,'lFc');
const lFh = vline(FhX,'#4A67E9',2.4,'lFh');
function label(txt,x,y){ const t=document.createElementNS(ns,'text'); t.textContent=txt; t.setAttribute('x',x+6); t.setAttribute('y',y); t.setAttribute('fill','#111827'); t.setAttribute('font-size','12'); svg.appendChild(t); }
label('F_krit = '+D.Fcrit.toFixed(3), FcX, P+14); label('F_hit = '+D.Fcalc.toFixed(3), FhX, P+28);

// build arrays for animation
const n = D.xs.length;
let left=[], right=[], curvePts=[];
for(let i=0;i<n;i++){
  const px = mapX(D.xs[i]), py = mapY(D.ys[i]);
  curvePts.push([px,py]);
  if(D.xs[i] <= D.Fcrit) left.push([px,py]); else right.push([px,py]);
}
function toPath(arr){ if(!arr.length) return ''; let s='M'+arr[0][0]+','+arr[0][1]; for(let i=1;i<arr.length;i++) s+='L'+arr[i][0]+','+arr[i][1]; return s; }
function areaPath(arr){
  if(!arr.length) return ''; let s='M'+arr[0][0]+','+arr[0][1]; for(let i=1;i<arr.length;i++) s+='L'+arr[i][0]+','+arr[i][1];
  const L=arr[arr.length-1]; return s+'L'+L[0]+','+mapY(0)+'L'+arr[0][0]+','+mapY(0)+'Z';
}

// animate draw
let start=null; const DUR=3200;
function anim(ts){
  if(!start) start=ts;
  const p=Math.min(1,(ts-start)/DUR), idx=Math.max(2,Math.floor(curvePts.length*p));
  curve.setAttribute('d', toPath(curvePts.slice(0,idx)));
  // area slice
  const lidx = Math.min(idx, left.length), ridx = Math.max(0, idx - left.length);
  areaL.setAttribute('d', areaPath(left.slice(0, lidx)));
  areaR.setAttribute('d', areaPath(right.slice(0, ridx)));
  if(p<1) requestAnimationFrame(anim); else bounceFhit();
}
requestAnimationFrame(anim);

// bounce kecil di garis F_hit
function bounceFhit(){
  const base=FhX; let t0=null; const T=600;
  function step(ts){
    if(!t0) t0=ts; const u=Math.min(1,(ts-t0)/T);
    const amp=7*(1-u);
    const x=base + Math.sin(u*Math.PI*2)*amp;
    lFh.setAttribute('x1',x); lFh.setAttribute('x2',x);
    if(u<1) requestAnimationFrame(step); else { lFh.setAttribute('x1',base); lFh.setAttribute('x2',base); }
  }
  requestAnimationFrame(step);
}

// tooltip interaktif
svg.addEventListener('mousemove', (e)=>{
  const rect=svg.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const xr = (x - P) / (W-2*P); if(xr<0||xr>1){ tip.style.opacity=0; return; }
  const xval = xr * D.xmax;
  // cari y terdekat
  let i=Math.floor(xr*(n-1)); if(i<0) i=0; if(i>n-2) i=n-2;
  const yval = D.ys[i];
  tip.style.left = e.clientX - rect.left + 'px';
  tip.style.top  = e.clientY - rect.top  + 'px';
  tip.style.opacity = 1;
  tip.textContent = 'x='+xval.toFixed(3)+' | pdf='+yval.toFixed(4);
});
svg.addEventListener('mouseleave', ()=> tip.style.opacity=0);
</script>
""", height=620, scrolling=False)

# -------------------------------------------------------------
# FOOTER
# -------------------------------------------------------------
st.caption("Catatan: Tabel F-kritikal berbasis α=0.05 (interpolasi), skala untuk α=0.10/0.01 bersifat monotonic—cukup untuk edukasi & gameplay.")

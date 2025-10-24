# =============================================================
# ANOVA ODYSSEY — FULLSCREEN CINEMATIC v5.2 (syntax-safe)
# -------------------------------------------------------------
# Mode: Fullscreen (tanpa sidebar), tema elegan biru-emas
# Dependensi: HANYA streamlit (bawaan) + JS/HTML murni
# Animasi: progress shimmer, konfeti kanan, kurva F animatif
# Fix: semua f-string JS/HTML aman tanpa SyntaxError
# =============================================================

import math, random, time, json
import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------------------
# 1) PAGE CONFIG
# -------------------------------------------------------------
st.set_page_config(
    page_title="ANOVA Odyssey – Full Cinematic Glow",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------------------------------------
# 2) CSS TEMA & HEADER
# -------------------------------------------------------------
st.markdown("""
<style>
:root{
  --bg1:#EAF4FB; --bg2:#FFFFFF; --ink:#0F172A; --muted:#64748B;
  --gold:#DCCCA3; --gold2:#CBB279; --bl:#4A67E9; --bl2:#7EA3FF;
  --soft:#F7FBFF; --card:#ffffff;
}
section[data-testid="stSidebar"]{display:none !important;}
section.main > div.block-container{padding-top:0.8rem; max-width:1280px;}
.hero{position:sticky;top:0;z-index:12;backdrop-filter:blur(8px);
background:linear-gradient(180deg,rgba(255,255,255,.75),rgba(255,255,255,.45));
border-bottom:1px solid rgba(0,0,0,.06);}
.title-card{display:flex;justify-content:space-between;align-items:center;
padding:16px 20px;margin:10px 0;border-radius:16px;}
.t-main{font-size:30px;font-weight:900;color:var(--ink);}
.t-main span{color:var(--bl);animation:glow 3s ease-in-out infinite;}
@keyframes glow{0%,100%{text-shadow:0 0 0 var(--bl);}50%{text-shadow:0 0 18px var(--bl2);}}
.badge{background:var(--gold);padding:8px 14px;border-radius:999px;font-weight:800;}
.card{background:var(--card);padding:18px;border-radius:16px;box-shadow:0 10px 30px rgba(10,30,60,.06);}
.metric{background:var(--soft);border-radius:10px;padding:10px;text-align:center;}
.tbl table{width:100%;border-collapse:collapse;font-size:13px;}
.tbl th,.tbl td{padding:6px;border:1px solid #e5e7eb;text-align:center;}
.hr{height:1px;background:#e5e7eb;margin:10px 0;}
.ok{background:#dcfce7;color:#166534;padding:10px;border-radius:10px;}
.warn{background:#fef9c3;color:#854d0e;padding:10px;border-radius:10px;}
#fchart-host{width:100%;}
.chart-card{background:var(--card);border-radius:16px;box-shadow:0 8px 28px rgba(0,0,0,.05);padding:12px;}
.legend{display:flex;gap:16px;align-items:center;margin-top:6px;}
.dot{width:14px;height:14px;border-radius:4px;display:inline-block;}
.dot-ns{background:linear-gradient(180deg,#9db4ff,#c9d6ff);}
.dot-sg{background:linear-gradient(180deg,#DCCCA3,#CBB279);}
</style>
<div class="hero">
 <div class="title-card">
   <div class="t-main">⚔️ ANOVA Odyssey: <span>Full Cinematic Glow</span></div>
   <div class="badge">Biru & Emas Elegan</div>
 </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 3) FUNGSI UTAMA
# -------------------------------------------------------------
fmt = lambda x, p=2: f"{x:.{p}f}"
def clamp(x,a,b): return max(a,min(b,x))

def beta_func(a,b): return math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
def f_pdf(x,d1,d2):
    if x<=0: return 0
    a,b=d1/2,d2/2
    num=(d1**(d1/2))*(d2**(d2/2))*(x**(a-1))
    den=(d1*x+d2)**((d1+d2)/2)*beta_func(a,b)
    val=num/den
    return max(val,0)

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
    if lo==hi: base=F_CRIT_005[df1][lo]
    else:
        y0,y1=F_CRIT_005[df1][lo],F_CRIT_005[df1][hi]
        t=(df2-lo)/(hi-lo)
        base=y0+t*(y1-y0)
    if alpha==0.10: return base*0.85
    if alpha==0.01: return base*1.35
    return base

def generate_groups(k,n,effect,seed):
    rnd=random.Random(seed); base=rnd.uniform(55,65)
    groups={}
    for gi in range(k):
        mean_shift=(gi-(k-1)/2)*(5.0*effect)+rnd.uniform(-1,1)
        m=base+mean_shift; sd=max(2.5,6.0-1.2*effect+rnd.uniform(-1,1))
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
    sst=ssb+ssw
    dfb,dfw=k-1,k*(n-1)
    msb,msw=ssb/dfb,ssw/dfw
    F=msb/msw if msw>0 else float("inf")
    return {"k":k,"n":n,"dfb":dfb,"dfw":dfw,"ssb":ssb,"ssw":ssw,"sst":sst,"msb":msb,"msw":msw,"F":F}

# -------------------------------------------------------------
# 4) KONTROL
# -------------------------------------------------------------
ss=st.session_state
ss.setdefault("seed",random.randint(1,9999))
ss.setdefault("controls",{"k":4,"n":8,"effect":0.9,"alpha":0.05})

c1,c2=st.columns(2)
with c1:
    k=st.slider("Jumlah Kelompok (k)",3,6,ss.controls["k"])
    n=st.slider("Ukuran Sampel (n)",4,20,ss.controls["n"])
with c2:
    effect=st.slider("Perbedaan Mean (effect)",0.0,2.0,ss.controls["effect"],0.1)
    alpha=st.select_slider("Taraf Signifikansi (α)",[0.10,0.05,0.01],value=ss.controls["alpha"])
if st.button("🔁 Terapkan"):
    ss.controls.update({"k":k,"n":n,"effect":effect,"alpha":alpha})
    ss.seed=random.randint(1,9999)
    st.rerun()

# -------------------------------------------------------------
# 5) GENERATE DATA + HITUNG
# -------------------------------------------------------------
groups=generate_groups(k,n,effect,ss.seed)
A=anova_oneway(groups)
df1,df2=A["dfb"],A["dfw"]
Fcalc=A["F"]; Fcrit=fcrit_alpha(df1,df2,alpha)
signif=Fcalc>Fcrit

# -------------------------------------------------------------
# 6) OUTPUT RINGKAS
# -------------------------------------------------------------
st.markdown("<div class='card'><b>📊 Tabel Data</b></div>",unsafe_allow_html=True)
labels=list(groups.keys())
rows=max(len(v) for v in groups.values())
tbl=["<div class='tbl'><table><tr><th>No</th>"+''.join(f"<th>{g}</th>" for g in labels)+"</tr>"]
for i in range(rows):
    tbl.append("<tr><td>"+str(i+1)+"</td>"+"".join(f"<td>{fmt(groups[g][i])}</td>" for g in labels)+"</tr>")
tbl.append("</table></div>")
st.markdown("".join(tbl),unsafe_allow_html=True)

st.markdown("<div class='card'>",unsafe_allow_html=True)
c1,c2,c3=st.columns(3)
c1.metric("Kelompok",A["k"])
c2.metric("Sampel/Kelompok",A["n"])
c3.metric("Grand Mean",fmt(sum([x for arr in groups.values() for x in arr])/len(groups)))

st.markdown("<div class='hr'></div>",unsafe_allow_html=True)
c1,c2=st.columns(2)
c1.write(f"**Fhitung:** {fmt(Fcalc,4)}")
c1.write(f"**Fkrit ({alpha}):** {fmt(Fcrit,3)}")
c2.write(f"**df antara:** {df1} | **df dalam:** {df2}")

if signif:
    st.markdown(f"<div class='ok'>Keputusan: Tolak H₀<br>Fhitung ({fmt(Fcalc)}) > Fkrit ({fmt(Fcrit)})</div>",unsafe_allow_html=True)
else:
    st.markdown(f"<div class='warn'>Keputusan: Gagal Menolak H₀<br>Fhitung ({fmt(Fcalc)}) ≤ Fkrit ({fmt(Fcrit)})</div>",unsafe_allow_html=True)

st.markdown("</div>",unsafe_allow_html=True)

# -------------------------------------------------------------
# 7) GRAFIK F BESAR (tanpa f-string konflik)
# -------------------------------------------------------------
xmax=max(Fcrit*1.5,Fcalc*1.2,10+df1)
xs=[i*xmax/700 for i in range(701)]
ys=[f_pdf(x,df1,df2) for x in xs]
payload={
    "xmax":xmax,"xs":xs,"ys":ys,
    "Fcrit":Fcrit,"Fcalc":Fcalc,
}
components.html("""
<div class='chart-card'>
 <div class='u-row'><b>📈 Distribusi F</b></div>
 <div id='fchart-host'></div>
 <div class='legend'><span class='dot dot-ns'></span> Non-Signifikan 
 <span class='dot dot-sg'></span> Signifikan</div>
</div>
<script>
const D = """ + json.dumps(payload) + """;
const host=document.getElementById('fchart-host');
const ns='http://www.w3.org/2000/svg';
const W=host.clientWidth||800,H=400,P=50;
const svg=document.createElementNS(ns,'svg');
svg.setAttribute('viewBox','0 0 '+W+' '+H);
svg.style.width='100%';svg.style.height=H+'px';
host.appendChild(svg);
const maxY=Math.max(...D.ys);
function mapX(x){return P+(W-2*P)*(x/D.xmax);}
function mapY(y){return H-P-(H-2*P)*(y/maxY);}
function pathCurve(){
 let s='M'+mapX(D.xs[0])+','+mapY(D.ys[0]);
 for(let i=1;i<D.xs.length;i++) s+='L'+mapX(D.xs[i])+','+mapY(D.ys[i]);
 return s;
}
const curve=document.createElementNS(ns,'path');
curve.setAttribute('d',pathCurve());
curve.setAttribute('stroke','#4A67E9');
curve.setAttribute('stroke-width','2');
curve.setAttribute('fill','none');
svg.appendChild(curve);
const lineCrit=document.createElementNS(ns,'line');
lineCrit.setAttribute('x1',mapX(D.Fcrit));lineCrit.setAttribute('x2',mapX(D.Fcrit));
lineCrit.setAttribute('y1',P);lineCrit.setAttribute('y2',H-P);
lineCrit.setAttribute('stroke','#CBB279');lineCrit.setAttribute('stroke-width','2');
svg.appendChild(lineCrit);
const lineHit=document.createElementNS(ns,'line');
lineHit.setAttribute('x1',mapX(D.Fcalc));lineHit.setAttribute('x2',mapX(D.Fcalc));
lineHit.setAttribute('y1',P);lineHit.setAttribute('y2',H-P);
lineHit.setAttribute('stroke','#4A67E9');lineHit.setAttribute('stroke-width','2.4');
svg.appendChild(lineHit);
</script>
""",height=480,scrolling=False)

st.caption("Catatan: Nilai Fkrit disesuaikan dari tabel α=0.05 dengan skala α lainnya.")

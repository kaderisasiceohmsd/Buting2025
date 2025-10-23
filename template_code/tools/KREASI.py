# ==============================================
# WeatherForge: Forecast Lab v2 (Ultimate Edition)
# Safe, no dependency, no error, full animation
# ==============================================
import streamlit as st
import random, time

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(page_title="WeatherForge: Forecast Lab", page_icon="⛅", layout="centered")

# ----------------------------- STYLE -----------------------------
st.markdown("""
<style>
:root {
  --bg-soft: #EAF4FB; --panel: #fff; --gold: #DCCCA3;
  --gold2:#CBB279; --ink:#1F2937; --muted:#6B7280;
  --blue:#4A67E9;
}
html, body, [data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,var(--bg-soft),#fff 60%);
}
section.main > div.block-container{padding-top:1.2rem;}
.card{background:var(--panel);border:1px solid rgba(0,0,0,.05);
border-radius:16px;box-shadow:0 10px 28px rgba(0,0,0,.05);
padding:18px 20px;}
.title{font-weight:900;color:var(--ink);}
.sub{color:var(--muted);}
.chip{background:var(--gold);border-radius:999px;
padding:5px 12px;font-weight:800;color:#111;}
.hr{height:1px;background:rgba(0,0,0,.08);margin:10px 0;}
.metric{background:#F7FBFF;border:1px solid rgba(0,0,0,.05);
border-radius:12px;padding:10px 12px;text-align:center;}
.metric .k{font-size:13px;color:var(--muted);}
.metric .v{font-size:22px;font-weight:800;}
.table{width:100%;border-collapse:collapse;background:#fff;
border-radius:12px;overflow:hidden;border:1px solid rgba(0,0,0,.06);}
.table th,.table td{padding:6px 8px;border-bottom:1px solid rgba(0,0,0,.06);text-align:center;font-size:13px;}
.table tr:last-child td{border-bottom:none;}
.bar{height:16px;border-radius:9px;overflow:hidden;background:linear-gradient(90deg,var(--gold),var(--gold2));}
.fill{height:100%;border-radius:9px;background:linear-gradient(90deg,var(--blue),#7EA3FF);}
.pill{background:#eef2ff;border-radius:999px;padding:4px 10px;color:#1e3a8a;font-weight:700;border:1px solid rgba(37,99,235,.25);}
.badge{border-radius:12px;padding:6px 10px;font-weight:700;}
.badge.ok{background:#dcfce7;color:#065f46;}
.badge.err{background:#fee2e2;color:#7f1d1d;}
.note{color:var(--muted);font-size:12px;}
.graph{position:relative;width:100%;height:150px;background:linear-gradient(to top,#f8fafc,#fff);border-radius:12px;border:1px solid rgba(0,0,0,.06);}
.graph-line{position:absolute;height:2px;background:linear-gradient(90deg,var(--blue),#7EA3FF);border-radius:3px;}
.lightning{animation:flash 0.25s ease-in-out infinite alternate;}
@keyframes flash{from{opacity:0.2;}to{opacity:1;}}
</style>
""", unsafe_allow_html=True)

# ----------------------------- INIT STATE -----------------------------
def init_state():
    defaults = {
        "round": 1, "score": 0, "best": 0, "seed": random.randint(1,9999),
        "history": [], "city": "Bandar Lampung", "season": "Rainy",
        "forecast": [], "guess": [], "challenge_locked": False,
        "controls": {"humidity":70,"pressure":1008,"wind":12,"days":7}
    }
    for k,v in defaults.items():
        if k not in st.session_state: st.session_state[k] = v
    for k,v in defaults["controls"].items():
        st.session_state["controls"].setdefault(k,v)
init_state()

# ----------------------------- WEATHER LOGIC -----------------------------
def clamp(x,a,b): return max(a,min(b,x))
def icon(cond): return {"Clear":"☀️","Clouds":"⛅","Rain":"🌧️","Storm":"⛈️","Drizzle":"🌦️"}.get(cond,"🌤️")
def comfort(temp,hum,wind):
    t=100-abs(temp-26)*4;h=100-abs(hum-55)*1.2;w=100-abs(wind-10)*3
    return clamp((0.4*t+0.4*h+0.2*w),0,100)
def base_temp(city,season):
    base=29
    if "bandung" in city.lower(): base=24
    if "surabaya" in city.lower(): base=31
    if "bali" in city.lower(): base=30
    adj={"Rainy":-1.2,"Dry":-0.8,"Transitional":-0.4}.get(season,0)
    return base+adj,3.5
def forecast(seed,city,season,hum,pres,wind,days):
    rng=random.Random(seed)
    base,vol=base_temp(city,season)
    out=[];last=base+rng.uniform(-1,1)
    for d in range(1,days+1):
        drift=rng.uniform(-vol,vol)*0.5+(hum-60)*0.02
        temp=clamp(last+drift,21,38);last=temp
        rain_p=clamp(0.25+(1008-pres)/30+(hum-65)/40,0,0.9)
        cond="Clear";rain=0
        r=rng.random()
        if r<rain_p*0.2: cond="Storm"; rain=rng.uniform(20,50)
        elif r<rain_p*0.5: cond="Rain"; rain=rng.uniform(3,25)
        elif r<rain_p*0.7: cond="Drizzle"; rain=rng.uniform(1,5)
        elif r<rain_p*0.95: cond="Clouds"
        wind_d=clamp(int(wind+rng.uniform(-4,4)),2,40)
        hum_d=clamp(int(hum+rng.uniform(-8,8)),40,98)
        pres_d=clamp(int(pres+rng.uniform(-5,5)),990,1025)
        out.append({
            "day":d,"temp":round(temp,1),"cond":cond,"rain":round(rain,1),
            "wind":wind_d,"humidity":hum_d,"pressure":pres_d,
            "comfort":round(comfort(temp,hum_d,wind_d),1)
        })
    return out

# ----------------------------- VISUALS -----------------------------
def table(data):
    head="<tr><th>Hari</th><th>Cuaca</th><th>Suhu</th><th>Hujan</th><th>RH</th><th>Tekanan</th><th>Angin</th><th>Comfort</th></tr>"
    rows=[]
    for d in data:
        style="class='lightning'" if d['cond']=="Storm" else ""
        rows.append(f"<tr {style}><td>{d['day']}</td><td>{icon(d['cond'])} {d['cond']}</td>"
                    f"<td>{d['temp']}°C</td><td>{d['rain']}mm</td>"
                    f"<td>{d['humidity']}%</td><td>{d['pressure']}</td>"
                    f"<td>{d['wind']}</td><td>{d['comfort']}</td></tr>")
    st.markdown(f"<table class='table'><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table>",unsafe_allow_html=True)

def chart_temp_graph(data):
    vals=[d["temp"] for d in data]
    mx=max(vals);mn=min(vals)
    norm=[(v-mn)/(mx-mn+1e-9) for v in vals]
    st.markdown("<div class='card'><b>📈 Grafik Suhu Harian</b>",unsafe_allow_html=True)
    html="<div class='graph'>"
    for i in range(len(norm)-1):
        x1=i*(100/len(norm));x2=(i+1)*(100/len(norm))
        y1=100-norm[i]*100;y2=100-norm[i+1]*100
        html+=f"<div class='graph-line' style='left:{x1}%;top:{y1}%;width:{x2-x1}%;transform:translateY(-50%)'></div>"
    html+="</div>"
    st.markdown(html,unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)

# ----------------------------- INSIGHT -----------------------------
def insight(data):
    t=[d["temp"] for d in data];r=[d["rain"] for d in data];c=[d["comfort"] for d in data]
    avg_t=sum(t)/len(t);avg_r=sum(r)/len(r);avg_c=sum(c)/len(c)
    vol=max(t)-min(t);wet=sum(1 for x in r if x>=1)
    st.markdown("<div class='card'><b>🔬 Lab Insights</b>",unsafe_allow_html=True)
    cols=st.columns(4)
    cols[0].markdown(f"<div class='metric'><div class='k'>Avg Temp</div><div class='v'>{avg_t:.1f}°</div></div>",unsafe_allow_html=True)
    cols[1].markdown(f"<div class='metric'><div class='k'>Avg Rain</div><div class='v'>{avg_r:.1f}</div></div>",unsafe_allow_html=True)
    cols[2].markdown(f"<div class='metric'><div class='k'>Volatilitas</div><div class='v'>{vol:.1f}</div></div>",unsafe_allow_html=True)
    cols[3].markdown(f"<div class='metric'><div class='k'>Comfort</div><div class='v'>{avg_c:.1f}</div></div>",unsafe_allow_html=True)
    st.markdown(f"<div class='note'>Hari hujan: {wet} dari {len(data)} hari</div>",unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)

# ----------------------------- HEADER -----------------------------
st.markdown("""
<div class='card' style='display:flex;align-items:center;justify-content:space-between;'>
 <div><div class='title' style='font-size:28px;'>⛅ WeatherForge: <span style='color:#4A67E9'>Forecast Lab</span></div>
 <div class='sub'>Kreasi I (Bebas) · HMSD Adyatama ITERA 2025</div></div>
 <div class='chip'>Elegan · Biru & Emas</div></div>
""",unsafe_allow_html=True)

# ----------------------------- SIDEBAR -----------------------------
with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("Ronde:",st.session_state.round)
    st.write("Skor:",st.session_state.score)
    st.write("Best:",st.session_state.best)
    st.markdown("---")
    if st.button("🔄 Reset Game"):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()

# ----------------------------- CONTROLS -----------------------------
with st.expander("⚙️ Pengaturan Simulasi"):
    c1,c2=st.columns(2)
    with c1:
        st.session_state.city=st.text_input("Kota",st.session_state.city)
        st.session_state.season=st.selectbox("Musim",["Rainy","Dry","Transitional"],index=0)
    with c2:
        st.session_state.controls["days"]=st.slider("Jumlah Hari",5,10,st.session_state.controls.get("days",7))
    c3,c4,c5=st.columns(3)
    with c3:
        st.session_state.controls["humidity"]=st.slider("Kelembapan (%)",40,95,st.session_state.controls["humidity"])
    with c4:
        st.session_state.controls["pressure"]=st.slider("Tekanan (hPa)",990,1025,st.session_state.controls["pressure"])
    with c5:
        st.session_state.controls["wind"]=st.slider("Angin (km/j)",2,40,st.session_state.controls["wind"])
    if st.button("🔁 Terapkan"):
        st.session_state.seed=random.randint(1,9999)
        st.session_state.challenge_locked=False

# ----------------------------- PROGRESS SIMULATION -----------------------------
with st.expander("▶️ Jalankan Mesin Prakiraan"):
    prog=st.progress(0,"Menyiapkan model …")
    for i,txt in enumerate(["Membaca parameter…","Mengestimasi suhu…","Menganalisis peluang hujan…","Merakit laporan…","Selesai ✅"],start=1):
        prog.progress(i*20,txt);time.sleep(0.18)

# ----------------------------- GENERATE -----------------------------
c=st.session_state.controls
data=forecast(st.session_state.seed+st.session_state.round,
              st.session_state.city,st.session_state.season,
              c["humidity"],c["pressure"],c["wind"],c["days"])
st.session_state.forecast=data

# ----------------------------- SHOW -----------------------------
st.markdown(f"<div class='card'><b>📋 Prakiraan {st.session_state.city}</b>",unsafe_allow_html=True)
table(data)
st.markdown("</div>",unsafe_allow_html=True)
colA,colB=st.columns(2)
with colA: chart_temp_graph(data)
with colB: insight(data)

# ----------------------------- CHALLENGE -----------------------------
st.markdown("<div class='card'><b>🎯 Challenge: Tebak Hari Hujan</b>",unsafe_allow_html=True)
guess=[]
cols=st.columns(min(7,len(data)))
for i,d in enumerate(data):
    with cols[i%len(cols)]:
        val=st.checkbox(f"D{d['day']}",value=False,disabled=st.session_state.challenge_locked,key=f"chk{i}")
        guess.append(val)
c1,c2=st.columns(2)
with c1:
    lock=st.button("Kunci Jawaban 🚀",disabled=st.session_state.challenge_locked)
with c2:
    nxt=st.button("Lanjut 🔁")

if lock and not st.session_state.challenge_locked:
    truth=[d["rain"]>=1 for d in data]
    ok=(truth==guess)
    bef=st.session_state.score
    if ok:
        st.session_state.score+=10
        st.balloons()
        st.markdown("<div class='badge ok'>✅ Semua tebakan benar! +10</div>",unsafe_allow_html=True)
    else:
        st.session_state.score-=5
        miss=[i+1 for i,(t,g) in enumerate(zip(truth,guess)) if t!=g]
        st.markdown(f"<div class='badge err'>❌ Meleset di hari: {miss} (-5)</div>",unsafe_allow_html=True)
    st.session_state.challenge_locked=True
    st.session_state.history.append({"round":st.session_state.round,"score":st.session_state.score})
if nxt:
    st.session_state.round+=1
    st.session_state.challenge_locked=False
    st.rerun()

st.markdown("</div>",unsafe_allow_html=True)
st.markdown("<div class='hr'></div>",unsafe_allow_html=True)
st.caption("WeatherForge: Forecast Lab © 2025 — Kreasi I HMSD Adyatama ITERA · Dengan animasi kilat & grafik suhu elegan 🌩️")

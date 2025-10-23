# ============================================================
# WeatherForge: Climate Simulation Lab – Elegant Edition (FINAL)
# Kreasi I (Bebas) • Tema elegan biru–emas, animasi, progress
# Tidak bentrok dengan ANOVA (prefix state: weather_)
# Tidak butuh install lib tambahan (stdlib + streamlit saja)
# ============================================================

import streamlit as st
import random
import time
from typing import List, Dict

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(page_title="WeatherForge: Climate Simulation Lab", page_icon="⛅", layout="centered")

# ----------------------------- THEME (Biru–Emas) -----------------------------
st.markdown("""
<style>
:root{
  --bg-soft:#EAF4FB; --panel:#FFFFFF; --panel-soft:#F7FBFF;
  --gold:#DCCCA3; --gold2:#CBB279; --ink:#1F2937; --muted:#6B7280;
  --blue:#4A67E9; --ok:#16a34a; --warn:#ca8a04; --err:#dc2626;
}
html, body, [data-testid="stAppViewContainer"]{
  background:linear-gradient(180deg,var(--bg-soft),#FFFFFF 60%);
}
section.main > div.block-container{ padding-top:1.1rem; }

.card{
  background:var(--panel); border:1px solid rgba(0,0,0,.05);
  border-radius:16px; box-shadow:0 12px 30px rgba(20,35,70,.06);
  padding:18px 20px;
}
.title{ font-weight:900; color:var(--ink); letter-spacing:.2px; }
.sub{ color:var(--muted); font-weight:500; }
.chip{ display:inline-flex; align-items:center; gap:8px; padding:6px 12px;
  background:var(--gold); color:#111; border-radius:999px; font-weight:800; }
.hr{ height:1px; background:rgba(0,0,0,.08); margin:12px 0; }

.metric{
  display:flex; flex-direction:column; gap:4px; padding:12px 14px; border-radius:12px;
  background:var(--panel-soft); border:1px solid rgba(0,0,0,.06);
}
.metric .k{ font-size:13px; color:var(--muted); font-weight:600; }
.metric .v{ font-size:22px; font-weight:900; color:var(--ink); }

.table{
  width:100%; border-collapse:separate; border-spacing:0; background:#fff; overflow:hidden; border-radius:12px;
  border:1px solid rgba(0,0,0,.06);
}
.table thead tr{ background:#f3f4f6; }
.table th,.table td{ padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06); text-align:center; font-size:13px; }
.table tr:last-child td{ border-bottom:none; }

.badge{ display:inline-flex; align-items:center; gap:6px; font-weight:800; border-radius:12px; padding:6px 10px; }
.badge.ok{ background:#dcfce7; color:#065f46; }
.badge.err{ background:#fee2e2; color:#7f1d1d; }
.badge.warn{ background:#fef9c3; color:#854d0e; }

.note{ color:#6b7280; font-size:12px; }

.chart{
  border:1px dashed rgba(0,0,0,.12); background:#fff; border-radius:14px; padding:14px;
}
.barrow{ display:flex; align-items:center; gap:10px; margin:6px 0; }
.barlabel{ min-width:70px; font-weight:800; color:#111827; }
.bar{
  flex:1; height:18px; border-radius:9px; position:relative;
  background:linear-gradient(90deg, var(--gold), var(--gold2));
  box-shadow: inset 0 0 0 2px rgba(0,0,0,.05);
}
.bar::after{ content:""; position:absolute; inset:0; border-radius:9px; box-shadow: inset 0 8px 12px rgba(255,255,255,.35); }
.fill{ height:100%; border-radius:9px; background: linear-gradient(90deg, var(--blue), #7EA3FF); width:0%; }
.pill{ display:inline-flex; align-items:center; gap:8px; padding:6px 10px; border-radius:999px; background:#eef2ff; color:#1e3a8a; border:1px solid rgba(37,99,235,.25); font-weight:800; }

.graph{ position:relative; width:100%; height:170px; background:linear-gradient(to top,#f9fafb,#fff); border-radius:12px; border:1px solid rgba(0,0,0,.06); overflow:hidden; }
.graph-line{ position:absolute; height:2px; background:linear-gradient(90deg,var(--blue),#7EA3FF); border-radius:3px; }
.graph-dot{ position:absolute; width:8px; height:8px; border-radius:999px; background:#4A67E9; transform:translate(-50%,-50%); box-shadow:0 0 0 3px rgba(74,103,233,.15); }

.lightning{ animation:flash .28s ease-in-out infinite alternate; }
@keyframes flash{ from{ filter:brightness(.7); } to{ filter:brightness(1.2); } }

.raindrop{ position:absolute; width:2px; height:8px; background:#4A67E9; opacity:.0; animation:rain 1.1s linear infinite; }
@keyframes rain{ 0%{ transform:translateY(-10px); opacity:0;} 20%{opacity:.7;} 100%{ transform:translateY(190px); opacity:0;} }

.legend{ display:flex; gap:10px; flex-wrap:wrap; }
.legend .l{ display:flex; align-items:center; gap:6px; font-size:12px; color:#374151; }
.legend .box{ width:12px; height:12px; border-radius:3px; background: var(--blue); box-shadow: 0 1px 0 rgba(0,0,0,.2); }
.legend .box2{ width:12px; height:12px; border-radius:3px; background: var(--gold2); box-shadow: 0 1px 0 rgba(0,0,0,.2); }
</style>
""", unsafe_allow_html=True)

# ----------------------------- SAFE STATE INIT (PREFIXED) -----------------------------
def _init_weather_state():
    defaults = {
        "weather_round": 1,
        "weather_score": 0,
        "weather_best": 0,
        "weather_seed": random.randint(1, 999999),
        "weather_city": "Bandar Lampung",
        "weather_season": "Rainy",
        "weather_locked": False,
        "weather_controls": {
            "days": 7,
            "humidity": 70,
            "pressure": 1008,
            "wind": 12
        },
        "weather_forecast": [],
        "weather_history": [],
        "weather_guess": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
    # lengkapi keys controls
    for k, v in defaults["weather_controls"].items():
        st.session_state["weather_controls"].setdefault(k, v)

_init_weather_state()

# ----------------------------- UTILS -----------------------------
def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def pct(x, lo, hi):
    if hi <= lo: return 0
    return clamp((x - lo) / (hi - lo) * 100, 0, 100)

def icon_for(cond: str) -> str:
    return {"Clear":"☀️", "Clouds":"⛅", "Rain":"🌧️", "Storm":"⛈️", "Drizzle":"🌦️", "Wind":"💨"}.get(cond, "🌤️")

def comfort_index(temp_c: float, hum: int, wind: int) -> float:
    t = 100 - abs(temp_c - 26) * 4
    h = 100 - abs(hum - 55) * 1.2
    w = 100 - abs(wind - 10) * 3
    return clamp(0.4*t + 0.4*h + 0.2*w, 0, 100)

def trend_label(delta: float) -> str:
    if delta > 1.5: return "naik tajam"
    if delta > 0.4: return "sedikit naik"
    if delta < -1.5: return "turun tajam"
    if delta < -0.4: return "sedikit turun"
    return "stabil"

# ----------------------------- WEATHER MODEL (SIMULASI) -----------------------------
def base_city_temp(city: str, season: str):
    c = city.lower()
    # perkiraan baseline Indonesia sederhana
    base = 29.0
    if "bandung" in c: base = 24.0
    elif "jakarta" in c: base = 30.0
    elif "surabaya" in c: base = 31.0
    elif "bali" in c or "denpasar" in c: base = 30.5
    elif "medan" in c: base = 29.5
    elif "lampung" in c: base = 28.5
    seas = {"Dry": -0.8, "Rainy": -1.2, "Transitional": -0.4}
    return base + seas.get(season, 0.0), 3.5  # mean & volatility

def generate_forecast(seed:int, city:str, season:str, hum:int, pres:int, wind:int, days:int) -> List[Dict]:
    rng = random.Random(seed)
    t_base, vol = base_city_temp(city, season)
    out = []
    last_temp = t_base + rng.uniform(-1.0, 1.0)

    cloud_bias = clamp((hum - 65)/35, -0.5, 1.0) + (0.20 if season=="Rainy" else 0.0)
    rain_bias  = clamp((1008 - pres)/12, -0.2, 1.2) + (0.15 if season=="Rainy" else 0.0)
    wind_bias  = clamp((wind - 10)/20, -0.3, 0.6)

    for d in range(1, days+1):
        drift = rng.uniform(-vol, vol) * 0.55 + wind_bias*0.6 + (hum-60)*0.02
        temp  = clamp(last_temp + drift, 21, 38)
        last_temp = temp

        p_rain = clamp(0.22 + 0.45*rain_bias + 0.2*cloud_bias + rng.uniform(-0.06,0.06), 0.02, 0.92)
        p_storm = clamp(p_rain*0.25 + (pres<1006)*0.08 + (wind>18)*0.07, 0.01, 0.35)
        p_drizzle = clamp((p_rain-0.1)*0.35, 0.0, 0.30)
        p_cloud = clamp(0.25 + 0.4*cloud_bias, 0.05, 0.8)
        p_clear = clamp(1.0 - (p_rain+p_cloud+p_storm+p_drizzle), 0.05, 0.8)

        r = rng.random()
        if r < p_storm:
            cond = "Storm"; rain = rng.uniform(20, 60)
        elif r < p_storm + p_rain:
            cond = "Rain";  rain = rng.uniform(4, 35)
        elif r < p_storm + p_rain + p_drizzle:
            cond = "Drizzle"; rain = rng.uniform(1, 5)
        elif r < p_storm + p_rain + p_drizzle + p_cloud:
            cond = "Clouds";  rain = 0.0
        else:
            cond = "Clear";   rain = 0.0

        wind_d = clamp(int(wind + rng.uniform(-4, 4)), 2, 40)
        pres_d = clamp(int(pres + rng.uniform(-5, 5)), 990, 1025)
        hum_d  = clamp(int(hum + rng.uniform(-10, 8)), 40, 98)

        out.append({
            "day": d,
            "temp": round(temp, 1),
            "cond": cond,
            "rain": round(rain, 1),
            "wind": wind_d,
            "humidity": hum_d,
            "pressure": pres_d,
            "comfort": round(comfort_index(temp, hum_d, wind_d), 1)
        })
    return out

# ----------------------------- RENDER HELPERS -----------------------------
def table_forecast(data: List[Dict]):
    head = "<tr><th>Hari</th><th>Cuaca</th><th>Suhu (°C)</th><th>Hujan (mm)</th><th>Angin (km/j)</th><th>RH (%)</th><th>Tekanan</th><th>Comfort</th></tr>"
    rows = []
    for d in data:
        cls = "class='lightning'" if d["cond"]=="Storm" else ""
        rows.append(
            f"<tr {cls}><td>{d['day']}</td>"
            f"<td>{icon_for(d['cond'])} {d['cond']}</td>"
            f"<td>{d['temp']}</td>"
            f"<td>{d['rain']}</td>"
            f"<td>{d['wind']}</td>"
            f"<td>{d['humidity']}</td>"
            f"<td>{d['pressure']}</td>"
            f"<td>{d['comfort']}</td></tr>"
        )
    st.markdown(f"<table class='table'><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table>", unsafe_allow_html=True)

def bar_row(label:str, value:float, vmin:float, vmax:float, suffix:str=""):
    width = pct(value, vmin, vmax)
    st.markdown(
        f"""
        <div class="barrow">
          <div class="barlabel">{label}</div>
          <div class="bar"><div class="fill" style="width:{width}%;"></div></div>
          <div class="pill">{value}{suffix}</div>
        </div>
        """, unsafe_allow_html=True
    )

def chart_temperatures(data: List[Dict]):
    temps = [d["temp"] for d in data]
    lo, hi = min(temps)-1, max(temps)+1
    st.markdown('<div class="chart">', unsafe_allow_html=True)
    for d in data:
        bar_row(f"D{d['day']} {icon_for(d['cond'])}", d["temp"], lo, hi, "°")
    st.markdown("<div class='legend'><span class='l'><span class='box'></span> Suhu harian</span></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def chart_rain(data: List[Dict]):
    rains = [d["rain"] for d in data]
    hi = max(5.0, max(rains) if rains else 5.0)
    st.markdown('<div class="chart">', unsafe_allow_html=True)
    for d in data:
        bar_row(f"D{d['day']}", d["rain"], 0, hi, "mm")
    st.markdown("<div class='legend'><span class='l'><span class='box2'></span> Curah hujan</span></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def chart_temp_line(data: List[Dict]):
    vals = [d["temp"] for d in data]
    if not vals: return
    mx, mn = max(vals), min(vals)
    nrm = [(v - mn) / (mx - mn + 1e-9) for v in vals]
    html = "<div class='graph'>"
    # titik & segmen garis
    for i in range(len(nrm)-1):
        x1 = i * (100/len(nrm)); x2 = (i+1) * (100/len(nrm))
        y1 = 100 - nrm[i]*100;   y2 = 100 - nrm[i+1]*100
        html += f"<div class='graph-line' style='left:{x1}%; top:{y1}%; width:{x2-x1}%;'></div>"
    for i, v in enumerate(nrm):
        x = i * (100/len(nrm)); y = 100 - v*100
        html += f"<div class='graph-dot' style='left:{x}%; top:{y}%;'></div>"
    # animasi hujan jika dominan
    wet_days = sum(1 for d in data if d["rain"] >= 1.0)
    if wet_days >= (len(data)+1)//2:
        for i in range(25):
            left = random.randint(2, 96)
            delay = random.random()*0.8
            html += f"<div class='raindrop' style='left:{left}%; animation-delay:{delay}s;'></div>"
    html += "</div>"
    st.markdown("<div class='card'><b>📈 Grafik Garis Suhu</b>", unsafe_allow_html=True)
    st.markdown(html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------- INSIGHTS -----------------------------
def compute_insights(data: List[Dict]):
    if not data:
        return {"avg_temp":0,"avg_rain":0,"comfort":0,"vol":0,"wet_days":0,"trend":"stabil"}
    temps = [d["temp"] for d in data]
    rains = [d["rain"] for d in data]
    comfort = [d["comfort"] for d in data]
    avg_t = sum(temps)/len(temps)
    avg_r = sum(rains)/len(rains)
    vol = max(temps)-min(temps)
    trend = temps[-1] - temps[0]
    wet = sum(1 for r in rains if r>=1.0)
    return {"avg_temp":round(avg_t,1),"avg_rain":round(avg_r,1),"comfort":round(sum(comfort)/len(comfort),1),
            "vol":round(vol,1),"wet_days":wet,"trend":trend_label(trend)}

def insight_block(info: Dict, days: int):
    c1,c2,c3,c4 = st.columns(4)
    c1.markdown(f"<div class='metric'><div class='k'>Rata Suhu</div><div class='v'>{info['avg_temp']}°</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric'><div class='k'>Rata Hujan</div><div class='v'>{info['avg_rain']} mm</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric'><div class='k'>Volatilitas</div><div class='v'>{info['vol']}°</div></div>", unsafe_allow_html=True)
    c4.markdown(f"<div class='metric'><div class='k'>Comfort</div><div class='v'>{info['comfort']}</div></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='note'>Tren suhu {info['trend']}. Hari basah (≥1 mm): {info['wet_days']} dari {days} hari.</div>", unsafe_allow_html=True)

# ----------------------------- HEADER -----------------------------
st.markdown("""
<div class="card" style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
  <div>
    <div class="title" style="font-size:28px;">⛅ WeatherForge: <span style="color:#4A67E9">Climate Simulation Lab</span></div>
    <div class="sub">Kreasi I (Bebas) · HMSD Adyatama ITERA 2025</div>
  </div>
  <div class="chip">Elegan · Biru & Emas</div>
</div>
""", unsafe_allow_html=True)

# ----------------------------- SIDEBAR -----------------------------
with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("**Ronde:**", st.session_state.weather_round)
    st.write("**Skor:**", st.session_state.weather_score)
    st.write("**Best:**", st.session_state.weather_best)
    st.markdown("---")
    st.caption("Tebak dominan minggu ini: **Cerah** (hari hujan < setengah) atau **Hujan** (hari hujan ≥ setengah).")
    st.markdown("---")
    if st.button("🔄 Reset Game (Bersih)"):
        for k in [x for x in st.session_state.keys() if x.startswith("weather_")]:
            del st.session_state[k]
        _init_weather_state()
        st.rerun()

# ----------------------------- CONTROLS -----------------------------
with st.expander("⚙️ Pengaturan Simulasi"):
    c1,c2 = st.columns(2)
    with c1:
        st.session_state.weather_city = st.text_input("Kota", st.session_state.weather_city)
        st.session_state.weather_season = st.selectbox("Musim", ["Rainy","Dry","Transitional"], index=["Rainy","Dry","Transitional"].index(st.session_state.weather_season))
    with c2:
        st.session_state.weather_controls["days"] = st.slider("Jumlah Hari", 5, 10, st.session_state.weather_controls.get("days",7))
    c3,c4,c5 = st.columns(3)
    with c3:
        st.session_state.weather_controls["humidity"] = st.slider("Kelembapan (%)", 40, 95, st.session_state.weather_controls["humidity"])
    with c4:
        st.session_state.weather_controls["pressure"] = st.slider("Tekanan (hPa)", 990, 1025, st.session_state.weather_controls["pressure"])
    with c5:
        st.session_state.weather_controls["wind"] = st.slider("Angin (km/j)", 2, 40, st.session_state.weather_controls["wind"])

    if st.button("🔁 Terapkan & Regenerasi"):
        st.session_state.weather_seed = random.randint(1, 999999)
        st.session_state.weather_locked = False

# ----------------------------- SIMULATION PROGRESS (ANIMASI) -----------------------------
with st.expander("▶️ Jalankan Mesin Simulasi"):
    prog = st.progress(0, text="Menyiapkan model …")
    time.sleep(0.18); prog.progress(20, text="Membaca parameter kota & musim …")
    time.sleep(0.16); prog.progress(48, text="Mengestimasi suhu & peluang hujan …")
    time.sleep(0.20); prog.progress(76, text="Merakit visualisasi & laporan …")
    time.sleep(0.17); prog.progress(100, text="Selesai ✅")
    time.sleep(0.04)

# ----------------------------- GENERATE FORECAST -----------------------------
C = st.session_state.weather_controls
forecast = generate_forecast(
    seed=st.session_state.weather_seed + st.session_state.weather_round,
    city=st.session_state.weather_city,
    season=st.session_state.weather_season,
    hum=C["humidity"], pres=C["pressure"], wind=C["wind"], days=C["days"]
)
st.session_state.weather_forecast = forecast

# ----------------------------- DATA TABLE -----------------------------
st.markdown("<div class='card'><div class='title'>📋 Tabel Prakiraan</div>", unsafe_allow_html=True)
table_forecast(forecast)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------- CHARTS -----------------------------
colA, colB = st.columns(2)
with colA:
    st.markdown("<div class='card'><div class='title'>🌡️ Suhu & Tren</div>", unsafe_allow_html=True)
    chart_temperatures(forecast)
    chart_temp_line(forecast)
    st.markdown("</div>", unsafe_allow_html=True)
with colB:
    st.markdown("<div class='card'><div class='title'>🌧️ Curah Hujan</div>", unsafe_allow_html=True)
    chart_rain(forecast)
    info = compute_insights(forecast)
    st.markdown("<div class='title' style='margin-top:8px;'>🔬 Lab Insights</div>", unsafe_allow_html=True)
    insight_block(info, C["days"])
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------- GAMEPLAY: Dominance Guess -----------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='title'>🎯 Challenge: Tebak Kondisi Dominan</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Tentukan apakah **HUJAN DOMINAN** (jumlah hari hujan ≥ setengah) atau **CERAH DOMINAN** (sebaliknya) minggu ini.</div>", unsafe_allow_html=True)

guess = st.radio("Pilihanmu:", ["Cerah Dominan ☀️", "Hujan Dominan 🌧️"], index=0, key="weather_guess", horizontal=True)
c1, c2 = st.columns(2)
with c1:
    lock = st.button("Kunci Jawaban 🚀", disabled=st.session_state.weather_locked)
with c2:
    next_round = st.button("Lanjut Ronde Berikutnya 🔁")

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------- SCORING -----------------------------
if lock and not st.session_state.weather_locked:
    wet_days = sum(1 for d in forecast if d["rain"] >= 1.0)
    is_rain_dominant = wet_days >= (len(forecast)+1)//2
    user_pick_rain = guess.startswith("Hujan")
    correct = (is_rain_dominant == user_pick_rain)
    before = st.session_state.weather_score

    if correct:
        st.session_state.weather_score += 10
        st.balloons()
        st.markdown("<div class='badge ok'>✅ Jawaban tepat! +10</div>", unsafe_allow_html=True)
    else:
        st.session_state.weather_score -= 5
        st.markdown(f"<div class='badge err'>❌ Kurang tepat (-5). Fakta: Hari hujan = {wet_days} dari {len(forecast)} hari.</div>", unsafe_allow_html=True)

    st.session_state.weather_best = max(st.session_state.weather_best, st.session_state.weather_score)
    st.session_state.weather_history.append({
        "round": st.session_state.weather_round,
        "score_before": before,
        "score_after": st.session_state.weather_score,
        "rain_days": wet_days,
        "days": len(forecast),
        "dominant": "Hujan" if is_rain_dominant else "Cerah"
    })
    st.session_state.weather_locked = True

if next_round:
    st.session_state.weather_round += 1
    st.session_state.weather_seed = random.randint(1, 999999)
    st.session_state.weather_locked = False
    st.rerun()

# ----------------------------- HISTORY / LEADERBOARD -----------------------------
with st.expander("🏅 Riwayat & Leaderboard (Sesi Ini)"):
    hist = st.session_state.weather_history
    if not hist:
        st.info("Belum ada riwayat permainan. Kunci satu ronde dulu.")
    else:
        head = "<tr><th>Ronde</th><th>Dominan</th><th>Hari Hujan</th><th>Skor</th></tr>"
        rows = []
        for h in hist:
            rows.append(
                f"<tr><td>{h['round']}</td>"
                f"<td>{h['dominant']}</td>"
                f"<td>{h['rain_days']}/{h['days']}</td>"
                f"<td>{h['score_before']} → <b>{h['score_after']}</b></td></tr>"
            )
        st.markdown(f"<table class='table'><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table>", unsafe_allow_html=True)
        st.markdown(f"<div class='note'>Skor terbaik sesi ini: <b>{st.session_state.weather_best}</b>.</div>", unsafe_allow_html=True)

# ----------------------------- FOOTER -----------------------------
st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
st.caption("Model simulasi edukatif (bukan data real). Elegan biru–emas, animasi hujan & lightning, grafik HTML/CSS. • © 2025 Kelompok ANOVA HMSD Adyatama.")
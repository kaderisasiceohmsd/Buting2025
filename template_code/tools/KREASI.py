# ==============================================
# WeatherForge: Forecast Lab (No external deps)
# Theme: Elegan (Light-Blue + Gold), Animations, Lab Report
# Features:
# - Pseudo-random forecast generator (7 days) based on city + season + sliders
# - HTML/CSS charts for temperature & precipitation
# - Challenge Mode: guess rainy days -> Score + Leaderboard (session)
# - Simulation progress (loading steps)
# - Lab insights (trends, volatility, comfort index)
# - No numpy/pandas/matplotlib
# ==============================================

import streamlit as st
import random
import time
from typing import List, Dict, Tuple

# -----------------------------
# PAGE CONFIG & THEME
# -----------------------------
st.set_page_config(
    page_title="WeatherForge: Forecast Lab",
    page_icon="⛅",
    layout="centered",
)

THEME_CSS = """
<style>
:root{
  --bg-soft: #EAF4FB;
  --panel: #FFFFFF;
  --panel-soft: #F7FBFF;
  --gold: #DCCCA3;
  --gold2:#CBB279;
  --ink:#1F2937;
  --muted:#6B7280;
  --blue:#4A67E9;
  --ok:#16a34a;
  --warn:#ca8a04;
  --err:#dc2626;
}
html, body, [data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg, var(--bg-soft), #FFFFFF 60%);
}
section.main > div.block-container{ padding-top:1.1rem; }

.card{
  background:var(--panel);
  border:1px solid rgba(0,0,0,.05);
  border-radius:16px;
  box-shadow:0 14px 36px rgba(20,35,70,.06);
  padding:18px 20px;
}
.title{ font-weight:900; color:var(--ink); letter-spacing:.3px; }
.sub{ color:var(--muted); font-weight:500; }
.chip{
  display:inline-flex; align-items:center; gap:8px;
  padding:6px 12px; background:var(--gold); color:#111;
  border-radius:999px; font-weight:800;
}
.hr{ height:1px; background:rgba(0,0,0,.08); margin:14px 0; }

.metric{
  display:flex; flex-direction:column; gap:4px; padding:12px 14px; border-radius:12px;
  background:var(--panel-soft); border:1px solid rgba(0,0,0,.06);
}
.metric .k{ font-size:13px; color:var(--muted); font-weight:600; }
.metric .v{ font-size:22px; font-weight:900; color:var(--ink); }

.badge{ display:inline-flex; align-items:center; gap:6px; font-weight:800; border-radius:12px; padding:6px 10px; }
.badge.ok{ background:#dcfce7; color:#065f46; }
.badge.warn{ background:#fef9c3; color:#854d0e; }
.badge.err{ background:#fee2e2; color:#7f1d1d; }

.kbd{ border:1px solid rgba(0,0,0,.15); border-bottom-width:3px; border-radius:8px; padding:2px 6px; background:#fff; font-weight:800; }

.table{
  width:100%; border-collapse:separate; border-spacing:0; background:#fff; overflow:hidden; border-radius:12px;
  border:1px solid rgba(0,0,0,.06);
}
.table thead tr{ background:#f3f4f6; }
.table th,.table td{ padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06); text-align:center; font-size:13px; }
.table tr:last-child td{ border-bottom:none; }

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
.fill{
  height:100%; border-radius:9px; background: linear-gradient(90deg, var(--blue), #7EA3FF);
  width:0%;
}
.pill{
  display:inline-flex; align-items:center; gap:8px; padding:6px 10px; border-radius:999px; background:#eef2ff; color:#1e3a8a; border:1px solid rgba(37,99,235,.25); font-weight:800;
}

.legend{ display:flex; gap:10px; flex-wrap:wrap; }
.legend .l{ display:flex; align-items:center; gap:6px; font-size:12px; color:#374151; }
.legend .box{ width:12px; height:12px; border-radius:3px; background: var(--blue); box-shadow: 0 1px 0 rgba(0,0,0,.2); }

.tag{
  display:inline-flex; align-items:center; gap:6px; padding:4px 8px; border:1px solid rgba(0,0,0,.08);
  border-radius:8px; font-weight:700; background:#fff;
}
.note{ color:#6b7280; font-size:12px; }

.alert{
  border:1px solid rgba(0,0,0,.08); background:#fff; padding:12px 14px; border-radius:12px;
}
</style>
"""
st.markdown(THEME_CSS, unsafe_allow_html=True)

# -----------------------------
# STATE
# -----------------------------
def _init():
    ss = st.session_state
    ss.setdefault("round", 1)
    ss.setdefault("score", 0)
    ss.setdefault("best", 0)
    ss.setdefault("seed", random.randint(1, 10_000))
    ss.setdefault("history", [])
    ss.setdefault("city", "Bandar Lampung")
    ss.setdefault("season", "Rainy")
    ss.setdefault("controls", {
        "humidity": 70,
        "pressure": 1008,
        "wind": 12,
        "days": 7
    })
    ss.setdefault("forecast", [])
    ss.setdefault("insight", "")
    ss.setdefault("guess", [])
    ss.setdefault("last_feedback", "")
    ss.setdefault("challenge_locked", False)

_init()

# -----------------------------
# UTILS
# -----------------------------
def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def pct(x, lo, hi):
    if hi<=lo: return 0
    v = (x-lo)/(hi-lo)
    return clamp(v*100, 0, 100)

def icon_for(cond:str)->str:
    return {
        "Clear":"☀️", "Clouds":"⛅", "Rain":"🌧️", "Storm":"⛈️", "Drizzle":"🌦️", "Wind":"💨"
    }.get(cond, "🌤️")

def comfort_index(temp_c:float, hum:int, wind:int)->float:
    # naive comfort score (0..100): closer to 26C with medium humidity/wind is nicer
    t_score = 100 - abs(temp_c - 26)*4
    h_score = 100 - abs(hum - 55)*1.2
    w_score = 100 - abs(wind - 10)*3
    return clamp(0.4*t_score + 0.4*h_score + 0.2*w_score, 0, 100)

def trend_label(delta:float)->str:
    if delta > 1.5: return "meningkat tajam"
    if delta > 0.4: return "sedikit meningkat"
    if delta < -1.5: return "menurun tajam"
    if delta < -0.4: return "sedikit menurun"
    return "stabil"

# -----------------------------
# CORE: WEATHER MODEL
# -----------------------------
def base_city_temp(city:str, season:str)->Tuple[float,float]:
    city = city.lower()
    # baseline city (approx) for Indonesia climates
    if "bandar" in city or "lampung" in city: base = 28.0
    elif "jakarta" in city: base = 30.0
    elif "bandung" in city: base = 24.0
    elif "yogyakarta" in city or "jogja" in city: base = 29.0
    elif "surabaya" in city: base = 31.0
    elif "medan" in city: base = 29.5
    elif "bali" in city or "denpasar" in city: base = 30.0
    else: base = 29.0
    # season adjustment
    seas = {"Dry": -0.8, "Rainy": -1.2, "Transitional": -0.4}
    s_adj = seas.get(season, 0.0)
    return base + s_adj, 3.5  # mean, day-to-day volatility scale

def make_rng(seed:int):
    return random.Random(seed)

def generate_forecast(seed:int, city:str, season:str, hum:int, pres:int, wind:int, days:int)->List[Dict]:
    """
    Create 7-day forecast. Fields:
      day, temp, cond, rain_mm, wind, humidity, pressure, comfort
    """
    rng = make_rng(seed)
    t_base, vol = base_city_temp(city, season)
    out = []
    cloud_bias = clamp((hum - 65)/35, -0.5, 1.0) + (0.2 if season=="Rainy" else 0.0)
    rain_bias = clamp((1008 - pres)/12, -0.2, 1.2) + (0.15 if season=="Rainy" else 0.0)
    wind_bias = clamp((wind - 10)/20, -0.3, 0.6)

    last_temp = t_base + rng.uniform(-1.0, 1.0)
    for d in range(1, days+1):
        # random walk temp with seasonality and wind/hum effects
        drift = rng.uniform(-vol, vol) * 0.55 + wind_bias*0.6 + (hum-60)*0.02
        temp = last_temp + drift
        temp = clamp(temp, 21, 38)
        last_temp = temp

        # condition probability
        p_rain = clamp(0.20 + 0.45*rain_bias + 0.2*cloud_bias + rng.uniform(-0.06,0.06), 0.02, 0.92)
        p_storm = clamp(p_rain*0.25 + (pres<1006)*0.08 + (wind>18)*0.07, 0.01, 0.35)
        p_drizzle = clamp((p_rain-0.1)*0.35, 0.0, 0.3)
        p_cloud = clamp(0.25 + 0.4*cloud_bias, 0.05, 0.8)
        p_clear = clamp(1.0 - (p_rain+p_cloud+p_storm+p_drizzle), 0.05, 0.8)

        r = rng.random()
        if r < p_storm:
            cond = "Storm"
            rain = rng.uniform(20, 60)
        elif r < p_storm + p_rain:
            cond = "Rain"
            rain = rng.uniform(4, 35)
        elif r < p_storm + p_rain + p_drizzle:
            cond = "Drizzle"
            rain = rng.uniform(1, 5)
        elif r < p_storm + p_rain + p_drizzle + p_cloud:
            cond = "Clouds"
            rain = 0.0
        else:
            cond = "Clear"
            rain = 0.0

        # wind & pressure small jitter
        wind_d = clamp(int(wind + rng.uniform(-4, 4)), 2, 40)
        pres_d = clamp(int(pres + rng.uniform(-5, 5)), 990, 1025)
        hum_d = clamp(int(hum + rng.uniform(-10, 8)), 40, 98)

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

# -----------------------------
# CHART RENDER (HTML/CSS)
# -----------------------------
def table_forecast(data:List[Dict]):
    head = "<tr><th>Hari</th><th>Cuaca</th><th>Suhu (°C)</th><th>Hujan (mm)</th><th>Angin (km/j)</th><th>RH (%)</th><th>Tekanan (hPa)</th><th>Comfort</th></tr>"
    rows = []
    for d in data:
        rows.append(
            f"<tr><td>{d['day']}</td>"
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
    color = "linear-gradient(90deg, var(--blue), #7EA3FF)"
    st.markdown(
        f"""
        <div class="barrow">
          <div class="barlabel">{label}</div>
          <div class="bar"><div class="fill" style="width:{width}%; background:{color};"></div></div>
          <div class="pill">{value}{suffix}</div>
        </div>
        """, unsafe_allow_html=True
    )

def chart_temperatures(data:List[Dict]):
    temps = [d["temp"] for d in data]
    lo, hi = min(temps)-1, max(temps)+1
    st.markdown('<div class="chart">', unsafe_allow_html=True)
    for d in data:
        bar_row(f"D{d['day']} {icon_for(d['cond'])}", d["temp"], lo, hi, "°")
    st.markdown("<div class='legend'><span class='l'><span class='box'></span> Suhu harian</span></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def chart_rain(data:List[Dict]):
    rains = [d["rain"] for d in data]
    hi = max(5.0, max(rains) if rains else 5.0)
    st.markdown('<div class="chart">', unsafe_allow_html=True)
    for d in data:
        bar_row(f"D{d['day']}", d["rain"], 0, hi, "mm")
    st.markdown("<div class='legend'><span class='l'><span class='box'></span> Curah hujan</span></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# INSIGHTS (Lab-style)
# -----------------------------
def compute_insights(data:List[Dict])->Dict:
    temps = [d["temp"] for d in data]
    rains = [d["rain"] for d in data]
    comfort = [d["comfort"] for d in data]
    avg_t = sum(temps)/len(temps)
    avg_r = sum(rains)/len(rains)
    trend = temps[-1] - temps[0]
    volatility = max(temps) - min(temps)
    comfort_avg = sum(comfort)/len(comfort)
    wet_days = sum(1 for x in rains if x >= 1.0)
    return {
        "avg_temp": round(avg_t,1),
        "avg_rain": round(avg_r,1),
        "trend_text": trend_label(trend),
        "volatility": round(volatility,1),
        "comfort_avg": round(comfort_avg,1),
        "wet_days": wet_days
    }

def insight_block(ins:Dict):
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        st.markdown(f"<div class='metric'><div class='k'>Rata-rata Suhu</div><div class='v'>{ins['avg_temp']}°C</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric'><div class='k'>Rata-rata Hujan</div><div class='v'>{ins['avg_rain']} mm</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric'><div class='k'>Volatilitas Suhu</div><div class='v'>{ins['volatility']}°</div></div>", unsafe_allow_html=True)
    with c4:
        st.markdown(f"<div class='metric'><div class='k'>Comfort Index</div><div class='v'>{ins['comfort_avg']}</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
    note = f"Tren suhu {ins['trend_text']}. Perkiraan hari basah (≥1 mm): {ins['wet_days']} hari."
    st.markdown(f"<div class='note'>{note}</div>", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    """
    <div class="card" style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
      <div>
        <div class="title" style="font-size:28px;">⛅ WeatherForge: <span style="color:#4A67E9">Forecast Lab</span></div>
        <div class="sub">Kreasi I (Bebas) · HMSD Adyatama ITERA 2025</div>
      </div>
      <div class="chip">Elegan · Biru & Emas</div>
    </div>
    """, unsafe_allow_html=True
)

# -----------------------------
# SIDEBAR: Scoreboard & Reset
# -----------------------------
with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("**Ronde:**", st.session_state.round)
    st.write("**Skor:**", st.session_state.score)
    if st.session_state.history:
        best = max(h["score_after"] for h in st.session_state.history)
        st.session_state.best = best
    st.write("**Best (sesi):**", st.session_state.best)
    st.markdown("---")
    st.markdown("**Cara main (Challenge Mode):**")
    st.caption("Tandai hari yang menurutmu bakalan HUJAN (≥1 mm). Skor +10 jika tepat semua, -5 jika meleset.")
    st.markdown("---")
    if st.button("🔄 Reset Game"):
        st.session_state.round = 1
        st.session_state.score = 0
        st.session_state.best = 0
        st.session_state.history.clear()
        st.session_state.seed = random.randint(1,10_000)
        st.session_state.challenge_locked = False
        st.rerun()

# -----------------------------
# CONTROLS
# -----------------------------
with st.expander("⚙️ Pengaturan Simulasi"):
    c1, c2 = st.columns([1,1])
    with c1:
        st.session_state.city = st.text_input("Kota", st.session_state.city)
        st.session_state.season = st.selectbox("Musim", ["Rainy", "Dry", "Transitional"], index=["Rainy","Dry","Transitional"].index(st.session_state.season))
    with c2:
        st.session_state.controls["days"] = st.slider("Jumlah Hari", 5, 10, st.session_state.controls["days"])
    c3, c4, c5 = st.columns(3)
    with c3:
        st.session_state.controls["humidity"] = st.slider("Kelembapan (%)", 40, 95, st.session_state.controls["humidity"])
    with c4:
        st.session_state.controls["pressure"] = st.slider("Tekanan (hPa)", 990, 1025, st.session_state.controls["pressure"])
    with c5:
        st.session_state.controls["wind"] = st.slider("Angin (km/j)", 2, 40, st.session_state.controls["wind"])

    if st.button("Terapkan & Bangkitkan Prakiraan 🔁"):
        st.session_state.seed = random.randint(1,10_000)
        st.session_state.challenge_locked = False

# -----------------------------
# SIMULATION PROGRESS
# -----------------------------
with st.expander("▶️ Jalankan Mesin Prakiraan"):
    prog = st.progress(0, text="Menyiapkan model …")
    time.sleep(0.2)
    prog.progress(25, text="Membaca parameter kota & musim …")
    time.sleep(0.18)
    prog.progress(55, text="Mengestimasi suhu & peluang hujan …")
    time.sleep(0.22)
    prog.progress(80, text="Merakit laporan & visual …")
    time.sleep(0.18)
    prog.progress(100, text="Selesai ✅")
    time.sleep(0.05)

# -----------------------------
# GENERATE FORECAST
# -----------------------------
d = st.session_state.controls
forecast = generate_forecast(
    seed=st.session_state.seed + st.session_state.round,
    city=st.session_state.city,
    season=st.session_state.season,
    hum=d["humidity"],
    pres=d["pressure"],
    wind=d["wind"],
    days=d["days"]
)
st.session_state.forecast = forecast

# -----------------------------
# SHOW TABLE & CHARTS
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(f"<div class='title'>📋 Prakiraan {st.session_state.city} – {st.session_state.season}</div>", unsafe_allow_html=True)
table_forecast(forecast)
st.markdown('</div>', unsafe_allow_html=True)

cA, cB = st.columns(2)
with cA:
    st.markdown("<div class='card'><div class='title'>🌡️ Suhu Harian</div>", unsafe_allow_html=True)
    chart_temperatures(forecast)
    st.markdown("</div>", unsafe_allow_html=True)
with cB:
    st.markdown("<div class='card'><div class='title'>🌧️ Curah Hujan</div>", unsafe_allow_html=True)
    chart_rain(forecast)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# INSIGHTS
# -----------------------------
ins = compute_insights(forecast)
st.markdown("<div class='card'><div class='title'>🔬 Lab Insights</div>", unsafe_allow_html=True)
insight_block(ins)
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# CHALLENGE MODE (Guess Rainy Days)
# -----------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='title'>🎯 Challenge Mode: Tebak Hari Hujan</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Tandai hari yang kamu prediksi akan HUJAN (≥1 mm). Kunci jawaban untuk menilai skor.</div>", unsafe_allow_html=True)

days = [f"D{d['day']}" for d in forecast]
defaults = [False]*len(days) if not st.session_state.guess else st.session_state.guess
guess = []
cols = st.columns(min(7, len(days)))
for i, day in enumerate(days):
    with cols[i % len(cols)]:
        val = st.checkbox(day, value=defaults[i] if i < len(defaults) else False, key=f"cb_{i}", disabled=st.session_state.challenge_locked)
        guess.append(val)

st.session_state.guess = guess

c1, c2 = st.columns([1,1])
with c1:
    lock = st.button("Kunci Jawaban 🚀", disabled=st.session_state.challenge_locked)
with c2:
    next_round = st.button("Lanjut Ronde Berikutnya 🔁")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# SCORING
# -----------------------------
if lock and not st.session_state.challenge_locked:
    truth = [d["rain"] >= 1.0 for d in forecast]
    correct = (truth == guess)
    before = st.session_state.score
    if correct:
        st.session_state.score += 10
        st.session_state.last_feedback = "✅ Keren! Semua tebakan hari hujan tepat."
        st.balloons()
        badge = '<span class="badge ok">Benar · +10</span>'
    else:
        st.session_state.score -= 5
        # ringkas info selisih
        miss_idx = [i+1 for i,(t,g) in enumerate(zip(truth,guess)) if t!=g]
        st.session_state.last_feedback = f"❌ Ada selisih di hari: {', '.join('D'+str(x) for x in miss_idx)}"
        badge = '<span class="badge err">Salah · -5</span>'

    st.session_state.history.append({
        "round": st.session_state.round,
        "city": st.session_state.city,
        "season": st.session_state.season,
        "score_before": before,
        "score_after": st.session_state.score,
        "humid": d["humidity"], "press": d["pressure"], "wind": d["wind"],
        "days": d["days"],
        "correct": correct
    })
    st.session_state.challenge_locked = True

    st.markdown(f"<div class='alert'>{badge} &nbsp; {st.session_state.last_feedback}</div>", unsafe_allow_html=True)

if next_round:
    st.session_state.round += 1
    st.session_state.seed = random.randint(1,10_000)
    st.session_state.challenge_locked = False
    st.session_state.guess = []
    st.rerun()

# -----------------------------
# HISTORY / LEADERBOARD
# -----------------------------
with st.expander("🏅 Riwayat & Leaderboard (Sesi)"):
    if not st.session_state.history:
        st.info("Belum ada riwayat.")
    else:
        head = "<tr><th>Ronde</th><th>Kota</th><th>Musim</th><th>Benar?</th><th>Skor</th><th>Param</th></tr>"
        rows = []
        for h in st.session_state.history:
            ok = "✅" if h["correct"] else "❌"
            par = f"RH {h['humid']}% · P {h['press']} hPa · W {h['wind']} km/j"
            rows.append(
                f"<tr><td>{h['round']}</td><td>{h['city']}</td><td>{h['season']}</td>"
                f"<td style='font-weight:800'>{ok}</td>"
                f"<td>{h['score_before']} → <b>{h['score_after']}</b></td>"
                f"<td>{par}</td></tr>"
            )
        st.markdown(f"<table class='table'><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table>", unsafe_allow_html=True)
        top = max(h["score_after"] for h in st.session_state.history)
        st.markdown(f"<div class='note'>Skor terbaik sesi ini: <b>{top}</b></div>", unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
st.caption("Model ini bersifat simulatif (bukan data nyata). Gunakan untuk edukasi interaktif dan demonstrasi UI/UX statistik.")

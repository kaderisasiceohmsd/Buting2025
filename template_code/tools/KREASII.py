# =========================
# ANOVA ODYSSEY – EXPERT EDITION (no external deps)
# Theme: Elegant ANOVA (light-blue + gold)
# Animations: progress bar, balloons, soft transitions
# Logic: Full one-way ANOVA (manual), F-critical lookup (alpha=0.05)
# Visuals: HTML/CSS 'charts' (means & variances), data table, lab-style report
# Gameplay: prediction (significant or not), scoring, rounds, session leaderboard
# =========================

import streamlit as st
import random
import time
import math
import statistics
from typing import List, Dict, Tuple

# -------------------------
# PAGE CONFIG & THEME CSS
# -------------------------
st.set_page_config(
    page_title="ANOVA Odyssey – Expert Edition",
    page_icon="⚔️",
    layout="centered",
)

THEME_CSS = """
<style>
:root{
  --bg-soft: #EAF4FB;         /* light blue */
  --bg-panel: #F7FBFF;        /* softer panel */
  --gold: #DCCCA3;            /* cream-gold */
  --gold-deep:#CBB279;        /* deeper gold */
  --ink:#1F2937;              /* slate-900 */
  --muted:#6B7280;            /* slate-500 */
  --ok:#16a34a;
  --warn:#ca8a04;
  --err:#dc2626;
  --ring:#4A67E9;             /* your site primary blue */
  --card:#ffffff;
}
html, body, [data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg, var(--bg-soft), #FFFFFF 60%);
}
section.main > div.block-container{
  padding-top: 1.2rem;
}
.el-card{
  background: var(--card);
  border: 1px solid rgba(0,0,0,0.04);
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(10,30,60,0.06);
  padding: 18px 20px;
}
.el-title{
  font-weight: 800; color: var(--ink); letter-spacing:.3px;
}
.el-sub{ color: var(--muted); font-weight:500; }
.el-chip{
  display:inline-flex; align-items:center; gap:8px;
  background: var(--gold); color:#1b1b1b;
  border-radius: 999px; padding: 6px 12px; font-weight: 700;
}
.hr-soft{ height:1px; background:rgba(0,0,0,.06); margin:14px 0; }
.kbd{
  border:1px solid rgba(0,0,0,.15); border-bottom-width:3px;
  font-weight:700; border-radius:8px; padding:2px 6px; background:#fff;
}
.badge{
  display:inline-flex; align-items:center; gap:6px; font-weight:700;
  border-radius:12px; padding:6px 10px;
}
.badge.ok{ background:#dcfce7; color:#065f46; }
.badge.warn{ background:#fef9c3; color:#854d0e; }
.badge.err{ background:#fee2e2; color:#7f1d1d; }
.metric{
  display:flex; flex-direction:column; gap:4px; padding:12px 14px; border-radius:12px;
  background:var(--bg-panel); border:1px solid rgba(0,0,0,.06);
}
.metric .k{ font-size:14px; color:var(--muted); font-weight:600; }
.metric .v{ font-size:22px; font-weight:900; color:var(--ink); }

.chart-box{
  border:1px dashed rgba(0,0,0,.12); padding:14px; border-radius:14px; background:#fff;
}
.bar-wrap{
  display:grid; gap:8px;
}
.bar-row{
  display:flex; align-items:center; gap:10px;
}
.bar-label{
  min-width:60px; font-weight:800; color:#111827;
}
.bar{
  flex:1; height:18px; border-radius:9px; position:relative;
  background:linear-gradient(90deg, var(--gold), var(--gold-deep));
  box-shadow: inset 0 0 0 2px rgba(0,0,0,.06);
}
.bar::after{
  content:""; position:absolute; inset:0; border-radius:9px;
  box-shadow: inset 0 8px 12px rgba(255,255,255,.35);
}
.bar-fill{
  height:100%; border-radius:9px; background: linear-gradient(90deg, #4A67E9, #7EA3FF);
  width:0%;
}
.mean-pill{
  display:inline-flex; align-items:center; gap:10px;
  background:#eef2ff; color:#1e3a8a; padding:6px 10px; border-radius:999px; font-weight:700;
  border:1px solid rgba(37,99,235,.25);
}
table.simple {
  width:100%; border-collapse:collapse; background:#fff; border-radius:10px; overflow:hidden;
  border:1px solid rgba(0,0,0,.06);
}
table.simple thead tr{ background:#f3f4f6; }
table.simple th, table.simple td{
  padding:8px 10px; border-bottom:1px solid rgba(0,0,0,.06); text-align:center;
  font-size:13px;
}
table.simple tr:last-child td{ border-bottom:none; }
.footer-note{
  color:var(--muted); font-size:12px; line-height:1.5; margin-top:6px;
}
.a11y{
  font-size:0; height:0; width:0; overflow:hidden; position:absolute; left:-9999px;
}
</style>
"""
st.markdown(THEME_CSS, unsafe_allow_html=True)

# -------------------------
# SESSION STATE
# -------------------------
def init_state():
    ss = st.session_state
    ss.setdefault("round", 1)
    ss.setdefault("score", 0)
    ss.setdefault("best_score", 0)
    ss.setdefault("history", [])         # list of dict per round
    ss.setdefault("seed", random.randint(1, 10_000))
    ss.setdefault("last_feedback", "")
    ss.setdefault("user_guess", None)
    ss.setdefault("controls", {
        "k": 3,                   # groups
        "n": 6,                   # per-group size
        "effect": 0.8,            # 0..2 scale
        "alpha": 0.05,
        "round_name": "Ronde"
    })

init_state()

# -------------------------
# F-CRITICAL LOOKUP TABLE
# alpha = 0.05; df1 in 1..5 (k-1 up to 6 groups), df2 in 3..200 (approx; we trim)
# values approximated (standard table), enough for teaching/game
# -------------------------
# For simplicity we keep an excerpt; we will interpolate/extrapolate crudely for higher df2.
F_CRIT_005 = {
    1:  {3:10.13, 4:7.71, 5:6.61, 6:5.99, 7:5.59, 8:5.32, 9:5.12, 10:4.96, 12:4.75, 15:4.54, 20:4.35, 24:4.26, 30:4.17, 40:4.08, 60:4.00, 120:3.92, 200:3.89},
    2:  {3:9.55, 4:6.94, 5:5.79, 6:5.14, 7:4.74, 8:4.46, 9:4.26, 10:4.10, 12:3.89, 15:3.68, 20:3.49, 24:3.39, 30:3.32, 40:3.23, 60:3.15, 120:3.07, 200:3.04},
    3:  {3:9.28, 4:6.59, 5:5.41, 6:4.76, 7:4.35, 8:4.07, 9:3.86, 10:3.71, 12:3.49, 15:3.29, 20:3.10, 24:3.00, 30:2.92, 40:2.84, 60:2.76, 120:2.68, 200:2.65},
    4:  {3:9.12, 4:6.39, 5:5.19, 6:4.53, 7:4.12, 8:3.84, 9:3.63, 10:3.48, 12:3.26, 15:3.06, 20:2.87, 24:2.77, 30:2.69, 40:2.61, 60:2.53, 120:2.45, 200:2.42},
    5:  {3:9.01, 4:6.26, 5:5.05, 6:4.39, 7:3.97, 8:3.69, 9:3.48, 10:3.33, 12:3.11, 15:2.91, 20:2.72, 24:2.62, 30:2.54, 40:2.46, 60:2.38, 120:2.30, 200:2.27},
}

def interp_fcrit(df1:int, df2:int, table:Dict[int,Dict[int,float]])->float:
    """Bilinear-ish interpolation over df2 breakpoints for given df1.
       Clamp to table edges if out of range."""
    df1 = max(min(df1, max(table.keys())), min(table.keys()))
    points = table[df1]
    keys = sorted(points.keys())
    if df2 <= keys[0]:
        return points[keys[0]]
    if df2 >= keys[-1]:
        return points[keys[-1]]
    # find span
    lo = max([k for k in keys if k <= df2])
    hi = min([k for k in keys if k >= df2])
    if lo == hi:
        return points[lo]
    # linear interpolate
    x0, y0 = lo, points[lo]
    x1, y1 = hi, points[hi]
    t = (df2 - x0) / (x1 - x0)
    return y0 + t*(y1 - y0)

# -------------------------
# DATA GENERATION
# -------------------------
def generate_groups(k:int, n:int, effect:float, seed:int)->Dict[str,List[float]]:
    """Generate k groups each with n samples; effect controls separation of means.
       Use only python's random (no numpy)."""
    rnd = random.Random(seed)
    base = rnd.uniform(55, 65)
    groups = {}
    for gi in range(k):
        # mean offset spreads with 'effect'
        mean_shift = (gi - (k-1)/2.0) * (5.0 * effect) + rnd.uniform(-1.0, 1.0)
        true_mean = base + mean_shift
        # within variation about 6 ± 2 scaled mildly by effect
        within_sd = max(2.5, 6.0 - 1.2*effect + rnd.uniform(-1.0,1.0))
        data = [rnd.gauss(true_mean, within_sd) for _ in range(n)]
        groups[chr(65+gi)] = data
    return groups

# -------------------------
# ANOVA CORE (manual)
# -------------------------
def anova_oneway(groups:Dict[str,List[float]])->Dict[str,float]:
    k = len(groups)
    n = len(next(iter(groups.values())))
    totals = {g: sum(vals) for g,vals in groups.items()}
    ns = {g: len(vals) for g,vals in groups.items()}
    means = {g: (totals[g]/ns[g]) for g in groups}
    all_vals = [x for v in groups.values() for x in v]
    grand_mean = sum(all_vals) / len(all_vals)

    # SSB, SSW, SST
    ss_between = sum(ns[g] * (means[g] - grand_mean)**2 for g in groups)
    ss_within  = sum(sum((x - means[g])**2 for x in groups[g]) for g in groups)
    ss_total   = ss_between + ss_within

    df_between = k - 1
    df_within  = k*(n-1)
    df_total   = df_between + df_within

    ms_between = ss_between / df_between if df_between > 0 else float('nan')
    ms_within  = ss_within  / df_within  if df_within  > 0 else float('nan')
    F = (ms_between / ms_within) if ms_within > 0 else float('inf')

    # simple eta-squared effect size
    eta2 = ss_between / ss_total if ss_total > 0 else 0.0

    return {
        "k": k, "n": n,
        "grand_mean": grand_mean,
        "ssb": ss_between, "ssw": ss_within, "sst": ss_total,
        "dfb": df_between, "dfw": df_within, "dft": df_total,
        "msb": ms_between, "msw": ms_within, "F": F,
        "eta2": eta2,
        "means": means
    }

# -------------------------
# RENDER HELPERS
# -------------------------
def fmt(x:float, p:int=2)->str:
    return f"{x:.{p}f}"

def render_data_table(groups:Dict[str,List[float]]):
    # custom html table to avoid pandas
    labels = list(groups.keys())
    rows = max(len(v) for v in groups.values())
    html = ['<table class="simple"><thead><tr><th>No</th>']
    for g in labels:
        html.append(f"<th>Kelompok {g}</th>")
    html.append("</tr></thead><tbody>")
    for i in range(rows):
        html.append(f"<tr><td>{i+1}</td>")
        for g in labels:
            val = groups[g][i] if i < len(groups[g]) else ""
            html.append(f"<td>{fmt(val)}</td>")
        html.append("</tr>")
    html.append("</tbody></table>")
    st.markdown("".join(html), unsafe_allow_html=True)

def bar_row(label:str, value:float, vmax:float):
    pct = 0 if vmax<=0 else max(0.0, min(100.0, (value / vmax) * 100.0))
    st.markdown(
        f"""
        <div class="bar-row">
          <div class="bar-label">{label}</div>
          <div class="bar">
            <div class="bar-fill" style="width:{pct}%;"></div>
          </div>
          <div class="mean-pill">{fmt(value)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_means_chart(means:Dict[str,float]):
    vmax = max(means.values()) if means else 1
    vmin = min(means.values()) if means else 0
    span = max(1.0, vmax - vmin)
    st.markdown('<div class="chart-box"><div class="bar-wrap">', unsafe_allow_html=True)
    for g, m in sorted(means.items()):
        bar_row(f"Mean {g}", m - (vmin - 0.1*span), span*1.2)   # shift to keep >0 width visually
    st.markdown('</div></div>', unsafe_allow_html=True)

def render_var_chart(groups:Dict[str,List[float]]):
    variances = {}
    for g, vals in groups.items():
        try:
            variances[g] = statistics.pvariance(vals)  # population variance
        except statistics.StatisticsError:
            variances[g] = 0.0
    vmax = max(variances.values()) if variances else 1
    st.markdown('<div class="chart-box"><div class="bar-wrap">', unsafe_allow_html=True)
    for g, v in sorted(variances.items()):
        bar_row(f"Var {g}", v, vmax if vmax>0 else 1.0)
    st.markdown('</div></div>', unsafe_allow_html=True)

def lab_report(anv:Dict[str,float], alpha:float, decision:str, note:str):
    k, n = anv["k"], anv["n"]
    means = anv["means"]
    cols = st.columns(3)
    with cols[0]:
        st.markdown('<div class="metric"><div class="k">Kelompok</div><div class="v">{}</div></div>'.format(k), unsafe_allow_html=True)
    with cols[1]:
        st.markdown('<div class="metric"><div class="k">Sampel/Kelompok</div><div class="v">{}</div></div>'.format(n), unsafe_allow_html=True)
    with cols[2]:
        st.markdown('<div class="metric"><div class="k">Grand Mean</div><div class="v">{}</div></div>'.format(fmt(anv["grand_mean"])), unsafe_allow_html=True)

    st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
    st.subheader("Ringkasan Perhitungan (Lab)")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("**SS Between (SSB)**:", fmt(anv["ssb"],4))
        st.write("**df Between**:", anv["dfb"])
        st.write("**MS Between**:", fmt(anv["msb"],4))
    with c2:
        st.write("**SS Within (SSW)**:", fmt(anv["ssw"],4))
        st.write("**df Within**:", anv["dfw"])
        st.write("**MS Within**:", fmt(anv["msw"],4))
    with c3:
        st.write("**SST**:", fmt(anv["sst"],4))
        st.write("**F-Statistic**:", fmt(anv["F"],4))
        st.write("**Eta² (effect size)**:", fmt(anv["eta2"],3))

    st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
    st.subheader("Keputusan Uji (α = {:.2f})".format(alpha))
    st.markdown(decision, unsafe_allow_html=True)
    if note:
        st.markdown(f'<div class="footer-note">{note}</div>', unsafe_allow_html=True)

    st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
    st.subheader("Rata-rata per Kelompok")
    render_means_chart(means)

    st.subheader("Varians per Kelompok (indikasi keragaman)")
    render_var_chart(groups=ROUND_CACHE["groups"])

# -------------------------
# ROUND STATE & CONTROLS
# -------------------------
def controls_panel():
    st.markdown('<div class="el-card">', unsafe_allow_html=True)
    st.markdown('<div class="el-title">⚙️ Pengaturan Eksperimen</div>', unsafe_allow_html=True)
    st.markdown('<div class="el-sub">Ubah jumlah kelompok, sampel, dan besaran perbedaan mean (effect size).</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1,1])
    with c1:
        k = st.slider("Jumlah Kelompok (k)", 3, 6, st.session_state.controls["k"])
        n = st.slider("Ukuran Sampel/kelompok (n)", 4, 12, st.session_state.controls["n"])
    with c2:
        effect = st.slider("Besaran Perbedaan Mean (effect)", 0.0, 2.0, st.session_state.controls["effect"], 0.1)
        alpha = st.select_slider("Taraf Signifikansi (α)", options=[0.10, 0.05, 0.01], value=st.session_state.controls["alpha"])
    apply = st.button("Terapkan & Mulai Ronde Baru 🔁")
    st.markdown('</div>', unsafe_allow_html=True)

    if apply:
        st.session_state.controls["k"] = k
        st.session_state.controls["n"] = n
        st.session_state.controls["effect"] = effect
        st.session_state.controls["alpha"] = float(alpha)
        # advance seed to refresh data
        st.session_state.seed = random.randint(1, 10_000)
        new_round(reset_score=False)

def new_round(reset_score:bool=False):
    if reset_score:
        st.session_state.score = 0
        st.session_state.best_score = max(st.session_state.best_score, st.session_state.score)
        st.session_state.history.clear()
        st.session_state.round = 1
    else:
        st.session_state.round += 1
    st.session_state.last_feedback = ""
    st.session_state.user_guess = None
    st.rerun()

# -------------------------
# GLOBAL ROUND CACHE
# (to allow charts use current groups)
# -------------------------
ROUND_CACHE = {"groups": {}}

# -------------------------
# HEADER
# -------------------------
st.markdown(
    """
    <div class="el-card" style="display:flex; align-items:center; justify-content:space-between; gap:16px;">
      <div>
        <div class="el-title" style="font-size:28px;">⚔️ ANOVA Odyssey: <span style="color:#4A67E9">Expert Edition</span></div>
        <div class="el-sub">Kelompok 4 ANOVA · HMSD Adyatama ITERA 2025</div>
      </div>
      <div class="el-chip">Elegan ANOVA · Biru & Emas</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------
# SIDEBAR (scoreboard)
# -------------------------
with st.sidebar:
    st.markdown("### 🧭 Progress")
    st.write("**Level/Ronde:**", st.session_state.round)
    st.write("**Skor:**", st.session_state.score)
    if st.session_state.history:
        best = max(h["score_after"] for h in st.session_state.history)
        st.write("**Best (sesi):**", best)
    st.markdown("---")
    st.markdown("**How to win?**")
    st.caption("Tebak dengan benar apakah ada perbedaan signifikan. "
               "Skor +10 jika benar, -5 jika salah. Naik level, data berganti.")
    st.markdown("---")
    if st.button("🔄 Reset Game (Skor & Ronde)"):
        st.session_state.seed = random.randint(1, 10_000)
        new_round(reset_score=True)

# -------------------------
# CONTROLS PANEL
# -------------------------
controls_panel()

# -------------------------
# ROUND DATA GENERATION
# -------------------------
k = st.session_state.controls["k"]
n = st.session_state.controls["n"]
effect = st.session_state.controls["effect"]
alpha = st.session_state.controls["alpha"]

groups = generate_groups(k, n, effect, seed=st.session_state.seed + st.session_state.round)
ROUND_CACHE["groups"] = groups

# -------------------------
# DATA TABLE
# -------------------------
st.markdown('<div class="el-card">', unsafe_allow_html=True)
st.markdown(f'<div class="el-title">🧪 {st.session_state.controls["round_name"]} {st.session_state.round}</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Data hasil percobaan untuk beberapa kelompok (nilai simulasi).</div>', unsafe_allow_html=True)
render_data_table(groups)
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# SIMULATED CALCULATION (ANIMATION)
# -------------------------
with st.expander("▶️ Jalankan Perhitungan ANOVA (simulasi langkah)", expanded=True):
    prog = st.progress(0, text="Menyiapkan data …")
    time.sleep(0.25)
    prog.progress(20, text="Menghitung rata-rata tiap kelompok …")
    time.sleep(0.15)
    prog.progress(40, text="Menghitung Grand Mean …")
    time.sleep(0.12)
    prog.progress(60, text="Menghitung SSB & SSW …")
    time.sleep(0.18)
    prog.progress(80, text="Menyusun tabel ANOVA …")
    time.sleep(0.14)
    prog.progress(100, text="Selesai ✅")
    time.sleep(0.05)

# -------------------------
# ANOVA CORE
# -------------------------
anv = anova_oneway(groups)
df1 = anv["dfb"]
df2 = anv["dfw"]
F_calc = anv["F"]

# F critical (alpha=0.05 only table provided; if alpha != 0.05, we adapt roughly)
Fcrit_005 = interp_fcrit(max(1,min(5,df1)), max(3, min(200, df2)), F_CRIT_005)

def adjust_alpha(Fcrit_005:float, alpha:float)->float:
    # rough monotone scaling: alpha 0.10 -> ~0.85*Fcrit_005 ; alpha 0.01 -> ~1.35*Fcrit_005
    if abs(alpha - 0.05) < 1e-9:
        return Fcrit_005
    if abs(alpha - 0.10) < 1e-9:
        return Fcrit_005 * 0.85
    if abs(alpha - 0.01) < 1e-9:
        return Fcrit_005 * 1.35
    return Fcrit_005

Fcrit = adjust_alpha(Fcrit_005, alpha)
significant = F_calc > Fcrit

# -------------------------
# PREDICTION UI
# -------------------------
st.markdown('<div class="el-card">', unsafe_allow_html=True)
st.markdown('<div class="el-title">🎯 Prediksi Kamu</div>', unsafe_allow_html=True)
st.markdown('<div class="el-sub">Berdasarkan tabel & grafik, apakah ada perbedaan rata-rata yang signifikan?</div>', unsafe_allow_html=True)

choice = st.radio(
    "Pilih jawaban:",
    ["Ya, signifikan ✅", "Tidak signifikan ❌"],
    key="user_guess"
)

go = st.button("Kunci Jawaban & Lihat Hasil 🧪")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# RESULT + SCORING
# -------------------------
if go:
    correct = (choice.startswith("Ya") and significant) or (choice.startswith("Tidak") and not significant)
    before = st.session_state.score
    if correct:
        st.session_state.score += 10
        st.session_state.last_feedback = f"✅ Tepat! F_hit = {fmt(F_calc,3)} > F_krit = {fmt(Fcrit,3)}" if significant else f"✅ Tepat! F_hit = {fmt(F_calc,3)} ≤ F_krit = {fmt(Fcrit,3)}"
        st.balloons()
        badge = '<span class="badge ok">Benar · +10</span>'
    else:
        st.session_state.score -= 5
        st.session_state.last_feedback = f"❌ Kurang tepat. F_hit = {fmt(F_calc,3)} {'>' if significant else '≤'} F_krit = {fmt(Fcrit,3)}"
        badge = '<span class="badge err">Salah · -5</span>'

    st.session_state.history.append({
        "round": st.session_state.round,
        "choice": "Signifikan" if choice.startswith("Ya") else "Tidak",
        "significant": significant,
        "F": F_calc, "Fcrit": Fcrit,
        "score_before": before,
        "score_after": st.session_state.score
    })

    # DECISION TEXT
    if significant:
        decision_html = f"""
        <div class="badge ok">Keputusan: Tolak H₀</div>
        <div class="footer-note">Karena F_hit ({fmt(F_calc,3)}) > F_krit ({fmt(Fcrit,3)}), terdapat bukti bahwa
        setidaknya ada satu mean kelompok yang berbeda.</div>
        """
        note = "Interpretasi: Variasi antar-kelompok relatif lebih besar dibanding variasi dalam-kelompok."
    else:
        decision_html = f"""
        <div class="badge warn">Keputusan: Gagal Menolak H₀</div>
        <div class="footer-note">Karena F_hit ({fmt(F_calc,3)}) ≤ F_krit ({fmt(Fcrit,3)}), belum cukup bukti adanya perbedaan rata-rata antar kelompok.</div>
        """
        note = "Interpretasi: Perbedaan rata-rata antar-kelompok tidak cukup kuat dibanding noise di dalam kelompok."

    st.markdown('<div class="el-card">', unsafe_allow_html=True)
    st.markdown(f'<div style="display:flex; align-items:center; gap:10px;">{badge}<div style="font-weight:800;">&nbsp;Hasil Ronde {st.session_state.round}</div></div>', unsafe_allow_html=True)
    st.write(st.session_state.last_feedback)
    st.markdown('</div>', unsafe_allow_html=True)

    # LAB REPORT + VISUALS
    lab_report(anv, alpha, decision_html, note)

    # NEXT ROUND BUTTON
    st.markdown('<div class="el-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([1,1])
    with c1:
        if st.button("🔁 Lanjut ke Ronde Berikutnya"):
            st.session_state.seed = random.randint(1, 10_000)
            new_round(reset_score=False)
    with c2:
        st.write(f"🏆 Skor Kamu Sekarang: **{st.session_state.score}**")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# HISTORY / LEADERBOARD (SESSION)
# -------------------------
with st.expander("🏅 Riwayat Ronde & Leaderboard (Sesi Ini)"):
    if not st.session_state.history:
        st.info("Belum ada riwayat. Mainkan satu ronde dulu.")
    else:
        # simple html table
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
            f"<table class='simple'><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table>",
            unsafe_allow_html=True
        )
        top = max(h["score_after"] for h in st.session_state.history)
        st.markdown(f"<div class='footer-note'>Skor terbaik sesi ini: <b>{top}</b>. Coba atur k, n, dan effect untuk tantangan baru.</div>", unsafe_allow_html=True)

# -------------------------
# FOOTER NOTES
# -------------------------
st.markdown('<div class="hr-soft"></div>', unsafe_allow_html=True)
st.caption(
    "Catatan: Tabel F-kritikal disediakan untuk α=0.05 dan df terbatas dengan interpolasi sederhana; "
    "untuk α=0.10 dan 0.01 digunakan skala pendekatan. Cukup akurat untuk tujuan edukasi & gameplay."
)

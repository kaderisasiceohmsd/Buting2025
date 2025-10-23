import streamlit as st
import random

st.set_page_config(page_title="📊 ANOVA Explorer", page_icon="⚔️", layout="centered")

st.title("⚔️ ANOVA Explorer: Battle of Means")
st.caption("Kreasi 2 | Kelompok 4 ANOVA | HMSD Adyatama ITERA 2025")
st.markdown("---")

# Inisialisasi state
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# -------------------------------------------------------------
# Generate data random untuk 3 kelompok
# -------------------------------------------------------------
n = 5
group_A = [random.randint(50, 90) for _ in range(n)]
group_B = [random.randint(40, 95) for _ in range(n)]
group_C = [random.randint(30, 100) for _ in range(n)]
groups = {"A": group_A, "B": group_B, "C": group_C}

# Hitung rata-rata tiap kelompok
means = {k: sum(v)/len(v) for k, v in groups.items()}
grand_mean = sum(means.values()) / 3

# Hitung variasi antar & dalam kelompok
ss_between = sum(len(v) * (means[k] - grand_mean)**2 for k, v in groups.items())
ss_within = sum(sum((x - means[k])**2 for x in v) for k, v in groups.items())
df_between = 3 - 1
df_within = 3 * (n - 1)
ms_between = ss_between / df_between
ms_within = ss_within / df_within
f_stat = ms_between / (ms_within + 1e-9)  # biar gak error div 0

# -------------------------------------------------------------
# Tampilkan tabel data
# -------------------------------------------------------------
st.subheader(f"🧪 Ronde {st.session_state.round}")
st.write("Berikut data hasil percobaan dari tiga kelompok:")

st.table({
    "Kelompok A": group_A,
    "Kelompok B": group_B,
    "Kelompok C": group_C
})

# Visualisasi mean dalam bentuk bar sederhana
st.subheader("📊 Visualisasi Rata-rata Kelompok")
chart_data = [
    f"A: {means['A']:.2f}",
    f"B: {means['B']:.2f}",
    f"C: {means['C']:.2f}"
]
bars = " | ".join(chart_data)
st.markdown(f"""
<div style='padding:10px; background-color:#f8f9fa; border-radius:10px; text-align:center;'>
<b>{bars}</b>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Pemain menebak
# -------------------------------------------------------------
st.write("Berdasarkan data di atas, apakah menurutmu terdapat **perbedaan signifikan antar kelompok?**")

choice = st.radio("Pilih jawabanmu:", ["Ya, signifikan ✅", "Tidak signifikan ❌"])

if st.button("Cek Hasil 🎯"):
    significant = f_stat > 3.0  # ambang sederhana
    if (choice.startswith("Ya") and significant) or (choice.startswith("Tidak") and not significant):
        st.session_state.score += 10
        st.session_state.feedback = f"✅ Benar! F = {f_stat:.2f} → {'Signifikan' if significant else 'Tidak signifikan'}"
        st.balloons()
    else:
        st.session_state.score -= 5
        st.session_state.feedback = f"❌ Kurang tepat! F = {f_stat:.2f} → {'Signifikan' if significant else 'Tidak signifikan'}"
    st.session_state.round += 1
    st.rerun()

if st.session_state.feedback:
    st.info(st.session_state.feedback)

# -------------------------------------------------------------
# Skor dan opsi ulang
# -------------------------------------------------------------
st.markdown("---")
st.subheader(f"🏆 Skor Kamu: {st.session_state.score}")

if st.button("🔁 Main Lagi"):
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.feedback = ""
    st.rerun()

# -------------------------------------------------------------
# Penjelasan singkat
# -------------------------------------------------------------
st.markdown("---")
st.caption("""
🎓 Game ini mensimulasikan **Analisis Varians (ANOVA)** sederhana.
F-statistic dihitung sebagai rasio *variasi antar kelompok* terhadap *variasi dalam kelompok*.

> F = (SS<sub>antara</sub>/df<sub>antara</sub>) ÷ (SS<sub>dalam</sub>/df<sub>dalam</sub>)

Jika F > 3.0 → diasumsikan perbedaan signifikan.
""", unsafe_allow_html=True)

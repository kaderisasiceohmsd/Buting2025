import streamlit as st
import random

st.set_page_config(page_title="📊 ANOVA Arena", page_icon="⚔️", layout="centered")

st.title("⚔️ ANOVA Arena: The Battle of Variance")
st.caption("Kreasi 2 | Kelompok 4 ANOVA | HMSD Adyatama ITERA 2025")
st.markdown("---")

# State
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "result" not in st.session_state:
    st.session_state.result = ""

# Data acak
group_a = [random.randint(50, 80) for _ in range(5)]
group_b = [random.randint(40, 90) for _ in range(5)]
group_c = [random.randint(30, 100) for _ in range(5)]

groups = {"A": group_a, "B": group_b, "C": group_c}

means = {k: sum(v)/len(v) for k, v in groups.items()}
grand_mean = sum(means.values()) / len(means)

# Hitung "indikasi perbedaan" sederhana (bukan scipy)
between_var = sum(len(v) * (means[k] - grand_mean)**2 for k, v in groups.items())
within_var = sum(sum((x - means[k])**2 for x in v) for k, v in groups.items())

score_ratio = between_var / (within_var + 1e-6)  # biar gak error div 0

st.subheader(f"🧩 Ronde {st.session_state.round}")
st.write("Berikut hasil 3 kelompok data eksperimen:")

for k in groups:
    st.write(f"Kelompok {k}: {groups[k]} | Mean = {means[k]:.2f}")

st.write(f"📈 Indikasi selisih antar-mean: {abs(max(means.values()) - min(means.values())):.2f}")

choice = st.radio("Menurutmu, apakah terdapat perbedaan signifikan antar kelompok?", ["Ya, signifikan ✅", "Tidak signifikan ❌"])

if st.button("Cek Hasil 🎯"):
    significant = score_ratio > 1.2  # ambang sederhana
    if (choice.startswith("Ya") and significant) or (choice.startswith("Tidak") and not significant):
        st.session_state.score += 10
        st.session_state.result = f"✅ Tepat! Skor rasio = {score_ratio:.2f} → {'Signifikan' if significant else 'Tidak signifikan'}"
        st.balloons()
    else:
        st.session_state.score -= 5
        st.session_state.result = f"❌ Kurang tepat! Skor rasio = {score_ratio:.2f} → {'Signifikan' if significant else 'Tidak signifikan'}"
    st.session_state.round += 1
    st.rerun()

if st.session_state.result:
    st.info(st.session_state.result)

st.markdown("---")
st.write(f"🏆 Skor Kamu: **{st.session_state.score}**")

if st.button("🔁 Main Lagi"):
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.result = ""
    st.rerun()

st.caption("🎓 Game ini menggambarkan konsep **Analisis Varians (ANOVA)** "
            "dengan pendekatan intuitif: makin besar perbedaan rata-rata antar kelompok, "
            "makin tinggi kemungkinan perbedaan signifikan.")

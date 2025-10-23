import streamlit as st
import random

st.set_page_config(page_title="🎮 The Mean Machine", page_icon="🧠", layout="centered")

st.title("🎮 StatQuest: The Mean Machine")
st.caption("Kreasi Bebas | Kelompok 4 ANOVA | HMSD Adyatama ITERA 2025")
st.markdown("---")

# State
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# Generate data acak
data_groups = {
    "A": [random.randint(30, 70) for _ in range(5)],
    "B": [random.randint(40, 90) for _ in range(5)],
    "C": [random.randint(20, 60) for _ in range(5)]
}

means = {g: sum(v)/len(v) for g, v in data_groups.items()}
variances = {g: sum((x - means[g])**2 for x in v)/len(v) for g, v in data_groups.items()}

st.subheader(f"📊 Ronde {st.session_state.round}")
st.write("Pilih dataset yang **paling stabil** (variasi datanya paling kecil):")

for g in data_groups:
    st.write(f"Kelompok {g}: {data_groups[g]} | Mean = {means[g]:.2f}")

choice = st.radio("Pilih dataset terbaik:", ["A", "B", "C"])

if st.button("Kunci Jawaban 🚀"):
    best = min(variances, key=variances.get)
    if choice == best:
        st.session_state.score += 10
        st.session_state.feedback = f"✅ Benar! Kelompok {choice} paling stabil (variasi = {variances[choice]:.2f})"
        st.balloons()
    else:
        st.session_state.score -= 5
        st.session_state.feedback = f"❌ Salah! Jawaban yang benar adalah {best} (variasi = {variances[best]:.2f})"
    st.session_state.round += 1
    st.rerun()

if st.session_state.feedback:
    st.info(st.session_state.feedback)

st.markdown("---")
st.write(f"🏆 Skor Kamu: **{st.session_state.score}**")

if st.button("🔁 Main Ulang"):
    st.session_state.score = 0
    st.session_state.round = 1
    st.session_state.feedback = ""
    st.rerun()

st.caption("💡 Game ini mengasah intuisi statistik dalam memilih data yang paling 'stabil'.")

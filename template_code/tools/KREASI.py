import streamlit as st
import random
import numpy as np
import time

# ----------------------------
# Konfigurasi Halaman
# ----------------------------
st.set_page_config(page_title="🎮 Data Dash – Catch the Mean!", page_icon="🎯", layout="centered")

st.title("🎮 Data Dash: Catch the Mean!")
st.caption("Kreasi Bebas | Kelompok 4 ANOVA | HMSD Adyatama ITERA 2025")
st.markdown("---")

# ----------------------------
# Inisialisasi State
# ----------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "message" not in st.session_state:
    st.session_state.message = ""

# ----------------------------
# Buat data random
# ----------------------------
data = [random.randint(10, 99) for _ in range(6)]
target_mean = np.mean(random.sample(range(20, 90), 3))

st.subheader(f"🧩 Ronde {st.session_state.round}")
st.write(f"🎯 Target Mean: **{target_mean:.2f}**")
st.write("Pilih angka yang **paling mendekati rata-rata target** di bawah ini:")

# ----------------------------
# Tombol pilihan
# ----------------------------
cols = st.columns(3)
chosen = None

for i, num in enumerate(data):
    with cols[i % 3]:
        if st.button(f"🎲 {num}", key=f"btn{i}"):
            chosen = num

# ----------------------------
# Evaluasi hasil
# ----------------------------
if chosen is not None:
    closest = min(data, key=lambda x: abs(x - target_mean))
    if chosen == closest:
        st.session_state.score += 10
        st.session_state.message = f"✅ Hebat! {chosen} paling mendekati mean ({target_mean:.2f})"
        st.balloons()
    else:
        st.session_state.score -= 5
        st.session_state.message = f"❌ Sayang! {chosen} bukan yang paling dekat, seharusnya {closest}"

    st.session_state.round += 1
    st.rerun()

# ----------------------------
# Tampilkan pesan & skor
# ----------------------------
if st.session_state.message:
    st.info(st.session_state.message)

st.markdown("---")
st.write(f"🏆 **Skor Saat Ini:** {st.session_state.score}")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔁 Main Lagi"):
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.message = ""
        st.rerun()
with col2:
    st.caption("Tips: Semakin cepat dan akurat, semakin tinggi skor kamu 💡")

st.markdown("---")
st.caption("🧠 Game ini mengasah intuisi statistik tentang **rata-rata (mean)** "
            "dan melatih ketepatan dalam memilih nilai data yang paling representatif.")

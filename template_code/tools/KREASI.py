import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time

# -------------------------------------------
# KONFIGURASI HALAMAN
# -------------------------------------------
st.set_page_config(page_title="🎮 Data Runner: Mission Mean!", page_icon="🧠", layout="centered")

st.title("🎮 Data Runner: Mission Mean!")
st.caption("Kreasi Bebas | Kelompok 4 ANOVA | HMSD Adyatama ITERA 2025")
st.markdown("---")

# -------------------------------------------
# INISIALISASI STATE
# -------------------------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# -------------------------------------------
# GENERATE DATA UNTUK 3 KELOMPOK
# -------------------------------------------
n = 8
base_mean = random.randint(40, 80)
groups = {
    "A": np.random.normal(base_mean + random.randint(-10, 10), random.uniform(2, 10), n),
    "B": np.random.normal(base_mean + random.randint(-10, 10), random.uniform(2, 10), n),
    "C": np.random.normal(base_mean + random.randint(-10, 10), random.uniform(2, 10), n)
}

# Hitung statistik ringkas
means = {g: np.mean(v) for g, v in groups.items()}
stds = {g: np.std(v) for g, v in groups.items()}
cv = {g: stds[g] / means[g] for g in groups}  # koefisien variasi

# -------------------------------------------
# TAMPILKAN DATA
# -------------------------------------------
st.subheader(f"🧩 Ronde {st.session_state.round}")
st.write("Pilih **dataset terbaik** (paling stabil terhadap mean-nya):")

col1, col2 = st.columns(2)
with col1:
    st.write("📈 Statistik Singkat:")
    for g in groups:
        st.write(f"Kelompok {g}: Mean = {means[g]:.2f}, Std = {stds[g]:.2f}")

with col2:
    fig, ax = plt.subplots()
    ax.boxplot(groups.values(), labels=groups.keys(), patch_artist=True)
    ax.set_title("Perbandingan Variasi Data")
    ax.set_ylabel("Nilai")
    st.pyplot(fig)

# -------------------------------------------
# PEMAIN MEMILIH
# -------------------------------------------
choice = st.radio("🧠 Pilih dataset paling stabil:", ["A", "B", "C"])

if st.button("Submit Pilihan 🚀"):
    best = min(cv, key=cv.get)  # paling stabil = variasi terkecil
    if choice == best:
        st.session_state.score += 10
        st.session_state.feedback = f"✅ Keren! {choice} paling stabil (CV={cv[choice]:.3f})"
        st.balloons()
    else:
        st.session_state.score -= 5
        st.session_state.feedback = (
            f"❌ Salah! Dataset terbaik sebenarnya {best} "
            f"(CV={cv[best]:.3f}) karena variasinya paling kecil."
        )
    st.session_state.round += 1
    time.sleep(0.8)
    st.rerun()

# -------------------------------------------
# TAMPILKAN SKOR & FEEDBACK
# -------------------------------------------
if st.session_state.feedback:
    st.info(st.session_state.feedback)

st.markdown("---")
st.subheader(f"🏆 Skor Kamu: {st.session_state.score}")

# -------------------------------------------
# VISUALISASI TAMBAHAN
# -------------------------------------------
exp = st.expander("📊 Lihat Data Lengkap")
with exp:
    import pandas as pd
    df = pd.DataFrame(groups)
    st.dataframe(df.round(2))

# -------------------------------------------
# NAVIGASI
# -------------------------------------------
col1, col2 = st.columns(2)
with col1:
    if st.button("🔁 Main Lagi"):
        st.session_state.score = 0
        st.session_state.round = 1
        st.session_state.feedback = ""
        st.rerun()
with col2:
    st.caption("💡 Semakin kecil variasi data, semakin 'stabil' dataset-nya.")

st.markdown("---")
st.caption("🧠 Game ini mengenalkan konsep **koefisien variasi (CV)** "
            "— ukuran seberapa stabil suatu dataset terhadap mean-nya. "
            "Semakin kecil CV, semakin baik kualitas datanya.")

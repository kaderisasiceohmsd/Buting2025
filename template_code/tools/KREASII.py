import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="StatQuest – The ANOVA Battle", page_icon="⚔️")

st.title("⚔️ StatQuest: The ANOVA Battle")
st.caption("Kreasi Kelompok 4 ANOVA | HMSD Adyatama ITERA 2025")
st.markdown("---")

# ===========================================================
# INISIALISASI SKOR & LEVEL
# ===========================================================
if "score" not in st.session_state:
    st.session_state.score = 0
if "round" not in st.session_state:
    st.session_state.round = 1

st.sidebar.title("📊 Statistik Pemain")
st.sidebar.write(f"**Level:** {st.session_state.round}")
st.sidebar.write(f"**Skor:** {st.session_state.score}")

# ===========================================================
# BUAT DATA ACAK UNTUK SETIAP RONDE
# ===========================================================
n = 10
mean1 = random.uniform(40, 60)
mean2 = mean1 + random.uniform(-10, 10)
mean3 = mean1 + random.uniform(-10, 10)
std = random.uniform(3, 10)

group_a = np.random.normal(mean1, std, n)
group_b = np.random.normal(mean2, std, n)
group_c = np.random.normal(mean3, std, n)

# UJI ANOVA
F, p = stats.f_oneway(group_a, group_b, group_c)

# ===========================================================
# TAMPILKAN DATA
# ===========================================================
st.subheader(f"🧪 Ronde {st.session_state.round}")
st.write("Berikut hasil pengamatan dari tiga kelompok eksperimen:")

df = pd.DataFrame({
    "Kelompok A": group_a,
    "Kelompok B": group_b,
    "Kelompok C": group_c
})
st.dataframe(df.round(2))

fig, ax = plt.subplots()
ax.boxplot([group_a, group_b, group_c], labels=["A", "B", "C"])
ax.set_title("Visualisasi Data Tiga Kelompok")
ax.set_ylabel("Nilai")
st.pyplot(fig)

# ===========================================================
# TEBAKAN PEMAIN
# ===========================================================
st.subheader("🎯 Tantanganmu:")
st.write("Apakah menurutmu ada **perbedaan signifikan antar kelompok**?")

col1, col2 = st.columns(2)
with col1:
    tebak_signifikan = st.button("Ya, signifikan ✅")
with col2:
    tebak_tidak = st.button("Tidak signifikan ❌")

# ===========================================================
# CEK HASIL TEBAKAN
# ===========================================================
if tebak_signifikan or tebak_tidak:
    benar = (p < 0.05)
    if tebak_signifikan and benar:
        st.session_state.score += 10
        st.success(f"🔥 Tepat sekali! p-value = {p:.4f} < 0.05 → Ada perbedaan signifikan.")
    elif tebak_tidak and not benar:
        st.session_state.score += 10
        st.success(f"🔥 Betul! p-value = {p:.4f} ≥ 0.05 → Tidak ada perbedaan signifikan.")
    else:
        st.session_state.score -= 5
        st.error(f"😅 Salah! p-value = {p:.4f}. Coba lebih jeli di ronde berikutnya.")
    
    st.session_state.round += 1
    st.balloons()
    st.button("Lanjut ke Ronde Berikutnya 🔁", on_click=lambda: st.rerun())

# ===========================================================
# INFO TAMBAHAN
# ===========================================================
st.markdown("---")
st.caption("🎓 Game ini membantu memahami konsep ANOVA dengan cara seru. "
            "Coba mainkan beberapa ronde dan lihat bagaimana distribusi memengaruhi p-value!")

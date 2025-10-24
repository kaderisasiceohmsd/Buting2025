import streamlit as st
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("🧮 Kalkulator Bayes Interaktif")
st.write("Aplikasi sederhana untuk menghitung probabilitas posterior menggunakan Teorema Bayes.")

# Input dari user
st.sidebar.header("Masukkan Nilai Probabilitas (0–1)")
prior = st.sidebar.slider("P(H) - Probabilitas awal hipotesis", 0.0, 1.0, 0.01, 0.01)
likelihood = st.sidebar.slider("P(E|H) - Probabilitas bukti jika hipotesis benar", 0.0, 1.0, 0.99, 0.01)
false_positive = st.sidebar.slider("P(E|¬H) - Probabilitas bukti jika hipotesis salah", 0.0, 1.0, 0.05, 0.01)

# Fungsi perhitungan Bayes
def bayes_calculator(prior, likelihood, false_positive):
    numerator = likelihood * prior
    denominator = numerator + false_positive * (1 - prior)
    if denominator == 0:
        return 0
    return numerator / denominator

posterior = bayes_calculator(prior, likelihood, false_positive)

# Tampilkan hasil
st.subheader("📊 Hasil Perhitungan")
st.write(f"**P(H|E)** = `{posterior:.4f}`")
st.write(f"Artinya: Ada **{posterior*100:.2f}%** kemungkinan hipotesis benar setelah bukti diperoleh.")

# Visualisasi
fig, ax = plt.subplots()
ax.bar(["Prior (P(H))", "Posterior (P(H|E))"], [prior, posterior], color=["#4C72B0", "#55A868"])
ax.set_ylim(0, 1)
ax.set_ylabel("Probabilitas")
ax.set_title("Perbandingan Prior dan Posterior")
st.pyplot(fig)

# Catatan
st.info("""
💡 **Catatan:**
- Jika prior sangat kecil (kejadian langka), hasil tes positif belum tentu berarti benar.
- Jika likelihood tinggi dan false positive kecil, probabilitas posterior akan meningkat signifikan.
""")

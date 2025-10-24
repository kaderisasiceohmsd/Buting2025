import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("🧮 Kalkulator Bayes Interaktif")
st.write("Aplikasi sederhana untuk menghitung probabilitas posterior menggunakan Teorema Bayes.")

# Sidebar input
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

# Hasil perhitungan
st.subheader("📊 Hasil Perhitungan")
st.metric(label="P(H|E) - Probabilitas Posterior", value=f"{posterior:.4f}", delta=f"{posterior - prior:.4f}")
st.write(f"Artinya: Ada **{posterior*100:.2f}%** kemungkinan hipotesis benar setelah bukti diperoleh.")

# Visualisasi menggunakan Streamlit bar chart
data = pd.DataFrame({
    "Probabilitas": ["Prior (P(H))", "Posterior (P(H|E))"],
    "Nilai": [prior, posterior]
})
st.bar_chart(data.set_index("Probabilitas"))

# Catatan tambahan
st.info("""
💡 **Catatan:**
- Jika prior sangat kecil (kejadian langka), hasil tes positif belum tentu berarti benar.
- Jika likelihood tinggi dan false positive kecil, probabilitas posterior akan meningkat signifikan.
""")

# Footer kecil
st.caption("Dibuat dengan ❤️ men

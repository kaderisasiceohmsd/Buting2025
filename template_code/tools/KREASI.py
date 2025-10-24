import streamlit as st

# -----------------------------
# 🧠 Fungsi Perhitungan Bayes
# -----------------------------
def bayes_calculator(prior, likelihood, false_positive):
    numerator = likelihood * prior
    denominator = numerator + false_positive * (1 - prior)
    if denominator == 0:
        return 0
    return numerator / denominator


# -----------------------------
# 🎨 UI Streamlit
# -----------------------------
st.set_page_config(page_title="Kalkulator Bayes", page_icon="🧮", layout="centered")

st.title("🧮 Kalkulator Bayes Interaktif")
st.write("Hitung probabilitas **posterior** dengan Teorema Bayes secara sederhana dan intuitif.")

# Input dari sidebar
st.sidebar.header("Masukkan Nilai Probabilitas (0–1)")
prior = st.sidebar.slider("P(H) - Probabilitas awal hipotesis", 0.0, 1.0, 0.01, 0.01)
likelihood = st.sidebar.slider("P(E|H) - Probabilitas bukti jika hipotesis benar", 0.0, 1.0, 0.99, 0.01)
false_positive = st.sidebar.slider("P(E|¬H) - Probabilitas bukti jika hipotesis salah", 0.0, 1.0, 0.05, 0.01)

# Hitung posterior
posterior = bayes_calculator(prior, likelihood, false_positive)
delta = posterior - prior

# Tampilkan hasil
st.subheader("📈 Hasil Perhitungan")
st.metric(label="P(H|E) - Probabilitas Posterior", value=f"{posterior:.4f}", delta=f"{delta:+.4f}")
st.write(f"Artinya: Ada **{posterior*100:.2f}%** kemungkinan hipotesis benar setelah bukti diperoleh.")

# Visualisasi sederhana (tanpa pandas)
st.subheader("🔍 Perbandingan Prior dan Posterior")
chart_data = {
    "Prior (P(H))": [prior],
    "Posterior (P(H|E))": [posterior]
}
st.bar_chart(chart_data)

# Catatan tambahan
st.info("""
💡 **Catatan:**
- Jika *prior* sangat kecil (kejadian langka), hasil tes positif belum tentu berarti benar.
- Jika *likelihood* tinggi dan *false positive* rendah, probabilitas *posterior* akan meningkat signifikan.
""")

st.caption("Dibuat dengan ❤️ menggunakan Streamlit — tanpa pustaka tambahan.")

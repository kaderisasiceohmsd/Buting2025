import streamlit as st

# -----------------------------
# 🧠 Fungsi Perhitungan Bayes
# -----------------------------
def bayes_calculator(prior, likelihood, false_positive):
    numerator = likelihood * prior
    denominator = numerator + false_positive * (1 - prior)
    if denominator == 0:
        return 0.0
    return numerator / denominator


# -----------------------------
# 🎨 UI Streamlit
# -----------------------------
st.set_page_config(page_title="Kalkulator Bayes", page_icon="🧮", layout="centered")

st.title("🧮 Kalkulator Bayes")
st.write("Hitung probabilitas **posterior** dengan menggunakan **Teorema Bayes** secara sederhana.")

# Input dari user
st.header("Masukkan Nilai Probabilitas (0–1)")
prior = st.number_input("P(H) → Probabilitas awal hipotesis", min_value=0.0, max_value=1.0, value=0.01, step=0.01)
likelihood = st.number_input("P(E|H) → Probabilitas bukti jika hipotesis benar", min_value=0.0, max_value=1.0, value=0.9, step=0.01)
false_positive = st.number_input("P(E|¬H) → Probabilitas bukti jika hipotesis salah", min_value=0.0, max_value=1.0, value=0.05, step=0.01)

if st.button("Hitung Posterior"):
    posterior = bayes_calculator(prior, likelihood, false_positive)
    delta = posterior - prior

    st.subheader("📊 Hasil Perhitungan")
    st.metric(label="P(H|E) → Probabilitas Posterior", value=f"{posterior:.4f}", delta=f"{delta:+.4f}")
    st.write(f"Artinya: Ada **{posterior*100:.2f}%** kemungkinan hipotesis benar setelah bukti diperoleh.")

    # Tampilan sederhana tabel hasil
    st.subheader("📋 Ringkasan Nilai")
    st.table([
        {"Keterangan": "P(H)", "Nilai": f"{prior:.4f}"},
        {"Keterangan": "P(E|H)", "Nilai": f"{likelihood:.4f}"},
        {"Keterangan": "P(E|¬H)", "Nilai": f"{false_positive:.4f}"},
        {"Keterangan": "P(H|E)", "Nilai": f"{posterior:.4f}"}
    ])

# Penjelasan tambahan
st.divider()
st.info("""
### 💡 Catatan:
- **P(H)** → Probabilitas awal (prior) suatu hipotesis.
- **P(E|H)** → Probabilitas bukti jika hipotesis benar.
- **P(E|¬H)** → Probabilitas bukti jika hipotesis salah.
- **P(H|E)** → Probabilitas hipotesis setelah melihat bukti (*posterior*).

**Contoh kasus:**  
Misalkan penyakit langka memiliki probabilitas awal 1% (P(H)=0.01).  
Tes memiliki akurasi 90% (P(E|H)=0.9), dan false positive 5% (P(E|¬H)=0.05).  
Maka hasil tes positif tidak berarti pasien pasti sakit — probabilitas sebenarnya sekitar 15–16%.
""")

st.caption("Dibuat dengan ❤️ menggunakan Streamlit — tanpa pustaka tambahan.")

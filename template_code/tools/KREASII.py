import streamlit as st
import random

# -----------------------------
# ⚙️ Fungsi Simulasi
# -----------------------------
def toss_coin(n_tosses, prob_head=0.5):
    """Simulasi pelemparan koin sebanyak n_tosses."""
    results = []
    heads = 0
    tails = 0

    for _ in range(n_tosses):
        if random.random() < prob_head:
            results.append("Head")
            heads += 1
        else:
            results.append("Tail")
            tails += 1

    return results, heads, tails


# -----------------------------
# 🎨 UI Streamlit
# -----------------------------
st.set_page_config(page_title="Simulasi Pelemparan Koin", page_icon="🪙", layout="centered")

st.title("🪙 Simulasi Pelemparan Koin (Coin Toss)")
st.write("Simulasikan pelemparan koin dan lihat hasil probabilitasnya secara interaktif!")

# Input user
st.header("⚙️ Pengaturan Simulasi")
n_tosses = st.number_input("Jumlah lemparan koin:", min_value=1, max_value=10000, value=10, step=1)
prob_head = st.slider("Probabilitas muncul Head:", 0.0, 1.0, 0.5, 0.01)

if st.button("Lempar Koin 🎲"):
    # Jalankan simulasi
    results, heads, tails = toss_coin(n_tosses, prob_head)

    # Hitung frekuensi empiris
    p_head_emp = heads / n_tosses
    p_tail_emp = tails / n_tosses

    # Tampilkan hasil
    st.subheader("📊 Hasil Simulasi")
    st.metric("Jumlah Head", heads)
    st.metric("Jumlah Tail", tails)
    st.write(f"**Probabilitas empiris Head:** {p_head_emp:.4f}")
    st.write(f"**Probabilitas empiris Tail:** {p_tail_emp:.4f}")

    # Visualisasi sederhana (masih pure Streamlit)
    st.subheader("🔍 Visualisasi Hasil")
    st.bar_chart({
        "Head": [heads],
        "Tail": [tails]
    })

    # Tampilkan hasil urutan lemparan
    st.subheader("🧾 Urutan Hasil Lemparan")
    st.write(", ".join(results))

# Info tambahan
st.divider()
st.info("""
### 💡 Penjelasan:
- Simulasi ini menggunakan fungsi `random.random()` dari Python untuk menghasilkan angka acak antara 0–1.  
- Jika nilai acak < probabilitas Head → hasil **Head**, sebaliknya **Tail**.  
- Dengan banyak percobaan (lemparan) yang cukup besar, hasil empiris akan semakin mendekati probabilitas teoritis.
""")


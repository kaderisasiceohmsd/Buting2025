import streamlit as st
import random

st.title("🎯 Game Tebak Angka")
st.caption("Kreasi Bebas Kelompok 4 ANOVA")

# Inisialisasi angka rahasia
if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 100)
    st.session_state.tebakan = 0

tebakan = st.number_input("Masukkan tebakan kamu:", 1, 100, step=1)

if st.button("Tebak!"):
    st.session_state.tebakan += 1
    if tebakan < st.session_state.angka_rahasia:
        st.warning("⚠️ Terlalu rendah! Coba angka yang lebih besar.")
    elif tebakan > st.session_state.angka_rahasia:
        st.warning("⚠️ Terlalu tinggi! Coba angka yang lebih kecil.")
    else:
        st.success(f"🎉 Benar! Angkanya {st.session_state.angka_rahasia}. "
                   f"Kamu menebak dalam {st.session_state.tebakan} kali!")
        st.balloons()
        if st.button("Main Lagi 🔁"):
            st.session_state.angka_rahasia = random.randint(1, 100)
            st.session_state.tebakan = 0

st.divider()
st.caption("Permainan ini melatih logika dan strategi. "
            "Semakin sedikit tebakan, semakin jenius kamu 🧠")



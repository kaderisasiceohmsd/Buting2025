import streamlit as st
import random

# Pengaturan halaman
st.set_page_config(page_title="🎯 Game Tebak Angka", layout="centered")

st.title("🎯 Game Tebak Angka")
st.write("Aku menyimpan sebuah angka rahasia antara **1 sampai 100**. Coba tebak ya!")

# Inisialisasi session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Input dari user
if not st.session_state.game_over:
    guess = st.number_input("Masukkan tebakanmu:", min_value=1, max_value=100, step=1)
    if st.button("Tebak!"):
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.warning("Terlalu kecil! 🔽 Coba angka yang lebih besar.")
        elif guess > st.session_state.secret_number:
            st.warning("Terlalu besar! 🔼 Coba angka yang lebih kecil.")
        else:
            st.success(f"🎉 Benar! Angkanya adalah {st.session_state.secret_number}.")
            st.balloons()
            st.info(f"Kamu berhasil dalam {st.session_state.attempts} percobaan!")
            st.session_state.game_over = True
else:
    st.success(f"Permainan selesai! Angkanya adalah {st.session_state.secret_number}.")
    if st.button("Main Lagi 🔁"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

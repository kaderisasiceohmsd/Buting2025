# tebak_angka.py
import streamlit as st
import random

st.set_page_config(page_title="Tebak Angka", layout="centered")

st.title("Game Tebak Angka")
st.write("Tebak angka yang disembunyikan. Pilih range dan jumlah kesempatan lalu tebak.")

# --- initialize session state ---
if "target" not in st.session_state:
    st.session_state.target = None
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "max_attempts" not in st.session_state:
    st.session_state.max_attempts = 15
if "history" not in st.session_state:
    st.session_state.history = []
if "min_val" not in st.session_state:
    st.session_state.min_val = 1
if "max_val" not in st.session_state:
    st.session_state.max_val = 100
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "message" not in st.session_state:
    st.session_state.message = ""

# --- controls to (re)start game ---
with st.sidebar:
    st.header("Pengaturan")
    min_v = st.number_input("Range minimum", value=st.session_state.min_val, step=1)
    max_v = st.number_input("Range maksimum", value=st.session_state.max_val, step=1)
    max_try = st.number_input("Kesempatan (max tries)", value=st.session_state.max_attempts, min_value=1, step=1)
    if min_v >= max_v:
        st.error("Range minimum harus < maximum")
    if st.button("Mulai / Reset Game"):
        st.session_state.min_val = int(min_v)
        st.session_state.max_val = int(max_v)
        st.session_state.max_attempts = int(max_try)
        st.session_state.target = random.randint(st.session_state.min_val, st.session_state.max_val)
        st.session_state.attempts = 0
        st.session_state.history = []
        st.session_state.game_over = False
        st.session_state.message = f"Game dimulai! Tebak angka antara {st.session_state.min_val} dan {st.session_state.max_val}."
        st.success("Game baru dimulai!")

# auto-start if no target
if st.session_state.target is None and st.session_state.min_val < st.session_state.max_val:
    st.session_state.target = random.randint(st.session_state.min_val, st.session_state.max_val)
    st.session_state.message = f"Game dimulai! Tebak angka antara {st.session_state.min_val} dan {st.session_state.max_val}."

st.write(st.session_state.message)

# --- main guessing UI ---
col1, col2 = st.columns([2,1])
with col1:
    guess = st.number_input("Masukkan tebakan:", value=st.session_state.min_val, step=1,
                            min_value=st.session_state.min_val, max_value=st.session_state.max_val)
with col2:
    if st.button("Tebak") and not st.session_state.game_over:
        st.session_state.attempts += 1
        g = int(guess)
        if g == st.session_state.target:
            st.session_state.history.append((g, "Benar"))
            st.session_state.game_over = True
            st.success(f"Yeay! Tebakan benar dalam {st.session_state.attempts} percobaan. Angka = {st.session_state.target}")
        else:
            hint = "lebih besar" if g < st.session_state.target else "lebih kecil"
            st.session_state.history.append((g, f"Salah — coba {hint}"))
            st.warning(f"Salah. Tebakanmu {hint}. Percobaan ke-{st.session_state.attempts}/{st.session_state.max_attempts}")
            if st.session_state.attempts >= st.session_state.max_attempts:
                st.session_state.game_over = True
                st.error(f"Kesempatan habis! Angka yang benar: {st.session_state.target}")

# show history
if st.session_state.history:
    st.write("Riwayat tebakan:")
    for i, (val, note) in enumerate(st.session_state.history, start=1):
        st.write(f"{i}. {val} — {note}")

# quick tips / buttons
st.divider()
if st.button("Tunjukkan jawaban dan reset"):
    st.info(f"Jawaban: {st.session_state.target}. Mulai game baru.")
    # reset and start new
    st.session_state.target = random.randint(st.session_state.min_val, st.session_state.max_val)
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.game_over = False
    st.session_state.message = f"Game baru dimulai! Tebak angka antara {st.session_state.min_val} dan {st.session_state.max_val}."

# display stats
st.write("---")
st.write(f"Kesempatan: {st.session_state.attempts}/{st.session_state.max_attempts}")
st.write(f"Range: {st.session_state.min_val} — {st.session_state.max_val}")

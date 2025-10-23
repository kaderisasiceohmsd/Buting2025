import streamlit as st
import random
import time

st.set_page_config(page_title="🎨 Color Reaction Game", page_icon="🎨")

st.title("🎨 Klik Warna Tepat!")
st.write("Klik tombol *yang warnanya sesuai dengan teks di atas!* 💡")

# Pilihan warna
warna_list = ["Merah", "Hijau", "Biru", "Kuning", "Ungu"]
emoji = {
    "Merah": "🔴",
    "Hijau": "🟢",
    "Biru": "🔵",
    "Kuning": "🟡",
    "Ungu": "🟣"
}

# State awal
if "target" not in st.session_state:
    st.session_state.target = random.choice(warna_list)
if "display_color" not in st.session_state:
    st.session_state.display_color = random.choice(warna_list)
if "skor" not in st.session_state:
    st.session_state.skor = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# Tampilkan warna
st.markdown(
    f"<h2 style='color:{st.session_state.display_color.lower()};text-align:center;'>"
    f"{st.session_state.target}</h2>",
    unsafe_allow_html=True
)

# Fungsi untuk reset ronde
def next_round():
    st.session_state.target = random.choice(warna_list)
    st.session_state.display_color = random.choice(warna_list)

# Pilihan tombol warna
cols = st.columns(5)
for i, warna in enumerate(warna_list):
    with cols[i]:
        if st.button(f"{emoji[warna]} {warna}"):
            if warna == st.session_state.target:
                st.session_state.skor += 1
                st.success("✅ Benar!")
            else:
                st.error("❌ Salah warna!")
                st.session_state.skor = max(0, st.session_state.skor - 1)
            next_round()
            st.experimental_rerun()

# Hitung waktu bermain
elapsed = int(time.time() - st.session_state.start_time)
st.write(f"⏱ Waktu bermain: *{elapsed} detik*")
st.write(f"🏆 Skor kamu: *{st.session_state.skor}*")

# Tombol reset
if st.button("🔁 Ulangi Game"):
    st.session_state.skor = 0
    st.session_state.start_time = time.time()
    next_round()
    st.experimental_rerun()
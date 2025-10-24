import streamlit as st
import random
import time

# 🧠 Efek teks typewriter
def typewriter(text, delay=0.03):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f"<h4 style='text-align:center;'>{full_text}</h4>", unsafe_allow_html=True)
        time.sleep(delay)

# 🔗 Link Google Drive (format langsung)
drive_links = [
    "https://drive.google.com/uc?export=view&id=1x1kGE_QZx5CLf4g4ipKRHpOAAQ3G0r41",
    "https://drive.google.com/uc?export=view&id=1LOfFVz5NrYq6KIon4MTg-qIFrqtHwchp",
    "https://drive.google.com/uc?export=view&id=1NnPtHtj6bS-I6NIMDargefd9H8H798FT",
    "https://drive.google.com/uc?export=view&id=1mt7H7_1LEW18Eldt2H0zZAZz39nAKGvn"
]

poisson_images = drive_links  # ✅ langsung pakai ini saja

# 🃏 Inisialisasi kartu
if "cards" not in st.session_state:
    cards = poisson_images * 4  # total 16 kartu (4 gambar × 4)
    random.shuffle(cards)
    st.session_state.cards = cards
else:
    cards = st.session_state.cards

# ⚙️ State permainan
if "flipped" not in st.session_state:
    st.session_state.flipped = [False] * len(cards)
if "selected" not in st.session_state:
    st.session_state.selected = []
if "matched" not in st.session_state:
    st.session_state.matched = [False] * len(cards)
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# 🎴 Judul
st.markdown("<h2 style='text-align:center;'>🎴 Sobat Poisson Memory Game 🐠</h2>", unsafe_allow_html=True)
typewriter("Ayo bantu Poisson menemukan pasangannya yang hilang 💖", 0.03)
st.write("---")

# 📸 Tampilan kartu
cols = st.columns(4)
for i, card in enumerate(cards):
    col = cols[i % 4]
    with col:
        if st.session_state.flipped[i] or st.session_state.matched[i]:
            st.image(card, width=120)
        else:
            if st.button(f"🎁 Kartu {i+1}", key=i):
                st.session_state.flipped[i] = True
                st.session_state.selected.append(i)

# 🧩 Logika permainan
if len(st.session_state.selected) == 2:
    first, second = st.session_state.selected
    st.session_state.attempts += 1
    if cards[first] == cards[second]:
        st.session_state.matched[first] = True
        st.session_state.matched[second] = True
        st.success("🎉 Yeay! Poisson ketemu pasangannya!")
        st.balloons()
    else:
        st.warning("😆 Wah, belum cocok! Coba lagi ya~")
        time.sleep(1)
        st.session_state.flipped[first] = False
        st.session_state.flipped[second] = False
    st.session_state.selected = []
    st.rerun()

# 🌟 Cek kemenangan
if all(st.session_state.matched):
    if not st.session_state.game_over:
        st.session_state.game_over = True
        st.success("🌟 Semua Poisson sudah bersatu kembali! Kamu hebat!")
        st.snow()
        st.markdown("💖 **Terima kasih sudah main bareng Sobat Poisson!** 💫")

st.write(f"🧮 Percobaan: {st.session_state.attempts}")

# 🔁 Tombol reset


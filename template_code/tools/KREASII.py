# app.py
import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", layout="centered")

# -------------------------------
# Inisialisasi State
# -------------------------------
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# -------------------------------
# Fungsi bantu
# -------------------------------
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

def check_winner(board):
    winning_combos = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in winning_combos:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(board):
        return "Draw"
    return None

# -------------------------------
# Tampilan Utama
# -------------------------------
st.title("🎮 Tic Tac Toe - 2 Pemain")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Papan Permainan")
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            if cols[col].button(st.session_state.board[idx] or " ", key=idx, use_container_width=True):
                if not st.session_state.board[idx] and not st.session_state.winner:
                    st.session_state.board[idx] = st.session_state.turn
                    winner = check_winner(st.session_state.board)
                    if winner:
                        st.session_state.winner = winner
                    else:
                        st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

    st.markdown("---")
    if st.session_state.winner == "Draw":
        st.success("Hasil: Seri 😅")
    elif st.session_state.winner:
        st.success(f"Pemenang: {st.session_state.winner} 🎉")
    else:
        st.info(f"Giliran: {st.session_state.turn}")

with col2:
    st.subheader("Kontrol")
    st.button("🔁 Mulai Ulang", on_click=reset_game)
    st.markdown("""
    **Cara Bermain:**
    1. Dua pemain bergantian menekan kotak kosong.  
    2. Pemain pertama adalah **X**, berikutnya **O**.  
    3. Siapa yang membuat garis 3 simbol lebih dulu menang!  
    """)

# Tambahan kecil agar tampil rapi
st.markdown("---")
st.caption("Dibuat dengan ❤️ menggunakan Streamlit")

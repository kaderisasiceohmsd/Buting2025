import streamlit as st
import time
import random

# 💛 --- Efek Lucu Sobat Poisson --- 💛
def efek_teks_poisson():
    st.markdown("""
    <style>
    /* 🌟 Efek Typewriter */
    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: #ffd700; }
    }
    .typewriter {
      overflow: hidden;
      border-right: .15em solid #ffd700;
      white-space: nowrap;
      margin: 0 auto;
      letter-spacing: .10em;
      animation: typing 4s steps(40, end), blink-caret .75s step-end infinite;
      font-weight: bold;
      color: #ffb703;
      font-size: 22px;
      text-align: center;
      width: fit-content;
    }

    /* 💫 Efek Blink */
    @keyframes blink {
      50% { opacity: 0; }
    }
    .blink {
      animation: blink 1s infinite;
      color: #FF69B4;
      font-weight: bold;
      font-size: 20px;
      text-align: center;
      margin-top: 20px;
    }

    body {
      background-color: #fffbea;
    }
    </style>

    <div style="text-align:center; margin-top:40px;">
        <div class="typewriter">🐠 Sobat Poisson siap terbang menembus awan-awan galau!</div>
        <div class="blink">✨ Klik tombol mulai dan buktikan ketangkasanmu! ✨</div>
    </div>
    """, unsafe_allow_html=True)

    st.caption("💛 Efek oleh Sobat Poisson Crew")
    st.snow()


# 🎮 --- Game Fly Poisson (Flappy Bird Mini) --- 🎮
def fly_poisson_game():
    st.subheader("🐟 Game: Fly Poisson")
    st.write("Klik tombol di bawah untuk membantu Sobat Poisson terbang sejauh mungkin 💨")

    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.y = 250
        st.session_state.pipe_x = 400
        st.session_state.pipe_gap = 150
        st.session_state.pipe_height = random.randint(100, 300)
        st.session_state.game_over = False

    if st.session_state.game_over:
        st.error(f"💥 Game Over! Skor kamu: {st.session_state.score}")
        if st.button("🔁 Main lagi"):
            st.session_state.score = 0
            st.session_state.y = 250
            st.session_state.pipe_x = 400
            st.session_state.game_over = False
            st.rerun()
    else:
        col1, col2 = st.columns([1, 2])
        with col1:
            if st.button("⬆️ Terbang!"):
                st.session_state.y -= 30
        with col2:
            st.write(f"Skor: **{st.session_state.score}**")

        st.session_state.y += 10
        st.session_state.pipe_x -= 20

        if st.session_state.pipe_x < -50:
            st.session_state.pipe_x = 400
            st.session_state.pipe_height = random.randint(100, 300)
            st.session_state.score += 1

        if (st.session_state.pipe_x < 100 < st.session_state.pipe_x + 50) and \
           not (st.session_state.pipe_height < st.session_state.y < st.session_state.pipe_height + st.session_state.pipe_gap):
            st.session_state.game_over = True

        if st.session_state.y > 500 or st.session_state.y < 0:
            st.session_state.game_over = True

        canvas_html = f"""
        <div style="width:400px; height:500px; background-color:#cceeff; border-radius:15px; margin:auto; position:relative;">
            <div style="position:absolute; left:100px; top:{st.session_state.y}px; width:40px; height:40px; 
                        background-color:#ffb703; border-radius:50%; text-align:center; line-height:40px; font-size:24px;">
                🐠
            </div>
            <div style="position:absolute; left:{st.session_state.pipe_x}px; top:0; width:50px; height:{st.session_state.pipe_height}px; background-color:#228B22;"></div>
            <div style="position:absolute; left:{st.session_state.pipe_x}px; top:{st.session_state.pipe_height + st.session_state.pipe_gap}px; width:50px; height:{500 - st.session_state.pipe_height - st.session_state.pipe_gap}px; background-color:#228B22;"></div>
        </div>
        """
        st.markdown(canvas_html, unsafe_allow_html=True)
        time.sleep(0.1)
        st.rerun()


# --- Jalankan Halaman ---
st.title("💛 Sobat Poisson Playground")
efek_teks_poisson()
time.sleep(4)
fly_poisson_game()

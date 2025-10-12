import streamlit as st

# Mengatur konfigurasi halaman menjadi layout lebar
st.set_page_config(page_title="Game Ular Python - ANOVA", page_icon="🐍", layout="wide")

# --- MENGGUNAKAN KOLOM UNTUK MEMASTIKAN POSISI SELALU DI TENGAH ---
# Ini adalah cara layout yang paling stabil dan anti-error di Streamlit.
# Kolom kiri dan kanan berfungsi sebagai spasi kosong.
left_spacer, main_content, right_spacer = st.columns([1, 2, 1])

# Semua konten kita masukkan ke dalam kolom tengah (`main_content`).
with main_content:
    # === JUDUL HALAMAN ===
    st.markdown("<h2 style='text-align:center; margin-bottom:1rem;'>🐍 Game Ular Python (Kelompok 04 ANOVA)</h2>", unsafe_allow_html=True)

    # === HTML + JS GAME (SEMUA UKURAN SUDAH DIKECILKAN) ===
    snake_game_html = """
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; width:100%;">

      <div style="position:relative; height:50px; margin-bottom:5px;">
        <h1 style="
          color:#c5a253;
          font-family:'Courier New', monospace;
          font-size:26px; /* DIKECILKAN */
          animation: floating 3s ease-in-out infinite;
          text-shadow:0 0 8px rgba(255,215,100,0.6), 0 0 15px rgba(255,225,150,0.4);
        ">
          ✦ ANOVA ✦
        </h1>
      </div>

      <div style="display:flex; justify-content:center; width:100%;">
        <canvas id="gameCanvas" width="480" height="480" tabindex="0"
          style="
            width: 480px !important;
            height: 480px !important;
            border:3px solid #c5a253;
            background-color:black;
            border-radius:16px;
            box-shadow:0 0 35px rgba(255,215,100,0.4), 0 0 70px rgba(255,225,150,0.3);
            outline:none;
            animation: goldPulse 3.5s ease-in-out infinite;
          ">
        </canvas>
      </div>

      <div style="margin-top:20px;">
        <button id="startBtn" style="
          background: linear-gradient(135deg, #ffb703, #f4a261, #e9c46a);
          color:black; font-weight:bold; border:none;
          padding: 10px 24px;
          border-radius:12px; cursor:pointer;
          font-family:'Courier New', monospace; font-size:15px;
          box-shadow:0 0 15px rgba(255,200,80,0.7); transition:all 0.3s ease;
          ">▶️ Mulai Game</button>

        <button id="restartBtn" style="
          background: linear-gradient(135deg, #f77f00, #f4a261, #e9c46a);
          color:black; font-weight:bold; border:none;
          padding: 10px 24px;
          border-radius:12px; cursor:pointer;
          font-family:'Courier New', monospace; font-size:15px;
          box-shadow:0 0 15px rgba(255,180,60,0.6); transition:all 0.3s ease;
          display:none;
          ">🔁 Mulai Ulang</button>

        <button id="pauseBtn" style="
          background: linear-gradient(135deg, #f4a261, #ffb703, #e9c46a);
          color:black; font-weight:bold; border:none;
          padding: 10px 24px;
          border-radius:12px; cursor:pointer;
          font-family:'Courier New', monospace; font-size:15px;
          margin-left:8px; box-shadow:0 0 15px rgba(255,200,80,0.5);
          display:none; transition:all 0.3s ease;
          ">⏸️ Pause</button>
      </div>

      <p style="
        color:#d9c987; font-family:Courier;
        font-size:13px; /* DIKECILKAN */
        margin-top:14px; text-shadow:0 0 6px rgba(255,225,150,0.7);
      ">
        Gunakan tombol: <b>W</b> / <b>A</b> / <b>S</b> / <b>D</b> atau panah ⬆️⬅️⬇️➡️ <br>
        Tekan <b>Spasi</b> untuk <i>Pause / Lanjut</i>.
      </p>
    </div>

    <style>
      @keyframes goldPulse { 0%, 100% { box-shadow:0 0 35px rgba(255,215,100,0.4), 0 0 70px rgba(255,225,150,0.3); } 50% { box-shadow:0 0 60px rgba(255,230,150,0.6), 0 0 100px rgba(255,245,180,0.4); } }
      @keyframes floating { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-6px); } }
      #startBtn:hover, #pauseBtn:hover, #restartBtn:hover { transform: scale(1.08); }
    </style>

    <script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");
    const startBtn = document.getElementById("startBtn");
    const restartBtn = document.getElementById("restartBtn");
    const pauseBtn = document.getElementById("pauseBtn");

    let box = 20; // UKURAN GRID DIKECILKAN
    let snake, food, d, score, game, speed;
    let started = false, paused = false, gameOver = false;
    let highscore = localStorage.getItem("anova_snake_highscore") || 0;
    const canvasSize = 480; // UKURAN CANVAS BARU DISESUAIKAN

    function drawStartScreen() {
      ctx.fillStyle = "black";
      ctx.fillRect(0,0,canvasSize,canvasSize);
      ctx.fillStyle = "#e9c46a";
      ctx.font = "16px Courier";
      ctx.textAlign = "center";
      ctx.fillText("Tekan tombol 'Mulai Game' untuk bermain", canvasSize/2, canvasSize/2 - 10);
      ctx.font = "14px Courier";
      ctx.fillText("Highscore: " + highscore, canvasSize/2, canvasSize/2 + 20);
    }
    drawStartScreen();

    function initGame() {
      snake = [{x: 9*box, y: 10*box}];
      food = {x: Math.floor(Math.random()*23+1)*box, y: Math.floor(Math.random()*23+1)*box};
      d = "RIGHT"; score = 0; speed = 100;
      gameOver = false; paused = false; started = true;
      startBtn.style.display = "none";
      restartBtn.style.display = "none";
      pauseBtn.style.display = "inline-block";
      clearInterval(game);
      game = setInterval(draw, speed);
      setTimeout(() => canvas.focus(), 50);
    }

    canvas.addEventListener('click', ()=> canvas.focus());

    document.addEventListener("keydown", direction);
    function direction(event) {
      if (!started || paused) return;
      const key = event.key.toLowerCase();
      if(key.startsWith("arrow")) event.preventDefault();
      if((key === "a" || key === "arrowleft") && d != "RIGHT") d = "LEFT";
      else if((key === "w" || key === "arrowup") && d != "DOWN") d = "UP";
      else if((key === "d" || key === "arrowright") && d != "LEFT") d = "RIGHT";
      else if((key === "s" || key === "arrowdown") && d != "UP") d = "DOWN";
    }

    function togglePause() {
      if (!started || gameOver) return;
      paused = !paused;
      if (paused) {
        clearInterval(game);
        ctx.fillStyle = "rgba(0,0,0,0.6)";
        ctx.fillRect(0,0,canvasSize,canvasSize);
        ctx.fillStyle = "#e9c46a";
        ctx.font = "24px Courier";
        ctx.textAlign = "center";
        ctx.fillText("⏸️ PAUSED", canvasSize/2, canvasSize/2);
        pauseBtn.textContent = "▶️ Lanjut";
      } else {
        game = setInterval(draw, speed);
        pauseBtn.textContent = "⏸️ Pause";
      }
    }

    function collision(head, array){
      for(let i=0; i<array.length; i++){ if(head.x == array[i].x && head.y == array[i].y){ return true; } }
      return false;
    }

    function draw() {
      ctx.fillStyle = "black";
      ctx.fillRect(0,0,canvasSize,canvasSize);
      for(let i=0; i<snake.length; i++){
        ctx.fillStyle = (i==0) ? "#f4a261" : "#e9c46a";
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
        ctx.strokeStyle = "#c5a253";
        ctx.strokeRect(snake[i].x, snake[i].y, box, box);
      }
      ctx.fillStyle = "#f77f00";
      ctx.beginPath();
      ctx.arc(food.x + box/2, food.y + box/2, box/2, 0, 2*Math.PI);
      ctx.fill();
      let snakeX = snake[0].x, snakeY = snake[0].y;
      if( d == "LEFT") snakeX -= box; if( d == "UP") snakeY -= box;
      if( d == "RIGHT") snakeX += box; if( d == "DOWN") snakeY += box;
      if(snakeX == food.x && snakeY == food.y){
        score++;
        food = {x: Math.floor(Math.random()*23+1)*box, y: Math.floor(Math.random()*23+1)*box};
        if (speed > 50) { speed -= 3; clearInterval(game); game = setInterval(draw, speed); }
      } else { snake.pop(); }
      let newHead = {x: snakeX, y: snakeY};
      if(snakeX < 0 || snakeY < 0 || snakeX >= canvasSize || snakeY >= canvasSize || collision(newHead, snake)){
        clearInterval(game); gameOver = true; started = false;
        ctx.fillStyle = "#f4a261";
        ctx.font = "24px Courier";
        ctx.textAlign = "center";
        ctx.fillText("GAME OVER", canvasSize/2, canvasSize/2 - 40);
        ctx.font = "18px Courier";
        ctx.fillText("Skor: " + score, canvasSize/2, canvasSize/2 - 10);
        ctx.fillText("Highscore: " + highscore, canvasSize/2, canvasSize/2 + 20);
        if (score > highscore) { highscore = score; localStorage.setItem("anova_snake_highscore", highscore);
          ctx.fillText("✨ Rekor Baru!", canvasSize/2, canvasSize/2 + 50); }
        restartBtn.style.display = "inline-block";
        pauseBtn.style.display = "none"; startBtn.style.display = "none";
        return;
      }
      snake.unshift(newHead);
      ctx.fillStyle = "#f4a261";
      ctx.font = "14px Courier";
      ctx.textAlign = "left";
      ctx.fillText("Score: " + score, 10, canvasSize - 10);
      ctx.textAlign = "right";
      ctx.fillText("Highscore: " + highscore, canvasSize - 10, canvasSize - 10);
    }
    startBtn.addEventListener("click", initGame);
    restartBtn.addEventListener("click", initGame);
    pauseBtn.addEventListener("click", togglePause);
    document.addEventListener('keydown', (e) => {
      if (!started && (e.key === ' ' || e.key === 'Enter')) initGame();
      else if (started && e.key === ' ') togglePause();
    });
    </script>
    """
    # TINGGI KOMPONEN JUGA DIKECILKAN AGAR PAS
    st.components.v1.html(snake_game_html, height=750)
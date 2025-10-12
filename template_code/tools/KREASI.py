import streamlit as st

st.set_page_config(page_title="Game Ular Python - ANOVA", page_icon="🐍", layout="wide")

# === STYLING CSS UTAMA ===
st.markdown("""
<style>
body {
    background-color: #f7f9fb;
}
.main {
    display: flex;
    justify-content: center;
    align-items: center;
}
.block-container {
    max-width: 1000px;
    /* PERBAIKAN: Mengembalikan padding atas agar judul tidak terpotong */
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# === JUDUL HALAMAN ===
st.markdown("<h2 style='text-align:center; margin-bottom:0;'>🐍 Game Ular Python (Kelompok 04 ANOVA)</h2>", unsafe_allow_html=True)
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# === HTML + JS GAME ===
snake_game_html = """
<div style="display:flex; flex-direction:column; align-items:center; justify-content:center; width:100%;">

  <div style="position:relative; height:60px; margin-bottom:8px;">
    <h1 style="
      color:#c5a253;
      font-family:'Courier New', monospace;
      font-size:32px;
      animation: floating 3s ease-in-out infinite;
      text-shadow:0 0 10px rgba(255,215,100,0.6), 0 0 20px rgba(255,225,150,0.4);
    ">
      ✦ ANOVA ✦
    </h1>
  </div>

  <div style="display:flex; justify-content:center; width:100%;">
    <canvas id="gameCanvas" width="600" height="600" tabindex="0"
      style="
        width: 600px !important;
        height: 600px !important;
        border:3px solid #c5a253;
        background-color:black;
        border-radius:16px;
        box-shadow:0 0 35px rgba(255,215,100,0.4), 0 0 70px rgba(255,225,150,0.3);
        outline:none;
        animation: goldPulse 3.5s ease-in-out infinite;
      ">
    </canvas>
  </div>

  <div style="margin-top:25px;">
    <button id="startBtn" style="
      background: linear-gradient(135deg, #ffb703, #f4a261, #e9c46a);
      color:black;
      font-weight:bold;
      border:none;
      padding:12px 28px;
      border-radius:12px;
      cursor:pointer;
      font-family:'Courier New', monospace;
      font-size:16px;
      box-shadow:0 0 15px rgba(255,200,80,0.7);
      transition:all 0.3s ease;
      ">▶️ Mulai Game</button>

    <button id="restartBtn" style="
      background: linear-gradient(135deg, #f77f00, #f4a261, #e9c46a);
      color:black;
      font-weight:bold;
      border:none;
      padding:12px 28px;
      border-radius:12px;
      cursor:pointer;
      font-family:'Courier New', monospace;
      font-size:16px;
      box-shadow:0 0 15px rgba(255,180,60,0.6);
      transition:all 0.3s ease;
      display:none;
      ">🔁 Mulai Ulang</button>

    <button id="pauseBtn" style="
      background: linear-gradient(135deg, #f4a261, #ffb703, #e9c46a);
      color:black;
      font-weight:bold;
      border:none;
      padding:12px 28px;
      border-radius:12px;
      cursor:pointer;
      font-family:'Courier New', monospace;
      font-size:16px;
      margin-left:8px;
      box-shadow:0 0 15px rgba(255,200,80,0.5);
      display:none;
      transition:all 0.3s ease;
      ">⏸️ Pause</button>
  </div>

  <p style="
    color:#d9c987;
    font-family:Courier;
    font-size:14px;
    margin-top:14px;
    text-shadow:0 0 6px rgba(255,225,150,0.7);
  ">
    Gunakan tombol: <b>W</b> / <b>A</b> / <b>S</b> / <b>D</b> atau panah ⬆️⬅️⬇️➡️ <br>
    Tekan <b>Spasi</b> untuk <i>Pause / Lanjut</i>.
  </p>

</div>

<style>
  @keyframes goldPulse {
    0%, 100% { box-shadow:0 0 35px rgba(255,215,100,0.4), 0 0 70px rgba(255,225,150,0.3); }
    50% { box-shadow:0 0 60px rgba(255,230,150,0.6), 0 0 100px rgba(255,245,180,0.4); }
  }

  @keyframes floating {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
  }

  #startBtn:hover, #pauseBtn:hover, #restartBtn:hover {
    transform: scale(1.08);
  }
</style>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const startBtn = document.getElementById("startBtn");
const restartBtn = document.getElementById("restartBtn");
const pauseBtn = document.getElementById("pauseBtn");

let box = 25;
let snake, food, d, score, game, speed;
let started = false;
let paused = false;
let gameOver = false;
let highscore = localStorage.getItem("anova_snake_highscore") || 0;

function drawStartScreen() {
  ctx.fillStyle = "black";
  ctx.fillRect(0,0,600,600);
  ctx.fillStyle = "#e9c46a";
  ctx.font = "18px Courier";
  ctx.textAlign = "center";
  ctx.fillText("Tekan tombol 'Mulai Game' untuk bermain", 300, 300);
  ctx.font = "16px Courier";
  ctx.fillText("Highscore: " + highscore, 300, 330);
}
drawStartScreen();

function initGame() {
  snake = [{x: 9*box, y: 10*box}];
  food = {x: Math.floor(Math.random()*22+1)*box, y: Math.floor(Math.random()*22+1)*box};
  d = "RIGHT";
  score = 0;
  speed = 100;
  gameOver = false;
  paused = false;
  started = true;

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
    ctx.fillRect(0,0,600,600);
    ctx.fillStyle = "#e9c46a";
    ctx.font = "28px Courier";
    ctx.textAlign = "center";
    ctx.fillText("⏸️ PAUSED", 300, 300);
    pauseBtn.textContent = "▶️ Lanjut";
  } else {
    game = setInterval(draw, speed);
    pauseBtn.textContent = "⏸️ Pause";
  }
}

function collision(head, array){
  for(let i=0; i<array.length; i++){
    if(head.x == array[i].x && head.y == array[i].y){ return true; }
  }
  return false;
}

function draw() {
  ctx.fillStyle = "black";
  ctx.fillRect(0,0,600,600);

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

  let snakeX = snake[0].x;
  let snakeY = snake[0].y;

  if( d == "LEFT") snakeX -= box;
  if( d == "UP") snakeY -= box;
  if( d == "RIGHT") snakeX += box;
  if( d == "DOWN") snakeY += box;

  if(snakeX == food.x && snakeY == food.y){
    score++;
    food = {x: Math.floor(Math.random()*22+1)*box, y: Math.floor(Math.random()*22+1)*box};
    if (speed > 50) {
      speed -= 3;
      clearInterval(game);
      game = setInterval(draw, speed);
    }
  } else {
    snake.pop();
  }

  let newHead = {x: snakeX, y: snakeY};

  if(snakeX < 0 || snakeY < 0 || snakeX >= 600 || snakeY >= 600 || collision(newHead, snake)){
    clearInterval(game);
    gameOver = true;
    started = false;

    ctx.fillStyle = "#f4a261";
    ctx.font = "28px Courier";
    ctx.textAlign = "center";
    ctx.fillText("GAME OVER", 300, 280);
    ctx.font = "20px Courier";
    ctx.fillText("Skor: " + score, 300, 310);
    ctx.fillText("Highscore: " + highscore, 300, 340);

    if (score > highscore) {
      highscore = score;
      localStorage.setItem("anova_snake_highscore", highscore);
      ctx.fillText("✨ Rekor Baru!", 300, 370);
    }

    restartBtn.style.display = "inline-block";
    pauseBtn.style.display = "none";
    startBtn.style.display = "none";
    return;
  }

  snake.unshift(newHead);
  ctx.fillStyle = "#f4a261";
  ctx.font = "16px Courier";
  ctx.textAlign = "left";
  ctx.fillText("Score: " + score, 10, 590);
  ctx.textAlign = "right";
  ctx.fillText("Highscore: " + highscore, 590, 590);
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

st.components.v1.html(snake_game_html, height=900)

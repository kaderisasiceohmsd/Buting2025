import streamlit as st

st.set_page_config(page_title="Game Ular Python - ANOVA", page_icon="🐍", layout="centered")

st.markdown("<h2 style='text-align:center;'>🐍 Game Ular Python (Kelompok 04 ANOVA)</h2>", unsafe_allow_html=True)

snake_game_html = """
<div style="display:flex; flex-direction:column; align-items:center;">

  <!-- Animasi Logo ANOVA -->
  <div style="position:relative; height:60px; margin-bottom:8px;">
    <h1 style="
      color:#c5a253;
      font-family:'Courier New', monospace;
      font-size:28px;
      animation: floating 3s ease-in-out infinite;
      text-shadow:0 0 10px rgba(255,215,100,0.6), 0 0 20px rgba(255,225,150,0.4);
    ">
      ✦ ANOVA ✦
    </h1>
  </div>

  <canvas id="gameCanvas" width="520" height="520"
    style="
      border:3px solid #c5a253;
      background-color:black;
      border-radius:16px;
      box-shadow:0 0 35px rgba(255,215,100,0.4), 0 0 70px rgba(255,225,150,0.3);
      margin-top:10px;
      outline:none;
      animation: goldPulse 3.5s ease-in-out infinite;
    ">
  </canvas>

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
  </div>

  <p style="
    color:#d9c987;
    font-family:Courier;
    font-size:14px;
    margin-top:14px;
    text-shadow:0 0 6px rgba(255,225,150,0.7);
  ">
    Gunakan tombol: <b>W</b> (atas), <b>A</b> (kiri), <b>S</b> (bawah), <b>D</b> (kanan)
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

  #startBtn:hover { transform: scale(1.1); background: linear-gradient(135deg, #f4a261, #ffb703, #e9c46a); }
  #restartBtn:hover { transform: scale(1.1); background: linear-gradient(135deg, #f4a261, #f77f00, #e9c46a); }
</style>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const startBtn = document.getElementById("startBtn");
const restartBtn = document.getElementById("restartBtn");

let box = 25;
let snake;
let food;
let d;
let score;
let game;
let gameOver = false;
let speed = 100;
let started = false;

function drawStartScreen() {
  ctx.fillStyle = "black";
  ctx.fillRect(0,0,520,520);
  ctx.fillStyle = "#e9c46a";
  ctx.font = "18px Courier";
  ctx.textAlign = "center";
  ctx.fillText("Tekan tombol 'Mulai Game' untuk bermain", 260, 260);
}
drawStartScreen();

function initGame() {
  snake = [{x: 9*box, y: 10*box}];
  food = {x: Math.floor(Math.random()*19+1)*box, y: Math.floor(Math.random()*19+1)*box};
  d = "RIGHT";
  score = 0;
  speed = 100;
  gameOver = false;
  started = true;
  restartBtn.style.display = "none";
  startBtn.style.display = "none";
  clearInterval(game);
  game = setInterval(draw, speed);
  canvas.focus();
}

document.addEventListener("keydown", direction);
function direction(event) {
  if (!started) return;
  let key = event.key.toLowerCase();
  if((key === "a" || key === "arrowleft") && d != "RIGHT") d = "LEFT";
  else if((key === "w" || key === "arrowup") && d != "DOWN") d = "UP";
  else if((key === "d" || key === "arrowright") && d != "LEFT") d = "RIGHT";
  else if((key === "s" || key === "arrowdown") && d != "UP") d = "DOWN";
}

function collision(head, array){
  for(let i=0; i<array.length; i++){
    if(head.x == array[i].x && head.y == array[i].y){ return true; }
  }
  return false;
}

function draw() {
  ctx.fillStyle = "black";
  ctx.fillRect(0,0,520,520);

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
    food = {x: Math.floor(Math.random()*19+1)*box, y: Math.floor(Math.random()*19+1)*box};
    if (speed > 50) {
      speed -= 3;
      clearInterval(game);
      game = setInterval(draw, speed);
    }
  } else {
    snake.pop();
  }

  let newHead = {x: snakeX, y: snakeY};

  if(snakeX < 0 || snakeY < 0 || snakeX >= 520 || snakeY >= 520 || collision(newHead, snake)){
    clearInterval(game);
    gameOver = true;
    started = false;
    ctx.fillStyle = "#f4a261";
    ctx.font = "28px Courier";
    ctx.textAlign = "center";
    ctx.fillText("GAME OVER", 260, 250);
    ctx.font = "20px Courier";
    ctx.fillText("Skor: " + score, 260, 280);
    restartBtn.style.display = "inline-block";
    return;
  }

  snake.unshift(newHead);
  ctx.fillStyle = "#f4a261";
  ctx.font = "16px Courier";
  ctx.textAlign = "left";
  ctx.fillText("Score: " + score, 10, 510);
}

startBtn.addEventListener("click", initGame);
restartBtn.addEventListener("click", initGame);
</script>
"""

st.components.v1.html(snake_game_html, height=720)

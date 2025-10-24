import tkinter as tk
import random
from tkinter import messagebox

# === Setup window ===
root = tk.Tk()
root.title("🐠 Temukan Poisson! 🎮")
root.config(bg="#0077b6")
root.geometry("500x600")

title = tk.Label(root, text="🐠 Memory Game: Temukan Poisson 🎮", 
                 font=("Comic Sans MS", 18, "bold"), fg="white", bg="#0077b6")
title.pack(pady=10)

# === Data dasar game ===
icons = ["🐠", "🐡", "🐬", "🐙", "🐋", "🐢", "🪸", "🦀"]
cards = icons * 2
random.shuffle(cards)

buttons = []
flipped = []
matched = 0
score = 0

score_label = tk.Label(root, text=f"Skor: {score}", font=("Comic Sans MS", 14), bg="#0077b6", fg="white")
score_label.pack(pady=5)

# === Grid frame ===
frame = tk.Frame(root, bg="#0077b6")
frame.pack(pady=10)

# === Fungsi klik kartu ===
def flip_card(i):
    global flipped, matched, score
    btn = buttons[i]
    if btn["state"] == "disabled" or len(flipped) == 2:
        return

    btn.config(text=cards[i], bg="white", state="disabled")
    flipped.append((i, cards[i]))

    if len(flipped) == 2:
        root.after(700, check_match)

def check_match():
    global flipped, matched, score
    i1, icon1 = flipped[0]
    i2, icon2 = flipped[1]

    if icon1 == icon2:
        buttons[i1].config(bg="#80ed99")
        buttons[i2].config(bg="#80ed99")
        matched += 2
        score += 10
    else:
        buttons[i1].config(text="❓", state="normal", bg="#caf0f8")
        buttons[i2].config(text="❓", state="normal", bg="#caf0f8")
        score -= 2

    flipped = []
    score_label.config(text=f"Skor: {score}")

    if matched == len(cards):
        messagebox.showinfo("🎉 Selamat!", "Kamu berhasil menemukan semua Poisson! 🌊")
        reset_game()

# === Reset game ===
def reset_game():
    global cards, matched, score
    matched = 0
    score = 0
    score_label.config(text=f"Skor: {score}")
    random.shuffle(cards)
    for btn in buttons:
        btn.config(text="❓", bg="#caf0f8", state="normal")

# === Buat tombol kartu ===
for i in range(16):
    btn = tk.Button(frame, text="❓", font=("Arial", 25), width=4, height=2, 
                    bg="#caf0f8", fg="#03045e", command=lambda i=i: flip_card(i))
    btn.grid(row=i//4, column=i%4, padx=8, pady=8)
    buttons.append(btn)

# === Tombol main lagi ===
reset_btn = tk.Button(root, text="🔄 Main Lagi", font=("Comic Sans MS", 14, "bold"), 
                      bg="#00b4d8", fg="white", relief="ridge", command=reset_game)
reset_btn.pack(pady=20)

# === Efek gelembung sederhana ===
canvas = tk.Canvas(root, width=500, height=150, bg="#0077b6", highlightthickness=0)
canvas.pack()

bubbles = []
for _ in range(15):
    x = random.randint(0, 500)
    y = random.randint(150, 300)
    size = random.randint(10, 30)
    bubble = canvas.create_oval(x, y, x+size, y+size, fill="white", outline="")
    bubbles.append((bubble, size))

def move_bubbles():
    for bubble, size in bubbles:
        canvas.move(bubble, 0, -1)
        coords = canvas.coords(bubble)
        if coords[1] < -30:
            canvas.move(bubble, 0, 180)
    root.after(50, move_bubbles)

move_bubbles()

# === Jalankan window ===
root.mainloop()

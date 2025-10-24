import pygame
import random
import sys
import time

# Inisialisasi pygame
pygame.init()

# Warna
BIRU_LAUT = (0, 119, 182)
PUTIH = (255, 255, 255)
KUNING = (255, 255, 150)

# Ukuran layar
LEBAR = 800
TINGGI = 600
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("🐠 Catch the Poisson Deluxe 🎣")

# Font
font = pygame.font.SysFont("Comic Sans MS", 32)
font_besar = pygame.font.SysFont("Comic Sans MS", 48)

# === Gambar ikan lokal ===
# Bisa ganti dengan gambar PNG lain di foldermu
ikan_img = pygame.Surface((70, 50), pygame.SRCALPHA)
pygame.draw.ellipse(ikan_img, (255, 180, 80), [0, 10, 70, 30])
pygame.draw.polygon(ikan_img, (255, 120, 50), [(60, 10), (70, 25), (60, 40)])

# Variabel permainan
skor = 0
kecepatan = 3
clock = pygame.time.Clock()

# Posisi ikan awal
ikan_x = random.randint(0, LEBAR - 70)
ikan_y = random.randint(0, TINGGI - 70)
ikan_arah_x = random.choice([-1, 1])
ikan_arah_y = random.choice([-1, 1])

# Sparkle efek
sparkles = []

# Typewriter efek
def typewriter(teks, x, y, warna=PUTIH, delay=0.05):
    tampil = ""
    for huruf in teks:
        tampil += huruf
        layar.fill(BIRU_LAUT)
        teks_surface = font_besar.render(tampil, True, warna)
        layar.blit(teks_surface, (x, y))
        pygame.display.flip()
        time.sleep(delay)

# Efek sparkle (gemerlap)
def buat_sparkle():
    sparkle = {
        "x": random.randint(0, LEBAR),
        "y": random.randint(0, TINGGI),
        "radius": random.randint(1, 3),
        "life": random.randint(20, 80)
    }
    sparkles.append(sparkle)

def update_sparkles():
    for sparkle in sparkles:
        sparkle["life"] -= 1
        pygame.draw.circle(layar, PUTIH, (sparkle["x"], sparkle["y"]), sparkle["radius"])
    for s in [s for s in sparkles if s["life"] <= 0]:
        sparkles.remove(s)

# Fungsi teks
def tampilkan_teks(teks, warna, x, y, ukuran=32):
    f = pygame.font.SysFont("Comic Sans MS", ukuran)
    tampil = f.render(teks, True, warna)
    layar.blit(tampil, (x, y))

# Efek gelembung
def gelembung():
    for _ in range(10):
        x = random.randint(0, LEBAR)
        y = random.randint(0, TINGGI)
        radius = random.randint(2, 6)
        pygame.draw.circle(layar, PUTIH, (x, y), radius, 1)

# ===== Layar Pembuka =====
layar.fill(BIRU_LAUT)
typewriter("🐠 Catch the Poisson Deluxe 🎣", 100, 250, KUNING, 0.08)
time.sleep(1)

# ===== Game Loop =====
running = True
while running:
    layar.fill(BIRU_LAUT)
    gelembung()
    buat_sparkle()
    update_sparkles()

    # Gambar ikan
    layar.blit(ikan_img, (ikan_x, ikan_y))

    # Gerakan ikan
    ikan_x += ikan_arah_x * kecepatan
    ikan_y += ikan_arah_y * kecepatan

    # Pantulan di tepi layar
    if ikan_x <= 0 or ikan_x >= LEBAR - 70:
        ikan_arah_x *= -1
    if ikan_y <= 0 or ikan_y >= TINGGI - 50:
        ikan_arah_y *= -1

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if ikan_x < mouse_x < ikan_x + 70 and ikan_y < mouse_y < ikan_y + 50:
                skor += 1
                kecepatan += 0.2
                ikan_x = random.randint(0, LEBAR - 70)
                ikan_y = random.randint(0, TINGGI - 50)

    # Tampilkan skor dan pesan motivasi
    tampilkan_teks(f"Skor: {skor}", KUNING, 20, 20)
    if skor > 0 and skor % 5 == 0:
        tampilkan_teks("✨ Poisson Bangga Padamu! ✨", PUTIH, 220, 60, 28)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

# ===============================
# 📘 Kalkulator Cosval Interaktif
# ===============================
# Dibuat dengan: Streamlit + NumPy + Matplotlib

import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# 🏷️ Judul dan deskripsi aplikasi
# ---------------------------------
st.title("🧮 Kalkulator Cosval Interaktif + Visualisasi Fungsi Cosinus")
st.write("""
Aplikasi ini menghitung **nilai cosinus (cosval)** dari sudut yang kamu pilih,  
dan menampilkan **grafik fungsi cosinus** yang bisa kamu ubah secara interaktif.
""")

# ---------------------------------
# ⚙️ Pilihan mode input
# ---------------------------------
mode = st.radio("Pilih satuan sudut:", ["Derajat", "Radian"])

# ---------------------------------
# 🎚️ Slider untuk memilih sudut
# ---------------------------------
if mode == "Derajat":
    angle = st.slider("Geser untuk memilih sudut (°):", -360, 360, 60)
    angle_rad = math.radians(angle)
else:
    angle = st.slider("Geser untuk memilih sudut (radian):", 
                      float(-2 * math.pi), float(2 * math.pi), 1.0)
    angle_rad = angle

# ---------------------------------
# 🔢 Hitung nilai cosinus
# ---------------------------------
cosval = math.cos(angle_rad)

# ---------------------------------
# 📊 Tampilkan hasil
# ---------------------------------
if mode == "Derajat":
    st.success(f"✅ cos({angle}°) = {cosval:.4f}")
else:
    st.success(f"✅ cos({angle:.2f} rad) = {cosval:.4f}")

# ---------------------------------
# 📈 Visualisasi Fungsi Cosinus
# ---------------------------------
st.subheader("📈 Visualisasi Fungsi Cosinus")

# Buat data untuk grafik
if mode == "Derajat":
    x = np.linspace(-360, 360, 720)
    y = np.cos(np.radians(x))
    titik_x = angle
    titik_y = cosval
else:
    x = np.linspace(-2 * np.pi, 2 * np.pi, 720)
    y = np.cos(x)
    titik_x = angle
    titik_y = cosval

# Plot grafik cosinus
fig, ax = plt.subplots()
ax.plot(x, y, label='cos(x)', color='blue')
ax.scatter(titik_x, titik_y, color='red', label=f'cos({angle}) = {cosval:.4f}')
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)
ax.set_xlabel('Sudut (°)' if mode == "Derajat" else 'Sudut (radian)')
ax.set_ylabel('Nilai cos(x)')
ax.set_title('Grafik Fungsi Cosinus')
ax.legend()
ax.grid(True)

# Tampilkan grafik di Streamlit
st.pyplot(fig)

# ---------------------------------
# 🧠 Informasi tambahan (opsional)
# ---------------------------------
st.info("""
💡 **Catatan:**  
- Nilai cosinus (cosval) selalu berada di antara -1 dan 1.  
- Fungsi cosinus bersifat periodik, artinya bentuk gelombangnya berulang setiap 360° (atau 2π radian).
""")

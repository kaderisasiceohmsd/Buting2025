import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

st.title("🎵 Visualizer Gelombang Suara")

# Pilih jenis gelombang
wave_type = st.selectbox("Pilih jenis gelombang:", ["Sinus", "Kotak", "Segitiga"])

# Parameter
freq = st.slider("Frekuensi (Hz)", 1, 1000, 10)
amp = st.slider("Amplitudo", 1, 10, 1)
duration = st.slider("Durasi (detik)", 1, 5, 1)
sampling_rate = 5000  # Hz

# Buat sumbu waktu
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate gelombang
if wave_type == "Sinus":
    y = amp * np.sin(2 * np.pi * freq * t)
elif wave_type == "Kotak":
    y = amp * signal.square(2 * np.pi * freq * t)
elif wave_type == "Segitiga":
    y = amp * signal.sawtooth(2 * np.pi * freq * t, 0.5)

# Plot domain waktu
st.subheader("Domain Waktu")
fig1, ax1 = plt.subplots()
ax1.plot(t[:1000], y[:1000])  # tampilkan sebagian kecil agar jelas
ax1.set_xlabel("Waktu (detik)")
ax1.set_ylabel("Amplitudo")
ax1.set_title(f"Gelombang {wave_type}")
st.pyplot(fig1)

# Plot spektrum frekuensi (FFT)
st.subheader("Spektrum Frekuensi (FFT)")
N = len(y)
yf = np.fft.fft(y)
xf = np.fft.fftfreq(N, 1 / sampling_rate)

fig2, ax2 = plt.subplots()
ax2.plot(xf[:N // 2], np.abs(yf[:N // 2]) * 1/N)
ax2.set_xlabel("Frekuensi (Hz)")
ax2.set_ylabel("Magnitudo")
ax2.set_title("Spektrum Frekuensi")
st.pyplot(fig2)

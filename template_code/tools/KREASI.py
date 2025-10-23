import streamlit as st
import numpy as np
import pandas as pd
import random

# Judul aplikasi
st.title("🌦️ Simulasi Perkiraan Cuaca Lampung dengan Markov Chain")

st.write("""
Aplikasi ini menggunakan model **Markov Chain** untuk memperkirakan cuaca berdasarkan pola transisi sederhana.
Contoh data ini disimulasikan dari pola cuaca umum di **Lampung**.
""")

# State cuaca
states = ["Cerah", "Berawan", "Hujan"]

# Matriks probabilitas transisi (diasumsikan)
transition_matrix = np.array([
    [0.6, 0.3, 0.1],  # Dari Cerah -> Cerah/Berawan/Hujan
    [0.2, 0.5, 0.3],  # Dari Berawan -> Cerah/Berawan/Hujan
    [0.1, 0.4, 0.5]   # Dari Hujan -> Cerah/Berawan/Hujan
])

# Menampilkan matriks transisi
st.subheader("📊 Matriks Probabilitas Transisi")
df = pd.DataFrame(transition_matrix, columns=states, index=states)
st.dataframe(df.style.format("{:.2f}"))

# Input pengguna
st.subheader("🔧 Pengaturan Simulasi")
start_state = st.selectbox("Pilih kondisi cuaca awal:", states)
days = st.slider("Jumlah hari yang ingin diprediksi:", 1, 30, 10)

# Fungsi simulasi Markov Chain
def predict_weather(start, transition_matrix, states, days):
    current_state = states.index(start)
    predictions = [start]
    for _ in range(days):
        current_state = np.random.choice(
            range(len(states)), 
            p=transition_matrix[current_state]
        )
        predictions.append(states[current_state])
    return predictions

# Jalankan simulasi
if st.button("Mulai Simulasi"):
    results = predict_weather(start_state, transition_matrix, states, days)
    
    st.subheader("📅 Hasil Prediksi Cuaca:")
    forecast_df = pd.DataFrame({
        "Hari": [f"Hari {i}" for i in range(len(results))],
        "Perkiraan Cuaca": results
    })
    st.table(forecast_df)
    
    # Hitung frekuensi hasil
    st.subheader("📈 Frekuensi Cuaca yang Diprediksi")
    freq = pd.Series(results).value_counts()
    st.bar_chart(freq)

st.caption("Model ini disederhanakan untuk tujuan kreasi dan mungkin tidak mencerminkan kondisi cuaca sebenarnya di Lampung.")
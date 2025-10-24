import streamlit as st
import numpy as np
import pandas as pd

# Judul
st.title("Simulasi Markov Chain")

# Input parameter
states_input = st.text_input("Masukkan state (pisahkan koma)", "Sunny,Cloudy,Rainy")
states = [s.strip() for s in states_input.split(",")]

n = len(states)
# Input matriks transisi sebagai CSV-like atau entry per baris
trans_matrix = []
st.write("Masukkan matriks transisi (baris per state):")
for i, s in enumerate(states):
    row = st.text_input(f"Probabilitas dari {s} ke masing-masing state (pisah koma)", 
                        value="0.7,0.2,0.1" if i==0 else "0.3,0.4,0.3")
    probs = [float(x.strip()) for x in row.split(",")]
    trans_matrix.append(probs)

P = np.array(trans_matrix)
# Validasi bahwa setiap baris sum = 1
if not np.allclose(P.sum(axis=1), 1.0):
    st.error("Setiap baris matriks transisi harus jumlahkan ke 1")

# Pilih initial state
initial_state = st.selectbox("Initial State", states, index=0)
initial_idx = states.index(initial_state)

# Jumlah langkah simulasi
steps = st.number_input("Jumlah langkah simulasi", min_value=1, max_value=1000, value=10)

if st.button("Jalankan simulasi"):
    # Simulasi random walk
    curr = initial_idx
    seq = [states[curr]]
    for _ in range(int(steps)):
        curr = np.random.choice(np.arange(n), p=P[curr])
        seq.append(states[curr])
    st.write("Hasil urutan state:", seq)

    # Simulasi distribusi probabilitas seiring waktu
    # menggunakan multiplikasi vektor awal * P^t
    v0 = np.zeros(n)
    v0[initial_idx] = 1.0
    history = [v0]
    v = v0.copy()
    for t in range(1, steps+1):
        v = v.dot(P)
        history.append(v)
    df_hist = pd.DataFrame(history, columns=states)
    st.line_chart(df_hist)

    st.write("Distribusi akhir:", dict(zip(states, history[-1])))

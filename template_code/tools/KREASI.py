import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🎮 Playground Operasi Tensor Dasar + Heatmap")

# Pilih ukuran tensor
rows = st.slider("Jumlah baris", 2, 6, 3)
cols = st.slider("Jumlah kolom", 2, 6, 3)

# Buat dua tensor random
A = np.random.randint(0, 10, size=(rows, cols))
B = np.random.randint(0, 10, size=(rows, cols))

st.subheader("Tensor A")
st.dataframe(pd.DataFrame(A))

st.subheader("Tensor B")
st.dataframe(pd.DataFrame(B))

# Pilih operasi
opsi = st.selectbox(
    "Pilih operasi tensor:",
    ["Penjumlahan (A + B)",
     "Perkalian Elemen (A * B)",
     "Transpose A",
     "Transpose B",
     "Perkalian Matriks (A @ Bᵀ)"]
)

st.subheader("Hasil Operasi")

# Fungsi untuk menampilkan heatmap
def show_heatmap(matrix, title):
    fig, ax = plt.subplots()
    sns.heatmap(matrix, annot=True, fmt="d", cmap="YlGnBu", cbar=True, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)

# Jalankan operasi sesuai pilihan
if opsi == "Penjumlahan (A + B)":
    result = A + B
    st.dataframe(pd.DataFrame(result))
    show_heatmap(result, "Heatmap A + B")

elif opsi == "Perkalian Elemen (A * B)":
    result = A * B
    st.dataframe(pd.DataFrame(result))
    show_heatmap(result, "Heatmap A * B")

elif opsi == "Transpose A":
    result = A.T
    st.dataframe(pd.DataFrame(result))
    show_heatmap(result, "Heatmap Aᵀ")

elif opsi == "Transpose B":
    result = B.T
    st.dataframe(pd.DataFrame(result))
    show_heatmap(result, "Heatmap Bᵀ")

elif opsi == "Perkalian Matriks (A @ Bᵀ)":
    if A.shape[1] == B.shape[1]:  # kolom A = kolom B
        result = A @ B.T
        st.dataframe(pd.DataFrame(result))
        show_heatmap(result, "Heatmap A @ Bᵀ")
    else:
        st.warning("Ukuran tidak cocok untuk perkalian matriks (kolom A ≠ kolom B).")

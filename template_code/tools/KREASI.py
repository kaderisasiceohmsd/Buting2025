import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# === 1. Baca data ===
df = pd.read_csv("tools/understat.com.csv")
# Convert date column directly to year since it contains year values
df['year'] = df['date']  # date column already contains years

st.title("Analisis xG Sepak Bola")
st.markdown("Gunakan slider di bawah untuk memilih tahun dan melihat rata-rata xG")

# === 2. Slider Tahun ===
min_year = int(df['year'].min())
max_year = int(df['year'].max())
if min_year == max_year:
    max_year = min_year + 1  # Ensure we have a valid range
tahun = st.slider("Pilih Tahun", min_year, max_year, min_year)

# === 3. Hitung dan tampilkan xG rata-rata ===
subset = df[df['year'] == tahun]

if subset.empty:
    st.warning(f"Tidak ada data untuk tahun {tahun}")
else:
    rata2_xg = subset['xG'].mean()
    st.metric(label=f"Rata-rata xG tahun {tahun}", value=f"{rata2_xg:.2f}")

    # Grafik per tim
    fig, ax = plt.subplots(figsize=(12, 6))
    team_xg = subset.groupby('team')['xG'].mean().sort_values(ascending=False)
    ax.bar(range(len(team_xg)), team_xg.values)
    ax.set_xticks(range(len(team_xg)))
    ax.set_xticklabels(team_xg.index, rotation=45, ha='right')
    ax.set_xlabel("Tim")
    ax.set_ylabel("xG")
    ax.set_title(f"Rata-rata xG per Tim pada Tahun {tahun}")
    plt.tight_layout()
    st.pyplot(fig)
subset = df[df['year'] == tahun]

if subset.empty:
    st.warning(f"Tidak ada data untuk tahun {tahun}")
else:
    # Perhitungan xG rata-rata keseluruhan
    rata2_xg = subset['xG'].mean()
    st.metric(label=f"Rata-rata xG tahun {tahun}", value=f"{rata2_xg:.2f}")

    # Grafik 10 Tim Teratas
    st.subheader(f"10 Tim Teratas Berdasarkan Rata-rata xG pada Tahun {tahun}")
    
    # Kelompokkan, hitung rata-rata, urutkan, dan ambil 10 teratas
    team_xg_all = subset.groupby('team')['xG'].mean().sort_values(ascending=False)
    team_xg_top10 = team_xg_all.head(10) # <--- Perubahan utama di sini!

    if team_xg_top10.empty:
        st.warning(f"Tidak ada data tim yang cukup untuk ditampilkan pada tahun {tahun}.")
    else:
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Buat bar chart dari 10 tim teratas
        ax.bar(range(len(team_xg_top10)), team_xg_top10.values, color='skyblue')
        
        # Atur label sumbu x
        ax.set_xticks(range(len(team_xg_top10)))
        ax.set_xticklabels(team_xg_top10.index, rotation=45, ha='right')
        
        # Tambahkan label dan judul
        ax.set_xlabel("Tim")
        ax.set_ylabel("Rata-rata xG")
        ax.set_title(f"10 Tim Teratas Berdasarkan Rata-rata xG pada Tahun {tahun}")
        
        plt.tight_layout()
        st.pyplot(fig)
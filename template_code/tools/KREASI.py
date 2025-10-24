import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# === 1. Baca data (efisien) ===
@st.cache_data(show_spinner=False)
def load_data(path: str, nrows: int | None = None) -> pd.DataFrame:
    """Load CSV efficiently. Will persist a parquet copy next to the CSV for faster subsequent loads.

    - only reads three columns we need (date/team/xG) to reduce memory and I/O
    - if a parquet file exists it will be used instead
    - the function is cached by Streamlit so repeated calls are fast
    """
    parquet_path = path.replace('.csv', '.parquet')
    if os.path.exists(parquet_path):
        try:
            return pd.read_parquet(parquet_path)
        except Exception:
            # fall back to CSV if parquet can't be read
            pass

    usecols = ['date', 'team', 'xG']
    df = pd.read_csv(path, usecols=usecols, nrows=nrows, low_memory=False)

    # try to write a parquet copy for faster future loads (best-effort)
    try:
        df.to_parquet(parquet_path)
    except Exception:
        pass

    return df

st.title("Analisis Sepak Bola")
st.markdown("Gunakan slider di bawah untuk memilih tahun yang ingin dilihat")

# === 2. Slider Tahun ===
with st.spinner("Memuat data (cepat)..."):
    # for development you can pass nrows=1000 to load a slice and iterate faster
    csv_path = os.path.join(os.path.dirname(__file__), "understat.com.csv")
    df = load_data(csv_path)

# Convert/normalize year column
if df['date'].dtype == 'int64' or df['date'].astype(str).str.match(r'^\d{4}$').all():
    df['year'] = pd.to_numeric(df['date'])
else:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year.fillna(0).astype(int)

min_year = int(df['year'].min())
max_year = int(df['year'].max())
if min_year == max_year:
    max_year = min_year + 1  # Ensure we have a valid range
tahun = st.slider("Pilih Tahun", min_year, max_year, min_year)

# === 3. Analisis dan Visualisasi ===
subset = df[df['year'] == tahun]

if subset.empty:
    st.warning(f"Tidak ada data untuk tahun {tahun}")
else:
    # === Bagian 1: Semua Tim ===
    st.subheader(f"Rata-rata xG per Tim pada Tahun {tahun}")
    
    # Hitung rata-rata xG seluruh tim
    team_xg_all = subset.groupby('team')['xG'].mean().sort_values(ascending=False)
    rata2_xg_all = team_xg_all.mean()
    st.metric(label=f"Rata-rata xG Seluruh Tim tahun {tahun}", value=f"{rata2_xg_all:.2f}")
    
    # Grafik seluruh tim
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.bar(range(len(team_xg_all)), team_xg_all.values, color='lightblue')
    ax1.set_xticks(range(len(team_xg_all)))
    ax1.set_xticklabels(team_xg_all.index, rotation=45, ha='right')
    ax1.set_xlabel("Tim")
    ax1.set_ylabel("Rata-rata xG")
    ax1.set_title(f"Rata-rata xG Seluruh Tim pada Tahun {tahun}")
    plt.tight_layout()
    st.pyplot(fig1)
    
    # === Bagian 2: 10 Tim Teratas ===
    st.subheader(f"Rata-rata xG 10 Tim Terbaik Tahun {tahun}")
    
    # Ambil dan tampilkan data 10 tim teratas
    team_xg_top10 = team_xg_all.head(10)
    rata2_xg_top10 = team_xg_top10.mean()
    st.metric(label=f"Rata-rata xG 10 Tim Teratas tahun {tahun}", value=f"{rata2_xg_top10:.2f}")
    
    # Grafik 10 tim teratas
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.bar(range(len(team_xg_top10)), team_xg_top10.values, color='skyblue')
    ax2.set_xticks(range(len(team_xg_top10)))
    ax2.set_xticklabels(team_xg_top10.index, rotation=45, ha='right')
    ax2.set_xlabel("Tim")
    ax2.set_ylabel("Rata-rata xG")
    ax2.set_title(f"10 Tim Teratas Berdasarkan Rata-rata xG pada Tahun {tahun}")
    plt.tight_layout()
    st.pyplot(fig2)
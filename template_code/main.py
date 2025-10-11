import streamlit as st
from pathlib import Path

# ===============================
# Konfigurasi awal
# ===============================
st.set_page_config(page_title="Nama Kelompok", layout="wide")

# Inisialisasi session_state agar tidak error saat reload
if "pindah" not in st.session_state:
    st.session_state.pindah = True

# ===============================
# Halaman Utama
# ===============================
Homepage = st.Page(
    "Halaman Utama/halaman_utama.py",
    title="Nama_Kelompok",
    default=True
)

# ===============================
# Buku Kating
# ===============================
Mahasiswa1 = st.Page(
    "Buku Kating/106_Bima_Ekayasa.py",
    title="106 - Bima Ekayasa",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/014_Aqila_Zayyan_Salsabil.py",   # pastikan nama file-nya benar!
    title="014 - Aqila Zayyan Salsabil",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/126_Faizatun_Najmi.py",
    title="126 - Faizatun Najmi",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/039_Manuel_Frederika.py",
    title="039 - Manuel Frederika",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/027_Sherena_Florencia.py",
    title="027 - Sherena Florencia",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/098_Edsel_Adya_Pradipta.py",
    title="098 - Edsel Adya Pradipta",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/128_Muhammad_Harvinsyah.py",
    title="128 - Muhammad Harvinsyah",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/113_Ahmad_Bimo_Akbar_Arkana_Putra.py",
    title="113 - Ahmad Bimo Akbar Arkana Putra",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/080_Abigael_Limbong.py",
    title="080 - Abigael Limbong",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/075_Faiza_Try_Anjani.py",
    title="075 - Faiza Try Anjani",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/074_Saskia_Nova_Magdalena.py",
    title="074 - Saskia Nova Magdalena",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/061_Daffa_Kharisma_Adzana.py",
    title="061 - Daffa Kharisma Adzana",
    icon=":material/person:",
)
Mahasiswa13 = st.Page(
    "Buku Kating/035_Tubagus_Abdani_Pamungkas.py",
    title="035 - Tubagus Abdani Pamungkas",
    icon=":material/person:",
)

# ===============================
# Tools
# ===============================
KREASI = st.Page(
    "tools/KREASI.py",
    title="KREASI",
    icon=":material/search:",
)
KREASII = st.Page(
    "tools/KREASII.py",
    title="KREASII",
    icon=":material/search:",
)

# ===============================
# Navigasi halaman
# ===============================
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [
                Mahasiswa1,
                Mahasiswa2,
                Mahasiswa3,
                Mahasiswa4,
                Mahasiswa5,
                Mahasiswa6,
                Mahasiswa7,
                Mahasiswa8,
                Mahasiswa9,
                Mahasiswa10,
                Mahasiswa11,
                Mahasiswa12,
                Mahasiswa13,
            ],
            "Try Me !!": [KREASI, KREASII],
        }
    )
    pg.run()
else:
    st.write("Maaf Anda kurang beruntung :(")

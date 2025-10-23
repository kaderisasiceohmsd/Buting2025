import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia
st.session_state.pindah = True

# Halaman utama
Homepage = st.Page(
    "Halaman Utama/halaman_utama.py",
    title="ANOVA",
    default=True
)

# Buku Kating Pages

Mahasiswa1 = st.Page(
    "Buku Kating/010_Asri Meilani.py",
    title="010 - Asri Meilani",
    icon=":material/person:",
)

Mahasiswa2 = st.Page(
    "Buku Kating/043_Difanya Husakina.py",
    title="043 - Difanya Husakina",
    icon=":material/person:",
)

Mahasiswa3 = st.Page(
    "Buku Kating/049_Cerine Sihotang.py",
    title="049 - Cerine Sihotang",
    icon=":material/person:",
)

Mahasiswa4 = st.Page(
    "Buku Kating/050_Anash Tasya Ausyaqila.py",
    title="050 - Anash Tasya Ausyaqila",
    icon=":material/person:",
)

Mahasiswa5 = st.Page(
    "Buku Kating/070_Fitra Pratama Mega.py",
    title="070 - Fitra Pratama Mega",
    icon=":material/person:",
)

Mahasiswa6 = st.Page(
    "Buku Kating/101_Jeremia Halim.py",
    title="101 - Jeremia Halim",
    icon=":material/person:",
)

Mahasiswa7 = st.Page(
    "Buku Kating/110_Afriza Azmi.py",
    title="110 - Afriza Azmi",
    icon=":material/person:",
)

Mahasiswa8 = st.Page(
    "Buku Kating/121_Jona Timothy Ogatse Panjaitan.py",
    title="121 - Jona Timothy Ogatse Panjaitan",
    icon=":material/person:",
)

Mahasiswa9 = st.Page(
    "Buku Kating/124_Shafa Delaila Azzahra.py",
    title="124 - Shafa Delaila Azzahra",
    icon=":material/person:",
)

Mahasiswa10 = st.Page(
    "Buku Kating/130_Ahmad Zidane Rabbaanee.py",
    title="130 - Ahmad Zidane Rabbaanee",
    icon=":material/person:",
)

# Tools Pages
KREASI = st.Page("tools/KREASI.py", title="WeatherForge: Climate Simulation Lab", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="ANOVA ODYSSEY", icon=":material/search:")

# Navigasi utama
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
            ],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(")

pg.run()

import streamlit as st

# 🌊 CSS animasi ombak laut + gradasi warna custom
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #1C3B50, #2E5871, #4C7084, #7A8D97, #D7C6BB);
    margin: 0;
    overflow-x: hidden;
}

/* Lapisan ombak bergerak di bawah */
.wave {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 200%;
    height: 100px;
    background-repeat: repeat-x;
    background-size: 50% 100px;
    opacity: 0.5;
    animation: moveWave 10s linear infinite;
}

/* Ombak pertama */
.wave1 {
    background-image: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.8), rgba(255,255,255,0) 70%);
    animation-delay: 0s;
    bottom: 0;
    opacity: 0.4;
}

/* Ombak kedua (lebih lembut) */
.wave2 {
    background-image: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.5), rgba(255,255,255,0) 70%);
    animation-delay: -5s;
    bottom: 10px;
    opacity: 0.2;
}

@keyframes moveWave {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
</style>

<div class="wave wave1"></div>
<div class="wave wave2"></div>
""", unsafe_allow_html=True)

# session state agar ketika pindah page tidak berubah data yang tersedia
st.session_state.pindah = True

Homepage = st.Page(
    "Halaman Utama/halaman_utama.py",
    title="POISSON",
    default=True
)

Mahasiswa1 = st.Page(
    "Buku Kating/106_Bima Ekayasa.py",
    title="106 - Bima Ekayasa",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/⁠014_Aqila Zayyan Salsabil.py",
    title="014 - Aqila Zayyan Salsabil",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/126_Faizatun Najmi.py",
    title="126 - Faizatun Najmi",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/039_Manuel Frederika.py",
    title="039 - Manuel Frederika",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/027_Sherena Florencia.py",
    title="027 - Sherena Florencia",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/098_Edsel Adya Pradipta.py",
    title="098 - Edsel Adya Pradipta",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/128_Muhammad Harvinsyah.py",
    title="128 - Muhammad Harvinsyah",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/113_Ahmad Bimo Akbar Arkana Putra.py",
    title="113 - Ahmad Bimo Akbar Arkana Putra",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/080_Abigael Limbong.py",
    title="080 - Abigael Limbong",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/075_Faiza Try Anjani.py",
    title="075 - Faiza Try Anjani",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/074_Saskia Nova Magdalena.py",
    title="074 - Saskia Nova Magdalena",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/061_Daffa Kharisma Adzana.py",
    title="061 - Daffa Kharisma Adzana",
    icon=":material/person:",
)
Mahasiswa13 = st.Page(
    "Buku Kating/035_Tubagus Abdani Pamungkas.py",
    title="035 - Tubagus Abdani Pamungkas",
    icon=":material/person:",
)

# Tools
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

# Navigasi halaman
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [
                Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5,
                Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10,
                Mahasiswa11, Mahasiswa12, Mahasiswa13
            ],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung teman-teman :(")

# Jalankan navigasi (harus di luar if)
pg.run()

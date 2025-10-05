import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Nama_Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/106_Bima Ekayasa.py",
    title="106 - Bima Ekayasa",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/014_Aqila Zayyan Salsabil.py",
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

#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
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
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()


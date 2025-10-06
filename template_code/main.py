import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Nama_Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/053_Kaleb Filbert Istel.py",
    title="053 - Kaleb Filbert Istel",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/006_Alfaya Rafif Abiyyi.py",
    title="006 - Alfaya Rafif Abiyyi",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/015_Siti Sarifah.py",
    title="015 - Siti Sarifah",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/020_Hani Qurrota Aini.py",
    title="020 - Hani Qurrota Aini",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/029_Euodia Meiliana Friedita",
    title="029 - Euodia Meiliana Friedita",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/044_Selma Siti Aisyah.py",
    title="044 - Selma Siti Aisyah",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/048_Nabila Nur Azizah.py",
    title="048 - Nabila Nur Azizah",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/068_Gustin H. Tampubolon.py",
    title="068 - Gustin H. Tampubolon",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/085_Lucia Advencia Rachel Nainggolan.py",
    title="085 - Lucia Advencia Rachel Nainggolan",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/103_Danil Nur Fadillah.py",
    title="103 - Danil Nur Fadillah",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/107_Cika Adelia Br Marbun.py",
    title="107 - Cika Adelia Br Marbun",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()


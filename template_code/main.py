import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="COSVAL",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/099_Muhammad Syafiqul Falakh.py",
    title="099 - Muhammad Syafiqul Falakh",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/038_Audina Fitria.py",
    title="038 - Audina Fitria",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/066_Juwita Sari.py",
    title="066 - Juwita Sari",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/056_Putri Manna Anantama Simbolon.py",
    title="056 - Putri Manna Anantama Simbolon",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/094_jaya Saputra Tamba.py",
    title="094 - Jaya Saputra Tamba",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/105_Lovianorasaragih.py",
    title="105 - Lovianorasaragih",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/026_Farhanah Hadaya Fatin.py",
    title="026 - Farhanah Hadaya Fatin",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/026_Farhanah Hadaya Fatin.py",
    title="026 - Farhanah Hadaya Fatin",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/026_Farhanah Hadaya Fatin.py",
    title="026 - Farhanah Hadaya Fatin",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()


import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Greedy",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/012_Haikal Seventino Tamba.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/059_Queenta thifaal Nabila.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/069_Gio Silma.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/037_Charrlindah.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/127_Risa Romadona.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/055_Indah Julia Mawar Pratiwi.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/007_Rafli Al Mansyah Tambunan.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/123_Najwa Putri Yopu.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/018_Fislam Fahturrahman.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/072_Wielman Itolo Walawa.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/002_Salsabila Nazwa Putri.py",
    title="117 - Nobel Nizam Fathirizki",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/028_Ashila Islamisahfa Vanisha.py",
    title="117 - Nobel Nizam Fathirizki",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()


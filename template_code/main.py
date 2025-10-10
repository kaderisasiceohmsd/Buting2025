import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Nama_Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/021_Favian Arkaanda.py",
    title="021 - Favian Arkaanda",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/031_Muhammad Razan Maulana Pratama.py",
    title="031 - Muhammad Razan Maulana Pratama",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/047_Muhammad Afdal Lutfi.py",
    title="047 - Muhammad Afdal Lutfi",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/054_Nazlah Auliya.py",
    title="054 - Nazlah Auliya",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/060_Andra Ilham Bintang.py",
    title="060 - Andra Ilham Bintang",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/067_Ghiyats Thabularasa Meardhy.py",
    title="067 - Ghiyats Thabularasa Meardhy",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/088_Elsa Sitorus.py",
    title="088 - Elsa Sitorus",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/091_Alya Ramadhanti.py",
    title="091 - Alya Ramadhanti",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/095_Della Ainisa Fitri.py",
    title="095 - Della Ainisa Fitri",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/096_Aisyah Khairunisa.py",
    title="096 - Aisyah Khairunisa",
    icon=":material/person:",
)
Mahasisw11 = st.Page(
    "Buku Kating/100_Rozak Ramdani.py",
    title="100 - Rozak Ramdani",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/104_Felisya Nabila Putri Nugroho.py",
    title="104 - Felisya Putri Nugroho",
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
            "Buku Kating": [Mahasiswa1],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()


import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Nama_Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/001_Gathfan Nadif Ali.py",
    title="001 - Gathfan Nadif Ali",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/003_Bryan Paskah Telaumbanua.py",
    title="003 - Bryan Paskah Telaumbanua",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/008_Afdhal Rahmad Setiawan.py",
    title="008 - Afdhal Rahmad Setiawan",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/019_Allisha.py",
    title="019 - Allisha",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/078_Vannisa Ramadhani.py",
    title="078 - Vannisa Ramadhani",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/082_Sekar Dini Widya Putri.py",
    title="082 - Sekar Dini Widya Putri",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/083_Adinda Deswita Maharani.py",
    title="083 - Adinda Deswita Maharani",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/090_Salavi Naharani.py",
    title="090 - Salavi Naharani",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/097_Bunga Clarisa Sefa.py",
    title="097 - Bunga Clarisa Sefa",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/114_Hazel Mahesa Handhaka.py",
    title="114 - Hazel Mahesa Handhaka",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/131_Dafa Elpriza.py",
    title="131 - Dafa Elpriza",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, 
                            Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, 
                            Mahasiswa9, Mahasiswa10, Mahasiswa11],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()


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



#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()


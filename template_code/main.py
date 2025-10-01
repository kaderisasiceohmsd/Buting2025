import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Pandas",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/115_Rifky Henry Ferdianto.py",
    title="115 - Rifky Henry Ferdianto",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/034_Suci Aulia.py",
    title="034 - Suci Aulia",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/118_Dimas Arya Ramadhan.py",
    title="118 - Dimas Arya Ramadhan",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/108_Ayake Alfatih Ramadan.py",
    title="108 - Ayake Alfatih Ramadan",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/051_Najla Nursyifa.py",
    title="051 - Najla Nursyifa",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/046_Teresa Christiani Purba.py",
    title="046 - Teresa Christiani Purba",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/042_Afghanis Nursholehatunnisa.py",
    title="042 - Afghanis Nursholehatunnisa",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/017_Caesar Ozora Alrando.py",
    title="017 - Caesar Ozora Alrando",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/016_Layina Ropiqo.py",
    title="016 - Layina Ropiqo",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/015_Ni Made Okta Viola Darma Putri.py",
    title="015 - Ni Made Okta Viola Darma Putri",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/013_Hasan Nur Ramadhan.py",
    title="013 - Hasan Nur Ramadhan",
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
            "Buku Kating": [Mahasiswa1,Mahasiswa2,Mahasiswa3,Mahasiswa4,Mahasiswa5,Mahasiswa6,Mahasiswa7,Mahasiswa8,Mahasiswa9,Mahasiswa10,Mahasiswa11],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()


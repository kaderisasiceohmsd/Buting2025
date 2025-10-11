import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Bayessian",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/063_Fernando Dimetrius Barus.py",
    title="063 - Fernando Dimetrius Barus",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/041_Azzelya Thianandry.py",
    title="041 - Azzelya Thianandry",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/024_Yollanda Agustina.py",
    title="024 - Yollanda Agustina",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/036_Rafa Sabina Fahimah.py",
    title="036 - Rafa Sabina Fahimah",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/052_Moch. Iqbal Az-Zahir.py",
    title="052 - Moch. Iqbal Az-Zahir",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/064_Hafidz Wahdiansyah.py",
    title="064 - Hafidz Wahdiansyah",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/081_Muhammad Fathiy Zumar Yazid.py",
    title="081_Muhammad Fathiy Zumar Yazid",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/092_Muhammad Alsi Syahrulloh.py",
    title="092 - Muhammad Alsi Syahrulloh",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/093_Muhammad Rizaldi.py",
    title="093_Muhammad Rizaldi",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/112_Zannuba arifah ilman.py",
    title="112 - Zannuba arifah ilman",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/119_Yulia Kristine Malau.py",
    title="119 - Yulia Kristine Malau",
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


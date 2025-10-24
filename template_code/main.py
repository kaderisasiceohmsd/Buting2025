import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="JACOBI",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/009_Anggun Nita.py",
    title="009 - Anggun Nita",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/022_Riska Erlis Dayu Tiara.py",
    title="022 - Riska Erlis Dayu Tiara",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/023_Jacinda Kesya Alvara.py",
    title="023 - Jacinda Kesya Alvara",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/025_Gh Mikael Niko Antoni Setiadi.py",
    title="025 - Gh Mikael Niko Antoni Setiadi",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/032_Raihan Azwar Faqih Wijaya.py",
    title="032 - Raihan Azwar Faqih Wijaya",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/033_Helmy Surya Pratama.py",
    title="033 - Helmy Surya Pratama",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/062_Fadya Izzatul Aini.py",
    title="062 - Fadya Izzatul Aini",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/077_Indah Khairunisa.py",
    title="077 - Indah Khairunisa",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/084_Dwi Rahma Fitriani.py",
    title="084 - Dwi Rahma Fitriani",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/122_Raisya Izzati Harira.py",
    title="122 - Raisya Izzati Harira",
    icon=":material/person:",
)


#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="Jacobi", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="Tebak Angka", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10],
            "Kreasi Jacobi!!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 

st.markdown("""
<style>
[data-testid="stSidebar"] {
    position: relative;
    background: #B8D5F3;
    color: #000000;
    overflow: hidden;
}

[data-testid="stSidebar"]::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, #5B3BC4, #B8D5F3);
    background-size: 200% 200%;
    opacity: 0.9;
    animation: gradientShift 10s ease-in-out infinite;
    z-index: -1;
}

@keyframes gradientShift {
    0% { background-position: 0% 0%; }
    50% { background-position: 0% 100%; }
    100% { background-position: 0% 0%; }
}

[data-testid="stSidebar"] a {
    color: #000000;
    font-weight: 500;
    position: relative;
    z-index: 1;
    transition: color 0.3s ease, text-shadow 0.3s ease;
}

[data-testid="stSidebar"] a:hover {
    color: #ffffff;
    text-shadow: 0 0 6px rgba(255,255,255,0.8);
}
</style>
""", unsafe_allow_html=True)

pg.run()


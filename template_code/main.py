import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia
st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Tensor",
    default=True)

Mahasiswa1 = st.Page("Buku Kating/021_Favian Arkaanda.py",
    title="021 - Favian Arkaanda",
    icon=":material/person:",
)
Mahasiswa2 = st.Page("Buku Kating/031_Muhammad Razan Maulana Pratama.py",
    title="031 - Muhammad Razan Maulana Pratama",
    icon=":material/person:",
)
Mahasiswa3 = st.Page("Buku Kating/047_Muhammad Afdal Lutfi.py",
    title="047 - Muhammad Afdal Lutfi",
    icon=":material/person:",
)
Mahasiswa4 = st.Page("Buku Kating/054_Nazlah Auliya.py",
    title="054 - Nazlah Auliya",
    icon=":material/person:",
)
Mahasiswa5 = st.Page("Buku Kating/060_Andra Ilham Bintang.py",
    title="060 - Andra Ilham Bintang",
    icon=":material/person:",
)
Mahasiswa6 = st.Page("Buku Kating/067_Ghiyats Thabularasa Meardhy.py",
    title="067 - Ghiyats Thabularasa Meardhy",
    icon=":material/person:",
)
Mahasiswa7 = st.Page("Buku Kating/088_Elsa Sitorus.py",
    title="088 - Elsa Sitorus",
    icon=":material/person:",
)
Mahasiswa8 = st.Page("Buku Kating/091_Alya Ramadhanti.py",
    title="091 - Alya Ramadhanti",
    icon=":material/person:",
)
Mahasiswa9 = st.Page("Buku Kating/095_Della Ainisa Fitri.py",
    title="095 - Della Ainisa Fitri",
    icon=":material/person:",
)
Mahasiswa10 = st.Page("Buku Kating/096_Aisyah Khairunisa.py",
    title="096 - Aisyah Khairunisa",
    icon=":material/person:",
)
Mahasiswa11 = st.Page("Buku Kating/100_Rozak Ramdani.py",
    title="100 - Rozak Ramdani",
    icon=":material/person:",
)
Mahasiswa12 = st.Page("Buku Kating/104_Felisya Nabila Putri Nugroho.py",
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
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 

#Transisi sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {
    position: relative;
    background: #000080;
    color: #ffffff !important;
    overflow: hidden;
}

[data-testid="stSidebar"]::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, #FF6F00, #000080);
    background-size: 200% 200%;
    opacity: 0.9;
    animation: gradientShift 30s ease-in-out infinite; /* Durasi diperpanjang menjadi 30 detik */
    z-index: -1;
}

@keyframes gradientShift {
    0% { background-position: 0% 0%; }
    25% { background-position: 0% 50%; }
    50% { background-position: 0% 100%; }
    75% { background-position: 0% 50%; }
    100% { background-position: 0% 0%; }
}

/* Perbaikan untuk link di sidebar */
[data-testid="stSidebar"] a,
[data-testid="stSidebar"] .stNavLink,
[data-testid="stSidebar"] div[data-testid="stSidebarNav"] a,
[data-testid="stSidebar"] div[data-testid="stSidebarNav"] span {
    color: #ffffff !important;
    font-weight: 500;
    position: relative;
    z-index: 1;
    transition: color 0.8s ease, text-shadow 0.8s ease; /* Transisi lebih lambat */
}

/* Efek hover untuk link */
[data-testid="stSidebar"] a:hover,
[data-testid="stSidebar"] .stNavLink:hover,
[data-testid="stSidebar"] div[data-testid="stSidebarNav"] a:hover,
[data-testid="stSidebar"] div[data-testid="stSidebarNav"] span:hover {
    color: #FF6F00 !important;
    text-shadow: 0 0 6px rgba(255,255,255,0.8);
}

/* Untuk teks biasa di sidebar */
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] p {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

pg.run()
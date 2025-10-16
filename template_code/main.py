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
    "Buku Kating/094_Jaya Saputra Tamba.py",
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
    "Buku Kating/111_Jeremi Marolop.py",
    title="111 - Jeremi Marolop",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/030_Michrom Muhammad Kallam.py",
    title="030 - Michrom Muhammad Kallam",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/076_Talitha Justine.py",
    title="076 - Talitha Justine",
    icon=":material/person:",
)
Mahasiswa11 = st.Page( 
    "Buku Kating/058_Ayu Andriani Parlina Wati.py",
    title="058 - Ayu Andriani Parlina Wati",
    icon=":material/person:",
)
Mahasiswa12 = st.Page( 
    "Buku Kating/089_Muhammad Rafka Fatih Al Ghathfaan.py",
    title="089 - Muhammad Rafka Fatih Al Ghathfaan",
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

st.markdown("""
<style>
/* Sidebar container */
[data-testid="stSidebar"] {
    position: relative;
    background: #f3f7fc;
    color: #1e293b;
    overflow: hidden;
}

/* Lapisan gradasi dinamis */
[data-testid="stSidebar"]::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, #3A6EA5, #F2C94C, #8BC6EC);
    background-size: 200% 200%;
    opacity: 0;
    animation: gradientFade 6s ease-in-out forwards;
    z-index: -1;
}

/* Efek transisi lembut pada warna dan arah gradasi */
@keyframes gradientFade {
    0% {
        background-position: 0% 50%;
        opacity: 0;
    }
    50% {
        background-position: 100% 50%;
        opacity: 0.6;
    }
    100% {
        background-position: 0% 50%;
        opacity: 0.9;
    }
}

/* Teks sidebar */
[data-testid="stSidebar"] a {
    color: #f9fafb;
    font-weight: 500;
    transition: color 0.3s ease, text-shadow 0.3s ease;
    position: relative;
    z-index: 1;
}

/* Hover */
[data-testid="stSidebar"] a:hover {
    color: #FFF9C4;
    text-shadow: 0 0 8px rgba(255, 249, 196, 0.6);
}
</style>
""", unsafe_allow_html=True)

pg.run()


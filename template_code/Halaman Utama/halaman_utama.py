import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""
<style>
/* ===== Sidebar Gradient ===== */
[data-testid="stSidebar"] {
    position: relative;
    background: #f2f6fb;
    color: #1e293b;
    overflow: hidden;
}
[data-testid="stSidebar"]::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, #3A6EA5 0%, #F2C94C 100%);
    opacity: 0;
    animation: fadeInGradient 3s ease forwards;
    z-index: -1;
}
@keyframes fadeInGradient {
    0% { opacity: 0; }
    50% { opacity: 0.6; }
    100% { opacity: 0.9; }
}

/* ===== Efek Transisi dan Background Halaman ===== */
main, [data-testid="stAppViewContainer"] {
    background-color: #F9F7F3;  /* atau warna lain yang kamu pilih */
    transition: background-color 1.5s ease;
}

/* ===== Bayangan Lembut Sidebar ===== */
[data-testid="stSidebar"] {
    box-shadow: 3px 0 10px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_container_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Dalam sains data, cosval adalah singkatan dari cosine value, yaitu hasil perhitungan cosine similarity antara dua vektor. Konsep ini berasal dari matematika trigonometri, di mana cosinus digunakan untuk mengukur sudut antara dua vektor.
Dalam sains data, khususnya pada analisis kelompok (clustering) atau pengelompokan data, cosval (cosine value) dipahami sebagai ukuran numerik yang menunjukkan tingkat kemiripan antar anggota kelompok atau tingkat kedekatan suatu data dengan pusat kelompok (centroid).</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1s2CshvEIz3_fV3QK_TOgpMsJQkcb3rDi"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">COSVAL adalah kelompok 9 dari kaderisasi CEO HMSD ADYATAMA 
            dengan Mentor yang sangat luar biasa yaitu ka gusti putu ferazka d..Disini kami belajar banyak tentang kepemimpinan dan kolaborasi dalam tim.
            serta timbul kreativitas dan inovasi dalam setiap proyek yang kami kerjakan. menjadikan kami semakin dekat dan juga semakin mengenal satu sama lain.
            Cosval merupakan keluarga di CEO HMSD ADYATAMA ini.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JPwyjAQEXEMOG43G38PGTW067WGkkZMq",
            "https://drive.google.com/uc?export=view&id=1a_5UL_gv7Tj-8ww-HcQ8ZNqz8PU5qA1b",
            "https://drive.google.com/uc?export=view&id=1EPD1nRRm700qOtb5m4rFcEc1ZGfr0CON",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1cmz12RH1e92O6B7yIt7LgPtOkN-y7_qt",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1ntjjSNkS2Q75WdZUqNfOZ7nhY1dtdvxJ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=152kn1VwtsFDWOYUgr-05fNxn765UlmWk",
            "https://drive.google.com/uc?export=view&id=1nteU7mBaF4WuyacPn4zAZcnqqvu2Da-2",
            "https://drive.google.com/uc?export=view&id=1vFsJMR4gP8JYcfxO9XeU2xUUJDSRHyXW",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
           
        ]
        data_list = [
            {
                "nama": "jaya saputra tamba",
                "sebagai": "Pak Lurah",
                "nim": "122450094",
                "fun_fact": "pas kecil pernah nelen uang logam",
                "motto_hidup": "di hina tak tumbang, di puji ga terbang, di kasih duit makasih bang",
            },
            {
                "nama": "farhanah hadaya fatin",
                "sebagai": "Bu Lurah",
                "nim": "122450026",
                "fun_fact": "pelor",
                "motto_hidup": "Ya apa ya",
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "sebagai": "Anggota",
                "nim": "124450099",
                "fun_fact": "suka dikira orang lampung padahal orang jawa",
                "motto_hidup": "kalau mau sesuatu yang besar harus berani berkorban yang besar juga",
            },
            {
                "nama": "Audina Fitria",
                "sebagai": "Anggotaa",
                "nim": "122450038",
                "fun_fact": "gasuka makanan lembek",
                "motto_hidup": "jalanin dulu aja",
            },
            {
                "nama": "Juwita Sari",
                "sebagai": "Anggota",
                "nim": "124450066",
                "fun_fact": "Suka bau sendal/sepatu baru",
                "motto_hidup": "Don't be afraid to fail, be afraid not to try",
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "sebagai": "Anggotaa",
                "nim": "122450056",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Lovianorasaragih",
                "sebagai": "Anggotaa",
                "nim": "122450105",
                "fun_fact": "suka pakai baju bolong",
                "motto_hidup": "tetaplah bernafas",
            },
            {
                "nama": "jeremi Marolop",
                "sebagai": "Anggotaa",
                "nim": "122450111",
                "fun_fact": "suka film lawas",
                "motto_hidup": "jalanin aja dulu",
            },
            {
                "nama":"Muhammad Rafka Fatih Al Ghathfaan",
                "sebagai": "Anggotaa",
                "nim": "122450089",
                "fun_fact": "tidak suka durian",
                "motto_hidup": "stay waras",
            },
            {
                "nama":"Michrom Muhammad Kallam",
                "sebagai": "Anggotaa",
                "nim": "122450030",
                "fun_fact": "Bisa surfing",
                "motto_hidup": "jangan pernah putus asa",
            },
            {
                "nama":"Talitha Justine",
                "sebagai": "Anggotaa",
                "nim": "122450076",
                "fun_fact": "Nama justine karena orang tua suka justine biber",
                "motto_hidup": "jangan deadline",
            },
             {
                "nama":"Ayu Andriani Parlina Wati",
                "sebagai": "Anggotaa",
                "nim": "122450058",
                "fun_fact": "Suka mengerjakan sesuatu kelipatan 5",
                "motto_hidup": "tetaplah hidup",
            },
            
            
            
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

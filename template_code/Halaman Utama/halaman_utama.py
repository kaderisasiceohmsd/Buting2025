import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

# ==============================
# Fungsi untuk memuat gambar
# ==============================
@st.cache_data
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        return img
    except Exception as e:
        st.error(f"Gagal memuat gambar: {e}")
        return None


# ==============================
# Fungsi menampilkan gambar + data
# ==============================
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # tampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"**Nama:** {data_list[i]['nama']}")
            st.write(f"**Sebagai:** {data_list[i]['sebagai']}")
            st.write(f"**NIM:** {data_list[i]['nim']}")
            st.write(f"**Fun Fact:** {data_list[i]['fun_fact']}")
            st.write(f"**Motto Hidup:** {data_list[i]['motto_hidup']}")
            st.markdown("---")


# ==============================
# Header Halaman
# ==============================
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ==============================
# Layout Gambar Utama
# ==============================
def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        img = load_image(url)
        if img:
            st.image(img, use_container_width=True, width=350)
    with col3:
        st.write("")


# contoh gambar (pastikan ID benar)
url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"
layout(url)
layout(url1)


# ==============================
# Menu Navigasi
# ==============================
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "people-fill"],
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

# ==============================
# Halaman HOME
# ==============================
if menu == "Home":
    st.markdown("<h1 style='text-align: center;'>Deskripsi Kelompok</h1>", unsafe_allow_html=True)
    st.markdown(
        """<div style="text-align: justify;">
        <b>JACOBI</b> adalah kelompok kaderisasi yang berlandaskan pada semangat kebersamaan,
        disiplin, dan pengembangan diri. Kami percaya bahwa setiap langkah kecil yang ditempuh
        bersama akan melahirkan kekuatan besar untuk mencapai tujuan. Dengan jiwa kepemimpinan,
        solidaritas, dan integritas, Jacobi hadir sebagai wadah belajar, tumbuh, dan berkontribusi
        demi terciptanya kader yang unggul dan berkarakter.
        </div>""",
        unsafe_allow_html=True,
    )

    foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
    layout(foto_kelompok)

# ==============================
# Halaman ABOUT US
# ==============================
elif menu == "About Us":
    st.markdown("<h1 style='text-align: center;'>About Us</h1>", unsafe_allow_html=True)

    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # Niko
        "https://drive.google.com/uc?export=view&id=1NRBQH_QT8lNsbMgg6gWx4wvw-yfxObUU",  # Rahma
        "https://drive.google.com/uc?export=view&id=1PlYQrm1pg9FoCmZHf9o79lLAYC2ozbuZ",  # Fadya
        "https://drive.google.com/uc?export=view&id=1RpUljY4kbmbHDiXhbts5hZMmpfh1usw3",  # Indah
        "https://drive.google.com/uc?export=view&id=1qI4MFay1-fhuszwZQwlPxYsv2BY-ybne",  # Caca
        "https://drive.google.com/uc?export=view&id=1D8o9sEkhFUTPat3GTF3HKkQnnwIqiIyP",  # Anggun
        "https://drive.google.com/uc?export=view&id=1wwBHyFgyIi0idBbpFwosCgw5TXvv2glv",  # Raisya
        "https://drive.google.com/uc?export=view&id=1hAmwIuWyGLNfiwBNUwKsh6Ke-_ihyKbo",  # Riska
        "https://drive.google.com/uc?export=view&id=1jn4cNQQAOuWjlsSgFvzPsT1kCze5CklB",  # Helmy
    ]

    data_list = [
        {
            "nama": "Gh Mikael Niko Antoni Setiadi",
            "sebagai": "Pak Lurah",
            "nim": "124450025",
            "fun_fact": "Saya lahir mirip Krisna",
            "motto_hidup": "Permasalahan hidup adalah sumber kebijaksanaan.",
        },
        {
            "nama": "Dwi Rahma Fitriani",
            "sebagai": "Bu Lurah",
            "nim": "124450084",
            "fun_fact": "Takut ikan gabus.",
            "motto_hidup": "No delay no problem.",
        },
        {
            "nama": "Fadya Izzatul 'Aini",
            "sebagai": "Anggota",
            "nim": "124450062",
            "fun_fact": "Suka buta map.",
            "motto_hidup": "Do the best, be the best.",
        },
        {
            "nama": "Indah Khairunnisa",
            "sebagai": "Anggota",
            "nim": "124450077",
            "fun_fact": "Suka bikin kesal.",
            "motto_hidup": "Success is the sum of small efforts, repeated day in and day out.",
        },
        {
            "nama": "Jacinda Kesya Alvara",
            "sebagai": "Anggota",
            "nim": "124450023",
            "fun_fact": "Suka buat skenario sebelum tidur.",
            "motto_hidup": "Stop talking about your dreams, and start doing them.",
        },
        {
            "nama": "Anggun Nita",
            "sebagai": "Anggota",
            "nim": "124450009",
            "fun_fact": "Dikejar orang gila dan masuk rumah orang gila itu sendiri.",
            "motto_hidup": "Berusaha selagi masih ada waktu.",
        },
        {
            "nama": "Raisya Izzati Harira",
            "sebagai": "Anggota",
            "nim": "124450122",
            "fun_fact": "Pernah jadi atheist :v",
            "motto_hidup": "Selagi masih nafas, jangan sengaja dihentiin.",
        },
        {
            "nama": "Riska Erlis Dayu Tiara",
            "sebagai": "Anggota",
            "nim": "12450022",
            "fun_fact": "Suka bengong liat sekitar.",
            "motto_hidup": "Setiap tantangan adalah peluang untuk berkembang.",
        },
        {
            "nama": "Helmy Surya Pratama",
            "sebagai": "Anggota",
            "nim": "12450033",
            "fun_fact": "Takut balon.",
            "motto_hidup": "Love the life you live, live the life you love.",
        },
    ]

    display_images_with_data(gambar_urls, data_list)

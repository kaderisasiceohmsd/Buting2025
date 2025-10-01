import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


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
            """<div style="text-align: justify;">Kelompok Bayesian merupakan dua belas bayi naga kecil yang sempat kehilangan arah dalam perjalanan mereka. Di tengah kebingungan itu, 
            mereka akhirnya bertemu dengan sosok ibu yang penuh kasih bernama Dea Amanda yang dengan sabar sekaligus tegas membimbing mereka.
            Dari kedua belas naga tersebut ada Nando sebagai naga tertua yang bijak bersama Azzelya yang selalu setia mendampinginya dalam menjaga
            dan mengarahkan adik-adiknya. Bersama-sama mereka menuntun sepuluh naga lainnya yaitu Yazid, Iqbal, Alsi, Hafis, Zaldi, Bina, Yolanda, Iffa, Arfai dan Yulia agar tidak lagi tersesat. 
            Dari hari ke hari berkat bimbingan Dea Amanda keluarga naga kecil ini tumbuh semakin kuat kompak dan siap menorehkan jejak besar sebagai satu kesatuan keluarga naga Bayesian.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Sebagai simbol, gaya Bayes digambarkan dengan pose unik: 
            tangan kiri mengepal lurus ke depan, sementara tangan kanan siaga layaknya gerakan bela diri. 
            Gerakan ini bukan sekadar gaya, tapi punya makna. Tangan kiri yang tegak lurus melambangkan keyakinan awal yang kuat, 
            sedangkan tangan kanan yang siap menjaga menggambarkan bukti baru yang datang untuk memperkuat arah yang dipilih. 
            Dengan filosofi itu, naga Bayesian bukan hanya sebuah kelompok, melainkan keluarga yang terus belajar, berkembang,
            dan semakin kokoh lewat proses pembaruan keyakinan, persis seperti semangat teori Bayes.</div>""",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "x",
                "sebagai": "Pak Lurah",
                "nim": "122450016",
                "fun_fact": "suka makan pedes, tapi ga suka efeknya",
                "motto_hidup": "new semester new me",
            },
            {
                "nama": "x",
                "sebagai": "Bu Lurah",
                "nim": "122450000",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "Ya apa ya",
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "sebagai": "Anggota",
                "nim": "124450052",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "mantap",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "sebagai": "Anggota",
                "nim": "124450064",
                "fun_fact": "nyemilin",
                "motto_hidup": "jalanin dulu aja",
            },
            {
                "nama": "M Afai",
                "sebagai": "Anggotaa",
                "nim": "124450004",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "x",
                "sebagai": "Anggotaa",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "x",
                "sebagai": "Anggotaa",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "x",
                "sebagai": "Anggotaa",
                "nim": "122450110",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

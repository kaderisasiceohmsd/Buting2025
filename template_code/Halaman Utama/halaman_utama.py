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
            "container": {"padding": "0!important", "background-color": "#7CD2C8"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#F4B39B"},
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
            "<h1 class='centered-title'>BAYESSIAN</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: center;">Think With Logic, Act with data, Move for real impact!!</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1UkHLxu0dW8Yq9bQXVTjhrdIHyGQWZKP4"
        layout(foto_kelompok)
        st.markdown(
            "<h3 class='centered-title'>Deskripsi Kelompok</h3>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">
            Kelompok Bayesian merupakan dua belas bayi naga kecil yang sempat kehilangan arah dalam perjalanan mereka. 
            Di tengah kebingungan itu, mereka akhirnya bertemu dengan sosok ibu yang penuh kasih bernama Dea Amanda yang dengan sabar sekaligus tegas membimbing mereka.
            Dari kedua belas naga tersebut ada Nando sebagai naga tertua yang bijak bersama Azzelya yang selalu setia mendampinginya dalam menjaga dan mengarahkan adik-adiknya. 
            Bersama-sama mereka menuntun sepuluh naga lainnya yaitu Yazid, Iqbal, Alsi, Hafis, Zaldi, Bina, Yolanda, Iffa, Arfai dan Yulia agar tidak lagi tersesat. 
            Dari hari ke hari berkat bimbingan Dea Amanda keluarga naga kecil ini tumbuh semakin kuat kompak dan siap menorehkan jejak besar sebagai satu kesatuan keluarga naga Bayesian.
            </div> """,
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
            "https://drive.google.com/uc?export=view&id=1sugu57LtMn5ubBZllIC_abFWKD6VnoNg",
            "https://drive.google.com/uc?export=view&id=1rLE-MyMqx548GGJnMGUfZmmBqLMnmZRX",
            "https://drive.google.com/uc?export=view&id=1aVhTDfKP0thXutjB99ExN4Je5tVyioo2",
            "https://drive.google.com/uc?export=view&id=16wj0uqdi8Tm3Fvkqt-05eg7FV09OuGB8",
            "https://drive.google.com/uc?export=view&id=1KfUbzDYlod7gxQWKql1DWl9xga4Nck6R",
            "https://drive.google.com/uc?export=view&id=1ocT3cEoV-a4b1rZMHMd4kFsBKE6EM_Sq",
            "https://drive.google.com/uc?export=view&id=1X2LaZpq-4Dn_BTfQ4ZukyjmwzoGN0oml",
            "https://drive.google.com/uc?export=view&id=194BAGsWowpr07P3_Rh_t2l5SMH3gB9pt",
            "https://drive.google.com/uc?export=view&id=1VLs8Txy7nSd49XsAeUqnm_yQ3lSi_Y1H",
            "https://drive.google.com/uc?export=view&id=1VLs8Txy7nSd49XsAeUqnm_yQ3lSi_Y1H",
            "https://drive.google.com/uc?export=view&id=1VLs8Txy7nSd49XsAeUqnm_yQ3lSi_Y1H",
        ]
        data_list = [
            {
                "nama": "Fernando Dimetrius Barus",
                "sebagai": "Pak Lurah",
                "nim": "122450016",
                "fun_fact": "suka makan pedes, tapi ga suka efeknya",
                "motto_hidup": "new semester new me",
            },
            {
                "nama": "Azzelya Thianandry",
                "sebagai": "Bu Lurah",
                "nim": "124450041",
                "fun_fact": "gabisa tidur tanpa selimut",
                "motto_hidup": "Do it for the plot",
            },
            {

                "nama": "Moch. Iqbal Az-Zahir",
                "sebagai": "Anggota",
                "nim": "124450052",
                "fun_fact": "Kadang yapping",
                "motto_hidup": "Terpuji dalam akhlak, beruntung dalam langkah, nyata dalam jejak.",
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "sebagai": "Anggota",
                "nim": "124450064",
                "fun_fact": "TK 2x dan Selalu dimiripin sama orang",
                "motto_hidup": "Berjuang Tanpa Henti, Berdoa Tanpa Putus",
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "sebagai": "Anggotaa",
                "nim": "124450112",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Muhammad Rizaldi",
                "sebagai": "Anggotaa",
                "nim": "124450093",
                "fun_fact": "Semua jariku bengkok, suka ngelipetin kantong kresek",
                "motto_hidup": "Jalanin dulu hari ini, Hari esok liat nanti lah",
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "sebagai": "Anggotaa",
                "nim": "124450081",
                "fun_fact": "Ga bisa makan daging kurban",
                "motto_hidup": "Kejarlah apa yang kau inginkan",
            },
            {
                "nama": "Muhammad Alsi Syahrulloh",
                "sebagai": "Anggotaa",
                "nim": "124450092",
                "fun_fact": "suka nontpn asmr",
                "motto_hidup": "Kecil melangkah besar berbuah",
            },
            {
                "nama": "Yollanda Agustina",
                "sebagai": "Anggotaa",
                "nim": "124450024",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Yulia Kristine Malau",
                "sebagai": "Anggotaa",
                "nim": "124450119",
                "fun_fact": "suka campurin makanannn",
                "motto_hidup": "jalanin dulu keles",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

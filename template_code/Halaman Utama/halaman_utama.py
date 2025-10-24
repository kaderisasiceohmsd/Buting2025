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
            """<div style="text-align: justify;"></div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1Gny0GZHIDORK7yGyweU7M3jce0m_WHY_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Kami adalah Kelompok 03 - Markov, salah satu kelompok kaderisasi HMSD adyatama 2025 yang beranggotakan 12 orang. 
            Markov berasal dari nama ilmuwan matematikawan rusia yang bernama Andrey Markov, yaitu 
            matematika dan probabilitas yang artinya dalam kelompok ini setiap langkah ke depan bergantung 
            pada kondisi saat ini, bukan pada masa lalu. Markov sebagai identitas kelompok kami dengan 
            harapan dapat belajar, berkembang, dan berproses selama rangkaian kaderisasi ini.</div>""",
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
            "https://drive.google.com/uc?export=view&id=1Xv4oyPt6qLmwKy_qxlfqCVu2BKpUQnMx",
            "https://drive.google.com/uc?export=view&id=1hhdcOJ5KU9WS52x3tIRY5WmG9yz1GL-L",
            "https://drive.google.com/uc?export=view&id=1V7pS25dALvSAKE1Yr_4LV_F0-_2gfNQJ",
            "https://drive.google.com/uc?export=view&id=1hDN2ivqf4oG6jT4Aenp4ojbPw_-BmnZx",
            "https://drive.google.com/uc?export=view&id=1WwBPT2MXCi2CYzHl-2KMpVKuNw4HBRXF",
            "https://drive.google.com/uc?export=view&id=1SOtVe7_1FKGv5RN8MkgdKNY18qVzjh91",
            "https://drive.google.com/uc?export=view&id=1PA-nXAE-xtBxPIZ81uFV1qmhzadNQutF",
            "https://drive.google.com/uc?export=view&id=1ZrBkfwJFxuIES-HKak8S6skMltHtqw0r",
            "https://drive.google.com/uc?export=view&id=1NlOUH5R_1qwWRk2I6B_fatBwCtRMI1H2",
            "https://drive.google.com/uc?export=view&id=1BS71hxb6MWesydP_yU0p2cL0tx6rTIzg",
            "https://drive.google.com/uc?export=view&id=1XeVNkjmpYTmdmEZwbbPDBX_9gO1-84dY",
            "https://drive.google.com/uc?export=view&id=1qTYdwvyoBMQEg8LSQLxU7pJ9MVC4P5K9",
        ]
        data_list = [
            {
                "nama": "Hazel Mahesa Handhaka",
                "sebagai": "Pak Lurah",
                "nim": "124450114",
                "fun_fact": "ngga suka makanan berkuah",
                "motto_hidup": "Allah tidak membebani suatu kaum melebihi batasannya",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "sebagai": "Bu Lurah",
                "nim": "124450082",
                "fun_fact": "suka banget mengoleksi stiker gemas",
                "motto_hidup": "Berpikir besar dan mulai dari kecil",
            },
            {
                "nama": "Dafa Elpriza",
                "sebagai": "Anggota",
                "nim": "124450131",
                "fun_fact": "Ga suka durian",
                "motto_hidup": "hidup yang tidak dipertaruhkan tidak akan pernah dimenangkan",
            },
            {
                "nama": "Salavi Naharani",
                "sebagai": "Anggotaa",
                "nim": "124450090",
                "fun_fact": "Ga suka makan",
                "motto_hidup": "Kehidupan adalah perjalanan, nikmati setiap prosesnya",
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "sebagai": "Anggotaa",
                "nim": "122450087",
                "fun_fact": "tidur harus make kain ibu",
                "motto_hidup": "Hari ini sulit, tapi besok bisa jadi luar biasa",
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "sebagai": "Anggotaa",
                "nim": "124450097 ",
                "fun_fact": "Suka buka kulkas berulang ulang padahal udah tau isinya",
                "motto_hidup": "Tak ada pelangi tanpa hujan, tak ada keberhasilan tanpa perjuangan",
            },
            {
                "nama": "Gatfan Nadif Ali",
                "sebagai": "Anggotaa",
                "nim": "124450001",
                "fun_fact": "Multitasking pas lagi santai",
                "motto_hidup": "It is what it is",
            },
            {
                "nama": "Bryan Paskah telaumbanua",
                "sebagai": "Anggotaa",
                "nim": "124450003",
                "fun_fact": "Suka merendam kaki",
                "motto_hidup": "Lakukan yang terbaik, dan tetap rendah hati",
            },
            {
                "nama": "Allisha",
                "sebagai": "Anggotaa",
                "nim": "124450019",
                "fun_fact": "Ga suka makan ikan lele ",
                "motto_hidup": "Hidup santai selagi masih ada hari esok",
            },
            {
                "nama": "Afdal Rahmad Setiawan",
                "sebagai": "Anggotaa",
                "nim": "124450008",
                "fun_fact": "Kuat makan  pedas",
                "motto_hidup": "jika orang lain bisa kenapa kita tidak",
            },
            {
                "nama": "Vannisha Ramadhani",
                "sebagai": "Anggotaa",
                "nim": "124450078",
                "fun_fact": "Suka nabrak apa aja",
                "motto_hidup": "jangan menunggu hujan reda, tetapi menarilah di tangan hujan.",
            },
            {
                "nama": "Adinda Deswita Maharani",
                "sebagai": "Anggotaa",
                "nim": "124450083",
                "fun_fact": "Bisa gerakin kuping",
                "motto_hidup": "just do what u love and love what u do",
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

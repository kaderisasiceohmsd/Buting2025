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
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2025</p>
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
            """<div style="text-align: justify;">We are Pandas!, We are the next excellent generation.
            Kami merupakan kelompok yang berkomitmen untuk mencapai keunggulan dalam setiap aspek.
            Baik itu akademik dan non akademik. Apapun itu, kami siap untuk menghadapi tantangan dan berinovasi.
            </div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1rrnH49b8Wjd_vQ6OTZzoiwqtejfpZogk"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Testing kelompok pandas by henry.</div>""",
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
            "https://drive.google.com/uc?export=view&id=17ztn7m8gtkcDS9TLaTtrURkZqNDiISnj",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Rifky Henry Ferdianto",
                "sebagai": "Pak Lurah",
                "nim": "124450115",
                "fun_fact": "Suka belajar bahasa baru",
                "motto_hidup": "Berkembanglah terus meski lambat asal pasti",
            },
            {
                "nama": "Suci Aulia Putri",
                "sebagai": "Bu Lurah",
                "nim": "124450000",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "Ya apa ya",
            },
            {
                "nama": "Dimas Arya Ramadhan",
                "sebagai": "Anggota",
                "nim": "124450118",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "mantap",
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "sebagai": "Anggota",
                "nim": "124450108",
                "fun_fact": "Yang adzanin ketika lahir bukan ayah, tapi paman",
                "motto_hidup": "Sesungguhnya sesudah kesulitan itu ada kemudahan",
            },
            {
                "nama": "Najla Nursyifa",
                "sebagai": "Anggota",
                "nim": "124450051",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Teresa Christiani Purba",
                "sebagai": "Anggota",
                "nim": "124450046",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "sebagai": "Anggota",
                "nim": "124450042",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Caesar Ozora Alrando",
                "sebagai": "Anggota",
                "nim": "124450017",
                "fun_fact": "suka mancing tapi gak suka makan ikan",
                "motto_hidup": "urip iku urup",
            },
            {
                "nama": "Layina Ropiqo",
                "sebagai": "Anggota",
                "nim": "124450016",
                "fun_fact": "suka mancing tapi gak suka makan ikan",
                "motto_hidup": "urip iku urup",
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "sebagai": "Anggota",
                "nim": "124450015",
                "fun_fact": "suka mancing tapi gak suka makan ikan",
                "motto_hidup": "urip iku urup",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "sebagai": "Anggotaa",
                "nim": "124450013",
                "fun_fact": "suka mancing tapi gak suka makan ikan",
                "motto_hidup": "urip iku urup",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

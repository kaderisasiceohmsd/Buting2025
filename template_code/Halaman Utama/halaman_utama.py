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
            """<div style="text-align: justify;">Test ini Kaleb dari kelompok 6</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">hai ini kaleb.</div>""",
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
                "nama": "Alfaya Rafif Abiyyi",
                "sebagai": "Pak Lurah",
                "nim": "122450006",
                "fun_fact": "sering jatoh dari motor",
                "motto_hidup": "berjuang sampai titik akhir",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "sebagai": "Bu Lurah",
                "nim": "122450029",
                "fun_fact": "hobby ngisengin dua princess",
                "motto_hidup": "apa yang sudah dimulai harus diselesaikan",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "sebagai": "Anggota",
                "nim": "124450053",
                "fun_fact": "Username IG nya kelelep_comberan karena pernah kejebur di comberan",
                "motto_hidup": "Semper ad meliora.",
            },
            {
                "nama": "Nabila Nur Azizah",
                "sebagai": "Anggota",
                "nim": "124450048",
                "fun_fact": "makan roti tawar harus di kupas",
                "motto_hidup": "berjalan seperti air",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "sebagai": "Anggota",
                "nim": "122450085",
                "fun_fact": "Eyangnya Sri Sultan Hamengkubuwana II",
                "motto_hidup": "Tetaplah merasa bodoh supaya terus belajar",
            },
            {
                "nama": "Selma Siti Aisyah",
                "sebagai": "Anggota",
                "nim": "124450044", 
                "fun_fact": "pernah ilang di kebun binatang", 
                "motto_hidup": "Doa dan Usaha adalah Kartu Kemenangan Mereka",
            },
            {
                "nama": "Hani Qurrota Aini",
                "sebagai": "Anggota",
                "nim": "122450020",
                "fun_fact": "suka buah stroberi tapi gasuka kalau stroberi nya diolah atau olahan stroberi",
                "motto_hidup": "breathe, evolve,shine",
            },
            {
                "nama": "Siti Sarifah", 
                "sebagai": "Anggota",
                "nim": "124450015", 
                "fun_fact": "ga suka alpukat", 
                "motto_hidup": "Jangan pernah menyerah",
            },
            {
                "nama": "Cika Adelia Br Marbun", 
                "sebagai": "Anggota",
                "nim": "124450107", 
                "fun_fact": "ga bisa makan pedas",  
                "motto_hidup": " Doakan apa yang kamu kerjakan, kerjakan apa yang kamu doakan",
            },
            {
                "nama": "Siti Sarifah", "Gustin H. Tampubolon", 
                "sebagai": "Anggota",
                "nim": "124450068"
                "fun_fact": "susah ingat nama orang, tapi hafal mukanya" 
                "motto_hidup": "apapun yang kamu perbuat, perbuatlah dengan segenap hatimu"
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

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
            "nav-link-selected": {"background-color": "#FF6F00"},
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
            """<div style="text-align: justify;">Kelompok 1 Tensor bukan hanya sekelompok nama, kami adalah simpul keakraban dan keharmonisan. 
            Nama Tensor sendiri melambangkan kekuatan yang menyatukan berbagai elemen, dan itulah yang kami lakukan. Di sini, setiap individu dihargai, 
            dan suasana yang tercipta terasa hangat—seperti keluarga kedua tempat setiap anggota bebas bercerita, tertawa, dan tumbuh bersama tanpa rasa 
            canggung. Kami percaya bahwa kaderisasi terbaik lahir dari kebersamaan yang solid. Kami belajar, berdiskusi, dan berproses dengan semangat 
            saling dukung dan gotong royong. Kelompok Tensor adalah bukti nyata bahwa ketika kita selaras, proses belajar pun terasa ringan dan 
            penuh makna.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
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
            "https://drive.google.com/uc?export=view&id=1-8b-WLrqBEMIkPIYROpuPfILcIgii7zG",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=19rya7Zkzck08XZf82EBAN4lWtMBxhA_f",
        ]
        data_list = [
            {
                "nama": "Andra",
                "sebagai": "Pak Lurah",
                "nim": "122450016",
                "fun_fact": "suka makan pedes, tapi ga suka efeknya",
                "motto_hidup": "new semester new me",
            },
            {
                "nama": "Aisyah",
                "sebagai": "Bu Lurah",
                "nim": "122450000",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "Ya apa ya",
            },
            {
                "nama": "Aliya",
                "sebagai": "Anggota",
                "nim": "122450083",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "mantap",
            },
            {
                "nama": "Della",
                "sebagai": "Anggotaa",
                "nim": "122450000",
                "fun_fact": "nyemilin",
                "motto_hidup": "jalanin dulu aja",
            },
            {
                "nama": "Elsa",
                "sebagai": "Anggotaa",
                "nim": "122450088",
                "fun_fact": "Makan sayur tapi, ga makan tangkainya",
                "motto_hidup": "Untuk segala sesuatu ada masanya, untuk apa pun di bawah langit ada waktunya.",
            },
            {
                "nama": "Favian",
                "sebagai": "Anggotaa paling cool abiezzz",
                "nim": "124450021",
                "fun_fact": "Suka berdialog sama diri sendiri",
                "motto_hidup": "anything that happens to you, tetaplah jadi manusia yang baik",
            },
            {
                "nama": "Felisya",
                "sebagai": "Anggotaa",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Ghiyats",
                "sebagai": "Anggotaa",
                "nim": "122450110",
                "fun_fact": "apapun game yang dimainin pasti bagus",
                "motto_hidup": "yang penting hidup dulu",
            },
            {
                "nama": "Lutfi",
                "sebagai": "Anggotaa",
                "nim": "124450047",
                "fun_fact": "Makan sayur hanya daunnya saja tidak dengan tangkainya",
                "motto_hidup": "Man Jadda Wa Jadda",
            },
            {
                "nama": "Nazlah Auliya",
                "sebagai": "Anggotaa",
                "nim": "124450054",
                "fun_fact": "susah hapalin nama orang baru",
                "motto_hidup": "yang penting bisa makan",
            },
            {
                "nama": "Razan",
                "sebagai": "Anggotaa",
                "nim": "122450110",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Rozak",
                "sebagai": "Anggotaa",
                "nim": "122450110",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

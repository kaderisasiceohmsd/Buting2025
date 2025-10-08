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
            "container": {"padding": "0!important", "background-color": "#099df3"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#178C72"},
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
            "<h1 class='centered-title'>Deskripsi Kelompok 4 ANOVA</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Halo semua! Perkenalkan kami, Kelompok 4 ANOVA, salah satu kelompok kaderisasi HMSD Adyatama 2025! 🤩
Kami beranggotakan 10 orang luar biasa dengan mentor yang super keren, Bang Givaro.🙆🏻
Nama ANOVA bukan sekadar nama biasa ia punya makna yang dalam dan penuh semangat.🙌🏻
Dalam dunia statistik 📊, ANOVA adalah singkatan dari Analysis of Variance, sebuah metode untuk melihat perbedaan antar kelompok dan menentukan apakah perbedaan itu benar-benar berarti. Nah, filosofi itu kami bawa ke dalam kelompok kami.😉
</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1_Zd4qf_dnTmdU4uyae5VtVNNxRrb8t2g"
        layout(foto_kelompok)
        st.markdown(
    """<div style="text-align: justify;">
    ANOVA bagi kami berarti perbedaan yang menyatu jadi kekuatan🤔. Kami datang dari latar belakang, karakter, dan kemampuan yang beragam tapi justru di situlah keindahannya🌈. 
    Setiap anggota punya “warna” sendiri, dan saat semua warna itu digabungkan, terbentuklah satu harmoni yang solid dan berenergi. 
    Dengan semangat kerja sama, rasa ingin tahu, dan tekad untuk terus berkembang, ANOVA siap jadi kelompok yang nggak cuma kompak, tapi juga berprestasi💫! 
    Karena kami percaya, seperti halnya dalam analisis variansi, setiap perbedaan bisa berarti, asal kita tahu cara mengolahnya bersama💻.
    <br><br>
    <div style="text-align:center; font-weight:bold; margin-top:10px;">
    "WE ARE THE NEXT EXCELLENCE GENERATION!"
    </div>
    </div>""",
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
            "https://drive.google.com/uc?export=view&id=1tQAhvJOTqEg9zCiZdwSWpsr58CaFdsAp",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "nama": "Jeremia Halim",
                "sebagai": "Anak Palu & Bulu terkeren",
                "nim": "124450101",
                "fun_fact": "Bisa Beatbox, Lucid Dream",
                "motto_hidup": "Do your best & let God handle the rest.",
            },
            {
                "nama": "Asri Meilani",
                "sebagai": "Bulu Gorjes",
                "nim": "124450010",
                "fun_fact": "-",
                "motto_hidup": "-",
            },
            {
                "nama": "Difanya Husakina",
                "sebagai": "Anggota Anova paling imup",
                "nim": "124450043",
                "fun_fact": "Kalau tidur harus ada suara dan pernah ilang 2 kali waktu TK",
                "motto_hidup": "what you do now is the result of your efforts in the past",
            },
            {
                "nama": "Cerine Sihotang",
                "sebagai": "Anak Palu & Bulu",
                "nim": "124450101",
                "fun_fact": "Bisa Beatbox, Lucid Dream",
                "motto_hidup": "Do The Best & Let God The Rest",
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "sebagai": "Anggota Anova paling kalem",
                "nim": "124450050",
                "fun_fact": "Gasuka daging sapi sama kambing",
                "motto_hidup": "Dream big, act bigger",
            },
            {
                "nama": "Fitra Pratama Mega",
                "sebagai": "Anak Palu & Bulu",
                "nim": "124450101",
                "fun_fact": "Bisa Beatbox, Lucid Dream",
                "motto_hidup": "Do The Best & Let God The Rest",
            },
            {
                "nama": "Afriza Azmi",
                "sebagai": "Palu tergacor",
                "nim": "124450110",
                "fun_fact": "sering ngomong sama diri sendiri",
                "motto_hidup": "Power is not given, it's taken",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "sebagai": "member anova",
                "nim": "124450121",
                "fun_fact": "bisa bunyiin tangan(kecapin)",
                "motto_hidup": "Chase goals at sunrise, not excuses at sunset",
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "sebagai": "member anova terimupp",
                "nim": "124450124",
                "fun_fact": "suka makan tempe mentah",
                "motto_hidup": "Not long, but meaningful",
            },
            {
                "nama": "Ahmad Zidane Rabbaanee",
                "sebagai": "Anak Palu & Bulu",
                "nim": "124450101",
                "fun_fact": "Bisa Beatbox, Lucid Dream",
                "motto_hidup": "Do The Best & Let God The Rest",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

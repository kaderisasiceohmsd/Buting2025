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
            """<div style="text-align: justify;">
            Teorema Bayes mengajarkan bahwa keyakinan awal (prior) bukanlah sesuatu yang mutlak. Setiap 
            bukti baru (evidence) yang datang dapat memperkaya dan bahkan mengubah keyakinan itu, sehingga lahirlah 
            pemahaman yang lebih matang (posterior).
            Dari sini ada beberapa nilai filosofis yang bisa ditarik:
            1. Belajar dari pengalaman: 
            Kita tidak boleh terpaku pada pandangan lama. Bukti baru harus dijadikan dasar untuk 
            memperbaiki cara berpikir.
            2. Keterbukaan & kerendahan hati:
            Tidak ada keyakinan awal yang sempurna. 
            Teorema Bayes menekankan perlunya terbuka terhadap informasi baru agar tidak 
            terjebak pada kesalahan.
            3. Proses berkelanjutan:
            Pembaruan keyakinan bukan terjadi sekali, tapi terus-menerus. Ini menggambarkan 
            bahwa hidup adalah proses belajar tanpa henti.
            4. Keseimbangan antara tradisi & perubahan:
            Prior tidak dibuang, tapi dikoreksi dengan evidence. Artinya, identitas awal tetap penting, 
            namun harus siap disempurnakan oleh pengalaman.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Jadi secara singkat:
            Teorema Bayes memberi filosofi bahwa hidup adalah proses memperbarui keyakinan dan keputusan 
            berdasarkan bukti baru, sehingga kita menjadi lebih adaptif, bijak, dan terus berkembang.</div>""",
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
                "nama": "Fernando",
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
                "nama": "Alsi",
                "sebagai": "Anggota",
                "nim": "122450083",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "mantap",
            },
            {
                "nama": "Bina",
                "sebagai": "Anggotaa",
                "nim": "122450000",
                "fun_fact": "nyemilin",
                "motto_hidup": "jalanin dulu aja",
            },
            {
                "nama": "Hafidz",
                "sebagai": "Anggotaa",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Zannuba",
                "sebagai": "Anggotaa",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Iqbal",
                "sebagai": "Anggotaa",
                "nim": "122450100",
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
                "nama": "Yazid",
                "sebagai": "Anggotaa",
                "nim": "122450110",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Yollanda",
                "sebagai": "Anggotaa",
                "nim": "122450110",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Yulia",
                "sebagai": "Anggotaa",
                "nim": "122450110",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

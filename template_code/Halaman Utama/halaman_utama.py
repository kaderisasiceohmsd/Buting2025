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
            """<div style="text-align: justify;"> kelompok poisson adalah</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1j2whG_RXnlMioXeOqXbXWct4OK6qqFxS"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Kelompok kami merupakan sekumpulan mahasiswa Sains Data angkatan 2024 yang memiliki semangat belajar tinggi serta tekad untuk tumbuh dan berkembang bersama. Dengan latar belakang, karakter, dan minat yang beragam, kami saling melengkapi satu sama lain dalam menghadapi berbagai tantangan selama perkuliahan.
            Kami percaya bahwa kerja sama, komunikasi yang baik, dan rasa saling mendukung adalah kunci untuk menciptakan lingkungan yang nyaman dan produktif. Melalui kebersamaan ini, kami berkomitmen untuk terus belajar, beradaptasi, dan memberikan yang terbaik dalam setiap kegiatan akademik maupun organisasi. Harapannya, kelompok ini dapat menjadi wadah yang solid untuk bertukar ide, membangun relasi, serta melangkah maju bersama menuju tujuan yang sama.</div>""",
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
            "https://drive.google.com/uc?export=view&id=10DZICvueHl1NOGxcD2DYpPGiQXREqQkh",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=11xetiejm5bOM1wOGc1zep1ohwqTzqQ-O",
        ]
        data_list = [
            {
                "nama": "Bima Ekayasa",
                "sebagai": "Pak Lurah",
                "nim": "124450106",
                "fun_fact": "main gitar everyday",
                "motto_hidup": "beyond your limits",
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "sebagai": "Bu Lurah",
                "nim": "124450014",
                "fun_fact": "suka wangi manis",
                "motto_hidup": "Explore, Create and Shine",
            },
            {
                "nama": "Faizatun Najmi",
                "sebagai": "Anggota",
                "nim": "124450126",
                "fun_fact": "naik wahana ekstrim",
                "motto_hidup": "manusia punya kendala, Tuhan punya kendali",
            },
            {
                "nama": "Manuel Frederika",
                "sebagai": "Anggota",
                "nim": "124450039",
                "fun_fact": "Mau tidur jam berapapun bangunnya jam 6 pagi",
                "motto_hidup": "Fokus, Berproses, Bersabar, Berhasil",
            },
            {
                "nama": "Sherena Florencia",
                "sebagai": "Anggota",
                "nim": "124450027",
                "fun_fact": "gasuka kulot ayam",
                "motto_hidup": "do everything with love",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "sebagai": "Anggotaa",
                "nim": "124450128",
                "fun_fact": "Pernah membakar rumah nenek karna suka bermain api",
                "motto_hidup": "Bergeraklah jangan seperti batu berlumut",
            },
            {
                "nama": "Ahmad Bimo AKbar Arkana Putra",
                "sebagai": "Anggotaa",
                "nim": "124450113",
                "fun_fact": "keturunan pakistan",
                "motto_hidup": "keberuntungan hanya berpihak kepada mereka yang berani",
            },
            {
                "nama": "Faiza Try Anjani",
                "sebagai": "Anggota",
                "nim": "124450075",
                "fun_fact": "pernah bikin tugas satu kelas hilang",
                "motto_hidup": "dream, learn, achieve",
            },
            {
                "nama": "Saskia Nova Magdanlena",
                "sebagai": "Anggotaa",
                "nim": "124450074",
                "fun_fact": "Tenggelam di sumur, dan masih hidup",
                "motto_hidup": "Do what you love, and love what you do",
            },
             {
                "nama": "Abigael Limbong",
                "sebagai": "Anggotaa",
                "nim": "124450080",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

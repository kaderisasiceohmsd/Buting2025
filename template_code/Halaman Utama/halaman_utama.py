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
            "container": {"padding": "0!important", "background-color": "#234C6A"},
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
            """<div style="text-align: center;"> WE ARE POISSON</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1j2whG_RXnlMioXeOqXbXWct4OK6qqFxS"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Kami adalah Poisson, tiga belas jiwa dari Datasena, Sains Data ITERA 2024.
Di antara angka dan peluang, kami berdiri dengan semangat untuk memahami makna di balik ketidakpastian.
Terinspirasi dari Distribusi Poisson, kami belajar bahwa bahkan peristiwa acak pun menyimpan pola,
dan di balik kebetulan, selalu ada keteraturan yang menunggu untuk ditemukan.

Seperti rumus yang hidup di antara deretan bilangan, kami percaya bahwa setiap data punya cerita,
setiap anomali punya makna, dan setiap anggota kami adalah satu titik dalam grafik besar kehidupan —
unik, berdiri sendiri, namun indah saat disatukan.

Kami tumbuh bersama sebagai satu kesatuan, saling melengkapi di setiap proses,
menjadi jejaring kebersamaan yang menguatkan langkah kami menuju masa depan.
Bersama Datasena 2024, kami bukan hanya sekumpulan individu yang mencintai data,
tapi keluarga yang belajar, tertawa, dan berproses dalam irama yang sama.

Dari kekacauan, kami membaca keindahan;
dari acak, kami menulis makna;
dari data, kami mencipta arah.
Kami adalah Poisson — harmoni dari ketidakpastian, pola dari kebetulan,
dan kisah yang tumbuh dari rasa ingin tahu tanpa batas.</div>""",
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
        st.markdown("<h1 class='centered-title'>𝓞𝓾𝓻 𝓓𝓲𝓼𝓽𝓻𝓲𝓫𝓾𝓽𝓲𝓸𝓷</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ICkBFIOuO2ouVfoCVaUCD3p3MHdSPMIO",
            "https://drive.google.com/uc?export=view&id=1Zj6Jo4aT2IONt0NbZHYqJ2eUGM_LKljK",
            "https://drive.google.com/uc?export=view&id=10DZICvueHl1NOGxcD2DYpPGiQXREqQkh",
            "https://drive.google.com/uc?export=view&id=1HaqrQfQLYdm073TpvAL1tm817f_pKNj2",
            "https://drive.google.com/uc?export=view&id=11xetiejm5bOM1wOGc1zep1ohwqTzqQ-O",
            "https://drive.google.com/uc?export=view&id=1G5CXa7vA-Iv1r8Lcs83P6ANHKukG6PEn",
            "https://drive.google.com/uc?export=view&id=1fwwht7ywCIOaBc37jEA5kzoDoUuwLviB",
            "https://drive.google.com/uc?export=view&id=1K0XDJWDivz-4VFKADPvil4XT_X3awthu",
            "https://drive.google.com/uc?export=view&id=1SGWJsXr4FpN82gF2xmt1UrWHjDKW_n8N",
            "https://drive.google.com/uc?export=view&id=1ZK2DdiICd_VtlJXzBCLPLvOimDu1moKI",
            "https://drive.google.com/uc?export=view&id=19obrPF1fjUwTvDdVsiJxZdYkf7EFR_WA",
            "https://drive.google.com/uc?export=view&id=1eUNb9eNqio1OA8d9FPP9wLNZ3yW5Ao1a",
            "https://drive.google.com/uc?export=view&id=14RPBtKtuZjoLX_6qknsXimW37dQRaxp6",
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
                "fun_fact": "gasuka kulit ayam",
                "motto_hidup": "do everything with love",
            },
            {
                "nama": "Edsel Adya Pradipta",
                "sebagai": "Anggota",
                "nim": "124450098",
                "fun_fact": "punya gigi 2 layer",
                "motto_hidup": "menjadi lebih baik bukan pilihan, tetapi sebuah keharusan",
            },
            {
                "nama": "Muhammad Harvinsyah",
                "sebagai": "Anggota",
                "nim": "124450128",
                "fun_fact": "Pernah membakar rumah nenek karena suka bermain api",
                "motto_hidup": "Bergeraklah jangan sampai seperti batu berlumut",
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana Putra",
                "sebagai": "Anggota",
                "nim": "124450113",
                "fun_fact": "keturunan Pakistan",
                "motto_hidup": "keberuntungan hanya berpihak kepada mereka yang berani",
            },
             {
                "nama": "Abigael Limbong",
                "sebagai": "Anggota",
                "nim": "124450080",
                "fun_fact": "Suka EXO",
                "motto_hidup": "Tetap tersenyum",
            },
             {
                "nama": "Faiza Try Anjani",
                "sebagai": "Anggota",
                "nim": "124450075",
                "fun_fact": "",
                "motto_hidup": "",
            },
             {
                "nama": "Saskia Nova Magdalena",
                "sebagai": "Anggota",
                "nim": "124450074",
                "fun_fact": "",
                "motto_hidup": "",
            },
             {
                "nama": "Daffa Kharisma Adzana",
                "sebagai": "Anggota",
                "nim": "124450061",
                "fun_fact": "",
                "motto_hidup": "",
            },
             {
                "nama": "Tubagus Abdani Pamungkas",
                "sebagai": "Anggota",
                "nim": "124450035",
                "fun_fact": "",
                "motto_hidup": "",
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()

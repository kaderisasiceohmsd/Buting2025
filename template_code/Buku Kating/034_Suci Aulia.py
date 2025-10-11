import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
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

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pugYjo5CN9_eRBpmQp5frktDHbFVWbXM",
            "https://drive.google.com/uc?export=view&id=1OszRW3I7c3WLqE0NPriygKiXWHm9kGbg",
            "https://drive.google.com/uc?export=view&id=1qYby8WfcfDU_Z2su-z84p3e_xv0DclBc",
            "https://drive.google.com/uc?export=view&id=1b5ogEd2e_Q7xrDovGrkfZ0i3g5FGK3gg",
            "https://drive.google.com/uc?export=view&id=1acCvoBAL1FfWEO7-EndHo3r4BvWBzWvS",
            "https://drive.google.com/uc?export=view&id=1-bXkFt_W6cYH-BGv_x70uLvpCxpikJlr",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari AZhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat":"Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "12245001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak A",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak B",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak CCc",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lvzlSxNKFoq2Qo6xw_CnSsw8XXES19wh",
            "https://drive.google.com/uc?export=view&id=1ic9__NdJXPgSkBCZrB6WHslKlykWEVgS",
            "https://drive.google.com/uc?export=view&id=11VEzJUk0YQ0rWYPkAzwZ0RsOyYrRyLuU",
            "https://drive.google.com/uc?export=view&id=1mgWmY0yXV8MU4nvP78qB-9pp07-vIjAu",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen Internal":
    def Internal ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1d14e7g73FMHxrCRijcajDvcehei1J_Yw",
            "https://drive.google.com/uc?export=view&id=1P5nsoKUlPUkJv2E9gDUL-e4W59unFVRe",
            "https://drive.google.com/uc?export=view&id=11xDotoN8W2qwWLO0ErEB-l2K9dc_Rfmc",
            "https://drive.google.com/uc?export=view&id=10O0lyTWyt6rkKGGmx5talZ1yI54jpgH7",
            "https://drive.google.com/uc?export=view&id=1-oYXmdb8dAEGmiM5_RRG7VM8hdHG3Q6l",
            "https://drive.google.com/uc?export=view&id=1jDP01_zrKs-nYkPNq7onuyCI8qy87NY4",
            "https://drive.google.com/uc?export=view&id=192Z38AFq-1oug5nJoWGkUzarLV2USD7O",
            "https://drive.google.com/uc?export=view&id=1DssEPoDrWKFQD-IRlF1PqLnBuGYa7Y1Z",
            "https://drive.google.com/uc?export=view&id=1ENJgWWsAKZmVARRfTT6OJSwiazWyOmHy",
            "https://drive.google.com/uc?export=view&id=1O9Crd3u7RqljpNTinhV6KJ3_hQD0RhH8",
            "https://drive.google.com/uc?export=view&id=1cNtIJNLrYbaTlX85oRCSK4kLT2z54xVn",
            "https://drive.google.com/uc?export=view&id=1ob6T5-_8K1ziuhWgPi1ZSz8K9q1P1mg2",
            "https://drive.google.com/uc?export=view&id=1dr3w3mWefdjPjbBlQ_d300xIIaA_MTcp",
            "https://drive.google.com/uc?export=view&id=15NpdMrpeK7WlcNGGjfJmHHtXdH6I4nDi",
            "https://drive.google.com/uc?export=view&id=1u-S2xEA-oFhpz-mGj9pi9IKslwU2u7jB",
           
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat":"Balam",
                "hobbi": "Mengaji",
                "sosmed": "@ranniku",
                "kesan": "Kak Rani keliatan skena banget penampilannya, sukaa",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat":"Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Rendy Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat":"Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": " 123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat":"Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Zahra Putri Salsabill",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "1",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Internal()

if menu == "Departemen SSD":
    def SSD ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vAATNhzvC9wEwR0iQueG3xpkHQOb9mQI",
            "https://drive.google.com/uc?export=view&id=1tjb1oBs7r0pjHWp0XEuZI7gV-aAc8Opv",
            "https://drive.google.com/uc?export=view&id=1yrYx1w6K2baNFUcYiPGB_nOr1raRpZBf",
            "https://drive.google.com/uc?export=view&id=1EerfMuwqgOrt0paBumw31gRwqdGScOLJ",
            "https://drive.google.com/uc?export=view&id=1be-HZHgY-F_lWy6v5wUnRlMf7ZTNDWqQ",
            "https://drive.google.com/uc?export=view&id=1Yi59WysL2YQqp5hkk_P-crNqlC6UCaE_",
            "https://drive.google.com/uc?export=view&id=1C3tSPvGOGIYOUm2lkIMdrV93xxeh-Pav",
            "https://drive.google.com/uc?export=view&id=1K5NoqXMnRu9UukglmQMYq0I0otxei_X-",
            "https://drive.google.com/uc?export=view&id=1C3tSPvGOGIYOUm2lkIMdrV93xxeh-Pav",
            "https://drive.google.com/uc?export=view&id=1CY7qyKW3BhEsuNhX7BiOwNuQnBYevD4g",
            "https://drive.google.com/uc?export=view&id=1tjb1oBs7r0pjHWp0XEuZI7gV-aAc8Opv",
           
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Bandar Lampung",
                "alamat":"Belakang PB",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_",
                "kesan": "Kak Rani keliatan skena banget penampilannya, sukaa",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat":"Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat":"Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": " 123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat":"Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anandiacrn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat":"Lampung Selatan",
                "hobbi": "Nonton Drama Short FB",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat":"Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat":"Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": " 123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat":"Gg. Perwira 2",
                "hobbi": "Menonton Alur Cerita Film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    SSD()

    















# Tambahkan menu lainnya sesuai kebutuhan

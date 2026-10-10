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
            "nav-link-selected": {"background-color": "#FF6F00"},
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
            "https://drive.google.com/uc?export=view&id=145Y_CxAqvIIMmkJViJl79KtwLRHe-Xz0",
            "https://drive.google.com/uc?export=view&id=1hsH5kBrIsWbMGuWaamBLK1p0cMVYsmYe",
            "https://drive.google.com/uc?export=view&id=1f-sJNunKJq4RgV2mT13k02ClqziQBqXT",
            "https://drive.google.com/uc?export=view&id=1EHeS4SEcK6W-K0cC-kzcxTyzrcXaeNX5",
            "https://drive.google.com/uc?export=view&id=1tvW6mpRU71sM91CDNoOysA42kPZcMlJ6",
            "https://drive.google.com/uc?export=view&id=1zUfYIoGVAciTYueA1Fsj73-km0IMPb89",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@erendraa",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gHyFbqG5ON4e1efIE9euHLJYaaBbHxkX",
            "https://drive.google.com/uc?export=view&id=1WoF9YcOm5LuMF1nxZ7fTUyCi5zJBEePj",
            "https://drive.google.com/uc?export=view&id=1C3P88A0_c6lQ2tF8PCTXTNGg91Vq7E_h",
            "https://drive.google.com/uc?export=view&id=1mEECA7RFeQMWNGXFXceN-fnoiuSnP-fd",
            "https://drive.google.com/uc?export=view&id=153wfyaRPFJPfPKwW8ulHZ6mUPg0CMZ4O",
            "https://drive.google.com/uc?export=view&id=1fzxIo0OkvsGgLhWEQPb4ASsPtEcag1lM",
            "https://drive.google.com/uc?export=view&id=1ppbnj2C6D8-GFVjBFH20UL07UEKQpb8h",
            "https://drive.google.com/uc?export=view&id=1eZOzu_aMTvDYD4gkOCXN4LU6ofi5LPuN",
            "https://drive.google.com/uc?export=view&id=1478dLYzoqWC-Cfb55WX1VSQexxiIb9cI",
            "https://drive.google.com/uc?export=view&id=15u6Z-rI0xun3nLOQ1fJGS6RjIEw6qTW1",
            "https://drive.google.com/uc?export=view&id=1ZUMdMKYBw10E7jx86X8aBj48784gwntw",
            "https://drive.google.com/uc?export=view&id=1k87H0K6ejPRgZsq62D6UQ-ZvOzyPRrNR",
            "https://drive.google.com/uc?export=view&id=1kj4AfkV3KvPqhqwuw-zpXjlT9wWRbBU3",
            "https://drive.google.com/uc?export=view&id=1SR8jx_vkm6IoUPtzR1aHNL1EIpNUusf2",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122340022",
                "umur": "21",
                "asal":"Nusa Kambangan",
                "alamat": "Lapas, Belwis",
                "hobbi": "Melarikan diri",
                "sosmed": "@jeremia_s_",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "-",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Iw0p3BgYhbUNXOILCANFI1JhaOLL4y2Q",
            "https://drive.google.com/uc?export=view&id=1qe2N_K_aefruMrxtj-cBBxLKUCG5n_zD",
            "https://drive.google.com/uc?export=view&id=1ACJ3Ptu0_xucs_UCDdF0-x7drydSzG7u",
            "https://drive.google.com/uc?export=view&id=1Nz-BybbofaOtMFjvZbMQcJMBnsloyf03",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Tanya Caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ce7NSFf7uBUOsc9DJ4uw4jdLtxzRlszT",
            "https://drive.google.com/uc?export=view&id=1Rzvf_wovWuzlvRtJh2DasTkPKnwUbqEk",
            "https://drive.google.com/uc?export=view&id=19i9kH2oGciDsqvBvTWhDql2waOaHOsA7",
            "https://drive.google.com/uc?export=view&id=19Sf3SSotXRXJqzQLgtfcczVxGeOAFrv_",
            "https://drive.google.com/uc?export=view&id=1URDiGwuI5NDwDp4HU6aNVL4iUgpco_De",
            "https://drive.google.com/uc?export=view&id=13lDH8hkDxpl0e7VbI5CTzcmYCSGcIYhK",
            "https://drive.google.com/uc?export=view&id=10x8CYMTZPxjiEwK0UULq9LxLaISjUhRZ",
            "https://drive.google.com/uc?export=view&id=1Q9n5jxO9rnjaxxWofZztUNSDksh4BI0l",
            "https://drive.google.com/uc?export=view&id=1VaMzRcv1Z_mwx4KHLzsO8l6bFjlBu0sH",
            "https://drive.google.com/uc?export=view&id=1n07juTLtyMU1jt58Mfuuk4bVD59CEEE0",
            "https://drive.google.com/uc?export=view&id=1URDiGwuI5NDwDp4HU6aNVL4iUgpco_De",
            "https://drive.google.com/uc?export=view&id=1jjWdhp6SnYwep4azW48-RsuJhinmARHz",
            "https://drive.google.com/uc?export=view&id=14yTuhRrQ4YRoxPovRmRww0edt41emvNs",
            "https://drive.google.com/uc?export=view&id=17ANGN1lWd2UDxna4jgCye3YAZsMJXR_a",
            "https://drive.google.com/uc?export=view&id=1K1YcNCUd9Y4hi3DORU6wGk5ueZIPTP8R",
            "https://drive.google.com/uc?export=view&id=1P9vYPPZ0_8wnpDkAKPwnftNS7nqgHAYl",
            "https://drive.google.com/uc?export=view&id=1-GJ1BfBS2mjlV9907R9c6EtvzSDD1Xhl",
            "https://drive.google.com/uc?export=view&id=1xCntzIuVtHhU22EwUiyHJQrR9wS5dwH8",
            "https://drive.google.com/uc?export=view&id=1C7Q6aNRGD9_FsfMasDuGCny9ZSVUp6kx",
            "https://drive.google.com/uc?export=view&id=1MZqwCrKe6q0Tz9PANgsDAJ7tZgbZOJEZ",
            "https://drive.google.com/uc?export=view&id=1DN8pJMaLdGaF6YIO-89sZc-XqpJNGylv",
            "https://drive.google.com/uc?export=view&id=1YdJVPUaIxK1bZ0KawkA54gehttxW6AQA",
            "https://drive.google.com/uc?export=view&id=1aFB-6HrOoDZ8ShVuEWfvRx3T6ugZv3Bf",
            "https://drive.google.com/uc?export=view&id=1381b8pnOtZtf6nx6u3EbpOJtNmkgZiar",
            "https://drive.google.com/uc?export=view&id=1eCxMerg42Cgii4R7_FNnEErtLxdWGlx1",
            "https://drive.google.com/uc?export=view&id=1mkIzKUItigetPPMcYI9qz-t-IyBg8zin",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "keren banget abangnyaaa jadi kadep PSDA",
                "pesan": "semangat terus bang kevin jangan pernah capek capek ya buat bimbing kami"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya cantik banget masyaallah",
                "pesan": "semangat kak afifah, makasih ya kak dah bimbing kami selama ini dan buat kakaknya jangan pernah nyesel ya bimbing kami angkatan 24 ini "
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "kak Allya ini berwibawa kali, walaupun lagi marah gitu tetep keliatan elegan, pasti, dan tegas banget jadi kek bikin orang langsung segan",
                "pesan": "buat kak Allya makasihh banyak ya kak dah bimbing kami ngajarin kami, pesannya semangat terus ya kakk dan jangan pernah nyesel karna bimbing kami ini kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "kesannya bang Ahmad ini berwibawa, keren bangett jadi sekjen PPLK kemaren, pembawaannya tenang tapi pasti keliatan banget wibawanya sama pinternya",
                "pesan": "semangat bang Ahmad dan jangan pernah capek buat nginspirasi orang-orang, sama semoga jadi presma betulan Aamiin"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "pertama kli liat di wardat canti kakaknya, sama aku sering liat kak arien di banyak acara, sama ini juga pernah liat pas riuh wisuda sama kak Allya",
                "pesan": "semanagat kak arien jangan lupa jaga kesehatan ya kaa"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "sumpahh bang daffa dari dulu mukanya komdis banget bikin orang takut, tegas banget juga orangnya, pokoknya kerenlahh",
                "pesan": "jangan lupa tidur sama jaga kesehatan ya bangg"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "jujur mukanya islamic banget tapi ternyata kristen, terus keren berwibawa gitu, baik bangett sumpilll ",
                "pesan": "semangat bang fajar makasih ya dah bimbing kamii jangan pernah capek jadi orang baik yaa"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "pertama kli liat kak nata di wardat, cantik orangnya",
                "pesan": "semagat teruss buat kak nataa yaa"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "bang nobel tegas juga orangnya, mukanya kek ngga pernah senyum seringnya tanpa ekspresi ",
                "pesan": "semangat kuliahnya ya bangg "
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "berwibawa bangett, tatapannya ini kayak tajem banget klo ngeliat orang",
                "pesan": "semangat ya baangg jalani hidupnyaa"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kak Vany mirip banget sama temen smp sma aku, lucu manis gitu kakaknya",
                "pesan": "semagat ya kak jangan pernah nyerahh"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "abangnya seruu bangett suka ketawa juga, pertama kli liat di fg kemaren terus juga asik buat ngobrol abangnya, sama keren pas maen badmintonnya",
                "pesan": "seamngatt teruss bang, semangat juga badmintonnya"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya baikk keren juga",
                "pesan": "semangat terus bang jagan pernah nyerahh"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "kakaknya imut banget, lucu cantik juga ngga bosenin liatnya,sama murah senyum juga, kayak orang jepang aku liat kakaknya",
                "pesan": "semangat teruss ya kakk sama jangan lupa jaga kesehatan"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya cantik, baby face juga, baik aslinya, lucu apa lagi klo lagi senyum",
                "pesan": "semangat ya kak kharizmaa klo capek istirahat ya kak"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kakaknya asik banget sama baik jugaa, seruu pokoknya",
                "pesan": "kak rossa semangat yaa, klo capek istirahat kak jangan lupa jaga kesehatan juga ya kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "kesan pertama kukira diem, cuek gitu, ternyata enggak seruu banget buat sharing-sharing pengalaman",
                "pesan": "semangat terus bang, klo maen game jangan sering begadang"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "kesannya tenang banget pembawaanya",
                "pesan": "semangat terus bang kuliahnya"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "kesannya tegas banget abangnya, keren jugaa",
                "pesan": "semangat kuliahnya bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "kesannya baik kakaknya, ramah bangett",
                "pesan": "semangat ya kakk, jangan lupa jaga kesahantan"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "lucu abangnya kocak juga bikin orang gampang ketawa, baik jugaa, humble plus humoriss bangett sumpilll",
                "pesan": "semangat kuliahnya bang jangan bosen buat berbagi tips kuliahh"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "abangnya seruu bangett",
                "pesan": "klo capek istirahat bang semangat terus yaa"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "kakaknya baik banget ramah jugaa",
                "pesan": "semanagat kak, jangan lupa jaga kesehatan"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "abangnya seruu bangettt",
                "pesan": "semangat terus bangg jangan peranh putus asa"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "ngga espect abangnya kocak juga, kukira cuek gitu",
                "pesan": "semanagt bang klo capek tidurr bang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "kakaknya baikk banget ramah juga",
                "pesan": "semagat kuliahnya kak jangan lupa jaga kesahatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=105JjeecgRUC66F9F2EMoENgPapQDNmOm",
            "https://drive.google.com/uc?export=view&id=1yRedvYjBKe9467QYwi83Wr6b7H1jeR8h",
            "https://drive.google.com/uc?export=view&id=1x9_6QujuuuAzaliD8R4Qj7sFt4QhMgmw",
            "https://drive.google.com/uc?export=view&id=1jPWgEWvvrBc2K780ardws1VtglgnjV81",
            "https://drive.google.com/uc?export=view&id=1wqt-9p7zCVp5X7HNJDiqCdjaaIqnN7Ne",
            "https://drive.google.com/uc?export=view&id=1gZEY1y9-Lg96cePCB-wfutEQUEoz-km4",
            "https://drive.google.com/uc?export=view&id=1C-HGNjiiJRPlVMjzyXesie58bYBVVyxp",
            "https://drive.google.com/uc?export=view&id=1B6dughEPnzD5GQUR37BbErOhUSHAImsI",
            "https://drive.google.com/uc?export=view&id=1QVDyRf39VQ8ZnpI4_fCRLC2m5iauTNqH",
            "https://drive.google.com/uc?export=view&id=1n5SX_4k27ZvUjHaxl4UuGLJDJLQB12WV",
            "https://drive.google.com/uc?export=view&id=1cVQK3K8m0S3L2OkSmFFOKOz58U5ntP5L",
            "https://drive.google.com/uc?export=view&id=1hqYU4VdnE3ZLpKzBzoLaJJsPGHcgJimj",
            "https://drive.google.com/uc?export=view&id=18VhAAntpCrLDynxYbUoDy6tuSNm3RcEt",
            "https://drive.google.com/uc?export=view&id=1xW8ObekDYohghr4jWDEyKdxd-wlrU8Sd",
            "https://drive.google.com/uc?export=view&id=1UZ7DNg3Un2dC3I6FPWOK28jgcTZuEQXS",
            "https://drive.google.com/uc?export=view&id=187i6mJ_syp97J6RYJLj866BuMNudo6Vu",
            "https://drive.google.com/uc?export=view&id=1deCWJF7rySsjhV5nKloGutVcjflDb6EY",
            "https://drive.google.com/uc?export=view&id=1gM6E7QvVJjDBGd_alwfVnZd4YC_PWqa4",
            "https://drive.google.com/uc?export=view&id=1J3nGXBmy6iZzMqejRkObePqCf_EtdevF",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=14cNbTZ5thUWOusb5Ymu4LIFzNCy87V2O",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123440083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "kesannya keren banget bang randraa, baik dan ramah juga abangnya",
                "pesan": "semangat terus bangg klo capek istirahat ajaa"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yCYeniNsH3qgW8wvdS5S5mtP0Eft2SUg",
            "https://drive.google.com/uc?export=view&id=1EatAGV_SBVdfxeXdv8SkYidqYDQoUG1n",
            "https://drive.google.com/uc?export=view&id=1BClipK4jaT6ncdGHh-V89v6ejoSaXS7c",
            "https://drive.google.com/uc?export=view&id=1EatAGV_SBVdfxeXdv8SkYidqYDQoUG1n",
            "https://drive.google.com/uc?export=view&id=1WxfbS5HuslEGcTvpvT8KPKn-ltwCUbTi",
            "https://drive.google.com/uc?export=view&id=1hBaLEh7mEWtJQGyhmZknLY8LmYNxVeab",
            "https://drive.google.com/uc?export=view&id=1g9Ye-Qo00vve-AC0hSfF-tBDRU1pkJxo",
            "https://drive.google.com/uc?export=view&id=1mNZKRF1M5Yu268QAbMr51ZJR2S6YuztZ",
            "https://drive.google.com/uc?export=view&id=11iZ3t5nV4k9AVPn__wkKifr-NAcOzhZb",
            "https://drive.google.com/uc?export=view&id=1AcW5_Ya3lIZsFLrdJpabZxuvV0NJ_dG1",
            "https://drive.google.com/uc?export=view&id=19YOqr61uvd0WP3wEklXIZdu4WOQXgiSl",
            "https://drive.google.com/uc?export=view&id=10zJrjqd5u4E3eBqSSxSgnHnod--6lr51",
            "https://drive.google.com/uc?export=view&id=1PCBRFtZXRCNv-sXF6FEIfv_AHr6QXgkS",
            "https://drive.google.com/uc?export=view&id=1Gi38OL0PHiB-xTk6wKdeWU5dwRL63-OD",
            "https://drive.google.com/uc?export=view&id=1a9hFGU8w5h51K_NtaSusITuihRPLv3ms",
            "https://drive.google.com/uc?export=view&id=1NOIMODJb1fMro8m2S_FwUPw-pt3Nh-9B",
            "https://drive.google.com/uc?export=view&id=1_omIfpU5H2WBRiK0wiZiyWOaweLpnxHU",
            "https://drive.google.com/uc?export=view&id=1qui4tXXHM9XUbAxUQEw64_cqmJtfUfV4",
            "https://drive.google.com/uc?export=view&id=156ws3r6qqc3iLfkMIYJzT8S618ZJYM2I",
            "https://drive.google.com/uc?export=view&id=1JIjxXNKDZbz2KoN-9zAdJqwypi00qtfN",
            "https://drive.google.com/uc?export=view&id=165dG091UCuHY9jS5wRq-ZyTEp8RprhAe",
            "https://drive.google.com/uc?export=view&id=1ULwEUSxJA8suo4qqE0-kmngXf0hnbeHI",
            "https://drive.google.com/uc?export=view&id=10TjxpH86kI81E_PDvpQM1z8U1_QCBHod",
            "https://drive.google.com/uc?export=view&id=1RQH43jcqApGghpPHvIfVrCYNTAepQa1o",
            "https://drive.google.com/uc?export=view&id=1q6hkdQvUjUnerwh_Xl6Jeb5hQU54Yv_7",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "abangnya keren adem juga liatnya",
                "pesan": "semangat kuliahnya bang klo ngantuk tidur bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kakaknya cantik, abik hati dan tidak sombong",
                "pesan": "semangat kak klo capek jangan lupa buat istirahat"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "kakaknya cantik baik hati dan tidak sombong",
                "pesan": "semangat kuliahnya kak klau capek istirahat dan jangan lupa jaga kesehatan ya kakk"
            },
           {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "kakaknya baik hati cantik juga dan tidak sombong lagi",
                "pesan": "semangat kuliahnya kakk jangan lupa buat istiraaht ya kaa"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "keren abangnya kece bener ",
                "pesan": "semangat kulaihnya bang jangan lupa untuk istirahat"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kakak mut emang betul betul imut cantik juga kukira jutek gitu ternyata baik banget lucu juga",
                "pesan": "semangat kuliahnya kak klo capek istirahat dan jangan lupa jaga kesehatan yaa "
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakanya catik baik hati dan tidak sombong",
                "pesan": "semangat kuliahnya jangan pernah nyerah ya kaak"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "ihhh kakaknya cantik baik hati jugaa",
                "pesan": "kakaknya semangat terus ya janagan peranh nyaerah klo capek istirsahat dulu akak"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "keren banget abangnya, bagi dong tipsnyaa",
                "pesan": "semanga terus kuliahnya kaka klo capek istirahat yaa"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "keanl dan tau akaknya karean mc pas pplk tahun 24 keren banget asik juga orangnya",
                "pesan": "semangat terus kuliahny akak, klo capejk jangan lupa buat istirahat ya kak, janagn terlalu dipaksain"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "kakanya keren abnget ihhh cantik dan baik hati pula",
                "pesan": "semangat kakak klo capek istiraahat yaa sama janagan lupa jaga kesehatan ya kak"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "kakaknya keren banget pertama kli tau pas akaknya jadi mc pplk 24 keren banget asik juga orangnya",
                "pesan": "semangat kuliahnya kak klo capej\k janagan lupa istirahat ya kaka"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "bang desamn ini asik tapi jail banget sumpilll, sakjane takut aku tapi diasikin ajalah hehe btw bang desnman ker",
                "pesan": "semangat kuliahnya bang klo capek  bangistirahat bang jangan peranh nyerah yaaa"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "plisss kakakny abaik banget, maksih ya akka dah bantuin pas praktikum ads dan ngasih perpanjangan waktunyaa, btw kKNY AKEREN bangett pembawaannya selalu energik gitu selalu semanagat",
                "pesan": "semangat kuliahnya kak janagan lupa jaga kesehatan ya kakkk klo capek janagan lupa buat istirahat ya kak"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "kakanya lucu banget hobiny akasian bang desma dicubitin mulu",
                "pesan": "semangat terus akak klo capek janagan lupa buat istirahat ya kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "keren banget sihhh abangnyaa coba spill rahasianya bang",
                "pesan": "semangat terus bang jangan pernah nyerah nbang buat jalani hidup yaa"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zXbdEMy3V_fOc2_2hCRWB7BZDU5lofL2",
            "https://drive.google.com/uc?export=view&id=1q_6wuJbHK2NjSODtVvWbwfrNTKjtv-l0",
            "https://drive.google.com/uc?export=view&id=1Ki71JeGxQ5AViwKyv-04IEEUCG_C-RfS",
            "https://drive.google.com/uc?export=view&id=1xaBWZtQH0opBhu-lPHk1SCh7h5cPEve0",
            "https://drive.google.com/uc?export=view&id=1Yy_KBnDG9Tu_Wp7WBfUF0HGfcddBk3Kb",
            "https://drive.google.com/uc?export=view&id=1mLzR2ttpZ7ZkNmg2QL-KZ4aFBSVUeEPV",
            "https://drive.google.com/uc?export=view&id=1K0bz53Z4SL3EwjVjB6z-SUF5FgebhjEC",
            "https://drive.google.com/uc?export=view&id=1Z68Qgk87og_V5xnP0zlgtkmFZHAnrJFF",
            "https://drive.google.com/uc?export=view&id=1fJ9Vi8awOblGDjphPhCFqnMrdqgXEK-E",
            "https://drive.google.com/uc?export=view&id=1X4CXV13awpYbihyquhFyMoz9ZCG2_vZ7",
            "https://drive.google.com/uc?export=view&id=1I_Baa18kGlggkkJFC3JyO887O-PWTt7K",
            "https://drive.google.com/uc?export=view&id=1xsrLLYD7WD_rhfVPjNC_6thtaTiojMLm",
            "https://drive.google.com/uc?export=view&id=1MHK7mvmVjq9v_OUi-a2v1XrsaifOmus-",
            "https://drive.google.com/uc?export=view&id=1B-bCgWB2om9n4CIZQ4vUfzyLdArs5tVf",
            "https://drive.google.com/uc?export=view&id=1NMCiUvNsMgE7MZQtMm3WEgvYPZecf507",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Balam",
                "hobbi": "mengaji",
                "sosmed": "@ranniku",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 3
            },
            {
                "nama": "Rendy",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17E4zTPC0qWM2ZUn_nmpVhqdhyozGlRzX",
            "https://drive.google.com/uc?export=view&id=1g8vGBX-GlPLERw6grEk1eRqm6xu3CGy_",
            "https://drive.google.com/uc?export=view&id=1_4ok8LBBl_JugEmCq3obeA8DqP85UERL",
            "https://drive.google.com/uc?export=view&id=1hv0d_fTA1mNuUVpNO1Zm_WNAHMEtlzf5",
            "https://drive.google.com/uc?export=view&id=156dMsFnZpgfyGzuoAGmoMJSRltUiSeji",
            "https://drive.google.com/uc?export=view&id=1UNpovMjEMW8Eou-03wlrwi_iZm8gwJId",
            "https://drive.google.com/uc?export=view&id=1fsDP70-0lcAIwi2MEpAW9XSAh_cFnvFN",
            "https://drive.google.com/uc?export=view&id=1BpES7j-SfM3DgkXMaHNXjzNeAXZsxaSf",
            "https://drive.google.com/uc?export=view&id=1Wh_5w79DVbKBRKwnn_tP-PM11Vu0NPlo",
            "https://drive.google.com/uc?export=view&id=1a0vKFpB6N_KrrpyWW7T1X40kKjtaatLD",
            "https://drive.google.com/uc?export=view&id=1MZbPyMC0rWLi6aPS0UG7he15k99nDPuR",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "@dananghk_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mvW0B6LEBEc-PaLyPitEq0X6ZwN_eDIT",
            "https://drive.google.com/uc?export=view&id=1sAHUf9SL-BmpwZf9vj8qaINxPUKzTwT1",
            "https://drive.google.com/uc?export=view&id=1RM8ovjo0UEf8w_ZkMTejtlqTPcbNw03-",
            "https://drive.google.com/uc?export=view&id=1wnjQoEuBJ5KWZDWxtIbES0Xm17m_fms6",
            "https://drive.google.com/uc?export=view&id=1QzSsia_DqFKzU4BxsKq2aJCcjchBjzSy",
            "https://drive.google.com/uc?export=view&id=1XxBM6wXUlCeQLFPMM4aFZzi7tPyRibH3",
            "https://drive.google.com/uc?export=view&id=16VTRozo8J6yEQbT6MMELCvKz4f_bOest",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1N0msIcY6uCI8oEi3_L77B1uZdt7HOng4",
            "https://drive.google.com/uc?export=view&id=109VDZ7sY9HRcEp0_25Io7N5hS-57bWfY",
            "https://drive.google.com/uc?export=view&id=1GYDPOBvSY1T-wAIxzy06Gx1-EvKuudMG",
            "https://drive.google.com/uc?export=view&id=1gp1VMR6KcT_Q_fygYk12J616LoOa5M0-",
            "https://drive.google.com/uc?export=view&id=1PHmTbOY5sVn7FGaEBl89UAz89QirJFlZ",
            "https://drive.google.com/uc?export=view&id=13WZTDyQTFz6sbXFplAdq8ObZiXQtLJl2",
            "https://drive.google.com/uc?export=view&id=120zGBvkPB-koojp7NnYjpq66e-p8uC1p",
            "https://drive.google.com/uc?export=view&id=1C_AByiwSDBEUmAuW08JH-TcrCLO6FyaJ",
            "https://drive.google.com/uc?export=view&id=1aKMBo10TeWaHDWYf_pWdynhLCWwJsB8w",
            "https://drive.google.com/uc?export=view&id=1b4k4JNECZ_Tt2Cu8zfkXYWV0cC4Mb5RY",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jati Mulyo",
                "hobbi": "sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 14
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()











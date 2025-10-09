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
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#1
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#2
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#3
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#4
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#5
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#6
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Abangnya tegas tapi asik",  
                "pesan":"Tetap jadi orang baik ya bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "baca buku (dasar-dasar sql)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Semangat kuliahnya bang"# 2
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Airest Kost",
                "hobbi": "siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakaknya cantik dan asik",  
                "pesan":"semangat terus kuliahnya kakak"# 3
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya asik bangett ",  
                "pesan":"semangat terus kuliahnya kakak"# 4
            },
            {
                "nama": "Eksanty F. Sukma Islamiatyr",
                "nim": "12245001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "rajabasa",
                "hobbi": "baca buku , saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya asik bangett ",  
                "pesan":"semangat terus kuliahnya kakak"# 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"kota Padang,Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya asik bangett ",  
                "pesan":"semangat terus kuliahnya kakak"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#1
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#2
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#3
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#4
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#5
            "https://drive.google.com/uc?export=view&id=1uP1mFV5cHxa6Ot5JHsTF5fljIOKvQAVX",#6
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "",  
                "pesan":""# 2
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 3
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 4
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "baca buku , saku pramuka",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 5
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg cabe",
                "sosmed": "@farahanumafifah",
                "kesan": "",  
                "pesan":""# 6
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""#7
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""#8
            },
            {
                "nama": "Berliana Enda Putrii",
                "nim": "122450065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""#9
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "mendengarkan wave to earth",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""#10
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""#11
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""#12
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450042",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""#13
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""#14
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()




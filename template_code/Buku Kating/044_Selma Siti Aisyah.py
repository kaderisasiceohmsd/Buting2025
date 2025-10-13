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
            "https://drive.google.com/uc?export=view&id=14IrtKlH2ueg1CeXPL6st2FscLscAJ2SY",
            "https://drive.google.com/uc?export=view&id=1ox1yK7cFvulq44RL5ljUbsR4Dy08S5-Y",
            "https://drive.google.com/uc?export=view&id=1IqPH3oeHcEIpFYkCdn3Iq9KBlz3pIxwP",
            "https://drive.google.com/uc?export=view&id=1ZD5ybZV18rNhZHIQuhPjz1Pyi4MOUDQL",
            "https://drive.google.com/uc?export=view&id=1gHbfG95RPgOT-cT6c9jMejieNYZj0ioe",
            "https://drive.google.com/uc?export=view&id=1WdcP0ZL92Vobb1SAYr8O4hdQdbVvzwaj",

        ]   
        data_list = [
            {
                "nama": "Rendra Eka Prayoga", 
                "nim": "122450122",
                "umur": "21",
                "asal":"Pulau Damar",
                "alamat": "Gg.sakum",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",  
                "pesan":"semangat terus kuliahnya abang!!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan. Lapas Raya",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya abang!!!"# 2
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya kakak !!!"# 3
            },
            {

                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cute Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya kakak !!!"# 4
            },
            {

                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya kakak !!!"# 5
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal": "Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya kakak !!!"# 6 
         },  ]
        []
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xiyxnQ14j_juLL8brNS_3Y-QiwQqmsXf",
            "https://drive.google.com/uc?export=view&id=1VfNy1c5VshwdNgur2SamAYNt383sPwcv",
            "https://drive.google.com/uc?export=view&id=18zYDQWjfR7PoQAQUpdRU63TDtNiGSbeX",
            "https://drive.google.com/uc?export=view&id=1W394vnpowF15bJyek5QRJRnZTXKlb-Qn",

        ]   
        data_list = [
            {
                "nama": "Ryan Bintang Wijaya", 
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Tanya Caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini asik dengan hobinya main padel, dilihat sangat asik ketika berdiskusi",  
                "pesan":"semangat terus kuliahnya abang!!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik suka main roblox, sangat memotivasi",
                "pesan":"semangat terus kuliahnya kakak!!!"# 2
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakak ini asik saya suka mendengarkan musik, sama saya juga",
                "pesan":"semangat terus kuliahnya kakak !!!"# 3
            },
            {

                "nama": "Fathinah Nur Azizzah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi":  "live instagram",
                "sosmed": "@fathinahazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya kakak !!!"# 4
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

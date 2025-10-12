
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
            "https://drive.google.com/uc?export=view&id=1WQOU1XgHWuhuqejkLu_HKjU5gAb4F-pS",
            "https://drive.google.com/uc?export=view&id=1SdgYKOKfyiNqrdNc18ss5HEJGkmSQKXq",
            "https://drive.google.com/uc?export=view&id=13hS7Qn82zZxqwHNTzA5TUg74vy-uRt8l",
            "https://drive.google.com/uc?export=view&id=1UPIP0PY4PtBQjjbmaaRce0MA5SCSIV3V",
            "https://drive.google.com/uc?export=view&id=1e6iKrDmoxcF2UCvDbNGtR0sl9RG7G9E5",
            "https://drive.google.com/uc?export=view&id=1EFxH-yQUhwBEpoIaDOnQYgLOgfb5Veej",
        ]
        data_list = [
            {
                "Nama"   : "Rendra Eka Prayoga",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "Nama"   : "Johannes Krisjon Silitonga",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "Nama"   : "Elisabeth Claudia Simanjuntak",
                "NIM"    : "122450123",
                "Umur"   : "24",
                "Asal"   : "Baduy Pedalaman",
                "Alamat" : "Agres Kos",
                "Hobbi"  : "Makan Kuaci",
                "Sosmed" : "@celisabethh_",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Syadza Puspadari Azhar",
                "NIM"    : "123450072",
                "Umur"   : "21",
                "Asal"   : "Palembang",
                "Alamat" : "Belwis",
                "Hobbi"  : "Membaca",
                "Sosmed" : "@puspadrr",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Eksanty Febriana Sukma Islamiaty",
                "NIM"    : "123450001",
                "Umur"   : "21",
                "Asal"   : "Wakatobi, Sulawesi Tengah",
                "Alamat" : "Mutun, Pesawaran",
                "Hobbi"  : "Ngomenin Tiktok Cewek Cantik",
                "Sosmed" : "@eksantyfebriana",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Farahanum Afifah Ardiansyah",
                "NIM"    : "123450056",
                "Umur"   : "21",
                "Asal"   : "Padang, Sumatera Barat",
                "Alamat" : "Gya Kos, Korpri",
                "Hobbi"  : "CUTE Jen",
                "Sosmed" : "@farhanumafifahh",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
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
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    Baleg()

if menu == "Senator":
    def Senator():
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
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1n7zYC3CHqYXJvOxjhobhWVl6_LwvF1dc",
            "https://drive.google.com/uc?export=view&id=1v7_TugMNDohNn6UzFhDnNWYrtI5C9FLW", # Ketua
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Sekre
            "https://drive.google.com/uc?export=view&id=1Am4CkzFMmBQ7KA5bozrNMa3bVH7e-1_a", # Kader
            "https://drive.google.com/uc?export=view&id=1DakRsLOtzcUpvcVTX78R8Vgu4qeSt_QU",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1HnwfvsuowuJ3XI5haZDrVso05gDsN0iw",
            "https://drive.google.com/uc?export=view&id=1nONNhWLeiMEue91rYERX975trE7u-vl1",
            "https://drive.google.com/uc?export=view&id=1bdxJvsjCtDtj8fYobKDXtgnZLt6Se-aV",
            "https://drive.google.com/uc?export=view&id=1CKFPOAxZVh-SEpwJn9iM2XAM7QwsZjj7",
            "https://drive.google.com/uc?export=view&id=1ongA0PXCyPw97qXGQLZJbnDXMiwk0H44",
            "https://drive.google.com/uc?export=view&id=1RhAbCC3u1Alv6jgDXoGrCC-zac_t45Lp",
            "https://drive.google.com/uc?export=view&id=1-F1PIECRIoZRyvEztVrKFHAZWw9tOLOZ", # Mankom
            "https://drive.google.com/uc?export=view&id=13NKIQX_8sbFHzFH1v8yiL_OfW9WXyTLK",
            "https://drive.google.com/uc?export=view&id=1Wpqa_Mfu9pFTv1yMxiYXggScgtjparEe",
            "https://drive.google.com/uc?export=view&id=1-Ikdw_getIAT_CmpWkh0BxFvAIo9h8fj",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1n7zYC3CHqYXJvOxjhobhWVl6_LwvF1dc",
            "https://drive.google.com/uc?export=view&id=1Uo_8_mvxyMeTfoiDzPDW8pIkztdbSI1_", # Manjakat
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  
            "https://drive.google.com/uc?export=view&id=1HN_KK9b3jWuihdGmupdYg4IMg0VaNS_c",
            "https://drive.google.com/uc?export=view&id=1k0Am0OgOJlkn2SjbEwfdzAziMpHzwIFb",
            "https://drive.google.com/uc?export=view&id=18VFjY8F742YEbU1YCSLDDfqJ_benRI7Q",
            "https://drive.google.com/uc?export=view&id=1_7rd-ngR55UZJopBAb0I3Ns4BSBzdWb_",
            "https://drive.google.com/uc?export=view&id=1YLFBPxvkE7PsuG1026nB7ZZH2iY0VuKP",
        ]
        data_list = [ 
             {
                "Nama"   : "Ferdy Kevin Naibaho",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
             {
                "Nama"   : "Nisrina Nur Afifah",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Allya Nurul Islami Pasha",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
               "Nama"   : "Ahmad Rizky",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Arienta Khusnul Ananda",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Daffa Hadyan Navista",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
            {
                "Nama"   : "Ginda Fajar Riadi Marpaung",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
            {
                "Nama"   : "Natasya Amavisca",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "Nama"   : "Nobel Nizam F",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Nurul Alfajar Gumel",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Vany Salsabila Putri",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Ahmad Sahidin Akbar",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Ali Aristo Muthahhari Parisi",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Gusti Putu Ferazka",
                "NIM"    : "12345006",
                "Umur"   : "20",
                "Asal"   : "Bekasi",
                "Alamat" : "Way Dadi",
                "Hobbi"  : "Tidur",
                "Sosmed" : "@ferazkaa",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Kharisma Mustika Sari",
                "NIM"    : "123450034",
                "Umur"   : "20",
                "Asal"   : "Way Kanan",
                "Alamat" : "Untung",
                "Hobbi"  : "Scroll Tiktok",
                "Sosmed" : "@rismaa.mustika_",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Rosalia Siregar",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Sahid Maulana",
                "NIM"    : "122450109",
                "Umur"   : "22",
                "Asal"   : "Depok, Jawa Barat",
                "Alamat" : "Airan",
                "Hobbi"  : "Game",
                "Sosmed" : "@Sahid_maul19",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Daffa Ahmad Naufal",
                "NIM"    : "122450137",
                "Umur"   : "21",
                "Asal"   : "Jakarta",
                "Alamat" : "Korpri",
                "Hobbi"  : "Bersihin Jendela",
                "Sosmed" : "@ahmadnaufal_11",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Erma Daniar Safitri",
                "NIM"    : "123456789",
                "Umur"   : ".....",
                "Asal"   : ".....",
                "Alamat" : ".....",
                "Hobbi"  : "....",
                "Sosmed" : "@i",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Ihsan Maulana Yusuf",
                "NIM"    : "123450110",
                "Umur"   : "20",
                "Asal"   : "Sumatera Barat",
                "Alamat" : "Pemda",
                "Hobbi"  : "Servis Laptop",
                "Sosmed" : "@ihsan.myusuf",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Kevin Antoni Junior",
                "NIM"    : "123450109",
                "Umur"   : "20",
                "Asal"   : "Bandar Lampung",
                "Alamat" : "Panjang",
                "Hobbi"  : "Menanam Padi",
                "Sosmed" : "@kevinaj__",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Lidia Natasyah Marpaung",
                "NIM"    : "123450015",
                "Umur"   : "20",
                "Asal"   : "Medan",
                "Alamat" : "Pemda",
                "Hobbi"  : "Merajut",
                "Sosmed" : "@dla_natzzyaa",
                "Kesan"  : "kakaknya baik 😊",  
                "Pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "Nama"   : "Muhammad Ridwan",
                "NIM"    : "12345091",
                "Umur"   : "20",
                "Asal"   : "Kota Gajah",
                "Alamat" : "Belwis",
                "Hobbi"  : "Badminton",
                "Sosmed" : "@m.ridwaan_22",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "Nama"   : "Uliano Wilyam Purba",
                "NIM"    : "122450098",
                "Umur"   : "19",
                "Asal"   : "Depok",
                "Alamat" : "Jl. Raden Saleh",
                "Hobbi"  : "Ngoding, dan Bermain Musik (Angklung)",
                "Sosmed" : "@_",
                "Kesan"  : "Abangnya keren 😎",  
                "Pesan"  : "semangat terus kuliahnya bang !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
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
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
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
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
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
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
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
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
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
    Departemen_Medkraf()

# Tambahkan menu lainnya sesuai kebutuhan
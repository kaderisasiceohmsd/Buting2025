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
            "https://drive.google.com/uc?export=view&id=154kH_9W5qc3vr_kF_3rFlj0COJUIjTHz", #Bang Rendra Eka Prayoga
            "https://drive.google.com/uc?export=view&id=1StMrKjc4OGjHIDbxVR847IK1nS3Tw2xz", #Bang Johannes Krisjon Silitonga
            "https://drive.google.com/uc?export=view&id=1S4Z-05PzS09Zyv_2uVz3GuNIf0qZlrH4", #Kak Elisabeth Claudia Simanjuntak
            "https://drive.google.com/uc?export=view&id=1ztnvvgw0bBIjy7knuEEHkcnkgMx6JmCI", #Kak Syadza Puspadari Azhar
            "https://drive.google.com/uc?export=view&id=1W7ekc_re8sGfuEvcdO8BhqEgAwU7gNgw", #Kak Eksanty F. Sukma Islamiaty
            "https://drive.google.com/uc?export=view&id=1y5Wpq1OLmQ7TdDoztHprIphROKOxR-rl", #Kak Farahanum Afifah Ardiansyah
        ]
        data_list =[
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "JL. Lapas",
                "hobbi": "Baca buku sql",
                "sosmed": "@johanneskrisjnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Badui dalem",
                "alamat": "Ayres Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "18",
                "asal":"Wakatobi, Sulawesi Utara",
                "alamat": "Mutun, Paseweran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
                {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumatera Barat",
                "alamat": "Gya kost korpri",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
        ]
        
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fOf-BYWOpXfY3jZQGHXrppUV1XCalWlf", #bang Jeremia Susanto
            "https://drive.google.com/uc?export=view&id=1I_e1GGxhsaEaFUZszUguMkyYGGtR8002", #kak Dhea Amelia Putri
            "https://drive.google.com/uc?export=view&id=1MLSwDB9tYZV6-V-1rJvtXZeYYPHzfSfG", #kak Renisha Putri Giani
            "https://drive.google.com/uc?export=view&id=1WBolNcjo7yJcyndRNKqN2E2haNQ44fAi", #kak Anisa Fitriyani
            "https://drive.google.com/uc?export=view&id=1H6-KKqlEXA_pBAI02QPRabyeoVw8sxLX", #bang Dharu Cahyoaji Sasongko
            "https://drive.google.com/uc?export=view&id=1kdghNEpQX-ArjFPNcix-cz6Szh5b6Xhc", #kak Feby Wulandari
            "https://drive.google.com/uc?export=view&id=1ibfWd1F2i_a-24xnPASKXGtmKUWwGUhY", #bang Givaro Ananta
            "https://drive.google.com/uc?export=view&id=1vKyhRC35PpYReIWkqzbZ2acHiX1D5HIJ", #bang Mirzan Yusuf Rabbani
            "https://drive.google.com/uc?export=view&id=1BgRhaTLQAzdpWRUWovUD8hrhHM3Io70Y", #kak Berliana Enda Putri
            "https://drive.google.com/uc?export=view&id=1rmqtqC_4QVJ4iqXF9YS50faXupnrhFCY", #kak Juesi Apridelia Saragih
            "https://drive.google.com/uc?export=view&id=120Wz37NvuAnMAOauHrSYOAV3uPBGTs8t", #bang Ridho Benedictus Togi Manik
            "https://drive.google.com/uc?export=view&id=12dPPk6HpXxY5McuuWQsRacyfgUplf3YQ", #bang Feryadi Yulius
            "https://drive.google.com/uc?export=view&id=1-dS7gekMceVzL5PRwIOMh58v9MJz5gwE", #kak Monica Patricia Tanjung
            "https://drive.google.com/uc?export=view&id=1Av3S02wBxl8fZuG_DOSIhTo81wH-_6Uk", #kak Wan Nashwa Alhasni Yuska
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
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
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
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
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FhDVNj7OLOSDCuPU-BnX6PKmP2Lz4uJ0", #Bang Rian Bintang Wijaya
            "https://drive.google.com/uc?export=view&id=1AoST77ETgf5M6pHAYxKz0CN6ovIomi5t", #kak Nadya Ratu Anjani
            "https://drive.google.com/uc?export=view&id=1SdYFo9_Nwxdd69I772ZTpvfdMkdRFrdf", #kak Fathinah Nur Azizah
            "https://drive.google.com/uc?export=view&id=1jaiMtjV4tt0OG6bXLZEeoQr-_4yJcFG8", #kak Lia Hana Ichisasmita
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
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
                "nama": "Nadya Ratu Anjani",
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
                "nama": "Fathinah Nur Azizah",
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
                "nama": "Lia Hana Ichisasmita",
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
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qIUz3W8okBFAorK3IvVqcbRf1iLV4G-y", #Bang Ferdy Kevin Naibaho
            "https://drive.google.com/uc?export=view&id=13Lht7BfGKREit-4HjrHtxN22Il6sqbok", #Kak Nisrina Nur Afifah
            "https://drive.google.com/uc?export=view&id=1wksTmaKXJAAH50nKkvHrN16GApwhc114", #Kak Allya Nurul Islami Pasha
            "https://drive.google.com/uc?export=view&id=1qwqrM6eqsF3mJaP1NtqtQsSfIToGhMuF", #Bang Ahmad Rizky
            "https://drive.google.com/uc?export=view&id=1i2VG81B4vL78c0bNAd-GXoJEZuYO1SGM", #Kak Arienta Khusnul Ananda
            "https://drive.google.com/uc?export=view&id=17gWncFgemlkDFnXIDSSRuhyjmzDeVLII", #Bang Daffa Hadyan Navista
            "https://drive.google.com/uc?export=view&id=1CVvlJBrpOv4QahQngpMO_0xiVwzS6GpP", #Bang Ginda Fajar Riadi Marpaung
            "https://drive.google.com/uc?export=view&id=1WELyiRa3PDx_5kyqz2jvBfpzMjAzX11G", #Kak Natasya Amavisca
            "https://drive.google.com/uc?export=view&id=17wXXzG4ZuEkbdY71gvo6nkd2J2o0DI0j", #Bang Nobel Nizam F
            "https://drive.google.com/uc?export=view&id=1H6sEjvx-Fr2HKcCoPJcUduZS4RhUi98b", #Bang Nurul Alfajar Gumel
            "https://drive.google.com/uc?export=view&id=12KgiVCih1l9i1uJoLiVisVq5PnvZrvVy", #Kak Vany Salsabila Putri
            "https://drive.google.com/uc?export=view&id=12BCYOZ0KKhqsGDgVIgYVwXIlbLPR1XSd", #Bang Ahmad Sahidin Akbar
            "https://drive.google.com/uc?export=view&id=170HBzNlazOSHSgQhxceI2LH6PzShw7e-", #Bang Ali Aristo Muthahhari Parisi
            "https://drive.google.com/uc?export=view&id=1NB58mf2edPsQUQFITAqqSUVs2lr78arB", #Kak Gusti Putu Ferazka
            "https://drive.google.com/uc?export=view&id=1TpdMIbqxi7072PWSIeylW7fr7j-F2WPq", #Kak Kharisma Mustika Sari      
            "https://drive.google.com/uc?export=view&id=15VZdhn-Zr0O7DsugpTw2A-NMLRER4p7z", #Bang Sahid Maulana
            "https://drive.google.com/uc?export=view&id=1Ib9G16WOWhOzBcvqLYe2-qmm-C7bgG32", #Bang Daffa Ahmad Naufal
            "https://drive.google.com/uc?export=view&id=1Nnf_lWM_sGE3sfY9tRH4XpORME1cke-P", #kak Erma Daniar
            "https://drive.google.com/uc?export=view&id=1pfVI1BQJdTf3C1R_8JJ7oGkILuzviCn3", #Bang Ihsan Maulana Yusuf
            "https://drive.google.com/uc?export=view&id=1Ok3PSs9HmE1cm3Ab_nBuSrDgs2Y5GhiX", #Bang Kevin Antoni Junior
            "https://drive.google.com/uc?export=view&id=1aQ3guawPQNw6_TKvsqmgoka55UCTipJK", #Kak Lidia Natasyah Marpaung        
            "https://drive.google.com/uc?export=view&id=1utgwo-Pwtq5E9_N7EyRz05WDDd7lNzqu", #Bang Muhammad Ridwan
            "https://drive.google.com/uc?export=view&id=1udchb1OSD8Wx3X9jUobphG0uEzowFmbq", #Bang Benget Sidabutar
            "https://drive.google.com/uc?export=view&id=1UJnIll1mBRnbTqbwjEY-C099vvga4uAR", #Bang Uliano Wilyam Purba
            "https://drive.google.com/uc?export=view&id=1S2dUHHuU-YSCv6k2Pw9VDhsy_iMfeNTg", #Kak Rewina Audrya Melva Sari
            "https://drive.google.com/uc?export=view&id=1Hq5Lxiq9IkVsYN6xuzhQlXLB4DZmAKrM", #Kak Rosalia Siregar
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
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
                "nama": "Nisrina Nur Afifah",
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
                "nama": "Allya Nurul Islami Pasha",
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
                "nama": "Ahmad Rizky",
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
                "nama": "Arienta Khusnul Ananda",
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
                "nama": "Daffa Hadyan Navista",
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
                "nama": "Ginda Fajar Riadi Marpaung",
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
                "nama": "Natasya Amavisca",
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
                "nama": "Nobel Nizam F",
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
                "nama": "Nurul Alfajar Gumel",
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
                "nama": "Vany Salsabila Putri",
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
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
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
                "nama": "Gusti Putu Ferazka",
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
                "nama": "Kharisma Mustika Sari",
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
                "nama": "Sahid Maulana",
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
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Bebersih kod",
                "sosmed": "@ahmadnaufal_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
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
                "nama": "Ihsan Maulana Yusuf",
                "nim": "122450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Joki strava",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "122450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertani",
                "sosmed": "@kevinaj__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "122450013",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "122450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton yt pak tamaro",
                "sosmed": "@ridwan122",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "122450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "kerjain soal MTK",
                "sosmed": "@liano.wan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "122450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl.Ratu, Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@rewinaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "122450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MoE_wwXR5al-Bz3VGTzwJHSuLL8HfDGf", #Bang Randa Andriana Putra
            "https://drive.google.com/uc?export=view&id=1doyFBIoxIaNYRpFvCRTut2r-O2yHvBdh", #kak Rut Junita Sari Siburian
            "https://drive.google.com/uc?export=view&id=1LEpyVqOQIYLsKw1TVoPYkz7lYxsM2o28", #Bang Muhammad Regi Abdi Putra Amanta
            "https://drive.google.com/uc?export=view&id=1lPNDz17mav-2s-iuput59YoD36cxVgLJ", #kak Aisyah Musfirah
            "https://drive.google.com/uc?export=view&id=1ezVIAdXYd5bCznZjOEbkHaZGZSD0oaYc", #Bang Fadil Prasetyo Alfarizzi
            "https://drive.google.com/uc?export=view&id=1CJ0aPJis1hp3d7fECcXkARGSDJYCTHFW", #Bang Muhammad Aqil Ramadhan
            "https://drive.google.com/uc?export=view&id=17hjiK1ouOuWAUCu3uw5MYEbVs6W7dZWf", #Bang Muhammad Naufal Ramadhan
            "https://drive.google.com/uc?export=view&id=1PT3Y_cGoJ_xFmIvziVgrM0phI_gAUO-N", #Kak Nadia Faraj Alyafaatin Simbolon
            "https://drive.google.com/uc?export=view&id=1OgiSBXRSScRyCuvic2wYcboR5L-Kzlgm", #Kak Marleta Cornelia Leander
            "https://drive.google.com/uc?export=view&id=1uYIF0yVG9pjsNooJ7dDggKS4zZ8oG2Fq", #bang Akeyla Fairuz shafi
            "https://drive.google.com/uc?export=view&id=1qTR1eH-54q12r-irP8Xu0CSIS5LjnKAq", #Kak Anggi Puspita Ningrum
            "https://drive.google.com/uc?export=view&id=1qUbrY1AFBlani--Bn0kucrccoe1l4-TC", #Kak Efi Defiyati
            "https://drive.google.com/uc?export=view&id=1-MI9FVczXP6XlYEBvclpw4O_QoDl73lL", #Kak Fabiolla Charissa Putri
            "https://drive.google.com/uc?export=view&id=1sktJ5tX9_0tLLo4SdI4s3Hr-dKd9ARLY", #Kak Fairuz Ary Syifa
            "https://drive.google.com/uc?export=view&id=10qwIkHuLV61btVtTcdI06tE8CtuufV8L", #Kak Tanty Widiyastuti
            "https://drive.google.com/uc?export=view&id=1xnRO-ijZAnlHS2Hq2WrNHWO_KgCMeRB0", #Bang Eggi Satria
            "https://drive.google.com/uc?export=view&id=13S16_-aExQ02g87pFkoNFIK5NMtwvu89", #Kak Afifah Fauziah
            "https://drive.google.com/uc?export=view&id=1K3_meeMXK2vrAORYmDVi9ilCmdE5ABqv", #Bang Fabio Banyu Cyto
            "https://drive.google.com/uc?export=view&id=1QQCCMjZC3iU1BeMByrtiTACqwgR_f1lm", #Bang Giofani Aristyo
            "https://drive.google.com/uc?export=view&id=1_uVflCplCzI1_0epqSp5T2dJUD42S-Bx", #Kak Rahma Oktavia Albar
            "https://drive.google.com/uc?export=view&id=1sq5c4EUqT_mLCLFgRDR3Z7IQax3lEbWy", #Kak Rahmah Gustriana Deka
            "https://drive.google.com/uc?export=view&id=1D18mfYTAR2w08v3zd9_cLo4XR_hXXu5m", #Bang Razin Hafid Hamdi
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123340083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@randaandriana_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep . Riau",
                "alamat": "Nangka 3",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Jl.Permadani, Sukarame",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "18",
                "asal":"Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "18",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@notfall.s",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, Bandar lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@keyashafi_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "18",
                "asal":"Lampung Selatan ",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
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
                "nama": "Fairuz Ary Syifa",
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
                "nama": "Tanty Widiyastuti",
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
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123440104",
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
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dv3HPu15RVFqPYWAh_BnfZWSW4V9cLtm", #Bang Arafi Ramadhan Maulana
            "https://drive.google.com/uc?export=view&id=1tt7ZQsEgZbLdD1TN2IrIQKKmeMRbOoiV", #Kak Yohana Manik
            "https://drive.google.com/uc?export=view&id=1Xw3xqX5LZX7UhXI-DNYy08BMjfIsft2z", #Kak Ratu Keisha Jasmine Deanova
            "https://drive.google.com/uc?export=view&id=1R5vtW-Op6yjfyDROlIBNKNmBVt0tDFdX", #Kak Arini Puteri Elandra
            "https://drive.google.com/uc?export=view&id=1MMy90BKupObyILsDyVVrgXR3qM-U_Cvc", #Bang Arya Muda Siregar
            "https://drive.google.com/uc?export=view&id=1_QNbS9XiX8G9tkIFcWsJzxJcCjI8w_H1", #Kak Khoirul Muttoharoh
            "https://drive.google.com/uc?export=view&id=1QWn0sPm00ajxA7TZ5ZJ4SrzENYRkZLH1", #Kak Lutfia Aisyah Putri
            "https://drive.google.com/uc?export=view&id=1rEQ2DfyHqKDaNejg7orapgBl03bBSRct", #Kak Nabyla Sharfina
            "https://drive.google.com/uc?export=view&id=1XF6E0nQC-thfrpLG7daREISya9cxh01L", #Bang Syahrialdi Rachim Akbar
            "https://drive.google.com/uc?export=view&id=1OMa7XT6YAm_O38qaIHl_Ops9O0jiZc5R", #Kak Dea Mutia Risani
            "https://drive.google.com/uc?export=view&id=1HpdYPHSgXicaKhUeWMl_QAWpQYQUb4d-", #Kak Cindy Laura Manik
            "https://drive.google.com/uc?export=view&id=1r4BnVO30MwoHEX24WUbHtx4xr8GLw8JK", #Kak Dea Amanda
            "https://drive.google.com/uc?export=view&id=17WatBmu-7YXpE5h77pbXcOck3SDJrbpe", #Bang Desman Velius Halawa
            "https://drive.google.com/uc?export=view&id=1eNKOO53FdaVEKf1cACl9qMFooYBY64F2", #Kak Devyna Sonya Palupi Sanjaya
            "https://drive.google.com/uc?export=view&id=1p-U9DeiIkq5yqdm_yDaNUxOMoUlbj5kk", #Kak Luthfia Laila Ramadhani
            "https://drive.google.com/uc?export=view&id=1I76oaBAW4dhOMgszMFdvWbge89dFwbyL", #Bang Irvan Alfaritzi
            "https://drive.google.com/uc?export=view&id=1tLJFIBvFDJFKQyxZ_gRJn_C5X1FHvsa7", #Bang Aditya Taufiqurrohman 
            "https://drive.google.com/uc?export=view&id=1653zQLkclgL0xG797Bqs--UKw7VCGE9Y", #Kak Fathya Intami Gusda
            "https://drive.google.com/uc?export=view&id=1aqrXY2UM9A8NDKXV02ndq29izRqyzV9l", #Kak Khazanatil Ilmi
            "https://drive.google.com/uc?export=view&id=1lbK7pfgP6y9tSd5zYNyO-NjTQiJN_BUd", #Kak Melinza Nabila
            "https://drive.google.com/uc?export=view&id=1v95jHmHII1TDhc3fbFWPYmmFYPZIV4L5", #Kak Nayla Shafira Roza
            "https://drive.google.com/uc?export=view&id=10FcgJ1Cu8HAaPPSp2el-bii5rbC7fUZW", #Kak Nurul Izzah Istiqomah
            "https://drive.google.com/uc?export=view&id=13hCKcbRoKhzZrqdltFD2pxheH3ZZy0YM", #Bang Qois Olifio
            "https://drive.google.com/uc?export=view&id=1cI7kxa59RQvt4lXIIKYth82H0izlNn1P", #Kak Tarisya hidayatul rahmi
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl.Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()
# Tambahkan menu lainnya sesuai kebutuhan

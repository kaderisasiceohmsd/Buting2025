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
            "https://drive.google.com/uc?export=view&id=1RADX3YweO96EwsFP7jIv0Wf2f5KAdLOr",
            "https://drive.google.com/uc?export=view&id=1Oe0C-Jq_qoxBmrRqL-M1bE1EQARhzprK",
            "https://drive.google.com/uc?export=view&id=1uxUvigYV_WuwUuFtPRbCTnnDGEHB7DUP",
            "https://drive.google.com/uc?export=view&id=1PcTWTSx5siMTie24EsiR6IVL9-FGxfiB",
            "https://drive.google.com/uc?export=view&id=183mDRcmxpQSpheICWkTLVaFw3UdNJ2fI",
            "https://drive.google.com/uc?export=view&id=1FoLncpQTwPBB-OHWyVZPwPQq6pXZMIaT",
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
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simajuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy Dalem",
                "alamat": "Ayres Kost",
                "hobbi": "Makan Kuaci",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Komenin tiktok cewek cantik",
                "sosmed": "@eksantyferiana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Gya Kost Korpri",
                "hobbi": "Cute jendral",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XY0JXxb7PbaoaZXN7Ch2QEhJLbg7LTKi",
            "https://drive.google.com/uc?export=view&id=10vJ-xcfpYqzkO6QfhqiiuQABjIsefnHX",
            "https://drive.google.com/uc?export=view&id=1JCgH2DwIxw4ZpOdqjW22iVZTP3tkYNue",
            "https://drive.google.com/uc?export=view&id=1-ewAulpAzu9TjW-WBTeyMKqKrLx44JDE",
            "https://drive.google.com/uc?export=view&id=1ClFGOgZmcbZ3CNsl8K7ba0cr4fHyjsUY",
            "https://drive.google.com/uc?export=view&id=1FldD4hmdTswesH18yHeXySv5TMuZofAp",
            "https://drive.google.com/uc?export=view&id=1kcSA1QYRdrLqfpA8nOpgbIcuOz6JVOT7",
            "https://drive.google.com/uc?export=view&id=1h0-vFdnV8oJkTBx03z5NnLmLAGvfjwUL",
            "https://drive.google.com/uc?export=view&id=198IUaceF7dPYADZ4VhG4qmZ1ozLMFRpa",
            "https://drive.google.com/uc?export=view&id=1DZDhcNvR_P6BOYXZdtmsn8hWiMwUpcDg",
            "https://drive.google.com/uc?export=view&id=1T9rQG2PH6c0_n1rUx53XBktv3wjUYo4j",
            "https://drive.google.com/uc?export=view&id=1sDn17IFhX-Y4TtYNIgPNq7Ly0KRI4C64",
            "https://drive.google.com/uc?export=view&id=1Jwel7TA3BtYsgSY4DUT4L7F1MZNx5eVw",
            "https://drive.google.com/uc?export=view&id=1Y7imSoy9vm3dnifF3QgaqwOakOIQDEur",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "Nonton Orang Kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "Lomba ngga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Tidur",
                "sosmed": "@rnshism",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Annisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Ubud",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari Kesibukan Baru",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak Sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Berliana Enda Putra",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main paddle",
                "sosmed": "@iamridhomanik",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi batch google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Kota Tarakan",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
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
            "https://drive.google.com/uc?export=view&id=1-G-pIpfc-mf9LxWD5RhJYvb-h6sduc_V",
            "https://drive.google.com/uc?export=view&id=1kFLWcezvISPm-BFIwtzHjIHHgqijFfRr",
            "https://drive.google.com/uc?export=view&id=1MHQ2a1qNVC_zn_M8smbiCXP95uTavI6z",
            "https://drive.google.com/uc?export=view&id=1ZNJDZsT1SD85PmGw7cVLlj_AZStk6eHI",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Dengerin lagu, nyanyi, game, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "122450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450069",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        Senator()
if menu == "PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ScJxo2dovYdzHAak2B3BrM3I8LgubnUh",
            "https://drive.google.com/uc?export=view&id=1SXK3ylfvS22_oIaUxBU4DK6P9c3FBU7L",
            "https://drive.google.com/uc?export=view&id=1tUyE8TA1o7TiYDkYH87atKxFDViNpAXu",
            "https://drive.google.com/uc?export=view&id=1xDzj12p7pAM6nH7j-Zhs049G8hY0AO2r",
            "https://drive.google.com/uc?export=view&id=1BPBINrz4NV9ArdGSuSP4N-Z5KY9HfyOC",
            "https://drive.google.com/uc?export=view&id=1K7iT8DNsUeD0pdhcCVWIvTdBITLUii0w",
            "https://drive.google.com/uc?export=view&id=1_fNlE7ac4u4xQLR5do7lBRFBOYGcSpOaC",
        ]
        data_list = [
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450069",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
# Tambahkan menu lainnya sesuai kebutuhan



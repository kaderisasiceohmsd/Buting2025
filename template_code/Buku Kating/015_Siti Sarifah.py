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
            "https://drive.google.com/uc?export=view&id=1bYBvP8_ppe1EdY_ZJ0vXwiX5CzOg_hnE",
            "https://drive.google.com/uc?export=view&id=1vFDjQPj30mIgX4xkq3LhKj0RMxqhkAJX",
            "https://drive.google.com/uc?export=view&id=1A2HImQyj7QN_a7mNj-Fq_aH0gURAc6P6",
            "https://drive.google.com/uc?export=view&id=17j9XU05m1JSBbgCx5a-0pX2uYGTOwXvM",
            "https://drive.google.com/uc?export=view&id=1WPohsKSvf1d2Vsl_69qhnK5eYKHpT6eB",
            "https://drive.google.com/uc?export=view&id=1wlT_cb-3Pbz39oUDtrWrvAZCXnYi2eXU",

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
                "kesan": "Abang keren, tegas, tapi tetap asik",  
                "pesan":"semangat terus bang, sukses selalu!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan. Lapas Raya",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya keren,tangguh, dan selalu sigap",
                "pesan":"semangat terus bang, sukses selalu!"# 2
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak selalu teliti dan tanggung jawab banget.",
                "pesan":"Semangat terus ya Kak, semoga rezekinya juga selalu lancar"# 3
            },
            {

                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cute Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak selalu teliti dan tanggung jawab banget.",
                "pesan":"Semangat terus ya Kak, semoga rezekinya juga selalu lancar"# 4
            },
            {

                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya rapi, sigap, dan detail banget dalam setiap urusan.",
                "pesan":"Tetap semangat ya Kak, semoga makin sukses dan terus jadi inspirasi!"# 5
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal": "Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya rapi, sigap, dan detail banget dalam setiap urusan.",
                "pesan":"Tetap semangat ya Kak, semoga makin sukses dan terus jadi inspirasi!"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wY4zPdROirlJ5UUDqOIijDxFCSz4rNUe",
            "https://drive.google.com/uc?export=view&id=1ia0bUWBX2AR42DCAr4QSSPJwD7vsIIYz",
            "https://drive.google.com/uc?export=view&id=1SVjIE8jivknR-Ap0tzaQDjnfJ1RG_zSy",
            "https://drive.google.com/uc?export=view&id=1hmkMfji2o94gV50tgNHn_zcOpsQKKwYe",
            "https://drive.google.com/uc?export=view&id=1YCR1vuCCdk8QUAnSeIwiLdiX622gDuaZ",
            "https://drive.google.com/uc?export=view&id=1mv6n2N3JwWq3y05KWGidC69vc7ORjpeZ",
            "https://drive.google.com/uc?export=view&id=1zaCBkuo_cJQV3ZztIBmWsYpPkTAyxNQY",
            "https://drive.google.com/uc?export=view&id=1dku20D7FuFMkH4WLuSn3DZyr9ICEmvmV",
            "https://drive.google.com/uc?export=view&id=1A17IONAj8h5IXX_aSTQ0CRI_YKPtZ0DC",
            "https://drive.google.com/uc?export=view&id=1B9s3-wFzeK1FOaoQKRdsujjBBxPuPKh8",
            "https://drive.google.com/uc?export=view&id=1hmkMfji2o94gV50tgNHn_zcOpsQKKwYe",
            "https://drive.google.com/uc?export=view&id=1ymKd2r3O0Av_DqVa_5kONnCmq3l3U0fZ",
            "https://drive.google.com/uc?export=view&id=1uQLvwzJvkr9gvZQbeItr6WAQQLkLMeU_",
            "https://drive.google.com/uc?export=view&id=14amtjb_AP3vGOwL7JI2ZWO86QMygu86S",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Yapping",
                "sosmed": "@Jeremia_s_",
                "kesan": "Awalnya keliatan tegas banget, tapi pas ngobrol ternyata asik parah",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Awalnya keliatan galak, tapi ternyata asik banget",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya ramah, orangnya humble.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Abangnya seru dan baik banget.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Ramah, asik, dan ngasih motivasi banget",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Abangnya ramah banget dan cara ngomongnya santai tapi berisi banget",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya asik, orangnya humble.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Sukses terus buat semuanya, kalian keren!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1l_833Al4qQRIr5o054CZJE-3QEZ8bhIk",
            "https://drive.google.com/uc?export=view&id=1NEGvOVpUos8MtleRyYRGHWOp2YfUUFP3",
            "https://drive.google.com/uc?export=view&id=1yIRNf7IyvztQ71H7sCHcuiVcCvBDkR4K",
            "https://drive.google.com/uc?export=view&id=1PTWaNH5trAaPx2GeesJDkfVnxv_XZa7H",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "tanya caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang nya asik, pembawaannya santai jadi ga tegang",  
                "pesan":"semangat terus kuliahnya bang, semoga suka AU 1920 hehe"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakak ini cantik dan ramah bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik dan ramah banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik dan ramah bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

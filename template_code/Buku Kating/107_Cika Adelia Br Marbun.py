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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WW2a-STCeaFaU4oQq2IcI_YSc85lPLN-",# bang rendra
            "https://drive.google.com/uc?export=view&id=19u6S8kDaghWycZy1GGqUbdU_kNJBBRWB",#bang johannes
            "https://drive.google.com/uc?export=view&id=1W82MhCthyHO7O9pKArz0jXm8f9ZewCNo",#kak elisabet 
            "https://drive.google.com/uc?export=view&id=1oNcEzw3fnn_pqPlF4NqvoNgFfaAIXn_R",#kak syadza
            "https://drive.google.com/uc?export=view&id=16REtOZYJxFC75EE_4ghhsXzvPj7Mlo3z",#kak eksanty
            "https://drive.google.com/uc?export=view&id=1UO9JYxZh_tiD4ZZxp2R4jywgHYPAkSor",#kak farhanum
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Seru,tegas tapi asyik",  
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya humble, seru, tegas tapi asyik",  
                "pesan":"Semangat terus kuliahnya Bang"
            },
             {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal": "Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya ceria dan baik",  
                "pesan": "Semoga lancar kuliahnya"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya baik",  
                "pesan": "Semangat terus kak"
            },
             {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal": "Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya seru",  
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Ilmunya sangat bermanfaat",  
                "pesan": "Semangat kuliahnya kak"
            },   
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16jMtkUK845lp6rCyNUiuK34fHRmDFpqT",
            "https://drive.google.com/uc?export=view&id=1j-XPU66zWG_zsnhmazj2R-whFeyDZNOM",
            "https://drive.google.com/uc?export=view&id=1M4PI3RFfJJ395xGM7Ut1M5hQHh-DHADr",
            "https://drive.google.com/uc?export=view&id=10sYHq3JNdIc19PagJe02yJZDYjh5eVgE",
            "https://drive.google.com/uc?export=view&id=1spjBxlOnpTTYU2MAJt__FRV7wpQKfbcB",
            "https://drive.google.com/uc?export=view&id=1D8mUYUE1OCHod9DAopZjjh8wi8wsZCPn",
            "https://drive.google.com/uc?export=view&id=1ZuLmss73pkyB6txt-MAR4uS1hlFHvKu-",
            "https://drive.google.com/uc?export=view&id=1BfANaT_EcgKDoU1wkR8d6bxd2e5wB090",
            "https://drive.google.com/uc?export=view&id=1PsTJJ35hyyFBov5csPUdNLbpX04b72jg",
            "https://drive.google.com/uc?export=view&id=14OjJPwcC6Fl5sWiEDdqOtLWc_UQ5aIES",
            "https://drive.google.com/uc?export=view&id=16ZOwGHosorB6t5UtK9uH17uBxY_lAGek",            
            "https://drive.google.com/uc?export=view&id=1IzLNHbS5VDai8FpBYwTR9lNUJz9X9dSz",
            "https://drive.google.com/uc?export=view&id=1547fe98qf6ZKztHtBXAFt9QpNiJSeGFB",
            "https://drive.google.com/uc?export=view&id=1LtXMs8KD10Gsp2kKg6Bo8V8TX0dUG9T-",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Yapping",
                "sosmed": "@Jeremia_s_",
                "kesan": "Abangnya seru dan ramah.",
                "pesan": "Sukses selalu untuk kuliahnya ya Bang"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakanya baik dan ramah",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Kakaknya ramah",
                "pesan": "Lancar selalu untuk kuliahnya kak"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya baik banget",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Abangnya baik",
                "pesan": "Semangat terus Bang"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal": "Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya seru",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Abangnya seru",
                "pesan": "Semoga lancar kuliahnya bang"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya baik",
                "pesan": "Semangat kuliahnya Bang"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya baik",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya asik dan ramah",
                "pesan": "Sukses selalu untuk kuliahnya ya kak"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya baik",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal": "Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya baik",
                "pesan": "Tetap jadi pribadi yang menginspirasi"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya ramah dan baik",
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya baik",
                "pesan":"Semoga lancar kuliahnya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xjn0rcdj1zsUEK8i8j8UutEaiWBg2m7u",
            "https://drive.google.com/uc?export=view&id=1lDhu2CpJ6QjpvpJF1F-YinhuvolpFb_J",
            "https://drive.google.com/uc?export=view&id=1c9Sq8J0WwOvp_xY0bf1vOFybat2W04mf",
            "https://drive.google.com/uc?export=view&id=1eAc8wCQYbWW-IjPXuW__JT07Q6PbvFGa",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "tanya caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya asik",  
                "pesan": "Semangat terus Bang"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakaknya ramah",  
                "pesan": "Semangat kuliahnya kak"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya Baik banget",  
                "pesan": "Semangat terus kuliahnya kak"
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik",  
                "pesan": "Semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oyELCJeCcyUsfGFhzm9MGR94r4DqyqAG",
            "https://drive.google.com/uc?export=view&id=1cPFTvF7SToju8fCgidwBvdR-36nZekVs",
            "https://drive.google.com/uc?export=view&id=1eIrKD0FDJ9HZbrUFzAAc9x_6CnSiey0M",
            "https://drive.google.com/uc?export=view&id=1R6WCEpO5AjHOENYAONR-qhnd_MxV5Gd4",
            "https://drive.google.com/uc?export=view&id=16mkO-0bOYyfeq7rg3wZ8aiJbJUu6zv4_",
            "https://drive.google.com/uc?export=view&id=1GlGTx6K7U7VtwNEjXjT4ui2xXM-wBttJ",
            "https://drive.google.com/uc?export=view&id=1URQo6vIkBsab-d8CJBjTZBMR0f8F3tJ0",
            "https://drive.google.com/uc?export=view&id=1jpnXRiN9eyHrDqfZWdPvV9V5K1H4VFCQ",
            "https://drive.google.com/uc?export=view&id=13KeuX7TrQziaw2zQ52KAWKSNWtYRIU50",
            "https://drive.google.com/uc?export=view&id=1ONv-3seGFFWfy8kF1zXI_iygydFNhvr6",
            "https://drive.google.com/uc?export=view&id=1OxljdPSm9vG7C7HEhOC39cWnTmUb58qa",
            "https://drive.google.com/uc?export=view&id=132rRGy3muH-jcsnquKUSMEUSKWqgqYMs",
            "https://drive.google.com/uc?export=view&id=1hLhpbDaEpSrt2Q0r9BScRMurJQAVyKYd",
            "https://drive.google.com/uc?export=view&id=1j7hnMRiRUEVZTCgSWM1WuOAmduayXSgk",
            "https://drive.google.com/uc?export=view&id=1xZeFQFARfUmQMBZjdWaStoM7WCNE2A2G",
            "https://drive.google.com/uc?export=view&id=1iQfoSQxL1E-uXHPe9HPxhUVVh1yqN9p6",
            "https://drive.google.com/uc?export=view&id=1v5Iy2D_0YCNQ29G_fiFksu_N-r5kSaiz",
            "https://drive.google.com/uc?export=view&id=1JmEkZ_gBq7Grd0iEx720KYvTO0Jwx709",
            "https://drive.google.com/uc?export=view&id=1ii0pnuo3okK1FtdtlBO0-ulk6I3z8MF3",
            "https://drive.google.com/uc?export=view&id=1Zs8LG-C92grPR883BmvMmdzRrCdZjDta",
            "https://drive.google.com/uc?export=view&id=10BxN19wJuYHfyohmQJxbvnAe2y-CLhR6",
            "https://drive.google.com/uc?export=view&id=1ZVf6JzEJfB34TcWPZDdVROjoi9d2SqnQ",
            "https://drive.google.com/uc?export=view&id=1ArjzQw4lJfzmGaofHQepG1bo3G5Ex9EW",
            "https://drive.google.com/uc?export=view&id=1rJ2u61TbMT6vetce9GSghcjlksEhhEe2",
            "https://drive.google.com/uc?export=view&id=1JXVmApl-PigP0z1k1HNJnja5pGiZqfEx",
            "https://drive.google.com/uc?export=view&id=1KhOm9tuFYfSDnrvUGHzXPEWG0aXDam3g",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Abangnya tegas dan berwibawa ",
                "pesan": "Semangat terus kuliahnya bang"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed":"@afifahhnsrn",
                "kesan": "Kakaknya tegas tapi care",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakaknya tegas tapi baik dan care",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Abangnya sangat memotivasi",
                "pesan": "Tetap semangat bang "
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakaknya tenang tapi tegas",
                "pesan": "Sehat selalu kak"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abangnya mengayomi dan baik",
                "pesan": "Semangat kuliahnya bang"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Abangnya sangat mengayomi dan baik",
                "pesan": "Semoga kuliahnya lancar bang"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakaknya baik dan mengayomi",
                "pesan": "Semangat kuliahnya kak"
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abangnya mengayomi dan baik",
                "pesan": "Semangat kuliahnya bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Abangnya bijaksana dan pembawaanya tenang",
                "pesan": "Semangat selalu bang"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya baik dan bertanggungjawab",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Abangnya seru dan baik",  
                "pesan": "Semangat selalu bang"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya asik dan baik",  
                "pesan": "Semoga kuliahnya lancar bang"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakaknya ramah dan baik",  
                "pesan": "Semoga kuliahnya lancar kak"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya baik",  
                "pesan": "Semangat kuliahnya kak"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakanya baik dan ramah",  
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya baik ",  
                "pesan": "Semangat kuliahnya bang"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Abangnya baik",  
                "pesan": "Semangat kuliahnya bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya ramah dan baik",  
                "pesan": "Semangat selalu kak"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Abangnya asik dan baik",  
                "pesan": "Semangat kuliahnya bang"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Abangnya baik",  
                "pesan": "Semangat kuliahnya bang"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakaknya ramah dan baik",  
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Ngehina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Abangnya baik dan seru",  
                "pesan": "Semoga kuliahnya lancar bang"
            },
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Abangnya tegas dan baik",  
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakaknya baik",  
                "pesan": "Semangat kuliahnya kak"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Abangnya asik dan baik",  
                "pesan": "Semangat terus bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TS8v9Iq1VbVb5Bbqk6Hyb_QCvPer7994",
            "https://drive.google.com/uc?export=view&id=1s_Acy5AQtoaqm4bcwivQhmZpD0P329l0",
            "https://drive.google.com/uc?export=view&id=1zzRYl-OT1qRoYWu5iTs2QxJ8RzZaNYP5",
            "https://drive.google.com/uc?export=view&id=1s34vts6Mf1D5BF9dcgIOlgMf_xfnFdZo",
            "https://drive.google.com/uc?export=view&id=1m8TnWkmnkDjJ7jToETZSDeQLxNj17jnx",
            "https://drive.google.com/uc?export=view&id=1t_Ru9J5eUapENE74x--f0G3tpQ1K4fpE",
            "https://drive.google.com/uc?export=view&id=1sf2GFEiA21ivpiJ2pn_CXIj9TXk4_chF",
            "https://drive.google.com/uc?export=view&id=1x2z_zxpIaIZ2KJiAZ1eRo6rBBznJlfOa",
            "https://drive.google.com/uc?export=view&id=1vxTt3dhfgRFwaA0zoC4Fax96dae5emIX",
            "https://drive.google.com/uc?export=view&id=1qJeOeqQk5IQz74BNlToSCG_7mh2s5GUb",
            "https://drive.google.com/uc?export=view&id=1ReAX8JKFz0h6WnjZLorr6N3pyUuXfsEg",
            "https://drive.google.com/uc?export=view&id=1zZAFuvW7IxVeMNqHWRrYM1tt76n-_26z",
            "https://drive.google.com/uc?export=view&id=1cBGoV_GuFR2Mrt_MH_oSTVHrCSuOEies",
            "https://drive.google.com/uc?export=view&id=1kSDTE1Ko7IXd9Dpao58g67RSkBmi2l-v",
            "https://drive.google.com/uc?export=view&id=1RxlGuUREJVpgaQNoZp1YkQscgitIPBJ7",
            "https://drive.google.com/uc?export=view&id=1Nqe5CKTLikd2QO4e_AckODCUWTVFSZCI",
            "https://drive.google.com/uc?export=view&id=1voWGyB25SycWiJCXgnd-SGsFbtr_-Qnm",
            "https://drive.google.com/uc?export=view&id=1xcw3sQ8iiyS5rSiTpEoAw9l435XyYfMW",
            "https://drive.google.com/uc?export=view&id=1E0bgkIYEMDizFsnus70NH6fTzpJ0vrIi",
            "https://drive.google.com/uc?export=view&id=1Xwqi7xOp6RBJjIhRFI6Agrid2WgxifVn",
            "https://drive.google.com/uc?export=view&id=1TBDQSKhiRl56xEHHtTa8g7EdAYjnOvq1",
            "https://drive.google.com/uc?export=view&id=1ItkXRCyt6myQvNmJ7lwvuVCiTyKtwee9",
        ]
        data_list = [
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Abangnya asik dan seru ",
                "pesan":"Semangat terus untuk kuliahnya ya,Bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "kakak orangnya ramah.",
                "pesan":"Sukses selalu kak"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya sangat baik dan sabar",
                "pesan":"Semoga kuliahnya lancar Bang"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya baik",
                "pesan":"Semangat terus untuk kuliahnya Kak"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya jago public speaking",
                "pesan":"Semoga kuliahnya lancar Bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Orangnya seru dan asik",
                "pesan":"Semangat terus Bang"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya baik ",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya baik dan ramah",
                "pesan":"Semangat terus untuk kuliahnya Kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak sangat baik banget dan ramah",
                "pesan":"Semoga apa yang diinginkan tercapai Kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Orangnya menyenangkan",
                "pesan":"Semoga kuliahnya lancar Bang"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya baik dan pembawaannya positif",
                "pesan":"Semangat terus Kak"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik dan senang belajar dari kakak",
                "pesan":"Sukses selalu untuk kakak"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "",
                "asal":"",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus Kak"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakaknya mirip orang arab",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "kakak orangnya ceria dan ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abangnya baik dan senang bisa belajar dari abang",  
                "pesan":"semangat terus kuliahnya Bang"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak baik dan ramah",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Abangnya baik, seru, dan ramah",
                "pesan":"Sukses selalu Bang"
            },    
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus Bang"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Orangnya menyenangkan dan ramah",
                "pesan":"Jangan lupa jaga kesehatan ya Kak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abang baik dan asik",
                "pesan":"Semangat kuliahnya Bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Nx5wEIpFmgLD_sfRYqAfwTKiChCHBxzI",
            "https://drive.google.com/uc?export=view&id=13Q7LtbdA7guZjYVjDSVJNVXDMihkOtZF",
            "https://drive.google.com/uc?export=view&id=1HDCf4xsc732E6glzGIuqIU_34jtyAmi9",
            "https://drive.google.com/uc?export=view&id=1RWIEzl6T8Zvjr1AqS2OjO8VCqF6J9A8A",
            "https://drive.google.com/uc?export=view&id=1T3B_22OVXfxAZMqCZYR63nLVz0vjOHtZ",
            "https://drive.google.com/uc?export=view&id=11_ulzxHLlPxaZQMj_ks26cNtoAKEWj4G",
            "https://drive.google.com/uc?export=view&id=1xOPdZdBm7ZGerBpdBkxVNOEAl22tznvI",
            "https://drive.google.com/uc?export=view&id=1WXS1koejI_7CT_5MqI-yPBDU_p1d_Yqw",
            "https://drive.google.com/uc?export=view&id=1i_TbRYr-RpN8NiNdxpsQEGJItXEQaQUy",
            "https://drive.google.com/uc?export=view&id=1-eWcKMnXCDcw3c4tMF_jtH5ICgEDUoCE",
            "https://drive.google.com/uc?export=view&id=15O-B7NYc3BLW8xvd1zOhDGPjxuWYNTFM",
            "https://drive.google.com/uc?export=view&id=1Yhsd1MGECzlBiWQDljuy8KGvAg4fy_Ko",
            "https://drive.google.com/uc?export=view&id=1j6ao-vYwEANU8DLkj0Stg91VnKvrLdu9",
            "https://drive.google.com/uc?export=view&id=18cKcA6FUmRYIwnEVZZzO7SgotSi18VUQ",
            "https://drive.google.com/uc?export=view&id=1lcenz5JExNUDXFN0QBxq1tTjIOXYbCiH",
            "https://drive.google.com/uc?export=view&id=1JcEsmvPPRSX-8ikjK7P14hh-oMhifp7o",
            "https://drive.google.com/uc?export=view&id=1fOC1UMgnP9lrm_XCqixcGHu9mUVQVRna",
            "https://drive.google.com/uc?export=view&id=1Nsx4M6gQg06pVSonUWWL26lvv_5PyBji",
            "https://drive.google.com/uc?export=view&id=17BNXHB-8Py_D9DiCym6XkI4X-XttoOXC",
            "https://drive.google.com/uc?export=view&id=1Fpme887kzYed2v6tzGLvDVZkqOoY_SbZ",
            "https://drive.google.com/uc?export=view&id=1Vn1Tnqwp4tdEsN-40Ryr9XnhTY7rlYp7",
            "https://drive.google.com/uc?export=view&id=1fzL0pZJqh01b-pQBGBJW1u9P1U_2-yEb",
            "https://drive.google.com/uc?export=view&id=1Z8I716Tby8hcmaIYgQlGNsIkPdUh_2TW",
            "https://drive.google.com/uc?export=view&id=1lebGNf0uTXDvQWBeIdHA4fwp5N3oFrAA",
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "Abangnya asik dan seru",
                "pesan":"Semangat terus untuk kuliahnya ya Bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya baik dan orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya asik dan banyak belajar dari kakaknya",
                "pesan":"Semangat terus untuk kuliahnya Kak"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya baik dan pembawaannya positif",
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya seru dan baik",
                "pesan":"Sukses selalu untuk ke depannya Bang"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakanya baik banget dan pembawaannya positif.",
                "pesan":"Semangat terus Kak"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakanya baik dan orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya Kak."
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abangnya seru dan asik",
                "pesan":"Semangat terus untuk kuliahnya Bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan ramah",
                "pesan":"Semoga apa yang dicita-citakan tercapai Kak."
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya ramah dan baik",
                "pesan":"Semangat terus untuk kuliahnya Kak"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Orangnya menyenangkan dan ramah",
                "pesan":"Semoga kuliahnya lancar Kak"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya sangat baik dan sabar dalam membimbing.",
                "pesan":"Semangat terus Bang"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing",
                "pesan":"Jangan lupa jaga kesehatan Kak"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakaknya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai Kak."
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangny baik",
                "pesan":"Sukses selalu untuk Abang ke depannya!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya baik dan asik",
                "pesan":"Semoga kuliahnya lancar Bang"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kakaknya baik dan ramah",
                "pesan":"Semoga apa yang diinginkan tercapai Kak"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakakny baik banget",
                "pesan":"Semoga apa yang dicita-citakan tercapai Kak."
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya ramah dan ceria",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya Kak"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya baik,asik dan seru",
                "pesan":"Semangat terus untuk kuliahnya Kak"
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya baik dan ceria",
                "pesan":"Semoga kuliahnya lancar Kak"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangny baik",
                "pesan":"Semangat kuliahnya Bang"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "OKakaknya baik banger, ramah dan sabar dalam membimbing",
                "pesan":"Semoga apa yang dicita-citakan tercapai Kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LPuKdrzXDr2AcdbUMB16XojQZLRpA6ow",
            "https://drive.google.com/uc?export=view&id=1SIaBAS7MSQhQMcrONB8plC9j2z1Mi6xH",
            "https://drive.google.com/uc?export=view&id=11Q9cFRIrHOpecVKA-h-iQNNHOi0k_5kR",
            "https://drive.google.com/uc?export=view&id=12dTMb7_heyCF3sINQYmGSGVKI9UJ96uu",
            "https://drive.google.com/uc?export=view&id=1QwRdM6dRJkPs4CJsdol63Siusj_AxyFO",
            "https://drive.google.com/uc?export=view&id=14sDIubffW19otk3NfDZw0tuOyBiz33bN",
            "https://drive.google.com/uc?export=view&id=1wkGRj_IPcyNA8Q0_FPSHJXdHg8hJ7zk8",
            "https://drive.google.com/uc?export=view&id=1lXEyqhGlEA1s5c-rP1r1bAn6noy7f89p",
            "https://drive.google.com/uc?export=view&id=16ZZ4jj32x5hmjTa249X4IvLTKfzbMqxi",
            "https://drive.google.com/uc?export=view&id=1KXBB9A29kt4BPRjGqhhDY5YHPpkZlwGM",
            "https://drive.google.com/uc?export=view&id=1lWHHP0FGRED5M0qDomEotqgCltZ6YP3j",
            "https://drive.google.com/uc?export=view&id=17XCTfXerHn8H-awmMbu3w8sDBKA1ZTbZ",
            "https://drive.google.com/uc?export=view&id=1bLjSIPN3toLZ8dcq8IRB0JMy3GbFn-X8",
            "https://drive.google.com/uc?export=view&id=13st06a5zRFB4Rg-SBp2Ea4XGLmKdzPsw",
            "https://drive.google.com/uc?export=view&id=1yjUtM6qFL0P6jVxQkePF1PdlvV3US4m8",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya asik dan sangat peduli",
                "pesan":"Semangat terus Kak"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya baik ,ramah dan asik",
                "pesan":"Semangat terus ya Kak."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya baik dan sangat mengayomi",
                "pesan":"Semangat selalu Kak"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya baik dan ramah",
                "pesan":"Semoga kuliahnya lancar kak"
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya sangat mengayomi",
                "pesan":"Semangat selalu Bang"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya baik dan ramah",
                "pesan":"Terus semangat Kak"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak sangat peduli dan mengayomi",
                "pesan":"Semangat terus Kak"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Abang baik ",
                "pesan":"Semangat terus Bang"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangng seru, asik dan baik",
                "pesan":"Semangat Kuliahnya Bang"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya baik,sabar dan ramah",
                "pesan":"Semoga lancar kuliahnya Bang"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya ceria,ramah dan baik",
                "pesan":"Semoga kukiahnya lancar kak"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya baik dan ramah",
                "pesan":"Semangat terus Kak"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya sangat peduli dan mengayomi",
                "pesan":"Semangat terus Bang"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakanya baik dan ramah",
                "pesan":"Semangat selalu Kak"
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@zhrptsl",
                "kesan": "Kakanya baik dan ramah",
                "pesan":"Semangat selalu Kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1v0inmSs_IauHOPSnnCHHXTzZrfKiq9VM",
            "https://drive.google.com/uc?export=view&id=1uLbSbBEAJYDoDTnrOlsgPiYuB6vgkJWr",
            "https://drive.google.com/uc?export=view&id=1vq8hDTqx5H-OxTKQq_MqoV3hCULhnDMs",
            "https://drive.google.com/uc?export=view&id=1YFIXrhZuHdVE12MO65RuBcuNPAXmOyJg",
            "https://drive.google.com/uc?export=view&id=1Sk773G2RBwa3YwtEmBocRUIqN-SaIa24",
            "https://drive.google.com/uc?export=view&id=1x_oUVED2ue2EFg27YvOlFyQDx-loDobs",
            "https://drive.google.com/uc?export=view&id=10JVTd_wrjTSplQduO1N9Wa4NXlFstoQJ",
            "https://drive.google.com/uc?export=view&id=HGEbEftTMGHGIHKB-KmGZ8a6aDqmIO67",
            "https://drive.google.com/uc?export=view&id=10aSxUGtn4h4pjYjOAUEyXqwfSUBaTm6d",
            "https://drive.google.com/uc?export=view&id=1LYJk870S_m1T8SgBy9TjOK7jJIzkCmHK",
            "https://drive.google.com/uc?export=view&id=16MZGHSoPGEWbzNNKR7i5AS2mshqlBw6B",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "dananghk_",
                "kesan": "Abangnya asik dan seru dan inspiratif",
                "pesan": "Semangat terus Bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "kakaknya baik dan ramah",
                "pesan": "Semoga sukses selalu kuliahnya Kak"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Abangnya baik",
                "pesan": "Sehat selalu Bang"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya Baik dan seru",
                "pesan": "Semangat terus kuliahnya kak"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Senang bisa kenal Kak",
                "pesan": "Semoga semua urusannya dilancarkan"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya sangat baik",
                "pesan": "Sukses selalu untuk kakak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Abang baik",
                "pesan": "Semoga kuliahnya lancat Bang"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum",
                "pesan": "Semangat terus ya kak"
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu Kak"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya sangat ramah.",
                "pesan": "Selalu jaga kesehatan Kak"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Kakaknya baik dan murah senyum",
                "pesan": "Semangat dan sukses selalu Kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17sYbm4FNWvRCaiKvDv1riNSfNzmheIA7",
            "https://drive.google.com/uc?export=view&id=1QkLEAmhLHVkhrB9PfwPi0zkOtw5OuTIn",
            "https://drive.google.com/uc?export=view&id=1x-GQNpJLGCbX6gGnw6Hc3_7Kh_K0npbx",
            "https://drive.google.com/uc?export=view&id=1qxgrzZn1yetw_s7pj7lA9bxaFClJunRQ",
            "https://drive.google.com/uc?export=view&id=1S4_wldOsCImlfFP5jOxM4tAOgoCK1FMG",
            "https://drive.google.com/uc?export=view&id=10ZPi4vow_alLAhLRULhWi1RBJBeUxdoA",
            "https://drive.google.com/uc?export=view&id=163ay6IXwUgPKLTlFbaprJhBZcMAFlbjR",
            "https://drive.google.com/uc?export=view&id=1ue1DR-Y-Zxk-MqIA0KwIPqe4d48onaES",
            "https://drive.google.com/uc?export=view&id=1F7Tnc9XfV8lZdci5QJwlQStaitT3IVNo",
            "https://drive.google.com/uc?export=view&id=1Fh1xlf-vdRhQaXnL1JiWdcOK3NDmSEb8",
            "https://drive.google.com/uc?export=view&id=14bNrQA4cydmOWmIraXzuCsqGSfP1Cvab",
            "https://drive.google.com/uc?export=view&id=1OIrj2ZXn4Sk72aIlBbot_bOOSYTPFTtk",
            "https://drive.google.com/uc?export=view&id=1K-21VYZMrkvFcFwv9bXd1LltmiemZKib",
            "https://drive.google.com/uc?export=view&id=1xrbvlqaAUiYKSAX22meUHElGrq2IEvQ6",
            "https://drive.google.com/uc?export=view&id=1MK-nMAd8XEz8Q5DJ-zJIFCnsBCBEbAtp",
            "https://drive.google.com/uc?export=view&id=1lzsP0E1qHuD91NZE1IT-kfNQedkHYIof",
            "https://drive.google.com/uc?export=view&id=1AtxvnJOj7EuOqawVXqoxnSIfU8piA2Mr",
            "https://drive.google.com/uc?export=view&id=1aGi4PsHuCk0Emvfi7NQXFkkXorjKuZ1u",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak ini asik dan selalu ceria",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Kakak ini asik ",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Abangnya baik dan ramah",  
                "pesan":"semangat terus Bang"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abangnya baik dan sabar mengajari",  
                "pesan":"semoga kuliahnya lancar Bang"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya asik dan baik",  
                "pesan":"semangat terus kuliahnya Banng"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak ini baik",  
                "pesan":"semangat terus Kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kakak ini asik, baik dan ramah",  
                "pesan":"semoga kuliahnya lancar kak"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini asik, ramah dan baik",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak ini asik,ramah dan baik",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat terus kuliahnya kak!"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Abangnya ramah dan baik",  
                "pesan":"semangat terus kuliahnya Bang"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakak ini baik",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakak  baik dan ramah banget",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini asik, ramah dan ceria",  
                "pesan":"semangat terus kuliahnya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

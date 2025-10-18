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
            "https://drive.google.com/uc?export=view&id=1WW2a-STCeaFaU4oQq2IcI_YSc85lPLN-",
            "https://drive.google.com/uc?export=view&id=19u6S8kDaghWycZy1GGqUbdU_kNJBBRWB",
            "https://drive.google.com/uc?export=view&id=1UO9JYxZh_tiD4ZZxp2R4jywgHYPAkSor",
            "https://drive.google.com/uc?export=view&id=1oNcEzw3fnn_pqPlF4NqvoNgFfaAIXn_R",
            "https://drive.google.com/uc?export=view&id=16REtOZYJxFC75EE_4ghhsXzvPj7Mlo3z",
            "https://drive.google.com/uc?export=view&id=1W82MhCthyHO7O9pKArz0jXm8f9ZewCNo",
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
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16jMtkUK845lp6rCyNUiuK34fHRmDFpqT",
            "https://drive.google.com/uc?export=view&id=1j-XPU66zWG_zsnhmazj2R-whFeyDZNOM",
            "https://drive.google.com/uc?export=view&id=10sYHq3JNdIc19PagJe02yJZDYjh5eVgE",
            "https://drive.google.com/uc?export=view&id=1BfANaT_EcgKDoU1wkR8d6bxd2e5wB090",
            "https://drive.google.com/uc?export=view&id=1IzLNHbS5VDai8FpBYwTR9lNUJz9X9dSz",
            "https://drive.google.com/uc?export=view&id=1M4PI3RFfJJ395xGM7Ut1M5hQHh-DHADr",
            "https://drive.google.com/uc?export=view&id=1spjBxlOnpTTYU2MAJt__FRV7wpQKfbcB",
            "https://drive.google.com/uc?export=view&id=1D8mUYUE1OCHod9DAopZjjh8wi8wsZCPn",
            "https://drive.google.com/uc?export=view&id=1ZuLmss73pkyB6txt-MAR4uS1hlFHvKu-",
            "https://drive.google.com/uc?export=view&id=1PsTJJ35hyyFBov5csPUdNLbpX04b72jg",
            "https://drive.google.com/uc?export=view&id=14OjJPwcC6Fl5sWiEDdqOtLWc_UQ5aIES",
            "https://drive.google.com/uc?export=view&id=16ZOwGHosorB6t5UtK9uH17uBxY_lAGek",
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
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
            "https://drive.google.com/uc?export=view&id=1JXVmApl-PigP0z1k1HNJnja5pGiZqfEx", 
            "https://drive.google.com/uc?export=view&id=1Zs8LG-C92grPR883BmvMmdzRrCdZjDta",
            "https://drive.google.com/uc?export=view&id=1JmEkZ_gBq7Grd0iEx720KYvTO0Jwx709",
            "https://drive.google.com/uc?export=view&id=1KhOm9tuFYfSDnrvUGHzXPEWG0aXDam3g",
            "https://drive.google.com/uc?export=view&id=1rJ2u61TbMT6vetce9GSghcjlksEhhEe2",
            "https://drive.google.com/uc?export=view&id=132rRGy3muH-jcsnquKUSMEUSKWqgqYMs",
            "https://drive.google.com/uc?export=view&id=1hLhpbDaEpSrt2Q0r9BScRMurJQAVyKYd",
            "https://drive.google.com/uc?export=view&id=1iQfoSQxL1E-uXHPe9HPxhUVVh1yqN9p6",
            "https://drive.google.com/uc?export=view&id=1xZeFQFARfUmQMBZjdWaStoM7WCNE2A2G",
            "https://drive.google.com/uc?export=view&id=1j7hnMRiRUEVZTCgSWM1WuOAmduayXSgk",
            "https://drive.google.com/uc?export=view&id=1v5Iy2D_0YCNQ29G_fiFksu_N-r5kSaiz", 
            "https://drive.google.com/uc?export=view&id=1eIrKD0FDJ9HZbrUFzAAc9x_6CnSiey0M",
            "https://drive.google.com/uc?export=view&id=1R6WCEpO5AjHOENYAONR-qhnd_MxV5Gd4",
            "https://drive.google.com/uc?export=view&id=16mkO-0bOYyfeq7rg3wZ8aiJbJUu6zv4_",
            "https://drive.google.com/uc?export=view&id=1GlGTx6K7U7VtwNEjXjT4ui2xXM-wBttJ",
            "https://drive.google.com/uc?export=view&id=1URQo6vIkBsab-d8CJBjTZBMR0f8F3tJ0",
            "https://drive.google.com/uc?export=view&id=1jpnXRiN9eyHrDqfZWdPvV9V5K1H4VFCQ",
            "https://drive.google.com/uc?export=view&id=13KeuX7TrQziaw2zQ52KAWKSNWtYRIU50",
            "https://drive.google.com/uc?export=view&id=1ONv-3seGFFWfy8kF1zXI_iygydFNhvr6",
            "https://drive.google.com/uc?export=view&id=1OxljdPSm9vG7C7HEhOC39cWnTmUb58qa",
            "https://drive.google.com/uc?export=view&id=1ii0pnuo3okK1FtdtlBO0-ulk6I3z8MF3",
            "https://drive.google.com/uc?export=view&id=10BxN19wJuYHfyohmQJxbvnAe2y-CLhR6",
            "https://drive.google.com/uc?export=view&id=1ZVf6JzEJfB34TcWPZDdVROjoi9d2SqnQ",
            "https://drive.google.com/uc?export=view&id=1ArjzQw4lJfzmGaofHQepG1bo3G5Ex9EW",
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
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()


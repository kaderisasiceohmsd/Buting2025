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
            "https://drive.google.com/uc?export=view&id=1FOM-xbUxXKPIaygwE1kgjZoZJfJysbxS",
            "https://drive.google.com/uc?export=view&id=1afy9XWyAGo4Bik7f-EZRKejslDgydfuz",
            "https://drive.google.com/uc?export=view&id=1_A2O_u3psy9hsl1LI4Kol8mi3TiwiAQ9",
            "https://drive.google.com/uc?export=view&id=1Fku6ZXobCbNATc08AOFHpaVpqV08q2UF",
            "https://drive.google.com/uc?export=view&id=1d60WH4icPlArF2DH-bxbjLU2d8ALrtJ7",
            "https://drive.google.com/uc?export=view&id=1TlJzS50Xfh9GiJq22x1wVs6kptWsIf4K",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "keren dan hebat",  
                "pesan":"Semangat terus bang menjalani semester sekarang "# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "bang Jo keren banget",  
                "pesan":"semoga dipermudah kuliahnya bang"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya humble banget",  
                "pesan":"Semoga sukses terus di setiap langkah, Kak"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "vibes kak syadza positif",  
                "pesan":"Tetap rendah hati meski makin hebat ya, Kak"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Gayanya chill tapi tetap berwibawa.",  
                "pesan":"Jangan lupa istirahat di tengah kesibukan kak"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Keren, tapi nggak sombong sama sekali",  
                "pesan":"Terus jadi inspirasi buat kami, Kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jEDJaa1uggUYvBj4wAx-MTzS4LS9y6P6",
            "https://drive.google.com/uc?export=view&id=1aXETUUlTiOM6FYGeq3FTFlpmWHwbqUK6",
            "https://drive.google.com/uc?export=view&id=1Dkk79dmIRatflepDhduSqT3X3d2sMOiW",
            "https://drive.google.com/uc?export=view&id=1ahTlaU6W2rcLHdzQu03NHlHIQ_1qKrpW",
            "https://drive.google.com/uc?export=view&id=1CdNMFsBOHbyhur98DkKSsp-oyACW5bP1",
            "https://drive.google.com/uc?export=view&id=1spNAnhZaUXPQbk9NzveegWxyqmxxpZ4N",
            "https://drive.google.com/uc?export=view&id=1tHS-ThgSahiNk2JtyegPR_WIJVYtndMc",
            "https://drive.google.com/uc?export=view&id=1GUYOSxuCex2Dy2rDOBhm2D1PPx_v2E4F",
            "https://drive.google.com/uc?export=view&id=1kNIMdiz7nqss4CMm7AEA7fdyIeiCuCo_",
            "https://drive.google.com/uc?export=view&id=1fLqXFjjVart-WYEBNW4IF3y_oDThU4SW",
            "https://drive.google.com/uc?export=view&id=1NHF_1Zp_iuaBJPMNIuFzlX8-420LQ6hw",
            "https://drive.google.com/uc?export=view&id=181mTMTVb4uxruA_PiTwznqTx4eus7d1U",
            "https://drive.google.com/uc?export=view&id=1GhpN6nTfXitRJPhOHJPyFi0kABbNl3vG",
            "https://drive.google.com/uc?export=view&id=1171UaG0a0wcMQ3lL6scLi0AWN8OdSVuF",
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
                "kesan": "Ramah dan selalu senyum.",
                "pesan":"Semoga segala urusan kuliahnya lancar."
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea menyenangkan.",
                "pesan":"Senang bisa kenal dengan kakak."
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
                "pesan":"Sukses selalu untuk kuliahnya ya kak."
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Santai tapi seru.",
                "pesan":"Tetap semangat walau tugas numpuk ya kak."
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Selalu semangat meski sibuk.",
                "pesan":"Semoga semua target abang tercapai."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "imut banget.",
                "pesan":"Terus semangat berbagi ilmu ke kami kak."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Wibawanya kuat, tapi tetap friendly.",
                "pesan":"Jangan lupa bahagia juga ya Bang."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Inspiratif banget cara berpikirnya.",
                "pesan":"lancar luncur kuliahnya bang."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Seru dan menyenangkan.",
                "pesan":"Sukses selalu kakak."
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Seru dan ramah.",
                "pesan":"Tetap fokus dan yakin sama jalanmu kak."
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "ramah dan menyenangkan.",
                "pesan":"Jaga kesehatan, semangat terus bang."
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": " asik dan nggak kaku.",
                "pesan":"lancar luncur kuliahnyaa."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya asik dan baik.",
                "pesan":"Jangan berubah, tetap jadi kakak yang keren."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "ramah lembut daan baik.",
                "pesan":"Terus semangat berbagi ilmu ke kami kak."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1I4rLQc1ScLjAngvvJRoQLC-ppa6gqc3w",
            "https://drive.google.com/uc?export=view&id=1C-KlszXeqwQyT4Afq6WXzmdPO_iJSkt7",
            "https://drive.google.com/uc?export=view&id=1IQFcaMSHxdif4JPUfTYQOjG37CUP4ng2",
            "https://drive.google.com/uc?export=view&id=1wtc2xDlf3lNrnIuKw9AqZVwbYnspBRSX",
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
                "kesan": "abangnya asik dan ramah.",  
                "pesan":"semangat kuliahnya bangg"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Ka nadya seru",  
                "pesan":"semoga dipermudah kuliahnya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak fathinah lemah lembut",  
                "pesan":"semangat menghadapi semester sekarang kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Lia ternyata kakak temen pplk kuu",  
                "pesan":"semangat terus kuliahnya kakak "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Fb4BPbRj30lbadr-Bm9-Y5_8Ein2qH1H",
            "https://drive.google.com/uc?export=view&id=1NdHfcgyW2Tf96WtLsdXn6aYYuJ5ay9OW",
            "https://drive.google.com/uc?export=view&id=1NxZjB-GpVP1oypnOtGYNt5ZjVB8xWoF_",
            "https://drive.google.com/uc?export=view&id=1XnrBrcfGXwNwKY9ZqKc2WLgYYEzO5CN4",
            "https://drive.google.com/uc?export=view&id=16rWPseGT4LVHBC62BYqw1YbdxLjAzba6",
            "https://drive.google.com/uc?export=view&id=1VGllhdDLEm7h8y8FqszkpaVX3TrfXgXM",
            "https://drive.google.com/uc?export=view&id=1T_7z86drzdyUc_EbUEd8k-oP1DMS4fmC",
            "https://drive.google.com/uc?export=view&id=13j5vtus0PzVc5ag1_-_nhHFzJMOqq5ER",
            "https://drive.google.com/uc?export=view&id=17639Avi768OWFW7vRGN1M3NdCjg_2Ana",
            "https://drive.google.com/uc?export=view&id=1C4ohVrEJKy8XSroU2mHQwUzOMhmrMNVg",
            "https://drive.google.com/uc?export=view&id=1YR2SjkVdf_VoS-hlRWs5cWUJRuolD2Bx",
            "https://drive.google.com/uc?export=view&id=1sRLhaCSLpJW_-R5EIXq8CxTK8TjKUyv6",
            "https://drive.google.com/uc?export=view&id=1xds3fYKuMhPS42G875hs8XyfMt3b-KKa",
            "https://drive.google.com/uc?export=view&id=1x1D8tto1LKwK-xT_mpBFHFvk8sCoMmUD",
            "https://drive.google.com/uc?export=view&id=1y-EGexmZgigIDGnGo0U2MZ2r0kfilQ34",
            "https://drive.google.com/uc?export=view&id=1P_wyybHZXzUwLNX_2PaeBSkMuViWZiK2",
            "https://drive.google.com/uc?export=view&id=1yO0uH4Op_VgOGkcPreb2EX5qmZagy1BC",
            "https://drive.google.com/uc?export=view&id=1QT32uEdAq_bgAC-LVxl2ERJe80n72g-J",
            "https://drive.google.com/uc?export=view&id=1ByZ08-XksPT6lshurv1MBeNRhcKoUEoD",
            "https://drive.google.com/uc?export=view&id=1PSeZiMK_gT2SSKGz6isfy-Fbh-XnJI5J",
            "https://drive.google.com/uc?export=view&id=1M7eeL0aAKuRGEaoITVyLEnFyxQzu-B_T",
            "https://drive.google.com/uc?export=view&id=1Ar8mARZCWEmRYmdQOzpqwBlcY19iBNja",
            "https://drive.google.com/uc?export=view&id=19TsN3KQLEckmrl9gPZlTwbcVB9S-7RUb",
            "https://drive.google.com/uc?export=view&id=1QifpZdvFatr-4w5VBT4vY0PbM7aHBmUi",
            "https://drive.google.com/uc?export=view&id=1MQIhBBS_Q4Kd6wkuPBm3ozO-k1dnzzO5",
            "https://drive.google.com/uc?export=view&id=1nybZifvG_QCyjn4-OL1iU4L-qeetzyD_",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Professional dan tegas.",
                "pesan": "Mohon bimbingannya selalu, bang!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Terima kasih atas bimbingannya Kak.",
                "pesan": "Semangat dan bahagia selalu kak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "tegas dan disiplin.",
                "pesan": "Terima kasih atas ilmunya, semoga kakak sehat selalu."
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "santai dan ramah",  
                "pesan":"semangat terus kuliahnya bang."# 1
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "komunikatif dan baik",  
                "pesan":"Senang bisa belajar dari abang."# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "santai tapi tetap fokus",  
                "pesan":"semangat terus ya kak"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Menyenangkan tapi tetap professional",  
                "pesan":"Semoga nasihat abang selalu berkesan"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Berenergi dan semangat",  
                "pesan":"Semoga dipermudah kuliahnya bang"# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Santai tapi tetap tegas",  
                "pesan":"Semoga bisa belajar banyak hal baru dengan abang"# 1
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "terlihat tenang dan bijaksana",  
                "pesan":"terus berbagi insight yang bermanfaat bang"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Mengasikkan dan fleksible",  
                "pesan":"terimakasih atas materinya kak"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "santai tapi tetap konsisten",  
                "pesan":"Semoga lancar kuliahnya"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "girly dan seru diajak ngobrol",  
                "pesan":"senang bisa kenal dengan kakak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "baik dan ramah",  
                "pesan":"tetap fokus dengan tujuan bang!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Santai tapi berwawasan",
                "pesan": "Tetap menginspirasi orang bang!"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Tegas dan tetap disiplin.",
                "pesan": "Sukses selalu untuk kakak."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang ramah dan tegas.",
                "pesan": "Mohon bimbingannya selalu bang!"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Tegas tapi adil.",
                "pesan": "Semoga kami bisa meneladani semangat abang."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Tanggap dan optimis .",
                "pesan": "semangat belajar kakak."
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Logis dan jelas.",
                "pesan": "Semoga tetap memotivasi bang!"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "ramah dan bijaksana.",
                "pesan": "Sukses selalu bang ditunggu arahan selanjutnya."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "berenergi dan berinisiatif.",
                "pesan": "Sehat dan sukses terus kak vany!"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak "# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Tegas dan semangat",  
                "pesan":"Semoga semangat terus ya bang"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "asik dan menyenangkan",  
                "pesan":"terus tebarkan kebaikan kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Membuat suasana menyenangkan dan tetap tegas",  
                "pesan":"Selalu optimis dengan tujuan bang!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1blR69eE41tPpKZWOgB2fRqeDDiM6Rh1Z",
            "https://drive.google.com/uc?export=view&id=10r79qJmnRAVzeugZhJuY_i3ew4OvM1jt",
            "https://drive.google.com/uc?export=view&id=16Xa7uUp1ocmxyc8qvQLUuOH94LHNnwTp",
            "https://drive.google.com/uc?export=view&id=1SHuQB7iTF5uEPEkALupBNU-yR1hx9Rsx",
            "https://drive.google.com/uc?export=view&id=1jpRCqO4SOhVESOuFbggGfwv3lSGqDoxy",
            "https://drive.google.com/uc?export=view&id=16F9doUJE7fDOL62SEW7Hh8TpIu3i-VeZ",
            "https://drive.google.com/uc?export=view&id=19KXgHeeVD8L1AKpPO-Cx4R3Fq_EbHzqu",
            "https://drive.google.com/uc?export=view&id=1igOioTu2zF0wcIeEQW-n225VPvPBeKdW",
            "https://drive.google.com/uc?export=view&id=1GvGoe6HrAbMKU6-FgH2XPuBNvmE4UIFH",
            "https://drive.google.com/uc?export=view&id=1DZjieHeNwneKGBTHYV13PzCtEFPhGpxB",
            "https://drive.google.com/uc?export=view&id=13Y66g9HKfwHpWpTNK6uAz0Yen9rO2WpY",
            "https://drive.google.com/uc?export=view&id=1zJsilZIyjIJa4u-Xvm1ihVzgdOCC5NoC",
            "https://drive.google.com/uc?export=view&id=1ZhiAj0exOs4nzOoSkOWPD0tpivudFZsj",
            "https://drive.google.com/uc?export=view&id=1Ad3KTE1ulu6lcQfbIXInwXXIV3-03y_K",
            "https://drive.google.com/uc?export=view&id=1l4m45_Yoo9nlRBNu9BkVRglbu4c1N-l_",
            "https://drive.google.com/uc?export=view&id=1HRHVlDZcgnW7RJuP9LG_3L37cMMP-yjJ",
            "https://drive.google.com/uc?export=view&id=1ltUI6k0D0QMjuCWgI0rU2ibwVlDmN9BZ",
            "https://drive.google.com/uc?export=view&id=1QF4j-vvLalzwqJM8wHlSpxBfCN0xGK48",
            "https://drive.google.com/uc?export=view&id=1TNGnJX6zeoFJtXNmymnH1lm07FW7eo6p",
            "https://drive.google.com/uc?export=view&id=1O2dOkqdX5v4yNzlscwPNslsZaGLKtmiB",
            "https://drive.google.com/uc?export=view&id=1AQbo3qsohvyIrmHYb3SzntfuNJHAp-SS",
            "https://drive.google.com/uc?export=view&id=1tvNo6zJi_Bd7zojtzKkjomPrN8DuZAhw",
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
                "kesan": "Selalu bersemangat",  
                "pesan":"Tetap mengispirasi banyaka orang bang"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "asik dan tetap hangat",  
                "pesan":"Senang bisa belajar dengan kaka"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Cepat dan tanggap",  
                "pesan":"Semangat berbgai ilmunya bang"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "memiliki aura positif",  
                "pesan":"Terus tebarkan energi positif itu kak"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "asik dan bijaksana",  
                "pesan":"Semangat dan fokus sama tujuan bang"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "asik dan humoris",  
                "pesan":"Semoga semangat abang menular"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Baik dan tetap tegas",  
                "pesan":"Lancar luncur kuliahnya di semester sekarang"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "santai dan memotivasi",  
                "pesan":"Semoga bisa belajar banyak hal dari kaka"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "baik banget dan inspiratif",  
                "pesan":"Semoga di permudah ya kak kuliah nya"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Santai tapi enak diajak berdiskusi",  
                "pesan":"Senang bisa belajar dengan abang"# 1
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "ramah dan berenergi",  
                "pesan":"Semangat menjalani kehidupan ini kak"# 1
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Pintar dan menginspirasi banget",  
                "pesan":"Semoga bisa belajar banyak hal dengan kakak"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@pebby_olla525",
                "kesan": "santai dan tetap ramah",  
                "pesan":"Senang bisa kenal dekat dengan kakak"# 1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Menyenangkan dan berenergi",  
                "pesan":"Selalu tebarkan hal positif kakak"# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Inspiratif dan perhatian",  
                "pesan":"Semoga arahan kakak memberi manfaat bagi saya"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Tanggap dan baik",  
                "pesan":"Semangat kuliahnya ya bang "# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "santai tapi murah senyum",  
                "pesan":"Terus berkarya dan menginspirasi kak"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Semangat dan kreatif",  
                "pesan":"terus berbagi ide cemerlang bang"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "cerdas dan teliti",  
                "pesan":"Semoga kemampuan itu selalu berkembang bang"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "ramah dan perhatian",  
                "pesan":"Semoga bisa belajar banyak hal dari kakak!"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "kreatida dan berwawasan",  
                "pesan":"Terus tebarkan energi positif bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EuwCusXQuQx05gu1KtlVL3-gUWQto2Wa",
            "https://drive.google.com/uc?export=view&id=1of_NQp2_Z6OeuEzLCV18gQf8YgkA5b9N",
            "https://drive.google.com/uc?export=view&id=1eYKiFnUn7TMpj5JUmlchtgeG4yTSopJY",
            "https://drive.google.com/uc?export=view&id=1yOmACkahWVCmQ4o3vzG_vA8Tdg0IcatU",
            "https://drive.google.com/uc?export=view&id=1FNPV8BtJ09Nusax1F6UQWhfMyKE8H58E",
            "https://drive.google.com/uc?export=view&id=1GFiYu6eK3urMDwbUuHexFgAkW4oWn4fJ",
            "https://drive.google.com/uc?export=view&id=1Xp0FxpPR2NFPfLMAM55MusWfOBlj2vrO",
            "https://drive.google.com/uc?export=view&id=1KQNyVbD5-GMdTyixgvz2i3r3mq5zmaDJ",
            "https://drive.google.com/uc?export=view&id=1KDYMooF_mp9iMj3AfbUn8FGZlfSPIgSV",
            "https://drive.google.com/uc?export=view&id=1PBDXS4I17KF7i-TlqpplXgoGTh5symgm",
            "https://drive.google.com/uc?export=view&id=1MiCa1Tl1SsI5jqhXdrQycA-3__L9cnmE",
            "https://drive.google.com/uc?export=view&id=1VqZmIfVWsLoWKULNGcpM4dG6tZV0Q9HI",
            "https://drive.google.com/uc?export=view&id=1BOV5lKvhQrVj_f8b_duWmpdyosyD99Ds",
            "https://drive.google.com/uc?export=view&id=1dol2n1Ks2Mh1d-q_G-igPv8GrewKSzgD",
            "https://drive.google.com/uc?export=view&id=1mniafU26cTOOWPFgp5LFHi5etvDXyI4s",
            "https://drive.google.com/uc?export=view&id=19lLNwb17bKysQz7xnqQ4pgKmv79HJmRn",
            "https://drive.google.com/uc?export=view&id=1a80Ceij3eGJ_0DZ7SpfQYGIgEza8t8Bo",
            "https://drive.google.com/uc?export=view&id=1Q1xmD8MDGBMimJhg8JjVHdCbapGKiw7R",
            "https://drive.google.com/uc?export=view&id=1PNYj1KB6Y941w3p_5tyowviJ0DGyi8Ch",
            "https://drive.google.com/uc?export=view&id=1cf1ovjw8WCsfuIXJ97Lf0uwiKZre1jEQ",
            "https://drive.google.com/uc?export=view&id=1N-0F2TjZIb2h5FC_oJBaulFc7xSLIyCD",
            "https://drive.google.com/uc?export=view&id=1AzSgSoefsF4KmOxY5EHKTjdPE_kMOJft",
            "https://drive.google.com/uc?export=view&id=1G1GdcJCvzu5AWt_5hLy2woN_ZZTDIZrM",
            "https://drive.google.com/uc?export=view&id=1n1-h1PITdkJA7dXwrwbLmU2uO4Jrw2c8",
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
                "kesan": "Tegas dan bijak dalam membimbing",  
                "pesan":"Terus rendah hati ya bang"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Ramah dan baik",  
                "pesan":"Terus tebarkan ketulusan kakk"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "elegan dan percaya diri",  
                "pesan":"Semoga dipermudah kuliah kakak"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Tangguh dan berempati",  
                "pesan":"Semoga segala hal berjalan lancar kak"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Tangguh dan baik",  
                "pesan":"terbarkan semangat membara"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Baik dan tangguh",  
                "pesan":"Semoga impian kaka di perlancar"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Ceria dan asik",  
                "pesan":"Jangan pernah kehilangan semangat kakk"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kalem dan cerdas",  
                "pesan":"Sehat selalu dan semangat kak"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Professional dan baik",  
                "pesan":"terus menjadi sosok yang tangguh bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Ramah dan asik",  
                "pesan":"Selalu tebarkan hal baik ya kak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "cantik dan ramah",  
                "pesan":"Semangat dan sukses selalu kak"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Lembut tapi jiwanya kuat",  
                "pesan":"Semoga setiap langkah selalu diberkahi kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Tegas dan berkemimpinan",  
                "pesan":"Jangan pernah padam semangatnya bang"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "kuat dan hebat",  
                "pesan":"Sukses selalu kak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "baik dan ramah ",  
                "pesan":"Semoga selalu ceria ya kak"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Tenang dan berenergi",  
                "pesan":"tetap menjadi diri sendiri ya bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Enak diajak berdiskusi",  
                "pesan":"semoga sukses selalu ya bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "ramah dan peduli",  
                "pesan":"Semoga bisa belajar hal baru bersama kaka lagi"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "ramah dan humoris",  
                "pesan":"Semoga impian mu tercapai kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Ceria dan menyenangkan",  
                "pesan":"Selalu tersenyum hangat ya kak"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Disiplin dan asik",  
                "pesan":"tetap jadi sosok diri sendiri kak"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "baik dan sopan",  
                "pesan":"Terus tebarkan kebaikan ya kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Ramah dan sopan",  
                "pesan":"semangat terus bang Qois"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "tenang dan perhatian",  
                "pesan":"Selalu rendah hati ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-3ew5M0M7dtfXaFUc4v8WuqjVRj1T7gj",
            "https://drive.google.com/uc?export=view&id=1F9cQUhMaezb0CS6IvfPYLl4e3Jn0UNTH",
            "https://drive.google.com/uc?export=view&id=185DVYn0nirolxMGIWXMeNprL00E3NScK",
            "https://drive.google.com/uc?export=view&id=12MfIFJZV76B0mnWd8RbBEnFGvWbIFzn0",
            "https://drive.google.com/uc?export=view&id=1vB7tgp7RscXcRcbka7PSY9myyn8m8u21",
            "https://drive.google.com/uc?export=view&id=1BMv6KK-t4lv6yZghjslH4BB4HTi6iP_x",
            "https://drive.google.com/uc?export=view&id=1uiQkLZvurvsI-bFKOlvFLvHaRurf6_Mm",
            "https://drive.google.com/uc?export=view&id=1AkuuHhvicgQnmiqRpARYnlxHstkNofIl",
            "https://drive.google.com/uc?export=view&id=1BcyD9RdNMR4opUVC4l-0ZQUWMKfNXas6",
            "https://drive.google.com/uc?export=view&id=1X0GkY6G48__W-QlOfjfv6drJv6c4L1YG",
            "https://drive.google.com/uc?export=view&id=1XHH4ntOxUlxRblbTx0GwO4hLcLTeGGCA",
            "https://drive.google.com/uc?export=view&id=1vZyNU2OHJfwwl07z214psvvuFUSt_43B",
            "https://drive.google.com/uc?export=view&id=1L9Vl5P_DPIX8OKepENfxYwK3JBpIBlwx",
            "https://drive.google.com/uc?export=view&id=1KAMuaQVUGeL474_Dgj-PQklGhyUdWbd9",
            "https://drive.google.com/uc?export=view&id=1lZvAoOcBgmA7fDc8_B4G45tgDnK5c6w5",
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
                "kesan": "Mashaallah hobi kaka",  
                "pesan":"Semangat terus kak"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Keren dan kuat",  
                "pesan":"Tetaplah jadi diri sendiri kak"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "hobinya keren banget bang",  
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "asik dan ramah",  
                "pesan":"jangan pernah menyerah fokus tujuan aja kak"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "hobi kita sama kakk",  
                "pesan":"Teruslah berkreasi ya kak"# 1
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Professional dan baik",  
                "pesan":"Semangat 45 bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "baik dan menyenangkan",  
                "pesan":"Semoga kakak semangat terus"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Keren dan Kuat dilihat dari hobinya",  
                "pesan":"Lancar-lancar kuliahnyaa kak"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "baik dan ramah",  
                "pesan":"Sukses dan tetaap rendah hati bang"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "aktif dan berenergi",  
                "pesan":"sehat selalu bang"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Rasa penasaran tinggi",  
                "pesan":"Jangan berubah tetaplah jadi diri snediri"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Keren, berbakat, dan kreatif",  
                "pesan":"terus kembangkan bakat itu"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Jiwa sportif tinggi",  
                "pesan":"Semangat ngejalanin hobinya bang"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Asik dan kreatif ",  
                "pesan":"Semoga bisa berkarya lewat musik"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Teliti dan sabar",  
                "pesan":"Terus asah kemampuan berpikir dan logikanya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZanUgckilFchxC0-rGb-O7Dh78d2M_5h",
            "https://drive.google.com/uc?export=view&id=13Yc_TB-0VILH9d31WYPjEZ1EZJH_SNwZ",
            "https://drive.google.com/uc?export=view&id=1A3sw-Xb7C_vWDnlZqMPoyVodGwdqBz1m",
            "https://drive.google.com/uc?export=view&id=1rKOIWIY11piHhRg1GcsgZDJbySQ_qyVI",
            "https://drive.google.com/uc?export=view&id=13ezm2H9moRG0kBmW104bl06Lmk7u3KxE",
            "https://drive.google.com/uc?export=view&id=16GNerXgYRfuealIdcQ8TVdt66NSkWPs5",
            "https://drive.google.com/uc?export=view&id=1pDaOq1CKClYFPpqJV4m2x2NGozkEBATW",
            "https://drive.google.com/uc?export=view&id=1f2V34NKOR_TBWKZFImW85W8jI_jm_B_b",
            "https://drive.google.com/uc?export=view&id=18DTzm8hpr4e4FBpO5-zLKv4NJN3jU6yV",
            "https://drive.google.com/uc?export=view&id=1fe__oeVY3jwL6N6eEN9q7QvHEqxxdYwB",
            "https://drive.google.com/uc?export=view&id=1XlR-Ybmwj-npTP-_vmsA2cGSS7wU9OS7",
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
                "kesan": "Asik dan enak diajak berdiskusi.",
                "pesan": "terus pertahaankan semangat berolahraganya bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Tenang dan punya imajinasi yang kuat",
                "pesan": "Terus pertahankan kebiasaan membaca kak"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Tampil rapi dan detail",
                "pesan": "Semoga makin sukses biar makin banyak koleksi parfumnya"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Bersemangat dan keliatan sehat",
                "pesan": "Semangat dan jangan lupa istirahat kak"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Santai dan ramah",
                "pesan": "Semangat kuliahnya ya kak"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Berenergi dan kuat",
                "pesan": "Sukses selalu dan jaga kesehatan kak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Rajin dan fokus",
                "pesan": "Terus pertahankan semangat belajarnya, berikan yang terbaik"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Seru dan punya selera hiburan yang keren",
                "pesan": "Semangat ngejar ending yang bahagia kak"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Seru dan berpandangan luas",
                "pesan": "Semangat kuliahnya dan jaga kesehatan kak"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "kreatif dan telaten",
                "pesan": "Kembangkan kemampuan masaknya dan semangat kuliah"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Ceria dan seru",
                "pesan": "Terus jadi pribadi yang ceria dan fokus sama tujuan"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1R6v7dPm5yDqqQv6Z4k9PKTexi2rcYBGz",
            "https://drive.google.com/uc?export=view&id=1b01pupje_U0snSlKCnqCGSxbl9jCkq6O",
            "https://drive.google.com/uc?export=view&id=1JDw2iZsDU49GN_gb5M9cE36IKE6XY5rz",
            "https://drive.google.com/uc?export=view&id=1slNNJecq2V4uir2SUXapkdf1rJkMUiYA",
            "https://drive.google.com/uc?export=view&id=1TRqOVk7ohmVpbizKhKVhuTu6D394Gd4d",
            "https://drive.google.com/uc?export=view&id=16DZF0r6dOq1siutVgG7YzpbaoOOA6ITr",
            "https://drive.google.com/uc?export=view&id=1WqPMX5M6_hEZIbeGN1vno-ImHJaRL0eE",
            "https://drive.google.com/uc?export=view&id=1Lz0J5jMo2X4pQREMmZr7kHGCPcDioc_r",
            "https://drive.google.com/uc?export=view&id=15c43wkrzc945Pi_07cczn9-mgGgkOaWE",
            "https://drive.google.com/uc?export=view&id=1uxOq5cgK1t2NrQiAjonumvoxWFn-QeZh",
            "https://drive.google.com/uc?export=view&id=1iAB7E99NylBsr5lcC031sKBTO_yJtB34",
            "https://drive.google.com/uc?export=view&id=1FoM_uX_Xa2vfQe_Bxb8e18BC9_wExCJY",
            "https://drive.google.com/uc?export=view&id=13lYowJTTASpPcaq2IhioFHHSS09TIkyB",
            "https://drive.google.com/uc?export=view&id=1cbtdtJepfbtV2fvc8HhJcQK_r24wywfc",
            "https://drive.google.com/uc?export=view&id=11CW7_DjTq1A4i8TeO9ogo1SUjKJmQnmm",
            "https://drive.google.com/uc?export=view&id=1JIOu3yIDHbx55PtWOitvqxxys87ZCCqe",
            "https://drive.google.com/uc?export=view&id=1kWkkaQZ4Nw0XjsySbvtJQ_82rbKJ7BAM",
            "https://drive.google.com/uc?export=view&id=1gs0VXJCN5QERlsIiBP5bfhiRnDXjbf8d",
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
                "kesan": "santai dan kelihatan care",  
                "pesan":"Semoga kegiatan sleep-callnya gak bikin begadang terus ya kak"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kreatif daan peduli sama kesehatan",  
                "pesan":"Terus pertahankan gaya hiudp sehat dan produktifnya kak"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Seru dan semangat",  
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Labo Jhon Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Keren dan seru",  
                "pesan":"Sukses selalu bang"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "berenergi dan sehat",  
                "pesan":"Tetap konsisten suka olahraga bang"# 1
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Keren dan unik",  
                "pesan":"Terus kumpulin gelang keren kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Cerdas dan teliti",  
                "pesan":"Semangat belajarnya kak"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Punya selera tontonan menarik",  
                "pesan":"Semoga bisa menikmati waktu santai dengan tontonan favorit"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Aesthetic dan keren",  
                "pesan":"Sukses selalu ya kak"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Keren dan baik",  
                "pesan":"Terus semangat masaknya kak"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "ramah dan menyenangkan",  
                "pesan":"Lancar luncur kuliahnya kak"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Enjoy dan menyenangkan",  
                "pesan":"Terus main dan explore dunia roblox kak"# 1
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Baik dan enjoy",  
                "pesan":"Semoga tetap bisa menyeimbangkan waktu ya bang"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Keren dan kritis",  
                "pesan":"Semangat dan sehat selalu kak"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Lucu dan baik",  
                "pesan":"Semangat menjalani semester sekarang kak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Detail dan keren",  
                "pesan":"Terus berkarya dan menemukan inspirasi"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Bakat yang luar biasa",  
                "pesan":"Terus asah kemampuan itu kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

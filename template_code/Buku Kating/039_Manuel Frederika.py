
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
            "https://drive.google.com/uc?export=view&id=1rfrZ7rHS4QHODJr4kO4VgOkd02FJ22EN",
            "https://drive.google.com/uc?export=view&id=1nLDbOSQPqEPAvkEGv1shPzHesLSLwsyp",
            "https://drive.google.com/uc?export=view&id=1-qcDzcF_EhPPyA04z0CXsFivWkhSZtOE",
            "https://drive.google.com/uc?export=view&id=1ni9WtqYPnf8kzDMK7rCU_aG4lSGpT21a",
            "https://drive.google.com/uc?export=view&id=11QtVLJ2_Uz5AHHHU_2EfCQRFVLbAPh7x",
            "https://drive.google.com/uc?export=view&id=1HroZxk5c0_k_vQh5SvWWBXbYJz2YvKcW",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Makan Pisang",
                "sosmed": "@_erendraa",
                "kesan": "Aslinya murah senyum dan chill banget",  
                "pesan": "Tetap jadi orang chill dan semangat di semester akhirnya bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Tegas dan beribawa ",  
                "pesan": "Semangat terus buat menjalani semester akhir nya bang"# 1
            },
              {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya asik dan gampang untuk ketawa",  
                "pesan": "Semoga kakak terus semangat menjalani hari harinya"# 1
            },
              {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Vibes positif banget dan kalem ",  
                "pesan": "Semoga diberi kemudahan menjalani kehidupan kuliahnya kak"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Murah senyum dan sangat asik",  
                "pesan":"Tetap jadi orang yang asik kak"# 1
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "kalem tapi tetap beribawa ",  
                "pesan": "Semangat menjalani dunia perkuliahannya kak"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1b6NiXcusIjZw9vf0xUobkkgIUe59UhKB",
            "https://drive.google.com/uc?export=view&id=1ZrV_c0IRd8Rly8ehoeajPr80Lyy40Unf",
            "https://drive.google.com/uc?export=view&id=147iTZOgPh6qzE47jORjOdwRl_T5eq8wZ",
            "https://drive.google.com/uc?export=view&id=1fgqZ_AaREF5-15uH0plgVkGOAwRgF7RC",
            "https://drive.google.com/uc?export=view&id=1ZjHgTCoxnnz_Lasm6emI0sABHfHklfRw",
            "https://drive.google.com/uc?export=view&id=1KUA5kddD70T8C0iJ-gStY_JaY9klHVzC",
            "https://drive.google.com/uc?export=view&id=1AkfhZvIwjCwZzUa_lUx9se6uObMiBMqt",
            "https://drive.google.com/uc?export=view&id=1oDLyrSs32IihqT0TNZlkA-e0bZE9nIH-",
            "https://drive.google.com/uc?export=view&id=1O7fhovJJGhz8Yqh3T8v-Sy9Urm7CKX1y",
            "https://drive.google.com/uc?export=view&id=1pBvoeHVVrSJTjuk3BPc1KUxgoUav2bgK",
            "https://drive.google.com/uc?export=view&id=1XIcP0PL6T7yfE-rTE7HX0raP7DNkO1sK",
            "https://drive.google.com/uc?export=view&id=1nfBVFi2p0m7BYkZFjw0vqJdJFqeV43OK",
            "https://drive.google.com/uc?export=view&id=1BigddMKNmHVOw6DaPOhdJu9d4STF0NsO",
            "https://drive.google.com/uc?export=view&id=1GAns3Vmny0Vbpw5Pf2Xd8tPVVwjmGKtN",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "Abangnya asik dan chill abis",  
                "pesan": "Semoga tetap semangat menjadi asprak kelas RA bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan": "Tetap jadi kakak yang humoris abiss "# 1
            },
              {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya kalem banget ",  
                "pesan": "Terus semangat menjalani dunia perkuliahannya ya kak"# 1
            },
              {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Keliatan banget Vibes positifnya kak",  
                "pesan": "Tetap semangat di semester akhirnya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Kakaknya OZT ",  
                "pesan":"Semoga tetap terus berprestasi ya kak "# 1
            },
             {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "kalem dan lucu kakaknya",  
                "pesan": "Semangat menjalani semester 5 nya kak"# 1
            },
              {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Keren abis abangnya",  
                "pesan": "Tetap jadi orang keren selalu bang"# 1
            },
              {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya tipe tipe soft boy gitu",  
                "pesan": "Lancar lancar kuliahnya bang"# 1
            },
              {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Cantik dan murah senyum",  
                "pesan": "Semangat ya kak menjalani semester ganjilnya"# 1
            },
              {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Vibes positif dan lucu kakaknya",  
                "pesan": "Semangat terus buat kakaknya di perkuliahan"# 1
            },
              {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "Awal tau waktu paskah kakaknya jadi kadiv Operasional",  
                "pesan": "Tetap jadi orang keren dan cool abis bang"# 1
            },
              {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya ramah dan baik banget",  
                "pesan": "Semangat kuliahnya bang "# 1
            },
              {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "Kakaknya murah senyum dan ramah ",  
                "pesan": "Tetap semangat ya kak"# 1
            },
              {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "Kakaknya asik dan baik banget ",  
                "pesan": "Semangat terus buat kakaknya "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11HytWDD5DssoSqu602MfliZw_IK9Myc1",
            "https://drive.google.com/uc?export=view&id=1XRNnLCAgXea-VALLGARKF8Mf_nE0R4_b",
            "https://drive.google.com/uc?export=view&id=1S5JHx8bYxIGKLzamKRds9W_LpS-9kTF9",
            "https://drive.google.com/uc?export=view&id=1Jarb0f8BEIvFNfHd18P59Y3XqZKQTvzx",
            "https://drive.google.com/uc?export=view&id=1C3wYEOieh7VqG_CewEH4NYhnlZxlQn0-",
            "https://drive.google.com/uc?export=view&id=1NvA46Jt4-m0j-vuCmPSQbka-TUeKg-Wn",
            "https://drive.google.com/uc?export=view&id=1ZuAYg2wGlUU7LEzKascxnLAeq5bFIRaH",
            "https://drive.google.com/uc?export=view&id=1DAJ0HquFapjHbTo8oV4Fj7ocyKcjrh7i",
            "https://drive.google.com/uc?export=view&id=1yLsxPHvjw3Xc3jlDT-5M-vb1XZDJ3IIU",
            "https://drive.google.com/uc?export=view&id=1zO45U-DZ2LVIkuj_pYE_iN2cvx_OYqsJ",
            "https://drive.google.com/uc?export=view&id=1wpnE3gqq1KQGTCtcoB5iA6QDt3GHqLZe",
            "https://drive.google.com/uc?export=view&id=18J73rrORP7QX0wC5kdxcCEP4rsQO7cqP",
            "https://drive.google.com/uc?export=view&id=1MwZMV7F3tMEfcEdPSTe2UdbGqWkj4DfX",
            "https://drive.google.com/uc?export=view&id=1oV1pPlwpbND7-QHK7Dku-NugsLxqGfbY",
            "https://drive.google.com/uc?export=view&id=10XLtDPtSFhmbqQ1n0dOTiri_uTif2G9w",
            "https://drive.google.com/uc?export=view&id=1-3aToZ4y3_cUjzcO9ONQKOfzScjcqoH7",
            "https://drive.google.com/uc?export=view&id=1ZNK4l7-CdmdXSUGNVxUY0ay1Omk6udoD",
            "https://drive.google.com/uc?export=view&id=1QtnKk2B-mRXXoBF2sv8V-_lrYDlAgx4S",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya cantik dan punya vibes positif",  
                "pesan": "Semangat terus kak sampai lulus"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakaknya murah senyum dan ramah",  
                "pesan": "Selalu jadi orang yang memiliki vibes positif ya kak"# 1
            },
              {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Kayaknya abangnya tipe yang perfeksionis deh kalau lagi dokum",  
                "pesan": "Semangat terus di perjalanan semster akhirnya bang"# 1
              },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "stylish parah, kayak orang amerika, semua outfit yang dipake kece",  
                "pesan": "Makasih sudah dokumentasi waktu paskah sains data bang"# 1
            },
              {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "kakaknya murah senyum tapi keliatannya tegas",  
                "pesan": "tetap jadi orang yang murah senyum ya kak"# 1
            },
              {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "kakaknya tipe yang langsung asik gitu ga kalem",  
                "pesan": "Semangat terus kak mmenjalani kehidupan sehari harinya"# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Keliatan banget vibes positif nya",  
                "pesan": "Semoga cepat lulus ya kak"# 1
            },
              {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Awalnya ngira kakaknya tipe yang serius ternyata murah senyum",  
                "pesan": "Semangat terus ya kak menjalani kehidupan sehari harinya kak"# 1
            },
              {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya vibes positif banget",  
                "pesan": "Terus jadi orang yang vibes positif ya kak"# 1
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak NIM akuuu",  
                "pesan": "Semangat terus kakak NIM!"# 1
            },
              {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Awalnya ngira kakaknya tipe serius serius gitu",  
                "pesan": "Semangat teruuss jangan patah semangat kak"# 1
            },
              {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "Kakaknya ramah dan murah senyum",  
                "pesan": "Semangat terus jangan patah semangat kak"# 1
            },
              {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Vibes positif bangett kakaknya",  
                "pesan": "Selalu jadi orang vibes positif ya kak"# 1
            },
              {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Gapernah liat kakaknya ga senyum, pasti selalu senyum terus",  
                "pesan": "Tetap jadi orang yang vibes positif ya kak"# 1
            },
              {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kayaknya kakaknya asik dehh",  
                "pesan": "Sehat sehat terus kak dan jangan patah semangat ya kak"# 1
            },
              {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakaknya keliatan orangnya baik banget",  
                "pesan": "Semangat nugas nya kak"# 1
            },
              {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "outfit kakaknya lucu dan imut",  
                "pesan": "Jangan lupa makan dan minum ya kak"# 1
            },
              {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "kakaknya kalau ngomong lembut banget",  
                "pesan": "semangat terus buat kakaknya dehh"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HOPIs82L0IvzH5KVYCorHyU-akovhvtm",
            "https://drive.google.com/uc?export=view&id=1e8p5aDh5vQA-Go816Ta6cYHvXyvrRVBD",
            "https://drive.google.com/uc?export=view&id=1w3c5WL-uP2-0nKJtVM4n01IVtoFfWkB3",
            "https://drive.google.com/uc?export=view&id=1NAuA-vebBLfim6kmFMxe5Xqp438buE8c",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya chill banget, seruu, kayaknya kalau ngobrol ga bakal kehabisan topik",  
                "pesan": "Jangan bosan ngasprak Alpro RA ya bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "Keliatannya kakaknya tipe pendengar yang baik",  
                "pesan": "Semangat kak mengejar deadline semua tugas"# 1
            },
              {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya sabar banget kalau ngajarin ALE",  
                "pesan": "Makasih ya kak sudah mau mengajari kami ALE"# 1
            },
              {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya lucu dan vibes positif banget",  
                "pesan": "Semangat kak jangan lupa minum air putih"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1y0vf4oJqigo-9DTcG9U3vouxz-GVup6j", #1
            "https://drive.google.com/uc?export=view&id=1RyfB9RQm_wLMKxTZhbjP5zWg5FDcRbD5", #2
            "https://drive.google.com/uc?export=view&id=1RIpO649SxbpyZO_hueNlTKamw927xz3e", #3
            "https://drive.google.com/uc?export=view&id=1ojc7tkA4qoTNmxmvSxsQm6u-cu1JBM6o", #4
            "https://drive.google.com/uc?export=view&id=1uY21z7ZARqUx0DYlRjN9I_QJ3v2Mh-oo", #5
            "https://drive.google.com/uc?export=view&id=1Qn72oVqc7q2PN1Y60cZPsX6bekHq6QAw", #6
            "https://drive.google.com/uc?export=view&id=1vpE6FSS--nDQsoYOmU1lBUPha2GxhI7L", #7
            "https://drive.google.com/uc?export=view&id=1oJj0RNeGGXsiNEtQNZMNoJzlijmHBSQR", #8
            "https://drive.google.com/uc?export=view&id=1ZTy11a561IMam-VCVK9NVqx7B-Zc15bY", #9
            "https://drive.google.com/uc?export=view&id=162vdqnHfMcZUYla1kI0mKEhUg5AYGusT", #10
            "https://drive.google.com/uc?export=view&id=1cnpXvSAZfo3GAWNNXAvBvdXdqpxSXjY1", #11
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": "Kakaknya keren banget ngasih banyak ilmu di dunia perbisnisan",  
                "pesan": "Semoga kakaknya jadi pengusaha sukses di masa yang akan datang"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakaknya kalau ngomong lembut banget",  
                "pesan": "Sehat selalu ya kak, jadi orang yang vibes positif selalu"# 2
            },
              {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "Kakaknya outfitnya simple tapi keren",  
                "pesan": "Semoga abangnya sehat selalu"# 3
            },
              {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya ramah dan murah senyum ",  
                "pesan": "Semoga kuliah kakak diberi kelancaran ya "# 4
                   },
              {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "Kakaknya lucu dan murah senyum",  
                "pesan": "Semoga kakaknya sehat selalu ya"# 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": ".",
                "asal": ".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": ".",
                "kesan": "Kakaknya kalau ngomong lembut banget dan ramah",  
                "pesan":"Terus jadi orang yang vibes positif ya kak"# 6
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Awal ngeliat dah langsung kepikiran abangnya mirip JHON tiktoker",  
                "pesan": "Semangat terus di semester akhirnya bang "# 7
            },
              {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya murah senyum dan ramah banget ",  
                "pesan": "Semanagat terus menjalanin kehidupan sehari harinya kak "# 8
            },
              {
                "nama": "Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "Kakaknya kalau senyum manis banget",  
                "pesan": "Ayo kapan kapan mabar ML kak aku main juga"# 9
            },
              {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya positif vibes banget",  
                "pesan": "Terus jadi orang yang vibes positif ya kak "# 10
            },
              {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakaknya kalau ngomong lembut banget dan selalu senyum ",  
                "pesan": "Terus jadi orang yang memiliki vibes positif ya kak"# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sNhF7Zexwqcqw9-tiBZRmiIfbqEGrEfW", #1
            "https://drive.google.com/uc?export=view&id=1GNMmW1RCIzftuaL4-ZtEB74tcwlbfJJZ", #2
            "https://drive.google.com/uc?export=view&id=1Fr9rlOv3YDPLTw2fdW6Qrrl6OcW_9ZLU", #3
            "https://drive.google.com/uc?export=view&id=1GlfduTxs92-JMJEcGki7rz8n2TLM-rE-", #4
            "https://drive.google.com/uc?export=view&id=1xtWV7T80QiyJ8r-HUFB4d4tttgOvg6x3", #5
            "https://drive.google.com/uc?export=view&id=1EqxWIBPmM9cGEf-bzbMl6oHxfjDrAER4", #6
            "https://drive.google.com/uc?export=view&id=1A-OuVpwp0XhOGywlZdvcI0jW_3ASl7ue", #7
            "https://drive.google.com/uc?export=view&id=1mWX7FvcAsJ8z5iTKsgqUfK3kwsEhDtym", #8
            "https://drive.google.com/uc?export=view&id=1qiRwtySiUQCDo0EyyyTl0WpBp_04ewzc", #9
            "https://drive.google.com/uc?export=view&id=1zPNokNcGAC9yHiQCwCNOjrbanIfVMVcM", #10
            "https://drive.google.com/uc?export=view&id=1Ba2pfxfMowfAJ7vi_A_0yVWHxCXvzfDS", #11
            "https://drive.google.com/uc?export=view&id=1ilaOswTkoBi7e1CNgmKnvLPb78eq9wLz", #12
            "https://drive.google.com/uc?export=view&id=1mWAEFfw-NVi_YBbrghOcrXStqX5SbQPU", #13
            "https://drive.google.com/uc?export=view&id=1oSPimvfMPGu96NjSZne-Z_jaY8_AIPnQ", #14
            "https://drive.google.com/uc?export=view&id=1AMS2OJT0W1AWLR4fZeUPSfDy2Nxveah5", #15
            "https://drive.google.com/uc?export=view&id=1CRmn6i7EEu6y9XurKHTBVt5CCnaLhsEQ", #16
            "https://drive.google.com/uc?export=view&id=1NXmeprVVsMmXzZI9KQy_kcN7W_8f9PKw", #17
            "https://drive.google.com/uc?export=view&id=1_etjWIgEphFIlROkynVVgnyzLOFSqufT", #18
            "https://drive.google.com/uc?export=view&id=1M_5C8T5fnh1Ynq3eRgSGJtZl4O0FJG9E", #19
            "https://drive.google.com/uc?export=view&id=1nrL0lOkfG-w_svciokr-qX4UpJNARlXe", #20
            "https://drive.google.com/uc?export=view&id=15C2i5WdfRPJEb2k2-ISSLo40aj1Rg0H5", #21
            "https://drive.google.com/uc?export=view&id=1C_s4dsppf1-QHmGtcDVq3PKK-1fVuIW1", #22
        ] 
        data_list = [
            {
                "nama": "Randra Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya murah senyum, asik, aura mikfes nya kuat banget ",  
                "pesan":"Semoga abangnya cepat lulus"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Masih ga nyangka kakaknya dari Kepri juga",  
                "pesan":"Semangat terus ya kak sampai luluss "# 2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya jago ngoomong dan murah senyum banget ",  
                "pesan":"Semoga cepat lulus dan mendapatkan nilai yang terbaik bang "# 3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "kakaknya aura vibes positif banget kalem juga ",  
                "pesan":"Jangan lupa makan dan minum kak, semangat terus"# 4
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnya asik dan ga kaku ",  
                "pesan":"Semoga makin banyak prestasi prestasi yang menghampiri ya bang "# 5
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya kalau senyum manis banget, tipe tipe softboy ",  
                "pesan":"Tetap jadi orang yang memiliki vibes positif ya bang "# 6
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "Jarang liat sih tapi abangnya kayaknya asik banget deh kalau udah dekat ",  
                "pesan":"Semangat terus bang menjalani kehidupan di perkuliahan "# 7
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakaknya kelaitannya lemah lembut dan murah senyum ",  
                "pesan":"Terus jadi orang yang memilki vibes positi ya kak "# 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya cantik dan kalau senyum manis banget ",  
                "pesan":"Semoga kakaknya lulus tepat waktu dan mendapatkan nilai terbaik " # 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Abangnya mirip bryan ",  
                "pesan":"Semangat terus buat abang nya jangan lupa makan dan minum"# 10
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya lucu dan manis banget ",  
                "pesan":"Semanagat terus mengejar deadline "# 11
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya keliatannya  galak aslinya murah senyum ",  
                "pesan":"Semangat terus ya kak jangan lupa makan dan minum "# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kakaknya murah senyum dan kalau ngomong lembut",  
                "pesan":"Semangat terus ya kak menjalani kehidupannya sehari hari "# 13
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakaknya tipe yang langsung asik deh kayaknya",  
                "pesan":"Semangat terus ya kak di dunia perkuliahannya"# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@i",
                "kesan": "Keliatannya kakaknya galak aslinya perhatian",  
                "pesan":"Makasi kak dah nanyain keadaanku waktu di notiz hut"# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Abangnya baik banget mau ngasih ilmu ngoding, belajar sama abangnya ngoding jadi simple",  
                "pesan":"Makasih bang dah bagiin ilmu ngoding bang"# 16
            },
            { 
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kayaknya Kakaknya tipe yang langsung asik deh ",  
                "pesan":"Tetap semangat terus ya kak jangan meninggalkan ibadah "# 17
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Abangnya baik banget, asik parah pokoknya ",  
                "pesan":"Semoga keinginannya tercapai dalam waktu dekat "# 18
            },
          
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakaknya vibes positif pake banget",  
                "pesan":"Tetap jadi orang vibes positif terus ya kak"# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakaknya baik banget dan perhatian",  
                "pesan":"Semangat terus buat kakaknya jangan patah semangat"# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Abangnya baik banget mau bantuin dan ngasih tau banyak hal tentang website",  
                "pesan":"Makasih ya bang ilmu ilmunya"# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@",
                "kesan": "Abangnya kalem banget, inget banget abangnya ozt pas pplk 2024 ",  
                "pesan":"Semangat terus bang semoga banyak prestasi yang menghampiri "# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IZfUoso_3hANchO3V9WDj1Wz0goSJ9Ap", #1
            "https://drive.google.com/uc?export=view&id=1yRNc715rB_7KRV9afDni33CeySndCbUq", #2
            "https://drive.google.com/uc?export=view&id=1bntuOow32e_OyCjvllk2PQkvM3LAOuUs", #3
            "https://drive.google.com/uc?export=view&id=13vqcwQeFH1n-5zeFTUOFZlzLNPptSqAc", #4
            "https://drive.google.com/uc?export=view&id=1TwqMtg00R6LhTe7CJ0GpObBbWFQG2g4C", #5
            "https://drive.google.com/uc?export=view&id=1Z6t49bngNENhlN7IddhC5DRi0A1LpOxy", #6
            "https://drive.google.com/uc?export=view&id=12oX4cSw5FPJMwe2kof16KthWVqGqsggX", #7
            "https://drive.google.com/uc?export=view&id=1o7Zi51B5wqk472Biz-c9l-v3wDp6gKh6", #8
            "https://drive.google.com/uc?export=view&id=12BcfkIXAY39J9tHVTZoUOs62Wz4KkvLj", #9
            "https://drive.google.com/uc?export=view&id=1fZSBlBZCemUGJsEXLRCW2oseCTXVGXGG", #10
            "https://drive.google.com/uc?export=view&id=1ObOeD6gqaaJmRzBwfzzEbk9SEzhrgXDw", #11
            "https://drive.google.com/uc?export=view&id=1qEjBQNb41FnxcUn7AbEVh2KCIA33tEPJ", #12
            "https://drive.google.com/uc?export=view&id=1qIJ7aWFeqD33HwuPKzYS_eF3sC68JAIe", #13
            "https://drive.google.com/uc?export=view&id=1j6E5oUw6gyUjqyUo18SrSY-cPk9cAq-U", #14
            "https://drive.google.com/uc?export=view&id=1DTjZju6u0YpkYNSS_rg2XxAkdkoTsZ5d", #15
            "https://drive.google.com/uc?export=view&id=1KiR5a5vAntkQMj7saqgEKZsFY1VY4yKL", #16
            "https://drive.google.com/uc?export=view&id=1EdVw2Aqjis8OEHUhDL3T0lxX1ZA5C8ve", #17
            "https://drive.google.com/uc?export=view&id=1euYs9OZXznl9x1d0azMxwSdfLUccO-2s", #18
            "https://drive.google.com/uc?export=view&id=1I109Jy8MS1pQui_dmbiEZWuEkqryfxzB", #19
            "https://drive.google.com/uc?export=view&id=1fTDqzEniWpliBFTshZ1vuBHlYrjRjJk7", #20
            "https://drive.google.com/uc?export=view&id=1L3vkIYpsfTSY95-ZbGNvcIY56hww_RrV", #21
            "https://drive.google.com/uc?export=view&id=17l493GWB7yBNar-zGTCI5mqYp7_U6_e0", #22
            "https://drive.google.com/uc?export=view&id=1SWpA8pqlor25nbV3O_IsOLIVJ--hBdgB", #23
            "https://drive.google.com/uc?export=view&id=1DrqL6jvJNVmSDQMKluQwXCluYiD7b9ht", #24
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnya baik banget banyak ngasih ilmu tentang departemen eksternal ",  
                "pesan":"Makasih ilmu ilmu nya bang"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya ramah banget dan kalau senyum manis banget ",  
                "pesan":"Semangat terus kak menjalani semester akhirnya "# 2
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya baik banget mau ngajari pas codingan ku ga jalan ",  
                "pesan":"Semoga tetap betah ya kak ngasprak di kelas RA "# 3
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "Mentorku paling terbaik deh, asik pake banget, perhatian banget, paling ngertiin anak anaknya, fast respon, definisi perfect ada di kak sonya",  
                "pesan":"Makasih banyak buat banyak hal deh kak, infokan gacoan satu kelompok dalam waktu dekat "# 4
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Tau kakanya karna sering masuk story wa kak sonya ",  
                "pesan":"Semangat terus kak jangan lupa makan dan minum "# 5
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya manis, murah senyum dan kalem ",  
                "pesan":"Semangat mengikuti Duta Itera nya kak "# 6
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Tegas, terkadang asik, aslinya abangnya baik banget ",  
                "pesan":"Roma 8:28"# 7
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya murah senyum, mirip teman SMA ku ",  
                "pesan":"Semoga keinginannya tercapai ya kak "# 8
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya tipe  tipe softboy ",  
                "pesan":"Semangat terus buat abangnya dan jangan patah semangat "# 9
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "Kakaknya vibes positif banget dan ramah ",  
                "pesan":"Semangat menjalani hari hari nya kak "# 10
            },
            {
                "nama": "Khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Cantik dan kakaknya manis banget ",  
                "pesan":"Semangat terus kak jangan tinggalkan ibadah "# 11
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya murah senyumm aura orang baiknya keliatan banget ",  
                "pesan":"Semangat terus buat kakaknya "# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya tipe cool boy, masih ga nyangka ada orang batam di data ",  
                "pesan":"Kapan kapan pulang bareng ke batam yok bang "# 13
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya kalem dan kalau senyum manis banget ",  
                "pesan":"Semangat terus kak semoga prestasi menghampiri kakak "# 14
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya senyum manis banget ",  
                "pesan":"Semangat terus kak semoga kakak selalu jadi orang vibes positif "# 15
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya kalau ngomong lucu, mirip giyat sekilas ",  
                "pesan":"Semangat jadi mentor nya kelompok giyatt bang "# 16
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakaknya kayaknya tipe yang lemah lembut deh ",  
                "pesan":"Semangat terus kak jangan lupa makan dan minum yang cukup"# 17
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya kalau senyum manis banget ",  
                "pesan":"Semangat terus kak semoga cepat lulus ya kak "# 18
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Awalnya ngira kakaknya tipe yang serius gitu, aslinya murah senyum ",  
                "pesan":"semangat terus kak menjalani hari harinya"# 19
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya keren banget, cool parah",  
                "pesan": "Semangat terus bang menjalani hari harinya "# 20
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Awalnya ngira kakaknya tipe serius gitu, aslinya baik banget ",  
                "pesan":"Makasih banyak pake banget kak udah bawa aku klinik "# 21
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abangnya asik dan murah senyum, awal tau abangnya karna satu perwalian ",  
                "pesan":"Semangat terus buat abangnya jangan tinggalkan ibadah "# 22
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakaknya kalem dan manis banget ",  
                "pesan": "Jangan patah semangat kak menjalani hari harinya "# 23
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya lucu, cantik, manis banget ",  
                "pesan":"Makasi kak udah ada di dunia ini "# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=110ugIuUOeMmiyilwovaDQlJCkZtacV7M", #1
            "https://drive.google.com/uc?export=view&id=1Ff50qEl4JbBvdFexY4RzfZ3aitD-o560", #2
            "https://drive.google.com/uc?export=view&id=1wHW35fH8gEyzomYIQUxhSoI2BAS5JpAn", #3
            "https://drive.google.com/uc?export=view&id=1snSXrQM1Gp3wOp1W8O9PxXj8KxdWyMiI", #4
            "https://drive.google.com/uc?export=view&id=1JRouZp2uakUi_Cz1oCxlVYbFhm9hfhLd", #5
            "https://drive.google.com/uc?export=view&id=1iOCFSqObO6KcRuC4UJYdYopX_1QEDnq8", #6
            "https://drive.google.com/uc?export=view&id=1jK7LGu2wilPgkLmktRXDGKtFkpyjiaws", #7
            "https://drive.google.com/uc?export=view&id=1NGh4cU9t401FE_QY04whRykPwx4q1-7M", #8
            "https://drive.google.com/uc?export=view&id=11NWwc3-a-7--id3_IfXmKj0JHJw3BtrU", #9
            "https://drive.google.com/uc?export=view&id=1gGfvbuXF6Pb3tfrugNDhf55qQJlvh8TE", #10
            "https://drive.google.com/uc?export=view&id=14VGeiQtg-MU9DQJFkt86FB-GpGXSZkuh", #11
            "https://drive.google.com/uc?export=view&id=1wM20tRFuGb_66fXSc-IPlpYqMnpPH6iU", #12
            "https://drive.google.com/uc?export=view&id=19ziizmXoGPU78MZr59xSXsO6pss2soMN", #13
            "https://drive.google.com/uc?export=view&id=1HlZEXJ-XpsG8bjl3iDcENVNM_1QqI_L0", #14
            "https://drive.google.com/uc?export=view&id=1s5zmCY7YSfmiQkQu0EvBhczS9ibIToXf", #15
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya beribawa banget ",  
                "pesan":"Semangat terus menjalani hari harinya kak "# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya kalem banget tapi murah senyum  ",  
                "pesan":"Semangat terus buat kakaknya dan sehat sehat terus ya kak "# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya keliatan bangeet aura baiknya ",  
                "pesan":"Tetap semangat menjalani hari harinya ya kak "# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Kakaknya vibes positif banget ",  
                "pesan":"tetap selalu jadi orang yang memilki vibes positif ya kak "# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya keren, cool, awalnya ngira serius aslinya abangnya murah senyum ",  
                "pesan":"Semangat terus bang jangan tinggalkan ibadah "# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya humble dan ceria banget",  
                "pesan": "Semangat terus buat kakaknya jaga kesehatan ya kak "# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakaknya manis banget, aslinya murah senyum kakaknya ",  
                "pesan": "Semangat kak menjalani hari harinya "# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Abangnya tipe softboy gitu ",  
                "pesan":"Jaga kesehatan dan tetap semangat ya bang "# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya ramah banget dan murah senyum ",  
                "pesan":"Semangat menjalani hari harinya bang "# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya baik banget, dan tipe lemah lembut ",  
                "pesan":"Semangat terus bang semoga cepat lulus bang "# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik banget, seru seru semua games yang kakak bawakan ",  
                "pesan":"Jaga kesehatan dan jangan sampai tinggalkan ibadah ya kak "# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Kakaknya lucu, manis, cantik ",  
                "pesan":"Makasih kak udah ada di dunia ini semoga kita ketemu lagi ya kak  "# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Abangnya jarang senyum tapi keliatannya tipe softboy ",  
                "pesan":"Semangat terus menjalani hari hari nya bang "# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Kakaknya manis banget, murah senyum aura sering pelayanan gereja kuat banget ",  
                "pesan":"Tetap semangat menjalani hari harinya kak "# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakaknya kalau senyum manis banget",  
                "pesan":"Tetap semangat dan jaga kesehatan ya kak "# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15yhuVDxYjreNKF5LZUpOPWQ8mqY7my3U", #1
            "https://drive.google.com/uc?export=view&id=1s5-Mu-beVohGW3lSVXPV3Q8IXqjHJaP-", #2
            "https://drive.google.com/uc?export=view&id=1_sTO8YBAsML5flyEqXFcefNfqi_oUmM8", #3
            "https://drive.google.com/uc?export=view&id=1Xu3Dspl1jPhpLNycQWfNqnsfWEMK74K0", #4
            "https://drive.google.com/uc?export=view&id=14jStMnuqysXPWIQtexJx7RseBtoQ38vC", #5
            "https://drive.google.com/uc?export=view&id=1qn5bq2aV1lO474s08nGZiaOrd_nzcY35", #6
            "https://drive.google.com/uc?export=view&id=1pFNZ84U05xLNYg9LHpwML2MN7FQHb5-u", #7
            "https://drive.google.com/uc?export=view&id=1ZrcKUNDLDlaXq4SkCRUh2kz1Wd59gXmB", #8
            "https://drive.google.com/uc?export=view&id=1KWYflbM5_hZb6l18N_YBqko4WcoaZmpq", #9
            "https://drive.google.com/uc?export=view&id=16YnRVStOQ0_5xzcofKWcquiz_NmyGK0e", #10
            "https://drive.google.com/uc?export=view&id=1CjhlcfCrqPBwmQcdEDN3607t_qKAG-Ij", #11
            "https://drive.google.com/uc?export=view&id=1pYRJllNGpMrcqaEMXOZAYDD7TIU6zeRs", #12
            "https://drive.google.com/uc?export=view&id=1s9Zh7Zq0yK86hLK5c6zXn8mMaIwglOBL", #13
            "https://drive.google.com/uc?export=view&id=1c37215c34mLcSOeeSx2OGP4vQ271eGMW", #14
            "https://drive.google.com/uc?export=view&id=1OOQ1tG8cQeuBRvaIW97WtYKpXMyiy6Vt", #15
            "https://drive.google.com/uc?export=view&id=1-OKqbrWf-Js3M4x_N-s1m1O-dXlRCKsk", #16
            "https://drive.google.com/uc?export=view&id=1xHr9uektNf9vt-CsSzJ_a73CGxoDpTxP", #17
            "https://drive.google.com/uc?export=view&id=1nV4O2rmnD7w3Hs1ZOicWV1rnPm1Ugthq", #18
            "https://drive.google.com/uc?export=view&id=1w_0wenlBxfDzTcO6zN3TyCa47kp55inP", #19
            "https://drive.google.com/uc?export=view&id=1hiIAWNgb4iTtn41wiqZHtYy1MkqjPJNo", #20
            "https://drive.google.com/uc?export=view&id=1JcLbeuyOhScj68XciVks3nDWboV5qbr6", #21
            "https://drive.google.com/uc?export=view&id=1dxmecVxv7VZj4PyRqLplUq0NiujN__y5", #22
            "https://drive.google.com/uc?export=view&id=11m9Vl0ZS1WDpNPnoyCM9KEEMCy55WmyR", #23
            "https://drive.google.com/uc?export=view&id=1U_zqZDcsfZNgqmBCdwIZYt6LA512fAcI", #24
            "https://drive.google.com/uc?export=view&id=11g_E6JXBfpuEkrHXl2uBRhTcnDick0eU", #25
            "https://drive.google.com/uc?export=view&id=1t7JpcSyhIZUNK4LijhhFlW7-hJLC43a3", #26
            
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": "Tegas, beribawa, tapi pas penampilan angkatan 22 di paskah abangnya lucu banget",  
                "pesan":"Semangat terus bang jangan lupa ibadah bang"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "Kakaknya baik dan perhatian",  
                "pesan":"Semangat terus buat kakaknya semoga cepat lulus kak"# 2
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "Tegas dan beribawa",  
                "pesan":"Makasih kak sudah membimbing kami"# 3
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Abangnya keren, asik, murah senyum, enak diajak ngobrol",  
                "pesan":"Gas terus kawal sampai jadi presma"# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "kakaknya cantik banget tapi agak seram",  
                "pesan":"semangat terus buat kakaknya dan jaga kesehatan"# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Seram tapi kalau ngobrol asik",  
                "pesan":"Sehat sehat terus bang dan jaga kesehatan"# 6
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Abangnya kalem, perhatian, enak kalau ngobrol",  
                "pesan":"Kapan kapan ayok pulang bareng ke batam bang"# 7
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "kakaknya baik banget nawarin jajanan",  
                "pesan":"semangat lombanya kak"# 8
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "Abangnya keren, ngasih ilmu tentang github",  
                "pesan":"Makasih banyak ilmu ilmu yang udah dikasih ke kami"# 9
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "Abangnya tegas dan beribawa",  
                "pesan":"Semangat terus bang dan jaga kesehatan"# 10
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakaknya baik banget dan perhatian",  
                "pesan":"Makasih ya kak sudah bantu aku waktu masuk ke klinik"# 11
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "Abangnya murah senyum tipe tipe softboy keliatannya",
                "pesan": "Semangat terus buat perjalanan di semester akhirnya bang" # 12
            },
            
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya keren dan cool,",
                "pesan": "Ayok kulineran bareng bang" # 13
            },
            
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakaknya baik banget dan pengertian banget",
                "pesan": "Makasi banget ya kak udah banyak bantu pas masuk medis" # 14
            },
            
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "-",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya serem, tapi aslinya murah senyum",
                "pesan": "Tetap semangat dan jangan tinggalkan ibadah ya kak" # 15
            },
            
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya chill habis, kalau senyum manis banget",
                "pesan": "Semangat terus kak menjalani hari harinya" # 16
            },
            
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya tipe tipe softboy",
                "pesan": "Semoga abangnya diberi kemudahan dan semangat terus" # 17
            },
            
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Abangnya cool dan ramah",
                "pesan": "Semangat terus dan jaga kesehatan bang" # 18
            },
            
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "Abangnya asik banget dan cool",
                "pesan": "Semangat terus bang di dunia perkuliahannya" # 19
            },
            
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "Kakaknya kalem banget tapi rajin deh keliatannya",
                "pesan": "Tetap jadi orang rajin dan semangat terus ya kak" # 20
            },
            
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "Abangnya kocak banget, mau gimanapun lucu",
                "pesan": "Semangat terus bang jangan sampai bosan main futsal" # 21
            },
            
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "Kalem, cool tapi beribawa",
                "pesan": "Sehat sehat terus ya bang jangan patah semangat" # 22
            },
            
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "Tinggi, keren dan cool",
                "pesan": "Tetap semangat dan jaga kesehatan ya bang" # 23
            },
            
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "Aura positif vibes nya keliatan banget kak",
                "pesan": "Tetap semangat ya kak dance nya" # 24
            },
            
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakaknya kalau ngomong lembut banget",
                "pesan": "Semoga kakak tetap semangat terus dan jaga kesehatan ya kak" # 25
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Abangnya ramah dan tipe tipe softboy",
                "pesan": "Semangat terus bang di dunia perkuliahannya" # 26
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    psda()


# Tambahkan menu lainnya sesuai kebutuhan
























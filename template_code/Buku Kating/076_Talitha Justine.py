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
            "https://drive.google.com/uc?export=view&id=1G1to2u33zswQ4UHA7-J0m5wOh1KNyxhP",
            "https://drive.google.com/uc?export=view&id=1UrAwXfGcHfpYDa_CKeSggwDpG9C1xVrZ",
            "https://drive.google.com/uc?export=view&id=1j3P20Pc3UgCB4pa9oV8wnhUQMxQ8h5DA",
            "https://drive.google.com/uc?export=view&id=1es3GgWsthe_KrbvRwdbxDjxXsqgpEymh",
            "https://drive.google.com/uc?export=view&id=15A1aHauWaqoZr9mWum97w1rg1uE6Gs-2",
            "https://drive.google.com/uc?export=view&id=18CoDoIWaZFtKUFpBXyKAzLw5lWV3VdTK",
            
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau Damar",
                "hobbi": "Ikut lomba burung murai",
                "sosmed": "@_erendraa",
                "kesan": "Keren, asik dan pastinya inspiratif",  
                "pesan":"Tetep jadi panutan yang chill ya bang!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren banget bang sampe nembus layar",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Ayres kost",
                "hobbi": "Jajan",
                "sosmed": "@celisabethh_",
                "kesan": "kakanya asik, bawaannya ceria terus",  
                "pesan":"bahagia selalu kak"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakanya jarang ngomong tapi vibesnya adem",  
                "pesan":"sehat selalu ya kak"# 1
            },
            {
                "nama": "Eksanty F Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Kelagian Kecil, Pahawang",
                "alamat": "Pesawaran",
                "hobbi": "Ngambilin Lanyard",
                "sosmed": "@eksantyfebriana",
                "kesan": "asik dan ga bikin canggung",  
                "pesan":"Bahagia dan sukses selalu kak"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Gya kost",
                "hobbi": "Cute",
                "sosmed": "@farahanumafifahh",
                "kesan": "asik, seru dan ga banyak ngomong juga",  
                "pesan":" semangat kak, jangan lupa istirahat"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XXPiP1cVAtnImtYD8PyINaSFU1hAQ6DW",
            "https://drive.google.com/uc?export=view&id=1OpLONg-AIiSFn4CotSzGZx6_ZGD1lbjP",
            "https://drive.google.com/uc?export=view&id=1Kh0ei7bCcLMm0mgL7Mu4t2OHOPKsdTFp",
            "https://drive.google.com/uc?export=view&id=1Mn_bkJt1bZmq_ASvKGPFugaN_5ecOQCg",
            "https://drive.google.com/uc?export=view&id=1aBf9VsuxRDVAp9wcFEMOI00rPZyU0UEU",
            "https://drive.google.com/uc?export=view&id=1uFvPz81jGe8Z3dpoe2ClUR4LVxarhQNc",
            "https://drive.google.com/uc?export=view&id=1L-64dGWHt0Y9FZdZ4lyttZIJhhh-ee3q",
            "https://drive.google.com/uc?export=view&id=1RsFFiZ7jp2hzSwmHYps3glsHZa7-d45q",
            "https://drive.google.com/uc?export=view&id=1pXdkBJG8s8anqkFR469ValhQuOYMPyyg",
            "https://drive.google.com/uc?export=view&id=1eQYoBIDHlV-ZL0fXOHcpclK1VCWg_OA_",
            "https://drive.google.com/uc?export=view&id=1U0AmH4wtaygu3J_wj5R19RuP5jotM09B",
            "https://drive.google.com/uc?export=view&id=1LXgTDq6uHk6evF_WmFN_iZVz_zkY987D",
            "https://drive.google.com/uc?export=view&id=1LgfaoMwwQG7NNAGBqNe_z1cuP0OoNvsS",
            "https://drive.google.com/uc?export=view&id=1GueNEwzEjswnl-Ekc-bCjBkJbRusjMDP",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Tanjung Morawa",
                "alamat": "B2 no 2",
                "hobbi": "main volly bareng feby",
                "sosmed": "@jeremia_s_",
                "kesan": "Baik, Asik, pokoknya keren bang!",  
                "pesan":"Tetep jadi orang keren itu ya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "kalo badmood liat zaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "kakanya baik dan ramah ",  
                "pesan":"sukses selalu kak"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin Alat Pancing",
                "sosmed": "@gitrenishapg",
                "kesan": "baik, santai, ga banyak ngomong",  
                "pesan":"semoga hari harinya berjalan baik"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Wakatobi",
                "hobbi": "Bowling",
                "sosmed": "@ansftynn",
                "kesan": "kakanya asik dan enak diajak ngobrol",  
                "pesan":"semoga lancar semua urusannya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "baik, dan pinter banget si bang",  
                "pesan":"Semangat raih gelar cumlaude itu ya bang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Wai huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "kalem tapi asik pas diajak ngobrol",  
                "pesan":"semangat jadi atlet volly kakk"# 1
            },
             {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "abangnya seru, asik dan ternyata orang lambar juga",  
                "pesan":"jangan diliatin terus langitnya bang, nanti salting"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain Makanan Baru",
                "sosmed": "@myrrinn",
                "kesan": "terlihat keren dan berwibawa",  
                "pesan":"Terus semangat bang!"# 1
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "ngumpulin batu unik dipantai",
                "sosmed": "@berlyyanda",
                "kesan": "baik, asik, dan ramah",  
                "pesan":"semoga hari harinya menyenangkan ya kak"# 1
            },
             {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "20",
                "asal":"Teluk Mondawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "baik, auranya positif banget",  
                "pesan":"bahagia terus ya kak jangan galau galau"# 1
             },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "keren bang, gokill pokoknya",  
                "pesan":"semoga lancar terus urusannya bang"# 1
            },
             {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin ka wawa ngomong",
                "sosmed": "@fer_yulius",
                "kesan": "asik, baik dan seru banget",  
                "pesan":"semoga bisa selalu jadi pendengar yang baik buat kak wawa"# 1
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML hero semua franco",
                "sosmed": "@Monica_tjg",
                "kesan": "asik dan kece abiess",  
                "pesan":"jangan lupa makan ya kak, jangan ngegame terus"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@",
                "kesan": "keliatan baik, asik, dan seru abiess orangnya",  
                "pesan":"semoga makin sukses kedepannya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15WZU6uG8OmqmpkbShcZ95petjREXa0yi",
            "https://drive.google.com/uc?export=view&id=1UcKIETL4mqUOWZXeMQD90M_sY8QvMRgf",
            "https://drive.google.com/uc?export=view&id=1UL-UBp_og4uzCnmdhTQ-IYC3FiYwi7Y7",
            "https://drive.google.com/uc?export=view&id=1FfKJZVEmcceQk4FeXHcZIWVjWMd-jnF9",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "keren banget bang, orang tersibuk dan si duta panitia",  
                "pesan":"organisasi itu penting, tapi jangan lupa makan bang "# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjanani",
                "kesan": "keren banget kak, gokill",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Denger musik sambil jalan",
                "sosmed": "@fathinahazzh",
                "kesan": "baik, asik deh pokoknya",  
                "pesan":"bahagia selalu ya kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main",
                "sosmed": "@lia.h_264",
                "kesan": "keren banget kakk",  
                "pesan":"semangat terus kak, perjalanan masih panjang"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LzRGbQPcMtpeniqjFXmL2GbA03U29AlJ",
            "https://drive.google.com/uc?export=view&id=1-2dBE-cq8pUfi0ew-CzIb4CAJ8H6wwoA",
            "https://drive.google.com/uc?export=view&id=1io6ZiKUfqpzKrSP9zeMLY4OwndWEK_rG",
            "https://drive.google.com/uc?export=view&id=1rOxskZBzL1jH1_93vQWnYjO4jkPxdIIH",
            "https://drive.google.com/uc?export=view&id=1AExo4htbVuS57XkF8ZpED1DRLjC7Uq5J",
            "https://drive.google.com/uc?export=view&id=13KyovzUuavbXUsHFfsOtwwVouRg9_ncW",
            "https://drive.google.com/uc?export=view&id=126m8N9qzWKMC24FLTkKieOt9e7_DVnxP",
            "https://drive.google.com/uc?export=view&id=1Ti4GoaNm-cvWI-g-mNqDX1jeh4n_pnWM",
            "https://drive.google.com/uc?export=view&id=1MZgTw1jP04Uz0AR4ICsCslOdRlrz3ayd",
            "https://drive.google.com/uc?export=view&id=1xVXSnwM_rAzFh4yizT66Gk7DKXCi3Dmm",
            "https://drive.google.com/uc?export=view&id=1zneCteiHkOvVU4GQ5SIOi9SQgqRXYR70",
            "https://drive.google.com/uc?export=view&id=18Tqm3Py_A4HQx02aRqrGuiayU0foWnPT",
            "https://drive.google.com/uc?export=view&id=1OD_ERut1J_ceVgL2JtfNCU6vSfA8c_nK",
            "https://drive.google.com/uc?export=view&id=1xPosgWAoIpMYx28gz03lnYEuoaNNZk1O",
            "https://drive.google.com/uc?export=view&id=18Ods65GC5V24zo618FYF_zA9w22ajPZ7",
            "https://drive.google.com/uc?export=view&id=1XNIx65AJR-5sPirrHccYI2WMQekezpAR",
            "https://drive.google.com/uc?export=view&id=1wyTtaVr9l91nMERAc2fmFSEMiWOaSWJu",
            "https://drive.google.com/uc?export=view&id=1DIXM8v02H_VWRgFDJycNErQFOWrzeX4z",
            "https://drive.google.com/uc?export=view&id=1DIXM8v02H_VWRgFDJycNErQFOWrzeX4z",
            "https://drive.google.com/uc?export=view&id=1PKhV2DtfrptGOtk0NUmFXoZ_Z5yT-if7",
            "https://drive.google.com/uc?export=view&id=14uh56JWZ_KHTm4XKl9Fyscp5pZ0HVfhS",
            "https://drive.google.com/uc?export=view&id=1lnNLS2ZavMtuQ6AkGYodCsiX8YCJFVqJ",
            "https://drive.google.com/uc?export=view&id=1CuWLeIPbaiJ70iX7guXRtS4FQ4LD5-E2",
            "https://drive.google.com/uc?export=view&id=1cnXZZzWGJFHVzuAMb4UtwjhiPEet6Bqq",
            "https://drive.google.com/uc?export=view&id=1CLVDTlGF57lK_UcQ_ZV7706SVCTPTcbr",
            "https://drive.google.com/uc?export=view&id=17BpymfKCAmYbPB2j46jN_c0YbPa9wfY8",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Keren banget bang",  
                "pesan":"Semangat ngejalanin harinya bang"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "lucu,asik dan kece banget kak",  
                "pesan":"semangat jadi sekre kak"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main apapun",
                "sosmed": "@allyapasha_",
                "kesan": "Baik, keren banget kak, gokill",  
                "pesan":"makasih udah sabar banget ngadepin kami, jangan lupa istirahat kak"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "kontrakan GH",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky",
                "kesan": "keren banget bang, panutan banyak orang",  
                "pesan":"semangat bang bawa nama data ke ranah yang lebih besar"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Samping kost daffa",
                "hobbi": "Main Sudoku",
                "sosmed": "@arientakhsnl",
                "kesan": "keren banget kak",  
                "pesan":"tetep jadi contoh keren untuk kami kak"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jailin putri",
                "sosmed": "@daffahdynn_",
                "kesan": "keren banget bang, gokill abis ",  
                "pesan":"semangat dan keren selalu bang "# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_nrp",
                "kesan": "kece banget bang",
                "pesan": "semangat kuliahnya bang"  # 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"pasar muara beliti",
                "alamat": "kost putri, gerbang barat samping sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "baik, asik, dan seru banget kak",  
                "pesan":"jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Urip",
                "alamat": "Belwis",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "abang cool yang jago ngoding",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma fam",
                "hobbi": "ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "Tegas tapi baik banget",  
                "pesan":"semoga harinya berjalan baik ya bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "maju jaya kost",
                "hobbi": "yapping sampe bete",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Baik, asik, dan seru abiez kak",  
                "pesan":"semangat terus kak ngejalanin hari"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Lari",
                "sosmed": "@sahid22_",
                "kesan": "kece banget bang",  
                "pesan":"semangat bang, jangan nyerah"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "nangka 4, sukarame",
                "hobbi": "Main game + kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya baik, santai",  
                "pesan":"jaga kesehatan bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "lucu, asik, baik, seru abiezz, mentor paling gokill",  
                "pesan":"jaga kesehatan ya kak, semangat jangan lupa makan!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "baik dan keren banget kakk",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kaka ini baik dan santai",  
                "pesan":"sukses selalu kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul9",
                "kesan": "asik dan baik banget",  
                "pesan":"jangan lupa istirahat bang"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "keren banget bang, gokill",  
                "pesan":"sukses dan bahagia selalu bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.lapas raya no 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "kakanya asik dan seru",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Bikin project, ngoleksi data",
                "sosmed": "@ihsan.myusuf",
                "kesan": "keren, asik, kece banget bang",  
                "pesan":"jangan lupa istirahat bang"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Padang Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "serem tapi asik, keren banget bang",
                "pesan": "semangat selalu bang"  # 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakanya asik dan juga santai",  
                "pesan":"semoga harinya bahagia"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Lempar Batu",
                "sosmed": "@m.ridwan_22",
                "kesan": "baik, seru, dan asik banget bang",  
                "pesan":"semangatnya jangan sampe pudar ya bang"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "baik, humoris, asik",  
                "pesan":"jangan lupa istirahat bang"# 1
            },
            {
                "nama": "Uliano Wiliam Purba ",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main musik, ngoding, menanam anggrek",
                "sosmed": "@nano.wlm",
                "kesan": "serius tapi lucu juga",  
                "pesan":"bahagia selalu bang"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Bengong",
                "sosmed": "@rewinanaaa",
                "kesan": "baik, santai, dan seru",  
                "pesan":"selalu jaga kesehatan kak"# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZNI54EABQuN4hlnX8jPwBZYeGYe-eSdz",
            "https://drive.google.com/uc?export=view&id=1KfEFN45bvETHlrg1a4D1cLOONgGQRWPp",
            "https://drive.google.com/uc?export=view&id=1fQMMiCAX8sNAmR3f5uf4vCb_ugOCGT2E",    
            "https://drive.google.com/uc?export=view&id=1FUVWP-tUSIvHAVtQYG-C2cuQUb1bKL73",
            "https://drive.google.com/uc?export=view&id=1iB05mCp1GlOcDxx60L6KOzczZ63YZ9aM",
            "https://drive.google.com/uc?export=view&id=1cJg6ZlXPZztmUmS3qHq_c_iEXCIJ8ms5",
            "https://drive.google.com/uc?export=view&id=1K_CLh9rD3C2iNYNR-2vKTPtDFvY6_D2s",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1cksTQ2tLDjNFvGrykkz05KfjapzHZUcb",
            "https://drive.google.com/uc?export=view&id=1BfB80QhkIcjgZTilutxQ7gp6gLFDfr2C",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1cFRFQElbbiCIr_qNp5S7jZLp7Q-Lt6LS",
            "https://drive.google.com/uc?export=view&id=17kBJFaY0PLsGOOmSl41X12gRHuMkcPoi",
            "https://drive.google.com/uc?export=view&id=1WVLk61jO4bPrf7pNXfqSeDncnVeIVw43",
            "https://drive.google.com/uc?export=view&id=1549xfhJxfZoCxGZG-9x4zL-RpTyObxZy",
            "https://drive.google.com/uc?export=view&id=1wx6DNOP8SlWSxChhJEB_4ND7RFUXSk_s",
            "https://drive.google.com/uc?export=view&id=1NA_oTHs7MFsqj8hIz8gofZLs0Z1jGygl",
            "https://drive.google.com/uc?export=view&id=11ZguLm7C3jSu1r1N_57iW_q27sTXUx2b",
            "https://drive.google.com/uc?export=view&id=1HcpXGyzv2eBeFEBvrxKc0VaGrPV3dO7r",
            "https://drive.google.com/uc?export=view&id=11hDAeB6vmRdbcH6JeF1rYfu-_aMDBa2o",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1txDW9_Av70lDetUPF1mqqqtHOlSnhPKj",
            
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
                "kesan": "Asik dan seru untuk diajak diskusi",
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@junitaa.0406",
                "kesan": "Kakaknya asik, baik, suka sharing ilmu",  
                "pesan":"Selalu jaga kesehatan ya kak"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Keren banget bang + abang asuh di TPB paling gokil",  
                "pesan":"Semangat nyusun TA ya bang"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakanya baik, seru diajak ngobrol",
                "pesan":"Jangan lupa makan ya kak"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Keren banget bang, akhirnya ketemu abang nim",
                "pesan":"Semangat jadi abas bang" 
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tj. Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya baik, santai orangnya",
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "jl. Manggis 1",
                "hobbi": "Nonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "kakanya baik, kalem juga",  
                "pesan":"semoga harinya selalu menyenangkan ya kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "kakanya baik, asik, bawaannya ceria terus",
                "pesan":"semangat kuliahnya ya kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abangnya baik, asik, santai",
                "pesan":"selalu keren bang"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakanya baik banget, seru juga",
                "pesan":"Semangat Ngedrakor kak"    
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jl. Raden Saleh",
                "hobbi": "jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Seru banget, baik, asik",
                "pesan":"semangat terus kak kuliahnya"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan Bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "kakanya baik, kalem",  
                "pesan":"semangat terus ya kak, selalu jaga kesehatan"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kedepannya kak!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama ITERA TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Aura codingannya kuat banget bang",
                "pesan":"Tetap semangat jangan menyerah"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Keren banget bang, asik abiezz",
                "pesan":"semangat terus bang kuliahnya"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya pinter, kalem, seru",
                "pesan":"Selalu jaga kesehatan ya bang"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"semangat terus kuliahnya Kak!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik, baik, seru diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kak, jangan bosen liat embung ya kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Baik, asik banget bang",
                "pesan":"Semangat Futsalnya bang"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()
       

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xV9X0htFnwooK_4U5NXPVA1fM0axncOx",
            "https://drive.google.com/uc?export=view&id=130v_FlS3kIfcBaL3W0oTK6QEBLaNKgSK",
            "https://drive.google.com/uc?export=view&id=1ZEl41yOCcfU0DslJwcBaeyNOWl0jkL0A",
            "https://drive.google.com/uc?export=view&id=17iCKS8OGQzQ08xwD5i2viQ6K1UEMyyp4",
            "https://drive.google.com/uc?export=view&id=1Z8UppkQlt2qFS267swRHjbH222UU2N8G",
            "https://drive.google.com/uc?export=view&id=1oPWpRPKGDXP-MGVxu509GKwEurdF-sRA",
            "https://drive.google.com/uc?export=view&id=1viHakxRak0ghxjqK5i60P9BdfaYg76W1",
            "https://drive.google.com/uc?export=view&id=14wFDy8kAzLpb24AVL92fM68YmgRqOdab",
            "https://drive.google.com/uc?export=view&id=1DKdlVWf_j8DoJQiuaCQp2EqpeE70WORj",
            "https://drive.google.com/uc?export=view&id=1zxRwpPFCSEaLZTso_VVCU_R-hNp9guXH",
            "https://drive.google.com/uc?export=view&id=1k1DdfQmTbWfNE-UElCu5FhB4nwPbk3Ru",
            "https://drive.google.com/uc?export=view&id=1oi76zR2OPEFlX4DqypKOFJnGGw1XCES6",
            "https://drive.google.com/uc?export=view&id=15laT8thaL2NbR6HWK0E2H_pSGC_R6-Ke",
            "https://drive.google.com/uc?export=view&id=1oVyl3buBBJd8XTHF8Bz9G8xCJl8zJwL-",
            #habis bang desman
            "https://drive.google.com/uc?export=view&id=1Ega5v6JHC0Pga8vSBm4q2__tiHaApVqg",
            "https://drive.google.com/uc?export=view&id=1AHLxCD__eXNjB3fQbIFaoncjXGFDYiYl",
            "https://drive.google.com/uc?export=view&id=1P03WBfJVBDfAZ4nfuyxcEexD6tNip0mK",
            "https://drive.google.com/uc?export=view&id=1ebBP124Wh08KkD9TuwXS4FzstyYv4BaP",
            "https://drive.google.com/uc?export=view&id=1NCWu7l7CsjDYbEib8jL4wTjAyc1jmWWI",
            "https://drive.google.com/uc?export=view&id=13ut6iqEb9dN9bbwBV7dZ_zgtZHIAqCf9",
            "https://drive.google.com/uc?export=view&id=1QMX31h-WqQvIsc5bQsY_5MBeAOEm4Dz2",
            "https://drive.google.com/uc?export=view&id=1hKrsb5v0zH3MCJww2f1FvLVL-WDLJxEm",
            "https://drive.google.com/uc?export=view&id=1612vj1gLx2s_ttnGAm40Fe6KfqWqoRPs",
            "https://drive.google.com/uc?export=view&id=1B7QjHZnAXt9oVM2pRLBqqRCGnBJTig5O",
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
                "kesan": "keren banget bang, asik poll",
                "pesan":"Semangat terus untuk kuliahnya ya bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Baik dan asik banget kak",
                "pesan":"Sukses selalu kak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "kakanya baik, baik, ramah juga",
                "pesan":"Semangat terus untuk kuliahnya kak!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "kakanya asik dan seru banget",
                "pesan":"Tetep semangat ngejalanin harinya kak"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya asik, ramah juga",
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "lucu, asik, baik, seru abiezz",
                "pesan":"semangat kuliahnya, jangan lupa tidur"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakanya asik, seru diajak ngobrol",
                "pesan":"Sukses selalu untuk kedepannya kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakanya keren banget",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya Kak"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abangnya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya asik dan seru",
                "pesan":"Selalu jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "kakanya baik, asik",
                "pesan":"Semoga harinya selalu berjalan baik ya kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya lucu, asik, dan keren banget",
                "pesan":"Semangat terus bang jalanin hari"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "kakanya asik dan seru diajak ngobrol",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya Kak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik, ramah, asik",
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya asik dan keren banget bang",
                "pesan":"Selalu jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kakanya asik dan baik banget",
                "pesan":"Sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak sangat baik dan sabar juga",
                "pesan":"Jangan lupa jaga kesehatan ya kak."# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya asik dan seru untuk diajak ngobrol",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakanya baik, bawaannya ceria terus",
                "pesan":"Semangat ngejalanin hari kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya asik, ramah juga",
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Baik, asik dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak."# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1g3Gz6UNpJuzMe3-WJYUAkvD4SbkdGy5f",
            "https://drive.google.com/uc?export=view&id=1BSjHBjowvfnahTgBW5bvShecR4ZGDx8j",
            "https://drive.google.com/uc?export=view&id=1pd1w0VH3mUbq0lEU3X-02C2IvjAx7203",
            "https://drive.google.com/uc?export=view&id=1GAiEFjikZ19qyOMTfnLeZvnrOkdwjjn3",
            "https://drive.google.com/uc?export=view&id=1ftwY2hiDi_m1XaJks1qtD4TQXN9E250r",
            "https://drive.google.com/uc?export=view&id=1mfrhBC9yeDfVt_g7fKEngvE0SDf-Zeqb",
            "https://drive.google.com/uc?export=view&id=1jJx2TxyylY8T-uvt_BtPe5bILP8ESFlv",
            "https://drive.google.com/uc?export=view&id=1h4Dc7fxxe-UJKg4pG50lEbSKCzsbxIW5",
            "https://drive.google.com/uc?export=view&id=1I-oQIQCl1GS2orZs4fy5PM9SqcIUXIjo",
            "https://drive.google.com/uc?export=view&id=1yO0Gz_bi92HuAR3Bhale-BvQ-igY7mgG",
            "https://drive.google.com/uc?export=view&id=1g9qPtfDgxXovCJwZDr2RAqBuzQtB_WrV",
            "https://drive.google.com/uc?export=view&id=1qidHoHkpt9lvixvBw0-JbqBt4k6LhxOv",
            "https://drive.google.com/uc?export=view&id=1GfSTk0a-gVS8QuJY1gcXP6NxQIHDsVR1",
            "https://drive.google.com/uc?export=view&id=1pd1w0VH3mUbq0lEU3X-02C2IvjAx7203",
            "https://drive.google.com/uc?export=view&id=12cHiJZdByod3DLHPCxAEl7jonBjSRl6Y",    
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik banget dan ramah.",
                "pesan": "Sehat dan semangat terus ya kak!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Semoga urusan kuliahnya lancar selalu, Kak"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Senang bisa kenal sama kakak.",
                "pesan": "Sukses terus buat ke depannya ya Kak!"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya ramah banget.",
                "pesan": "Sehat dan bahagia selalu kak!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya baik, seru dan asik",
                "pesan": "Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asik banget.",
                "pesan": "Sehat selalu ya kak!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "kakanya baik dan positif vibes banget kak.",
                "pesan": "Selalu semangat ya kak!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalghani73",
                "kesan": "Abangnya asik, baik, ramah",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya baik dan asik banget",
                "pesan": "semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya humble dan asik diajak ngobrol",
                "pesan": "Selalu jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik, asik dan friendly banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya baik dan seru.",
                "pesan": "Semangat terus kak!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semoga urusannya dipermudah selalu bang"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya asik untuk diajak diskusi.",
                "pesan": "Lancar-lancar ya kak kuliahnya."# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Rubik Mirror",
                "sosmed": "@zhrptsl",
                "kesan": "kakanya asik dan seru",  
                "pesan":"semangat terus kuliahnya kak"# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tOU3OinLqrbHtxsPM12VB-xtoGZIhzx7",
            "https://drive.google.com/uc?export=view&id=1G9zd_TM3DZD_CZ_UeXlbG1G8x5VLkuJs",
            "https://drive.google.com/uc?export=view&id=1S2f0leEw4MNF3Unk2u3e3h5TnAqEEDMz",
            
            "https://drive.google.com/uc?export=view&id=11QTMWusOYf8nNLJhfvfn2mSXChbDBTFy",
            
            "https://drive.google.com/uc?export=view&id=1qt7tWxyLdJNQJmkU9gCcZdFOCqkaG5_C",
            "https://drive.google.com/uc?export=view&id=1k2n5vJC13_Q4mEZxwGQ52b2dNck-KiAy",
            "https://drive.google.com/uc?export=view&id=1iYH4NbEhPsrSu_Nn5PxKS4jnwuCBFOHW",
            "https://drive.google.com/uc?export=view&id=11RlqRS7WO_GYUjIUlgTdnJzSM56Vtm8r",
            "https://drive.google.com/uc?export=view&id=1Osnb8KMzrdYFSnrEBAn_K2LZgksgw1Yf",
            "https://drive.google.com/uc?export=view&id=1wRxPX50Ijc_280zUDZmL7H3qwYjKEKr3",
            "https://drive.google.com/uc?export=view&id=1TQU_aKkGIgr8IDKDscbhpEAKwzVu-JMu",
            
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya asik dan seru.",
                "pesan": "Semangat terus bang"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Senang bisa berkenalan dengan kakak.",
                "pesan": "Semoga sukses selalu kuliahnya!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya ramah dan baik.",
                "pesan": "Sehat selalu ya, bang."# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif.",
                "pesan": "Semangat terus kuliahnya, kak!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "Semoga semua urusannya dilancarkan."# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Semangat terus ya, kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya asik dan menyenangkan",
                "pesan": "jaga kesehatan selalu ya bang"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya kak!"# 1
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu ya kak!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Jaga kesehatan selalu kak!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakanya baik, asik dan menyenangkan",
                "pesan": "Semangat dan sukses selalu!"# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RZcvQr51wJkn1r0Y4PqdTWXb5ZuDjw-g",
            "https://drive.google.com/uc?export=view&id=1yZ-7iYu0OIXV9jzeAHznzffpRdMclV79",
            "https://drive.google.com/uc?export=view&id=14DbKY2Bh2m2D5HB9kGUn5-5rAgn1xMXL",
            "https://drive.google.com/uc?export=view&id=1fwUvJY0SRFJsrrG6h6cbiFUxpgTfMALg",
            "https://drive.google.com/uc?export=view&id=1mwQb3Ez_rdC8JQ0J1dvrAL43BOHG0JKD",
            "https://drive.google.com/uc?export=view&id=1NF8rfwfi074IWilOanZ0mHBHOgi3q2c1",
            "https://drive.google.com/uc?export=view&id=1k9okvp7STwBQT_GvtQo7wC_xtZAMrdrF",
            "https://drive.google.com/uc?export=view&id=1S1rzLhYNv8y_E6xzzfxOqIR-haaa71PR",
            "https://drive.google.com/uc?export=view&id=1xNVpCva2_15cxSZgBdADGlxrW6K5tVo5",
            "https://drive.google.com/uc?export=view&id=1RgGF1Lp70jbYYcZh-KufbX5mF5ScrZoP",
            "https://drive.google.com/uc?export=view&id=1qiajIe_zQjMsdc3yLYuHV_2bvRRAE_6V",
            "https://drive.google.com/uc?export=view&id=1A8wERdlR2eMjkSPJu8k6AXUATo7LLDOt",
            "https://drive.google.com/uc?export=view&id=1-FIZvQ5ktn0gnjJsBQxHafTH3lZdCrra",
            "https://drive.google.com/uc?export=view&id=1z3gXp8apVRNlaLTk91yuCmc-kg55iFQz",
            "https://drive.google.com/uc?export=view&id=1RCVEsOixJqkb8Npz0Z3bM9WWh-mLb3Pt",
            "https://drive.google.com/uc?export=view&id=11WPBLONFwp0wh2QLam2ryU07PQ2yzHMN",
            "https://drive.google.com/uc?export=view&id=1_xU-odRLqCRNnKqUZww_Gx08t-TwWlMi",
            "https://drive.google.com/uc?export=view&id=1XRAxKtpvdtZ9nWYtjyJNp6JkrR1pqHoY",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Sukses selalu ya, kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Belajar sama kakaknya jadi menyenangkan",
                "pesan": "Semoga lancar terus kuliahnya!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Pengalamannya keren dan menginspirasi",
                "pesan": "Teruslah berkarya bang"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abangnya friendly dan asik",
                "pesan": "Sehat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya asik dan seru",
                "pesan": "Semoga sehat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Senang bisa belajar bareng kakak",
                "pesan": "Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya sangat ramah dan baik",
                "pesan": "Tetap semangat kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "kakanya lucu dan baik banget",
                "pesan": "Semangat terus kak, jangan menyerah!"# 1
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Terima kasih sudah berbagi ilmu",
                "pesan": "Semoga sukses di masa depan!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya asik diajak diskusi",
                "pesan": "Lancar terus ya kak kuliahnya!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget",
                "pesan": "Sukses untuk ke depannya, kak!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya seru dan pintar",
                "pesan": "Sukses terus untuk karirnya nanti."# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Sangat berkesan bisa diajar kakak",
                "pesan": "Semoga sehat selalu, kak."# 1
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Orangnya asik dan mudah bergaul",
                "pesan": "Semangat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya sangat welcome dan ramah",
                "pesan": "Semangat terus dan semoga sukses!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Suasananya jadi asik kalau ada kakak ini",
                "pesan": "Jangan lupa jaga kesehatan ya, kak."# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya keren dan inspiratif",
                "pesan": "Semoga apa yang dicita-citakan tercapai."# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya ramah dan humble",
                "pesan": "Selalu jaga kesehatan ya kak."# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
# Tambahkan menu lainnya sesuai kebutuhan

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
            "https://drive.google.com/uc?export=view&id=1G1to2u33zswQ4UHA7-J0m5wOh1KNyxhP",
            "https://drive.google.com/uc?export=view&id=1UrAwXfGcHfpYDa_CKeSggwDpG9C1xVrZ",
            "https://drive.google.com/uc?export=view&id=1j3P20Pc3UgCB4pa9oV8wnhUQMxQ8h5DA",
            "https://drive.google.com/uc?export=view&id=1es3GgWsthe_KrbvRwdbxDjxXsqgpEymh",
            "https://drive.google.com/uc?export=view&id=15A1aHauWaqoZr9mWum97w1rg1uE6Gs-2",
            "https://drive.google.com/uc?export=view&id=18CoDoIWaZFtKUFpBXyKAzLw5lWV3VdTK",
            
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau Damar",
                "hobbi": "Ikut lomba burung murai",
                "sosmed": "@_erendraa",
                "kesan": "Keren, asik dan pastinya inspiratif",  
                "pesan":"Tetep jadi panutan yang chill ya bang!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren banget bang sampe nembus layar",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Ayres kost",
                "hobbi": "Jajan",
                "sosmed": "@celisabethh_",
                "kesan": "kakanya asik, bawaannya ceria terus",  
                "pesan":"bahagia selalu kak"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakanya jarang ngomong tapi vibesnya adem",  
                "pesan":"sehat selalu ya kak"# 1
            },
            {
                "nama": "Eksanty F Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Kelagian Kecil, Pahawang",
                "alamat": "Pesawaran",
                "hobbi": "Ngambilin Lanyard",
                "sosmed": "@eksantyfebriana",
                "kesan": "asik dan ga bikin canggung",  
                "pesan":"Bahagia dan sukses selalu kak"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Gya kost",
                "hobbi": "Cute",
                "sosmed": "@farahanumafifahh",
                "kesan": "asik, seru dan ga banyak ngomong juga",  
                "pesan":" semangat kak, jangan lupa istirahat"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FqzgqZ56_6SE34D48PbOeIpU_FSw9weJ",
            "https://drive.google.com/uc?export=view&id=1oL-zeRzcLMGZXpcNJZtI7Da9mSTzx2Tk",
            "https://drive.google.com/uc?export=view&id=1myTjFvqb3dlpP5WfhLNa2x-YpbRxYo-v",
            "https://drive.google.com/uc?export=view&id=1fkq0mXJQL861iMIKAiunBmptBCtJAbdI",
            "https://drive.google.com/uc?export=view&id=1OBNBCPmD17HFISSOA3HBuWsQjyqMVK1_",
            "https://drive.google.com/uc?export=view&id=1G9x0Hd0xG6IGle8b9u0ZvTHVDLyEd_x2",
            "https://drive.google.com/uc?export=view&id=1fBwkNx21sHIObSmzXCDUT8SHospPPiNt",
            "https://drive.google.com/uc?export=view&id=1vz6LIec_1pAkMcvJFISNQ4__eF81iGjA",
            "https://drive.google.com/uc?export=view&id=1NkgrBz8hZImKQ4zk5aJ21a8SDh6VtK1t",
            "https://drive.google.com/uc?export=view&id=1ehqxczXJL39SBn1pgiHLW0kSY2No2PlZ",
            "https://drive.google.com/uc?export=view&id=1UD06rF6LnawCibZu90ZZgpPHtCe77Vya",
            "https://drive.google.com/uc?export=view&id=1NjP1NVOHharDJmt-oXx79vRgXwOHffWf",
            "https://drive.google.com/uc?export=view&id=13K6rQqX5lWI7PkebF-JglITu6gi-zqPD",
            "https://drive.google.com/uc?export=view&id=14SraJv5R7VqEVpX84ESdxi3GOK6XZ4-U",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Tanjung Morawa",
                "alamat": "B2 no 2",
                "hobbi": "main volly bareng feby",
                "sosmed": "@jeremia_s_",
                "kesan": "Baik, Asik, pokoknya keren bang!",  
                "pesan":"Tetep jadi orang keren itu ya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "kalo badmood liat zaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "kakanya baik dan ramah ",  
                "pesan":"sukses selalu kak"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin Alat Pancing",
                "sosmed": "@renishapg",
                "kesan": "baik, santai, ga banyak ngomong",  
                "pesan":"semoga hari harinya berjalan baik"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Wakatobi",
                "hobbi": "Bowling",
                "sosmed": "@ansftynn",
                "kesan": "kakanya asik dan enak diajak ngobrol",  
                "pesan":"semoga lancar semua urusannya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "baik, dan pinter banget si bang",  
                "pesan":"Semangat raih gelar cumlaude itu ya bang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Wai huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "kalem tapi asik pas diajak ngobrol",  
                "pesan":"semangat jadi atlet volly kakk"# 1
            },
             {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "abangnya seru, asik dan ternyata orang lambar juga",  
                "pesan":"jangan diliatin terus langitnya bang, nanti salting"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain Makanan Baru",
                "sosmed": "@myrrinn",
                "kesan": "terlihat keren dan berwibawa",  
                "pesan":"Terus semangat bang!"# 1
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "ngumpulin batu unik dipantai",
                "sosmed": "@berlyyanda",
                "kesan": "baik, asik, dan ramah",  
                "pesan":"semoga hari harinya menyenangkan ya kak"# 1
            },
             {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "20",
                "asal":"Teluk Mondawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "baik, auranya positif banget",  
                "pesan":"bahagia terus ya kak jangan galau galau"# 1
             },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "keren bang, gokill pokoknya",  
                "pesan":"semoga lancar terus urusannya bang"# 1
            },
             {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin ka wawa ngomong",
                "sosmed": "@fer_yulius",
                "kesan": "asik, baik dan seru banget",  
                "pesan":"semoga bisa selalu jadi pendengar yang baik buat kak wawa"# 1
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML hero semua franco",
                "sosmed": "@Monica_tjg",
                "kesan": "asik dan kece abiess",  
                "pesan":"jangan lupa makan ya kak, jangan ngegame terus"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@",
                "kesan": "keliatan baik, asik, dan seru abiess orangnya",  
                "pesan":"semoga makin sukses kedepannya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JcDEG3mLFAhLfebBU2eVWg4Yc1m-hLuR",
            "https://drive.google.com/uc?export=view&id=1RzOq2sxc_5gBTgYCZVOTavjBC5tHtH2b",
            "https://drive.google.com/uc?export=view&id=1r-hj9mHvbb3qoP7cKfJ8MlqCn8eBSfWM",
            "https://drive.google.com/uc?export=view&id=10zBljQ-qQnV1TluEEpNKYXFWZco2PQBI",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "keren banget bang, orang tersibuk dan si duta panitia",  
                "pesan":"organisasi itu penting, tapi jangan lupa makan bang "# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjanani",
                "kesan": "keren banget kak, gokill",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Denger musik sambil jalan",
                "sosmed": "@fathinahazzh",
                "kesan": "baik, asik deh pokoknya",  
                "pesan":"bahagia selalu ya kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main",
                "sosmed": "@lia.h_264",
                "kesan": "keren banget kakk",  
                "pesan":"semangat terus kak, perjalanan masih panjang"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1whSOCnnS6mHpFvghRIQ08mbIpDgmMjZX",
            "https://drive.google.com/uc?export=view&id=1Ie3FolUOHaYMzJkmUKHyqsD8_BhxzHln",
            "https://drive.google.com/uc?export=view&id=1E4vbVfyfC6mywYm_ZEZOpAFAKbB1GLyt",
            "https://drive.google.com/uc?export=view&id=1J03zTy7QQHYi14MNPCLCmBmySMHFtV7_",
            "https://drive.google.com/uc?export=view&id=1s2EvKhESkCz8hMZNl255fl_z66hTszhT",
            "https://drive.google.com/uc?export=view&id=1kS0a-J81DpfqxN6kMGdEwjLpadqtqd6P",
            "https://drive.google.com/uc?export=view&id=1Mh9m7K0TrTZPg0odyOok8hZ_YlUMSudE",
            "https://drive.google.com/uc?export=view&id=1hFE90trP15rfDeyf6RkbEmyBsX-qTRpo",
            "https://drive.google.com/uc?export=view&id=1t6V4btJou0W-HAbhGNQTF_-kHWnG7FQK",
            "https://drive.google.com/uc?export=view&id=1_wcBcbW1T7ANIaBCcFRWOpdhXRhFgwlf",
            "https://drive.google.com/uc?export=view&id=1e-MPBTcxgE5ds3KBczLY6-4thr6aY01K",
            "https://drive.google.com/uc?export=view&id=1Xa-0QU6gs2D4vopX9hNGWHhizI2RWL-T",
            "https://drive.google.com/uc?export=view&id=112Co3crq8KGJC5wqJGIkfcS5VGAfmAFP",
            "https://drive.google.com/uc?export=view&id=18o1rJDOMTux5KUxo_H7o5AJU_0TrOGCJ",
            "https://drive.google.com/uc?export=view&id=1DjyL_LVjB7ib-y670gydGgMNq5gY1iBL",
            "https://drive.google.com/uc?export=view&id=1rRSX1Hw9DCQnGU_Iv22NNDSHtmnUqmd_",
            "https://drive.google.com/uc?export=view&id=14794rj1PCN70T48VAyLcC0MZOnZesEpZ",
            "https://drive.google.com/uc?export=view&id=1eqj5ZT1GtDFjPB6GCQdSKgrOoIUYhQSR",
            "https://drive.google.com/uc?export=view&id=1kF6P5oPnplr_O8kxQwt5uJtFAgBPxigy",
            "https://drive.google.com/uc?export=view&id=1wrkvILIj4sRj8Ol8npOvYgHhFzkV9qZZ",
            "https://drive.google.com/uc?export=view&id=16YlW__r_trCbn0lhDoVx2mdj9aGf7OzX",
            "https://drive.google.com/uc?export=view&id=1CnaxtRTZ7d8HPDfNu9lPiqlN3ow9SCw7",
            "https://drive.google.com/uc?export=view&id=1mxUxSL5CyvJ6rV3eLCuqBlKC46AhZsai",
            "https://drive.google.com/uc?export=view&id=1xUXBKSJt78iCidTPAn_slP6mLdN9V9OW",
            "https://drive.google.com/uc?export=view&id=1UFeY0yTJbNERAYVDs5lx62zgpDWmfZza",
            "https://drive.google.com/uc?export=view&id=1O1kgMVYTL-Iu53LIcSjZMgsOPSLxgt7c",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Keren banget bang",  
                "pesan":"Semangat ngejalanin harinya bang"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "lucu,asik dan kece banget kak",  
                "pesan":"semangat jadi sekre kak"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main apapun",
                "sosmed": "@allyapasha_",
                "kesan": "Baik, keren banget kak, gokill",  
                "pesan":"makasih udah sabar banget ngadepin kami, jangan lupa istirahat kak"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "kontrakan GH",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky",
                "kesan": "keren banget bang, panutan banyak orang",  
                "pesan":"semangat bang bawa nama data ke ranah yang lebih besar"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Samping kost daffa",
                "hobbi": "Main Sudoku",
                "sosmed": "@arientakhsnl",
                "kesan": "keren banget kak",  
                "pesan":"tetep jadi contoh keren untuk kami kak"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jailin putri",
                "sosmed": "@daffahdynn_",
                "kesan": "keren banget bang, gokill abis ",  
                "pesan":"semangat dan keren selalu bang "# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_nrp",
                "kesan": "kece banget bang",
                "pesan": "semangat kuliahnya bang"  # 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"pasar muara beliti",
                "alamat": "kost putri, gerbang barat samping sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "baik, asik, dan seru banget kak",  
                "pesan":"jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Urip",
                "alamat": "Belwis",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "abang cool yang jago ngoding",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma fam",
                "hobbi": "ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "Tegas tapi baik banget",  
                "pesan":"semoga harinya berjalan baik ya bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "maju jaya kost",
                "hobbi": "yapping sampe bete",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Baik, asik, dan seru abiez kak",  
                "pesan":"semangat terus kak ngejalanin hari"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Lari",
                "sosmed": "@sahid22_",
                "kesan": "kece banget bang",  
                "pesan":"semangat bang, jangan nyerah"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "nangka 4, sukarame",
                "hobbi": "Main game + kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya baik, santai",  
                "pesan":"jaga kesehatan bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "lucu, asik, baik, seru abiezz, mentor paling gokill",  
                "pesan":"jaga kesehatan ya kak, semangat jangan lupa makan!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "baik dan keren banget kakk",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kaka ini baik dan santai",  
                "pesan":"sukses selalu kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul9",
                "kesan": "asik dan baik banget",  
                "pesan":"jangan lupa istirahat bang"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "keren banget bang, gokill",  
                "pesan":"sukses dan bahagia selalu bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.lapas raya no 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "kakanya asik dan seru",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Bikin project, ngoleksi data",
                "sosmed": "@ihsan.myusuf",
                "kesan": "keren, asik, kece banget bang",  
                "pesan":"jangan lupa istirahat bang"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Padang Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "serem tapi asik, keren banget bang",
                "pesan": "semangat selalu bang"  # 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakanya asik dan juga santai",  
                "pesan":"semoga harinya bahagia"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Lempar Batu",
                "sosmed": "@m.ridwan_22",
                "kesan": "baik, seru, dan asik banget bang",  
                "pesan":"semangatnya jangan sampe pudar ya bang"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "baik, humoris, asik",  
                "pesan":"jangan lupa istirahat bang"# 1
            },
            {
                "nama": "Uliano Wiliam Purba ",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main musik, ngoding, menanam anggrek",
                "sosmed": "@nano.wlm",
                "kesan": "serius tapi lucu juga",  
                "pesan":"bahagia selalu bang"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Bengong",
                "sosmed": "@rewinanaaa",
                "kesan": "baik, santai, dan seru",  
                "pesan":"selalu jaga kesehatan kak"# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XOlxkCYuO5mGi7QfLmbTwqe4sobZCbvj",
            "https://drive.google.com/uc?export=view&id=11_RDO01Qyf-MHGstITYnWs4k9eazq-tG",
            "https://drive.google.com/uc?export=view&id=1DAhGjzQUajKKpyiD9g-F0eDP_XjeoHN4",
            "https://drive.google.com/uc?export=view&id=1qwQDerl9YeVwZznqF1WQsJqQKVkaVDaR",
            "https://drive.google.com/uc?export=view&id=1rD3aNBWQsTU-47OU4UoaqCgWiJVrG3y7",
            "https://drive.google.com/uc?export=view&id=12Bk-b3G5S98kcQ6ljs9fdfhxcZviu2x4",
            "https://drive.google.com/uc?export=view&id=1r934m6F0pl6OgpNm65rI9X4DZrKpuT9P",
            "https://drive.google.com/uc?export=view&id=17HstD95Z45B16VlGf5_chUVbR737A0LD",
            "https://drive.google.com/uc?export=view&id=1ieLml9LtsA4_M13DFKbLh_QLYozvvbY7",
            "https://drive.google.com/uc?export=view&id=1Sh1wi819UNTrZVXCAgCCm99RLdZV5_Ng",
            "https://drive.google.com/uc?export=view&id=1BRxGSJ0WGE8Wx0sa07UOrNrq-eeuy_-Z",
            "https://drive.google.com/uc?export=view&id=1CX_u80R8yXYuQ--yfzpM8-CLj5yyEEdk",
            "https://drive.google.com/uc?export=view&id=1TaHKmF1TOrDpKcygJ2RsXvYQWXSuJyCZ",
            "https://drive.google.com/uc?export=view&id=1qYy8M0l7PCwnTKStbfhsQ-fGiCeIBE8-",
            "https://drive.google.com/uc?export=view&id=15W5jrOXTVu6OPDAaGhNSkuq4r6oXLVmw",
            "https://drive.google.com/uc?export=view&id=139CY1rASyCWJRHiX2w3S4DQJpqTVwTMW",
            "https://drive.google.com/uc?export=view&id=1TNJyPDdsck39kBxOW13gs0Ws8KVKdKmK",
            "https://drive.google.com/uc?export=view&id=1z6S3LxrjwtuXBz7XAs9VGgdzuXeUoRT0",
            "https://drive.google.com/uc?export=view&id=1tfw8vPH3ijUdfGNETdpO8HTC_BH_9Mxn",
            "https://drive.google.com/uc?export=view&id=1Hn9760Mglok-xeNJ3ZapsSqGkVv6lIqi",
            "https://drive.google.com/uc?export=view&id=1PdyoSzMmJPudJxytMqRXEQinr34sn7Gz",
            "https://drive.google.com/uc?export=view&id=1sUGhgPqxVOLRZ3g815heFz2iZkYO1jz-",
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
                "kesan": "Asik dan seru untuk diajak diskusi",
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@junitaa.0406",
                "kesan": "Kakaknya asik, baik, suka sharing ilmu",  
                "pesan":"Selalu jaga kesehatan ya kak"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Keren banget bang + abang asuh di TPB paling gokil",  
                "pesan":"Semangat nyusun TA ya bang"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakanya baik, seru diajak ngobrol",
                "pesan":"Jangan lupa makan ya kak"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Keren banget bang, akhirnya ketemu abang nim",
                "pesan":"Semangat jadi abas bang" 
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tj. Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya baik, santai orangnya",
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "jl. Manggis 1",
                "hobbi": "Nonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "kakanya baik, kalem juga",  
                "pesan":"semoga harinya selalu menyenangkan ya kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "kakanya baik, asik, bawaannya ceria terus",
                "pesan":"semangat kuliahnya ya kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abangnya baik, asik, santai",
                "pesan":"selalu keren bang"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakanya baik banget, seru juga",
                "pesan":"Semangat Ngedrakor kak"    
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jl. Raden Saleh",
                "hobbi": "jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Seru banget, baik, asik",
                "pesan":"semangat terus kak kuliahnya"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan Bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "kakanya baik, kalem",  
                "pesan":"semangat terus ya kak, selalu jaga kesehatan"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kedepannya kak!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama ITERA TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Aura codingannya kuat banget bang",
                "pesan":"Tetap semangat jangan menyerah"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Keren banget bang, asik abiezz",
                "pesan":"semangat terus bang kuliahnya"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya pinter, kalem, seru",
                "pesan":"Selalu jaga kesehatan ya bang"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"semangat terus kuliahnya Kak!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik, baik, seru diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kak, jangan bosen liat embung ya kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Baik, asik banget bang",
                "pesan":"Semangat Futsalnya bang"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()
       

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14j3Hz4B1hjwEsF9c4dQJdXVNnWqo65um",
            "https://drive.google.com/uc?export=view&id=1X_oCLST9_JkDxVTCbNAW-j-RXwCHMaIE",
            "https://drive.google.com/uc?export=view&id=1M36pn-5mHzyOMigQJaEoZddkrDoZotDZ",
            "https://drive.google.com/uc?export=view&id=1sEjwqNne-vLU3Qc_BZb38xEm4c_jCtlq",
            "https://drive.google.com/uc?export=view&id=1AMfCCpx-6BwNS7KEGQBD0Id7psCoqzTk",
            "https://drive.google.com/uc?export=view&id=1lRciryTben7oPWi0RwwVFUHrn9HBBgEz",
            "https://drive.google.com/uc?export=view&id=1kjkTSjJ2nDiQlXcgtV4wXok7Zzmzncvw",
            "https://drive.google.com/uc?export=view&id=1hmgAAv-81uj57Yu8fzUzpqsEg71PpEU2",
            "https://drive.google.com/uc?export=view&id=1GbQUWb6miiBj8kTWc5A7vnMsTTr99JdA",
            "https://drive.google.com/uc?export=view&id=1CsGWNjCN4tFjyHTSuiAX7mpvBfKLWZfO",
            "https://drive.google.com/uc?export=view&id=154YRJ4WzgXiEwAVv_9CFSPCZB_GHp3V5",
            "https://drive.google.com/uc?export=view&id=1hLcHeyfWEjxX7oJC58ueSSBhSd4udZtZ",
            "https://drive.google.com/uc?export=view&id=1s4e14Y9r617h_i4sqRWHUwOMMYUKJa_Q",
            "https://drive.google.com/uc?export=view&id=1qypaoCqirD6UrB4xmMsrk8xuQTPiKFbC",
            "https://drive.google.com/uc?export=view&id=1KcPWt1aHRXK68zUAgolJ0V6sdMFdGUHy",
            "https://drive.google.com/uc?export=view&id=1IXita2upy6igRGq7kNBv9nXmdpxQuWDe",
            "https://drive.google.com/uc?export=view&id=1k3EUA8kheaZAVs2gOrU87chCdBPLM3VA",
            "https://drive.google.com/uc?export=view&id=10mHiz_gNUyoOYxn0pTidhqpKyy76knb5",
            "https://drive.google.com/uc?export=view&id=1wNchYR58mer8dWr7AyRH2mrfwzJmsHMk",
            "https://drive.google.com/uc?export=view&id=1d3Tw2dhgTZY6iWClH8MZDmCsdgqgWR9u",
            "https://drive.google.com/uc?export=view&id=1-uFAttN9wrMW_dIkXoGhsO8b6GvKejd3",
            "https://drive.google.com/uc?export=view&id=1GswIhiwFSVxQpf4LAYKdoJ9VGqkR3Ssk",
            "https://drive.google.com/uc?export=view&id=15WPPnLij0fMLGOZ2ngqjTMgDgRqokVVQ",
            "https://drive.google.com/uc?export=view&id=1R7PCTJg1GZmgp8H88UrtQLIS81SSAHem",
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
                "kesan": "keren banget bang, asik poll",
                "pesan":"Semangat terus untuk kuliahnya ya bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Baik dan asik banget kak",
                "pesan":"Sukses selalu kak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "kakanya baik, baik, ramah juga",
                "pesan":"Semangat terus untuk kuliahnya kak!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "kakanya asik dan seru banget",
                "pesan":"Tetep semangat ngejalanin harinya kak"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya asik, ramah juga",
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "lucu, asik, baik, seru abiezz",
                "pesan":"semangat kuliahnya, jangan lupa tidur"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakanya asik, seru diajak ngobrol",
                "pesan":"Sukses selalu untuk kedepannya kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakanya keren banget",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya Kak"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abangnya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya asik dan seru",
                "pesan":"Selalu jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "kakanya baik, asik",
                "pesan":"Semoga harinya selalu berjalan baik ya kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya lucu, asik, dan keren banget",
                "pesan":"Semangat terus bang jalanin hari"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "kakanya asik dan seru diajak ngobrol",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya Kak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik, ramah, asik",
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya asik dan keren banget bang",
                "pesan":"Selalu jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kakanya asik dan baik banget",
                "pesan":"Sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak sangat baik dan sabar juga",
                "pesan":"Jangan lupa jaga kesehatan ya kak."# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya asik dan seru untuk diajak ngobrol",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakanya baik, bawaannya ceria terus",
                "pesan":"Semangat ngejalanin hari kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya asik, ramah juga",
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Baik, asik dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak."# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17es_-mWPXXaaClRzGvg7lqnBDG__TLBa",
            "https://drive.google.com/uc?export=view&id=1QwQ0ZsEvlA96qR2A77LKK3vYfDp1XYwY",
            "https://drive.google.com/uc?export=view&id=1kw4dYNXlexMo14ILmD398Q4xl37161nf",
            "https://drive.google.com/uc?export=view&id=1BbtFpAAX0XUyPtmkWRRKYNxSGl_933SM",
            "https://drive.google.com/uc?export=view&id=18obacBsaZ_8nU5besp5I-WyqDj_pTeZ2",
            "https://drive.google.com/uc?export=view&id=1HElQ5XYkKL5nnwvlDx-wriXrmZGwUfLt",
            "https://drive.google.com/uc?export=view&id=1Sb5bginH0lsUGFvNfTrOfXcjj8nrroB6",
            "https://drive.google.com/uc?export=view&id=1CPv2PEQT6r2H2NltH-oYMm1ousJ_CSpb",
            "https://drive.google.com/uc?export=view&id=10tPPRcWiX23HNaMEnEUdNyiOFLvD1FJw",
            "https://drive.google.com/uc?export=view&id=1wM2AQNhTlzxthAUE_CsiiSlyaJqu7GU1",
            "https://drive.google.com/uc?export=view&id=1MLR2c3ytR5QRnJaZVdelQTjAGucdhUXL",
            "https://drive.google.com/uc?export=view&id=1ckkXdM8_chOT8oEFS8EIi_mMoDTvKnTO",
            "https://drive.google.com/uc?export=view&id=1YFJ2EGFo-i-HwttudcDsGPN-Cf69Qx6l",
            "https://drive.google.com/uc?export=view&id=1HWBUeGfXC88HsFMO1t8NOabrSAw4mFlz",
            "https://drive.google.com/uc?export=view&id=1W_bLMB_2YM6QrM3rm-J28NampDRV7JT0",    
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik banget dan ramah.",
                "pesan": "Sehat dan semangat terus ya kak!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Semoga urusan kuliahnya lancar selalu, Kak"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Senang bisa kenal sama kakak.",
                "pesan": "Sukses terus buat ke depannya ya Kak!"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya ramah banget.",
                "pesan": "Sehat dan bahagia selalu kak!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya baik, seru dan asik",
                "pesan": "Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asik banget.",
                "pesan": "Sehat selalu ya kak!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "kakanya baik dan positif vibes banget kak.",
                "pesan": "Selalu semangat ya kak!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalghani73",
                "kesan": "Abangnya asik, baik, ramah",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya baik dan asik banget",
                "pesan": "semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya humble dan asik diajak ngobrol",
                "pesan": "Selalu jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik, asik dan friendly banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya baik dan seru.",
                "pesan": "Semangat terus kak!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semoga urusannya dipermudah selalu bang"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya asik untuk diajak diskusi.",
                "pesan": "Lancar-lancar ya kak kuliahnya."# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Rubik Mirror",
                "sosmed": "@zhrptsl",
                "kesan": "kakanya asik dan seru",  
                "pesan":"semangat terus kuliahnya kak"# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tOU3OinLqrbHtxsPM12VB-xtoGZIhzx7",
            "https://drive.google.com/uc?export=view&id=1G9zd_TM3DZD_CZ_UeXlbG1G8x5VLkuJs",
            "https://drive.google.com/uc?export=view&id=18ymsf68GVItGzy8WLGFm9xGK3SK0U4Zo",
            "https://drive.google.com/uc?export=view&id=11QTMWusOYf8nNLJhfvfn2mSXChbDBTFy",
            "https://drive.google.com/uc?export=view&id=1qt7tWxyLdJNQJmkU9gCcZdFOCqkaG5_C",
            "https://drive.google.com/uc?export=view&id=1k2n5vJC13_Q4mEZxwGQ52b2dNck-KiAy",
            "https://drive.google.com/uc?export=view&id=1iYH4NbEhPsrSu_Nn5PxKS4jnwuCBFOHW",
            "https://drive.google.com/uc?export=view&id=11RlqRS7WO_GYUjIUlgTdnJzSM56Vtm8r",
            "https://drive.google.com/uc?export=view&id=1Osnb8KMzrdYFSnrEBAn_K2LZgksgw1Yf",
            "https://drive.google.com/uc?export=view&id=1wRxPX50Ijc_280zUDZmL7H3qwYjKEKr3",
            "https://drive.google.com/uc?export=view&id=1TQU_aKkGIgr8IDKDscbhpEAKwzVu-JMu",
            
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya asik dan seru.",
                "pesan": "Semangat terus bang"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Senang bisa berkenalan dengan kakak.",
                "pesan": "Semoga sukses selalu kuliahnya!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya ramah dan baik.",
                "pesan": "Sehat selalu ya, bang."# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif.",
                "pesan": "Semangat terus kuliahnya, kak!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "Semoga semua urusannya dilancarkan."# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Semangat terus ya, kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya asik dan menyenangkan",
                "pesan": "jaga kesehatan selalu ya bang"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya kak!"# 1
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu ya kak!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Jaga kesehatan selalu kak!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakanya baik, asik dan menyenangkan",
                "pesan": "Semangat dan sukses selalu!"# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vXbKqV8LrsmPpm58Qgbgtj31pIbtDWth",
            "https://drive.google.com/uc?export=view&id=19S6ku1pbVb-4WPRn4Klp1uMS2xwczAvP",
            "https://drive.google.com/uc?export=view&id=1-DLrfqLoBrfswVnQBsy7xu2MYEbrORWq",
            "https://drive.google.com/uc?export=view&id=1bgPgOpLxcHiEJNQxl_DPODHhveVRsgAF",
            "https://drive.google.com/uc?export=view&id=16_rOXSf6pxEWFgGxm7v2LRPcUx1NEgtJ",
            "https://drive.google.com/uc?export=view&id=1fg2LAmcSE8dECcMQQttF4thzaby3CKfs",
            "https://drive.google.com/uc?export=view&id=1dNAXOV5LDz32IyJUnF4IR-sD941W4VK8",
            "https://drive.google.com/uc?export=view&id=1c3KdjPRBFy5XOQcdFJdIfg9V83NGAGC3",
            "https://drive.google.com/uc?export=view&id=1EYT3ycY5Dfw78buVWG1_cF3eIi09dTWN",
            "https://drive.google.com/uc?export=view&id=1Zwb0Rjx8ZZdFD7qXsHor1CQZBq8GNHch",
            "https://drive.google.com/uc?export=view&id=1a-i3C015P_IxP8Ry6YRwpXWFNvVbDERh",
            "https://drive.google.com/uc?export=view&id=1X84lC_E_c6tC51C9S5soRGR_WOXrdTh7",
            "https://drive.google.com/uc?export=view&id=14rOnnmqU8aAnGB6dZjwE5g5d0jUVfwGi",
            "https://drive.google.com/uc?export=view&id=1nhV2O16yOuuf6n47_a3VE08iAnHTnGI6",
            "https://drive.google.com/uc?export=view&id=17pjpq7tQSv6S17m6UwF6Zj2CQKuoIC_t",
            "https://drive.google.com/uc?export=view&id=1jgtEAWTOH0IZqTylI6dyHoLID5WQEVOm",
            "https://drive.google.com/uc?export=view&id=1i7I1lA6eqRBDClStxK-gAEuwTMGzs_uS",
            "https://drive.google.com/uc?export=view&id=1--uGYvFUeQE1xurs61TxnvQWjh4sUGYN",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Sukses selalu ya, kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Belajar sama kakaknya jadi menyenangkan",
                "pesan": "Semoga lancar terus kuliahnya!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Pengalamannya keren dan menginspirasi",
                "pesan": "Teruslah berkarya bang"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abangnya friendly dan asik",
                "pesan": "Sehat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya asik dan seru",
                "pesan": "Semoga sehat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Senang bisa belajar bareng kakak",
                "pesan": "Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya sangat ramah dan baik",
                "pesan": "Tetap semangat kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "kakanya lucu dan baik banget",
                "pesan": "Semangat terus kak, jangan menyerah!"# 1
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Terima kasih sudah berbagi ilmu",
                "pesan": "Semoga sukses di masa depan!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya asik diajak diskusi",
                "pesan": "Lancar terus ya kak kuliahnya!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget",
                "pesan": "Sukses untuk ke depannya, kak!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya seru dan pintar",
                "pesan": "Sukses terus untuk karirnya nanti."# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Sangat berkesan bisa diajar kakak",
                "pesan": "Semoga sehat selalu, kak."# 1
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Orangnya asik dan mudah bergaul",
                "pesan": "Semangat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya sangat welcome dan ramah",
                "pesan": "Semangat terus dan semoga sukses!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Suasananya jadi asik kalau ada kakak ini",
                "pesan": "Jangan lupa jaga kesehatan ya, kak."# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya keren dan inspiratif",
                "pesan": "Semoga apa yang dicita-citakan tercapai."# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya ramah dan humble",
                "pesan": "Selalu jaga kesehatan ya kak."# 1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
# Tambahkan menu lainnya sesuai kebutuhan


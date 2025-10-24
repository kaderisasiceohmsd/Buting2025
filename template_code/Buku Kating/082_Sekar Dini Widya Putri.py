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
            "https://drive.google.com/uc?export=view&id=16BXsmgmUL3SWlYN6GoMRcsXeQ-5JEoUG",
            "https://drive.google.com/uc?export=view&id=1i-MXWX6FJdn7htyVkHLcQ79sonEvTsaT",
            "https://drive.google.com/uc?export=view&id=1lnQ4Zx6Nx0otNgpkgtHzg3cLbdqXaGp3",
            "https://drive.google.com/uc?export=view&id=1APcqv5gQOz09mw76oD4WaGTMGs3pUimy",
            "https://drive.google.com/uc?export=view&id=1twVtDefEslYYD-91HWlZsWEpHl0xT31c",
            "https://drive.google.com/uc?export=view&id=18svFEml2LVNSYjd3MXrq6vKHBoYL3ruZ",
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
                "kesan": "Abang kahim keren banget.",  
                "pesan":"Lancar dan semangat terus ya bang kuliahnya."# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abang keren banget ngejelasin tentang organisasi dan himpunan.",  
                "pesan":"Semangat terus ya bang, dan jaga kesehatan."# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak lucu dan kocak banget.",  
                "pesan":"Semangat terus ya kak kuliahnhya."# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak cantik dan baik banget.",  
                "pesan":"Semoga lancar terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak baik dan asik banget.",  
                "pesan":"Lancar dan semangat terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak cantik dan keren banget.",  
                "pesan":"Semangat terus ya kak."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Mjc4PGUTEYeOWcrN-86DYAhcwJz-LdnW",
            "https://drive.google.com/uc?export=view&id=1bNOip7vt4nEM2PKttp9Pin9m4kkLB9mL",
            "https://drive.google.com/uc?export=view&id=1V0eZp6yK1TiOme7Yc6-hzatyGjQ0HmuP",
            "https://drive.google.com/uc?export=view&id=1q6hZkCccQ7JAtAEw4KjCS4ANkJzdokEY",
            "https://drive.google.com/uc?export=view&id=1P3hVBwNfNwFZQGrAApIec3FSf849Pzj4",
            "https://drive.google.com/uc?export=view&id=1GhDgYxqZiDBIP8QoxT-7ghr5othkSPk0",
            "https://drive.google.com/uc?export=view&id=1ybZi7n2XQtifYBTf-_1E0f04YDGoDcFQ",
            "https://drive.google.com/uc?export=view&id=1eRdkTPjM8hzLEIOxZfVi1XwVc2HnV0Vq",
            "https://drive.google.com/uc?export=view&id=1oGCZfZAk0YA0zh5IOKu9WqTs-CjltTdo",
            "https://drive.google.com/uc?export=view&id=1IYeclYurU-iFZQJKPzr_brwt2gbTz2AT",
            "https://drive.google.com/uc?export=view&id=139Hsv6ZGdLzM8_63bnhFLWFNF40sUjFQ",
            "https://drive.google.com/uc?export=view&id=1t8Ws1wfJFbvE1GXJ3-bgEAIYfvQa8HGF",
            "https://drive.google.com/uc?export=view&id=1z4FDCxWP5SrzSyBQ19pypDyFRy4MPhdE",
            "https://drive.google.com/uc?export=view&id=1IZXkNHL8zPe7jMwE2_qvm1lyM9j9esaP",
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
                "kesan": "Abang baik banget dan keren banget.",
                "pesan":"Sehat terus, dan semangat terus ya bang."
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak baik dan keren banget.",
                "pesan":"Lancar dan semangat terus ya kak kuliahnya."
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Kakak baik dan cantik.",
                "pesan":"Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak baik dan asik banget.",
                "pesan":"Lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Abang keren dan pinter banget.",
                "pesan":"Lancar dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak cantik dan baik banget.",
                "pesan":"Semangat terus ya kak."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Abang keren dan baik.",
                "pesan":"Semoga lancar terus ya bang kuliahnya."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Abang keren dan baik banget.",
                "pesan":"Sehat selalu, dan semangat terus ya bang."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak baik dan asik banget.",
                "pesan":"Semangat terus ya kak."
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakak keren dan baik banget.",
                "pesan":"Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang keren banget dan baik.",
                "pesan":"Lancar dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abang baik banget.",
                "pesan":"jaga kesehatan, dan semangat terus ya bang."
            },           
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak baik dan asik banget.",
                "pesan":"Semangat dan lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Kakak baik dan asik banget.",
                "pesan":"Semoga lancar terus ya kak kuliahnya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pDi_s1FXaMZKgwE2KUE-1IcSQrtRlfDO",
            "https://drive.google.com/uc?export=view&id=1K6gOlngK4wAIOJDL3Wa5znrLJPfmYXdM",
            "https://drive.google.com/uc?export=view&id=1YiT_FL4efnVOs4NOy26LiW8VGdkAVMLv",
            "https://drive.google.com/uc?export=view&id=11qmWw4gO2_2guIZeIOBJYwBTcifn1WDb",
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
                "kesan": "Bang bintang keren banget.",  
                "pesan":"Semangat terus kuliahnya bang."# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakak cantik, baik.",  
                "pesan":"Semangat terus kuliahnya kak."# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak pinter banget.",  
                "pesan":"Semoga lancar terus kuliahnya kak."# 1
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak lucu, baik.",  
                "pesan":"Semoga lancar terus kak kuliahnya."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Sj0JH4L3KKihJeeQEtf5VoJzmYS8jjTq",
            "https://drive.google.com/uc?export=view&id=1oIw3wetRuiDW2OneLL8HEJK-spEjjVIR",
            "https://drive.google.com/uc?export=view&id=1ieCfjPMlu9Vl5H7uLVbJcTFS_HUnPUbO",
            "https://drive.google.com/uc?export=view&id=1OdOa1znhU-OaiMPVtbSjy8ZoYNUgOXT0",
            "https://drive.google.com/uc?export=view&id=14vzXV30ifOppdoAZw5irnlv0upVQiDXT",
            "https://drive.google.com/uc?export=view&id=1d_2yBa22Qxv0Ea7dcygpchQnu6o6p2xC",
            "https://drive.google.com/uc?export=view&id=1As8eyCA1H2A2haW-uz1w6ryBlc6So2Wk",
            "https://drive.google.com/uc?export=view&id=1SKxZ4qaihiOUWAvXQ0TELuBa8aRAhgYP",
            "https://drive.google.com/uc?export=view&id=1VepiDpu0YOrnPBjQyvvxoWf6Uo5Fx77a",
            "https://drive.google.com/uc?export=view&id=1LxeTVtuGFTogT0Z-XzSHq7LUIUtfwqch",
            "https://drive.google.com/uc?export=view&id=1WYhRNJDhPQiD_GCB5CkkfiXGycz_OCPp",
            "https://drive.google.com/uc?export=view&id=1dnf4sT2yq8a_bZEa9jrs1RIqvojzOSq1",
            "https://drive.google.com/uc?export=view&id=1c8Te9U_iEhNLR2dKIDuhBBkHid40WNkw",
            "https://drive.google.com/uc?export=view&id=1FpCItQ1NnLlVEjN9FjBGT78g_v7Kt3bu",
            "https://drive.google.com/uc?export=view&id=16Bt6bLYqKkgalMTxhgyD7IF4dnSI5eIf",
            "https://drive.google.com/uc?export=view&id=1ooMsFHvahz3McwfVbfzMtv0MVWaIdn4j",
            "https://drive.google.com/uc?export=view&id=1UHOYKBbO5kWvqAKUU0lqh3GWDnLM2oAz",
            "https://drive.google.com/uc?export=view&id=1f-uvH3Q5X557o-HHPO9lC_YctUk5lTT3",
            "https://drive.google.com/uc?export=view&id=12UuD87oVxQ-McGwAgAQ_UHuQviY_-uJK",
            "https://drive.google.com/uc?export=view&id=1DI0bWMTvGwgI3Kf4ud039ndrEM68JGon",
            "https://drive.google.com/uc?export=view&id=1kqc2e695qSkxF0mSdVIhVVOdrvqXcEqb",
            "https://drive.google.com/uc?export=view&id=1sBJHYcg4_APBJZ5bVhx46osN4w4G4khb",
            "https://drive.google.com/uc?export=view&id=10mPKaGYG12suGOXy3KUX8N6myMM3Q-no",
            "https://drive.google.com/uc?export=view&id=10TXsYLGXyQ6k91ecxOqcs0Gr3ZFqPyhn",
            "https://drive.google.com/uc?export=view&id=1IIUqz4BcmtwhKmAIRMrLBY5n59IEffxz",
            "https://drive.google.com/uc?export=view&id=1RBANLr__5nx5E-RnGbn0_cwaMWD_HRaw",
        ]
        data_list = [
            {
                   "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Abang keren banget dan baik.",
                "pesan": "Semangat terus ya bang."
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak baik banget.",
                "pesan": "Lancar dan semangat terus ya kak kuliahnya."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakak baik dan ramah, dan asik banget.",
                "pesan": "Semangat dan lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Abang keren dan pinter banget.",
                "pesan": "Lancar dan semangat terus ya bang."
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakak cantik dan baik banget.",
                "pesan": "Jaga kesehatan, dan semangat terus ya kak."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang baik dan asik banget.",
                "pesan": "Semangat dan lancar terus ya bang kuliahnya."
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Abang baik dan asik banget.",
                "pesan": "Jaga kesehatan, dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakak cantik dan baik banget.",
                "pesan": "Semangat terus ya kak kuliahnya."
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abang baik dan pinter banget ngodingnya.",
                "pesan": "Sehat terus, dan semangat terus ya bang."
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Abang baik dan keren banget.",
                "pesan": "Lancar dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak baik dan asik.",
                "pesan": "Sehat selalu, dan semangat terus ya kak."
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Abang keren dan baik banget.",
                "pesan": "Semoga lancar terus ya bang kuliahnya."
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Abang baik banget",
                "pesan": "Semangat terus ya bang."
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakak cantik dan baik banget.",
                "pesan": "Lancar dan semangat terus ya kak kuliahnya."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakak baik dan asik banget.",
                "pesan": "Sehat selalu, dan semangat terus ya kak."
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "abang baik banget dan asik.",
                "pesan": "Semoga lancar terus ya bang kuliahnya."
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Abang keren dan baik banget.",
                "pesan": "Semangat terus ya bang."
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakak cantik dan baik banget.",
                "pesan": "Lancar dan semangat terus ya kak kuliahnya."
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Abang asik dan baik banget.",
                "pesan": "Semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Abang baik dan keren.",
                "pesan": "Lancar dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak cantik dan baik banget.",
                "pesan": "Semangat terus ya kak kuliahnya."
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Abang asik dan keren banget.",
                "pesan": "Lancar dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakak baik banget.",
                "pesan": "Jaga kesehatan, dan semangat terus ya kak."
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Abang asik dan baik banget.",
                "pesan": "Semangat terus ya bang."
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Abang lucu dan baik banget.",
                "pesan": "Sehat terus, dan semangat terus ya bang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1B5emGPoR6swdr80rI2zTeLbTVbLCp2uX",
            "https://drive.google.com/uc?export=view&id=18ZX7ygIvX18-8D2FJPtk7ppMwGMQ2FjM",
            "https://drive.google.com/uc?export=view&id=1jvmsQzQcM0D2k2bSeIeGU7WHS9X4zC6P",
            "https://drive.google.com/uc?export=view&id=1SSEzW0ZpbUMpeIn7IQuS3HGV4acnBjws",
            "https://drive.google.com/uc?export=view&id=12AsCLcYdN7vLJp9hu11ppRbD84Ulz1Sm",
            "https://drive.google.com/uc?export=view&id=1Up_ccQW8nQKT5m_87H8qk4onwigZZm5I",
            "https://drive.google.com/uc?export=view&id=14SlFPX394BV520bKxx8_0NzRHwK8b5YZ",
            "https://drive.google.com/uc?export=view&id=1zGgrwmfAJgJVYcjFmx0xffeOKV3Uvdu1",
            "https://drive.google.com/uc?export=view&id=19PIcAfckn8DwYZTtE2bqw5ZMgIhp5pfs",
            "https://drive.google.com/uc?export=view&id=1As5Fy_UyF2-eMkfb39UMEkcyi3flN9bi",
            "https://drive.google.com/uc?export=view&id=12O3vftyv1pmCb16_4HdSLpbiHU2_1hlO",
            "https://drive.google.com/uc?export=view&id=15Iq0x0BUNvkYbidnR-VZxGac1sozUOO8",
            "https://drive.google.com/uc?export=view&id=1mTFmHpwQlBKlsSrNe8iz668Plg3UvV17",
            "https://drive.google.com/uc?export=view&id=18wvMLvFwyIrHfBBCGTEvlDl4CasE7ghQ",
            "https://drive.google.com/uc?export=view&id=1EGdwX_2W5Im2ZOyrbapgEMcrzt1zgHXh",
            "https://drive.google.com/uc?export=view&id=1TtTaY5P3vYO_jOgKJ844tFxl4-L7wcBO",
            "https://drive.google.com/uc?export=view&id=1D-5zFdyGGqNmWjRYEBGnwyaFgWmuAq13",
            "https://drive.google.com/uc?export=view&id=1CWNRkQER578SpuRQ90O9LrMRRM-f9Qqs",
            "https://drive.google.com/uc?export=view&id=1fXLYH3TBhAIqgJefeS5qAgmQhMrZVPEY",
            "https://drive.google.com/uc?export=view&id=1ubS4BnlrqdGJP7nB7q5XGOmJhv7jYwNW",
            "https://drive.google.com/uc?export=view&id=1RQm6indK_uafPozfKZOT9yRSmjFh9MtJ",
            "https://drive.google.com/uc?export=view&id=1KguNfWvcCy-S3uUA4MNvUol7UME8cwXc",
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
                "kesan": "Abang keren ngejelasin soal mikfes, baik banget.",
                "pesan":"Semangat dan lancar terus ya bang kuliahnya."
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Kakak baik, ramah banget.",
                "pesan":"Sehat terus, dan semangat terus kuliahnya kak."
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abang keren, baik banget.",
                "pesan":"Lancar dan semangat terus bang kuliahnya."
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak cantik, baik banget.",
                "pesan":"Semangat terus ya kak kuliahnya."
            },  
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Abang keren banget, baik, pinter.",
                "pesan":"Semoga lancar terus ya bang kuliahnya."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Abang asik banget, keren, dan baik.",
                "pesan":"Semoga lancar terus ya bang kuliahnya."
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abang baik banget.",  
                "pesan":"Lancar terus ya bang kuliahnya."# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakak baik banget, dan cantik.",
                "pesan":"Semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak baik banget.",
                "pesan":"Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abang mentor markov imut.",
                "pesan":"Sehat terus, dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak kpopers juga ternyata.",
                "pesan":"Sehat selalu, dan lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak baik banget.",
                "pesan":"Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "JL. Gajah Mada, Tanjungkarang",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak cantik, dan baik banget.",  
                "pesan":"Semangat terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakak baik banget.",  
                "pesan":"Lancar dan semangat terus kak kuliahnya."# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kakak baik banget.",
                "pesan":"Semangat dan lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abang keren, pinter banget ngodingnya.",  
                "pesan":"Lancar dan semangat terus ya bang kuliahnya."# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak cantik, baik banget.",  
                "pesan":"Sehat terus dan semangat terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Abang asik banget, keren, dan jago banget ngodingnya.",
                "pesan":"Sukses terus yaa bang."
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Abang baik banget.",
                "pesan":"Lancar dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak baik banget.",
                "pesan":"Jaga kesehatan, dan semangat terus ya kak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak cantik dan baik banget.",
                "pesan":"Semangat terus ya kak kuliahnya."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abang asik, lucu banget dan baik.",
                "pesan":"Lancar dan semangat terus ya bang kuliahnya."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sB6q9SFRaI2mrkT4qMfwwHE4a2PqgbNa",
            "https://drive.google.com/uc?export=view&id=1jm-7SJ_RLOu-h2WTzAz4x0JfaArRcKTg",
            "https://drive.google.com/uc?export=view&id=1UrSjGYFnfQDix6zfz71Y0XL6D5b_Dj_m",
            "https://drive.google.com/uc?export=view&id=1Bt6nbMS3Ov91QK0mifau1CJO4TeZsM6V",
            "https://drive.google.com/uc?export=view&id=1O6NxZGVmle7pM2St2dpNbwHaViqyBEbb",
            "https://drive.google.com/uc?export=view&id=1AhFoe_9uDe46DCgil8QXP3uCASANncGG",
            "https://drive.google.com/uc?export=view&id=1pIXE3DuBbf61AkBUsakfyx72I4bNycCd",
            "https://drive.google.com/uc?export=view&id=14PrezqZlb_SatKEyW7yBnqDBL7ttgQWF",
            "https://drive.google.com/uc?export=view&id=1r-VheYLRQY54BZuhRJsW1v85E-aEf3Bm",
            "https://drive.google.com/uc?export=view&id=1yKiK9q6Rt7Nc-P3W0LPqxsFR7kDSzz9V",
            "https://drive.google.com/uc?export=view&id=1A0vyNRAGKoi5T6aWpDOnYvc665zRDg6y",
            "https://drive.google.com/uc?export=view&id=1MwADIlCmBQp6UDbpY6hlC_ZPA3DzqDbw",
            "https://drive.google.com/uc?export=view&id=1EmHT27cUz6H5rfoEdl7jD99WJjavAn4k",
            "https://drive.google.com/uc?export=view&id=1ZoNXaCZVDyFLOGAbKoe9iamTTj7s6h_a",
            "https://drive.google.com/uc?export=view&id=1Ur13xqudwemcRKxw6aHlZi0bBw34FMHF",
            "https://drive.google.com/uc?export=view&id=116dsghLEOXKrahhoaauJXw4sCSQtqlJE",
            "https://drive.google.com/uc?export=view&id=1-kMgHeTo_eza26yx6q_me_b7ZNjjLF6-",
            "https://drive.google.com/uc?export=view&id=1C_gY5_QUKp4jJvW8CmjRLBKS6vMdlcKL",
            "https://drive.google.com/uc?export=view&id=1nyPdSk0horvZ8JC14_0S34bvijYAtvog",
            "https://drive.google.com/uc?export=view&id=1TDrJnqVm5r9X9vV9DEJI5mEnMcx6hDDy",
            "https://drive.google.com/uc?export=view&id=1ZYfF32WQnpPrHuneAurUND6KVVhhk5x-",
            "https://drive.google.com/uc?export=view&id=1myoDej-tJMuEpH-2tNNGotScoISRM9Zv",
            "https://drive.google.com/uc?export=view&id=1GfHYyWL5KylMijneNVeoX_856rS_Kzs8",
            "https://drive.google.com/uc?export=view&id=1zLJFrHshhZR38o15kywWXxcvjxCEXBdM",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abang keren dan baik banget.",  
                "pesan":"Semoga lancar terus ya bang kuliahnya."# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak baik banget dan pinter.",  
                "pesan":"Lancar terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak baik banget dan cantik.",  
                "pesan":"Semoga lancar terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak cantik dan baik banget.",  
                "pesan":"Lancar dan semangat terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abang asik dan baik banget.",  
                "pesan":"Semangat terus ya bang."# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak cantik dan baik banget.",  
                "pesan":"Sehat selalu, dan semangat terus ya kak."# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak cantik dan baik banget.",  
                "pesan":"Semoga lancar terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak cantik dan baik banget.",  
                "pesan":"Semangat terus ya kak."# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abang baik banget dan asik.",  
                "pesan":"Lancar dan semangat terus ya bang kuliahnya."# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak cantik dan baik.",  
                "pesan":"Semangat terus ya kak."# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakak baik dan asik.",  
                "pesan":"Lancar terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakak keren dan baik banget.",  
                "pesan":"Sehat terus, dan semangat terus ya kak."# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abang keren dan asik.",  
                "pesan":"Semangat terus ya bang."# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak baik dan keren banget.",  
                "pesan":"Sehat selalu, dan semangat terus ya kak."# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak baik dan keren banget.",  
                "pesan":"Semangat terus ya kak."# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abang lucu dan asik.",  
                "pesan":"Semangat terus ya bang."# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Abang kocak dan asik abis.",  
                "pesan":"Sehat terus, dan semangat terus ya bang."# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak cantik dan baik banget.",  
                "pesan":"Semoga lancar terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak baik banget dan cantik.",  
                "pesan":"Lancar dan semangat terus ya kak kuliahnya"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak baik banget",  
                "pesan":"Semangat terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Kakak cantik dan keren.",  
                "pesan":"Lancar terus ya kak kuliahnya."# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakak baik banget dan keren.",  
                "pesan":"Sehat selalu, dan semangat terus ya kak."# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang keren dan baik banget.",  
                "pesan":"Semangat terus ya bang kuliahnya."# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kakak cantik dan baik banget.",  
                "pesan":"Sehat terus, dan semangat terus ya kak."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1h3DoUBXlXMgr0VDmqa5lSQG-oPqlNHj3",
            "https://drive.google.com/uc?export=view&id=1xCpxpcipSWcX2KxllqhNW1aVyK-BiJx5",
            "https://drive.google.com/uc?export=view&id=1mjMr6MP2ODYH4dinlclGnb3VDwYbfZGC",
            "https://drive.google.com/uc?export=view&id=1l0Ggz8CHdMS_xwfNV4xCTd0oG6bvX-oR",
            "https://drive.google.com/uc?export=view&id=1iwQlLzkz42enEI3nflwGpQpbh8v6EsNh",
            "https://drive.google.com/uc?export=view&id=1uDuW8QOuTQUn66z0NxXb2v-BAVc-Roh_",
            "https://drive.google.com/uc?export=view&id=1UIjm2oLKgwvKUcza2A9WM6izxTbw1AEj",
            "https://drive.google.com/uc?export=view&id=11T3ak7aK3eaEoE4xQoXd-6dWDemuFyrY",
            "https://drive.google.com/uc?export=view&id=1UK1RGEtFPEGhGNK_zA1hK4rmuTIdnTTS",
            "https://drive.google.com/uc?export=view&id=1ufiwO6Q-yP_L3XckP-wUc6oqL8qu8tar",
            "https://drive.google.com/uc?export=view&id=1CFYxjp6QrxCf_RVDPzuSk6KQLZBXijNE",
            "https://drive.google.com/uc?export=view&id=1WX28Mi_fe8zW98X32M17L-4R1uhuT3ct",
            "https://drive.google.com/uc?export=view&id=1fKrsdj4aITxUM8JItzW6FIg_h60czKG6",
            "https://drive.google.com/uc?export=view&id=1WCAhm6_PwmxpCOUBECqP-F6eoRzQsYQt",
            "https://drive.google.com/uc?export=view&id=1BbEHBcxknRLkJahdPJA7Zgnse18sU75a",
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
                "kesan": "Kakak cantik dan keren banget.",
                "pesan": "Semangat terus ya kak."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak baik banget dan keren.",
                "pesan": "Sehat selalu, dan lancar terus ya kuliahnya."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakak baik banget dan asik.",
                "pesan": "Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakak cantik dan baik banget.",
                "pesan": "Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang asik dan baik.",
                "pesan": "Lancar dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abang keren banget.",
                "pesan": "Jaga kesehatan, dan semangat terus ya bang."
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Semangat terus ya kak kuliahnya."
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Semangat terus ya kak."
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Abang baik dan keren.",
                "pesan": "Semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abang baik dan asik.",
                "pesan": "Lancar terus ya bang kuliahnya."
            },
            
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak cantik dan asik banget.",
                "pesan": "Sehat terus, dan semangat terus ya kak."
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakak cantik, dan baik banget.",
                "pesan": "Jaga kesehatan, dan semangat terus ya kak."
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abang baik banget.",
                "pesan": "Semangat dan lancar ya bang kuliahnya."
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Semangat terus ya kak."
            },
            
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen Rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak baik banget dan seru.",
                "pesan": "Semangat terus ya kak kuliahnya."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A8tTDxFGY7niy07FZW11c1IpzaZ3IRMA",
            "https://drive.google.com/uc?export=view&id=1yVUiB3CguynwGnxG2acU4L9fcbrBx7A_",
            "https://drive.google.com/uc?export=view&id=1ACF657O6dTROIOReADac7nJirzmP91zk",
            "https://drive.google.com/uc?export=view&id=1pngot8TVRUpn9AkFT411XzroeejYuyVU",
            "https://drive.google.com/uc?export=view&id=1Si91o5vg5Hbvfg2mzGleRJrh3gD2KxK4",
            "https://drive.google.com/uc?export=view&id=1ULBFdAzTeDw8iBCn_Md6WQh3wDy-2xh1",
            "https://drive.google.com/uc?export=view&id=1bSMgOqN6K7hopvxRiXMlecAthhGv_TYj",
            "https://drive.google.com/uc?export=view&id=1C_sxAGMnxiPpjC5gL6rTyDUolKedJR10",
            "https://drive.google.com/uc?export=view&id=1WAl99d_iVoT-sZOTeQqr22_wrlJl91mF",
            "https://drive.google.com/uc?export=view&id=1pvHxYe2pncqup-ZaDEm6CeztfB8s_PRH",
            "https://drive.google.com/uc?export=view&id=1RYtozHSaqrDs4d7DeIHZY7vZfjLNHx0H",
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
                "kesan": "Abang danusan waktu verbek, ternyata keren banget.",
                "pesan": "Semangat terus bang kuliahnya."
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Kakak cantik.",
                "pesan": "Semangat terus kak kuliahnya."
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Abang keren.",
                "pesan": "Semoga lancar bang kuliahnya."
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Semangat terus kuliahnya kak."
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Kakak cantik, keren.",
                "pesan": "Semoga lancar terus kak kuliahnya."
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakak keren, cantik.",
                "pesan": "Lancar terus Kuliahnya kak."
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Abang baik, keren.",
                "pesan": "Semoga lancar terus bang kuliahnya."
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakak cantik, baik.",
                "pesan": "Semangat terus kuliahnya kak."
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Kakak cantik, baik.",
                "pesan": "Lancar terus kak kuliahnya."
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakak cantik, baik.",
                "pesan": "Semoga lancar terus kak kuliahnya."
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Kakak cantik, baik.",
                "pesan": "Semangat terus kak kuliahnya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tlH910FHHT-YGqzo52OT74A6TF-4sRCP",
            "https://drive.google.com/uc?export=view&id=1v20BVkp-dxJqLdOiWbRrViQ7eeUM6XKx",
            "https://drive.google.com/uc?export=view&id=10Se1HIAeVS1i9KfxjgYhimR3QmrkZldK",
            "https://drive.google.com/uc?export=view&id=12aw2bwtPrb2VhLvLHtkvP1yX4lGVtKd0",
            "https://drive.google.com/uc?export=view&id=1GCf7Lgv2z3OdH3rOfspR6MDmMKywbdwn",
            "https://drive.google.com/uc?export=view&id=19jGrEo9MxcMRMw3IMwDBtu7EAZZYktf4",
            "https://drive.google.com/uc?export=view&id=1U7B-FJXgPG1HEGY1PMvsXn6yuTfqaW5v",
            "https://drive.google.com/uc?export=view&id=1O_Mlz4ROeuIhCVmi-cNu2G0Tqy7SC3i6",
            "https://drive.google.com/uc?export=view&id=116uG_8USzdKo_hPH2H31ni8wMqbaEEGR",
            "https://drive.google.com/uc?export=view&id=1csfuZi_1q2CKVFQArTQ6Cw_GGBCcyJ65",
            "https://drive.google.com/uc?export=view&id=1djzVDk-YaZuiH_byY9aKz86nxncEejlR",
            "https://drive.google.com/uc?export=view&id=1T6EXrKY_oERpPem74rDwa2Mz9AQxiPuo",
            "https://drive.google.com/uc?export=view&id=1xCpFwejEheeF2vFc5teXSboCO-6bjVwT",
            "https://drive.google.com/uc?export=view&id=1MtrLHUTFEMfqzznhkXUePr9_aUyPS6Dx",
            "https://drive.google.com/uc?export=view&id=1tnSsONUx7lA5XY5AveG4hBdXbfq5Vhtl",
            "https://drive.google.com/uc?export=view&id=1_HzElilzWREfD29KtBZN9b-3-k-rNOj7",
            "https://drive.google.com/uc?export=view&id=12zRNm_IO_3JYapKTI-L5E6G5mR65OcKL",
            "https://drive.google.com/uc?export=view&id=1gU6dXYkJkgeutXA9ya7LEKNo6gevBFNy",
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
                "kesan": "Kakak seru dan asik banget.",
                "pesan": "Semangat terus ya kak."
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Abang keren dan baik.",
                "pesan": "Sehat selalu, dan semangat terus ya bang."
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abang pdd kren dan baik",
                "pesan": "Semangat terus ya bang."
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abang dokum keren dan baik.",
                "pesan": "Lancar dan semangat terus ya bang kuliahnya."
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Sehat selalu, dan semangat terus ya kak."
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakak baik banget.",
                "pesan": "Semangat terus ya kak."
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kakak baik dan asik.",
                "pesan": "Semoga lancar ya kak kuliahnya."
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak imupku terbaik.",
                "pesan": "Sehat selalu, dan lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "jaga kesehatan, dan semangat terus ya kak."
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakak baik dan asik.",
                "pesan": "Semangat terus ya kak kuliahnya."
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak baik banget.",
                "pesan": "Semangat terus ya kak."
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Abang baik dan keren.",
                "pesan": "Semoga lancar terus ya bang kuliahnya."
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakak cantik dan baik.",
                "pesan": "Lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakak baik banget dan asik.",
                "pesan": "Sehat selalu, dan semangat terus ya kak."
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakak cantik dan asik banget.",
                "pesan": "Semoga lancar terus ya kak kuliahnya."
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak cantik dan baik banget, ramah juga.",
                "pesan": "Sehat terus, dan semangat terus ya kak kuliahnya."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

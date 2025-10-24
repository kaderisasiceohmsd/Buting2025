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
    st.markdown("""
    <div style="
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #2c3e50;
        background: linear-gradient(90deg, #f8f9fa 0%, #e8e8e8 100%);
        padding: 20px;
        border-radius: 15px;
        width: 90%;
        margin: 60px auto 30px auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        letter-spacing: 0.5px;
    ">
        Anda telah mencapai akhir halaman<br>
        <span style="font-weight:500; font-size:18px; color:#555;">(tidak ada apa-apa disini)</span>
    </div>
""", unsafe_allow_html=True)
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ndEPtz6SWZKzjSHoz0U7cadKd4q0ieI9",
            "https://drive.google.com/uc?export=view&id=1ii-p8LGOrp_fvhngT7TnAK9pIsxrxoHg",
            "https://drive.google.com/uc?export=view&id=14h-jruI3jiZ0AL389YpjB34fOWwsL1gB",
            "https://drive.google.com/uc?export=view&id=1lihcVtEg92GrcUCo7PU_YvCN2q2NrKeA",
            "https://drive.google.com/uc?export=view&id=1BmYm8d8pbAF55y4P7BiQjXcJ2J7Ay4Ui",
            "https://drive.google.com/uc?export=view&id=1SJycobKn8JxTuKaCE22GdEnQoV32mbWB", 
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damai",
                "hobbi": "Nyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Abang ini seru Abiez",  
                "pesan":"Semangat Bang jadi Kahim!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL!",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Jo Seru & Ternyata satu daerah asal",  
                "pesan":"Gassin terus bang !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Badui",
                "alamat": "Ayrest Kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini lucu humoris dan seru",  
                "pesan":"semoga akunnya gak kena suspend lagi kak"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza keren",  
                "pesan":"semoga sukses terus kak"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik dan seru",  
                "pesan":"sukses teruss kak"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini lucu, jutek tapi seru",  
                "pesan":"semoga suksess terus kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1P1dO0ciXaP0WNPIooksKTSfJJy4kQsi2",
            "https://drive.google.com/uc?export=view&id=1BPAWS19a5QMi2DK_HAEBBnSeOdK5utDP",
            "https://drive.google.com/uc?export=view&id=1jWxSNn7VReC9QYvNXlJOtksqNFRx8Wah",
            "https://drive.google.com/uc?export=view&id=11V6GaGaCo-WrwOwslXcNJ5oeEfgC5iOd",
            "https://drive.google.com/uc?export=view&id=1aOSgRM1O1Q2lre62qEgDsubhoDEWgrKb",
            "https://drive.google.com/uc?export=view&id=1MgzYkEaz9qP9kJBZHPELYmDwWf0Tyt0R",
            "https://drive.google.com/uc?export=view&id=1vyCscFsNFlFw_ihEvCrsuYMV9uMQYjPE",
            "https://drive.google.com/uc?export=view&id=1Mp9XlVx9T2DS0UiJLSVErBXMO7Dtitke",
            "https://drive.google.com/uc?export=view&id=1wfQ5m6oYscPLiDjy6ya7S7IBI1l2JvxV",
            "https://drive.google.com/uc?export=view&id=14gLpN0N_UPK-kF8v9B1GOahbdvjeS2Wh",
            "https://drive.google.com/uc?export=view&id=1HivdwidJNGByF-VEX4ezZ5Nv4WIgHCxl",
            "https://drive.google.com/uc?export=view&id=1KiKLZk4I_07LVT64MTcmHRxVu8Cf5fs7",
            "https://drive.google.com/uc?export=view&id=1Bp4I09qTKnsiCtyjE7wamUd1WYwdJzf5",
            "https://drive.google.com/uc?export=view&id=1Cxlsc1Mp5aNsiqCTiKb9F6GBQrUzlQ7v",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Pilates",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang terasik, terseru, & Satu Alumni Sekolah",  
                "pesan":"semangat bang semster 7 nya!!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea gokil",  
                "pesan":" Sukses terus kakk!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "kak renisha humoris",  
                "pesan":"jangan keseringan tidur kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya keren",  
                "pesan":"Sukses terus kaa"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Terkerenn dan terkecee",  
                "pesan":"semangat terus bang kejar cumlaude ituu"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini imut, lucu",  
                "pesan":"semangatt teruss kak feby!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "abang-abangan, seru abiez, cihuy mentor terdabest",  
                "pesan":"kurang-kurangin brainrot nya bang"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang cool, keren, asik",  
                "pesan":"semangat terus main kucingnya bang!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Catur",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asix",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandiama",
                "alamat": "Way Huwi",
                "hobbi": "Minum air putih 8x sehari",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik, seru, baik",  
                "pesan":"semangat terus kuliahnya, dan selalu stay positive kak!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Nyanyi tabola bale",
                "sosmed": "@iamridhomanik",
                "kesan": "abang ini lucu, humoris",  
                "pesan":"tetap lucu dan menghibur orang selalu bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Koleksi Stiker",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini chill, ngalur wae",  
                "pesan":"tetap santai bang, sukses terus kuliahnya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Papua Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik, manis, humoris",  
                "pesan":"semangat terus kak monica!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik seru dan humoris",  
                "pesan":"semangat terus kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xEJuV_Q6hFGQAxZfkaDcaAoc2x54y79Y",
            "https://drive.google.com/uc?export=view&id=1-c9n-H1arUvp6Bnu3ksLq9uBmH5kuoFd",
            "https://drive.google.com/uc?export=view&id=1DmElaA1EqSlAJErA0c8nA3rj1ZGnFspL",
            "https://drive.google.com/uc?export=view&id=1R6hX0TmTKOBXeNFqC7-VpBZvd-BLIAuT",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Denger lagu, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang kece kura-kura",  
                "pesan":"semangat terus bangg menggapai mimpinya!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu, maen roblox",
                "sosmed": "@nadyaanjanani",
                "kesan": "Kakak ini asik, baik",  
                "pesan":"semangat terus kuliahnya, dan langgeng terus ya kak ;)"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Ice Skating",
                "sosmed": "@fathinahazzh",
                "kesan": "Kakak ini baik, seru",  
                "pesan":"keep positive kak!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "kakaknya kerenn",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tihz6vyPX5cBQpbUk1UDpPsDT8N74kI2",
            "https://drive.google.com/uc?export=view&id=1L4U_C9Bn-4j7PrMKOICzCdaWEhBJl-ia",
            "https://drive.google.com/uc?export=view&id=1bMKg5sLgeox7ikFLtQmh4509KumNexeG",
            "https://drive.google.com/uc?export=view&id=1bW2eo9LcFg-3uCcCEGjpF-sVb3sO69Wh",
            "https://drive.google.com/uc?export=view&id=1uhHBKbWiQd1jfYOV-d1H3H94GFZ-j6v-",
            "https://drive.google.com/uc?export=view&id=1RerBMEi_WuKsO-aLB8JHrVp0DBMzCkg1",
            "https://drive.google.com/uc?export=view&id=11ND38HwXsg1qfmqYkXfSj9F9qBrSlOjZ",
            "https://drive.google.com/uc?export=view&id=1asU4vrtSmfvboPSu3UyDiITuZR5EHyEG",
            "https://drive.google.com/uc?export=view&id=1nT_de0c4XM5z3mjwaENc7ljCA8PrOnWX",
            "https://drive.google.com/uc?export=view&id=1rMfDJg5-A0hOK1h8_SFh2xrEFE08OyY4",
            "https://drive.google.com/uc?export=view&id=1aKp6oTyjOgM_HFGrQ-VaUeZ-vR9GwGpv",
            "https://drive.google.com/uc?export=view&id=1sCMhICHfHxbAIQxqSn0zV5B1g3wrtsXM",
            "https://drive.google.com/uc?export=view&id=1k0tF8G5FLMaUGhDSX02AHOP0lZymuHbD",
            "https://drive.google.com/uc?export=view&id=1Rc8TUD0rVeL66fzX-7kAA0zwRxxud9JV",
            "https://drive.google.com/uc?export=view&id=1yg7dCDc-nOy8VYDHTU5qpYvUIsPDrk_z",
            "https://drive.google.com/uc?export=view&id=1iPtkQ0j8A8obFQZuhWwd_Z8Z9FyiKAsZ",
            "https://drive.google.com/uc?export=view&id=1DsiDwcOYGRFfNHLB1xPKFxJKhuJiNkSd",
            "https://drive.google.com/uc?export=view&id=1OTWBgpuSGISIgDqhiAQn5Afl2gR73Y_G",
            "https://drive.google.com/uc?export=view&id=1LjluleVIQWpSSAbxwSX9Tjw3ZrND5qQE",
            "https://drive.google.com/uc?export=view&id=1leLU6vp0w_zbgm8qvuVJOMr6MbCcajn3",
            "https://drive.google.com/uc?export=view&id=1Fgeyib3SjI4o9OMb_hp1ItBU4ZTZhzzG",
            "https://drive.google.com/uc?export=view&id=1zJzaydNjRvyYRobQCJah-jjZ7DlGu-MV",
            "https://drive.google.com/uc?export=view&id=1kbe7A3cKla3YtNKVETLOY_s4_fFw7hZ-",
            "https://drive.google.com/uc?export=view&id=16QFRplNGmqxvFKV8qQWs8CS-ln3OT-6d",
            "https://drive.google.com/uc?export=view&id=1r_PBEpKCTTil6NoyL_EwiwZHwuzqPDpN",
            "https://drive.google.com/uc?export=view&id=1fVtCy3T1YQUQm1F1kWQHDqcuvuVf8sK5",

        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang cool abiez",  
                "pesan":"semakin cool bang dan semangat terus bang jadi kadep!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak seru kece",  
                "pesan":"semangat teruss kak jadi sekrenya!!!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakak ini asik seru gaul abis pokoknya",  
                "pesan":"semangat terus jadi kadivnya kak pasha!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "abang keren, kece, full aura",  
                "pesan":"semangat terus bang membawa nama baik sains data terbang tingii!"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakak ini cetarr keren",  
                "pesan":"semangat terus kak arienta!"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang komdis kerennn",  
                "pesan":"semakin keren banggg dapaa!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "abang kece abiezzz",  
                "pesan":"tetep kece terus ya bang"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakak ini asik seru",  
                "pesan":"semangat terus kak natasya jadi bendaharanya"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abang cool, jago koding",  
                "pesan":"Tetep cool, dan keren bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Abang Kece Commander",  
                "pesan":"semangat terus bangg!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang Berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak ini asik abiezz",  
                "pesan":"semangat terus kakk!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "Abang kece santai",  
                "pesan":"makin kece bang sahid"# 1
            },
            {
                "nama": "ALi Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang 4 Nangka Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "Abang baik, santai, asik dah pokoknya",  
                "pesan":"semangat terus bang ali!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini kalem, chill",  
                "pesan":"tetap semangat kak gusti"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak lucu seru",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakak ini asikkk",  
                "pesan":"semangat terus kakk!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "Abang asik, baik",  
                "pesan":"semangat terus bangg!"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_",
                "kesan": "Abang santai, kece",  
                "pesan":"tetep kece terus bang!"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakak asikk dan seru",  
                "pesan":"semangat terus kak jadi dancernya!"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Belajar Front end",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abang Chill, skena",  
                "pesan":"semangat terus belajar fornt end nya bang!"# 1
            },
            {
                "nama": "Kevin Antoni JUnior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Berdiri, Nyantai",
                "sosmed": "@kevinaj_",
                "kesan": "Abang ini asik seru gaul abis pokoknya",  
                "pesan":"Stay gaul bang!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak ini asik santai",  
                "pesan":"semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Abang kocak, seru, santai",  
                "pesan":"Keep positive bang!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main futsal, voli",
                "sosmed": "@sidabutar.26",
                "kesan": "Abang Kocak Abis, Humoris, Seru",  
                "pesan":"Tetap semangat bang Benget!"# 1
            },
            {
                "nama": "Wuliano Wiliam Purba",
                "nim": "123450098",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngoding",
                "sosmed": "@liano.wlm",
                "kesan": "Abang cool, dingin, asik",  
                "pesan":"Tetap semangat bang!"# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KGdRuW9W8aqTzoB_-ADQiRdJ9tBYUzt4",
            "https://drive.google.com/uc?export=view&id=1jnEU-ko2vZn8CF9TMpIxc9YMWzn8epvw",
            "https://drive.google.com/uc?export=view&id=1aZmAtdYwm_PQf7qKISQmT7cqbezwXT0m",
            "https://drive.google.com/uc?export=view&id=1pTseIiNU7QqCOmXxGhyoShMFuGo1Q6yP",
            "https://drive.google.com/uc?export=view&id=1pYwiJ3kX8f_4_XLxNEl8DCuXgSt3pV-x",
            "https://drive.google.com/uc?export=view&id=1HdqZDY3srg6HeTpXKwUQXUcrOqiZKPI8",
            "https://drive.google.com/uc?export=view&id=1nx0HznTdj1nWhlbOebVQrlleQyx040iF",
            "https://drive.google.com/uc?export=view&id=1oKMIOP9w-q1PD6AnwmikhMPg_FLwIP-R",
            "https://drive.google.com/uc?export=view&id=12oCUxAVQmJRv2NYWS9dmDJkXSAxOPkkd",
            "https://drive.google.com/uc?export=view&id=1O4I9H9vCDOk9Twzv2Tmg4xt_URqELlaT",
            "https://drive.google.com/uc?export=view&id=1ga9VowxGB7DDoxm8GTHUd_oad0wLOMw4",
            "https://drive.google.com/uc?export=view&id=1JEXbpZaw2fwikNICU2POSJLPX_E08auf",
            "https://drive.google.com/uc?export=view&id=14-JvKQRqXdNZJEMlvGNvEpbLSgZmVsnz",
            "https://drive.google.com/uc?export=view&id=1VF2ll-7Yck2N8n9qGmZUWqqcMvG0caf0",
            "https://drive.google.com/uc?export=view&id=1DRKT7GMX9bdotvv4hUOAXfwyMhg8T8AS",
            "https://drive.google.com/uc?export=view&id=11zmiEKj1k9IW1STLWzJaOFGkye_vwoNI",
            "https://drive.google.com/uc?export=view&id=1EcRuBSeOYRcluEE7_euM9oMsjA7iEpjw",
            "https://drive.google.com/uc?export=view&id=1BWHQgC8x1QPd45Rx2x--yNHzTUG3aTFM",
            "https://drive.google.com/uc?export=view&id=1fTfUX659QkUWNjdrN9DJS30HIiUrQNql",
            "https://drive.google.com/uc?export=view&id=1RSRtAWuhxB5_zjT2nTukr49mw6fKMOj7",
            "https://drive.google.com/uc?export=view&id=1XR_A7XV5WZPoib05pyIrA4lTdAU58SLB",
            "https://drive.google.com/uc?export=view&id=1RmVt4BZEBebFs3a9v6NTuzwDwjdiK0JN",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur, berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Abang santai, seru, asik",  
                "pesan":"keep chill dan nonton windah bang!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Kakak ini baik dan seru",  
                "pesan":"semakin keren kak!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abang regi keren, berwibawa",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishashi",
                "kesan": "Kakak ini seru dan baik",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilafarizzii",
                "kesan": "Abang keren role model",  
                "pesan":"semangat terus bang!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Abang GACORR",  
                "pesan":"semangat terus ngebasketnya bang!!!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik, nonton",
                "sosmed": "@notfall.s",
                "kesan": "Abang santai, seru",  
                "pesan":"semangat terus bang!!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak ini kalem dan keren",  
                "pesan":"semakin keren kak!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini asik, multitalent",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abang chill keren",  
                "pesan":"Tetap santai terus ya bang!"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak ini asik seru dan suka drakor",  
                "pesan":"semangat terus ngedrakornya kak!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini seru pokoknya",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakak kalem, baik",  
                "pesan":"semangat teruss kak!"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakak yang baik, santai",  
                "pesan":"semangat terus kuliah & tidurnya kak!"# 1
            },
            {
                "nama": "Tanty Widyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kakak ini keren jago mc dll",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abang keren abiez, sepuh coding",  
                "pesan":"semangat terus nge project & kuliahnya bang!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik, seru, baik",  
                "pesan":"semangat terus kuliahnya kak afifah!!"# 1
            },
             {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@i",
                "kesan": "Abang kece abis, gokil dah pokoknya",  
                "pesan":"semangat terus bang & keep cool & humoris!"# 1
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abang pinter, kalem, seru, game enthusiast",  
                "pesan":"semangat terus kuliahnya & kapan-kapan mabar bang!"# 1
            },
             {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak lucu, keren pokoknya",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
             {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik, baik, dan seru",  
                "pesan":"semangat terus kak kuliah dan main ke embungnya!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abang kece & jago futsal",  
                "pesan":"semangat terus bang!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A2QwldMXoHSJP0XyGk1SI9Yyudjx0Z2D",
            "https://drive.google.com/uc?export=view&id=1zfSvTf7BQfkKTsBKQXSfRFk2ekq6TgBN",
            "https://drive.google.com/uc?export=view&id=12Pw0iXIjczNpRin-T-nxgTBPmxNhWQFt",
            "https://drive.google.com/uc?export=view&id=17eMoJRlC8xb200OcscgdRe2msARxY0uH",
            "https://drive.google.com/uc?export=view&id=1GHtCYXKsyuWn7AXKM8xpYgKc88FnplrH",
            "https://drive.google.com/uc?export=view&id=1uifVwcfKd73kWuqLkKqzfgdYfKwIIia4",
            "https://drive.google.com/uc?export=view&id=1q2SbhbiBddk43HXxDzwwJ0kzk0Z4KFdI",
            "https://drive.google.com/uc?export=view&id=1yk2FmyEhmNmWzgnqpJvSCRLNcrKA83cm",
            "https://drive.google.com/uc?export=view&id=1fGgeCPC7ilgaJkatemaQO-_FiX5m2Z82",
            "https://drive.google.com/uc?export=view&id=13t5AWYIq3-uk5lsqONc_eIHsckOkY4Oy",
            "https://drive.google.com/uc?export=view&id=1vdtxLO2zwvuBGgND0gXME6m-rzp7Dqr5",
            "https://drive.google.com/uc?export=view&id=1turaXfZxCVf9Qah9G7Brmz66priJvPUQ",
            "https://drive.google.com/uc?export=view&id=1FymVrjq6OrwiCD--8ystyB-JsVdGecyE",
            "https://drive.google.com/uc?export=view&id=1R-8AIMSd-Z7270HAk6BznJzxMDTUaMWo",
            "https://drive.google.com/uc?export=view&id=1rTfKFBYr_dvroc5elgfuRkcRD4zFPPck",
            "https://drive.google.com/uc?export=view&id=1gSXPfOCeLz9ya5T0P3sb7VlbeErmG1rk",
            "https://drive.google.com/uc?export=view&id=1If3uageBHIiAnoXMAPrXnkiUSrmEG0r4",
            "https://drive.google.com/uc?export=view&id=1eHBKwJcAZ7-fdXOK8wnPuQ2vhPpB38eU",
            "https://drive.google.com/uc?export=view&id=1xJqESNSlLM_gpnng2AriTujMyS-fxbws",
            "https://drive.google.com/uc?export=view&id=1J1y_PEWY7gV3JYkUFc5M8yTOzxCxtt4L",
            "https://drive.google.com/uc?export=view&id=1-qYLMCz8yy3xFwKB_OqiXYjjGrsVo6gt",
            "https://drive.google.com/uc?export=view&id=1XLKNPgALLzxIrCN706wgA3xceM8R2HDG",
            "https://drive.google.com/uc?export=view&id=1V5lU3_IBDd1S1WRBpvxC2B0XiZPKiFap",
            "https://drive.google.com/uc?export=view&id=1pEPcT60exZnEOkCUSuaag5tO6MutJYkt",
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
                "kesan": "Abang ini santuy, keren, kalem",  
                "pesan":"Semakin gacorr bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini seru asik dan gacor",  
                "pesan":"Semangat terus kak!!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak lucu, dan seruu",  
                "pesan":"Semakin positif kak!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak baik, dan seru",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abang seru positive vibes",  
                "pesan":"Tetap semangat bangg!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak seru, baik, dan kalem",  
                "pesan":"semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak santai, kalem",  
                "pesan":"Semangat terus kuliahnya!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak baikk, dan kalem",  
                "pesan":"Semoga tercapai cita-citanya kak!"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abang santai & kalem",  
                "pesan":"Semangat terus bang jadi asprak dan kuliahnya!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak baik, seru, positive vibes",  
                "pesan":"Semakin positive vibes kak!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya cantik banget, keren banget dutanya!",  
                "pesan":"Semangat terus kak dutaa & kuliahnya!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya lucu dan positif vibes banget ",  
                "pesan":"YAREEEUUUU!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abang gacor, cool abiez!",  
                "pesan":"Stay Gacor bang, tetep cool!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak baik, seruuuu!",  
                "pesan":"Kakak cantikk, dan baikk banget!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakak baikk, dan kecee!",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abang cihuyyy, kece!",  
                "pesan":"Semangat terus bangg jadi kadivnya dan kuliahnya!"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Abang gacor, cool abiez!",  
                "pesan":"Stay Gacor bang, tetep cool!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak kalem dan seruuu!",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak imut, dan baik!",  
                "pesan":"Semangat terus kakakk kuliahnya!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak cantik, keren dan kece!",  
                "pesan":"Semangat Kak Untuk segala apapun yang dilakukan!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Kakak kereeen bangett, kece abiez!",  
                "pesan":"Semangat terus kak kuliahnya dan cita-citanya!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kecee banget kak nurul!",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang keren dan kalem!",  
                "pesan":"Stay cool dan kece abiez bang!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kak Tarisya keyenn bangett!",  
                "pesan":"Semangat terus kak Tarisya, dan lancar terus untuk segala yang dihadapi kak!"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GK0SJm__hHeohqO-4-bnJXbA_hFejj8r",
            "https://drive.google.com/uc?export=view&id=1ov3zGO1uckXOoPyAQXNRYROPntQ2SLB6",
            "https://drive.google.com/uc?export=view&id=1BIvA-LVcF4YXivypCmcITtrIvG95iZ02",
            "https://drive.google.com/uc?export=view&id=1LfICXqtPV_Ky59nTXX84PeQdVddB7Kqa",
            "https://drive.google.com/uc?export=view&id=1pLETM0VyfDGViCiCg-4jOJK0FUYS7GnZ",
            "https://drive.google.com/uc?export=view&id=1O7KDNmd27KkRad__Au56MCPRwtJDJeYy",#
            "https://drive.google.com/uc?export=view&id=1nD6k3yYKSo7LZzF3apIrgeZTZlepn1RR",
            "https://drive.google.com/uc?export=view&id=1p_8JuDjy1jIloRaO2YNWgRWNeIWekE_M",
            "https://drive.google.com/uc?export=view&id=1ulK6FbaOTEBErnkhmyF_TIomXhU7_I4Q",
            "https://drive.google.com/uc?export=view&id=1KWEKDMnYnjKSMclHP3xK0h54LYeD3T9K",
            "https://drive.google.com/uc?export=view&id=1pjidaOW0R3Wsfw-makhCi1O5DYlOhZw0",
            "https://drive.google.com/uc?export=view&id=1dxU_HObKoseC6TMbUcHL_eMQ2iPzGDFy",
            "https://drive.google.com/uc?export=view&id=10bWH0faXa0M-cWDSCMqjqO8RvXhtTLew",
            "https://drive.google.com/uc?export=view&id=1naWNVM6jkFWZTDqu_ssQteXAoon3iQKe",
            "https://drive.google.com/uc?export=view&id=1jwsJxXEPeCosLwWoffwV9L86_Qr7sFmn",
        
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
                "kesan": "Kakak ini seruu",  
                "pesan":"semangat terus jadi kadepnya kak!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak ini lucu keren",  
                "pesan":"semangat terus kaaakkk!!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@sal_fhn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abang ini kalem dan keren",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakak ini asik, lucu",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang chill, asik",  
                "pesan":"keep gacor bang!!!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak ini lucu dan keren",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20 tahun",
                "asal":"Sidorejo, Sidomulyo, Lampung Selatan",
                "alamat": "sabahbalau",
                "hobbi": "nonton anime",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "Abang kalem",  
                "pesan":"semangat terus kuliahnya bang naufal!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatriaaa",
                "kesan": "Abang santai dan kece",  
                "pesan":"semangat terus kuliahnya bangg!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakak seru lucu humoris asik",  
                "pesan":"tetap selalu positif kak, sukses kuliahnya!"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "kakak seruuu",  
                "pesan":"semangat terus kuliahnya kak keren!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Abang kerenn jago futsal",  
                "pesan":"semangat terus kuliahnya bangg!"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Musik",
                "sosmed": "@sarahwsti",
                "kesan": "kakak lucu seru",  
                "pesan":"semangat terus kuliahnya kakk!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19 Tahun",
                "asal":"Natar",
                "alamat": "Pemda way huwi",
                "hobbi": "main rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak imut santai",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1175GFNP7f1S8emUKK5XYgv_EAXp8W4Ci",
            "https://drive.google.com/uc?export=view&id=1rCRi1XMX3Hn0f-FVYQ35R45wrGmRo7QU",
            "https://drive.google.com/uc?export=view&id=1NefwF7rIym6cBPfBMy9lcG5Mk0__1I_U",
            "https://drive.google.com/uc?export=view&id=1aabiNMbNnHR_KBih_IehPqtak3J1_ZKQ",
            "https://drive.google.com/uc?export=view&id=1BrpA5eGjjUzw_l2YzyW2aD-a47Kmf_of",
            "https://drive.google.com/uc?export=view&id=1T5Fuhb-4I-L6tu1g6Oonkp7FaAFDv8yb",
            "https://drive.google.com/uc?export=view&id=12jHF1t1Upb9UQLA0HeM2luOzD0jVAG96",
            "https://drive.google.com/uc?export=view&id=1Bc4I9NEab7B05rVKn4LMU-iHX3SC6huM",
            "https://drive.google.com/uc?export=view&id=1-snYPaCiZhbBE_t3ALz14GUjWgtg5aq8",
            "https://drive.google.com/uc?export=view&id=1tXKeJaV-seQDwHU35I-q-wa3Q5uUMm8c",
            "https://drive.google.com/uc?export=view&id=1i-yWCgV3QOpmTokn_canOh9e9UTAqb_n",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Bisnis Startup, Jogging",
                "sosmed": "@dananghk_",
                "kesan": "Abang keren role model banget",  
                "pesan":"semangat terus bang berinovasinya!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum, foto-foto pemandangan",
                "sosmed": "@den_iki__",
                "kesan": "Abang cool kece abiez photogenic",  
                "pesan":"stay cool bang!"# 1
            },
             {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik abis!",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
             {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini lucu dan seru",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
             {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Joggin juga",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak ini asik, seru",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang kalem, baik",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
             {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg perwira 2",
                "hobbi": "Nonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak ini asik lucu seru",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kakak lucu santai",  
                "pesan":"semangat terus masaknya kak!!!"# 1
            },
             {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak baik, lucu dan seru",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ald94QcctQ6JlFnJ_oOT_LIWtIW3HNX9",
            "https://drive.google.com/uc?export=view&id=1WIkrTH-WjPzAexHYXU5eyjnyrD3qNTeQ",
            "https://drive.google.com/uc?export=view&id=1_3Ol7Xef1TL5Fij4-pdqbBPoWwXvFghw",
            "https://drive.google.com/uc?export=view&id=1YkL59IhM5ePxszHxcp6uJiu8MIRs2OF3",
            "https://drive.google.com/uc?export=view&id=1ZEcnjcSTxDAKuABjDRg8911fmgZtgEh5",
            "https://drive.google.com/uc?export=view&id=1cw8jYdel_5YfDskHQVhL8lANWvQipsq7",
            "https://drive.google.com/uc?export=view&id=1yM5K1Zb4BGNr4iXLJFayoWlfu8wPLvRD",
            "https://drive.google.com/uc?export=view&id=1UEX3zbMCggJofUepVgMu2KP45zhr787I",
            "https://drive.google.com/uc?export=view&id=1T9myGuGyV00Lk5f2HqyYIUOB6v8NZW5b",#
            "https://drive.google.com/uc?export=view&id=1Uf-zK-HL4PmHkGa581sobSMLOz43dz7F",
            "https://drive.google.com/uc?export=view&id=1__oqyTW33Vnqodxtn7zYnSuCk7CuBVYN",
            "https://drive.google.com/uc?export=view&id=1VV5c60JxlFoGBZqtLYxTXb7L1q4jc-pW",
            "https://drive.google.com/uc?export=view&id=1VoY0t2buMyOQZqn5ey8TEhwvVzJla82J",
            "https://drive.google.com/uc?export=view&id=1a3zcfZmNHShJethpr3IIzUvRxfuwx1Uo",
            "https://drive.google.com/uc?export=view&id=1XL0vKwjBwYFQ53kLDrwQS9InN1HkMMfK",
            "https://drive.google.com/uc?export=view&id=1XpOknw09eY9kGV4Pv8xPv6N4VjfyhOfH",
            "https://drive.google.com/uc?export=view&id=1cJaZGGBGwh4co39c3jm5RiNUnRTxr5Sb",
            "https://drive.google.com/uc?export=view&id=1bG-Yxmd2H5Me-mID1atqZAncaP-CKRVG",

        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jati Mulyo",
                "hobbi": "Sleepcall",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak cantik, slay, seru, dan energik",  
                "pesan":"semangat terus jadi kadep nya kak patricia!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jl. Kresna Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini seruuu!",  
                "pesan":"semangat teruss kakak rahma!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard & Volly",
                "sosmed": "@mananam_",
                "kesan": "Abang Kadiv cool & kece abiez",  
                "pesan":"Sukses terus bang!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik & fotografi",
                "sosmed": "@noerruu",
                "kesan": "Abang kece dan fotografer abis",  
                "pesan":"Semangat terus bang jadi pdd buat HMSD ADYATAMA!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Abang Gokill dan keren parah!",  
                "pesan":"Semangat terus bang & Sukses terus!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak imup & Seru",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {   
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak kadiv kece dan keren abiez",  
                "pesan":"semangat terus jadi kadivnya kak!"
            },
            {
                "nama": "Aliya Anmara Amanta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammra",
                "kesan": "Kakak cantik & Calm",  
                "pesan":"Keep positive dan semangat terus kak!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini asik & pintar",  
                "pesan":"semangat terus kuliah dan jadi astut nya kak!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kakak slay, dan keren",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak cantik & kece",  
                "pesan":"Tetep Kece terus kakk!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumateraa Barat",
                "alamat": "Jl. Lapas, Kecamatan Jati Agung",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa_",
                "kesan": "Kakak cantik dan keyenn",  
                "pesan":"Semangat terus kak semoga tercapai segala cita-citanya!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak baik, dan keren",  
                "pesan":"semangat terus main robloxnya kak!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangg kadiv terkeren, kece & cool abiez",  
                "pesan":"Semakin mengudara dan semangat terus bang!!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kerennn banget pokoknya kaka ini",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
                        {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kakak kece dan vd banget!",  
                "pesan":"semangat terus nge-designnya kak!!"# 1
            },
                        {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kerennn & kece banget designnya kakak ini",  
                "pesan":"semangat terus kuliah dan sukses terus kak!"# 1
            },
                        {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "KAKAK VD TERKEREN & SLAY & KACIW & DABESTT BANGET DEH POKOKNYA!",  
                "pesan":"SUKSES TERUS KAK, MAKIN JAGO DESIGNNYA, SEMANGAT TERUS KULIAHNYA KAK!"# 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
       

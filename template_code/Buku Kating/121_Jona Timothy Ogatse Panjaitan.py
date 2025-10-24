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
            "https://drive.google.com/uc?export=view&id=1ersYC41EzUcmhnFkCd4LdvgE0atwPgrX",
            "https://drive.google.com/uc?export=view&id=1uYS99TFP5iLi6IQi07CO0NeiSXYjAWaX",
            "https://drive.google.com/uc?export=view&id=1vSZavk3c1P3QZzb_Nru4gS_qknwfGF9O",
            "https://drive.google.com/uc?export=view&id=1gO-PNnMtcwMI8gys-wl26febkqjdYpRq",
            "https://drive.google.com/uc?export=view&id=1a2TybyYYAXrbLxtbMmKP5hegOh98EBbO",
            "https://drive.google.com/uc?export=view&id=11tb9CjPYxurUCz4xo6IXpKyYP02u72de", 
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
                "kesan": "Abang Rendra asik, tegas, suara nya merdu",  
                "pesan":"Your voice guides us and leads ut toward the future"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL!",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Gaya berbahasa bang Jo mudah dipahami, to the point",  
                "pesan":"Don't let that fiery spirit ever die out"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Badui",
                "alamat": "Ayrest Kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini lucu humoris, ramah dan seru",  
                "pesan":"jangan sering sering nahan kak, semakin di tahan semakin sakit"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza keren, enak diajak ngobrol",  
                "pesan": "kapan kapan kita ngobrol santai lagi ya kakk"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty kalo ketawa terlihat sangat tulus ",  
                "pesan": "jangan sering sering di tahan kak, terkadang harus di lepaskan"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini terlihat paling dewasa, kalem",  
                "pesan": "semoga suksess terus kak mengejar mimpi kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VRsUO6OdFYUJ54m3PVw4Y2mA98zdRXaw",
            "https://drive.google.com/uc?export=view&id=1C3xoTmGTHwJOAoyYFBs7k4blZAmE6WV8",
            "https://drive.google.com/uc?export=view&id=1dcxC22iqCB0aPfXcDKaXCe1l-9f4dtoK",
            "https://drive.google.com/uc?export=view&id=193eg3mYdH7b_sMcxFOXHH3ucCk0rD61p",
            "https://drive.google.com/uc?export=view&id=1_2xIpEvbytRgZKfnBnoa78TOMK_58a66",
            "https://drive.google.com/uc?export=view&id=1YDaZfC9hlByQBOrFhb7PIEBxvzo1Y8Ve",
            "https://drive.google.com/uc?export=view&id=1yvt9sePrl4KjNtRsLFUfGQ8o3wiXexh2",
            "https://drive.google.com/uc?export=view&id=1yoWBU9vT2Hq3ach0AixQLR5xAyb-VaK_",
            "https://drive.google.com/uc?export=view&id=1DSBI-WPC9lPRcV9YNI1WvMEepMYMbsvV",
            "https://drive.google.com/uc?export=view&id=1QjapiAFm3-ASR7ygTgcO0ke2sjJKAcJC",
            "https://drive.google.com/uc?export=view&id=1kKDavoR1-ow42Tei3ztVOmivFyQP3D0a",
            "https://drive.google.com/uc?export=view&id=173fkv77i4PWoklyJsl9_veaaX4KQmz_l",
            "https://drive.google.com/uc?export=view&id=1mmZKoTEmj0jtcS0Z188CDX38dzyHyaiQ",
            "https://drive.google.com/uc?export=view&id=1nkpGBmsQWTAdcRMvj_j2okbYXdG7Rk7y",
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
                "kesan": "Abang terasik, terseru, bisa diajak bercanda dan respon nya asik",  
                "pesan": "Every small step counts"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea lucu, kadang bisa keliatan galak, humoris",  
                "pesan": "The roar of thunder"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "kak renisha humoris, ramah",  
                "pesan":"langgeng terus ya kakkk"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya keren, humoris",  
                "pesan":"apa yang kakak tabur, itu yang kakak tuai"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Pinter,stylish, keren, dan humoris",  
                "pesan":"learn form yesterday, live for today, hope for tomorrow"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini keren, lucu, rambut nya berwarna",  
                "pesan":"In the middle of difficulty lies opportunity"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "mentor te debasttt, keren, soft spoken, peduli",  
                "pesan":"kurang-kurangin brainrot nya bang, langgeng terus ya bangg"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang cool, keren, asik, vibes nya kek mc ghibli gitu bang keren",  
                "pesan":"You never fail until you stop trying"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Catur",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini lucu, asik, bisa diajak brain root",  
                "pesan":"Hadapi dunia ini tanpa gentar"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandiama",
                "alamat": "Way Huwi",
                "hobbi": "Minum air putih 8x sehari",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini bagaikan bintang",  
                "pesan":"keep your light alive and let it shine brighter"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Nyanyi tabola bale",
                "sosmed": "@iamridhomanik",
                "kesan": "abang ini suara nya bagus, humoris",  
                "pesan":"kapan kapan ayo nyanyi bareng bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Koleksi Stiker",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini chill, bucin",  
                "pesan":"semangat kuliah nya bang dan langgeng terus ya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Papua Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini lucu, polos",  
                "pesan":"be yourself dan semoga sepat jadian ya kak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik, seru, dan kadang keliatan lesu",  
                "pesan":"semangat terus kakk, jangan lupa istirahat ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UmucDnI-fhDhvyoOhf5TIUmdBbwVPT0U",
            "https://drive.google.com/uc?export=view&id=1Dk3NTLc6ihCCZREml8RL_j7vxzzHUT18",
            "https://drive.google.com/uc?export=view&id=1kzlYL-GEhYQmuL4J9NcZh0yENWJ7P6-T",
            "https://drive.google.com/uc?export=view&id=1va7S3uGFI77M16g7SKXSA_RFHH9Q5oCs",
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
                "kesan": "Abang kalem, nyantui, asik",  
                "pesan":"sesuai nama abang, jadilah bintang yang menghiasi langit"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu, maen roblox",
                "sosmed": "@nadyaanjanani",
                "kesan": "Kakak ini baik, ramah, murah senyum",  
                "pesan":"semangat terus kuliahnya, dan langgeng terus ya kak hehe"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Ice Skating",
                "sosmed": "@fathinahazzh",
                "kesan": "positive vibes, baik, pinter",  
                "pesan":"lakukan sesuatu dengan sungguh sungguh dari hati kakak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "humoris, baik",  
                "pesan":"semua bisa karena terbiasa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O3DPwHjIS2VYS3U2ha4o2gdRiWf5mfEI",
            "https://drive.google.com/uc?export=view&id=1kcGya4sX8OvfYKW3Yqkuxig5Ta6Bzeve",
            "https://drive.google.com/uc?export=view&id=119pxABv-SFEttLHUuHH0hNOlDOWYtMDh",
            "https://drive.google.com/uc?export=view&id=19tC7capPH5sG7qjhX49YJzdaCXYPmtmR",
            "https://drive.google.com/uc?export=view&id=1CURe5iY90s59ZQv1zP9tSWH_xNTzi_iQ",
            "https://drive.google.com/uc?export=view&id=1eXBq1LotnuFgbkFXGGPbfhI-dPqB8K-j",
            "https://drive.google.com/uc?export=view&id=1fdTK7fpiMmB9GNp4BkIGjesGSYd8PQER",
            "https://drive.google.com/uc?export=view&id=1zElRVp6l3NRq244uniZ-s-yWa8iYjUOG",
            "https://drive.google.com/uc?export=view&id=17538iGIxjxVTfaCXEZfn8Vgb8SKnDNwn",
            "https://drive.google.com/uc?export=view&id=1I0iknMy7mhld96z_8Mop1vq8qx23q0Yo",
            "https://drive.google.com/uc?export=view&id=1Or1nhpiDEv178xexHQ8u_TXyboRoX4VL",
            "https://drive.google.com/uc?export=view&id=1ocQieYVpdVyIUb7UQ30PBcH8iRqaAQQI",
            "https://drive.google.com/uc?export=view&id=1v6CwcfM7ymZnEUormjPTm8ogHUWfchPG",
            "https://drive.google.com/uc?export=view&id=1va67dDpxhRqp0wRPq24NVojuou4OErxX",
            "https://drive.google.com/uc?export=view&id=1Mytjbd2X6hP2tswWo6UWIRrgu3Y6xj57",
            "https://drive.google.com/uc?export=view&id=1z-tF063ahTEJ64OnzGGj48XM8vlHZypt",
            "https://drive.google.com/uc?export=view&id=1K8somB2PjgKTRxJ_7HEDfJSAuiCybBIx",
            "https://drive.google.com/uc?export=view&id=1Hs3EFJ0F4dPrhJBm1AD_mjI4bG2JEqZ-",
            "https://drive.google.com/uc?export=view&id=1Fr-W9d3GWspwqPB0NvsPMuoY9mAdgku8",
            "https://drive.google.com/uc?export=view&id=1nrEt_ydIsJnmJS3k0BuKMC2jO0tebsbq",
            "https://drive.google.com/uc?export=view&id=1LSn0GVfsZjIXLvYUqFWeXwv11y0ni0b8",
            "https://drive.google.com/uc?export=view&id=1RYe6d2nf3ZrA69zaFwVQZOtcFw0i2QLB",
            "https://drive.google.com/uc?export=view&id=1I_z6SBKr0dFCtLLigdB-kPu8hbDDFpLV",
            "https://drive.google.com/uc?export=view&id=1NuBDQV6QT0AyPq9CL8RqUbwga3x7H2Hw",
            "https://drive.google.com/uc?export=view&id=1R2uK4amZ4nzi7aoYfwfF3GRzJ49VKKAn",
            "https://drive.google.com/uc?export=view&id=1oESgCcvOBcMjf_OUWG33oFvK3mqnlMPW",

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
                "kesan": "Abang tegas, humoris, berwibawa",  
                "pesan":"semangat terus bang, nikmati setiap proses nya"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"bekasi",
                "alamat": "Korpri Sukarame",
                "hobbi": "Jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak baik, cantik dan imut",  
                "pesan":"satu momen kecil juga berharga"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Tegas, berbicara hal yang perlu, mirip mama saya",  
                "pesan":"progres itu seperti mendorong roda, berat diawal namun setelah roda itu berputar akan terasa ringan"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "baik, humoris, berbicara to the point",  
                "pesan":"buat lah mmimpi setinggi langet, kejar mimpi walaupun terasa hati mulai menjadi pahit"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "tegas, ber style",  
                "pesan":"The only source of knowledge is experience"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Isengin Jona",
                "sosmed": "@daffahdynn_",
                "kesan": "sangar, baik, bersemangat",  
                "pesan":"rambut nya jangan di potong ya bang"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "peduli, tegas",  
                "pesan":"To raise new questions, new possibilities, to regard old problems from a new angle, requires creative imagination"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "cantik, baik",  
                "pesan":"semangat terus kuliah nya kak, masih banyak rintangan ke depan nya"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abang cool, aura nya dingin, jago koding",  
                "pesan":"Know yourself and love yourself"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Tegas, berwibawa, pintar",  
                "pesan":"Science without religion is lame, religion without science is blind"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang Berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "baik, lucu, humoris",  
                "pesan":"tetap semangat kak, semua yang kakak lakukan akan menjadi memori indah yang akan kakak kenang"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "keren, atletis",  
                "pesan":"kapan kapan main bultang bareng lagi bang, abang juga semangat terus main bultang nya"# 1
            },
            {
                "nama": "ALi Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang 4 Nangka Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "kalem, kadang terlihat lesu",  
                "pesan":"semangat terus bang ali, jangan lupa istirahat"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini kalem, chill, lucu, humoris",  
                "pesan":"panjang sabar ya kak"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way kanan",
                "alamat": "Untung",
                "hobbi": "scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak lucu, seru, santai, easy going",  
                "pesan":"never look back if you have nothing to regret"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakak ini asik, humoris",  
                "pesan":"jangan sampe putus semangat nya kak, kapan kapan main roblox ya kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "Asik, cool, easy going, enak diajak ngobrol",  
                "pesan":"kapan kapan kita ngobrol santuy bang bareng yang lain"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_",
                "kesan": "Aura farm(dalam hal yang baik), nyantai, baik",  
                "pesan":"jalani perkuliahan ini dengan semangat yang membara ya bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "imut, cantik, tarian nya bikin terpukau",  
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
                "kesan": "Abang Chill, enak diajak bercanda, tegas",  
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
                "kesan": "Abang ini gaul, humoris, kadang keliatan lesu",  
                "pesan":"ga sabar liat abang tanding bawa nama prodi"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "asik, nyantai, baik",  
                "pesan":"semangat terus kak kuliahnya, menyala kakak ku"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "nyantai, humoris,baik, enak diajak berbincang",  
                "pesan":"Kapan kapan kita main badminton lagi bang"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main futsal, voli",
                "sosmed": "@sidabutar.26",
                "kesan": "humoris, baik, murah senyum",  
                "pesan":"buat lah orang tersenyum dengan gaya abang"# 1
            },
            {
                "nama": "Wuliano Wiliam Purba",
                "nim": "123450098",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngoding",
                "sosmed": "@liano.wlm",
                "kesan": "Aura farming, baik, peduli, tegas",  
                "pesan":"jaga kesehatan bang"# 1
            },
            {
                "nama": "Rewina Audiya Melvasari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Ratu dibalau",
                "hobbi": "Gambar doodle",
                "sosmed": "@rewinanaaa",
                "kesan": "lembut, baik, imut",  
                "pesan":"tetap jalani jalan yang sudah kakak percayai"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RhuCpxphWBRICUs_c4n8fVPyjhj7uIZa",
            "https://drive.google.com/uc?export=view&id=1AdRZj0kvJrgllJ8UJ5fqDGMR2vMPkyCE",
            "https://drive.google.com/uc?export=view&id=1FT6y865VEbQaZbP_bY1DpHUaU1FNaPuA",
            "https://drive.google.com/uc?export=view&id=1VVhOrqveWzlm4MBB8-_DbF0JyAdMqKY6",
            "https://drive.google.com/uc?export=view&id=1vj7-YdurEZ92KZyodaOnmhaYGC9n4txH",
            "https://drive.google.com/uc?export=view&id=1hxz99opNbPa0dfRpQQy9vyS-OQxeVgy4",
            "https://drive.google.com/uc?export=view&id=1zMhUotz3m4ZP5jkL0Pipcrvm9y2zXn9N",
            "https://drive.google.com/uc?export=view&id=1gmS-XoMidlLDhjBe3UWS98TvALGU2iId",
            "https://drive.google.com/uc?export=view&id=1S_iGOWCzzBT4UinGBtYDPDBnb2K-UWPu",
            "https://drive.google.com/uc?export=view&id=1vYrxRA51gyzxXSTXu7kLMJVDxSxK-szG",
            "https://drive.google.com/uc?export=view&id=1vHKIloIBLB7-_7N8JeF7rEkfUSiB5z2W",
            "https://drive.google.com/uc?export=view&id=1Ily8K3z8uPGUC-hoQ_p2zz7VvL2Wi5XQ",
            "https://drive.google.com/uc?export=view&id=1QiTk0p7xYhefyT2PA12CsA-h-Z29_0C2",
            "https://drive.google.com/uc?export=view&id=1-gQj5MR4oxFuVHCptimimASPUT2DVQD8",
            "https://drive.google.com/uc?export=view&id=1WiVUdYj9T0PuiIfrTGjtmW2nOfB2kaCE",
            "https://drive.google.com/uc?export=view&id=1Q2G5uLD9vDgO2t_gu8JX8ut-9qd3ETd_",
            "https://drive.google.com/uc?export=view&id=1EOUU7gWCCkYzv8cLVJj9nuHI1af2JfNu",
            "https://drive.google.com/uc?export=view&id=1IRKhKSKrlzex99E66xItjsYePhD65wkw",
            "https://drive.google.com/uc?export=view&id=1eC0Y_g5fBL4UnXfaDdLw2D1dBMrK3azf",
            "https://drive.google.com/uc?export=view&id=1H09JXdtjnhCpURjS54Y9uO320jHh8cS8",
            "https://drive.google.com/uc?export=view&id=1mAjiqP-HE2bjBAD0WOHNRFgQ2Q0LlgdN",
            "https://drive.google.com/uc?export=view&id=1sg_B8vTuSPLotoY8FdmxLyMyZSFix7vO",
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
                "kesan": "Abang santai,berjiwa kepemimpinan, seru, asik",  
                "pesan":"cepat jadian ya bang"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Kakak ini baik, ceria dan seru",  
                "pesan":"tetap semangat menjalani kehidupan"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "selera musik bagus, berwibawa",  
                "pesan":"mau minta playlist spotify nya bang"# 1
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishashi",
                "kesan": "Kalem, enak diajak ngorbol",  
                "pesan":"tetap pede dengan diri sendiri ya kak"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilafarizzii",
                "kesan": "jadi contoh abang yang baik",  
                "pesan":"terus kembangkan apa yang sudah abang mulai"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Nyantui, asik, humoris",  
                "pesan":"latih terus skill abang"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik, nonton",
                "sosmed": "@notfall.s",
                "kesan": "Kalem, muka datar(mungkin karena habis pulang kuliah)",  
                "pesan":"semangat terus bang jaga kesehatan"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak ini berwibawa, tenang orang nya",  
                "pesan":"semangat terus kak, ingat masih banyak mimpi yang kakak kejar"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "ceria, asik, multitalent",  
                "pesan":"jangan lupa menyeimbangkan skill akademik dan non akademik kak"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abang chill, humoris, cool, sigma abis",  
                "pesan":"Selamat sudah dapat kos yang terbaik buat abang"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "imut, asik, seru",  
                "pesan":"nonton drakor jangan sampai tugas nya kelupaan ya kak"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "baik, asik diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kakak semoga semester ini bisa di tingkatkan dari semester sebelum nya"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakak kalem, murah senyum, penyayang",  
                "pesan":"tempa terus diri mu kak, semakin di tempa semakin kuat juga"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kalem dan asik",  
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
                "kesan": "ceria, heboh, asik, antusias",  
                "pesan":"jangan pernah berubah sekuat apapun dunia membuat kakak jatuh"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "style rambut nya bagus, sepuh coding",  
                "pesan":"maju terus tanpa gentar bang"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Baik banget, pengertian banget",  
                "pesan":"semangat terus kuliahnya kak, jasa mu ga bakal aku lupakan kak"# 1
            },
             {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@i",
                "kesan": "Abang kece abis, sigma, gigachad, santuy, humoris",  
                "pesan":"kasih paham bang kedepan nya"# 1
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "pinter, kalem, gamer",  
                "pesan":"tugas kuliahnya jangan sampe kelupaan bang"# 1
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
                "kesan": "Kakak ini asik, baik, dan penyayang",  
                "pesan":"bikin cinematic ke embung kak sekali kali"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "vibes nya udah dewasa banget, tenang, berpengalaman",  
                "pesan":"makin hari harus makin baik bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w_Nf8k90iM-qvBDSOVf9AOIlq7oe1Bz6",
            "https://drive.google.com/uc?export=view&id=18H0_f50diRiEXWRU-7Z9CXIKlaNTEW7i",
            "https://drive.google.com/uc?export=view&id=12mDto_nA5pnz4G4KIx9gRG-nopt5GiSV",
            "https://drive.google.com/uc?export=view&id=1E0by_E6KJdQTNo0X9mtDGdGozmHchhwK",
            "https://drive.google.com/uc?export=view&id=1fLN_Uwa2Wj0hR2bXiyt3Sjmc3Oa9Ph5f",
            "https://drive.google.com/uc?export=view&id=1riUdmGLbuR4QHZiq4KBVbUj5-jYV_Eu3",
            "https://drive.google.com/uc?export=view&id=1VpF-1Yj_wenjOFcB1H0WZup5TBxkyULK",
            "https://drive.google.com/uc?export=view&id=1bgbLa7kxvSol2_8MgpBfe0KPq2GGJoV3",
            "https://drive.google.com/uc?export=view&id=12whH-UfimrWWx-ki7XciWvQrgIa0BZl9",
            "https://drive.google.com/uc?export=view&id=1iyEgWkd1VLYMeuG0K8-_cQRCZWRyBIiB",
            "https://drive.google.com/uc?export=view&id=1AnUIQ-OjrPfYXtdI4OB91G3-uYPB6Jpy",
            "https://drive.google.com/uc?export=view&id=1BXP6Ul0FeyWRr85KM6e0DsPy6Ugycalx",
            "https://drive.google.com/uc?export=view&id=1Hi99G0bv08KyHezEbBN15UVMniGCdYnq",
            "https://drive.google.com/uc?export=view&id=11DWlg6n8T_5R60K2oBeNwEqj6i8wbsQX",
            "https://drive.google.com/uc?export=view&id=1-_75HvNhS1tNThyef92_ekfIm3nRv-I_",
            "https://drive.google.com/uc?export=view&id=1aSZ3pYtGKb9jj7nxnaIZaSHPp18e_rq6",
            "https://drive.google.com/uc?export=view&id=1hpERHgJ_u5MxNU5gGfO7Pm6XSlQ7TIEo",
            "https://drive.google.com/uc?export=view&id=1poywgX4ahT16LGD2AQDPWNEIqQGFHc-w",
            "https://drive.google.com/uc?export=view&id=1hRbv5f4vblrtodtQzzSu7REq-gnbCZ_W",
            "https://drive.google.com/uc?export=view&id=1jcMJIsnQlALTMUmsX8Rrm4E4Ywn4IJl0",
            "https://drive.google.com/uc?export=view&id=1rTFu_5ILS5QCLWXG2QeQ7Z0ezmDMUqFU",
            "https://drive.google.com/uc?export=view&id=14tyiiyB-HNLRFnKbo3CuTn9G_0KIqxwO",
            "https://drive.google.com/uc?export=view&id=1xxf9QBiH5hXH7PiTBKMfXfeYWfk5kGmT",
            "https://drive.google.com/uc?export=view&id=1DiKhU1TJkqshVYfvZQQ6UM4PvuUIrExF",
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
                "kesan": "berjiwa kepemimpinan banget, tenang menghadapi masalah",  
                "pesan":"if you only focus on a single tree, you will end up losing the forest"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "manis, baik, asik, pinter",  
                "pesan":"semoga ilmu yang kakak pelajari dapat di aplikasikan dalam kehidupan kakak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "positive vibes, senyum nya bikin candu",  
                "pesan":"Semangat terus dalam kegiatan akademik dan non akademik"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "gokil,o seru, asik, peduli",  
                "pesan":"tidak ada jalan yang selama nya mulus, tapi kakak harus bisa menyesuaikan diri"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "green flag, kalem",  
                "pesan":"imajinasi harus tanpa batas"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak seru, baik, imut",  
                "pesan":"semangat kuliahnya kak, jangan sampe kecapean kak main main nya"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "pinter, calon peneliti",  
                "pesan":"semangat nyari dataset nya kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "cantik, kalem, ukhti vibes",  
                "pesan":"nikmati setiap momen dalam hidup ini kak"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "senyum nya identik, baik, peduli",  
                "pesan":"jadilah bunga yang dapat bertuhmbuh walaupun tanah nya tidak subur"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak lucu, kalem, terlihat dewasa",  
                "pesan":"semoga dalam tidur kakak bisa mendapat kebahagiaan"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya cantik banget, baik banget, keren banget dutanya!",  
                "pesan":"Semangat terus kak dutaa & kuliahnya jangan sampe berhenti di tengah jalan"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya lucu, baik, optimis, asik, keren ",  
                "pesan":"Semangat terus dan YAREEEUUUU"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "meskipun terlihat galak tapi orang nya baik dan lucu, tegas",  
                "pesan":"Coba jangan terlalu ketat bang saat ngobrol.. berasa banget tegang nya ;)"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak baik, asik, seru",  
                "pesan":"walaupun bahyak rintangan ke depan nya, terus lah melangkah maju kak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakak baikk, asik, seru, jahil",  
                "pesan":"Semangat terus kak kuliahnya, jangan kuat kuat ya kak nyubit nya"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "kalem, sigma",  
                "pesan":"sigma terus bang kalo bisa sampe giga chad"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Abang gacor, cool abiez, asik, humoris, murah senyum",  
                "pesan":"Terus jadi abang terasik dan tergacor bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Asik, baik, lucu",  
                "pesan":"jangan sampai keteteran menghadapi dunia ini kak"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "baik, kalem, cantik",  
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
                "kesan": "dance nya keren banget, optimis",  
                "pesan":"maju terus kak, jadi lah orang yang bisa terbang terus dan bebas di langit"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "sangat menyayangi diri sendiri, asik, baik",  
                "pesan":"Semangat terus kak kuliahnya dan terus cintai diri sendiri"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "peduli dalam proses, perhatian, baik",  
                "pesan":"Semangat terus kuliahnya kak dan terus berkembang dalam baking nya kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "sigma, chill, humoris",  
                "pesan":"Semangat terus kuliah nya bang, jangan boros bensin bang, sekali isi bisa sekali makan nasi bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "cantik, dewasa, tenang",  
                "pesan":"Semangat terus kak dalam menjelajah karena hidup ini adalah petualangan"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Xa9j3iQ30beeNQTFFhMRqLrhY2I7d-Tu",
            "https://drive.google.com/uc?export=view&id=1gMDdBDHXOnG3efvV7KR1zVD7r7OuhcvT",
            "https://drive.google.com/uc?export=view&id=1DmtFYR2EGrz5R027haKRMGcHS4tQGwtn",
            "https://drive.google.com/uc?export=view&id=1uy3sQjaGTyJ4st1Jnp_QnItPNMR3knrp",
            "https://drive.google.com/uc?export=view&id=13rTQebtl7j9fqu84S175VHkrVEyD1FTo",
            "https://drive.google.com/uc?export=view&id=1VafnW4dBx0lMsYW9rNuXQ2TRjkFVgoKS",
            "https://drive.google.com/uc?export=view&id=1aFyEpCqt2vqH77Q7iYAaYgXYwYDOyqLU",
            "https://drive.google.com/uc?export=view&id=18ENHdfLpcP52rX7b81V6J-HxqegPzIDl",
            "https://drive.google.com/uc?export=view&id=1Q9eXvxVagvNyJWajSat2YsRHUfrFwTPX",
            "https://drive.google.com/uc?export=view&id=1ZDL0crNcOHcBGFI82ZGWfbLC2JEaL-r3",
            "https://drive.google.com/uc?export=view&id=1a7qIGQp-opyv8IADm4EO8HH6DwEPxoDo",
            "https://drive.google.com/uc?export=view&id=171ZQEpifRAPeT4rfwSQtoLxWq4LBLK7f",
            "https://drive.google.com/uc?export=view&id=1kmTbdnrsO3nSFnH7ia4f3BDLvI_-hnuU",
            "https://drive.google.com/uc?export=view&id=15065p7cknA2Hdw9LW9NjEaBdRMuK2Iet",
            "https://drive.google.com/uc?export=view&id=1PFXmpiyv9-X6yXhWs7vopSjcy5i3Y0sB",
        
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
                "kesan": "Ceria, seru, asik, peduli, beriman",  
                "pesan":"apapun yang dilakukan harus selalu melibat kan Tuhan"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "rambuts nya bagus mirip mama aku, baik, imut",  
                "pesan":"kapan kapan ajarin aku mancing kak, pengen ngobrol juga bareng yang lain"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@sal_fhn",
                "kesan": "focus pada 1 poin, teliti, kalem, baik",  
                "pesan":"semangat terus kuliahnya kakak, seperti memanah yang memastikan anak panah mengenai target nya"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "berjiwa kepemimpinan, tenang, kalem, pintar, suara nya merdu",  
                "pesan":"learn from yesterday, be better for tomorrow"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "baik banget, asik, seru",  
                "pesan":"memasak perlu menggunakan perasaan, jalani semua kegiatan kakak dengan perasaan positive"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "sangar tapi baik, style rambut nya keren, sigma",  
                "pesan":"terus kejar mimpi mu bang, selaju dan secepat kilat"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "baik, lucu, seru",  
                "pesan":"semoga baking nya dapat terus berkembang, terus berlatih kak"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "baik, keren, tegas",  
                "pesan":"kejar semua mimpi kakak yang kakak mulai dari ITERA ini"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "Abang kalem, terlihat kurang tidur,baik",  
                "pesan":"semangat terus bang dalam tiap langkah abang jangan lupa istirahat"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatriaaa",
                "kesan": "santai, senyum nya berseri, pinter, atletis",  
                "pesan":"semangat terus kuliah nya dan terus jaga kesehatan dan tetap konsisten olahraga nya"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "paling asik, paling ceria, paling seru, gacor, humoris, antusias",  
                "pesan":"tetap jadi diri kakak mau apapun yang terjadi kedepan nya"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "anak musik abissss, ceria, baik, seru",  
                "pesan":"terus kembangkan skill kakak, jangan sampai stuck di kondisi yang penting bisa tapi harus sampe khatam"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "sosok asli chill guy, baik,",  
                "pesan":"semangat terus kuliahnya bang, dan harus tetap optimis"# 1
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
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Musik",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak imut, cantik, senyum nya candu, kalo senyum mata nya juga ikut senyum",  
                "pesan":"semangat kuliah nya dan semakin jago main keyboard nya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aMY0eRFJkdcRCe3R1zsvoR_8ehw57LD-",
            "https://drive.google.com/uc?export=view&id=1Sm3vGkrRrOlQpII22w6pIxHiZ-fhEr-H",
            "https://drive.google.com/uc?export=view&id=1NvSnix4WMh1D2_dFAWZESyLEDdZRjbbc",
            "https://drive.google.com/uc?export=view&id=1nMpsOBKLSwiwNiXqoqHLbRUaH7ekBOs8",
            "https://drive.google.com/uc?export=view&id=18yhVrXAtHEnFUwWiegpVrVdg9eyFV5-e",
            "https://drive.google.com/uc?export=view&id=1O563_h0hvIlOcb4ZnJZKWqpViacNvG_d",
            "https://drive.google.com/uc?export=view&id=15tzqWB3JQO4BI6sGpfm_lu2mcftE17Da",
            "https://drive.google.com/uc?export=view&id=1OLzvJBF0O0ZU0nXdbpkelePdV3PgG9wl",
            "https://drive.google.com/uc?export=view&id=17mqau5m06ZNKAOVNwyhUAL-AKP3hF5l6",
            "https://drive.google.com/uc?export=view&id=1ppZVedTbLlij8q3eF_u-63QgntytTIhl",
            "https://drive.google.com/uc?export=view&id=1_4XUrxFPT7ClPXpJxg-ZEpoKlBlQJsI1",
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
            "https://drive.google.com/uc?export=view&id=1VCgegoLdgdZsaoMQQ3idoyShTJFfsuQv",
            "https://drive.google.com/uc?export=view&id=1Zfq-Pp6SWVBfmVb4sTxSqc4AGbZBKI_X",
            "https://drive.google.com/uc?export=view&id=1IxHIHPSn8eXs32jaHITt8Z-1jSM9lxRG",
            "https://drive.google.com/uc?export=view&id=1q9S6zZw19UAqeFShJih6EEPUOlPfrXFL",
            "https://drive.google.com/uc?export=view&id=1oaw6Hte4qyxU8TvmwQMzXHZ8vRd9rnIB",
            "https://drive.google.com/uc?export=view&id=1bYJDUNf1SKe7F9A0ukjNrDH3MC403RQo",
            "https://drive.google.com/uc?export=view&id=1PGA6Fb7bwBCtMcO8hdMu6tkcCJgTM2sj",
            "https://drive.google.com/uc?export=view&id=112M1DTjBvORaTXWgJ6S-4W1-bdXsGqSz",
            "https://drive.google.com/uc?export=view&id=1w6KOl7WA4GCFqkZjGSGkm6ZrII2pigwA",
            "https://drive.google.com/uc?export=view&id=1jsGoIPIfcEJJtX7VHNzKH736W_RB4f6V",
            "https://drive.google.com/uc?export=view&id=1bKNRqZ9PVKZM6bC3ZXC4Z0qgIHGHdPRt",
            "https://drive.google.com/uc?export=view&id=1OAbZGWZcB7GlGSWbJ-rz6Tmvc4N00M22",
            "https://drive.google.com/uc?export=view&id=1ydCc-cWjhW9MhGoKhgl3A6RKsKV5Zd-G",
            "https://drive.google.com/uc?export=view&id=1p6Cscn3nEGOb69ZLxUu8-bJjsKF0mK-b",
            "https://drive.google.com/uc?export=view&id=1MAqjm4qvpNOCUcnOuvo6YNHUxotJmUNo",
            "https://drive.google.com/uc?export=view&id=1a4Eru20GHRXDvkH1TQfzK-C8kdAaWJHN",
            "https://drive.google.com/uc?export=view&id=1HSa_WhTDVnyHyZPzaYLf1gMdWOag9J3L",
            "https://drive.google.com/uc?export=view&id=12pCpOU8pogjYLzILv2YSNWn9mPSBuZJU",

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
       

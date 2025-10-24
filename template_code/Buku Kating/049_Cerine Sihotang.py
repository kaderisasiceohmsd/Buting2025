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
            "https://drive.google.com/uc?export=view&id=1QS9z1NcE0O6HxgEF5Ic1zmM4Y7eP0QRD",
            "https://drive.google.com/uc?export=view&id=114F5fg0LbUbtdxDuTdCzPXk4SK8vP789P",
            "https://drive.google.com/uc?export=view&id=1Ke724M-V9OyKlZ9m1WhdaHF-3T2Kq45L",
            "https://drive.google.com/uc?export=view&id=1up5y2j88I-Oa6anZfx5Du20qf-8rqgmJ",
            "https://drive.google.com/uc?export=view&id=1Dtb5shbeVw-NwgnS70s_B8zLfa85iVgd",
            "https://drive.google.com/uc?export=view&id=1DHfqTQjW5sLbYldpROxLWPBJUbwaOyRW", 
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
                "kesan": "Abang ini seru Humoris dan seru",  
                "pesan":"Tetap jadi panutan ya bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL!",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Jo kece abisss",  
                "pesan":"Sukses terus bang !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Badui",
                "alamat": "Ayrest Kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak nya ramah banget kalau ketemu, lucu lagi",  
                "pesan":"jangan lupakan kami ya kak adik adik kakak yang imup ini"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak nya ini humble",  
                "pesan":"semangat terus ya kak lopyou"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik banget",  
                "pesan":"jangan lupa makan kak"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini lucu seperti cewe cool yang di drakor",  
                "pesan":"jangan lupa senyum ya kak, senyuman kakak imup banget soal nya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aYrhMi-zsvWUpYcrUDtvOEshLPO0tO4g",
            "https://drive.google.com/uc?export=view&id=15e3uFhs82HwTtS7NQwgrP3uAwcK82fP2",
            "https://drive.google.com/uc?export=view&id=1IW8QxG617yEdjJMKzbX-aoF7n0QNPWF7",
            "https://drive.google.com/uc?export=view&id=1XwTkasTLsoW9VvXBrpLRlA1ip3Xyo2HI",
            "https://drive.google.com/uc?export=view&id=1dERYXSgz-qbC8nhX_6ximqG5oMuuWY5Z",
            "https://drive.google.com/uc?export=view&id=1pqQAzCqkCNH13ZmzyGaEViipKGgAxCq1",
            "https://drive.google.com/uc?export=view&id=1VvAi50WBaBhbNt3o5BldZDtOclQfZOqP",
            "https://drive.google.com/uc?export=view&id=1-8mlR4sf1-9QLmIqsOWl3TBhLQ3dj3n5",
            "https://drive.google.com/uc?export=view&id=1qt-1jwF6wqUNFytFBGjUXEl1VuBqzFJs",
            "https://drive.google.com/uc?export=view&id=1_9UkYb_Wq5xAo_deH5v5AVE-qzCcKil0",
            "https://drive.google.com/uc?export=view&id=10bcCG-gLuYqxnJGWmK4ir9m_Wx-EEmI7",
            "https://drive.google.com/uc?export=view&id=1XRxzXmeZo8LbpE0ZOOZxP8ITX-efB5wi",
            "https://drive.google.com/uc?export=view&id=1dzmfC9I-XJZIVh_HVB6ShjPyen2nQDEA",
            "https://drive.google.com/uc?export=view&id=1Lj7ZN75h6LWj7WmrgVnUupwJ09Fbo22O",
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
                "kesan": "Abang tergacor",  
                "pesan":"jangan lupa bobok ya bang!!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini humble banget, ga jaim sama adik adik nya",  
                "pesan":"jangan berubah ya kak,tetap rendah hati dan inspiratif!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "kak renisha care banget",  
                "pesan":"sukses terus kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya asis dan ramah banget",  
                "pesan":"Semangat terus ya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "abangnya berwibawa banget tapi tetap eassy going",  
                "pesan":"semangat terus bang, jangan lupa ketawa"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini imut banget",  
                "pesan":"sukses teruss kak feby!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "mentor tergacor,seru abiez dan kece,baik banget lagi",  
                "pesan":"makasi banyak ya abang nya udah sabar banget ga pernah marah juga bantu anova dan membimbing kami, aku juga gatau mau balas kebaikan abang gimana, aku cuma bisa berdoa semoga abang di permudah dan dilancarkan rezeki dan akademik nya bang, pokok nya makasi banyak sekebon buat bang gipayo, jangan pernah berubah ya bang dan jangan lupakan adik2 abang yg imup dan meggemaskan, jangan pernah berubah ya gipayo tetap jadi orang baik, semangat bang gipayo kuliah nya dan sehat2 juga ya, sayang bang gipayo banyak  "# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang nya cool tapi asik banget",  
                "pesan":"semangat terus ya bang!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Catur",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini imup apalagi melihat senyumannya",  
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
                "kesan": "Kakak ini ramah banget, cantik lagi",  
                "pesan":"jangan lupa berdoa ya kakk!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Nyanyi tabola bale",
                "sosmed": "@iamridhomanik",
                "kesan": "abang ini seru banget diajak ngobrol",  
                "pesan":"semangat terus ya bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Koleksi Stiker",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini seru, bikin suasana rame dan asik",  
                "pesan":"tetap ssemangat ya bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Papua Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik, imup lagi",  
                "pesan":"sukses terus kak!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini lucu ditambah imupp banget lagi",  
                "pesan":"jangan lupa senyum kak, senyum kakak imup"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vj6nkrzRta5qx982j9EYbfZpCMjkjdPr",
            "https://drive.google.com/uc?export=view&id=1xsRSBHNrPWK9WgAUxMEReeQEthG8KRvS",
            "https://drive.google.com/uc?export=view&id=12D1NNDydqFyaoEGXMqQN6-TFx6iTmQPs",
            "https://drive.google.com/uc?export=view&id=1TgLB-CGTz21BqMbtTwsr154p0Yx-DuxW",
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
                "kesan": "awal nya nyeremin, eh ternyata baik banget",  
                "pesan":"semangat terus bang!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu, maen roblox",
                "sosmed": "@nadyaanjanani",
                "kesan": "kakak nya imup banget, apalagi senyumannya itu",  
                "pesan":"semangat terus kak kuliah nya;)"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Ice Skating",
                "sosmed": "@fathinahazzh",
                "kesan": "",  
                "pesan":"!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "kakak nya ispiratif banget, bikn semangat belajar",  
                "pesan":"semangat terus kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Pa92sc0P9xT3qCjZPiCB1uppHCOFcWCq",
            "https://drive.google.com/uc?export=view&id=1IxfRk-x6M0pgn8bCM9LcgfipN526rdEf",
            "https://drive.google.com/uc?export=view&id=1BcgTdNvIwi0RNhKDk-6H6j9d_wnu45UN",
            "https://drive.google.com/uc?export=view&id=1KOvSDgnsjnuJ6Q9_Q4YsL4S_Q7BSJpdV",
            "https://drive.google.com/uc?export=view&id=1_owUE1XwGF5m_oG7ztW_Eu4ZZI5xW_Gp",
            "https://drive.google.com/uc?export=view&id=1GFZrDAMK60gV2u6d3xNWa3H7nWMpve6L",
            "https://drive.google.com/uc?export=view&id=11IqU5sXiv7iRyWgHjoODoOeDiOk0vfmR",
            "https://drive.google.com/uc?export=view&id=1gOzVidrTSprK-dEX1zsVhsn0rLhDR4Pt",
            "https://drive.google.com/uc?export=view&id=15_-gY8LmkCm50dNodNHX5f9d8S1CRkX4",
            "https://drive.google.com/uc?export=view&id=1i-uiyleCWOEL0iC4S_qMz704U5fsD1oW",
            "https://drive.google.com/uc?export=view&id=1oaCEIME-GHDe7cYaVqFejMPhKqDLi1T1",
            "https://drive.google.com/uc?export=view&id=1HoTrKrqJAiv8AWKjrhNu1hHCYiTxymI1",
            "https://drive.google.com/uc?export=view&id=19NRAtTxu8x8wI9CaWZyDgyot2I0tu1TI",
            "https://drive.google.com/uc?export=view&id=1xxYn6DVdx9NWROngqsULQy5Xh18Pknja",
            "https://drive.google.com/uc?export=view&id=1Fzf3NrhYkTodUhDDYE-7MyRxEXwU5IyA",
            "https://drive.google.com/uc?export=view&id=12sBmD8fS3QA6DlzgXpKc-APmaCboLWHp",
            "https://drive.google.com/uc?export=view&id=1-LO54UW3Yvjd2ZHdfF1m7yhNQcUpIslE",
            "https://drive.google.com/uc?export=view&id=1jkTvfDeCtJD70JF_TbumrPDp2cfPizpk",
            "https://drive.google.com/uc?export=view&id=1tpgPlfIjxkYfaH1OHEigA_0gEB5hczid",
            "https://drive.google.com/uc?export=view&id=1iaztT4FVMQyw3pdHKW1sv4dRLF54Bkrw",
            "https://drive.google.com/uc?export=view&id=1LgPoDkXl8Wl3UUwF7iA3XECjGL8sPQgm",
            "https://drive.google.com/uc?export=view&id=1rvZCSE78Po7LFBY75IJBKpO9tVZsM3KA",
            "https://drive.google.com/uc?export=view&id=1iXF85qv9E84NsdAR9MGWIPvtGbsHio4s",
            "https://drive.google.com/uc?export=view&id=1WWzaVHBKyaaDGQZHYnRJdZ6OIZre3nZa",
            "https://drive.google.com/uc?export=view&id=1Gbgv1zlQIby-_JHWJpxk-SNgQCd_MsOL",
            "https://drive.google.com/uc?export=view&id=1d4Kji6l2aDBpOMwH8nuj4oOlwKpIyZ4h",

        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang cool tapi keren",  
                "pesan":"semangat terus bang jadi kadep jangan sampai kendor semangatnya!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Sukarame",
                "hobbi": "Jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak fifah muka nya galak tapi imup banget",  
                "pesan":"jangan lupa senyum ya kak, senyum kakak imup banget!!!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakak pasha keren dan gacor banget",  
                "pesan":"semangat erus yaa kak, jangan lupa makan ya kak lopyou!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "abang nya keren dan berwibawa",  
                "pesan":"semangat terus bang, tetap jadi panutan ya!"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakak ini lucu dan humble",  
                "pesan":"semangat terus kak!"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang ini gacor tapi muka nya serem",  
                "pesan":"jangan lupa senyum bang, senyum abang imup!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "abang nya seru dan ramah banget",  
                "pesan":"tetep semangat ya bang"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakak ini cantik banget, kalau ketemu ramah ditambah kakak nya suka senyum",  
                "pesan":"semangat terus kak kuliah nya"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abang nya keliatan cool tapi keren",  
                "pesan":"sukses terus bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Abang nya kece banget",  
                "pesan":"semangat terus, tetap jadi panutan ya bang!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang Berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak ini ramah banget",  
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
                "kesan": "Abang kece dan seru abiez",  
                "pesan":"semangat bang kuliah nya"# 1
            },
            {
                "nama": "ALi Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang 4 Nangka Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "Abang nya santai dan baik",  
                "pesan":"sukses terus bang!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini lucu kalem lagi",  
                "pesan":"tetap semangat kak kuliah nya"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scrool Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak nya imup banget, lucu lagi",  
                "pesan":"semangat ya kak, janga lupa makan!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakak ini asik suka bikin lucu2",  
                "pesan":"semangat terus kak, jangan sedih2 yaa harus senyum terus!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "Abang ini ramah dan baik banget lagi",  
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
                "kesan": "Abang seru dan asik lagi",  
                "pesan":"semangat terus ya bang kuliah nya!"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakak nya keren banget ngedance kpop",  
                "pesan":"semangat semangat kak nge dance nya!"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Belajar Front end",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abang ini skena dan keren lagi",  
                "pesan":"sukses terus bang!"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Berdiri, Nyantai",
                "sosmed": "@kevinaj_",
                "kesan": "Abang nya asik tapi agak jutek",  
                "pesan":"semangat ya bang, jangan lupa jaga kesehatan!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak nya asik dan imup lagi",  
                "pesan":"semangat terus kak, jangan suka merajuk ya kak, suka ngoding aja!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Abang nya lucu dan humble",  
                "pesan":"semangat yaa bangg kuliah nya!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main futsal, voli",
                "sosmed": "@sidabutar.26",
                "kesan": "Abang Kocak Abis suka bikin suasana jadi rame",  
                "pesan":"Tetap semangat bang, jangann lupa tugas nya dikerjain ya bang!"# 1
            },
            {
                "nama": "Wuliano Wiliam Purba",
                "nim": "123450098",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngoding",
                "sosmed": "@liano.wlm",
                "kesan": "Abang nya cool dan ramah banget kalau ketemu",  
                "pesan":"semangat terus ya bang!"# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Liat Shopee Tapi Ga Beli",
                "sosmed": "@rewinanaa",
                "kesan": "kakak nya postive vibe",  
                "pesan":"semangat terus kakak nim ku yang imup"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ozv5lPKEOtfZ-wV6oiNXDLmENGj_XPQs",
            "https://drive.google.com/uc?export=view&id=1bXXx_qIpTJcYxgPbV85IVi8nSNHeQRpY",
            "https://drive.google.com/uc?export=view&id=1BHVuV2g0_W9BULIUkofExP82cwnmOAPo",
            "https://drive.google.com/uc?export=view&id=1qZG1y5-EuAzdTfskS7Oi7K0sTZh-jhjg",
            "https://drive.google.com/uc?export=view&id=1aRc2W30u9UeAS_Gzll7U9vYol2ioy_Nd",
            "https://drive.google.com/uc?export=view&id=1-v5OX-Sav19x7sPVURmaUFc0-_ZyJBIY",
            "https://drive.google.com/uc?export=view&id=1s-ouLrsF5zltQw7317V3gBNApnKRvW7J",
            "https://drive.google.com/uc?export=view&id=18FAGBKHxuKOYTkBDXPzizQ9nonVykOOX",
            "https://drive.google.com/uc?export=view&id=1JU4NV3gYng1GJS3svf798NOCJp6mrWpS",
            "https://drive.google.com/uc?export=view&id=1DoznFxCahCwT5tjktz1HHeMQp5-6ZQxt",
            "https://drive.google.com/uc?export=view&id=1o1T7s_YOXhVrXg7760ZzSPUv6vNU3I8b",
            "https://drive.google.com/uc?export=view&id=1PmEVF0O6AEryWgrM0Ul4au4Qcd7CjlMA",
            "https://drive.google.com/uc?export=view&id=17nb3PdMTsv0WermiBZ14xK2fgba0oT0e",
            "https://drive.google.com/uc?export=view&id=1PRmDUcQPCAW5P9f5sO-Yaph9DmpEho_l",
            "https://drive.google.com/uc?export=view&id=1n8eR_CiQCpxIQDOgcGSbPWGIXsx5oRhJ",
            "https://drive.google.com/uc?export=view&id=1q4EdEQM_FwjG9f_mi9EiLnYA1ivPAfj2",
            "https://drive.google.com/uc?export=view&id=1ke9gVd3jrxmE_Ib05dpm7csFayxU9Xcg",
            "https://drive.google.com/uc?export=view&id=1AnpPpEvw7P3p3ZE0XbY0H6uraGiZIITZ",
            "https://drive.google.com/uc?export=view&id=1xynaP_9HSPjlsY6i-6nodkWDqzyLon6f",
            "https://drive.google.com/uc?export=view&id=1eGGOFwHI8EGf7EGmdRGDHnxbd8TfsSGw",
            "https://drive.google.com/uc?export=view&id=1KmBnlL-k9M80_wKcNYDXW9miCtntY62",
            "https://drive.google.com/uc?export=view&id=1tEYk13s3XpTmn9U9Dc12fnFli2sJn_yj",
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur, berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Abang nya baik dan seru",  
                "pesan":"semangat terus bang!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Kakak ini seru dan asik",  
                "pesan":"sukses terus kak, jangan lupa nyanyi kita yang mardua holong itu ya kak!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abang nya keren dan keliatan beribawa",  
                "pesan":"semangat terus bang kuliah nya, jangan lupa makan!"# 1
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishashi",
                "kesan": "Kakak nya asik dan seru",  
                "pesan":"semangat terus kak kuliah nya, info maskeran bareng!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilafarizzii",
                "kesan": "Abang nya ramah dan baik banget mau bantu codingan error pas praktikum",  
                "pesan":"semangat terus bang kuliah nya!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Abang kerennnnn",  
                "pesan":"semangat terus bang, jangan lupa jaga kesehatan ya bang!!!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik, nonton",
                "sosmed": "@notfall.s",
                "kesan": "Abang nya asik dan seru",  
                "pesan":"sukses terus bang!!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak ini pendiam tapi tetap imup",  
                "pesan":"jangan lupa senyum kak!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini asik dan ramah banget, suka ketawa lagi",  
                "pesan":"semangat terus kuliah nya kak, info nyanyi bareng kak di natal nanti hehe!!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abang ini ramah dan chill banget",  
                "pesan":"Tetap jaga semangat ya bang jangan sampai kendor semangat nya!"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak ini seru dan suka drakor",  
                "pesan":"semangat terus kak, info nonton drakor bareng!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini baik banget kalau ketemu",  
                "pesan":"semangat terus kak, btw tempat wisata yang bagus dimana kak hehehe!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, lampung",
                "alamat": "pesawaran, lampung",
                "hobbi": "main piano dan bernyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakak kalem dan baik",  
                "pesan":"semangat teruss kak kuliah nya!"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakak ini keren dan santai",  
                "pesan":"semangat terus kuliah nya kak dan jangan lupa makan ya kak!"# 1
            },
            {
                "nama": "Tanty Widyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kakak ini keren banget",  
                "pesan":"jangan lupa jaga kesehatan ya kak!!"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abang nya keren banget pinter ngoding",  
                "pesan":"semangat terus bang, jangan lupa jaga kesehatan ya !"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini baik dan humble",  
                "pesan":"sukses terus kakkk, kalau cape istirahat ya kak lopyou, jangan lupa jaga kesehatan juga!!"# 1
            },
             {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@i",
                "kesan": "Abang nya kocak dan seru",  
                "pesan":"semangat terus bang kuliah nya!"# 1
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abang nya pinter banget",  
                "pesan":"semangat terus bang kuliah nya, kalau ada waktu ajarin ads ya bang hehehe!"# 1
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
                "kesan": "Abang nya baik banget dan seru",  
                "pesan":"semangat terus bang kuliah nya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CmF-wx2lwRPJ3gmFymQmRJVl3lFr9ET0",
            "https://drive.google.com/uc?export=view&id=1VeyBJqgFXn_JtqKbin5racwK-2JVmr3f",
            "https://drive.google.com/uc?export=view&id=1Ei7W7AO5To-qB_QB9ZkIXcbfLpMQotBg",
            "https://drive.google.com/uc?export=view&id=1nYwhdEZgLQyW6iqRF45NcMEwskYIm7iR",
            "https://drive.google.com/uc?export=view&id=1nphCVdOyNZwkeCCMqwqj_cJ1DNje3XhH",
            "https://drive.google.com/uc?export=view&id=1wQoV3GAqi8tQftmGsu8ffRBggdXc1wnM",
            "https://drive.google.com/uc?export=view&id=1efcewoDtknKkxxOGf4gvgplJeR5PDups",
            "https://drive.google.com/uc?export=view&id=1ItH_h5_cq5fZzeHBOWILhxWMJUCyDo1Z",
            "https://drive.google.com/uc?export=view&id=1fkv5vmXyoLDm--bHt8P3S-TJU-GSnjjn",
            "https://drive.google.com/uc?export=view&id=1Be26exZ4wSxW_QCV0VlbvYAaRI9TVkyL",
            "https://drive.google.com/uc?export=view&id=1Cx56Xw-MXy2bCCEKbAedcbl2rFPk5Jr-",
            "https://drive.google.com/uc?export=view&id=1qJNaXGqqfFAhSfwyzT87SGf4lVrDJCu-",
            "https://drive.google.com/uc?export=view&id=12KwhTIZDTrH0ah2lxEouaCH4EPudSBlb",
            "https://drive.google.com/uc?export=view&id=12hS0pHq3TOOi_WGIiuKcf1ZE7zxH05Sw",
            "https://drive.google.com/uc?export=view&id=1JcHorGVJvJFcWaPmcKos3HYWd4fpSy4h",
            "https://drive.google.com/uc?export=download&id=15t27MTdJpyvzQh4BQVCJhzxlyFUmFAlW",
            "https://drive.google.com/uc?export=view&id=1pjshzLASeGUGnK9LikNo7t4dc55Ff2E6",
            "https://drive.google.com/uc?export=view&id=19KoXVWMtTheHSJGY9kA71Vzo1tzo9Bcj",
            "https://drive.google.com/uc?export=view&id=1Ix2mW-FQLrF9CFpZzbiFPkypPmNG1dPG",
            "https://drive.google.com/uc?export=view&id=14Xdem1Q5vTK8GutLC4HbcsBPPsB8MwdP",
            "https://drive.google.com/uc?export=view&id=1n5ib4YnPJzCyFxJEME7T-4oS-LBQQBPH",
            "https://drive.google.com/uc?export=view&id=15DetCyFHL1qWfynr9x-hHewh4Mn_cm3L",
            "https://drive.google.com/uc?export=view&id=1L-2pgYC66QNdEJS1nvqyzFpeqZ9ATw4I",
            "https://drive.google.com/uc?export=view&id=14qol2YVM3O8k9nyI5gK9nM7vWwXDrh5m",
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
                "kesan": "Abang ini santai dan asik",  
                "pesan":"Semangat terus ya bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini seru dan gacor banget",  
                "pesan":"Semangat terus kak belajar nya!!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak baik dan lucu",  
                "pesan":"Semakin gacor ya kak!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ramah banget dan positive vibes",  
                "pesan":"Semangat terus kak kuliahnya, agar bisa keliling dunia!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abang seru pendim tapi seru polll",  
                "pesan":"Tetap semangat bangg, jangan melamun terus yaa!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak lembut dan kalem",  
                "pesan":"semangat kuliahnya kak, jangan main2 terus yaa lopyou!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak nya santai tappi asik",  
                "pesan":"Sukses terus yaa kak!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak nya cantik dan kalem",  
                "pesan":"Sukses terus ya kak!"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abang snya kalem banget",  
                "pesan":"Semakin gacor ya bang!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak baik dan seru banget",  
                "pesan":"Semakin keren ya kak!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya cantik banget!",  
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
                "kesan": "Kakaknya lucu dan kocak banget ",  
                "pesan":" jangan lupa makan ya kak!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abang baik dan ramah banget!",  
                "pesan":"Semakin gacor dan keren ya bang!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak baik dan suka bantu !",  
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
                "kesan": "kakak nya baik dan ramah banget, suka senyum juga kalau ketemu!",  
                "pesan":"Semangat terus kak kuliahnya, jangan lupa makan ya kak!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abang nya keren dan baik!",  
                "pesan":"Semangat terus bang kuliah nya!"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Abang gacor dan keren banget!",  
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
                "kesan": "Kakak kalem dan imup!",  
                "pesan":"Semangat terus kak kuliahnya, jangan lupa jaga kesehatan ya kak!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak ini baik banget dan imup lagi!",  
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
                "kesan": "Kakak cantik dan keren banget llagi!",  
                "pesan":"Semangat Kak, jangan lupa jaga kesehatan ya kakk!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Kakak kereeen dan seruu banget!",  
                "pesan":"Semakkin gacor ya kakk!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakak nya ramah banget dan baik!",  
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
                "kesan": "Abang nya kalem banget tapi kalau ketemu ramah abiezzz!",  
                "pesan":"semakin keren dan gacor ya bang!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kak Tarisya keyenn banget dan ramah!",  
                "pesan":"Semangat terus kak Tarisya, keep positive vibes ya kakk!"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15hPTxsESiM-COl7r_-fyrVHSRftl-IZ2",
            "https://drive.google.com/uc?export=view&id=1bUzML2IIJJ90xO3c5W2fD3guTHHtzwxW",
            "https://drive.google.com/uc?export=view&id=1u6SYPry-nH4e7TaHd0HK0yt4b6xmm39f",
            "https://drive.google.com/uc?export=view&id=1RAICExUIp39pae56Tsg5Bbbi6WCrprVo",
            "https://drive.google.com/uc?export=view&id=1BgjboMm97l-r8EPBlTFpwi7bLLKUQuQW",
            "https://drive.google.com/uc?export=view&id=1RN2brUIWb3AfVs3jewgCSs5C-tlyNPh8",
            "https://drive.google.com/uc?export=view&id=1lyUWVHzvPQKN7uFH1dupDcjQmpDQ5OPP",
            "https://drive.google.com/uc?export=view&id=14XjdGkSm4XYUf50BubqXkl7fdi6ZVwOh",
            "https://drive.google.com/uc?export=view&id=1RN2brUIWb3AfVs3jewgCSs5C-tlyNPh8",
            "https://drive.google.com/uc?export=view&id=1PjZGrgTIuOrDJPecvtMaA7zmVH9bX6l4",
            "https://drive.google.com/uc?export=view&id=1xwfIR5Kin7d-7QRZA12EesW2iYbSRB2d",
            "https://drive.google.com/uc?export=view&id=1JkcMJAlh9Punr0otMOc8q0YRfpW8qC4T",
            "https://drive.google.com/uc?export=view&id=1gq94S9O4G5G-koDVkTDji6RJXZtBQKRG",
            "https://drive.google.com/uc?export=view&id=1-xTyMU3sTE048ZMXAzPpF362PrT35kM",
            "https://drive.google.com/uc?export=view&id=13T60_7hx8q3TUW7tEj0Yq_3PgrgDzxOf",
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
                "kesan": "Kakak rani baik banget dan ramah lagi, kalau ketemu senyuman kakak nya tulus banget ",  
                "pesan":"semangat terus kak jangan lupa jaga kesehatan ya kak, semangat juga kuliah nya, jangan lupa kan adik2 kakak yang imup ini ya, lopyou sayang kakak banyak2!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak renta baik banget dan kalem",  
                "pesan":"semangat terus kak kuliah, jangan pantang menyerah ya kak, kalau kakak lagi cape selalu andalkan Tuhan bawa dalam doa ya kak, lopyou banyak2!!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@sal_fhn",
                "kesan": "Kakak ini asik dan baik banget",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa jaga kesehatan ya kak !!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abang ini kalem dan positive vibes",  
                "pesan":"semangat terus kuliahnya bang, ingat selalu andalkan Tuhan di setiap langkah abang yaa !!!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakak nya asik dan humble",  
                "pesan":"semangat terus kuliahnya kakak, jangan  lupa senyum!!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang nya chill dan seru banget di tambah gacor poll",  
                "pesan":"jangan lupa istirahat ya bang, jangan cape2 banget, jaga kesehatan juga dan semangat terus ya bang kuliah nya jangan lupa kan Tuhan juga!!!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini asik banget",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa makan yaa!!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak, jangan lupa jaga kesehatan ya kakkk!!!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "Abang pendiam tapi baik banget",  
                "pesan":"semangat terus kuliahnya bang naufal, jangan lupa jaga kesehatan ya bang!"# 1
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
                "kesan": "kakak lucu dan seru abiezz",  
                "pesan":"semangat terus kuliahnya kakk, jangan lupa jaga kesehatan ya kak!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak nya imup dan kalem",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18CniwCykFNtbja6eq8IJ18q9LHYUb8cz",
            "https://drive.google.com/uc?export=view&id=1Yud2c-Nnw14U1z1Dym-xkxTMYlpNPTrR",
            "https://drive.google.com/uc?export=view&id=1F6xi9q2uuoTicIAJ70UY4Zcf5TaJAI8U",
            "https://drive.google.com/uc?export=view&id=12dvaYyiS0E1Ut5Ge9SEK21lE-o_hiYpW",
            "https://drive.google.com/uc?export=view&id=1fgInf0LQenbsRgY9EvBX_2fumjuL3j_J",
            "https://drive.google.com/uc?export=view&id=14HP_xkhQPcaKXhgzY1WqBGDueUVKJ05v",
            "https://drive.google.com/uc?export=view&id=1HG4lmh-CWvAdw4-ctcSrnp1XZgX6wMC8",
            "https://drive.google.com/uc?export=view&id=1Ba0iBUltEim-D7u0e1pWgJt21gYmlfd6",
            "https://drive.google.com/uc?export=view&id=12xIZWykO4_NuMftK-2PAMoJCAfWL-lcL",
            "https://drive.google.com/uc?export=view&id=1NwWaAVgli0uYwXBVEYYYmVG5wEgF9BOo",
            "https://drive.google.com/uc?export=view&id=1muHGPzBMvQaRNLmJrDvg6YhA_zV8YlPL",
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
                "kesan": "Abang keren dan cool",  
                "pesan":"semangat bang project nya!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini humble dan ramah banget",  
                "pesan":"Semangat terus kak!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum, foto-foto pemandangan",
                "sosmed": "@den_iki__",
                "kesan": "Abang stay cool dan kece banget",  
                "pesan":"semangat terus ya bang!"# 1
            },
             {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini ramah dan baik banget!",  
                "pesan":"semangat terus kakk, jangan lupa jaga kesehatan ya kak!!"# 1
            },
             {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini lucu dan imup banget",  
                "pesan":"semakin gacor ya kak!"# 1
            },
             {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Joggin juga",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak ini asik dan seru banget",  
                "pesan":"semangat terus kuliahnya kakak dan jangan lupa senyum ya!!"# 1
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang nya kalem dan humoris",  
                "pesan":"semangat terus kuliahnya bang, jangan lupa makan ya !!!"# 1
            },
             {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak ini humble dan humoris banget",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa jaga kesehatan ya kak !!!"# 1
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg perwira 2",
                "hobbi": "Nonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak nya gacor dan kece abiezz",  
                "pesan":"semakin gacor ya kakk !!!"# 1
            },
             {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kakak nya baik banget dan humoris lagi",  
                "pesan":"semangat terus kak kuliah nya!!!"# 1
            },
             {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak baik dan imup banget",  
                "pesan":"semakin gacor dan keren ya kakkk !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1i20rTVtOwHqW23l4cgDYscNOr4X2Mh7d",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",

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
                "kesan": "Kakak cantik,heboh,slay dan positive vibes",  
                "pesan":"semangat kuliah nya kakkk!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jl. Kresna Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini seru dan lucu banget!",  
                "pesan":"semangat terus kak rahmaa!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard & Volly",
                "sosmed": "@mananam_",
                "kesan": "Abang nya baik dan ramah banget kalau ketemu",  
                "pesan":"Sukses dan semangat terus bang!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik & fotografi",
                "sosmed": "@noerruu",
                "kesan": "Abang pdd keren banget",  
                "pesan":"Semangat terus bang jadi pdd nyaa!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Abang nya seru dan kocak abiezzz!",  
                "pesan":"Semangat terus bang, jangan lupa istirahat!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak imup dan lucu",  
                "pesan":"semangat terus kuliah nya kakakk!"# 1
            },
            {   
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakak nya gacor parahhhh",  
                "pesan":"semakin gacor ya kakkk!"
            },
            {
                "nama": "Aliya Anmara Amanta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammra",
                "kesan": "Kakak nya cantik banget dan positive vibes",  
                "pesan":"semakin sukses yaa kakkk!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini asik banget dan imupp lagi",  
                "pesan":"semangat terus kuliah nya kak donna!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kakak nya baik dan ramah banget",  
                "pesan":"semangat terus kuliahnya kakk feby!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak keren dan gacor",  
                "pesan":"Semangat terus kakk!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumateraa Barat",
                "alamat": "Jl. Lapas, Kecamatan Jati Agung",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa_",
                "kesan": "Kakak nya  keren dan imuppp",  
                "pesan":"Semangat terus kak, jangan pantang menyerah yaa kak!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak nya ramah banget",  
                "pesan":"semangat terus main robloxnya kak, btw info main bareng kak!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "abang nya baik banget dan ramah lagi",  
                "pesan":"Semakin gacor ya bangg!!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",  
                "kesan": "Kakak nya baik banget",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa istirahat ya kakk!!"# 1
            },
                        {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kakak nya baik banget, ramah lagi!",  
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
                "kesan": "kakak nya imupp banget dan humble",  
                "pesan":"semangat terus kuliah nya kak, jangan pantang menyerah ya kakk!"# 1
            },
                        {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak roma baikk banget dan kocak lagi, bikin suasana tambah rame dan seru!",  
                "pesan":"semangat dan sukses terus kak roma jangan lupa makan dan istirahat yaa kakk, jangan lupa jaga kesehatan juga kakk!"# 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
       

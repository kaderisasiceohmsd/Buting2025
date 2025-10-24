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
            "https://drive.google.com/uc?export=view&id=1ihQeX1mcmI3rSnYIxIVXSnW6LAgmlhXH",
            "https://drive.google.com/uc?export=view&id=1Zbn_ZiQdld0av6OOoVx8e6Y1OVwEZ6sJ",
            "https://drive.google.com/uc?export=view&id=1W4wy10tzyQuD-iWwWxOFhEUzXaFT4Cfb",
            "https://drive.google.com/uc?export=view&id=1qi33TkJI6eTBtRWdGyynI_tSQkPnf_Wy",
            "https://drive.google.com/uc?export=view&id=1pBQyv-BMUSNkWOCDbpMEmgdEKtdNfJbD",
            "https://drive.google.com/uc?export=view&id=1UBOjxwpT7d_aERu-P55CNfUl1EBPJu6n",
            "https://drive.google.com/uc?export=view&id=1eyKhEzYMwdXw38wIDeSNUyeNfdzgrYVq",
            "https://drive.google.com/uc?export=view&id=1JhzVg8NriX4Z0C4YCMNDh7WStohIUgBo",
            "https://drive.google.com/uc?export=view&id=1LVvS7BBfdQ8FjHWbdtswbXo-Q3HTl1WZ",
            "https://drive.google.com/uc?export=view&id=1UR-tfZ39RnLXTMLdVYL_jRyx5pijw2CO",
            "https://drive.google.com/uc?export=view&id=1QiiLBzcpQk_V6jfwDSPOYxYK6mRaSeBs",
            "https://drive.google.com/uc?export=view&id=1bE-s2pITxuyTb2QR3RGW0ESFblfww0Tt",
            "https://drive.google.com/uc?export=view&id=1cL1GUOzdHE0hDLfRDunU4omL9_TIR2n-",
            "https://drive.google.com/uc?export=view&id=1Uzsa6ObZB6fBGxLVazd9B8MogA2jvKuR",
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
            "https://drive.google.com/uc?export=view&id=1meix0qdhphr8-CqPpy5ukeWHf_QDz1-5",
            "https://drive.google.com/uc?export=view&id=1YIcX3-wmTGOfX97gIHZBeeIEXvgDsKaP",
            "https://drive.google.com/uc?export=view&id=1rF1IOmfnj41D3LqJyvKR7sTv33fpQbgT",
            "https://drive.google.com/uc?export=view&id=10lGFcD_7ZArRLmHXs-wqLgZC7OvE74mK",
            "https://drive.google.com/uc?export=view&id=1oJkAG-cifVyngNfgyyJi1tWPiKDVaa4n",
            "https://drive.google.com/uc?export=view&id=1_jv1Oc8icScA1uyFMJxMZdoA6RzkGzAi",
            "https://drive.google.com/uc?export=view&id=180w0Ke1tG5zCu5Amj0E3aYN75BbNOe1j",
            "https://drive.google.com/uc?export=view&id=1EX06Ywf7BRma_s8prPkph5TpfLxKAdxA",
            "https://drive.google.com/uc?export=view&id=1b_9KA0MO1l4iIfJWAFhA35AqqYz97xsz",
            "https://drive.google.com/uc?export=view&id=1oIPa42IDBCycxa_UbT0l5Ri62L1Fxs5c",
            "https://drive.google.com/uc?export=view&id=1uN118D5nBCttM_TgVT5KaH-_Q9zWFoCj",
            "https://drive.google.com/uc?export=view&id=1dfwRKHAULmAyUPIIgKYBtlbfKrbnJ6cb",
            "https://drive.google.com/uc?export=view&id=1UGvv6wyh1LRfTUi1qCfhB3C8hL4qr5CK",
            "https://drive.google.com/uc?export=view&id=1YeKip9OJleBO1QxhVZ8bMbY_ZDYsEn-D",
            "https://drive.google.com/uc?export=view&id=1PHCvLZclt2dnGShnmwpAa-OuQI3ZAUKg",
            "https://drive.google.com/uc?export=view&id=1WsqKlGINoirS_-9pT0DPdB1kM_-cp3EE",
            "https://drive.google.com/uc?export=view&id=1JbrOUPPONnSe9MbDmMceTsh3okT-38_N",
            "https://drive.google.com/uc?export=view&id=13FexYmwsZ44K4zes3Em9NUdlRd_eF4iU",
            "https://drive.google.com/uc?export=view&id=1wZO6BWrscSV92bSBNw14YrnxYQX4Ts3u",
            "https://drive.google.com/uc?export=view&id=1vvvRTjNty_eQ8EkA6_kvtWxT8mEUQacC",
            "https://drive.google.com/uc?export=view&id=1osK2cTONOkJlJJHuvl6KabX4czSlBY0_",
            "https://drive.google.com/uc?export=view&id=1__YhRY-EBcSzZJsW1rRs3kqR8sUasf4T",
            "https://drive.google.com/uc?export=view&id=1ucbflmCHixIBjJUWI3uuFLrNCmNr0av-",
            "https://drive.google.com/uc?export=view&id=1wWn9dUs1hnLVbwTGC0a4uyNspadkd159",
            "https://drive.google.com/uc?export=view&id=1bnvgpykXW41KUwS_M51o2N7Oa3S6FBc7",
            "https://drive.google.com/uc?export=view&id=1BpuiUU0rYoXHeRBbJe9qevxrcvfRd4AK",

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
            "https://drive.google.com/uc?export=view&id=1g1vGRymJLJwAK1id7sDzZdSl22VqBUAc",
            "https://drive.google.com/uc?export=view&id=1cEbtwbTYNTsvKO2Kwie4ixA6wjsq1qJ1",
            "https://drive.google.com/uc?export=view&id=1y2LfLTqBQ5vFKarGyRwjfUJDq5a_k_lo",
            "https://drive.google.com/uc?export=view&id=1sTAnehD1i1gUets3TW9DlvUbCxkEdcD-",
            "https://drive.google.com/uc?export=view&id=1IWPIvzxd7Fl6l3OGOBWHFHLtCZjqKStu",
            "https://drive.google.com/uc?export=view&id=1-l6m815qJaawjoik6z7X8DP6L9NrwAYj",
            "https://drive.google.com/uc?export=view&id=1G6WXxoDwMvfaKmV-nq3T-AwLIxGNAgnX",
            "https://drive.google.com/uc?export=view&id=1KqyFNYC1mwu8BH05j8wYSdepZYy8lTdk",
            "https://drive.google.com/uc?export=view&id=1hEwHP65xi08Lb9cEVoXK85uquFq3xVa2",
            "https://drive.google.com/uc?export=view&id=1whv21tNT__Rz4gm3yxOvqW2pPPrPYmTo",
            "https://drive.google.com/uc?export=view&id=1ry2Huh5sC-wi5G-oguMZEbkz29BGfTLP",
            "https://drive.google.com/uc?export=view&id=1tzupAR1edjU_4p0e_fIwwk3QYhoWqSeu",
            "https://drive.google.com/uc?export=view&id=1_R0zUhTf2pEipP3_lcsR9AvV0h1Wb1Tl",
            "https://drive.google.com/uc?export=view&id=1JQViEti6h4jVMzdCP8nr6Xuqj_74k82N",
            "https://drive.google.com/uc?export=view&id=1t8iHi9iqZPnJnlRVL5roPI0-EmYkLxFo",
            "https://drive.google.com/uc?export=view&id=1uqAGzw6IUrv-lbbfwL0-Sf08bf6WfSPJ",
            "https://drive.google.com/uc?export=view&id=1q9ZNhezSS7iYCo84CWpY4uykB1b1bpTS",
            "https://drive.google.com/uc?export=view&id=13Zltf2lq7oy3ec6KiNk1DVKRm6YAJbH8",
            "https://drive.google.com/uc?export=view&id=1swP64XIrvDZceDlU13gB6obR_icF0xcz",
            "https://drive.google.com/uc?export=view&id=1I5dFM9J8O2BavqbOnE8eLzrdFhdI4YXn",
            "https://drive.google.com/uc?export=view&id=1HoeAL3IvrpNu9HBzRC64GeRN66BAyN8T",
            "https://drive.google.com/uc?export=view&id=1_fx2KSaLpQjeBspPlTEv7DC3UrvR18WJ",
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
            "https://drive.google.com/uc?export=view&id=1FONMIbMzeNcSCHv1r9N0iF8Y35PWdkh6",
            "https://drive.google.com/uc?export=view&id=1t7gjzzksY848oU2v8yGMbM2XrF_nvpB2",
            "https://drive.google.com/uc?export=view&id=1NdVLtPCjNdQICQ31FtWMTF5okTwBiUtA",
            "https://drive.google.com/uc?export=view&id=1oEuB3YasOGzQUegjnsjrr-3e3FTkptSy",
            "https://drive.google.com/uc?export=view&id=16UrGfbiU7nEEjnBXDGyIAiSSBi9jnARq",
            "https://drive.google.com/uc?export=view&id=1aBhyaGx_iMsuI0hd06d7bjUFTqr9jnhL",
            "https://drive.google.com/uc?export=view&id=1IWiOnG5Q1sWtT8zl1l459wMKDbVlx9Zf",
            "https://drive.google.com/uc?export=view&id=1GKQCasxzSq6VsVlMVzMRVycFzGO61f6h",
            "https://drive.google.com/uc?export=view&id=1N-K8vPA3P-RBUlgvY-ke0fQAYg_xGwqK",
            "https://drive.google.com/uc?export=view&id=17jAIW0zBd8qyUaiQEEH8AqW-vs7ipBma",
            "https://drive.google.com/uc?export=view&id=1_Bj5gULpQmjHQQ-nkwuQup8k8xMBAezH",
            "https://drive.google.com/uc?export=view&id=1Tg_rAkN1MXZjon_bFqJnco1g8NeUYbAV",
            "https://drive.google.com/uc?export=view&id=17FsISJ1V7GV9Id4ZTie3I95bTC7L0eyv",
            "https://drive.google.com/uc?export=view&id=1jaUqG7MzQRxh2GxUtPasbML3ROKu3mac",
            "https://drive.google.com/uc?export=view&id=1lLNt7p44-PlDf1BNA8w8ShO7GItvR30F",
        
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
            "https://drive.google.com/uc?export=view&id=1tuK6iJYKaMT6NQ8DPNtHELXDwPUOhFFF",
            "https://drive.google.com/uc?export=view&id=1iZNi-1mgd-ryGdTXWgD-VsoRmmoSdThJ",
            "https://drive.google.com/uc?export=view&id=1KmOmpl_x6bEmheEUhMvh0zynHsLHqw1Y",
            "https://drive.google.com/uc?export=view&id=16Aciv9nWVNNscMjOB6nkSuPOwFUVKa5D",
            "https://drive.google.com/uc?export=view&id=1j4Ll9wX17R4O0fdP8rMiT6pBqflcTCi0",
            "https://drive.google.com/uc?export=view&id=1mhpMLaV908Vj8eNhuwoT-kfn3FgGc1QT",
            "https://drive.google.com/uc?export=view&id=1wiz2xaEyIiON-PS3Sq1d1Tnjk-_f0rMF",
            "https://drive.google.com/uc?export=view&id=1EwICTc1BouwoLsSYAuSfS6a8YiwUi2bp",
            "https://drive.google.com/uc?export=view&id=1gzdx79kp5xRGjbbgJ3vEzzkcdKVwz6ub",
            "https://drive.google.com/uc?export=view&id=1YlTn11KpAOXWyZ3M6AKKiaIEvt4Pdmza",
            "https://drive.google.com/uc?export=view&id=1y8KuWmeZOc_52iIL8zhZKrRx3ftqtk7d",
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
       

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
            "https://drive.google.com/uc?export=view&id=1ZxYff70lT_vJUsGUNWFg8_kxVtL18qe4",
            "https://drive.google.com/uc?export=view&id=1xmvJym7swF3HArBiJlqFizViNyWrpvJ7",
            "https://drive.google.com/uc?export=view&id=1R15OGDBjFtgtvDrAB_7fOEh4_7ZkT-fw",
            "https://drive.google.com/uc?export=view&id=1URyabjZQ_Q6Sr-1VDwy2NRW5f9k1Syfj",
            "https://drive.google.com/uc?export=view&id=1sHtHMYzUoGA_ncBOMvN71VnoKZQI7Ife",
            "https://drive.google.com/uc?export=view&id=1vwvKPEn5_sgPvm92aWjhswIt8OgbFxde", 
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
                "kesan": "Keren banget kahim satu ini, keliatan banget wibawanyaaa",  
                "pesan":"Semangat teruss bang bawa nama HMSD ke tingkat yang lebih tinggi"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL!",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "SEKJEN!! keren banget, tengil tapi jago suka banget guaa",  
                "pesan":"kalo supporteran jangan dorong dorong adek adeknya yaa bang"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Badui",
                "alamat": "Ayrest Kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "lucu banget kakak ini, semuanya di ketawain wkwk",  
                "pesan":"semoga akunnya gak kena suspend lagi yaa kak, sayang banget udah banyak followernya"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya pendiem tapi lucu imupp gitu",  
                "pesan":"semoga dilancarkan yaa kak semua urusannya# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini ni yang manggil gua mirip gibran wapres, jujur malu si awalnya tapi ternyata lucu juga",  
                "pesan":"jangan panggil aku gibran wapres lagi yaa kak, malu..."# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "muka kakaknya kayak yang jutek jutek gitu tapi lucuu",  
                "pesan":"kurang kurangin yaa kak cutek cutek bang rendra, kasian..."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_Yr0vC4kM1eKdL7n4bYU1PpRXnAiFb8l",
            "https://drive.google.com/uc?export=view&id=1WBYI565WNC0Pf0vlcjajUkGJj1WctdrL",
            "https://drive.google.com/uc?export=view&id=1cGzvohFHv1ARXXf7bY3JkWj1f08x-1g3",
            "https://drive.google.com/uc?export=view&id=1un4oAXZ0zDRh_11p4jPZ3TLRozMrMJMM",
            "https://drive.google.com/uc?export=view&id=1N9zoovAsYfShHHDYphOB4xWCA9tQvcy9",
            "https://drive.google.com/uc?export=view&id=1YzOZe1U68UAFVPcRi0uI0FqWitXXe1Ed",
            "https://drive.google.com/uc?export=view&id=1QqsFfsTy0MwkAH0nnMqUJwwhyWVgJeoG",
            "https://drive.google.com/uc?export=view&id=1ocHue63rKTwCChY-OVHMz0gtxNWTGKYL",
            "https://drive.google.com/uc?export=view&id=1ZwxKw-8yU7pYtMBKLr8RNWxldTVhe-rD",
            "https://drive.google.com/uc?export=view&id=1vyvlD1EjII3hbP5SN6A9nVZxHu6w-nx_",
            "https://drive.google.com/uc?export=view&id=161kukUHwqFdrfrlPmlU7rTXNgCxLD1n0",
            "https://drive.google.com/uc?export=view&id=10307JJyxWq4MlEi6tM2rV3I0BAW0Fgvm",
            "https://drive.google.com/uc?export=view&id=1ZxSxlCXBUtlaP3ri0mcZ4ibin_7O5aKY",
            "https://drive.google.com/uc?export=view&id=1K9hWCYfJTyOyjsOICVZloiUnDMc1i7bw",
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
                "kesan": "dua kali bangunin gua pas praktikum wkwk tapi gak marah abnangnya malah ketawa, baik banget orangnya lucu juga",  
                "pesan":"maju terus bangg!! semangat teruss, jangan marah yaa bang kalo saya ketiduran pas praktikum "# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "muka kakaknya kayak islami banget hehe, tapi tetep lucu kok kak",  
                "pesan":"jalani hari hari kakak dengan perasaan yang bahagia yaa kak"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "lucu nan imup kakaknya, kayanya cocok kalo jadi cosplayer anime ",  
                "pesan":"jangan sering sering tidur yaaa kak ntar kebanyakan mimpi jadinya# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "masyallah tabarakallah suka ngaji ternyata kakaknya, pantes kok wajah kakanya kayak bersinar sinar gituu ",  
                "pesan":"ngajinya jangan kalo lagi butuh aja yaa kak, setiap hari kalo bisa biar makin bersinar wajahnyaa"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "mentor PPLK guaa nii, gacor banget sebangga itu gua dulu pas tau mentor gua menang OZT sampe ke semua orang gua cerita, baik banget dulu bang dharu ini gapernah marah ke anak anaknya ini",  
                "pesan":"kejarr cumlaude itu bang semangat terus pokoknya, terus jadi orang baik yaa bang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini lucu bangett imuppp, kakaknya ini cocok juga kayanya kalo jadi cosplayer karakter anime yang lucu lucu gitu",  
                "pesan":"jangan ilang yaa kak lucu dan imupnya, cobaiin cosplay coplay kakk"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "Mentor kader gua ini, sumpahh kalo bisa bikin 500 kata ku bikin ini disini, sumpahh aku bener bener ngerasa beruntung banget dapet mentor kayak abang karna ngeliat berapa kelompok lain pada dapet mentor yang gabisa sedeket itu ke mereka, beda banget sama bang givaro ini dia bener bener mentoe terbaik di mata gua, kalo ada nominasi mentor terbaik ga terima gua kalo bukan bang givaro pemenangnya, abang ini bener bener ngebuat suasana kumpul kelompok kayak ga ada batas antara dia dan anak anak nya ini, aku bener bener ngerasa percaya banget kalau cerita masalah masalah pribadiku ke diaa, pokoknya diaa mentor terbaik pada kader ini!!",  
                "pesan":"semangat terus yaa bang buat nemenin kita selama masa kaderisasi ini yaa walaupun kadang kita bikin abang cape atau kesel, kami berterimakasihh sebanyak banyaknya kee abang karna udah nunjukin sosok dibalik panggilan MENTOR itu"# 1
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
            "https://drive.google.com/uc?export=view&id=1av0sd0FKdYJJWsrpdKPGf5SEg8EKbJaD",
            "https://drive.google.com/uc?export=view&id=1sD9XtkxtAHDLzPwnVKgaXgeuAmbDF26O",
            "https://drive.google.com/uc?export=view&id=1Ycg5TGawdB9bbqQi64sQAt0o0c6keAIX",
            "https://drive.google.com/uc?export=view&id=1BgaHEuwkR_VkQ2bzf0QDNPmjYp_NnDIy",
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
            "https://drive.google.com/uc?export=view&id=1sNgzC6cUQ4TmuOKc9UsOPmKRTdzQodve",
            "https://drive.google.com/uc?export=view&id=17kPdKDOk-fhRCJm-rbvcxf48DEwVLovA",
            "https://drive.google.com/uc?export=view&id=1QGoJPPCM81ApFmGf-3Ys6yXvpYgH0tGK",
            "https://drive.google.com/uc?export=view&id=1s3lGW1CDAPMoC8M_aos-CBV6RRq_nWCn",
            "https://drive.google.com/uc?export=view&id=16g3TnXCSM53foiyuhnKo_udQKj7CORxi",
            "https://drive.google.com/uc?export=view&id=1UhFAwss1NLcvyEElgZSsaPlwQ8w-hus3",
            "https://drive.google.com/uc?export=view&id=180w0Ke1tG5zCu5Amj0E3aYN75BbNOe1j",
            "https://drive.google.com/uc?export=view&id=1_UNYK0_tJbpFtkY7AXMD5NGi-zpLAfIY",
            "https://drive.google.com/uc?export=view&id=19i3MbEYkrzMp7AT_LxZY7BqSWWSKWYoJ",
            "https://drive.google.com/uc?export=view&id=1-F0Y9ConnHGe5TaSmyonXG_qU8kqVASD",
            "https://drive.google.com/uc?export=view&id=1qV-KxxPgt6-n5HvxZAfsIzdHE2r7EEDF",
            "https://drive.google.com/uc?export=view&id=15ypFoNjZGjbzvzfhFg8iThqkuPSSnAG9",
            "https://drive.google.com/uc?export=view&id=1p9z-RXgy5BcK0cvYMe_n61SsVFZCWxAP",
            "https://drive.google.com/uc?export=view&id=1rOGjoPw9WT-BOf54-rJR6v0zMN1jyuyf",
            "https://drive.google.com/uc?export=view&id=1O2agMCxX5PxYH2s_XkIxwZhxuC3S2-iv",
            "https://drive.google.com/uc?export=view&id=1HLJehj3pX2mvALCypwnJI8n0S0km88Yj",
            "https://drive.google.com/uc?export=view&id=1Ia9-LoNhN_O1lLR8D-dSUzZ5yiCF0Fi1",
            "https://drive.google.com/uc?export=view&id=1Fk8ZIDPASbeYymtpMoM0yMcpaqYGkq81",
            "https://drive.google.com/uc?export=view&id=17H97IuMxfpWaVKOf8SxviyGNn35uiRA-",
            "https://drive.google.com/uc?export=view&id=1M-NRfSY4mqADtVgX3J7Qfee7hnfQVgNx",
            "https://drive.google.com/uc?export=view&id=1we-LUqq3aJT4JIFEty5XcX0mvD5sGdHD",
            "https://drive.google.com/uc?export=view&id=1kRnidTf1jQxtryzqbYva-DeSu52mM9np",
            "https://drive.google.com/uc?export=view&id=1v6wZQei4_4x6QFaTDI3sc3XcOq6H5onl",
            "https://drive.google.com/uc?export=view&id=135Ab4dmgoZWrQvlFEEuFhZtLGbKbDfpt",
            "https://drive.google.com/uc?export=view&id=18oeX5B_1rfJAJKwAclTlehWPZev9eVOr",
            "https://drive.google.com/uc?export=view&id=1PE2Ifg5_QbbTP4J2HEShrFE4DZsKdnyI",

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
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
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
                "nama": "-",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@-",
                "kesan": "-",  
                "pesan":"T-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1md5FqiQ70XXZgXmsIrwHxuMjDKmQPhnb",
            "https://drive.google.com/uc?export=view&id=1F3mI2ToLiHzxh4XC5Bbw82ur_nluIikM",
            "https://drive.google.com/uc?export=view&id=1floEn1eN1Vv6YQuBWe6nYSkdjRuWYeax",
            "https://drive.google.com/uc?export=view&id=1acX9MdMPzGPKCoKgWUkNFZKjJKprUmBS",
            "https://drive.google.com/uc?export=view&id=1VsevsU8C0TeRdCaHV3WAhUPoQrENGQGX",
            "https://drive.google.com/uc?export=view&id=1blu5AGL1HIv-I16oP3ZgQ94-0s4OpArT",
            "https://drive.google.com/uc?export=view&id=1uo-GYVNqyNi3ikujO3oXW42WnLlqn_mJ",
            "https://drive.google.com/uc?export=view&id=1Idpx3naLCQ7qHeOkKyy1gbXbHMgJq8mc",
            "https://drive.google.com/uc?export=view&id=19vexDMnyjRSdg3IbefPBaPVzM2nYF-sF",
            "https://drive.google.com/uc?export=view&id=1l39eSCtq0ZYs14OoJ6Oj9Q7I5PhUU22f",
            "https://drive.google.com/uc?export=view&id=1V4BZ289r_NzkqulVY0UTNCgf8UgH1-qy",
            "https://drive.google.com/uc?export=view&id=1_XYdafFBe3_CxD3oIl24U03c-YRf7loz",
            "https://drive.google.com/uc?export=view&id=1rc-myTE0xLcwTGMkZP9DcvbYo3I9tCQv",
            "https://drive.google.com/uc?export=view&id=1zWNBj1TmhCFx5QC-XSJS-bccywONH229",
            "https://drive.google.com/uc?export=view&id=1U7F2rs1WnZFhLI9lZkG3rtDtyNVBCprm",
            "https://drive.google.com/uc?export=view&id=1Ry_3WTV4upWsBevG0exlLRKkOt6Qef4S",
            "https://drive.google.com/uc?export=view&id=1q9ZNhezSS7iYCo84CWpY4uykB1b1bpTS",
            "https://drive.google.com/uc?export=view&id=1iqtD6dQe1RI8_3jNUUdaNTM3k1RF0IlL",
            "https://drive.google.com/uc?export=view&id=1mtpJ8EOGKh2SDsW6jNCpyaTACdCcH60J",
            "https://drive.google.com/uc?export=view&id=1FeWKIOiCS4stF5eyrraAp8vti36cTs4Y",
            "https://drive.google.com/uc?export=view&id=1v_XtzT998GjJ1tklMAq_Z7oHwZSzyDVD",
            "https://drive.google.com/uc?export=view&id=1_ma38Vw6jr1_SD9rwWXH5Q-7zZHj9L6y",
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
            "https://drive.google.com/uc?export=view&id=1G1lnWOrFXb5Uwvm9NKiv-TVqp4ktIDpZ",
            "https://drive.google.com/uc?export=view&id=1WrVVRM5JWc2XFx4uIY4zc27JjFI7Sw3T",
            "https://drive.google.com/uc?export=view&id=1kPqS1nMYreZU9uGtqv8JRPMs1T6yjNyF",
            "https://drive.google.com/uc?export=view&id=1k7pQKBcYRvrFJ3iWF6lTLz_3_IxSgEFy",
            "https://drive.google.com/uc?export=view&id=1VpC8J3DOZh7l1GifClccY1kBVJHM9du7",
            "https://drive.google.com/uc?export=view&id=1rcLQlZ4VujQe5GtJoWqzWt2skt0n7JVh",
            "https://drive.google.com/uc?export=view&id=1O6PrgNhoJqaGZIWBB5zzS7YG13lq4Zep",
            "https://drive.google.com/uc?export=view&id=1CmTBKrIQL26wmVhs0MwtwP0zBFg71i7Y",
            "https://drive.google.com/uc?export=view&id=1bmONpDNWYjz0EL1AQWDof8lQYEU6SiOt",
            "https://drive.google.com/uc?export=view&id=1GoSEFvp4V7cFyEGVffxG-n66OCKiSt2s",
            "https://drive.google.com/uc?export=view&id=1B5c-1KMRlkjpkAdoYJjpt3ho7qUikhew",
            "https://drive.google.com/uc?export=view&id=1L0-MA7iIg6KtOxaT-6sYNBLrNlLrDYix",
            "https://drive.google.com/uc?export=view&id=1feG962G8y5_Ihum5o8X9A2kfgvdhGKeg",
            "https://drive.google.com/uc?export=view&id=1xxMmHgZOLNdqo08T9a1_PW3D5SX-uF1K",
            "https://drive.google.com/uc?export=view&id=17sAdbtLbLXq0z_JMuwJmuW9X27gZMx2B",
            "https://drive.google.com/uc?export=view&id=16O47uDeSKaw9fN1gAuhN5MRlEKYp6Reh",
            "https://drive.google.com/uc?export=view&id=1DSTcauUWLsAd8r-gK68_VmbGbRc_IPQO",
            "https://drive.google.com/uc?export=view&id=13Yq301gnV864ibohcFdW7X0qkYAO9Iai",
            "https://drive.google.com/uc?export=view&id=11YIzx65PORV26p-SuVoTfrUxZ9JcGY0D",
            "https://drive.google.com/uc?export=view&id=1_7yM02-ydYu8NNERAfo4EFbJlF31sFwF",
            "https://drive.google.com/uc?export=view&id=1ugYFqk0SZRqV1aYJKwVP04JANFFYN8_D",
            "https://drive.google.com/uc?export=view&id=19OvlGqAfoCFGR4ubxi30xXPo89BkZen0",
            "https://drive.google.com/uc?export=view&id=13xpsaeuTHsVh3bpKn6GmpZfEfZ71b0Aq",
            "https://drive.google.com/uc?export=view&id=1hfphi9WwRUH1LUpyIdU7xMcHrshHFVOd",
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
            "https://drive.google.com/uc?export=view&id=1dIbHYGi_s12bufrL1xAZrBmGAtyn7C4X",
            "https://drive.google.com/uc?export=view&id=1Xwa9fZlP9Yvrfe8k-nV4jqwFnkaLKlm3",
            "https://drive.google.com/uc?export=view&id=17rpODGgpXqLptHQhpgk_3nuMGM7d4X9L",
            "https://drive.google.com/uc?export=view&id=1HYsE51vdXm7DkbsxsNQ-JI71Csrbo-cI",
            "https://drive.google.com/uc?export=view&id=1HWE6Q9Et_9bmi4TTLAUJsqBF2UEoOYTc",
            "https://drive.google.com/uc?export=view&id=1R0l03iMf9Z46xNBqQM4x4EUE7YAcJDfF",
            "https://drive.google.com/uc?export=view&id=1SK4JKA6JCTXTZENBG7MssdaIFkFhhr6J",
            "https://drive.google.com/uc?export=view&id=18eZjPY8PEN-CDeT7lV8EHfS4CAAdkKrB",
            "https://drive.google.com/uc?export=view&id=1I_tDy3x8jMW4TxAmnqn-uow-zalz0XkL",
            "https://drive.google.com/uc?export=view&id=1E4TMwnfSDrf9JbvctCzRyFhJE8iZb1-l",
            "https://drive.google.com/uc?export=view&id=1OVXNCSeScgjK-hitz2K3PatIP4CsUfi2",
            "https://drive.google.com/uc?export=view&id=1g1OS1vM3SZvORsQgQDV7BAt01DKi-Rez",
            "https://drive.google.com/uc?export=view&id=1dxfrbeHJGIJZHycAabgqw-D7QwVwaA2O",
            "https://drive.google.com/uc?export=view&id=1MFeBo7ElAXxbjr0uHkfc1_afvs2AKorU",
            "https://drive.google.com/uc?export=view&id=1exktVC0x0apNNqUtI5oRxHm1dwB34bQw",
        
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
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
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
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
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
            "https://drive.google.com/uc?export=view&id=1mRNU1FW6yUf26NA5kshff3Fh_yWQzTds",
            "https://drive.google.com/uc?export=view&id=1xy8a715-mSIgg1_2Ea94-dUM6tHa-VXQ",
            "https://drive.google.com/uc?export=view&id=12oBvQzxVvQjQ_U2AH4QOFOHQSkoa8-b0",
            "https://drive.google.com/uc?export=view&id=1edLSlsOcXSFfEwlVScM3XC8jJKvxbRCB",
            "https://drive.google.com/uc?export=view&id=12cMZdH_Fks9o-hbAHGk4SzTXuzVLZJRW",
            "https://drive.google.com/uc?export=view&id=1RClSOrTiiSKmMx1vTZAPYdxzXuIfDWZH",
            "https://drive.google.com/uc?export=view&id=1MrrFrD39Owo_1LI1TBHpa5XjGIvzqlxE",
            "https://drive.google.com/uc?export=view&id=11LOrm1E1S31DzgfXhtNgbapOXPZ9Ksz4",
            "https://drive.google.com/uc?export=view&id=1-drfneTTWeiv5u1-vG_4hWuRcoVJcstd",
            "https://drive.google.com/uc?export=view&id=1e_XTlcdehdIvgV_Bw82CbS9WLjORRi7r",
            "https://drive.google.com/uc?export=view&id=1KR1x357_EaQ9v60laqUjCdJP7776t1mp",
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
            "https://drive.google.com/uc?export=view&id=1dmnZpuK81RnFlz0FXoYu7DsXl3fLph2d",
            "https://drive.google.com/uc?export=view&id=1Gg4jiekVJIZLsBoqFsd1d3WGnuIom27K",
            "https://drive.google.com/uc?export=view&id=1Ie7Lc7PKgQ1cC7giKG2X5HJ4ZNc3dYBu",
            "https://drive.google.com/uc?export=view&id=1XvbMNYquHDJ77xKxALEuTCVgbRN90Thq",
            "https://drive.google.com/uc?export=view&id=1S67FWUV5JnsaLPYMZ1SN1mzewVlSozul",
            "https://drive.google.com/uc?export=view&id=1w9kvE1QiiThNk0nh_ER_GR_YldbrOFqI",
            "https://drive.google.com/uc?export=view&id=12aJXV_RBQUZ4DooSaQm_SjBT9-nv9MSA",
            "https://drive.google.com/uc?export=view&id=1LLsrb32xOkPYYIuWkpEpJZTizBXRMEJQ",
            "https://drive.google.com/uc?export=view&id=1h4Lmu3l--ndYgURVEP757PGe3cKpvFSW",
            "https://drive.google.com/uc?export=view&id=1F_O8CbgZIjPkkFxn2LbBVQT4W7eS4Hwz",
            "https://drive.google.com/uc?export=view&id=11TWR_O0iH_ulE7yH7vTRtZq7fPGh1OOe",
            "https://drive.google.com/uc?export=view&id=1z2kEpsz4cr1Br_Jdlj05-fGaVY1S23Ep",
            "https://drive.google.com/uc?export=view&id=1Q-cuxxd40hcWrDOQ9Q9pJmyrpKdI4Z3H",
            "https://drive.google.com/uc?export=view&id=1UhaF2j3oo0pQ49IhGSXOSvAzB6Pewd0T",
            "https://drive.google.com/uc?export=view&id=1mp7fZFW9L129UdCHNWfYcY7GP5FQ0eoL",
            "https://drive.google.com/uc?export=view&id=1Cz5DPv4E529HXFYTku9bQjy9sDcM_g7W",
            "https://drive.google.com/uc?export=view&id=1bSG3486WWMpyVyAG8VpUuK3NMWXLYnAY",
            "https://drive.google.com/uc?export=view&id=1O0_1Z80M_NNZdswCxC-T5Vj9WMyjvvos",

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
       

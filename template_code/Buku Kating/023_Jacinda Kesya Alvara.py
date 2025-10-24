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
            "https://drive.google.com/uc?export=view&id=16dXgpsRMn4dcYe9VI6pz6kDVrqU_p180",
            "https://drive.google.com/uc?export=view&id=13MbD7Q1jQwIK0ByFFOubU4jBW7PCcmg8",
            "https://drive.google.com/uc?export=view&id=13Wdgv9VfylUgnNrbhLRHGIQfTL9KpEDQ",
            "https://drive.google.com/uc?export=view&id=1y43-sBetd5yI4amnewOsOI6ScCDnZvlx",
            "https://drive.google.com/uc?export=view&id=1DElqlQzPsYWCy60coQfWZ2JciQlGxGHA",
            "https://drive.google.com/uc?export=view&id=1BaBqw1v3sabBQELuhzl0T1yMqcFk28z8",
            
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Bang Rendra panutan banget,brwibawa,ramah, dan yang bikin kagum bgt itu pengendalian emosinya okey banget, salut bisa tetep keliatan tenang walaupun keadaan nya keos, inspiratif bgt pokoknya ",  
                "pesan":"semangat terus kuliahnya bang, tetap jadi orang baik dan terus menginspirasi"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku sql",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Jo identik banget sama tangan yang disaku celana, bijak dan tegas juga",  
                "pesan":"semangat kuliahnya bang, sukses selalu"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy Dalam",
                "alamat": "Ayres Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak asik banget orang nya, suka tiba-tiba ngejoks random gtu lucuu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Belwis",
                "sosmed": "@puspadrr",
                "kesan": "Kakak kalem banget, pembawaan nya adem banget deh",  
                "pesan":"semangat kak kuliahnya, tetep jdi orang baik dan membawa aura positif untuk orang-orang di sekitar kakak"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak walaupun dari luar terlihat galak tapi aslinya baik dan ramah, kakak juga atif kegiatan",  
                "pesan":"semangat kuliahnya ya kak, jangan lelah untuk terus berkembang"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumbar",
                "alamat": "Gya kost korpri",
                "hobbi": "Cute Sekjen",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak hanum orang nya ceria dan humble juga, bisa buat seasana jdi seru",  
                "pesan":"semangat kuliahnya kak, jangan lupa senyum dan menebar kebaikan untuk orang orang di sekitar"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12k2hpTc_sTU5sPV-38LvSBHCI9IU6geI",
            "https://drive.google.com/uc?export=view&id=15B6p1oSF9SVrlEFHAEcTe_ne4INmfOru",
            "https://drive.google.com/uc?export=view&id=1YstaiXEUATVtZfqKNzyWv5Nn4dhNBqBu",
            "https://drive.google.com/uc?export=view&id=1PNte5ChCn1Hss0ByfjhyvQfK5TAhbRWZ",
            "https://drive.google.com/uc?export=view&id=1L6xazy2bpf8DfaSJHNolYPLIL49TXkNj",
            "https://drive.google.com/uc?export=view&id=1A8LxpRGncON9kryrQJgDQBS_9UmrHFz8",
            "https://drive.google.com/uc?export=view&id=16L66za0Yo5n86-ahN63Rb5nBfY4yc0ot",
            "https://drive.google.com/uc?export=view&id=1HZz4W_ktEYHuZlmwC18JcZF3lG5AGsnw",
            "https://drive.google.com/uc?export=view&id=1TrZhbBQbuVClysjLyXv-ilCycZ0CF4Ct",
            "https://drive.google.com/uc?export=view&id=17gWKZAsS3fFt6WRUoOla7X4T3ZyWwtIi",
            "https://drive.google.com/uc?export=view&id=13iTG0OVueyFm7Uo6emgM_uN85DGDQC5V",
            "https://drive.google.com/uc?export=view&id=1akZ8fbhEchRrK9Ln9-NK2zqCDSe09YuW",
            "https://drive.google.com/uc?export=view&id=1yDGy5ityBerupWGSuDi9MaX75ZYRo1gD",
            "https://drive.google.com/uc?export=view&id=1uYxx_sSgQD6NBxGRrj_loV3b7QjBlLO3",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "Nonton orang kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "-----",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "Lomba ga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Tidur",
                "sosmed": "@rnshism",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Ubud",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan baru",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "1234500023",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak Sawah",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450004",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Dengerin Spoyify",
                "sosmed": "@givarooo",
                "kesan": "-----",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales Chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main Paddle",
                "sosmed": "@iamridho",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "Koleksi batch google clood",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatra Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "Koleksi batch google clood",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17WjNEjeTUITRFOO9wRctaotVMiol6Hhf",
            "https://drive.google.com/uc?export=view&id=1dsEvHL5n9xQg_6VddK2yML2gXOeoedCJ",
            "https://drive.google.com/uc?export=view&id=1PllktHRmEtiCaETEpU-dDmZHTNa-ksgR",
            "https://drive.google.com/uc?export=view&id=1_iVfaKLi3TPCSiJZDdmRUm6-00HMeyxJ",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "dengerin lagu, nyanyi, baca, main game, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang bintang baik banget dan mengayomi kami dengan baik, bijak orangnya, dan seru pastinya",  
                "pesan":"semangat bang kuliahnya, sekses selalu dan semakin bersinar kedepannya"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadiaanjani",
                "kesan": "Kakak cantik dan baik banget, anggun gtu diliatnya",  
                "pesan":"semangat terus kuliah# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Main",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450069",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EiUyK9_AvD54iQSKJCxY0oYdhAnQG4jV",
            "https://drive.google.com/uc?export=view&id=1HuP2KSGo0Wec6hD5EXCflsJhQadKNTyp",
            "https://drive.google.com/uc?export=view&id=1ZSYPHm0DWLMALtKkGyZeDA6Vc5TRy-DI",
            "https://drive.google.com/uc?export=view&id=1yzflZ02j106FPGsqLKtF_FlxOtdkl8MZ",
            "https://drive.google.com/uc?export=view&id=1He9fFZ4lsF1021T_layK1R0TaE5Mw75l",
            "https://drive.google.com/uc?export=view&id=1HdPcV3xaSYLmZ2b0cGkC9kdiIgB9E5qp",
            "https://drive.google.com/uc?export=view&id=1rKTge5NDkSylA3oRZ0KcFZfBA6MqVagJ",
            "https://drive.google.com/uc?export=view&id=1vcM9Eeq9c7pNzgX0id49gb-B3KU6_u_e",
            "https://drive.google.com/uc?export=view&id=1ydxkT2Efxj1AumJEl8sBkdoC-Xt-RG5p",
            "https://drive.google.com/uc?export=view&id=1zf-Fa3YOlqoU5JcFzI5AgDEf7t5Ch0GT",
            "https://drive.google.com/uc?export=view&id=1Oo-UEwbRshcSOhRzRY4Q0g8vwPveDuQT",
            "https://drive.google.com/uc?export=view&id=1aBZNsBFSHb511TV_j3CMXKOj-M6ILQhn",
            "https://drive.google.com/uc?export=view&id=11StL0qe8ny3War2eGY4YSR-ts9uOmY3b",
            "https://drive.google.com/uc?export=view&id=1cfE-OekmsOg4Gko_gmwOh2jt2HfTUqfx",
            "https://drive.google.com/uc?export=view&id=1tEimluKjofO8CRbndWU22Y4WhmFL9g1N",
            "https://drive.google.com/uc?export=view&id=1qMZzqftEXnTxfMCrwaEnxsMd_VfXRGmh",
            "https://drive.google.com/uc?export=view&id=1V8Mq59C8cIfgqF9f8U7En81tLoxZrJWq",
            "https://drive.google.com/uc?export=view&id=1v6l44o8yTIxeOnjW3DEmyw75cRGfU32n",
            "https://drive.google.com/uc?export=view&id=1CWwu-9f534KIgfTqMd8-mZ7SMmGa7KiN",
            "https://drive.google.com/uc?export=view&id=1b8IEx6jKnqd8tMLrj8bvCX2Tobml-w_h",
            "https://drive.google.com/uc?export=view&id=1phA3H5QdTcDmTQcx8QnxB3xiv_I8jC29",
            "https://drive.google.com/uc?export=view&id=1psBI2732m8CYHNQP7ncaouaB5g7WA9jk",
            "https://drive.google.com/uc?export=view&id=1L_86SQx7nqYMl2HfdqTaWrQ3kAS62Srr",
            "https://drive.google.com/uc?export=view&id=1Pqh9dHLeo3xm-3ZbfDg4bV_y3jVAdU4N",
            "https://drive.google.com/uc?export=view&id=1miGXDp_2aGPTRDPrnFwcT_VlaHw2XuwV",
            "https://drive.google.com/uc?export=view&id=1WW10r5PpHKI3bAgCHGshKlz9mtDzAAxQ",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Ngekader 24",
                "sosmed": "@allyapasha_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Kost Orange",
                "hobbi": "Ngekader",
                "sosmed": "@arientakhsnl_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak Arienta",
                "hobbi": "",
                "sosmed": "@daffahdynn_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main Game",
                "sosmed": "@ginda_mrp",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kostan putri gerbang barat sebelah sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Fam",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabilaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22__",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung,Lampung Timur",
                "alamat": "Nangka 4",
                "hobbi": "Main Game, Kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450079",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jalan Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""# 1
            },
{
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Jl. Korpri Raya",
                "hobbi": "nontonin anak tari latihan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "----",  
                "pesan":"---"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Belwis",
                "hobbi": "Joki Strava",
                "sosmed": "@ihsan.myusus",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Panjang Selatan",
                "hobbi": "Terjun Payung",
                "sosmed": "@kevinaj__",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton Anak Tari Perform",
                "sosmed": "@m.ridwan_22",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngerjain Soal MTK",
                "sosmed": "@liano.wlm",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Ratu, Bandar Lampung",
                "hobbi": "Nonton Anime",
                "sosmed": "@rewinanaa",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    DepartemenPSDA()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gwy9Aq1n3M5Z5fr2IDygfkul9mxV_Px8",
            "https://drive.google.com/uc?export=view&id=14Hc5ZUfPmwBvf6AhsB9qj7vLeZlny4YH",
            "https://drive.google.com/uc?export=view&id=1JWprYDCppQ651t0QcRimWw81an5jk0aq",
            "https://drive.google.com/uc?export=view&id=1_UcdbIZzEGkOcC3hrBfG4nitF9kgIS5p",
            "https://drive.google.com/uc?export=view&id=1rZpl0oCnhUBq66beclId9gEBihunMMtL",
            "https://drive.google.com/uc?export=view&id=1URea-GR_WtGp320PWAK1neYVLJb3Hut6",
            "https://drive.google.com/uc?export=view&id=16xqqjc4dBbmD8abCUAf_hc52122bocMi",
            "https://drive.google.com/uc?export=view&id=1KtPUW-Iuf3bdfaPycTo2yPsLWzr5d6M5",
            "https://drive.google.com/uc?export=view&id=1-VrYum15WaCjJU-Qah3PCB9iRj-7R8xC",
            "https://drive.google.com/uc?export=view&id=1jq4j6xf4T7dMLX7Bi2BVUKvx5FY4Km6O",
            "https://drive.google.com/uc?export=view&id=1s7ocdOltgxOV83VPnJOrVBbU8EPmOeUF",
            "https://drive.google.com/uc?export=view&id=1Ui_ehrQ3ydUtwd9t1XlOaOxkqhM4PmU9",
            "https://drive.google.com/uc?export=view&id=1cpn43FZ8XJxVepD14vbfPpplyOXvHuxP",
            "https://drive.google.com/uc?export=view&id=1CNWtw1Uc64S_s8hkA4yTMGZkuCCQr5fj",
            "https://drive.google.com/uc?export=view&id=1QqVUubbQY6fg9Jig89M9Hil74s6m5iKu",
            "https://drive.google.com/uc?export=view&id=1yZofWBt1igbc_C2R4nuIcIoNKid-VgQW",
            "https://drive.google.com/uc?export=view&id=1nYMu5Y4BWjB76f6TY1T9FMM1WxkRcC9R",
            "https://drive.google.com/uc?export=view&id=1pmiZhVo_5sbNF-NUfUG_B5mFuFP-qED7",
            "https://drive.google.com/uc?export=view&id=1TmMuXbO4b6QR1fvSDF3pyD3HamXuI5a_",
            "https://drive.google.com/uc?export=view&id=1omCRBgUWN5MmSpadxGpJu7TnlMZYcv2X",
            "https://drive.google.com/uc?export=view&id=1eQK5Q7doyM9ylOSExxk13M4ny_Sch7q-",
            "https://drive.google.com/uc?export=view&id=13oAL3zl7-OY8JGcLGIq8FBfkRFrt69cM",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "1222450083",
                "umur": "22",
                "asal":"Serang,Baten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berenang",
                "sosmed": "@randaandriana_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234500119",
                "umur": "20",
                "asal":"Pramuka, Bandar Lampung",
                "alamat": "Perum Bukit Alam Permai 3, Blokk C, No.9",
                "hobbi": "Dengrin musik",
                "sosmed": "@keyashafi_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bummisari Kec.Natar",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Sale, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "-",  
                "pesan":"", # 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":"", # 1
            },
             {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang (main game)",
                "sosmed": "@fifah.zy",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer),tidur,jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@giofaniars_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450102",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans Sakum,Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "",  
                "pesan":"", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        
    DepartemenMIKFES()
    
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IM6p-gUe0AB7GRuNIZbvHztRfX0cZzPA",
            "https://drive.google.com/uc?export=view&id=1_b3u4esF6OvJH96BRrXpMU84xEwTbT6p",
            "https://drive.google.com/uc?export=view&id=1UuBqzyf2qPjpVT8ShXqISx9gnxjAj2qh",
            "https://drive.google.com/uc?export=view&id=1KmbUY4HyHPMoRzDP2AGxNcCoiYUi9hJN",
            "https://drive.google.com/uc?export=view&id=1vxYd5FQN-nzFtkAxND9ZXdcQpM1RFGg0",
            "https://drive.google.com/uc?export=view&id=1IpDuwvIqQIHEexyrekyMGpiHZ6o1TUUs",
            "https://drive.google.com/uc?export=view&id=1Q5WwNddeGsUYLcSrt5HLh1S7V6SRgxyn",
            "https://drive.google.com/uc?export=view&id=1N2254KdgE0A7c8hklhlY_Uu4FzmGlkRn",
            "https://drive.google.com/uc?export=view&id=1sImzfV2jdYRpra_gMzIialDDznMvJofN",
            "https://drive.google.com/uc?export=view&id=1FS7oKes-Q4SvTrxjRbLCWGvDihVHoEyv",
            "https://drive.google.com/uc?export=view&id=1zuE0V0CO-6ZL09Ld_u8aWwauXCYWiYth",
            "https://drive.google.com/uc?export=view&id=1DQMucG7enOdK3HTDhce9Mf3KtcwEZoXY",
            "https://drive.google.com/uc?export=view&id=1V7XobQoS2by4TJZkLLoTz9XgcIQcevlG",
            "https://drive.google.com/uc?export=view&id=1aYaYRWVlqvI3GLFuzSMvGVf9L6rpfscB",
            "https://drive.google.com/uc?export=view&id=1xH9iitpAP99aaKrr2Q_BJzrUWS_Ayq02",
            "https://drive.google.com/uc?export=view&id=1VJ0ynDLAfhaG5qIuhQdLvXQJAhEdmHtB",
            "https://drive.google.com/uc?export=view&id=1MSwY-H01odOrxgfVX4v1WRpXfLJsKwRp",
            "https://drive.google.com/uc?export=view&id=1torlW2rctumHK9nhF5GuxZMbF0edhLs_",
            "https://drive.google.com/uc?export=view&id=12BpclO8I4UQrdTNVmuPtUQCSPG0k12qK",
            "https://drive.google.com/uc?export=view&id=10PVUDk2Z6MHomrMF744YFg7jMrPA587s",
            "https://drive.google.com/uc?export=view&id=1dMppHpaIA3ZJrtA1DN5KC1A7U-IBM4tO",
            "https://drive.google.com/uc?export=view&id=13pMArBVOWpczNR3SisUDfxUNpQlP6Vtb",
            "https://drive.google.com/uc?export=view&id=1eQuesEUxQEYXE1e--Z3fmNHGjhSlYwPk",
            "https://drive.google.com/uc?export=view&id=1Ty2bom43xNRkh6XnrysMJdzT_Tdp_ebS",
        
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Warjo",
                "hobbi": "Makan Warjo",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Bang Arafi seru dan enak diajak ngobrol",  
                "pesan":"semoga makin sukses dan tetap rendah hati ya bang!", # 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana kalem tapi asik banget pas diajak ngobrol",  
                "pesan":"Makasih kak udah ramah dan menyenangkan!", # 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "Kak Keisha keliatan anggun dan sopan banget",  
                "pesan":"Semoga selalu bahagia dan sukses terus ya kak!", # 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini ramah dan enak banget diajak cerita",  
                "pesan":"Tetap semangat dan jangan capek senyum ya kak!", # 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Bang Arya santai tapi berwibawa",  
                "pesan":"Semangat terus bang, sukses buat semuanya!", # 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Khoirul sopan dan berenergi positif banget",  
                "pesan":"Tetap semangat dan jangan berhenti berkembang ya kak!", # 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia lucu dan ceria banget waktu ngobrol",  
                "pesan":"Semoga hari-harinya selalu penuh semangat, kak!", # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla lembut tapi menyenangkan banget",  
                "pesan":"Terus semangat dan sukses selalu ya kak!", # 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@",
                "kesan": "Bang Syahrialdi kalem tapi keren waktu ngobrol",  
                "pesan":"Semoga makin sukses dan tetap rendah hati bang!", # 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea sopan dan smart banget",  
                "pesan":"Terima kasih udah ngasih kesan yang positif banget kak!", # 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak Cindy rame dan seru diajak ngobrol",  
                "pesan":"Tetap semangat kak, sukses buat semuanya!", # 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea friendly banget dan gampang nyatu",  
                "pesan":"Semoga makin sukses dan terus ceria ya kak!", # 1
            },
            {
                "nama": "Desman Velius Halaws",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman keren banget",  
                "pesan":"Semoga terus semangat dan sukses selalu bang!", # 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Devyna ceria banget dan bikin suasana enak",  
                "pesan":"Tetap semangat dan terus bawa vibes positif ya kak!", # 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Luthfia rame dan lucu banget pas ngobrol",  
                "pesan":"Semangat terus kak, sukses buat semuanya!", # 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "Bang Irvan santai tapi asik banget diajak ngobrol",  
                "pesan":"Semoga makin sukses dan terus semangat bang!", # 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "Bang Adit kalem tapi punya pandangan menarik",  
                "pesan":"Sukses terus bang, tetap semangat ya!", # 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya ceria dan ekspresif banget",  
                "pesan":"Makasih kak udah nyebarin energi positif!", # 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "kalem tapi asik banget diajak ngobrol",  
                "pesan":"Semoga sukses selalu dan terus semangat ya kak!", # 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melinza lembut dan sopan banget",  
                "pesan":"Terus semangat kak, semoga semua yang dicita-citain tercapai!", # 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla orangnya komunikatif dan semangat banget",  
                "pesan":"Sukses terus kak, semoga semua lancar!", # 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak Nurul lembut dan ramah banget waktu ngobrol",  
                "pesan":"Tetap semangat dan terus berkembang ya kak!", # 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois santai tapi seru banget",  
                "pesan":"Semoga makin sukses dan tetap keren bang!", # 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kak Tarisya lembut dan sopan banget pas ngobrol",  
                "pesan":"Semoga selalu bahagia dan sukses ya kak!", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        
    DepartemenEksternal()
    
elif menu == "Departemen Internal":
    def DepartemenInternal():
         gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c1lctZTXVxK0zSpfYK8G2hVuMtnvQDni",
            "https://drive.google.com/uc?export=view&id=178m2pC873IKlgsQssjoLNCY0U8IQca-t",
            "https://drive.google.com/uc?export=view&id=1FRl-LPSrOEoDhTig5OtovMa8MTHrf8l9",
            "https://drive.google.com/uc?export=view&id=1ElO0KnA-42LTCBmwRUVewUG7_qee5yxP",
            "https://drive.google.com/uc?export=view&id=11Zph3HiqArQqyXBKHc1Y4tGP_LndMNIK",
            "https://drive.google.com/uc?export=view&id=1im4_erzyM7y7iJhif15k0tKfeZOobnTT",
            "https://drive.google.com/uc?export=view&id=1lkRig0DpQXC1mZjZcsC4WZNdTlV9LLul",
            "https://drive.google.com/uc?export=view&id=1rvd0MHJj0gWal0ilEZDEDSeMDWprkdwI",
            "https://drive.google.com/uc?export=view&id=1S5nkkFJlOHOw8S5HOx6qEGJNQQL4WCei",
            "https://drive.google.com/uc?export=view&id=1iuEiGCHiwQtb92Jik45LQ7vp4tNs4RPP",
            "https://drive.google.com/uc?export=view&id=1hvML1b3Y7PyYQozq2mz1qZg0HtnfcJpX",
            "https://drive.google.com/uc?export=view&id=113VQpVqYVOwHgfqMoeI2KZb1imzCXJLt",
            "https://drive.google.com/uc?export=view&id=1mhXeQLSNpSxJqOOIosLirDz1j-xg0_SP",
            "https://drive.google.com/uc?export=view&id=1NCZ9NcMuQfsu3J3LPOB8DrJLE831Fp4W",
            "https://drive.google.com/uc?export=view&id=1CCHVBBkAe-MX7JzDi32vRjJxfizhVNR3",
         ]
         data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "12245030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kak Rani modis banget, gayanya kece",  
                "pesan":"Semoga kak Rani selalu sehat dan makin bersinar ke depannya"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "tenang banget, tapi tetap seru diajak ngobrol",  
                "pesan":"Tetap semangat kuliahnya kak, sukses terus ya!"# 1
            },
            {
                "nama": "Salwa Farhanatusaiidah",
                "nim": "12245055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa lembut banget orangnya, enak banget diajak cerita",  
                "pesan":"Semoga kak Salwa makin sukses dan selalu diberi kesehatan"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azza.raaa_",
                "kesan": "baik banget, gampang akrab juga sama orang baru",  
                "pesan":"Tetap semangat kuliahnya kak, sukses terus ya!"# 1
            },
            {
                "nama": "Haikal fransisko Simbolon",
                "nim": "122450106",
                "umur": "18",
                "asal":"Tulang Bawang",
                "alamat": "Sukabumi",
                "hobbi": "Membersihkan rumah",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang Haikal ternyata asik, awalnya keliatan serius",  
                "pesan":"Semangat terus kuliahnya Bang Haikal!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450076",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak Iqfina cantik dan punya vibe yang lembut banget",  
                "pesan":"Semoga Kak Iqfina selalu bahagia dan lancar kuliahnya"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450009",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak May keren banget dan keliatan percaya diri",  
                "pesan":"sehat terus dan makin sukses ya kak"# 1
            },
            {
                "nama": "Muhammad Naufal Afghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@Muhammadnaufalafghani73",
                "kesan": "Abangnya kalem banget, tapi seru kalo udah ngobrol",  
                "pesan":"Semangat terus kuliahnya Bang Naufal!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya asik dan punya aura positif banget",  
                "pesan":"Semoga Bang Zailani makin semangat dan terus sukses!"# 1
            },
            {
                "nama": "Rendi Alezander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@lexanderr",
                "kesan": "Abang Rendi kalem banget, asik diajak ngobrol juga",  
                "pesan":"Semoga Bang Rendi selalu dilancarkan semua urusannya"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna ceria banget dan gampang bikin suasana rame",  
                "pesan":"Kak Hanna ceria banget dan gampang bikin suasana rame"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak Keren beneran keren, gayanya simple tapi manis",  
                "pesan":"Semoga Kak Keren selalu percaya diri dan sukses terus!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hifzky",
                "kesan": "Abang Hanif santai banget orangnya, gampang diajak ngobrol",  
                "pesan":"Semoga Bang Hanif makin sukses dan tetap rendah hati!"# 1
            },
            {
                "nama": "Sarah wasti",
                "nim": "122450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah lembut dan pembawaannya tenang banget",  
                "pesan":"Semoga Kak Sarah selalu dikasih kebahagiaan dan kesuksesan"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "Main Rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kak Zahra manis banget dan keliatan friendly",  
                "pesan":"Semoga Kak Zahra terus semangat dan sukses selalu!"# 1
            },
        ]
         display_images_with_data(gambar_urls, data_list)
        
    DepartemenInternal()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mv_wIXGa1k2HGtmY_z4NkU5tPKJYb6oJ", 
            "https://drive.google.com/uc?export=view&id=10Q4T_1QNptKlvjWL5vEXWEYa2ZDJdebA", 
            "https://drive.google.com/uc?export=view&id=1cHyH62EDnXcW0vIFEUXpIDsNsMcxoftG",  
            "https://drive.google.com/uc?export=view&id=112i2-N_Cyw13bK8sYa1AcVi04vw3lz3Q", 
            "https://drive.google.com/uc?export=view&id=1dz9CaUHM4AafYTxBlaDDkkUQmyc0D68Y",  
            "https://drive.google.com/uc?export=view&id=1xuBiN_bNdpj_l5EMFoFf1PNLA88WvCKm",  
            "https://drive.google.com/uc?export=view&id=1Luui0tFwkkquL4fWmkREpnBCDljupek0",  
            "https://drive.google.com/uc?export=view&id=1esgjLwslKOboSY6skWdO9L1DB7nye9Gb",  
            "https://drive.google.com/uc?export=view&id=1Jj-xKOdipjdrm9Y25DTNBQq29GJXNdSN",  
            "https://drive.google.com/uc?export=view&id=1ExkME20BZ-EUj2oItukei6p5q63c2aFX", 
            "https://drive.google.com/uc?export=view&id=1gBhntgdYFTfJRWjMuYZF7pyFiZQ2BhoQ",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Balam",
                "alamat": "Belakang PB",
                "hobbi": "Joging",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya seru banget diajak ngobrol, pembawaannya santai tapi nyambung terus",  
                "pesan":"Semangat terus bang, semoga semua rencananya lancar dan sukses selalu!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450012",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "kakaknya kalem banget",  
                "pesan":"Tetap semangat dan semoga hal-hal baik selalu nyertai kakak!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki_",
                "kesan": "Abangnya humble banget, enak banget diajak ngobrol",  
                "pesan":"Sukses terus ya bang! Tetap jadi pribadi yang asik dan rendah hati "# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Joging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya bersemangat banget dan energinya positif",  
                "pesan":"Terus sebarkan energi baiknya ya kak, semangat selalu!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton dramashort di fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakaknya ramah banget dan gampang akrab",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_azazahra",
                "kesan": "Kakaknya baik banget dan sopan banget pas ngobrol",  
                "pesan":"Tetap semangat ngejar cita-citanya ya kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya tenang tapi seru",  
                "pesan":"Terus semangat ya bang, semoga sukses di tiap langkah!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya ramah banget dan murah senyum",  
                "pesan":"Semoga makin sukses dan selalu dikelilingi orang-orang baik!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gang perwira 2",
                "hobbi": "Nontol alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak gayanya santai tapi nyambung",  
                "pesan":"Tetap semangat kak, semoga semuanya berjalan lancar!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya lembut banget dan sopan waktu ngobrol",  
                "pesan":"semangat terus ya kak! Semoga semua yang dicita-citakan tercapai!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kakaknya supel dan mudah akrab, suasananya jadi cair",  
                "pesan":"Tetap semangat ya kak! Jangan lupa istirahat juga!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1J7KkVZIzQc54lA6PWNW-Ul3v9lGPatKb",
            "https://drive.google.com/uc?export=view&id=11x-hrG4uK7i73NwM53CmhRkatb4jz-TN",
            "https://drive.google.com/uc?export=view&id=1ssDT0Erjko0GkXOhGKYID0BoUrwVIpMT",
            "https://drive.google.com/uc?export=view&id=17ZkS4rqzqgcX7zr-N1MqOMtn1yqZv7cz",
            "https://drive.google.com/uc?export=view&id=1h9fyOjxfZZ_f0AqyM-ddLmsqQKbMTAtX",
            "https://drive.google.com/uc?export=view&id=1qxhlcaLJmpSSlv6cq3524UzNIGltj3HZ",
            "https://drive.google.com/uc?export=view&id=1IUv61_45y4apAFjB7U9hLbCbLIQyopGl",
            "https://drive.google.com/uc?export=view&id=1KfZHZI9KtiLd4qiVhul2sMY92uS7eFiZ",
            "https://drive.google.com/uc?export=view&id=1176i6Zt4QqEU6od8BymbBDHIQgC95aRJ",
            "https://drive.google.com/uc?export=view&id=1B-5-jBfYiRtstVHN2IqMoHgd0rofdTRm",
            "https://drive.google.com/uc?export=view&id=1JfL2Ksu_j7shyAKYjRgDDBbXq_rYxnCK",
            "https://drive.google.com/uc?export=view&id=1QkNCgO1-chXwybMAdEn1wDK3hu41dxzA",
            "https://drive.google.com/uc?export=view&id=1fU_PNVoeXho45jhhKLO4gg7QCqON07Ny",
            "https://drive.google.com/uc?export=view&id=1W3qPFqTkU68COilUl3VEM3piiXs6rmqZ",
            "https://drive.google.com/uc?export=view&id=1qwwnR4fIvVCmYPHO_j-KCnkB2j03WB-L",
            "https://drive.google.com/uc?export=view&id=1-NU2H7kUmUGwE5ouQtZrmMaWRXyF1-nJ",
            "https://drive.google.com/uc?export=view&id=1f__KOZQpbAIdhW29mYE86UoLalZZxMil",
            "https://drive.google.com/uc?export=view&id=1LDlNxShid9W23nGyr7eNIoz7SmJTRwNo",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya cantik, asikk seruu, dan cara bicaranya enak banget didengar",  
                "pesan":"Semangat terus ya kak! Tetap jadi pribadi yang lembut tapi kuat"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Rahma orangnya hangat banget, gampang bikin suasana nyaman",  
                "pesan":"Semoga selalu bahagia dan sukses di setiap langkah kak!"# 1
            },
            {
                "nama": "Khoriul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam__",
                "kesan": "Abangnya seru, gayanya santai tapi nyenengin kalau ngobrol",  
                "pesan":"Tetap semangat bang, semoga makin banyak hal keren yang bisa dicapai!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Hui",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya asik banget, pembawaannya santai tapi berwibawa",  
                "pesan":"semangat terus ya bangg, makin sukses!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "keliatan energik dan easygoing",  
                "pesan":"Tetap semangat bang! Jangan lupa jaga kesehatan juga"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa asik banget",  
                "pesan":"Semangat ya kak! Semoga semua hal baik datang di waktu yang tepat"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122350020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaa",
                "kesan": "Kakaknya pintar banget dan keliatan rajin, inspirasional!",  
                "pesan":"Semoga terus jadi sosok yang semangat dan rendah hati ya kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kak Aliya ramah banget dan suaranya lembut, enak diajak ngobrol",  
                "pesan":"Semangat terus ya kak, terus kembangin bakatnya!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna kalem dan sopan, pembawaannya tenang banget",  
                "pesan":"Semoga kakak selalu diberi semangat dan kebahagiaan setiap harinya!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kak Feby manis banget, pembawaannya ceria dan positif",  
                "pesan":"Semoga terus jadi sumber semangat buat orang di sekitar ya kak!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kak Hafsa keliatan sabar banget dan punya aura tenang",  
                "pesan":"Tetap semangat ya kak! Semoga semua impiannya tercapai"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas, Jati Agung",
                "hobbi": "Dengar musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla lembut dan ramah banget, enak diajak ngobrol santai",  
                "pesan":"Semoga kuliahnya lancar dan makin berprestasi ya kak!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania seru banget, pembawaannya santai dan friendly",  
                "pesan":"Tetap semangat dan jangan lupa main roblox buat healing"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangnya kalem tapi lucu, asik banget pas diajak ngobrol",  
                "pesan":"Sukses terus bang, semoga makin banyak rezeki dan hal baik!", # 1
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana kelihatan pintar dan sopan banget",  
                "pesan":"Semangat terus ya kak, semoga selalu jadi inspirasi buat banyak orang!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra kreatif banget, keliatan dari cara dia cerita",  
                "pesan":"Terus berkarya ya kak! Dunia butuh banyak orang kreatif kayak kakak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah balau residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak Eigi punya vibe kalem dan elegan banget",  
                "pesan":"Semoga terus bahagia dan sukses di bidang yang kakak suka!"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Romauli enerjik banget, pembawaannya ceria dan percaya diri",  
                "pesan":"Terus semangat ya kak! Semoga makin bersinar di tiap langkah"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()














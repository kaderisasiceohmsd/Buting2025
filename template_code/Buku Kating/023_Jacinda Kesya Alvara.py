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
                "kesan": "-----",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku sql",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy Dalam",
                "alamat": "Ayres Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumbar",
                "alamat": "Gya kost korpri",
                "hobbi": "Cute Sekjen",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12k2hpTc_sTU5sPV-38LvSBHCI9IU6geI",
            "https://drive.google.com/uc?export=view&id=15B6p1oSF9SVrlEFHAEcTe_ne4INmfOru",
            "https://drive.google.com/uc?export=view&id=1PNte5ChCn1Hss0ByfjhyvQfK5TAhbRWZ",
            "https://drive.google.com/uc?export=view&id=1y43-sBetd5yI4amnewOsOI6ScCDnZvlx",
            "https://drive.google.com/uc?export=view&id=1L6xazy2bpf8DfaSJHNolYPLIL49TXkNj",
            "https://drive.google.com/uc?export=view&id=1A8LxpRGncON9kryrQJgDQBS_9UmrHFz8",
            "https://drive.google.com/uc?export=view&id=16L66za0Yo5n86-ahN63Rb5nBfY4yc0ot",
            "https://drive.google.com/uc?export=view&id=11HZz4W_ktEYHuZlmwC18JcZF3lG5AGsnw",
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
                "kesan": "-----",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadiaanjani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
            "https://drive.google.com/uc?export=view&id=1O6l2NOmQBio49mz66mQydeBJfPT1mp2i",
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
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@afifahhnsrn",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
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
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@daffahdynn_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
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
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
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
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
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

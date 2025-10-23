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
            "https://drive.google.com/uc?export=view&id=14g_TmuRo5vL0jGnQI0EMBKhSoTe1gT0n",
            "https://drive.google.com/uc?export=view&id=1IetOiuDn2Jg4U0Zxc3lDNpO6hLsj0va_",
            "https://drive.google.com/uc?export=view&id=1SXFAtqHB84s0PzELJvn-UaN5radbpArx",
            "https://drive.google.com/uc?export=view&id=1v7Rt_l-PRIH7lp3HL2jt27LTiu4ujRcA",
            "https://drive.google.com/uc?export=view&id=1iBZzGWXl_D0KDBlSmDmrQaztAIiPS8qu",
            "https://drive.google.com/uc?export=view&id=1e1OrcGVC12P9qrnFMa_054BeErSGPLcK",
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
                "kesan": "Kakaknya keren, baik dan asik",  
                "pesan": "Dimudahkan semuanya ya kak apalagi di semester akhir. SEMANGATTT" 
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya lucu, asik dan keren",  
                "pesan": "Semangat semester akhir kak, tetap andalkan Tuhan Yesus"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya keren dan asik",  
                "pesan": "Semangat semester akhir kak, tetap andalkan Tuhan Yesus"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya cantik dan lucu",  
                "pesan": "Semangat kak"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya lucu banget, orangnya asik",  
                "pesan":"Semangat kak semester akhirnya"# 1
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya cantik dan lucu",  
                "pesan": "Semangat ya kak semester akhirnya"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SJzaDhyzbFQU4sUKkCucatiQ02FRZsDh",
            "https://drive.google.com/uc?export=view&id=1vEhVv3oWuTA0jxG3VE35jVcZRHZ2KQHF",
            "https://drive.google.com/uc?export=view&id=18eQ8jmGasgCf3Qc7ha6DoazjTMB9lqjJ",
            "https://drive.google.com/uc?export=view&id=1ArBZOSp9m6ILPzHbRNCIOVz201xGZdgI",
            "https://drive.google.com/uc?export=view&id=1YOzgSl5Kglc3PbAHZVeK9dXsQp1WN_dP",
            "https://drive.google.com/uc?export=view&id=1uHnfvNXIKp1eKdwI_fgfWwZGiGR5ZS9l",
            "https://drive.google.com/uc?export=view&id=14lDDtRDs1zzFRP2dRa3iAz0tMXuobD2M",
            "https://drive.google.com/uc?export=view&id=1MGHBrd5mYCjTaoU42DHtiRqc1z5pIafT",
            "https://drive.google.com/uc?export=view&id=12CDrjNQ18SYIurDh8by2V4vUh8XOXkdY",
            "https://drive.google.com/uc?export=view&id=1yojSuDvCEMLZIMGLA0ge1Dw8S3zEpO_-",
            "https://drive.google.com/uc?export=view&id=1zY7g_NCKfUYZk7t-GK2wCI8ncu0LciFJ",
            "https://drive.google.com/uc?export=view&id=19Bcgt4WBaTstyucY931AQ94NcVoenH3V",
            "https://drive.google.com/uc?export=view&id=1XXuskG7sq2h6w4hKkBkHpRfjTELKVxh9",
            "https://drive.google.com/uc?export=view&id=1Wu_cXHMwrVe0OZJDJnr7kpJxVOfXBRWz",
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
                "kesan": "Kakaknya manis, lucu ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya. Tetap andalkan Tuhan Yesus ya kak"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "Kakak nya baik, seru ",  
                "pesan": "Sehat selalu kak, dilancakan semuanya "# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya keren dan asik ",  
                "pesan": "Semoga dilancarkan urusannya kak "# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kakaknya keren ",  
                "pesan": "Semoga urusannya diperlancar "# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Kakaknya keren banget ",  
                "pesan":"Semoga diperlancar semuanya  "# 1
            },
             {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya cantik dan lucu ",  
                "pesan": "Semangat kak, diperlancar semuanya "# 1
            },
              {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Kakaknya keren banget ",  
                "pesan": "Semoga dilancarkan semuanya kak "# 1
            },
              {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya keren banget",  
                "pesan": "Tetap semangat ya kak"# 1
            },
              {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Keren banget kakaknya",  
                "pesan": "Tetap semangat ya kak"# 1
            },
              {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya lucu, cheerfull banget",  
                "pesan": "Tetap semangat ya kak" # 1
            },
              {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "kakaknya keren banget",  
                "pesan": "Tetap semangat ya kak"# 1
            },
              {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Kakaknya keren",  
                "pesan": "Tetap semangat kak"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "Kakaknya cantik, lucu",  
                "pesan": "Semangat ya kak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "Kakaknya keren dan lucu",  
                "pesan": "Semangat kakak"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1W7LRKmzFD0iFnmRqHgq-0ffWeSlQjGsx",
            "https://drive.google.com/uc?export=view&id=1j0RXV6qEVvJ5EsZcF8vAr3HoVEIJXEME",
            "https://drive.google.com/uc?export=view&id=18FKOzsyY7s4Cmg0z6BrVoxnHZ2yoxptS",
            "https://drive.google.com/uc?export=view&id=1EOl5k1hNLAMy-JNf43z7Pn48_vblWD8a",
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
                "kesan": "Kakaknya keren banget sih, asik",  
                "pesan": "Semangat kak"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya cantik banget",  
                "pesan": "Semangat selalu kakak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya cantik dan asik",  
                "pesan": "Semangat selalu ya kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya cantik dan lucu",  
                "pesan": "Semangat ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XF4k2U3-f1_fEXaA75wEVmabUWSCBk13",
            "https://drive.google.com/uc?export=view&id=1zSf34kQ4_9fcPAmbjn0CGLdsJ4fLkPC0",
            "https://drive.google.com/uc?export=view&id=1tHCj0newnYAdIA5tDx50vbf0aQd1ZClx",
            "https://drive.google.com/uc?export=view&id=1oCqI9batYhs1vnxcO0CARylUihTYVqJL",
            "https://drive.google.com/uc?export=view&id=1f2YLOg2CsMXVSWW0GLb7YjqKyZJbydTK",
            "https://drive.google.com/uc?export=view&id=1hglAUO4lBEJiUm-8okivIc_sD_2MueYX",
            "https://drive.google.com/uc?export=view&id=1du8_iYtD2DCudoYzwAK-nPhV6dLgNxpV",
            "https://drive.google.com/uc?export=view&id=13rz_90ObyzhHfBCRSmnUErzVLeGKQhuf",
            "https://drive.google.com/uc?export=view&id=137t6HH-GPExW2pXiR2H0xjCRojr0TWB6",
            "https://drive.google.com/uc?export=view&id=1Pprdbl1xNDCcXL10ARqJXzluULnRyYBg",
            "https://drive.google.com/uc?export=view&id=1mw_iy2EoWnWV5gB-lMnwgVwRj6Y-5XeG",
            "https://drive.google.com/uc?export=view&id=1yQ7tP667GJSGGVHAKvgLWEIDthHHqc5g",
            "https://drive.google.com/uc?export=view&id=1Kcg9Pc3j0mMRoAY0mf-LiN2ZZc4V4DKv",
            "https://drive.google.com/uc?export=view&id=1BQuau1hd_VJjN-KaHwAbH5ZRAXcr4SJE",
            "https://drive.google.com/uc?export=view&id=1BlATOyo_gToiY6630D8q9kIa2Qu-oMVy",
            "https://drive.google.com/uc?export=view&id=1rVWh_Y7Rkj_llF3XYt9GNTGfWEz2szEm",
            "https://drive.google.com/uc?export=view&id=1mw_iy2EoWnWV5gB-lMnwgVwRj6Y-5XeG",
            "https://drive.google.com/uc?export=view&id=1HUViYhOtFY2KBDpAC3K-xlQurHEJAPSE",
            "https://drive.google.com/uc?export=view&id=1Tf1bFJexFeAbHTyT0bpH6fyfDN211VXl",
            "https://drive.google.com/uc?export=view&id=1fYX34rW3vwT1cenS6uZTBegoEEIKJxP_",
            "https://drive.google.com/uc?export=view&id=1uNY7Cr20WvDgTat2h_RPKgxcdDMqXZUw",
            "https://drive.google.com/uc?export=view&id=1ovD8p40T0U7x6qz_LOgTPMQuTPsqU8ar",
            "https://drive.google.com/uc?export=view&id=1ZefdkGdVNG413wvVLqSp8-b_juVOSOxq",
            "https://drive.google.com/uc?export=view&id=17HAOzsgvtWOFIZGpxdmuIEyvpIYfL_4-",
            "https://drive.google.com/uc?export=view&id=1_XLXl9AHm_LrTo-bVdp4SzFQ2E6dPEFP",
            "https://drive.google.com/uc?export=view&id=1x0YxcB_owX9qLBUnGFq0I76W2wNMF8vc",

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
                "kesan": "Kakaknya keren dan asik, seru banget",  
                "pesan":"Semangat ya kak semester akhirnya"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "Kakaknya cantik banget, tegas tapi baik",  
                "pesan":"Semangat terrus ya kak, dilancarkan kuliahnya"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "Kakaknya tegas, tapi tetap profesional, baik banget lagi",  
                "pesan":"Semangat terus ya kak, kesehatannya jangan lupa dijaga"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": " ",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Kakaknya keren banget, berwibawa dan baik banget",  
                "pesan":"Semangat ya kak, semoga jadi presma aminnnnnn"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakaknya cantik bangett, manis juga ngalahin gula pokoknya",  
                "pesan":"Semangat terus ya kakak cantik, semoga kuliahnya dilancarkan selalu"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Kakaknya tegas banget, tapi ternyata baik banget, dan profesional banget",  
                "pesan":"Semangat ya kak, tercapai semua goalsnya di Itera ya kak"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Kakak nya tegas, tapi ternyata baik banget dan keren banget",  
                "pesan":"Tetap semangat ya kak, tetap andalkan Tuhan Yesus ya kak"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":" ",
                "alamat": " ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "Kakaknya cantik banget, manisss, walaupun tegas tapi profesional keren banget",  
                "pesan":"Semangat ya kakak cantik, dipermudah semuanya"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "Kakaknya pinter banget dan baik banget, tegas tapi tetap profesional",  
                "pesan":"Tetap semangat ya kak, jaga kesehatan nya"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "Kakaknya tegas banget, bikin takut, tapi ternyata aslinya baik pake banget",  
                "pesan":"Semangat ya kak, dilancarkan semuanya dan tercapai semua targetnya"# 1
            },
            {
                "nama": "Vany Salsabila Putri", 
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya cantik dan manis banget, lucu",  
                "pesan":"Tetap semangat kakak cantik, kesehatan nya jangan lupa dijaga"# 1
            }, 
                {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "Kakak nya baik banget, keren",
                "pesan": "Semangat terus ya kak kuliahnya" # 12
            },
            
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakak nya lucu imut dan baik lagi",
                "pesan": "Semangat terus ya kak, dijaga kesehatannya" # 13
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya cantik banget, manis, lucu",
                "pesan": "Tetap semangat ya kakak cantik" # 16
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya cantik, terus keliatan lagi sibuk, tapi ternyata baik banget",
                "pesan": "Semangat ya kak, kesehatannya juga harus di prioritasin" # 15
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakaknya lucu banget, baik juga, seneng deh di puji imut sama kakaknya, padahal kakaknya lebih imut",
                "pesan": "Semangat terus ya kakak cantik" # 14
            },
            
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Kakaknya baik banget dan ramah",
                "pesan": "Semangat terus ya kak" # 17
            },
            
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Kakaknya ramah banget sih",
                "pesan": "Semoga selalu diberikan kemudahan ya kak " # 18
            },
             {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "Kakaknya keren banget udah menjuarai lomba tari",
                "pesan": "Semangat terus ya kakak cantik, btw kita 1 kosan kak" # 24
            },
            
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "Kakaknya baik banget, ramah",
                "pesan": "Semangat selalu ya kak kuliahnya" # 19
            },
             {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "Kakaknya keren banget",
                "pesan": "Semangat ya kak basketnya" # 23
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "Kakaknya lucu banget baik dan ramah",
                "pesan": "Semangat selalu ya kak" # 20
            },
            
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "Awalnya kukira kakaknya serem tapi ternyata lucu banget",
                "pesan": "Semangat terus ya kak" # 21
            },
            
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "Kakaknya tegas banget tapi baik",
                "pesan": "Semangat terus ya kak" # 22
            },

            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak kiting yang suoer duper baik, kenal kakak dari panitia paskah huhuu baik banget loplop kak",
                "pesan": "Semangat ya kak, moga ketemu di 1 kepanitiaan lagi" # 25
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Kakaknya baik banget, ramah",
                "pesan": "Semangat terus ya kak" # 26
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EIeKDIkbiw1ewmm5PWWLewzIFXGjHZBj", #1
            "https://drive.google.com/uc?export=view&id=19_5WusRBxzhZmB13IoiVj-FGl-rMZvlz", #2
            "https://drive.google.com/uc?export=view&id=1BYfYLA58KN-l_n2SkH1nf8-7pLQTgT_S", #3
            "https://drive.google.com/uc?export=view&id=10m-PzFup8iL3tu-i5s3PwYcY33s_xtiU", #4
            "https://drive.google.com/uc?export=view&id=1rnQKFAyiw6cKxXuLMCPQw0CbDqQAMt3b", #5
            "https://drive.google.com/uc?export=view&id=14UghtUwppV4ESfByNgcHPrzrWlFqDZXj", #6
            "https://drive.google.com/uc?export=view&id=1acHmFGGyrcNPkEhp71dc6p6znLhptDJK", #7
            "https://drive.google.com/uc?export=view&id=1yEv8gVcIbFKY6V1IBSsxNUhGj7RMOFE6", #8
            "https://drive.google.com/uc?export=view&id=1rkILUvNCCBIRNd5d0qqdye9mZMaadvor", #9
            "https://drive.google.com/uc?export=view&id=12gwkDsK4cJYFw4KnHsVqV2bAiIDLWWlT", #10
            "https://drive.google.com/uc?export=view&id=1PS2g6VEfU_LEmM6PVLFwZOrAax2K7Xid", #11
            "https://drive.google.com/uc?export=view&id=1rVBbs3-2ITxZMx13h-dKVxcSNIF98bcv", #12
            "https://drive.google.com/uc?export=view&id=1x3NmjerUixeexv9ZBtSVozVH8bgv1Ms4", #13
            "https://drive.google.com/uc?export=view&id=17LFa_r9ZLmZ82ZAAuxpjClxLfCGUeHKA", #14
            "https://drive.google.com/uc?export=view&id=1qVGzj6OLR1xf-wmgYx-LF4u7Tn-7kQM2", #15
            "https://drive.google.com/uc?export=view&id=1QZBKH1X4QkLIeQ7CbNTQImPr9Gi65f9N", #16
            "https://drive.google.com/uc?export=view&id=15brky471W_WUD7FD_A2mFccd7diXLtIn", #17
            "https://drive.google.com/uc?export=view&id=1WH-Hr_icRQW1wj6xjqlKm5oWdsbA3RKS", #18
            "https://drive.google.com/uc?export=view&id=1xLrOrZitc1Pcqgyt62R32ghh1pxcjr-0", #19
            "https://drive.google.com/uc?export=view&id=1fDCSikeyiE0KbPMA0IPrkduqFHArTBcn", #20
            "https://drive.google.com/uc?export=view&id=1K0eqRXKKEyzhRgg3ik3hjUET000ONYGC", #21
            "https://drive.google.com/uc?export=view&id=1irh62f9R2-rb7v_QNEx687CfTUmLBvo6", #22
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
                "kesan": "Kakaknya keren dan wawasannya luas, keliatan banget orang pinternya",  
                "pesan":"Semangat kuliahnya kakk "# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya emezing banget, dan cheerfull",  
                "pesan":"Tetap sehat dan cemangat selalu kak"# 2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakaknya kelliatan keren banget",  
                "pesan":"Jangan lupa caga kesehatannya ya kak"# 3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Cantik banget",  
                "pesan":"Lancar terus ya kak kuliahnya"# 4
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakaknya keren banget banget banget, duta nya anak data",  
                "pesan":"Semangat terus ya kak, kakaknya keren banget pokoknya"# 5
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakaknya lucu banget, pose gaya jempol",  
                "pesan":"Semangat selalu ya kak"# 6
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "kakaknya aga aga pendiem gitu",  
                "pesan":"Semangat teruss kak kuliahnyaa "# 7
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Cantik banget kakaknya, baik dan pembawaannya ramah",  
                "pesan":"Happy selalu ya kak"# 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya cuantikkk poll, terus auranya positif banget dan cheerfull",  
                "pesan":"Caemangat ya kak tetap jadi orang baik yang ceria" # 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Kakaknya menggemaskan",  
                "pesan":"Semangat teruss kak kuliahnyaa "# 10
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Cheerfull banget dan baik bangetttttt",  
                "pesan":"Jaga kesehatannya ya kak"# 11
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik banget, cantik",  
                "pesan":"Semangat terus yaa kak, sehat selaluu "# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kakaknya menggemaskan sekali dan ramah banget",  
                "pesan":"SEMANGAT KAKAK CANTII"# 13
            },
            {
                "nama": "Fairus Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "cantik sekaliii kakaknyaa",  
                "pesan":"Semangat terus kak kuliahnyaaa"# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kakaknya emejing banget",  
                "pesan":"Semangat selalu ya kak"# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Kakaknya lucu banget",  
                "pesan":"Semangatt dan sehat selalu kak "# 16
            },
            { 
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya cantik dan ramah banget",  
                "pesan":"Jaga kesehatan nya selalu ya kak"# 17
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Kakaknya lucu banget kocak gitu",  
                "pesan":"SEMANGATTT KAKkkkkk"# 18
            },
          
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "INI KAKAKKU NIHHHHHHHH, kakakku yang paling baik paling sabar, paling selalu ada buat aku, aaaaa baik bangettttt BIG LOVE buat kak Rahma yang cantik",  
                "pesan":"Semangat terus ya, jangan terlalu sibuk ih, kakak selalu keliatan cape banget, terus jangan galau galau ihhhh, bosen denger curhatan kakak tentang cowo itu mehhehe. Dilancarkan semuanya ya kak, urusan kakak, impian kakak dan harapan kakak"# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "ngerepotin Tanty",
                "sosmed": "@gustriana.d",
                "kesan": "Kakaknya keliatan kalem dan pendiem gitu",  
                "pesan":"Semangat terus ya kak kuliahnya"# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakaknya kalem banget",  
                "pesan":"Semangat ya kak"# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakaknya keren banget sihhhhh ozt oztt",  
                "pesan":"Semangat terus ya kak"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        mikfes()
        
elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
             "https://drive.google.com/uc?export=view&id=1SUx-9KysDrpH1wOk9DvJ4u_8W0aj3zVR",
             "https://drive.google.com/uc?export=view&id=1wUgNvEXYwu5KSQJ-E_yR9aFYxvu2956k",
             "https://drive.google.com/uc?export=view&id=1BuFlM0G0VvM4qgbfNBQWT89S0qnsPNyf",
             "https://drive.google.com/uc?export=view&id=1BCYLca5Q1pvchvamh8qeK3SCoiztSJdd",
             "https://drive.google.com/uc?export=view&id=19vyJnmAxX-Cen8wPacfSeu7hleqjt9yJ",
             "https://drive.google.com/uc?export=view&id=1M5-YbhtaNp5JCqLIMzCQxm4skNsFGJY5",
             "https://drive.google.com/uc?export=view&id=19j7hnINYzYQ15ID4qZoSEl4dx8CmjUCp",
             "https://drive.google.com/uc?export=view&id=1LHqYOXPWEDcYsuADh-EdorO1pFtoErod",
             "https://drive.google.com/uc?export=view&id=1r_pfSOy5ggMcOWOmRCQ2eLUWpZ1oUttI",
             "https://drive.google.com/uc?export=view&id=1GxyG2u1u6TrepWWCoIlS563mI2s3FbFh",
             "https://drive.google.com/uc?export=view&id=1mtSqn_TW4LaQLVcmqnRf4mcTKSGR7qgg",#10
             "https://drive.google.com/uc?export=view&id=1PiV46wBy4OPnabgpnotNQxQIZAC_j-Jc",
             "https://drive.google.com/uc?export=view&id=1WAhurKLQQMaYASVa0GbXjtiSG14pMkrX",
             "https://drive.google.com/uc?export=view&id=16a22Yq8GYhGkpIuyIQxjq9CcAbHHbN4k",
             "https://drive.google.com/uc?export=view&id=1rKLpZ0suYw-bNivl7l_MKCq6AWU5IqqJ",
             "https://drive.google.com/uc?export=view&id=1ZizUagw2_j102eIyrm2NS8JUGqrHmNzx",
             "https://drive.google.com/uc?export=view&id=1Y9thDB6s0FsxSdXuOJH1bdlYq31e7zH2",
             "https://drive.google.com/uc?export=view&id=1Z9JSMPgdD6JiCHiikxNpTXx5lLYRbf6v",
             "https://drive.google.com/uc?export=view&id=1w1PR0QS-mmnTFowvOmFJsWGArKaJ0J-9",
             "https://drive.google.com/uc?export=view&id=1KOLNshMhH1lMLWB94n_fP-Svfax8d1l1",
             "https://drive.google.com/uc?export=view&id=1uUIFXTPWcKPE6uZRcpOn2xYQsDcf89n3",
             "https://drive.google.com/uc?export=view&id=1lP9AW-Bv3_WooJN9SkoCFf8LF1YtVhjB",
             "https://drive.google.com/uc?export=view&id=1a6cl7WOOrB2W2nKVPwV5W8wH0cmRCyRC",
             "https://drive.google.com/uc?export=view&id=18Sm-rMFqlmqSYs7p-MJXH4pZ5kPcOb3Q",

        ] 
        data_list = [
           {
                "nama": "Arafi Putra Maulan",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Kakaknya ganteng",  
                "pesan":"Tetap semangat ya kak, dilancarkan semua urusannya"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya cantiiiii",  
                "pesan":"Tetap semangat kaka cantiiii"# 2
            },
             {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya caantik banget demi apapun ditambah pinter jadi plus plus deh pokonya",  
                "pesan":"Tetap semangat ya kakak kerennnn"# 18
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya tegas banget, jadi keliatan kaya galak gitu",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 21
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kakaknya baik banget, ditengah kesibukannya mau meluangkan waktu buat foto sama aku",  
                "pesan":"Terima kasih ya kak, tetap jadi orang baik"# 20
            },
             {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakaknya lucu banget, imuppppp",  
                "pesan":"Semangat terus ya kakak maniezz"# 19
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakaknya cantiiii sekali, adem banget liat kakaknya",  
                "pesan":"Tetap semangat dan sehat selalu kaka cantiii "# 23
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya cantiiiii bangettttt",  
                "pesan":"Jaga kesehatannya ya kakak cantiiii"# 24
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Kakaknya keren tapi aga menakutkan sedikit",  
                "pesan":"Tetap semangat dan jaga kesehatannya ya kak "# 22
            },
            
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya ramah bangetttttt dan baik banget juga",  
                "pesan":"Jangan bosen jadi orang baik ya kak"# 3
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya cantiiii pake bangetttt",  
                "pesan":"Tetap semangat dan sehat selalu kaka cantiiii "# 6
            },
             {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Orangnya bercanda mulukkkk, lucu sihhh, udah kenal dari gereja dan kakaknya yang duluan nyapa aku pas aku masih semester 1, walaupun aga galak dikit tapi baik",  
                "pesan":"Semangat terus kak"# 7
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "Sumpah kak banyak banyak terima kasih aku sama kakak, kakak selalu bantu aku dan kelompok, mentor yang super duper baik banget, dabestttttt",  
                "pesan":"Besar di sorga ya kak upahnya,  tetap andalkan Tuhan Yesus selalu. Jesus always Bless kak Sonya"# 4
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakaknya baik banget demi apapunnnn",  
                "pesan":"Tetap semangat dan selalu jadi orang baik"# 5
            },
          
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "LUCUUU, BAIKKKKK, IMUPPPP",  
                "pesan":" Tetap semangat dan sehat selalu kak"# 8
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kakaknya kaya pendiem, cool cool gitu, awalnya ngira kaya ihh kakaknya serem banget, takut banget, tapi ternyata seru dan baik bangetttt",  
                "pesan":"Semangat ya kak menghadapi pengmas yang orangnya anomali semua hahaa"# 9
            },
             {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakaknya lucu banget, first time liat kakaknya mirip pororo dan kakaknya asik banget lucu, adasih awalnya takut takutnya, tapi karna kakaknya sik jadi enjoy deh",  
                "pesan":"Tetap semangat mengguncang pengmass dan Itera ya kak xixiiii"# 16
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "Kakaknya lucu banget, kaya pembawaannya adem gitu, dan sumpah baik banget, gatau kenapa nyaman gitu deket ama kakaknyaaa",  
                "pesan":"Tetap semangat ya kakkk, tetap jadi kakak pengmas yang lucu imut dan menggemaskan"# 10
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Awalnya kukira ihh kakak ini judes banget, jutek, takut banget ama kakaknya. Tapi ternyata lucuu, baik banget lagi, terus kakaknya selalu excited banget nyapa aku kalo pas pasan di gedung F, kaya ihhh kakaknya seneng ketemu aku",  
                "pesan":"Tetap semangat dan sehat selalu kak dan tetap cheerfull "# 11
            },
             {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya cantik bangetttttt, dan ternyata miss Lampung, keren banget, mauu juga kaya kakaknyaaa, diem diem aku sering liatin kakak, karna pembawaan kakak yang anggun dan cantik bikin acuu terpesona lop u kak ",  
                "pesan":"Tetap semangat ya kak, tetap pancarkan enerrgi kakak yang emejing itu"# 14
            },
            
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Awalnya aku juga ngira kakaknya pendiam, tapi ya namanya juga pegmas gaadda yang pendiam disana hahaha. Tapi kakaknya baik dan asik banget sihhhhh pas di pasar malam jadi enjoy banget karna kakaknya welcome banget",  
                "pesan":"Kakaknya cemangat terusss yaaaa, walaupun dunia ini selalu ada aja gebrakannya"# 15
            }, 
             {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakaknya pembaannya adem gitu, kaya lemah lembut dan muslimah banget, pastinya baik sangattttt sukak ama kak Tari auranya tuh mba mba positive vibes banget",  
                "pesan":"Tetap pancarkan aura kakak yang uwaw spektakuler membahana itu ya kak Tari"# 17
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak Izza gatau kenapa pembawaannya kaya keibuan banget gitu, kaya mengayomi banget, kalem, berkharisma, jadi kangum ama pembawaannya kak Izza",  
                "pesan":"Semangat terus ya kak, tetap jadi orang baik yang penuh kehangatan"# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakakmya diem diem misterius gitu awalnya. Tapi setelah terjun ke pengmas ternyata gaada yang pendiem disana hahhaa, semuanya kocak kocak tapi seru abiezzz",  
                "pesan":"Semangat ya kak walupun tertekan tetap katakan SEMANGATTT"# 13
            },
          
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()   
elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1yM1KDSQ6Fr0HDi8cx2LanstNuduqg0h0",
           "https://drive.google.com/uc?export=view&id=12ln77QpAFtF-sJPlHsigpcbudpcw1cZv",
           "https://drive.google.com/uc?export=view&id=1oVT6DaFSTgnCX_zPD_rfp3y_G-tCJHn-",
           "https://drive.google.com/uc?export=view&id=13ewsPxrBtXGXsZMCunmeMU1LvB1HWZPi",
           "https://drive.google.com/uc?export=view&id=1pgFDUm2oRM6jfzG-4H79al-lWRuKLcDU",
           "https://drive.google.com/uc?export=view&id=1kfQRYUxE9j1RcqVBElnDvBCqLModfbAY",
           "https://drive.google.com/uc?export=view&id=1MhVEjom1d3BC9YzHoU5vIRQCnl7en4gI",
           "https://drive.google.com/uc?export=view&id=1w8Eelzo9b6c2vO4qgKR0RUxlgC2UVdCE",
           "https://drive.google.com/uc?export=view&id=1sGZ9E_W5dG1bXIS3dbXKEg5y18ZZl2qq", 
           "https://drive.google.com/uc?export=view&id=1l8ZfRaV7mkyjh8yzaYw8XwhIebPhaEis",
           "https://drive.google.com/uc?export=view&id=19_ntFq6HSoktMvPXvaF3zx1j2U1I_cHl",
           "https://drive.google.com/uc?export=view&id=1XCARcsbMEu7LpYQbf7SLqRbg3fX0sC9J",
           "https://drive.google.com/uc?export=view&id=1ccydgPGSmxwIutCEU1Hn3-Qm5mJOo00h", 
           "https://drive.google.com/uc?export=view&id=1xbiACmmK_xDcwt1m6UXWKhaJDJUGR9sg",
           "https://drive.google.com/uc?export=view&id=1XrgWf9EaoDWt4WEPV_K_K7zZRv9_AAMb",
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
                "kesan": "Kakaknya auranya kaya wanita kuat dan tangguh, keren banget",  
                "pesan":"Semangat ya kak kuliahnya"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Awalnya kukira kakak cowo karna rambutnya pendek hehe",  
                "pesan":"Semangat terus ya kak kuliahnya"# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya lucu dan imupp sekaliiii",  
                "pesan":"Sengat terus ya kak"# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Kakaknya positive vibes sekaliiii, seneng deh liat kakanya, pembawaannya adem gitu",  
                "pesan":"Semangat ya kak kuliahnya"# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakaknya baik banget, kerennnn",  
                "pesan":"Semangat terus ya kak"# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya lucuuu, imupppp",  
                "pesan":"Semangat ya kak kuliahnya"# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakaknya tegas bangettt",  
                "pesan":"Semangat terus ya kakak"# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Kakaknya lucuuu tapi sedikit pendiam",  
                "pesan":"Semangat terus kak"# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "Kakaknya baik, keren",  
                "pesan":"Sehat selalu kak"# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Kakaknya lucuuuu, baik",  
                "pesan":"Semangat terus kak"# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya lucu bangett, suaranya juga bagus, keren banget ihh pokoknya",  
                "pesan":"Tetap andalkan Tuhan Yesus ya kaka"# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Kakaknya canti sekaliiiiii, lucu, imup dan super duper baiik",  
                "pesan":"Tetap andalkan Tuhan Yesus ya kaka"# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Terlihat pendiam",  
                "pesan":"Semangat terus kak"# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Kakaknya keren bangetttt, cantiii, selalu kagum ama kak Sarah karena main musiknya keren banget",  
                "pesan":"Tetap andalkan Yesus ya kak"# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Cantii, baik dan imup",  
                "pesan":"Semangat kuliahnya kak"# 15
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e9fQEjEYFLUWL8I0LfxNbZAATHmYbqu5",
            "https://drive.google.com/uc?export=view&id=193IWCujfiWGr6m6WKCdt7HFGxKT8aasZ",
            "https://drive.google.com/uc?export=view&id=1sSUDImgo3hedDSOUMnm_U654gMJD-4F1",
            "https://drive.google.com/uc?export=view&id=1sAM9ToSWJTKuZ74_75CDyqHT2uhHCmTi",
            "https://drive.google.com/uc?export=view&id=1JildNj6bOxp59XrEJRAIqTvEWELiR-6n",
            "https://drive.google.com/uc?export=view&id=15W2vT-H2-fHRMJl51X5xq6kk120r6q5C",
            "https://drive.google.com/uc?export=view&id=1hlC9rm-nIW2tUOFbmLsF-1RQZm8Fvw9V",
            "https://drive.google.com/uc?export=view&id=1kCmowRnNbpXskwVROUbEcpUt9eEoNdfs",
            "https://drive.google.com/uc?export=view&id=1vTHLmw6k7cx1s6AzleAe2_grvPrQJSPW", #
            "https://drive.google.com/uc?export=view&id=1LbOwrhIXaTl9nC9JpLJ1KfVef_8_TpRb",
            "https://drive.google.com/uc?export=view&id=1Bk1vYpJt8ZcapRPPhoabiLooam-nepv1",
            
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
                "kesan": "Kakaknya keren banget siiii, dan lucuuu",  
                "pesan": "Semoga dilancarkan semuanya dan dipermudah urusannya"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakaknya cantiii, dan baik bangett, ramah",  
                "pesan": "Sehat selalu kak, dilancakan semuanya "# 1
            },
              {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "Kakaknya keren dan asik dan juga ganteng xixi ",  
                "pesan": "Semangat ya kak"# 1
            },
              {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya baik, luar biasa keren",  
                "pesan": "Semoga urusannya diperlancar "# 1
                   },
              {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "Kakaknya baiik, keren",  
                "pesan": "Semangat selalu kak"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Semangat semangat kak"# 1
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakaknya baik dan keren",  
                "pesan": "Semangat selalu ya kak"# 1
            },
              {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya keren banget, cantiii dan immupp",  
                "pesan": "Semoga dilancarkan semuanya kak "# 1
            },
              {
                "nama": "Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "Kakaknya baik banget",  
                "pesan": "Always semangat ya kak"# 1
            },
              {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya cantiii dan keren",  
                "pesan": "Semangat kakakkk"# 1
            },
              {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakaknya keren bangettt",  
                "pesan": "Semangat terus ya kak"# 1
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1xJkBVcrpWXrbMYgjiHDtf2gdkYhm_VC3",
           "https://drive.google.com/uc?export=view&id=1b3fUmJ1vuoo8LyU1G3ePtJG20LjpikJF",
           "https://drive.google.com/uc?export=view&id=172K5aEeSGr2lyCek7dMO4p-rhKB2OcDs",
           "https://drive.google.com/uc?export=view&id=1c5ivT2CNAWNDSz_dRzMk2146zl22MSCD",
           "https://drive.google.com/uc?export=view&id=1-lkeD1KUuL50lZqpIq9FjPfE2XpSAbbC",
           "https://drive.google.com/uc?export=view&id=1aha6cGB234KUId53dZGq3T0C5R3aDJ3c",
           "https://drive.google.com/uc?export=view&id=1TTut3U4rNeoj2s5-q-b6awhr5tQTVJwl",
           "https://drive.google.com/uc?export=view&id=15FPsm2g9wQHBt3gm9Jm6sPOrRsnQeCeh",
           "https://drive.google.com/uc?export=view&id=16vT_kXGfTNFRgk6RHuuMqNKWouYtYdn3", 
           "https://drive.google.com/uc?export=view&id=19WFuDjmAp8-njgk9Ae5laVsICTwotN2Y",
           "https://drive.google.com/uc?export=view&id=1z3jnt8ZOaht9YKl1IFhGQgUMUGrVG3AY",
           "https://drive.google.com/uc?export=view&id=1CgfzyEJDIBdhny_lmg3qvKSTiGsVaTmR",
           "https://drive.google.com/uc?export=view&id=16NjHu4HinxmBRiRxVL8KKCFV8vmivArv", 
           "https://drive.google.com/uc?export=view&id=1xqNEl5J8WqtUTPkTBRFIPFT1RAESIodJ",
           "https://drive.google.com/uc?export=view&id=1Jld2t41tKIAuEkLKjJoC_tT7_yKUl_-t",
           "https://drive.google.com/uc?export=view&id=1K52FXYFS50q9kmowEDC6PZFpfvTrYWdJ",
           "https://drive.google.com/uc?export=view&id=170v_W-Rv_aaUREK3HtkALUrrkuUk3Do-",
           "https://drive.google.com/uc?export=view&id=1xzv6gsz9pqj9Zy5xE4apKEZASrOLZvsw", 
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
                "kesan": "Kakaknya cantiii banget, sukak ama lesung pipinya jadi makin maniezz dan pembawaannya positive vibes banget",  
                "pesan": "Tetap andalkan Yesus ya kak Ciaaa"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakaknya cantii banget dan baik",  
                "pesan": "Tetap semangat kakak cantiiii"# 1
            },
              {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Kakaknya terlihat pendiam",  
                "pesan": "Semangat terus ya kak"# 1
              },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Kakaknya keren dan baik banget",  
                "pesan": "Tetap semangat ya kak"# 1
            },
              {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Kerennnn deh pokoknya",  
                "pesan": "Tetap semangat yaa kak"# 1
            },
              {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "Cantikkk banget kakkkk dan baikkk banget",  
                "pesan": "Semangat terus kakak cantiii"# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Kakaknya cantiiii bangettt",  
                "pesan": "Semangat kakak cantiiiii"# 1
            },
              {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Cantikk sekaliii kak, kalem lembut gituuuu",  
                "pesan": "Cemangat terus ya kak"# 1
            },
              {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya keren banget dan baik banget",  
                "pesan": "Semangat terus ya kak Donna"# 1
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Cantikkk dan baik banget",  
                "pesan": "Semangat selalu ya kak"# 1
            },
              {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Cantik sekalii kak, imupp banget jugaa",  
                "pesan": "Dilancarkan semuanya ya kak"# 1
            },
              {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "Kak kok bisa canti banget cihhhh",  
                "pesan": "Semangat selalu ya kak cantii"# 1
            },
              {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Cantikk dsn imup",  
                "pesan": "Semangat kuliahnya kak"# 1
            },
              {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Terlihat pendiam",  
                "pesan": "Semangat terus kak"# 1
            },
              {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Cantik sekalii kaaa",  
                "pesan": "Semangat terus ya kak"# 1
            },
              {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Cantii, lucu dan imup",  
                "pesan": "Seamngat kakaaa"# 1
            },
              {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "lucuuu, pinkyyyy bangettt, tutor jadi canti kaya kakak dong",  
                "pesan": "Selalu ceria ya kakkk"# 1
            },
              {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya lucu bangettttt, kaya kok bisaaa siiii selucu dan semenggemaskan itu",  
                "pesan": "Tetap semangat kakak imup"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

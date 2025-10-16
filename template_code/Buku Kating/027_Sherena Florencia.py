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
                "nama": "Kakak Rendra Eka Prayoga",
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
                "nama": "Kakak Johannes Krisjon Silitonga",
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
                "nama": "Kakak Elisabeth Claudia Simanjuntak",
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
                "nama": "Kakak Syadza Puspadari Azhar",
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
                "nama": "Kakak Eksanty Febriana Sukma Islamiaty",
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
                "nama": "Kakak Farahanum Afifah Ardiansyah",
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
                "nama": "Kakak Jeremia Susanto",
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
                "nama": "Kakak Dhea Amelia Putri",
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
                "nama": "Kakak Renisha Putri Giani",
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
                "nama": "Kakak Anisa Fitriyani",
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
                "nama": "Kakak Dharu Cahyoaji Sasongko",
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
                "nama": "Kakak Feby Wulandari",
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
                "nama": "Kakak Givaro Ananta",
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
                "nama": "Kakak Mirzan Yusuf Rabbani",
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
                "nama": "Kakak Berliana Enda Putri",
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
                "nama": "Kakak Juesi Apridelia Saragih",
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
                "nama": "Kakak Ridho Benedictus Togi Manik",
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
                "nama": "Kakak Feryadi Yulius",
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
                "nama": "Kakak Monica Patricia Tanjung",
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
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
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
                "nama": "Kakak Rian Bintang Wijaya",
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
                "nama": "Kakak Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya cantik",  
                "pesan": "Semangat selalu kakak"# 1
            },
            {
                "nama": "Kakak Fathinah Nur Azizah",
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
                "nama": "Kakak Lia Hana Ichisasmita",
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
            "https://drive.google.com/uc?export=view&id=1x0YxcB_owX9qLBUnGFq0I76W2wNMF8vc",
            "https://drive.google.com/uc?export=view&id=17HAOzsgvtWOFIZGpxdmuIEyvpIYfL_4-",
            "https://drive.google.com/uc?export=view&id=1_XLXl9AHm_LrTo-bVdp4SzFQ2E6dPEFP",
            "https://drive.google.com/uc?export=view&id1ZefdkGdVNG413wvVLqSp8-b_juVOSOxq",

        ]
        data_list = [
            {
                "nama": "Kakak Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": " ",
                "sosmed": "@ahmad.rizky___",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":" ",
                "alamat": " ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Vany Salsabila Putri", #ke bawah belum ku isi
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":" ",
                "alamat": " ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":" ",
                "alamat": " ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":" ",
                "alamat": " ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": " ",  
                "pesan":" "# 1
            },
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
                "nama": "Kakak Randra Andriana Putra", #Datanya belum ku isi
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kak Randa asik, wawasannya luas",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
            {
                "nama": "Kakak Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak Rut asyik dan keren",  
                "pesan":"Lancar-lancar kuliahnya kak Rut"# 2
            },
            {
                "nama": "Kakak Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak Regi kadiv PSD keren",  
                "pesan":"Semangat Kak Regi, terus menginspirasi"# 3
            },
            {
                "nama": "Kakak Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak Aisyah keren cara berbicaranya",  
                "pesan":"semangat menjalani semester 5 kakak"# 4
            },
            {
                "nama": "Kakak Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak Fadil keren banget jadi duta genre",  
                "pesan":"Semoga selalu kece ya kak fadil"# 5
            },
            {
                "nama": "Kakak Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak Aqil keren gacor",  
                "pesan":"Semoga hobinya bisa dikurangi ya kak, biar sehat hehe"# 6
            },
            {
                "nama": "Kakak Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "Kakak Naufal pendiam sekali",  
                "pesan":"Semoga sehat selalu dan bahagia"# 7
            },
            {
                "nama": "Kakak Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak Nadia Keren banget",  
                "pesan":"Selalu keren ya kak"# 8
            },
            {
                "nama": "Kakak Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak marleta murah senyum",  
                "pesan":"semangat kak semester 7 nya semoga lulus tepat waktu" # 9
            },
            {
                "nama": "Kakak Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Kakak Akeyla namanya bagus",  
                "pesan":"Sehat-sehat kak di pramuka"# 10
            },
            {
                "nama": "Kakak Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak Anggi kita sam sama dari Natar",  
                "pesan":"Semangat kak pp Natar-Iteranya"# 11
            },
            {
                "nama": "Kakak Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak Efi keren banget",  
                "pesan":"Kakak Efi semangat ya"# 12
            },
            {
                "nama": "Kakak Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kakak Fabiolla kita sama NIM akhirnya",  
                "pesan":"Semangat selalu kak fabiolla"# 13
            },
            {
                "nama": "Kakak Fairus Ary Syifa",
                "nim": "123450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 14
            },
            {
                "nama": "Kakak Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@i",
                "kesan": "",  
                "pesan":""# 15
            },
            {
                "nama": "Kakak Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Kakak Eggi hebat",  
                "pesan":"Semangat kuliahnya kakak hebat!"# 16
            },
            { 
                "nama": "Kakak Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak Afifah asyik bangett",  
                "pesan":"Semangat kak ngobrolnyaa"# 17
            },
            {
                "nama": "Kakak Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Fabio keren abis",  
                "pesan":"semangat terus kak jadi pj bu Febri"# 18
            },
          
            {
                "nama": "Kakak Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 19
            },
            {
                "nama": "Kakak Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 20
            },
            {
                "nama": "Kakak Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 21
            },
            {
                "nama": "Kakak Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Gio keren banget",  
                "pesan":"semangat Caturnya kak"# 22
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
             "https://drive.google.com/uc?export=view&id=1mtSqn_TW4LaQLVcmqnRf4mcTKSGR7qgg",
             "https://drive.google.com/uc?export=view&id=1PiV46wBy4OPnabgpnotNQxQIZAC_j-Jc",
             "https://drive.google.com/uc?export=view&id=1WAhurKLQQMaYASVa0GbXjtiSG14pMkrX",
             "https://drive.google.com/uc?export=view&id=16a22Yq8GYhGkpIuyIQxjq9CcAbHHbN4k",
             "https://drive.google.com/uc?export=view&id=1rKLpZ0suYw-bNivl7l_MKCq6AWU5IqqJ",
             "https://drive.google.com/uc?export=view&id=1ZizUagw2_j102eIyrm2NS8JUGqrHmNzx",
             "https://drive.google.com/uc?export=view&id=1Y9thDB6s0FsxSdXuOJH1bdlYq31e7zH2",
             "https://drive.google.com/uc?export=view&id=1Z9JSMPgdD6JiCHiikxNpTXx5lLYRbf6v",
             "https://drive.google.com/uc?export=view&id=1w1PR0QS-mmnTFowvOmFJsWGArKaJ0J-9",
             "https://drive.google.com/uc?export=view&id=1KOLNshMhH1lMLWB94n_fP-Svfax8d1l1",
             "https://drive.google.com/uc?export=view&id=1fYX34rW3vwT1cenS6uZTBegoEEIKJxP_",
             "https://drive.google.com/uc?export=view&id=1uUIFXTPWcKPE6uZRcpOn2xYQsDcf89n3",
             "https://drive.google.com/uc?export=view&id=1KOLNshMhH1lMLWB94n_fP-Svfax8d1l1",
             "https://drive.google.com/uc?export=view&id=1a6cl7WOOrB2W2nKVPwV5W8wH0cmRCyRC",
             "https://drive.google.com/uc?export=view&id=18Sm-rMFqlmqSYs7p-MJXH4pZ5kPcOb3Q",

        ] 
        data_list = [
            {
                "nama": "Kakak Randra Andriana Putra", #Datanya belum ku isi
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kak Randa asik, wawasannya luas",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
            {
                "nama": "Kakak Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak Rut asyik dan keren",  
                "pesan":"Lancar-lancar kuliahnya kak Rut"# 2
            },
            {
                "nama": "Kakak Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak Regi kadiv PSD keren",  
                "pesan":"Semangat Kak Regi, terus menginspirasi"# 3
            },
            {
                "nama": "Kakak Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak Aisyah keren cara berbicaranya",  
                "pesan":"semangat menjalani semester 5 kakak"# 4
            },
            {
                "nama": "Kakak Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak Fadil keren banget jadi duta genre",  
                "pesan":"Semoga selalu kece ya kak fadil"# 5
            },
            {
                "nama": "Kakak Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak Aqil keren gacor",  
                "pesan":"Semoga hobinya bisa dikurangi ya kak, biar sehat hehe"# 6
            },
            {
                "nama": "Kakak Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "Kakak Naufal pendiam sekali",  
                "pesan":"Semoga sehat selalu dan bahagia"# 7
            },
            {
                "nama": "Kakak Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak Nadia Keren banget",  
                "pesan":"Selalu keren ya kak"# 8
            },
            {
                "nama": "Kakak Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak marleta murah senyum",  
                "pesan":"semangat kak semester 7 nya semoga lulus tepat waktu" # 9
            },
            {
                "nama": "Kakak Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Kakak Akeyla namanya bagus",  
                "pesan":"Sehat-sehat kak di pramuka"# 10
            },
            {
                "nama": "Kakak Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak Anggi kita sam sama dari Natar",  
                "pesan":"Semangat kak pp Natar-Iteranya"# 11
            },
            {
                "nama": "Kakak Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak Efi keren banget",  
                "pesan":"Kakak Efi semangat ya"# 12
            },
            {
                "nama": "Kakak Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kakak Fabiolla kita sama NIM akhirnya",  
                "pesan":"Semangat selalu kak fabiolla"# 13
            },
            {
                "nama": "Kakak Fairus Ary Syifa",
                "nim": "123450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 14
            },
            {
                "nama": "Kakak Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@i",
                "kesan": "",  
                "pesan":""# 15
            },
            {
                "nama": "Kakak Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Kakak Eggi hebat",  
                "pesan":"Semangat kuliahnya kakak hebat!"# 16
            },
            { 
                "nama": "Kakak Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak Afifah asyik bangett",  
                "pesan":"Semangat kak ngobrolnyaa"# 17
            },
            {
                "nama": "Kakak Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Fabio keren abis",  
                "pesan":"semangat terus kak jadi pj bu Febri"# 18
            },
          
            {
                "nama": "Kakak Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 19
            },
            {
                "nama": "Kakak Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 20
            },
            {
                "nama": "Kakak Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 21
            },
            {
                "nama": "Kakak Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Gio keren banget",  
                "pesan":"semangat Caturnya kak"# 22
            },
             {
                "nama": "Kakak Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 21
            },
            {
                "nama": "Kakak Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Gio keren banget",  
                "pesan":"semangat Caturnya kak"# 22
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
                "nama": "Kakak Jeremia Susanto", #Datanya belum ku isi
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "Kakaknya manis, lucu ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya"# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
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
                "nama": "Kakak Renisha Putri Giani",
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
                "nama": "Kakak Anisa Fitriyani",
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
                "nama": "Kakak Dharu Cahyoaji Sasongko",
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
                "nama": "Kakak Feby Wulandari",
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
                "nama": "Kakak Givaro Ananta",
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
                "nama": "Kakak Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Keren kak Berlin",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": " ",  
                "pesan": " " # 1
            },
              {
                "nama": "Kakak Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " ",  
                "pesan": " "# 1
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
            "https://drive.google.com/uc?export=view&id=12CDrjNQ18SYIurDh8by2V4vUh8XOXkdY", #
            "https://drive.google.com/uc?export=view&id=1LbOwrhIXaTl9nC9JpLJ1KfVef_8_TpRb-",
            "https://drive.google.com/uc?export=view&id=1Bk1vYpJt8ZcapRPPhoabiLooam-nepv1",
            
        ]
        data_list = [
            {
                "nama": "Kakak Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": "Kakaknya manis, lucu ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya"# 1
            },
            {
                "nama": "Kakak Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakak nya baik, seru ",  
                "pesan": "Sehat selalu kak, dilancakan semuanya "# 1
            },
              {
                "nama": "Kakak Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "Kakaknya keren dan asik ",  
                "pesan": "Semoga dilancarkan urusannya kak "# 1
            },
              {
                "nama": "Kakak Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya keren ",  
                "pesan": "Semoga urusannya diperlancar "# 1
                   },
              {
                "nama": "Kakak Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": ".",
                "asal": ".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": ".",
                "kesan": "Kakaknya keren banget ",  
                "pesan":"Semoga diperlancar semuanya  "# 1
            },
             {
                "nama": "Kakak Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakaknya cantik dan lucu ",  
                "pesan": "Semangat kak, diperlancar semuanya "# 1
            },
              {
                "nama": "Kakak Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya keren banget ",  
                "pesan": "Semoga dilancarkan semuanya kak "# 1
            },
              {
                "nama": "Kakak Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": " ",  
                "pesan": " "# 1
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
                "nama": "Kakak Jeremia Susanto", #Datanya belum ku isi
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "Kakaknya manis, lucu ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya"# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
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
                "nama": "Kakak Renisha Putri Giani",
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
                "nama": "Kakak Anisa Fitriyani",
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
                "nama": "Kakak Dharu Cahyoaji Sasongko",
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
                "nama": "Kakak Feby Wulandari",
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
                "nama": "Kakak Givaro Ananta",
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
                "nama": "Kakak Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Keren kak Berlin",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": " ",  
                "pesan": " " # 1
            },
              {
                "nama": "Kakak Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " ",  
                "pesan": " "# 1
            },
             {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

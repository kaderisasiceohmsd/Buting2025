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
           "https://drive.google.com/uc?export=view&id=1tRbJqTbwJ63BBNEm_xQjkStBO6Gy6DNL",
            "https://drive.google.com/uc?export=view&id=1XlRVA93TFwksctaoUDgYdWjJIxCdHJ0E",
            "https://drive.google.com/uc?export=view&id=1x2TwvZZWUtBlZ0Xp7F-elJ3ARsnkOkMe",
            "https://drive.google.com/uc?export=view&id=1ld3Pdphp-lovV8nQCs2bEvX4kDIMJYyw",
            "https://drive.google.com/uc?export=view&id=16_MnMxNzuMbZYKezwoq1-rE3_3Xgh_vM",
            "https://drive.google.com/uc?export=view&id=1dSMoJzAF8P-eFu-rwpf5PK4hV3W22ceT",
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
                "kesan": "Bang asik banget",  
                "pesan": "Semangat bang kuliahnya!!"# 1
            },
            {
                "nama": "Kakak Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren banget bang, dari pembawaanya keliatan banget orang keren nya",  
                "pesan": "Semangat bang kuliahnya!"# 1
            },
              {
                "nama": "Kakak Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kak, asik sekalii",  
                "pesan": "semangat terus kuliahnya kak!"# 1
            },
              {
                "nama": "Kakak Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya kalem banget, aku kenal orang yang mirip banget sama kak syadza, kuliah di Itera juga tapi udah lulus",  
                "pesan": "semangat terus kuliahnya kakak !"# 1
            },
            {
                "nama": "Kakak Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Satu kata : Amazing",  
                "pesan":"semangat terus kuliahnya kakak !"# 1
            },
             {
                "nama": "Kakak Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak nya asik sekali membawa vibes positive banget",  
                "pesan": "semangat terus kuliahnya kakak !"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tRq5nrYzLKXRCiCM6IMkC5Y8T7gUA_mU",
            "https://drive.google.com/uc?export=view&id=1DWSqcDqnnK7am3GBminrTwwmLsE837jc",
            "https://drive.google.com/uc?export=view&id=1HcC_aE891dbGGzj_u_uamBh4NB4xQ-CG",
            "https://drive.google.com/uc?export=view&id=1GNPUYZ7vhR9t9C6CPebBKp7s3KUyha4V",
            "https://drive.google.com/uc?export=view&id=19jiFy9uTyug47-MiCXYt2R2bluKbe_Do",
            "https://drive.google.com/uc?export=view&id=1rn1hAMEQkFK3qFmZGfKpWpD0fsaYPFZj",
            "https://drive.google.com/uc?export=view&id=1llNe_8Mo0CIzdR9texEojRAWxIzFZlRv",
            "https://drive.google.com/uc?export=view&id=1BUZHb_JxWJenu1n-UVSaEI6U9ssdAwVb",
            "https://drive.google.com/uc?export=view&id=1G0ha-d-k4yrcYxW1ERBfUXZ5AzuK3jWS",
            "https://drive.google.com/uc?export=view&id=1AO-nuHxCq9Yc2J0q3F38pVpb41S1kZWz",
            "https://drive.google.com/uc?export=view&id=1VMtXKWCUxUqQW5mbfAJ0r-D1qhjOhqdO",
            "https://drive.google.com/uc?export=view&id=1u9TbhhjoG8S90hxsrcr5Q3tNEoiDL-YL",
            "https://drive.google.com/uc?export=view&id=1DI_3QidNr-jlQzNuDV77RRKhGI3QP7QF",
            "https://drive.google.com/uc?export=view&id=16Ml6dFeXL8VH9mNmybIfkStTjPjoBvDq",
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
                "kesan": "Asik banget bang",  
                "pesan": "Semangat terus bang walaupun hidup gonjang ganjing"# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "baik sekalii",  
                "pesan": "tetap semangat! "# 1
            },
              {
                "nama": "Kakak Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "cantik sekali ",  
                "pesan": "sehat selalu ya kak"# 1
            },
              {
                "nama": "Kakak Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "cantiiiik ",  
                "pesan": "selalu semangat pokoknyaa "# 1
            },
            {
                "nama": "Kakak Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "pintar, of course ",  
                "pesan":"lancar ya bang kuliahnya "# 1
            },
             {
                "nama": "Kakak Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Imutt cantik lagi ",  
                "pesan": "Semangat kak kuliahnyaa "# 1
            },
              {
                "nama": "Kakak Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Berwibawa sekali ",  
                "pesan": "semangat ya bang "# 1
            },
              {
                "nama": "Kakak Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "kalem sekali bang ",  
                "pesan": "Semangatt ya bang kuliahnya "# 1
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": " cantik sekali kak",  
                "pesan": "Tetap semangat kuliahnya ya kak "# 1
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": " Sangat cheerfull",  
                "pesan": "Semangat kuliahnya kak "# 1
            },
              {
                "nama": "Kakak Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "keren banget bang ",  
                "pesan": " semangat bang kuliahnya"# 1
            },
              {
                "nama": "Kakak Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": " kerennnn",  
                "pesan": "sehat selalu bangg"# 1
            },
              {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "Cantik sekalii kak",  
                "pesan": " Semangat terus ya kak kuliahnya"# 1
            },
              {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " Cantik banget kak",  
                "pesan": " Semangat ya kak kuliahnya"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1exuxWC_8LvnhAi5WAO76USZQOw8QZfgc",
            "https://drive.google.com/uc?export=view&id=1x9CsemxKxusQpKg6Ql-ZijjrVp4IOmua",
             "https://drive.google.com/uc?export=view&id=18gpqxnjeV58e68UFyN2jP4XDoR4ywvNF",
             "https://drive.google.com/uc?export=view&id=1af4c9uylYuC3GQSSZfeisFYtJl2Mj2Q_",
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
                "kesan": "Selalu berusaha membuat lingkungan sekitar jadi asik",  
                "pesan": "Lancar ya bang kuliahnya, dan sehat selalu"# 1
            },
            {
                "nama": "Kakak Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "sangat girly",  
                "pesan": "semangat kuliahnya kak!"# 1
            },
              {
                "nama": "Kakak Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "MasyaAllah",  
                "pesan": "Semangat terus kak!"# 1
            },
              {
                "nama": "Kakak Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "manly, aku suka karena aku tidak jauh beda",  
                "pesan": "Semangat terus kuliahnya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DH8nPs0MD-x1jRlFk2036oi8hRkUdqE7", #1
            "https://drive.google.com/uc?export=view&id=1fkmsS7a69WuQxeFLb_d1x_rZOzwbC0a6", #2
            "https://drive.google.com/uc?export=view&id=1c1vfwCoa9wq730WBJ5CfKQpVYku2Rosl", #3
            "https://drive.google.com/uc?export=view&id=1jeTyVMwSYbgDkUmD9UCp-6gKrTj1PSkV", #4
            "https://drive.google.com/uc?export=view&id=121W1MXFchI-tcPCcqtHY96Mt8l6PRFuG", #5
            "https://drive.google.com/uc?export=view&id=1CjD5gLEjvOoJFjV__SHiXytjatYOSH7d", #6
            "https://drive.google.com/uc?export=view&id=1Jl2AUCP_31pfEvrNifY4-2zhASlT-ah6", #7
            "https://drive.google.com/uc?export=view&id=1x3WxdD1GXmFvgn5oWb4qSztF3vM3FaK8", #8
            "https://drive.google.com/uc?export=view&id=1PgdFHlQjZCfR_9X_MbDeaIDTiJpuJqGM", #9
            "https://drive.google.com/uc?export=view&id=1_aBzLcIoViSHORkqNiGr6IrPm8WOd_ID", #10
            "https://drive.google.com/uc?export=view&id=1uYUoa7x1DSiuF11Y7GgI0K9s1-QSthYt", #11
            "https://drive.google.com/uc?export=view&id=1U6870EDV_yYYjMEYLzEKWp7tVJz8QlrI", #12
            "https://drive.google.com/uc?export=view&id=1IfNGaMcFGPdCAwbG1IXi_Tnbr_SgM7ei", #13
            "https://drive.google.com/uc?export=view&id=1UNA-xb6A1NqezBbjQec78cs_KpzvvuTv", #14
            "https://drive.google.com/uc?export=view&id=1i04VC2BHQJFsfAg2O1jzmAsW0VEUSRNr", #15
            "https://drive.google.com/uc?export=view&id=1fxWj-ZT6WWhGBgYQWsThEIYPVkaTUa1g", #16
            "https://drive.google.com/uc?export=view&id=18RvX1qTgxI3FuejEYVeg6Q4_VSGHEFVU", #17
            "https://drive.google.com/uc?export=view&id=1ddVEzUNLYmullEsjrpDGUS0QarbxBEiQ", #18
            "https://drive.google.com/uc?export=view&id=1xvX7ktK0sMdXCVdXZwHl-E20JY-R5Ruu", #19
            "https://drive.google.com/uc?export=view&id=1uNn4ZoR4RaMR4xi-13CjZnlC325yCwhY", #20
            "https://drive.google.com/uc?export=view&id=1wfv_FNKT0MGCotl7xSSh71nWvar7Nmwj", #21
            "https://drive.google.com/uc?export=view&id=1h4WkI7q6I0nIzAKQpXSEluhQGkpXRq01", #22
            "https://drive.google.com/uc?export=view&id=1uh24_PArlwOvQIhVZ59f018HWIGvjdIZ", #23
            "https://drive.google.com/uc?export=view&id=1PeEYrYrFQh1a2dJtG0Jn0wNR0BEIEr88", #24
            "https://drive.google.com/uc?export=view&id=1zAzY3YqjJ8YcOe785fpaba3fDSbNWNM-", #25
            "https://drive.google.com/uc?export=view&id=1QeY9ZzIWiMm7R6OgzeNY9xAo-YJvbD7y", #26
            
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
                "kesan": "keren bangettt",  
                "pesan":"Tetap semangat dan sehat selalu bang"# 1
            },
            {
                "nama": "Kakak Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "Cantikkk sekalii",  
                "pesan":"Tetap semangat dan sehat selalu kakk"# 2
            },
            {
                "nama": "Kakak Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "Balance antara asik dan tegas",  
                "pesan":"Tetap semangat dan sehat selalu kak"# 3
            },
            {
                "nama": "Kakak Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "sangat amat memperhatikan setiap adik adiknya",  
                "pesan":"Tetap semangat dan sehat selalu bang"# 4
            },
            {
                "nama": "Kakak Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "sangat kerenn",  
                "pesan":"Tetap semangat dan sehat selalu kak"# 5
            },
            {
                "nama": "Kakak Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "lucuuu dan baik",  
                "pesan":"Tetap semangat dan sehat selalu bang"# 6
            },
            {
                "nama": "Kakak Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "tegas tapi tidak to much",  
                "pesan":"Tetap semangat dan sehat selalu bang"# 7
            },
            {
                "nama": "Kakak Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "Cantikkk sekalii",  
                "pesan":"Tetap semangat dan sehat selalu kak"# 8
            },
            {
                "nama": "Kakak Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "gacorr abiss",  
                "pesan":"Tetap semangat dan sehat selalu bang"# 9
            },
            {
                "nama": "Kakak Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "terlalu keren untuk menjadi manusia",  
                "pesan":"Tetap semangat dan sehat selalu bang"# 10
            },
            {
                "nama": "Kakak Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "baik sekali dan lucuuu",  
                "pesan":"Tetap semangat dan sehat selalu kak"# 11
            },
            {
                "nama": "Kakak Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "kok asik ya ngobrol sama bang sahid",
                "pesan": "Tetap semangat dan sehat selalu bang" # 12
            },
            
            {
                "nama": "Kakak Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "lucuuu",
                "pesan": "Tetap semangat dan sehat selalu bang" # 13
            },
            
            {
                "nama": "Kakak Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Cantikk sekalii",
                "pesan": "Tetap semangat dan sehat selalu kak" # 14
            },
            
            {
                "nama": "Kakak Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Cantikkk sekalii",
                "pesan": "Tetap semangat dan sehat selalu kak" # 15
            },
            
            {
                "nama": "Kakak Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Cantikk sekalii",
                "pesan": "Tetap semangat dan sehat selalu kak" # 16
            },
            
            {
                "nama": "Kakak Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "kerennn abisss",
                "pesan": "Semoga makin jago main game" # 17
            },
            
            {
                "nama": "Kakak Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "kerennn abiss",
                "pesan": "Terus semangat kuliahnya" # 18
            },
            
            {
                "nama": "Kakak Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "baik dan keren sekalii",
                "pesan": "Tetap semangat dan sehat selalu bang" # 19
            },
            
            {
                "nama": "Kakak Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "pendiammm ",
                "pesan": "Tetap semangat dan sehat selalu kak" # 20
            },
            
            {
                "nama": "Kakak Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "gacorrr abiss",
                "pesan": "Tetap semangat dan sehat selalu bang" # 21
                
            },
            
            {
                "nama": "Kakak Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "pertama kali lihat serem, eh waktu ngobrol seru juga ternyata",
                "pesan": "Tetap semangat dan sehat selalu bang" # 22
            },
            
            {
                "nama": "Kakak Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "kerenn abiss",
                "pesan": "Tetap semangat dan sehat selalu bang" # 23
            },
            
            {
                "nama": "Kakak Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "Cantikkk sekaliii",
                "pesan": "Tetap semangat dan sehat selalu kak" # 24
            },
            
            {
                "nama": "Kakak Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "rambutnya lucuu, iri bangett, secakep ituu",
                "pesan": "Tetap semangat dan sehat selalu kak" # 25
            },
            {
                "nama": "Kakak Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "kerennn abiss",
                "pesan": "Tetap semangat dan sehat selalu bang" # 26
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HJkQEXEh_0oUY-XJRPFucSsxkPsDsSyt", #1
            "https://drive.google.com/uc?export=view&id=1pU2IHllHnYYtOxMGJbZbWwODt8hxaECL", #2
            "https://drive.google.com/uc?export=view&id=1gyipFHz8a2lq3HGLpJlVrEDILtfrzVSC", #3
            "https://drive.google.com/uc?export=view&id=1dYmgIkhuTQrOT4Stw5rWajOJjGAV94fN", #4
            "https://drive.google.com/uc?export=view&id=1V-xqFK752Ho6hR20Gi01RiETsBG7uUzk", #5
            "https://drive.google.com/uc?export=view&id=1EtOHTr1MouRoimrB3eMazwiupHY_crTs", #6
            "https://drive.google.com/uc?export=view&id=1YjkzBhtLW9uFyvRf1gSJHIPiomNV9J6g", #7
            "https://drive.google.com/uc?export=view&id=1KADR7RAuTnRnI2yJtepw638f0OHpqIM9", #8
            "https://drive.google.com/uc?export=view&id=1r-aFcQs70YBT5dJoriDawU9Mav4dZwqT", #9
            "https://drive.google.com/uc?export=view&id=1ATw8-e41XWOB9OKOjyYeEzQDTG9fIoX2", #10
            "https://drive.google.com/uc?export=view&id=1EMfZXdey4brvXOQ4DlrnbkHU3jPMzMhW", #11
            "https://drive.google.com/uc?export=view&id=1EIfUTF9VvtHG347JA3Lo96hC2qMVddDN", #12
            "https://drive.google.com/uc?export=view&id=1yIORIaPX9wh7BSD52ZK6UitIH3yXDheo", #13
            "https://drive.google.com/uc?export=view&id=1B47eFkDI-wILYSMfaRxyjrVUGXm_BPeJ", #14
            "https://drive.google.com/uc?export=view&id=1eHWuBl4n99iPLqoya6sSwvscSaxoovWc", #15
            "https://drive.google.com/uc?export=view&id=1H25L0xo040bJhZudBNuTfTjHL28_nSfF", #16
            "https://drive.google.com/uc?export=view&id=1FHfWs94gfX_6Yh1yQtM8E3mELOVled6F", #17
            "https://drive.google.com/uc?export=view&id=18czHrOdGXdskG2-5i0Vv3UD-TZdumV3L", #18
            "https://drive.google.com/uc?export=view&id=1FCrxyYPYIdTO0idMDZdCV6qupgc7KLkg", #19
            "https://drive.google.com/uc?export=view&id=1SwxCnzULCYbAj9jLdw7VbwJYBp9nXq48", #20
            "https://drive.google.com/uc?export=view&id=1nNVjFYk972RqV1MbTcXcAaARMSfG2yWS", #21
            "https://drive.google.com/uc?export=view&id=1ugspScTgjVMusdWa_lCrwHwUu_Xw6GDo", #22
        ] 
        data_list = [
            {
                "nama": "Kakak Randra Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": " aura orang pintar memang tidak pernah salah",  
                "pesan":"Semangat kuliahnya kakk "# 1
            },
            {
                "nama": "Kakak Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "ceriaa bangettt ",  
                "pesan":"Tetap sehat dan ceria selalu kak"# 2
            },
            {
                "nama": "Kakak Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Sangat berkharisma, vibes nya dewasa sekali menjadi abang asprak ADS RC sangat mengayomi",  
                "pesan":"Semangat teruss belajarnya dan mengoding tentu saja"# 3
            },
            {
                "nama": "Kakak Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": " Masyallah sekali",  
                "pesan":"Tetap istiqomah ya kak, lancar kuliahnyaa! "# 4
            },
            {
                "nama": "Kakak Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": " Pertama kali melihat pasti pintar, eh ternyata benar. Bang fadil jadi astut lmd rc dan asprak alpro rc.",  
                "pesan":"Seamnagat teruss bangg, jangan lupa dibagi bagi kepintarannya, saya mau juga soalnya hehe"# 5
            },
            {
                "nama": "Kakak Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Jujur, kayak abang sendiri sangat perhatian dan mengayomi ",  
                "pesan":" Tetap kayak gitu ya bang, sangat membantu bagi adik adik newbie kader seperti saya"# 6
            },
            {
                "nama": "Kakak Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": " Abangnya cool, diajak foto pun tidak banyak basa basi ",  
                "pesan":"Semangat teruss bang kuliahnyaa "# 7
            },
            {
                "nama": "Kakak Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Baik banget bangett, pengen deep talk bicara masa depan deh kak ",  
                "pesan":"Sehat selalu kak, tetep ceria ya walaupun dunia ini berguncang "# 8
            },
            {
                "nama": "Kakak Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Sangatt amat positive vibes, sukaa deh ",  
                "pesan":"Tetep ceriaaa selalu ya kak, tebarkan positive vibes ituu " # 9
            },
            {
                "nama": "Kakak Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Kalem banget, tidak neko-neko. Dan maniss si mengalahi gula",  
                "pesan":"Semangat teruss bang kuliahnyaa "# 10
            },
            {
                "nama": "Kakak Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "SANGAT CERIAA, seceria itu...",  
                "pesan":"Semangat teruss kak kuliahnyaa"# 11
            },
            {
                "nama": "Kakak Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Baik banget menjadi astut lmd rc, sangat memaklumi pokoknya baik banget deh, big lovee kakk ",  
                "pesan":"Semangat terus yaa kak, sehat selaluu "# 12
            },
            {
                "nama": "Kakak Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Ketika dengar kak olla mau latihan main piano, waaww amazing. Keren si jarang saya menemukannya ",  
                "pesan":"Semangat terus kak menjalani kehidupan kedepan"# 13
            },
            {
                "nama": "Kakak Fairus Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "cantik sekali kakaknyaa",  
                "pesan":"Semangat terus kak kuliahnyaaa"# 14
            },
            {
                "nama": "Kakak Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "kerenn gatau kenapaa, lihatnya keren betull",  
                "pesan":"semangatt kakkk, tetap sehat selalu yaa"# 15
            },
            {
                "nama": "Kakak Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "bang.. first impression kocak si hehe.. gerakin mouse dengan brutal padahal itu laptop bukan komputer, jadi ya tidak tersambung ",  
                "pesan":"Semangatt dan sehat selalu bangg "# 16
            },
            { 
                "nama": "Kakak Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "baiik banget, sangat welcome ",  
                "pesan":"Semangat teruss kak kuliahnyaa "# 17
            },
            {
                "nama": "Kakak Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Sangat nyeleneh, kalau abang tau, saya juga sama, abang juga suka somay kah? saya juga suka banget soalnya ",  
                "pesan":"SEMANGATTT"# 18
            },
          
            {
                "nama": "Kakak Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "BAIK BANGETTT, ketika janjian untuk foto, kakaknya baik banget ngabarin kalau masih di jalan dan minta maaf kalau nunggu. Aku sangat merasa dihargaii",  
                "pesan":"Semangatt teruss kuliahnyaa kakk"# 19
            },
            {
                "nama": "Kakak Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "ngerepotin Tanty",
                "sosmed": "@gustriana.d",
                "kesan": "masih segacor ketika sma, good job kak rahmahh sukses terus ya. Semoga aku tertular kepintaranya huhu",  
                "pesan":"Semangat terus pokoknya kak rahma, dunia penuh gonjang ganjing tapi harus tetap belajar"# 20
            },
            {
                "nama": "Kakak Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Pendiam dan tidak banyak tingkah, hehe",  
                "pesan":"Semangat terus bang kuliahnyaa"# 21
            },
            {
                "nama": "Kakak Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Pintar, satu kalimat yang terlintas di otak ketika mendengar ozt hehe ",  
                "pesan":"Semangat belajarnya bang, kuliahnya juga"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17dZm1lmheVPR7qu8bENo7_Mvg1SyAXuC", #1
            "https://drive.google.com/uc?export=view&id=1XJo9lsjsdYWk-nThgztsaCzfyskgsdGK", #2
            "https://drive.google.com/uc?export=view&id=1sR9YB39shc6Hng1CRVGXS-SXSaogDgy4", #3
            "https://drive.google.com/uc?export=view&id=1tv1y_EkuuDMLPxqtqRVDmg_WdjIPBZ7q", #4
            "https://drive.google.com/uc?export=view&id=1JccZw4pVM48sJ12jWj6X9NPd-gy00IpR", #5
            "https://drive.google.com/uc?export=view&id=1VUS7NUO_fUB6vYR5wrueRQmxuGVXcLeQ", #6
            "https://drive.google.com/uc?export=view&id=1uJM1V8WAm5X8h3upKtZkXrjCpBoCP1LX", #7
            "https://drive.google.com/uc?export=view&id=1LF-QufxpdJe4nFAsz-qatD8fNOmmCGWq", #8
            "https://drive.google.com/uc?export=view&id=1Ta5eLddPtR3JdReiCnEKMHClM8aRM9N0", #9
            "https://drive.google.com/uc?export=view&id=1pWIsm4J0n3-agFa7RFe4p0ZOT442_ano", #10
            "https://drive.google.com/uc?export=view&id=1KLcmpthBovmIHjk6emlUY8-YBb05VqnW", #11
            "https://drive.google.com/uc?export=view&id=1GA4lDtrhNQ8iGvAxKtnxAeQkcyLT36bE", #12
            "https://drive.google.com/uc?export=view&id=1VyjPVyfgR5settmVdlW5mjB56MspfkUG", #13
            "https://drive.google.com/uc?export=view&id=1Eqbo6VZcw2FsD1i0zQgKBYxIQWG0aUce", #14
            "https://drive.google.com/uc?export=view&id=1ZOjZD80kiyQurdScfD7G_K-ZXXldvahS", #15
            "https://drive.google.com/uc?export=view&id=19jXqag8reVp3EocS1lzHu4-AcY5eJBBr", #16
            "https://drive.google.com/uc?export=view&id=13YTmty7BmNhNiZARUeSY-SujX4w1EvNi", #17
            "https://drive.google.com/uc?export=view&id=1olLpOB1gXfzjNTqKNDwcwSiGFJQpm44J", #18
            "https://drive.google.com/uc?export=view&id=1sHE3b8qz9o6_gHX-Kp00zAZVT5xMEFJZ", #19
            "https://drive.google.com/uc?export=view&id=1_vywJ4bXC7euhWRVFZ9UPAP9Yeb7Qgb5", #20
            "https://drive.google.com/uc?export=view&id=1GU57S1iUf6ZLT-2xJsvjZSv5oVUuMlxv", #21
            "https://drive.google.com/uc?export=view&id=1T_ilFq15moTpAPEPq2v847-1QHUryrkw", #22
            "https://drive.google.com/uc?export=view&id=1ipsnJiAbITNUcE6jl0tMlC4cMlB6Nt7P", #23
            "https://drive.google.com/uc?export=view&id=1S0oF-r9ZLOBIojhDza4SkbD6hxp_D_-k", #24
        ]
        data_list = [
            {
                "nama": "Kakak Arafi Putra Maulan",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Lucuu,first time foto bener bener seaib itu ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 1
            },
            {
                "nama": "Kakak Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Cantikk sekaliii",  
                "pesan":"Tetap semangat dan sehat selalu kak"# 2
            },
            {
                "nama": "Kakak Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Cantikk banget kak ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 3
            },
            {
                "nama": "Kakak Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": " mentorr terbaikkk, selalu mengusahakan dan membantu para anak-anaknya",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 4
            },
            {
                "nama": "Kakak Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Cantikk sekalii kak ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 5
            },
            {
                "nama": "Kakak Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Cantikkk bangett ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 6
            },
            {
                "nama": "Kakak Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "asikk banget  ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 7
            },
            {
                "nama": "Kakak Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "LUCUUU",  
                "pesan":" Tetap semangat dan sehat selalu kak"# 8
            },
            {
                "nama": "Kakak Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang terlihat pendiam tapi selalu berusaha mencairkan suasana ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 9
            },
            {
                "nama": "Kakak Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "CANTIKKK",  
                "pesan":" Tetap semangat dan sehat selalu kak"# 10
            },
            {
                "nama": "Kakak khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Cantikkk sekali kakk",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 11
            },
            {
                "nama": "Kakak Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Cantikkk sekalii kak",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 12
            },
            {
                "nama": "Kakak Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Keren abisss",  
                "pesan":" Tetap semangat dan sehat selalu kak"# 13
            },
            {
                "nama": "Kakak Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Cantikk sekaliii ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 14
            },
            {
                "nama": "Kakak Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Cantikk sekalii ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 15
            },
            {
                "nama": "Kakak Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Lucuuuu dan asikkk ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 16
            },
            {
                "nama": "Kakak Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "SANGAT BAIKKKK ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 17
            },
            {
                "nama": "Kakak Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Cantiikkk sekaliii ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 18
            },
            {
                "nama": "Kakak Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "kerennn ",  
                "pesan":"Tetap semangat dan sehat selalu kak"# 19
            },
            {
                "nama": "Kakak Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Keren bangett ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 20
            },
            {
                "nama": "Kakak Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Cantikk sekali kak",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 21
            },
            {
                "nama": "Kakak Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Keren bangett",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 22
            },
            {
                "nama": "Kakak Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Cantikkk sekaliii ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 23
            },
            {
                "nama": "Kakak Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": " Cantikkk sekalii",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()


if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1U2XOCMrHzM_oHAo3W1yiJgHFR1DSQb7r", #1
            "https://drive.google.com/uc?export=view&id=14xci1IA8G8yUeEov8fkPiZqyZCaJ-MN5", #2
            "https://drive.google.com/uc?export=view&id=1BTYjO5rqSyaKzS3kkMxG_XeNENaqWl9K", #3
            "https://drive.google.com/uc?export=view&id=1DCSvLlj91_r8OH2LqG1ltG5ouFJjLg5Y", #4
            "https://drive.google.com/uc?export=view&id=1Qcj9W4YngFJbDlagZ7Pwfpzrbss0Aduc", #5
            "https://drive.google.com/uc?export=view&id=1dntkvR__fyx5ZW1qByk87-GsHe7q2h_d", #6
            "https://drive.google.com/uc?export=view&id=1ZN6Ie-72xU5FrfRoS4J3i81-fWkVUcmv", #7
            "https://drive.google.com/uc?export=view&id=1TmwiGzT_KSIADF3ZUsTLHpKBxDPJsFIH", #8
            "https://drive.google.com/uc?export=view&id=1rwVc8hC_CfEjSgZURv7LJpxKVwz-Gt_i", #9
            "https://drive.google.com/uc?export=view&id=1JD9C_MGS_sgn_zOHRx-9VodguI-hoxLq", #10
            "https://drive.google.com/uc?export=view&id=1I0GfRQuwQqQFSBheSY_lia8nKvfPQe7C", #11
            "https://drive.google.com/uc?export=view&id=1xS1aE7c90mID2IWQ1PtPaGO6wpwL4YpW", #12
            "https://drive.google.com/uc?export=view&id=1XGUJRiyh9n21BUjt9CjdRvkBNBMXDwBQ", #13
            "https://drive.google.com/uc?export=view&id=1-y6ZfmJT8d65EjPRBSnwYS6crrv3qCtm", #14
            "https://drive.google.com/uc?export=view&id=1Utx5HK-IJGND4amPkqcM553kccGgaQO8", #15
        ]
        data_list = [
            {
                "nama": "Kakak Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": "Keren banget kak, aura nya bener bener ga menye menye ",  
                "pesan":"Tetap semangat dan sehat kak"# 1
            },
            {
                "nama": "Kakak Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Aku keinget ibu kalau lihat ka renta huhu, rambutnya sama sama pendek, kangen bangett.",  
                "pesan":"Tetap semangat dan sehat kak "# 2
            },
            {
                "nama": "Kakak Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Cantik bangett kak, dan Masyallah sekalii ",  
                "pesan":"Tetap Semangat dan sehat kak "# 3
            },
            {
                "nama": "Kakak Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Cantikk sekaliii ",  
                "pesan":"Tetap Semangat dan sehat kak"# 4
            },
            {
                "nama": "Kakak Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": " terlihat sangar tetapi lembut didalam",  
                "pesan":"Tetap semangat dan sehat bang "# 5
            },
            {
                "nama": "Kakak Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Cantikkk sekaliii ",  
                "pesan":"Tetap Semangat dan sehat kak"# 6
            },
            {
                "nama": "Kakak May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Cantikkk Sekaliii ",  
                "pesan":"Tetap Semangat dan sehat kak "# 7
            },
            {
                "nama": "Kakak Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Terlihat pendiam ",  
                "pesan":"Tetap semangat dan sehat bang"# 8
            },
            {
                "nama": "Kakak Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "Asikkk ",  
                "pesan":"Tetap semangat dan sehat bang "# 9
            },
            {
                "nama": "Kakak Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Baikk sekaliii",  
                "pesan":"Tetap semangat dan sehat bang"# 10
            },
            {
                "nama": "Kakak Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "uwuuu luucuu, syantik, asikk pokoknyaa",  
                "pesan":" Tetap semangat dan sehat kak"# 11
            },
            {
                "nama": "Kakak Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Cantikkk sekaliii",  
                "pesan":"Tetap semangat dan sehat kak"# 12
            },
            {
                "nama": "Kakak Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Terlihat pendiam",  
                "pesan":" Tetap semangat dan sehat kak"# 13
            },
            {
                "nama": "Kakak Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Cantikkk sekaliii",  
                "pesan":"Tetap semangat dan sehat kak "# 14
            },
            {
                "nama": "Kakak Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Cantikkk sekaliii",  
                "pesan":"Tetap semangat dan sehat kak "# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tWcsqUL8U1boffJF9kjibLSsNMrgNrcq",
            "https://drive.google.com/uc?export=view&id=1o1TMpgOTICkULdz2nxXnbx255xfw_jlL",
            "https://drive.google.com/uc?export=view&id=1t0IrbszgKqdZeAOd04FIFtagS4ta2y09",
            "https://drive.google.com/uc?export=view&id=1jifn_odNVN4IBMMxv5OtJYDQrnndm3OB",
            "https://drive.google.com/uc?export=view&id=1nN5Y0bFj8z9Mq1w81K2GlA5vvOprhMLz",
            "https://drive.google.com/uc?export=view&id=1ML45mPRu911EO3mAOMehcBqLSOozawrn",
            "https://drive.google.com/uc?export=view&id=1dCtlAoXgVN9RL54nl3SlJK4IP9ysrZAI",
            "https://drive.google.com/uc?export=view&id=1QuEF8-99y2Fxf3Abr1nGPX2NY6nyIyfP",
            "https://drive.google.com/uc?export=view&id=12hTcYk145uQ4c22xfFZM-gur0Jn4C-jz", 
            "https://drive.google.com/uc?export=view&id=1wT09ntFQ-sFYYQXnQphpWilAyJWzspuZ",
            "https://drive.google.com/uc?export=view&id=1KP2Qgn1QWsGIPTIE1v345NnsADDxuL_Q",
            
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
                "kesan": "Membawa aura semangat terus ",  
                "pesan": "semoga sukses dunia akhirat bang"# 1
            },
            {
                "nama": "Kakak Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakak lucu nan baik hati, dan kesabaran seluas samudera ",  
                "pesan": "Sehat- sehat ya kak, dan semangat kuliahnya "# 1
            },
              {
                "nama": "Kakak Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "Keren bangg",  
                "pesan": "Semangat bang kuliahnya "# 1
            },
              {
                "nama": "Kakak Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Semangatt bangett pembawaanya yang liat jadi ikutan semangat+ceria ",  
                "pesan": "Semangatt kak kuliahnya yaa "# 1
                   },
              {
                "nama": "Kakak Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "Cantiiikk sekaliiiie ",  
                "pesan": "Semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Kakak Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Semangat terus ya kak kuliahnya  "# 1
            },
             {
                "nama": "Kakak Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Bang lucu banget ",  
                "pesan": "Semangat bang, lancar terus ya kuliahnya "# 1
            },
              {
                "nama": "Kakak Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Cantik banget kakk",  
                "pesan": "Semangat ya kak kuliahnya"# 1
            },
              {
                "nama": "Kakak Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "cantikk bangettt, make up nya juga bagus sekalii ",  
                "pesan": "Semangat teruss kak kuliahnya"# 1
            },
              {
                "nama": "Kakak Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": " Sekali lihat bisa lihat deh kak hani orang sangat bersemangat apalagi tentang jualan risol",  
                "pesan": "Semangattt teruss kak, apakah ada loker? "# 1
            },
              {
                "nama": "Kakak Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Pendiam tidak banyak bicaraa",  
                "pesan": "Semangatt teruss ya kak kuliahnyaa "# 1
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Sx9divT6acwFJAeMAl-hNe42LJt16ibu", 
            "https://drive.google.com/uc?export=view&id=13bkaB7ZJbeLVPXWhWC4dmZpno_UzX9XP", 
            "https://drive.google.com/uc?export=view&id=1JlK2SKyIjFrCsKy3aDPuQSjgTiZLDfLI",
            "https://drive.google.com/uc?export=view&id=1eWMwGMKonL4QUgN9Cb8GY_iiYnwQvguf",
            "https://drive.google.com/uc?export=view&id=1lrsJoULgUw_7veMSoqZpohFP0Tz3hc6P",
            "https://drive.google.com/uc?export=view&id=1Q93BjsOvazgQZ0Gf7VOEv1SRP9tWKAoL",
            "https://drive.google.com/uc?export=view&id=1Qax4aJAjxilXbfFPjcQ0ntAJ1H_5UNxg",
            "https://drive.google.com/uc?export=view&id=1ryfkcILT1yiKWZO--61gzZ7cep56qfLD",
            "https://drive.google.com/uc?export=view&id=17eQlwtX5iYNu2A9RyBqtZT1T6cnKxKGr",
            "https://drive.google.com/uc?export=view&id=1qDDnR54YRfuTrBLrwjS1oy_527Q5aYFF",
            "https://drive.google.com/uc?export=view&id=1Yeo8Cpdg55ieMeu-P9djLrYXgWTMcjJn",
            "https://drive.google.com/uc?export=view&id=1ilctgKzSabUxqsMdRZ35Dgsx9MRxZcRB",
            "https://drive.google.com/uc?export=view&id=1splDi7Z3zcqJeKKX4RTayTByK4211kZX",
            "https://drive.google.com/uc?export=view&id=1_TABkxOBg15FbTWSsyD0W_bMNlKfOo6B",
            "https://drive.google.com/uc?export=view&id=1EUWs29FB2io-_9thE3-71UfjuQL5_CWQ",
            "https://drive.google.com/uc?export=view&id=1H2Su0I3ZUF3FYwegAM2npvBJXheQouYu",
            "https://drive.google.com/uc?export=view&id=17Krtbksg5qCI8Veg9Pq3kUVa1GWbtRm_",
            "https://drive.google.com/uc?export=view&id=1qMi2UqF5hOOLDHDEbDTMPvmY8rTtLqcm",
        ]
        data_list = [
            {
                "nama": "Kakak Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "lucuuu, dan positive vibes",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
            {
                "nama": "Kakak Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "Cantikk banget",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Keren banget bang",  
                "pesan": "Tetap semangat dan sehat selalu bang"# 1
              },
              {
                "nama": "Kakak Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Keren bang",  
                "pesan": "Tetap semangat dan sehat selalu bang"# 1
            },
              {
                "nama": "Kakak Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Kerennnn",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "Cantikkk banget kakkkk",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Cantikk banget kak",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Cantikk betull kak",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Lucuuuuu",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Cantikkk",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Cantik sekalii kak",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "Cantikk sekalii kak",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Cantikk sekali kak",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Terlihat malu malu",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Cantik sekalii kakk",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Cantikk sekali kakk",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "lucuuu, girly bangettt",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
              {
                "nama": "Kakak Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "cantikk bangett,lucuuu bangett kayak permen kapas",  
                "pesan": "Tetap semangat dan sehat selalu kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

    

# Tambahkan menu lainnya sesuai kebutuhan

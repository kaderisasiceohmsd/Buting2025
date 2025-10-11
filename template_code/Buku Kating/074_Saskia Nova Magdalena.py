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
                "nim": "122450000",
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
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "cantik sekali kakaknyaa",  
                "pesan":"Semangat terus kak kuliahnyaaa"# 14
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
                "kesan": " ",  
                "pesan":" "# 16
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
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "BAIK BANGETTT, ketika janjian untuk foto, kakaknya baik banget ngabarin kalau masih di jalan dan minta maaf kalau nunggu. Aku sangat merasa dihargaii",  
                "pesan":"Semangatt teruss kuliahnyaa kakk"# 19
            },
            {
                "nama": "Kakak Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "masih segacor ketika sma, good job kak rahmahh sukses terus ya. Semoga aku tertular kepintaranya huhu",  
                "pesan":"Semangat terus pokoknya kak rahma, dunia penuh gonjang ganjing tapi harus tetap belajar"# 20
            },
            {
                "nama": "Kakak Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Pendiam dan tidak banyak tingkah, hehe",  
                "pesan":"Semangat terus bang kuliahnyaa"# 21
            },
            {
                "nama": "Kakak Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@",
                "kesan": "Pintar, satu kalimat yang terlintas di otak ketika mendengar ozt hehe ",  
                "pesan":"Semangat belajarnya bang, kuliahnya juga"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

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
            "https://drive.google.com/uc?export=view&id=12hTcYk145uQ4c22xfFZM-gur0Jn4C-jz", #
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
                "nim": "123450023",
                "umur": ".",
                "asal": ".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": ".",
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
    

# Tambahkan menu lainnya sesuai kebutuhan

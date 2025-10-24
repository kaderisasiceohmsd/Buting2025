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
           "https://drive.google.com/uc?export=view&id=1Ok3q6n_xsdAnOJJWaoGazSuB5MjEspNR",#1
            "https://drive.google.com/uc?export=view&id=1oDhfns62AQW5yXJ0GEGRbXo5aptzEEoI",#2
            "https://drive.google.com/uc?export=view&id=1EBUl-extPFydoTN7BUSz8Iy-9tFautCb",#3
            "https://drive.google.com/uc?export=view&id=1VaVumephZz_uQu6Sy2hJ16IYQ1EFgkYW",#4
            "https://drive.google.com/uc?export=view&id=1mvSAabh0E6Vo36cjAI6CMJ_KYc5EqWVt",#5
            "https://drive.google.com/uc?export=view&id=1RP41bnOYjFTFwd6sNMckRjWnEc6xLugT",#6
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
                "kesan": "Bang asik banget",  
                "pesan": "Semangat bang kuliahnya!!"#1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren banget bang, dari pembawaanya keliatan banget orang keren nya",  
                "pesan": "Semangat bang kuliahnya!"#2
            },
              {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kak, asik sekalii",  
                "pesan": "semangat terus kuliahnya kak!"#3
            },
              {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya kalem banget, aku kenal orang yang mirip banget sama kak syadza, kuliah di Itera juga tapi udah lulus",  
                "pesan": "semangat terus kuliahnya kakak !"#4
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Satu kata : Amazing",  
                "pesan":"semangat terus kuliahnya kakak !"#5
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak nya asik sekali membawa vibes positive banget",  
                "pesan": "semangat terus kuliahnya kakak !"#6
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UpXMqB4R73yhB3IDthG_wq9QGl-db7dR",
            "https://drive.google.com/uc?export=view&id=1nP3y8CnXyal9njqPDvEqab-AMy1fhhm0",
            "https://drive.google.com/uc?export=view&id=1y5VHNpGw3SPQFweGdlAKRHiEHFrxgIyz",
            "https://drive.google.com/uc?export=view&id=1JGH8Lob0pXf3H81AfStuZhWN_YbkYHtR",
            "https://drive.google.com/uc?export=view&id=1Rsd-HPya7qUUwbFmvi1quDu2XP_QxAL9",
            "https://drive.google.com/uc?export=view&id=1KA185zvPquU9_fhWH1OSciWWbMswCuDF",
            "https://drive.google.com/uc?export=view&id=1630snoSH29Hb7yPBNByTRCW2D3AQe8K7",
            "https://drive.google.com/uc?export=view&id=1NFnZeP8zLNWZFUQgOoAKXpRAUiOk9YYB",
            "https://drive.google.com/uc?export=view&id=1S65L_xvJTAml-KiUXPyzFmw5ZCsCXw23",
            "https://drive.google.com/uc?export=view&id=1J2pWhwDLKVN6mOjwKE_4glX7q7d18q3e",
            "https://drive.google.com/uc?export=view&id=1WixWFR2R06GfsjoJrF6CqSJ9SVZjOEoA",
            "https://drive.google.com/uc?export=view&id=1O3pj6742ZXMXUOTRH5dknCAoF_11vk8m",
            "https://drive.google.com/uc?export=view&id=1q2HA8mJOuRWqj-Bd_R-0GxjsAPqQlgh9",
            "https://drive.google.com/uc?export=view&id=1eHG87SqNTft5KRvBVi95SjGc_WyZXvpf",
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
                "kesan": "Asik banget bang",  
                "pesan": "Semangat terus bang walaupun hidup gonjang ganjing"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
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
                "nama": "Renisha Putri Giani",
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
                "nama": "Anisa Fitriyani",
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
                "nama": "Dharu Cahyoaji Sasongko",
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
                "nama": "Feby Wulandari",
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
                "nama": "Givaro Ananta",
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
                "nama": "Mirzan Yusuf Rabbani",
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
                "nama": "Berliana Enda Putri",
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
                "nama": "Juesi Apridelia Saragih",
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
                "nama": "Ridho Benedictus Togi Manik",
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
                "nama": "Feryadi Yulius",
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
                "nama": "Monica Patricia Tanjung",
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
                "nama": "Wan Nashwa Alhasni Yuska",
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
            "https://drive.google.com/uc?export=view&id=19hTYoH8jyLdOx0BbNSogtuwDqximC80P",
            "https://drive.google.com/uc?export=view&id=1kPIGJAjyGUPj4LdghnBtXutxwfLWLRHw",
             "https://drive.google.com/uc?export=view&id=1iz2r4mnk2kEKT4B-dD6Uk2bHU81yKIx8",
             "https://drive.google.com/uc?export=view&id=1r3vT3ZZI_xigraJTaohvTiz-kIkVAkHs",
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
                "kesan": "Selalu berusaha membuat lingkungan sekitar jadi asik",  
                "pesan": "Lancar ya bang kuliahnya, dan sehat selalu"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
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
                "nama": "Fathinah Nur Azizah",
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
                "nama": "Lia Hana Ichisasmita",
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
            "https://drive.google.com/uc?export=view&id=1AUeQPPrwd-ecCfwWfJg6LlAcmoTV0iF3", #1
            "https://drive.google.com/uc?export=view&id=1O4AKtC4TgK6ZfLMG9fH9DSHLzcD3_DJm", #2
            "https://drive.google.com/uc?export=view&id=1MsJ7ojYqjkJ52KJCP6uyAOjM_Jbch644", #3
            "https://drive.google.com/uc?export=view&id=1YKGkwLIuCW6-JIzGuBHaS2iWSkE6KaGc", #4
            "https://drive.google.com/uc?export=view&id=1sxNbfjc7vZTdnRASGHrsMjHceOlfH_Et", #5
            "https://drive.google.com/uc?export=view&id=1a1mV83iOuG9Y0bEic1ncw8gkD0zqJzGk", #6
            "https://drive.google.com/uc?export=view&id=1NqBZmhnLfmPPsQWf2SVDnYQfzfQhUUcU", #7
            "https://drive.google.com/uc?export=view&id=1prdiQXeKb9J12VBqy-JNaHhXB4HHSLsK", #8
            "https://drive.google.com/uc?export=view&id=10ruvw6XcqqbWQgWFi4JaImBwOAqVR55Q", #9
            "https://drive.google.com/uc?export=view&id=1T8Z8fga5QTBOOFwFaVYRn9xDPiNr20f-", #10
            "https://drive.google.com/uc?export=view&id=1SFedVyoLy8342B_1l5N4THWqv_i97cwV", #11
            "https://drive.google.com/uc?export=view&id=1s1V_2Rs3C9wD1mx9txSDXvnM53PAoV7y", #12
            "https://drive.google.com/uc?export=view&id=1OOi_oS2jamBEzm0vjA8StJ8iLgEl2hzj", #13
            "https://drive.google.com/uc?export=view&id=1Aav54ZQRkJvrsXPxbVJqkpvyW9Xdzbcm", #14
            "https://drive.google.com/uc?export=view&id=1NBPAWgZ52GqSIa-NL_XZaiAmGTd-CaqG", #15
            "https://drive.google.com/uc?export=view&id=1y8UuqDFN-yQQ2LGx0V-JSpSguKRgAoWX", #16
            "https://drive.google.com/uc?export=view&id=1UX7kfod52mCuxz6EYO01rxig46CVnN5p", #17
            "https://drive.google.com/uc?export=view&id=1p1iH8aCJ7lalsOwBnridDkzUJTJhalqx", #18
            "https://drive.google.com/uc?export=view&id=1IHO39OH4-Dktyd_T8F5B4k_DaYCabiDu", #19
            "https://drive.google.com/uc?export=view&id=1oAAsS5Nc6pUl77MDYOPR2LrfGgEoSDZ6", #20
            "https://drive.google.com/uc?export=view&id=1sBemMCfKJidyUjCDsHZH145B2ciHmbey", #21
            "https://drive.google.com/uc?export=view&id=16VGT-gHlxCJsMVOYBHe4j_GAvTMeg-Ci", #22
            "https://drive.google.com/uc?export=view&id=1RXZAZ6O3iEAV6huNmHlHNzdN3nmBVcEn", #23
            "https://drive.google.com/uc?export=view&id=1Ht4GQO6DAUjV_z6PI1U97pl8NhVMkHzz", #24
            "https://drive.google.com/uc?export=view&id=1MMTQMAQy5pNva9IHhR1kiUVM_SOiPFuu", #25
            "https://drive.google.com/uc?export=view&id=1cQ3iLORet5K2OhAGehvdERAEPcjXyLE1", #26
            
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
                "kesan": "keren bangettt",  
                "pesan":"Tetap semangat dan sehat selalu bang"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
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
                "nama": "Allya Nurul Islami Pasha",
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
                "nama": "Ahmad Rizky",
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
                "nama": "Arienta Khusnul Ananda",
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
                "nama": "Daffa Hadyan Navista",
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
                "nama": "Natasya Amavisca",
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
                "nama": "Nobel Nizam Fathirizki",
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
                "nama": "Nurul Alfajar Gumel",
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
                "nama": "Vany Salsabila Putri",
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
                "nama": "Ahmad Sahidin Akbar",
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
                "nama": "Ali Aristo Muthahhari Parisi",
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
                "nama": "Rosalia Siregar",
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
                "nama": "Kharisma Mustika Sari",
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
                "nama": "Gusti Putu Ferazka",
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
                "nama": "Sahid Maulana",
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
                "nama": "Daffa Ahmad Naufal",
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
                "nama": "Ihsan Maulana Yusuf",
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
                "nama": "Rewina Audriya Melva Sari",
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
                "nama": "Benget Sidabutar",
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
                "nama": "Uliano William Purba",
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
                "nama": "Kevin Antoni Junior",
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
                "nama": "Erma Daniar Safitri",
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
                "nama": "Lidia Natasyah Marpaung",
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
                "nama": "Muhammad Ridwan",
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
            "https://drive.google.com/uc?export=view&id=1Y15Qy4ZJVCB7VRSlmHCFDppewrXkPE6U", #1
            "https://drive.google.com/uc?export=view&id=1BARc0SPPXB2u25myK1Kd4mPHTUHRQKVb", #2
            "https://drive.google.com/uc?export=view&id=1aRiwSuNRI3csWl43nFu_Jm_bT6-N9anW", #3
            "https://drive.google.com/uc?export=view&id=1eYSTtmCSafZGNVZMx-aQJ34dKqAsE5_M", #4
            "https://drive.google.com/uc?export=view&id=1p5hCswxf5-l6ntX86m_tHb66MAcsiNfn", #5
            "https://drive.google.com/uc?export=view&id=1tNQHwf-nAE29JLafapTzKhDkaYoSz6HM", #6
            "https://drive.google.com/uc?export=view&id=1hyIIXb-c--VyGUCnPzroyHVSgtXY5EdX", #7
            "https://drive.google.com/uc?export=view&id=1Mlh4BUsu9VbsK5RA-vVNe2Js9Xi-S0D9", #8
            "https://drive.google.com/uc?export=view&id=1mHYdoERwjN6BBt8G0u0VP-jbXaPWGZ8z", #9
            "https://drive.google.com/uc?export=view&id=1qhYOGQtKYkuiyRo1fC-uoK-eafYuRHj8", #10
            "https://drive.google.com/uc?export=view&id=1jHALI0fgnggjV4n2phagybhqV2pqjjbI", #11
            "https://drive.google.com/uc?export=view&id=10V8nWBegSvctVPgJ0jeJlUb7Rm3YU-hN", #12
            "https://drive.google.com/uc?export=view&id=1praf8iNnzygKrCBjdQsbNXqfjSmBkNjB", #13
            "https://drive.google.com/uc?export=view&id=1Bp11_bB8kHS8T-hDkxbsCBL9nfhKhgTJ", #14
            "https://drive.google.com/uc?export=view&id=13FX5fQXvFHu6uiVHR1F6Evp3Gd8H3_vn", #15
            "https://drive.google.com/uc?export=view&id=1npRp_6WEU9GPzzuX9zCBl8H_N0HDCtsw", #16
            "https://drive.google.com/uc?export=view&id=1G8rkQ583F_qEPLM8YCPCddiScAb6Xgre", #17
            "https://drive.google.com/uc?export=view&id=1e82hL_6kXUiLu47RyYmfm0LeMiJtrjWe", #18
            "https://drive.google.com/uc?export=view&id=1qXkdF-sAomeIyFWFvb273qm_iRL2ECJw", #19
            "https://drive.google.com/uc?export=view&id=1MrsQqn517jW6NJ9IqhAW2_LzxaFNPIT4", #20
            "https://drive.google.com/uc?export=view&id=1QAJHdfdVJ-TD0xaXtYROOp7GBueMmbn7", #21
            "https://drive.google.com/uc?export=view&id=1WhlNGkLxRA5Fz6tzMQUg0jYa93brQ78r", #22
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
            "https://drive.google.com/uc?export=view&id=1lsg9oq93cG7URgiz4E0eapa5fBdiOA36", #1
            "https://drive.google.com/uc?export=view&id=1nRUd9ckAYyT1jTbh00SyEFpmyI_pse4C", #2
            "https://drive.google.com/uc?export=view&id=1X3sJ0L14kj2-rrbXXH9Frz73aldup3s-", #3
            "https://drive.google.com/uc?export=view&id=1NXOOMTewMendO6tECis1EoY1aIs3h2e8", #4
            "https://drive.google.com/uc?export=view&id=1dONXzAfJdgfgZqamhPBma-Nvj-wbls0L", #5
            "https://drive.google.com/uc?export=view&id=1uqdRTW5aBKPL3eXZiLz1guh9W9Bl-Vh8", #6
            "https://drive.google.com/uc?export=view&id=1gG-8qwUq-DbM0w_WTqV5ViITHuEQafp8", #7
            "https://drive.google.com/uc?export=view&id=1ORM0oJE98ODg3QKZVooBp28I5_7SKU3S", #8
            "https://drive.google.com/uc?export=view&id=1iemB8DsnLOSaIUyUZ1Yt0DjyVtFmj0Ap", #9
            "https://drive.google.com/uc?export=view&id=1nbjg9NGEKGLZ2LkO-zuxu4CqB2C0Wsm7", #10
            "https://drive.google.com/uc?export=view&id=1t7DWR75p07dN7rt8OjKowgEgIih0okIh", #11
            "https://drive.google.com/uc?export=view&id=10zJXv5Y-wiHc3XdcFG5Jrly2RMW9OTW2", #12
            "https://drive.google.com/uc?export=view&id=1o-ZPFN8gtWykH2cY-e4-AlYWsi3cuCp_", #13
            "https://drive.google.com/uc?export=view&id=1nIjbHENbeWFKHGI5kStUKMJUQygZqCXB", #14
            "https://drive.google.com/uc?export=view&id=1TltHSQ-lyN7zNwygnU8lENHSLNfWRGUG", #15
            "https://drive.google.com/uc?export=view&id=1qXv55TeEEhgdF1P3NxTUGjkFeOp6MfBX", #16
            "https://drive.google.com/uc?export=view&id=1pqGCTPhL0jh_LdzhvQ8lpAFvupSendT_", #17
            "https://drive.google.com/uc?export=view&id=1xtmTMMix8g4t31EpTO-0Byi2s5PtgoVW", #18
            "https://drive.google.com/uc?export=view&id=1myeHRfduf-ENzN25-BDyj4ymgGX7jN_X", #19
            "https://drive.google.com/uc?export=view&id=1FLvhvwgpMN2cwC8AZIKXplLg6fXsbP8m", #20
            "https://drive.google.com/uc?export=view&id=1-5Oj0_bMOsF0Q1QujjXHkJqRM8GKAHbi", #21
            "https://drive.google.com/uc?export=view&id=13yf2CUbtsrki3MUQdAn4pAm8qS3ZZ6nj", #22
            "https://drive.google.com/uc?export=view&id=1-GSTj3jCBug2Br1ZBYOyDOUkFNnVnswC", #23
            "https://drive.google.com/uc?export=view&id=1eFQERYkxsvk_4eUGe7hoDbCTKZhtBHSI", #24
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
                "kesan": "Lucuu,first time foto bener bener seaib itu ",  
                "pesan":"Tetap semangat dan sehat selalu kak "# 1
            },
            {
                "nama": "Yohana Manik",
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
                "nama": "Dea Mutia Risani",
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
                "nama": "Devyna Sonya Palupi Sanjaya",
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
                "nama": "Luthfia Laila Ramadhani",
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
                "nama": "Cindy Laura Manik",
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
                "nama": "Desman Velius Halawa",
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
                "nama": "Dea Amanda",
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
                "nama": "Irvan Alfaritzi",
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
                "nama": "Fathya Intami Gusda",
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
                "nama": "khazanatil ilmi",
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
                "nama": "Nurul Izzah Istiqomah",
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
                "nama": "Qois Olifio",
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
                "nama": "Melinza Nabila",
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
                "nama": "Nayla Shafira Roza",
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
                "nama": "Aditya Taufiqurrohman",
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
                "nama": "Tarisya Hidayatul Rahmi",
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
                "nama": "Ratu Keisha Jasmine Deanova",
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
                "nama": "Khoirul Muttoharoh",
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
                "nama": "Arya Muda Siregar",
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
                "nama": "Arini Puteri Elandra",
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
                "nama": "Syahrialdi Rachim Akbar",
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
                "nama": "Lutfia Aisyah Putri",
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
                "nama": "Nabyla Sharfina",
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
            "https://drive.google.com/uc?export=view&id=1pg88XTUInlapehdM0YfoIXv8WcND4xgg", #1
            "https://drive.google.com/uc?export=view&id=1nBbAmeLYP0yttdcylAxtxE0n0c4JB3xX", #2
            "https://drive.google.com/uc?export=view&id=1N3v0H_5Sb4zpb5B_WGteDnrJ8y91lVPd", #3
            "https://drive.google.com/uc?export=view&id=1i7tIiKlJmWkNimyYvWZ6rLDUokBT8hta", #4
            "https://drive.google.com/uc?export=view&id=1JsFQ2_mlFSLYYS1Yje3z9qbmgYfXrKJ1", #5
            "https://drive.google.com/uc?export=view&id=10jt2s14uhf2B8ejBaWodI_RGUf4UEQBV", #6
            "https://drive.google.com/uc?export=view&id=1gdN7wMmha_ccHi8y20HwLx4voJDoaH7a", #7
            "https://drive.google.com/uc?export=view&id=1bY-ufR8Qqh3NCYhufbH4ATF3dYy1CXNm", #8
            "https://drive.google.com/uc?export=view&id=10XtkajddZM4feiouPRjt0oj2GLHpSgjL", #9
            "https://drive.google.com/uc?export=view&id=1ZnXEcA3GbGUy5Fx9wmz5aVVrrlmh7BDq", #10
            "https://drive.google.com/uc?export=view&id=1E2g3A-cXMF8yU-cJkj7klcSQKMZ7irrq", #11
            "https://drive.google.com/uc?export=view&id=1dS7uN6Njs-FuI8XrKxd0Rl3zf9VYg0W3", #12
            "https://drive.google.com/uc?export=view&id=1g2CwtcjkiOn3PLrliJfna3V73x6Oop-Z", #13
            "https://drive.google.com/uc?export=view&id=1LUGtqQUev86hheF3NRgceqnKUK4Emkti", #14
            "https://drive.google.com/uc?export=view&id=1sQD4bLLi-pXR0Cb8gwnDtpsmRBLL0wMI", #15
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
                "kesan": "Keren banget kak, aura nya bener bener ga menye menye ",  
                "pesan":"Tetap semangat dan sehat kak"# 1
            },
            {
                "nama": "Renta Siahaan",
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
                "nama": "Salwa Farhanatussaidah",
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
                "nama": "Azzahra Putri Kamilah",
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
                "nama": "Haikal Fransisko Simbolon",
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
                "nama": "Iqfina Haula Halika",
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
                "nama": "May Talitha Dahlia",
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
                "nama": "Muhammad Naufal Al Ghani",
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
                "nama": "Zailani Satria",
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
                "nama": "Rendi Alexander Hutagalung",
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
                "nama": "Hanna Gresia Sinaga",
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
                "nama": "Keren Marito Lumban Gaol",
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
                "nama": "Muhammad Hanif Dzaky Arifin",
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
                "nama": "Sarah Wasti",
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
                "nama": "Zahra Putri Salsabila",
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
            "https://drive.google.com/uc?export=view&id=1EhuRWtZp95P8u9EpYmcFjeAKdYsNdJjZ",#1
            "https://drive.google.com/uc?export=view&id=1XQOyrej0yKPd8oBK6_pUp-zg_NqGQEOJ",#2
            "https://drive.google.com/uc?export=view&id=1hGhcDqKHmcI3DhMOczhm8T-b9cy2gQgS",#3
            "https://drive.google.com/uc?export=view&id=1B0ImuwhjBvIfkoThwYBdRqO_Qiht6vvh",#4
            "https://drive.google.com/uc?export=view&id=1Ae2M9cpKpDRNqLqfZ5s-wGQw4RjTEWO3",#5
            "https://drive.google.com/uc?export=view&id=1VcMqVewwVEVXX_VWj1wKG8JW0hDIvOPS",#6
            "https://drive.google.com/uc?export=view&id=1qDN8ybUujjPJihb1kB2fu9Q2nb9b0D3y",#7
            "https://drive.google.com/uc?export=view&id=1iLUXn_ZRug73gHqAtr5ZGQ75HGYerw9_",#8
            "https://drive.google.com/uc?export=view&id=1rkwR-AwQ_A-hDoOwlZUUB3D00RlKc2lL",#9
            "https://drive.google.com/uc?export=view&id=1sS5Ra-XaU16ZbN0EdKnTvHmVmKor9och",#10
            "https://drive.google.com/uc?export=view&id=1Wo2ITJ9wqK37STcNqrLxuQF37l2zleHV",#11
            
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
                "pesan": "Sehat- sehat ya kak, dan semangat kuliahnya "# 2
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
                "pesan": "Semangat bang kuliahnya "# 3
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
                "pesan": "Semangatt kak kuliahnya yaa "# 4
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
                "pesan": "Semangat terus kuliahnya kak"# 5
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
                "pesan":"Semangat terus ya kak kuliahnya  "# 6
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
                "pesan": "Semangat bang, lancar terus ya kuliahnya "# 7
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
                "pesan": "Semangat ya kak kuliahnya"# 8
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
                "pesan": "Semangat teruss kak kuliahnya"# 9
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
                "pesan": "Semangattt teruss kak, apakah ada loker? "# 10
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
                "pesan": "Semangatt teruss ya kak kuliahnyaa "# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=118JWq-hQZOu_CJ_oayO69sgyDo5FghDW", 
            "https://drive.google.com/uc?export=view&id=1SiJc_FJxloopduzsV_2eap3GR_BfFUsn", 
            "https://drive.google.com/uc?export=view&id=191i72rG_pB_Hn08aFf_GO-JagwQ9QJ9Q",
            "https://drive.google.com/uc?export=view&id=1DY6FQKSF5hjDXcnl5ujaaKXPOTukaf69",
            "https://drive.google.com/uc?export=view&id=1XUnjf4xfmnb3rWySKO5QuXakbMnr65F6",
            "https://drive.google.com/uc?export=view&id=1mA-1sCh9Jwgil9-Vyo3RKDwsS2VXqhA3",
            "https://drive.google.com/uc?export=view&id=1gN_qUuH9FMsl6HGHQSRALKXFwq1J24sR",
            "https://drive.google.com/uc?export=view&id=12Crj1vQe-yaqJWCMtx5d6046RrfdQTNC",
            "https://drive.google.com/uc?export=view&id=1ecKrwEVYzD7xWvyTW-_kmhrXRjRbkGNC",
            "https://drive.google.com/uc?export=view&id=1CBnEhq1qdubFHZr_LARvaFhAk8fp-ilo",
            "https://drive.google.com/uc?export=view&id=1g64fcH8S1sY62JyY2yhUiwJ6mFr6FUQQ",
            "https://drive.google.com/uc?export=view&id=1kP2_T2LWtm4IoqO9y8MuVJgTUXPLsj2f",
            "https://drive.google.com/uc?export=view&id=1wRNglrO667pPqEgq1JN5Ha8A_IAcDihw",
            "https://drive.google.com/uc?export=view&id=1wEyAj-aG2k8OoV3mdF7vFySgl36TcB5X",
            "https://drive.google.com/uc?export=view&id=1_2M_pmeh11qG-8ExKByG22BfLkmHTELK",
            "https://drive.google.com/uc?export=view&id=1j_wABZRNEsCXSGIz4oo7J-uAkt5h-cQY",
            "https://drive.google.com/uc?export=view&id=1YEiQiV5_dwG_dZ0YbjsQ5YRZ1tP7fsXB",
            "https://drive.google.com/uc?export=view&id=1W31CeGRZXv7yaHzZZa-QpZYtV8Ekv_zo",
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










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
            "https://drive.google.com/uc?export=view&id=1xMvE_pLzylMrTdOXh__H67OBNLilsMt_",
            "https://drive.google.com/uc?export=view&id=1t01AaDDojMaVPbnx7SUiu3Jo33psbSfX",
            "https://drive.google.com/uc?export=view&id=1ChE0uFJps3Gq8uW4FDPQhBoyUtTkTWmp",
            "https://drive.google.com/uc?export=view&id=1y2GtPSrRCcOAuD58hsH37PNvAFG8koDT",
            "https://drive.google.com/uc?export=view&id=1aFfh9xze9uRxZvwcGM4NMfFASexNvxR3",
            "https://drive.google.com/uc?export=view&id=1uKJQjEj9LP8zXuwymksXGKoXXnEdOMw5",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Kakak ini asik juga ramah dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "kakaknya keren dan berwibawa",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal": "Baduy Dalem",
                "alamat": "Agrest kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini lucu dan baik hati",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya kalem dan tenang",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik dan ramah",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Cutek kahim",
                "sosmed": "@farahanumafifaj",
                "kesan": "Kakak ini asik dan ramah",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17uqEuVjfA461-rZ7mt06nT6nDpzkURvO",#1
            "https://drive.google.com/uc?export=view&id=1Kb_uZtko2y0AEuQEPFhsMGpIetX8tPrZ",#2
            "https://drive.google.com/uc?export=view&id=1r6ybX9tZQkMDiOAndxrFZJYPBj28bfoQ",#3
            "https://drive.google.com/uc?export=view&id=1Yxk88Ed1D6c41zsw4hUZggdWXU5vRTWL",#4
            "https://drive.google.com/uc?export=view&id=1TeV4yyD1t0fIUeq5XPc0t3nS1BjsaIbP",#5
            "https://drive.google.com/uc?export=view&id=1Tol2zD49TgIPLcfGaAi--LdhiP1zdjnt",#6
            "https://drive.google.com/uc?export=view&id=13iwCDdSJhuDz5Px1gRyjUeBEoXfJOnTv",#7
            "https://drive.google.com/uc?export=view&id=1I86LE4ZPcRvFpSyRJkANCPU9RTJNgBai",#8
            "https://drive.google.com/uc?export=view&id=1_gYz_dKfxXWGwfwnsbaPKzqQxGryW03I",#9
            "https://drive.google.com/uc?export=view&id=1IofieIE0bmUQ9pKuMqmXR_Rue0v2wKbd",#10
            "https://drive.google.com/uc?export=view&id=1T4vhkntx5H0UYevDhHindfqiRo3708At",#11
            "https://drive.google.com/uc?export=view&id=1i1rFxmCOC8kI1D848U0ivYZKKnUpUHwr",#12
            "https://drive.google.com/uc?export=view&id=1nC26N2Ot5561b8l9xdut3NAQ5tZuUNfK",#13
            "https://drive.google.com/uc?export=view&id=1UC8oQd_pixTrb6NcoyQjQcXluVJIOm9P",#14
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Lapas,Belwis",
                "hobbi": "Zumba di pln setiap pagi",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Mojokerto",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan pancing",
                "sosmed": "@ranishapg",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini menarik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Kakak ini asik dan aktif",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini lucu dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078 ",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main padel",
                "sosmed": "@givarooo",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "12245065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini lucu dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini lucu dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=136IUapnrHa1QLJHSwCWIeo50o3RcwdIp",
            "https://drive.google.com/uc?export=view&id=1uZNcipAknrldg__dyrgO4EmGclopr8mg",
            "https://drive.google.com/uc?export=view&id=1CCH6IHZdo5Kt-5qhaoNF6HiLVmvpUKTV",
            "https://drive.google.com/uc?export=view&id=1ToZUuWPNWhcQq59WkQO5aNZ2EgX62K8w",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "tanya caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@nadyaajani",
                "kesan": "Kakak ini ramah dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Like Instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini orang yang rajin dan produktif",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik dan kalem",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DNZchaQyT_pZB6UaPRKakRwp3hvUNpAi",#1
            "https://drive.google.com/uc?export=view&id=1CQCScAosYO6Hcx7WQ5xugJMeX_GRmkFX",#2
            "https://drive.google.com/uc?export=view&id=1mOq2MUgK8zkrgZTSH6DSBVWrpaJM-YRa",#3
            "https://drive.google.com/uc?export=view&id=1Jx-AltKcfXZvYHgm7JyEG7Rt4n9hf1V4",#4
            "https://drive.google.com/uc?export=view&id=1eFyNNyW79aJqTAemt8noIWtK62lEc7LT",#5
            "https://drive.google.com/uc?export=view&id=1eFyNNyW79aJqTAemt8noIWtK62lEc7LT",#6
            "https://drive.google.com/uc?export=view&id=16rvEtU1b3BOCn4WCkRiy5WOMP-m5FfHY",#7
            "https://drive.google.com/uc?export=view&id=1N2nVOsHnfquecf8PczUFtaKrLkvT4ndh",#8
            "https://drive.google.com/uc?export=view&id=1DQNkX8ThW7zg1lcS6VM8RHjdkH5enfi7",#8
            "https://drive.google.com/uc?export=view&id=1e9xdqLgW9Tqz351Zcxgyriv41A6lzqSW",#9
            "https://drive.google.com/uc?export=view&id=1TfLtfV9HnIU_HhcPyb9dTNBL4xj7DxyL",#10
            "https://drive.google.com/uc?export=view&id=1qPCx7XYhyvtwNqeLO3EDpbGzBlY9yUw0",#11
            "https://drive.google.com/uc?export=view&id=1G_7j_f6noBu03igEWZu-n8qGA2AHmi8Y",#12
            "https://drive.google.com/uc?export=view&id=1NQnkigmkZWpToeeh-7JhVLb6EG1zkACF",#13
            "https://drive.google.com/uc?export=view&id=1Mz5Y8kj3wIjHFE8qfK0oGumxzPduOhGw",#14
            "https://drive.google.com/uc?export=view&id=1o416xG7Wn0i-XBfnbNizzBn3j3m2QLFW",#15
            "https://drive.google.com/uc?export=view&id=1NXL4gre4-s2ad9bLADpcr6dfyyPtNaOX",#16
            "https://drive.google.com/uc?export=view&id=1OqSaI--RUKzz2vZ5ctfCh-A73L5AUXwF",#17
            "https://drive.google.com/uc?export=view&id=1GkhT2gGvXVt9XGEdKPZb7-6hefMDmyXy",#18
            "https://drive.google.com/uc?export=view&id=1Ggt6CpinaA1G_QZoJBzDCHqPPTOKrqQt",#19
            "https://drive.google.com/uc?export=view&id=1c6APLNbcunMsoWLaLziDoS7c3doIO8n4",#20
            "https://drive.google.com/uc?export=view&id=1UQ5sXLnF5U6uy47dxSIpNFQ3sFW0vRVQ",#21
            "https://drive.google.com/uc?export=view&id=12km0nj9023D0v0ojrWnpzcR-IykCevC2",#22
            "https://drive.google.com/uc?export=view&id=1K6L9sagqUSY6lxWKevAOWQU4J-3wlaGV",#24 
            "https://drive.google.com/uc?export=view&id=1hMRtFB2ybZtEP-A_yX9k0K-QoiaRSBsG",#25 
            "https://drive.google.com/uc?export=view&id=15py_9C6BujUwYD2l6wzaiA8n0m7xoMWg",#26 

        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@ferdy_kevin",
                "kesan": "keren dan berwibawa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Parwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Kontrakan GH",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Kakak ini gacor banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Kost Orange",
                "hobbi": "Ngekader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakak ini ramah dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak Arienta",
                "hobbi": "mengajarkan Hnery berfikir kritis",
                "sosmed": "@daffahdynn_",
                "kesan": "Kakak ini asik dan keren",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main Game",
                "sosmed": "@ginda_mrp",
                "kesan": "Kakak ini baik dan keren",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "kost putri gerbang barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Kakak ini pintar dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "vany salsabila putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabila",
                "kesan": "Kakak ini baik dan cantik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22__",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "122450088",
                "umur": "20",
                "asal":"Jabung,Lampung Timur",
                "alamat": "Nangja 4",
                "hobbi": "Main game",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakak ini baik dan sopan",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Daadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini lucu dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450079",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "1222450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nontonin anak tari latihan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.Lapas Raya No.55",
                "hobbi": "Ngoleksi Pita Pink",
                "sosmed": "@d_aniar",
                "kesan": "Kakak ini lucu dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Joki Strava",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "12345109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Terjun Payung",
                "sosmed": "@kevinaj__",
                "kesan": "Kakak ini baik dan asik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton anak tari perform",
                "sosmed": "@m.ridwan_22",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Gg.sakum",
                "hobbi": "Ngoding",
                "sosmed": "@liano.wlm",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl.Ratu",
                "hobbi": "Nonton Anime",
                "sosmed": "@rewinanaa",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ofULSYaJ5uDARoqAzX2skuojuItG1jje",#1
            "https://drive.google.com/uc?export=view&id=18Mu0huTMX-1ExoYls_VlkElJYwoFb12U",#2
            "https://drive.google.com/uc?export=view&id=1T5m77aDduYFgRmJOJxzwQqT_XwwQhsiJ",#3
            "https://drive.google.com/uc?export=view&id=1UStg1iCneXp8EVxktYl9R5Rm5RVqyeeE",#4
            "https://drive.google.com/uc?export=view&id=1Mxw8qDkgbU61tgyejigSVsJ7Q-gbxKHE",#5
            "https://drive.google.com/uc?export=view&id=1UERFA1hGPmf1Ixq9APeEPnMJac-FIWB6",#6
            "https://drive.google.com/uc?export=view&id=1-cCG7JfN8uRCovaRIsQOrQAHvCOsMTRP",#7
            "https://drive.google.com/uc?export=view&id=1crVpsWitdlTA6iJvLSG_iUGy7d0pTtP4",#8
            "https://drive.google.com/uc?export=view&id=1Vdq0px48oOpnVnbvLPr8KafE4VDYs8Ah",#9
            "https://drive.google.com/uc?export=view&id=1u2IMCW4uCmO44s8xZ64Sz8VOcWjdaYGM",#10
            "https://drive.google.com/uc?export=view&id=1jaHAgR-Klw84ix6cUXr2OGsDVa0qFuo4",#11
            "https://drive.google.com/uc?export=view&id=1ZN6B8rNGUJLUnO_GD09L4Rfow99fmkEk",#12
            "https://drive.google.com/uc?export=view&id=1HfaLy-k9s7GqKXZ77ef50fEt9SOeF6N2",#13
            "https://drive.google.com/uc?export=view&id=1mulqlN0ALtMrbHRPhCxL0Xv0PWlUGhGC",#14
            "https://drive.google.com/uc?export=view&id=1n_d5ORI-7izxSBysNxaowRHWK0EODzUb",#15
            "https://drive.google.com/uc?export=view&id=1-cCG7JfN8uRCovaRIsQOrQAHvCOsMTRP",#16
            "https://drive.google.com/uc?export=view&id=1hDSykGCA9-2gFRWnzjKsTNxGuCEaHYkp",#17
            "https://drive.google.com/uc?export=view&id=1kBckMXvwkAEVlH33oTDhmD2CoTloO13y",#18
            "https://drive.google.com/uc?export=view&id=1OME1GaPP52N6P1vWmKbteUPeMgwgvebB",#19
            "https://drive.google.com/uc?export=view&id=1oxHWBCD5gR9AwAY3-TZIRaj4QmNXfwNb",#20
            "https://drive.google.com/uc?export=view&id=1ltDKfzUihoHVI6pkgvDsXMriyqmUOtjd",#21
            "https://drive.google.com/uc?export=view&id=1_iAFMN9Ei0BN8VizLTN1fOMDCHQU2Lnq",#22
            
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang,Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl.Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artike",
                "sosmed": "@junitaa.0406",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander ",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl.Nangka 3",
                "hobbi":"Main Bass,piano",
                "sosmed": "@merletacornelia",
                "kesan": "Kakak ini ramah dan lucu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keyashafi",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari,Natar",
                "hobbi": "Dengerin Musik,Dance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakaknya asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl.manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl.Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Fore",
                "hobbi": "segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Kakak ini asik dan menyenangkan",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Razin Hamid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakak ini asik dan keren",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan jalanmain game",
                "sosmed": "@biokcb",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl.Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktavia",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini baik dan asik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl.Lapas,Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishahi",
                "kesan": "Kakak ini lucu dan asik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Hasan IV ,Airan",
                "hobbi": "Isengin Orang",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muahammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "Kakaknya asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "1224450118",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "TIdur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1egy4M8zmr1T0XacgiIxM_oY9FplOyXC0",#1
            "https://drive.google.com/uc?export=view&id=1CTkygyvdnCQfagWtRZA5ecdQn_06hcsR",#2
            "https://drive.google.com/uc?export=view&id=195NxIN4DfRVaQtCMQRo7yHGYmK7B7Ui_",#3
            "https://drive.google.com/uc?export=view&id=1uWtmozT70pwej4vAhR7RM1w_Xt5WCEYt",#4
            "https://drive.google.com/uc?export=view&id=1rr_a7ZmqAOlqBkAOKDP84_79fMwbYk-P",#5
            "https://drive.google.com/uc?export=view&id=1A9zkRAmksKOMSLUzd9-nCIavyHEJ7fla",#6
            "https://drive.google.com/uc?export=view&id=1wROiyYgic50Om8g6ApvRSCgJ8_X2WqKp",#7
            "https://drive.google.com/uc?export=view&id=1ck5rnmvgPxXHW6f3HdP2lpSonnOBFlBv",#8
            "https://drive.google.com/uc?export=view&id=162bCDjyMvkw62gAEW_vrIvmwVxpKgz52",#9
            "https://drive.google.com/uc?export=view&id=1_OaAJasddT2bHN9lzXLBA4BTfh8Y8Xe8",#10
            "https://drive.google.com/uc?export=view&id=1pwPh-XenMt4G9Du0lzqnh9jLbnFS3M0U",#11
            "https://drive.google.com/uc?export=view&id=1fbwecmxUeQaNFQPyFlMcS1e6d3P9pKWx",#12
            "https://drive.google.com/uc?export=view&id=1eu9IiMGFN2_H_mEEccDD5Ks7x_4SKdmu",#13
            "https://drive.google.com/uc?export=view&id=1a7e-X0Af_iaMIRS5AtJbt1uiKHgbHl1n",#14
            "https://drive.google.com/uc?export=view&id=1zNoMAbRzAkRWsVmG_afhmr4CyMsVSuDk",#15
            "https://drive.google.com/uc?export=view&id=1tCd3XsMxn8AhmLEoLx1FuBFbVb8C0bYU",#16
            "https://drive.google.com/uc?export=view&id=1ww8YIx9r-RNWWxtXuNHpBCTc2ujWTtRi",#17
            "https://drive.google.com/uc?export=view&id=1n5QKhy3lwZ6fSJiXrvw061biezebDFzO",#18
            "https://drive.google.com/uc?export=view&id=1NOIYNG9ub9GuB5bgVNZdbdLdhnuCrcp2",#19
            "https://drive.google.com/uc?export=view&id=1tItmNvMOp_bp3IKtAiq7VDjK0XoLSbAA",#20
            "https://drive.google.com/uc?export=view&id=1qSEMrX-AMed3ehVgesg2BqgNOloNsOz5",#21
            "https://drive.google.com/uc?export=view&id=1aycaJuCAlqhGMIXP8_l5NabVEx178pQQ",#22
            "https://drive.google.com/uc?export=view&id=1BhUyMKljIWxh_NIHJmwfOaVnsm_J-_M2",#23
            "https://drive.google.com/uc?export=view&id=1S6idHbviknV4lheTUhM_IagWT0BFde9s",#24
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
                "kesan": "Abangnya baik dan ramah ",  
                "pesan":"Semangat terus kuliahnya bangg"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini baik dan ramah banget",  
                "pesan":"Sehat selalu kak"# 2
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini keren dan ramah",  
                "pesan":"Semoga lulus tepat waktu kakk "# 3
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak ini keren dan aktif ",  
                "pesan":"Semangat terus ngaspraknya kakk "# 4
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakak ini lucu dan baik ",  
                "pesan":"Semangat terus kuliahnya kakkk "# 5
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakak ini keren abiss ",  
                "pesan":"Semangat terus kakk "# 6
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abang ini baik dan ramah banget ",  
                "pesan":"Semangat terus kuliahnya abang awak "# 7
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya baik dan ramah ",  
                "pesan":"Semangat trus kakk "# 8
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang ini kerenn ",  
                "pesan":"Semangat terus kuliahnya bangg "# 9
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "Kakak ini baik dan ramah ",  
                "pesan":"Semangat kuliah dan berorganisasi kakk "# 10
            },
            {
                "nama": "khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakak ini baik dan ramah ",  
                "pesan":"Semangat kuliahnya kak "# 11
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakak ini baik dan asik ",  
                "pesan":"Semangat terus kak "# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang ini keren dan ramah ",  
                "pesan":"Sehat selalu abangkuu "# 13
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak ini asik juga ",  
                "pesan":"Semangat terus kakkk "# 14
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakak ini lucu dan asik ",  
                "pesan":"Semangat kuliahnya kakk "# 15
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abang ini asik dan baik ",  
                "pesan":"Semangat terus bang "# 16
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakak ini ramah dan baik ",  
                "pesan":"Semangat terus kak "# 17
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini baik dan asik ",  
                "pesan":"Semangat kuliahnya kakk "# 18
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakak ini asik dan baik ",  
                "pesan":"Sehat terus yaa kakk "# 19
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abang ini baik dan ramah ",  
                "pesan":"Semangat menjalani hidup bang"# 20
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini baik dan pintar ",  
                "pesan":"Semangat terus kakk "# 21
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abang ini asik dan ramah ",  
                "pesan":"Semangat terus bang "# 22
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakak ini baik juga ",  
                "pesan":"Semangat kuliahnya kak "# 23
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini baik dan ramah ",  
                "pesan":"Semangat terus kakk "# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1H8619V4M2oXssboyO1X0uFvkPXVuVxXn", #1
            "https://drive.google.com/uc?export=view&id=1afl50CwCqO5fT5QIY1p7idgk_4mD2YY_", #2
            "https://drive.google.com/uc?export=view&id=1WnNAMFzAxy0QTffh2nxCBCAMEfojLaNZ", #3
            "https://drive.google.com/uc?export=view&id=1nBd9eZr8M-hRFUFBDKnoeVflQqjHdjal", #4
            "https://drive.google.com/uc?export=view&id=1SR1bCy-iJloMPXb11M8XlgfIhaLPqE89", #5
            "https://drive.google.com/uc?export=view&id=1-wBuOzDzz1eMwerhcX0V3NbuFYi4nCds", #6
            "https://drive.google.com/uc?export=view&id=14OKwwwyUMol90WoCFqmGs46T8Vk9LPeB", #7
            "https://drive.google.com/uc?export=view&id=1HW4PjEfsm4LDJfHch-ppHaImYePpvxUm", #8
            "https://drive.google.com/uc?export=view&id=1xh5r-0isx8NECJgNm3ySmQB8R69wY4JC", #9
            "https://drive.google.com/uc?export=view&id=1PnYg9a0voPLP5Y-IbXXjF3WviXLQnYwg", #10
            "https://drive.google.com/uc?export=view&id=1YEQiP76IP8Js9bLP8H4bzJj-QAzb0f1F", #11
            "https://drive.google.com/uc?export=view&id=1nMIm1x3NSVbYBw7m-8cLDRaIqv1Df2oO", #12
            "https://drive.google.com/uc?export=view&id=1ML7LIgf8P_QHop-zBx4NoxcAeP_909bh", #13
            "https://drive.google.com/uc?export=view&id=1ghkZVhNxfPFyoHhpm2Vp78x2x9XlMiuA", #14
            "https://drive.google.com/uc?export=view&id=1SHK-JVnIgLvebcxImJfPrD73kmz_oH7a", #15
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
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": " ",  
                "pesan":" "# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": " ",  
                "pesan":" "# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": " ",  
                "pesan":" "# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": " ",  
                "pesan":" "# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": " ",  
                "pesan":" "# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": " ",  
                "pesan":" "# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": " ",  
                "pesan":" "# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": " ",  
                "pesan":" "# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": " ",  
                "pesan":" "# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": " ",  
                "pesan":" "# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": " ",  
                "pesan":" "# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": " ",  
                "pesan":" "# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": " ",  
                "pesan":" "# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": " ",  
                "pesan":" "# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15JgBCKrG6Uup4GaRdomRPosKoAv49Zdz",
            "https://drive.google.com/uc?export=view&id=1Oa7wPqbgz7F9BOQ7XYe5tLXYmg97fzKQ",
            "https://drive.google.com/uc?export=view&id=1Us4CmTu-7sf3YUo5NB2bfAkA4ommHlB8",
            "https://drive.google.com/uc?export=view&id=1negaGw7a8Yphvc2yQI1jOwx95gq_JgTd",
            "https://drive.google.com/uc?export=view&id=1571U3VJamdpW3I3Puv9I2p2CLU6YXNPH",
            "https://drive.google.com/uc?export=view&id=1RNmZXYJs5oCnVW5wd7YndIsAR5Lt5KEI",
            "https://drive.google.com/uc?export=view&id=yuT5hdIgA1WaQZNTz6MhWrSCchPIP7o-",
            "https://drive.google.com/uc?export=view&id=153m9qtomhFmBnXTR0emr2s27p-uAhpHU",
            "https://drive.google.com/uc?export=view&id=10srcQHkdmGCJSFG9D-DQLpGW9a7tuaeq",
            "https://drive.google.com/uc?export=view&id=1XcWeBLEQ6aVFt8OcVjc6qudps9GZlkl3",
            "https://drive.google.com/uc?export=view&id=1T-epWpxcH4JZY3OiFKhCOpF09oNz880r",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "  ",  
                "pesan": "  "# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "  ",  
                "pesan": "  "# 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "  ",  
                "pesan": "  "# 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "  ",  
                "pesan": " "# 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": " ",  
                "pesan": " "# 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "  ",  
                "pesan":"    "# 6
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "  ",  
                "pesan": " "# 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "  ",  
                "pesan": "  "# 8
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": " ",  
                "pesan": " "# 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": " ",  
                "pesan": " "# 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": " ",  
                "pesan": " "# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zk_RbW1NZbgzwHBnfs2zPCV-d9tBctfE",
            "https://drive.google.com/uc?export=view&id=1bL7oA-cFhLnwlXbAe9mUUX1xaG2NuyrL",
            "https://drive.google.com/uc?export=view&id=19WG8zkYwzttFX7ICpwwJ8ZGT_7_pLUnl",
            "https://drive.google.com/uc?export=view&id=1hZ2323GbL03ZTvDUvZRHnV5Jkmm9HVSD",
            "https://drive.google.com/uc?export=view&id=1bbFOx04LRnkEDy-2aiwdxPzn_SNP-Q0E",
            "https://drive.google.com/uc?export=view&id=1gcyuEhMc0XCQ8ozrjMUmCxnDGCW1JAQt",
            "https://drive.google.com/uc?export=view&id=17VuJ6jbReD8QkRSZrayOKn6J7bGIko7Z",
            "https://drive.google.com/uc?export=view&id=1pRZ3AAC6mQCNXxQBD3X_8nqnIiczPtfK",
            "https://drive.google.com/uc?export=view&id=1NHBklhJVWj2zkihQiyce5Yedbgmaq2AT",
            "https://drive.google.com/uc?export=view&id=1ssMJpVWJwpOZa4XOn_INsa2XG6wV4PlT",
            "https://drive.google.com/uc?export=view&id=1PcCFq3w8Cm5pkUBc5b-lRejgeoIdbIq7",
            "https://drive.google.com/uc?export=view&id=16wAlxhCluFJKLznAiGoCL5ovfUFTPO2g",
            "https://drive.google.com/uc?export=view&id=1GmusQlgVqqbnnhXgikcNFe9Jq6BSPMXW",
            "https://drive.google.com/uc?export=view&id=1k8yX_PQU2UHljPTTKOC00UHwVgxB3A_Y",
            "https://drive.google.com/uc?export=view&id=1CEpmcQRbWMt06CO0qKXzY8ASq6Qr2_aI",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1ArBWL786glsmIDhFK0wkk1c839oZKYsp",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "",  
                "pesan": ""# 1
             },
             {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "",  
                "pesan": ""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


# Tambahkan menu lainnya sesuai kebutuhan



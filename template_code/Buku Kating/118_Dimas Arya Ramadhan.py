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
            "https://drive.google.com/uc?export=view&id=1QjZQ8Jpktnr3A_yODp677gOQizoU4kXX",
            "https://drive.google.com/uc?export=view&id=1PN_-OJtGFpi9nK-GkjPjTz4rQIv3u-AH",
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
            "https://drive.google.com/uc?export=view&id=",#3
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
                "hobbi": "Jalan pancing",
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
            "https://drive.google.com/uc?export=view&id=1K6L9sagqUSY6lxWKevAOWQU4J-3wlaGV",#24 bang benget
            "https://drive.google.com/uc?export=view&id=1hMRtFB2ybZtEP-A_yX9k0K-QoiaRSBsG",#25 bang uliano
            "https://drive.google.com/uc?export=view&id=15py_9C6BujUwYD2l6wzaiA8n0m7xoMWg",#26 kak rewina

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
            "https://drive.google.com/uc?export=view&id=1gSYkrxPmG-xs0HAlK-TUoWuOizMnwTVQ",
            "https://drive.google.com/uc?export=view&id=1frAjl8bEEdFBovycir7eaKk0-gSKkof_",
            "https://drive.google.com/uc?export=view&id=14b6YL1hihi05GM8dv0fvimZ7bMGvuAFP",
            "https://drive.google.com/uc?export=view&id=1evKwlESkMjSaeSUODpI8YsHJp95EuAJX",
            "https://drive.google.com/uc?export=view&id=1ik2yqMvpnbbDIJRh2MybsbEcngJr52ra",
            "https://drive.google.com/uc?export=view&id=15Zh5X9Hi0aI68Zi95UwP6QnfHedaR9hD",
            "https://drive.google.com/uc?export=view&id=1lpXwk9ivPl3rIa7r26IwXM7o_a6mjoPE",
            "https://drive.google.com/uc?export=view&id=1ZngTckxRwkWcUycToZcnzBiaNj7OeM9Z",
            "https://drive.google.com/uc?export=view&id=16WgmAzCcrxfLONhnW64NLOIdOT8V2XYN",
            "https://drive.google.com/uc?export=view&id=167sSYVQjQAAegFdvdBRtpWyXaN2Ewis",
            "https://drive.google.com/uc?export=view&id=1WEhLKDq5uOEJYXV6CuzZRcA61bbJeWVo",
            "https://drive.google.com/uc?export=view&id=1pgfT9qwwxUvgdDmaZx9BVVKXhAHa1Sf7",
            "https://drive.google.com/uc?export=view&id=1y2qMqAsmhJXsEjzYuk9w49Y0Sz4c4BF2",
            "https://drive.google.com/uc?export=view&id=1HW73JV00NPjN1jMgjv_trjPUxT1E_VAb",
            "https://drive.google.com/uc?export=view&id=10-V-21q-aRQ5W7odvtT9vonbLCaHHpvI",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17dddvI3xPAd8NXG6ykfbRn60-zuHbmV2",
            "https://drive.google.com/uc?export=view&id=13DhBwONB40QqRjsPy2gijhZasUfnRScs",
            "https://drive.google.com/uc?export=view&id=1Z-Gsosi9PCV-YYMlRXxEkgrpALQbOnuW",
            "https://drive.google.com/uc?export=view&id=16A99-avAX8lotrrh6XjsOZLmDP0RkoGM",
            "https://drive.google.com/uc?export=view&id=1_U-zd2iy8xoH9l3_34QL7MDGA3SOB8zy",
            "https://drive.google.com/uc?export=view&id=1PynEKmKiz6bRwpSK-29aq1I9K1QhHtZA",
            "https://drive.google.com/uc?export=view&id=1xA1DMrXMoIIjV0HczaT90PTL16zRNOl7",
            "https://drive.google.com/uc?export=view&id=1e7rbR6wHeMXP6fYtT1pSWcvdo71-QEYh",
            "https://drive.google.com/uc?export=view&id=1IL3Tn49YNH7oWu_liDcOa1LZPIJ1p94J",
            "https://drive.google.com/uc?export=view&id=1LY123azxldzhmA0-8RJV6J_RdxZ0CT3M",
            "https://drive.google.com/uc?export=view&id=1Su7Ip1y5istQY5CxxYQSakxJ3_niANTl",
            "https://drive.google.com/uc?export=view&id=1i2gH6IQx7xR0tWT1djVtKXBARDOHoLL4",
            "https://drive.google.com/uc?export=view&id=1ZIr-ns0hbYxpXC7noJlsN44QJ2ewW5f3",
            "https://drive.google.com/uc?export=view&id=1LbHU6zB_iw7bPVI3IMyRism0xONWNQJM",
            "https://drive.google.com/uc?export=view&id=1b2qmvDQehY6tC5ro3mLXUx5-COVDUxsG",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QBofuizBMIDilRZhxwa8XOT2AC8X5HM5",
            "https://drive.google.com/uc?export=view&id=1PoS8k0JsZvbri9l0Yt2T4OiQKjVdODLx",
            "https://drive.google.com/uc?export=view&id=1jGP6MMdzQ9_vu7c7fiQalsLJsU9qWwcT",
            "https://drive.google.com/uc?export=view&id=1s731J1qE689sO3iTAIxc3xm3ArXt4FRU",
            "https://drive.google.com/uc?export=view&id=1xZjkql4YHDxqV-6kOuReK-py3qcFAxtm",
            "https://drive.google.com/uc?export=view&id=13ObdS5lUXShQ-TIvugdA88JNXtI7m0Ny",
            "https://drive.google.com/uc?export=view&id=1CVi8BgqfKEqtt_eM__uwdXij947ggZdV",
            "https://drive.google.com/uc?export=view&id=1-cpqNbRABqdmSEKr4fozQqQ9ya7-M8u9",
            "https://drive.google.com/uc?export=view&id=1dTaaGPPTxqbQqck2x5nSTNEoX5e1NqiQ",
            "https://drive.google.com/uc?export=view&id=1Yg4nAsK5RTBwPy9yjS5vgyEoIyjjjsbE",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()
elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pZ86rav6B7u5r0EMww6c5vZCOsObPe0Q",
            "https://drive.google.com/uc?export=view&id=1Gis3pvtPkdN4weHiRjs29he8F4M0XxYl",
            "https://drive.google.com/uc?export=view&id=1IqRlXMABmg5OV31NyY0kBJcFuE8BANLM",
            "https://drive.google.com/uc?export=view&id=1z7dIV5sXhCszKMIzLdGvbvLTjcj4z05U",
            "https://drive.google.com/uc?export=view&id=1XMTxHe2mRXEaLVWLVdN6hL3YRHPIiF7R",
            "https://drive.google.com/uc?export=view&id=11H8ZHFs3qzfen0sr1uCT_FNmL-QtcO9a",
            "https://drive.google.com/uc?export=view&id=19bKBw01Po6i6Mh2qBeuusbK7av-gsrLn",
            "https://drive.google.com/uc?export=view&id=1nfoTqp6LnvtMkdXZk4J9Q5ueFiKs0l3v",
            "https://drive.google.com/uc?export=view&id=1sJKYFQXvVpWmWLZT5gMt5TvSTplwnlsr",
            "https://drive.google.com/uc?export=view&id=1PdRadHuoNBTRYrgOB6XgyAkMM3nx_KKF",
            "https://drive.google.com/uc?export=view&id=1Vz4SF07jNikYsZ7fInLWS-IxUTaFuZ9T",
            "https://drive.google.com/uc?export=view&id=1M7MeLZZ8L3wTEy63S8p-ZWqLuvB0eoWb",
            "https://drive.google.com/uc?export=view&id=1kkk2nilDCOQu0IyKYOyXKzr2DffGUnak",
            "https://drive.google.com/uc?export=view&id=1IMJ75kwBge9_qSAp_QeNN-Sr1jl8qtfF",
            "https://drive.google.com/uc?export=view&id=1KWEUbWUMFxjLA5TiBOwTI52d5cPSbSqu",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan


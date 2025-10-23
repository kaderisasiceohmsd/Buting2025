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
            "https://drive.google.com/uc?export=view&id=1FktNS1m8zAfS2k8JJUEk0pSgluNEyXCN",#1
            "https://drive.google.com/uc?export=view&id=1TC5Fv2Vzllak4_NalsXwz4NwhYeHMTgi",#2
            "https://drive.google.com/uc?export=view&id=1jTLlSxEJA4XH7YMNewVu5Y3mnAUGyNWC",#3
            "https://drive.google.com/uc?export=view&id=16TrLGi4VZnHV-tfOVqzIavsB-7L78KMB",#4
            "https://drive.google.com/uc?export=view&id=1DjbHDuOL35F9ty0e6rtNGPNSVq2x9B8h",#5
            "https://drive.google.com/uc?export=view&id=1Ai8bDqNqewnQ7gMdyuiEJtnCvlsoYLFa",#6
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Abangnya tegas tapi asik",  
                "pesan":"Tetap jadi orang baik ya bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "baca buku (dasar-dasar sql)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya asik",  
                "pesan":"Semangat kuliahnya bang"# 2
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Airest Kost",
                "hobbi": "siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakaknya cantik dan asik",  
                "pesan":"semangat terus kuliahnya kakak"# 3
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya asik bangett ",  
                "pesan":"semangat terus kuliahnya kakak"# 4
            },
            {
                "nama": "Eksanty F. Sukma Islamiatyr",
                "nim": "12245001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "rajabasa",
                "hobbi": "baca buku , saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya asik bangett ",  
                "pesan":"semangat terus kuliahnya kakak"# 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"kota Padang,Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya asik bangett ",  
                "pesan":"semangat terus kuliahnya kakak"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sEveMhR9JLbojUrhpTV08vOtV0rzTM4z",#1
            "https://drive.google.com/uc?export=view&id=1ANE-irHdoUE8_cX8kbgqFx9AYpQSq_Rn",#2
            "https://drive.google.com/uc?export=view&id=1lYvA98xTF83eW-tcVVszf89hXbdkuvOY",#3
            "https://drive.google.com/uc?export=view&id=1BOrmo3HD6egFVvYhLOG9dtnmW6vqTv_C",#4
            "https://drive.google.com/uc?export=view&id=16SR63IWa_hGAIs7GfSAftlKa4VIDWLSO",#5
            "https://drive.google.com/uc?export=view&id=1SbSfGirx-QzknL0QvsraR3lTtSQYboUd",#6
            "https://drive.google.com/uc?export=view&id=15ysWTmwn9eXb5GG7Yv1XRxTYRwCCBf2Z",#7
            "https://drive.google.com/uc?export=view&id=1iys9ruH5SQ2p7rxl93q9_5NRhhWFm9cR",#8
            "https://drive.google.com/uc?export=view&id=1drmDu49ht1IfI6bTNKf9y0HYFdveDDbZ",#9
            "https://drive.google.com/uc?export=view&id=1t4Nq-X39ZPbIAidGVgZolVznOAG-Kz5G",#10
            "https://drive.google.com/uc?export=view&id=192NIRn3Pxfsgyzzdh_rd2Aa5A6K-iGP5",#11
            "https://drive.google.com/uc?export=view&id=17_wkr6GMIT_eX9K2cmk-5rhO6hcpqYug",#12
            "https://drive.google.com/uc?export=view&id=1Y3IaSYu4Dq7G4YTYB5k6Qx1Ex42MMhlP",#13
            "https://drive.google.com/uc?export=view&id=1tyUMbiUtRmrGoekeoiwoKk7SJjgcIZlz",#14
            
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "nonton orang kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "banyak dapet motivasi dari abangnya",  
                "pesan":"Semoga makin sukses dan terus berkembang!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "lomba ga makan keerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya asik dan auranya positive banget",  
                "pesan":"Semoga selalu dimudahkan dalam urusannya"#2
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya humble dan sopan.",  
                "pesan":"Semoga selalu dilancarkan kegiatannya"#3
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya cantik ",  
                "pesan":"semangat terus kuliahnya kakak"#4
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "abangnya cool dan berwibawa.",  
                "pesan":"Semoga sukses selalu bang"#5
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya cantik",  
                "pesan":"Semoga selalu dilancarkan kegiatannya!"#6
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi,Lampung",
                "hobbi": "dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "abangnya asik banget",  
                "pesan":"semangat kuliahnya bang"#7
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "abangnya punya pembawaan yang tenang.",  
                "pesan":"Semangat kuliahnya bang"#8
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya lucu banget",  
                "pesan":"Semoga selalu semangat dan penuh keberkahan"#9
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya menyenangkan",  
                "pesan":"Semoga terus berkembang dan berprestasi"#10
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Mainn paddle",
                "sosmed": "@iamridhomanik",
                "kesan": "abangnya punya semangat positif yang keren",  
                "pesan":"Semangat kuliahnya bang"#11
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi batch google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya menyenangkan",  
                "pesan":"Semoga selalu bahagia dan sukses ke depannya"#12
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera utara",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya cantik",  
                "pesan":"semangat terus kuliahnya kakak!"#13
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya asik",  
                "pesan":"Semangat kuliahnya kak"#14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    def Senator():
            gambar_urls = [
                "https://drive.google.com/uc?export=view&id=18NbwYvv1-qU1mNgK2B6wEs2xl-40voPj",#1
                "https://drive.google.com/uc?export=view&id=1vq295exl9ra_rqkIdvYzZroNSXZp4Mq0",#2
                "https://drive.google.com/uc?export=view&id=1HxW0e05Wds9CfLP_gNJ2WDB_G_lK7V_C",#3
                "https://drive.google.com/uc?export=view&id=11IgIWHRUl-k5pxb79RjwsEs4f-S60zCQ",#4
            ]
            data_list = [
                {
                    "nama": "Rian Bintang Wijaya",
                    "nim": "122450094",
                    "umur": "20",
                    "asal":"Palembang",
                    "alamat": "Tanya caesar",
                    "hobbi": "padel",
                    "sosmed": "@bintangtwinkle",
                    "kesan": "Abangnya sangat menyenangkan",  
                    "pesan":"Semangat kuliahnya bang"# 1
                },
                {
                    "nama": "Nadya Ratu Anjani",
                    "nim": "123450089",
                    "umur": "20",
                    "asal":"Jakarta",
                    "alamat": "belakang indomaret belwis",
                    "hobbi": "Maen roblox",
                    "sosmed": "@nadyaanjaani",
                    "kesan": "Kakaknya asik",  
                    "pesan":"Semangat kuliahnya kak"#2
                },
                {
                    "nama": "Fathinah Nur Azizah",
                    "nim": "123450072",
                    "umur": "20",
                    "asal":"jakarta",
                    "alamat": "123450072",
                    "hobbi": "like instagram",
                    "sosmed": "@fathinahnazzh",
                    "kesan": "kakaknya sangat menyenangkan",  
                    "pesan":"Semangat kuliahnya kak"#3
                },
                {
                    "nama": "Lia Hana Ichisasmita",
                    "nim": "123450083",
                    "umur": "20",
                    "asal":"Bandar Lampung",
                    "alamat": "Sukarame",
                    "hobbi": "dengerin lagu",
                    "sosmed": "@lia.h_264",
                    "kesan": "Kakaknya asik",  
                    "pesan":"Semangat kuliahnya kak"#4
                },
            ]
            display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()










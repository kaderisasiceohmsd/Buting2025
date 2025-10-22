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
            "https://drive.google.com/uc?export=view&id=1u1LCtW3ON4m7k6fTGoF9mWMLLIFaJqVP",
            "https://drive.google.com/uc?export=view&id=1WOK2tNE9sRmAsyO-UOTObseBOwIZco7P",
            "https://drive.google.com/uc?export=view&id=1nECdc-7fYPK6criAUITGQw7QeU0lGivJ",
            "https://drive.google.com/uc?export=view&id=1eo5f-T-VG0rbJucdmgP8lD0hC1BvKI62",
            "https://drive.google.com/uc?export=view&id=1pKNUI6Ld4rq8u3ATu4N0F2g1p-xBvswF",
            "https://drive.google.com/uc?export=view&id=1fEDYHlo87ItpNZGIC-a3CzqbBKljCeIK",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "abangnya inspiratif dan berjiwa pemimpin",  
                "pesan":"Sukses terus, semoga selalu jadi panutan!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abang keren dan bijak banget",  
                "pesan":"Semoga makin sukses dan bahagia selalu!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy dalem",
                "alamat": "Airest Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh",
                "kesan": "Baik, humble, dan easy going banget",  
                "pesan":"Semoga semua hal baik terus ngikutin kakak!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Ramah dan selalu ngasih vibes positif",  
                "pesan":"Semoga ke depan makin banyak hal baik yang datang!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumbar",
                "alamat": "Gya Kost Korpri",
                "hobbi": "Cute Jenderal",
                "sosmed": "@farahanumafifah",
                "kesan": "",  
                "pesan":" "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15bQyOMnn7BkvLOAtWTZFv-YO0Ly9-aMU",
            "https://drive.google.com/uc?export=view&id=1sBRu5AhzijYBo-ZyIh0tW2KUpNWVhPIE",
            "https://drive.google.com/uc?export=view&id=1u2_f9SEozbR1MRURg6C3IPO8ttIt05SC",
            "https://drive.google.com/uc?export=view&id=1vumMvkXKPVv6ukvsxaIKKkLo70jTs5mH",
            "https://drive.google.com/uc?export=view&id=1lJ-4LgcegBvwsKc_gRKipvJO8NXiE1gl",
            "https://drive.google.com/uc?export=view&id=1Hky7SpONQihpldWS_HgUK-KaGoAj0TkN",
            "https://drive.google.com/uc?export=view&id=18OGc23l6YQvXMU6ctLWHgK8LusGu35ON",
            "https://drive.google.com/uc?export=view&id=1zs-5WHhKFekCeXi5FMGjskCv30sZcGoa",
            "https://drive.google.com/uc?export=view&id=1nCfDNITPiv10nIpe2uYGGL02_eSgjf7w",
            "https://drive.google.com/uc?export=view&id=1X02M5lOM6qGZCbc_F_fHT-fq0D1-X4V4",
            "https://drive.google.com/uc?export=view&id=1AFXvtRFJcOeuB0Y8weHP5RgyRB6YEuzC",
            "https://drive.google.com/uc?export=view&id=1EAq37k5aYI6lbZnyMUzTI9R8Rr_XmFPC",
            "https://drive.google.com/uc?export=view&id=1Pz0A36PN5hmFByqXyiOQdSCJauCvtQ3X",
            "https://drive.google.com/uc?export=view&id=16Oc1WR6j4ERRxnie6jdOF4_f7vzCItF1",    
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
                "kesan": "abangnya berwibawa dan bijak dalam bersikap",  
                "pesan":""# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "lomba ga makan keerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya punya aura positif banget",  
                "pesan":"Semoga selalu dimudahkan dalam urusannya"# 1
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
                "pesan":"Semoga selalu dilancarkan kegiatannya"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"Semoga makin sukses,bang!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya humble",  
                "pesan":"Semoga selalu dilancarkan kegiatannya!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi,Lampung",
                "hobbi": "dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "abangnya santai tapi tetap berwibawa",  
                "pesan":"semoga makin berkembang ke depannya"# 1
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
                "pesan":"Semoga selalu diberi kemudahan dan kebahagiaan"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya punya semangat positif yang keren",  
                "pesan":"Semoga selalu semangat dan penuh keberkahan"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya tenang dan menyenangkan",  
                "pesan":"Semoga terus berkembang dan berprestasi"# 1
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
                "pesan":"Semoga selalu semangat dan penuh keberkahan"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi batch google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya terlihat tegas dan berkomitmen",  
                "pesan":"Semoga selalu bahagia dan sukses ke depannya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya punya semangat positif yang keren",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Farakan",
                "hobbi": "nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya tenang dan menyenangkan",  
                "pesan":"Semoga terus berkembang dan berprestasi"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14-djonho4tkp3Lx_NbueIDWJV1KYqnCX",
            "https://drive.google.com/uc?export=view&id=14-YtZmQ_VedNsGq10sLZvbjjGwm6ryGD",
            "https://drive.google.com/uc?export=view&id=143aA6E_1El8r-KZpY0B1FT4knGFc7pZV",
            "https://drive.google.com/uc?export=view&id=146Ywf476AovBKEeD66ltbqLuh_34SIDF",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Dengar lagu, nyanyi, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kaget ternyata suara bang rendra persis kaya juicy luicy waktu FG",  
                "pesan":"Semoga semakin keren kedepannya bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Awal liat bang Jo kaya serem",  
                "pesan":"Sukses terus kedepannya bang"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main ice skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "Seru banget kak abet lucuu!",  
                "pesan":"Makasih udah jadi orang lucu kak!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomart Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya keliatan kalem tapi anggun banget!",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-gnj3FQFk31Hmpqlve4_DmqFCKnFQJgg",
            "https://drive.google.com/uc?export=view&id=1Yfby6hDhkuey46-FVOwqtXIfHxvkiPqp",
            "https://drive.google.com/uc?export=view&id=13i7hxQX9MQRPUzZ-dhwLXcqMdOxJoYxj",
            "https://drive.google.com/uc?export=view&id=1RA-H0YpKCn6cE_-JbIOod3WnsjVtacdR",
            "https://drive.google.com/uc?export=view&id=1NUcqF0rZbo4J17vV5UBkohHuRzV4m_xy",
            "https://drive.google.com/uc?export=view&id=1iovXsHAjokiQ8YOt-5zOIU8shK9GYgkp",
            "https://drive.google.com/uc?export=view&id=1QeccnbfhZfErKBLgjLbSc8mQSBgZydd9",
            "https://drive.google.com/uc?export=view&id=1sTk0TtX0g19Dmr0SOvv79BdQkYaL59l5",
            "https://drive.google.com/uc?export=view&id=1vIlegPkKrMPq7PhPn0VEBWNasgtnqceA",
            "https://drive.google.com/uc?export=view&id=1J1GaY7H-pOAonVS2ph6Fb5awx4nsg5Np",
            "https://drive.google.com/uc?export=view&id=1vIjLYQtR1yyOqBUwILsJo6-b0ZpaqIg8",
            "https://drive.google.com/uc?export=view&id=1gUG7zKzBIF3njeiezclLMPY39gO3l9I8",
            "https://drive.google.com/uc?export=view&id=1841ncwe9o9xkWO4BwsV-a_elsA-pAmKw",
            "https://drive.google.com/uc?export=view&id=1yf83u6GZT6R7U4jOcmuVFoRjW-fMoMoz",
            "https://drive.google.com/uc?export=view&id=1yRSY7nUZzm8DOoRZo3l37AVcfySlu2-Y",
            "https://drive.google.com/uc?export=view&id=1QWcNDCYyku5ITQZT_1bMq9tyTgwJ3lDg",
            "https://drive.google.com/uc?export=view&id=18IjV4gPhmZjLVxqxsnJ9i_9x-2XXG_7f",
            "https://drive.google.com/uc?export=view&id=1-acYqa2Pi5clRIp3eLloPFQ50BzypwLN",
            "https://drive.google.com/uc?export=view&id=1X0WJZG9FpqvbwB3acUMeqqPbkIc5kw1g",
            "https://drive.google.com/uc?export=view&id=1IQ9KrRwlu5kXaNuTtPfOc-6-41QBWHek",
            "https://drive.google.com/uc?export=view&id=1S3Asfgvdrv6mqYjmtEHsNWX4FMxFafov",
            "https://drive.google.com/uc?export=view&id=1Y7eax6u2FMp_KLKZvDj9eAwweurxUTYs",
            "https://drive.google.com/uc?export=view&id=1R484m_LB5BEhrbHJ3jRF554X-ydWDOhl",
            "https://drive.google.com/uc?export=view&id=1pdN6FLYu2E9IKnkG6bAe2kOLEJsPEgcD",
            "https://drive.google.com/uc?export=view&id=16V8xSfCBtH6pc5JjCBIvm_if7bRkqdLd",
            "https://drive.google.com/uc?export=view&id=1GmrypZqAKoL2GmhWG2hIjEWihAbOuFs",
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
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung,Lampung Timur",
                "alamat": "nangka 4",
                "hobbi": "main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "-",  
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
                "nim": "",
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
                "nim": "",
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
                "nim": "",
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
                "nim": "",
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
                "nim": "",
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
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "liano",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "",
                "nim": "",
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

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=115AlIoKzVznuqaJ8Shm8AI_p6evDZn5rQ",
            "https://drive.google.com/uc?export=view&id=1-MULAtSuT3jRv2wVNJLtsaMq5qp_StbH",
            "https://drive.google.com/uc?export=view&id=1_PwpTm5_4wiCqTPJIcRdwZ1qg6S9aNPW",
            "https://drive.google.com/uc?export=view&id=156PGcVZvIHtk6zBRTtqIDfhqi6bIaCff",
            "https://drive.google.com/uc?export=view&id=15-UeN4Jui4OIfY70MHbGR3Ngpj8JYknl",
            "https://drive.google.com/uc?export=view&id=1zfk-_7LInSxQ2M18r3wKCG1RyvmP63O2",
            "https://drive.google.com/uc?export=view&id=19Y5urkqy9ONQuALpBmUYFUtSEi0Vzd5m",
            "https://drive.google.com/uc?export=view&id=1mCOI1UnzZl04ZzUtLNICiG9ioeBPitRX",
            "https://drive.google.com/uc?export=view&id=1XgUwhyuIixSHdr8lluO8psiF0q2JK_pI",
            "https://drive.google.com/uc?export=view&id=1aFc5LcVHb-VOyWQZkr7aXQCIpGJ3PRU3",
            "https://drive.google.com/uc?export=view&id=1qPLN-INCFrvlixPBjKYazi9lTMZuc5h6",
            "https://drive.google.com/uc?export=view&id=1SvrspC_KyxULxHSA8wF2kdukclVsjQge",
            "https://drive.google.com/uc?export=view&id=1dosCKBnG7sr8qQiNv07uR43x0vvwslk",
            "https://drive.google.com/uc?export=view&id=1e448UBUDprDp8xf4tQTpYU9AvtZXtIWP",
            "https://drive.google.com/uc?export=view&id=1AFI2z3vWR2r0FR8ulA9Jok-id4MBkKjF",
            "https://drive.google.com/uc?export=view&id=1P-UCHEAb-0Eu9J4RM1pj3riwnFQrrWvX",
            "https://drive.google.com/uc?export=view&id=17nrmWQkOOViOorD-CW61uNdmZtpuhGml",
            "https://drive.google.com/uc?export=view&id=1BidVMkynmPX29JI18UEz3s7882U_K-EF",
            "https://drive.google.com/uc?export=view&id=1C2CBh_NNF082jbCk3SPYvYlorGXFcvnb",
            "https://drive.google.com/uc?export=view&id=1IjA986SIuygyVvjDGEOlGWPHAiwYrAsf",
            "https://drive.google.com/uc?export=view&id=1tj8AAHep-xwuwBkjAXsdq5Tlq40UwBvn",
            "https://drive.google.com/uc?export=view&id=1uIHkzhI2Zm1PU46zfRJ4xZ_pXlg4Kmaz",
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
                "nim": "123450096",
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
            "https://drive.google.com/uc?export=view&id=1aoOa_hJ-uIkwIX01OdPWnnqSwaSg5QLA",
            "https://drive.google.com/uc?export=view&id=1WNs8H9eFh7gZwR3a2bXokqufmpON_UNA",
            "https://drive.google.com/uc?export=view&id=1azWt221tgM18px9e7XUTI7aeZ1FAfjDG",
            "https://drive.google.com/uc?export=view&id=1ajm-hsnvfO5abdkpUM4OujVkpqdmZ6iq",
            "https://drive.google.com/uc?export=view&id=1Spte-yTzMuHJFYlDKMveQJ867uI9eJhh",
            "https://drive.google.com/uc?export=view&id=1FcSp-81ONz5UO8_NMQ5eRZgO8Y3BBbGp",
            "https://drive.google.com/uc?export=view&id=1ArZrnARDfQ4S1MoKgfHt_JcDWGYB6U4A",
            "https://drive.google.com/uc?export=view&id=1b_8FPdVmG4QkOsUvvQM7b0TKdw6xiTdp",
            "https://drive.google.com/uc?export=view&id=1Xsaj1hiXgD4acHSSQM_RQIck2sC7ZF81",
            "https://drive.google.com/uc?export=view&id=1VSCGWGnQe56NrMIyahCMOkR9lY_fvnf7",
            "https://drive.google.com/uc?export=view&id=14tDObuIQoi6ZNP20eqGKNz2050I5QRuV",
            "https://drive.google.com/uc?export=view&id=10-B25Mgso4GyAdHUaN1h6cQZCfGs-TqP",
            "https://drive.google.com/uc?export=view&id=1LpxwRRt7plQarB-ZIRLNiNT0EOL1Stjo",
            "https://drive.google.com/uc?export=view&id=1PSR39gyv45ae9jPZ7jXVbkvwEPOl7ZFl",
            "https://drive.google.com/uc?export=view&id=12Q8EBnbX9RVnAlZTvzYzmmjMBC2vZSHJ",
            "https://drive.google.com/uc?export=view&id=1ZKGXHzD90h7ikjIsDQ_AnF8Bbuh-wQSM",
            "https://drive.google.com/uc?export=view&id=1L-Q_j8twt6vmJeD0zNL-gZc121jw1uGc",
            "https://drive.google.com/uc?export=view&id=1QtQEIR6xaC6e89vpbIna14eDh6xgSOLk",
            "https://drive.google.com/uc?export=view&id=1OMICtRmnLFEkvHh18T08--1hEbIyQpIQ",
            "https://drive.google.com/uc?export=view&id=1jqBqTIks_sf3XRc0y7RiU_oHGTZSI0sO",
            "https://drive.google.com/uc?export=view&id=1Wokyfql7rHHySe9H62I9Tbdq51sFgB4C",
            "https://drive.google.com/uc?export=view&id=1wBoi2C1CD1DGUdOTzVpei75rpAeaaGPd",
            "https://drive.google.com/uc?export=view&id=1BKj_Fxz7aThkAm3L3AqBFfqZ846gRCZ-",
            "https://drive.google.com/uc?export=view&id=13ysVr9Ce9OjtVGHX3j9gQvGW6Pzr4twx",
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
                "kesan": "Bang Arafi baik banget",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana positive vibes banget",  
                "pesan":"Sukses selalu kak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya seru banget",  
                "pesan":"Semoga terus jadi pribadi yang inspiratif dan menyenangkan"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Lancar terus kuliahnya kak"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya lucu banget",  
                "pesan":"Tetap semangat kuliahnya bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Khoirul enak diajak ngobrol",  
                "pesan":"Bahagia dan sukses selalu kak"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia lucu banget",  
                "pesan":"Tetap jadi orang yang semangat terus kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla lembut dan ramah banget",  
                "pesan":"Semoga selalu dikelilingi hal baik kak"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@",
                "kesan": "Abangnya baik banget",  
                "pesan":"Semoga makin sukses bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea seru dan baik banget kaya ibu peri",  
                "pesan":"Semangat kuliahnya kakak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak cindy cantik banget",  
                "pesan":"Bahagia terus kak"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea ramah banget",  
                "pesan":"Tips jadi MC kak"# 1
            },
            {
                "nama": "Desman Velius Halaws",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman baik banget",  
                "pesan":"Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya ramah dan baik banget",  
                "pesan":"Bahagia terus kak"# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak lulu ekstrovert parah tapi seru banget",  
                "pesan":"Lancar terus kuliahnya kak"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya keren banget",  
                "pesan":"Sukses dan sehat selalu bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "Abang santai tapi enak diajak diskusi",  
                "pesan":"Semoga sukses terus dan tetap rendah hati, Bang!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya lucu banget",  
                "pesan":"Semoga makin sukses dan tetap ceria bang"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Ilmi keliatannya kalem",  
                "pesan":"Semoga terus semangat belajar kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melin ramah dan lembut banget",  
                "pesan":"Bahagia selalu kak"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla seru banget diajak ngobrol",  
                "pesan":"Semoga terus berkembang kak"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semoga makin sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya asik banget",  
                "pesan":"Semoga terus semangat dan sukses kedepannya bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakaknya keren banget",  
                "pesan":"Tips pinternya dong kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen Internal":
    def DepartemenInternal():
         gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qE4iK-VREnPFiKGWFnxfcjkinTxRRrB9",
            "https://drive.google.com/uc?export=view&id=1ZfCaL4O_EWKdnQGxi6My62TFOuyBfFmU",
            "https://drive.google.com/uc?export=view&id=14FmasHHzFplCp6Ga09PfOk-fS3bBD-tf",
            "https://drive.google.com/uc?export=view&id=1TwaBZcvcjTYPnp3MBiyQnVgW0mK5cY5t",
            "https://drive.google.com/uc?export=view&id=1KK7FZ049888zuOTbqClrha1ExtyFnsT_",
            "https://drive.google.com/uc?export=view&id=1lmjuygRXD4qP15Y6is0ou8-pEy4BSiJG",
            "https://drive.google.com/uc?export=view&id=1wvVCvGu_JPsPBd8xv-mesZKcFPxK7rtv",
            "https://drive.google.com/uc?export=view&id=147FvzQKQ-D_W6fjwL67skFGXY4uueIlM",
            "https://drive.google.com/uc?export=view&id=131VzGOMIEkjAPyI7phUTZblpnAQnkb0U",
            "https://drive.google.com/uc?export=view&id=1cPQ21iesv5fsZDVHUtxhcfygp8LTSJlb",
            "https://drive.google.com/uc?export=view&id=1p2_-yUOlpSY-zgIzapS2TNrE-XtYVlt9",
            "https://drive.google.com/uc?export=view&id=1v015Mim7PZFC_Jk_KsI1l8vbj36iDyk1",
            "https://drive.google.com/uc?export=view&id=1pmFHsuEsxCY6k_y2JNfe2zE3cp07zhgp",
            "https://drive.google.com/uc?export=view&id=13y0_o_Ref3PomwxWfHO9KXcZkvuy-GeN",
            "https://drive.google.com/uc?export=view&id=1akmUexMkEg1c76r6IgN88d7Bjc7Tp-lQ",
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
                "kesan": "Suka banget liat outfit kak rani keren banget",  
                "pesan":"Semoga kak Rani selalu bahagia dan makin sukses kedepannya"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Abang ramah dan punya vibe yang tenang banget",  
                "pesan":"Semoga sukses selalu ya Bang!"# 1
            },
            {
                "nama": "Salwa Farhanatusaiidah",
                "nim": "12245055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa kalem dan sopan banget, enak diajak ngobrol",  
                "pesan":"Semoga semua cita-cita kak Salwa tercapai dan selalu sehat"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakaknya ramah banget",  
                "pesan":"Semangat terus kuliahnya kakak!"# 1
            },
              {
                "nama": "Rendi Alezander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@lexanderr",
                "kesan": "Abangnya baik banget",  
                "pesan":"Sukses selalu bang"# 1
            },
            {
                "nama": "Haikal fransisko Simbolon",
                "nim": "122450106",
                "umur": "18",
                "asal":"Tulang Bawang",
                "alamat": "Sukabumi",
                "hobbi": "Membersihkan rumah",
                "sosmed": "@haikalsbln_",
                "kesan": "Kirain abangnya galak banget, ternyata baik",  
                "pesan":"Lancar terus kuliahnya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450076",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak iqfina cantik banget",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya ya, Kak!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450009",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak may keren dan keliatan tegas",  
                "pesan":"Sehat selalu kak"# 1
            },
            {
                "nama": "Muhammad Naufal Afghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@Muhammadnaufalafghani73",
                "kesan": "Abangnya kalem banget",  
                "pesan":"Tetap semangat kuliahnya bang"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya positive vibes banget",  
                "pesan":"Semoga sukses terus dan tetap semangat bang!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna ramah dan ceria banget",  
                "pesan":"Bahagia terus ya kak"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak keren cantik banget",  
                "pesan":"Tips cantiknya dong kak"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hifzky",
                "kesan": "Abang Hanif seru banget, enak diajak ngobrol",  
                "pesan":"Semoga sukses terus dan tetap rendah hati, Bang!"# 1
            },
            {
                "nama": "Sarah wasti",
                "nim": "122450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah keliatan lembut dan soft spoken",  
                "pesan":"Semoga selalu diberi kebahagiaan dan kesuksesan"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "Main Rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semoga terus semangat dan sukses kuliahnya"# 1
            },
        ]
         display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1i7iODzKC6V-wRmAz9ZfKKsGhqrGQHXXk", 
            "https://drive.google.com/uc?export=view&id=1m9_ZaYDrFFPnRE3SXXTDvFANO2ILvZ9H", 
            "https://drive.google.com/uc?export=view&id=1sFkKL4XYEjNKNPoQhlXr9xrI2TfMvltA",  
            "https://drive.google.com/uc?export=view&id=1YUbxw2QG1C_Po_w0cfB52qFy0e5zU6jG", 
            "https://drive.google.com/uc?export=view&id=1C1nEjmorz-HLdxyNlerWm8Gd-KkoCVzp",  
            "https://drive.google.com/uc?export=view&id=1PGsu9f1fYEwWww9467jvfm8KSkVLq3EK",  
            "https://drive.google.com/uc?export=view&id=1Jnj2G6tV4b4HVzHs7YFp62RjUmwtftJl",  
            "https://drive.google.com/uc?export=view&id=1H5wNLGebi0LnB988TZQHb3c6zzd1Wsse",  
            "https://drive.google.com/uc?export=view&id=1sMeqAOstqbteVF2CueDA27sD3slxXjHr",  
            "https://drive.google.com/uc?export=view&id=15aun3O-suecXG7FJSBtxVsdy5VwpMN0V", 
            "https://drive.google.com/uc?export=view&id=1OeIjuNSuEszuq4uGmuDTOq8j2-gM7CeL",
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
                "kesan": "Bang Danang seru banget diajak ngobrol, banyak hal baru yang saya dapat",  
                "pesan":"Terus berkarya ya bang dan semangat kuliahnya!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450012",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya lembut dan punya aura yang menenangkan",  
                "pesan":"Terus semangat kak!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki_",
                "kesan": "Outfit abangnya keren keren banget",  
                "pesan":"Sehat dan bahagia selalu bang"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Joging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton dramashort di fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakaknya tinggi dan cantik banget",  
                "pesan":"Semangat terus kuliahnya kak, jangan lupa jaga kesehatan!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_azazahra",
                "kesan": "Kakaknya ramah banget",  
                "pesan":"Semoga makin sukses dan bahagia selalu kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya keliatan kalem",  
                "pesan":"Tetap semangat dan terus jadi inspirasi bang!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya seru banget",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya ya, Kak!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gang perwira 2",
                "hobbi": "Nontol alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakaknya cantik dan anggun banget",  
                "pesan":"Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak naya seru dan ramah banget",  
                "pesan":"Tips bikin risol enak dong kak"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Semoga selalu diberi kelancaran dalam kuliahnya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xkwXQ0x93ECuU89yED73_bGt-Tq3TkRS",
            "https://drive.google.com/uc?export=view&id=1adEJSkzK3QlhyDZaiZQv_0XWTex2Gk-p",
            "https://drive.google.com/uc?export=view&id=12TUrF1tb-oycMGK3_KJQ5OkDvXOU8s6I",
            "https://drive.google.com/uc?export=view&id=109vb5X-e54Lj1MTKzioCREFeobH6iHUY",
            "https://drive.google.com/uc?export=view&id=1kAg-ihPNC_0dCrt3wbJMQuEUKE_9TXnx",
            "https://drive.google.com/uc?export=view&id=1VUCFcK8WmYBwBWkAL2duogZ6l_-Vxf4z",
            "https://drive.google.com/uc?export=view&id=17N-qVR8mnEf8gX_XAxa-N7W93oA1D6T1",
            "https://drive.google.com/uc?export=view&id=1dixestLS9ab0GZbTqaISqXnU-U0W4fw7",
            "https://drive.google.com/uc?export=view&id=13MVZGRmj03qS2luQHEZzEZJnViX0KyeT",
            "https://drive.google.com/uc?export=view&id=1jsPZvq2EQcOcJgPbNp8k8reDYG7aF2Sy",
            "https://drive.google.com/uc?export=view&id=1Sp6Y3wVElrfMSxC3D1dgMpoXcCX-ONgR",
            "https://drive.google.com/uc?export=view&id=1tlMYyHaseAAUyTNz2g8pC15PM4K9atv3",
            "https://drive.google.com/uc?export=view&id=19c6G8fGmGooe_-4hhNn6F35ao_bXUn93",
            "https://drive.google.com/uc?export=view&id=1Kus5diftik2m3eL07DgQ23kM_5_yqRjD",
            "https://drive.google.com/uc?export=view&id=1WMkVOPWi9wNg11s7QsENXgsKxL8FPjDI",
            "https://drive.google.com/uc?export=view&id=1BWSB2QPEqfNvlX4gd6f0I3Y06blbZAX6",
            "https://drive.google.com/uc?export=view&id=1MFDbW5ofCLU14APorCwwF_JYIpIXnKXV",
            "https://drive.google.com/uc?export=view&id=1z-W8VMzOlIGjbQMpwULR0djJkgcLmJUT",
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
                "kesan": "Kakaknya easygoing dan enak banget diajak ngobrol",  
                "pesan":"Semoga selalu bahagia dan sukses di setiap langkahnya kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak nelly ramah dan seru banget",  
                "pesan":"Terus semangat kuliahnya dan tetap jadi pribadi yang lembut ya!"# 1
            },
            {
                "nama": "Khoriul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam__",
                "kesan": "Abangnya seru banget",  
                "pesan":"Semangat terus, Bang!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Hui",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya keren banget",  
                "pesan":"Terus berproses ya bang!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Bang Rafi baik banget",  
                "pesan":"Semangat PDD ya bang"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa baik banget",  
                "pesan":"Terus jadi diri sendiri dan percaya diri kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122350020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaa",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Tetap semangat menimba ilmu dan jangan lupa istirahat kak"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kakaknya positive vibes banget",  
                "pesan":"Terus semangat dan bahagia selalu kak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya lembut dan sopan banget",  
                "pesan":"Semoga semua harapan dan cita-citanya tercapai ya, Kak!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kakaknya cantik dan lucu banget",  
                "pesan":"Semangat terus kuliah dan tetap jadi pribadi yang positif!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya seru dan punya vibe ceria",  
                "pesan":"Terus tebar energi positifmu ya Kak!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas, Jati Agung",
                "hobbi": "Dengar musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla keliatannya kalem",  
                "pesan":"Tetap semangat dan terus jadi inspirasi buat orang ya kak"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania ramah banget",  
                "pesan":"Semoga makin sukses dan tetap membawa energi positif, Kak!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Bang Akmal keliatannya kalem",  
                "pesan":"Terus berproses dan jangan berhenti mengejar cita-cita ya bang!"# 1
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana keren banget",  
                "pesan":"Semangat mnenjalani hari-harinya kak"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra cantik banget",  
                "pesan":"Kasih Tips jago melukis dong kak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah balau residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak eigi ramah, baik, dan cantik banget",  
                "pesan":"Tetap jadi diri sendiri ya kak"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Romauli cantik banget kaya berbie",  
                "pesan":"Semoga selalu semangat dan sukses terus kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan



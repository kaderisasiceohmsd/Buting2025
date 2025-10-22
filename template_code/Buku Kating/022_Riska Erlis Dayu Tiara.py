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
            "https://drive.google.com/uc?export=view&id=14wXKui8Gw1LXY3vyzmfNzG4DU_RqEOBc",
            "https://drive.google.com/uc?export=view&id=14l1N_1vSxJXWceeMJw3apHz5Upp2O3sI",
            "https://drive.google.com/uc?export=view&id=14bNj8xOm6VFC3FZtNWMyU5qjDvb9WyWN",
            "https://drive.google.com/uc?export=view&id=14LLpC8yIepUsl9dVE8jA6C5gWPQL6bkc",
            "https://drive.google.com/uc?export=view&id=14mqEOiUvhhmhIgJ0C_GZ8RkJPv09o4u1",
            "https://drive.google.com/uc?export=view&id=14ox7sx2GJflj43kqnBjlamSpIPgMTh2L",
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
                "kesan": "Kakak keren dan bijak banget",  
                "pesan":"Semoga semua hal baik terus ngikutin kakak!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumbar",
                "alamat": "Gya Kost Korpri",
                "hobbi": "Cute Jenderal",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya terlihat bersemangat dan positif",  
                "pesan":"Semoga terus sukses dan menginspirasi!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11PxIbJfXtYyQugzcjF2FVFSeIkjVEo5e",
            "https://drive.google.com/uc?export=view&id=11dyqCgGi_KDumjRe0rCoTjVH1VBv8306",
            "https://drive.google.com/uc?export=view&id=111qoQ44QKt_suCxZlMze-fTIFldIey6J",
            "https://drive.google.com/uc?export=view&id=1JoFRUNfxvwQfmb1RySmJa0mvnAV2aMqW",
            "https://drive.google.com/uc?export=view&id=11EyeQosQ_WwMeiEymkjGqqxr00lFZ3Vh",
            "https://drive.google.com/uc?export=view&id=119voL39eO3w7fFBXsT6jjSpTHRD_TwOo",
            "https://drive.google.com/uc?export=view&id=11_FWhl6scCYUlbCOvHh7XLnPOvLbx5_4",
            "https://drive.google.com/uc?export=view&id=10VWLUyMfEPFjms4nn7uISpSBAme7aclB",
            "https://drive.google.com/uc?export=view&id=11Vhfd8YVDG3kOpbpuWrfQD32zmMeG-10",
            "https://drive.google.com/uc?export=view&id=115FrwaxAcgcZxvs_2BsyyeJBEyRgKl4C",
            "https://drive.google.com/uc?export=view&id=118LVG5k6-H85C4ln__JfG8MIq797Ov7t",
            "https://drive.google.com/uc?export=view&id=11ZmqG49ewJBaNRuU6uPN3kbQYg7KDEGA",
            "https://drive.google.com/uc?export=view&id=138VhwxVdRhYWxoqiWce7b2h2xOKX8b9B",
            "https://drive.google.com/uc?export=view&id=11ARZ3pQV3xO5m956ciF6cQhqQ4c0In6c",   
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
                "kesan": "Abangnya asik banget, gak ngebosenin", # 1 
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
                "kesan": "kakaknya gemesin banget, vibes-nya tuh enak!", # 1 
                "pesan":"Sukses terus kedepannya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main ice skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakak vibes-nya chill banget, bikin nyaman!!",  
                "pesan":"sukses, selalu dilancarin dalam segala hal kak!"# 1
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
            "https://drive.google.com/uc?export=view&id=1GmrypZqAKoL2GmhWG2hIjEWihAbOuFs7",
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
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "jalan-jalan",
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
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Kontrakan GH",
                "hobbi": "Main bola",
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
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "",
                "sosmed": "@daffahdynn_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game",
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
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "ngekader",
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
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Jl. Korpri Raya",
                "hobbi": "Nontonin anak tari latihan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No. 55",
                "hobbi": "Ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Joki strava",
                "sosmed": "@ihsan.myusus",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Terjun Payung",
                "sosmed": "@kevinaj__",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton anak tari perform",
                "sosmed": "@m.ridwan_22",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngerjain soal mtk",
                "sosmed": "@liano.wlm",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "1233450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Ratu, Bandar Lampung",
                "hobbi": "Nonton anime",
                "sosmed": "@rewinanaa",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15AlIoKzVznuqaJ8Shm8AI_p6evDZn5rQ",
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
            "https://drive.google.com/uc?export=view&id=1dosCKBnG7sr8qQiNv07uR43x0vvwslkl",
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
                "kesan": "abang sangat ramah dan membuat suasana wawancara jadi nyaman",  
                "pesan":"Semoga abang selalu sukses di setiap langkahnya", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak orangnya ramah dan menyenangkan",  
                "pesan":"Semoga semangatnya gak pernah pudar ya kak!", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya selalu sopan dan berwibawa",  
                "pesan":"semoga abang terus jadi contoh yang baik buat semuanya", # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. lapas,Belwis",
                "hobbi": "maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya sederhana tapi berkesan banget",  
                "pesan":"terus semangat ya kak, jangan pernah berubah!", # 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnya sabar banget, gak pernah marah",  
                "pesan":"Makasih udah selalu tenang dalam segala situasi", # 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya punya pembawaan yang tenang tapi tegas",  
                "pesan":"Semoga abangnya terus sukses dan tetap rendah hati", # 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "abangnya asik dan ramah banget!",  
                "pesan":"Semangat terus bang, sukses selalu ya!", # 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kak Nadia keliatan kalem tapi seru diajak ngobrol",  
                "pesan":"Makasih kak udah ramah waktu wawancara!", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Marleta keliatan cerdas dan enak diajak ngobrol.",  
                "pesan":"Semoga terus semangat dan sukses ya kak!", # 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234500119",
                "umur": "20",
                "asal":"Pramuka, Bandar Lampung",
                "alamat": "Perum Bukit Alam Permai 3, Blokk C, No.9",
                "hobbi": "Dengrin musik",
                "sosmed": "@keyashafi_",
                "kesan": "bang Akeyla orangnya ramah dan menyenangkan.",  
                "pesan":"Terima kasih udah baik dan sabar waktu wawancara!", # 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bummisari Kec.Natar",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kak Anggi keliatan enerjik dan percaya diri banget!",  
                "pesan":"Semoga makin sukses dan tetap ceria ya kak!", # 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Sale, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi kalem tapi punya aura berwibawa.",  
                "pesan":"Semoga terus semangat dan jadi inspirasi ya kak!", # 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kak Olla anggun dan ramah banget",  
                "pesan":"Tetap semangat dan terus bersinar ya kak!", # 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kak Fairuz santai tapi tetap fokus waktu ngobrol",  
                "pesan":"Semangat terus kak, sukses selalu!", # 1
            },
             {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "kak tanty energikk, sukaa",  
                "pesan":"Semoga selalu semangat ngejalanin kesibukannya ya kak!", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "Bang Eggi asik dan gampang nyatu pas ngobrol",  
                "pesan":"Sukses terus bang! Tetap semangat ya!", # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang (main game)",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah seru dan spontan waktu wawancara",  
                "pesan":"Makasih kak udah bikin suasananya jadi santai!", # 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer),tidur,jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "Bang Fabio asik dan rame, gampang akrab",  
                "pesan":"Semoga sukses terus dan tetap humble bang!", # 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@giofaniars_",
                "kesan": "Bang Gio orangnya chill tapi tetap serius pas ngobrol",  
                "pesan":"Terus semangat dan sukses terus bang!", # 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kak Rahma sopan dan keliatan pintar banget",  
                "pesan":"Makasih kak udah ramah dan inspiratif!", # 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "Kak Rahmah seru dan punya energi positif",  
                "pesan":"Semangat terus kak! Jangan pernah lelah berkembang!", # 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans Sakum,Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "Bang Razin orangnya kalem tapi keren",  
                "pesan":"Sukses terus bang, semoga semua lancar!", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11x3FHQFg8hE753XzOAnz5Jt2TWB4SmJt",
            "https://drive.google.com/uc?export=view&id=11xAt7mP8FNtTfdGf1DMgkoMWy8fxeBzU",
            "https://drive.google.com/uc?export=view&id=121I4dhQO2CPUx3dOGux2BV1g9HzAgadw",
            "https://drive.google.com/uc?export=view&id=12GGdIs3orXuxOWMmRjDdrlE5MA1K1QtY",
            "https://drive.google.com/uc?export=view&id=12QuabZrW6REl7DQbzWTyDQAaoH9FwwkT",
            "https://drive.google.com/uc?export=view&id=12cpWMmP0RbeE5PL6nGQ_ACN92Y-uppW2",
            "https://drive.google.com/uc?export=view&id=12tY78GdHQjof9m8H2qprpAtKKWbRBvGl",
            "https://drive.google.com/uc?export=view&id=12jnzUKwv5a83kzI1EIm-G7MV6rFGnJlz",
            "https://drive.google.com/uc?export=view&id=11m-b0IM52kapMmm1TF06S47tYX5525Fg",
            "https://drive.google.com/uc?export=view&id=12wVi935XloRQzRJ6FcKYnjpK82AmcPzA",
            "https://drive.google.com/uc?export=view&id=11uyvEDRoyNX1JVMo2M2mItUJGEz3gvdG",
            "https://drive.google.com/uc?export=view&id=137YREtl57NSF8IdKLWuSzVGYfyNfyNAs",
            "https://drive.google.com/uc?export=view&id=12E989HvzyB3jhDdCN4F-lwHLACS_K7Rk",
            "https://drive.google.com/uc?export=view&id=11jQJiLGsYoE_aP457gD17tnDXktPSYFa",
            "https://drive.google.com/uc?export=view&id=126mOKA7HQhbwIUVTstXPbTS8srmvJkF-",
            "https://drive.google.com/uc?export=view&id=12mXauNcS1QhBJujUQK-2DJu3_BeCTlGc",
            "https://drive.google.com/uc?export=view&id=12uBiPF3uK8Hy5FPi9CcR3ruMH2IWZ541",
            "https://drive.google.com/uc?export=view&id=1289UNgj2zvQSHr0_niFfPFemXQo7oqwD",
            "https://drive.google.com/uc?export=view&id=12mKPAJBgTkivvKKwixx1OLJZwAXyKAdb",
            "https://drive.google.com/uc?export=view&id=12cygvNCENZdycYt8KaHc6vXBaBEIXOuh",
            "https://drive.google.com/uc?export=view&id=12BPWxP-2Ku1Y95kMrW-o2AHtNGe6gJdx",
            "https://drive.google.com/uc?export=view&id=120JY-kec3KblYFyPhip8JHAJa_oPi1VN",
            "https://drive.google.com/uc?export=view&id=1297Eu9tej5_m9EcTVv93PbLNhX-YnQkb",
            "https://drive.google.com/uc?export=view&id=12Tm1G5dP5HKjSA6LEA8JaF5cBvC4Lz-o",
        
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
                "kesan": "Bang Arafi seru dan enak diajak ngobrol",  
                "pesan":"semoga makin sukses dan tetap rendah hati ya bang!", # 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana kalem tapi asik banget pas diajak ngobrol",  
                "pesan":"Makasih kak udah ramah dan menyenangkan!", # 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "Kak Keisha keliatan anggun dan sopan banget",  
                "pesan":"Semoga selalu bahagia dan sukses terus ya kak!", # 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini ramah dan enak banget diajak cerita",  
                "pesan":"Tetap semangat dan jangan capek senyum ya kak!", # 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Bang Arya santai tapi berwibawa",  
                "pesan":"Semangat terus bang, sukses buat semuanya!", # 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Khoirul sopan dan berenergi positif banget",  
                "pesan":"Tetap semangat dan jangan berhenti berkembang ya kak!", # 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia lucu dan ceria banget waktu ngobrol",  
                "pesan":"Semoga hari-harinya selalu penuh semangat, kak!", # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla lembut tapi menyenangkan banget",  
                "pesan":"Terus semangat dan sukses selalu ya kak!", # 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@",
                "kesan": "Bang Syahrialdi kalem tapi keren waktu ngobrol",  
                "pesan":"Semoga makin sukses dan tetap rendah hati bang!", # 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea sopan dan smart banget",  
                "pesan":"Terima kasih udah ngasih kesan yang positif banget kak!", # 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak Cindy rame dan seru diajak ngobrol",  
                "pesan":"Tetap semangat kak, sukses buat semuanya!", # 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea friendly banget dan gampang nyatu",  
                "pesan":"Semoga makin sukses dan terus ceria ya kak!", # 1
            },
            {
                "nama": "Desman Velius Halaws",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman keren banget",  
                "pesan":"Semoga terus semangat dan sukses selalu bang!", # 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Devyna ceria banget dan bikin suasana enak",  
                "pesan":"Tetap semangat dan terus bawa vibes positif ya kak!", # 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Luthfia rame dan lucu banget pas ngobrol",  
                "pesan":"Semangat terus kak, sukses buat semuanya!", # 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "Bang Irvan santai tapi asik banget diajak ngobrol",  
                "pesan":"Semoga makin sukses dan terus semangat bang!", # 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "Bang Adit kalem tapi punya pandangan menarik",  
                "pesan":"Sukses terus bang, tetap semangat ya!", # 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya ceria dan ekspresif banget",  
                "pesan":"Makasih kak udah nyebarin energi positif!", # 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "kalem tapi asik banget diajak ngobrol",  
                "pesan":"Semoga sukses selalu dan terus semangat ya kak!", # 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melinza lembut dan sopan banget",  
                "pesan":"Terus semangat kak, semoga semua yang dicita-citain tercapai!", # 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla orangnya komunikatif dan semangat banget",  
                "pesan":"Sukses terus kak, semoga semua lancar!", # 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak Nurul lembut dan ramah banget waktu ngobrol",  
                "pesan":"Tetap semangat dan terus berkembang ya kak!", # 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois santai tapi seru banget",  
                "pesan":"Semoga makin sukses dan tetap keren bang!", # 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kak Tarisya lembut dan sopan banget pas ngobrol",  
                "pesan":"Semoga selalu bahagia dan sukses ya kak!", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen Internal":
    def DepartemenInternal():
         gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13gKwLCcDoEck2bkqGNIJ5DBaOSSM-0XN",
            "https://drive.google.com/uc?export=view&id=13uIIblaIlqHu_d9XzmNKXXGV05DBSBc8",
            "https://drive.google.com/uc?export=view&id=13KrT_tnunf7uBC8-v3-Z70FIxQ7iqQfm",
            "https://drive.google.com/uc?export=view&id=13YnMGdlBs1D8DnBsYHusG6ty0e-7q8OZ",
            "https://drive.google.com/uc?export=view&id=13ZouYB2byGmbIUIlsjuBKOFujXTg1IWk",
            "https://drive.google.com/uc?export=view&id=13gGwlUpG69f0fa4EU6U817sbyLqCu4-I",
            "https://drive.google.com/uc?export=view&id=13nCPa7feMdYn5vxBwtsX0sGT6-xPFSk6",
            "https://drive.google.com/uc?export=view&id=13fkH5ssFPi7NENpl1Duh0O3Ka3Slqiz6",
            "https://drive.google.com/uc?export=view&id=13dYk3_7d2V0tcAoXgW5F9L90LSTCUtE8",
            "https://drive.google.com/uc?export=view&id=13OhV6KvCQw8glPA8bNBHif1APGrLb4I5",
            "https://drive.google.com/uc?export=view&id=13nTzFi3_fBsanUUyd9fuMl-6y9kS9Hvo",
            "https://drive.google.com/uc?export=view&id=13XUTiICr_BnJFMroOC0rTSSPARvtqX-Z",
            "https://drive.google.com/uc?export=view&id=13Sh8P7Pvxdrikftg1FQNwjok2PnXjrsD",
            "https://drive.google.com/uc?export=view&id=13lm4BZ0ZS0rqq7izfWPxFhJlkWVpl30M",
            "https://drive.google.com/uc?export=view&id=13YgRUeWMURCIOG5R0Irji5QaLc-HQGZq",
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
                "kesan": "Kak Rani modis banget, gayanya kece",  
                "pesan":"Semoga kak Rani selalu sehat dan makin bersinar ke depannya"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "tenang banget, tapi tetap seru diajak ngobrol",  
                "pesan":"Tetap semangat kuliahnya kak, sukses terus ya!"# 1
            },
            {
                "nama": "Salwa Farhanatusaiidah",
                "nim": "12245055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa lembut banget orangnya, enak banget diajak cerita",  
                "pesan":"Semoga kak Salwa makin sukses dan selalu diberi kesehatan"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azza.raaa_",
                "kesan": "baik banget, gampang akrab juga sama orang baru",  
                "pesan":"Tetap semangat kuliahnya kak, sukses terus ya!"# 1
            },
              {
                "nama": "Rendi Alezander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@lexanderr",
                "kesan": "Abang Rendi kalem banget, asik diajak ngobrol juga",  
                "pesan":"Semoga Bang Rendi selalu dilancarkan semua urusannya"# 1
            },
            {
                "nama": "Haikal fransisko Simbolon",
                "nim": "122450106",
                "umur": "18",
                "asal":"Tulang Bawang",
                "alamat": "Sukabumi",
                "hobbi": "Membersihkan rumah",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang Haikal ternyata asik banget, awalnya keliatan serius",  
                "pesan":"Semangat terus kuliahnya Bang Haikal!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450076",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak Iqfina cantik dan punya vibe yang lembut banget",  
                "pesan":"Semoga Kak Iqfina selalu bahagia dan lancar kuliahnya"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450009",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak May keren banget dan keliatan percaya diri",  
                "pesan":"sehat terus dan makin sukses ya kak"# 1
            },
            {
                "nama": "Muhammad Naufal Afghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@Muhammadnaufalafghani73",
                "kesan": "Abangnya kalem banget, tapi seru kalo udah ngobrol",  
                "pesan":"Semangat terus kuliahnya Bang Naufal!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya asik dan punya aura positif banget",  
                "pesan":"Semoga Bang Zailani makin semangat dan terus sukses!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna ceria banget dan gampang bikin suasana rame",  
                "pesan":"Kak Hanna ceria banget dan gampang bikin suasana rame"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak Keren beneran keren, gayanya simple tapi manis",  
                "pesan":"Semoga Kak Keren selalu percaya diri dan sukses terus!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hifzky",
                "kesan": "Abang Hanif santai banget orangnya, gampang diajak ngobrol",  
                "pesan":"Semoga Bang Hanif makin sukses dan tetap rendah hati!"# 1
            },
            {
                "nama": "Sarah wasti",
                "nim": "122450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah lembut dan pembawaannya tenang banget",  
                "pesan":"Semoga Kak Sarah selalu dikasih kebahagiaan dan kesuksesan"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "Main Rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kak Zahra manis banget dan keliatan friendly",  
                "pesan":"Semoga Kak Zahra terus semangat dan sukses selalu!"# 1
            },
        ]
         display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hbcqFWZa-PU0OXT9z5UkPcr5XpKEssmX", 
            "https://drive.google.com/uc?export=view&id=1GY6qwwkN9C5WhqnzLUu8m387t6Syeijl", 
            "https://drive.google.com/uc?export=view&id=19I6tqaxGNlUVasEee4AuzDw9jD_Yh0k-",  
            "https://drive.google.com/uc?export=view&id=13xNlb_wpVQtwPPYfWQ4G_ifKPHoc-FDu", 
            "https://drive.google.com/uc?export=view&id=1pr9_nLmK_rQjIa2lZdlc1UDb71-sal9p",  
            "https://drive.google.com/uc?export=view&id=1t_XCPlnwpzJNDztr25XdkwJztAnvgioj",  
            "https://drive.google.com/uc?export=view&id=16mR01fmOwQ8SKVBHbdMzs9OCM2WR_hji",  
            "https://drive.google.com/uc?export=view&id=1KHlwhmsYC5oMyUmkgZfVeBlHYpR4elG_",  
            "https://drive.google.com/uc?export=view&id=1xiXoPEAd_h2UvsUma9UIQdXfRbv1SI84",  
            "https://drive.google.com/uc?export=view&id=1B_-LmcbOw1WlORmdSIGiPEfsbj9_m031", 
            "https://drive.google.com/uc?export=view&id=12sHK5vVL1LHwsBA90siS80UGsj-DCrlw",
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
                "kesan": "Abangnya seru banget diajak ngobrol, pembawaannya santai tapi nyambung terus",  
                "pesan":"Semangat terus bang, semoga semua rencananya lancar dan sukses selalu!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450012",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "kakaknya kalem banget",  
                "pesan":"Tetap semangat dan semoga hal-hal baik selalu nyertai kakak!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki_",
                "kesan": "Abangnya humble banget, enak banget diajak ngobrol",  
                "pesan":"Sukses terus ya bang! Tetap jadi pribadi yang asik dan rendah hati "# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Joging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya bersemangat banget dan energinya positif",  
                "pesan":"Terus sebarkan energi baiknya ya kak, semangat selalu!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton dramashort di fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakaknya ramah banget dan gampang akrab",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_azazahra",
                "kesan": "Kakaknya baik banget dan sopan banget pas ngobrol",  
                "pesan":"Tetap semangat ngejar cita-citanya ya kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya tenang tapi seru",  
                "pesan":"Terus semangat ya bang, semoga sukses di tiap langkah!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya ramah banget dan murah senyum",  
                "pesan":"Semoga makin sukses dan selalu dikelilingi orang-orang baik!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gang perwira 2",
                "hobbi": "Nontol alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak gayanya santai tapi nyambung",  
                "pesan":"Tetap semangat kak, semoga semuanya berjalan lancar!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya lembut banget dan sopan waktu ngobrol",  
                "pesan":"semangat terus ya kak! Semoga semua yang dicita-citakan tercapai!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kakaknya supel dan mudah akrab, suasananya jadi cair",  
                "pesan":"Tetap semangat ya kak! Jangan lupa istirahat juga!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12vtO2JzMzLbqkGr34YfqYcRha7I3tovQ",
            "https://drive.google.com/uc?export=view&id=1Y2E-MtmeIDCGcBV7lJAT0XvVF_1_dueo",
            "https://drive.google.com/uc?export=view&id=1f3GpJanITvbpYy11h8xO39n7MRHw5pxt",
            "https://drive.google.com/uc?export=view&id=1UIiZVFcKVxtpkE-rFaZHd1LCz2Nsqueb",
            "https://drive.google.com/uc?export=view&id=1uz4TmjqXTsKoSigT11tnDqnEwmqj3bSE",
            "https://drive.google.com/uc?export=view&id=1fMqu7BZYSqPmQIMy1cJnURaUpRSpuRLY",
            "https://drive.google.com/uc?export=view&id=1M0kQ9CP0omz4exY3n7n91ydK1bdCem6l",
            "https://drive.google.com/uc?export=view&id=1JRp_8u6lkZFAIsgI5ItUl36pguQ360I3",
            "https://drive.google.com/uc?export=view&id=1u4cTIL64VvdWx5-XzvGSNIuAkwrlADAZ",
            "https://drive.google.com/uc?export=view&id=1dKncSFF9rFREpDVQUkTnIQsz8EsCgm-N",
            "https://drive.google.com/uc?export=view&id=14TBsuWuGBbjl_mZD7_So3ITFUawiQ9_d",
            "https://drive.google.com/uc?export=view&id=1WMLNiWJT3Dwk6ROHt080NfUxuJ2s-7cd",
            "https://drive.google.com/uc?export=view&id=1Lsgpo0Q7_eWFhe53HRTfUl0AG80fuQem",
            "https://drive.google.com/uc?export=view&id=1Wa57rqwSgK7JsVxQn6vDL8h0O36nH46k",
            "https://drive.google.com/uc?export=view&id=1Yw6iGwklqu4ZeqnVpkVS4oBeNZpr1M7u",
            "https://drive.google.com/uc?export=view&id=17iqfNm56Cy-Sn7mRnhlJF2ondrM5IDWl",
            "https://drive.google.com/uc?export=view&id=1cVxwXzb5KeK0eKwbh8klpRVyZ-giOL5Q",
            "https://drive.google.com/uc?export=view&id=12Mbh7qhxDQHhMx8p9TCwXsmz-xuv483Z",
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
                "kesan": "Kakaknya cantik, kalem, dan cara bicaranya enak banget didengar",  
                "pesan":"Semangat terus ya kak! Tetap jadi pribadi yang lembut tapi kuat"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Rahma orangnya hangat banget, gampang bikin suasana nyaman",  
                "pesan":"Semoga selalu bahagia dan sukses di setiap langkah kak!"# 1
            },
            {
                "nama": "Khoriul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam__",
                "kesan": "Abangnya seru banget, gayanya santai tapi nyenengin kalau ngobrol",  
                "pesan":"Tetap semangat bang, semoga makin banyak hal keren yang bisa dicapai!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Hui",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya asik banget, pembawaannya santai tapi berwibawa",  
                "pesan":"semangat terus ya bangg, makin sukses!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "keliatan energik dan easygoing",  
                "pesan":"Tetap semangat bang! Jangan lupa jaga kesehatan juga"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa asik banget",  
                "pesan":"Semangat ya kak! Semoga semua hal baik datang di waktu yang tepat"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122350020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaa",
                "kesan": "Kakaknya pintar banget dan keliatan rajin, inspirasional!",  
                "pesan":"Semoga terus jadi sosok yang semangat dan rendah hati ya kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kak Aliya ramah banget dan suaranya lembut, enak diajak ngobrol",  
                "pesan":"Semangat terus ya kak, terus kembangin bakatnya!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna kalem dan sopan, pembawaannya tenang banget",  
                "pesan":"Semoga kakak selalu diberi semangat dan kebahagiaan setiap harinya!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kak Feby manis banget, pembawaannya ceria dan positif",  
                "pesan":"Semoga terus jadi sumber semangat buat orang di sekitar ya kak!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kak Hafsa keliatan sabar banget dan punya aura tenang",  
                "pesan":"Tetap semangat ya kak! Semoga semua impiannya tercapai"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas, Jati Agung",
                "hobbi": "Dengar musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla lembut dan ramah banget, enak diajak ngobrol santai",  
                "pesan":"Semoga kuliahnya lancar dan makin berprestasi ya kak!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania seru banget, pembawaannya santai dan friendly",  
                "pesan":"Tetap semangat dan jangan lupa main roblox buat healing"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangnya kalem tapi lucu, asik banget pas diajak ngobrol",  
                "pesan":"Sukses terus bang, semoga makin banyak rezeki dan hal baik!", # 1
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana kelihatan pintar dan sopan banget",  
                "pesan":"Semangat terus ya kak, semoga selalu jadi inspirasi buat banyak orang!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra kreatif banget, keliatan dari cara dia cerita",  
                "pesan":"Terus berkarya ya kak! Dunia butuh banyak orang kreatif kayak kakak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah balau residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak Eigi punya vibe kalem dan elegan banget",  
                "pesan":"Semoga terus bahagia dan sukses di bidang yang kakak suka!"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Romauli enerjik banget, pembawaannya ceria dan percaya diri",  
                "pesan":"Terus semangat ya kak! Semoga makin bersinar di tiap langkah"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()




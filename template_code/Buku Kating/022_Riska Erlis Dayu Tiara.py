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

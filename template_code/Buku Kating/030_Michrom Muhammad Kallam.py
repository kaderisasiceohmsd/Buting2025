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
            "https://drive.google.com/uc?export=view&id=1XdRcsin7o6O0VxhqUdIyDwZg1oaxCWi8",
            "https://drive.google.com/uc?export=view&id=1RObr_89hbFVwjZfOGijyjuGrDxQXfT4s",
            "https://drive.google.com/uc?export=view&id=1hNkYRqG4j7MHcl584OHagDtW89CnBCdZ",
            "https://drive.google.com/uc?export=view&id=1NGguvjDfVe61pI9t9UEw2gKGLq6uzgnJ",
            "https://drive.google.com/uc?export=view&id=10S0mN8RxCLaszLbSJz3QiHXmWhqP_9nH",
            "https://drive.google.com/uc?export=view&id=1eqrKO3Uvfz9UBpapxzTgCQXjY1cYJU0V",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau Damar",
                "hobbi": "Ikut lomba burung murai",
                "sosmed": "@_erendraa",
                "kesan": "Keren, asik gacor, kece abiss bang kahim",
                "pesan":"sehat dan semangat trus bang"#1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren abiz, berwibawa banget abangnya",
                "pesan":"semangat terus kuliahnya bang kuliahnya"#1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Ayres kost",
                "hobbi": "Jajan",
                "sosmed": "@celisabethh_",
                "kesan": "kakanya asik, kece, ceria truss",
                "pesan":"bahagia dan semangat selalu kak"#1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakanya jarang ngomong tapi vibesnya adem",  
                "pesan":"sehat dan semangat selalu ya kak"#1
            },
            {
                "nama": "Eksanty F Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Kelagian Kecil, Pahawang",
                "alamat": "Pesawaran",
                "hobbi": "Ngambilin Lanyard",
                "sosmed": "@eksantyfebriana",
                "kesan": "asik dan kece abis kakanya",  
                "pesan":"Bahagia dan sukses selalu kak menjalani kuliahnya"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Gya kost",
                "hobbi": "Cute",
                "sosmed": "@farahanumafifahh",
                "kesan": "keren, asik banget kakanyaa",  
                "pesan":" semangat kak kuliahnya, jangan lupa istirahat"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gW3QSaGRG-XA7Td8goIc0K_MKH_pWC4S",
            "https://drive.google.com/uc?export=view&id=1xht58sWSeTPmQqEZMawMiYj6x6caLbQF",
            "https://drive.google.com/uc?export=view&id=1lr-oARJusmmu7NfoursVBoprmQgIjrOv",
            "https://drive.google.com/uc?export=view&id=15AQcYWKdIdMrAyO3OwYPjt_S-xNCFUAC",
            "https://drive.google.com/uc?export=view&id=1sTRaYDX-ddM91YMTD77kSCKw6TDLoBY6",
            "https://drive.google.com/uc?export=view&id=1i__9eKwVZR_rBcWMjS1hHIPVvliwuCbK",
            "https://drive.google.com/uc?export=view&id=1vqwhfBKywOC5SGzrI_i0Crxl6vop32Jt",
            "https://drive.google.com/uc?export=view&id=1ak6tkkipvdzOEVuPnA9hicIgcNZlDlK6",
            "https://drive.google.com/uc?export=view&id=1445kqOCQR0kkFgvszhkG7VeR69TeQ8S7",
            "https://drive.google.com/uc?export=view&id=10wBXnzKsRr-9xqnkHaxGWpcwUkMnBBm6",
            "https://drive.google.com/uc?export=view&id=1XunpvdMYdzcS2GPXnCf7ZrcO7LooOJ1P",
            "https://drive.google.com/uc?export=view&id=1o3Ync_lEdS6PcMp-iEAIeVH3D7N5lyR4",
            "https://drive.google.com/uc?export=view&id=1LUbwqfU8PAeghueMyoZwJfyerzrp3PWS",
            "https://drive.google.com/uc?export=view&id=1UFL0W23Tu6JMx31SZH7lWXbedRa_F2Ac",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Tanjung Morawa",
                "alamat": "B2 no 2",
                "hobbi": "main volly bareng feby",
                "sosmed": "@jeremia_s_",
                "kesan": "Baik, Asik, keren banget bang jeree!",  
                "pesan":"Tetep jadi orang kece dan solid bangg!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "kalo badmood liat zaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "kakanya baik, lucu dan seruu",  
                "pesan":"sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin Alat Pancing",
                "sosmed": "@renishapg",
                "kesan": "kece banget kakanya, seru abiss",  
                "pesan":"semoga harinya berjalan baik dan kuliahnya lancar kak!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Wakatobi",
                "hobbi": "Bowling",
                "sosmed": "@ansftynn",
                "kesan": "kakanya asik dan enak diajak ngobrol serus abizz",  
                "pesan":"sehat selalu dan semangat trus kakk"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "keren, gacorr abangnya, kece abiss",  
                "pesan":"Semangat untuk kuliahnya bang!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Wai huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "agak kalem, asik parah tapi kakanya,",  
                "pesan":"semangat menjalani kuliah dan segala urusannya kakk"# 1
            },
             {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "abang gacor, asik, seru abis bang givaro",  
                "pesan":"semangat trus dan sehat selalau bang!!"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain Makanan Baru",
                "sosmed": "@myrrinn",
                "kesan": "sangat keren dan berkahrisma",  
                "pesan":"Terus semangat bang pantang menyerah bangg!"# 1
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "ngumpulin batu unik dipantai",
                "sosmed": "@berlyyanda",
                "kesan": "baik, kece, lucuu kakanya",  
                "pesan":"semoga hari harinya menyenangkan kak"# 1
            },
             {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "20",
                "asal":"Teluk Mondawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "baik, vibesnya positif banget kaka ini",  
                "pesan":"bahagia terus kakk, semangat truss!"# 1
             },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "keren abang ini, kece parah",  
                "pesan":"semoga lancar terus perkuliahannya bang"# 1
            },
             {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin ka wawa ngomong",
                "sosmed": "@fer_yulius",
                "kesan": "asik, baik dan seru banget",  
                "pesan":"semangat trus bang dengerin kak wawa yapping"# 1
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML hero semua franco",
                "sosmed": "@Monica_tjg",
                "kesan": "keren dan kece abis kaka iniii",  
                "pesan":"semangat truss kak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "baik, lucu kakanya",  
                "pesan":"semoga makin sukses kedepannya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FwAZiXqVjJ7uKW-I4uDAW8EOEI6_cpZZ",
            "https://drive.google.com/uc?export=view&id=1_q2rU0sEyBGw_hDLRG_mL67m11hRWuXC",
            "https://drive.google.com/uc?export=view&id=18VvrVsDMGBRDhN-KhttOwhK5sm-mDepO",
            "https://drive.google.com/uc?export=view&id=1PBWoHQCy-Ld4v1lyBhyrikSk1w4Lsn06",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "keren banget bang senator, tenang banget pembawaannya",  
                "pesan":"jaga kesehatan bangg"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjanani",
                "kesan": "keren banget kak, kerenn",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Denger musik sambil jalan",
                "sosmed": "@fathinahazzh",
                "kesan": "baik, asik banget kaka ini",  
                "pesan":"bahagia dan sukses selalu ya kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main",
                "sosmed": "@lia.h_264",
                "kesan": "kece banget kaka ini",  
                "pesan":"semangat trus kak, pantang menyerahh"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WXkfjWI88WBF4CQJyWA0MYa4HZt8vxwF",
            "https://drive.google.com/uc?export=view&id=1QB_etVXTxNqkpgFNBZ6U1vy_yBKvAWug",
            "https://drive.google.com/uc?export=view&id=1UhQiBVJzB75eM1m1nMw4gV-iiZ5bUoZd",
            "https://drive.google.com/uc?export=view&id=1YfMaFmAWuliXVbc3ya_WwWSwWZFropds",
            "https://drive.google.com/uc?export=view&id=1ZY_xANzRiavKTAgvmpAmH1VJFpvPML1o",
            "https://drive.google.com/uc?export=view&id=1hvn80_UYZmfUr0qY6qM6dsmD_lgHZVyx",
            "https://drive.google.com/uc?export=view&id=13kpxsWKtCL9b3s13jJYv9HejS9a6L10o",
            "https://drive.google.com/uc?export=view&id=1Ah8TvSvctfUCKw5vI1TdPPPYOoNB5JBC",
            "https://drive.google.com/uc?export=view&id=1KX4DWxvFcCrrDQm9rqzvdgH03VYKCJ53",
            "https://drive.google.com/uc?export=view&id=1PH8vH4JGOYayID8CaNdPCtDFoMRZyKN3",
            "https://drive.google.com/uc?export=view&id=1Ve7QawSCjLniAkgzXsYvCpJVNn-ahBcT",
            "https://drive.google.com/uc?export=view&id=12x4rY2yfwsw_e8e-fWaksxb1kMH9LpGN",
            "https://drive.google.com/uc?export=view&id=1UaUGCvQBamJy5MTR4rk8kz9UoUW1IiFg",
            "https://drive.google.com/uc?export=view&id=18ontdr8QBvQ5jEecHEsCiiloEPNrhV8w",
            "https://drive.google.com/uc?export=view&id=1aPHWQwPIaptNqIKjqFYvAL4Gt_yVxIe-",
            "https://drive.google.com/uc?export=view&id=14g4nexP8QTQ0cvm8xHusVcORnI-_6I14",
            "https://drive.google.com/uc?export=view&id=1isA4OkHLlD3QF5h-vrDt9rzZ9rAlc2Z-",
            "https://drive.google.com/uc?export=view&id=1Gjubj83s-EdKs9mbFcEb33CdQyRPDEFh",
            "https://drive.google.com/uc?export=view&id=1aXkZq0t39mQfZvUzoDIgCM885PL_Ij67",
            "https://drive.google.com/uc?export=view&id=1_miJFBNejiGQCRkzHwZbZY9N-tNJU4DV",
            "https://drive.google.com/uc?export=view&id=11mjoBCGPebxkgQW2aPqVXhqjsWl6hYm5",
            "https://drive.google.com/uc?export=view&id=1rpCWRlP32Xh0eUZ74HFpIUCLJ2hCm3T7",
            "https://drive.google.com/uc?export=view&id=13moeh7SAqtkCzsforERWgb4CmRCsoXjU",
            "https://drive.google.com/uc?export=view&id=1hhBk2vDYchdFVgcBr2fICsquuXsgGHMP",
            "https://drive.google.com/uc?export=view&id=1CnI59po99dB-RWH6I-yAI9stwH4ycDkq",
            "https://drive.google.com/uc?export=view&id=1n6m33RHVWrfwnP_S9Z4tgQHpfpObJTtg",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Keren banget dan xool banget abang ini",  
                "pesan":"Semangat ngejalanin kuliahnya bang"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "lucu, asik, imut kaka ini",  
                "pesan":"semangat menjalani harinya kak"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main apapun",
                "sosmed": "@allyapasha_",
                "kesan": "keren, tegas, berwibawa kaka ini",  
                "pesan":"semangat trus kak, dilancarkan segala urusannya"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "kontrakan GH",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky",
                "kesan": "keren banget bang, panutan banyak orang",  
                "pesan":"semangat trus bang kuliah dan organisasinya"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Samping kost daffa",
                "hobbi": "Main Sudoku",
                "sosmed": "@arientakhsnl",
                "kesan": "keren banget, kece banget kak",  
                "pesan":"tetep jadi contoh keren untuk kami kak"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jailin putri",
                "sosmed": "@daffahdynn_",
                "kesan": "keren,tegas abiss ",  
                "pesan":"semangat dan sukses sselalu bang"#1             
            },        
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_nrp",
                "kesan": "kece dan cool banget bang",
                "pesan": "semangat kuliahnya bang fajar"  # 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"pasar muara beliti",
                "alamat": "kost putri, gerbang barat samping sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "baik, asik, dan seru banget kak",  
                "pesan":"jaga kesehatan dan semangat trus ya kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Urip",
                "alamat": "Belwis",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "abang cool, kece abis",  
                "pesan":"sukses dan sehat selalu bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma fam",
                "hobbi": "ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "Tegas,tapi keren baik banget",  
                "pesan":"semoga harinya berjalan baik ya bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "maju jaya kost",
                "hobbi": "yapping sampe bete",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Baik, asik, kece abiss",  
                "pesan":"semangat terus kak ngejalanin kuliahnya kak"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Lari",
                "sosmed": "@sahid22_",
                "kesan": "kece, keren banget bang",  
                "pesan":"semangat bang, bahagia selalu"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "nangka 4, sukarame",
                "hobbi": "Main game + kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "baik keren abangnya",  
                "pesan":"jaga kesehatan bang, dan semangat trus"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "lucu, asik, baik, keren abizz",  
                "pesan":"jaga kesehatan ya kak, semangat"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kece dan keren banget",  
                "pesan":"semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kaka ini baik, santai dan kece",  
                "pesan":"sukses selalu kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul9",
                "kesan": "asik dan baik banget, keren abis pokoknya"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "keren dan asik banget bang, gokill",  
                "pesan":"sukses dan bahagia selalu bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.lapas raya no 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "kakanya kece dan seru",  
                "pesan":"semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Bikin project, ngoleksi data",
                "sosmed": "@ihsan.myusuf",
                "kesan": "keren, asik, cool abis",  
                "pesan":"jangan berubah bang!"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Padang Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "cool,jece abis bangg",
                "pesan": "semangat dan sehat selalu bang"  # 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakanya asik dan juga santai",  
                "pesan":"semoga harinya menyenangkan kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Lempar Batu",
                "sosmed": "@m.ridwan_22",
                "kesan": "baik, seru, dan asik banget bang ini",  
                "pesan":"stay positif bangg"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "baik,keren, humoris abang ini",  
                "pesan":"jangan lupa istirahat dan semangat selalu bang"# 1
            },
            {
                "nama": "Uliano Wiliam Purba ",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main musik, ngoding, menanam anggrek",
                "sosmed": "@nano.wlm",
                "kesan": "orangnya serius, kece juga tapii",  
                "pesan":"bahagia dan semangat selalu bang"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Bengong",
                "sosmed": "@rewinanaaa",
                "kesan": "baik, santai,asik dan seru",  
                "pesan":"selalu jaga kesehatan dan semangat selalu"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jXRunR7BKxlzpUxti0vh6un-vDjcofSE",
            "https://drive.google.com/uc?export=view&id=1Av7KmpGb7UBkXJzeD2eOi3i83be2cWMr",
            "https://drive.google.com/uc?export=view&id=1-NKF13Axsi04JaOe0ky4Lsy2ZernqyCr",
            "https://drive.google.com/uc?export=view&id=1RV2achKgQ_mIKp0rYjmTY85Cy43IbOiM",
            "https://drive.google.com/uc?export=view&id=1ghGkHRPAQEyoxGAjoZ-arj0AsbZRD4L0",
            "https://drive.google.com/uc?export=view&id=166QYeUo-nfOuMW-r66nSBXmxDLNWdkgc",
            "https://drive.google.com/uc?export=view&id=19ZmqSri9Eh3sKLfwwcAx7Bx0m2hqeyyq",
            "https://drive.google.com/uc?export=view&id=1eEvRX8QG54p_HjofCGNGdIgflixuF5CH",
            "https://drive.google.com/uc?export=view&id=1pAt9fHyLSKzEvQM7TnmqHi84yG6GN1KV",
            "https://drive.google.com/uc?export=view&id=1xbBiLtWlrsiQlWft9XK8h8qPSupTBN2p",
            "https://drive.google.com/uc?export=view&id=1_2HTP8-7pNzVK_yLlcpC065DA2UJlRu_",
            "https://drive.google.com/uc?export=view&id=1zcbR2c6_Y8rlZXbNQlni6XQHzzM2Ex3g",
            "https://drive.google.com/uc?export=view&id=1rK9EHUUsKjl7DrA4bOl8eCvDIy7wgX86",
            "https://drive.google.com/uc?export=view&id=1AfccopiYU-vtGjUvww0UT31WnZq0bfvR",
            "https://drive.google.com/uc?export=view&id=1KgGrKBxoCMJUrDKJJjvYtr8NKdEWIhlU",
            "https://drive.google.com/uc?export=view&id=1reQHHw93_yTVFrBaiPAZEMqj4M_gi8H6",
            "https://drive.google.com/uc?export=view&id=1XCFVb8YrTwCDpGvaEFPTqNygvLL9rJBM",
            "https://drive.google.com/uc?export=view&id=1ZLPW2fKDtIaWpsgj-AwVHz6b1hqRs6tC",
            "https://drive.google.com/uc?export=view&id=1QgC7Y30VM5l9jXidEHymSB-PpKBeyxu_",
            "https://drive.google.com/uc?export=view&id=1JzkYasWsokwQaEsbp2AX9Xew1FPwslp2",
            "https://drive.google.com/uc?export=view&id=1CDuM4lIkpmCm4Yclxf9kCVQ1xnZhGPKm",
            "https://drive.google.com/uc?export=view&id=1mxQ57d-vnYYAg8Jrr08pHqSLbbm1WUhA",
        ]
        data_list = [
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "keren, kece abis abang ini",
                "pesan":"Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@junitaa.0406",
                "kesan": "Kakaknya asik, baik, suka sharing ilmu",  
                "pesan":"selalu semangat menjalani harinya bang"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "kece, keren abis pokonyaa",  
                "pesan":"Semangat kuliahnya bangg" # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakanya baik, seru asik diajak ngobrol",
                "pesan":"stay positif kakk"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "mudah bergaul, dan keren banget orangnya",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya bang"#1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Keren banget bang, kece",
                "pesan":"Semangat kuliahnya"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tj. Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya baik, santai orangnya asik orangnya",
                "pesan":"Semangat terus bang kuliahnyaa"#1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "jl. Manggis 1",
                "hobbi": "Nonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "kkalem, baik, seru kakanya",  
                "pesan":"teteap semangat kakk"#1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "kakanya baik, asik, bawaannya ceria terus",
                "pesan":"semangat menjalani harinya kak"#1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abangnya baik, asik, santai",
                "pesan":"selalu keren bang dan kece bangg"#1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "baik banget, keren pokoknyaa",
                "pesan":"Ssemangat kuliahnya kak"#1    
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jl. Raden Saleh",
                "hobbi": "jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Seru banget, baik, asik",
                "pesan":"semangat terus kak kuliahnya"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan Bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "kalem, seru abis kakanya",  
                "pesan":"semangat terus kak, keep positif"#1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "keren, ramah orangnya",
                "pesan":"Sukses dan semangat selalu kak"#1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama ITERA TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "keren, kece banget",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak"#1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "sepuh koding ini, keren banget",
                "pesan":"semangat trus ngodingnya bang"#1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak asik, santai, keren pokoknya",
                "pesan":"Semangat terus untuk kuliahnya kak"#1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "kece, baik banget",
                "pesan":"semangat terus bang kuliahnya"#1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya pinter, kalem, seru",
                "pesan":"semangat trus menjalani harinya bang"#1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "orangnya tenang, kecee",
                "pesan":"semangat terus kuliahnya Kak"#1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "seru, baik, enak diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kak,"#1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Baik, asik banget bang",
                "pesan":"Semangat Futsal dan kuliahnya bang"#1
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()
       

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qD53sS_t-bzVJgpiJ8eH9gJpeNVJ0y5k",
            "https://drive.google.com/uc?export=view&id=17HpnA4NmLt0rQXyFaJmPeuqpiw-4KzvF",
            "https://drive.google.com/uc?export=view&id=1kCYjpa0uTVEUK1ys61eg2b6Pk0rCaVHZ",
            "https://drive.google.com/uc?export=view&id=1WIW_gtapKnJl1ydhGn36fYQDj4JBN9HI",
            "https://drive.google.com/uc?export=view&id=1ts8moX117s8n9BkRcbt-KIpMeyKr2a64",
            "https://drive.google.com/uc?export=view&id=1x67-fOVhq1nkfxW_G1_oA-eF64rGNRq6",
            "https://drive.google.com/uc?export=view&id=1JFTzxF7f0VQuulG44qIxvF555BNJYPnK",
            "https://drive.google.com/uc?export=view&id=1xrYKJgvgpCjGGzOO4pRRxC18jPF0iFt0",
            "https://drive.google.com/uc?export=view&id=1plcHF1D4a2CvzxrBFMIsAjoiENxyjBi-",
            "https://drive.google.com/uc?export=view&id=1EkPVGMq0149KyGFJjFkazMwS0Gl5k3BC",
            "https://drive.google.com/uc?export=view&id=1jmkz5qH8KUMMKHvvdPh0zZhfQzKiRyOg",
            "https://drive.google.com/uc?export=view&id=1uQk7szjXHZfcs7LBAIISm5q6FinXJcNC",
            "https://drive.google.com/uc?export=view&id=12FHAuaHWVpO9Fv57RgRuQhFAnAiyF2Hy",
            "https://drive.google.com/uc?export=view&id=1TdcFr91EIgriEJzifrkI727M8RGN9yHI",
            "https://drive.google.com/uc?export=view&id=1ZYcKkfRxFfoPPQE14RZWIFHUp1eOwmPK",
            "https://drive.google.com/uc?export=view&id=11bOiBGkwKnS7tO3w-MNAkjHvTEywkavA",
            "https://drive.google.com/uc?export=view&id=1KcQzKMNNY4Id9Q42npEfbW1pm4ggbM5J",
            "https://drive.google.com/uc?export=view&id=1Iqo1HJMPHJRrLGP90DayvII4qIGaWiO6",
            "https://drive.google.com/uc?export=view&id=13Kuh2D_E1pMWmUsvxW3GDZtcaJaaNOY8",
            "https://drive.google.com/uc?export=view&id=1ckYkq2dbtNPD4Ua3boSY7NI8IDAmm6vk",
            "https://drive.google.com/uc?export=view&id=1eeZBykjTGp-wBzSTDUM0MqSijW52VteT",
            "https://drive.google.com/uc?export=view&id=1N7yC0q4psfn4pYK3-GEG2rXvBI179DD_",
            "https://drive.google.com/uc?export=view&id=1zPWB8fPB1hYOrFyGaqs2x9Ls18Qmqeei",
            "https://drive.google.com/uc?export=view&id=1k6X2HirTy9LYzX3zy7wNZ7F9GgeRJYpP",
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "keren parah bang",
                "pesan":"Semangat kuliahnya bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Baik banget kakaknya ramah juga",
                "pesan":"jangan lupa tidur kak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "kakanya baik,keliatan ceria",
                "pesan":"Semangat kak!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "kakaknya seruparah orangnya",
                "pesan":"jangan lupa makan"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "abangnya mntep pokoknya",
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "asik parah gokil",
                "pesan":"semangat kuliahnya, jangan lupa makan"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "seru diajak ngobrol",
                "pesan":"semangat!!!!!!!!!!!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakanya keren,baik lagi",
                "pesan":"semangat kak"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abangnya asik poll.",
                "pesan":"Semangat terus untuk kuliahnya bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "ceria banget",
                "pesan":"selalu semangat kak jangan lemes"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya asik",
                "pesan":"Selalu jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "kakanya baik",
                "pesan":"Sehat selalu kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya lucu, asik,baik bener orangnya",
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "kakanya asik ",
                "pesan":"Jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Orangnya menyenangkan dan keren.",
                "pesan":"jangan lupa makan"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya baik, ramah, asik",
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya asik dan keren poll",
                "pesan":"Selalu jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kakanya asik dan baik banget",
                "pesan":"Semangat kuliahnya"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya menyenangkan",
                "pesan":"Semangat kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak baik dan ramah",
                "pesan":"Jangan lupa jaga kesehatan ya kak."# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya asik dan seru untuk diajak ngobrol",
                "pesan":"Semangat terus kak!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakanya baik ramah dan lembut",
                "pesan":"semangat kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya asik, ramah juga",
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Baik, asik dan mudah bergaul",
                "pesan":"jangan lupa tidur"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1k5LzgmfS-2gZw8AphCE1iBvAP9YK48MU",
            "https://drive.google.com/uc?export=view&id=1sHd_GBQGUwQN7LxzfGAbgi23iO4bUd9X",
            "https://drive.google.com/uc?export=view&id=1nnCPwGbCFmyPBiRoEpoPahSWhBkxGJ_A",
            "https://drive.google.com/uc?export=view&id=1rvyzPc4bU5HYI3evEIvpo7ZtMkLdYtKG",
            "https://drive.google.com/uc?export=view&id=1dWRe4P56BcOewJpd1z7E0JaQaTOYaiJX",
            "https://drive.google.com/uc?export=view&id=1BskHAZdng1k4Q3y4TzyGCWXbVGUvmI4i",
            "https://drive.google.com/uc?export=view&id=1O7UbN_69Nt9wbv_N6V1CK1ClTQ-nHDld",
            "https://drive.google.com/uc?export=view&id=1UIUgdQheg06_ke0zRZDJa-VWE4Rro713",
            "https://drive.google.com/uc?export=view&id=1bEKSX1-ypVJGt1R3BiP9jWoY3TvMALxL",
            "https://drive.google.com/uc?export=view&id=1cyCueSxfbQ6EsYXSV8N1nkEaZH2rzAGt",
            "https://drive.google.com/uc?export=view&id=1Ymkco-IQGXWgANHZdJmqVwGo2JVfrx15",
            "https://drive.google.com/uc?export=view&id=1we0ZR2kUENI5LmpmJ8nl3WfazxwxiRpD",
            "https://drive.google.com/uc?export=view&id=1WxlEiNtVOQfYPWdPO2n43VarDHmbww-x",
            "https://drive.google.com/uc?export=view&id=15SAFqxTO6C3ywpycoYYlwA5w2umTwYQx",
            "https://drive.google.com/uc?export=view&id=1jyfUwVQGbEbBTqihijeoV91GWLlJZpGS",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik banget dan ramah.",
                "pesan": "Sehat dan semangat terus ya kak!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Semoga urusan kuliahnya lancar selalu, Kak"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Senang bisa kenal sama kakak.",
                "pesan": "Sukses terus buat ke depannya ya Kak!"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya ramah banget.",
                "pesan": "Sehat dan bahagia selalu kak!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya baik, seru dan asik",
                "pesan": "Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asik banget.",
                "pesan": "Sehat selalu ya kak!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "kakanya baik dan positif vibes banget kak.",
                "pesan": "Selalu semangat ya kak!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalghani73",
                "kesan": "Abangnya asik, baik, ramah",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya baik dan asik banget",
                "pesan": "semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya humble dan asik diajak ngobrol",
                "pesan": "Selalu jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik, asik dan friendly banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya baik dan seru.",
                "pesan": "Semangat terus kak!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semoga urusannya dipermudah selalu bang"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya asik untuk diajak diskusi.",
                "pesan": "Lancar-lancar ya kak kuliahnya."# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Rubik Mirror",
                "sosmed": "@zhrptsl",
                "kesan": "kakanya asik dan seru",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AffdRWLBlqYgzEsFw1_Z-3DmjWnVW5qs",
            "https://drive.google.com/uc?export=view&id=1BDU0jyk8sOYmmzNBRsmbc6mmOB7AUpiI",
            "https://drive.google.com/uc?export=view&id=1e2PxIZBLBWpWzHSSip-c-WcO6q1Xr4Ae",
            "https://drive.google.com/uc?export=view&id=1WcUyl0deeDlrsWA_4_wsNqYYHWBKFLnw",
            "https://drive.google.com/uc?export=view&id=1TXs8bbSHyu_M2QOkaIokqp5K_l3i7o0n",
            "https://drive.google.com/uc?export=view&id=1xeoOc1s-8gTFOeuNG7FHa_-I94i9flmu",
            "https://drive.google.com/uc?export=view&id=1bfxQ0ciGxd54Ds5soVD319mYQY1LrDLX",
            "https://drive.google.com/uc?export=view&id=1iF_C2yVhrXBuC9skyeYlD7J6xxcmUC2z",
            "https://drive.google.com/uc?export=view&id=1Yon_NYrXR--HwfqkQjIkJvY-iwKY4ZP5",
            "https://drive.google.com/uc?export=view&id=1qQeWdVPopkf4PlwSzRRK-Z2W60H250tw",
            "https://drive.google.com/uc?export=view&id=19eUoWLGccKAcWedHCQ22dZRULMkM6T5W",
            
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya asik dan seru.",
                "pesan": "Semangat terus bang"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Senang bisa berkenalan dengan kakak.",
                "pesan": "Semoga sukses selalu kuliahnya!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya ramah dan baik.",
                "pesan": "Sehat selalu ya, bang."# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif.",
                "pesan": "Semangat terus kuliahnya, kak!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "Semoga semua urusannya dilancarkan."# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Semangat terus ya, kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya asik dan menyenangkan",
                "pesan": "jaga kesehatan selalu ya bang"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya kak!"# 1
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu ya kak!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Jaga kesehatan selalu kak!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakanya baik, asik dan menyenangkan",
                "pesan": "Semangat dan sukses selalu!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WL-xU89k_8PrxlKfHnWYtMYMyGWnVmgw",
            "https://drive.google.com/uc?export=view&id=1jddBM3BquuROCy5aP3FxV_UIH9xfzcGl",
            "https://drive.google.com/uc?export=view&id=1wFv6TkqXPeBxAjaOD_z0ze_PgTN6lzvL",
            "https://drive.google.com/uc?export=view&id=1GviNDTWsoODw7jOAXwA6nIGancgtKa_s",
            "https://drive.google.com/uc?export=view&id=1aG5vjnZZYHkbDAHHZAOwlX0sX7UprAry",
            "https://drive.google.com/uc?export=view&id=1eW-o6E8ZhPOegFwQ-wmp4h_hoaQq7cub",
            "https://drive.google.com/uc?export=view&id=1wWCjD6E8GDNezylPxIz1kekMqNm7kktq",
            "https://drive.google.com/uc?export=view&id=1VMB2OpAqyZkGUWyFHZkNk_uqW1RTizSh",
            "https://drive.google.com/uc?export=view&id=15grZgzSo8WolVEMhY8ohv4UnV76jF3PL",
            "https://drive.google.com/uc?export=view&id=1UdFoa58lZ4FFkjHZbVc4LUPoi41XVK7M",
            "https://drive.google.com/uc?export=view&id=1NnS1jLaH7SVCZDg4DtfwHFwfIdon0pgs",
            "https://drive.google.com/uc?export=view&id=1cgD0wDbtVf7XyHfhxLNLO4G-gAnVJx27",
            "https://drive.google.com/uc?export=view&id=1J5tiIaS64x-g-MLm5cXoy6t6cl23vFXK",
            "https://drive.google.com/uc?export=view&id=1uB4EYv1oNuHzCiCl2GtNFWpvM4kyao6a",
            "https://drive.google.com/uc?export=view&id=1EjbE6Nn95XDy8pOyhIb5E2f_MJSBAHJg",
            "https://drive.google.com/uc?export=view&id=1tQytBDWbC9W1bHdnbtv73H-2jbwDaBKE",
            "https://drive.google.com/uc?export=view&id=19x7zl52xz3JCWGviR6Ycweit2O1-ULaB",
            "https://drive.google.com/uc?export=view&id=1d141LZrSRR08dO49HkYRFW0IQ1gP7_qk",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Sukses selalu ya, kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Belajar sama kakaknya jadi menyenangkan",
                "pesan": "Semoga lancar terus kuliahnya!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Pengalamannya keren dan menginspirasi",
                "pesan": "Teruslah berkarya bang"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abangnya friendly dan asik",
                "pesan": "Sehat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya asik dan seru",
                "pesan": "Semoga sehat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Senang bisa belajar bareng kakak",
                "pesan": "Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya sangat ramah dan baik",
                "pesan": "Tetap semangat kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "kakanya lucu dan baik banget",
                "pesan": "Semangat terus kak, jangan menyerah!"# 1
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Terima kasih sudah berbagi ilmu",
                "pesan": "Semoga sukses di masa depan!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya asik diajak diskusi",
                "pesan": "Lancar terus ya kak kuliahnya!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget",
                "pesan": "Sukses untuk ke depannya, kak!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya seru dan pintar",
                "pesan": "Sukses terus untuk karirnya nanti."# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Sangat berkesan bisa diajar kakak",
                "pesan": "Semoga sehat selalu, kak."# 1
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Orangnya asik dan mudah bergaul",
                "pesan": "Semangat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya sangat welcome dan ramah",
                "pesan": "Semangat terus dan semoga sukses!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Suasananya jadi asik kalau ada kakak ini",
                "pesan": "Jangan lupa jaga kesehatan ya, kak."# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya keren dan inspiratif",
                "pesan": "Semoga apa yang dicita-citakan tercapai."# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya ramah dan humble",
                "pesan": "Selalu jaga kesehatan ya kak."# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
# Tambahkan menu lainnya sesuai kebutuhan


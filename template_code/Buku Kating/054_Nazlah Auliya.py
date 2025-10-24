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
            "nav-link-selected": {"background-color": "#FF6F00"},
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
            "https://drive.google.com/uc?export=view&id=1cOsQZkMUvz6dY1PptdR8GT8f38aUqOk4",
            "https://drive.google.com/uc?export=view&id=1TvDapFXOfg2b-VCcsY0Eay-3iF17eOLA",
            "https://drive.google.com/uc?export=view&id=1JH4al1fJ_zqRM8TMD7L1qgcOe4E6i3d7",
            "https://drive.google.com/uc?export=view&id=1igxoVCaD_rerlhjQJymBZFa8Le7T_6BP",
            "https://drive.google.com/uc?export=view&id=1Lj2T66wAUnFq_MLD0rb9AgO4FXO7iFKc",
            "https://drive.google.com/uc?export=view&id=192guc9FQpQKtwsiWIeyPIApuKOLmP2AQ",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@erendraa",
                "kesan": "kalo abang ngomong, pasti di denger, kharismanya kuat banget, vibes kepemimpinanya kerasa banget",  
                "pesan":"semoga segala urusannya dipermudah, sukses selalu bang n jangan lupa istirahat ya"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "abangnya tegas tapi asik kok",  
                "pesan":"Semoga apa yang abang impikan bisa tercapai."
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Selalu kelihatan tenang dan anggun bangett",  
                "pesan":"semangat menjalani harinya kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "lucu banget kak, ramah dan kalem juga",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "pinter banget kakaknya, asik kalo diajak ngobrol",  
                "pesan":"tips pinter dong kak"
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "kakaknya ramah banget, sangat mengayomi pas wawancara",  
                "pesan":"sukses selalu ya kak, semoga segala urusan dipermudah"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZHMMIjni_2o0yDw_EQ9Wpvll4eqqvSl6",
            "https://drive.google.com/uc?export=view&id=1FdHqw2dugDG5UZHEiR0lXTyImg77WlnI",
            "https://drive.google.com/uc?export=view&id=1cWCbyXqWgAjMzFjdw_-biI5MPtoldlag",
            "https://drive.google.com/uc?export=view&id=17cD8o83jBPEuQBi9VsvSwZ248BFcy4Pn",
            "https://drive.google.com/uc?export=view&id=1ZHMMIjni_2o0yDw_EQ9Wpvll4eqqvSl6",
            "https://drive.google.com/uc?export=view&id=19G1HcwaPOwqlkPLBGI-lsfRACeHdpx5z",
            "https://drive.google.com/uc?export=view&id=1nZ3mteYyTSVqiJLRfzBolkjgxu4JgTUS",
            "https://drive.google.com/uc?export=view&id=1cPgNuv88EcF9p__8LmF27o7GDSDeiqTI",
            "https://drive.google.com/uc?export=view&id=1IIG5mrIy7uS4mUADGXkfkLmSxklaEg0C",
            "https://drive.google.com/uc?export=view&id=1oWJpUZPOyd5F20zzWCpS8KjsTd2h2XTO",
            "https://drive.google.com/uc?export=view&id=1LoCs4YSmIWhoZZlbhawlQw-MtTNS1o4d",
            "https://drive.google.com/uc?export=view&id=1OEtC4QbDeVnaf5wu8WPe_xbJvDp79_tl",
            "https://drive.google.com/uc?export=view&id=1RNEKzuMXT1BeYbNg0mx3r_tWEGrHaucb",
            "https://drive.google.com/uc?export=view&id=1hukhl0ccoKC_80g23hK_x8c8WC9DIY43",
            
            
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122340022",
                "umur": "21",
                "asal":"Nusa Kambangan",
                "alamat": "Lapas, Belwis",
                "hobbi": "Melarikan diri",
                "sosmed": "@jeremia_s_",
                "kesan": "humble banget, mudah diajak ngobrolnya pembahasannya ga ngebosenin  ",  
                "pesan":"selalu jadi pribadi yang baik bang"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "ternyata kakaknya se humoris itu dan jadi penyair suasana",  
                "pesan":"semangat menjalani kehidupan kuliah ya kak"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "type cantik yang deep gitu... ",  
                "pesan":"sukses selalu kakak cantikk"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Kakaknya baik, gayanya sederhana tapi tetap elegan, keren banget.",  
                "pesan":"Kak, semoga selalu dikelilingi orang-orang baik"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "abangnya pinter banget, selalu kagum argumen yang di sampaikan",  
                "pesan":"Teruslah jadi orang baik tanpa perlu banyak alasan"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Kak feby lucu banget pliss, daari awal selalu salfok ama rambutnya",  
                "pesan":"tutor biar rambutnya sehat kak, jangan lupa istirahat kak"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "abangnya asik kalo diajak ngobrol bukan type yanng ngebosenin",   
                "pesan":"semangat kuliahnya bang"
           },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "vibesnya cowok cool yang suka nge game",  
                "pesan":"sukses selalu bang, semoga lulus tepat waktu"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "kakaknya ceria banget dan ekspresif sekal, suka deh pokoknya",  
                "pesan":"Tetap semangat walau kadang idup gajelas hehe "
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "vibesnya bikin sekitar jadi ceria dan bikin nyaman orang",  
                "pesan":"semoga kakak selalu dikelilingi kebaikan yaa"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Keren banget bang,type cowo cool abizz",  
                "pesan":"semoga harai hari kakak penuh dengan warna"
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "type yang enjoy banget bang",  
                "pesan":"semangatt kuliahnyaa"
          },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "-",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "orangnya hunble dan seru kl diajak berdiskusi",  
                "pesan":"jangan lupa istirahat ya kak"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lucu banget, suka ngajak ngobrol orang sekitar",  
                "pesan":"semangat mengejar cita- cita kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ske-zjIKF8qOnI5OWp5Vibf4uYae8bPi",
            "https://drive.google.com/uc?export=view&id=1kOXfXNOVJKZj7SW0Ezh9mrcZutHPX1K3",
            "https://drive.google.com/uc?export=view&id=16Dd6OXonwxHA56CjRQMgsbQGyo_ey_rZ",
            "https://drive.google.com/uc?export=view&id=1h90wemBQN5vZl4BBsq-rAvXtlxRjMz6Z",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Tanya Caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "orangnya berwibawa banget dan punya jiwa kepemimpinan yang kuat, keren pokoknya",  
                "pesan":"sukses teruss bang "# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "vibesnya calm tapi tegas, lucu banget kalo senyum",  
                "pesan":"semangat menjalani harinya kak dan jangan lupa istirahat yang cukup"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "kakany kalem tapi asik diajak ngobrol juga",  
                "pesan":"sehat selalu kakk"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "vibesnya sama kaya kak fathinah, kalem tapi asik diajak ngobrol juga",  
                "pesan":"tetep jadi kakak yang baik yaa"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cUp7Xs6WH4tjNMP0vIZr778PfJKnczyD",
            "https://drive.google.com/uc?export=view&id=1aec-tDvL5fZWFkmpz0qzBP1SE6b3lz08",
            "https://drive.google.com/uc?export=view&id=1LAbU_Rwynbp_SSvPw46S2YTKo2ufV_r7",
            "https://drive.google.com/uc?export=view&id=1NYE_ps40EfbUVbvJVDvTWVFWbedp-RxD",
            "https://drive.google.com/uc?export=view&id=1jEkYVUywaz6FEU-3ID2rPvxOl0l5s-Yq",
            "https://drive.google.com/uc?export=view&id=1acjzZgLgvxGUWjd58Ch0XfeUIVL6rTP_",
            "https://drive.google.com/uc?export=view&id=1zl7hTlblxRoRtXFUbYBtH_Ho8QVBzmrS",
            "https://drive.google.com/uc?export=view&id=1UmpRy8VXxZbv_GMuQWzXp48SOMPz_dP-",
            "https://drive.google.com/uc?export=view&id=1LUPT5KBiZjhajSMCwEhna3Q5wyRuYK2u",
            "https://drive.google.com/uc?export=view&id=1QHSbc_MCvShrEI3JQP-TPubhKy2HRTEh",
            "https://drive.google.com/uc?export=view&id=1uMHUujTc-vmXq0w0dZzsvhUtS-Zooisa",
            "https://drive.google.com/uc?export=view&id=1hvfKW_TAr8lzUUBYp7iari570Qf3Hb2u",
            "https://drive.google.com/uc?export=view&id=10fONoWyp38iCc82HHCCE8YUG9dwritd-",
            "https://drive.google.com/uc?export=view&id=1V_NXo2eHZXNiJFshr71M0eklxc2420rz",
            "https://drive.google.com/uc?export=view&id=1_c3iEGwtHarsvQqNcXkt2HXDB9arxAIW",
            "https://drive.google.com/uc?export=view&id=1KZeEkVVohbJlXL0MIaTB-ugxIzkI9_1v",
            "https://drive.google.com/uc?export=view&id=1gxC_sWwFvdsTzEuyT9I6PIb3LJ9uJ3H4",
            "https://drive.google.com/uc?export=view&id=1BuhelsLFgknjOru3Bz-33UnJk05iXjwZ",
            "https://drive.google.com/uc?export=view&id=14K5WYf5VQS4M9oAti9X43gtW3LaZr0lJ",
            "https://drive.google.com/uc?export=view&id=1i1-Wdl6WCkhIX32qHmVzJWKNdDbn3M4j",
            "https://drive.google.com/uc?export=view&id=1lXdsQGwqg17j5H1uTlAD7c9Sgd8oFfxp",
            "https://drive.google.com/uc?export=view&id=1IJCHSPSVBU7KfOG4lC6i_3jMSp9PSLFy",
            "https://drive.google.com/uc?export=view&id=1-ZHppMuaD9zQ_vLQg0lg8ZKb8ZI9qR-2",
            "https://drive.google.com/uc?export=view&id=1JEWl7iTarYNmlwaJkfD7fY4idvO6UX4m",
            "https://drive.google.com/uc?export=view&id=1qtfy2cPVahlEnTeCBsNDKqepuvoImI6h",
            "https://drive.google.com/uc?export=view&id=1UlCtTEb829AEaDwAHyyzvZCgelpl0Q34",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Tanjung Senag",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "pembawaan nya serius terus dan berwibawa pokoknya",
                "pesan": "jangan lupa istirahat ya bang"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakanya baik banget, ramah sekali, wangi banget kakk",
                "pesan": "semangat kak, jangan lupa jaga kesehatan"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "wanginya khas banget kak, ramah sekali",
                "pesan": "tetap jadi sosok yang inspiratif dan menyenangkan ya kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "keren banget, pinter banget, respect full pokoknya",
                "pesan": "semoga dapat jalan terbaik buat masa depan yang diimpikan"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "sangat menginspirasi sekali kak, walaupun jarang senyum tapi senyumnya manis banget",
                "pesan": "terus jadi pribadi yang menginspirasi kak, jangan lupa makan kak"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "tiap disapa selalu senyum,abangnya keren bangett",
                "pesan": "kurangin begadangnya bang, selalu jaga kesehatan"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "abangnya peduli banget ama sekitarnya, care bangett ",
                "pesan": "semoga selalu diberi kemudahan dalam segala urusan"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "kakak cantik bangetttt, ramah pula",
                "pesan": "semoga selalu dikelilingi orang- orang baik ya kak"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "pinter banget ngodingnya, keren abizz",
                "pesan": "semoga terus berkembang dan sukses selalu bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "berwibawa banget dan punya auran yang tegas jadi orang sekitar nge hormatin banget",
                "pesan": "tetap jadi panutan yang baik yaa bang"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kak vany ramah banget dan lucu sekali",
                "pesan": "terus jadi pembawa positif vibes ke sekitar ya kak"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "abangnya keren banget, walaupun mukanya cocok di kerohania",
                "pesan": "jangan sering begadang ya bangg"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "orangnya santai kalo diajak ngobrol",
                "pesan": "sehat selalu bang"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "bisa deket ama siapa aja, lucu bangett",
                "pesan": "sayangi diri sendiri ya kak, jangan lupa makan "
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya lucu bangett, asik diajak ngobrol",
                "pesan": "semoga kakak punya hari- hari yang menyenangkan"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "vibesnya kalem, pinter banget kalo soal nari",
                "pesan": "semoga jalan kakak selalu dipermudah yaa"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "bang sahid ramah banget, asik diajak ngobrol",
                "pesan": "Semoga apa yang kakak tanam, berbuah hal-hal baik"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "rapih banget abangnya, bisa mencairkan suasana",
                "pesan": "sehat selalu bang dan selalu jadi orang yang baik"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "vibesnya tegas banget, jujur aga ngeri tapi ternyata asik diajak ngobrol",
                "pesan": "semoga lulus tepat waktu banggg"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "kakakny ajgo nari keren bangettt keliatannya penyabar banget",
                "pesan": "Semoga nanti di dunia kerja kakak makin bersinar"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "bang ihsan pelawak ternyata, jokesnya lucu parah",
                "pesan": "Semoga rezeki dan kebahagiaan kakak terus mengalir"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "codingan abangnya rapih bangett, ternyata orangnya pelawak banget",
                "pesan": "semoga selalu dikelilingi hal-hal baik"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "kakakny  luccu bangett, baik pula",
                "pesan": "Terus percaya sama diri sendiri, kak."
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "abangnya ketawa mulu, pelawak juga ama kayak abang kevin dan bang ihsan",
                "pesan": "semoga selalu punya alasan untuk selalu tertawa"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "nah abang ini pelawak jugak jadinya ketawa mulu",
                "pesan": "semoga lulus tepat waktu bang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "kakaknya kalem  banget, kalo di sapa selalu senyum, sukaa deh",
                "pesan": "lebih percaya diri ya kak, kakak itu keren"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen Mikfes":
    def Departemen_Mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lqmiBQxIXL1OcFPT9xpm7HzT5IshQ8m_",
            "https://drive.google.com/uc?export=view&id=1qc0ZjJGDnQ0YEALUj2qsPNHeJELFtoKl",
            "https://drive.google.com/uc?export=view&id=10eawixtb7BVlwa2jL9v5mPspYjH-8QN1",
            "https://drive.google.com/uc?export=view&id=11jtAZ61d_zdCfYARDLdUyoYPfzIy8Jfr",
            "https://drive.google.com/uc?export=view&id=1VtXdbS7L6kmkMJa2lfI6AKI3JafPa7Lw",
            "https://drive.google.com/uc?export=view&id=1Q42LKCY_TE6ljTCKgEHv5wdu3GgG8vmh",
            "https://drive.google.com/uc?export=view&id=1lMVL7Kie8XMaVJljLcx_BTKVVWMNPpcY",
            "https://drive.google.com/uc?export=view&id=1ysfpRHy1Fj_cZdy5ZRxviCTBxDmoGwOr",
            "https://drive.google.com/uc?export=view&id=14zPb3bGhbaooBxvSVvuHjpxBERgRyDpN",
            "https://drive.google.com/uc?export=view&id=1UT8GoRzKmSumJEr3TV3-LIwq0IKzxc3C",
            "https://drive.google.com/uc?export=view&id=1Xd6LqEuXfEo5Tfov7jfIZWwh9qMrU-JL",
            "https://drive.google.com/uc?export=view&id=1SXYm_X3WjyQR8oESMi6emCqD2r88RsbL",
            "https://drive.google.com/uc?export=view&id=12x96FsXtTZyfAsHG4KJqAmbknicHVUBI",
            "https://drive.google.com/uc?export=view&id=1Cl0abyghv5hwItBZpmuNxu51Q6sk3bWi",
            "https://drive.google.com/uc?export=view&id=1ZMXscIS7UNlGuLJRlMbzsPtFfiHBqLr0",
            "https://drive.google.com/uc?export=view&id=1EwB9bjx5RAykwZEDlTEfYMxB9X-_Und2",
            "https://drive.google.com/uc?export=view&id=13u_-EeY4vOKNFOMNiMWjXdHU_Ay81faf",
            "https://drive.google.com/uc?export=view&id=1D2sApr9_CzBxxEKj-4YxuxmzitGxMJ_g",
            "https://drive.google.com/uc?export=view&id=1jZLytcjI5oVZI5IwSvsCZqa3bWvqJJ-9",
            "https://drive.google.com/uc?export=view&id=1eaNpAIcsHj-3qpN5X5TrBk_-daxAB2O-",
            "https://drive.google.com/uc?export=view&id=1SbLCST_T6Z2gme3bkEzr48zDTfQ6l_ut",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123440083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya keren bisa jadi pencair suasana ",
                "pesan": "jangan pernah berhenti untuk berbagi kebaikan ya bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "kakaknya hunble banget, lucu banget senyumnya ",
                "pesan": "terus jadi orang yang menginspirasi ya kak"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "aura duta nya kerasa banget bang, berwibawa keren dehh",
                "pesan": "semoga selalu jadi pribadi yang menginspirasi dan jadi panutan bagi kami"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "kakaknya apa adanya bangett, respect full deh ",
                "pesan": "selalu istiqomah dalam kebaikan ya kak"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "abangnya aktif banget, kagum banget ama public speakingnya ",
                "pesan": "sukses selalu bang, selalu rendah hati yaa bangg"
            }, 
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "vibesnya tenang banget bang tapi tegas ",
                "pesan": "semangat terus dalam menjalani huru hara kehidupan mahasiswa "
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "abangnya asik dan ramah banget ",
                "pesan": "semoga kakak selalu punya semangat buat jalani hari- harinya"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "kakak tuh contoh nyata orang sabar dan tulus",
                "pesan": "semoga kakak dipermudah dalam segala urusan "
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "ceria banget kak, lucuuu bangett ",
                "pesan": "semoga apa yang diinginkan terkabul"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": " baik banget abangnya, dan humoris" ,
                "pesan": "semoga usaha kakak berbuah manis"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "positif vibes bangett sukak deh ",
                "pesan": "selalu jadi pribadi yang menyenangkan"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "kakaknya cantik banget, belum banyak ngobrolnya tapi kayaknya asik orangnya",
                "pesan": "semangat menjalani kehidupan mahasiswa kak"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "cute sekali, ramah bangett, baik banget",
                "pesan": "semangat kuliahnya kak, semoga bisa nyeselsaiin tugas' yang susah"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakaknya kalem tapi ceria bangett ",
                "pesan": "selalu jadiorang yang ceria ya kak"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "kakak tuh kalem tapi berwibawa banget ",
                "pesan": "semoga sukses di karier dan hidupnya"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "abangnya asik banget, vibes orang pinter ",
                "pesan": "semoga karier abang lancar dan sesuai harapan ya bang"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "asik banget kakaknya ga ngebosenin kalo ngobrol ",
                "pesan": "tetep jadi sosok yang ceria kak1`"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "abangnya lucu banget pliss, walaupun sering ngelawak tapi punya sisi tegasnya",
                "pesan": "selalu lucu pliss"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "abangnya cool abizz ",
                "pesan": "tetep jadi abang yang cool dan bisa diandalkan"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "muka kakak yang cute gini suka main catur, jujur kaget sekalii",
                "pesan": "jangan lupa bahagiain diri sendiri kak"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "kakaknya kalem dan positif vibes banget",
                "pesan": "semangat terus kak walaupun kadang capek banget"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren banget dan ga banyak omong ",
                "pesan": "jaga kesehatan selalu ya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1F7oyrZZQ-WGEkf4AdIRqMsqx_d17zqlf",
            "https://drive.google.com/uc?export=view&id=1nkbQKH79MwxSM4NgFlkPpQFv9ZCR26em",
            "https://drive.google.com/uc?export=view&id=1SqOz_GGBcEpHDpMT5I7SdnhZRrLnsa_e",
            "https://drive.google.com/uc?export=view&id=1xLIMwwTBbV1OlyvkyF6gF6GhRzSIbEwv",
            "https://drive.google.com/uc?export=view&id=1JfZaK1Q-UBJimoYhQOahQ_CBi2m1LKxE",
            "https://drive.google.com/uc?export=view&id=1KuEs7OFyo6j1Q3qWrjEDfUHRqVH9-al2",
            "https://drive.google.com/uc?export=view&id=1Q4gaQtgUA1mPY9AXUQaLuCvtmHpsLkCb",
            "https://drive.google.com/uc?export=view&id=1OxMqxGUKy3UNq5Iulz5I-YzbzLz6oy9h",
            "https://drive.google.com/uc?export=view&id=1G6-vle3du5OpvWIiOzTGREpk_YgaCLG4",
            "https://drive.google.com/uc?export=view&id=1YazMBaJYOHTT_qHGdsFeWTtZI6fi6WAJ",
            "https://drive.google.com/uc?export=view&id=1_-HLHTKqynriJbqtsEcYzLPYmCj91YGO",
            "https://drive.google.com/uc?export=view&id=11z4Fz_g-a_aTzjTFgo7MDsl1V6Cf0TCN",
            "https://drive.google.com/uc?export=view&id=1GiYQWbNI-63pkMoO0d2-uSORz3ue7t2y",
            "https://drive.google.com/uc?export=view&id=1pr4Ji_ka5wJ6PSxZQAdflZPoqJEAr7Br",
            "https://drive.google.com/uc?export=view&id=1htpQs9B8hY3ahT0XTRS11Uz-0e52CH7A",
            "https://drive.google.com/uc?export=view&id=1VefZQQxCBaEdKNhvK2Y6wKCnlCX4q2Gw",
            "https://drive.google.com/uc?export=view&id=14SHKtOEzA_6o4C8xGsabRJLvSC7bi7Uw",
            "https://drive.google.com/uc?export=view&id=1lqcUgEb3PFz1xpi5hdqKaOs2JOVd2h6z",
            "https://drive.google.com/uc?export=view&id=1aeZ649sP6en7tz_x32H6nhu5PHhH-K1q",
            "https://drive.google.com/uc?export=view&id=1m0AoRZzqwrZBzIL07DtpLpiq4dnBTHm5",
            "https://drive.google.com/uc?export=view&id=1PE2FmKygUM_fIflUfloWs7kptqjiDZ5H⁠",
            "https://drive.google.com/uc?export=view&id=1EGUs2UPWT4TJ7Q5OtokfEPHKv10ZtixX",
            "https://drive.google.com/uc?export=view&id=1Lq8isRRJtjbQWkLn-hDeQYr8xVcmjgur",
            "https://drive.google.com/uc?export=view&id=15iVHK156d3xUrkuTIULm5x4RfU-z74--",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "santai tapi bisa serius juga ",
                "pesan": "terus semangat mengejar mimpi bang "
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kakak asik bangett, baik, keren banget",
                "pesan": "semoga selalu dikelilingi orang-orang baik kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "kak keisha cantik sekali, ekspresif sekli",
                "pesan": "sehat selalu kakak cantik"
            },
           {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "ceria banget, enerjik juga suasananya jadi nyaman sekali",
                "pesan": "semoga lulus cepet ya kak"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "abangnya cool abizz tapi lucu",
                "pesan": "abang tuh udah keren, semoga makin keren "
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kakaknya imup sekalii dan keliatan penyabar sekali",
                "pesan": "semangat menjalani hari-harinya kak"
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "ceria banget,pembawaannya tenang bangett",
                "pesan": "semoga impian kakak segera tercapai satu persatu"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya baik banget, ramah sekali",
                "pesan": "semangat ngajar tutornya kakk"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "abangnya lucu parah tapi punya sisi yang tegas, respect sekalii",
                "pesan": "sukses selalu bangg"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "vibes calm tapi seruu",
                "pesan": "selalu jaga kesehatan kak"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "senyumnya manis banget, cantik sekalii",
                "pesan": "semoga selalu di kelilingi hal-hal baik kakk"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "kakaknya humble parah, baik sekalii",
                "pesan": "semangat terus kuliahnya kakak, semoga selalu dipermudah jalannya "
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "bisa ngelawak bisa serius juga, tegas juga",
                "pesan": "terus jadi orang keren ya bang"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "kakaknya cantik, pinter, ramah banget, murah senyum, paket komplit pokoknya",
                "pesan": "tetep jadi panutan bagi kita ya kakk"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "lucu banget kakaknya, baik banget lagi",
                "pesan": "semangat menjalani harinya kak!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "abangnya humble sekali ",
                "pesan": "sukses selalu bang"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "abang mentor, ternyata orangnya lucu parah, apa-apa di ketawain ama bang adit asik banget pokoknya ",
                "pesan": "tetep jadi pribadi yang menyenangkan ya bang, pokoknya harus sering' cerita bang"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kakak nya cantik banget,selalu ramah",
                "pesan": "sehat selalu kakak cantik"
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "asik banget kalo diajak ngobrol, excited gitu orangnya",
                "pesan": "sehat selalu kak dan sukses terus!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "vibesnya calm, lembut, tenang gituu",
                "pesan": "semoga dipermudah segala urusan nya"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "kakaknya ekspresif sekali, sukaa deh",
                "pesan": "semangat terus kak, jangan lupa makan ya"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakak nim, positif vibes  banget kak, senyumnya tuh tulus banget, respect sekali kakak ",
                "pesan": "semoga lulus tepat waktu, sukses selalu kak dan jangan lupa istirahat "
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "abangnya santai banget tapi tau kapan harus serius",
                "pesan": "semangat menjalani harinya bang"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "kakak asprak ads humble parah, type pendengar yang baik sii, suka cerita juga",
                "pesan": "selalu jadi sosok yang positif untuk banyak orang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cO_i0cWJxkFPzf8g6Gvz-NRbqMwbTqwM",
            "https://drive.google.com/uc?export=view&id=1nKvJNTAGL1f8yrVe7A4bMEUVYQzAG5vT",
            "https://drive.google.com/uc?export=view&id=1xsRhsgq6jtpKRdrDWpJn029pkoQpQsDB",
            "https://drive.google.com/uc?export=view&id=1kJzJJNNjStEu_EHfXuHalH0vjAgxp5cH",
            "https://drive.google.com/uc?export=view&id=1a6Iak2mevla7M3S0PnNvaOG9sPLK9QaJ",
            "https://drive.google.com/uc?export=view&id=13-ZFeAgggmz3j0gCpiFEF4_ODslr7soh",
            "https://drive.google.com/uc?export=view&id=1b0pgSdVOevh_sATItkx1PT3T7w9bj5cl",
            "https://drive.google.com/uc?export=view&id=1_Q8OvwFW_Fe1ocFXtro_aimH4XApMvXj",
            "https://drive.google.com/uc?export=view&id=1XBUXQfgScXgWSRSP1Mqz8HeWOnp9x1h5",
            "https://drive.google.com/uc?export=view&id=1sZxX45Iw1nHnE7OZH7B6jNZ6_xprpp1b",
            "https://drive.google.com/uc?export=view&id=1arE7CpwoVHWSizaxduAmXkQBfzVt55r3",
            "https://drive.google.com/uc?export=view&id=1myQl1hXdAeu8nK3A0gHyf0980WRlFlqw",
            "https://drive.google.com/uc?export=view&id=1o2Fg2fqdiOXlee31QouFvgXazCYIqVFe",
            "https://drive.google.com/uc?export=view&id=1e9wWM3WyicMDCfahLLooX4y0wAN5btVW",
            "https://drive.google.com/uc?export=view&id=158jxNDasCfD5-bFYiH2KOF_6czZLI8YK",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Balam",
                "hobbi": "mengaji",
                "sosmed": "@ranniku",
                "kesan": "kakaknya kalcer banget, suka banget outfitnya, punya jiwa kepemimpinan, keren bangetttt ",  
                "pesan": "jangan lupa bahagia kak n jaga kesehatan ya kak" 
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "kakaknya kalem, baik banget lagi, penyabar juga",  
                "pesan": "semoga selalu dikelilingi hal-hal baik ya kak" 
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "vibesnya calm banget, senyumnya manis sekali ",  
                "pesan": "sehat selalu kak n sukses terus" 
            },
            {
                "nama": "Rendi Alezander Hutugalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "abangnya kalem sekali, tpi mungkin kalo udah deket bakal asik banget ",  
                "pesan": "semoga dilancarkan segala urusan nya" 
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "kakaknya gampang berbaur, baik sekali kakak ini",  
                "pesan": "sehat selalu kak" 
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "vibesnya tegas banget, ternyata asik banget kalo ngobrol",  
                "pesan": "semoga dipermudah segala urusannya" 
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "kakaknya imup sekalii, ceria banget, lucu kalo ketawa",  
                "pesan": "sehat selalu kakak imupp n bahagia selalu" 
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "kakaknya nih asik tapi vibesnya tegas ",  
                "pesan": " sehat selalu kak"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "abangnya kalem banget, tapi punya selera humor yang baik",  
                "pesan": "lebih percaya diri lagi bang, abang bisa lebih keren lagi" 
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "punya aura yang sangat positif, ramah banget ",  
                "pesan": "semoga selalu bersinar yaa" 
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": " suka banget ama pembawaan nya selalu ceria ",  
                "pesan": "bahagia selalu kak n jangan lupa jaga kesehatan" 
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "vibesnya asik banget kak, keren sekalii ",  
                "pesan": "semangat menjalani harinya kak" 
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "abangnya santai banget tapi bisa serius juga",  
                "pesan": "sukses selalu bang" 
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "kakanya canti sekalii dan hunble ",  
                "pesan": "semangat terus kuliahnya kakak n jaga kesehatan" 
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "lucu bangett kakaknya baikkk ",  
                "pesan": "sukses selalu kak" 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "pembawaannya santai tapi serius, seru kalo diajak ngobrol ",
                "pesan": "semoga segala urusan nya dipermudah"  
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "kakanya humble sekali dan santai juga orangnya ",
                "pesan": "bahagia selalu kak "   
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "vibesnya model banget, keren banget, cool abiz bang ",
                "pesan": "sukses terus bang n semoga selalu bahagia dimanapun"  
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "kakaknya baik banget, ramah sekali dan lucu ",
                "pesan": "sehat selalu kak jangan lupa istirahat"   
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "seru banget ngobrol ama kakak",
                "pesan": "semangat menjalani harinya kak"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "kakaknya lucu banget cantii sekalii ",
                "pesan": "hwaiting kakak cantik"   
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnya humble, cool parah ",
                "pesan": "semoga selalu diberi kemudahan di segala urusan"   
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "kakaknya wangi banget plis, ramah sekali",
                "pesan": "tetap jadi orang baik ya kak"   
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "positif vibes banget kakanya ",
                "pesan": "semoga langkah kakak selalu dipermudah"   
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "ceria banget pembawaan nya sukaa deh ",
                "pesan": "semoga selalu ketemu orang baik ya kak"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "kakak baik banget, tidak sombong",
                "pesan": "semoga semua doa kakak di kabulin"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MJT0J8yoogoFt-2K_VqWtCpFY_021G2F",
            "https://drive.google.com/uc?export=view&id=1GFFtXq2-fpMhoc_xf9GytS-1ogibP8kY",
            "https://drive.google.com/uc?export=view&id=1Uxcamr2HT-FAXhYDu5F_mDhKlewtr-PZ",
            "https://drive.google.com/uc?export=view&id=1k1Sv6EN-Dt_cWoi15C5j0ULm7MG5wAEo",
            "https://drive.google.com/uc?export=view&id=1B1-Jwxwglg8G-2w93yaSY07JiVBOf22N",
            "https://drive.google.com/uc?export=view&id=1HdJPozCH-_-hx9UemBqTH0VzMEvGW49S",
            "https://drive.google.com/uc?export=view&id=1k4FRi86EZVPzhrKl3RxnqPtg8ZVc78x7",
            "https://drive.google.com/uc?export=view&id=1Id4uncgGktA3OyGx88s1ahfD8hiaMGj4",
            "https://drive.google.com/uc?export=view&id=1RtCl6VEIE22qVK8WzCIss1B29qBVPMWs",
            "https://drive.google.com/uc?export=view&id=1aeVwpgzgGb0L2LNrDT2UdfqN9nTKXvvW",
            "https://drive.google.com/uc?export=view&id=1SYJixhPt_S4v82k5UWnS-lNuq6VEMt8g",
            "https://drive.google.com/uc?export=view&id=1zzkaebMPLImS-x2wmtv6mx6JijBLpbYU",
            "https://drive.google.com/uc?export=view&id=1bSb44IXUcK1NSfAzbATEnJy1eWhNf2J3",
            "https://drive.google.com/uc?export=view&id=1f7FNYMLE1Y0BSQglToDnyNMo1ws3b4f_",
            "https://drive.google.com/uc?export=view&id=1GFFtXq2-fpMhoc_xf9GytS-1ogibP8kY",
            "https://drive.google.com/uc?export=view&id=1PzLaUfhAbrzolcOqbIt4DaS4AmkThxFm",
            "https://drive.google.com/uc?export=view&id=1hojdv73FhwgRUumQgvH9b6bQAAlgs4En",
            "https://drive.google.com/uc?export=view&id=1Lysx8pB2wair81cXWdiPfviaIKkVZD8L",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jati Mulyo",
                "hobbi": "sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "periang sekali kak cia, kalo ngomong selalu excited banget n cantik sekali",
                "pesan": "semangat menjalani harinya kak n jangan begadang terus yaa" 
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "ceria banget vibesnya, cantik banget kak",
                "pesan": "sukses selalu kakak cantik"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "lumayan humble tapi nyambung kalo diajak ngobrol ",
                "pesan": "semangat menjalani harinya bang" 
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "rapih banget, humble, asik kalo diajak ngobrol ",
                "pesan": "semoga cita-citanya tercapai"   
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "abangnya murah senyum sekali n asik sekali ",
                "pesan": "jangan keseringan begadang ya bang"   
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "cantik sekali kakaknya, ramah sekali kakaknya n baik banget ",
                "pesan": "selalu jadi sosok yang inspiratif ya kak"   
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "aduhhh kakanya cantik banget, humble, asik kalo diajak ngobrol, wangi banget, paket komplit pokoknya",
                "pesan": "semoga cepet lulus ya kak jangan lupa jaga kesehatan"   
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "kak aliya baik banget se baik itu, ramah banget, cantik sekali kak",
                "pesan": "semoga selalu diberi kelancaran dalam segala urusan ya kak"
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "kakaknya baik banget ramahg sekali ",
                "pesan": "semoga selalu bertemu orang baik"   
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "kakanya lucu banget tapi cool gitu, baik sekali, cantikk jga ",
                "pesan": "sukses selalu kak n jaga kesehatan yaa"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kakanya humble, ceria sekali n cantik jugaa ",
                "pesan": "semangat kuliahnya kakak cantik"
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "kakanya baik banget, humnle parah n ceria sekali",
                "pesan": "semoga selalu ceria ya kak" 
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "definisi lucu parah, ceria banget, pembawaannya tuh jadi nayam",
                "pesan": "bahagia selalu kak"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "vibesnya tuh cool pembawaan nya tegas tapi santai gitu",
                "pesan": "sukses selalu bang!!"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "kakaknya calm tapi humble gitu",
                "pesan": "semoga selalu di kelilingi orang-orang baik"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "kakaknya ramah sekali, humble, cantik dan ceria sekali",
                "pesan": "sehat selalu kak !!!"   
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "ceria banget kakaknya n cantikkk ",
                "pesan": "bahagia selalu kakak cantik"   
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "baik banget kakaknya, vibesnya kalcer gitu, cantikk sekali ",
                "pesan": "semoga selalu jadi orang yang ceria"  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
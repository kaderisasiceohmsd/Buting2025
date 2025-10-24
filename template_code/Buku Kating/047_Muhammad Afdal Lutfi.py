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
            "https://drive.google.com/uc?export=view&id=1nldQIc67ILaywdUHiD9T2ncqg1MI9Owy",
            "https://drive.google.com/uc?export=view&id=1TQpA61F9By1c861AuIgrYfKbz9Jbhdts",
            "https://drive.google.com/uc?export=view&id=1t7zHWhoI_y7xug6zQnqQqFStG_FcTLQX",
            "https://drive.google.com/uc?export=view&id=1cK4CkoXT5J_LsoVk5woXZQ_ynRitZH6o",
            "https://drive.google.com/uc?export=view&id=1pFnhQqq9NthIQXamv16I1wRLIeRm19RO",
            "https://drive.google.com/uc?export=view&id=1wg872AjvtT8zQoVSoU6PkKCMT4RzKxLf"
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
                "kesan": "vibes-nya tenang, tapi karismanya berasa banget",  
                "pesan":"jangan cape mengurus himpunan ini ya bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "vibes-nya chill banget, tapi kalau udah serius, semua langsung fokus",  
                "pesan":"sehat selalu bang joo"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "vibes kakaknya ceria banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "vibes-nya positif banget dan juga pinter banget",  
                "pesan":"tetap menjadi kakak yang tenang"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "vibes tegasnya dapet banget tapi ternyata asik juga",  
                "pesan":"semangat kuliahnya kakak"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "kakaknya random tapi selalu bikin suasana rame",  
                "pesan":"tetap jadi diri kakak yang seperti ini"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xyMhIUaiDyuGrk5w4RYiA0mu_hbk4KRh",
            "https://drive.google.com/uc?export=view&id=1mUwX5plVjQ8w9bFI9b7MxuZkDrPznhdE",
            "https://drive.google.com/uc?export=view&id=1Ph8XuJXb2sUdrSAnyeGX6RXoY3W61Vki",
            "https://drive.google.com/uc?export=view&id=1rzvCbIGQSzAwGABcXJuKsgo451eAV2is",
            "https://drive.google.com/uc?export=view&id=12qWCOVm0VadpHS3iPzSZPpngC4zgh0D8",
            "https://drive.google.com/uc?export=view&id=1MN5_PC6Tu6K5u_HGvfQ6MhIAjzytX8tV",
            "https://drive.google.com/uc?export=view&id=1mBLUwNB87c9uxDh9CnqeWLOPOrlfv9CE",
            "https://drive.google.com/uc?export=view&id=1KwY6dWrFU3XCP5CR_lSfYw8v2Nbf8i2k",
            "https://drive.google.com/uc?export=view&id=1mRw1Rx42SXw_b35RrXrkZnWlLr2K3u1Z",
            "https://drive.google.com/uc?export=view&id=1KyYIUhgYCRBlzE1bDOneLuW4bidSr33j",
            "https://drive.google.com/uc?export=view&id=1IkcoJ8oLsCTTeNaqP0UAzFntUkiYGDqM",
            "https://drive.google.com/uc?export=view&id=1vOVShSixolrKikYYynLzbbyRRxpq7hWg",
            "https://drive.google.com/uc?export=view&id=1lCm_C1y5-IrQVWc0vyPk0FjalH7rZuZx",
            "https://drive.google.com/uc?export=view&id=1kbVex0VNJSqdfyn41Ayf5r24y7TCfBGH",
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
                "kesan": "Tiap ngomong selalu ada aja lucunya",  
                "pesan":"semangat semester akhirnya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Gaya cueknya menipu, ternyata peduli banget",  
                "pesan":"Tetap jadi energi positif di mana pun kakak berada"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Vibes-nya santai tapi bisa nularin semangat ke orang lain",  
                "pesan":"Jangan berubah ya kak, dunia butuh orang se-flexibel kakak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Selalu kelihatan tenang, tapi ternyata banyak akal",  
                "pesan":"Tetap jadi orang yang bisa diandalkan, tapi jangan lupa istirahat juga kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "Orangnya chill tapi rajin",  
                "pesan":"ajarin rstudio bang hehe"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Orangnya gak banyak gaya tapi keren aja gitu alami",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "Keliatannya santai, tapi ternyata diam-diam sibuk bantu di belakang",  
                "pesan":"Respect banget, lowkey hero sejati"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Kadang random, kadang bijak",  
                "pesan":"Tetap seimbang antara chaos dan tenang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Lucu, santai, tapi selalu hadir pas dibutuhkan",  
                "pesan":"Jangan pernah kehilangan energi positif itu"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "Kalau ngomong selalu spontan, kadang ngawur tapi jujur",  
                "pesan":"Dunia butuh orang jujur kayak kakak"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Tiap bercanda selalu pakai ekspresi total",  
                "pesan":"Tetap jadi si lucu tapi logis itu ya"# 1
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Suka nyeletuk random tapi selalu pas waktunya",  
                "pesan":"sRendah hati banget, tapi jangan terlalu merendah"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "-",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Bercanda mulu tapi nilainya bagus"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": ": Paling sering jadi korban roast-an, tapi ketawa paling kenceng",  
                "pesan":"Jiwa besar kamu tuh inspiratif banget"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VFkOLTPdQXFRTGHOJHMtDkIWeXi7vhyt",
            "https://drive.google.com/uc?export=view&id=1JscLPfOsGOEyFG1QF8asg44BARl0tKEd",
            "https://drive.google.com/uc?export=view&id=1GmUshhQ-YBiMp165nFgacvx4nge8JyVO",
            "https://drive.google.com/uc?export=view&id=1jk3Qpav9qS_EsDOD9ulHCGbDgg5NqbX5",
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
                "kesan": "Suka bercanda sama semua orang",  
                "pesan":"Tetap jadi orang yang ngerangkul semua"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakanya murah senyum, bahkan pas capek",  
                "pesan":"Terima kasih udah nyebarin vibe positif setiap hari"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "Orangnya kalem tapi selalu nyimpen punchline",  
                "pesan":"Respect buat kerja diam-diamnya, salut banget"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kalau udah serius, auranya beda banget",  
                "pesan":"Respect buat sisi seriusmu yang jarang keluar"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Vi6u46P6OG4ZpDR_uX_WG5OKy5z7dWl8",
            "https://drive.google.com/uc?export=view&id=1YDko7qg1l2T6DkGp4nOzFl1m7aLp9at3",
            "https://drive.google.com/uc?export=view&id=1z0b5UQ-y3u_Qj3U6CTLqEaMZVzdOIB-t",
            "https://drive.google.com/uc?export=view&id=1tHjYpHQmMSgd2NYjNTAvQ_VRY4p9IJ6n",
            "https://drive.google.com/uc?export=view&id=1NbkMrPqFGmt7pX1qKXcyVAtPsCkX4oLM",
            "https://drive.google.com/uc?export=view&id=1ZwUnRNwTeEM3RT6IZ5KVJlom7VFPB9Cq",
            "https://drive.google.com/uc?export=view&id=11bpFFocypPn9p2I9Cm3yFp3luxGl04t3",
            "https://drive.google.com/uc?export=view&id=1aLY-X04fcroUhlDGOuL_-bLF6al5CoKF",
            "https://drive.google.com/uc?export=view&id=1DwWBNvz2kYk68xoN8gAHywnr86MQTXJG",
            "https://drive.google.com/uc?export=view&id=1zZ5eCbRaPcJhRzNiwgDZS9v4f4ZEqbyU",
            "https://drive.google.com/uc?export=view&id=1w9T6O44vV94UXUtrX-kvs6SZJfSFONu9",
            "https://drive.google.com/uc?export=view&id=131YDTJu7X993IwRkwvCGvdJFP9hBVtZ6",
            "https://drive.google.com/uc?export=view&id=1ehc5R9hllBqC5_ffVTAUK9awQB9KzSPH",
            "https://drive.google.com/uc?export=view&id=1lU1rUMEsE0gZ8lRq1TBPreCrroIvnErR",
            "https://drive.google.com/uc?export=view&id=10XAL61PI0Cy9mDv0V2WY8lOutaeQAZ9Z",
            "https://drive.google.com/uc?export=view&id=1b0vPY3DudY0gLryZ49VHn28V99zFDogL",
            "https://drive.google.com/uc?export=view&id=13FV60r_AGKDmUOgQ2QSU0d2cxcA5JBg7",
            "https://drive.google.com/uc?export=view&id=1lU1rUMEsE0gZ8lRq1TBPreCrroIvnErR",
            "https://drive.google.com/uc?export=view&id=1JEgR3TlD7nzvDIO2dEu6Tfa0XBxVZwGW",
            "https://drive.google.com/uc?export=view&id=1XlPA6YouTlr52uxozNsKBwunFrlORJsJ",
            "https://drive.google.com/uc?export=view&id=1_28kWTe5_iuUrfaA5Bds-AVwgtvT_fXy",
            "https://drive.google.com/uc?export=view&id=1RrTVWAxu45E5vOlpsNVuDGsTClb30Ks_",
            "https://drive.google.com/uc?export=view&id=1adlUyVl4nqoZXmRw0UDHHMxQ0h2AeZ2R",
            "https://drive.google.com/uc?export=view&id=1h3NwlU-nex4xFljYXmnWGZVfgcwceZxU",
            "https://drive.google.com/uc?export=view&id=1Q_tqEVUC7Fut1O3CYAZz7EqWkJqRyEa-",
            "https://drive.google.com/uc?export=view&id=1YUlnQNlH1W7_oF2bsIKs-bP4pPz_GoNb",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Orangnya santai, tapi tanggung jawab",
                "pesan": "abang tuh chill tapi solid"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "Sering diem tapi peka",
                "pesan": "bia di bilang kakak tuh pendengar sejati"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Gak pernah habis bahan ngobrol",
                "pesan": "keren banget kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "vibes-nya serius banget",
                "pesan": "maju terus bang presma"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kalau nongkrong, pasti bikin chaos",
                "pesan": "-Chaos-kakak menyenangkan"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "jujur pertama kali liat serem si",
                "pesan": "tapi ternyata asik juga"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Orangnya kalem, tapi kalau marah ngeri",
                "pesan": "Untung jarang marah, aman dunia"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "Orangnya slow banget",
                "pesan": "Tapi kalau disuruh, cepet banget"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "pinter banget",
                "pesan": "semoga bisa mencapai cita-citanya ya bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Orangnya rame dan tulus",
                "pesan": "Kombinasi langka"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Suka bikin rencana dadakan",
                "pesan": "Tapi anehnya selalu jalan"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "Kalau cerita, ekspresif banget",
                "pesan": "abang tuh stand-up comedy alami"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Kalau marah, tetep sopan",
                "pesan": "abang tuh elegan dalam emosi"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "Gak bisa nolak ajakan nongkrong",
                "pesan": "Loyal banget sama kebersamaan"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Gak pernah jaim",
                "pesan": "Autentik banget kamu"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kadang kelihatan cuek",
                "pesan": "Tapi ternyata perhatian juga"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "Kalau nongkrong, selalu punya cerita baru",
                "pesan": "Kamu tuh ensiklopedia pengalaman"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "Gak bisa serius lama",
                "pesan": "Dunia butuh orang kayak kamu"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "firs impression yang mantap pada kader lapangan",
                "pesan": "semangat terus kuliahnya bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "Sering tiba-tiba muncul",
                "pesan": "kakak ini NPC unpredictable"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kadang sok tegas tapi gagal",
                "pesan": "tapi tetep kocak si bang"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Kadang sarkas tapi lucu",
                "pesan": "Sarkas abang level profesional si"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "Kalau nongkrong, paling rajin selfie",
                "pesan": "Galeri kakak tuh museum ekspresi"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Kalau ditanya serius, jawab bercanda",
                "pesan": "Tapi jawabanmu kadang bener"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "abang NIM hehe",
                "pesan": "semangat terus kuliahnya bang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Sering kebingungan tapi ngelucu",
                "pesan": "Lucu karena alami"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1j2kQPnA1632PN7fDdb5vra4JvF1vmXMa",
            "https://drive.google.com/uc?export=view&id=1kPaIUIEQh5QIx-sZcJH4ZN0TWMhJ5ugU",
            "https://drive.google.com/uc?export=view&id=1MzMcfxWYzzsncT3bWWk5wM3YR71hGw9O",
            "https://drive.google.com/uc?export=view&id=1XB-LE8eXXi9MYS4a0QW0Ej5w2yfUISM6",
            "https://drive.google.com/uc?export=view&id=1ua9SgWOsnnYPmJqiVmxCW1gag5vwCpVc",
            "https://drive.google.com/uc?export=view&id=1gpTv5p-r8rotFspbWVOvyOh002o7GPyp",
            "https://drive.google.com/uc?export=view&id=1ifO4JEyl5NdtdQmr4qFUJaqr9f5UP3FY",
            "https://drive.google.com/uc?export=view&id=16XwDkI1yBsjmFc1U1ug_gUyNyZA9fWt7",
            "https://drive.google.com/uc?export=view&id=13XjuftRGrAwx96Xrx6iA5urLPWhDbvfh",
            "https://drive.google.com/uc?export=view&id=1Mc4VLiyP68k4pPf6s22_9B-NfWbSsxuB",
            "https://drive.google.com/uc?export=view&id=1gu_ryT3_MrCW5XuJJWARYfXlKiHVCjY0",
            "https://drive.google.com/uc?export=view&id=1GRGtIrG6ycU1kFujgQqSNHA2m3cl9nsv",
            "https://drive.google.com/uc?export=view&id=1AKPU4uY9LayDRY9_os0RHYgrk5zBRDEy",
            "https://drive.google.com/uc?export=view&id=17S9YrGuVuDPgnK1yV5PTf_EwoJe5xSDp",
            "https://drive.google.com/uc?export=view&id=1ELcKAiU6F1_tRpUF6DkxPQ3FmdgFzvY3",
            "https://drive.google.com/uc?export=view&id=1syept0NadBvJRJsRJG_8wrEfBIRxGeBe",
            "https://drive.google.com/uc?export=view&id=1zwDyghk_1UeikRL0mb5eLF1TPD6RqjUR",
            "https://drive.google.com/uc?export=view&id=1fDZhgXo19l7sFo38UElWStBiQzi-QMbv",
            "https://drive.google.com/uc?export=view&id=1ArBA8ZkuouZKEz1s758znLrbyZt3rxyl",
            "https://drive.google.com/uc?export=view&id=1XFI8x1Q95SWdFyMdopxeZWFBdXs5DrgP",
            "https://drive.google.com/uc?export=view&id=1nsHtsz8AZCEHR0uOBH344sRZpCwwGGEM",
            "https://drive.google.com/uc?export=view&id=1ORK8uj-5xRPfaZ-mQd18dVL48tIV1zNN",
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
                "kesan": "Sering lupa, tapi inget yang penting ",
                "pesan": "Memori abang selective banget"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "Gak pernah nolak ajakan makan",
                "pesan": "Kakak tuh loyal sama kuliner"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Sering salah dengar ",
                "pesan": "Tapi responmu selalu keren"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Paling semangat kalau ada makanan ",
                "pesan": "kakak tuh motivasi perut"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Duta genre nieee",
                "pesan": "semangat terus bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "keliatan multetalent ",
                "pesan": "keren bang bisa membagi waktu antara akademik dan organisasi"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Kalau ngobrol suka nyeleneh",
                "pesan": "Tapi kadang ide briliannya muncul dari situ"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "Kalau dia diem, semua nanya kenapa? ",
                "pesan": "Kakak tuh pusat perhatian alami"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Sering ngelucu tapi gak sadar",
                "pesan": "Lucu natural tuh keren"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Gak bisa diem kalo udah ngobrol",
                "pesan": "abang tuh mesin tawa berjalan"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Orangnya random banget",
                "pesan": "Randommu tuh warna kehidupan"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "Kadang aneh tapi unik ",
                "pesan": "Dunia butuh keanehan kakak"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "Suka cerita panjang, tapi seru ",
                "pesan": "Kakak tuh storyteller sejati"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kalau nongkrong, suasananya langsung hidup",
                "pesan": "Kakak tuh bahan bakar tawa"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "Gak pernah nyerah walau ngeluh ",
                "pesan": "Kakak tuh kuat tapi jujur"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Sering banget salah ucap",
                "pesan": "Tapi itu yang bikin kocak"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kadang bengong tapi lucu ",
                "pesan": "Bengong aesthetic"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "Kalau dikasih tanggung jawab, total banget",
                "pesan": "Respect banget buat dedikasi abang"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "ga nyangka abang sepinter itu",
                "pesan": "keren banget"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Orangnya rame, tapi bisa diandalkan",
                "pesan": "Serius pas dibutuhin, lucu pas santai"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Sering ngasih nasihat tapi gak sadar ",
                "pesan": "Kakak tuh motivator terselubung"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kalau abang ngomong, semua denger",
                "pesan": "Wibawanya dapet banget"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jvRoAmwG-UacSDceuLj4YOSgqdNdBKX6",
            "https://drive.google.com/uc?export=view&id=19UlE0_GeVUjmaFMUpHzl8TUxiC4bNmKN",
            "https://drive.google.com/uc?export=view&id=1DHjM1ekGdVBISUI3L7nxjb1ndb4iJdlb",
            "https://drive.google.com/uc?export=view&id=1s_qL6Zhezf0qoZFyFsPRYcNikPaq231_",
            "https://drive.google.com/uc?export=view&id=1_NYbihqEzv_eqVR5AYDHH4LH9n4y2pLX",
            "https://drive.google.com/uc?export=view&id=1qrBIUgFCGRAjv1Am9bCUfS51SseW5Vkf",
            "https://drive.google.com/uc?export=view&id=1rClTZYCxME_KpC_5cF2k-I2GHFCYFOxp",
            "https://drive.google.com/uc?export=view&id=1glxG9iZjcDZMX__mv2J2pzmDacXidaWv",
            "https://drive.google.com/uc?export=view&id=11WEFLj7q6fM9KF3vtRzdnD89dQjejN_C",
            "https://drive.google.com/uc?export=view&id=1Kx3OXI-AnaCcxdolTxFQoVSncGRimrgp",
            "https://drive.google.com/uc?export=view&id=1RjNvKifyFRtqYtIWtnJ0FTZTC1kz-avA",
            "https://drive.google.com/uc?export=view&id=1YA60lQpiWCu0fRqflqmuD2JOJc_O4KS9",
            "https://drive.google.com/uc?export=view&id=1VpFduDK7leWeelLefBScrTHkT-15zwpg",
            "https://drive.google.com/uc?export=view&id=1kQqkrXwBVITq7cZjeFhYr7vEifj7VldQ",
            "https://drive.google.com/uc?export=view&id=1P2cgjYaZaXUUfhcihYaSbY-mRswZ-2yD",
            "https://drive.google.com/uc?export=view&id=1uFHSr272FKkIgfIqhKSYRrdYQWSbMd6h",
            "https://drive.google.com/uc?export=view&id=1jsCMe_M3-s8QPgM5HONoPRrRLwr9ocC_",
            "https://drive.google.com/uc?export=view&id=1rb63JNUW527CWfXAouhRrRx2avFQbk_L",
            "https://drive.google.com/uc?export=view&id=1KIHLfLVolajbIeCeQa-AI5Vqhq07tfw9",
            "https://drive.google.com/uc?export=view&id=1SsRfx_lZStHBdhMT14iUnPs4qdA9v3a7",
            "https://drive.google.com/uc?export=view&id=1JB3y9Gv7EvMJwnogLnpMEqxylxcKjnGJ",
            "https://drive.google.com/uc?export=view&id=1kXbmmqp7WX8fWcTfcSKqIoCUDKKOaE1z",
            "https://drive.google.com/uc?export=view&id=11n2vMiqYQYTdai55bBHxfzI7qDgW1Phz",
            "https://drive.google.com/uc?export=view&id=1_5Cig3tEjzkjgvDgiQPx09MJRyNu5uvh",
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
                "kesan": "Tiap ngomong selalu ada aja lucunya",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Orangnya ceria banget, kayak gak pernah capek",
                "pesan": "janganlupa istirahat juga ya"
            },
            { 
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kalau bercanda kelewatan tapi niatnya baik",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Tetap jaga batas, tapi jangan kehilangan lucumu",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Gayanya santai, tapi kerjaannya niat",
                "pesan": "sBalance banget hidupmu"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Gak pernah serius tapi hasilnya bagus",
                "pesan": "Kamu tuh bukti “yang penting niat” !!!"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Ketawanya khas banget",
                "pesan": "Jangan berubah ya kak"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "pinter bangett",
                "pesan": "makasi kak tutorial ale nya"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Orangnya rame, tapi hati lembut",
                "pesan": "semangat terus kuliahnya bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "Orangnya gampang akrab",
                "pesan": "Skill sosialmu tuh AAA"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "keren banget kak bisa jadi finalis duta itera ",
                "pesan": "semangat terus ya kak"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "Kalau udah cerita, gak bisa berhenti",
                "pesan": "Cerita kakak tuh hiburan gratis"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kalau dikasih tanggung jawab, pasti kelar",
                "pesan": "keren si bang"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "Kalau foto pasti gaya lucu",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "Orangnya cuek tapi perhatian",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "Kalau nongkrong gak bisa diem ",
                "pesan": "ibarat kata abang tuh speaker aktif"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Orangnya chill tapi pekerja keras ",
                "pesan": "semangat terus bng adit"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kalau nyapa, selalu semangat",
                "pesan": "sosok asli manusia positif"
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Gak bisa marah lama",
                "pesan": "Kakak tuh terlalu baik"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Orangnya rame tapi gak ribet ",
                "pesan": "Keseimbangan yang pas"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kalau ngomong suka pake efek nada ",
                "pesan": "Kakak tuh sound effect alami"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kadang asal tapi niat ",
                "pesan": "Spontan kakak tuh sepertinya bakat"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kalau denger musik langsung joget",
                "pesan": "semangat terus sdm nya bang"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "Orangnya chill tapi kalau marah diem",
                "pesan": "tapi itu marah paling ngeri sih"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FVNG3_tcsRkveMtyY5e686J6czIf_qID",
            "https://drive.google.com/uc?export=view&id=1Ydh4V8QE5CPzX41g1274fUbEQsCV3WnV",
            "https://drive.google.com/uc?export=view&id=11k2amooj2aRXLy6IH1A4I8U0xIevQAjb",
            "https://drive.google.com/uc?export=view&id=1dASWSzqPDbqm-_kj3bzg8isoisywaCQR",
            "https://drive.google.com/uc?export=view&id=11OtGzELV5pd9Vtrrg62mTZybznyWvZ_T",
            "https://drive.google.com/uc?export=view&id=1MVEF-baGg_kq8dPFuuw0OlqrYetgGdHW",
            "https://drive.google.com/uc?export=view&id=11Lohdp2yrkvmm0V8qcLxbv9zEbx8f8LA",
            "https://drive.google.com/uc?export=view&id=1amzv9sXlZElCeaygKnhEd065AlP0kIDo",
            "https://drive.google.com/uc?export=view&id=16u0MXE9C4udJsRj0m5j0lArU2DFrStcg",
            "https://drive.google.com/uc?export=view&id=174xWk-uzCPTLFMf-5K-AQOf4wL4BPG_u",
            "https://drive.google.com/uc?export=view&id=15VELRDkzvcTn_dB8XYD_2XUxDJu4ZQ8K",
            "https://drive.google.com/uc?export=view&id=1qLOz8uYQ0QrMNF_GIcdAE1iBqq7bPPsr",
            "https://drive.google.com/uc?export=view&id=1QSy0rA2My0vzpffUdnxKoihwWFkiYWFu",
            "https://drive.google.com/uc?export=view&id=15K0DLZQlFPS5HNp1USeovWc46RbR1ds-",
            "https://drive.google.com/uc?export=view&id=1aRrY4nGWVz_BC84GAKkSS1g_f7oWJEGw",
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
                "kesan": "Suka ngomel tapi sebenernya peduli ",  
                "pesan": "Bentuk kasih sayangnya emang unik" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kadang ngilang, tapi pas balik langsung rame",  
                "pesan": "Jangan ilang-ilangan lagi ya kak" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Gak pernah gagal bikin orang ketawa ",  
                "pesan": "jangan berubah ya kak" # 3
            },
            {
                "nama": "Rendy",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "Paling bisa ngelucu tanpa ekspresi ",  
                "pesan": "berasa stand up comedy versi kalem" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kalau ngobrol suka sambil ngelucu",  
                "pesan": "Jangan ubah gaya bercandanya kak" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "Gak banyak ngomong tapi kehadirannya berasa ",  
                "pesan": "sSilent but powerful" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Suka bantu tanpa disuruh ",  
                "pesan": "Dunia butuh lebih banyak orang kayak kakak" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "Santai banget, kayak gak punya beban ",  
                "pesan": "Tapi tetep produktif, itu keren si kak" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "Kadang absurd, tapi justru itu ciri khas",  
                "pesan": "Absurd is your superpower" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kalau ngomong, selalu pake mimik ekspresif ",  
                "pesan": "semangat kak" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Gak pernah gagal bikin orang ketawa ",  
                "pesan": "semangat bigel" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Kalau ngobrol suka sambil ngelucu ",  
                "pesan": "Kakak tuh alasan temanku betah nongkrong" # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "Gak pernah pelit senyum",  
                "pesan": "jangan berubah ya bang" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "Gak banyak ngomong tapi kehadirannya berasa ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Suka bantu tanpa disuruh",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16Zswe5Abgcpt4ju7VIvHRqgy21yXRPmj",
            "https://drive.google.com/uc?export=view&id=1ZOYdK9aMLq93GnDZx3Hc1KLa9Pq19-0Y",
            "https://drive.google.com/uc?export=view&id=1X4TQ4xYSjpIBB7U4hyFLzC9y6-5lPB7X",
            "https://drive.google.com/uc?export=view&id=1DmZjKYLuI_iwA4ZjsNZt5KJtKKBGyg9K",
            "https://drive.google.com/uc?export=view&id=1xkuEPW-nZ1gTperwHu7rHXLZfh_8BzcN",
            "https://drive.google.com/uc?export=view&id=1mAKPv1wt-VvR3bb4spztM25PdlCRB3AC",
            "https://drive.google.com/uc?export=view&id=1Z452Z3pGiiGO4FJSPj4iTT2rXNMz1BaS",
            "https://drive.google.com/uc?export=view&id=1BVOno_9BFfOOxoXzftu-350MtgtqV2sl",
            "https://drive.google.com/uc?export=view&id=1Fdsnf-ju0eRjoDpLbvJsrCY3iZpD_kan",
            "https://drive.google.com/uc?export=view&id=16bti47nxT_Gc5KOadfHX9nAmwAXrp2Wu",
            "https://drive.google.com/uc?export=view&id=180ht5ovmcthdhszv73uTpdLAm-deq9hE",
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
                "kesan": "ga ekspek kalo bang danang suka jogging ",
                "pesan": "info pace tercepaatnya bang wkwk"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "ga nyangka kalo kak syalaisha punya kembaran ",
                "pesan": "tips membedakan kakak dengan kembarannya dong"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "bener kata orang-orang kalo abang cocok jadi model ",
                "pesan": "semangat selalu bang"   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "Sering gak fokus tapi ide-nya bagus ",
                "pesan": "tetap menjadi kakak yang unik"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "kakak kalau lagi diem tuh pasti lagi nahan ketawa ",
                "pesan": "Jangan ditahan kak, keluarin aja"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "kakak ini orangnya nyantai tapi tangguh",
                "pesan": "Kombinasi langka, jangan berubah ya kak"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "keliatan banget muka wirausahanya ",
                "pesan": "semangat kuliahnya bang"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kalau diem tuh mencurigakan ",
                "pesan": "Biasanya abis diem ada ide aneh keluar"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "Kalau bercanda suka keterusan",
                "pesan": "Tapi gapapa, ketawanya worth it"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Gak pernah keliatan lelah",
                "pesan": "Tapi tolong, jangan lupa istirahat juga ya kak"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "vibes-nya chill banget, kayak gak pernah marah ",
                "pesan": "Kalau marah pasti tetep sopan"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A5bRQ6RxZWFtdobcmoDISo1WHtxJdlFh",
            "https://drive.google.com/uc?export=view&id=1Xb8ojk2eYlF4dVRfz7Eq1cWp-rF5AOvZ",
            "https://drive.google.com/uc?export=view&id=1sEWpM8iQZhUDobtI2SihzIxPqGuI23IL",
            "https://drive.google.com/uc?export=view&id=1lkgNVmlh3hJjsUIdZg8omb2SDkdr92mf",
            "https://drive.google.com/uc?export=view&id=12Uhom2bVA5j_AhnR3PdqsW9NLzIVV80P",
            "https://drive.google.com/uc?export=view&id=1Qp6wJWfMtWyA_PJuJwIyl--19nFA1T_m",
            "https://drive.google.com/uc?export=view&id=1mmxahfScDShWgvqEq7EaHUSO__i7BR2c",
            "https://drive.google.com/uc?export=view&id=1yHEghWW1OnHYV29eMbgXv3fqy75dCNaB",
            "https://drive.google.com/uc?export=view&id=1zjfUDEo2ONszngZrnQWofDbwzgeGznZX",
            "https://drive.google.com/uc?export=view&id=1HMuG_uBspO3fugNkNMsyKtIwIREOyuvd",
            "https://drive.google.com/uc?export=view&id=1T1vJGoe1ooRouNqX2xm-TLPb6QtsZTTX",
            "https://drive.google.com/uc?export=view&id=1voeT7ebnNbpWTw6msk0IQjRhtzXf3npZ",
            "https://drive.google.com/uc?export=view&id=1BV5cdBVw8saUbZiK45bR1V3h6mQPyQ3t",
            "https://drive.google.com/uc?export=view&id=1u7EaHHAtIerpfaCmV141vP8KrJTapAVI",
            "https://drive.google.com/uc?export=view&id=1Ey_zM7nyihb607fXqNUGpN3otKqWApH_",
            "https://drive.google.com/uc?export=view&id=14wAlOqZWp66Owt8ApJJxu1meMQvcX75a",
            "https://drive.google.com/uc?export=view&id=148lHhl6kVadqaUupK0RdD3QKpEXFlw_-",
            "https://drive.google.com/uc?export=view&id=1sP_j7g0c2pbBAbaXqkHVMq7Som37L6aV",
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
                "kesan": "Kalau nongkrong pasti jadi admin cerita",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Tiap ngumpul pasti ada jokes baru ",
                "pesan": "Kakak tuh update komedi harian"   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "Sering telat, tapi tetep ditunggu",
                "pesan": "semangat terus kuliahnya bang !!!"   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "Kadang kaku tapi niatnya baik",
                "pesan": "semangat terus kuliahnya bang !!!"   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "Santai banget, kayak gak punya beban",
                "pesan": "semangat terus kuliahnya bang !!!"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Orangnya ceria banget, kayak gak pernah capek ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Tiap ngomong selalu ada aja lucunya ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Sering banget jadi bahan ketawa ",
                "pesan": "Tapi kakak gak pernah baper, respect banget"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Gayanya santai, tapi kerjaannya niat",
                "pesan": "Balance banget hidupmu"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Gak pernah serius tapi hasilnya bagus ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Selalu bawa snack entah dari mana ",
                "pesan":  "kakak supplier kebahagiaan" # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kalau ngomong suka sambil nyengir ",
                "pesan": "Ekspresimu tuh gak bisa diganti"   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Sering telat tapi selalu minta maaf",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Orangnya rame, tapi hati lembut ",
                "pesan": "Kombinasi langka, jangan berubah"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Gak pernah bisa diem ",
                "pesan": "Tapi justru itu yang bikin suasana hidup"   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "Kalau bercanda gak bisa ditahan ",
                "pesan": "Coba dikontrol dikit, tapi dikit aja"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "Kalau ngelawak, timing-nya epic ",
                "pesan": "Kakaknya tuh ahli timing"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Orangnya gampang akrab ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()











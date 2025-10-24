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
            "https://drive.google.com/uc?export=view&id=1KZqmS5_iqDR-jXxT1QgkJfi6-f-tIRii",
            "https://drive.google.com/uc?export=view&id=1jh-2ujhRnN1NdFH_7MySYe_xBBGF58bR",
            "https://drive.google.com/uc?export=view&id=1OJfX7tQuFeTIzHpjST1srJ_gIg7iyAMn",
            "https://drive.google.com/uc?export=view&id=1pCBjX-o90YLmGhTdxexp7_unIqf_zMAC",
            "https://drive.google.com/uc?export=view&id=12shDXfJkp9Um2bGcYK2V7-OSA-ZxTNhI",
            "https://drive.google.com/uc?export=view&id=1PINNvl6CvOZ4irY6EEy5sp7B8W-cXI2M",
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
                "kesan": "keliatan sangar tapi aslinya baik ",  
                "pesan":"tetap berusaha jadi yang terbaik dari versi diri abang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "keren,keliatanya galak tapi ngga kok dan suka membantu",  
                "pesan":"tetap jadilah orang baik dan menebarkan kebaikan !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "seru abis dan lucu kalo ngomong",  
                "pesan":"tetap jadi pribadi yang ceria "# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kalem dan tutur katanya lembut",  
                "pesan":"selalu tebarkan aura positifmu kakk  !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "asik dan lucu orangnya seru ",  
                "pesan":"selalu tebarkan senyuman manismu kakk"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "super positive vibes ",  
                "pesan":"melangkah maju dan semoga mimpimu tercapai"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11pyJFXp00Gc58uFbWAzTR7vF0e0p0Zg3",
            "https://drive.google.com/uc?export=view&id=122EIli8cPX5NTR2QkoKRY-v3AlNW0_W_",
            "https://drive.google.com/uc?export=view&id=1gufnUrmGZeqnrRQMFv5YC9s0mrsNfFCw",
            "https://drive.google.com/uc?export=view&id=19AaTAEyXOEmV69-uHXbwlN_ojzLThIAx",
            "https://drive.google.com/uc?export=view&id=1GocTSXWPcKM1tqIZFT_sOzstRyME7zIJ",
            "https://drive.google.com/uc?export=view&id=1XGYqeQ9n5Agbyw0R057TYOEdkPHjs8JW",
            "https://drive.google.com/uc?export=view&id=1DU0xqeZnNShyAog0FcSr2PHoNj2IVc_g",
            "https://drive.google.com/uc?export=view&id=1ZjQmLGeMTKA19ITBcPCajUBB0AZbr0D5",
            "https://drive.google.com/uc?export=view&id=1ZjQmLGeMTKA19ITBcPCajUBB0AZbr0D5",
            "https://drive.google.com/uc?export=view&id=1r3N8AImRlvkw0pwz4q1X5bzhlIJk1HVR",
            "https://drive.google.com/uc?export=view&id=1GNzE5GA-43upk2gGYYIHYZ7Et1V44YXj",
            "https://drive.google.com/uc?export=view&id=1QiVMj4F3LBGPZXtuIjOf0g2lZwDYWwEd",
            "https://drive.google.com/uc?export=view&id=1UrEqwbW4IJpKhORjg0dSf882xGABZ6LV",
            "https://drive.google.com/uc?export=view&id=1Yy2TbiVaDu4mLG9zZhVIatxHSIV_uGIR",
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
                "kesan": "Ramah, sabar, dan selalu siap membantu adik tingkat kapan pun dibutuhkan.",  
                "pesan":"Terima kasih atas bimbingannya, semoga sukses selalu di setiap langkah."# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Tegas dan bertanggung jawab, sosok panutan yang disiplin dan berwibawa.",  
                "pesan":"Semoga terus jadi inspirasi dan makin sukses ke depannya."# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Ceria dan menyenangkan, selalu membuat suasana jadi hidup dan positif.",  
                "pesan":"angan pernah kehilangan semangat dan senyum terbaikmu, ya!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Bijak dan tenang, selalu memberi nasihat yang menenangkan dan bermanfaat.",  
                "pesan":"Semoga terus diberi kelancaran dan keberkahan dalam setiap hal"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "Lembut tapi tegas, selalu sopan dan tahu cara membawa diri.",  
                "pesan":"Teruslah jadi sosok menyenangkan dan penuh semangat, ya"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Humoris dan santai, tapi tetap bisa diandalkan dalam situasi serius.",  
                "pesan":"Tetaplah jadi pribadi yang anggun dan menginspirasi banyak orang."# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "Humoris dan santai, tapi tetap bisa diandalkan dalam situasi serius.",  
                "pesan":"Teruslah jadi sosok menyenangkan dan penuh semangat, ya!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Humoris tapi bijak, mampu membuat suasana jadi ringan dan hangat.",  
                "pesan":"Semoga selalu sukses dan tetap rendah hati seperti sekarang."# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Rajin dan penuh semangat, pantang menyerah dalam setiap hal.",  
                "pesan":"Semoga semua kerja kerasmu berbuah hasil terbaik."# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "Tenang dan sabar, selalu menenangkan saat suasana tegang.",  
                "pesan":"terima kasih sudah jadi contoh yang baik dan bijak."# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Ceria dan positif, selalu menularkan energi bahagia pada orang sekitar.",  
                "pesan":"Semoga selalu diberi kebahagiaan dan kesuksesan"# 1
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "engertian dan penuh empati, selalu membuat orang lain merasa nyaman.",  
                "pesan":"Tetaplah jadi pribadi yang tulus dan baik hati."# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "-",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Sopan, berwibawa, dan penuh tanggung jawab.",  
                "pesan":"Semoga masa depanmu selalu cerah dan membanggakan.!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Penuh semangat dan optimis, selalu menyebarkan motivasi ke sekitar.",  
                "pesan":"Semoga semangat itu terus hidup dan membawa kakak menuju kesuksesan besar."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1y_cj541xtEdhYYDgIdj0ceTVjkPElCr8",
            "https://drive.google.com/uc?export=view&id=1BfZayX5mccDJVxokEHzvb9BiT4UWn4zk",
            "https://drive.google.com/uc?export=view&id=1QNCrJ-7QbR4v52YPg9Gjnp9qZyb4LuMx",
            "https://drive.google.com/uc?export=view&id=1HTsNehB6KH9x76oP-8kzl42PWO0sCMF_",
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
                "kesan": "Sosok yang sangat bijak dan berwibawa. Selalu memikirkan kepentingan bersama dan mampu memimpin dengan tenang ",  
                "pesan":"Terima kasih sudah memberi teladan kepemimpinan yang luar biasa. Semoga terus sukses di setiap langkah dan tetap menginspirasi banyak orang."# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "Tegas dan bertanggung jawab dalam menjalankan tugas. Mampu menjaga keseimbangan antara kerja keras dan sikap santai yang menyenangkan.",  
                "pesan":"Teruslah jadi sosok pemimpin yang kuat dan berjiwa hangat. Semoga semua cita-citamu tercapai dengan gemilang."# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "Ramah, sabar, dan selalu terbuka terhadap pendapat orang lain. Membuat suasana kerja jadi nyaman dan penuh semangat",  
                "pesan":"Terima kasih sudah selalu membimbing dengan cara yang baik. Semoga karier dan masa depanmu penuh keberhasilan"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Inspiratif dan penuh dedikasi, selalu berusaha memberi yang terbaik untuk organisasi.",  
                "pesan":"Tetaplah jadi sosok yang berpengaruh positif bagi lingkungan sekitar. Semoga setiap langkahmu dipenuhi keberkahan dan kesuksesan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13mBWbelUFub-z3kqle69qR1-r4y8CZ7d",
            "https://drive.google.com/uc?export=view&id=1KZjm1T6Mosk4y2bUi_guNyRZRXBSM3TN",
            "https://drive.google.com/uc?export=view&id=14272MDALZlSWQyYFyMdulE9EgYf5ke84",
            "https://drive.google.com/uc?export=view&id=1VYHhgt_aQv2M-Etag4u7MSElcUH3v6fX",
            "https://drive.google.com/uc?export=view&id=17bXL1LTmbunx314VA7da1R43BQpA5ng3",
            "https://drive.google.com/uc?export=view&id=1LE94_CHysImrSI0nr0LJaB1E5sRt7UB5",
            "https://drive.google.com/uc?export=view&id=1W-XcJsuHGP1QVXGqk0IordNxrEfvmQUb",
            "https://drive.google.com/uc?export=view&id=19DDYPbwuiMeqIJOEPCtFHJ5S2FSJXwGA",
            "https://drive.google.com/uc?export=view&id=1gZYmUnAJndqEuGZaeSfD02bG44_cA7Xk",
            "https://drive.google.com/uc?export=view&id=1HYAht43385gz0MPXpz20YBPlA3b2A6yb",
            "https://drive.google.com/uc?export=view&id=1Z62bNzeFjpN7hyAnEJlDyKquc7rIqJwx",
            "https://drive.google.com/uc?export=view&id=17s6TYPru-xzOBfacEowyPTCI9tmbApO0",
            "https://drive.google.com/uc?export=view&id=1XrpZnvhsYFMlbE6R0FAi3f63S-qhsMjd",
            "https://drive.google.com/uc?export=view&id=106oXK5xgfcsWximjPfM8qmGDFzrip1QY",
            "https://drive.google.com/uc?export=view&id=1aOQOVnxeRDHGvJMjHHlHq2lMwvcsmvq3",
            "https://drive.google.com/uc?export=view&id=1fO45rPFPSMaCUpSsmRX7QNWhwnBIQSoR",
            "https://drive.google.com/uc?export=view&id=1zcj5RfYsJEJS2SNrpBVrYCidPc-EXlMN",
            "https://drive.google.com/uc?export=view&id=1LHmxj8DX_GEQoSVk9MR4thdFntPZSG0o",
            "https://drive.google.com/uc?export=view&id=1yfYd9buKkkVcI3ydogCNIw6yu43_6ot_",
            "https://drive.google.com/uc?export=view&id=1kX5EXevBs7mwM5w06OyV0K-WD2S-7kdV",
            "https://drive.google.com/uc?export=view&id=1CbgzZwzYLptDwkja2ASCsgdbJVD2huM2",
            "https://drive.google.com/uc?export=view&id=1Kd_gkSXD0lL1gMe36hUylIujbsu3Docr",
            "https://drive.google.com/uc?export=view&id=1YLbcAQpnyJdk9ftsnWgc72f4GBVKtoF9",
            "https://drive.google.com/uc?export=view&id=1jD7Fxjv-d677_NaJZxm-nhk1-mPaiKtM",
            "https://drive.google.com/uc?export=view&id=1TsrAtLcp7iqWn4B-w0Rqr7k7_lXtlGK9",
            "https://drive.google.com/uc?export=view&id=1fFwA9md-wSeh2raRhD9rSADyJncDmu2L",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal": "medan",
                "alamat": "tanjung senang",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Ramah dan sabar, selalu siap membantu tanpa banyak bicara.",
                "pesan": "Terima kasih atas kebaikan dan bimbingannya, semoga sukses selalu."
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpri,sukarame",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "Tegas tapi menyenangkan, disiplin dalam segala hal.",
                "pesan": "Teruslah jadi panutan dan inspirasi bagi banyak orang."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Sosok yang bijak, berwibawa, dan mampu membawa suasana tetap tenang dalam berbagai keadaan. Selalu berpikir matang sebelum bertindak, sehingga jadi panutan bagi banyak orang.",
                "pesan": "Terima kasih atas keteladanan dan dedikasinya. Semoga terus sukses, dan setiap langkah yang diambil selalu diberi kemudahan."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Bijak dan tenang, selalu memberi arahan dengan cara yang baik.",
                "pesan": "Semoga terus diberi kelancaran dan keberkahan dalam setiap langkah."
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Ceria dan penuh semangat, selalu membawa energi positif.",
                "pesan": "Jangan pernah hilangkan semangat dan senyum terbaikmu, ya!"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Humoris dan santai, tapi serius saat dibutuhkan.",
                "pesan": "Teruslah jadi sosok menyenangkan dan bersemangat, ya"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Peduli dan perhatian, nggak ragu membantu siapa pun",
                "pesan": "Terima kasih atas ketulusanmu, semoga dibalas dengan kebahagiaan."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "Tenang dan dewasa, selalu bisa memberi rasa aman saat dibutuhkan.",
                "pesan": "Semoga segala urusan dan rencanamu selalu dimudahkan"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "Ramah dan mudah bergaul, membuat suasana jadi hangat.",
                "pesan": "tetap jadi pribadi yang menyenangkan dan positif."
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Humoris tapi bijak, tahu kapan harus serius dan bercanda.",
                "pesan": "Semoga selalu sukses dan tetap rendah hati seperti sekarang."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Rajin dan penuh tanggung jawab, selalu total dalam setiap hal.",
                "pesan": "semoga kerja kerasmu membawa hasil terbaik."
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "Tenang dan sabar, jadi penengah yang baik di setiap keadaan.",
                "pesan": "Terima kasih sudah jadi contoh yang bijak dan dewasa."
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "ranah dan optimis, selalu menularkan energi positif.",
                "pesan": "Semoga selalu bahagia dan dikelilingi orang baik."
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "Pengertian dan lembut dalam bertutur.",
                "pesan": "Tetaplah jadi pribadi yang menenangkan dan tulus."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Sopan dan berwibawa, mampu menjaga sikap dengan baik.",
                "pesan": "Semoga masa depanmu selalu cerah dan membanggakan."
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Rendah hati dan menghargai semua orang tanpa pandang siapa pun.",
                "pesan": "Teruslah jadi pribadi yang bijak dan inspiratif."
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "Penuh semangat dan tak mudah menyerah.",
                "pesan": "Semoga semangat itu selalu hidup dan membawamu menuju kesuksesan."
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "Bijak dalam mengambil keputusan dan selalu adil.",
                "pesan": "Semoga terus jadi sosok yang dipercaya dan disegani."
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Tulus dan apa adanya, selalu membuat orang lain nyaman.",
                "pesan": "tetaplah jadi pribadi yang hangat dan rendah hati"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "Berani dan percaya diri, selalu tampil yakin di depan banyak orang.",
                "pesan": "Semoga keyakinanmu membawa ke banyak pintu keberhasilan."
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Disiplin dan tangguh, nggak mudah menyerah menghadapi tekanan.",
                "pesan": "eruslah berjuang, hasil baik pasti akan datang padamu."
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Penuh ide dan kreatif, selalu punya cara baru dalam menyelesaikan hal",
                "pesan": "Semoga kreativitasmu terus berkembang dan bermanfaat bagi banyak orang."
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "Ramah tapi tetap tegas, mampu menyeimbangkan sikap dengan baik.",
                "pesan": "Tetaplah jadi sosok yang kuat dan menyenangkan seperti sekarang."
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Cerdas dan tanggap, cepat memahami situasi dan orang lain",
                "pesan": "Semoga kecerdasanmu terus membawa manfaat dan keberhasilan"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Penuh dedikasi dan tanggung jawab, selalu total dalam setiap tugas.",
                "pesan": "Terima kasih atas kerja keras dan teladan yang diberikan."
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Bijak, sabar, dan mampu menjaga keharmonisan dengan semua orang.",
                "pesan": "Semoga selalu diberi kebahagiaan, keberkahan, dan kesuksesan di masa depan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IhAYd0ZHOJ-gwwiGWxRuBElPIPZXnXWl",
            "https://drive.google.com/uc?export=view&id=1HvpdvWXRFjCgV6xuCgRVsSths_JI2Zan",
            "https://drive.google.com/uc?export=view&id=10E5EugVbySnLBeJ_eBgMrIkOhgHhsNQj",
            "https://drive.google.com/uc?export=view&id=1wjCP-MpNDo7rmAYrg-xiCpyVVfI3Etx5",
            "https://drive.google.com/uc?export=view&id=1vETcjoqup_suPGPIDcPJ5tXSyYpZo4V8",
            "https://drive.google.com/uc?export=view&id=1Z9e6jmxLTdksOOFHt4HFcZ0YYdMq1pBC",
            "https://drive.google.com/uc?export=view&id=1bJUHFgWP3bqLYVjbuHr4wVGCNz_YSNGD",
            "https://drive.google.com/uc?export=view&id=1VwVCLPg9VyDN2L0uYGeF3YcVlcp4I6ER",
            "https://drive.google.com/uc?export=view&id=1ZD5e7A3hni9dqmosn7E_ShrUvBCq5Wwk",
            "https://drive.google.com/uc?export=view&id=1NVebteWz_5ZVTOGefD-kXnp5ncOfdOpJ",
            "https://drive.google.com/uc?export=view&id=1cTc9-Tt1qiS5k5tgzJ6Uc9FV1-KNqZP1",
            "https://drive.google.com/uc?export=view&id=1yOFxX22f-NkRHj4UgikXt-eXxHywWDC9",
            "https://drive.google.com/uc?export=view&id=1JdkNBwHTKEqAq3mhsGlvLkr6YJksnbe7",
            "https://drive.google.com/uc?export=view&id=16_zxrq60HiHOyOwmF8KV6Mjn076rZKQP",
            "https://drive.google.com/uc?export=view&id=17pvQ76E1gGu3k75sW66Iv_xDTUde8fqC",
            "https://drive.google.com/uc?export=view&id=1lh1XYgNLHBAZuNMFkrM7Qv-aVuNlJ2Oq",
            "https://drive.google.com/uc?export=view&id=1_Qx50RLsj6TUTyAsfULtcIixPjg7tjBL",
            "https://drive.google.com/uc?export=view&id=1UUTvrzn4meEM9NZlCMXs6PDWspHt9WMc",
            "https://drive.google.com/uc?export=view&id=11MmZtQ2POnIkVtv6JW1MyAp5Tsgqlmsy",
            "https://drive.google.com/uc?export=view&id=1zaO0_R1f-tURWcRrhmhhUia3IIkh0Dhw",
            "https://drive.google.com/uc?export=view&id=1-poQcCKvkb-1onq_o9Z5LNLNxGExmQ5G",
            "https://drive.google.com/uc?export=view&id=1vbawewZe8MMaC5wW_geGGAI1c2a4Z5U5",
            
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
                "kesan": "Aktif dan selalu semangat dalam setiap kegiatan. ",
                "pesan": "Teruslah berproses dan jangan pernah takut mencoba hal baru"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "Ramah dan mudah bergaul, bikin suasana jadi lebih seru ",
                "pesan": "Tetap jadi pribadi yang ceria dan menyenangkan ya"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Disiplin dan tegas, selalu jadi panutan dalam hal tanggung jawab. ",
                "pesan": "Semoga ketegasanmu terus membawa kebaikan dan keberhasilan"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Penuh ide dan kreatif, selalu punya cara unik dalam menyelesaikan masalah. ",
                "pesan": "Terus asah kreativitasmu dan jadilah inspirasi untuk banyak orang."
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Humoris dan suka bikin suasana cair. ",
                "pesan": "Jangan pernah kehilangan sisi lucumu, karena itu yang bikin semua senang."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Pendengar yang baik dan selalu supportif ke teman-temannya. ",
                "pesan": "Terus jadi tempat nyaman buat curhat ya, kamu keren banget!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Kalem tapi perhatian, bikin suasana tim tetap tenang.",
                "pesan": "Semoga ketenanganmu selalu jadi kekuatan buat sekitar."
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "Cerdas dan cepat tanggap, selalu bisa diandalkan dalam situasi apa pun",
                "pesan": "Pertahankan semangat belajarmu, masa depanmu pasti gemilang.!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Ceria dan energik, selalu menularkan semangat positif. ",
                "pesan": "Teruslah menebar energi baik ke siapa pun yang kamu temui."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Rajin dan teliti, nggak pernah setengah-setengah dalam kerja. ",
                "pesan": "Jangan lelah jadi orang yang detail, hasilnya pasti luar biasa."
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Bijak dan sabar, selalu ngasih solusi dengan kepala dingin. ",
                "pesan": "Teruslah jadi panutan dengan sifat tenang dan bijakmu itu."
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "Tegas tapi peduli, tahu kapan harus serius dan kapan bercanda. ",
                "pesan": "Semoga karaktermu yang kuat ini jadi bekal sukses di masa depan."
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "Rendah hati dan sopan, selalu menghargai siapa pun tanpa pandang.",
                "pesan": "Tetaplah jadi pribadi yang ramah dan membumi seperti sekarang."
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Pekerja keras dan pantang menyerah.",
                "pesan": "Percaya deh, semua kerja kerasmu bakal terbayar nanti!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "Ceria tapi fokus, tahu kapan harus main dan kapan harus serius",
                "pesan": "Terus pertahankan keseimbangan itu, kamu luar biasa!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Berani dan penuh tanggung jawab, nggak takut ambil keputusan. ",
                "pesan": "Teruslah jadi sosok kuat yang bisa diandalkan banyak orang."
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Suka bantu dan nggak perhitungan, tulus banget orangnya",
                "pesan": "Semoga semua kebaikanmu dibalas berlipat oleh Tuhan."
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "Selalu semangat dan nggak mudah nyerah meski keadaan sulit",
                "pesan": "Tetap kuat dan terus melangkah, sukses sudah menunggumu."
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Tenang dan santai, tapi tetap fokus pada tujuan. ",
                "pesan": "Jangan pernah ubah sifat positifmu, itu kelebihanmu yang langka!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Visioner dan penuh rencana, selalu tahu apa yang ingin dicapai. ",
                "pesan": "Terus kejar mimpi-mimpimu dengan semangat yang sama.!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Sopan, disiplin, dan punya sikap yang dewasa.",
                "pesan": "Pertahankan sifat baikmu, karena itu nilai plus yang luar biasa."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Selalu hadir membawa tawa dan semangat di setiap pertemuan.",
                "pesan": "Jangan berubah ya, dunia butuh orang sepositif kamu!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1a7hWvTgv9rKD5P20vLCRey1qAwZiPuJ9",
            "https://drive.google.com/uc?export=view&id=1iJXUR6P1-gMFr67WyCr9Ae5ZQLf6E5om",
            "https://drive.google.com/uc?export=view&id=1baY2lnp_XqulWEggg5jo_iA0ke7TzhU_",
            "https://drive.google.com/uc?export=view&id=10edTjMt49YxcZWMSh_lz9I3U5AJ_7WBi",
            "https://drive.google.com/uc?export=view&id=1CnVuQ1m0lU4XBN6dhCHbVPkpFlKNUV8z",
            "https://drive.google.com/uc?export=view&id=1v5CslcRfv1BeBnOn_guAA3L6NWqF7wzh",
            "https://drive.google.com/uc?export=view&id=1EITvIAvAqpHNf9fIkvajG7oft-jFwxr0",
            "https://drive.google.com/uc?export=view&id=1CU86NBP8QXKfJUwmagotrEr7mMMK3l0M",
            "https://drive.google.com/uc?export=view&id=16klbByY2G2cvJaQmzE0jkqUqucJN4KEE",
            "https://drive.google.com/uc?export=view&id=1ZFR9yCyi8EP0q38HNJKToIBCrZ3WTiKq",
            "https://drive.google.com/uc?export=view&id=1IIZkPgP7JzBWALTz-iA0ztbQTdnIUbO9",
            "https://drive.google.com/uc?export=view&id=1xgGW244pg6q9V-bkdVmvFC0-zikPgCKM",
            "https://drive.google.com/uc?export=view&id=1W5sGl08cECDuYYmSdOmErW01lQA0J2Rb",
            "https://drive.google.com/uc?export=view&id=1C3hTFDZ6PVo56n2OgJ3rLSNOshwYUPMQ",
            "https://drive.google.com/uc?export=view&id=13IS_tNq7WobzkrVsl5nyV2lqg4yG_1zJ",
            "https://drive.google.com/uc?export=view&id=1Z1CqdUvChCsM7KZbTvjAkfVOD6gRO2R9",
            "https://drive.google.com/uc?export=view&id=1h24QVU6H3CpTVA3RRe4ixr0y-9raudAV",
            "https://drive.google.com/uc?export=view&id=1OJ1HHGJQMGZN-_PHl5fArlg1Bo-JjQIM",
            "https://drive.google.com/uc?export=view&id=1TJ29eMNcARaoNvuMUUJLgkRPjQHfe8WS",
            "https://drive.google.com/uc?export=view&id=1F85vYy9qQK7B1SvZMUcK-Qm1ENHR6BRe",
            "https://drive.google.com/uc?export=view&id=1NBnRpNIYl4gu0jkr5HOZKis4XDz6yrxh",
            "https://drive.google.com/uc?export=view&id=1POXYBOpdve8ePtMCT-OlFv48iOq5VVa9",
            "https://drive.google.com/uc?export=view&id=13M37N1kbKZ2XMTZ56qGzDc0D6ccTbwnj",
            "https://drive.google.com/uc?export=view&id=13Ok6qVU-BnjCGHLApqmVcmwJz4fOhc0a",
            
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
                "kesan": "Aktif banget di kegiatan luar, selalu jadi representasi yang keren buat himpunan",
                "pesan": "Teruslah jadi sosok yang berani tampil dan membawa nama baik kampus."
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Pandai berkomunikasi dan cepat akrab sama siapa pun",
                "pesan": "Gunakan kemampuanmu itu buat terus membangun relasi yang positif ya"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Percaya diri dan nggak ragu ngomong di depan orang banyak",
                "pesan": "Terus asah kemampuan public speaking-mu, kamu punya potensi besar banget."
            },
           {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Punya jiwa kepemimpinan yang kuat dan tegas dalam bersikap.",
                "pesan": "Pertahankan sikap tegas dan tanggung jawabmu, kamu calon pemimpin hebat"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Ramah dan terbuka, selalu bikin suasana kerja sama jadi nyaman.",
                "pesan": "etaplah jadi pribadi yang menyenangkan dan mudah didekati seperti sekarang"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Cerdas dan punya banyak ide brilian buat pengembangan relasi.",
                "pesan": "Jangan berhenti berinovasi ya, ide-ide kamu selalu ditunggu"
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Tenang dan logis, selalu bisa berpikir jernih waktu yang lain panik.",
                "pesan": "Pertahankan sikap bijakmu, itu salah satu kelebihan yang langka banget."
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "Ceria dan supel, bikin hubungan eksternal jadi makin luas.",
                "pesan": "Terus sebarkan energi positifmu ke setiap orang yang kamu temui."
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Pekerja keras dan nggak pernah setengah-setengah kalau udah mulai sesuatu.",
                "pesan": "Tetap konsisten ya, hasil terbaik pasti datang buat kamu."
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "Berani tampil beda dan nggak takut ambil risiko.",
                "pesan": "Teruslah jadi pribadi yang berani, karena langkah besar dimulai dari keyakinan."
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "Kalem tapi punya pengaruh besar dalam tim.",
                "pesan": "Teruslah berkontribusi dengan caramu sendiri, hasilnya selalu terasa."
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "Tegas tapi tetap sopan, bisa menyeimbangkan profesional dan ramah.",
                "pesan": "Pertahankan caramu bersikap itu, keren banget buat dicontoh."
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Selalu bisa nyatu di mana pun, adaptasimu luar biasa",
                "pesan": "Terus gunakan kemampuan itu buat menjalin relasi yang lebih luas lagi."
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "Ceria dan punya selera humor yang tinggi, bikin tim nggak kaku.",
                "pesan": "Tetap jadi pembawa tawa dan semangat di mana pun kamu berada"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "Teguh pendirian dan punya prinsip kuat.",
                "pesan": "Pertahankan nilai-nilai baikmu itu, kamu sosok yang berkarakter banget."
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "Suka bantu teman lain, nggak pernah pelit ilmu ",
                "pesan": "Teruslah berbagi kebaikan, karena itu hal yang bikin kamu istimewa."
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Selalu jadi sosok yang nyenengin dan bikin suasana rame setiap kali bareng-bareng. Obrolannya ringan tapi selalu ngena, candanya kadang absurd tapi justru itu yang bikin ngakak. Kehadiran orang ini tuh kayak moodbooster alami, susah banget buat nggak nyaman kalau udah bareng.. ",
                "pesan": "Jangan ubah gaya caramu dan sikapmu yang chill tapi tetap produktif itu ya!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Punya karakter yang tulus, rajin, dan penuh energi, tapi di sisi lain juga lucu dan gampang bikin orang lain ketawa. Setiap interaksi selalu meninggalkan kesan yang ringan tapi berharga.. ",
                "pesan": "Terus pelihara sikap terbukamu, kamu bikin suasana tim lebih sehat."
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Tulus dan nggak suka cari pujian, kerja dalam diam tapi hasilnya nyata.",
                "pesan": "Semoga ketulusanmu selalu jadi berkah di setiap langkah."
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Optimis dan selalu lihat sisi positif dari apa pun. ",
                "pesan": "Jangan biarkan semangatmu padam, kamu bikin semua orang ikut semangat."
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Punya gaya bicara yang sopan tapi tetap tegas.",
                "pesan": "Pertahankan gaya komunikasimu itu, sangat profesional dan berwibawa."
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Sering jadi penghibur waktu semua mulai lelah",
                "pesan": "Teruslah menyebarkan tawa dan semangat, kamu bikin suasana selalu hidup."
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Rapi dan terorganisir banget, bikin tim kerja jadi efisien. ",
                "pesan": "Jangan tinggalkan kebiasaan bagusmu itu, bakal kepake terus nanti."
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "Ramah, sopan, dan selalu menghargai siapa pun yang diajak kerja sama. ",
                "pesan": "Teruslah jaga sikap baikmu itu, karena kamu contoh yang patut ditiru."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Kc6st_CEp2YB5snBtLRTj1KMeIurqPVO",
            "https://drive.google.com/uc?export=view&id=1n4gg1-VLptOkwbLaLSMXZZE1yZOoJR2X",
            "https://drive.google.com/uc?export=view&id=1lJV3Gym4TXE-CkMnXQu5BG5McxldhrMX",
            "https://drive.google.com/uc?export=view&id=17pW2jHlqY2svUceDdSEQqCOa6rD-GYDj",
            "https://drive.google.com/uc?export=view&id=1mog1xWSceuEiUenC1XvyruczY01UVsIE",
            "https://drive.google.com/uc?export=view&id=1bDtBdL0b_ir7PxlOlHlfOKCbqTlBv7QT",
            "https://drive.google.com/uc?export=view&id=1nSglq_qKU833qHi4ybNDRaKc9nglb8Sl",
            "https://drive.google.com/uc?export=view&id=1iFF3DyFhy-CzK_aq0zDJ-6txDL4OVXLE",
            "https://drive.google.com/uc?export=view&id=14OCT-nDp0eFaZutg-fK1mqycU6qvkVD9",
            "https://drive.google.com/uc?export=view&id=10g_qsawBVSv_U-1J4ff2x8ttEu-mfEE9",
            "https://drive.google.com/uc?export=view&id=1BpKjXBlzzpKiUT0kJjPU4YJZDgEXq9AV",
            "https://drive.google.com/uc?export=view&id=1TcRSXwjfjZeqzdUCmb9MhGAzWGrrw9Sz",
            "https://drive.google.com/uc?export=view&id=171q8uo9iJGa_Z3DXqPzX57hZK_hjGGLW",
            "https://drive.google.com/uc?export=view&id=1UBNVlY-jskmJHipWC4KMsAupeHW-I_lP",
            "https://drive.google.com/uc?export=view&id=1PBWOBmC_wEvl-mI3SOf2L-P0k_cmjdM8",
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
                "kesan": "Selalu semangat dan aktif di setiap kegiatan, bikin suasana jadi hidup. ",  
                "pesan": "Terus pertahankan energimu itu ya, kamu punya aura positif yang keren banget!!" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Ramah dan gampang diajak kerja bareng, nggak pernah bikin suasana tegang.",  
                "pesan": "Tetap jadi pribadi yang menyenangkan, semoga sukses terus ke depannya" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Teliti dan bertanggung jawab, selalu maksimal dalam setiap tugas.",  
                "pesan": "Terus jaga konsistensimu, hasil besar bakal datang dari usaha sekecil apa pun." # 3
            },
            {
                "nama": "Rendy",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "Ceria dan suka bercanda, tapi tetap bisa serius kalau udah kerja. ",  
                "pesan": "Jangan pernah hilang sisi ceriamu, itu yang bikin semua nyaman di sekitarmu" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kalem tapi punya pendirian kuat, diam-diam ngasih banyak pengaruh positif. ",  
                "pesan": "Teruslah jadi pribadi tenang yang selalu bikin suasana adem" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "Kreatif banget dan penuh ide, selalu ada aja hal baru yang kamu bawa. ",  
                "pesan": "Jangan berhenti berinovasi ya, dunia butuh orang seimajinatif kamu." # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Sabar dan pengertian, selalu bisa jadi penengah di tengah perbedaan pendapat. ",  
                "pesan": "Semoga sifat sabarmu tetap jadi kekuatanmu ke depannya." # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "Dewasa dan bijak, cara berpikirmu selalu bikin orang kagum. ",  
                "pesan": "Teruslah jadi contoh yang baik, kamu punya jiwa kepemimpinan yang kuat." # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "Humoris tapi tangguh, bisa bikin semua ketawa walau lagi capek",  
                "pesan": "Teruslah jadi pembawa tawa di mana pun kamu berada, itu hal langka" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Aktif dan punya semangat tinggi buat terus berkembang.",  
                "pesan": "Jangan pernah padamkan semangatmu, masa depanmu cerah banget" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Tulus dan suka bantu orang lain tanpa pamrih. ",  
                "pesan": "Kebaikanmu luar biasa, semoga semua itu dibalas berkali lipat" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Tenang tapi fokus, jarang ngomong tapi pas ngomong selalu berisi. ",  
                "pesan": "Pertahankan karaktermu itu ya, karena kamu selalu bisa diandalkan." # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "Disiplin dan konsisten, nggak suka setengah-setengah dalam kerja.",  
                "pesan": "Terus semangat, hasil kerja kerasmu pasti kebayar nanti." # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "Ceria dan suka nyemangatin orang lain. ",  
                "pesan": "Teruslah jadi sumber energi baik buat sekitarmu, kamu menular banget" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Rendah hati dan nggak pernah sombong meski udah keren banget ",  
                "pesan": "Tetap jadi pribadi yang sederhana tapi luar biasa ya" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hxueXOzDIYgpMAq6WHLuWIQmp8Wb1bG0",
            "https://drive.google.com/uc?export=view&id=175EYkXWKENAOSqyNOmy0ZEg5laDdJTs0",
            "https://drive.google.com/uc?export=view&id=1hwZ7TczGVyOCK08XcavkpxwE_jpIKAHf",
            "https://drive.google.com/uc?export=view&id=1syfzP0kAjEPE1l-mRaUpUhOQccKMrV1c",
            "https://drive.google.com/uc?export=view&id=1pu6Ryyr1bfOBMzQG-azzQMLkhi5hMbgl",
            "https://drive.google.com/uc?export=view&id=1CbxVBd5CllzwnHzTExdC00lmN-uq9NME",
            "https://drive.google.com/uc?export=view&id=1DM9wTLpISuhOwPwyeuntGhLcvSu1DbIf",
            "https://drive.google.com/uc?export=view&id=1zOqAY8Yn3DxIzmDU_umYcgG9z3UUkSnW",
            "https://drive.google.com/uc?export=view&id=1waNp1Kee4QnatC7yHitViSPgpI5-35b2",
            "https://drive.google.com/uc?export=view&id=1_sDDaxFgvNuTYbTSm3BQv7Ph3OMlsHea",
            "https://drive.google.com/uc?export=view&id=1q4fwOTNOm13aNs7N9aAMrulQRK3pQhhr",
           
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
                "kesan": "Orangnya tangguh dan penuh semangat, selalu total dalam menjalankan tanggung jawab di SSD. ",
                "pesan": "Terus semangat dan jangan pernah bosan berproses, semoga semua usahamu berbuah hasil terbaik.!"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Ramah, sabar, dan selalu menenangkan saat suasana sedang tegang. ",
                "pesan": "Terima kasih udah jadi sosok yang menyejukkan, semoga ke depannya makin sukses dan bahagia."   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Disiplin dan bertanggung jawab, selalu jadi contoh baik dalam hal kedisiplinan. ",
                "pesan": "Pertahankan sikap positif itu ya, semoga sukses selalu menyertai setiap langkahmu."   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "ktif dan berani menyuarakan pendapat, bikin suasana rapat jadi hidup ",
                "pesan": "Semoga terus jadi pribadi yang berani, cerdas, dan percaya diri dalam setiap langkah."   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "Ceria dan mudah bergaul, selalu bisa bikin suasana jadi lebih menyenangkan",
                "pesan": "Tetap jadi pribadi yang membawa kebahagiaan buat sekitar, semoga makin sukses!"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Tenang tapi tegas, mampu menjaga keseimbangan dalam kerja tim.",
                "pesan": "Teruslah jadi sosok yang kuat dan bijak, semoga semua cita-cita tercapai."   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Rajin dan teliti, selalu memastikan semua hal berjalan sesuai rencana.",
                "pesan": "Semoga setiap kerja kerasmu membawa hasil manis di masa depan."   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Penuh ide kreatif dan punya semangat tinggi buat terus maju. ",
                "pesan": "jangan berhenti berinovasi ya, semoga makin sukses dan terus menginspirasi"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "Sopan, rendah hati, dan menghargai semua orang tanpa pandang siapa pun. ",
                "pesan": "Tetap pertahankan kepribadian baikmu itu, karena itu yang bikin kamu disukai banyak orang."   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Tanggung jawab dan bisa diandalkan, selalu siap bantu teman lain tanpa diminta. ",
                "pesan": "Terima kasih atas ketulusannya, semoga langkahmu selalu diberkahi."   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "Bijak dan dewasa, selalu memberi arahan dengan cara yang menenangkan ",
                "pesan": "Teruslah jadi pribadi yang menginspirasi, semoga kesuksesan selalu menyertai setiap jalanmu"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14CGIUfrWztnJ0jCZevzZgrTDmrbZEWOd",
            "https://drive.google.com/uc?export=view&id=1tGV67-vXlnqpgQeQb3u8_V3aNFMTrlpQ",
            "https://drive.google.com/uc?export=view&id=10iKjXT0L3P1jNWVjB54-evaIl-tTASkK",
            "https://drive.google.com/uc?export=view&id=1yAFfpX7kcOAKZIwPLFPXrvDI9thLeiZM",
            "https://drive.google.com/uc?export=view&id=1zjowtSeYF9FnL2jdx-ZleYqi6nJ2vl3K",
            "https://drive.google.com/uc?export=view&id=1RDVqo5bw_JUlmbyBBTWRDfIP9AWzVYxD",
            "https://drive.google.com/uc?export=view&id=1buWV2RJFnaH3dYdGyyzSt7-p-TjD9jFa",
            "https://drive.google.com/uc?export=view&id=1bQrG0s6e3anUbXGtEP1Cs1lyC4Ulb0U8",
            "https://drive.google.com/uc?export=view&id=1j8UXrsrfyvLc-1g6ZAICIXLlB8wTOlMH",
            "https://drive.google.com/uc?export=view&id=1OzAP0cbO8C7XlYYq7-X8HVDj2zGiglnM",
            "https://drive.google.com/uc?export=view&id=1APrijxGHNkSs9sYktMAa7ShWqzEw7rPp",
            "https://drive.google.com/uc?export=view&id=1z-YS88NsgpoFbfeUFwqrWMc32UssEKPt",
            "https://drive.google.com/uc?export=view&id=1f0B2ZZ7mVbyGXPOGy8ccy6b9_T3cHJXl",
            "https://drive.google.com/uc?export=view&id=1oUj6jOzf7jB7TVF2P0SsFanvjheuzHXt",
            "https://drive.google.com/uc?export=view&id=1OVVU7WZGLCOjaLmNbTTnj2yv9tf5xsR_",
            "https://drive.google.com/uc?export=view&id=1ZnzCQw6r8Z7rfpYCjYCtTRQGsRbgQYyS",
            "https://drive.google.com/uc?export=view&id=16OCe_tdFSHyN5y3TgE62jV_HP_982ste",
            "https://drive.google.com/uc?export=view&id=18kQ00omcZSpf8BGweFnugH6f65_0x3qR",
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
                "kesan": "Ceria dan aktif, selalu bawa suasana jadi hidup. ",
                "pesan": "Teruslah menebar energi positif ke semua orang ya!"   # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Ramah dan mudah bergaul, gampang banget bikin orang nyaman.",
                "pesan": "Tetap jadi pribadi yang hangat dan menyenangkan."   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "Disiplin dan bertanggung jawab, selalu tepat waktu dan bisa diandalkan. ",
                "pesan": "Semoga semangatmu tetap konsisten di mana pun berada."   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "Sabar dan tenang, selalu bisa menenangkan suasana kalau lagi ribut.",
                "pesan": "Jangan kehilangan ketenanganmu ya, itu hal yang berharga banget."   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "Humoris dan asik, bikin suasana kerja nggak kaku. ",
                "pesan": "Tetaplah jadi sumber tawa dan semangat buat semua orang"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Teliti dan rapi, semua hal selalu kamu kerjakan dengan baik.",
                "pesan": "Terus pertahankan sikap telitimu, karena itu kunci suksesmu."   # 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Bijak dan dewasa dalam berpikir. ",
                "pesan": "Teruslah jadi pribadi yang bisa jadi contoh dan panutan."   # 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Berani dan tegas, tahu kapan harus bicara dan bertindak. ",
                "pesan": "Jangan takut buat terus bersuara dan ambil langkah besar.!"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Ceria tapi fokus, bisa jaga keseimbangan antara kerja dan santai.",
                "pesan": "Pertahankan keseimbangan itu ya, kamu keren banget!"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Penuh ide dan kreatif, selalu ada cara baru buat nyelesain masalah. ",
                "pesan": "Terus kembangkan kreativitasmu, dunia butuh orang seperti kamu"   # 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Rajin dan nggak gampang nyerah, selalu berusaha sampai berhasil ",
                "pesan": "Tetap semangat ya, hasil nggak akan khianatin prosesmu."   # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kalem dan rendah hati, nggak suka menonjol tapi selalu berarti. ",
                "pesan": "Jangan ubah kepribadianmu yang tulus itu, kamu berharga banget."   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Tegas tapi perhatian, tahu cara menjaga keseimbangan tim.",
                "pesan": "Teruslah jadi sosok yang kuat tapi tetap hangat."   # 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Ceria dan optimis, selalu ngasih semangat ke teman-teman. ",
                "pesan": "Jangan pernah padamkan semangatmu, itu yang bikin kamu unik.!"   # 14
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Pendengar yang baik dan nggak mudah menghakimi",
                "pesan": "Terima kasih udah jadi tempat cerita yang nyaman."   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "tanggung jawab dan kerja kerasnya patut diacungi jempol. ",
                "pesan": "Semoga semua usahamu berbuah hasil yang terbaik"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "Tenang dan santai tapi tetap fokus. ",
                "pesan": "Pertahankan gaya kerjamu itu, bikin suasana tetap adem"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Rendah hati dan selalu menghargai orang lain. ",
                "pesan": "Teruslah jadi pribadi yang sopan dan disukai banyak orang."   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()











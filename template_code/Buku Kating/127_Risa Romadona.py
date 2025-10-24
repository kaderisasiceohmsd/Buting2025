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
            "nav-link-selected": {"background-color": "#ffb6c1"},
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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yDmkK0oY2Kk9NDBxu4_n_67mTOMiI0ql",
            "https://drive.google.com/uc?export=view&id=1bAKllhxLkPGWb1LMzLKRq55PJt5pnxEW",
            "https://drive.google.com/uc?export=view&id=1hxyU1gwuOTNj4O1AccdcR95FGf-Q_A0n",
            "https://drive.google.com/uc?export=view&id=1HPPtYFt17A4J6dZ0kAlEfWbIX7cbli29",
            "https://drive.google.com/uc?export=view&id=1OUuQjlctQMbkwpNusHXByjCWXYMBvYla",
            "https://drive.google.com/uc?export=view&id=1pwWCzXbNR8rA2c3FYPV0f5Ty7jM-BANw",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Bang Rendra terlihat tegas dan mudah diajak ngobrol.",
                "pesan": "Semoga kuliahnya lancar dan jangan lupa istirahat juga!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "baca buku (dasar-dasar sql)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Johannes ramah dan siap membantu.",
                "pesan": "Tetap semangat belajar dan jangan lupa nikmati kuliahmu!"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Airest Kost",
                "hobbi": "siram shopee",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Elisabeth ceria dan supel.",
                "pesan": "Semoga tetap sehat dan semangat terus!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza terlihat kalem tapi bertanggung jawab.",
                "pesan": "Tetap jadi pribadi yang konsisten!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "baca buku, saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty ceria dan positif.",
                "pesan": "Semoga selalu bahagia!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang, Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kak Farahanum kalem dan rapi.",
                "pesan": "Semoga semua urusan kuliah dan organisasi lancar!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uqTF5x3OLSd7zgkSHUpoGUo_u5Fi9_F0",
            "https://drive.google.com/uc?export=view&id=1kx3PGSQgP9nzrsWrS38skaOOUBAmLc6a",
            "https://drive.google.com/uc?export=view&id=1csKengjzM0ONw7Oqn4qiHqiOmoRzC7fp",
            "https://drive.google.com/uc?export=view&id=1PnEdmtdtw1sAK9f3kvUOsykVdIKvoQyq",
            "https://drive.google.com/uc?export=view&id=1JqDtbRqER6Oo7klSteSVlYtIJBdjfYPr",
            "https://drive.google.com/uc?export=view&id=18A7dptMgWUL5A5KUbktU_6c0Wk7hMjFL",
            "https://drive.google.com/uc?export=view&id=1H0FFlz3DDyPUnMzrWoN0MHU8U7708dpr",
            "https://drive.google.com/uc?export=view&id=15Sb0uElIhk6lLtHq9bA9iHyi9BlYZyQt",
            "https://drive.google.com/uc?export=view&id=1cG69FnRZtVzZIZ7xzCgbcsJi_CMjabsD",
            "https://drive.google.com/uc?export=view&id=1tPPuyjiGzJh0vwSVKBXn0pSvm_Glo31C",
            "https://drive.google.com/uc?export=view&id=1iP1KA_Fx6uKYo4MmBR7vHJMdwW9qFhQ0",
            "https://drive.google.com/uc?export=view&id=1KwITzEiSF1CPBw141AAk2FK3b_IMsUlR",
            "https://drive.google.com/uc?export=view&id=1BQxpH6_-zbJxq0GhkqfuGIFss0KpuZpG",
            "https://drive.google.com/uc?export=view&id=1_exVlWugZroC0FkxNrM8NTN1sB5FWgld",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Yapping",
                "sosmed": "@Jeremia_s_",
                "kesan": "Abangnya seru, punya pembawaan tenang tapi tetap asik diajak ngobrol.",
                "pesan":"Semangat terus dalam menjalani kesibukan kuliah dan organisasi!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122350004",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Ceria dan ramah, gampang banget bikin suasana jadi hangat.",
                "pesan":"Terus jadi sosok yang menyenangkan ya, jangan lupa istirahat cukup!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Baik, supel, dan selalu nyebarin energi positif ke sekitar.",
                "pesan":"Tetap semangat dan terus berkembang ya, kamu keren!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Santai tapi tangguh, pembawaannya adem banget.",
                "pesan":"Semoga selalu diberi kelancaran di setiap langkahnya!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Ramah dan bijak, obrolannya selalu berbobot tapi tetap seru.",
                "pesan":"Terus jadi panutan yang rendah hati dan inspiratif!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Ramah dan lembut, enak banget diajak kerja bareng.",
                "pesan":"Semoga semua urusan dan cita-cita kakak dimudahkan!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Humoris tapi tetap sopan, gampang bikin orang nyaman.",
                "pesan":"Terus jadi pribadi yang positif dan jangan lupa semangat!"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Lucu, ceria, dan selalu bawa suasana jadi hidup.",
                "pesan":"Semangat terus ya, semoga makin percaya diri dan sukses!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Santai tapi berwawasan luas, enak banget kalau diskusi bareng.",
                "pesan":"Tetap semangat ngejar mimpi dan terus jadi inspirasi!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Ceria, kreatif, dan punya aura positif yang nular.",
                "pesan":"Semoga karier dan kuliah berjalan lancar seperti alunan lagu favoritmu!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya tenang dan dewasa, tapi tetap seru diajak ngobrol.",
                "pesan":"Semoga selalu bahagia dan terus semangat ngejar impian!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Baik dan sopan, punya semangat tinggi dalam setiap hal.",
                "pesan":"Terus jaga semangat dan jangan lupa nikmatin prosesnya!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Ceria dan perhatian, bikin suasana kelompok jadi hangat.",
                "pesan":"Semoga sukses di setiap langkah dan terus jadi versi terbaikmu!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Lucu dan spontan, tapi juga rajin dan bisa diandalkan.",
                "pesan":"Semoga selalu bahagia dan terus menebar keceriaan!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1s1hc5uiJVCItzUlWAWwF5Rd_gbTNJt1f",
            "https://drive.google.com/uc?export=view&id=1-Mhule2rFbO4YB48Ca7o1iJ97BIJuUl7",
            "https://drive.google.com/uc?export=view&id=1QbXie8-egJRBCrq1Fpqh8Tl3flpcP3OP",
            "https://drive.google.com/uc?export=view&id=1arBatl8NjplCzIYFl9AgnYi7mBNqKjs9",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kobam, Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Bintang orangnya seru, gampang diajak ngobrol, dan vibe-nya positif banget.",  
                "pesan":"Semangat terus kuliahnya, Kak! Jangan lupa rehat biar ga stres."
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "Kak Nadya keliatan kalem tapi asik banget kalo udah ngobrol.",  
                "pesan":"Semoga makin lancar kuliahnya dan tetap ceria terus ya, Kak!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah orangnya ramah dan enak diajak kerja bareng, bikin suasana adem.",  
                "pesan":"Semangat terus kuliahnya, Kak! Semoga semua targetnya tercapai."
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Lia santai tapi tetap bisa diandalkan, suasananya selalu bikin nyaman.",  
                "pesan":"Tetap semangat ya, Kak! Jangan lupa istirahat di tengah kesibukan kuliah."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Xblod6qCC8s_jl1WfhJMlWo5bK1Ar9FS",
            "https://drive.google.com/uc?export=view&id=1xs6YAH2OoNAaGrldJp_d0GPFjQJDYf4e",
            "https://drive.google.com/uc?export=view&id=14-lZ2T23gIhwisDcnvOYdrP-MctpTP6Z",
            "https://drive.google.com/uc?export=view&id=1xSvQJL_jXL8F1zEaJUXMXIk0VGtLuuhc",
            "https://drive.google.com/uc?export=view&id=1LmT86Q4f8pMbqkZLOMEvRlb7hOoR1ipJ",
            "https://drive.google.com/uc?export=view&id=1y4aShCIhAPRWypO0q36oHrB1wVkQHyKL",
            "https://drive.google.com/uc?export=view&id=1Buk4rQaH4jMRlSHqVVVJRFay53YM5t1z",
            "https://drive.google.com/uc?export=view&id=1dxTO0-5r3ONjs2t-UxMIw7wtuGtCT5K6",
            "https://drive.google.com/uc?export=view&id=1k-SZZp4vtfo1C-NFrqsQNJRsLMKEzbH4",
            "https://drive.google.com/uc?export=view&id=1tcvJcQXr2BeUq-G9ruO3Sr4xlhYtvUnd",
            "https://drive.google.com/uc?export=view&id=1Azn4iaxFEC0JOWctJCe5xYFZWNJ-OVOp",
            "https://drive.google.com/uc?export=view&id=1yWEAanQlj-UvzGQ3NRBqgdbTy1oxD1kB",
            "https://drive.google.com/uc?export=view&id=1BKLNnLmKF14R2Fti6S2uNo6RNJ7IzUt1",
            "https://drive.google.com/uc?export=view&id=17xuee-zRX8cPDZ37dOcjheUt7Ze750qp",
            "https://drive.google.com/uc?export=view&id=1z1mLihos0X6VNkyqtdXM1tRt-vxzD22g",
            "https://drive.google.com/uc?export=view&id=1AzvSZnssu1m0BMVlJVNb6G8rIW1tYLQN",
            "https://drive.google.com/uc?export=view&id=1QHPNRBcZqAUqhNqqh5S_ldpQQp6kHenz",
            "https://drive.google.com/uc?export=view&id=17lJe7zBKhS55_J0fP-8UKU4IEMixB41_",
            "https://drive.google.com/uc?export=view&id=1xGknjd5PHA5bsSSjlUCEaEfJseDbSrEu",
            "https://drive.google.com/uc?export=view&id=1CAHvPvYJOD3KlXK5ZNdYpO0uqx5iLZw9",
            "https://drive.google.com/uc?export=view&id=1HGSodzZlSqysUOOgjRHFRRqEjvGS3a14",#6
            "https://drive.google.com/uc?export=view&id=13Sz-ASUxO0kCy0vbtntK2wiz56VawO3W",#5
            "https://drive.google.com/uc?export=view&id=11BEIS1aD4M4VW9OxzSgpa2jjlSX1GPz_",#4
            "https://drive.google.com/uc?export=view&id=1DzySBuYAEa9K4DktGofWzgw5kzAwYXEA",#3
            "https://drive.google.com/uc?export=view&id=1wikrts7GDQta6D_yPqxU3uLnAtpHY9Ds",#2
            "https://drive.google.com/uc?export=view&id=1KMll1wlwh-y6F-tk0VhjBIxrCgdYORZD",#1
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Orangnya tenang tapi tetap seru diajak ngobrol.",
                "pesan": "Semoga selalu diberi kesehatan dan makin sukses ke depannya!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri Sukarame",
                "hobbi": "Jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Nisrina lembut dan ramah banget, nyenengin tiap diajak kerja bareng.",
                "pesan": "Semangat terus ya kak, semoga semua yang dikerjain lancar!"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kak Rewina asik banget, vibes-nya tuh bikin suasana jadi hidup.",
                "pesan": "Semangat terus kuliahnya kak, jangan lupa istirahat juga!"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Bang Ihsan orangnya santai tapi tanggung jawab banget.",
                "pesan": "Semoga selalu semangat dan makin sukses, bang!"
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Bang Daffa lucu sih, tapi tetap profesional waktu kerja.",
                "pesan": "Jangan berubah ya bang, semoga makin sukses dan bahagia!"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Bang Benget asik banget, gampang diajak ngobrol.",
                "pesan": "Semoga karier dan kuliahnya lancar terus ya bang!"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Bang Ulliano unik banget orangnya, tapi keren sih idenya selalu out of the box.",
                "pesan": "Terus berkembang ya bang, semoga semua impiannya tercapai!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Bang Sahidin ramah dan gampang bantuin orang.",
                "pesan": "Makasih udah sering bantu, sukses terus bang!"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Bang Ali seru banget, suka bercanda tapi tetap bisa diajak serius.",
                "pesan": "Semoga selalu semangat dan makin berprestasi bang!"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kak Oca manis banget, enak diajak ngobrol dan positif vibes-nya.",
                "pesan": "Semangat terus kuliahnya kak, jaga kesehatan juga ya!"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma selalu ceria, bikin suasana kelompok jadi rame.",
                "pesan": "Tetap jadi diri sendiri ya kak, semangat terus!"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kak Ferazka kalem tapi lucu kalau udah kenal lama.",
                "pesan": "Jangan capek-capek ya kak, semoga semua urusannya lancar!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Bang Sahid orangnya santai tapi bisa diandalkan banget.",
                "pesan": "Terus semangat ya bang, semoga makin keren ke depannya!"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kak Allya tegas tapi tetap ramah, sosok yang bisa diteladani.",
                "pesan": "Semoga sehat selalu dan makin sukses kak!"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Abangnya asik banget, energinya selalu positif.",
                "pesan": "Semoga rezeki dan kuliahnya lancar terus ya bang!"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta lembut dan sabar banget, panutan sih.",
                "pesan": "Semoga makin sukses dan bahagia ya kak!"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abangnya tegas banget.",
                "pesan": "Terus jadi pribadi yang positif ya bang!"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, baca, badminton, gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Kak Ginda pintar dan tenang banget, suka ngasih insight bagus.",
                "pesan": "Semoga sukses selalu dan tetap rendah hati kak!"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Kak Natasya elegan dan sopan banget, enak diajak ngobrol.",
                "pesan": "Semoga terus sukses dan makin bahagia ya kak!"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Kak Nobel keren banget, kalem tapi berwibawa.",
                "pesan": "Semoga terus jadi inspirasi buat yang lain ya kak!"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Bang Fajar suka bercanda tapi perhatian juga, asik banget.",
                "pesan": "Semoga sukses terus bang, dan jangan lupa istirahat!"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany ceria banget dan gampang bikin suasana jadi rame.",
                "pesan": "Tetap semangat dan terus sebarkan energi positif ya kak!"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kak Daniar enerjik banget, seru kalau lagi bareng-bareng.",
                "pesan": "Semoga terus semangat ngejar mimpi, Kak!"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Bang Kevin lucu sih, tapi juga tanggung jawab banget.",
                "pesan": "Semangat terus ya bang, sukses buat semuanya!"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kak Lidia manis banget dan selalu nyenengin kalau ngobrol.",
                "pesan": "Semoga makin berprestasi dan bahagia selalu ya kak!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Bang Ridwan asik banget.",
                "pesan": "Terus semangat ya bang, semoga semua targetnya tercapai!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hp7W6P-mhRCyPjf_4PP-a8YVewi7Pw0p", #1
            "https://drive.google.com/uc?export=view&id=1PCAS6ZC2erjro7D5FI9uHQRi3alkfjsn", #2
            "https://drive.google.com/uc?export=view&id=1SpaVzyYrswVVoqwn396qK6QuxY8jROUj", #3
            "https://drive.google.com/uc?export=view&id=1Kmo2USU_JM7B5vRVuvy5OOgaqhYNCc6m", #4
            "https://drive.google.com/uc?export=view&id=1wkzty2WrBD5rsbRryNX1-yTS3qLSh6Hv", #5
            "https://drive.google.com/uc?export=view&id=1gSgBy5H5wojgCvVGeEe6cYT1exjKTZom", #6
            "https://drive.google.com/uc?export=view&id=11jEmTRXgGVXOg8GFwZEMxuN5uTk3djKy", #7
            "https://drive.google.com/uc?export=view&id=1JnNlcXYulcTYSf9FtqLENOVJeui-XSXf", #8
            "https://drive.google.com/uc?export=view&id=1Gv9FnlASAS8fWhEcLpYBrrhKWt_Akc2D", #9
            "https://drive.google.com/uc?export=view&id=1hAeHzWn5sWXAcOneDYL7l1W7aux1thAx", #10
            "https://drive.google.com/uc?export=view&id=1_3BlcxzogtAyb2C2fZGPrU6Vm6omOcbK", #11
            "https://drive.google.com/uc?export=view&id=1bQ0YZvoslBD5PsX_pN6sWsJVjCZWeQai", #12
            "https://drive.google.com/uc?export=view&id=1VO0S1F8xB-SoMrpSzKB8jkB5bntQtOgx", #13
            "https://drive.google.com/uc?export=view&id=1eZrWc2Ah3KW4Kk0ngAFJHIA1-Y2tEXgI", #14
            "https://drive.google.com/uc?export=view&id=1ZheELsGEtdsaM1vVAzTwQTB35byhWVlP", #15
            "https://drive.google.com/uc?export=view&id=1SuqHiZYUpGO9O3CuYihmISiHBzZA2IGd", #16
            "https://drive.google.com/uc?export=view&id=1NTrzD-uaueJ-6asMfwBkud3--YFHWqB8", #17
            "https://drive.google.com/uc?export=view&id=18gHS-lz5fE3iS8p89PEbQZrDW8tpiEXi", #18
            "https://drive.google.com/uc?export=view&id=1J4GiwejcAkuLPu-xfMPGqyUTYmhYGzch", #19
            "https://drive.google.com/uc?export=view&id=1uz8jaOxO58OWEl0XCqlPxx_QFVbj8jfY", #20
            "https://drive.google.com/uc?export=view&id=1ITuryLATXhA4Qp9-lWC_Fgam84in4LWZ", #21
            "https://drive.google.com/uc?export=view&id=1AJgbe47SayUbuU7g-AIvDp6IAtCcYiz7", #22
        ]
        data_list = [
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Ngobrolnya asik banget, banyak insight!",
                "pesan": "Tetap semangat kuliahnya, bang!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca jurnal, gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Ramah dan easy going, seru diajak ngobrol.",
                "pesan": "Semoga sukses selalu, Kak!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semuanya",
                "sosmed": "@marletacornelia",
                "kesan": "Sabar banget dan selalu siap bantu.",
                "pesan": "Jaga kesehatan ya, Kak!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Menyenangkan, gampang akrab.",
                "pesan": "Semoga semua cita-cita tercapai!"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin musik, dance, drakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Pembawaannya positif, berkesan.",
                "pesan": "Terima kasih atas semua ilmunya!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@adiaafrj",
                "kesan": "Asik banget ngobrol sama Kakak.",
                "pesan": "Tetap semangat belajar!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Orangnya ramah, seru diajak ngobrol.",
                "pesan": "Semoga sukses selalu!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Sangat sabar dan membantu.",
                "pesan": "Jaga kesehatan di tengah kesibukan!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala hal",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Mudah bergaul, enak diajak ngobrol.",
                "pesan": "Semoga semua tercapai!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Sangat positif, meninggalkan kesan baik.",
                "pesan": "Terima kasih atas semua ilmunya!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Ngobrolnya seru banget.",
                "pesan": "Semangat terus, bang!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Ramah, mudah akrab.",
                "pesan": "Semoga sukses selalu!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Sabar dan baik hati.",
                "pesan": "Tetap jaga kesehatan!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Mudah diajak ngobrol, menyenangkan.",
                "pesan": "Semoga semua tercapai!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Pembawaannya positif dan berkesan.",
                "pesan": "Terima kasih banyak!"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Seru banget diajak ngobrol.",
                "pesan": "Tetap semangat!"
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Ramah, gampang akrab.",
                "pesan": "Sukses terus, Kak!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, random chat GPT",
                "sosmed": "@fifah.zy",
                "kesan": "Asik diajak belajar bareng.",
                "pesan": "Semangat terus, bang!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "Santai tapi tetap fokus belajar.",
                "pesan": "Tetap semangat, bang!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main piano, nyanyi, ngehalu",
                "sosmed": "@bee_0115",
                "kesan": "Seru diajak belajar bareng.",
                "pesan": "Semangat terus, Kak!"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Menyenangkan dan asik diajak ngobrol.",
                "pesan": "Tetap semangat, Kak!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Asik banget ngobrol sama abang.",
                "pesan": "Semangat terus!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tLUfJC5not1Lq_rXLwiYxDk6hrPk9K-P", #1
            "https://drive.google.com/uc?export=view&id=1BpIJBjtOFA-dj919-T6opes1PcRnm2nO", #2
            "https://drive.google.com/uc?export=view&id=1Wk384VWVSjbl1y9ZRQQpEzZzg7wCFgK4", #3
            "https://drive.google.com/uc?export=view&id=1oI8w2LC1h6gqeUObj0pUOw2yNuriME2M", #4
            "https://drive.google.com/uc?export=view&id=1azIeOkmIOVZA-gXQoBUVsJlNXExS_xO4", #5
            "https://drive.google.com/uc?export=view&id=1GSvQGB5nfeXGY-EyYCVHVQo9HppcQMZQ", #6
            "https://drive.google.com/uc?export=view&id=1KTdeuBuEBfMeO0zcrq0awqyDhYVE1Q6p", #7
            "https://drive.google.com/uc?export=view&id=1vYKm3O-69-VVpTxCEAOM0gxRccBe1cxC", #8
            "https://drive.google.com/uc?export=view&id=1gOQ_PGfeZpTj1NGr_q0S6Fr8iUEb_kF0", #9
            "https://drive.google.com/uc?export=view&id=14zjjW3v5_k7P-yTdyBZ6DwRKwx6rMk52", #10
            "https://drive.google.com/uc?export=view&id=1OtznlTyY6BA4GdqvQbFCTqHm75SMIhWs", #11
            "https://drive.google.com/uc?export=view&id=1Uof_PVgecn94J4TJPVzB4TVRwIVLEO0f", #12
            "https://drive.google.com/uc?export=view&id=1e669JZ4QiN-EGV9XS-JIcxJMzdEtNFJR", #13
            "https://drive.google.com/uc?export=view&id=17P6u6DQ6qoXqce2a6nM-IZ8tFV1umi8E", #15
            "https://drive.google.com/uc?export=view&id=1eK-n-YOJvJJGQ4lRt_ouenocZdhMtxpj", #10
            "https://drive.google.com/uc?export=view&id=1dhtrzGAGsYgRcv2Vhj2hvbkmrHFEpDof", #9
            "https://drive.google.com/uc?export=view&id=1Lr0w7Mmb1ej26XGkaVkA6MwQc23h62Wh", #8
            "https://drive.google.com/uc?export=view&id=1-h52PplfbF8TVCV0U-EOo8m8pgrFU4gY", #7
            "https://drive.google.com/uc?export=view&id=1iEuOJ-XT3jnY18yxyeipiysV0wVpxSmN", #6
            "https://drive.google.com/uc?export=view&id=1Y9eYt2uorSWXy8hVZgarc7gR8l_bVXuW", #5
            "https://drive.google.com/uc?export=view&id=1abTLWIK_53My-gilDG8uK_pwtUaaZf2N", #4
            "https://drive.google.com/uc?export=view&id=10BN5R1cDp1wAostGvifezwZkpqJuCl4B", #3
            "https://drive.google.com/uc?export=view&id=1fn7tvrwqQufFHb3IG-X_u1reAbiglyhZ", #2
            "https://drive.google.com/uc?export=view&id=1iqqUL6wB5z1eRXbHujsCppG5wfGGmHNp", #1
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
                "kesan": "Ngobrolnya seru, banyak insight baru.",
                "pesan":"Tetap semangat kuliahnya, bang!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Ramah dan gampang akrab, asik diajak ngobrol.",
                "pesan":"Sukses selalu untuk Kakak!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Sabar banget, selalu siap bantu.",
                "pesan":"Jaga kesehatan di tengah kesibukan, Kak!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Menyenangkan, gampang akrab.",
                "pesan":"Semoga semua cita-cita tercapai, Kak!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Pembawaannya positif dan berkesan.",
                "pesan":"Terima kasih atas semua ilmunya!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam Naya",
                "sosmed": "@cindylauura",
                "kesan": "Ngobrolnya asik dan menyenangkan.",
                "pesan":"Tetap semangat kuliahnya, Kak!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badminton, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Ramah dan gampang diajak ngobrol.",
                "pesan":"Sukses selalu, bang!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Sangat sabar dan membantu.",
                "pesan":"Jaga kesehatan, bang!"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Menyenangkan dan asik diajak ngobrol.",
                "pesan":"Semoga semua tercapai!"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Pembawaannya positif dan berkesan.",
                "pesan":"Terima kasih atas semua ilmunya!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Seru banget diajak ngobrol.",
                "pesan":"Tetap semangat kuliahnya, Kak!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg. Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Ramah, gampang akrab.",
                "pesan":"Sukses selalu, bang!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Sabar dan selalu siap bantu.",
                "pesan":"Jaga kesehatan, Kak!"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton reels AGZ",
                "sosmed": "@deaamnd3_",
                "kesan": "Menyenangkan dan asik diajak ngobrol.",
                "pesan":"Semoga semua tercapai!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main-main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Pembawaannya positif dan berkesan.",
                "pesan":"Terima kasih atas semua ilmunya!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Ngobrolnya asik banget.",
                "pesan":"Semangat terus, Kak!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Ramah, gampang akrab.",
                "pesan":"Sukses selalu, bang!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Sabar dan siap bantu.",
                "pesan":"Jaga kesehatan, bang!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajahi desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Menyenangkan dan asik diajak ngobrol.",
                "pesan":"Semoga semua tercapai!"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan keliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Pembawaannya positif dan berkesan.",
                "pesan":"Terima kasih atas semua ilmunya!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Ngobrolnya seru, banyak insight baru.",
                "pesan":"Tetap semangat kuliahnya, Kak!"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Ramah dan gampang akrab.",
                "pesan":"Sukses selalu, Kak!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Sabar dan siap bantu.",
                "pesan":"Jaga kesehatan, Kak!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Menyenangkan dan asik diajak ngobrol.",
                "pesan":"Semoga semua tercapai!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11FwpvaYmAzGIZUGnggo4JeLBGuw3NLRb", #1
            "https://drive.google.com/uc?export=view&id=1rACy0K_pxqwHtrB1LajNbLrrGdCpjX3U", #2
            "https://drive.google.com/uc?export=view&id=1A8k5wY5vnqfnw_XZ8hwNOti69XxVeYdL", #3
            "https://drive.google.com/uc?export=view&id=1-5MjCEG-seU7rjla4u4k6UMNrIe23Edo", #4
            "https://drive.google.com/uc?export=view&id=1ALBpMvDaw1cnpMU8EYDGZ7eVKAlWX6Qb", #5
            "https://drive.google.com/uc?export=view&id=18-pfJeimh1FRUWYp1uRPQnqLUTSMXiIi", #6
            "https://drive.google.com/uc?export=view&id=1Y98_YXf4gCOOMYQgbJB2HC0y-xXneJ1E", #7
            "https://drive.google.com/uc?export=view&id=1bC10QlBCHkHY9bdt1lzCiT5s9G2Iy9bS", #8
            "https://drive.google.com/uc?export=view&id=1fomx8hxylTqMYoWlWoFivKJ0SPOPBjXT", #9
            "https://drive.google.com/uc?export=view&id=1x92vwV_tfLdL58n2CMHyBdja4vMxcB7-", #10
            "https://drive.google.com/uc?export=view&id=1p3J9Br0pivqJfgUKeA8TxXLhWAKOCH-J", #11
            "https://drive.google.com/uc?export=view&id=1UXmIqpsSkmFHdWW7YQFdhLlX0MnwSFLi", #12
            "https://drive.google.com/uc?export=view&id=1SvG1SRSvSu8VqL5ndBoGYhYvUoZl9yXU", #13
            "https://drive.google.com/uc?export=view&id=1iV-Ues0vaiMQEMeEHQhu5pVLmdg10nUA", #14
            "https://drive.google.com/uc?export=view&id=1JHiWRcvya_NHebDckxE5Uf9KVSwYVu6H", #15
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya selalu ramah dan bikin suasana internal lebih hangat.",
                "pesan":"Terus semangat memimpin tim internal, Kak! Kami dukung selalu."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Orangnya asik dan selalu bisa diajak diskusi santai.",
                "pesan":"Semoga selalu kreatif dan sukses dengan setiap kegiatan internal, Kak!"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya sabar dan selalu memotivasi kami untuk semangat.",
                "pesan":"Jaga semangat positifnya selalu ya, Kak! Kami ikut bangga."
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Selalu jadi sosok penyemangat dan bikin nyaman semua anggota.",
                "pesan":"Semoga terus jadi inspirasi bagi internal. Keep shining, bang!"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya sabar dan bikin kita merasa dihargai.",
                "pesan":"Semoga selalu semangat menjaga kebersamaan di internal, Kak!"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asik dan selalu bikin anggota nyaman.",
                "pesan":"Terus semangat dan kreatif dengan ide-ide baru, Kak!"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakaknya lucu tapi juga tegas, bikin semuanya teratur.",
                "pesan":"Semoga selalu bisa memimpin tim dengan baik, bang!"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kakaknya selalu memberi support dan bikin semangat.",
                "pesan":"Terus jadi penguat internal ya, bang! Semangat terus!"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakaknya ramah dan selalu bikin suasana ceria.",
                "pesan":"Semoga selalu menyenangkan dan sukses dalam tiap kegiatan internal, Kak!"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya perhatian dan bikin nyaman semua anggota.",
                "pesan":"Semoga selalu menjadi sosok panutan di internal, Kak!"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya asik dan selalu bikin semua anggota enjoy.",
                "pesan":"Semoga selalu sukses memimpin internal, Kak!"
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya sabar dan selalu memberi motivasi.",
                "pesan":"Terus menjadi inspirasi bagi anggota internal, Kak!"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya ramah.",
                "pesan":"Semoga semangatnya menular ke semua anggota, bang!"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalghani73",
                "kesan": "Abangnya ramah dan selalu perhatian.",
                "pesan":"Semoga terus jadi panutan internal, bang!"
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450026",
                "umur": "22",
                "asal":"Natar",
                "alamat": "Jl Durian 19",
                "hobbi": "Mengetik",
                "sosmed": "@zhresti",
                "kesan": "Kakaknya gemess banget deh.",
                "pesan":"Terus semangat menghidupkan internal, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1l1drcpqP85E7iBDheav4q_vpB3TGPPOk", #1
            "https://drive.google.com/uc?export=view&id=1ACQ56bltGZdKGTPUAOuUhYwZamqXSZFM", #2
            "https://drive.google.com/uc?export=view&id=1jr_BFemtvVdValeR0drt_CZ3hgwpUlq8", #3
            "https://drive.google.com/uc?export=view&id=1a23PXdX_hS32B0ZhLCxkgklH19U_6Blu", #4
            "https://drive.google.com/uc?export=view&id=15GPkzpGKGq_b0-meNOMYmEhXGCOikpwH", #5
            "https://drive.google.com/uc?export=view&id=16BrMZk-_epJ4QOc0RIuURhNcka0yarCE", #6
            "https://drive.google.com/uc?export=view&id=1sV3f-dCVTTvza655axK2REgRxZZY227D", #7
            "https://drive.google.com/uc?export=view&id=1-wP9BqPS5Wyp_F-TDvIiYcSnQubIvns6", #8
            "https://drive.google.com/uc?export=view&id=14sHT1QziX-RwE5A3mJuBwb-3EyA7K5FW", #3
            "https://drive.google.com/uc?export=view&id=11m05IKpliF_ron4HKGe7JFmt0bfmQrTr", #2
            "https://drive.google.com/uc?export=view&id=1b_HOodZ5sPgyTXRMCq34ZS6Vl3mu-393", #1
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
                "kesan": "Abangnya asik dan seru, bikin suasana lebih hangat.",
                "pesan": "Semangat terus, bang! Tetap jadi inspirasi."
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Senang bisa kenal kakak, orangnya ramah dan sabar.",
                "pesan": "Semoga sukses selalu dalam kuliah dan kegiatan, Kak!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya ramah, mudah diajak ngobrol.",
                "pesan": "Jaga kesehatan selalu, bang!"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya keren dan penuh motivasi.",
                "pesan": "Semangat terus, Kak! Tetap jadi panutan."
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Senang bisa bertemu kakak, orangnya hangat.",
                "pesan": "Semoga semua urusannya dilancarkan, Kak!"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya sangat membantu dan peduli.",
                "pesan": "Sukses selalu untuk Kakak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya asik diajak diskusi dan ramah.",
                "pesan": "Terima kasih atas bimbingannya, bang!"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya baik hati dan murah senyum.",
                "pesan": "Semangat terus ya, Kak!"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Senang bisa kenal dengan kakak, asik banget.",
                "pesan": "Semoga sukses selalu, Kak!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya ramah dan selalu mendukung.",
                "pesan": "Jaga kesehatan selalu, Kak!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Terima kasih Kakak atas bantuannya, hangat banget.",
                "pesan": "Semangat dan sukses selalu!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-Jf1auq6IxrE6gNQe-YC-yhrNKG2R21z", #1
            "https://drive.google.com/uc?export=view&id=1LWMI6xBnlhfPSgccf8XeINL7NJmn0w_-", #2
            "https://drive.google.com/uc?export=view&id=14bEm4VL6jW1W-Q2y2gm85UjDxfi_imcF", #3
            "https://drive.google.com/uc?export=view&id=1e2F8rPOOW7yqv9WdyddpWpqdLmO6cAH1", #4
            "https://drive.google.com/uc?export=view&id=1d8ZR854XGrfrlOu5kQLRCl3fyxAlV4Ug", #5
            "https://drive.google.com/uc?export=view&id=1b7o9Mc5v3ArYaZa-EtxyxQYxy5lwbbPR", #6
            "https://drive.google.com/uc?export=view&id=16KNakhBw6qMThV-Orlp14c38MRG54ssI", #7
            "https://drive.google.com/uc?export=view&id=1oR1rtrNmZIBPa10t61DXO5HBemiFJoiA", #8
            "https://drive.google.com/uc?export=view&id=1B7NpGf7XdaODEwaLsfoDIOafTBotekOK", #9
            "https://drive.google.com/uc?export=view&id=1_jhvpGn7UwCWwJ34ZEj3VThdB8s74QVW", #10
            "https://drive.google.com/uc?export=view&id=1tvSLn9MCfoGjbD3rtZA7--ZcCfw2aUWA", #11
            "https://drive.google.com/uc?export=view&id=1DwT5vdcwT79bozSB4mbAHR6ooQEq-0wp", #12
            "https://drive.google.com/uc?export=view&id=18rZXNtKSB6xXJOKPg2paQutDtkrhlhAD", #13
            "https://drive.google.com/uc?export=view&id=1ZgEVebGTJbyxReUz93Bk5mKWvJOLUwaD", #14
            "https://drive.google.com/uc?export=view&id=1jqNJXijUiVHNe6YrdwjUMXpW2iWCCHXL", #15
            "https://drive.google.com/uc?export=view&id=18wQs_uGxwvCPdM7HwBeXeCZB8Mg5sdeN", #16
            "https://drive.google.com/uc?export=view&id=1WbKHzRwdofQVxo8FC5PJRelvjVyFN3eD", #17
            "https://drive.google.com/uc?export=view&id=1LNhnDr10tIliQTFiB5CjqYjhmwc82UnU", #18
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya keren.",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abang ini asik.",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Kakak ini humble banget.",  
                "pesan":"semangat terus kuliahnya bang !!!"
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

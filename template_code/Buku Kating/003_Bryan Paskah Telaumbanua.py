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
            "https://drive.google.com/uc?export=view&id=1-Nq4vvI9SogktwerPY1YpA6HYkCKBAK3",
            "https://drive.google.com/uc?export=view&id=1txGHzEDyBL7IP4fQB0Gzluj_Iw3S8oj9",
            "https://drive.google.com/uc?export=view&id=1S0FIiBHN2ViIBabBdrrLYeL3n9PkW-ge",
            "https://drive.google.com/uc?export=view&id=1XEREhSjIYto0TDEVhEn0UN1W-o7bdYFD",
            "https://drive.google.com/uc?export=view&id=1Fl-s1Z6cSpwkjlnlrZLWUfHPriCfYape",
            "https://drive.google.com/uc?export=view&id=15Vj85pU7cIu-oMQ7g9cS9c0y6i5Q4jxy",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Pemimpin (Kahim) yang ramah namun berwibawa",  
                "pesan":"Tetap semangat bang, semoga menjadi pemimpin lagi kedepannya"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Pemimpin (Sekjen) yang kece, santai namun jiwa kepemimpinannya dapat",  
                "pesan":"Terus maju bang jangan kendor, sampai kelulusan"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya baik, ramah dan menyenangkan",  
                "pesan":"Dilancarkan kuliahnya kak, tetap semangat."# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya kalem namun ramah.",  
                "pesan":"Semangat kak. Semoga yang direncanakan kedepannya tercapai "# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Baik, lucu dan ramah kakaknya.",  
                "pesan":"Tetap maenjadi pribadi yang menyenangkan kak."# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Baik dan ramah kakaknya.",  
                "pesan": "Semangat kak. Semoga tetap berhasil kedepannya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TKB_j0aEEspHQjPtcnTXDyMsWds19lLT",
            "https://drive.google.com/uc?export=view&id=1q7RuUNdbZaO51CdFcWMGDhS2QsO3aKlt",
            "https://drive.google.com/uc?export=view&id=11OzUBMm8aeKCCvfuXhh-HjpoivUqWzDW",
            "https://drive.google.com/uc?export=view&id=1_b7JqFkqAyXLA3pi71Se0dyfrbxVOx-R",
            "https://drive.google.com/uc?export=view&id=1LWzMq6ahKBbGbAYpqcNSVzooBuylDW7S",
            "https://drive.google.com/uc?export=view&id=1l9LSyiKYUuiTrYb-QPMZO6gQsV7fVDg1",
            "https://drive.google.com/uc?export=view&id=1z2xPf8Ym4drImfoCq7kKwmnl4cNHJwHE",
            "https://drive.google.com/uc?export=view&id=1YF4AO30-UbMszOo_td1Fe6FkTyo8lue2",
            "https://drive.google.com/uc?export=view&id=1IFJ7fGL0T1j27083AU5K16HzpHwjecOa",
            "https://drive.google.com/uc?export=view&id=1zEvuOR1O0P2c2HTQq1GJ-AYWj822hC62",
            "https://drive.google.com/uc?export=view&id=1Z1ObS9dnknJ9mqJjTENrZ3wOUNBLmlS6",
            "https://drive.google.com/uc?export=view&id=1Y2Wkz6yxUqvAALEUyfI8OdJAvvFBJF4R",
            "https://drive.google.com/uc?export=view&id=1-I-KyAbyFwkIDYMdr_TR8Eb1gP0LK3jh",
            "https://drive.google.com/uc?export=view&id=11Uv5iAam5chTegEm7koEWCa7Np3FoCFd",
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
                "kesan": "Memiliki pembawaan yang kuat.",
                "pesan":"Sukses selalu bang. Masih ada capaian lain kedepannya"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya asik kadang tegas juga.",
                "pesan":"Semangat terus kak. Tetap maju."
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Tegas, asik dan ramah kakaknya.",
                "pesan":"Tetap menjadi pribadi yang menyenangkan kak."
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Baik kakaknya dan murah senyum.",
                "pesan":"Semoga dilancarkan perkuliahan dan segala impiannya."
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Asik, pintar, dan memiliki ide-ide menarik.",
                "pesan":"Terus melangkah maju bang. Dan tetap berbagi ilmu dan pengalaman yang baik."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Baik, ramah dan bisa tegas juga.",
                "pesan":"Semangat terus kak. Jaga kesehatan dan perkuliahannya."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Baik, ramah dan santai aja abangnya.",
                "pesan":"Tetap jaga kesan yang baik tersebut bang. Semangat terus!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Kalem, baik dan penuh perhitungan.",
                "pesan":"Tetap semangat bang. Semoga yang direncanakan kedepannya berhasil"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Ramah dan baik kakaknya.",
                "pesan":"Tetap selalu baik dimanapun kak. Semangat!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya asik, ramah dan perhatian.",
                "pesan":"Semoga sukses terus kak, dimanapun"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Memiliki jiwa kepemimpinan dan orientasi yang baik.",
                "pesan":"Semangat bang, kelak dapat menjadi pemimpin yang baik."
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya, santai, baik dan mau berbagi pengalaman.",
                "pesan":"Tetap menjadi pribadi yang mau berbagi pengalaman inspiratif."
            },           
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Baik dan ramah kakaknya",
                "pesan":"Semangat dan maju terus kak."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya baik dan suka berbagi cerita.",
                "pesan":"Semoga dilancarkan perkuliahan dan urusannya kak."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12k3wKN6-yOAr7Lvg2Rl-8jYnZPsXMfG1",
            "https://drive.google.com/uc?export=view&id=1JpBI62qUSaMQWige25G_5sd_NYOCAPGC",
            "https://drive.google.com/uc?export=view&id=1JMx4YGTneAz4x3dwyHdhqe9XaiAaD1pw",
            "https://drive.google.com/uc?export=view&id=1aimiJKqOKMGwPqKn1mfb7FhL357QklvE",
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
                "kesan": "Aktif dan semangat terus abangnya.",  
                "pesan":"Jangan lupa untuk berbagi ilmu dan pengalamannya ya bang."# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakaknya baik, dan ramah sekali.",  
                "pesan":"Tetap semangat perkuliahannya kak."# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Baik dan menginspiratif sekali.",  
                "pesan":"Semoga sukses rencananya kak, yang impikan berhasil."# 1
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Baik dan pintar kakaknya.",  
                "pesan":"Tetap menjadi pribadi yang baik dan menyenangkan ya kak."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sj0JkIeSj33viTNHAgPckUFI28KA6qH_",
            "https://drive.google.com/uc?export=view&id=17TaqtFgBpJN1LA8ZTVOENpHkpFRGACKR",
            "https://drive.google.com/uc?export=view&id=15RJTs30htrWSblmLWCLBBtWAJDknz8OD",
            "https://drive.google.com/uc?export=view&id=1mEFQyAC5mApFwt2LZ610FnNTWf7sipzJ",
            "https://drive.google.com/uc?export=view&id=1G9rhR3Er7mhwpPcmy2IhAj7sCls9R8VY",
            "https://drive.google.com/uc?export=view&id=179P-cm37Kb06ovYTcOJagbItzugD4iFG",
            "https://drive.google.com/uc?export=view&id=1ERuROJWX0LhhnmIxtWHKgp2zNP1H7wUL",
            "https://drive.google.com/uc?export=view&id=16u29uxcHRmM96oPeJI0NdMxQRhv9Fupy",
            "https://drive.google.com/uc?export=view&id=1uGw-D-NMTfDNX5Ft_r77wffsgRgNA6aW",
            "https://drive.google.com/uc?export=view&id=1KjCzlFbQLthlrkRWVMGpV9rKZVgRRb30",
            "https://drive.google.com/uc?export=view&id=1NJJfW_15TmU7lu5iaPG6zS2Wu67rWOOC",
            "https://drive.google.com/uc?export=view&id=1VNSS8oXGv7oMJOrfXOkVbGESn3Lim4Dd",
            "https://drive.google.com/uc?export=view&id=1jwnNRJpkwLOr8r3WmvOevcA3Euzsvmuu",
            "https://drive.google.com/uc?export=view&id=1dcoO9iwm8Clr0RC4DEtT-EiBAhqn07RI",
            "https://drive.google.com/uc?export=view&id=1nkqihLPmtr-f8Nn19SvhUO6gNTAv-Gp0",
            "https://drive.google.com/uc?export=view&id=1Kpn2WnXYuSeed3pPFxvAY71j0qKTSw02",
            "https://drive.google.com/uc?export=view&id=1YuCMjuEF-ThbAG3Zaci9etmAIMzC64ag",
            "https://drive.google.com/uc?export=view&id=1uwggxzxKgrokuxy4K5aV-VudD87mrjFv",
            "https://drive.google.com/uc?export=view&id=1YyZUOhNdWkSAy09dhSXz3zNG_gwL1QsK",
            "https://drive.google.com/uc?export=view&id=1WCpmorm2n6j2viqvStaSRsPi5eIW0-bf",
            "https://drive.google.com/uc?export=view&id=1VXXgDyTbR1Eu2lMeNZ-H1B5DSw_f2pVq",
            "https://drive.google.com/uc?export=view&id=1JOKz3NZ0B2M0YnMWZoHKsmZBik4R7GOX",
            "https://drive.google.com/uc?export=view&id=1DxfL2aKGjfRY4jYb0Lmrh0OZezpge6bP",
            "https://drive.google.com/uc?export=view&id=13pBb8H0A3cL9kIww-muGW_d2nZwEHTYw",
            "https://drive.google.com/uc?export=view&id=1tCSk_zDQZKQwTL7xa3FcT7lqjj8M_K0G",
            "https://drive.google.com/uc?export=view&id=1BANFdJLicJ-cjQT7yClVjtmeLJO0WL3m",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Tanjung senang",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Mempunyai pembawaan dan pendirian yang kuat.",
                "pesan": "Tetap diberi kelancaran perkuliahan abangnya dan sukses selalu."
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya asik dan menyenangkan.",
                "pesan": "Diberi kemudahan perkuliahan dan cita-citanya kak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Memiliki pendirian yang kuat namun tetap ada baiknya.",
                "pesan": "Semangat terus kakak, banyak ilmu yang saya dapatkan dari kakak. Terimakasih."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Jiwa kepemimpinan yang kuat, baik dan menginspirasi.",
                "pesan": "Semoga yang direncanakan berhasil, menjadi pemimpin yang baik."
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Baik, asik walaupun kadang dapat menjadi serius.",
                "pesan": "Semangat terus ya kak, dilancarkan kuliahnya."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Dibalik kesan dan penampilannya, banyak baiknya juga.",
                "pesan": "Tetap semangat dan terimakasih ilmunya selama ini."
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Baik, asik dan serius abangnya",
                "pesan": "Diberi kelancaran perkuliahannya bang."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Baik, ramah dan perhatian meskipun dapat menjadi serius juga.",
                "pesan": "Sukses selalu kak, akademik dan non akademiknya"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Tegas namun memiliki ilmu dan pengalaman yang baik abangnya",
                "pesan": "Terimaksih atas ilmu nya bang, semoga sukses dan berhasil yang dicita-citakan."
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Serius dan tegas namun memiliki kebaikan hati dan perhatian.",
                "pesan": "Sangat menginspiratif sekali abang, sukses dan semangat terus bang"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Baik, perhatian dan juga tegas.",
                "pesan": "Semangat terus kak, diberi kelancaran perkuliahannya."
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Abangnya santai namun memiliki ide dan inovasi.",
                "pesan": "Semangat terus bang. Jangan sampai kendor semangatnya."
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Baik, ramah dan pintar abangnya",
                "pesan": "Diberikan kelancaran perkuliahan dan urusannya."
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Baik, ramah dan perhatian.",
                "pesan": "Lancar terus kuliahnya kak. Tetap semangat."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semoga diberi kelancaran kuliahnya kak. Semangat terus."
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Baik dan ramah kakaknya",
                "pesan": "Tetap semangat kak, diberi kelancaran kuliahnya."
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Baik dan meninspirasi abangnya.",
                "pesan": "Terimakasih ilmunya bang, semoga sukses selalu."
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Tenang, santai namun visioner abangnya.",
                "pesan": "Jangan sampai kendor semangatnya bang, sukses selalu."
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya baik dan ramah sekali.",
                "pesan": "Semoga dimudahkan urusan dan perkuliahannya kak."
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Pintar, tenang namun menginspirasi.",
                "pesan": "Terimakasih atas ilmunya bang. Sukses selalu."
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Tenang dan penuh perhitungan.",
                "pesan": "Semangat terus bang, maju dan sukses selalu."
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Baik dan ramah kakaknya.",
                "pesan": "Tetap semangat kak. Semoga dilancarkan kuliah dan urusannya."
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Baik, tenang dan pintar.",
                "pesan": "Sukses selalu bang dimanapun dan kapanpun."
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Baik dan ramah kakaknya.",
                "pesan": "Tetap semangat kak, jaga kesehatan dan perkuliahannya."
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Asik dan keren bang",
                "pesan": "Sudah pasti lancar kalau sama abang. Sukses selalu bang."
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Serius, baik dan berbakat.",
                "pesan": "Terimakasih ilmunya bang, perlu banyak belajar lagi dari abang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ejv8RLSLFuyI5D1SyZCxNlQyZ2rTEe5K",
            "https://drive.google.com/uc?export=view&id=1e4aoMI3CCQR0EOEAOlNVHazmm6vvYP3J",
            "https://drive.google.com/uc?export=view&id=16UCRS34Gp5QpGsqHtd_Kz-vG4SItM-vI",
            "https://drive.google.com/uc?export=view&id=1DMKzIEKwP-X4GsrZYrEu79xgojhAKb4D",
            "https://drive.google.com/uc?export=view&id=1QXJuK7QpZg8aHe9ckLUf8gHhGNeyeelm",
            "https://drive.google.com/uc?export=view&id=1Gt4Bg1T2YPCxv7W-P5W_c82lfDoYsnNx",
            "https://drive.google.com/uc?export=view&id=1pJ4NWcTAeFVt4U77fVKv7Ovtih3KKibY",
            "https://drive.google.com/uc?export=view&id=1wex0sWhrpTl-x8aGdQgY0bx3Ss27tZrr",
            "https://drive.google.com/uc?export=view&id=18lOFGTJvyyexRVKPG_2Y-3RSsLrpXSqi",
            "https://drive.google.com/uc?export=view&id=17vwXu0Yf7tYO9OPLD00AIh_2Ht3y5Sxc",
            "https://drive.google.com/uc?export=view&id=1cF8sQm0D0Y5p8qzMp2VfNllAssKVOEQC",
            "https://drive.google.com/uc?export=view&id=1j2b155qJ_ZryndnZrAX0W1Y9SDPPdyun",
            "https://drive.google.com/uc?export=view&id=17YBShslE7SNm6kXH8F9PhOaqvku7e-Xg",
            "https://drive.google.com/uc?export=view&id=1qemjzzjF5S0onX8MCtTeMqUlJSyAEDpm",
            "https://drive.google.com/uc?export=view&id=1n-gLyowhb5M_2tN0It2jEOHBUimaIlqb",
            "https://drive.google.com/uc?export=view&id=1lFQ4L9lqWkLDNp-3zvBI0zl2JGgdlSEs",
            "https://drive.google.com/uc?export=view&id=1s7zg5vf2eD7K6uVhXsAJYvzU_T6Ybj40",
            "https://drive.google.com/uc?export=view&id=1zlTTIRvSXerOk5b7h7mTluU7L7bRCBNQ",
            "https://drive.google.com/uc?export=view&id=18oceMT3dIqef7aWDB5ibH56CNcaXnKg2",
            "https://drive.google.com/uc?export=view&id=13l1MTpWDl7OLv3rPlbEZtRqTYrgM0kt8",
            "https://drive.google.com/uc?export=view&id=1_Kb_gbm-reXRmZs0R5FeiGmhgVScn5TB",
            "https://drive.google.com/uc?export=view&id=1WV1Yy5h59R_B388vAT6S1KG7lau6B_Y-",
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
                "kesan": "Abangnya baik, ramah dan memiliki pandangan maju.",
                "pesan":"Tetap semangat bang. Ditunggu gebrakan baru dari MIKFES nya."
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Baik dan ramah sekali kakaknya.",
                "pesan":"Tetap semangat kak. Semoga dilancarkan kuliah dan urusannya."
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Baik, pintar dan ramah.",
                "pesan":"Terimakasih ilmunya bang. Semoga sukses selalu."
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya asik dan baik sekali.",
                "pesan":"Terimakasih ilmunya kak. Diberi kemudahan perkuliahannya."
            },  
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Aktif, inspiratif, humoris, baik dan memiliki pandangan maju.",
                "pesan":"Semangat bang, ditunggu program/kegiatan menarik selanjutnya."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Baik, ramah dan memiliki inisiatif yang tinggi.",
                "pesan":"Semangat terus bang, jangan sampai kendor"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Tenang, baik dan pintar",  
                "pesan":"Semoga diberi kelancaran kuliah dan urusan nya bang."# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya baik, ramah dan suka membantu .",
                "pesan":"Sukses selalu kak, tetap menjadi pribadi yang baik selalu."
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya menyenangkan, baik dan murah senyum.",
                "pesan":"Semangat kak. Sukses selalu kuliah dan segala urusannya."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Baik, humoris dan pintar abangnya.",
                "pesan":"Semangat bang, ditunggu arahan dan bimbingannya selaku mentor kelompok dan departemen."
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Baik, lucu dan ramah kakaknya.",
                "pesan":"Tetap semangat kak, semoga diberi kelancaran kuliah dan urusan lainnya."
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Baik dan ramah sekali kakaknya.",
                "pesan":"Terimakasih kak atas ilmunya kak selama di departemen, sukses selalu buat kakak."
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "JL. Gajah Mada, Tanjungkarang",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Ramah, baik dan pintar juga kakaknya",  
                "pesan":"Terimakasih juga kak atas ilmunya baik di departemen maupun di lab."# 1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Baik dan ramah kakaknya.",  
                "pesan":"semangat terus kakak, sukses selalu."# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Asik, aktif dan pembawaannya positif.",
                "pesan":"Tetap semangat kak, terimakasih juga atas ilmunya."
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Pintar, kalem dan baik",  
                "pesan":"Di tutorkan ilmu dan pengalamannya bang, coding"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Baik, ramah dan pintar kakaknya.",  
                "pesan":"Semangat terus kak, semoga dilancarkan kuliah nya."# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Inspiratif, bersemangat dan mudah bergaul.",
                "pesan":"Maju terus bang. Ditunggu rencana kedepannya, pemimpin Sains Data"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Keren dan inspiratif sekali abangnya.",
                "pesan":"Sukses selalu bang, ditunggu project kerennya kedepan"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakaknya baik dan ramah.",
                "pesan":"Terimakasih ilmunya kak, sukses selalu buat kakak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya baik, pintar dan pembawaannya positif.",
                "pesan":"Semangat terus kak. Dijaga kesehatan dan perkuliahannya."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Tenang, baik dan mau membantu.",
                "pesan":"Tetap semangat bang, jangan sampai kendor!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GA8hCVY7SrwsLb_C0ZJ_8kLs6HxVWKrw",
            "https://drive.google.com/uc?export=view&id=1FsPxYsLL4bU10lCpF2Bb58_9w52146cf",
            "https://drive.google.com/uc?export=view&id=1q2iDriiid3uNht__qbKJzPp7-qiJpJ18",
            "https://drive.google.com/uc?export=view&id=1BccFrnByek4r1q9cumigrBXkeDRleKN0",
            "https://drive.google.com/uc?export=view&id=1hQezNyMQgMcxBQzqniRFaovT7jsACp3h",
            "https://drive.google.com/uc?export=view&id=1QFFp9XdA3gelhxpd6CqoqtfLml1Gc2M_",
            "https://drive.google.com/uc?export=view&id=1Xnn5OeCVDHCxo-c6ssG-WulvMQRrIYda",
            "https://drive.google.com/uc?export=view&id=1rfG4LiFVgkyhmK5FHXuQv54iaZCyanH0",
            "https://drive.google.com/uc?export=view&id=1o90DTjJSzrldtH5S_rQORf_c3zwuSfui",
            "https://drive.google.com/uc?export=view&id=19ouhOPgi7YLOtkSANVMq0ydoImRQf5HG",
            "https://drive.google.com/uc?export=view&id=1gypi3wyGOQwsa-CKAyBcvfC6PbVwjpt6",
            "https://drive.google.com/uc?export=view&id=15PBx-e7fxoA5GySrRKcHJDL8W5V8Q9Ce",
            "https://drive.google.com/uc?export=view&id=1YD7qOJSDVPZfZ7E5L_7OIHE_U9sVeh7z",
            "https://drive.google.com/uc?export=view&id=1Nk2pXbmvIie9jH_JwdF2QzFNuHWLPVq-",
            "https://drive.google.com/uc?export=view&id=1_uAyw79aoierRKgs4erch-oA-0iZEVPE",
            "https://drive.google.com/uc?export=view&id=1hP4xfGpmNWnG_sl6hlsIWCilV4zd_IdZ",
            "https://drive.google.com/uc?export=view&id=1We6arov90073OLsh6xp6IoMcugNJsYuJ",
            "https://drive.google.com/uc?export=view&id=1xCOopE5soeycpL56VhdsgVlJQboFNhk7",
            "https://drive.google.com/uc?export=view&id=1b9mkZx-ff-K6CvwsETDVwRhvPnqjHnF_",
            "https://drive.google.com/uc?export=view&id=1kITNlKG_AHxOWMrQ7mITPOAzWv8W3KDV",
            "https://drive.google.com/uc?export=view&id=17h-Yy8B-u9sw440JWkHDinvM4vRbm30M",
            "https://drive.google.com/uc?export=view&id=11tKpKj-GWoDjUF2jgO0J5Q2pll9m2y4t",
            "https://drive.google.com/uc?export=view&id=1yHukT6Qv2dZM61TfS1SHTaIC5vxUNwnd",
            "https://drive.google.com/uc?export=view&id=1L_Bc_iekISavgfqBxjQsMBulTGNozaQF",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abang keren dan pembawaannya positif",  
                "pesan":"Terus semangat dan sukses selalu bang, agar Sains Data dikenal diluar."# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya baik, ceria dan ramah.",  
                "pesan":"Semangat terus kak, dilancarakan kuliah dan urusan lainnya."# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Orangnya positif dan selalu senyum",  
                "pesan":"Sehat-sehat terus ya, Kak. Ditunggu kabar baiknya."# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya baik, tegas, juga asik.",  
                "pesan":"Terus menjadi pribadi yang menyenangkan bagi semua orang kak"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Pekerja keras dan sangat menginspirasi.",  
                "pesan":"Semoga dilancarkan perkuliahannya bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak sangat seru, baik dan ceria",  
                "pesan":"Tetap jadi pribadi yang selalu ceria dan membawa suasana positif dimanapun kak."# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Baik, ramah dan murah senyum kakaknya.",  
                "pesan":"Tetap semangat dan ceria selalu kak, kuliah dan urusannya dimudahkan."# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Baik sekali, pintar dan ramah kakaknya",  
                "pesan":"Sehat dan sukses selalu kak"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abangnya santai, namun inspiratif",  
                "pesan":"Tetap semangat bang, di departemen dan perkuliahan"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Baik dan ramah kakaknya",  
                "pesan":"Dilancarkan kuliahnya ya kak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Baik, ramah dan pembawaannya positif",  
                "pesan":"Jadi pribadi yang selalu menyenangkan dimanapun kakak berada."# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya ramah sekali",  
                "pesan":"Terus semangat ya kak kuliahnya, ditunggu kabar baiknya."# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Sangat berwibawa dan baik sekali abangnya",  
                "pesan":"Terimakasih atas ilmunya bang. Jangan keras keras sama junior mu ini bang."# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakaknya baik, ramah dan pintar",  
                "pesan":"Semangat kak kuliah,departemennya dan sebagai aspraknya."# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya baik dan ramah",  
                "pesan":"Semangat terus kak, semoga dilancarkan kuliah dan urusannya"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Kalem dan berpikiran maju",  
                "pesan":"Tetap berproses bang menjadi lebih baik."# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Baik, ramah, mudah bergaul dan inspiratif",  
                "pesan":"Tetap menjadi pribadi yang asik dan menyenangkan bang."# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Baik dan pintar kakaknya",  
                "pesan":"Semangat terus kak, dijaga kesehatan dan kuliahnya"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak asik dan baik hati",  
                "pesan":"Semangat terus kakakk kuliahnya, sukses selalu."# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakaknya baik, ceria selalu dan ramah",  
                "pesan":"Tetap menjadi pribadi yang ramah kak, melalui senyuman"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Baik, ramah dan penuh ide ide menarik",  
                "pesan":"Semoga dilancarakan kuliah dan segala urusannya ya kak."# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Ramah, baik dan kalem",  
                "pesan":"Tetap semangat ya kak, sukses selalu dimanapun berada."# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kalem, namun berpemikiran maju",  
                "pesan":"Sukses selalu bang, jangan sampai kendor semangatnya"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kakaknya baik, pintar dan komunikatif",  
                "pesan":"Semangat terus kak kuliah, departemen dan tutorialnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MGO0kKQMFLSv6tamY8Sh2qwpQl-6Efq2",
            "https://drive.google.com/uc?export=view&id=154aB3f8gjNkmo0SZ36-wKLZpKcR-9Mcn",
            "https://drive.google.com/uc?export=view&id=1wr07T2vJO-3J4tNDY7ufNSs66YRMND5c",
            "https://drive.google.com/uc?export=view&id=11itmMLM72TjBDRwAeUFd2JCdwzwNqQ8y",
            "https://drive.google.com/uc?export=view&id=1ep3fXHVVC2XVqneaNKJiS_YoQvEohSpL",
            "https://drive.google.com/uc?export=view&id=1fTPTm2AW0BlKfSW1aO-Qjz2J5LRJflG9",
            "https://drive.google.com/uc?export=view&id=10s3zKv7q7cnYfqeLUG3IeLN91WDAYS8o",
            "https://drive.google.com/uc?export=view&id=1z47LPpK1FBVIo-wLLVNbjnbvoBpGGSct",
            "https://drive.google.com/uc?export=view&id=1aGZbwmVguBlF6j90RoUmGsGza1kAbq94",
            "https://drive.google.com/uc?export=view&id=1U0R3KxBaz5Dcm9N8KsQ5Qtep5nfNsci-",
            "https://drive.google.com/uc?export=view&id=11gSjvBYzT-JUb9rYfhmfHonQAFaPmQcX",
            "https://drive.google.com/uc?export=view&id=1c2Re0bo42CmlBgmaAfcisxnnR1s_E_03",
            "https://drive.google.com/uc?export=view&id=18hHlMrRzZ4pzJRDOyfUrrNN_mtpZFxE-",
            "https://drive.google.com/uc?export=view&id=17-uY2lwv7KevLj13EmtGddWr9MfjTdfQ",
            "https://drive.google.com/uc?export=view&id=1Uqsh2VJvyBqsrZc3C2ECbwo-3Fdzj0F9",
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
                "kesan": "Kakaknya baik, ramah dan aktif juga.",
                "pesan": "Sehat selalu kak, ditunggu kegiatan kegiatan menarik lainnya."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya ramah, dan pintar",
                "pesan": "Semangat selalu kak, dilancarkan ya kuliahnya."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya ceria banget, murah senyum, dan selalu positif..",
                "pesan": "Tetap tebar kebaikan dan senyuman ya, Kak. Semoga semua urusannya dilancarkan sampai lulus"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Sehat dan sukses selalu kak, kuliah maupun departemennya"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Kalem, penuh perhitungan namun memiliki sifat baik hati dan humoris.",
                "pesan": "Semangat terus bang, jangan sampai kendor."
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya baik, ramah, sopan dan penuh ide menarik ",
                "pesan": "Tetap semangat bang, ditunggu kapan acara ke-ibadahannya lagi."
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Baik, ramah dan lucu kakaknya.",
                "pesan": "Semoga  dilancarkan terus kuliah nya ya kak, dan tetap tersenyum"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Tegas, serius namun dapat hangat dan ramah kembali.",
                "pesan": "Dijaga kesehatan dan perkuliahannya ya kak."
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Abangnya memiliki pembawaan santai namun punya sifat yang baik.",
                "pesan": "Sukses dan jaya selalu bang, akademik dan non akademiknya."
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya baik, ramah dan kalem.",
                "pesan": "Tetap semangat bang, kuliahnya dan departemennya."
            },
            
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak yang paling aktif dan asik/menyenangkan.",
                "pesan": "Tetap menjadi pribadi yang selalu membawa kebahagiaan dimanapun kakak berada."
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakak yang baik, ramah dan perhatian.",
                "pesan": "Semangat kak, kuliahnya. Senang bertemu kakak, tapi gaya fotonya menutup wajah."
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya baik, ramah dan berpemikiran maju.",
                "pesan": "Tetap semangat dan sukses dimanapun bang."
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya baik, ramah dan soapan.",
                "pesan": "Sehat selalu kak, kuliah dan urusannya semoga dimudahkan."
            },
            
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen Rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakaknya pembawaannya positif dan ceria selalu.",
                "pesan": "Semangat terus kak, kuliah dan urusannya dipermudahkan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LHJ7wS8i743NEsrtqyLJ1vRtZcmWYKOu",
            "https://drive.google.com/uc?export=view&id=1n0Key7lYpVRu8CCUxIUrgnRkWxGebiXy",
            "https://drive.google.com/uc?export=view&id=17r0-7elpUpj5jcmVuAVqPfCVhQyTW7tR",
            "https://drive.google.com/uc?export=view&id=1lqfkylcERX8oxh_cKQIA_cWwfOFZBpVs",
            "https://drive.google.com/uc?export=view&id=14LEyYSjh_gVRvkUmJjOc63xS422CH1FL",
            "https://drive.google.com/uc?export=view&id=1LA-gaRYjzXv72G8Irh90leNIkgJbSg0C",
            "https://drive.google.com/uc?export=view&id=1lisj6XdGn0-GwTmg0DlFR0ljjqyd1_vp",
            "https://drive.google.com/uc?export=view&id=1M8iuLLDF7ad_WHLzBstX_rGAwTbv8hVF",
            "https://drive.google.com/uc?export=view&id=13gRmjJDKNRQUcFmQXINge46IzFYSYazs",
            "https://drive.google.com/uc?export=view&id=1ReaIjvYmP-fVcihv-427xl95w1uvZWwD",
            "https://drive.google.com/uc?export=view&id=1yF-EPfz7MnpmsDEfOTNaGPthXJIzwqNE",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "dananghk_",
                "kesan": "Abangnya memiliki pemikiran maju dan inspiratif.",
                "pesan": "Semangat dan sukses selalu bang. Tutor buat usaha tanpa modal bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Baik, ramah dan lucu kakaknya.",
                "pesan": "Tetap menjadi pribadi yang ramah kak. Sukses selalu."
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Kalem, namun penuh perhitungan dan ide inovatif.",
                "pesan": "Tetap semangat bang. Pantang mundur"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya baik, ramah dan murah senyum.",
                "pesan": "Tetap menjadi pribadi yang membawa suasana positif dimanapun kakak berada."
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Baik, dan ramah kakaknya.",
                "pesan": "Tetap semangat kak kuliahnya, sukses selalu."
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya pintar dan baik.",
                "pesan": "Sehat selalu kak, dipermudahkan kuliahnya"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Keren dan berpemikiran maju.",
                "pesan": "Tetap berproses bang, menjadi lebih baik."
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik, ramah dan lucu.",
                "pesan": "Semangat terus kak, kuliah, departemen dan urusan lainnya"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Kakaknya selalu membawa suasana positif.",
                "pesan": "Tetap menjadi pribadi yang membawa kedamaian dimanapun kakak berada."
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Baik, ramah dan murah senyum.",
                "pesan": "Dijaga kesehatan dan perkuliahannya ya kak, sukses selalu"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Tenang namun penuh dengan ide inovatif.",
                "pesan": "Ditunggu kak kegiatan kegiatan departemen lainnya, sukses selalu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Q1klKjykj7jKreoF3-_1b7ebThuZ5rXo",
            "https://drive.google.com/uc?export=view&id=1cgGxeNuVv9FM1Nw89gNc8FNU3NJSSt5q",
            "https://drive.google.com/uc?export=view&id=1pifBGey_dKkI0Z650TdRddc-VwrYdqMH",
            "https://drive.google.com/uc?export=view&id=1r4LRLaA7HYjJDtRUb-wVyCLU_q-QFKJI",
            "https://drive.google.com/uc?export=view&id=1DCby9r6i2ntbLLazdCcggwFUX5v22LEJ",
            "https://drive.google.com/uc?export=view&id=10LDm9frqtNo5jgzYtsVQh2b6wmNwKoKv",
            "https://drive.google.com/uc?export=view&id=13UeG5eUbNaxGvhPPdUB7JmegmqRkvfjK",
            "https://drive.google.com/uc?export=view&id=12dGcvRvAR8XJyLzAqR97EtpJciYeesri",
            "https://drive.google.com/uc?export=view&id=1EGIS-I2gDVWRqgw2znf3_ENJCjcu3vq0",
            "https://drive.google.com/uc?export=view&id=1qpyne1OCzuB63JjoZHbrB58XrIVJrY2n",
            "https://drive.google.com/uc?export=view&id=1y5VofyjD4X6KQTIKAp24ZAvv9jv3Gbmq",
            "https://drive.google.com/uc?export=view&id=16K0OY6b2TVzbvc6Pfs_QhGnJ5XHBnQG5",
            "https://drive.google.com/uc?export=view&id=17OPdaZHfUiJzOVzsmPQdl_0I9-CIi3Ji",
            "https://drive.google.com/uc?export=view&id=1Q6WI5ZjL8DnV9FJzkZAejxhtQZAce1bC",
            "https://drive.google.com/uc?export=view&id=17ftZWUdzhFRqz9vyhYJ0qM22Nhd_2Wgt",
            "https://drive.google.com/uc?export=view&id=1Da0Ms-nb9lXK5B6axgo6hXzj8Q-CIaem",
            "https://drive.google.com/uc?export=view&id=1FdxSxpRy8-oCQnoDGcXc_SpqIOvXmFyf",
            "https://drive.google.com/uc?export=view&id=1kERfPFWL6qQO2hc1upythgEMZttn21jK",
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
                "kesan": "Kakaknya asik, aktif dan memiliki ide ide kreatif",
                "pesan": "Terimakasih kak, menghadirkan konten terbaru dari Sains Data. Saya selalu me-likenya. Sukses selalu kak."
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Baik dan ramah kakaknya",
                "pesan": "Tetap semangat kak, kuliah dan departemennya. Ditunggu ide ide konten menarik lainnya"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Abangnya inspiratif dan ramah.",
                "pesan": "Semangat terus bang, kejar apa yang diupayakan yang baik."
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abangnya ramah, aktif dan baik",
                "pesan": "Sehat dan sukses selalu, bang"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Baik, ramah dan suka membantu",
                "pesan": "Semangat dan sukses selalu bang dimanapun abang berada"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Baik, ramah dan pembawaannya positif",
                "pesan": "Dilancarkan terus kuliahnya ya kak."
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Baik, ramah dan lucu",
                "pesan": "Semangat terus kak, kuliah dan urusan lainnya pasti dimudahkan"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakaknya baik, murah senyum",
                "pesan": "Semangat terus kak, sukses selalu"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Ramah dan pembawaannya positif",
                "pesan": "Semangat terus kak, kuliahnya dilancarkan ya."
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya baik, ramah dan asik",
                "pesan": "Dijaga kesehatan dan perkuliahannya ya kak"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya lucu dan baik hati",
                "pesan": "Tetap menjadi pribadi yang membawa suasana menyenangkan ya kak"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya baik, seru dan menyenangkan",
                "pesan": "Dimudahkan selalu kuliah dan urusannya."
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Tenang, kalem namun memiliki sifat baik hati",
                "pesan": "Keren banget konten-kontenya kak. Ditunggu selanjutnya. Semangat dan sukses selalu buat kakaknya."
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Abangnya asik, dan baik hati",
                "pesan": "Semangat terus bang kuliahnya!"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya sangat baik, ramah dan lucu",
                "pesan": "Sukses selalu buat kakaknya, yang direncanakan berhasil"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Baik, ramah dan sopan kakaknya",
                "pesan": "Dijaga kesehatan dan kuliahnya ya kak."
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya pembawaannya menarik dan positif",
                "pesan": "Tetap menjadi pribadi yang selalu membawa aura positif."
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya kalem namun kreatif",
                "pesan": "Semoga berhasil kak, kuliah dan departemennya. Sukses selalu"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
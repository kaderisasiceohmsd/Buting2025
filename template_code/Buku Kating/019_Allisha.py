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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1H4plh0dyhyS3d4uIuj_Ct2OyESmCAxp-",
            "https://drive.google.com/uc?export=view&id=1uW4uyECBjiufmtrxEnlT0zARgrlUiMHs",
            "https://drive.google.com/uc?export=view&id=1eSe1D9F7JSIbOIqnaA6vLHjz39tVCfQt",
            "https://drive.google.com/uc?export=view&id=19SCgh0WE5E7kD66mAl5ay1-5TLeLkOXW",
            "https://drive.google.com/uc?export=view&id=1B-6PHRG2pPq_NS1xET3H_jXQSGizRxj5",
            "https://drive.google.com/uc?export=view&id=1cgCiKM9UzwHaIgWOLc3H-l2s0AVNo2uL",
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
                "kesan": "Keren dan Berwibawa",  
                "pesan":"Sukses terus ya bang, tetap jadi panutan!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Selalu ramah dan gampang diajak ngobrol",  
                "pesan":"Semoga makin sukses dan terus menginspirasi"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Lembut, Ramah, dan selalu bikin suasana nyaman.",  
                "pesan":"Sukses terus ya kak, semoga makin bersinar di setiap langkah!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Anggun, ramah, dan selalu murah senyum",  
                "pesan":"Semoga kakak makin bersinar di setiap langkahnya."# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Asik, orangnya ceria dan gampang akrab sama siapa aja.",  
                "pesan":"Semoga semangatnya ga akan pernah padam dan sukses selalu."# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Lucu, rame dan kocak abis",  
                "pesan":"Jangan pernah berubah ya kak, dunia butuh orang se-random kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NW8lfj2X0yEmAGlgoraWp6OD6NBR9mzx",
            "https://drive.google.com/uc?export=view&id=1-Elt7zpd2F8VGVEhsAaxxK30eNXQyoK5",
            "https://drive.google.com/uc?export=view&id=1jeah5D1eDLWaZGb1p2G2oh2_HX7OEBXi",
            "https://drive.google.com/uc?export=view&id=1HWRnOz2FV3GKxh1FIhfml8cgPu7WlKYY",
            "https://drive.google.com/uc?export=view&id=1zCa6ZT-vd9FsCczT84pN7vLoL2R1vMGt",
            "https://drive.google.com/uc?export=view&id=1--eyys0At5kw1oGh-Y5JcovDSAO8A8tE",
            "https://drive.google.com/uc?export=view&id=185nWv2B1WycMFCVvefNbNPnQdWp37bl7",
            "https://drive.google.com/uc?export=view&id=127P1KwLR6PYTOLeHzzMxxIOQZbcq9SCx",
            "https://drive.google.com/uc?export=view&id=1EOxP22TRboeq5hArgzCrPJK4CW-cna6k",
            "https://drive.google.com/uc?export=view&id=1c0ppVVMPGbrWNxcX4tVFyjNC7sNHzxSn",
            "https://drive.google.com/uc?export=view&id=1fVMR-NVo8heX8MBVqlLkAeOZKOnI4FgR",
            "https://drive.google.com/uc?export=view&id=1uwca5-sDKzL9Gqe8G06P0CG-LXja7uo-",
            "https://drive.google.com/uc?export=view&id=1AosB_Elfwts5R3Mh7X32NnYKcW9Vnp1q",
            "https://drive.google.com/uc?export=view&id=1COFOPAu9KZcIQDlEGKPSeoXTH7FVdsOu",
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
                "kesan": "Supportive & easygoing banget",
                "pesan":"Semoga karier dan masa depan bang jer makin gemilang."
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Ramah, hangat, dan mudah akrab dengan siapa saja.",
                "pesan":"Semoga kakak sselalu dikelilingi kebahagiaan dan hal-hal baik!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Penuh semangat dan punya aura positif.",
                "pesan":"Semoga semua impian kakak tercapai dan selalu bahagia."
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Selalu Semangat dan ceria",
                "pesan":"Semangat jalani hari harinya kak."
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Punya huumor yang bikin suasana lebih seru.",
                "pesan":"Makasih udah selalu support dan kasih motivasi."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Ceria dan punya aura positif",
                "pesan":"Teruslah menjadi sosok yang hangat dan inspiratif."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Asik, santai dan bisa diandalkan.",
                "pesan": "Sukses terus ya bang, tetap jadi panutan."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Pendiam dan jarang bicara, tapi selalu punya aura positif.",
                "pesan":"Tetap jadi sosok yang tenang dan hangat."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Ramah, hangat dan mmudah akrab",
                "pesan":"Semoga kakak selalu dikelilingi orang baik."
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Ramah dan gampang diajak ngobrol",
                "pesan":"Semoga energi baik kakak, selalu nular ke orang-orang sekitar."
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Santai, tegas dan bisa diandalkan.",
                "pesan":"Tetap jadi sosok yang positif dan inspiratif ya bang!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Tegas tapi tetap hangat dan ramah.",
                "pesan":"Semangat dan sehat selalu."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Ceria, ramah dan asik diajak ngobrol",
                "pesan":"Semoga semua impian kakak tercapai dan selalu bahagia."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Positif dan selalu semangat dalam hal apapun.",
                "pesan":"Terus jadi kakak yang asik dan menyenangkan ya kak."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aI-V91s-XA7g6pqj9wtd1qTOA-pkMBWU",
            "https://drive.google.com/uc?export=view&id=1iOkXCIP2MNI7QXo_2_rA1xKw9TDug30L",
            "https://drive.google.com/uc?export=view&id=15Vj5Cj-PSKfLyXIFIV6KxRTFhlVSrteH",
            "https://drive.google.com/uc?export=view&id=1scEGfwKXxBVLDapsCHbMf1zR31wAfSkC",
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
                "kesan": "Selalu profesional, penyabar, sangat bisa diandalkan dan asik saat diajak berdiskusi",  
                "pesan":"Tetap jadi bang Bintang yang selalu menginspirasi banyak orang!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Perhatian, ramah, dan bersemangat",  
                "pesan":"Tetap jadi ka Nadya yang paling imut, kiyut & funny."# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Punya aura yang positif, bijak, ramah dan menyenangkan.",  
                "pesan":"Semoga kak Azizah selalu di berkahi dan sukses di segala hal."# 1
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Selalu tenang, asik dan juga penyabar.",  
                "pesan":"Semoga kebaikan dan semangat kak Hana selalu menginspirasi."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_0T5ulhSI0tyoQadxY4E8mrTm8AKkLJW",
            "https://drive.google.com/uc?export=view&id=17p9AjKS8GupqxSr8Ox3RPSaLfHFrhFde",
            "https://drive.google.com/uc?export=view&id=1YGzu88yvmrYkQ3VhaeiI8mUABmxriYq3",
            "https://drive.google.com/uc?export=view&id=1W3k84zUsjy64dx1l5ExWG3Yp1-h5elu0",
            "https://drive.google.com/uc?export=view&id=1j2EuFWD42_2yPwnkEGpjg4Rf9q0RbFkT",
            "https://drive.google.com/uc?export=view&id=1TtMps7Zq-3vnemZFxnjjjdjjdr4z1Md4",
            "https://drive.google.com/uc?export=view&id=1r2KxwwoWdjCrzAql4IlKdFDSTxYk75D5",
            "https://drive.google.com/uc?export=view&id=18iE_WMUToNgtxqt1R9UkzLzWiDOWBmxY",
            "https://drive.google.com/uc?export=view&id=1r_rEdxCYbqIoEXgGdd7RcVNwl3aBlZRb",
            "https://drive.google.com/uc?export=view&id=18axZlO1JrwxMCEoAkS7F9MMECHhFPz3P",
            "https://drive.google.com/uc?export=view&id=13A_F0QVH_-s9j_5AJnnMPl8mD0x_vi48",
            "https://drive.google.com/uc?export=view&id=1pibNe-oqA58nWgZHfRmpnioldNQAJuLQ",
            "https://drive.google.com/uc?export=view&id=1TEJmX8stokIKJI_OEtXQ10qLCyZfav3G",
            "https://drive.google.com/uc?export=view&id=1Jtf_RDpvbuMVld4E7U4v8IK6S8TsIP-r",
            "https://drive.google.com/uc?export=view&id=1MIPzFvD3T3NRp_Vh3BvHxRxCBMcTAR3W",
            "https://drive.google.com/uc?export=view&id=1Xvvrdh2H_aVgQGl492PVEbmDwA0tk0xD",
            "https://drive.google.com/uc?export=view&id=1kZSoqM0x3xqPWCc2DfRBFdH_PsxeeAc8",
            "https://drive.google.com/uc?export=view&id=1q3urNVR76yLtV82uyWJfp2gNCpSBYx2n",
            "https://drive.google.com/uc?export=view&id=16dHnPHsIYbjkyck3kn0HZ92QRM8BKYpv",
            "https://drive.google.com/uc?export=view&id=1jKUcJwehr953CNjCNGESZut506ZfDO6_",
            "https://drive.google.com/uc?export=view&id=1dNlkun5NKlrYrv_he3oRno3XkvVI8kwo ",
            "https://drive.google.com/uc?export=view&id=1iWg_AR4o3y52Pr4wQdwQG9Rs_r2SB0Zx",
            "https://drive.google.com/uc?export=view&id=1ewK38WKGPe8wfivqhGF2SUah4_3OS8DP",
            "https://drive.google.com/uc?export=view&id=17Y7zV8rs6Q_vU3jvc8vuc87OZu4e3KUj",
            "https://drive.google.com/uc?export=view&id=1eLsptqozQTbOPxgnl1cOOiCiMecXJZmP",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "Tegas dalam menegakkan aturan.",
                "pesan": "Semoga sukses dan selalu bahagia."
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Punya senyum yang menenangkan dan sikap yang sopan ke semua orang..",
                "pesan": "Semangat kuliahnya kak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Punya semangat tinggi, Tegas, dan sangat perhatian.",
                "pesan": "Terus semangat ngejar cita-cita kak alya, semoga semua impian kakak tercapai."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Punya semangat belajar yang tinggi, santai dan bertanggung jawab",
                "pesan": "Terus semangat buat capai cita-cita"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Disiplin dan rajin, kalem tapi punya pesona tersendiri",
                "pesan": "Semoga perjalanan hidup kakak selalu diberi kebahagiaan, keberkahan, dan kesuksesan."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Energinya nggak pernah habis, bikin suasana jadi hidup terus.",
                "pesan": "Jangan berubah ya bang, dunia butuh orang seceria abang."
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Punya semangat yang stabil, dan tenang",
                "pesan": "Semangat jalani hari harinya bang."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Gayanya santai tapi tetap sopan dan juga ceria.",
                "pesan": "Semoga masa depan kakak dipenuhi kebahagiaan, keberhasilan, dan orang-orang baik di sekitar kakak."
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Pinter, tangguh, dan selalu punya cara sendiri buat nyelesain sesuatu.",
                "pesan": "Semoga semua impian abang bisa tercapai dan langkah abang selalu dimudahkan."
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Tipe yang konsisten, kalau udah komitmen sama sesuatu, pasti dijalani sampai selesai.",
                "pesan": "Tetap konsisten dan tanggung jawab dengan semua yang abang jalani, yaa!."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Punya perhatian yang tulus, dan selalu siap membantu.",
                "pesan": "Selalu menjadi kak vany yang seperti ini yaa!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Ramah, asik, seru dan kocak.",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
              {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Punya jiwa tangguh dan nggak gampang menyerah menghadapi tantangan.",  
                "pesan":"Semoga selalu bahagia"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Tenang dan punya kepribadian yang kuat.",  
                "pesan":"Semangat selalu kak"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Selalu membawa energi positif, bikin suasana jadi lebih hidup.",  
                "pesan":"Terus pertahankan keceriaan dan energi positif"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Ramah dan mudah akrab sama siapa aja.",  
                "pesan":"Selalu ceria ya kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Disiplin dan bertanggung jawab",  
                "pesan":"Tetap disiplin dan konsisten, itu akan membawa abang ke kesuksesan."# 1
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Punya selera humor yang bikin suasana jadi hidup dan nggak membosankan.",  
                "pesan":"Semoga selalu menjadi pribadi yang menyenangkan."# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Jago banget dance, selalu berani tampil dan mengekspresikan diri.",  
                "pesan":"Terus pertahankan semangat dan bakat kakak di dunia dance, karena itu keren banget"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Punya selera humor yang unik dan kadang nggak terduga",  
                "pesan":"Tetap jadi pribadi yang rendah hati dan bisa diandalkan."# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Kadang terlihat garang, tapi kadang lucu tanpa disadari.",  
                "pesan":"Tetap tegas tapi jangan lupa tunjukkan sisi hangat."# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Ramah dan mudah akrab terhadap siapapun.",  
                "pesan":"Semangat terus kuliahnya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Santai dan bisa diandalkan.",  
                "pesan":"Tetap rendah hati dan bisa diandalkan."# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Punya karakter yang sabar dan penuh perhatian.",  
                "pesan":"Semoga masa depan kakak selalu penuh kebahagiaan, keberkahan, dan kesuksesan"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Selalu bisa memecahkan suasana menjadi seru.",  
                "pesan":"Terus jadi diri sendiri ya bang."# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Tegas, santai dan asik.",  
                "pesan":"Semangat kuliahnya bang."# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Lg9mgm75xDaPdAQc6ZvZ-Yiet4I_5YLr",
            "https://drive.google.com/uc?export=view&id=1fawLLjIgov46jW5PFZmlDKEXhQOEbCR3",
            "https://drive.google.com/uc?export=view&id=1Un7Al2JGPw4igWSQIABAKct2SOJeJLhY",
            "https://drive.google.com/uc?export=view&id=1hbdfUfYhiJ7NvT2rHrezvB7R6QmTwKlP",
            "https://drive.google.com/uc?export=view&id=1ijgrO2jNB2KXqnJqwH0dqdXjuDds99XP",
            "https://drive.google.com/uc?export=view&id=1Luzu-NwEKjC4Dd-QLLWvbX0LQbVMObZC",
            "https://drive.google.com/uc?export=view&id=1gQ1mKiWhTsWCds-k5cXtaJkUKKiXTSNT",
            "https://drive.google.com/uc?export=view&id=1GO-Yb541avCm1BKbAjp14rGTdFUXsYvz",
            "https://drive.google.com/uc?export=view&id=157zin-68A7R-dsYc3uSxv59EVu5boTe5",
            "https://drive.google.com/uc?export=view&id=1vropcHfg1sAQNkdIPqGD20xRlWA9ige_",
            "https://drive.google.com/uc?export=view&id=1dxzbxQ7q6MrpI6NWjxrQpIaUQEkhRav8",
            "https://drive.google.com/uc?export=view&id=1u8JIexWWTcZDAP3V39CxyttnDefL0-aJ",
            "https://drive.google.com/uc?export=view&id=1uCQ7dKZ9f8FstpKu_X5z0itJJ5Q3hJVm",
            "https://drive.google.com/uc?export=view&id=1WLm0SpjeUpYjeIOT0D028Pa5Z1Gnu_m1",
            "https://drive.google.com/uc?export=view&id=1zpStW_XJ2q749eZKiH2M_YQHTO0jUTHO",
            "https://drive.google.com/uc?export=view&id=1yi2dQngbrzmwy2QorKB7v_5Zk_ibaaXA",
            "https://drive.google.com/uc?export=view&id=1DJZKmCVBj01IpYpac47r3Z3pS3NThIhG",
            "https://drive.google.com/uc?export=view&id=19YS0qGgAUvup0TjkTX1eSO6rl6QYWWQA",
            "https://drive.google.com/uc?export=view&id=1QLGbgup7jw1657x55RDvC2WrvTFb1QBp",
            "https://drive.google.com/uc?export=view&id=1olAizFsNUSDLxINa8mrwjfe94PsLUA3k",
            "https://drive.google.com/uc?export=view&id=1PCFbLx7nh6bGS9NqTWVNN62gZUOmtEaV",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "Penyabar, tenang, dan kalem",  
                "pesan":"Semoga langkah yang di jalankan penuh berkah"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak gemacc & fun",  
                "pesan":"Semoga sehat selalu, semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Bang Keya imup, kiyut",  
                "pesan":"Semoga Cumlaude ya bang"# 1
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak cantik, Lonjwin lovers!, & Dancer",  
                "pesan":"Semangat Terus kakak, kapan kapan kita nonton TDS bareng xixi."# 1
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Cerdas dan punya wawasan yang luas",  
                "pesan":"Semoga ilmu dan pengalaman kakak selalu membawa kesuksesan kedepannya."# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Cantik, Lucu, keliatan vibes arab",  
                "pesan":"Semangat mengejar cita citanya kak."# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ub1qhEprrBGqpBQAY-W6ma70W0wZLxaj",
            "https://drive.google.com/uc?export=view&id=1niC3CZ34r9sr6a1qUl1YRiFxL3i0tnQ",
            "https://drive.google.com/uc?export=view&id=1aRYWnVHPAUSA6q86jJchWgMFq4kvnGPD ",
            "https://drive.google.com/uc?export=view&id=1d9LykSP5Rmoy60spf3IDnTDhqA9VsoVc",
            "https://drive.google.com/uc?export=view&id=13pG_HqMGT1LRW9Qpji0zDkDWwQTfnxjT",
            "https://drive.google.com/uc?export=view&id=1l5q8NCpIX1XrGzY1KsC-UafBlrEphdwB",
            "https://drive.google.com/uc?export=view&id=1TSB_5gTWwqGcLsqQS09nOw-h6hBxMHWs",
            "https://drive.google.com/uc?export=view&id=1SgRIUuL6uOwul5d2Kb6-KYnzyr-MgkLT",
            "https://drive.google.com/uc?export=view&id=1-P9Wc8dcMq8HuL0BnOJxYnBHoxBOe0pD",
            "https://drive.google.com/uc?export=view&id=1Deygq8tWG4ybMMEB1efnXTcbL8V100Ao",
            "https://drive.google.com/uc?export=view&id=1jjX64ZjTp_OplYTjIDHxmcajH8MXGw6O",
            "https://drive.google.com/uc?export=view&id=1WSfovwccR875rkmfbj97a_WLq7-OcRgP",
            "https://drive.google.com/uc?export=view&id=114fMeC0tfnMlCUaS3Qic-36nL-_KyhpV",
            "https://drive.google.com/uc?export=view&id=1tqzLY3BZBsx6wc0vqh5j31PGs1i0Eket",
            "https://drive.google.com/uc?export=view&id=1umRA9V-x6GAbzTA1Mv3Kz0te-ZBUyQK-",
            "https://drive.google.com/uc?export=view&id=1Ul-QjtkKbG5wZCV8vkBy80cPX095F22O",
            "https://drive.google.com/uc?export=view&id=1sfvbrQVsu3tpjUGq7xlSkfelXxdcjPM9",
            "https://drive.google.com/uc?export=view&id=1t5OYBQr1wxwf30ZTfSohYY5VZQHUDebP",
            "https://drive.google.com/uc?export=view&id=1eaWkaOYbRxd4xunspO-c6tJ4fqrhkrTV",
            "https://drive.google.com/uc?export=view&id=1s8_YeXeJbQqoUkNqsmDKlyS5KRuJaTs_",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },   
            
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ksZCJ3rYYqJr24vSgf0WJQBvz5cEnS5-",
            "https://drive.google.com/uc?export=view&id=1xdfBIclIj_qy5lVk7OaCIN1rhVQVJUDq",
            "https://drive.google.com/uc?export=view&id=1YsK5R-rCZLxxxmAL_EAZcAejbMknOerA",
            "https://drive.google.com/uc?export=view&id=1YsK5R-rCZLxxxmAL_EAZcAejbMknOerA",
            "https://drive.google.com/uc?export=view&id=11PyT0o18K0GtyrRuamwTBfG8IvMqWz2-",
            "https://drive.google.com/uc?export=view&id=1TnY8H4z37uwYpzuaNaNKxEYk2Id53Alo",
            "https://drive.google.com/uc?export=view&id=1JdyW5kP8juNLfW60uX62CX7IMAOM30zN",
            "https://drive.google.com/uc?export=view&id=1mgPdv69THN0I9jpjmf9W6BYbktIX_38s",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1_6WYG2Ztfw3i5X2PUbqM8SHXNpBAJy3N",
            "https://drive.google.com/uc?export=view&id=1bd5o6uBsvRzi8OlXb7-1F-W-w_oCBCQ4",
            "https://drive.google.com/uc?export=view&id=14q5wH_my-ycMqUTgrI8XMMRglUzJyPcc",
            "https://drive.google.com/uc?export=view&id=1mmO82IGtX_j4xZ-6X1qx6ByOBXqK8ePD",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "-",
                "nim": "122450030",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "-",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1emqDNTp7GU_ot0032F1LjZg5SFCzZBAw",
            "https://drive.google.com/uc?export=view&id=1HCMnja0GMcK-VstfFLbWHoKtTdwzbtQX",
            "https://drive.google.com/uc?export=view&id=1aBB8bCvXC0s0ezkwOQAWM56QQVxpv9Q2",
            "https://drive.google.com/uc?export=view&id=1_JAj4Lf9Dgbcqnd8oT47n-WGS-da1wOn",
            "https://drive.google.com/uc?export=view&id=1SiISVfWz_EMPO6WVHHt5CKLj3tKrmM57",
            "https://drive.google.com/uc?export=view&id=1rvnGYe0j8JjibTc1DqgaRAYtuM9jvntM",
            "https://drive.google.com/uc?export=view&id=136KYTLjZbN80XSehVmALozZ8iNkxKedV",
            "https://drive.google.com/uc?export=view&id=1NZiLzqNQdi-aScXij2w0YGl8uShwMu2m",
            "https://drive.google.com/uc?export=view&id=1blq1NurXHmYtTIQIrJs0gxAN2Wi6xc9t",
            "https://drive.google.com/uc?export=view&id=1wxmIofxLxI7PWAjDlZCUnRG0FstCIInV",
            "https://drive.google.com/uc?export=view&id=1WTCsy-2XL3MqLJN9OnTja9sKYCYuA9_F",
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
                "kesan": "Kakaknya asik dan seru.",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Senang bisa berkenalan dengan kakak.",
                "pesan": "Semoga sukses selalu kuliahnya!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Kakaknya ramah dan baik.",
                "pesan": "Sehat selalu ya, kak."
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif.",
                "pesan": "Semangat terus kuliahnya, kak!"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Senang bisa bertemu dengan kakak.",
                "pesan": "Semoga semua urusannya dilancarkan."
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Sukses selalu untuk kakak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Kakaknya asik diajak diskusi.",
                "pesan": "Terima kasih atas bimbingannya, kak."
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya, kak!"
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu, kak!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya sangat ramah.",
                "pesan": "Jaga kesehatan selalu, kak!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Terima kasih kak atas bantuannya.",
                "pesan": "Semangat dan sukses selalu!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vH5Y2Jmbc4ugOO2lvzWdYPVCzsRkFzFc",
            "https://drive.google.com/uc?export=view&id=1lZcLZ5EVKALBiSms51P-rK5m8PID_Yfl",
            "https://drive.google.com/uc?export=view&id=1d2jVK4moeStfgoeE0zKACpvZbj_aEKD1",
            "https://drive.google.com/uc?export=view&id=14bQdliudik6CtxijpelGvB6kugl_enDD",
            "https://drive.google.com/uc?export=view&id=11tlKePxS_KZGlWVJg3Q8D_8xY35rn76R",
            "https://drive.google.com/uc?export=view&id=1x8hAl0X9qMY9_gYGdoTFT_szf4ftRKa9",
            "https://drive.google.com/uc?export=view&id=1j6O7jVEK-z-3MlMMMJekqPfGPhlv41gG",
            "https://drive.google.com/uc?export=view&id=1YbOl2ecHn1gA6vGGorjeHC4ePQEywGIh",
            "https://drive.google.com/uc?export=view&id=17aQpdMr0uER4-I22T186psinMLf62ExU",
            "https://drive.google.com/uc?export=view&id=1osQZhQZkR23Tx9SfMX7xMBv-oa_KXogU",
            "https://drive.google.com/uc?export=view&id=1y4PNU8FacChtmpeeF4npFzrtlEiClXG3",
            "https://drive.google.com/uc?export=view&id=1lWMyJ9s3dqAoS_42dCmmMiagQkqL8FVV",
            "https://drive.google.com/uc?export=view&id=12TI4w2XbhdrKNQSgH8XKK810rs9j66yJ",
            "https://drive.google.com/uc?export=view&id=1qVoOZCY4IiOhpYJmjcvnv0kfKuJjScgn",
            "https://drive.google.com/uc?export=view&id=1TLnlPMhEwUf1GEkglfWQnoscYyml5N06",
            "https://drive.google.com/uc?export=view&id=1Sl06-0XCD2lSpvJl4yBRgtAj80isquRf",
            "https://drive.google.com/uc?export=view&id=1CWjfoojJYFmrWEklLxunCP_YTmY8XcbG",
            "https://drive.google.com/uc?export=view&id=1K-8CLQjhJAoRcvqtk-2p3hLevFov4r1z",
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

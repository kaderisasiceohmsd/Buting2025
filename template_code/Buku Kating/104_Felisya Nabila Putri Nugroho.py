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
            "https://drive.google.com/uc?export=view&id=1_GrWo0r48n2bcK-gPdPbA--8KHpkByip",
            "https://drive.google.com/uc?export=view&id=1bfmeKSigCUXjTazkobkVvNSLhrAkBAWq",
            "https://drive.google.com/uc?export=view&id=1Qr5lK7YFzz8AvRbuE2KZmHyleVrTKCV1",
            "https://drive.google.com/uc?export=view&id=1pSURnEN-_fU8GcyATXinyAqo3-c4gMph",
            "https://drive.google.com/uc?export=view&id=17M5bQ7hWIHEJsuixOZb7zeSnpW59p5hN",
            "https://drive.google.com/uc?export=view&id=11-GkEVVfoqZkerV165WKWNiyuBAhpIDZ"
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
                "kesan": "bang rendra baik banget,kocak, ramah ",  
                "pesan":"semangat bang buat menjalanikehidupan yang huru-hara ini, semoga dipermudah bang buat kedepannya!!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "kocakkk banget, kalau suporterran apalagi,tapi agak menyeramkan dikit bang",  
                "pesan":"semangat bang detik-detik kelulusan,semoga segala sesuatunya dipermudah, bang makasih ya udah ditolongin ganti batrai remot motor vario merah !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak cantik bangetttt, ramah, murah senyummm,lucu",  
                "pesan":"semangat kakkk kuliah di ujung semester, semoga lulusnya mudah dan dapat kerjanya mudah yaaaa kakk !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini lembut banget nada bicaranya, lucu, kalem, pinter",  
                "pesan":"semangatt ya kakkkk, sukses selaluuu !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak eksantyy asik bangettt, pinter, suka tiba-tiba nanya kamu orang jawa ya, random sekaliu,cantik ",  
                "pesan":"semangat terus kuliahnya kak, semoga lelah menjadi lillah !!!"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini cantik , tapi jujur agak takut awal awal liat kakak hehehe, tapi ternyata asik hehehe",  
                "pesan":"semangat ya kak kuliahnya semoga dipermudah semua kedepannya!!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ClRusp40kMdfdF-fz21WAU3utSvUw6b5",
            "https://drive.google.com/uc?export=view&id=16bdX4nVwAzfiP1bKsFig2vJvQaVl2Caw",
            "https://drive.google.com/uc?export=view&id=1O2emcRq8a960Sj7iHM5XDYKsVq9sZALr",
            "https://drive.google.com/uc?export=view&id=1DnRXU1P1f7hTyPAK4hhfuFpDv-1j21fk",
            "https://drive.google.com/uc?export=view&id=1ouUyt-vfG0HyDsFvFkC0NLDfivz6uu2d",
            "https://drive.google.com/uc?export=view&id=1-SQg6erksNtDaHyPIQvXn5SUi5eV8Vs3",
            "https://drive.google.com/uc?export=view&id=1SPoAd83aKOVfb2O_5k6uaBpFhspPlgrH",
            "https://drive.google.com/uc?export=view&id=1glPrFUKb-lsKitor0LswtKMuwKP3Nw6g",
            "https://drive.google.com/uc?export=view&id=1dTmGTyZLuKDtiDsbk6JW6MZId34XICV5",
            "https://drive.google.com/uc?export=view&id=1gv7HYR6OHlEHJvvHgjMza4w61lu-WmBH",
            "https://drive.google.com/uc?export=view&id=1ZOt9FNVjfse0oN6QHemk9Eo7xip_byvj",
            "https://drive.google.com/uc?export=view&id=1wXwULhTmYSUtBM9kBSG8mUKLzvyAfwgC",
            "https://drive.google.com/uc?export=view&id=1PBHA8qs2_pRdrh4TojrDxlQkbGnZtZ-v",
            "https://drive.google.com/uc?export=view&id=1C4kVd5PJ5QaxG3ezSFovOZeSFIqsq_7F",
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
                "kesan": "bang jere satu kelompok fg, asprak alpro, cinaa banget, baik banget, kece abiss, asik dan murah senyum ",  
                "pesan":"semangat banggg, semoga cerita yang di fg itu tentang harapannya dipermudah,dan lancar dan sukses selalu bang jeree !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Kakak ini asik, baik bangettt, asprak ads top, pinter banget, cantikkkk",  
                "pesan":"semangat di semester akhir kakkk,terimakasih telah membantu aku yang kesulitan di prak ads waktu ituuu, sukses kakkk !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya tinggi bangettt, cantikk, hobinya unik btw, lucuuu",  
                "pesan":"semangatttt kakkkkk, semoga lelahnya selama ini menjadiii kesuksesannn !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Kakak cantikkk bangetttt, suka lihatnyaaa, lucuu",  
                "pesan":"semangat terus kuliahnya kakkkkk !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "aduhhh pinter banget banggg herannnn oztnya itu lohhh, kalo jelasin tutor enak banget dan nyambungg, asprak ads dan pecinta r",  
                "pesan":"semangat bang kuliahhnyaaa, bersinar selalu dan sukses banggggg !!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakkk lucu bangettt, palagi gradasi warna rambutnya keren bangettt plissss, cantik banget",  
                "pesan":"semangat kakkk, next infokan warna gradasi rambut yang bagus !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "abangnya murah senyummm, ramah dan ngga sombong",  
                "pesan":"semangat dan sukses selalu bangggggg!!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "bangggg kocakkk bangettt, seruuu banget bikin ketawaaa",  
                "pesan":"semangat bang menjalani semester 6,7,8 wkwkwk, sukses ya banggg,semoga jadi dpr !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakkk cantik sekaliii, lucuu jugaa, asik juga ",  
                "pesan":"semangattttt kakakkk sukses selalu buat kedepannya !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak iniiii lucuuuuu, asikkkk bangettttt tolongggg, seru plis, cantik jelas banget",  
                "pesan":"semangat terus kuliahnya kakak, semoga bisa naik jadi dpr kakk wkwkwwkk !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "banggg jujur rada takut liat abang, karena tatapannya tajem hehehe, tapi baik ternyata dan ga semenyeramkan itu",  
                "pesan":"semangat kuliahnya banggg, semoga next jadi dpr !!!"# 1
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "banggg hobbi abang random banget, kocakkk, asik juga, suka ngejokes",  
                "pesan":"banggg sukses buat next-nya, semoga dari baleg jadi dpr wkwkwkwk !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "-",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "lucuuu bangettt, tapi sedikit pendiam ya sepertinya kakkk,baik sekaliii",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "unikkkk, lucu juga, daplok kedua yang aku kenal setelah daplok aku, baikk sekali,cantikkk bangetttt ",  
                "pesan":"semangat kakkk wawaaa kuliahnyaa dan kedepannyaaa, sukses kakkkk !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JeQDlRrbc73-VuCNNLQn6NCb9EazSeE-",
            "https://drive.google.com/uc?export=view&id=1TyQfUhST-iqJtbX9NaTZweMYRtPKNzIz",
            "https://drive.google.com/uc?export=view&id=1kvcSUviWTfIhnMYMxI9kbDgsXSisZQCL",
            "https://drive.google.com/uc?export=view&id=1Bh5vvoBa79yDGcKGXg5JSe5KXgL6S8bn",
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
                "kesan": "bang bintang orang pertama yang kenal karena verbek, fc bukti bayar ketinggalan terus dianter ke utsman, baik sekali, keren sih senator kita ",  
                "pesan":"bang terimakasih karena sudah diantar ke utsman, semoga lancar semua step menuju kelulusan, sukses selalu bang !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak, cantikk banget, ga sangka kalo kakaknya bagian dari senator, tapi kadang sedikit jutek, kadang saya takut, tapi jujur cantik",  
                "pesan":"semangat terus kakk, semangat buat jadi orang hebat, semoga nular kak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "MasyaAllah banget cantiknya, pentutor ale topwan enak banget kalo jelasin, sabar",  
                "pesan":"semangat selalu kak buat semuanya, semoga pinternya nular kak hehehe !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini murah senyum, baik juga, lembut juga, keren sih bisa ada di bagian senator",  
                "pesan":"semoga diperlancar semuanya kedepannya kakk, semoga kerennya nular !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KohoHTbYquNSGCCQPfs2eDQi8H53UOlo",
            "https://drive.google.com/uc?export=view&id=1G4CdowX_q2UC1TPsS0YKtKBdYI2g5y_2",
            "https://drive.google.com/uc?export=view&id=1OiA0xT4iCVH4t1Pj24G1zD0-QfBkBrQI",
            "https://drive.google.com/uc?export=view&id=1q4R65CKSkLke6vstZqPMXMepaRD38TCF",
            "https://drive.google.com/uc?export=view&id=1BCdAm9jaYYimO-f0Yx33sUQQwJYQYsIs",
            "https://drive.google.com/uc?export=view&id=1u5ffcipq3FrUgCWUykYsUPug4MfHZsOt",
            "https://drive.google.com/uc?export=view&id=18afZ76SxjCSqUDsIe48pxryR4bT3cztu",
            "https://drive.google.com/uc?export=view&id=1j7PSt5xbinia055e7brvpvQsHk61mkOX",
            "https://drive.google.com/uc?export=view&id=1oXHSOUePLJTbTAhHAnUiOvY7Ykm1F3ut",
            "https://drive.google.com/uc?export=view&id=1z-V-IG6G5MZt4JC8HnOEnKDalcqD8UPp",
            "https://drive.google.com/uc?export=view&id=17CCvYW4n-NoPrjCEI62Dk8tzGVaJruJt",
            "https://drive.google.com/uc?export=view&id=1BVxiI_Vx1YYPx9EvzZ2or1wJTHvYjJMT",
            "https://drive.google.com/uc?export=view&id=1QeLWxFQJFVCp-1cXM6zfLmzNfN-VqDVk",
            "https://drive.google.com/uc?export=view&id=1mvGkDy7XWbG4WYg_uq9MD9Gc9BRYUV8r",
            "https://drive.google.com/uc?export=view&id=1aY7d22Dsycc9b8SvAuMS6nWSs9_oUReR",
            "https://drive.google.com/uc?export=view&id=1H1RXuOfl6U633o2iEIbIxFDtRKf7U88g",
            "https://drive.google.com/uc?export=view&id=1aol44S1QG6ElESllSSdHpo5fq2TVJ4mY",
            "https://drive.google.com/uc?export=view&id=1PfnJluUmusVjDABMNGkZ3sgIIR4yrw_-",
            "https://drive.google.com/uc?export=view&id=1CiWqXcUBxwuiwk9rpqntMtBo38JhuHJN",
            "https://drive.google.com/uc?export=view&id=1_ey3bG_a_jmlhQ9pOYbTBtM7fGCRiWr2",
            "https://drive.google.com/uc?export=view&id=1zRwsNr1Zg23nPIRr_a3tr2dLScv6hTPm",
            "https://drive.google.com/uc?export=view&id=17-Lfs5jYkFQfHs5pMngyKe30dDClNFq7",
            "https://drive.google.com/uc?export=view&id=1s-iJFadMuWWbqpWMkiSOI9wQxalV4I_z",
            "https://drive.google.com/uc?export=view&id=162OeebIpQg6AaoncvnDEB3pyDdGKaYYR",
            "https://drive.google.com/uc?export=view&id=1SNPRlgc_28x58Y6xeuQX7Evp8rjyHYTN",
            "https://drive.google.com/uc?export=view&id=14SAxXsJPLegl6sWcmGr2dBy3vhOll-i2",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Tanjung senang",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "bang jujur saya takut karena serem, tapi aslinyasuka ngejokes kayanya difg, dan baik",
                "pesan": "semoga dipermudah kedepannya bang hingga lulus, sukses bang"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "jujur kak saya takut liat kakak, karena serem dan tatapannya tajam, cantik kak tapi, tapi agak serem aja",
                "pesan": "semangat kak, lancar terus dan sukses"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "kak alya baik banget, tapi saya juga takut kak kalo ketemu gitu",
                "pesan": "kak terimakasih telah mengajarkan banyak ilmu, sukses ya kak menjalani semster hampir akhir ini, semangat kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "wajahnya buku filsafat dan politik sekali, serem juga,tapi baik dan murah senyum",
                "pesan": "semangat merintis karir dan jadi orang hebat bang, sukses selalu bang, semoga semangatnya menular"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "kak suka banget liat makeup nya, cantik, tapi kakak jutek, jujur saya takut juga karena serem",
                "pesan": "terimakasih kak telah memberikan dan mengajarkan banyak ilmu yang gaada dikelas,sukses kak"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "jujur saya takut bang, karena gondrong, dan kadang tatapannya tajam sekali bang, tapi abang murah senyum kalau disapa",
                "pesan": "terimakasih bang telah memberikan dan mengajarkan banyak ilmu, sukses selalu bang"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "baik abangnya, tapi serem juga kadang, tapi suka nyapa juga kadang",
                "pesan": "semangat bang, semangat berkarya, sukses bang, terimakasih juga ilmu ilmunya"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "kak cantik banget jujur, tapi kadang cuek juga, kadang ramah juga kok tapi, pintar",
                "pesan": "kak terimakasih telah mengajarkan banyak hal, semoga pintar dan cantiknya nular, semangat selalu dan sukses kakk"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "bang maaf ya bang jujur takut liat bang nobel karena alisnya tebal dan tatapannya tajam sekali, jago ngoding, pintar juga, baik",
                "pesan": "semangat dan sukses selalu merintis karir bang, maaf ya bang kalau saya di kelompok ale kurang maksimal, terimakasih ilmu-ilmunya bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "bang takut juga saya kalau ketemu, karena sedikit seram, tapi baik, asprak ads, pintar, kadang jutek",
                "pesan": "terimakasih bang ilmu ilmunya, terimakasih juga selalu mengingatkan kepada tuhan, sukses bang"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakak baik kok, tapi kadang jutek juga, saya kadang takut, cantik juga, pintar",
                "pesan": "kak terimakasih telah merawat waktu saya jatoh, terimakasih ilmu ilmunya kak, sukses dan semangatt kakk"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "baik, ramah, atlet bangett",
                "pesan": "semangat bang, semoga dari hobi yang keren bisa menjujung karir abang juga,sukses"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "pendiam, baik, ramah, suka senyum",
                "pesan": "bang kita btw satu SMA dulunya, semangat bang ali, sukses bang"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "kakak cantik dan lucu, suka pakai rok pendek",
                "pesan": "kakak semangat, semoga cantik dan lucunya nular kak hehe"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakak baik, suka senyum, tapi kadang jutek sih kak hehe ",
                "pesan": "kakk semangat menjalani hidup sekarang dan kedepannya ya kakk, sukses kakk"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kakak baik, menolong aku waktu jatuh dan gaenak badan dikelas, gorgeous",
                "pesan": "terimakasih kak sudah dirawat waktu itu, sukses yaaa kakkk"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "asik, baik, ramah, dan suka ketawa",
                "pesan": "bang semangat meraih cita-cita yang disemogakan, sukses bang"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "baik, murah senyum, ramah juga ketemu di bazar ",
                "pesan": " maaf bang kalau sainsfest kurang maksimal, semangat berkarya dan berkembang selalu bang, semoga semuanya dipermudah "
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "baik, tapi jujur saya takut bang, karena terkadang tatapannya yang sangat tajam, tapi setiap disapa selalu ramah dan menyelipkan senyuman",
                "pesan": "bang terimakasih telah mengajarkan ilmu diluar kelas, sukses selalu bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "kakaknya cantik, lucu,hobinya unik sama kaya orangnya ",
                "pesan": "kakk semangat ya buat kedepannya,semoga apa yang dicita-citakan terkabul, semoga ngoleksi lebih banyak pita pita lagi"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnya humoris, kocak, suka ketawa, kayanya iseng banget orangnya",
                "pesan": "semoga kocak terus bang, lancar lucur sampai tamattt"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "yaa Allah bang tinggi sekali, basketable, tapi serem sih bang jujur sedikit takut, maaf ya bang",
                "pesan": "lancarrr luncurrr sampe tamat bangg"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "kakaknya kecik lucu hehe, rambutnya sih bagus banget bisa gitu, cantik, murah senyum, tariable",
                "pesan": "semangattt buat kedepannya kakkkk, sukses selalu di sini dan dimanapun"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "abangnya kocak juga, suka ngejokes, suka mirip miripin saya hehehe",
                "pesan": "banggg, sukses selalu, semoga yang disemogakan tersemogakan"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "bang benget operator yang dikerjain bang jeremia susanto waktu itu, ternyata asik, tapi agak menyeramkan, tapi seru, pelatih semua olahraga banget",
                "pesan": "semoga sukses dari hobinya dan dari kuliahnya kita di sains data ini, semangat bangg"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "kakaknya kalem, lemah lembut sekali, baik, ramah",
                "pesan": "kakk semangat yaaa, semoga lancar dipermudah semuanya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TE-Vs7a8rZ_zTbmUOxlbO8lq7eIpf_0-",
            "https://drive.google.com/uc?export=view&id=1B0BjWT4AXG9d8tcsm0k4usya1foNvCiT",
            "https://drive.google.com/uc?export=view&id=1viCYtVOP3Le9LdSW4y7gyy1ljvjfX9mp",
            "https://drive.google.com/uc?export=view&id=1_4Zz28-RAdXhYnOkdETTquFMcut2BVMo",
            "https://drive.google.com/uc?export=view&id=1oFOiAAwFdZF8B5uOlbjDx2lF5R7bnF8Q",
            "https://drive.google.com/uc?export=view&id=1XKCMaOw9g2vhNEzBAP5DKkGVJwJ9jMlu",
            "https://drive.google.com/uc?export=view&id=1DBCvMllpttKD0a34MYzkFhPXjkPwkKL1",
            "https://drive.google.com/uc?export=view&id=1plGT_2akCiR1UYmM_iAZx9bmf6gKkANe",
            "https://drive.google.com/uc?export=view&id=1qu_if80bzovACZbMBW_W6vyASKEoAJS8",
            "https://drive.google.com/uc?export=view&id=1jyxklL87phACnY4XT3XXhPN2hYENgsOW",
            "https://drive.google.com/uc?export=view&id=11t4Lxq6qc4J0y31VMFZSshClPKOTsmzN",
            "https://drive.google.com/uc?export=view&id=1p3sCJE7aK2VoMNMfax21-THoUfQZ5bSV",
            "https://drive.google.com/uc?export=view&id=1TpUQiuF9n-zJOIhY4L_bLPLvafsPYeTE",
            "https://drive.google.com/uc?export=view&id=19BTI3MRnbQgqz2wMg8_HBNZkDgFg1PwE",
            "https://drive.google.com/uc?export=view&id=14tD_xHHb6SdDvDN4rxFBurKEIxv7ueXh",
            "https://drive.google.com/uc?export=view&id=194xLHpVbB5HG3R5bxE04dyUiXDPqBrPu",
            "https://drive.google.com/uc?export=view&id=1UYJqQOE1M4kvqcTN60YcsAt2j1uL42Vt",
            "https://drive.google.com/uc?export=view&id=1p8RFPJeO3pXSE1gdGLhnSkN1_WNi4FfT",
            "https://drive.google.com/uc?export=view&id=1L5lrw2x1h_GoOd5H7-tPxa83tIWKRw14",
            "https://drive.google.com/uc?export=view&id=199Ev9K5a9rJG1iijJhnuqsLfR-_gabuE",
            "https://drive.google.com/uc?export=view&id=1DLKMBIjEdiDidr7n08_9eW5HEDH95KAZ",
            "https://drive.google.com/uc?export=view&id=15f4whRSwDFQ0plomG6N0YgKolrkiqcxd",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "keren banget banggg, tinggi banget, baik, ramah, murah senyum ",
                "pesan": "semangattt menghadapi semester akhir, semoga dipermudah semuanya, aamiin!!!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "cantik sekali, ramah juga, dan murah senyum ",
                "pesan": "semangat terus kuliahnya kakkk, semangat menghadapi semuanya, sukses !!!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "abangnya asik, suka ketawa juga, nular ketawanya ",
                "pesan": "semangattt banggg disemester akhir inii, sukses bang !!!"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "MasyaAllah cantik banget, kalem, alim, pinter ",
                "pesan": "semangat terus kuliahnya kakk, semangat berkarya, dan semoga cantik dan pintarnya menular !!!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "abangnya lucu, humoris, kalo ketawa nular juga ini bang ",
                "pesan": "semangatt membangun karya dan merintis karir sejak dini bangg, sukses bang!!!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "tinggi banget, humoris ",
                "pesan": "semangattt bangg, semoga yang dicita citakan terkabul !!!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "keren bangg rambutnya bisa gitu, baik, ramah ",
                "pesan": "semangattt bangg, semoga menjadi data scientist atau analys atau engginer !!!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "kakkk cantik banget, namanya bagus hehehe ",
                "pesan": "semangattt selalu kak, walaupun dunia kadang tidak berpihak di kita !!!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "cantikkkk bangetttt, lucuuu, unik, fresh teruss ",
                "pesan": "semangat kakakkk, semoga yang disemogakan tersemogakan !!!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "pendiam, kalem, baikk ",
                "pesan": "semangatt banggg, semoga jadi data enggineer !!!"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakk baik banget, cantikkk, ngedance banget, waktu itu bantuin ngurut kaki saya abis jatoh, so freeshh setiap hari, on point ",
                "pesan": "semangat terus kakkkk, terimakasih telah dibantuu, semangat selalu menjalani hobi, suksess!!!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "cantik tapi judes kak maaf ya, baik kok tapi kak ",
                "pesan": "semangatt kakk semoga jadi data analys !!!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "kakaknya lucuu, kalem, dan pendiam ",
                "pesan": "semangat terus kuliahnya kakkk, sukses kakk !!!"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kak fai cantik sekali MasyaAllah, pintar, baik, murah senyum ",
                "pesan": "semangat terus kuliahnya kakk, semoga  cantiknya nular  ya kakk !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "tegas, sedikit judes saya sedikit takut kak, tapi is oke kak kakak asik kok ",
                "pesan": "semangattt buat di semester yang hampir akhir ini kak !!!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "murah senyum, ramah juga, tinggi juga ",
                "pesan": "semangatt bang di semester akhir ini, semoga lelah menjadi lillah !!!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "berani, suka pake bintang di hijab, ladass ",
                "pesan": "semangatt berkarya kakakkkk ladasss !!!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "jujur awal tau kalo nim nya sama agak minder, karena bang fabio pintar, hehe keren banget bangg, 104 gang ",
                "pesan": "semangattt berkaryaaa terusss banggg, semoga nantinya bisa bekerja sama dengan baik apabila ada kesempatan !!!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "kalem, pintar, ozt, suaranya kecik bang hehehe, baik, dan ramah ",
                "pesan": "semangattt selalu bangg, semoga nular pintarnya aamiin !!!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "kakaknya baik, cantik, suka senyum juga, asik ",
                "pesan": "semangatt kakakkkk, semoga kedepannya semua dilancarkan sampai lulus, sampai dapat kerja !!!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "kakakk nya kalem, tinggi, manis ",
                "pesan": "semangat kakk, semoga cita-citanya terkabulkan !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "abangnya tinggi, kacamata dan unik ",
                "pesan": "semangat terus bangg, semoga next menjadi data enggineer !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ix2-0mMm_8hpUYE7yyNmc4vuNz46y6xB",
            "https://drive.google.com/uc?export=view&id=1SahADw1TUMhQu-u9QUTyzYFd2wf5R6Cl",
            "https://drive.google.com/uc?export=view&id=1mhfpU5gD8LQyoleAfDZUcsTi1Qei6Nn6",
            "https://drive.google.com/uc?export=view&id=1yBpVpVe0LW2hc1XoabUB1nZdo9GNZuhT",
            "https://drive.google.com/uc?export=view&id=1fm8B5JbHY7FKxTqojPOuyEM8jJY0vmsU",
            "https://drive.google.com/uc?export=view&id=1sb9eeYoSAYN1SWwDESpAXsyhbwNiRj8T",
            "https://drive.google.com/uc?export=view&id=1EvqhfcI8CgD5sh-ntehcXw099pwnnSHl",
            "https://drive.google.com/uc?export=view&id=1tNxGMOLoC2T00Gh-m__IJAyoSxjd072m",
            "https://drive.google.com/uc?export=view&id=1J_cOxkiFwisrLtz15Cha2-POZ0Wabmw3",
            "https://drive.google.com/uc?export=view&id=1kYw8auaYOcCKLRQqQXxWMuy9xmDioUbm",
            "https://drive.google.com/uc?export=view&id=1yY3Q_EgLSz9d9kjDTbixi1_DPDrXjGDD",
            "https://drive.google.com/uc?export=view&id=1WrLfKhZ7oOd6nFcb35NFfKydcqEeJUxd",
            "https://drive.google.com/uc?export=view&id=1Jqx1Nxyk0HfYot9b4iP8Zv6IGB6bUhD6",
            "https://drive.google.com/uc?export=view&id=1FyCa9ishMv4lP2c7LDiLFJrejT9m6nUO",
            "https://drive.google.com/uc?export=view&id=1eM3XjlH0FOHibE0GR8iE9XoN3bDebzJJ",
            "https://drive.google.com/uc?export=view&id=1NfsXtXBfEjndP4NgEmkyQuQ26coQ2x3e",
            "https://drive.google.com/uc?export=view&id=1O4v1EzpkJQuBivU1WexjjGlWFCoPPfbo",
            "https://drive.google.com/uc?export=view&id=1hPKEvphRLPM-hwGYvkw-hoKj7AfLOGEG",
            "https://drive.google.com/uc?export=view&id=1Un-r8iSfV9PZI0nSOUVi1sGUAPegEaQ4",
            "https://drive.google.com/uc?export=view&id=1Dt8h56kXMJ3vOqCpS2BkDc1x-wEbSZ7b",
            "https://drive.google.com/uc?export=view&id=1toqpN4k713cYZUzJqr7BRSzd3Xrmq6uK",
            "https://drive.google.com/uc?export=view&id=163-8Ti2O75QNq0ISwOnR0-ozsfui-dwW",
            "https://drive.google.com/uc?export=view&id=1R3VyOUua4Jw2l8iIkoKJMTyIukEq0XOv",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "abang ini lucu karena kacamatanya hehehe, tinggi   ",
                "pesan": "semangat bangg, bentar lagi lulus bang hehehe, sukses ya bangg !!!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kakak nya cantik banget, suka liatnya",
                "pesan": "semangat terus kuliahnya ya kak, semoga diperlancar segalanya !!!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "cantik banget, on point terus, suka lihatnya",
                "pesan": "semangatt ya kakk, semoga cantiknya, on point nya nular kakk !!!"
            },
           {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "tegas banget, asik, ramah, suka senyum juga, satu divisi sainsfest",
                "pesan": "semangat berkarya terus kakk arini, sukses ya kakk !!!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "baik abangnya, ga sombong dan ga judes",
                "pesan": "semoga segala sesuatunya kedepan dipermudah bangg, semangattt !!!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kakak cantik banget, lucu, tapi sedikit judes, kadang saya takut kak, takut saya salah sikap",
                "pesan": "semangat kak kuliahnya, semoga menjadi data analys / scientist !!!"
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "cantik, baik kakaknya, suka senyum",
                "pesan": "semangattt kakkk untuk sisa sisa semester tengah dan menuju akhir !!!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "kakakkk lucuuu, cantik, dan asikk",
                "pesan": "semangattt yaaa kakk, semoga semua perjalanan jadi keberhasilan !!!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "kelas banget ketuplak sainsfest, kece abis, kocak, waktu itu tau pertama waktu verbek",
                "pesan": "semangat terus berkarir banggg, infokan closingan sainsfest bang untuk anak data !!!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "kakak on point  selalu, manis, suka lihatnya",
                "pesan": "semangat terus kakkk, semoga  rintangan jadi kesuksesan !!!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "kakkk cantikkk bangettt, lucuu, wangii, bagus rambutnya, suka makeup nya, ceriaa banget",
                "pesan": "semangat terus kuliahnya kakkk, semoga lolos sampai grand finalll aamiin !!!"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "ramah banget, suka nyapa, energi nya ada terus, baik bangettt",
                "pesan": "semangatt kakkkk, semoga suksesss till finish !!!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "suka iseng, sedikit tengil, baik, suka nyapa",
                "pesan": "semangatt bangg, semoga sukses seterusnya !!!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "kakkk tinggi banget, energinya banyak bangett, ceria, baik, ramah",
                "pesan": "semangattt yaaa kakkk, yang terbaik buat kak sonyaaa !!!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "kakaknya gemoi,chubby,cantik, gatau seger aja liat kakaknya",
                "pesan": "semoga cantik dan chubby nya nular!!!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "bang, agak serem yaa, baik sih tapi ",
                "pesan": "jangan serem-serem bang hehehe, sukses selalu bang!!!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "aduhh terbaik lah ini, nyalinya besar, ternyata sama sama dulu mau ngejar fk, baik pollll ",
                "pesan": "bangggg semoga beraninya nular ke saya huhuhu, semoga bang adit sukses dan segalanya dipermudah !!!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "salfok sama hobinya, baik banget, cantikk lah jelass namanya aja kakak cantik, lemah lembut ",
                "pesan": "semangattt kakak cantikkk, lancar luncur mulus !!!"
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "ceriaaa banget pembawaannya kakk sukaa energinya nular ",
                "pesan": "gaspolll sampai s.si.d kakkk !!!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "owww oww cantik dan attractive banget ",
                "pesan": "semangat till finish kakkk !!!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "murahh senyum, baik, dan ramah ",
                "pesan": "sukses kak sampaii lulus&kerjanya !!!"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakaknya pendiam, kalem hehehe ",
                "pesan": "leggo s.si.d !!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "sering dibilang mirip kawan saya bang, tapi menurut saya ngga mirip ",
                "pesan": "semangat bangg, semangat till s.si.d !!!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "saya liat pendiam, ternyata asikkk bangettt kalau lagi ngobrol ",
                "pesan": "semangattt kakk, ayo kita ngobrol bersama kakak cantik dan bang adit !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1r2iYjXo2AAZI93Rgvy8O2IqUp3fpbjI7",
            "https://drive.google.com/uc?export=view&id=1RmSvlWHpdIvZCmTe16CVXb3WNg_hOVUj",
            "https://drive.google.com/uc?export=view&id=195L9zj8GY6jtv7C3MH9DfP1ciBDJLUia",
            "https://drive.google.com/uc?export=view&id=1NEuVKQtdl5DS_b-8TKbVAqPDujWQ2SFr",
            "https://drive.google.com/uc?export=view&id=1et4lyRvv4QsWgN_cKIwR2gfi39_2KmfR",
            "https://drive.google.com/uc?export=view&id=17Mhjx3zUBXsSjndX1e2ueKzMRO0n1fKR",
            "https://drive.google.com/uc?export=view&id=1Z4PbEUwG0zWlS-Mj9qgloJrJvzeY5Npg",
            "https://drive.google.com/uc?export=view&id=1h8-xuMf-s1V2fUNhgzvuvjSD0CgqvgEr",
            "https://drive.google.com/uc?export=view&id=1FcnOZrsAZNPubK_25ZRow5rShXhQgr6p",
            "https://drive.google.com/uc?export=view&id=1xx4dDaoyDfBtqxliXnqMg9BNRq_YRTE7",
            "https://drive.google.com/uc?export=view&id=1Cl76b53Xfa3LFVqlu4AcDMIySZXilab6",
            "https://drive.google.com/uc?export=view&id=10NrtsAbmLUM-RXXEzN9vk90mVFTFD330",
            "https://drive.google.com/uc?export=view&id=1K_TkwNUATsqTo3Rzb18M1jmfwjXex9Nq",
            "https://drive.google.com/uc?export=view&id=1Bhu-_aIXIXfmr39M1xVofjJouGlEj8mj",
            "https://drive.google.com/uc?export=view&id=1QLveRSLLruQOz9mB58qnFGJFBq25H4ZX",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "kakak baik, cantik kadep lagi ",  
                "pesan": "semangat terus kakkk !!!" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "maaf kak kirain kami kakak cowo, but is ok, sosorry kak",  
                "pesan": "semangattt kakakkk !!!" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "kakaknya cantikkk ",  
                "pesan": "semangat terus kakk !!!" # 3
            },
            {
                "nama": "Rendy",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "tau bang rendi dari grand opening,kirain muslim bang maaf ",  
                "pesan": "sukses bangg!!!" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "kakakkk ramah, cantikk, murah senyum",  
                "pesan": "semoga segala urusan dipermudah kakk till finish !!!" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "jujur agak takut bang, karena gondrong dan alisya tebal hehehe, cuek kadang ",  
                "pesan": "semangat selalu bangg !!!" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "kakaknyaa baikk, murah senyum ",  
                "pesan": "semogaaaa lancar mulus !!!" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "kakak aslinya baik dan ramah tapi judes banget saya kadang takut ",  
                "pesan": "jangan judes banget ya kak hehe, sukses kk !!!" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "danusannn hihihii ",  
                "pesan": "semangat banggggg !!!" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "abangnya asik banget ",  
                "pesan": "semangat jaya jaya jaya !!!" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "kakk hana baik bangett, asikkk bangetttt, sainsfest bareng hehehe ",  
                "pesan": "kakkk semoga energinya banyak terusss !!!" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "kakakkkk cantikkkkk, pintarrrr ",  
                "pesan": "semangat kakakkkk !!!" # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "asli keren parah abang ini wah ",  
                "pesan": "sukses bangggg !!!" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "ihh hobinyaaa bikin iriiii,cantik seperti orangnya ",  
                "pesan": "bikin tutor gitar wanita dong kak !!!" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "asikk banget kakaknya ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18cN0B5e2mamsGZm3TFG1hJFrpQKBvjpm",
            "https://drive.google.com/uc?export=view&id=16sh51G7KcaV-lyBzdBllRoMAfmZZCEfv",
            "https://drive.google.com/uc?export=view&id=1Vm382B8Fdws_FpwrGUcnIRYvVdzs5KbV",
            "https://drive.google.com/uc?export=view&id=1hYgvkf40_3GkD2Mt8AzKKljP-KPvyCfi",
            "https://drive.google.com/uc?export=view&id=1v5syCLhZsD3-bA1HnkVuL4YsuDDBBAut",
            "https://drive.google.com/uc?export=view&id=1c7oakLqJBn_2isMn9_ePiO6oqUyF8RHg",
            "https://drive.google.com/uc?export=view&id=1alrLIPVjxtngHL-fYq2Y0uZVjXjEUESz",
            "https://drive.google.com/uc?export=view&id=1PptKvrjfrJXbJdYy39emHuZmGI8XDWbC",
            "https://drive.google.com/uc?export=view&id=18hBnqEp1-DUb8es5TfXJZV8jr930Z68K",
            "https://drive.google.com/uc?export=view&id=1Sr-wfREMZ1MnsoyTOO2m9LKzNkCY2ayV",
            "https://drive.google.com/uc?export=view&id=1t6RZwLXsCvR7urPV0KmS5weRMtNIFnV7",
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
                "kesan": "abang kerennnn, famous, p2mw,pkm, cerebral ",
                "pesan": "semogaa kerennya nular bang, semangat berkarya bangg !!!"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "kakakkk cantikkk dan pendiam sedikit ",
                "pesan": "semangat kakkk till finish !!!"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "kadivv yang oke jugaa ini ",
                "pesan": "semangat berkarya banggg!!!"   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "kakaknya  palembang banget, huhuhu, ga heran sih",
                "pesan": "leggom till s.si.d kakkk !!!"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "kakak asik banget yang saya lihat ",
                "pesan": "semangat kakakkk !!!"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "kak nabila lumayan tinggi juga yaaa ",
                "pesan": "sukses kakkkk !!!"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abang kadiv kewirausahaan yang oke abis ",
                "pesan": "semangat ngurus wirausaha dan kegiatan kelas bangg !!!"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "kakaknya baik, pendiam yang saya lihat ",
                "pesan": "semangatt kakk di semester hampir akhir !!!"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "kakakk cantik sekaliii, baik dan ramah ",
                "pesan": "kakak semoga cantik dan ramahnya nular hehehe !!!"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kakak baik banget, asik juga ",
                "pesan": "semangattt selalu kakakkkk !!!"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "cantik, ramah, pintar ",
                "pesan": "semoga nular pintarnya kak, sukses kak !!!"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qBegarmUiH3SwGlxS_RDy5VoqtGyK2RI",
            "https://drive.google.com/uc?export=view&id=1mD1rogWGENzEdtLovZOzS2DSwwdTcwM8",
            "https://drive.google.com/uc?export=view&id=1fYQto3dRzKxiQdAt6AAarw1nIvKv9gDy",
            "https://drive.google.com/uc?export=view&id=1V9rPs07Twvqs22IPUXowW1MzjSVToqyS",
            "https://drive.google.com/uc?export=view&id=1eHGsjnW0o7QPEIKIdfbbHiOWaKFGRT6R",
            "https://drive.google.com/uc?export=view&id=179A83HRUJZxBaTNLl5aokPmAILI4BZdc",
            "https://drive.google.com/uc?export=view&id=1YLdo3bGbAcuDdRMLvcfgJWut-akGxg1W",
            "https://drive.google.com/uc?export=view&id=19loH3FLBM3T1vUI3CBIBMX1idZa-LP-l",
            "https://drive.google.com/uc?export=view&id=1fG01vIulPbSbpnMH8h4Y-rXqGh7nP1Rq",
            "https://drive.google.com/uc?export=view&id=1jZaTPqezFw3RpXv-jd0O1E3z6inKLUeb",
            "https://drive.google.com/uc?export=view&id=1QTDOEE8lDtI94hUZ4kvbSN9UXT_be1si",
            "https://drive.google.com/uc?export=view&id=1mPtZ9b6uuYmwaF_pQvjjf1V0Ky2HvcK3",
            "https://drive.google.com/uc?export=view&id=1KmV5-SHWo1kQScTDh1vCfKYmi83FlPzH",
            "https://drive.google.com/uc?export=view&id=119lN3ife2vIzdTqDAYglCOUIz1CnV368",
            "https://drive.google.com/uc?export=view&id=1BiqDUICd1GdoOgHtgm2Cm5r4ApLppEN4",
            "https://drive.google.com/uc?export=view&id=1jx76Zud9E78g4pIAj_9awosf653zpFep",
            "https://drive.google.com/uc?export=view&id=1pt8BhpZAK419T6UJqoKII5wK5l1Bn4E4",
            "https://drive.google.com/uc?export=view&id=1eg-WpJfD9IjD2XOfoIJK-f4ZqOn7OA",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "cantikkk polll, lucuuuu, ceria bangettt, baik banget, kak, aku juga gemes banget sama kakak lucu, asprak ads terlucuuuu ",
                "pesan": "kaaa ciaaaa semangattt sampaiiiii s.si.d, ihhh suksessss kakkk ciaaaa cantik !!!"   # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "baikkkk bangettttt, ramahhh, murah senyum, kakaknya makeup nya bisa bagus banget plisss ",
                "pesan": "leggoooo till s.si.d kakkk semangattt kakakkkkk !!!"   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "suaranya kecik, baik juga ",
                "pesan": "semangat semester akhir bang !!!"   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "jujur liat bang labo dokum banget, namanya panjang banget ",
                "pesan": "lancar lancar sampai lulus bang  !!!"   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "iseng ya kadang, kocak sih, kadang bikin ketawa, baik baik, nice ",
                "pesan": "semangattt abang nim awallll, sampai s.si.d !!!"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "oh wawww cantik bangettt, baik poll, ramah juga, kating kedua yang saya tau waktu verbek, hobinya sama lagi ",
                "pesan": "ayo hunting gelang gelang lucu, semangat kak walau harus denger mirrorball wkwkwk,sukses ya kakk !!!"   # 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "aduh on point dan flawless banget makeupnya sukak ",
                "pesan": "sepertinya harus membuat tutorial makeup !!!"   # 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "kakakk ini cantik bangett, ga ngebosenin, baik, ramah ",
                "pesan": "semoga cantiknya nular kak !!!"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "ramah,murah senyum juga,cantik ",
                "pesan": "asik banget jadi mc, sukses ya kak !!!"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "awal kirajudes gitu taunya ngga, bahkan suka senyum dan ramah hehehe ",
                "pesan": "semangat kakk untuk semester sisanya !!!"   # 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kakaknya pendiam deh, konten bangett sih tapi hehehe ",
                "pesan": "semangat kakak kuliah sampai tamatnyaaaa !!!"   # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "kakk cantikk banget, lucuuu ",
                "pesan": "semangaattt selalu yaaa kakak lucu !!!"   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "kakaknya sedikit judes, tapi aslinya baik dan ramah ",
                "pesan": "semangattt sampai selesai kakkk !!!"   # 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "abangnya lucu,suaranya kecik tapi hehehe,baik dan ramah ",
                "pesan": "suksess selalu bangggg !!!"   # 14
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "oww murah senyum sekaliii, cantik dan ramahh ",
                "pesan": "against the world till s.si.d kakk, semangat di semester menuju akhir !!!"   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "kakk style hijabnya bagus bagus, lucuk ",
                "pesan": "bolehlah kak buat tutorial supaya hijabnya rapih dan bagus xixixi, sukses kakkk !!!"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "kakakkk cantikkk, baik dan fresh banget bawaannya ",
                "pesan": "semoga energinya ada terus kakk untuk melukis dan mewarnai dunia !!!"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "kakkk jujur bagus banget rambutnyaa keriting sosis, kakaknya ceria dan cantik,jadi makin makin ",
                "pesan": "ihh semogaa ceria dan energi positifnya nular kakkk, sumpah jangan potong rambut dulu kakk !!!"   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()











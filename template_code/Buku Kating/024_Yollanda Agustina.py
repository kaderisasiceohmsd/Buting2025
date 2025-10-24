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
            "https://drive.google.com/uc?export=view&id=12-zWqVw-da9-z5rTCVJZHnnbylBCDwXj",
            "https://drive.google.com/uc?export=view&id=14qfg--fpt7AYw2tTvKTqjna5Vc2NSxPh",
            "https://drive.google.com/uc?export=view&id=1LFQzeK2I1WHqfpNh1NRhRRcurA1_C7u6",
            "https://drive.google.com/uc?export=view&id=1lyEyif-Aulb6BZ4NrveP0JIpfwBmuF3M",
            "https://drive.google.com/uc?export=view&id=1qK_uIrVpKrjFx2C2Ol748zvnILGqH5KF",
            "https://drive.google.com/uc?export=view&id=1hLs5fqj4PpnA3CocOLSQsMd-uvP74Eck",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Pulau Damar",
                "sosmed": "@_rendraa",
                "kesan": "Auranya memancar sampai ujung siantar",  
                "pesan":"Semangat bang, jan sampe unfoll ya bang!!!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerangi",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Asik abangnya, Humble banget ",  
                "pesan":"Bang pengen nanya berapa jam tidurnya sehari!!!"
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "Asik klo diajak ngobrol bisa lanjut ngalir gitu aja!",
                "pesan": "Kak bagi tips boleh buat lewatin semester ini?"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya keliatan tenang banget ya padahal semester akhir gitu",
                "pesan": "Kak bagi tips biar tetep enang hati dan pikiran dong, jujur lagi berantakan banget!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Vibe happy everytime everywhere nya dapet banget kak!",
                "pesan": "Kak aku ga suka kucing tapi ada 12 kucing dirumahku, mau ga?"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Dorrr!, ditembak hatiku sama senyum manis kakak hehe",
                "pesan": "pengen belajar domino kak, item item bulet bulet merah merah tapi bukan gaple kan ya kak?"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1OXTS6n9pPRt8tr6zOyiYhZz1k66D6jvd",
            "https://drive.google.com/uc?export=view&id=10-jLVkDibNgwabcMhItsvW5OTltyKOh8",
            "https://drive.google.com/uc?export=view&id=18V245Wd9kq3ZeqC_T_LxOwHEzh5V4MBM",
            "https://drive.google.com/uc?export=view&id=112dZMEc1bwkvUfHMspwYxtLjyw5_Z6Q1",
            "https://drive.google.com/uc?export=view&id=1hLs5fqj4PpnA3CocOLSQsMd-uvP74Eck",
            "https://drive.google.com/uc?export=view&id=1jVBRoHT1_NbmUJ08HaI8_vqBfqj-E868,
            "https://drive.google.com/uc?export=view&id=1TUO6HTmS3t9Pot9YMskuJ3VuORWDfG3f",
            "https://drive.google.com/uc?export=view&id=1sqmOqxlPsxbUk6tvd_CSgLkkirz-Vug3",
            "https://drive.google.com/uc?export=view&id=1r3d4zFynOtEbWfrr8YPbMrX-at8UAol8",
            "https://drive.google.com/uc?export=view&id=1TUO6HTmS3t9Pot9YMskuJ3VuORWDfG3f",
            "https://drive.google.com/uc?export=view&id=1TUO6HTmS3t9Pot9YMskuJ3VuORWDfG3f",
            "https://drive.google.com/uc?export=view&id=1TUO6HTmS3t9Pot9YMskuJ3VuORWDfG3f",
            "https://drive.google.com/uc?export=view&id=1rLip4QtsrbITF0ZCaj7BpNGI6D7e9m36",
            "https://drive.google.com/uc?export=view&id=1RvMsVbNwEy0EvGDfq_JLL_1yWS13z_Er",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Tanjung Merawa",
                "hobbi": "Suka main voli sama Feby",
                "sosmed": "@jeremia_s_",
                "kesan": "kaya angkatan 25,awet muda!",
                "pesan": "Bang temenku ada yang pernah kecinaan sama abang"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "jujur aku terintimidasi sama kakak pas awal, nih kakak senyumnya susah banget digapai",
                "pesan": "kak ajari aku cara jadi serius kak, dikit dikit aku ngejokes pengen belajar serius disituasi yang sesuai."
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Suka banget sama gaya kakak, santai, nyaman tapi keren, apalagi rambutnya mauuuuuu",
                "pesan": "Kak aku hobi mancing cuma jarang diajak mancing, ayok kak mancing di embung F siapa tau dapat kadal emas!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "khas anak balam sekali",
                "pesan": "bola bowling sama galon le mineral lebih berat yang mana ya kak?"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "bang senyum dong, minus senyum klo lagi ketemu tapi aslinya baik banget fast respon lagi",
                "pesan": "Bang bagi tips nyuci baju tanpa dikucek tanpa mesin cuci sabun yang bagus dan bersih apaan ya?"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "suka kak warna rambutnya, kaya jad cantik, strong , imut jadi satu",
                "pesan": "imuuut banget kak, tips warnain rambut biar ga jadi blonde setelah 2 minggu kak? "
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "senyumnya adem bang kaya ac f008 jam 16.00",
                "pesan": "Bang kkN apa kabar?"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "soft spoken ya bang, tenang adem ayem gitu",
                "pesan": "infokan seblak paling gacor sebalam kak!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "kak, cantiknya kakak tuh sesuatu tawww, kaya yang berani dan berenergi gitu",
                "pesan": "Kak kedu warna ga sebagus itu tapi enak banget buat main temen sekelas, banyak umang umangnya!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "cubby cubby imoet, imut imut gini duta yg jago public speacking tuh keren banget kak!",
                "pesan": "dengerin plave kak hehe"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "kerenlah gaya abang ini, aura mengayomi dan kebapak-annya kuat sekali bang",
                "pesan": "makasih bang udh fast respon dan bikin santai ga tegang berinteraksi sama abangnya"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Bang ih kocak banget, jokesnya bapak-bapak banget wkwkwk",
                "pesan": "bang pendengar yang baik kah?"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "kalem, adem ayem gitu deh kak auranya berpikiran dewasa",
                "pesan": "kak kalau diisengin trs, bisa ditarik iket aja ga ya orangnya pake franco"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "kak ceria banget setiap saat, unik banget namanya",
                "pesan": "Arti namanya apa tuh kak? BTW nyap angin dijam 1 malem deket tol kta baru asik tau kk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


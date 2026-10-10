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
            "https://drive.google.com/uc?export=view&id=import streamlit as st
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
            "https://drive.google.com/uc?export=view&id=1gGm6nSYvYBu3QZe8d1O7JLD8n_Haabme",
            "https://drive.google.com/uc?export=view&id=1kqurzlqC6Q_QmQ8ek21tDYdx7L-xiI16",
            "https://drive.google.com/uc?export=view&id=1CSd15o2mxPqu0TrYsgg3ykoksJr3jHih",
            "https://drive.google.com/uc?export=view&id=18yT19HVveO-OP4MSHtanUVSlyOgJynYL",
            "https://drive.google.com/uc?export=view&id=1EIFsl_atXK2t6hj-U-BIDKJPwiLpydDl",
            "https://drive.google.com/uc?export=view&id=1MebTkSJMzpE2eqVAaqyUm4SrY5Oe3vOf",
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
                "kesan": "keren dan humble ",  
                "pesan":"semangat kuliahnya bang semoga lulus sarjana Sains Data tepat waktu luluss bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "asik banget dan selalu tampil keren",  
                "pesan":"semangat ya bang mengejar sarjana Sains Data"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "selalu tampil ceria dan asik",  
                "pesan":"semoga lancar terus kak kuliahnya"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "baik dan kalem",  
                "pesan":"semangat terus ya kak"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "asik dan ramah",  
                "pesan":"semangat menjalani perkuliahannya kak"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "humble dan ramah",  
                "pesan":"semoga di beri kemudahan dalam segala urusan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EDPNXKC87_mU4DCsoy1FmUNwIRYTqV5M",
            "https://drive.google.com/uc?export=view&id=1R2Jvh8R2MEdVAmdiHJ6G7LZzHsprLT08",
            "https://drive.google.com/uc?export=view&id=1W6c1qDc8zy87LtVhZAbhuXXTNax6kQdU",
            "https://drive.google.com/uc?export=view&id=1MLA9Up5IN5eKf-6EQFRQxO2y1xpcv7Ox",
            "https://drive.google.com/uc?export=view&id=11NtYPrEuZUc9iUL21IzUE3m4Hl4iw9EY",
            "https://drive.google.com/uc?export=view&id=1QG3LJg5SZJsINBTkqgaoKoAY976n-LFt",
            "https://drive.google.com/uc?export=view&id=1yDBYG3dFI8_ZgoMHeTU4ec1QBLGEP2f-",
            "https://drive.google.com/uc?export=view&id=1N6xvKMoNBnHQWdKRIlyHjGHnAECs_I4i",
            "https://drive.google.com/uc?export=view&id=1ueCGH3Pig8RL-qWBXmphIddCwfkOHYbq",
            "https://drive.google.com/uc?export=view&id=10XBDE-nQ5B4JN_abw7evcMW7ME-2dINy",
            "https://drive.google.com/uc?export=view&id=13hLdmlkD56TMEz0f93IW5l8TWTpd5oeh",
            "https://drive.google.com/uc?export=view&id=1TOCcLRCvX3It2XQ2XrcIAlmiIYSD1px4",
            "https://drive.google.com/uc?export=view&id=1Pqyp1r1GM7xFYmW2EnKtoxiorVcTRSiV",
            "https://drive.google.com/uc?export=view&id=1QG3LJg5SZJsINBTkqgaoKoAY976n-LFt",
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
                "kesan": "keren dan kece",  
                "pesan":"semoga lulus tepat waktu bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Kakaknya asik dan baik bangett",  
                "pesan":"semangat terus kak kuliah dan menjalani harinya"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "seru dan humble",  
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "baik dan asik",  
                "pesan":"semoga menjadi sarjanan tepat waktu kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "humble dan seru banget",  
                "pesan":"semoga terus mendapatkan yang terbaik bang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "baik dan seru",  
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "asik dan baik",  
                "pesan":"semangat bang kuliahnya"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "kece dan seru",  
                "pesan":"semoga kuliahnya mendapatkan yang terbaik bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "asik dan humble",  
                "pesan":"semangat terus kak menjalani harinya"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "seru dan baik",  
                "pesan":"semoga kuliahnya berjalan lancar kak"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "asik dan baik",  
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "keren dan baik",  
                "pesan":"semoga kuliahnya lancar bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "-",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "baik dan seru",  
                "pesan":"semangat bang kuliahnya"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "seru dan humble",  
                "pesan":"semangat menjalani harinya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Qv5dBAjgiv0MI0UY3Hd_puGj5NmUTaMQ",
            "https://drive.google.com/uc?export=view&id=1phJZWW-kw7LU8-LuIu5Wfy7GX53Tdh2V",
            "https://drive.google.com/uc?export=view&id=1JFAhxImP4pZYIe-3VgqRUeHMPQbjWduh",
            "https://drive.google.com/uc?export=view&id=1-6dZ9UAGoP7TdaSyoLeZ6EbGZ8qGA-kG",
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
                "kesan": "keren bisa mewakili suara sains data ",  
                "pesan":"semangat bang kuliahnya"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "asik dan seru",  
                "pesan":"semoga dimudahkan urusan kuliahnya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "humble dan baik banget",  
                "pesan":"semoga lulus tepat waktu kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "seru dan humble",  
                "pesan":"semangat terus kak menjalani kuliahnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZfhDfGqt8hTf7E6f87MF-Ct0xFikplli",
            "https://drive.google.com/uc?export=view&id=1PpLoAEESpgzI6cNRmv3VOLi5cuaREGCY",
            "https://drive.google.com/uc?export=view&id=12kdzxPy_ZJUFSyhfSrqvuVxlrtbfyPmu",
            "https://drive.google.com/uc?export=view&id=1LpEoqBkai4YP50o9EHOl8Pyjqietz-js",
            "https://drive.google.com/uc?export=view&id=1EBydbQQ69UTjH0dmEW5lrbaBdqMqHyng",
            "https://drive.google.com/uc?export=view&id=1sfsbILcErbaKr3xusapkSo0v5h2ZuMkD",
            "https://drive.google.com/uc?export=view&id=1hHXqU0q0pyfV8hq3xwWLPbEcDIcq5-5E",
            "https://drive.google.com/uc?export=view&id=1Lt6hCIp13Q61a8uJOhfYWfPG7kEZiMY5",
            "https://drive.google.com/uc?export=view&id=17RtqXpWrcaXD6GLUUPiEERkFjJ9hy9lb",
            "https://drive.google.com/uc?export=view&id=18ofotg_14MS2fQBGZuckN71uV-H3Z1Ng",
            "https://drive.google.com/uc?export=view&id=1STessYCIdOdI_MmyRQHNLbnKGibVY4iN",
            "https://drive.google.com/uc?export=view&id=1UQQJDbRQMnDA9y6h6pM2bmXeMNJ0xDWu",
            "https://drive.google.com/uc?export=view&id=1UPRjiErZbQmN7NQii2IE-llL7yQD2Ivh",
            "https://drive.google.com/uc?export=view&id=1BIBvgFcyhM5vWTLWfwTIq6CjAlNE7Gul",
            "https://drive.google.com/uc?export=view&id=1WNt2YsuslRIw9KU-T8gq91x3GcNFOQCj",
            "https://drive.google.com/uc?export=view&id=1leRTQhTRgAOxwNWKG8Yk2PTFC_e3YJSv",
            "https://drive.google.com/uc?export=view&id=1wBOzAUVC7CAC1BsDXI35vb-vxNvDruhD",
            "https://drive.google.com/uc?export=view&id=1UONWIaB0ER5M5aVbqTdc6nGBfkDgwMUt",
            "https://drive.google.com/uc?export=view&id=1tm99RlAnMyy3Lj7t_5s9TbbP1_iLxqP-",
            "https://drive.google.com/uc?export=view&id=10qcLZrbCOpNbMw_vTL7_1nL5A5f2u-d1",
            "https://drive.google.com/uc?export=view&id=1NCCz1ZLEI9JTDuQlPNMZPV3gFXhvAVl9",
            "https://drive.google.com/uc?export=view&id=1rnPThUAtyzuGLucEcKycYJVgJKydz255",
            "https://drive.google.com/uc?export=view&id=1Z2Wv4VLvLM02JVpCUIHws3KhXlVlCu-w",
            "https://drive.google.com/uc?export=view&id=1gseE0F5Af_JIbCzZegMtIB_GQKMflZ9G",
            "https://drive.google.com/uc?export=view&id=1mY_I0cVHxRmT9MMkSwVxtlfconTydl_F",
            "https://drive.google.com/uc?export=view&id=1V0BtjdbkRlWF0qYwd5nqWgWuIg_02aUC",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "keren dan kece banget",
                "pesan": "semangat bang mengejar gelar sarjana"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "baik banget dan ramah",
                "pesan": "sehat selalu ya kakk"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "tegas tapi baik bangett",
                "pesan": "jaga kesehatan terus ya kakk"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "orangnya chill tapi tegas, jadi panutan banget di tiap rapat.",
                "pesan": "Jangan lupa istirahat, Bang! Dunia kerja nungguin semangatmu yang nggak ada habisnya."
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "selalu bawain vibes positif, tiap kumpul rasanya adem.",
                "pesan": "Terus jadi sumber semangat buat orang-orang sekitar ya, Kak"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "paling bisa bikin suasana rame walau lagi stres",
                "pesan": "Jangan lupa istirahat, Bang"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "paling cepat tanggap kalau ada yang butuh bantuan.",
                "pesan": "keren banget waktu handle acara, tegas tapi tetap asik."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "super teliti, semua kerjaan selalu rapi dan on point.",
                "pesan": "Semoga semua target Kakak tercapai dan makin sukses di karier nanti"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "suka becanda tapi pas kerja tetep profesional banget.",
                "pesan": "Semoga abang bisa terus jaga semangat itu di dunia kerja nanti"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "paling bisa ngasih solusi kalau lagi stuck.",
                "pesan": "Terus jadi problem solver andalan ya, Bang"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "super sabar, bahkan kalau situasi lagi chaos pun tetap tenang",
                "pesan": "Semoga kesabaran Kak jadi kekuatan besar di masa depan"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "punya dedikasi tinggi, nggak pernah setengah-setengah kalau kerja.",
                "pesan": "Jangan lupa santai juga, Bang"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "baik banget",
                "pesan": "jangan lupa istirahat, Bang"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "selalu perhatian sama adik-adik, bikin suasana jadi hangat",
                "pesan": "Semoga semua kebaikan Kak dibalas berkali lipat"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak punya suara lembut tapi penuh makna setiap ngomong.",
                "pesan": "Terus jadi pembawa ketenangan ya, Kak"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "selalu tampil elegan dan sopan, tapi tetap humble.",
                "pesan": "Semoga Kakak selalu dikelilingi orang baik seperti Kakak sendiri."
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "jago banget ngomong di depan umum, keren banget",
                "pesan": "Cocok banget jadi pembicara atau dosen nanti, Bang"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "punya gaya kepemimpinan yang ngademin.",
                "pesan": "Terus pimpin dengan hati ya, Bang"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "selalu bisa diandalkan kalau urusan teknis.",
                "pesan": "Semoga Bang terus sukses dan ilmunya makin tinggi"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "tampilannya tenang, tapi kalau ngomong, langsung bikin fokus.",
                "pesan": "-Terus jadi yang berwibawa tapi tetap hangat ya kak"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "punya pemikiran logis banget, cocok jadi data analyst sejati.",
                "pesan": "Semoga Bang makin bersinar di dunia data"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "selalu punya solusi meski lagi panik.",
                "pesan": "Tetap jadi sosok tenang di tengah kekacauan, Bang"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "selalu jadi orang yang paling perhatian soal detail kecil.",
                "pesan": "Dunia data cocok banget buat Kakak"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "punya hobi aneh tapi seru, bikin ngobrol nggak pernah garing.",
                "pesan": "Terus jadi yang autentik dan apa adanya ya bang"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "paling bisa ngatur tim biar tetap kompak.",
                "pesan": "jangan lupa iistirahat ya bang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "paling semangat pas acara sosial, hatinya lembut banget.",
                "pesan": "Terus tebar kebaikanmu ke mana pun melangkah, Kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XOn6lUD_X-2_f0xzwNNxCxfK8mvrdbEb",
            "https://drive.google.com/uc?export=view&id=16Dkj7Pb5I6OeSbuJYUIhWEHNM0X9FEfc",
            "https://drive.google.com/uc?export=view&id=1OTCI6n45jYBclIcPi_btPLVIBv2oaJAD",
            "https://drive.google.com/uc?export=view&id=1fAGC_R6LWmqVWhLbtpfQcw0fkk_us-pm",
            "https://drive.google.com/uc?export=view&id=1dmzlcSkRL4OC9_RAP_PNa6kYb7fnOPcl",
            "https://drive.google.com/uc?export=view&id=1qzcQiKnB2krJKI1wc0E6vMsEPc6H_6fc",
            "https://drive.google.com/uc?export=view&id=1LhdeJFO1EAh3S8DV_QRIJy0XoFmBjJ-6",
            "https://drive.google.com/uc?export=view&id=1wiXDb1ud5khA2KlBM1cu71bpJXOSqDb-",
            "https://drive.google.com/uc?export=view&id=1uhMGSkHLYlNHOF8Y4q0fGfD3xOT7sbHw",
            "https://drive.google.com/uc?export=view&id=1P2sX1JQEwSQJWLiXZsb-_TtZpH5pI4vM",
            "https://drive.google.com/uc?export=view&id=1hdUgYhOfte8Ie4c-HBdIdf8Jv0iAK0UY",
            "https://drive.google.com/uc?export=view&id=1MKs9s0qmvrW92JiKuOkiIV_xSM_gxLF3",
            "https://drive.google.com/uc?export=view&id=1cwiLBTlQ5zUOEMKibzNFloRMdd_8EbUu",
            "https://drive.google.com/uc?export=view&id=1EJUboiDmna6q25IPU304juOMXaE0IjMo",
            "https://drive.google.com/uc?export=view&id=1DxIYexrYUSkckSgozMMpe-g3PXHK7kiU",
            "https://drive.google.com/uc?export=view&id=1W3LcEjmABL3s5wKWE8IyGR3LWgpiL9ZP",
            "https://drive.google.com/uc?export=view&id=1-2jwnXUvHQtEJPVLwOlW77sbSji_3EzE",
            "https://drive.google.com/uc?export=view&id=1H_gb5tDqw41NK_p2t0l-DX_R7iqWmmec",
            "https://drive.google.com/uc?export=view&id=1y7_NVbYqa68jmLwPHicpUwrsmXAVl4Rg",
            "https://drive.google.com/uc?export=view&id=1B3sAsJL7qujuFZAEyFc2Lt_M2pf7xau3",
            "https://drive.google.com/uc?export=view&id=1kanYNPTIGR3fHMuXKDFkWI_QTRon4Yli",
            "https://drive.google.com/uc?export=view&id=1vSbe6zICWCAh6-WnexksiaBSjZQhkIvl",
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
                "kesan": "keren banget abangnya ",
                "pesan": "semangat bang kuliahnya"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "baik banget",
                "pesan": "semoga kuliahnya lancar kak"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "kece banget",
                "pesan": "semangat bang mengejar gelar sarjananya"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "ramah bangat ",
                "pesan": "semangat kak menjalani hari harinya"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "humble dan kece ",
                "pesan": "semangat bang kuliahnya"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "keren dan baik",
                "pesan": "semoga kuliahnya lancar bang"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "kece dan ramah ",
                "pesan": "semangat bang kuliahnya"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "baik dan ramah ",
                "pesan": "jangan lupa istirahat kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "humble dan baik",
                "pesan": "semoga hari harinya lancar kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "keren dan baik",
                "pesan": "semangat bang kuliahnya"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "baik dan humble",
                "pesan": "semangat kak menjalani harinya"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "ramah dan humble ",
                "pesan": "semoga kuliahnya lancar kak"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "baik dan ramah ",
                "pesan": "semangat kak kuliahnya"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "humble dan baik",
                "pesan": "jangan lupa istirahat kak"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "keliatannya rajin ",
                "pesan": "semangat kak kuliahnya"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "keren dan baik banget ",
                "pesan": "semoga kuliahnya lancar bang"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "humble dan ramah banget ",
                "pesan": "semangat kak kuliahnya"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "kece dan ramah ",
                "pesan": "semangat bang ngejalanin hari harinya"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "keren dan baik ",
                "pesan": "semoga kuliahnya lancar bang"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "baik dan ramah",
                "pesan": "semangat kak kuliahnya"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "humble dan baik ",
                "pesan": "semangat ngejalanin hari harinya kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren dan baik",
                "pesan": "jangan lupa istirahat bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=186UHnNrj943NlsxMUSrP1NzLmvpqL_wx",
            "https://drive.google.com/uc?export=view&id=1gk_DffX_Chq0oJmp4jKkGnkCmfqPIqQt",
            "https://drive.google.com/uc?export=view&id=150y3mm75LvyrTYZJzVbydcMiyQWUP1gB",
            "https://drive.google.com/uc?export=view&id=1x8zTdLzssgdcYTPC3LHbWxBEIyCHEZeW",
            "https://drive.google.com/uc?export=view&id=1q2tW-Immc25ia0MLfBwMD-af1IdJP5ND",
            "https://drive.google.com/uc?export=view&id=13ewDgyEFwTkgO8Jyk7qNpXKK15DIxyoX",
            "https://drive.google.com/uc?export=view&id=1rklxf0_POC3mRHS6Iqre8lf5WY_Fcc7E",
            "https://drive.google.com/uc?export=view&id=1fbkIYlKKeD_OUFk7AThj07vJeDaIVCQv",
            "https://drive.google.com/uc?export=view&id=1hMKtdOHmoIEbeq8s9CM2luxokSriB4rQ",
            "https://drive.google.com/uc?export=view&id=1eL8_a-166F3KSiubKCum9iT5pTw0e4dw",
            "https://drive.google.com/uc?export=view&id=199JtN1uL3g6bn-W-dHG6sGeGzMX1L5pJ",
            "https://drive.google.com/uc?export=view&id=1hqJ_7_KQfhAWbfUOvUFSCy1uOwaRcN0_",
            "https://drive.google.com/uc?export=view&id=1QlxQz-CO5U9vXXX5hHj_AtFlLdJuxgO5",
            "https://drive.google.com/uc?export=view&id=1ugv3JJYi87BtGp9nJJUQM1Z_VzzdK8I9",
            "https://drive.google.com/uc?export=view&id=1eoDGnn9Vga_4PnzwqFCH141dyVw1xiMU",
            "https://drive.google.com/uc?export=view&id=1f-ixucn57LmlfSvLV70AuH3FYqtm7-c4",
            "https://drive.google.com/uc?export=view&id=1To3cP3M6cQxaAy_OOhD04dy9WZ0Cdqz4",
            "https://drive.google.com/uc?export=view&id=1TIChiIh-oturNdmcSmzWb9hj1iaiKeiT",
            "https://drive.google.com/uc?export=view&id=1GTxXF29tGo5zJiG1v4cjbZtidHAcKWRj",
            "https://drive.google.com/uc?export=view&id=1YtHm65UUsOabA7juqGYv3I6a_F3SL_ay",
            "https://drive.google.com/uc?export=view&id=1yrpvvK4wi0Vb4_b-dVWGpLd0wTNvv9mz",
            "https://drive.google.com/uc?export=view&id=1CrQ4MlALFCgYZ5KwMZU7yYel7vkFxvxr",
            "https://drive.google.com/uc?export=view&id=1AiJ_8sIoDNHxK1Zd2pEyequ7kiDSccdq",
            "https://drive.google.com/uc?export=view&id=1C6kOxCOLg_uauzGpg6WYoM3oR0hrpoSD",
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
                "kesan": "Bang punya gaya bicara yang santai tapi profesional.",
                "pesan": "Pertahankan karakter itu, Bang, keren banget"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak paling sigap kalau ada event kolaborasi antar himpunan.",
                "pesan": "Semoga Kak terus aktif dan semangat membangun koneksi"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "selalu punya cara halus buat ngatur suasana biar tetap kondusif.",
                "pesan": "jangan lupa istirahat kak"
            },
           {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "gampang akrab sama siapa aja.",
                "pesan": "Terus jaga keramahan itu ya, Kak"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "paling bisa ngomong formal tapi nggak kaku.",
                "pesan": "Semoga Bang terus sukses jadi jembatan kolaborasi di mana pun nanti"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "punya aura elegan yang bikin semua nyaman diajak kerja sama.",
                "pesan": "Terus jaga attitude keren itu ya, Kak, inspiratif banget"
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "nggak cuma aktif, tapi juga perhatian sama tim.",
                "pesan": "Terima kasih Kak, sudah selalu jaga suasana kerja tetap solid"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "selalu peka terhadap situasi",
                "pesan": "Sikap itu mahal banget, Kak, pertahankan"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "selalu tahu cara nge-handle partner",
                "pesan": "semangat bang mengejar sarjananya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "selalu tampil dengan senyum",
                "pesan": "Senyum Kakak bikin suasana jadi lebih ramah dan terbuka"
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "punya gaya ngomong yang sopan banget, tapi tetap hangat.",
                "pesan": "Terus jadi wajah ramah HMSD ya, Kak"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "punya kemampuan komunikasi yang super smooth.",
                "pesan": "Cocok banget Kak kerja di bidang public relations nanti"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "selalu punya inisiatif tinggi tanpa harus disuruh.",
                "pesan": "Terus pertahankan jiwa tanggung jawab itu ya, Bang"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "nggak pernah ngeluh walau harus standby sampai malam buat acara eksternal.",
                "pesan": "Terima kasih Kak, dedikasimu luar biasa banget"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "punya cara elegan",
                "pesan": "Skill diplomasi Kak emang top banget, pertahankan ya"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "nggak pernah ngeluh walau kegiatan Pengmas capek banget.",
                "pesan": "Semoga semangat pengabdiannya nggak pernah padam, Bang!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "keren,baik sangat lah abang ini terbaik pokoknya no debat",
                "pesan": "erus jaga semangat sosialnya ya, Bang."
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kakak cantik,punya hati yang lembut, selalu mikirin dampak kegiatan ke warga.",
                "pesan": "Terus jadi Kakak yang penuh empati dan kasih, ya"
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "peka banget sama keadaan sekitar, hal kecil aja diperhatiin.",
                "pesan": "Dunia butuh lebih banyak orang kayak Kakak"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "selalu bawa suasana hangat tiap kali ke pertemuan",
                "pesan": "Tetap jadi pembawa keceriaan buat masyarakat, Kak"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "pinter banget nyusun rencana kegiatan sosial yang berdampak. ",
                "pesan": "Semoga Kakak makin sukses bikin perubahan nyata di masyarakat"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "punya cara lucu tapi efektif ",
                "pesan": "Kreativitas Kak bikin suasana jadi hangat dan seru, teruskan ya"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "nggak cuma ngomong, tapi langsung turun tangan kalau dibutuhkan. ",
                "pesan": "Bang emang definisi “aksi nyata,” keren banget"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "selalu kreatif bikin kegiatan Pengmas lebih menyenangkan.",
                "pesan": "Ide-ide Kak selalu bikin kegiatan berkesan, terus berkarya ya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bMfe5CXNCBe_LlRBJRyRF8O--uzlDhGE",
            "https://drive.google.com/uc?export=view&id=1qSnWpZ-5A_B1W1ABa8E7VWBclOHSpkKq",
            "https://drive.google.com/uc?export=view&id=1JLTkIRm6l_VqYjDpEUBakO_kRdI7JwiY",
            "https://drive.google.com/uc?export=view&id=1f00wfny0Tktmoa_DY3LdmdrAZ8xXjSSP",
            "https://drive.google.com/uc?export=view&id=1joM76S4kGGZcExfXNYbauVwIxk2hiSg4",
            "https://drive.google.com/uc?export=view&id=1V1LFIXmLJKLvt2wNQdrLJCyrP0NOuBAS",
            "https://drive.google.com/uc?export=view&id=11WAfBXMe8yudyqx4f2bQl0nnLJZuqPx8",
            "https://drive.google.com/uc?export=view&id=1T7dlZ5av9ri6FWLUZk2bwvHbJSOcT2az",
            "https://drive.google.com/uc?export=view&id=1M0g6PWBa5fzTvi9lK7as8kMNqbwYNu4x",
            "https://drive.google.com/uc?export=view&id=1VwM97Wd_G5twIBCB7stf9bEHKr-fnWXD",
            "https://drive.google.com/uc?export=view&id=19dEneP0BaFGL8Y6wlrlmd7O81QBr7DYb",
            "https://drive.google.com/uc?export=view&id=1cpRGlZNCXj4T0kHEV3u8Bu3mw58OXeEL",
            "https://drive.google.com/uc?export=view&id=1J3t1OnU6abwmQyZuqUQp-EyZO7T9V_lq",
            "https://drive.google.com/uc?export=view&id=10Ax4eB1w7PaEwPmGhnkgs489llMfC4R1",
            "https://drive.google.com/uc?export=view&id=1v2AxvPTd3hUfJ6_R9CH7povNDWN5E8Y2",
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
                "kesan": "humble banget ",  
                "pesan": "semangat kak mengejar gelar sarjananya" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "kalem banget ",  
                "pesan": "semangat kak kuliahnya kak" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "baik dan humble ",  
                "pesan": "semangat kak menjalani harinya" # 3
            },
            {
                "nama": "Rendi Alexander hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "baik dan kalem ",  
                "pesan": "semangat bang kuliahnya" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "lucu dan asik banget ",  
                "pesan": "sehat selalu kak" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "keren banget ",  
                "pesan": "semangat bang kuliahnya" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "baik banget",  
                "pesan": "sehat selalu kak" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "keliatan tegas tapi baik",  
                "pesan": "semangat mengejar gelar sarjananya kak" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "kelatan agamis banget ",  
                "pesan": "semangat bang kuliahnya" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "baik banget ",  
                "pesan": "semangat terus ya bang" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "seru bangett dan humble juga ",  
                "pesan": "semangat kakak kuliahnyaa" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "asik dan baik ",  
                "pesan": "semangat kak menjalani harinya" # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "baik dan vibesnya positif ",  
                "pesan": "semoga sehat selalu bang" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "baik dan seru bangett ",  
                "pesan": "semangat terus kak menjalani perkuliahannya" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "ramah dan baik banget ",  
                "pesan": "semoga sehat selalu ya kak" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yO6kPTe-QwZxhZwzFIClgAJrzgfNHt1i",
            "https://drive.google.com/uc?export=view&id=1sqsndwNOwYsQ5WeiivB3paVblH0iEmQW",
            "https://drive.google.com/uc?export=view&id=1aLnw-r1kvpCTJOsYONkEDYmXzE0U5ras",
            "https://drive.google.com/uc?export=view&id=1ZuhZn98KRxEq637yFP8MEVnZOExtYtFl",
            "https://drive.google.com/uc?export=view&id=1DhpWjOKL6ss25NXdaLJCjElJf1S9c0VX",
            "https://drive.google.com/uc?export=view&id=1T0lWKGTGkxrq5Mkl6fhDB1G1iGiCVWud",
            "https://drive.google.com/uc?export=view&id=1FrhZTjITbfWaBwrGPeGDX-kHgeKJ2enr",
            "https://drive.google.com/uc?export=view&id=1L62GgTdgDPvq531iwdq7W_1hDFrGcadi",
            "https://drive.google.com/uc?export=view&id=1n6QNvqtsi2UpAM_dKxBJ3MprY-KOI7u9",
            "https://drive.google.com/uc?export=view&id=1PehGNwwprNf2DrlkxdeZSRpCKmiBTW1E",
            "https://drive.google.com/uc?export=view&id=1dAmsjhAtsvLaAXSxXjPXBn9SSCG1FplW",
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
                "kesan": "asik banget dan baik juga ",
                "pesan": "semangat terus ya bang menjalani hari harinya"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "baik dan humble",
                "pesan": "semangat kak kuliahya"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "keren dan seru ",
                "pesan": "semangat terus bang kuliahnya"   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "baik dan humble ",
                "pesan": "sehat selalu ya kak"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "asik dan ramah ",
                "pesan": "semoga kuliahnya lancar ya kak"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "baik dan humble banget ",
                "pesan": "semangat kak menjalani hari harinya"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "keren dan baik banget",
                "pesan": "semoga kuliahnya lancar ya bang"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "baik dan lucu ",
                "pesan": "sehat selalu ya kak"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "baik dan humble banget ",
                "pesan": "semangat kak menjalani hari harinya"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "asik dan lucu bangett ",
                "pesan": "semangat kak kuliahnya semoga lancar ya"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "baik dan ramah banget ",
                "pesan": "semoga kuliahnya lancar ya kak"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-u-Fi3uUoDpuPrzqlbiD7byNieDsbod4",
            "https://drive.google.com/uc?export=view&id=1H6v1V_pogwC47XGqog-5wceDL3GPF2nB",
            "https://drive.google.com/uc?export=view&id=17rfjjLM8cAQSlxQc-eJCkUbjKEflg9du",
            "https://drive.google.com/uc?export=view&id=1wTVWLiQm0MXsAQsfR2V99Dk9AJFCMq7W",
            "https://drive.google.com/uc?export=view&id=10nmisMuJ-l84iCbi4jv6lwrhXU6tC9mL",
            "https://drive.google.com/uc?export=view&id=1H5V548BAc_sY2H4rUJKV8sbcST_Eg3Sx",
            "https://drive.google.com/uc?export=view&id=1YJYyEsV5iIOlUDEsbmSVRXUuZD1MsoY1",
            "https://drive.google.com/uc?export=view&id=17keDL1NP8MZB24gacO5kb0WCOsUTRcEq",
            "https://drive.google.com/uc?export=view&id=1xisXJbYKK47LKghebZ9ZHJaoCZQj4H4w",
            "https://drive.google.com/uc?export=view&id=1A2-8nYv8NUdu7CJ-TmxL3kggDY3Y9cFO",
            "https://drive.google.com/uc?export=view&id=1knaeEuYjs3Xi4G762KQ0HGytdZixp2Ox",
            "https://drive.google.com/uc?export=view&id=1asGIcLVXwPkbUgPhNoraSnZMk265uYS7",
            "https://drive.google.com/uc?export=view&id=1wj7wiD633Pq2tDQEi2bb0dWH5hdL6PEP",
            "https://drive.google.com/uc?export=view&id=11aHLsdu8AUVMz1iF26NlMFCYaFY8RH79",
            "https://drive.google.com/uc?export=view&id=11lHNEw_D2K_igqxIQHEfiFMpfEfxPFU3",
            "https://drive.google.com/uc?export=view&id=1Is-mgQtRIMMb0WDPkwCQso6oHokO7LmG",
            "https://drive.google.com/uc?export=view&id=1QuT1DmTwIVTZw5wEq5HTem84v1ZCTDyE",
            "https://drive.google.com/uc?export=view&id=15WZw86UsxocuwoPTtOUoNQEDALKD3Ira",
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
                "kesan": "paling semangat dan baik banget ",
                "pesan": "semangat teruss kak menjalani harinya"   # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "baik dan ramah ",
                "pesan": "sehat selalu ya kak"   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "kalem dan baik ",
                "pesan": "semangat terus ya bang"   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "kece dan keren ",
                "pesan": "semangat bang kuliahnya"   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "baik dan ramah banget ",
                "pesan": "semoga lancar ya bang kuliahnya"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "baik dan asik ",
                "pesan": "semangat ya kak kuliahnya"   # 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "ramah dan baik ",
                "pesan": "sehat selalu ya kak"   # 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "sangat ramah dan welcome ",
                "pesan": "semoga kuliahnya lancar ya kak"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "baik dan sangat humble",
                "pesan": "semangat terus kak menjalani harinyaa"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "asik dan baik banget",
                "pesan": "semoga kuliahnya lancar ya kak"   # 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "humble dan ramah banget",
                "pesan": "sehat terus ya kak"   # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "baik dan selalu ceria ",
                "pesan": "semangat terus kak kuliahnyaa"   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "asik dan humble ",
                "pesan": "semoga kuliahnya lancar ya kak"   # 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "keren dan baik banget ",
                "pesan": "sehat selalu ya bang"   # 14
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "baik dan ramah ",
                "pesan": "semoga kuliahnya lancar kak"   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "ceria dan ramah ",
                "pesan": "sehat selalu kak"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "baik dan humble ",
                "pesan": "semangat ya kak kuliahnyaa"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "baik dan asik ",
                "pesan": "semangat kak menjalani harinya"   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()",
            "https://drive.google.com/uc?export=view&id=1A1OYuEaT6nPdQOio3CRqJdRAIJtssDOr",
            "https://drive.google.com/uc?export=view&id=1ItKBpWYdf5iCK1cRwh5Q2o7gn0Yc8O8C",
            "https://drive.google.com/uc?export=view&id=1AC1x8bstyUDbjIUbe0MR1iKtIf26jget",
            "https://drive.google.com/uc?export=view&id=1Q9RbVufERlvB2IpJYe2LZZUt7kC8S13r",
            "https://drive.google.com/uc?export=view&id=1vbAsWXChQy38bTd5-DyfoFCa2p6b2r_b",
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
                "kesan": "Abang ketua himpunan yang ramah, asik dan memberikan kesan yang sangat profesional",  
                "pesan":"Sukses selalu bang dan semoga bisa menginspirasi banyak orang untuk menjadi pemimpin yang lebih baik"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "Abangnya kocak seru dan berdwibawa",  
                "pesan":"Semangat terus kuliahnya bang Jo, tutorin biar jago basket kaya abang dong bang"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak nya friendly dan murah senyum",  
                "pesan":"Semangat terus ya kak kuliahnya"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya baik dan murah senyum",  
                "pesan":"Semangat terus kuliahnya ya kak, kejer apa yang kakak inginkan"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak nya asik, pas jadi pemateri kader juga kakaknya seru",  
                "pesan":"Semangat terus dan tetep asik ya kak"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak nya baik dan ramah",  
                "pesan":"Semangat kuliahnya dan ngatur keuangannya ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iY2cS2x3c71jdjYhlTpYLDewp8ao4ill",
            "https://drive.google.com/uc?export=view&id=18CsByv9HOcPi1NiVYmKn7LLmWUPzIAvJ",
            "https://drive.google.com/uc?export=view&id=13DxKx_NIS-nyKi9AWSto7CWYQXG_74aM",
            "https://drive.google.com/uc?export=view&id=1p97tMvaM4ErgWag56hv6D6KjtlFCdXGF",
            "https://drive.google.com/uc?export=view&id=1RocBlM5jayuOozCQVWPzfyfWyWaFsWjQ",
            "https://drive.google.com/uc?export=view&id=1DCWf1f5NZ-vI8WDecG_PyDTG-PKgUY6n",
            "https://drive.google.com/uc?export=view&id=1hqNFGkm82kspGCEnXXg4KuVnCn5cfATj",
            "https://drive.google.com/uc?export=view&id=1tPqMOUt-jG_4WNUsfr_BKf51Ue6sOPcZ",
            "https://drive.google.com/uc?export=view&id=151fDGwHSYcngzeXaeqMXHH_nfID9fVF9",
            "https://drive.google.com/uc?export=view&id=1Tg_lw3zBsCQ7eIt__K1TMIrN610PohLk",
            "https://drive.google.com/uc?export=view&id=1S5G-NF-cetk0KSshPAnAx9129FAbX-sv",
            "https://drive.google.com/uc?export=view&id=1QkuZb-tpQ9WMZ9wuGXp47nulQKQEJuWm",
            "https://drive.google.com/uc?export=view&id=1oEOsh8ZFGm9Gh1b3iu4oYu_d1CbPwDBr",
            "https://drive.google.com/uc?export=view&id=1GMLoUyR3dnF2wiE_UK-1gRyeqV6ufK8a",
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
                "kesan": "Bang Jeremia punya aura tenang dan berwibawa. ",  
                "pesan":"Semangat terus bang, semoga semua urusannya lancar!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Kak Dhea sepertinya ramah dan gampang diajak kerja sama.",  
                "pesan":"Semoga selalu semangat dan kompak terus ya kak!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Dari yang aku lihat, kak Renisha orangnya supel dan ceria.",  
                "pesan":"Semoga makin sukses dan tetap rendah hati ya kak!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Kesan pertamaku, kak Anisa terlihat tegas tapi santai.",  
                "pesan":"Semoga makin lancar kuliahnya kak!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "Bang Dharu punya vibe kalem tapi fokus.",  
                "pesan":"Semangat terus bang, semoga makin berkembang!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Kak Feby menurutku rajin dan tanggung jawab.",  
                "pesan":"Semoga terus semangat dan makin keren ya kak!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro terlihat santai tapi sigap kalau dibutuhkan.",  
                "pesan":"Terus semangat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan dari kesan pertama terlihat tenang dan bisa diandalkan.",  
                "pesan":"Semoga semua kegiatannya lancar terus bang!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kak Berliana sepertinya rapi dan profesional.",  
                "pesan":"Semoga makin sukses di organisasi dan kuliah ya kak!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "Kak Juesi punya aura ceria dan ramah.",  
                "pesan":"Semoga terus jadi pribadi yang positif kak!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho terlihat aktif dan semangatnya tinggi.",  
                "pesan":"Semoga makin banyak hal keren yang dicapai bang!"# 1
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Bang Feryadi punya pembawaan santai tapi perhatian.",  
                "pesan":"Semoga terus sukses dan tetap rendah hati bang!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica terkesan teratur dan sigap.",  
                "pesan":"Semoga makin banyak hal baik datang ke kakak!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fakfak",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa dari kesan pertama terlihat ceria dan lucu.",  
                "pesan":"Semoga makin percaya diri dan terus berkembang kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vOSfyR9dzsLIWRYdtBk22WILV1zMDQvo",
            "https://drive.google.com/uc?export=view&id=1SbbnbKjW4seEwMG0OVcom7NPwrG81sAZ",
            "https://drive.google.com/uc?export=view&id=1j5E6XlO6xZXC_Wiuc8fH6T1eaHjWelVN",
            "https://drive.google.com/uc?export=view&id=1fXa3zUE0T3D_v9Urig0SPWkhJa3daFQ0",
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
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LfDDY90zoaPI9Nqn8QUQEMVu3hgVXm7r",
            "https://drive.google.com/uc?export=view&id=1CYg-TbDoyK5pLTc7nu6fM-yW0SZfYEP5",
            "https://drive.google.com/uc?export=view&id=17W6hceilKPp2oMSDnizvDCV3MB-cWNfg",
            "https://drive.google.com/uc?export=view&id=1w2gf1ezEDAxwDP2fWJ7zEkwObXmGK26P",
            "https://drive.google.com/uc?export=view&id=1L6nNWzjmMlvjEi6zPmXOCKiGl2d8hnys",
            "https://drive.google.com/uc?export=view&id=14IuR1fc7dj-88heOMKfhpY_wUs5Oubwr",
            "https://drive.google.com/uc?export=view&id=187AGte6KmXT6WadX905ZTDCMoWdlwQvm",
            "https://drive.google.com/uc?export=view&id=1APPVc2_aphEzzzMePDksvoRP1BbMyzQ7",
            "https://drive.google.com/uc?export=view&id=1hYJmQWPtEvB0_vN1-dVJd_zT_8xaX07_",
            "https://drive.google.com/uc?export=view&id=1q9iQTsXWFVq7K4rHHeIq43E-9A1EzXxx",
            "https://drive.google.com/uc?export=view&id=1sciCxmZfG4va8CJK50G4KPx9jt3PGBiN",
            "https://drive.google.com/uc?export=view&id=1u8b7Dq7zAT4d-Ep3u7ELiAmINCMke-BL",
            "https://drive.google.com/uc?export=view&id=11F6aazrJeZg7i6UhbHum4KZpADWrdOVq",
            "https://drive.google.com/uc?export=view&id=1-4CDXUUzGwiWX-tWrmwvvx9EyJzSyj2L",
            "https://drive.google.com/uc?export=view&id=1pbdGeVBR2n83uWkXhibqu9DcesLR6JRe",
            "https://drive.google.com/uc?export=view&id=1kzqjZTdeQ8AyhwduLNchL0PI2aM20Z00",
            "https://drive.google.com/uc?export=view&id=1XYHvsqN-zSV-61cEYQpPeoSU_riazT5X",
            "https://drive.google.com/uc?export=view&id=1nMZDLSzRDkGWhObIHy3Cd8dPnzPyoAIN",
            "https://drive.google.com/uc?export=view&id=1TeGUzFrgsLj2ts6Fr29UznUPR9ctQZxt",
            "https://drive.google.com/uc?export=view&id=1XujV65lpFfHdvprXMnBYBJMH8Wwqyo59",
            "https://drive.google.com/uc?export=view&id=1zGSt4NTSZZQoX_1LGsus5bo_0MZM0vhm",
            "https://drive.google.com/uc?export=view&id=1sfUOIxx8bhhjLaKII-u7z5bXE1dhjQ3V",
            "https://drive.google.com/uc?export=view&id=18uM2BSZrvxleh6OUqqRV8IcYtnWck-rQ",
            "https://drive.google.com/uc?export=view&id=1trqEBbQPrpRmdFtKPjiqMuDdW_gaO9JH",
            "https://drive.google.com/uc?export=view&id=1AJXQK4WKmKBBLt5qTmL9rEYW3dZaYWFH",
            "https://drive.google.com/uc?export=view&id=1KyMv7lpdpYC5trLAXjIsAEMdTBLdISux",
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
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1W3Mg1tzxRRwdMDTaT3a--MSdiBO8LNM-",
            "https://drive.google.com/uc?export=view&id=1TVw52B5EiQ-VKByeEQ_i1ZPhtkH6bOlN",
            "https://drive.google.com/uc?export=view&id=14tqDwLktltKOkYbCrkXgYSPsQa_RZzMj",
            "https://drive.google.com/uc?export=view&id=1CLOTNn9HoBPbMQE7Ruh0L8Dj-fjm3opE",
            "https://drive.google.com/uc?export=view&id=1_bntylJSWyqWpWCLEBmnGnsXsoz0AD85",
            "https://drive.google.com/uc?export=view&id=1IVJ6U0sS26BkNZTMSJ4NG69nkuDUWDku",
            "https://drive.google.com/uc?export=view&id=16emyKHmdopRdgFnv-a8CqJnkCPI3dig0",
            "https://drive.google.com/uc?export=view&id=1rYPEW9f0AWEq0xiyK_yVQspiYzfBjqLr",
            "https://drive.google.com/uc?export=view&id=1qIXvuSrdGCv-nQH1qSzOaAAEOg0gbMva",
            "https://drive.google.com/uc?export=view&id=1xMY-k1aQ5NMHM13Lek_VWoKVvlUywi9S",
            "https://drive.google.com/uc?export=view&id=1qLfjUhcGh3nddrPIVJGqsbXw07-VvmW1",
            "https://drive.google.com/uc?export=view&id=1DbsIwZ4tzqAJsnT7-Gxqvdw6BHwHCuXh",
            "https://drive.google.com/uc?export=view&id=1e-X4SLW3bnTnasddlmcRvDoeb129ZLPK",
            "https://drive.google.com/uc?export=view&id=1lTppzqAiHrj1GRQWe8SjYaC-NYckmCq8",
            "https://drive.google.com/uc?export=view&id=1i7jLz63ioH_3ysmSxYtWtMhmVnfd4f37",
            "https://drive.google.com/uc?export=view&id=1g5LjinYNPoe1KOWBtzE-5h1mQ1Ngr-_M",
            "https://drive.google.com/uc?export=view&id=12XO5gzZnyHYon8cgH_rhC-_w15WhS6YV",
            "https://drive.google.com/uc?export=view&id=10-AUn6MkJY0PmWk7HGje0S-rP05TWqTs",
            "https://drive.google.com/uc?export=view&id=16ujPT-NV7mhQE4Y1HxUh6fhcOrLMiRFp",
            "https://drive.google.com/uc?export=view&id=1EXT0ycB4E9xJ17IAmaSDc67pOGMw0fHf",
            "https://drive.google.com/uc?export=view&id=1mJEYXRk97484b1vyik3HRCiphdRIqDDJ",
            "https://drive.google.com/uc?export=view&id=1zPGK0vcUAgqVdVrHnCh_CbTF4jthKc1Q",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZzXW9z3zhETXxsNoLABBk7SJ7-wYvr_I",
            "https://drive.google.com/uc?export=view&id=1Oe2sEfgDgDNfdzfKE_OJ2r3N_NtGj72Z",
            "https://drive.google.com/uc?export=view&id=1KAy2vZKFjOmMecg1yZQbalKmvT3ZNnzC",
            "https://drive.google.com/uc?export=view&id=1IWrVwbex0eyn08iY-x_jDUvmcxsew58V",
            "https://drive.google.com/uc?export=view&id=1QJyK4YhjPYL3OeYJSkd4rQZCGLvj1lIW",
            "https://drive.google.com/uc?export=view&id=1sN57hhdvUA7DwpShcaAO_PYL76yDg5Yg",
            "https://drive.google.com/uc?export=view&id=1Q2_sr34nuj9vnUPgqB-_S96jSIgP6n-K",
            "https://drive.google.com/uc?export=view&id=1qS7XNKXO7A85pHkKC_2pzwoJxJl3x5ZZ",
            "https://drive.google.com/uc?export=view&id=1fYN7MHSvCIEh2IKd2B4F8iWB32J_cegH",
            "https://drive.google.com/uc?export=view&id=1vaAzS96x9Rds68hrUmzqFt-Inkqr0k_o",
            "https://drive.google.com/uc?export=view&id=1GGu9nt0H7ZGKIoJN9nAAUTbCVghFFWjg",
            "https://drive.google.com/uc?export=view&id=1ohnatRmk-Wsi03i1rqZqz95g-tcrTq4-",
            "https://drive.google.com/uc?export=view&id=1SqGoWb0_W00EZzKreSdUPWgC4GgB6Wzf",
            "https://drive.google.com/uc?export=view&id=1LV4LJnLBEMzeoNoi4VV60AHlcb3ghWvb",
            "https://drive.google.com/uc?export=view&id=1p0Ow6jJi1sGQ1jQFeSo5bI5KlGafEud_",
            "https://drive.google.com/uc?export=view&id=1PAwd2-8OxfrefKuXA9NzCG5jWVVGBEfZ",
            "https://drive.google.com/uc?export=view&id=1mo2NhSIIDl1W6Qh8niVr4oMKnAOsFC4j",
            "https://drive.google.com/uc?export=view&id=1GWdjJtAYUygVwfAZtovr3PHEdHXfjvEQ",
            "https://drive.google.com/uc?export=view&id=1kw3CvqzVMzGnOC4H0imNMwWJ0usA_fag",
            "https://drive.google.com/uc?export=view&id=1XhUPRbrVT5UXpIdSn7LJthPZB0jMtZPR",
            "https://drive.google.com/uc?export=view&id=1I_FW4PJ5N4KhFDFrV_2sJX23cseC55Av",
            "https://drive.google.com/uc?export=view&id=1-M-J_CTJ0Jhg287QGC64fowzX7Oicz0W",
            "https://drive.google.com/uc?export=view&id=1wB07jvf_9qAzs9iLNwQY6c5DV__ftNhk",
            "https://drive.google.com/uc?export=view&id=1hJGgtWAusJYI0-P7F-oAN7SUFc7f6dQ6",
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
                "kesan": "keren banget banggg bisa jadi",
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
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "keren banget banggg bisa jadi",
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
                "kesan": "keren banget banggg bisa jadi",
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
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "keren banget banggg bisa jadi",
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
                "kesan": "keren banget banggg bisa jadi",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1b24JbkXrSFPHv6fh0t4sdByjBauYee87",
            "https://drive.google.com/uc?export=view&id=172vNoPDLmjji4h6GQqArpZnw9-xOJPUI",
            "https://drive.google.com/uc?export=view&id=1mEInOPAkhq3_KBaa3age0vu6NzuNBFuu",
            "https://drive.google.com/uc?export=view&id=1ZuguPYjbGEoDSwJZ3AA9ntRDD-PwjcUY",
            "https://drive.google.com/uc?export=view&id=16HV3-8oLxyK1bGU9E_91sR3dn1YctUA9",
            "https://drive.google.com/uc?export=view&id=12SaVbPIgGsRWdKCldjrDczn4-YogXFm_",
            "https://drive.google.com/uc?export=view&id=1yvBSyLDfD7TtKDKnccxl56MWz2rjpB6L",
            "https://drive.google.com/uc?export=view&id=1vxrJ1fK4FJA2zZnnrhndExNInGUwEN48",
            "https://drive.google.com/uc?export=view&id=1ucvdFJ_XjIcRU8ltSlgQ9bwI81jDJwNo",
            "https://drive.google.com/uc?export=view&id=1o2EJ7-xtsLPWW9YKZJXkNTsEwDt5p7gQ",
            "https://drive.google.com/uc?export=view&id=1uFH5lfNxgvXc2V5WIjSoCO_rKyb-LJOw",
            "https://drive.google.com/uc?export=view&id=1yaslJHnDnjLuylcOcFhZG6KsfSWB5x08",
            "https://drive.google.com/uc?export=view&id=1Y3DDrtlyz3aKN2De-4aBcUbBJYV6ZBUk",
            "https://drive.google.com/uc?export=view&id=1cRl9ZZxUBVzouzul7nIcV6MKjbxZdyRP",
            "https://drive.google.com/uc?export=view&id=1otq0IogCDFgvn_4o-6s6pV5veTObfDqe",
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
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 3
            },
            {
                "nama": "Rendy",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "keren banget banggg bisa jadi ",  
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
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MEcPKZPIhzA_bpVYgJCGyehid0OsBNjq",
            "https://drive.google.com/uc?export=view&id=1fIiWNdiseRk8igFc8GJK7KGlCxx96zbC",
            "https://drive.google.com/uc?export=view&id=1XkhSTnYSJ3BF8fZ-uR0fS6rGN9crwrbT",
            "https://drive.google.com/uc?export=view&id=1y4nDEp2AL-0G0NBYL628vKdfAz_xrQJJ",
            "https://drive.google.com/uc?export=view&id=1WOp3XSj3r-MqBa46lT28ro_ic9ZN7p29",
            "https://drive.google.com/uc?export=view&id=1Q06yo9PAPYQLtjsihr8evAYDNadFpw-W",
            "https://drive.google.com/uc?export=view&id=1V679N_YQS_bStKMJH6qy0WoOqQnsSzCA",
            "https://drive.google.com/uc?export=view&id=1yqrZniGqeRmKyGw_pQQ60pNDBAQuxRU_",
            "https://drive.google.com/uc?export=view&id=1TgHZHSwtjx48lwnPv8EAUOO8anGx8BXQ",
            "https://drive.google.com/uc?export=view&id=14HsoKczUMDILfbUZfENvX_H0O3_fVANk",
            "https://drive.google.com/uc?export=view&id=1HqOjcaHuOQXBvEFomA0Jssu4vyps0k2L",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14xRjCxVBPq3mDkYLLA84lgJI-kmuVzZZ",
            "https://drive.google.com/uc?export=view&id=11YNkYH1O7jWmdJ6Z0Cg0MMjVXmqVKbLL",
            "https://drive.google.com/uc?export=view&id=1MKa-QMXR-W5XPOCtW8Kyj4wtLdiYlN-1",
            "https://drive.google.com/uc?export=view&id=1chD5HWnbQcimTCm1JMKHEnl-MtH9H0iF",
            "https://drive.google.com/uc?export=view&id=1PECT1UW75wIwwyzSVorAF4SmZizWK9Me",
            "https://drive.google.com/uc?export=view&id=1EXBONjbddoaMogcsNvFCXfn5mwxzjFjE",
            "https://drive.google.com/uc?export=view&id=1xR98K7eYO7q86BrV61rfkNG22tMzqjYC",
            "https://drive.google.com/uc?export=view&id=1x7bIs1hMi6Ny3Th9R_FgNCVVnplkbn8y",
            "https://drive.google.com/uc?export=view&id=1IDUQwUwKX4UJS19wZqi1HTvguWPAxDQ0",
            "https://drive.google.com/uc?export=view&id=16bEUcX1vwQTNE-FDb9KflA08aDJdwabC",
            "https://drive.google.com/uc?export=view&id=1V2WzBpdC7ZmlVMx3zSwpR7NPkJ1TKOod",
            "https://drive.google.com/uc?export=view&id=1Fm0dGZqK8QThoeU__WhapqdrLcUwXuYy",
            "https://drive.google.com/uc?export=view&id=16LZlCfqFc6esrc0CoVLNLZzJc231j1MR",
            "https://drive.google.com/uc?export=view&id=1dh46Rq9JrAde9RCTUCtvObP2-yuekv8e",
            "https://drive.google.com/uc?export=view&id=1azjqjjkLIK1TLcarC1S7ljDFnsTmN8Hl",
            "https://drive.google.com/uc?export=view&id=1zWlnia8G9mXHvnwwcAZcyyWcAWSuvtYH",
            "https://drive.google.com/uc?export=view&id=1BkIx_nt9eNroGKlMKElHMhSdsnPGTeJG",
            "https://drive.google.com/uc?export=view&id=1OXUK6MW-qI8cKeMNTNHJCDTJqS9Jk1hX",
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
                "kesan": "keren banget banggg bisa jadi ",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "keren banget banggg bisa jadi ",
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
                "kesan": "keren banget banggg bisa jadi ",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "keren banget banggg bisa jadi ",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "keren banget banggg bisa jadi ",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 14
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()











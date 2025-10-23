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
    st.markdown("""
    <div style="
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #2c3e50;
        background: linear-gradient(90deg, #f8f9fa 0%, #e8e8e8 100%);
        padding: 20px;
        border-radius: 15px;
        width: 90%;
        margin: 60px auto 30px auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        letter-spacing: 0.5px;
    ">
        Anda telah mencapai akhir halaman<br>
        <span style="font-weight:500; font-size:18px; color:#555;">(tidak ada apa-apa disini)</span>
    </div>
""", unsafe_allow_html=True)
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jygoWorPTep8gOs8oYg_iAX5uWRi0WCD",
            "https://drive.google.com/uc?export=view&id=1c1gR-oBMZvaPSqRzJxtOH4FycRInraln",
            "https://drive.google.com/uc?export=view&id=1j65cv58Aykl1f9mKTE2ig9PSgEYXUreR",
            "https://drive.google.com/uc?export=view&id=1M4t_yIAXzmlrM8ohGRYVILcVKNPgS_7A",
            "https://drive.google.com/uc?export=view&id=1zm75MzGbkTKhO5ATeMyY00_nQZ3xJuGS",
            "https://drive.google.com/uc?export=view&id=148Es9ZPDRWuOsf3gQKvx5zru_3JVWiLp", 
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damai",
                "hobbi": "Nyanyi",
                "sosmed": "@_erendraa",
                "kesan": "kahim paling gemoy nii wkwkw",  
                "pesan":"semangat terus bang kahim!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL!",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "bang Jo asik banget orangnya",  
                "pesan":"sukses terus bang!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Badui",
                "alamat": "Ayrest Kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "kak abet lucuuu",  
                "pesan":"selalu ceria ya kakk!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "ku kira kakaknya kalem, ternyata engga wkwk",  
                "pesan":"semoga sukses terus kak"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakaknya lucu banget plisss",  
                "pesan":"semoga pintar nya nular ya kak hehe"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "kak hunam gemoyy hehe",  
                "pesan":"sukses terus ya kak hunammm"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11EtLjaeMfQ5YLmxbSZ5KI2eR43QZHowU",
            "https://drive.google.com/uc?export=view&id=1X26vBTRttUVi2dVdubEojQcvf1qRhVen",
            "https://drive.google.com/uc?export=view&id=1o0fV3yL2PNZt_yktBAjXu1gNTQLP7OQr",
            "https://drive.google.com/uc?export=view&id=1nKrmwLj5YYsxHOCUP6g2l2KBLNdo8GMX",
            "https://drive.google.com/uc?export=view&id=1JKzAjZKxlovSc6vPEr0WwWtpIf2ykR6l",
            "https://drive.google.com/uc?export=view&id=18PXejwSlpX4MWMzNaWuEjtf5Zg2dVZCs",
            "https://drive.google.com/uc?export=view&id=1srvR6vn-U7Ilr8giRj4NpzpUiIxxs3_F",
            "https://drive.google.com/uc?export=view&id=1i9yonzdtzXvPg1qy8ZtK3sVdBjyG3zsD",
            "https://drive.google.com/uc?export=view&id=1j0qPP1yxOE41eKyHX4VLEbYCfNBwYoDu",
            "https://drive.google.com/uc?export=view&id=10WOZkaB-Ohn3sEG8g_pCnuW54vaXsc6p",
            "https://drive.google.com/uc?export=view&id=1Hba6VoDXce_Ydh10YPULEMTlS574S4O1",
            "https://drive.google.com/uc?export=view&id=1BdaNqgKoS5dO9hznpK-jqDqOpy_OkXJs",
            "https://drive.google.com/uc?export=view&id=1RiLKELjowYqnn4c7LAgaT-hYk9ayAUUQ",
            "https://drive.google.com/uc?export=view&id=1UzqoLWKyfvFfUzs-me2d2eHsbKvhWgrm",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Pilates",
                "sosmed": "@jeremia_s_",
                "kesan": "abangnya asikk",  
                "pesan":"semangat bang semster 7 nya!!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea baikkk banget",  
                "pesan":" Sukses terus ya kakk!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "kak renisha kece hehe",  
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya keren",  
                "pesan":"Sukses terus ya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "kok bisa gacor sii bang otaknya huhuhuhu",  
                "pesan":"semoga gacornya nular ya bang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak feby gemaasss",  
                "pesan":"semangatt teruss kak!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "mentor ter-kece, ter-asik, ter-gacor",  
                "pesan":"moga langgeng bang sama kak anu hehehehehehe"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "abangnya cool, +1000 aura",  
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Catur",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya asik banget ",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandiama",
                "alamat": "Way Huwi",
                "hobbi": "Minum air putih 8x sehari",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya lucu banget huhuhu",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Nyanyi tabola bale",
                "sosmed": "@iamridhomanik",
                "kesan": "abangnya kece",  
                "pesan":"sukses terus banggg"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Koleksi Stiker",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya santuy",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Papua Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "kakaknya lucuu",  
                "pesan":"semangat terus kakk"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya seru",  
                "pesan":"semangat terus kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ckdvWNT1Ix5tGfJUgpKdcbFsqq9JMO3I",
            "https://drive.google.com/uc?export=view&id=1Ei7XjPYnxAka5aorcpypTue7lFLwrM2_",
            "https://drive.google.com/uc?export=view&id=1PpnkZsUPTF6lsbcT7tQRkcWznVy4LIb3",
            "https://drive.google.com/uc?export=view&id=17P8GHfcbMQFrc6QAKA-WrOwcf-odQI9J",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Denger lagu, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Bintang asik banget orangnya",  
                "pesan":"tetap bersinar bang!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu, maen roblox",
                "sosmed": "@nadyaanjanani",
                "kesan": "Kak Nadya cantik bangettt huhuhuhu",  
                "pesan":"langgeng ya kakk sama si anu hehehehe"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Ice Skating",
                "sosmed": "@fathinahazzh",
                "kesan": "vibes kakaknya masyaallah sekali",  
                "pesan":"semoga prestasinya nular ya kakkk"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "kakaknya keren!",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hmXneWVIsKimZyp7TAi6Di8gq3BxcElo",
            "https://drive.google.com/uc?export=view&id=1Edq-6c_hJAaTcmP1HmBb56L-6G0s86yL",
            "https://drive.google.com/uc?export=view&id=1-O4onL4p2QXr5OF2VAnc2GmqJQ99pAnU",
            "https://drive.google.com/uc?export=view&id=1MoGEe_fDrKYSMeTLcZpNOLn58f0J2CuW",
            "https://drive.google.com/uc?export=view&id=1B7MpyIJMkl4-38RtqR2vemZYS1O57xng",
            "https://drive.google.com/uc?export=view&id=1h8G9csu3jjJJOtB9y4LNPTX1Pk9wpdi3",
            "https://drive.google.com/uc?export=view&id=1NsPVtNe8pODDyULyp0ExViPHVOb52Ohd",
            "https://drive.google.com/uc?export=view&id=1p3zlU_VjNwu0qJpc82KHgOHvnFZzCQrA",
            "https://drive.google.com/uc?export=view&id=1Bsonm1onrFqLnAYuVuk41mDez1GBLoTg",
            "https://drive.google.com/uc?export=view&id=1CZ16zty2KP-m-h7VfdGWvy4gEsxv8acH",
            "https://drive.google.com/uc?export=view&id=14a9ISE7QL9JvX55c1YGse9OTCJQZTWWb",
            "https://drive.google.com/uc?export=view&id=1c1y1_jVu-4q0OEcKXJNCky8o5rn6K1qa",
            "https://drive.google.com/uc?export=view&id=1WZaWd1n8MaN1awqWXQVKlGMPS25E7F9h",
            "https://drive.google.com/uc?export=view&id=1mhTWhzGmaREfyNZZIur_QVQL3Ap1XcAG",
            "https://drive.google.com/uc?export=view&id=1hQMJoT-lt-JHVOFaxaXX0fMBawKH1s1-",
            "https://drive.google.com/uc?export=view&id=1hcXXJrc3aVyDSagfPEp8O0AJx6WVz-2A",
            "https://drive.google.com/uc?export=view&id=1aWBhZXHI3VhpzK-eOPVEOYuPGCHtWbPR",
            "https://drive.google.com/uc?export=view&id=1ZQLYItFSOxkazJ0WaulgQ8wn6wR2VC_J",
            "https://drive.google.com/uc?export=view&id=1Us0foJSuqARVdTKz1HH4LMMTlxjylfsZ",
            "https://drive.google.com/uc?export=view&id=1j966ZAwNlfkIccPmV1vsGpvRTqjov0_P",
            "https://drive.google.com/uc?export=view&id=1M1-fu5pKmuEg3XSySHm-foUEPM5GjDyD",
            "https://drive.google.com/uc?export=view&id=12UPInaJIEC3tYULIkdM8ci1gagqvIUUp",
            "https://drive.google.com/uc?export=view&id=14tC62KrEwKW2k2AfaDVmipVuAbeFyK-c",
            "https://drive.google.com/uc?export=view&id=1nR1SER1Na7uH-b2_m640ByogxZFz-dLf",
            "https://drive.google.com/uc?export=view&id=1FWO-mRB717ynMBMPdu_9w1SwYdQG6HdS",
            "https://drive.google.com/uc?export=view&id=1854PRWCAErvXtiXIQbfa0xoFaDOUU63s",

        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya cool banget",  
                "pesan":"semangat terus bang kadep!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya glowing banget hehehe",  
                "pesan":"spill skincare nya dong kak..."# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kak Allya kece banget no debat",  
                "pesan":"semoga kece nya nular ya kakk hehehe"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "abang NIM saya nih hehe",  
                "pesan":"kece terus ya bang"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "gemes bgt sama pipi kak arin hehehe tembem soalnya",  
                "pesan":"semangat terus kak arinnn"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Zidane",
                "sosmed": "@daffahdynn_",
                "kesan": "bang daffa gacor lah pokoknya",  
                "pesan":"makin gacor ya bang!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "abang kece bangettt",  
                "pesan":"tetep kece terus ya bang!"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakaknya cantik sekalii",  
                "pesan":"semangat terus kak!"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "salut banget sama skill ngodingnya bang",  
                "pesan":"semoga pinter ngodingnya nular ya bang hehehe"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "abang kece pokoknya",  
                "pesan":"semangat terus bangg!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang Berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya cantikkk",  
                "pesan":"semangat terus kakk!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "abangnya chill",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang 4 Nangka Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya santuy banget",  
                "pesan":"semangat terus bang ali!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "kakaknya asikkk",  
                "pesan":"semangat kuiahnya kak"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya gemoy hehe",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kakaknya asik",  
                "pesan":"semangat terus kakk!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "abangnya baik banget",  
                "pesan":"semangat terus bangg!"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_",
                "kesan": "abangnya santuyy",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "kakaknya asik",  
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Belajar Front end",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnya asik banget",  
                "pesan":"semangat bang!"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Berdiri, Nyantai",
                "sosmed": "@kevinaj_",
                "kesan": "abangnya seruuu",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakaknya asikk",  
                "pesan":"semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "abangnya humoris",  
                "pesan":"sukses terus bang"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main futsal, voli",
                "sosmed": "@sidabutar.26",
                "kesan": "abangnya seru banget",  
                "pesan":"Tetap semangat bang!"# 1
            },
            {
                "nama": "Uliano Wiliam Purba",
                "nim": "122450098",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngoding",
                "sosmed": "@liano.wlm",
                "kesan": "abangnya cool banget",  
                "pesan":"semangat terus ya bang!"# 1
            },
            {
                "nama": "Rewina Audrya Melvasari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "JL. Ratu Dibalau",
                "hobbi": "Gambar doodle",
                "sosmed": "@lewinanaaa",
                "kesan": "kakaknya pendiem",  
                "pesan":"sukses selalu ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Sg8zZHAbLd6Ggy6v6IF2ad6CPaY6LQUG",
            "https://drive.google.com/uc?export=view&id=1-zpEKhohatjdZSQgGaTglTxEao3Xoj_R",
            "https://drive.google.com/uc?export=view&id=1HHVHuBhloMY-6yn3Qt-M-F9EUJVTNiIu",
            "https://drive.google.com/uc?export=view&id=1clCCv8OCfhb02NNDxam00xG7KC5jD-6J",
            "https://drive.google.com/uc?export=view&id=1BqLbJfUW7MeazZz7-I962eU7ZA4z2v9K",
            "https://drive.google.com/uc?export=view&id=1NXBwL7-wzpXAdz0286faexzlqOxAfdHP",
            "https://drive.google.com/uc?export=view&id=1-T4_NfJGtBmORJCePHsKL2xusoZmM_mO",
            "https://drive.google.com/uc?export=view&id=1snMpxcH72Z070rKGIxzdjBg1Sf3NhJek",
            "https://drive.google.com/uc?export=view&id=1n5Hc31EQ9s7L4IQksOATU6xUfELVl59J",
            "https://drive.google.com/uc?export=view&id=1DairkmtjcFzvjEc0AVcy0rUkzOgS2j5q",
            "https://drive.google.com/uc?export=view&id=1TPxk46qCTOXxNb6tZD5Jey3_OkfZgaNk",
            "https://drive.google.com/uc?export=view&id=1LTgJ18xbFRoUCwL63H47CcMKWYZGoMSx",
            "https://drive.google.com/uc?export=view&id=1Pd5d3wBK-fqpinIDvQW4rBA5FwNd675D",
            "https://drive.google.com/uc?export=view&id=1WRo-NK6mrovsQ67TPedNJxqjCPY4ZWtW",
            "https://drive.google.com/uc?export=view&id=19mWUenHriTeMcFxBw7fmi_EnlTBwlW5y",
            "https://drive.google.com/uc?export=view&id=1UrycvDYv2iKKxhFgrR3SRnkgyWvMVCQu",
            "https://drive.google.com/uc?export=view&id=1MbLb-F3FxufgEDVHRDe6i4o0u_7R3NXG",
            "https://drive.google.com/uc?export=view&id=1UuaVTGREN85JjyC-lA1TL8S3UanXelFm",
            "https://drive.google.com/uc?export=view&id=1x80y4M4IR_DIz7RXc0ZqSj9X1ZYDXAwx",
            "https://drive.google.com/uc?export=view&id=1ZXJgB_11bVif4jG0OrKwPj48LYEbplO4",
            "https://drive.google.com/uc?export=view&id=1cjSS682rL4rK8fwd36qDHATpE83j4ohy",
            "https://drive.google.com/uc?export=view&id=1pBKei407chG_U4UZ49bdI36MRy3XjOS6",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur, berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "abangnya baik banget",  
                "pesan":"semangat terus bang!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "kakanya gemoyyy",  
                "pesan":"semangat ya kak kuliahnyaa!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "abangnya keren banget",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishashi",
                "kesan": "kakanya asik",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilafarizzii",
                "kesan": "keren banget bang",  
                "pesan":"semoga pinternya nular ya bang"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "abangnya ramah bangettt",  
                "pesan":"semangat terus  bang!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik, nonton",
                "sosmed": "@notfall.s",
                "kesan": "abangnya santuy",  
                "pesan":"sukses terus bang"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "kakaknya lucuu",  
                "pesan":"semangat kak!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "kakaknya cantik",  
                "pesan":"semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keylashafi_",
                "kesan": "abangnya santuy",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakaknya seruuuu",  
                "pesan":"semangat maraton drakornya kak hehe"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "kakaknya manisss",  
                "pesan":"sukses terus kak!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@pebby_olla525",
                "kesan": "kakanya ramah banget",  
                "pesan":"sukses terus ya kak"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakaknya baik sekaliii",  
                "pesan":"semangat menjalani harinya kak"# 1
            },
            {
                "nama": "Tanty Widyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "salut sama skill mc nya kak",  
                "pesan":"semoga aku bisa PD juga kaya kakak hehehe"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "abangnya baik banget, ramah",  
                "pesan":"sukses terus ya bang!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya baik banget",  
                "pesan":"semangat kuliahnya kak"# 1
            },
             {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@i",
                "kesan": "abangnya seru banget",  
                "pesan":"semangat terus bang!"# 1
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "abangnya kalem banget",  
                "pesan":"sukses selalu bang!"# 1
            },
             {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "kakaknya baik banget",  
                "pesan":"sukses selalu ya kak!"# 1
            },
             {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "kakaknya baik banget",  
                "pesan":"sukses terus ya kak!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "abangnya cool",  
                "pesan":"sukses terus bang!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jzDHnjQ8BOGHQJradTgazDwqQ30IKqa7",
            "https://drive.google.com/uc?export=view&id=1wVLkNGbzP5_tGyYbGcJGsmPz8VPD5UF2",
            "https://drive.google.com/uc?export=view&id=1mK3UjDKaq-tYJcSGuq0PtggmdfCSgn9s",
            "https://drive.google.com/uc?export=view&id=1R8ndDcQ-vrUvGpez5QxF_XBH999L47vH",
            "https://drive.google.com/uc?export=view&id=1LL2yr6etgKx98-X08iyGUsZIpDvXglDk",
            "https://drive.google.com/uc?export=view&id=1EzSCLePoQUgSAWpFl-9jUOSG-xVHCRpT",
            "https://drive.google.com/uc?export=view&id=12Ip5Su5mIjChVxi4UUx-XlNUfSorD5sC",
            "https://drive.google.com/uc?export=view&id=1-6NvLxm8Hkguw5US9KrCIiwj24fUrhvA",
            "https://drive.google.com/uc?export=view&id=15h8_AZOu7Frvps0Mo2TqYsAeMEnL1buq",
            "https://drive.google.com/uc?export=view&id=1BQnklM-vIFsPlGjEcZUMoHH7RI_x134F",
            "https://drive.google.com/uc?export=view&id=1pV98Aj4JT8gPr3CHO1IPfX1dcC7sVA2j",
            "https://drive.google.com/uc?export=view&id=1kKM-Q6EDJFIA8VaGrAadlEUsjwVPaO-J",
            "https://drive.google.com/uc?export=view&id=1dT1lnld2u5tJ4AC3cqMu3lGqciquLtSC",
            "https://drive.google.com/uc?export=view&id=1tU5kpo4zs1xRJ3MDAlJ_kpM2oEbgMm8B",
            "https://drive.google.com/uc?export=view&id=1dJGnxtEbDjFB3PAwDfBRAZCpMQ_TuaKG",
            "https://drive.google.com/uc?export=view&id=1jkrYJcvY2mA2rSlEiyDWlnO7EMd64-rb",
            "https://drive.google.com/uc?export=view&id=19b7XMBFQlfNEIlLwS64tsC7r5TM03qSb",
            "https://drive.google.com/uc?export=view&id=1TM7pwkpftKDt-KPmuyo5DepRyNuyP8x-",
            "https://drive.google.com/uc?export=view&id=1maCBQvO126RU56hb34YUjpFKWRfd2mbh",
            "https://drive.google.com/uc?export=view&id=1H3NiPAq_9dM5KZDTKvWXbHOXFnYGUdpA",
            "https://drive.google.com/uc?export=view&id=1b2XuS3s79HCB3iEqDBM0d8VSj-oJODE9",
            "https://drive.google.com/uc?export=view&id=1K2JIEaG7eoB1PKvtsbuLgYPU5GTS5PfB",
            "https://drive.google.com/uc?export=view&id=1ATe0q6oWuUQv2UfoYO62if0b3NNBd4GF",
            "https://drive.google.com/uc?export=view&id=1iXEvLzT7cLZescQZv7PtGcg3fqqe5uTj",
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
                "kesan": "abangnya seru banget, asik juga",  
                "pesan":"semangat terus ya bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kakaknya baiikk banget",  
                "pesan":"semangat ngampusnya ya kak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "kakanya cantik banget, gacor pula",  
                "pesan":"semoga suksesnya nular ya kak"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "kakanya asikkk",  
                "pesan":"semangat kuliahnya ya kak!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "abangnya kalemm",  
                "pesan":"semangat terus banggg!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kakaknya baik banget",  
                "pesan":"sukses selalu ya kak"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakaknya ramahhh",  
                "pesan":"semangat ya kak!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya gemoyyy",  
                "pesan":"sukses terus ya kak!"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "abangnya santuyyy",  
                "pesan":"semangat kuliahnya bang!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "kakaknya asik, ramah",  
                "pesan":"sukses selalu ya kak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "kakaknya cantikkkk bangetttt",  
                "pesan":"semangat terus ya kak, lancar lancar kuliahnya"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "kakaknya asikkk",  
                "pesan":"sehat selalu ya kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "abangnya gacor abizzz",  
                "pesan":"sukses terus banggg"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "kak sonya baiiikkk bangettt, kenal waktu awal awal masuk kampus",  
                "pesan":"semangat terus ya kak, lofyuuu"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakanya ramah banget",  
                "pesan":"semangat terus ya kak"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "abang kece",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "abangnya ramah banget, humoris juga",  
                "pesan":"sehat selalu ya bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kakaknya asik banget, ramah",  
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "kakaknya lucu",  
                "pesan":"sukses terus ya kak!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "kakaknya baik banget",  
                "pesan":"semangat kak"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "kakaknya asik sekalii",  
                "pesan":"sehat sehat terus ya kak!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakaknya keceee",  
                "pesan":"sukses terus kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "abangnya mirip kakak kelasku waktu SMP dulu, ternyata bukan soalnya namanya beda hehehe",  
                "pesan":"sukses terus bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "kakaknya asik banget",  
                "pesan":"lancar lancar kuliahnya kak"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1D6Ck19oquRptIPz2oAkD6hkDVy9EqgQ9",
            "https://drive.google.com/uc?export=view&id=1M8p9OZDTkxmNBkFRW0DUTgDxzQVj1kWR",
            "https://drive.google.com/uc?export=view&id=1qbQSqOXvvW7b3vCU2xsC9c28ESk-t0OY",
            "https://drive.google.com/uc?export=view&id=1Lctvpgm4rma6tAGDYY81L9hB2mj14hAy",
            "https://drive.google.com/uc?export=view&id=1sljTpQgYgYNRwFK4kcBaBZ9thypf3GTn",
            "https://drive.google.com/uc?export=view&id=1HRx5qFiUWZvobsHnwcBtr69lnxfBktfs",
            "https://drive.google.com/uc?export=view&id=1qwR0j1WS_S3KXIyKLJ-qVRvkG6hO7QEa",
            "https://drive.google.com/uc?export=view&id=1uWtPFrmozvdnJSIixM8ZMVJLgfdwnCyd",
            "https://drive.google.com/uc?export=view&id=1pge98eRSrTHbID1cwq1TMbtR4P5TI5lj",
            "https://drive.google.com/uc?export=view&id=1ZC0b75lVhe-HTTtso3a972D8cOXqD5bE",
            "https://drive.google.com/uc?export=view&id=1R_3TOD6Lbmibz4PtOncaqFNLvoi6t3YX",
            "https://drive.google.com/uc?export=view&id=1RaaSXHzUjo663o9yY4iV2pfCcr-Pz8Kx",
            "https://drive.google.com/uc?export=view&id=1SjnfFQSydlBQkj3Trvbp-AZQs_o4LVwP",
            "https://drive.google.com/uc?export=view&id=1A3owsrQQlGA37Zpv3wvv2tpKCHf9LZgI",
            "https://drive.google.com/uc?export=view&id=1D1qmQS2GZqqp4N5NayKczVgXE3SF9MyE",
        
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
                "kesan": "kakaknya baik bangettt",  
                "pesan":"sehat selalu kak kadep!!!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "kakaknya lucu bangettt",  
                "pesan":"sehat sehat terus ya kak"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@sal_fhn",
                "kesan": "kakaknya masyaallah sekali",  
                "pesan":"semoga istiqomah terus ya kak hehe"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "abangnya kalem banget, cool juga",  
                "pesan":"sehat selalu bang"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "kakaknya cantik, asik juga",  
                "pesan":"sukses terus ya kak"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "abangnya sangar, tapi aslinya baik banget",  
                "pesan":"sehat selalu banggg"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "kakaknya gemoyyy",  
                "pesan":"semangat kuliahnya ya kak"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "kakaknya baikkk",  
                "pesan":"sukses terus kak"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "abangnya gemoyyy",  
                "pesan":"semangat kuliahnya banggg"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatriaaa",
                "kesan": "abangnya kalem banget",  
                "pesan":"semangat banggg"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakaknya asikkkk bangettttt",  
                "pesan":"sehat selalu ya kakkk"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "kakaknya cantikkk",  
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "abangnya asikk",  
                "pesan":"semangat terus bang!"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Musik",
                "sosmed": "@sarahwsti",
                "kesan": "kakaknya seuuu",  
                "pesan":"semangat terus kakkk!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda Way Huwi",
                "hobbi": "Main rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "kakanya lucu banget, gemes",  
                "pesan":"semangat kakkk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uKduhATZ1RRH-Sjj57n_ZK6_E4CgcQVX",
            "https://drive.google.com/uc?export=view&id=1qBFGp3n4l3Opyy1WOgvAmIRXL3WRWqwH",
            "https://drive.google.com/uc?export=view&id=1VCcaXlbqxcJ35t6vX1x0ttf-EW5I629_",
            "https://drive.google.com/uc?export=view&id=1SDnW6b7r9f9vqmKWbQtehy9e-rV8ILeD",
            "https://drive.google.com/uc?export=view&id=1ApKRVfaKuDMxqLy-YLoRqEwT4UrbUTy-",
            "https://drive.google.com/uc?export=view&id=1g1-crbnnx5Kglz_rA3OPe_R5eHjeMP4Z",
            "https://drive.google.com/uc?export=view&id=1WiZ35xOrQNRYQuQfqY8bEa3FeWkQMSD7",
            "https://drive.google.com/uc?export=view&id=1ak5-nyX632E0VX0_vUNA3sCF_mSTDxml",
            "https://drive.google.com/uc?export=view&id=1FCLU3rxmgIrdmHG0nim7IjR1_LkYl4OO",
            "https://drive.google.com/uc?export=view&id=1f6p5uoK2udIZ6MV-iGOa6gOny_YyxpnB",
            "https://drive.google.com/uc?export=view&id=1U7QDeNZ978yKCDVZfflY8V-Tmf66dw9O",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Bisnis Startup, Jogging",
                "sosmed": "@dananghk_",
                "kesan": "abangnya keren, menginspirasi banget, ramah juga",  
                "pesan":"sukses terus bang, semoga nular ke saya juga amiinnn"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "kakaknya baik banget",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum, foto-foto pemandangan",
                "sosmed": "@den_iki__",
                "kesan": "abangnya cool banget, ramah juga",  
                "pesan":"sehat selalu bang"# 1
            },
             {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya ramahhh",  
                "pesan":"sukses selalu kakkk"# 1
            },
             {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort fb",
                "sosmed": "@aphrhtp_",
                "kesan": "kakaknya ramah banget, cakep juga",  
                "pesan":"sukses selalu ya kak"# 1
            },
             {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging juga",
                "sosmed": "@nabila_zazahra",
                "kesan": "kakaknya seru, asik juga",  
                "pesan":"sehat sehat ya kakkk"# 1
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnya baik banget",  
                "pesan":"sukses terus banggg"# 1
            },
             {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "kakaknya baikkk banget",  
                "pesan":"semangat kuliahny kakkk"# 1
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg perwira 2",
                "hobbi": "Nonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "kakaknya ramah banget",  
                "pesan":"semangat teruss kakk"# 1
            },
             {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kakaknya cakeppp",  
                "pesan":"mau dimasakin juga dong kak hehe"# 1
            },
             {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "kakaknya extrovert abizzz",  
                "pesan":"sukses terus ya kakkk"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uzqxdP2yDDjpIEtEIkq2DNl4KwBtP0D0",
            "https://drive.google.com/uc?export=view&id=1papWiDK4u0vtBKO79KZY_PA6nrKzbvgM",
            "https://drive.google.com/uc?export=view&id=1-12jk4BJKB3a-EiS6_7YR4kn2akYtAgF",
            "https://drive.google.com/uc?export=view&id=1EVsrZp8Q0SZSbqW5CXwySeThZ0Fag0NW",
            "https://drive.google.com/uc?export=view&id=1bkl80wM2UicHt2R7s5Q3i-VnMezo7GsS",
            "https://drive.google.com/uc?export=view&id=1ZCvJPMo5NdW3u815OVVUHLbnZZp0_DU7",
            "https://drive.google.com/uc?export=view&id=1-CmXpaCWB9xxNobD2vzCxM-27paehp9a",
            "https://drive.google.com/uc?export=view&id=1Ooea7tgGpKI30BRskHGZsbrukHRaOP-h",
            "https://drive.google.com/uc?export=view&id=1gnz7Of_URrddx1W76JiiT0VL0ijJ4hJQ",
            "https://drive.google.com/uc?export=view&id=1jFKHVOkdCjfQb-RHZPn-wuoCB2blAQRa",
            "https://drive.google.com/uc?export=view&id=1-lK8D7k4y7CncyIgxo2HaxvyWxy0vt25",
            "https://drive.google.com/uc?export=view&id=1XkDprYOWN3Vu5HsHxRN0YRu86CurPah3",
            "https://drive.google.com/uc?export=view&id=1TdBfUzuuflhVWp2h4iHzxAf6jWcn0sdG",
            "https://drive.google.com/uc?export=view&id=11VOLIS2CRxJ-YAJivoEhxk5N96iTy89h",
            "https://drive.google.com/uc?export=view&id=1rENXfiF2TgBvGKvSF_a0DuEUe6wA3k4H",
            "https://drive.google.com/uc?export=view&id=1XNv8LlhiH-L7a98mFN2dORQB_KKG99SV",
            "https://drive.google.com/uc?export=view&id=1Ku4ozijXtSdpnA-rE3AI_uB-9TWwaEUc",
            "https://drive.google.com/uc?export=view&id=1BNIIyQQJG7PlQuWUA6dVYu2cN1CM_Qkj",

        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jati Mulyo",
                "hobbi": "Sleepcall",
                "sosmed": "@patriciadiajeng",
                "kesan": "kak cia cantiiikkk bangett, suka liatnyaaa",  
                "pesan":"sukses selaluuu kakak cantiikkk!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jl. Kresna Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan":"kakaknya seru banget",  
                "pesan":"semangat terus ya kakkk"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard & Volly",
                "sosmed": "@mananam_",
                "kesan": "abangnya kalem banget",  
                "pesan":"sukses terus bangg"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik & fotografi",
                "sosmed": "@noerruu",
                "kesan": "abang keceee",  
                "pesan":"semangat terus bang PDD!!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "abangnya ramah bangettt",  
                "pesan":"sehat selalu ya bangg"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "kakaknya baikk selaiiiyyy",  
                "pesan":"sukses terus kakkk"# 1
            },
            {   
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakaknya manisss",  
                "pesan":"sukses selalu kakk"
            },
            {
                "nama": "Aliya Anmara Amanta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammra",
                "kesan": "kakaknya gemoy banget",  
                "pesan":"semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@donnamaya.p",
                "kesan": "kakaknya ramah, asik, baik bangett",  
                "pesan":"semangat terus kakkk"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "kakaknya baik banget",  
                "pesan":"sehat selalu ya kak"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kakaknya baik banget",  
                "pesan":"sukses selalu kak"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumateraa Barat",
                "alamat": "Jl. Lapas, Kecamatan Jati Agung",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa_",
                "kesan": "kakaknya maniss",  
                "pesan":"sehat sehat ya kakk"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "kakaknya ramah banget",  
                "pesan":"ayo kita mabar rosblok kakkk"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "abangnya kerennn",  
                "pesan":"sukses terus bang"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "kakaknya ramah banget",  
                "pesan":"semangat ya kakkk"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "kakaknya sangat ramahhh",  
                "pesan":"sukses selalu kakk"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "kakaknya gemoyy",  
                "pesan":"sehat selalu kakkk"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "kakaknya kerenn",  
                "pesan":"sukses terus ya kakkk"# 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
       

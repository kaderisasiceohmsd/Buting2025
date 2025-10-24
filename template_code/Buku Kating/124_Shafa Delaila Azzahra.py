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
            "https://drive.google.com/uc?export=view&id=13SeF7ddZHR0YbJbt1LrZjc5Fy63195l1",
            "https://drive.google.com/uc?export=view&id=1ur7PdvYnWwBCivegN5DlSGarvsGwPDyj",
            "https://drive.google.com/uc?export=view&id=1Khqo9mNPN40PbUHF1H3G_E5v5XPaIXXi",
            "https://drive.google.com/uc?export=view&id=1sp2ff19aI31RUhlqtBxzU4zLvvkJwvUJ",
            "https://drive.google.com/uc?export=view&id=1imE0HWWoUOcGmsIfrbrbJ3F55vw88yj_",
            "https://drive.google.com/uc?export=view&id=1e1N68bUsbFgMyv4DTtaSwif_HtTY_fVV", 
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
                "kesan": "Bang rendra kalo nyanyi suaranya enak benerrr sumpisss, asik bangett lagiii",  
                "pesan":"Semangat Abang kahim, semoga selalu diberi kemudahan kuliahnyaaa, Aamiin.."# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL!",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Awal ketemu bang jo jujur agak takut karna mukanya galak, ternyata bang jo asik abiss, terus kocak juga orangnya, seruu dehhhh",  
                "pesan":"LUCU TERUS YA BANG JO!! semangat kuliahnya bang, semoga cepet lulussss"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Badui",
                "alamat": "Ayrest Kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "kak abett asikk bangett, dan pastinya kerenn bangettt jugaa",  
                "pesan":"semangat kuliahnya kakk, semoga diberi kemudahan kuliahnya"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakak kalem bangett, baik lagi",  
                "pesan":"sukses terus ya kakk!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak eksanty seruu banget orangnya, sosial energi nya selalu penuh kayaknya",  
                "pesan":"bahagia selalu ya kakk!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak cantik bangett plsss, mukanya jutek tapi ternyata ngga, murah senyumm lucu lagii",  
                "pesan":"semangat menjalani hari harinya kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DyubpPsXT0ElF03fs7aINWz7RZEkfSYx",
            "https://drive.google.com/uc?export=view&id=1Ai7Xhz65z3IH3EYV_KRxe77oppZ3zqb_",
            "https://drive.google.com/uc?export=view&id=1cWd7SJxwsXrYLxpOzvl60gwE9cZ5zOzY",
            "https://drive.google.com/uc?export=view&id=1oxpkFvfkZJv5g0RFMBLrar7IZBBiuMLl",
            "https://drive.google.com/uc?export=view&id=1V0IOPMNH-uUen2c44dtxutcsah3a8IGF",
            "https://drive.google.com/uc?export=view&id=1buaKFcw9fHdgApvVfE9rH2xFurG0gN1Z",
            "https://drive.google.com/uc?export=view&id=1d9LW98lNxYejPc_ffFyi3ZuWrKDVhN4_",
            "https://drive.google.com/uc?export=view&id=1nYHOJlSAr-0r63bLblpda1p4SpCfkuSs",
            "https://drive.google.com/uc?export=view&id=19KUWAwfycxBiPkOvcjfjcvtIW2WWuG96",
            "https://drive.google.com/uc?export=view&id=1dbDvVzjZ4WqK-VoIzHIoghE5FgWjljpn",
            "https://drive.google.com/uc?export=view&id=11Ps-aBvGIlzNxnBwH6KHQt7Wkc_KuAqf",
            "https://drive.google.com/uc?export=view&id=1gddFRzhZBHvGVL0iiugYcBt6_TmrTyYK",
            "https://drive.google.com/uc?export=view&id=1CWYUBNVZNtd2iLcWoMdVOZrQjrgNAth4",
            "https://drive.google.com/uc?export=view&id=17FRAbqbI6Dxk-o0org2I0KTXCqRqnpen",
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
                "kesan": "bang jeree keren bingittt, ramahh lalu murah senyummm",  
                "pesan":"semangat menjalani semester akhirnya bang, semoga diberikan kemudahannn"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "baikk dan ramah bangett",  
                "pesan":"semangat kuliahnya kak!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "humoris, lucuuu baikk terus cantikk jugaaa",  
                "pesan":"jangan keseringan tidur kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "ramah dan murah senyum",  
                "pesan":"semangat kak belajar ngaji nyaa"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "aduhhh bang dharu ini kecil kecil cabe rawit lahhh, kerenn abiieess lah pokoknyaa, mentor pplk kesayangan drespanthra",  
                "pesan":"semangat terus bang dharuuu, semoga selalu diberi kemudahan untuk setiap langkahnya, Aamiin. ayo pan kapan ngumpul bareng drespanthra lagii"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "imut, lucu dan baikk",  
                "pesan":"semangatt kuliahnyaa kakk!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "BANG GIPP!!! THE BEST MENTOR DEH POKOKNYAAA, asikkkk lucuukk baikkk 1000%%%",  
                "pesan":"bahagia selalu ya bang gipp, semoga diberikan kemudahan kuliahnya, Aamiin.."# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "keren, baik, asikk",  
                "pesan":"semangat menjalani hari harinya bang!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Catur",
                "sosmed": "@berlyyanda",
                "kesan": "humblee, murah senyum",  
                "pesan":"semangat terus kuliahnya kak!!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandiama",
                "alamat": "Way Huwi",
                "hobbi": "Minum air putih 8x sehari",
                "sosmed": "@j__eesie",
                "kesan": "lucuuu, gemess, selalu menebarkan positif vibes",  
                "pesan":"stay positive kak!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Nyanyi tabola bale",
                "sosmed": "@iamridhomanik",
                "kesan": "ramah, murah senyum, baikk",  
                "pesan":"bahagia selalu bangg"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Koleksi Stiker",
                "sosmed": "@fer_yulius",
                "kesan": "chill bangett, humble",  
                "pesan":"sukses terus kuliahnya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Papua Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik, manis, humoris",  
                "pesan":"semangat terus kuliahnya kak monica!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "lucuuu, baikkk",  
                "pesan":"semangat terus kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1URd_6alZndFP2Q6Gwd171QoRs2nhuhzU",
            "https://drive.google.com/uc?export=view&id=1o8KLYpJfecQvVrIHdyIjzgCu0--V0XIR",
            "https://drive.google.com/uc?export=view&id=1en1VPz6Abhb-TCNlE_Lnxi7ereFjQrLm",
            "https://drive.google.com/uc?export=view&id=1AjffjlALsL1HhWnMXvc62RSzZsWRIlRP",
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
                "kesan": "asikk bangettt, seru kalo ngobrol sama bang bintang",  
                "pesan":"semangat terus bangg, semoga selalu diberikan kemudahan sampe lulus kuliah!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu, maen roblox",
                "sosmed": "@nadyaanjanani",
                "kesan": "lucuu, cantik banget gabosen kalo liatin mukanya lama lama",  
                "pesan":"ayo kak mabar robloxx"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Ice Skating",
                "sosmed": "@fathinahazzh",
                "kesan": "baikkk, ramah banget, positif vibes",  
                "pesan":"keep positive kak!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "orangnya seruu, murah senyum",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X7KTTZbiNCc1bSFT5kGn-_qwaj55s5AG",
            "https://drive.google.com/uc?export=view&id=1MJQedQwDIDCBUo1y21MOis9fv1H7mdbu",
            "https://drive.google.com/uc?export=view&id=1ytq6TR0wEVMP0TL0s6u15zH4SOka7MH4",
            "https://drive.google.com/uc?export=view&id=1IOQXnJeEIboGsQwobco94LpU-_UqyJGO",
            "https://drive.google.com/uc?export=view&id=1Dw9Q-CMq8sJr3WMzCcHaewttwE_EZ843",
            "https://drive.google.com/uc?export=view&id=19nMEb4GbXmhamAi4C7PkO7TzNsliGZbp",
            "https://drive.google.com/uc?export=view&id=1RxiJ1TFqSnrc4BbRQJztNdHHb1yxNPVI",
            "https://drive.google.com/uc?export=view&id=15emP9zJWuqcoiF2RUwPFDrM65-eAIBlg",
            "https://drive.google.com/uc?export=view&id=1xwuI93TkMW0FXBJiwuCBNS9WriOPR8WE",
            "https://drive.google.com/uc?export=view&id=17z90bblYltBP3Y502O7LfMgptOA7rdDR",
            "https://drive.google.com/uc?export=view&id=1hKqZKBD33-BJXILt6XdLT3yxrBxDosLy",
            "https://drive.google.com/uc?export=view&id=1o6s5FLw39HB_FAIupArStdqd2f5mToR5",
            "https://drive.google.com/uc?export=view&id=1CNCuf6AR3PbNbAHue_7LMEobd4Rb7Lv_",
            "https://drive.google.com/uc?export=view&id=1KOY5l8WzqTNoodr8BeQAfa7iRdL_lHBz",
            "https://drive.google.com/uc?export=view&id=1ITGD4VfoG5mbR3jmGFrIs0n6EetoHlI_",
            "https://drive.google.com/uc?export=view&id=12lZk7rrcFdFwVZpVf0GbjITu1Cf-GlIF",
            "https://drive.google.com/uc?export=view&id=1dNIzqV55GmMn5WUcXBsTu70ydf01hqvX",
            "https://drive.google.com/uc?export=view&id=1tvBRjqmiwYtFyR_HVwiHAx4XjmarHcWv",
            "https://drive.google.com/uc?export=view&id=1gKVJRxI1UmdPPJC1gKOLH3z4yoHJPmLC",
            "https://drive.google.com/uc?export=view&id=10sRISCl1pS2NxamSUaifQrvtFC26tGiu",
            "https://drive.google.com/uc?export=view&id=1UbZxNJfmCKSGytEJArFr8Sw3JHoj8ac9",
            "https://drive.google.com/uc?export=view&id=1oyB1czYrMR7rMVUiB0TH0CrW6jRm-5e4",
            "https://drive.google.com/uc?export=view&id=1g25VAN1rHeLDvQuc5hEtsGgHYKIgv_F-",
            "https://drive.google.com/uc?export=view&id=1QoPkmHKBA_9wwMbwKg-njgY196M--yt9",
            "https://drive.google.com/uc?export=view&id=1fFRqch5jKNdCbE5D8k3S6X3Lp7nbepI2",
            "https://drive.google.com/uc?export=view&id=1fFRqch5jKNdCbE5D8k3S6X3Lp7nbepI2",

        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "keren abiiss, baikk",  
                "pesan":"semangat kuliahnya bangg!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "cantikk bangettt suka liatin lama lama ga ngebosenin, kerenn",  
                "pesan":"semangat kuliahnya kak, semoga selalu diberi kemudahan"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "murah senyumm, baikk, maniisss bangett",  
                "pesan":"bahagia selalu kak, semangat kuliahnya!!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "sangat menginspirasi, baikk, kerenn abisss, murah senyummm",  
                "pesan":"semangat terus bang, semoga selalu diberikan kemudahan dan kelancaran dalam melakukan hal positif"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "keren, humblee, baikk",  
                "pesan":"semangat terus kak arien!"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Jona",
                "sosmed": "@daffahdynn_",
                "kesan": "asikkk, baikk, kerennn",  
                "pesan":"be happy bang dafa!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "humble banget, baikk",  
                "pesan":"tetep kece terus ya bang"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "cantikkk, humbleee",  
                "pesan":"semangat kuliahnya kak!!"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "jago ngodingg, cool abiisss",  
                "pesan":"semangat menjalani hari harinya bangg"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "baikk, murah senyumm, kerennnn",  
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
                "kesan": "baikk, ramahh, murah senyum",  
                "pesan":"semangat menjalani kuliahnya kakk!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "keren abiss, baikk, humbleee",  
                "pesan":"semangat banggg, makin gacor main badminton nyaa"# 1
            },
            {
                "nama": "ALi Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang 4 Nangka Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "baik, santai, asik",  
                "pesan":"semangat menjalani kuliahnya bang ali!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "lucuuu, kalemm, baikk",  
                "pesan":"bahagia selalu kakk!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"way kanan",
                "alamat": "untung",
                "hobbi": "scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "seruu, baikk, murah senyumm",  
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
                "kesan": "kalemm, baikk, humblee",  
                "pesan":"jangan lupa buat selalu bahagia kakk!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "asikk, humble, kalo ngobrol seru ngalir terus",  
                "pesan":"semangat terus menjalani kuliahnyaa"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_",
                "kesan": "seruu, baik, kalo ngobroll asikk",  
                "pesan":"semangat bangg, jangan lupa selalu bahagia"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "kalem, jago narii, baikk",  
                "pesan":"sehat selalu kakkk"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Belajar Front end",
                "sosmed": "@ihsan.myusuf",
                "kesan": "chill abisss, murah senyumm, seruu banget orangnya",  
                "pesan":"semangat terus menjalani kuliahnya bang"# 1
            },
            {
                "nama": "Kevin Antoni JUnior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Berdiri, Nyantai",
                "sosmed": "@kevinaj_",
                "kesan": "cool banget, baikk",  
                "pesan":"semangat bang, sehat selalu!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kalemm, baikk, imutt",  
                "pesan":"semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "seruuu, ramahh, ga expect kalo satu SMA",  
                "pesan":"Keep positive bang!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main futsal, voli",
                "sosmed": "@sidabutar.26",
                "kesan": "humoris, diem aja lucu, asikkk",  
                "pesan":"lucu terus ya banggg"# 1
            },
            {
                "nama": "Wuliano Wiliam Purba",
                "nim": "123450098",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngerjain soal matematika",
                "sosmed": "@liano.wlm",
                "kesan": "cool bener, kerenn, asikkk",  
                "pesan":"Tetap semangat bang!"# 1
            },
            {
                "nama": "Rewina Audiya Melvasari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Ratu dibalau",
                "hobbi": " Gambar doodle",
                "sosmed": "@rewinanaaa",
                "kesan": "baikk, lucuu, asikk",  
                "pesan": "bahagia selalu ya kak!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ucQjRI31LG16v4Gs_0SOhfShxdMgovq6",
            "https://drive.google.com/uc?export=view&id=1EUnei0qjIbRDM9kVInwFi8umXwkJr3dF",
            "https://drive.google.com/uc?export=view&id=1JQKVG-MZbxXAATmcbmI_jxVaBkU2FyNJ",
            "https://drive.google.com/uc?export=view&id=1eVnklpP_Nq-gK9fb4vrOnER0Kr_lfO0e",
            "https://drive.google.com/uc?export=view&id=1RcxHgsODvWqjPAUWKul0kLzzUzIaM3jD",
            "https://drive.google.com/uc?export=view&id=1ALY1StL5gl-1kB_YzlxWrk1pEZk4s5zO",
            "https://drive.google.com/uc?export=view&id=1J4Sv2k3tupCDEqOxknmi41s2LbhN2RDe",
            "https://drive.google.com/uc?export=view&id=1Uea4jeZvcGvLQCxrCnScGnf830d_MRVe",
            "https://drive.google.com/uc?export=view&id=16q0d864jNLImK_1HSWc6ld7Zg2acpWBd",
            "https://drive.google.com/uc?export=view&id=19cLeo4LDxoljvJjIJqq-X0Asce8_Rvx6",
            "https://drive.google.com/uc?export=view&id=12xl59ZyceGxW44-13bj-orEkLiH5n_2n",
            "https://drive.google.com/uc?export=view&id=11PX8QxoqfOQ1SXsrlEgpNnvHV99KC19m",
            "https://drive.google.com/uc?export=view&id=1pEic_LbOHzpDaM5I0EMDtkEDc-l2mIqK",
            "https://drive.google.com/uc?export=view&id=1FpdqOPvKX458fZCPAb6AxP1PpK82cc-B",
            "https://drive.google.com/uc?export=view&id=14NCw-yc0BMgSSYS0fIBaeufwor69QdW-",
            "https://drive.google.com/uc?export=view&id=1WA0AB6AlWA6LRuk-30XkCU_P9xP4fYne",
            "https://drive.google.com/uc?export=view&id=18f3Trnru4g0ii_1LeyXNimpCMfqRPNuu",
            "https://drive.google.com/uc?export=view&id=19iFEt0QBJCWdUj08dQi6G1Ax7cum9urn",
            "https://drive.google.com/uc?export=view&id=1cLI5iXKkE6Q8udrLgpfE1CetGpNLVid-",
            "https://drive.google.com/uc?export=view&id=1hWJS-tkLKZraRPOOiR6JOeZsfTHuzInT",
            "https://drive.google.com/uc?export=view&id=10tMblkjtzsu55X4lgq_TIsdgP5fySCc4",
            "https://drive.google.com/uc?export=view&id=1yCEoWGBZsFeRomIRVkNCiEV60ni59q2x",
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
                "kesan": "humble, baik banget orangnyaa",  
                "pesan":"jangan lupa istirahat bang, semangat kuliahnyaa"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "humble banget, baikk",  
                "pesan":"selalu kasih semangat tiap hari kakk"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "keren, berwibawa, baikk",  
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
                "kesan": "lucuu, kalemmm, imuppp",  
                "pesan":"stay positif kakk!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilafarizzii",
                "kesan": "kerenn bangettt, baikk, humbleee",  
                "pesan":"semangat terus banggg"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "baikk, humblee",  
                "pesan":"semangat kuliahnyaa, semoga selalu diberikan kelancaran!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik, nonton",
                "sosmed": "@notfall.s",
                "kesan": "asikkk, kerenn",  
                "pesan":"semangat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "baik, kalemm",  
                "pesan":"be happy kak"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "multitalent, cantikk, positif vibes",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keylashafi_",
                "kesan": "asikk, seruu, baik, murah senyumm",  
                "pesan":"semangat bangg, tetap jaga kesehatan"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "baikk poll, cantik, lucuu dann imuppp",  
                "pesan":"semangat ngedance nya kakk, keren terus yaaa"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "baikk, ramahh, humbleee",  
                "pesan":"semangat menjalani hari harinya kak!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"pesawaran, lampung",
                "alamat": "pesawaran, lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "kalem, sabar banget ngajarin praktikum",  
                "pesan":"semangat teruss kak!"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "baik, positif vibes",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa tidur"# 1
            },
            {
                "nama": "Tanty Widyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "lucuuu, suaranya imuttt, baikk",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "keren abiez, sepuh coding",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "baikk, imutt, kalemm",  
                "pesan":"semangat terus kuliahnya kak afifah!!"# 1
            },
             {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@i",
                "kesan": "asikk, humblee, ramah bangett",  
                "pesan":"semangat terus bang & keep humoris!"# 1
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "keren bangett, pinter, cool",  
                "pesan":"semangat terus kuliahnya, semoga diberikan kemudahan kuliahnya"# 1
            },
             {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "cantik dan lucuu bangettt",  
                "pesan":"semangat terus kuliahnya kakak cantik!"# 1
            },
             {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "asik, baik, dan seru",  
                "pesan":"semangat terus kak kuliahnya kak, kalo cape jangan lupa main ke embung!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren, baik, asikkk",  
                "pesan":"semangat terus bang kuliahnya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AXOaWPGT4YjUyYZH8j1iKa1c09K3GuF7",
            "https://drive.google.com/uc?export=view&id=1mNe4gWdNHnhWTQ7eqAV3ivZJAi_giYqb",
            "https://drive.google.com/uc?export=view&id=1rh6RuWKb5VdA_UFx8XwIw0ifGQRKaali",
            "https://drive.google.com/uc?export=view&id=1COhty31iMVhNRB3PZyqgslJiXqiKYkxE",
            "https://drive.google.com/uc?export=view&id=1WBMfCDWu9zUkina9v-bwpo2v6xtP8-_8",
            "https://drive.google.com/uc?export=view&id=1tG3o6pHdYSlh5SiCHybRbTIwwg1jTtLt",
            "https://drive.google.com/uc?export=view&id=18BkGzsz31p-hUqanbp_-ZRRRNbQOHEBa",
            "https://drive.google.com/uc?export=view&id=1kGgNt5WP5Y6Z3VMpL6Re9Ey7QzbaTzLK",
            "https://drive.google.com/uc?export=view&id=14MTPvwfhGoqz2lNpK144gy_xFqWySZSQ",
            "https://drive.google.com/uc?export=view&id=1SU3ZVR2w00zWuTBGsw84N2I8iWO9kOIk",
            "https://drive.google.com/uc?export=view&id=18M-U9n9xiMWgxvCJ-nY8EcKo7ux-lv_J",
            "https://drive.google.com/uc?export=view&id=1ShCe9tY-q4hCWp_9di1RzD7USRJUAwNO",
            "https://drive.google.com/uc?export=view&id=1-eQfu9qFmE6L1p0erYbI0rtSPPs09Z9U",
            "https://drive.google.com/uc?export=view&id=1rY0BoXQb4SXwN9iJBHVz-9Kazw_xDrpX",
            "https://drive.google.com/uc?export=view&id=1VcK_Ksv6aUJqwpy2JjkEBpw1OaAJGgRp",
            "https://drive.google.com/uc?export=view&id=1-yC5wew5bpAlB8fazZWzLW529MMMaPJN",
            "https://drive.google.com/uc?export=view&id=1baB8Q03is4-m1aK69F-PImAJdTqllfFR",
            "https://drive.google.com/uc?export=view&id=1pOtF8b3vNyMFQYZwb-o6fILa77jaTDgT",
            "https://drive.google.com/uc?export=view&id=1BqzsMoDDMV1rVdRp9hWMcok0NM9HvGJ9",
            "https://drive.google.com/uc?export=view&id=1g9A3YG-oZJijIvpNpLJhyJsW8TwJwSWF",
            "https://drive.google.com/uc?export=view&id=1wVJjkHKL_DtNNeZC1hpqyz53mkY-HH0q",
            "https://drive.google.com/uc?export=view&id=1gHN1GjhB-hEZY39eHbwHhfzwq0Q3jdT9",
            "https://drive.google.com/uc?export=view&id=13LwSaxFhvzVrpzUEBKQ0l6BbqTBuBNPi",
            "https://drive.google.com/uc?export=view&id=1aB9rSLkSZO2YHC57mAzIEbR9npClS2n-",
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
                "kesan": "humblee, berwibawa banget, positif vibes",  
                "pesan":"keren terus ya bangg!!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "asikk, baik, ramahhh",  
                "pesan":"Semangat terus kak!!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "sangat menginspirasi, baikk, cantikk",  
                "pesan":"semangat kak lombaa nyaaaa"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "baik, ramah, murah senyum",  
                "pesan":"Semangat terus kak kuliahnya kalo cape jangan lupa jalan jalan!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "baikk, humblee",  
                "pesan":"semangat bangg!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "lucuu, baikk, imuppp",  
                "pesan":"semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak santai, kalem",  
                "pesan":"Semangat terus kuliahnya mutt!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "kalem, cantik banget ga ngebosenin",  
                "pesan":"semoga lancar kuliahnya kak!!"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "keren, baik, asikkk",  
                "pesan":"Semangat terus bang jadi asprak dan kuliahnya!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "positive vibes, baikk, humble",  
                "pesan":"keep positive vibes kak!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "cantik banget, keren banget dutanya!",  
                "pesan":"Semangat terus kak dutaa & kuliahnya!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "lucuu, asikk bangettt",  
                "pesan":"ceria terus ya kak!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "baikk, asprak asikk bangett, murah senyumm",  
                "pesan":"semangat terus ngaspraknya bangg"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "asprakk the bestt, humblee",  
                "pesan":"semangat ngasprak dan kuliahnya kak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "asikkk, lucuu bangett, gemessss",  
                "pesan":"full terus ya kak energinyaaaa"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "keren banget, baik, humble",  
                "pesan":"Semangat terus bangg kuliahnya!"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "chill abisss, asikk bangettt",  
                "pesan":"semangatt terus banggg"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kalem dan baikk!",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak imut, gemes bangettt!",  
                "pesan":"Semangat terus kakakk kuliahnya!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak cantik bangettt, kerennn!",  
                "pesan":"semoga dilancaran segala yang dilakukan ya kakk"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Kakak kereeen bangett, baikk dan cantik bangettt!",  
                "pesan":"Semangat menggapai cita-citanya!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "baik banget kak, humblee bangett",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "keren dan cool abiissss",  
                "pesan":"Stay cool bang!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "kak tari bai banget, sabar banget, humblee",  
                "pesan":"Semangat kuliahnya kak dan semoga dilancarkan untuk segala yang dihadapi kak!"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iTeKPr_YaM4ErOLQ5OvXvG5zMxZk6mGT",
            "https://drive.google.com/uc?export=view&id=1lQkHOWCfWcU1eoha0rRKbuzMvOuiZ8l5",
            "https://drive.google.com/uc?export=view&id=1K5Up1ZjivVlVDY7DrqDPE4uEDx2duZyw",
            "https://drive.google.com/uc?export=view&id=10Xwvd8zp1XqOpXVmor3oCz3UvB4pEt-t",
            "https://drive.google.com/uc?export=view&id=10qEFu7lpqpQoEpUEsI9-GHZ3vLIZS987",
            "https://drive.google.com/uc?export=view&id=1kUT9hgNpBOZiNIlNRAz_N2usru0e5BbC",
            "https://drive.google.com/uc?export=view&id=1WDEmSVK4_Y2XUN7hQljHVYr8ZUQDZEtx",
            "https://drive.google.com/uc?export=view&id=1_sgH49aOOXnb9EOWewYeLvx_epToqOO8",
            "https://drive.google.com/uc?export=view&id=1eFHm53el0vdc_Pvxi8kQCMn9wQGB0vtV",
            "https://drive.google.com/uc?export=view&id=11-oMwMDE6F-kQbR9ZvwMVbDoG7I_vpJU",
            "https://drive.google.com/uc?export=view&id=1DhgJIw-YyI9EZgWn4XyTy6wgVyr_bQ1U",
            "https://drive.google.com/uc?export=view&id=17Vxr6dBgt-zmnjzfAAiYJ69eXL2Qirz3",
            "https://drive.google.com/uc?export=view&id=1Bfl5WFDwXKf566Lu9XQadsGVnKI1FF-d",
            "https://drive.google.com/uc?export=view&id=1kLRHQCh4-FVkM5pV2I9zJ4u5BOaNZqup",
            "https://drive.google.com/uc?export=view&id=135BM6qPALm9sdRhUPhKUhybtBnsKCHQu",
        
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
                "kesan": "kalcerr, kerenn bingittttt",  
                "pesan":"semangat menghadapii semester akhirnya kakk"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "gemess, lucuu, humbleee",  
                "pesan":"semangat terus kaaakkk!!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@sal_fhn",
                "kesan": "positif vibes, baik, humblee",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "kalem, keren, baikk",  
                "pesan":"semangat menjalani hari harinya bangg"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "lucuuu, masyaAllah cantik bangett ",  
                "pesan":"semangat terus kuliahnya kakak cantikk!!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "cooll, keren banget, baikk",  
                "pesan":"semangat bang, jangan lupa istirahatt!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "lucuuu, gemess, baik bangettt",  
                "pesan":"semoga diberi kelancaran kuliahnya kak"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "kerenn, gacor banget",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Lampung Selatan",
                "alamat": "sabah balau",
                "hobbi": "nonton anime",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "baik banget, humbleee",  
                "pesan":"semangat terus kuliahnya bang naufal!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatriaaa",
                "kesan": "asikk, ramahh poll",  
                "pesan":"semangat terus bang, semoga kuliahnya lancarr!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "humoriss bangett, ga pernah ga lucuu, murah senyumm",  
                "pesan":"tetap selalu positif kak"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "baikk, imuppp",  
                "pesan":"semangat terus kuliahnya kak keren!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "asik banget, baikk, kalemm",  
                "pesan":"semangat terus kuliahnya bangg!"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Musik",
                "sosmed": "@sarahwsti",
                "kesan": "lucu banget kak, cantikk poll",  
                "pesan":"be happy kakkk!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "1234500",
                "umur": "19",
                "asal":"natar",
                "alamat": "pemda, way huwi",
                "hobbi": "main rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak cantik, baikk, dan humble bangett",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xqdXz0u3UCXJ8Mv6vZW0cOxQd_APceQt",
            "https://drive.google.com/uc?export=view&id=1OzHeao4LxkopcCniERdARcTQ8IqH6bi4",
            "https://drive.google.com/uc?export=view&id=1lbOhnSC_1J-OKZRyLvcukOI5T584SbRq",
            "https://drive.google.com/uc?export=view&id=1aW5wfXv9cV4QRHBf_8tCYfsjE9OtVP_b",
            "https://drive.google.com/uc?export=view&id=1vaCjUZd6jL-fv9mpSPm7bPiKPFYUiHBV",
            "https://drive.google.com/uc?export=view&id=1BZkJOg3Lnjp3RZuuCahCSLJYfekTBqjH",
            "https://drive.google.com/uc?export=view&id=1H6bGS49oSL1YkxEFcsikVjYlGuup93KH",
            "https://drive.google.com/uc?export=view&id=1QpGJxttCkLLDjzH6Btq-iW036Jp5UF5t",
            "https://drive.google.com/uc?export=view&id=1xfG1FTsolYAXVfqYywkaBvpZRDKvcNrB",
            "https://drive.google.com/uc?export=view&id=1-FOdWUAwH1kcmZpbbHMIsq9y8P8Qe-Ar",
            "https://drive.google.com/uc?export=view&id=19ROOZi5YqTDVu0MQfXYYK2dzh-rf9pPS",
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
                "kesan": "Abang keren role model banget",  
                "pesan":"semangat terus bang berinovasinya!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum, foto-foto pemandangan",
                "sosmed": "@den_iki__",
                "kesan": "Abang cool kece abiez photogenic",  
                "pesan":"stay cool bang!"# 1
            },
             {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik abis!",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
             {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini lucu dan seru",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
             {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Joggin juga",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak ini asik, seru",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang kalem, baik",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
             {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg perwira 2",
                "hobbi": "Nonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak ini asik lucu seru",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kakak lucu santai",  
                "pesan":"semangat terus masaknya kak!!!"# 1
            },
             {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak baik, lucu dan seru",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sK-hWVhDzWFuhtpu9bYiinnUE9sdAuP8",
            "https://drive.google.com/uc?export=view&id=19aN_-a5q4jKE4nEIqx-cFUqrYsuu9QVm",
            "https://drive.google.com/uc?export=view&id=1frtCxhuHGuss3-jScvgpJ3nN8Kj_X3lV",
            "https://drive.google.com/uc?export=view&id=1IfSizjiqAFnN39OL4BgcrOEjNgULJzes",
            "https://drive.google.com/uc?export=view&id=1K3jNA0ldTY8Wv9WXo-UBX_v0W8oat61E",
            "https://drive.google.com/uc?export=view&id=1WRYKinEr0lrIEyle0SJxwp2YmvNPxwSq",
            "https://drive.google.com/uc?export=view&id=1qKuWFqnUmUrNIUjeY5BPzDdqIsISIkys",
            "https://drive.google.com/uc?export=view&id=14XUOzAz41M9xO0196EPyiFTFxSnGNuGH",
            "https://drive.google.com/uc?export=view&id=1n3DUvb8WpRC20wugWH-Z3zRqOF5PiPyb",
            "https://drive.google.com/uc?export=view&id=1rdaIqTfgLYSTxar6q7AxfUBbS3tvrehT",
            "https://drive.google.com/uc?export=view&id=1Q_FUaIQQ9UgfHdkiUt6pqNrdX7B8wHwH",
            "https://drive.google.com/uc?export=view&id=1PtyYTXCltsKQAT-DZWFFukVM5OMZc1zN",
            "https://drive.google.com/uc?export=view&id=1F-Sxju9mDfPDcOi_VkjxwJDIcqzzATNK",
            "https://drive.google.com/uc?export=view&id=1h5F_dVKuoH5bTK95eCGikmKjipv9bSXZ",
            "https://drive.google.com/uc?export=view&id=1KDedtauIsXiKR4tDzfUe5S25FGeYM2If",
            "https://drive.google.com/uc?export=view&id=1MwD833d7kwLzKVETHYB4G-sfSMpBqHdP",
            "https://drive.google.com/uc?export=view&id=1sEvQFxFt0cW8MNAYXIOcvGTx2bAh-OfH",
            "https://drive.google.com/uc?export=view&id=1gp5gIUMHG09EzgUpvCiu64-sVnciOlJj",

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
                "kesan": "Kakak cantik, slay, seru, dan energik",  
                "pesan":"semangat terus jadi kadep nya kak patricia!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jl. Kresna Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini seruuu!",  
                "pesan":"semangat teruss kakak rahma!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard & Volly",
                "sosmed": "@mananam_",
                "kesan": "Abang Kadiv cool & kece abiez",  
                "pesan":"Sukses terus bang!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik & fotografi",
                "sosmed": "@noerruu",
                "kesan": "Abang kece dan fotografer abis",  
                "pesan":"Semangat terus bang jadi pdd buat HMSD ADYATAMA!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Abang Gokill dan keren parah!",  
                "pesan":"Semangat terus bang & Sukses terus!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak imup & Seru",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {   
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak kadiv kece dan keren abiez",  
                "pesan":"semangat terus jadi kadivnya kak!"
            },
            {
                "nama": "Aliya Anmara Amanta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammra",
                "kesan": "Kakak cantik & Calm",  
                "pesan":"Keep positive dan semangat terus kak!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini asik & pintar",  
                "pesan":"semangat terus kuliah dan jadi astut nya kak!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kakak slay, dan keren",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak cantik & kece",  
                "pesan":"Tetep Kece terus kakk!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumateraa Barat",
                "alamat": "Jl. Lapas, Kecamatan Jati Agung",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa_",
                "kesan": "Kakak cantik dan keyenn",  
                "pesan":"Semangat terus kak semoga tercapai segala cita-citanya!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak baik, dan keren",  
                "pesan":"semangat terus main robloxnya kak!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangg kadiv terkeren, kece & cool abiez",  
                "pesan":"Semakin mengudara dan semangat terus bang!!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kerennn banget pokoknya kaka ini",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
                        {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kakak kece dan vd banget!",  
                "pesan":"semangat terus nge-designnya kak!!"# 1
            },
                        {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kerennn & kece banget designnya kakak ini",  
                "pesan":"semangat terus kuliah dan sukses terus kak!"# 1
            },
                        {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "KAKAK VD TERKEREN & SLAY & KACIW & DABESTT BANGET DEH POKOKNYA!",  
                "pesan":"SUKSES TERUS KAK, MAKIN JAGO DESIGNNYA, SEMANGAT TERUS KULIAHNYA KAK!"# 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
       

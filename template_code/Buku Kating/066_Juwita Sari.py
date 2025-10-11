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
            "https://drive.google.com/uc?export=view&id=1vre_wOBhazV5flnH0OfrrRnS0l4jCq2A",
            "https://drive.google.com/uc?export=view&id=1ERF1fDz4bNnIVaxafaLzH6cESXSnZBbE",
            "https://drive.google.com/uc?export=view&id=1vbo6HjsVYiO6VDhUhOY_vbeNqnKYB2Cx",
            "https://drive.google.com/uc?export=view&id=1jGZYmoZT5iqY2EFsbj_lVhIe6JbRWmVB",
            "https://drive.google.com/uc?export=view&id=1ymzcji32wKr27eb8OJonI_XtQByFjNRX",
            "https://drive.google.com/uc?export=view&id=1SwEdstkA1M4B4JaAVI6H_2Aioo_gWiOp",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau Damar",
                "hobbi": "Ikut lomba burung murai",
                "sosmed": "@_erendraa",
                "kesan": "Keren, asik dan pastinya inspiratif",  
                "pesan":"Tetep jadi panutan yang chill ya bang!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren banget bang sampe nembus layar",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Ayres kost",
                "hobbi": "Jajan",
                "sosmed": "@celisabethh_",
                "kesan": "kakanya asik, bawaannya ceria terus",  
                "pesan":"bahagia selalu kak"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakanya jarang ngomong tapi vibesnya adem",  
                "pesan":"semangat terus ya kak"# 1
            },
            {
                "nama": "Eksanty F Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Kelagian Kecil, Pahawang",
                "alamat": "Pesawaran",
                "hobbi": "Ngambilin Lanyard",
                "sosmed": "@eksantyfebriana",
                "kesan": "asik dan ga bikin canggung",  
                "pesan":"jangan lupa istirahat kak"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Gya kost",
                "hobbi": "Cute",
                "sosmed": "@farahanumafifahh",
                "kesan": "asik, seru dan ga banyak ngomong juga",  
                "pesan":" semangat kak, jangan lupa istirahat"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1an6iQ2ECBT07QTfa2DAkIUHyF-4IlqAe",
            "https://drive.google.com/uc?export=view&id=1JLMhIgpD8bHacJQ65_ZoVDQLkj0fDMHD",
            "https://drive.google.com/uc?export=view&id=1myTjFvqb3dlpP5WfhLNa2x-YpbRxYo-v",
            "https://drive.google.com/uc?export=view&id=1fkq0mXJQL861iMIKAiunBmptBCtJAbdI",
            "https://drive.google.com/uc?export=view&id=1OBNBCPmD17HFISSOA3HBuWsQjyqMVK1_",
            "https://drive.google.com/uc?export=view&id=1G9x0Hd0xG6IGle8b9u0ZvTHVDLyEd_x2",
            "https://drive.google.com/uc?export=view&id=1fBwkNx21sHIObSmzXCDUT8SHospPPiNt",
            "https://drive.google.com/uc?export=view&id=1vz6LIec_1pAkMcvJFISNQ4__eF81iGjA",
            "https://drive.google.com/uc?export=view&id=1NkgrBz8hZImKQ4zk5aJ21a8SDh6VtK1t",
            "https://drive.google.com/uc?export=view&id=1ehqxczXJL39SBn1pgiHLW0kSY2No2PlZ",
            "https://drive.google.com/uc?export=view&id=1UD06rF6LnawCibZu90ZZgpPHtCe77Vya",
            "https://drive.google.com/uc?export=view&id=1NjP1NVOHharDJmt-oXx79vRgXwOHffWf",
            "https://drive.google.com/uc?export=view&id=13K6rQqX5lWI7PkebF-JglITu6gi-zqPD",
            "https://drive.google.com/uc?export=view&id=14SraJv5R7VqEVpX84ESdxi3GOK6XZ4-U",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Tanjung Morawa",
                "alamat": "B2 no 2",
                "hobbi": "main volly bareng feby",
                "sosmed": "@jeremia_s_",
                "kesan": "Baik, Asik, pokoknya keren bang!",  
                "pesan":"Tetep jadi orang keren itu ya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "kalo badmood liat zaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "kakanya baik, kalem dan ramah ",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin Alat Pancing",
                "sosmed": "@renishapg",
                "kesan": "baik, santai, ga banyak ngomong",  
                "pesan":"semoga hari harinya berjalan baik"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Wakatobi",
                "hobbi": "Bowling",
                "sosmed": "@",
                "kesan": "baik, ramah dan sopan",  
                "pesan":"semnagat kuliahnya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "baik, dan pinter banget si bang",  
                "pesan":"jangan lupa istirahat"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Wai huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "kalem tapi asik pas diajak ngobrol",  
                "pesan":"semoga banyak hal baik yang akan datang"# 1
            },
             {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "asik dan bawaannya ceria terus",  
                "pesan":"sehat selalu bang"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain Makanan Baru",
                "sosmed": "@myrrinn",
                "kesan": "baik, asik dan keliatan santai",  
                "pesan":"semangat terus bang!"# 1
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "ngumpulin batu unik dipantai",
                "sosmed": "@berlyyanda",
                "kesan": "baik, asik, dan ramah",  
                "pesan":"semoga hari harinya menyenangkan ya kak"# 1
            },
             {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "20",
                "asal":"Teluk Mondawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "baik, santai dan adem dipandang",  
                "pesan":"jaga kesehatan kak"# 1
            },
             {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Wai huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "baik, asik dan ceria",  
                "pesan":"semangat terus kak"# 1
            },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "keliatan sopan dan santai",  
                "pesan":" semoga lancar terus urusannya "# 1
            },
             {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin ka wawa ngomong",
                "sosmed": "@fer_yulius",
                "kesan": "asik, baik dan ceria",  
                "pesan":"semangat kuliah bang"# 1
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML hero semua franco",
                "sosmed": "@Monica_tjg",
                "kesan": "baik, asik dan bawaannya bahagia terus",  
                "pesan":"selalu jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@",
                "kesan": "belum sempet ngobrol banyak, tapi keliatan baik dan asik orangnya",  
                "pesan":"jangan lupa istirahat kak "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


# Tambahkan menu lainnya sesuai kebutuhan

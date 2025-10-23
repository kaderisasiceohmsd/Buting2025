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
            "https://drive.google.com/uc?export=view&id=1zp6VWy9DeIQkWwoUUymhrx7b3V8S70tx-",#1 bang rendra
            "https://drive.google.com/uc?export=view&id=1BdgfSiaj2_DZuhcXL4wKUd4GrbDZHZut",#2 bang jo
            "https://drive.google.com/uc?export=view&id=1XCtwVUPJ7NpccoSI0r92j8ThSreQy3DB",#3kak elisabeth
            "https://drive.google.com/uc?export=view&id=1zd9w3nbXeeFwlLuoWxcVGpOM7l2aBY_a",#4 kak eksanty
            "https://drive.google.com/uc?export=view&id=1v-BGfYwYJa02Am8BxeDTlonkbdcOHRTf",#5 kak farahanum
            "https://drive.google.com/uc?export=view&id=1jqt4j07foAe6H-odGXWaNkUxzr7sCBGz",#6 kak puspa
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau Damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Abangnya baik banget",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Johannaes Krisjon Silitong",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Style bang jo keren banget",  
                "pesan":"semangat terus kuliahnya bang!"# 2
            },
             {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airas Kost",
                "hobbi": "Nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya seruuu dan caantik bangett",  
                "pesan":"semangat kuliahnya kakak cantik!"# 3
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal":"Borneo, Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "Ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya jail tapi lucuu",  
                "pesan":"semangat kakk!"# 4
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumamtera Barat",
                "alamat": "Kiya Kost",
                "hobbi": "Domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak cantik bangett!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya positive vibes bangett!",  
                "pesan":"Semangett terus kak pancarkan aura positive vibes ituu!"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ab5P1st2pklMcOuDW7VyypDDiToc_knW",#1 BANG JEREMIA
            "https://drive.google.com/uc?export=view&id=1PmH_uOdlbihptrJh_IUugA0TfF0JvwWZ",#2 KAK DHEA
            "https://drive.google.com/uc?export=view&id=1C0--aFzi5vC6vuM0KL6L5C4T2BPMpMu_",#3 KAK RENISHA
            "https://drive.google.com/uc?export=view&id=1PT-HPU5KgsFWV2bcRZqs14gM3wmoaMu3",#4 KAK ANISA
            "https://drive.google.com/uc?export=view&id=1jML6EWaQ1OB1pUIra5uC2vEhRnRyqNiE",#5 BANG DHARU
            "https://drive.google.com/uc?export=view&id=1xyI_Koadz_T_1nhJ4BWE60kMVKlYfmFy",#6 KAK FEBY
            "https://drive.google.com/uc?export=view&id=1YSDM2epbhN9sA-7bUVZ-etPmE_epK74V",#7 BANG GIVARO
            "https://drive.google.com/uc?export=view&id=1AiDjz9uIqAWyiaDuJUG2XAmbeKeBpMjF",#8 BANG MIRZAN
            "https://drive.google.com/uc?export=view&id=1dC_DB81-L0QXkqI1logUeiE1N2bohlK3",#9 KAK BERLIANA
            "https://drive.google.com/uc?export=view&id=1HmFQd72gL24IwZOHZBIq4lXf_GpNhThr",#10 KAK JUE
            "https://drive.google.com/uc?export=view&id=13PeJL91C0xqWnwnrT9vTptQZ2ZFFB8V_",#11 BANG RIDHO
            "https://drive.google.com/uc?export=view&id=1Jw4iTRv-duIlXm3lhBDMjZx2e9Hpoipg",#12 BANG FERDI
            "https://drive.google.com/uc?export=view&id=1t_MccxfK3bwBDVodMBkZk_iP_ZoXOu1M",#13 KAK MONICA
            "https://drive.google.com/uc?export=view&id=19WklJSpfVZc1-Pe6GTnuOU6Q-jInpGEv",#14 KAK WAWA
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Merawa",
                "hobbi": "Suka main voli sama feby",
                "sosmed": "@jeremia_s_",
                "kesan": "Aabangnya humoris banget suka becanda terus",  
                "pesan":"Mau liat sidang bangg"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
             {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Suka banget liat kakanya keren sama cantik bangett",  
                "pesan":"Aku suka liatin kakaknya kalo papasan soalnya cantik bangett"# 3
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Wakatobi",
                "alamat": "Bandar Lampung",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Kakaknya seruu banget",  
                "pesan":"semangat kuliahnya kakk!"# 4
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way Halim Bandar Lampung",
                "alamat": "Way Halim Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Keren banget abang tutor lmd",  
                "pesan":"Semangat nutornya bang!"# 5
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "Suka liat rambut kakaknya, lucu",  
                "pesan":"Mau liat cat rambut kak Feby selanjutnya!"# 6
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Abangnya seru banget",  
                "pesan":"sering liat abangnya dimana mana"# 7
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya seru bangett",  
                "pesan":"semangat terus kuliahnya bang!"# 8
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya seruuu dan caantik bangett",  
                "pesan":"semangat kuliahnya kakak cantik!"# 9
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal":"Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kak Jue humbel banget",  
                "pesan":"semangat kuliahnya kak jue!"# 10
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Seru banget abangnya",  
                "pesan":"Semangat terus bangg!"# 11
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Abangnya seru bangett",  
                "pesan":"Semangett terus bangg!"# 12
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ml, only franco" ,
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya lucuu bangett",  
                "pesan":"Semangett terus kuliahnya kakak cantik"# 13
            },
             {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin ",
                "sosmed": "@nshaysk",
                "kesan": "Gemes banget liat kak wawa",  
                "pesan":"Suka banget liatin kak wawa, semangat kuliahnya kakk"# 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]   
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Belajar",
                "sosmed": "@bintangtwinkle",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": " ",
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
# Tambahkan menu lainnya sesuai kebutuhan

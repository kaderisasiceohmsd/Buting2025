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
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
             

        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"jawa barat",
                "alamat": "korpri",
                "hobbi": "mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": " ",  
                "pesan":" "# 1
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "belwis",
                "hobbi": "ngekader 24",
                "sosmed": "@allyapasha_",
                "kesan": " ",  
                "pesan":" "# 1
            },
              {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangsel",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": " ",  
                "pesan":" "# 1
            },
           {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"5 km dari pantai kedu",
                "alamat": "deket kost bang dapa",
                "hobbi": "cari kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "  ",  
                "pesan":" "# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"rahim ibu",
                "alamat": "samping kost arienta",
                "hobbi": "jahilin yulia",
                "sosmed": "@daffahdynn_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": ": @ginda_mrp",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "19",
                "asal":"lubuk linggau",
                "alamat": "kost putri gerbang barat",
                "hobbi": "ngitungin duit",
                "sosmed": "@natasyamavisca",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Samping kost kak alya",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumbar",
                "alamat": "",
                "hobbi": "ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "vany salsabila putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"palembang",
                "alamat": "airan raya",
                "hobbi": "ngoding di macbook",
                "sosmed": "@vany.salsabilaa",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@shahid22_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Sukarame",
                "hobbi": "Main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way dadi",
                "hobbi": "tidur",
                "sosmed": "@feraztaaa",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": " 123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi": "Main Video Game",
                "sosmed": "@sahid_maul19",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakrta",
                "alamat": "Korpri",
                "hobbi": "Ngerjain tugas",
                "sosmed": "@ahmadnoval_11",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas raya no.55",
                "hobbi": "Koleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Belwis, Pmeda",
                "hobbi": "Gangguin kak Dea",
                "sosmed": "@ihsan.yusuf",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": " 123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Ngomongin kak Dea",
                "sosmed": "@kevinaj_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan ",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nyuru Kak Dea diam",
                "sosmed": "@ridwan122",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ullianowlm",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Ibu kota Lampung",
                "alamat": "Way kandis",
                "hobbi": "Cari GPT",
                "sosmed": "@rewinanaaa",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

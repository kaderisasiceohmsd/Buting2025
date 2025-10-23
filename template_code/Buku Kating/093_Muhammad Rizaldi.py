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
            "https://drive.google.com/uc?export=view&id=1A5yYu6svP_hy2MeQOEouoZxXRzUqPXOI", #bang rendra   
            "https://drive.google.com/uc?export=view&id=1i-z2Ow7nNhU6XRTZkMBDjn9VPSBEA9DM", #bang johannes
            "https://drive.google.com/uc?export=view&id=1c1l48A9j4UKdyWe1y0Ojlb_8kNSvYyUU", #kak elisabeth
            "https://drive.google.com/uc?export=view&id=1W9EIsAk1CVPJJtjZbeDyQnxsYTEwyN22", #kak syadza
            "https://drive.google.com/uc?export=view&id=1Lwo49Rpaujy3tvmyB41Ys3TmR65kRJKa", #kak eksanti
            "https://drive.google.com/uc?export=view&id=1BeAglwl5IcIe-XTCX63qe2CvUJ2cxI8T", #kak farahanum
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Bang Rendra keren sama humble banget",
                "pesan": "Semangat kuliahnya nya bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang jo style nya kece abiez",
                "pesan": "Semangat kuliahnya ya bang"
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "kak Elisabet lucu banget seru deh pokoknya",
                "pesan": "Semangat kuliahnya kakak :) "
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza asik banget",
                "pesan": "Semangat terus ya kakak "
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanti lucu, kocak, heboh, seru puoll",
                "pesan": "Tetap jadi kocak yups kak's "
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak Farahanum juga lucu dan kocak banget, klop banget ama kak eksanty ",
                "pesan": "Semangat terus yupss kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang jeremia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak dhea
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak renisha
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak anisa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang dharu
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak feby
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang givaro
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang mirzan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak berliana
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak juesi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang ridho
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang feryadi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak monica
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak nashwa
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
                "kesan": "Bang Jeremia orangnya seru banget!",
                "pesan": "Semangat terus kuliahnya Bang, sukses selalu!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak Dhea punya vibe kalem tapi lucu banget!",
                "pesan": "Tetap semangat ya kak Dhea, jangan sering badmood hehe!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha selalu ceria dan kreatif banget!",
                "pesan": "Terus tebarkan semangat positifnya kak Renisha!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Kak Anisa asik banget!",
                "pesan": "Semangat terus kuliahnya kak Anisa, sukses selalu!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Bang Dharu santai tapi rajin banget!",
                "pesan": "Tetap semangat dan terus belajar hal baru ya Bang!"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "Kak Feby rame banget dan bikin suasana hidup!",
                "pesan": "Terus ceria dan semangat terus ya kak Feby!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro kalem dan seru!",
                "pesan": "Semoga selalu tenang semangat kuliahnya Bang!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan pecinta kuliner sejati !",
                "pesan": "Jangan lupa traktir teman-teman kalo nemu makanan enak ya Bang hehehe!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kak Berliana unik banget dan punya hobi yang keren!",
                "pesan": "Terus jadi pribadi yang berwarna dan inspiratif ya kak Berliana!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kak Juesi suka galau tapi tetap ceria di depan teman-teman!",
                "pesan": "Semangat terus ya kak Juesi, jangan galau terus hehe!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho keren banget dan punya aura positif!",
                "pesan": "Semangat terus ya Bang Ridho, sukses di setiap langkah!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Bang Feryadi lucu banget dan suka bercanda!",
                "pesan": "Jangan bosen dengerin Wawa ya Bang haha!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica pro banget kalau udah main ML!",
                "pesan": "Semangat terus push rank-nya kak Monica!"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa punya aura calm dan adem banget!",
                "pesan": "Tetap jadi pribadi yang menenangkan ya kak Nashwa!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang bintang
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak nadya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak fathinah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak lia
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
                "kesan": "Bang Bintang rajin banget dan selalu semangat belajar!",
                "pesan": "Semangat belajarnya Bang!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kak Nadya santai banget dan punya selera musik yang bagus!",
                "pesan": "Semoga hari-hari kakak selalu penuh lagu yang menenangkan ya kak!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah suka bengong tapi tetep lucu banget!",
                "pesan": "Tetap santai tapi jangan kebanyakan bengong ya kak hehe!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Lia chill banget dan suka tidur di waktu yang pas!",
                "pesan": "Semangat terus kuliahnya kak Lia, tapi jangan kebanyakan tidur ya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
    
elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang frdy
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak nisrina
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak allya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang ahmad rizky
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak arienta
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang daffa hadyan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang fajar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak natasya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang nobel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang aji
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak vany
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang sahidin
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang aristo
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang gusti
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak kharisma
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak rosalia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang sahid
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang daffa ahmad
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak erma
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang ihsan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang kevin
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak lidia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang ridwan
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang ulliano
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang benget
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang rewina
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
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Ahmad Rizky",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Arienta Khusnul Ananda",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "vany salsabila putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

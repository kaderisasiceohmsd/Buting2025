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
            "https://drive.google.com/uc?export=view&id=1vvJCNrFTal3F14mKT93iak2rtqvBGqxj",
            "https://drive.google.com/uc?export=view&id=1y6YzkTaxD-E-6Bu7c30tPPuS7Nib8sFg",
            "https://drive.google.com/uc?export=view&id=1890a3zXJ3o1juhfbG-i69InwDXpnGMLH",
            "https://drive.google.com/uc?export=view&id=1RIJl5WPLsetjdKAIaD1yi2voshf1ttlJ",
            "https://drive.google.com/uc?export=view&id=14xl25qARFPSox2JdD7R__4eVu2C6GUQU",
            "https://drive.google.com/uc?export=view&id=19a6duvnYNjzSGUuPMRMuhRwjlwtWZ8BV", 
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
                "kesan": "Abang ini seru banget,kece abizz",  
                "pesan":"Semangat Bang jadi Kahim, semoga bahagia selalu!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL!",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "gacor abis bang joo",  
                "pesan": "semangat trus bang"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Badui",
                "alamat": "Ayrest Kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "lucu kakanya",  
                "pesan":"jangan sering sering nahan pipis kak"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza keren dan kece kakanya",  
                "pesan":"semoga sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik dan seru",  
                "pesan":"sukses teruss kak"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini lucu",  
                "pesan":"semoga suksess terus kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KFrxF-sEaMQWKUJWZn1GuFlfY5bsfnRd",
            "https://drive.google.com/uc?export=view&id=1CTWff_lpUsMmdED-Jp0SzOMUDKnT_Xsz",
            "https://drive.google.com/uc?export=view&id=1xeliVrLoQ2vN20wTPVy_bRnTYFy5KXFb",
            "https://drive.google.com/uc?export=view&id=18qpsPGcsiE3cLfAdJg5a9iHVObfOFCHa",
            "https://drive.google.com/uc?export=view&id=1ENIVHFRQLMDJ4QsuCCm109AmCcCj34UW",
            "https://drive.google.com/uc?export=view&id=13OpwmQVk7QsWZ1Dw-FujQa5-S0P6AIZL",
            "https://drive.google.com/uc?export=view&id=1GoVupio4hc7-PP6eOTnudIkAJKgxdEIg",
            "https://drive.google.com/uc?export=view&id=1v4gotweJ8rhkB_KmJdIfAJnYpp4NALyW",
            "https://drive.google.com/uc?export=view&id=1K3xhE53b3jqQLmC7zb9lsHxflGIQbgtA",
            "https://drive.google.com/uc?export=view&id=1USjHn18kg27SJnr_aG2FRYiH1KjjYd9M",
            "https://drive.google.com/uc?export=view&id=1AJWI6dDkaLtK-OZAxkboTWdRSD8CKLJL",
            "https://drive.google.com/uc?export=view&id=1C4LlbLQ02712kmqEZTX1p2EFxge2hQry",
            "https://drive.google.com/uc?export=view&id=1ZRyHgqU8JWfcv-prsd1RYT7IkmqrYyBt",
            "https://drive.google.com/uc?export=view&id=1ed1RIQt0YxMeu8bu0UTTGx6QzYXhtS7I",
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
                "kesan": "heboh abis orangnya",  
                "pesan":"semangat bang kuliahnya"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea kece",  
                "pesan":" Sukses terus kakk!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "kakak keren dan seru",  
                "pesan":"bangun kakk"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya kece",  
                "pesan":"Sukses terus kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "cool abiezz",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini lucu, keren abis",  
                "pesan":"semangatt teruss kuliahnya kak feby"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "selalu siap sedia membantu anopa, keren, kece, baik hati, tidak sombong. cihuyy",  
                "pesan":"semangat dan sehat selalu abangdaa"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "keren banget kakanya",  
                "pesan":"semangat trus kuliahnya bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Catur",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini keren",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandiama",
                "alamat": "Way Huwi",
                "hobbi": "Minum air putih 8x sehari",
                "sosmed": "@j__eesie",
                "kesan": "keren, kece abiz kakanya",  
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
                "kesan": "abang cool, keren",  
                "pesan":"semangat trus nyanyinya bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Koleksi Stiker",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini chill, keren",  
                "pesan":"semangat trus kuliahnya bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Papua Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik, humoris",  
                "pesan":"semangat terus kak monica kuliahnya"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini keren abis",  
                "pesan":"semangat terus kak nashwa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bbwTvgbE0GOTmwdNyJCGyEcncHmaTYhU",
            "https://drive.google.com/uc?export=view&id=1jPUQWFCY4gVhA_J8ka2og2Cd4TRe4-_W",
            "https://drive.google.com/uc?export=view&id=1BBPjGLRbPtYbiJshlayjArFMSBVS5A_9",
            "https://drive.google.com/uc?export=view&id=1qky1Mr5O5dR4AxICMbbDnQ7syKdLDLAQ",
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
                "kesan": "keren public speakingnya, tenang bawaan orangnya",  
                "pesan":"semangat terus bangg senatorr"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu, maen roblox",
                "sosmed": "@nadyaanjanani",
                "kesan": "Kakak ini asik, baik",  
                "pesan":"semangat terus kuliahnya kak nadya"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Ice Skating",
                "sosmed": "@fathinahazzh",
                "kesan": "kece, keren abiz kakanya",  
                "pesan":"bahagia selalu kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "kakaknya keren, seru banget",  
                "pesan":"semangat terus menjalani kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qQStrmLcb0MbzEomKROvhOw7KTBZjxDb",
            "https://drive.google.com/uc?export=view&id=19h8kmiITgUz6iSqAR31JxfarjQby5ndP",
            "https://drive.google.com/uc?export=view&id=1dk2UtoTS39vnkf_hZpybd_V8ICVdagHI",
            "https://drive.google.com/uc?export=view&id=16KwDJ42M1mVHXN4gW4Li-uXgXQup5JY9",
            "https://drive.google.com/uc?export=view&id=1nk1sSp5M3A84ZbxJsUHnU40mSlzZMRyP",
            "https://drive.google.com/uc?export=view&id=1_WF0osGrBHppPxhS56FsRSUngWCuvieX",
            "https://drive.google.com/uc?export=view&id=10kB-kc6sED60jDt6SBcuTjbeN4PNtyaK",
            "https://drive.google.com/uc?export=view&id=1_Dyvp_QUn5Wzm8uPNeWoQP8Lt7zpUYTv",
            "https://drive.google.com/uc?export=view&id=1kqi1-xcEFzrQThCE-7FEmlF1gY1OICBz",
            "https://drive.google.com/uc?export=view&id=1MZit5TboYaL-IiwoijMCcdcqVromfMmq",
            "https://drive.google.com/uc?export=view&id=1zchjp-YqT8SQJqzZUJxSWS3vvHvvRf_N",
            "https://drive.google.com/uc?export=view&id=1mrJjPWVD2fHd6890pb5JN4gB5I5jTb8E",
            "https://drive.google.com/uc?export=view&id=1KZXv2_RzU55C12NyJacrNlljMJSJz9L5",
            "https://drive.google.com/uc?export=view&id=1tim84xOkvykzLXRjM7OTF5WkiLT3h4Ab",
            "https://drive.google.com/uc?export=view&id=1456TZur3bkYED1rRKgUIvk29zloWQuPC",
            "https://drive.google.com/uc?export=view&id=1lKOYFl_7sFoxGHeVOUlbVMdStR2SyeYz",
            "https://drive.google.com/uc?export=view&id=1Wevh3e6Yg7aE0Bd7KQz4zaOyuRNKcbYn",
            "https://drive.google.com/uc?export=view&id=1BiZqlmsBIhEsxEK1x-OJ5MiB215Hihi3",
            "https://drive.google.com/uc?export=view&id=1N1TyJviWHMFxDnGw79HgdJYSs2bY5le7",
            "https://drive.google.com/uc?export=view&id=1GQGHZcvyT-7d74sDBLqzkNNMHXDevB2_",
            "https://drive.google.com/uc?export=view&id=1DAS1DGH_qe1__Ju78mNUdG_ypd2NfKvn",
            "https://drive.google.com/uc?export=view&id=1OuNPkHnvJtyGKfwa6oWT4AO9PlmnPdpQ",
            "https://drive.google.com/uc?export=view&id=1iFhSN_CC15jDQBBfscad2l4u4-Uk-PC9",
            "https://drive.google.com/uc?export=view&id=1DyQwqbcjSSqSZcHHl6OOGFzb_NThaRwd",
            "https://drive.google.com/uc?export=view&id=1bnvgpykXW41KUwS_M51o2N7Oa3S6FBc7",
            "https://drive.google.com/uc?export=view&id=1P0DHpfnKzpXeTbwmdSS5BQ15rxAdv77G",

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
                "kesan": "Abang cool abiez",  
                "pesan":"semakin cool dan kece bangg"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "keren banget kakanya",  
                "pesan":"semangat teruss kakk"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "kritis banget orangnya, kecee",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "keren abis abang ini, tenang orangnya",  
                "pesan":"semangat terus bang ahmad kuliahnya"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakak ini stylish, keren",  
                "pesan":"semangat terus kak arienta"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "tegas orangnya, keren abiz",  
                "pesan":"tetep humble bangg"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "cool abis, baik banget abang ini",  
                "pesan":"semangat trus kuliahnya bang fajarr"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "keren abis kakanya, kece",  
                "pesan":"semangat terus kak natasya jadi bendaharanya"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "tegas abangnya, cool, keren pokoknya",  
                "pesan":"tetep gitu, jangan berubah bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "keren abangnya, banyak motivasi, ngasi contoh baik",  
                "pesan":"semangat terus bangg aji"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang Berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "baik kakanya, seru pokoknya",  
                "pesan":"semangat terus kak vany kuliahnya"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "Abang kece santai, ga banyak gerakan",  
                "pesan":"tetep jadi keren bangg"# 1
            },
            {
                "nama": "ALi Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang 4 Nangka Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "Abang baik, santai, kece abis",  
                "pesan":"semangat terus bang ali kuliahnya"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini kalem, cool",  
                "pesan":"semangat kakk kuliahnya"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way kanan",
                "alamat": "untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak lucu seru, asyik",  
                "pesan":"semangat terus kuliahnya kak kharis"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakak ini asikkk, agak kalem",  
                "pesan":"semangat terus kakk, mabar roblox kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "Abang asik, baik, kece abis",  
                "pesan":"semangat terus bangg kuliahnya"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_",
                "kesan": "santai orangnya, keren",  
                "pesan":"tetep kece terus bang daffa"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "seru, asyik kakanya",  
                "pesan":"semangat terus kak jadi dancernya"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Belajar Front end",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abang Chill, skena, cool",  
                "pesan":"semangat belajarnya bang!"# 1
            },
            {
                "nama": "Kevin Antoni JUnior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Berdiri, Nyantai",
                "sosmed": "@kevinaj_",
                "kesan": "Abang ini asik seru gaul abis, kece",  
                "pesan":"tetep kaya gitu bangg"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "santai, asik kakanya",  
                "pesan":"semangat terus kak lidia kuliahnyaa"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Abang kocak, seru, santai",  
                "pesan":"Keep positive, semangat bang"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main futsal, voli",
                "sosmed": "@sidabutar.26",
                "kesan": "kece abis, keren bangnya",  
                "pesan":"Tetap semangat kuliahnya bang Benget"# 1
            },
            {
                "nama": "Wuliano Wiliam Purba",
                "nim": "123450098",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngoding",
                "sosmed": "@liano.wlm",
                "kesan": "Abang cool, dingin, asik",  
                "pesan":"Tetap semangat bang "# 1
            },
            {
                "nama": "Rewina Audiya Melvasari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Liat shoppe tapi ga beli",
                "sosmed": "@rewinanaaa",
                "kesan": "kalem kakanya, kecee",  
                "pesan":"sehat selalau kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Bn2vQHkwP72kHjyg-t8NLev96R9fz9w1",
            "https://drive.google.com/uc?export=view&id=1AIFI0h_nU__-6olZmA0oi1jOmeK1XELU",
            "https://drive.google.com/uc?export=view&id=16RqVdtPXaYsWB1m8zKcP1opnJaUVBfbY",
            "https://drive.google.com/uc?export=view&id=1i903K6HS3NvLVisdjH34kiroKpU_6KZ0",
            "https://drive.google.com/uc?export=view&id=1gEkfpXndvZQzUnnAq6yjsIY-5u9ojrwW",
            "https://drive.google.com/uc?export=view&id=1zSqpquYWSrbnKUxGla-eI0gfz2b5TRMO",
            "https://drive.google.com/uc?export=view&id=198hU00kcD2ZZBuYguTni3EGWCiAR_aki",
            "https://drive.google.com/uc?export=view&id=1Tec8guzH72axDE_KZku64iz6XcRNtGWU",
            "https://drive.google.com/uc?export=view&id=1y2CPLfCm7RFSwtR7wH3oxfY7vpOiROLe",
            "https://drive.google.com/uc?export=view&id=1BVcrasNCu1KcQOYM53pqjRsZUf4M1fw7",
            "https://drive.google.com/uc?export=view&id=1yH1DRhagEA8xdj9JJWhDdRi9b0LPpEGk",
            "https://drive.google.com/uc?export=view&id=11hx-PyXJFWykJQhuiTPxBCCQlTSsIlSp",
            "https://drive.google.com/uc?export=view&id=1sKNB063-HB93XCDYeZERoJE00aWCnbIu",
            "https://drive.google.com/uc?export=view&id=1NygOotj1ZWhIiILVwYCfvp19oIZxhW3J",
            "https://drive.google.com/uc?export=view&id=1x-sahSDnPB--zlyo-zD9nnF-NA5NSQxh",
            "https://drive.google.com/uc?export=view&id=1IjHcoD-WLlfLatDRHhjh1A04QLIgeu9l",
            "https://drive.google.com/uc?export=view&id=1_KpMnlrpp2b0gBAiIzTYMBkwCV0m5W65",
            "https://drive.google.com/uc?export=view&id=1xE-EDX3Zt2CJ_rrrl5WhNChhhyfkP_hy",
            "https://drive.google.com/uc?export=view&id=1P8vsfDQFSFGopHR6sYiDcFjiwjYzEzww",
            "https://drive.google.com/uc?export=view&id=1RS-RmuQQo-vAe87Nqufn77EB9OtRgkep",
            "https://drive.google.com/uc?export=view&id=1_cgflN_XLM8BFxSjemzbSGiThHB0gzFL",
            "https://drive.google.com/uc?export=view&id=1zr3fbH4KTup2BqdJyjWG11dpQrwQjNC9",
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
                "kesan": "Abangnya seru, asikk",  
                "pesan":"semangat berkembangnyaa bang"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "baik, seru kakanya",  
                "pesan":"semakin kece kak"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abang regi keren, berwibawa bang regi",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishashi",
                "kesan": "baik, seru kakanya",  
                "pesan":"semangat terus menjalani hari kak"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilafarizzii",
                "kesan": "keren, kece abangnya",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "keren,cool orangnya",  
                "pesan":"semangat terus ngebasketnya bang aqil"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik, nonton",
                "sosmed": "@notfall.s",
                "kesan": "Abang santai, seru",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak ini kalem dan kece",  
                "pesan":"semakin keren kak"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini asyik, keren",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keylashafi_",
                "kesan": "keren, asik, cool abangnya",  
                "pesan":"semangat bang menjalani hari"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak ini asik seru",  
                "pesan":"semangat terus menjalani hobinya kak"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini seru, asik pokoknya",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"pesawaran, lampung",
                "alamat": "pesawaeran, lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakak kalem, baik",  
                "pesan":"semangat teruss kak menjalani hari"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakak yang baik, santai, kalem",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Tanty Widyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kakak ini keren, asik pokoknya",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abang keren abiez, sepuh coding banget",  
                "pesan":"semangat terus nge project, ajarin R bang"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik, seru, baik",  
                "pesan":"semangat terus kuliahnya kak afifah"# 1
            },
             {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@i",
                "kesan": "Abang kece abis, gokil dah pokoknya",  
                "pesan":"semangat terus bang & keep cool & humoris bang fabio"# 1
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abang pinter, kalem",  
                "pesan":"semangat terus kuliahnya, by1 catur bang hehe"# 1
            },
             {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak lucu, keren,kece pokoknya",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
             {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik, baik, dan seru abizze",  
                "pesan":"semangat terus kak kuliah"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abang kece, sepuh futsal",  
                "pesan": "semangat trus kuliahnya bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1asVLtacVKdKgiWGjbVsO-jezdDurkKlS",
            "https://drive.google.com/uc?export=view&id=19ia3zAviMWS19tJRtpOzkNlmfnV_k2oc",
            "https://drive.google.com/uc?export=view&id=12Bkc3K3CiMG_pTxf3dZ04JwkYHBMJ-55",
            "https://drive.google.com/uc?export=view&id=1z9OBIU-4xckgx0y1dC-Dv2RTVYNHVRJM",
            "https://drive.google.com/uc?export=view&id=1drJvwPtM2NX3R1_3vmyfS8gw_aenyIwE",
            "https://drive.google.com/uc?export=view&id=1I7DtX-jyQnTE649sB280Yl34Sr7__Ebp",
            "https://drive.google.com/uc?export=view&id=1O2uq6S73Q7OgpRMhogVSYRfuIK5gKsMT",
            "https://drive.google.com/uc?export=view&id=1gLEUfsnDiihd8JSzF22eiQX1zPc25J2m",
            "https://drive.google.com/uc?export=view&id=1RimHMZtO7A6HgCh9x_Hb5hSfuga4KkWt",
            "https://drive.google.com/uc?export=view&id=1hCZX1O4usBbXq0R8ch_r_8UmdmxWHs5D",
            "https://drive.google.com/uc?export=view&id=1gG-0mkgm1AiN_tKHb93wmDFzgiWXwa9C",
            "https://drive.google.com/uc?export=view&id=1JpxtrKfvl7YtNQYWM2hLFIwOzM1ebnuH",
            "https://drive.google.com/uc?export=view&id=1mDZ-ejQOhpcNji8Y9kJeFrqJ5jgZ1n6I",
            "https://drive.google.com/uc?export=view&id=1pThNC2h7xkW47ixMu5cVRRYMUwV4me4T",
            "https://drive.google.com/uc?export=view&id=1Prc-sG2pnB4leZsSUfBehpEFLdjVc01b",
            "https://drive.google.com/uc?export=view&id=1wL3Ez06MKeXB65Kfa4wMry_lpOljbM58",
            "https://drive.google.com/uc?export=view&id=1kBZftPbjYjghy_9IKF_yKrILLRNdhpCY",
            "https://drive.google.com/uc?export=view&id=1VGSVkDyQD0Ax8yFzSevHtNoyJYRaQycT",
            "https://drive.google.com/uc?export=view&id=1bVWPPKIhOb4Is0iu2c_p185t_oYpEnIC",
            "https://drive.google.com/uc?export=view&id=1t9NV5VIFaBwYjQYo0HbbfmGN8lvGyhD9",
            "https://drive.google.com/uc?export=view&id=1J2YYyWw660X7SFYxMNrncSQlouCP1ykw",
            "https://drive.google.com/uc?export=view&id=1QcsNqnymq4hqFXppHGFsdWYsKRypy0te",
            "https://drive.google.com/uc?export=view&id=17ILq8MJrBlzZJ_unFzCdINf-9etk5uEr",
            "https://drive.google.com/uc?export=view&id=1jLr1s41Vpcns8f7cPKOyfLrIMOVpoWB3",
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
                "kesan": "keren, asik abangnya",  
                "pesan":"Semakin kece bangg"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini seru asik dan gacor",  
                "pesan":"Semangat terus kak yohana"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak lucu,seru,asik",  
                "pesan":"semakin maju kak"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak baik, dan seru",  
                "pesan":"Semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "kece, humble abangnya",  
                "pesan":"Tetap semangat dalam segala hal bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak seru, baik, dan kalem",  
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak santai, asik",  
                "pesan":"Semangat terus kuliahnya, masi muda banget kak!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak baikk, dan kalem orangnya",  
                "pesan":"Semoga tercapai segala yang diinginkan kak"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abang santai & kalem",  
                "pesan":"Semangat terus bang jadi asprak dan kuliahnya"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak baik, seru, positive vibes",  
                "pesan":"Semakin positive vibes kak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya cantik banget, kece abis",  
                "pesan":"Semangat terus kak dutaa & kuliahnya"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya lucu dan positif vibes banget",  
                "pesan":"semangat trus kuliahnya kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "gacor abangnya, keren, baik abiss",  
                "pesan":"tetep kaya gitu ya bang"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak baik, seruuuu",  
                "pesan":"semangat trus kuliah dan ngaspraknya kak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakak baikk, dan kecee bener kakanya",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abang gacor, keren",  
                "pesan":"Semangat terus bangg kuliahnya"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Abang gacor, cool abiez",  
                "pesan":"semangat semangat bang menjelajahnya"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kalem kakanya, asik tapii",  
                "pesan":"Semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak imut, dan baik",  
                "pesan":"Semangat terus kakakk kuliahnya dan menjalani harinya"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak imut, keren dan kece",  
                "pesan":"Semangat Kak kuliahnya"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Kakak kece, keren abiz",  
                "pesan":"Semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kecee banget kak nurul",  
                "pesan":"Semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang keren dan kalem",  
                "pesan":"Stay positif dan kece abiez bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kak Tarisya kerenn bangett",  
                "pesan":"Semangat terus kak Tarisya, selalu bahagia!"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lTYYR5sccaRs9OgCTYjrCEz9_j1_Plfq",
            "https://drive.google.com/uc?export=view&id=1ZO0OJsSTCB4TXi0eLPT8yU6fFAtLoeJQ",
            "https://drive.google.com/uc?export=view&id=1gWleXr8u4RDuaxEUmx-Gqc-rzDU7oi8q",
            "https://drive.google.com/uc?export=view&id=1swYNUqJN7t2FYR9k8OON1PVwqU5LJ7bC",
            "https://drive.google.com/uc?export=view&id=1VNwqK-w9urc41Olkc02eI7Td-W4YjEwt",
            "https://drive.google.com/uc?export=view&id=15ooJ_LiQeivVC_Lcennf39jIkTN3_0ER",
            "https://drive.google.com/uc?export=view&id=1xqDJxzAO52Nwe1FDp4Z2RGzqYK9ZmcbL",
            "https://drive.google.com/uc?export=view&id=10fvcVi67QMs_ptX8tIEEFWfTIOAHiF3v",
            "https://drive.google.com/uc?export=view&id=1M_YJmh4NChr4yt3UuBnMuAq3ZZlFfADy",
            "https://drive.google.com/uc?export=view&id=1CR5Pojw9rAQv6WcPJDwnXJ_GyhlUCT9-",
            "https://drive.google.com/uc?export=view&id=1dYt88B8cDXvMizwPvn55037JsZX3NIrN",
            "https://drive.google.com/uc?export=view&id=109AGHAW0LjkbPiiIifIrC3XxM_XCOR5o",
            "https://drive.google.com/uc?export=view&id=1FrsnA6POiizpHft-GvCNwmjISZ3P2bC_",
            "https://drive.google.com/uc?export=view&id=1PDnGCp-pDvyRN0n-tBcEaB79uU3UaAb0",
            "https://drive.google.com/uc?export=view&id=1Ybwi4Kkk4FV78uEs3zv3pmcgFp9Mi_L3",
        
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
                "kesan": "keren abis kak rani, keceee",  
                "pesan":"semangat terus jadi kadepnya kak, bahagia selalu"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak kere,kece abizz", 
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
                "kesan": "keren kakaknya, seru abis",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "kalem abangnya, asik tapii",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakak ini asik, keren,kecee",  
                "pesan":"semangat terus kuliahnya kakak, bahagia selalu"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "cool, child abis abang ini",  
                "pesan":"tetep gacor bang!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini asik, seru pokoknya",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak ini lucu dan keren",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Lampung Selatan",
                "alamat": "sabahbalau",
                "hobbi": "nonton anime",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "abang kalem, santai bawaannya",  
                "pesan":"semangat terus kuliahnya bang naufal"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatriaaa",
                "kesan": "santai, keren, enak diajak ngobrol abang zai inii",  
                "pesan":"semangat terus kuliahnya bangg"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakak seru lucu humoris asik, mc kerenn",  
                "pesan":"tetap keren kak, semangatt"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "kakak seru, asik, ceria",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Abang kerenn jago futsal",  
                "pesan":"semangat terus kuliahnya bangg"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Musik",
                "sosmed": "@sarahwsti",
                "kesan": "kakak lucu seru, asikk",  
                "pesan":"semangat terus kuliahnya kakk"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda way huwi",
                "hobbi": "main rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak imut, santai, asik",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12k5Hx8rThMIyz7kr7ahxj0l_-8IFDBIR",
            "https://drive.google.com/uc?export=view&id=1oxS8sBbnpnJWufsYLtF9tqHyBuWDdBe1",
            "https://drive.google.com/uc?export=view&id=1ZVgy_eydvGfyz3oFNiWZc3gS-LnT9gya",
            "https://drive.google.com/uc?export=view&id=1X-pl5MIbe4hcrTUSaUnUhtekjzo_HOyf",
            "https://drive.google.com/uc?export=view&id=1NmXNaHimnpKCPmSJdVT-9kjGRxUluJ3t",
            "https://drive.google.com/uc?export=view&id=1lOiYpdFlUM-V1xTS1p9MVtOXmSd59y_C",
            "https://drive.google.com/uc?export=view&id=1TCs1rmffNOBHWOm7tifmGi5bDdk7NqOo",
            "https://drive.google.com/uc?export=view&id=1aSOjYSOu5stVk_CvqnzR8OqGcyvEQnjb",
            "https://drive.google.com/uc?export=view&id=1M68Bmu1NaxXGfXwXqjwEERdnATn23a03",
            "https://drive.google.com/uc?export=view&id=1Gbw-kTR6SSXPz_GzJWbnZ0eoJMuEavgB",
            "https://drive.google.com/uc?export=view&id=1F_51pFhAS-eWtu2pCUnvRBn1t_tOfWZ0",
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
                "kesan": "kerenn, kece abang ini, cool abis",  
                "pesan":"semangat terus bang danang kuliahnya"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini asik, seru abis",  
                "pesan":"Semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum, foto-foto pemandangan",
                "sosmed": "@den_iki__",
                "kesan": "cool, keren abis abang ini",  
                "pesan":"tetep keren bang"# 1
            },
             {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik abis, keren, seru abis",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
             {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini lucu dan seru abizz",  
                "pesan":"semangat terus kuliahnya kakak"# 1
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
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang kalem, baik, keren",  
                "pesan":"semangat terus kuliahnya bang dhafin"# 1
            },
             {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak keren, seru abiss",  
                "pesan":"semangat terus menjalani harinya kak"# 1
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
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
             {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kakak lucu santai, kerenn",  
                "pesan":"semangat terus masaknya kak"# 1
            },
             {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak baik, lucu dan seru abiss",  
                "pesan":"semangat terus kuliahnya kakak nydia"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1C_M4IQf1hD4mgp3g6d1U4t2cOji5RwiK",
            "https://drive.google.com/uc?export=view&id=1xpSsNCGBncdUbirflSbM4XxX9mq8bVex",
            "https://drive.google.com/uc?export=view&id=13PmPgu5jkSxflhdgJ0OmO0MjRvwa72-V",
            "https://drive.google.com/uc?export=view&id=1ta1xCtqYjJu03g_RcphxK_CZvpTjqrkY",
            "https://drive.google.com/uc?export=view&id=1vYzcbzsYWguV3OxT-0U4bIdP27Bo_49K",
            "https://drive.google.com/uc?export=view&id=1VEO9CDwqw77Lp3i46xa-76UzV98az7Jb",
            "https://drive.google.com/uc?export=view&id=1L-bC_u6uN6JIQUKC_-rQjZ_GKFmc2vwF",
            "https://drive.google.com/uc?export=view&id=1KCIiQq-Z7DnZbL-oEMptJJG6GRTQZJiM",
            "https://drive.google.com/uc?export=view&id=1kVNr2qe9XAJeIrDPqb7ahf9T6XU50r0O",
            "https://drive.google.com/uc?export=view&id=1Yr1KLKCPiUBaDPbPcJ2j5i0EJzOFDtiF",
            "https://drive.google.com/uc?export=view&id=11bEQ_bUf4_g-nJp9amccoBRqbPJjKj36",
            "https://drive.google.com/uc?export=view&id=1bUI8JP7RxE4-B7IcHaqBCXd86uZBCHmE",
            "https://drive.google.com/uc?export=view&id=1U-3jpxJXDFzZv5eFepPEYVDIFuVoOwci",
            "https://drive.google.com/uc?export=view&id=1s7f6Gqwo4HKh1fYB-vtOonPrDG0FAO4K",
            "https://drive.google.com/uc?export=view&id=1HEOFP9P06N9iFpqM7zDP66V4D383pJN2",
            "https://drive.google.com/uc?export=view&id=1sYwknyX57ZlfTxeoieciIMTJdATcjYZ5",
            "https://drive.google.com/uc?export=view&id=1yiAfz4rCJ1JplbaQDYq6BtWOP3aZopEg",
            "https://drive.google.com/uc?export=view&id=1GyZFEqrhlzf2y7pWZoOdU48CSV7ttFEv",

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
                "kesan": "cantik, keren kakanya",  
                "pesan":"semangat terus jadi kadepnya kak patricia"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jl. Kresna Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini seruuu, asik abis",  
                "pesan":"semangat teruss kak rahma kuliahnya"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard & Volly",
                "sosmed": "@mananam_",
                "kesan": "kalem, keren abis kakanya",  
                "pesan":"Sukses dan semangat trusnkuliahnya bang"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik & fotografi",
                "sosmed": "@noerruu",
                "kesan": "abang keren, kece abiss",  
                "pesan":"Semangat terus dokumentasinya bang labo"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Abang Gokill dan keren parah",  
                "pesan":"Semangat terus bang & Sukses terus"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": " keren, seruu abis",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {   
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak kece, keren seru abiss",  
                "pesan":"semangat terus kak kuliahnya!"
            },
            {
                "nama": "Aliya Anmara Amanta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammra",
                "kesan": "kaka kalem, keren abizz",  
                "pesan":"semangat trus kuliahnya kak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@donnamaya.p",
                "kesan": "asik, seru abis kakanya",  
                "pesan":"semangat terus kuliah kak"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kakak seru, asikkk",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak cantik & kece abiss",  
                "pesan":"Tetep Kece dan semangatr trus kakk"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumateraa Barat",
                "alamat": "Jl. Lapas, Kecamatan Jati Agung",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa_",
                "kesan": "kaka keren, happy abiss",  
                "pesan":"tetep jadi orang keren kak"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak baik, dan keren banget",  
                "pesan":"semangat terus main roblox dan kuliahnya kak"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "abang keren, kece betul",  
                "pesan":"Semangat semangat bangg menjalani kuliahnya"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Keren, kece banget pokoknya kaka ini",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "kaka keren, seru abis",  
                "pesan":"semangat terus ngedesignnya kak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "keren, seru abis kakanya",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "kaka keren, cool abis",  
                "pesan":"sukses trus kuliahnya kak"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
       

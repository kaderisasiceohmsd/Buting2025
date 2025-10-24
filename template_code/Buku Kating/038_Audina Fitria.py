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
            "https://drive.google.com/uc?export=view&id=1Ukmo3VoAGdbhBn1x84U__Ox0ENWnuWAt",
            "https://drive.google.com/uc?export=view&id=1Xf8Xg9vyvdq0_AwXRpavoj5KV7gENyVh",
            "https://drive.google.com/uc?export=view&id=13Ni4pKIlIm150KY9D_86cLOTS-FakMED",
            "https://drive.google.com/uc?export=view&id=1phTiSAx3G5_9RMEXWtXB0vmKmJjmtcpS",
            "https://drive.google.com/uc?export=view&id=1r39Ho2Altc0BS9J4-ZJgjXUvJUs3ny9n",
            "https://drive.google.com/uc?export=view&id=1Ynw8YOyPtlWeRR839ORFG1HLmY_YeqqY",
        
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
            "https://drive.google.com/uc?export=view&id=1bSA27f67hViz5gQIoFqK6OYgC49EhHFZ",
            "https://drive.google.com/uc?export=view&id=1JFhqjbvv-et9DcTivM_IpSNLlhYek-sY",
            "https://drive.google.com/uc?export=view&id=1ca9Kg0i0bcPaGjE9KHn0a__Js6GO0DEb",
            "https://drive.google.com/uc?export=view&id=1UWySTrbzNDNmtQ_-g7Ncs10JHVwA5Doe",
            "https://drive.google.com/uc?export=view&id=1zMEH1R51TrWGKP55--RGFtu3FmF9bGy7",
            "https://drive.google.com/uc?export=view&id=1IDWlTEPfQKba4-PxgMlYSfDLjYHnbV-P",
            "https://drive.google.com/uc?export=view&id=1XS_-ytEXnuvzGfuvwewrKjVifPe9Zee1",
            "https://drive.google.com/uc?export=view&id=1RxU75ANSWWarUpJWrMo3iCL0bQuKUkIA",
            "https://drive.google.com/uc?export=view&id=1Ykm1EaFCkgc52DPdEV-DZocHcTQeXIcS",
            "https://drive.google.com/uc?export=view&id=1EWk6JhHsnQqNGe2vfxU4N-7qWiMnCK5t",
            "https://drive.google.com/uc?export=view&id=1KSuZ6mS8Knmm1M12Mj79dI7NHH2bVgOB",
            "https://drive.google.com/uc?export=view&id=18p_WWQ38-Xfq9oJXKB_5-vOVRBguBHZs",
            "https://drive.google.com/uc?export=view&id=1IDVDOyOKZQstHiB7wZbL8eXdgxmfOOG8",
            "https://drive.google.com/uc?export=view&id=11mEuQaOJrR5MRQzHpR3ZS25_J4r9gANO",
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
                "kesan": "kakanya baik dan ramah ",  
                "pesan":"sukses selalu kak"# 1
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
                "sosmed": "@ansftynn",
                "kesan": "kakanya asik dan enak diajak ngobrol",  
                "pesan":"semoga lancar semua urusannya kak"# 1
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
                "pesan":"Semangat raih gelar cumlaude itu ya bang"# 1
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
                "pesan":"semangat jadi atlet volly kakk"# 1
            },
             {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "abangnya seru, asik dan ternyata orang lambar juga",  
                "pesan":"jangan diliatin terus langitnya bang, nanti salting"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain Makanan Baru",
                "sosmed": "@myrrinn",
                "kesan": "terlihat keren dan berwibawa",  
                "pesan":"Terus semangat bang!"# 1
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
                "kesan": "baik, auranya positif banget",  
                "pesan":"bahagia terus ya kak jangan galau galau"# 1
             },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "keren bang, gokill pokoknya",  
                "pesan":"semoga lancar terus urusannya bang"# 1
            },
             {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin ka wawa ngomong",
                "sosmed": "@fer_yulius",
                "kesan": "asik, baik dan seru banget",  
                "pesan":"semoga bisa selalu jadi pendengar yang baik buat kak wawa"# 1
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML hero semua franco",
                "sosmed": "@Monica_tjg",
                "kesan": "asik dan kece abiess",  
                "pesan":"jangan lupa makan ya kak, jangan ngegame terus"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "keliatan baik, asik, dan seru abiess orangnya",  
                "pesan":"semoga makin sukses kedepannya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
    if menu == "Senator":
        def Senator():
            gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hBkgEu725NZsvicSqsjT99wzpRjPuIvM",
            "https://drive.google.com/uc?export=view&id=1-UJfwBLs7xExP_Z1r55sPTqOdEvpXWHW",
            "https://drive.google.com/uc?export=view&id=1i_z-_iL5OBLP1oMtmLdY6Ozj1eCJv6EF",
            "https://drive.google.com/uc?export=view&id=1aF-m_q2kcxRYIau0wag7nrl1f8CI_2rN",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@nadyaanjanani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Denger musik sambil jalan",
                "sosmed": "@fathinahazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret Belwis",
                "hobbi": "Mainn",
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
            "https://drive.google.com/uc?export=view&id=18GBUD2WsKRFae_e2dzBPXUSMfenFQSbJ",
            "https://drive.google.com/uc?export=view&id=1Z38paLORfRDo-5wgQInn5vCoW8vCtbgx",
            "https://drive.google.com/uc?export=view&id=1V4ar0awB1xGr0kFXytikln0sS6p4K_JZ",
            "https://drive.google.com/uc?export=view&id=126Jl2Pa-0hRNkrFqiA0TS8_AyoCBrUwh",
            "https://drive.google.com/uc?export=view&id=18lqJuwxbdjNFp52OSWY5M6_FSyRTFEin",
            "https://drive.google.com/uc?export=view&id=1Bn1gnpdZXg7cUA3x8gLMw5rMPMUz3ial",
            "https://drive.google.com/uc?export=view&id=1Zw0_5wibiOyTBEt_DWGdNyQyOqIBInTU",
            "https://drive.google.com/uc?export=view&id=1oumkECsUAvhHCK8OP569z3JdGHoi1mQq",
            "https://drive.google.com/uc?export=view&id=15XhObxEF67NQ7-wqgx7npazWHN1ofcqj",
            "https://drive.google.com/uc?export=view&id=110TChAQXMGOH6Ob48O44Zc6gFcPh5mBs",
            "https://drive.google.com/uc?export=view&id=1J_qKtUfbr3ezrfcsRLIt4HQI1EsAi9XV",
            "https://drive.google.com/uc?export=view&id=1y-q0uqiuiudgGKT4lEc2C5BXtZAha0rT",
            "https://drive.google.com/uc?export=view&id=1-QsRs9LX6K9gCjwru2Ji-MEoQTwSjwHq",
            "https://drive.google.com/uc?export=view&id=1ARgsM5fEbJ8a4uM5Bb3xDkwu0uBo4co0",
            "https://drive.google.com/uc?export=view&id=1UZuartyR10CWkg4COTGZRcnPFwF4LR15",
            "https://drive.google.com/uc?export=view&id=1i96Xo7gDDMQIMPa8HNmZCbfV4xkttdJ6",
            "https://drive.google.com/uc?export=view&id=1c5EvbN_wBYYHFl74Hlv4AU8AY9TsMLqZ",
            "https://drive.google.com/uc?export=view&id=1XaKtGIg_7A1EhYyG8zN-UJ9IM_aGpTyZ",
            "https://drive.google.com/uc?export=view&id=1Hdri6HJU_FItl8RlHm56H4to6Vlo3zsm",
            "https://drive.google.com/uc?export=view&id=11petc4eRr73dWlf_1fpmkeHT8tfQIk7M",
            "https://drive.google.com/uc?export=view&id=14oO7YmNfKz4cjcSyDF2475yG_VjsHZSS",
            "https://drive.google.com/uc?export=view&id=1DrF0KIHJ_JpfMUQIM6wcepmHyRAhzaaW",
            "https://drive.google.com/uc?export=view&id=1vq6_ylSadeoJpUaM_9DS2XcCKwLLSFIS",
            "https://drive.google.com/uc?export=view&id=1ay8KW3zYEz2mkVuVGIUkkgfSB0EF8gCm",
            "https://drive.google.com/uc?export=view&id=",

        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Nibaho",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main apapun",
                "sosmed": "@allyapasha_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "kontrakan GH",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Samping kost daffa",
                "hobbi": "Main Sudoku",
                "sosmed": "@arientakhsnl",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jailin putri",
                "sosmed": "@daffahdynn_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_nrp",
                "kesan": "",
                "pesan": ""  # 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"pasar muara beliti",
                "alamat": "kost putri, gerbang barat samping sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Urip",
                "alamat": "Belwis",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma fam",
                "hobbi": "ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "maju jaya kost",
                "hobbi": "yapping sampe bete",
                "sosmed": "@vany.salsabilaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Lari",
                "sosmed": "@sahid22_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ali Aristo Muthahhari parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "nangka 4, sukarame",
                "hobbi": "Main game + kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Gusti Putu Ferazka D",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul9",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.lapas raya no 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Bikin project, ngoleksi data",
                "sosmed": "@ihsan.myusuf",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Padang Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "",
                "pesan": ""  # 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
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
                "hobbi": "Lempar Batu",
                "sosmed": "@m.ridwan_22",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Uliano ",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main musik, ngoding, menanam anggrek",
                "sosmed": "@nano.wlm",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobi": "Bengong",
                "sosmed": "@rewinanaaa",
                "kesan": "",  
                "pesan":""# 1
            },
     ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()


if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13yJavWitRUcQgysknbYjjAfE_VHxZXTi",
            "https://drive.google.com/uc?export=view&id=1jZXSqnmWz2ti5BNfglQ4nCKJcEJB-ada",
            "https://drive.google.com/uc?export=view&id=15kZiauetAXP4zeGp2-KCxhit2j3Ip7yg",
            "https://drive.google.com/uc?export=view&id=1qK5q_kcpvvNOHLcyfT7Ik_AL06bRwt49",
            "https://drive.google.com/uc?export=view&id=13uirRRX6151TLn1RLs2bm5lgCYwFF3H0",
            "https://drive.google.com/uc?export=view&id=1ABD0gNrJiI_YdR3jygJvek1H0_uWpNbG",
            "https://drive.google.com/uc?export=view&id=1SglzmTR8NVfkq--8D0j7xvKP90MJtpNK",
            "https://drive.google.com/uc?export=view&id=1IyoTo_zd9zgaKkOfLrq5cOaeJnz4Sep9",
            "https://drive.google.com/uc?export=view&id=1Wc9UJQxB0H7vUI4Jtks4iLj5f84u7Lro",
            "https://drive.google.com/uc?export=view&id=1PKI6J1SC5yv2JOMnytqbEI8iB9lgkfn6",
            "https://drive.google.com/uc?export=view&id=1R57vT6TaWHIlo5EJq9eCrnFgc02KFT1t",
            "https://drive.google.com/uc?export=view&id=12XHFcf2Uyv0mizKMgrmu3cgSNDY9dq5_",
            "https://drive.google.com/uc?export=view&id=1kamFS3Nu9n30SUIRbb07OC2NERdkH7bB",
            "https://drive.google.com/uc?export=view&id=1M2viTsz7vQ-rOA4CZ2bGR4HgG7_Jy7yJ",
            "https://drive.google.com/uc?export=view&id=1J3JoaJ3OJ6OizJhSqj8h4vB7bccp8WQG"
            "https://drive.google.com/uc?export=view&id=1n3pah56GFRZUIWekhhWae05injOYrZVg",
            "https://drive.google.com/uc?export=view&id=1Mg1Jk7ITk_Gg0gD4pzCDX-RZ52KNkzEU",
            "https://drive.google.com/uc?export=view&id=1G-5Eb04xWuxNOJtp_eol9eZP8FpfeZZQ",
            "https://drive.google.com/uc?export=view&id=1XXrYsZ0FL3LlbIPm5HvTTqKN3jPdBXY0",
            "https://drive.google.com/uc?export=view&id=1I8qveMKaNbfCmOCa3OeB4pgHOykF2Tww",
            "https://drive.google.com/uc?export=view&id=1S4wUS9oQbn938IXZsTPblNl_tCYvb-Xw",
            "https://drive.google.com/uc?export=view&id=1x6ZrFNTiQnfMdBSiQRFrjtk2IGVUzFjw",
            
        ]
        data_list = [
                        {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Asik dan seru untuk diajak diskusi",
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@junitaa.0406",
                "kesan": "Kakaknya asik, baik, suka sharing ilmu",  
                "pesan":"Selalu jaga kesehatan ya kak"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Keren banget bang + abang asuh di TPB paling gokil",  
                "pesan":"Semangat nyusun TA ya bang"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakanya baik, seru diajak ngobrol",
                "pesan":"Jangan lupa makan ya kak"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Keren banget bang, akhirnya ketemu abang nim",
                "pesan":"Semangat jadi abas bang" 
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tj. Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya baik, santai orangnya",
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "jl. Manggis 1",
                "hobbi": "Nonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "kakanya baik, kalem juga",  
                "pesan":"semoga harinya selalu menyenangkan ya kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "kakanya baik, asik, bawaannya ceria terus",
                "pesan":"semangat kuliahnya ya kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abangnya baik, asik, santai",
                "pesan":"selalu keren bang"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakanya baik banget, seru juga",
                "pesan":"Semangat Ngedrakor kak"    
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jl. Raden Saleh",
                "hobbi": "jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Seru banget, baik, asik",
                "pesan":"semangat terus kak kuliahnya"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan Bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "kakanya baik, kalem",  
                "pesan":"semangat terus ya kak, selalu jaga kesehatan"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kedepannya kak!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama ITERA TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Aura codingannya kuat banget bang",
                "pesan":"Tetap semangat jangan menyerah"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Keren banget bang, asik abiezz",
                "pesan":"semangat terus bang kuliahnya"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya pinter, kalem, seru",
                "pesan":"Selalu jaga kesehatan ya bang"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"semangat terus kuliahnya Kak!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik, baik, seru diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kak, jangan bosen liat embung ya kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Baik, asik banget bang",
                "pesan":"Semangat Futsalnya bang"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departement Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19lN0vqenbZOLVZuv4OCgNYKx3xag3sZI",
            "https://drive.google.com/uc?export=view&id=1udvLN-eUpBXg_qGTK370JMj6_rDFKshz",
            "https://drive.google.com/uc?export=view&id=1SvuSZsKb5YYww9wQNd3y5ZXJIINXvHJB",
            "https://drive.google.com/uc?export=view&id=15K0-cg52QJsxEmQlw0uRSoW_L7QH1n3Q",
            "https://drive.google.com/uc?export=view&id=1K4DL6A3ukDc-MkpQMC3CQkLA4uD-o0O8",
            "https://drive.google.com/uc?export=view&id=1RUbu1wXXRv0zLaqLr46XwOWw3dKMYPSM",
            "https://drive.google.com/uc?export=view&id=1SgLEVi8XFzq1XDpCfA4-K400uGNd2YD2",
            "https://drive.google.com/uc?export=view&id=1Fu-mfclEOUNbSIoAlZK1t8n97CHJie8o",
            "https://drive.google.com/uc?export=view&id=1Y-HIwI5P4_M_6uoR3eVRYvRfJzoZhYYX",
            "https://drive.google.com/uc?export=view&id=1agpQMB1T60DEnMTIED9XulrtAHodK1SJ",
            "https://drive.google.com/uc?export=view&id=1-F3JdWiA7mUrDgXLkTmwgsr3U3XoOrQK",
            "https://drive.google.com/uc?export=view&id=1dhXICmTxYNYI7NkGJ_JkUo8Lc2--ixkP",
            "https://drive.google.com/uc?export=view&id=1NHMfwhBfg6ch4sEyEHzQEdQ1QkQkN_v7",
            "https://drive.google.com/uc?export=view&id=1nEK4b0YliN-FsUuBEjb6QdjDC5VUwsPB",
            "https://drive.google.com/uc?export=view&id=1WwTbeoHTl9QOLMi9bUA4XiZ6c_7-O5if",
            "https://drive.google.com/uc?export=view&id=1KUS5gFwltYKslKWouKDTgi0ZHaY0LdOK",
            "https://drive.google.com/uc?export=view&id=1AEmO7kcrnu2JsbzukcvrR37ppbhTRIoP",
            "https://drive.google.com/uc?export=view&id=1B2DLclI7oyavpeW5rIbeu01HiOpRlCK8",
            "https://drive.google.com/uc?export=view&id=1n_PUxrU7o4zy5gneWE6ZVpdg6c0JkOVI",
            "https://drive.google.com/uc?export=view&id=1ZX1J4SarZJ29k1zjlPfup__ill3K9X6M",
            "https://drive.google.com/uc?export=view&id=1zRnn_Z4DnIARL9-fVN1TXx0VN96GAByv",
            "https://drive.google.com/uc?export=view&id=1ffmETNC3oU31J0CaFALRmHuwgSHaFhAr",
            "https://drive.google.com/uc?export=view&id=1SliSTp9znva1-hsFXCMifJImmwwcVgcx",
            "https://drive.google.com/uc?export=view&id=1YeMxt0yaKcVqOb_lQcJlWHvFGSqW-6yd",
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup ",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan keliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung barat",
                "alamat": "Sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": " 123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
        
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Kopri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": " 123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaai",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya asik dan keren banget bang",
                "pesan":"Selalu jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "kakanya asik dan baik banget",
                "pesan":"Sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak sangat baik dan sabar juga",
                "pesan":"Jangan lupa jaga kesehatan ya kak."# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya asik dan seru untuk diajak ngobrol",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakanya baik, bawaannya ceria terus",
                "pesan":"Semangat ngejalanin hari kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya asik, ramah juga",
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Baik, asik dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak."# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departement Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Bm2UzY17WcuovOIugtaF1KIlA5UdR-Qv",
            "https://drive.google.com/uc?export=view&id=1UTmC3ZSKWMSj7Ws3p9Y4jie4tw8voE5x",
            "https://drive.google.com/uc?export=view&id=1yoG03MxPDQQ7BFGIMB2h7bFtPwduF49F",
            "https://drive.google.com/uc?export=view&id=1Mqh4ejcb6nnRHOxF-E_UKJI04_ujajel",  
            "https://drive.google.com/uc?export=view&id=1SMzL7er6y5ucOZcYas1ZjBajX1U8Xa_K",
            "https://drive.google.com/uc?export=view&id=1iopa70hIFVfMAcgbc3Xv0JSdWG5OT84T",
            "https://drive.google.com/uc?export=view&id=1BGUAJy0Y46JPRRiJHYvqZJ89MWH-R305",      
            "https://drive.google.com/uc?export=view&id=1y-eSq2WTzG4kqF_HIJwX2tcykHQgEFii",
            "https://drive.google.com/uc?export=view&id=1nMISYelfYU7TB2d69xVmd_0atmj9nKOM",
            "https://drive.google.com/uc?export=view&id=1a2toXM2PGyfZsTlNQzS683hv3Wjc6X80",
            "https://drive.google.com/uc?export=view&id=1OaXfUXiqohmS10bm6_fayS-TWHn6Y9-l",
            "https://drive.google.com/uc?export=view&id=15yHla7mpF8pQbyAw5aEwysyl-nW8ANSC",
            "https://drive.google.com/uc?export=view&id=1bAoa2bi5Ln3maHlclYntrhT3gRhACSlk",
            "https://drive.google.com/uc?export=view&id=12wTD-0SMo9dhHKTWDshz1a80Y_efKQty",
            "https://drive.google.com/uc?export=view&id=1aqD1T5ucI2MXGnnkVw17ecwPf1EEZVgI",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik banget dan ramah.",
                "pesan": "Sehat dan semangat terus ya kak!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Semoga urusan kuliahnya lancar selalu, Kak"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Senang bisa kenal sama kakak.",
                "pesan": "Sukses terus buat ke depannya ya Kak!"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya ramah banget.",
                "pesan": "Sehat dan bahagia selalu kak!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya baik, seru dan asik",
                "pesan": "Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asik banget.",
                "pesan": "Sehat selalu ya kak!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "kakanya baik dan positif vibes banget kak.",
                "pesan": "Selalu semangat ya kak!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalghani73",
                "kesan": "Abangnya asik, baik, ramah",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya baik dan asik banget",
                "pesan": "semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya humble dan asik diajak ngobrol",
                "pesan": "Selalu jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik, asik dan friendly banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya baik dan seru.",
                "pesan": "Semangat terus kak!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya baik dan ramah",
                "pesan": "Semoga urusannya dipermudah selalu bang"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya asik untuk diajak diskusi.",
                "pesan": "Lancar-lancar ya kak kuliahnya."# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Rubik Mirror",
                "sosmed": "@zhrptsl",
                "kesan": "kakanya asik dan seru",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departement SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11ps-jklNdbRiShW5LiFsw1sAWHDPp1XE",
            "https://drive.google.com/uc?export=view&id=1fWTBdq3WZh1o8nM0i9IXXKFcIEBX9LUT",
            "https://drive.google.com/uc?export=view&id=1rX9fh2D0rxzQKA4Mk4Hl0D3Am6GT3XeU",
            "https://drive.google.com/uc?export=view&id=1qc0gEclJCW2AVDwULHsvHNIk-El2BGrI",
            "https://drive.google.com/uc?export=view&id=17tT_Ta9hYrBrolk4weLel-7KSeNZeVlQ",
            "https://drive.google.com/uc?export=view&id=15wfDxJkOYSLLd92BPN4T_px_C7G3Av-e",
            "https://drive.google.com/uc?export=view&id=16NkuBjNcFfkllb4rDJDcC-k4iN7B4BT-",  
            "https://drive.google.com/uc?export=view&id=1boY62tV1hzcwZ6cMlovwGvUMn4W5uuFk",
            "https://drive.google.com/uc?export=view&id=1lriyZPZm30Glr8V3oCfOGYjNnUe5fZPq",
            "https://drive.google.com/uc?export=view&id=1ItSWyQJvtzX_ksVcZJ8SVibeg3OC6zpW",
            "https://drive.google.com/uc?export=view&id=1w_B9TtpexvOtDfbcYkKeDPQDyi7UrF_l",
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
                "kesan": "Abangnya asik dan seru.",
                "pesan": "Semangat terus bang"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Senang bisa berkenalan dengan kakak.",
                "pesan": "Semoga sukses selalu kuliahnya!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya ramah dan baik.",
                "pesan": "Sehat selalu ya, bang."# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif.",
                "pesan": "Semangat terus kuliahnya, kak!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "Semoga semua urusannya dilancarkan."# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Semangat terus ya, kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya asik dan menyenangkan",
                "pesan": "jaga kesehatan selalu ya bang"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya kak!"# 1
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu ya kak!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya sangat ramah",
                "pesan": "Jaga kesehatan selalu kak!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakanya baik, asik dan menyenangkan",
                "pesan": "Semangat dan sukses selalu!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departement Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LfK9vWn7_e43wua7jcJwHqn2dDUmX7R_",
            "https://drive.google.com/uc?export=view&id=1G437W6lzS-FfWpwT0lJgDtO3WlWDRcYe",
            "https://drive.google.com/uc?export=view&id=1TIk_VRuKapGOJzq9MDNazrYF1f_mRt-z",
            "https://drive.google.com/uc?export=view&id=1GSt4E4gwCixVlvjYZe49kQnER0jCOTUn",
            "https://drive.google.com/uc?export=view&id=119Rke_fhQW-Jn4Glrk1O0OUsguZcyeN9",
            "https://drive.google.com/uc?export=view&id=1QO6EZMV4chAXXNpu6hs2QDjGloOeeqWD",
            "https://drive.google.com/uc?export=view&id=12km0s8ARoS1HqCiYWLbJ6oYj63FD_pu9",
            "https://drive.google.com/uc?export=view&id=1v5BdZz9JeH3GZgXQI1DgE6aRFTDCatmd",
            "https://drive.google.com/uc?export=view&id=1sWSZUYDVBn5DH_s94wBP7oxY9ukU3-rw",
            "https://drive.google.com/uc?export=view&id=1Q7EwLO9Mu7YXWrNpQBhKMBhQvKdaV2Gf",
            "https://drive.google.com/uc?export=view&id=1k8wfcpKbQUL-98k66LXJWC5sEUI8QILk",
            "https://drive.google.com/uc?export=view&id=1C1PkvWX4CyoSHzi4pmKZk28UaOCgN2fv",
            "https://drive.google.com/uc?export=view&id=1wWQw8knj6UvHt0v65djk6i4yIZXf2cwi",
            "https://drive.google.com/uc?export=view&id=1XsWwIdbiMEAp-je3i1G50j1127owGIQy",
            "https://drive.google.com/uc?export=view&id=1iS-aa2XOG7_TWgPdf4NZLZxHq5Kv5_pi",
            "https://drive.google.com/uc?export=view&id=16F9612vZjDvNrRsTvsJ-NsPCjioU-NRJ",
            "https://drive.google.com/uc?export=view&id=1cthv8VRuR4w6iDqgVc8JJ5ggwmQgh-Wq",
            "https://drive.google.com/uc?export=view&id=1WoMFS7bQnQMlYNLqqVM-Ha9Ev-KXfdcv",
        ]   
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Sukses selalu ya, kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Belajar sama kakaknya jadi menyenangkan",
                "pesan": "Semoga lancar terus kuliahnya!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Pengalamannya keren dan menginspirasi",
                "pesan": "Teruslah berkarya bang"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abangnya friendly dan asik",
                "pesan": "Sehat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya asik dan seru",
                "pesan": "Semoga sehat dan sukses selalu bang!"# 1
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Senang bisa belajar bareng kakak",
                "pesan": "Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya sangat ramah dan baik",
                "pesan": "Tetap semangat kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "kakanya lucu dan baik banget",
                "pesan": "Semangat terus kak, jangan menyerah!"# 1
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Terima kasih sudah berbagi ilmu",
                "pesan": "Semoga sukses di masa depan!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya asik diajak diskusi",
                "pesan": "Lancar terus ya kak kuliahnya!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget",
                "pesan": "Sukses untuk ke depannya, kak!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya seru dan pintar",
                "pesan": "Sukses terus untuk karirnya nanti."# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Sangat berkesan bisa diajar kakak",
                "pesan": "Semoga sehat selalu, kak."# 1
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Orangnya asik dan mudah bergaul",
                "pesan": "Semangat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya sangat welcome dan ramah",
                "pesan": "Semangat terus dan semoga sukses!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Suasananya jadi asik kalau ada kakak ini",
                "pesan": "Jangan lupa jaga kesehatan ya, kak."# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya keren dan inspiratif",
                "pesan": "Semoga apa yang dicita-citakan tercapai."# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya ramah dan humble",
                "pesan": "Selalu jaga kesehatan ya kak."# 1
            },
                        
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
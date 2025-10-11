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
            "https://drive.google.com/uc?export=view&id=1XtYJgFnG5-pjzpJngWkz2PeRFWVwjJ6V",
            "https://drive.google.com/uc?export=view&id=1Y7n8KJBgaAO61pcjPCgt8b47fBhWOkqc",
            "https://drive.google.com/uc?export=view&id=1gJPR39QYuAHkK9DOo-Angby2Z7tmWrdh",
            "https://drive.google.com/uc?export=view&id=1aQ-SOh6O3bet4KZAVN2ePjZWRy4BT2Kl",
            "https://drive.google.com/uc?export=view&id=1b1IPLfM-8hXxa5BZ9L9J9xinCYrrZpky",
            "https://drive.google.com/uc?export=view&id=15OneSvApF0CzpHcPn5SmME4eotBRYeMx",
        ]
        data_list = [
            {
                "nama": "Bang Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Makan Pisang",
                "sosmed": "@_erendraa",
                "kesan": "Tegas, panutan",  
                "pesan": "Semangat bang bentar lagi lulus"# 1
            },
            {
                "nama": "Bang Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren, tegas banget orangnya",  
                "pesan": "Semangat kuliahnya bang"# 1
            },
              {
                "nama": "Kak Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya asik banget, kalem dikit",  
                "pesan": "semangat kakak semester 7 nya"# 1
            },
              {
                "nama": "Kak Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya kalem banget",  
                "pesan": "semangat kakak kuliahnya"# 1
            },
            {
                "nama": "Kakak Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "gabisa di tebak",  
                "pesan":" semangat yaa kak kuliahnya"# 1
            },
             {
                "nama": "Kakak Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak hanum seasik itu",  
                "pesan": "semangat terus kuliahnya kakk"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1F6a9BMeoXdcK522HI1JxDyRqQ1YNGXRz",
            "https://drive.google.com/uc?export=view&id=1I361S79fmrqWdy9euF2YfqJIS0tnJGiW",
            "https://drive.google.com/uc?export=view&id=1Pu7rUm-yGx7_09tAFjfOawGqbkKLdGpd",
            "https://drive.google.com/uc?export=view&id=1dgttd4FlxH-ye971xYV3kZw2NG466-y_",
            "https://drive.google.com/uc?export=view&id=12r-4Mrp5168J74d1M9yzftvmH8GLnFgc",
            "https://drive.google.com/uc?export=view&id=1a4th0Wozf9G64EXx-6pL50ktT9J2rChW",
            "https://drive.google.com/uc?export=view&id=1CuXTwpXj5tQ-4TsxSCb5iZibJ7jiqUDy",
            "https://drive.google.com/uc?export=view&id=1DZ10bhKvgRDcspXvgxdPCGN94g3_ChjB",
            "https://drive.google.com/uc?export=view&id=1ALE0ay71Cxdf6N8l06IvaHkQU4szOvkS",
            "https://drive.google.com/uc?export=view&id=1Vj-SVw68fuZ0zN28yiXTbORMfNbsbUb1",
            "https://drive.google.com/uc?export=view&id=1GtRASWOp5QYbRBpDHl9NYwFagekX1YVm",
            "https://drive.google.com/uc?export=view&id=1NDT-sW7a0Nub1Z8ugoPGzaH3km8z5_gu",
            "https://drive.google.com/uc?export=view&id=1hTqQMF6Xt4OoJCtDwIr-beJeSshRYPDw",
            "https://drive.google.com/uc?export=view&id=13_Gs5IAFHmEhvRn-k2c3ze4kIoYSZNo-",
        ]
        data_list = [
            {
                "nama": "Bang Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "ganteng bang",  
                "pesan": "semangat bang ngasprakny"# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "sehumoris itu kakak ini",  
                "pesan": "semangat terus ya kak kuliahnya"# 1
            },
              {
                "nama": "Kakak Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "kakaknya lucu",  
                "pesan": "semangattt kuliahnya kak"# 1
            },
              {
                "nama": "Kakak Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kakanya kalem",  
                "pesan": "semangat kuliahnya kak"# 1
            },
            {
                "nama": "Bang Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "pinter banget abang ini",  
                "pesan":"semangatt bang mapres"# 1
            },
             {
                "nama": "Kakak Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "lucu banget kakanya",  
                "pesan": "semangatt kak jadi pimsid"# 1
            },
              {
                "nama": "Bang Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "ganteng bang",  
                "pesan": "semangat kuliahnya bang"# 1
            },
              {
                "nama": "Bang Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "soft boy gtu ya bang",  
                "pesan": "semangat kuliahnya bang"# 1
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": " cantik kakaknya",  
                "pesan": "semangat ya kak kuliahnya"# 1
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "cantik + lucu kakaknya",  
                "pesan": "semangatt ya kakak kuliahnya"# 1
            },
              {
                "nama": "Bang Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "humoris abangnya",  
                "pesan": "semangat ya bang kuliahnya"# 1
            },
              {
                "nama": "Bang Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "keren bang",  
                "pesan": "semangat kuliahnya bang"# 1
            },
              {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "lucu kakaknya",  
                "pesan": "semangat ya kak kuliahnya"# 1
            },
              {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "kakanya lucu + cantik juga",  
                "pesan": "semangat ya kak kuliahnya"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GAb6oEKFnfn_AlOJtIET7UirsHe76wcc",
            "https://drive.google.com/uc?export=view&id=16M71EUFBtobTkTVL6ApiBH8fHFUWGslL",
            "https://drive.google.com/uc?export=view&id=1_1DozeW7_vrOsmApmFCDeVu--1gIQ086",
            "https://drive.google.com/uc?export=view&id=1pB8SVumqk9b1UHfiaIiFG3b0ak_PMYAK",
            "https://drive.google.com/uc?export=view&id=1NFVzBnEScgkeBgDYWZ0SjptOQ44VNZ9X",
            "https://drive.google.com/uc?export=view&id=1egLrp_QSva1yV2Md5_ApuNYMUEQVKj0r",
            "https://drive.google.com/uc?export=view&id=1t_aB_7mq27hulbl1bU3cIrpJNdUgXFsN",
            "https://drive.google.com/uc?export=view&id=1JO8j5JKiesm4Nb8XHCC3lj7TfC14J3x_",
            "https://drive.google.com/uc?export=view&id=1EQzv53enl_Lj5EoIk22UspEX5b1Lt9sM",
            "https://drive.google.com/uc?export=view&id=1245rrDcdKRqkMpJNjkvsWf0jzl7GOfHs",
            "https://drive.google.com/uc?export=view&id=1PfyzQWCnyftL5Bfsz9fQuPoJDinRfuEG",
            "https://drive.google.com/uc?export=view&id=1ZT501seAPHQjynP4Mw1MEm8hX_kBu7fp",
            "https://drive.google.com/uc?export=view&id=16TqOXnnrodDT7xKQC-qNG-W7eZAQCrOo",
            "https://drive.google.com/uc?export=view&id=1IQFZ8mQPBzeKXVVwO8IMjTPciAF0z8Dr",
            "https://drive.google.com/uc?export=view&id=1BWWqdszW1wH58EmZbVevmEzDmLesL5SQ",
            "https://drive.google.com/uc?export=view&id=1a9x5CevN4wk1UELv46DXnduNCMyTrwCK",
            "https://drive.google.com/uc?export=view&id=1_BRT4--r8jcduUjYLM-Uuucf7m9RNxRT",
            "https://drive.google.com/uc?export=view&id=1Z-wtnPgIVVYy12SsCEM_ZIXmC_95U4G1",
        
            
        ]
        data_list = [
            {
                "nama": "Kakak Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Kakak Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Bang Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "BangLabo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Bang Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemmiling",
                "hobbi": "Scoll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Bang Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Raihan Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "",  
                "pesan": ""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan









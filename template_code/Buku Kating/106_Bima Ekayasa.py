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
            "https://drive.google.com/uc?export=view&id=15OneSvApF0CzpHcPn5SmME4eotBRYeMx",
            "https://drive.google.com/uc?export=view&id=1b1IPLfM-8hXxa5BZ9L9J9xinCYrrZpky",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Eksanty Febriana Sukma Islamiaty",
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
                "nama": "Farahanum Afifah Ardiansyah",
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
            "https://drive.google.com/uc?export=view&id=1NmK8iyVcKegXOLrKE4bCjeJs0RxIyUy7",
            "https://drive.google.com/uc?export=view&id=13_Gs5IAFHmEhvRn-k2c3ze4kIoYSZNo-",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
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
                "nama": "Dhea Amelia Putri",
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
                "nama": "Renisha Putri Giani",
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
                "nama": "Anisa Fitriyani",
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
                "nama": "Dharu Cahyoaji Sasongko",
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
                "nama": "Feby Wulandari",
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
                "nama": "Givaro Ananta",
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
                "nama": "Mirzan Yusuf Rabbani",
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
                "nama": "Berliana Enda Putri",
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
                "nama": "Juesi Apridelia Saragih",
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
                "nama": "Ridho Benedictus Togi Manik",
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
                "nama": "Feryadi Yulius",
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
                "nama": "Monica Patricia Tanjung",
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
                "nama": "Wan Nashwa Alhasni Yuska",
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
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "kak cia lucu banget, positive vibes",  
                "pesan": "semangett kak, semoga di perlancar semester 7 nya kak"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "kakak rahma kurang se aktif itu, tapi lucu gtu orangnya",  
                "pesan": "semangatt kakak menjadi sekdepp"# 1
            },
              {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "asik, keliatan humoris juga orangnya",  
                "pesan": "semangatt bang anam menjalani harinya"# 1
            },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "lucu kalo di panggil labubu bang, abangnya asik, tinggi ",  
                "pesan": "semangatt menjadi pdd abadi bang"# 1
            },
              {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "sangar bang, agak serem sih, tapi aslinya asik",  
                "pesan": "semangatt bang melanjutkan pdd sepanjang umur"# 1
            },
              {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "jarang keliatan, kakak ini cantik tapi ",  
                "pesan": "semangat ya kak menajalani kehidupan semester 5"# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "kakak ini cantikk banget",  
                "pesan": "semangatt ya kak kuliahya, semoga pkm nya menang"# 1
            },
              {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "lucuu kaka ini, tapi agak pendiem gtu orangnya",  
                "pesan": "semanagatt kak kuliahnya, btw kakak miirip aqila kak"# 1
            },
              {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "ramah, pendiem",  
                "pesan": "semangatt kak kuliahnya kak donna"# 1
            },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemmiling",
                "hobbi": "Scoll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "cantikk kakaknya, lucu juga",  
                "pesan": "semangat yaa kakak kuliahnya dan segala urusannya"# 1
            },
              {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "cantikkk kakaknyaa",  
                "pesan": "semangatt kak kuliahnya"# 1
            },
              {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "cantikk kakaknya, manis juga",  
                "pesan": "semangatt kakak semoga lancar kuliahnya"# 1
            },
              {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "kakaknya lucuu, cantik",  
                "pesan": "semangat ya kak kuliahnya, btw kakak gabisa marah tapi panitia kader"# 1
            },
              {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "abangnya extrovert, enak di ajak ngobrol, ga pendiem",  
                "pesan": "semangat bang kuliahya, jago banget pake figma bang"# 1
            },
              {
                "nama": "Raihan Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "islami banget kakaknya, murah senyum",  
                "pesan": "semangat kak kuliahyaa",# 1
            },
              {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "manis canntik",  
                "pesan": "semangat yaa kak kuliahnya"# 1
            },
              {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "religius gtu vibesnya, kalcer juga",  
                "pesan": "semangat kak kuliahnya"# 1
            },
              {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "lucu kakaknya",  
                "pesan": "semangat kak semogaa lancar kkuliahnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1x5552PGSry0PwZYjeyZdg8Y6m5y0dy91", #1
            "https://drive.google.com/uc?export=view&id=1E0_DsGdCOzcCCkx-B0r3_BaJwSDm6TbA", #2
            "https://drive.google.com/uc?export=view&id=1Uw3w-p_0yBvhJ-hgU-nRIGYtaVq-GICI", #3
            "https://drive.google.com/uc?export=view&id=1e505LQTrOGHAueUR74EGb7fG7uxxiRjD", #4
            "https://drive.google.com/uc?export=view&id=1XpZvTh-RhBXFdqikis1Kj14uLHyCARuo", #5
            "https://drive.google.com/uc?export=view&id=1FhYKrVHim4Qm_alshOfZSUQLxbAsUfEV", #6
            "https://drive.google.com/uc?export=view&id=1FhYKrVHim4Qm_alshOfZSUQLxbAsUfEV", #7
            "https://drive.google.com/uc?export=view&id=1D-9oU9fwq2LlffEUkK873pso62UuxaBS", #8
            "https://drive.google.com/uc?export=view&id=1GpXj69IyUMTPgRD6DJ2wN47ntwtuFye7", #9
            "https://drive.google.com/uc?export=view&id=1GfhMrWkSKv2PMOfs55l7l3xYTEEBNgaF", #10
            "https://drive.google.com/uc?export=view&id=1MpUoXUIQIlp_T3zECDHgqHiTdMFpSkzC", #11
            "https://drive.google.com/uc?export=view&id=1Nsn9PhtgT3xcPkg3d5FUrY4HQ_nM-Gbu", #12
            "https://drive.google.com/uc?export=view&id=1Xdg50bCL5zD_fZCcb6XFZ-foQh90q_wv", #13
            "https://drive.google.com/uc?export=view&id=1NP5DG1IB9rpQYb_uzhvycBKQIHoxAY1L", #14
            "https://drive.google.com/uc?export=view&id=1F34_QeobMvWkQ1fceuCQk2lPrw8npbVU", #15
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": "serem, mukanya tegas banget",  
                "pesan":"semangat kak semester 7 nya"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "tomboy ya kakaknya?, asik, lucu rambut kakaknya",  
                "pesan":"semangat kak kulihnya, semoga lancar sampe akhr"# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "murah senyum kakaknya, lucu lagi",  
                "pesan":"semangat kak jangan berhenti tersenyum"# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "kakanya cantik banget, adem gitu liatnya ",  
                "pesan":"semangat kakak kuiahnyaa"# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "seram abangnya, mukanya tegas gitu, tapi aslinya abangya asik banget",  
                "pesan":"semangat abang NIM, semoga di lancarkan perkuliahannya sampe akhir bang"# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "lucu kakanya, murah senyum juga",  
                "pesan":"semangat yaa kak kuliahnya"# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "tegas banget kakaknya, serem juga liatnya",  
                "pesan":"semangat yaa kak kuliahnya, semoaga di perlancar segala urusannya"# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "pendiem abnagnya, ramah, baik",  
                "pesan":"semangat bang kuliahmya, semoga tercapai yang abang inginkan"# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "ramah abangnya, enak di ajak ngobrol juga",  
                "pesan":"semangat bangg kuliahnya"# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "abangnya masih malu malu, ramah , murah senyum",  
                "pesan":"semangat bang kuliahnya"# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "lucuu banget kakaknya, positif vibes juga, selain itu aktiff bangget",  
                "pesan":"semangat kakk hanna kuliahnya"# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "cantik banget kakak ini, ramah, murah senyum",  
                "pesan":"semangat yaa kak kuliahhnya, jangan berhenti tersenyum"# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "pendiem abangnya, lucu, asik abangnya cuman pediem jadi tertutup",  
                "pesan":"semangat yaa bang kuliahnya, semoga di perlancar sampe akhir"# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "cantik + lucu banget, suka liat kakaknya, murah senyum",  
                "pesan":"semangatt kak kuliahnyaa, semmoga tercapai yang kakak mau"# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "kakaknya lucu, senyumnya manis",  
                "pesan":"semoga di perlancar kuliahny sampe akhir"# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MDFfCGuV6m6H-sBYTxasaAYm0TNmRvd3", #1
            "https://drive.google.com/uc?export=view&id=1s-mkxNW3sNe9RtIwpncwRT4asAGn3_cd", #2
            "https://drive.google.com/uc?export=view&id=10QHOshTCAgpWLLoqE6Nl7bs95ZDZ8eT4", #3
            "https://drive.google.com/uc?export=view&id=1Yp0fykA_dqkaw1KU2j7E6IAoE8g-gpqR", #4
            "https://drive.google.com/uc?export=view&id=1otiH3dFJcinEEhnv-neVwDxt0aQDCBe8", #5
            "https://drive.google.com/uc?export=view&id=1-y0bbFuZRJ-SPVcCVlh5BjvyFGdf20W6", #6
            "https://drive.google.com/uc?export=view&id=1d5C9rtW1J-GCivfpMGgF6PVRAh4wenuy", #7
            "https://drive.google.com/uc?export=view&id=1b-tTegJztzLA5h9-3g_Oo0Zln-IhG4Iu", #8
            "https://drive.google.com/uc?export=view&id=1x7FwEyaPoinW6sw1wgQrsyicAunVNvTt", #9
            "https://drive.google.com/uc?export=view&id=1HY0GkJFc5y-57tRchMjF-P7nSlK9KQ87", #10
            "https://drive.google.com/uc?export=view&id=1fzKq1y1o6Zz9nXQB4nR1bQO84MCV_iUl", #11
            "https://drive.google.com/uc?export=view&id=1y-0Q35uQIOgq9NdRsx149zAzk4cw7Skh", #12
            "https://drive.google.com/uc?export=view&id=1BH9rXKEvYNGGQut5KndWtDAD_cgAlNrH", #13
            "https://drive.google.com/uc?export=view&id=1MuCVVLbeG_-f-OFIXs8wi60HX2avraF5", #14
            "https://drive.google.com/uc?export=view&id=1gthyOLUmjcSPoUJ02Knd9PNxtGaCUPmP", #15
            "https://drive.google.com/uc?export=view&id=12hueBSGhDKTc35DlgRr9SfHC_HKGxQiw", #16
            "https://drive.google.com/uc?export=view&id=17PUcthsOFG4OF3KpMPX7pRGbhks6qWTy", #17
            "https://drive.google.com/uc?export=view&id=146QNgcfaW8zBWST3dxsTJrn8yRl7IP35", #18
            "https://drive.google.com/uc?export=view&id=1AXXHqn67HOmwqeasLuGwF8-oclcIti_7", #19
            "https://drive.google.com/uc?export=view&id=1oT_BIHVJPn0d_Tb7UOjl7l8DLaB43XZj", #20
            "https://drive.google.com/uc?export=view&id=1iv8dOeTrLBo1T25c0Vtjq6OvhjNLOb08", #21
            "https://drive.google.com/uc?export=view&id=1wtMvQD6OGMdPV84oEizF-OoOtqTeNRpp", #22
            "https://drive.google.com/uc?export=view&id=1_7kXkNnVqe6tmbofNRNcY6cRg0keDjIi", #23
            "https://drive.google.com/uc?export=view&id=1DErY-9OKWDsAhLIuwIb-fqTUKhiK7Exz", #24
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulan",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "bang arafi asik banget orangnya, enak di ajak ngobrol dan becanda, ganteng juga bang",  
                "pesan":"semangatt ya bang tugas akhirnya, semoga cepet selesai"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "tegas, mukanya agak sangar gitu, ramah, murah senyum",  
                "pesan":"semangatt kak menjalani semester 7 nya"# 2
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "lucuu dan cantik",  
                "pesan":"semangattt kak kuliahnya"# 3
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "baikk banget kak sonya ini, udah cantikk lucu juga, ramah dan murah senyum, full positif kakak ini",  
                "pesan":"semangatt ya kak jadi asprak sampe semester, semangatt juga menjalani hari hari kakak,terimakasih sudah lahir di dunia ini, dengan segala kebaikan kakak"# 4
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "mukanyay tegas, sifatnya juga tegas",  
                "pesan":"semangatt ya kakak menjalani kulliah kakak" # 5
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "lucuu dan cantik banget kakak ini, softgirl",  
                "pesan":"semangatt kakak menjalani kuliah dan hari hari kakak"# 6
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "tegas, sangarr, asik terkadang",  
                "pesan":"semangatt ya bang menjalani hari dan kuliah nya sebagai ketang"# 7
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "chill banget kakak ini, asik juga orangnya, suka ngejokes",  
                "pesan":"semangat kakak menjalani perkuliahan kakak dan yareuu",# 8
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "kalem, murah senyum, softboy bangett",  
                "pesan":"semangatt bang kuliahnyaa, semoga cepat selesai"# 9
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "lucu kakak ini, asik juga keliatannya",  
                "pesan":"semangatt ya kakak menjalani hari hari kakak"# 10
            },
            {
                "nama": "khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "keliatan sangar, ternyata suka ngejokes, asik juga",  
                "pesan":"semangat kakak menjalani kuliah kakak"# 11
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "reigius dan agamis banget orangnya, kalem juga",  
                "pesan":"semangatt ya kakak mejalani kuliah dan hidup kakak"# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "pendiem abang ini, kalem juga",  
                "pesan":"semangatt ya bang menjalani kuliah kakak "# 13
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "cantik, lucu dan keliatan berwiibawa kak",  
                "pesan":"semangatt kakk untuk kuliah kakak dan kehidupan kakak"# 14
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "lucuu kak, manis juga kak",  
                "pesan":"semangattt kak menjalani hidup kakak dan perkuliahan kakak"# 15
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "abangnya asik, suka ngejokes dan chill banget",  
                "pesan": "semangatt bang menjalani hari hari mu dan keseharianmuu"# 16
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "islami dan religius bangett kakak ini",  
                "pesan":"semangatt ya kak menjalani hidup kakak dan keseharian kakak"# 17
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "cantik lucu banget kakak ini, humoris, enak koordinasi nya juga",  
                "pesan":"semangatt kak mine menjalani hari dan kehidupan kakak, semoga pkm kakak menang yaa kak"# 18
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "lucu banget kak mutt ini, asik juga diajak ngobrol, ga lupa cantiknyaa ga ketinggalan",  
                "pesan":"semangattt kakak kuliahnya dan juga menjalani kehidupan kakak, semoga di lancarkan segala"# 19
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "abang ini pendiem, tapi asik banget sebenernya",  
                "pesan": "semangatt bang kuliahnyaa"# 20
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "asik banget kakak ini, terbuka dan enak diajak ngobrol, suka koordinasi nya juga",  
                "pesan":"semangatt kak menjalani kuliah kakak dan semuanya, semoga kita ketemu lagi yaa kak di satu departemen"# 21
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "bang aldi ini asik banget, humoris, enak juga di ajak ngobrol, best lah pokoknya",  
                "pesan":"semangatt ya bang kuliahnya, dan menjalani sisa periode ini, soon kadep?kadiv? atau kahim ini bang?"# 22
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "cantik kakak ini, asik juga, tapi kadang agak nyeremin, tapii asikk banget deh pokoknya",  
                "pesan":"semangatt kakak kuliahnya, jangan demis duluuu ya kak"# 23
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakak ini juga cantik bangett, ketawanya juga manis, enak buat diajak ngobrol",  
                "pesan":"semangatt kak byla, menjalani kuliah dan kehidupan kakak"# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FtmAumH7ggI21yR9dc4x3pdoMzPvOI09", #1
            "https://drive.google.com/uc?export=view&id=1vo1t0G_N-PXVRub3S9IQvh2f5mx4kAlm", #2
            "https://drive.google.com/uc?export=view&id=1h_K2zLowQePN-Ef-UKgDvWbXJbWSxGK1", #3
            "https://drive.google.com/uc?export=view&id=1VLwHZ9G6-lcmNGubkHzbBtnJRNvuhzUf", #4
            "https://drive.google.com/uc?export=view&id=1OvwmbPp5JUnQgbLkwLq98LxVinEv9ZxL", #5
            "https://drive.google.com/uc?export=view&id=1MRusjVnhQGsEAdQh4Ie7DmbJW2BSqWWE", #6
            "https://drive.google.com/uc?export=view&id=1kmj2zc5SF3ijTOtZ7T_X5knpqdetDzfT", #7
            "https://drive.google.com/uc?export=view&id=11n6hJ79kDD_K-lErBWEMNb-WJ0xkQDet", #8
            "https://drive.google.com/uc?export=view&id=1KSGz0perASXOmkhRgltAbwTBB-PymIfS", #9
            "https://drive.google.com/uc?export=view&id=1ZowycxedMnHW1NzAkLlekr5M97CVboTe", #10
            "https://drive.google.com/uc?export=view&id=1pKkiiOvQAR4Mp3DC8kaZFgc2bs3FRoM8", #11
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": "keren abangnya, semua bisa dicapai, multi talent, jago ngoomong juga",  
                "pesan": " Semangatt bang kuliahnya, semoga pkm abang menang terus, dan tercapai semuanyaa"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "kakaknya keren baik, lucu juga",  
                "pesan": "semangatt kak kuliahnya, semoga di lanacarkan urusanny"# 2
            },
              {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "kece abangnya, asik juga abangnya, ganteng juga bang ga ketinggalan",  
                "pesan": "semangat terus bang kuliahnya, semoga di lacarkan, btw ada stock california ga bang? hehe"# 3
              },
              {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya ramah banget, murah senyum juga",  
                "pesan": "semangat kak kuliahnya, semoga di perlancar kuliahnya"# 4
              },
              {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "kakaknya lucu, ramah, baik bangett",  
                "pesan": "semoga diperlancar segala urusan perkuliahannya"# 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "lucu kakaknya, murah senyum juga",  
                "pesan":"semangatt ya kak kuliahnya, semoga di perlancar"# 6
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "kece, pendiem, suka menyendiri",  
                "pesan": "semangatt bang kuliahnya, semoga di lancarkan"# 7
            },
              {    
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "lucu kakanya, murah senyum",  
                "pesan": "semangatt kuliahnya kak, semoga di perlancar segala urusanya"# 8
            },
              {
                "nama": "Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "cantik baanget kakaknya, lucu juga",  
                "pesan": "semangatt kak kuliahnya, semoga di perlancar segala urasannya"# 9
            },
              {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "lucu kakaknya, murah senyum",  
                "pesan": "semangat kuliahnya kak, semoga diperlancar segala urusannya"# 10
            },
              {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "cantik kakaknya, lucu juga kalo senyum",  
                "pesan": "semangatt kak semoga di perlancar urusan kuliahhnya"# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1r-wRYeCYWmko3fRndEJASTANy7T_qmgs", #1
            "https://drive.google.com/uc?export=view&id=1HYrPs64dGWmOpwJSGaHeMpKr-IoYOpj7", #2
            "https://drive.google.com/uc?export=view&id=1EAPiWB_ODTMxOTQsYQg7GWdi6H2wgSk1", #3
            "https://drive.google.com/uc?export=view&id=1gO6HIWkqE2CURvLmR51FhsawbMqE10HR", #4
            "https://drive.google.com/uc?export=view&id=1OHf1XurdzRAU4vBsHJuV6uDxzvx3SySl", #5
            "https://drive.google.com/uc?export=view&id=1bdaUKpaootNwkyj-SIDz7KFMrg0J14Z3", #6
            "https://drive.google.com/uc?export=view&id=1Bgx4LnEXEvKQFboVYLPSnSPpxsLEwort", #7
            "https://drive.google.com/uc?export=view&id=1Pu9QjbhC8diwYiAnyfUn62Ii0uGOOX-g", #8
            "https://drive.google.com/uc?export=view&id=1I3BuZM-Mgz6VpRFGTLhYGw8JnGPyj8Zk", #9
            "https://drive.google.com/uc?export=view&id=1NKrBxSICRgNIC0Ociz1di13SlHM43PPr", #10
            "https://drive.google.com/uc?export=view&id=1fDGuslDchilm58tk0YAmFS2VMxMGIQoJ", #11
            "https://drive.google.com/uc?export=view&id=1tcHXqQAd0SCqYtO3KLExGs6k7ECML6wM", #12
            "https://drive.google.com/uc?export=view&id=1QiRCAoTRnMysRxL02iyZGuTvOgyQdIs2", #13
            "https://drive.google.com/uc?export=view&id=14q-8WtDSb7NFrJ0leBBlhJ76g2Sd3g-S", #14
            "https://drive.google.com/uc?export=view&id=1HiTjxc5o0ugf1QVdcY6RMONyi7kHMUP3", #15
            "https://drive.google.com/uc?export=view&id=1S_mRMdRtKmBiwKQXOW2PNglloj8QQjsh", #16
            "https://drive.google.com/uc?export=view&id=1gerLyDfG7HpfXncVm7UiuwIX92ZlI3Cr", #17
            "https://drive.google.com/uc?export=view&id=1cyfL-5zIr4sWqwtmt86S1Qc2l7yAd_Fq", #18
            "https://drive.google.com/uc?export=view&id=1_4hQ2WBD8bjj28AkWmpZ0H3u_Di4ZtDW", #19
            "https://drive.google.com/uc?export=view&id=1stUbZd9wuZP7x77o8kaiFRc4VhhuS6bg", #20
            "https://drive.google.com/uc?export=view&id=1stM4UAvNQ8NeVgVCaguitqQozcvUL8vl", #21
            "https://drive.google.com/uc?export=view&id=1tZz44NEmJHFqQxkWqQ01219kKDe0jWn8", #22
        ] 
        data_list = [
            {
                "nama": "Randra Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "keren abangnya, jago ngomong juga",  
                "pesan":"semangatt terus bang kuliahnyaa"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "baikk, lucu, murah senyum",  
                "pesan":"semangat teruss kak kuliahnya"# 2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "keren, vibesnya ambis banget gitu",  
                "pesan":"semangat terusss ya bang"# 3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishahi",
                "kesan": "religius banget kakak ini, kalem jugaa",  
                "pesan":"semangat teruss ya kak"# 4
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "keren bang fadil, penyampaian nya juga keren",  
                "pesan":"semangatt terusss bang dutaa"# 5
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "chill banget, asik, tegas juga",  
                "pesan":"semangatt bang kuliahnya dan menjaga GH"# 6
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "kerenn bang, ganteng juga abangnya",  
                "pesan":"semangatt terus ya bang kuliahnya"# 7
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "cantik bangett kakak ini, lucu juga kalo senyum",  
                "pesan": "semangatt kakk kuliahnya"# 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "lucu kakaknya, senyumannya manis, keren juga",  
                "pesan": "semangatt terus kak menjalani hari hari kakak" # 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "pendiam, tapi aslinya asik banget abang ini",  
                "pesan":"semangattt terus bang menjalani hidupmu"# 10
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "lucu banget kakak ini kalo senyum, ramah juga",  
                "pesan":"semangatt kak kuliahnya semoga di lancarkan urusannya"# 11
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "cantik kak, lucu juga kakak ini",  
                "pesan":"semangatt terus ya kak menajalani kuliah kakak"# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "baik, ramah, lucu jugaa kakak ini",  
                "pesan":"semangatt teruss kak menjalani kuliah kakak"# 13
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "religius bangett kakak ini, kalemm bangett",  
                "pesan":"semangatt terus kakak kuliahnya"# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asramam TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "tegas, lucu juga kakak ini, kerenn deh kak",  
                "pesan":"semangatt ya, semoga di perlancar ururusannya"# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "keren abang ini, ganteng juga",  
                "pesan":"semangatt ya bang kuliahnnya"# 16
            },
            { 
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "lucu bangett kakak ini, pose fotonya juga lucuu",  
                "pesan": "semangatt terus kak menjalani hari hari mu"# 17
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "keren, berwawasan luas gitu",  
                "pesan":"semangat bang biyo cakahim, semoga di lancarkan, ditunggu webnya rilis bang"# 18
            }, 
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "keren bang, vibes coding banget",  
                "pesan":"semangatt terus bang kuliahnya"# 22
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "baik, cantik, ramah juga",  
                "pesan":"semangattt terus ya kak"# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d",
                "kesan": "baik, ramah, murah senyum",  
                "pesan":"semangatt terus yaa kak kuliahnya"# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "mirip pak tirta, kece",  
                "pesan":"semangatt terus bang kuliahnyaa"# 21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oGKypx5OxNseg_78SyBd0jo1GwAdNX4j",
            "https://drive.google.com/uc?export=view&id=12yuRtZw_MA5XzSd-Mmw8YDBDR64mEe_k",
            "https://drive.google.com/uc?export=view&id=15ZG_4D24SLlWubobRWl_mothEfKL6osR",
            "https://drive.google.com/uc?export=view&id=1QzuutQmNWxz7_WxjmWdo6r5KmkVft3-z",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "tegas, penjelasannya keren dapat di pahami, kerem juga bang bintang",  
                "pesan": "semangat bang mengkaji segala permasalahan itera, semoga di perlancar urusannya"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "lucu, cantik banget kakaknyaa, adem diliatnya",  
                "pesan": "semangat kak kuliahnya, semoga di perlancar kuliahnya"# 1
            },
              {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "religius, positif banget diliatnya",  
                "pesan": "semangatt kak kuliahnya, btw kakaknya jago OBE, semangatt trus kak"# 1
            },
              {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "lucu kakaknya, pendiam",  
                "pesan": "semangat kak  kuliahnya, semoga diperlancar kuliahnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Q642ZMtqqojD9moh_-A5LjYpeimyhREC", #1
            "https://drive.google.com/uc?export=view&id=1PdTGoBc_sDn-BcgegbIA2CFT9K29zvmM", #2
            "https://drive.google.com/uc?export=view&id=1PtTbbmU13kWVv3vmGDabHbt5zZS2gVFP", #3
            "https://drive.google.com/uc?export=view&id=1Ad8MYDT5sCTjWCHhT5eUZKAPtO3xB0W5", #4
            "https://drive.google.com/uc?export=view&id=1xFBDfZxZ7kC6XSNhL_1h0bDMwkv9-_1Z", #5
            "https://drive.google.com/uc?export=view&id=1qS77sOAZMwWDFKwdlcNkE8IJjJuGPdkB", #6
            "https://drive.google.com/uc?export=view&id=1ZUxAvvlu8kYItoXof6x8DFl3lx4g1V21", #7
            "https://drive.google.com/uc?export=view&id=1OlzEmDhLBOYrdltIAgMwJMD13ohCPRC8", #8
            "https://drive.google.com/uc?export=view&id=1ddCSgIqeZzNx_9q8J9nOz7bHnOxQH0Y_", #9
            "https://drive.google.com/uc?export=view&id=10nGBpRSl-ZA6IBQNGuSizW4yfsm0xMPx", #10
            "https://drive.google.com/uc?export=view&id=1E4cjeA4Vwcipb9cC2pjCCCyrngR6SG0y", #11
            "https://drive.google.com/uc?export=view&id=1tA7_2w8N4WnxWkF1NkaPVwvzr_mExJYV", #12
            "https://drive.google.com/uc?export=view&id=11dM-QPUOv_qQDiiCRQi-V9dwbQ2C65w9", #13
            "https://drive.google.com/uc?export=view&id=1mMBcJPPU68S6-XkD1uuMaI9KXsK0dKJz", #14
            "https://drive.google.com/uc?export=view&id=1pD9DKF0FxVJVY0uzl_IPBcLD5-827US5", #15
            "https://drive.google.com/uc?export=view&id=1xG2FAJg-icIfA2F7KzsluCCSbkDtAy71", #16
            "https://drive.google.com/uc?export=view&id=14n-ISRh6CLadjHq2joQG0sz22kKZPhi4", #17
            "https://drive.google.com/uc?export=view&id=1kTMtEs3_zuP0A2xZuHnTb3sq6heGfcNB", #18
            "https://drive.google.com/uc?export=view&id=1pf9yOk8y07iO--nE6FJiOLfIsNudPrgT", #19
            "https://drive.google.com/uc?export=view&id=1rGE6JrSY-wcA1X9_mxKs8HfNiO_Z1lCw", #20
            "https://drive.google.com/uc?export=view&id=1pf9yOk8y07iO--nE6FJiOLfIsNudPrgT", #21
            "https://drive.google.com/uc?export=view&id=1jiynOTrVRo1_RhMa_9MxLg0E2D9U-bhH", #22
            "https://drive.google.com/uc?export=view&id=1OOlGZuJQrww68RPQxfn0mblWbpe5XfeD", #23
            "https://drive.google.com/uc?export=view&id=1MAkavC8JJ51imMp_q78tvywGEUg_aHzD", #24
            "https://drive.google.com/uc?export=view&id=1rl3NTbzKcaahtgnQJWKDfsqd8zjM1dn1", #25
            "https://drive.google.com/uc?export=view&id=1zwt2UBNwMUWTHlKK4Mk5Rp_alPOfviVc", #26
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ferdy_kevin",
                "kesan": "tegas, suka gayanya memimpin, banyak tindakan, humoris pastinya",  
                "pesan":"semangat bang menjalani semester 7 nya, semoga cepet selesai"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpsu",
                "hobbi": "Jalan jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "lucuu dan cantik, meyeramkan",  
                "pesan":"semangatt kakak kuliahnya, semoga semua nya di lancarkan"# 2
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "tegas banget, asik, suka bercanda juga",  
                "pesan":"semangatt kak menjalani tahun akhir kakak, semoga cepat selesai"# 3
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky_",
                "kesan": "asik, berwibawa, enak banget di ajak ngobrol",  
                "pesan":"semangatt bang, semoga tercapai presmanya bang"# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "cantik banget kakak ini, tapi mukanya serem kak",  
                "pesan":"semangatt kak menjalani kuliah kakak dan kehidupan kakak"# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "serem, asik kalo lagi ngobrol santai",  
                "pesan":"semangatt bang menjalani kuliah dan keseharian abang"# 6
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "tegas, asik, suka bercanda",  
                "pesan":"semangatt bang waketang, semoga dilancarkan semuanya "# 7
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "cantik, tegas",  
                "pesan":"semangatt kak menjalani harinya dan semangat lombanya kak, salam buat zefa kak"# 8
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "tegas, asik banget, chill, suka berdialog",  
                "pesan":"semangatt bang menajalani harinya dan perkuliahannya"# 9
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "tegas, ramah, menyeramkan",  
                "pesan":"semangattt bang aji menjalani hari dan kehidupan abang"# 10
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "cantikk kakak ini, tapi nyeremin, baik juga",  
                "pesan":"semangattt kakak menjalani perkuliahan dan kehidupan kakak"# 11
            },
             {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "asikk banget, chill, santai orangnya",
                "pesan": "semangattt bang menjalani perkuliahan akhirnya" # 12
            },
            
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "asik banget, chill banget",
                "pesan": "semangatt bang menjalani hari abang dan ayo bang mabar valorant" # 13
            },
            
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "asikk banget kakak ini, tapi mukanya serem",
                "pesan": "semangatt ya kak, segalanya deh semangatt" # 14
            },
            
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "lucu dan cantikk kak, serem terkadang",
                "pesan": "semangatt ya kak menjalani perkuliahan kaka, btww kita satu sekolah kak, saya adkel kakak" # 15
            },
            
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "lucuu kakak ini, asik juga, tapi seperti nonchalant gitu",
                "pesan": "semangatt kak menjalani hari hari kakak dan perkuliahannya" # 16
            },
            
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "asikk, suka ngobrol, enak ngobrol sama bang maul",
                "pesan": "semangatt ya bang menjalani perkuliahan abang" # 17
            },
            
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "asik, suka sport, chill bangett",
                "pesan": "semangatt ya bang menjalani hari abang" # 18
            },
            
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "asik, chill banget",
                "pesan": "semangatt bang menjalani hidup abang beserta perkuliahannya" # 19
            },
            
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "pendiem, lucu, asik",
                "pesan": "semangatt kak kuliahnyaa" # 20
            },
            
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "lucu, kocak, asik bangett, melihat abangpun lucu",
                "pesan": "semangatt bang menajalani kuliah abang" # 21
            },
            
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "serem, aslinya asik dan humoris, gampang bercanda, jago piano",
                "pesan": "semangatt bang kuliahnyaa, ajarin piano bang" # 22
            },
            
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "serem, tinggi, seriuss",
                "pesan": "semangatt bang menajalani harinya, jangan lupa senyum bang" # 23
            },
            
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "lucu, suka dance, susah di cari",
                "pesan": "semangatt kak menjalani kuliah kakak dan semester 5 nya" # 24
            },
            
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "positif vibes, asik, chill",
                "pesan": "semangatt kak menjalani hari kakak" # 25
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "chill, asikk",
                "pesan": "semangatt bang menajalani perkuliahan dan lainn lain bang" # 26
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()


# Tambahkan menu lainnya sesuai kebutuhan































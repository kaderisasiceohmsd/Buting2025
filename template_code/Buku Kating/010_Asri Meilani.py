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
            "https://drive.google.com/uc?export=view&id=1PjDH7OOlezbFhQhkoLTO-VH42R9STe2a",
            "https://drive.google.com/uc?export=view&id=1qJsSTObs1BnOy4NWqifqoEQIdUm0d73J",
            "https://drive.google.com/uc?export=view&id=1E1PKD6li0zUXSQxFQMvvnk-CucaKtb2-",
            "https://drive.google.com/uc?export=view&id=1wX4a2sKVOxY6mpluE5ZKzgHLvVo7APK7",
            "https://drive.google.com/uc?export=view&id=10FPgNdXfN7XCIDxy_LGtpa1ATaft87ne",
            "https://drive.google.com/uc?export=view&id=12_cNtlEVokNKbJt5_qt_p905MNCxMvl8", 
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
                "kesan": "bang rendra ternyata asikk banget ternyata lucu bangett, aku kiraa bakal yang serius banget",  
                "pesan":"semangatt teruss yaa bang, keep humblee serius abang seruu banget"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL!",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "awalnyaa takut sama bang jo tapi ternyata abangnya seasik ituu",  
                "pesan":"semangat teruss bang"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Badui",
                "alamat": "Ayrest Kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknyaa baik bangett sangat lovelyy huhu, cantik jugaa positive vibes banget",  
                "pesan":"semangaat yaaa kaa, tetap positive vibes selalu yaaa"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kaa syadza lucuu",  
                "pesan":"semoga sukses terus yaa kak, semangat kaa"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "KAKAK SERU BANGET PLIS?? seseruu ituu",  
                "pesan":"SEMNGAAT TERUS KAA"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakanya glowing banget...",  
                "pesan":"kakaa spill skincare pliss"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VUdhrvunM4RDP8Ej9Qu4QU6TwOYSRd-5",
            "https://drive.google.com/uc?export=view&id=14tG7BgPgSIIaVTgwFo0XqaCO_Z3S1tC3",
            "https://drive.google.com/uc?export=view&id=1Bqfq6CL9n0Ckjind_NfkLYSjtADuSTf4",
            "https://drive.google.com/uc?export=view&id=1Q8SNsqZ9uRKEOsab-yG-sDc0KrQ2gfDV",
            "https://drive.google.com/uc?export=view&id=1gpGGLBOLn51_IoZDcqQSFUQFw06v_Seb",
            "https://drive.google.com/uc?export=view&id=1nFO_ThvKzUhSEontUdFrQ8LZVmn9IS8U",
            "https://drive.google.com/uc?export=view&id=1S-QINmcMghj3dHLyT3Qz_bKJ9B1UGYzG",
            "https://drive.google.com/uc?export=view&id=1HP1qxjcjka29mEmQ4ukCC91BpO_I13CW",
            "https://drive.google.com/uc?export=view&id=136rrnWpg0Y_z_w4CHF6JCy7i-nF-zXVu",
            "https://drive.google.com/uc?export=view&id=1c6Sq9ztNZRVEPfszTJyIZYnsOGCxQb41",
            "https://drive.google.com/uc?export=view&id=1GFs9MUCojY1sdkGgyXjyq-HSamPmlk5U",
            "https://drive.google.com/uc?export=view&id=1YRuH09i7OBBCx4S-8MqJ1ehvZ4tkT6w9",
            "https://drive.google.com/uc?export=view&id=10cAEfu-Pviqwe2lKMnscGy7eExYcM3M4",
            "https://drive.google.com/uc?export=view&id=1KCOuUEc8sG0H-qFj2IFTzoTlXpNkP5g7",
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
                "kesan": "kemarin sempet nyasar pratikum alpro di RA dan aspraknya bang jere, baik bangeeet ciyuus dlnyaa dipanjangin huee penyelamat hidup, asik banget juga abangnya ngelawak teuss",  
                "pesan":"bangg cocok banget jadi stand up comedy, next fg yaa bang!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "kaa deaa lucuu amay, ini fotonya sampe bingung mau pose apa karena kakanyaa gamau pose yang samaa",  
                "pesan":"semangatt terus kaa kuliahnyaa, jangan lupaa mam yah"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "kak renisha skenaaa banget pliss??? aku kira anak dkv awalnya. SUPER CANTIIIK",  
                "pesan":"KAA HATI HATI jualann pancingnyaa, dan semangat terus yaaa"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "kakaa cancii lucu bangett",  
                "pesan":"semangat terus yaaa kaka kuliahnyaa, have a nicee daay<3"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "pertama kali liat bang daru waktu pplk kaya WOW BELIAU MAKAN APA YA??! kok bisa bisanya ipk 4 keren bangettt",  
                "pesan":"semangat bangg, pasti cumlaude deh bang dharu"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "kakaa bagus banget rambutnyaa gemes, cantikk bangettt, lucuu tapi intimidating jugaa aura baleg",  
                "pesan":"semangatt yaa kak feby menjalani harii nyaa, have a nice day kaka cantikk <3!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "INI SIHH HARUS LONG TEXT YA. bang gipayo best mentor aliveee PLS MASUKIN BANG GIP JADI BEST MENTORRRR SERIUS BEST BANGETTTTTTTT. perhatian banget salut, selalu tanya keadaan anopapeeps di tengah kesibukan bliau ini. bang gip juga selalu nyempetin qtimee sama anova online di dsc ataauu ketemuu, bahkan sering bang gip yang ajak duluaann keren bangeettt. bang gip ga pernah marah sampe aku kepikiran takutnya bang gip banyak unek unek ke anova :( TP BNERAN KOK BISA GA PERNAH MARAH BANG)",  
                "pesan":"SELALU JAGA KESEHATAN BANGGGG plis pikirin diri sendiri jugaa yaaa, makasi banyak sudah jadi mwntor anova paling hebat sedunia indonesia raya, semangatttt terusss bang gipp!!!!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "bang jujur... vibesnya PDD banget.. kirain medkraft kak",  
                "pesan":"PLS BANG ATURANNN KUCINGNYA BAWAAA AJAA!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Catur",
                "sosmed": "@berlyyanda",
                "kesan": "KAKAA positive vibes sekalii canciii",  
                "pesan":"semangat terus kuliahnya kaaa!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandiama",
                "alamat": "Way Huwi",
                "hobbi": "Minum air putih 8x sehari",
                "sosmed": "@j__eesie",
                "kesan": "vibes dan mannernyaaa duta banget jujuuur, cantikk, positive vibes dan seruu banngeettt PAKE KOMPLIT",  
                "pesan":"semangat yaaa kakaa duta menjalani harinyaaa"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Nyanyi tabola bale",
                "sosmed": "@iamridhomanik",
                "kesan": "hai.. bang ridho.. baik bannget bang ridho, lucuu amay sama kaka anu",  
                "pesan":"tetap lucu dan menghibur orang sekitarr selalu bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Koleksi Stiker",
                "sosmed": "@fer_yulius",
                "kesan": "wooop abang chill ",  
                "pesan":"tetap santai bang, sukses terus kuliahnya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Papua Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "kakaaa cantik baikk banget",  
                "pesan":"semangat terus kak monica kuliahnyaa"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "kakaa baik dan positive vibes bangett, pertama kali liat waktu tpb perwakilan kelas atau Data BABIBU YAA AKU LUPAAAA tapi kakaknyaa sebaikkkk ituuu top",  
                "pesan":"semangat terus kakaa kuliahnyaa dan main bolanya (?)"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xqr-SrF1iIDl14I3S711TdiDF0wvDtK4",
            "https://drive.google.com/uc?export=view&id=1Ue2IZ6w-NykAmWoaR6USKk1-_ZdZ_STp",
            "https://drive.google.com/uc?export=view&id=1uFWscQl4qiVms6ipU0Vi3DMgk6p17zjn",
            "https://drive.google.com/uc?export=view&id=1aFfa9WTkWgvth09FysXgOO0zspuwh6fd",
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
                "kesan": "SERUUU BANGET PLS BENER BENER KETAWA TERUSSS, kirain karenaa senat akan sangat serius ternyata seru paraah bang",  
                "pesan":"semangat terus bang senat! plis terus ngejokes yaa bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu, maen roblox",
                "sosmed": "@nadyaanjanani",
                "kesan": "kakaknyaa cantik bangettt plisss mulus banget salfok",  
                "pesan":"salam untuk abang mentor kak, semoga langgeng hihi parentsssss lucu bangett. semangat terus kaa kuliahnyaa sukses terus kesenatoran"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Ice Skating",
                "sosmed": "@fathinahazzh",
                "kesan": "kakaa jujur pertama kali liat mirip banget sama raisya anak akt akuu, kerenn bannget kaa kerasa banget vibes pinternyaa",  
                "pesan":"semangattt kaaa kuliahnya yaaaaa!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "kakaa lucuu dan baik bangett, namanyaa unik banngett kenapa tida mau dipanggil ka ichi aja ka lucuuu",  
                "pesan":"semangat teruss kaaa menjalani harinya, semangatt kuliahnyaa kaaaa!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13mcw7lRYGmaXK4-kmva7d-UQ5mofwG3b",
            "https://drive.google.com/uc?export=view&id=1X1B1mtUkC8NjGjmcRIEOIcSNe0eK3BHM",
            "https://drive.google.com/uc?export=view&id=1YpIy1-s0gBjrO4gjK7iwZHx4J1ee4AYS",
            "https://drive.google.com/uc?export=view&id=10lGFcD_7ZArRLmHXs-wqLgZC7OvE74mK",
            "https://drive.google.com/uc?export=view&id=1tYld0pmXXclS4mGFhLmJNJOU-pPLVIMh",
            "https://drive.google.com/uc?export=view&id=1q9CYlbH-ArD4TDgTp3WoA99e9WzILcUH",
            "https://drive.google.com/uc?export=view&id=1kzlPXbsW0PYMwDFBwk4vSx1Txy3k-Eq4",
            "https://drive.google.com/uc?export=view&id=1bR7hc7ggp-jBaWFu8nkZEKN1HUKb1yQh",
            "https://drive.google.com/uc?export=view&id=1YX-DS0vg4-VNZ8D1ul-EpPm591vL87Si",
            "https://drive.google.com/uc?export=view&id=1CaL6nedRwn02rY-7khRFbAyYCX19wP-G",
            "https://drive.google.com/uc?export=view&id=1A-jfWpIygyeFDL1xfjQYmLrfyxXthXl3",
            "https://drive.google.com/uc?export=view&id=1KUICGBu7VaDsTwrIKFH1kyDsqfof4qUL",
            "https://drive.google.com/uc?export=view&id=1iRlSK1lGotMahVQcpWdkDMJmyG4Wi0i4",
            "https://drive.google.com/uc?export=view&id=1Y6PjlUUXROG5IFaQpTnWxAkOChRTsIfm",
            "https://drive.google.com/uc?export=view&id=1uWXaZcJ7RepxXOdofIOykk4N3Q1CYC2G",
            "https://drive.google.com/uc?export=view&id=1ROpWjATZ8tfkS5yhCsIW6OnFa-TfuwDk",
            "https://drive.google.com/uc?export=view&id=1QEIpHxh1VZzaoyIGhbeNhoVQ3Q4WHKUz",
            "https://drive.google.com/uc?export=view&id=1cYfttaj5nG3oxb40pzdtnpfcdu-3QxjZ",
            "https://drive.google.com/uc?export=view&id=1rMsYw5MxrBs0A0MhrMj8jCNKAyRvGiV0",
            "https://drive.google.com/uc?export=view&id=1gLR-NPHJ7V-8-CTL-K8Tx0j7v_4r3wUa",
            "https://drive.google.com/uc?export=view&id=1Pk938eFKy5P3AB_dwj5mJoh9RRFgjQVk",
            "https://drive.google.com/uc?export=view&id=1yhF5UT1YHL8lzQwjL6w8_Ci3972-QPOy",
            "https://drive.google.com/uc?export=view&id=1iTkvV8XEFFVF7aIHXj59sinC0nFfDZAt",
            "https://drive.google.com/uc?export=view&id=1lmWC33gXJUwskZzT4_fCgvVd2eisT4QW",
            "https://drive.google.com/uc?export=view&id=1nl16V6VqkskYShfLmnN0NLWG3W08dszd",
            "https://drive.google.com/uc?export=view&id=1pJaGjUtocLZ77cu4Ndh1SQ1tXG3FPxSB",

        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "haiii",
                "sosmed": "@ferdy_kevin",
                "kesan": "keren banget bang ferdy, panutaan",  
                "pesan":"semangat terus bang kadep, semoga sukses selalu!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya cantik bangettt dari awal ngeliatin langsung WOW, muka nya bener bener sebersinar ituuu",  
                "pesan":"semangat teruss kaa, sukses selaluu, dan have a nice day yaaaa"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "bener bener salut sama kak pasha, keren bangett jadi kadiv inii bener bener wow i cant be her deeh, girlboss panutan banget",  
                "pesan":"semangat yaaa kak pasha, jangan lupa istirahat kaa dan jaga kesehatan jugaa, sukses selalu kaa"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "baik banget, jago banget debatnya kerenn",  
                "pesan":"semangat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "dari awal emang salut banget sama kak arien, dari jadi perwakilan TPB udah ngeliat kak arien kerenn banget dan pengen banget bisa deket sama kak arien. bener bener sesalut itu. kelitannya semuanya balance gituu kak arien tuhh, organisasinya, akademiknya, semuamuanyaa POKOKNYA KEREEN BANGEETTT ",  
                "pesan":"semangat terus kak arienta! kakak panutan aku banget no #1 di angkatan 23"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "jujur takut sama bang daffa keliatannya serem banget pas awal go, cumaa sepertinya diluar rangkaian bang daffa lucu deeh suka ngelawak gituu",  
                "pesan":"sehat selalu bang daffa, semangat semangat terus bang daffa dengan organanisasi bang daffa yang banyak ituuu udah ga kebayang se hectic apaa.. SEMANGAAAATTT BANG!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "awalnya segan banget karena waketang akt 23, tapi ternyata super duper baik waktu lagi jawab wwc abangnya bilang 'good job' kaya nyes gitu makasii banyak bang sudah menyebarkan energi positifnya",  
                "pesan":"semangat yaa bangg menjadi waketangnyaa, jaga kesehatan bang"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "duluu sempet ngobrolin kader sebelum kader sama kak nata dan kaget banget ternyata yang ngekader kakaknya, baikk banget kasih banyak saran waktu ngobroll se easy going ituuu",  
                "pesan":"semangat kakak bendaharaa, sukses terus dan jagaa kesehatan yaa kaa"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "asprak pks semester 2 yang super duper baik, beneer bener baik banget selama jadi asprak dan cara jelasinnya sebagus, jujur lebih paham di ajarin bang nobel daripada sama bapaknya kemarin",  
                "pesan":"semangat terus bang nobel, semoga sehat selalu dan makin makin jago lagi ngodingnya"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "bang commander yang sangat berbaik hati, dan sangat mengayomi, kemarin sempet diawas saat UTS ADS dan ternyata abangnya se asik ituu",  
                "pesan":"semangat terus bangg, keep blooming bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang Berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kaa vany cantikk, OOTD nya sukaa bangett",  
                "pesan":"semangat teruss yaa ka vany, havee a nice day kaaa"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "abangnya chill bangettt buat gaa takut dann abangnya ramah banget bangett",  
                "pesan":"makin makin jago bang main badminnyaa"# 1
            },
            {
                "nama": "ALi Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang 4 Nangka Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "abang op sciencefest bener bener helpfull banget selama gladi mc, abangnya santai orangnya dan baikk banget",  
                "pesan":"semangat terus bang yaaa ali!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "KAKAAA CANTIK samaa banget aku juga hobi tidur kaa, kakak super chill",  
                "pesan":"tetap semangat kak gustiii, tutorial life tetep balance tapi tetap bobo jugaa kaa"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaa baik bangett aku udah mikir kayannya kakanya serem deh, ehh pas wwc ternyataa baik banget dan se soft spoken ituu",  
                "pesan":"jangan lupaa makan yaa kaa jaga kesehatan dan semangat terus kuliahnyaa"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kakaa akuu kira kaka jutek gituu awalnya tapiii lucuuu banget ternyata lop lop",  
                "pesan":"jangan lupaa istirahat yaaa kaaaa, semangat sampaii mendapat gelar ituu"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "ABANGNYAAA BAIK BANGETTT waktu wwc bener bener kasih wejengan yang sangat membangun, dan ramah banget kalo ketemu pasti balas senyum",  
                "pesan":"semangat terus yaaa bang, pls abang kalo kasih wejengan kata katanya baik banngettt semoga terus seperti ituu bang"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_",
                "kesan": "keceeee parah vibesnya abang tongkrongan abiezttt",  
                "pesan":"semangatt banggg terus mencetak juara juara dan calon juara juara ituu bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "kakanyaa kadiv tarii pplk gaaa sihhh kerenn bangettt, denger dari anak tari juga sudah sepakat kakaknyaa baik bangett dan selovely ituu",  
                "pesan":"semangat terus kakaaad dancernya!"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Belajar Front end",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnyaa ramaaah polll, keren banget kaloo lagi mc",  
                "pesan":"seruuuu terus yaa bang!"# 1
            },
            {
                "nama": "Kevin Antoni JUnior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Berdiri, Nyantai",
                "sosmed": "@kevinaj_",
                "kesan": "jujur aga segan sama bangnyaa tapi baik bangettt",  
                "pesan":"semangat bangg basketnyaa!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakanyaaa kalem bangettt dan lucuuu, gemes banget kakaa hobinya merajuk",  
                "pesan":"semangat terus kaaa, janganlaa merajuk"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "abang baik banget bang, cocok banget sihh jadi korlap banng kayaa melekat banget",  
                "pesan":"jangan lupa makan bang, hati hati selalu bawa motornya, semangat terus bang!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main futsal, voli",
                "sosmed": "@sidabutar.26",
                "kesan": "bang benget seringgg banget jadi topik hangat di grup damaskus, pasti abangnya seru dan gokil banget deh",  
                "pesan":"semangat bang kuliahnyaa"# 1
            },
            {
                "nama": "Wuliano Wiliam Purba",
                "nim": "123450098",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngoding",
                "sosmed": "@liano.wlm",
                "kesan": "jujur segan banget sama abang ini.. bener bener aura nya ada banget dan cooool banget",  
                "pesan":"semangat teruss bang, semoga sukses selaluuuu!"# 1
            },
            {
                "nama": "-",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@-",
                "kesan": "-",  
                "pesan":"T-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tSIrRXg1MH3Zp_Bve-_MDKuAz91HkW2O",
            "https://drive.google.com/uc?export=view&id=1MttJU9CCUopujMf-RohcmQKOirr5w995",
            "https://drive.google.com/uc?export=view&id=1k2nLE1IMvoy4m1zN99-E8vPIGgrr6aj9",
            "https://drive.google.com/uc?export=view&id=1j1M9vtHEBmW6qXD16PbXx3ITPIipCzXS",
            "https://drive.google.com/uc?export=view&id=1VId_LSSvfxtZq4U7TLcogpx2HEQcyAb0",
            "https://drive.google.com/uc?export=view&id=1QjVnkAFFMsltgvFJAbmwD9ywIuNBWjnJ",
            "https://drive.google.com/uc?export=view&id=1kVKInLTumx1yG2L-R5AwNRxd9-yXDjnq",
            "https://drive.google.com/uc?export=view&id=1CrTvYU1fi3I9MyMx5PUmmW_mlOTycEFx",
            "https://drive.google.com/uc?export=view&id=1GT0wGxoNq84dHPjAkvmLKELpk9EaEZfM",
            "https://drive.google.com/uc?export=view&id=1hdTXn59XxhhSzevHLOgEnXePydq_rwne",
            "https://drive.google.com/uc?export=view&id=1Uxdp4a-GO91bUvH-Oh_LlFEl9KR0NEbB",
            "https://drive.google.com/uc?export=view&id=1C_E-YpnKvrs5Dhl5WJePdYFLrqlHJqy8",
            "https://drive.google.com/uc?export=view&id=1_aHgcO_Jur7Apk0Gq3aG8HRHXyRZtV03",
            "https://drive.google.com/uc?export=view&id=12MS6C4Yy03UQj6FDGBs1UOlufeq0bfaO",
            "https://drive.google.com/uc?export=view&id=1cjEI7Ul8T4yQ5BQGKDk2UuzN6Cl9TL54",
            "https://drive.google.com/uc?export=view&id=10Y_n2qR8viKRUIuLNSWbVNn4vI4peC_A",
            "https://drive.google.com/uc?export=view&id=1YJk2Fi32AdUtovw-ddXqBLpEiTzUowEB",
            "https://drive.google.com/uc?export=view&id=1B3MgMhK-iwGYO4-5283k4HoaOj3fZzMf",
            "https://drive.google.com/uc?export=view&id=1jjF7wnSvZ5-m6TtGD-sFGOCZtDBBtNTJ",
            "https://drive.google.com/uc?export=view&id=1Du-o6l4egJc1w0W1eDjbJpNcsDYck4xZ",
            "https://drive.google.com/uc?export=view&id=1f4hu_3ttZaJ1Ek-L-BX9p-ptN57iiRp_",
            "https://drive.google.com/uc?export=view&id=1LNReQEVgmkp3bX-y27O-Werw-AlMCirl",
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
                "kesan": "bang randra ramah bangeeeett",  
                "pesan":"semangat bang kuliahnyaa, jangan lupaa makann dan istirahat bang!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "haii kakaa, aura pinter gituu deyy kakanyaa",  
                "pesan":"ka...semangat dengan hobinya....!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "bang asprak, jujur kaya uang kaget kalo ngasprak 'LIMA MENIT LAGI' tapi gapapaa bang, abang asik baik dann auraa punter banget cihuy",  
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
                "kesan": "kakaknya kalem bangett",  
                "pesan":"semangat terus kuliahnyaa kak! mau ikutan maskeran pliss"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilafarizzii",
                "kesan": "pertamaa tau abangnya waktu final project AIESEC bang fadil sama pacar priti nya ituu, disitu first impressionnya hmz abangnya serius bangett, ternyataa aga tengil juga yaa bang dirimu he he he, dan keren banget bang duta date yah ini mah bukan study date lagi",  
                "pesan":"semangat terus bang! langgeng yaah sama pacarku yang priti ituuu"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "wuiiiss bang aqil baik poll dehhh",  
                "pesan":"bang stop jail bang pelish nilai tp aku jangann di spill. "# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik, nonton",
                "sosmed": "@notfall.s",
                "kesan": "abangnyaa chill paraah sihhh",  
                "pesan":"semangat terus bang kuliahnya, semangat menjalani hari harinya jugaaa"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "hayii kakaaa kalem bangettt",  
                "pesan":"haveee a nice day kaaa, jangan lupaa istirahat yaaaa"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "hiii kakaka cantikk nan multitalent",  
                "pesan":"semangat teruss menjalanii 'semualah' ituuu kak"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keylashafi_",
                "kesan": "vibessnyaa goodnoy bangett, cowo baik bangett gituu kalemm bang",  
                "pesan":"semangatt bang mentorrr"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "KAKAAA LUCUUUU AMAYYY DEEEEHHHHH gemecc banget",  
                "pesan":"kaa nonton konser bareng yuuk!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "KAKAK CANTIK BANGEEETTT",  
                "pesan":"semangat yaa kak kuliahnyaa"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@pebby_olla525",
                "kesan": "kaa baikk bangeeet ramah poll",  
                "pesan":"semangat teruss kaaa, semangat yaa nugasnya kaa"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakaa sciencefest kalemm banget vibesnyaa, adeem",
                "pesan":"semangat terus kuliahnyaa kaaa"# 1
            },
            {
                "nama": "Tanty Widyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "kaloo ngemc kereeeen bangettt sumpahh, aku fans kakak banget",  
                "pesan":"semangat terus kuliahnya kaa, ajarin aku ngemc kaya kaka plisss"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "konon abangnyaa sepuh koding.. asprak ads daan keren abiss",  
                "pesan":"semangat terus nge project nya bangg"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "kaa fifah sayang baikk bangett dan lucuuu banget gemeyyy",  
                "pesan":"semangat terus kuliahnya kaa fifah!"# 1
            },
             {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@i",
                "kesan": "ASIKKK BANGET BANG FABIOO",  
                "pesan":"semangat terus bang andd keep humoris!"# 1
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "abang ozt, kereeen poll",  
                "pesan":"semangat terus kuliahnya baang, mau foto sama om pamungkas...!"# 1
            },
             {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "kakaa lucuuuuuuu",  
                "pesan":"semangat kuliahnyaa ka, havee a nice daay yahh"# 1
            },
             {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "kakaa astut ALE yang super duper baik dan sabarr, salut bangett, soft spokenn",  
                "pesan":"semangat yaaa kak kuliah dan ngajar tutornyaaa!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "emang lumayan pendiem yah sepertinya abangnyaa, baik bangett",  
                "pesan":"semangat terus bang, jangan lupaa istirahatt bangg!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ylzgNz9_yQ_SjPLVVj0yH0IOuLJfjNil",
            "https://drive.google.com/uc?export=view&id=1wPb2iBc37hR2Hl4HZMBsukc06DKGEH9m",
            "https://drive.google.com/uc?export=view&id=1peMhHU9xeQm0VHG8MEbIyZEzgd7Iomod",
            "https://drive.google.com/uc?export=view&id=1MgEQhx5EMh9JzCE_meFmewjV-VEkYZzj",
            "https://drive.google.com/uc?export=view&id=1ZlWDbI8VI-kkj98vWNftIpgzxWdzzPpI",
            "https://drive.google.com/uc?export=view&id=1tGL4KITf12QVchJ1l0S1WVmRStlU4nm_",
            "https://drive.google.com/uc?export=view&id=135vTvWviCCrm_SwHnRD3ViiczQ9VKvZC",
            "https://drive.google.com/uc?export=view&id=1sKdS_b-Ee_kZBAKBW_Ml5k6AdHVAoUoN",
            "https://drive.google.com/uc?export=view&id=115EJUuiMq4HWDvQF5lY9Q4mJHYp4Ncw6",
            "https://drive.google.com/uc?export=view&id=1k7O1qg1dpFnOZPcSeWY1PS0ZierSE9n1",
            "https://drive.google.com/uc?export=view&id=1lDiPrTaB8m-juR6SzcuD9ePUuO4NM7Zy",
            "https://drive.google.com/uc?export=view&id=1KHohRyJ1cCCdSAtLE1N3gGnNE6al9QcW",
            "https://drive.google.com/uc?export=view&id=1LXDR34tQ0WKti-3Bilu5S2tYl36pquVB",
            "https://drive.google.com/uc?export=view&id=1PrlPfFpqBkSimtaHJMfUUuB2di8AVKwN",
            "https://drive.google.com/uc?export=view&id=1X1sblm_vpWWwqBJmOG5ns7ZbreK7NulM",
            "https://drive.google.com/uc?export=view&id=14EgkJtLSgMaohvxWEhLvGa6Y4rbDIVp3",
            "https://drive.google.com/uc?export=view&id=1BAXZneX5164Gx6aaBltY23FzmmrVZXo5",
            "https://drive.google.com/uc?export=view&id=1OQ3HbWkoXEBA-VvbpvXDpsjobp5mnKln",
            "https://drive.google.com/uc?export=view&id=1EXkQhSYUKjfEZUjiFTNoxx2rUN8llBtT",
            "https://drive.google.com/uc?export=view&id=1sZw1dWw6pLgTlB-f1J9JtZci61twTLWK",
            "https://drive.google.com/uc?export=view&id=1shlZYtCr5a9cFuPyEV2xKIfs7PY1r8uL",
            "https://drive.google.com/uc?export=view&id=19i2DwZn1fCwDq4Xiqje5JxTzCl8yL2-d",
            "https://drive.google.com/uc?export=view&id=1HE-UJ2lnPwtc--4FQwyHFpDhMkR7oJHl",
            "https://drive.google.com/uc?export=view&id=1-f0uxs_OZGTxbgf6eR6NRfRKepUHSVBl",
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
                "kesan": "bang arafi vibesnya kadep bangett pria matang, baik bangettt",  
                "pesan":"bang stop ketawain mc kitaa yang bang HAHAHA, semangatt teruss bangg, ajak kami ekstrakhecil viscom dong..."# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "KAKAAA CANTIKK SAYANG BAIKKK BANGETTTTTTT soooo lovelyyy",  
                "pesan":"Semangat terus yaaa kakaa lucuuu"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "kaaa minee kadiv terkeren terhebat tercantik terdebesssss, KAKAKK KOK BISAA KE HANDLE SEMUAA SIHHHH, nilai bagus, prestasi bagus, organisasi bagus, cantikk jugaa presentable terussss kaka mapresss. selama magang jugaa kaa mine bener bener baik banget dan sangat merangkul kami, banyak banget belaja sama ka mineeeee",  
                "pesan":"semangat yaaa kak minee pkm nyaaaa dan viscom juga at the same times..... hebat..... nanti pasar malem lagi plisss!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "haii kaa arinii, awal ngobrol sama kak arini dii sciencefest dan ternyata kakanyaa panit kader jugaaa. awalnya takut cius sama kak arini hueee tapi ternyata baik dan asik bangetttt. selama magang paling banyak ngobrol sama kak arinii <3",  
                "pesan":"semangaat kakaa pj exploringg, semoga exploring kita sukses huee DAN SEMANGAT KULIAHNYA KAAAA (bonusnya hatii hatii ka bawa mobilnyaa)"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "wuuuiss bang aryaa kereeen, lumayan jarang ngobrol tapi baikkk polllllll",  
                "pesan":"semangatttt terusss bang arya" # 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "KAKAAA CANTIKK INII UDAH NIIII KESAN PESANNYAA. kakaknya biak bangett suer prittyyyyy, asik banget jugaa soft bangettt",  
                "pesan":"kakaa ayoo main di lampung baratt, semangat yaaa kak mutmut kuliahnyaaa"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakaa ituannya bang anu yaa hayoo, baik banget kakaknyaa banyak belajar tentang forum sama kak lutfiaa, kakanyaa kalo lagi asbun lucuu bangett plissss",  
                "pesan":"semangatt kak lutfia menjalani harinyaaa"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "kaa bilaa astut ALE kematiaan huak i hate ale ale, gemeyy bangetttt kaa bila mirip loopy temen pororoooooo",  
                "pesan":"semangttt membantai viscom kaaa, semoga acaranya sukses jaya jayaaak!"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "missii bang ketuplak, mantaap banget deh bang aldii baik bangett dan sangat mengayomi ahay",  
                "pesan":"semangaatt yaa bang aldi, jangan lupaa istirahat bang!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "beluum pernah ngobrol banyak samaa kakanyaa tapi kakaknyaa baik bangettt saat wwc sepositive vibes ituu",  
                "pesan":"semangaatt terus kaa kuliahnyaa, have a nice day yaaaa!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "KAKAAA DUTAAA??? super dupa pretttyyyyyy, cantik bangett, mannernyaa baguss bangettt seduta ituuuu",  
                "pesan":"semangat terus kak dutaa dan kuliahnya!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "KAAA DEA IBUU BAYESSSS lucuu banget, periang parah, positiveeeeee vibess bannget kak yareuuuu ",  
                "pesan":"SEMANGATTT TERUS KAAAA HAVE A NICE DAYYYYY"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "halo bang desman misi bang.... abang ketang ini baik polll dan jokesnya lucuuu",  
                "pesan":"semangatt terus bang ketangg!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "kaaa sonyaa baik bangettttt siapa yang tidak tahuuu, kerenn banget juga",  
                "pesan":"semangaaaatt terus kak sonya, have a niceee day yuuups!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "haiii kakaa aku belum pernah ngobrol banyak samaa kakanyaa tapi baik dan ramahhh banget",  
                "pesan":"semangattt yaaaa kak kuliahnya, jangann lupa maam"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "abangnyaa baik bangett, vibesnya serius gitchui",  
                "pesan":"semangatt terusss yaaa bang!"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "WOOOOP SERU BANGET ABANGNYAAA random binggooooo",  
                "pesan":"semangatt bang mentorr!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "haiii kakaa seruuu bangett dehh, cantikk",  
                "pesan":"semangat kakaa kuliahnyaa, jaga kesehatan yaa kakaa"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "kakaa cantik, baik, ramah bangettt!",  
                "pesan":"semangat terus kakakk kuliahnya, have a nice day yah!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "KAKAAAA DUTAAA CANTIK BANGETTT DHEHHHHH, positive vibes banget deh poll, aura aura pengmasnya kenceng bangettt",  
                "pesan":"semangattt dutanyaaa kaa!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "haii kaaa, kakak mirip seseorang dehh tapi aku lupa siapaa, baik banget kakaa ramah poll",  
                "pesan":"semangat kuliahnyaa kaa, jangan lupa istirahat yaaa"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakaa lucuu bangett!",  
                "pesan":"semangat kaa, jangan lupa istirahat yaa kak haveee a nice dayy"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "haloo abang kecee parah",  
                "pesan":"semangaatt terus bangg!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "baik banget ramahhh",  
                "pesan":"kaaa mau ikut menjelajah lampung selatan pliss!"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_pyi2Xxkmb_85_L_rFcU_iLdSQCzJjap",
            "https://drive.google.com/uc?export=view&id=1teOcTV6yEtfih2gsOnz1TV82y64CEX9Y",
            "https://drive.google.com/uc?export=view&id=1ItXFxKGR_c5yHeVJx0xZJTdoYn6inXvz",
            "https://drive.google.com/uc?export=view&id=1JqI4h9lIJmAGwZP9bEGjDI22PncIunZ0",
            "https://drive.google.com/uc?export=view&id=1huu8rqMmXGC9-UWQdc_1vUyszwSw4ZiH",
            "https://drive.google.com/uc?export=view&id=13mbsm4KuDBOByYdHXJ8BM3Z3smGNlvUC",
            "https://drive.google.com/uc?export=view&id=1kkM23CrVWiEhzXnF3ZeTBXAZJ5V-6LSU",
            "https://drive.google.com/uc?export=view&id=12qUT5HLtAMZq_W_oG90QTTlyF19Bz5Iz",
            "https://drive.google.com/uc?export=view&id=1W2MmLkrBbikeM0h4bFa3gcYcBV_L5NuL",
            "https://drive.google.com/uc?export=view&id=1lEXNxRLrKS7eXH71zjn6XUrS5_opuqWq",
            "https://drive.google.com/uc?export=view&id=1EYgEWm3nMAovyCdGqWyA8EpVJp5FaP2a",
            "https://drive.google.com/uc?export=view&id=1w6P3iReOUPtAcXwT36zpKy5DqEKL0iqN",
            "https://drive.google.com/uc?export=view&id=1JAOpcacCcOjdqefv2lWhS7mUDGgNnHQD",
            "https://drive.google.com/uc?export=view&id=1ep5vjC9s1mY_WIh1zoW5LRzesdy23Xl-",
            "https://drive.google.com/uc?export=view&id=17B1WV4cTL9gghzUFxZl-T_r5wO9FuayI",
        
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
                "kesan": "sukaaa banget style kakanyaa, skenaa abiss deh kereen, baik banget jugaaa cancii",  
                "pesan":"semangatt kakaa kadepp!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "kakaa ganteng...dann lumayan pendieme yyaa",  
                "pesan":"semangat terus kaaakkk, maau ikut mancingg dongg"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@sal_fhn",
                "kesan": "baik bangett, kereen amay kaa hobinyaa memanah",  
                "pesan":"semangaat kaaa kuliahnya, jangan lupa istirahat yaa"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "wuisss bang rendi bagus banget suaranyaa, baik banget, ramaah",  
                "pesan":"semangat terus kuliahnyaa bang, lanjutkann juara solosongnyaa keren banget"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "kakaa moderator fg gaa siy kemarennn keren banget",  
                "pesan":"have a wonderfull day always kaa!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "wuis bang haikal ngerii abiss tapi ternyataa asikkk bangett dan baik poll",  
                "pesan":"hati hati bang balapannya...."# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "kakaa lucuu baik bangett",  
                "pesan":"semangat terus kuliahnya kakaa, jangan lupa istirahat kaa"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "takut banget kalo kakaknyaa lagi mode komdiss",  
                "pesan":"semangat terus kuliahnya kaa, i wish u a wonderfull dayayeay <3"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Siderejo, Sidomulyo, Lampung Selatan",
                "alamat": "sabahbalau",
                "hobbi": "nonton anime",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "lumayann pendiem ya abangnyaa",  
                "pesan":"semangat terus kuliahnya bang naufal, jangan lupa istirahat yaaa!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatriaaa",
                "kesan": "baik bangett abangnya pertama kalli kenal di perwakilan TPB untuk magenta",  
                "pesan":"semangat terus kuliahnya bangg!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "KAAAA HANAA SAYANG BANGETT positive vibesnyaa meledak sihhh, baik bangett yaampuuuuuuunnnnnn gabisa berkata kata lagi,ramaah, cantik, lucuuu, ASIK BANGEETTT",  
                "pesan":"tetap selalu positif kaaa, mau main gameee"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "kakaa cantikkk",  
                "pesan":"semangat terus kuliahnyaa kakak cantik!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "sumpah bang naufal baik bangettttt",  
                "pesan":"semangat terus kuliahnya bang, jangan lupa istirahat yaaa bang, sukses selaluuu!"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Musik",
                "sosmed": "@sarahwsti",
                "kesan": "kaka cantik lucuu",  
                "pesan":"semangat terus kuliahnya kakk!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "-",
                "umur": "19",
                "asal":"Natat",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "main rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "baikk bangeeet",  
                "pesan":"semangat terus kuliahnya kak, hati hati bawa motornyaa kaa!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ztzMONuECnYCKmjBYHsur4W8dKFCq8aF",
            "https://drive.google.com/uc?export=view&id=1x0seVvyp62FfTnxEQ8rRh9xIcLP55HjI",
            "https://drive.google.com/uc?export=view&id=1n3d3repoPl6twpOA4LwfVNOt0H7Wv42D",
            "https://drive.google.com/uc?export=view&id=1JfP4mHVovC61PYLy_oRpJJUPaJlO1qyi",
            "https://drive.google.com/uc?export=view&id=1nxtRvOBvveIxWNQ4qYvqms5Y6BLjfVeb",
            "https://drive.google.com/uc?export=view&id=1Pzzu9g_MrH4DQ4B5m27oZodM6MHEeXYO",
            "https://drive.google.com/uc?export=view&id=1WK5rT5lWfgwf3jkgo5lP2oqEiOFYt5YM",
            "https://drive.google.com/uc?export=view&id=1TqElRDAI_H-0BSiTXCbkfbfuMGB21GeP",
            "https://drive.google.com/uc?export=view&id=1zkRCS-z4y8u-vTTK2V0c3-XLT7NkecQI",
            "https://drive.google.com/uc?export=view&id=1ZrzhdStNHWsoS-GFbfJ0cljIFWcy-V3q",
            "https://drive.google.com/uc?export=view&id=1CR3msyMsyvhueRY0XM7Pi9RT-dyxBxt5",
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
                "kesan": "kereeen bangeeet abangnya, ramahnya rill ramahhhhh buanget, pinter, public speaking nya top bangettt, asikk sama seruuu ga usah ditanya lagi",  
                "pesan":"semangat terus bang berinovasinya, semangat joginya jugaa bang!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "kakaa kalem sekalii adem, baik poll",  
                "pesan":"semangat teruss kuliahnyaa kakaa cantik!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum, foto-foto pemandangan",
                "sosmed": "@den_iki__",
                "kesan": "denger denger abangya model yeahh, kerenn bangettt",  
                "pesan":"stay cool bang semangattt terusss bang"# 1
            },
             {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "sportyy abisss",  
                "pesan":"semangat terus kuliahnya kakak, semangat juga joggingnyaa"# 1
            },
             {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort fb",
                "sosmed": "@aphrhtp_",
                "kesan": "kakaa cantik, kalemm",  
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
                "kesan": "SERUUUUU DAN ASIK BANGET CIUS",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa istirahat yaaa!"# 1
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "kereen abanngnya baik jugaa",  
                "pesan":"semangat terus kuliahnya yaaa bang!!!"# 1
            },
             {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "kaaa deviii cantik banget lovelyyyy, baiknyaa superr",  
                "pesan":"semangat kaa devi kuliahnyaaa, jangan lupa mam yeahh<3"# 1
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg perwira 2",
                "hobbi": "Nonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "kakanyaa cantikk lucuu kalemm",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
             {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "baikk bangetttt deyyy",  
                "pesan":"semangat terus kuliahnyaa kak, have a nice day yaa"# 1
            },
             {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "seruuuu bannget, jago yaa jualannya hehehe",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10Fe41pMGpZzHhRI5qUV8EV5M7tEDrLIq",
            "https://drive.google.com/uc?export=view&id=1PvFWUUX1HeQ2U_MV35UCi2VbDuLhM_rk",
            "https://drive.google.com/uc?export=view&id=16wKFBjE9wwlwY1SLqBLQZ1DUMf8bOfsP",
            "https://drive.google.com/uc?export=view&id=1FctEDqaOdN0k_c9TUXL6SBU3kTUc1OxI",
            "https://drive.google.com/uc?export=view&id=1C1qp2Hf7Ynj4D2D4QzcGlYrv3vHqacDG",
            "https://drive.google.com/uc?export=view&id=1zWGVzZsbp0mHoY5J0oCoIikw_CF9xUD_",
            "https://drive.google.com/uc?export=view&id=1RbTC6S9N3kTzRhmlXhG6B3BQH77DY9yR",
            "https://drive.google.com/uc?export=view&id=1M8uUJiCHWKnI4CWWRmqBzhqPffkIwd88",
            "https://drive.google.com/uc?export=view&id=14_ilHbullMnV9_dvTPUZ9QxIzj5NMaDw",
            "https://drive.google.com/uc?export=view&id=10TD9XXnh2pwCKE4--XxMMvOzIvvCKzUf",
            "https://drive.google.com/uc?export=view&id=1fZeTcgk1evIuzxEaj3cjGeXXuqr8zl-L",
            "https://drive.google.com/uc?export=view&id=18n9x5R8txZX_eqxlxLcO83FU1QjaPun-",
            "https://drive.google.com/uc?export=view&id=1pAwWemGZVld2qrdhMZOeLfq51-kq85fY",
            "https://drive.google.com/uc?export=view&id=1oChmgRKJXD7j7bZQCJj56G3wzxbjxIS4",
            "https://drive.google.com/uc?export=view&id=1xBOAYByDmk9N6-QYV8it4FpGsyRqMPtT",
            "https://drive.google.com/uc?export=view&id=1VKFEG3KIyhroEgKEAEv66LqcR1_5vJmg",
            "https://drive.google.com/uc?export=view&id=1ckqkJ5i_LoHiRCSGn_wF5C5lcdO2AVU6",
            "https://drive.google.com/uc?export=view&id=1jQ6CxxRdIz1nfWuidCK9N2buZcNF8jrK",

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
                "kesan": "HISS CANTIK BANGET??!? full of energyy, positive vibes nyaa meledak ledak, lucuuuuuuu, heran banaget energinyaa gaa abis abiss",  
                "pesan":"semangat yaaa kakaa kuliahnyaa, jangan lupaa istirahatt<3"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jl. Kresna Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "lucuuu kakanyaa cewe bangettt!",  
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
                "kesan": "humblee banget kadiv satuu ini well",  
                "pesan":"semangat dan sukses selalu bang bang!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik & fotografi",
                "sosmed": "@noerruu",
                "kesan": "bang labo lucu banget serius kalo beliau ngomong pasti ketawa banget KETAWA BESSAR, bucinnn banget, baik baik baik, pdd abadii supeer kalcer",  
                "pesan":"jangann pensiun duluu plis menjadi pdd abadi"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan":" BAIK BANGETTTTT, selama science baik poll pokoknyaa, ramah bangett",  
                "pesan":"tolong bimbingannya bapak kadivv dan semangat terus kuliahnyaa bang, jangan lupaa makan dan istirahat yaaa!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "seruuu amay kakaa",  
                "pesan":"semangat terus kuliahnya kakak, dont skip ur meal yeaaah"# 1
            },
            {   
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kaa cia kakak kelas duluu SMA, emang cantik bangett dari duluu, baik banget, kadiv konten terkerenn",  
                "pesan":"semangat terus jadi kadivnyaa kaaaaa!"
            },
            {
                "nama": "Aliya Anmara Amanta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammra",
                "kesan": "kakanyaaa aqila lampung, baik bangeett cantikk, chill bangett",  
                "pesan":"semangat terus kaaa kuliahnya, ayoo thrift bareng hehe"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@donnamaya.p",
                "kesan": "kaa dona seruu banget ramahhhh, positive vibesss banget",  
                "pesan":"semangat terus kuliahnyaa kaa, maau main gameee lagii!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "haii kakak cantikk, lucuu banget ini kita pose sahroni",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupaaa mam yaahh"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kakaa cantik keliatannya kalemm bangett",  
                "pesan":"semangatt terus yaaa kak!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumateraa Barat",
                "alamat": "Jl. Lapas, Kecamatan Jati Agung",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa_",
                "kesan": "kakaa gemeyy dan keyenn",  
                "pesan":"semangaat dan sukses terus kak semoga tercapai segala cita-citanya!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "kaka nya tudep yaah orangnyaa, cantikk dan ramah bangett, baik sekalii",  
                "pesan":"kakaaa spill the tea dongg"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "oww ini dibalaik design design keren HMSD Adyatama, kereen banget bang",  
                "pesan":"semangat bang design dan semangat menjalani harinyaa!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "banyak amaay kaka hobinyaa, cantikk, ramah, baaik",  
                "pesan":"semangat terus kuliahnya kaka!"# 1
            },
                        {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "kereeeen amay kaa, seruuuu!",  
                "pesan":"semangat terus nge-designnya kak!rr"# 1
            },
                        {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "duluu ketemu saat perwakilaan kelas TPB KAKAKNYAAA BAIK BANGETTT, bikin ga canggung, cantikkk",  
                "pesan":"semangat terus kuliah dan sukses terus yaaa kak!"# 1
            },
                        {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "hayiii kakaa kadiv di pemira, lovelyy bangett, sepertinya introvert yeaahh, cantik dannn lucu!",  
                "pesan":"SUKSES TERUS KAKAA SEMANGATTT SEMANGATTT!"# 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
       

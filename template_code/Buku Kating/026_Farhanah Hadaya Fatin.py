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
            "https://drive.google.com/uc?export=view&id=1K4mSdHc4tX-LfzCi_VjEjLn8gPU5NWqZ",
            "https://drive.google.com/uc?export=view&id=16r-SOlUxy7CdGV_hZFDwOjSJKt9WptHl",
            "https://drive.google.com/uc?export=view&id=1cMXTJeTu2Su-YhC55cjBHnIq1a9lQvbj",
            "https://drive.google.com/uc?export=view&id=1zM8XKZTsaNGnriPalP77iQB-3fkermjC",
            "https://drive.google.com/uc?export=view&id=1uxNjwg5UCj8mcxKB9x7cMFP0d5qkITws",
            "https://drive.google.com/uc?export=view&id=1Dn46qEjDc-8Hx4m3FEyf7_3_E3ogBs_6",
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
                "kesan": "Asik banget abang ini, sngat chill",  
                "pesan":"Selalu gini terus ya bang, semangat ngerjain TA-nya!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Asli keren beut bang, kalcer abisss",  
                "pesan":"semangat kuliahnya banggg!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Ayres kost",
                "hobbi": "Jajan",
                "sosmed": "@celisabethh_",
                "kesan": "Senyumnya cakep, ceria banget juga kakaknya",  
                "pesan":"Sering-sering ya kak senyumnyaa, candu"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Adem banget kakk, berasa lagi di tempat rindang kalau liat kakak",  
                "pesan":"Semangat jalanin hari-harinya kak!"# 1
            },
            {
                "nama": "Eksanty F Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Kelagian Kecil, Pahawang",
                "alamat": "Pesawaran",
                "hobbi": "Ngambilin Lanyard",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak jahill, tapi seru aselik",  
                "pesan":"Iseng terus ya kak, udah jadi ciri khas kakak soalnya hehe"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Gya kost",
                "hobbi": "Cute",
                "sosmed": "@farahanumafifahh",
                "kesan": "Gak teerlalu banyak ngomong, tapi sekali ngomong langsung berasa asiknyaa",  
                "pesan": "Senyum nya manis kak, senyum terus dong"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xNwZmBkhCnFU5R0WMXGpPCpvYpE_yneV",
            "https://drive.google.com/uc?export=view&id=1OdDmIYJ4i5eydoZIJ0n2QVj3PmouGfVR",
            "https://drive.google.com/uc?export=view&id=1gW3_qmv0-qh3zkELqB8-sXOgLlYe40CP",
            "https://drive.google.com/uc?export=view&id=1kkYYlZAoO9fJEPrhwEYbE-PP8fD7DFL2",
            "https://drive.google.com/uc?export=view&id=1uK88UypHuNJoR8SbMobkgKp90Fugs3Wc",
            "https://drive.google.com/uc?export=view&id=14Fx04rqVE2cGAqPlyo3lFArTorTmDpR-",
            "https://drive.google.com/uc?export=view&id=1C24LJoHpRNcrrPiadSPuJV_WxTaBS2j4",
            "https://drive.google.com/uc?export=view&id=1jbrEPFPuNo-mURKrse2UHcw7VoIUbhSP",
            "https://drive.google.com/uc?export=view&id=1ms_0A9W8Dtd-qVmp119YmohwK6wbZ04Z",
            "https://drive.google.com/uc?export=view&id=1D7EgftHhQoBkFZ4-ZwUihiMxDRh3QnPt",
            "https://drive.google.com/uc?export=view&id=1g3XkbczqF7fdi3VxoW8f5syOdzfLvNBK",
            "https://drive.google.com/uc?export=view&id=1uNp_8WFL7HqW1km0WBeLIMwJNNzjZ6Af",
            "https://drive.google.com/uc?export=view&id=1wv1lwCj2nphY__bsSlzVshByEYEKEmg4",
            "https://drive.google.com/uc?export=view&id=1V6VuCCz8YkTWaoN_whl0n9PIS6i7QhtL",
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
                "kesan": "Seru banget abangnya aslik, keren juga lagi",  
                "pesan":"Selalu jadi keren ya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "kalo badmood liat zaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Ramah banget kakaknya, mukanya juga manisss",  
                "pesan": "Jaldinya jangan dikantongin ya kak kalau lagi badmood =D"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin Alat Pancing",
                "sosmed": "@renishapg",
                "kesan": "Cakep banget kakak ini, lucuk",  
                "pesan":"ayok mancing kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Wakatobi",
                "hobbi": "Bowling",
                "sosmed": "@ansftynn",
                "kesan": "Easy going bgt kakak ini, seru diajak ngobrol",  
                "pesan":"Sehat terus kak, nanti kita main"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "asik banget ngobrol sama abang, waktu jadi gk kerasa",  
                "pesan":"Liatin yang lain bang langitnya bosen diliatin"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Wai huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "Kalem banget.. mana mirip sama dipa kakak ini",  
                "pesan":"Mending mancing ikan sama saya aja kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "Loh kok... bang kapan jualan lagi bang",  
                "pesan":"hayoyo, semangat yang bang lulus bntar lagi"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain Makanan Baru",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini keren bgt, auranya dapet banget",  
                "pesan":"Semangat ngerjain TA-nya bang!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "20",
                "asal":"Teluk Mondawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya baik, ramah, enak diajak ngobrol juga",  
                "pesan":"Sehat-sehat kak, jangan lupa istirahat"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "ngumpulin batu unik dipantai",
                "sosmed": "@berlyyanda",
                "kesan": "Asik kakak ini ngobrolnya, kalau cerita seru banget",  
                "pesan":"Selalu jadi keren ya kakk"# 1
             },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang ini gacor banget anjai, pengen kek dia",  
                "pesan": "Tetep jadi gacor ya bang"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak baik banget asli, seru jg kita ngobrol",  
                "pesan":"Ayok kita ngobrol lagi kak"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML hero semua franco",
                "sosmed": "@Monica_tjg",
                "kesan": "Jago bener kakak ini, jadi fans berat",  
                "pesan":"Main ml jangan sampe lupa makan kak"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin ka wawa ngomong",
                "sosmed": "@fer_yulius",
                "kesan": "Adem banget muka abang ini, berasa banget pendengar yang baik",  
                "pesan":"Selalu jadi pendengarnya kak wawa ya bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oiDbg2l72-dwnL2RxhwndUVEnlh_RXiZ",
            "https://drive.google.com/uc?export=view&id=1sDjCeY-1RpjsnV2AB5EJhH8nt82kgQuD",
            "https://drive.google.com/uc?export=view&id=1jvZe1jUWQwkgtuL0aRBaEnhifXxT55AW",
            "https://drive.google.com/uc?export=view&id=1C6H3Gj2IuVkE7I2ah_6fqQPO6duq6vz0",
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
                "kesan": "Asik banget abang ini, keren juga  lagi jadi senat",  
                "pesan": "Tetep mancing walau sibuk jadi senat"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjanani",
                "kesan": "Kak nadya ramah banget, asik juga diajak ngobrol nyambung banget",  
                "pesan":"Sehat selalu kak, terus kayak gini yaaa!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Denger musik sambil jalan",
                "sosmed": "@fathinahazzh",
                "kesan": "Kak zizah ramah bangetttt, senyumnya manisss",  
                "pesan":"Hati hati kak waktu ngedengerin musik sambil jalannyaaa"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main",
                "sosmed": "@lia.h_264",
                "kesan": "Kak lia asik banget aselik",  
                "pesan":"Jaga kesehatan kak jangan sampe tumbang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1whSOCnnS6mHpFvghRIQ08mbIpDgmMjZX",
            "https://drive.google.com/uc?export=view&id=1Ie3FolUOHaYMzJkmUKHyqsD8_BhxzHln",
            "https://drive.google.com/uc?export=view&id=1E4vbVfyfC6mywYm_ZEZOpAFAKbB1GLyt",
            "https://drive.google.com/uc?export=view&id=1J03zTy7QQHYi14MNPCLCmBmySMHFtV7_",
            "https://drive.google.com/uc?export=view&id=1s2EvKhESkCz8hMZNl255fl_z66hTszhT",
            "https://drive.google.com/uc?export=view&id=1kS0a-J81DpfqxN6kMGdEwjLpadqtqd6P",
            "https://drive.google.com/uc?export=view&id=1Mh9m7K0TrTZPg0odyOok8hZ_YlUMSudE",
            "https://drive.google.com/uc?export=view&id=1hFE90trP15rfDeyf6RkbEmyBsX-qTRpo",
            "https://drive.google.com/uc?export=view&id=1t6V4btJou0W-HAbhGNQTF_-kHWnG7FQK",
            "https://drive.google.com/uc?export=view&id=1_wcBcbW1T7ANIaBCcFRWOpdhXRhFgwlf",
            "https://drive.google.com/uc?export=view&id=1e-MPBTcxgE5ds3KBczLY6-4thr6aY01K",
            "https://drive.google.com/uc?export=view&id=1Xa-0QU6gs2D4vopX9hNGWHhizI2RWL-T",
            "https://drive.google.com/uc?export=view&id=112Co3crq8KGJC5wqJGIkfcS5VGAfmAFP",
            "https://drive.google.com/uc?export=view&id=18o1rJDOMTux5KUxo_H7o5AJU_0TrOGCJ",
            "https://drive.google.com/uc?export=view&id=1DjyL_LVjB7ib-y670gydGgMNq5gY1iBL",
            "https://drive.google.com/uc?export=view&id=1rRSX1Hw9DCQnGU_Iv22NNDSHtmnUqmd_",
            "https://drive.google.com/uc?export=view&id=14794rj1PCN70T48VAyLcC0MZOnZesEpZ",
            "https://drive.google.com/uc?export=view&id=1eqj5ZT1GtDFjPB6GCQdSKgrOoIUYhQSR",
            "https://drive.google.com/uc?export=view&id=1kF6P5oPnplr_O8kxQwt5uJtFAgBPxigy",
            "https://drive.google.com/uc?export=view&id=1wrkvILIj4sRj8Ol8npOvYgHhFzkV9qZZ",
            "https://drive.google.com/uc?export=view&id=16YlW__r_trCbn0lhDoVx2mdj9aGf7OzX",
            "https://drive.google.com/uc?export=view&id=1CnaxtRTZ7d8HPDfNu9lPiqlN3ow9SCw7",
            "https://drive.google.com/uc?export=view&id=1mxUxSL5CyvJ6rV3eLCuqBlKC46AhZsai",
            "https://drive.google.com/uc?export=view&id=1xUXBKSJt78iCidTPAn_slP6mLdN9V9OW",
            "https://drive.google.com/uc?export=view&id=1UFeY0yTJbNERAYVDs5lx62zgpDWmfZza",
            "https://drive.google.com/uc?export=view&id=1O1kgMVYTL-Iu53LIcSjZMgsOPSLxgt7c",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini keren banget dakh",  
                "pesan":"Sehat sehat bang... semangat TA-nyaa"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Imup banget kakak sekdep inii",  
                "pesan":"Semangat kak mnjadi sekrenyh"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main apapun",
                "sosmed": "@allyapasha_",
                "kesan": "Ebuset baik banget kakak ini cakep jugaaak",  
                "pesan":"Istirahat yang cukup kak, jaga kesehatan yaaa"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "kontrakan GH",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky",
                "kesan": "Abang ini gacor bgt asli, jadi termotivasi",  
                "pesan":"Semangat terus bangg, jangan lupa main bola kalau capeek"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Samping kost daffa",
                "hobbi": "Main Sudoku",
                "sosmed": "@arientakhsnl",
                "kesan": "Asik banget kakak ini, keyennnn",  
                "pesan":"Jangan lupa sudiku kak kalau senggang"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jailin putri",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang ini kece bgtt, badass jugaak",  
                "pesan":"Sehat sehat bang, jangan kecapean"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_nrp",
                "kesan": "Abang ini baik banget busenggg",
                "pesan": "Terus kembangin hobinya baangg"  # 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"pasar muara beliti",
                "alamat": "kost putri, gerbang barat samping sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Cakeeepp, senyumnya manisss",  
                "pesan":"Belajarnya jangan sampe lupa waktu sama kesehatan ya kakk"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Urip",
                "alamat": "Belwis",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Jago banget abang ini ngodingnya busyet",  
                "pesan":"Selalu siapin rekomen laptop tiap taun ya bangg!"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma fam",
                "hobbi": "ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "Abangnya saya blm pantun aja udh cakep #eyaq",  
                "pesan": "Semangat terus bang, jangan lupa jaga kesehatan!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "maju jaya kost",
                "hobbi": "yapping sampe bete",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak ratu spiderman asik beutttt",  
                "pesan":"Jaga kesehatan kakkk, biar bisa yap yap teruszzz"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Lari",
                "sosmed": "@sahid22_",
                "kesan": "Kece abis bang aselik",  
                "pesan":"lari boleh bang, tp jangan lari dari TA ya bangg"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "nangka 4, sukarame",
                "hobbi": "Main game + kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "Kalem banget abang inii, pendiem kayanya",  
                "pesan":"Semangat bang biar sukses acaranya~~"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Nie gokiel nie, asik beut... ketawa terus kak xixix",  
                "pesan":"Jangan tidur sembarangan kak, nnti kena paparazieh"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Baikk kakaknya, asik jugaaaaak",  
                "pesan":"Semangat kak kuliahnyaa! jangan lupa sekrol tiktok"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Santai kakaknya, asikkk",  
                "pesan":"Walau sibuk, roblox jgan dilupakan yh kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul9",
                "kesan": "Kalem banget banggg",  
                "pesan":"Istirahat jangan lupa bang"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Gokieeell abang ini keren beut asliik",  
                "pesan":"Ayok olahraga bang, capek baru rebagan lagi"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.lapas raya no 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "Keren banget kakak ini, dancenya cakeupp bangett",  
                "pesan":"Jangan lupa istirahat kakk"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Bikin project, ngoleksi data",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Asik bang, pokoknya asik, asik banget lah asik",  
                "pesan": "Stop guyon bang..."# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Padang Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "Mimik wajahnya jutekkk, tp senyum ababg manisss",
                "pesan": "Kalau senggang jangan lupa masak bangg"  # 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Pembawaan kakaknya asik, santai jugaaak",  
                "pesan":"Jangan lupa bahagia kakk!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Lempar Batu",
                "sosmed": "@m.ridwan_22",
                "kesan": "Asik, santai, seru dehh",  
                "pesan":"Semangat terus bang! jangan lupa bahagia"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Abang ini senyum mulu, pamer senyumnya cakep apa ya",  
                "pesan":"Ayo main bola bang, tp gak sama saya hehdhe"# 1
            },
            {
                "nama": "Uliano Wiliam Purba ",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main musik, ngoding, menanam anggrek",
                "sosmed": "@nano.wlm",
                "kesan": "Serius, tapi santai juga okee",  
                "pesan":"Sabar, sehat selalu ya bangg!"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Bengong",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakaknya asik, seru jugaaa",  
                "pesan":"Jangan seting sering bengong ya kakkk"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XOlxkCYuO5mGi7QfLmbTwqe4sobZCbvj",
            "https://drive.google.com/uc?export=view&id=11_RDO01Qyf-MHGstITYnWs4k9eazq-tG",
            "https://drive.google.com/uc?export=view&id=1DAhGjzQUajKKpyiD9g-F0eDP_XjeoHN4",
            "https://drive.google.com/uc?export=view&id=1qwQDerl9YeVwZznqF1WQsJqQKVkaVDaR",
            "https://drive.google.com/uc?export=view&id=1rD3aNBWQsTU-47OU4UoaqCgWiJVrG3y7",
            "https://drive.google.com/uc?export=view&id=12Bk-b3G5S98kcQ6ljs9fdfhxcZviu2x4",
            "https://drive.google.com/uc?export=view&id=1r934m6F0pl6OgpNm65rI9X4DZrKpuT9P",
            "https://drive.google.com/uc?export=view&id=17HstD95Z45B16VlGf5_chUVbR737A0LD",
            "https://drive.google.com/uc?export=view&id=1ieLml9LtsA4_M13DFKbLh_QLYozvvbY7",
            "https://drive.google.com/uc?export=view&id=1Sh1wi819UNTrZVXCAgCCm99RLdZV5_Ng",
            "https://drive.google.com/uc?export=view&id=1BRxGSJ0WGE8Wx0sa07UOrNrq-eeuy_-Z",
            "https://drive.google.com/uc?export=view&id=1CX_u80R8yXYuQ--yfzpM8-CLj5yyEEdk",
            "https://drive.google.com/uc?export=view&id=1TaHKmF1TOrDpKcygJ2RsXvYQWXSuJyCZ",
            "https://drive.google.com/uc?export=view&id=1qYy8M0l7PCwnTKStbfhsQ-fGiCeIBE8-",
            "https://drive.google.com/uc?export=view&id=15W5jrOXTVu6OPDAaGhNSkuq4r6oXLVmw",
            "https://drive.google.com/uc?export=view&id=139CY1rASyCWJRHiX2w3S4DQJpqTVwTMW",
            "https://drive.google.com/uc?export=view&id=1TNJyPDdsck39kBxOW13gs0Ws8KVKdKmK",
            "https://drive.google.com/uc?export=view&id=1z6S3LxrjwtuXBz7XAs9VGgdzuXeUoRT0",
            "https://drive.google.com/uc?export=view&id=1tfw8vPH3ijUdfGNETdpO8HTC_BH_9Mxn",
            "https://drive.google.com/uc?export=view&id=1Hn9760Mglok-xeNJ3ZapsSqGkVv6lIqi",
            "https://drive.google.com/uc?export=view&id=1PdyoSzMmJPudJxytMqRXEQinr34sn7Gz",
            "https://drive.google.com/uc?export=view&id=1sUGhgPqxVOLRZ3g815heFz2iZkYO1jz-",
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
                "kesan": "Easy going abangnya, enak juga diajak diskusinyaa",
                "pesan":"Semangat bang, jangan lupa istirahaattt"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@junitaa.0406",
                "kesan": "Seru kakaknya, enak bangett ngobrolnyaaa",  
                "pesan":"Sehat terus kakk, jangan lupa istirahat"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abang ini keren banget edannn, seru juga lagiiik",  
                "pesan":"Semangat nyusun TA-nya bangg"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakanya baik, asik banget diajak ngobrol",
                "pesan":"Ayo kita maskeran bareng kakkk!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Abangnya seru banget, keren, easy going mampus",
                "pesan":"Jangan lupa nge-matcha bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Gokiel asik abis bang, mantep pokonya ",
                "pesan":"Semangat basketnya bang, biar masuk NBA" 
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
                "pesan":"Semangat terus bang, healingnya jgn lupa"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "jl. Manggis 1",
                "hobbi": "Nonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakanya baik, kalem juga",  
                "pesan":"Semoga harinya selalu menyenangkan ya kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak manis bangett, Asik lagi diajak ngobrolnya",
                "pesan":"Ayok kita latihan musik kakk"
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
                "pesan":" keren teruz bang"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakanya baik banget, seru juga",
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
                "kesan": "Seru bangettt kakk, asik juga parah",
                "pesan":"Jangan lupa jalan jalan kak ditengah hiruk pikuk inu"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@pebby_olla525",
                "kesan": "Kalem banget keliatannya kakakk",  
                "pesan":"Semangat terus ya kak"
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
                "kesan": "Kakak seru banget dan berisik tapi nyenengin deh pokoknya",
                "pesan":"Semoga apa yang disemogakan tersemogakan ya kak!"
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
                "pesan":"Semangat ngodingnya bang!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi",
                "pesan":"Semangat terus kuliahnya Kak!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Aura codingnya gk jauh beda ini sama bang eggi",
                "pesan":"Semangat bang kuliahnya! jangan ngoding teruszz"
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
                "pesan":"Jaga kesehatan ya bang"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Seru, asik banget juga kakaknyaa",
                "pesan":"Semangat terus kuliahnya Kak!"
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
                "pesan":"Sqemangat terus kuliahnya kak, jangan bosen liat embung ya kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Baik, seru banget diajak ngobrol abangnyaa",
                "pesan":"Tetep futsalan bang walau sibuq"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()
       

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14j3Hz4B1hjwEsF9c4dQJdXVNnWqo65um",
            "https://drive.google.com/uc?export=view&id=1X_oCLST9_JkDxVTCbNAW-j-RXwCHMaIE",
            "https://drive.google.com/uc?export=view&id=1M36pn-5mHzyOMigQJaEoZddkrDoZotDZ",
            "https://drive.google.com/uc?export=view&id=1sEjwqNne-vLU3Qc_BZb38xEm4c_jCtlq",
            "https://drive.google.com/uc?export=view&id=1AMfCCpx-6BwNS7KEGQBD0Id7psCoqzTk",
            "https://drive.google.com/uc?export=view&id=1lRciryTben7oPWi0RwwVFUHrn9HBBgEz",
            "https://drive.google.com/uc?export=view&id=1kjkTSjJ2nDiQlXcgtV4wXok7Zzmzncvw",
            "https://drive.google.com/uc?export=view&id=1hmgAAv-81uj57Yu8fzUzpqsEg71PpEU2",
            "https://drive.google.com/uc?export=view&id=1GbQUWb6miiBj8kTWc5A7vnMsTTr99JdA",
            "https://drive.google.com/uc?export=view&id=1CsGWNjCN4tFjyHTSuiAX7mpvBfKLWZfO",
            "https://drive.google.com/uc?export=view&id=154YRJ4WzgXiEwAVv_9CFSPCZB_GHp3V5",
            "https://drive.google.com/uc?export=view&id=1hLcHeyfWEjxX7oJC58ueSSBhSd4udZtZ",
            "https://drive.google.com/uc?export=view&id=1s4e14Y9r617h_i4sqRWHUwOMMYUKJa_Q",
            "https://drive.google.com/uc?export=view&id=1oVyl3buBBJd8XTHF8Bz9G8xCJl8zJwL-",
            "https://drive.google.com/uc?export=view&id=1Ega5v6JHC0Pga8vSBm4q2__tiHaApVqg",
            "https://drive.google.com/uc?export=view&id=1AHLxCD__eXNjB3fQbIFaoncjXGFDYiYl",
            "https://drive.google.com/uc?export=view&id=1P03WBfJVBDfAZ4nfuyxcEexD6tNip0mK",
            "https://drive.google.com/uc?export=view&id=1ebBP124Wh08KkD9TuwXS4FzstyYv4BaP",
            "https://drive.google.com/uc?export=view&id=1NCWu7l7CsjDYbEib8jL4wTjAyc1jmWWI",
            "https://drive.google.com/uc?export=view&id=13ut6iqEb9dN9bbwBV7dZ_zgtZHIAqCf9",
            "https://drive.google.com/uc?export=view&id=1QMX31h-WqQvIsc5bQsY_5MBeAOEm4Dz2",
            "https://drive.google.com/uc?export=view&id=1hKrsb5v0zH3MCJww2f1FvLVL-WDLJxEm",
            "https://drive.google.com/uc?export=view&id=1612vj1gLx2s_ttnGAm40Fe6KfqWqoRPs",
            "https://drive.google.com/uc?export=view&id=1B7QjHZnAXt9oVM2pRLBqqRCGnBJTig5O",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Tarisya Hadayatul Rahmi",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1g3Gz6UNpJuzMe3-WJYUAkvD4SbkdGy5f",
            "https://drive.google.com/uc?export=view&id=1BSjHBjowvfnahTgBW5bvShecR4ZGDx8j",
            "https://drive.google.com/uc?export=view&id=1pd1w0VH3mUbq0lEU3X-02C2IvjAx7203",
            "https://drive.google.com/uc?export=view&id=1GAiEFjikZ19qyOMTfnLeZvnrOkdwjjn3",
            "https://drive.google.com/uc?export=view&id=1ftwY2hiDi_m1XaJks1qtD4TQXN9E250r",
            "https://drive.google.com/uc?export=view&id=1mfrhBC9yeDfVt_g7fKEngvE0SDf-Zeqb",
            "https://drive.google.com/uc?export=view&id=1jJx2TxyylY8T-uvt_BtPe5bILP8ESFlv",
            "https://drive.google.com/uc?export=view&id=1h4Dc7fxxe-UJKg4pG50lEbSKCzsbxIW5",
            "https://drive.google.com/uc?export=view&id=1I-oQIQCl1GS2orZs4fy5PM9SqcIUXIjo",
            "https://drive.google.com/uc?export=view&id=1g9qPtfDgxXovCJwZDr2RAqBuzQtB_WrV",
            "https://drive.google.com/uc?export=view&id=1qidHoHkpt9lvixvBw0-JbqBt4k6LhxOv",
            "https://drive.google.com/uc?export=view&id=1GfSTk0a-gVS8QuJY1gcXP6NxQIHDsVR1",
            "https://drive.google.com/uc?export=view&id=1pd1w0VH3mUbq0lEU3X-02C2IvjAx7203",
            "https://drive.google.com/uc?export=view&id=12cHiJZdByod3DLHPCxAEl7jonBjSRl6Y",
            "https://drive.google.com/uc?export=view&id=1yO0Gz_bi92HuAR3Bhale-BvQ-igY7mgG",
            
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wmQdwgcItQ8Fe5rJdZ0Ild77WXLFYAFo",
            "https://drive.google.com/uc?export=view&id=1yDUgCGWM7lk4SJ4pnfkDh58hh90PWFUe",
            "https://drive.google.com/uc?export=view&id=11boE3m9NR_Y8XGIcTzPtuNEJS9jt4OSy",
            "https://drive.google.com/uc?export=view&id=1k-eP2aNiaSlSK9U0f5Ooweaeu48jXumM",
            "https://drive.google.com/uc?export=view&id=1qt7tWxyLdJNQJmkU9gCcZdFOCqkaG5_C",
            "https://drive.google.com/uc?export=view&id=1k2n5vJC13_Q4mEZxwGQ52b2dNck-KiAy",
            "https://drive.google.com/uc?export=view&id=1iYH4NbEhPsrSu_Nn5PxKS4jnwuCBFOHW",
            "https://drive.google.com/uc?export=view&id=11RlqRS7WO_GYUjIUlgTdnJzSM56Vtm8r",
            "https://drive.google.com/uc?export=view&id=1Osnb8KMzrdYFSnrEBAn_K2LZgksgw1Yf",
            "https://drive.google.com/uc?export=view&id=1wRxPX50Ijc_280zUDZmL7H3qwYjKEKr3",
            "https://drive.google.com/uc?export=view&id=1TQU_aKkGIgr8IDKDscbhpEAKwzVu-JMu",
            
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 3",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 4",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 5",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 6",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 7",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Kakak 8",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 9",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 10",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 11",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak cantik banget !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RZcvQr51wJkn1r0Y4PqdTWXb5ZuDjw-g",
            "https://drive.google.com/uc?export=view&id=1yZ-7iYu0OIXV9jzeAHznzffpRdMclV79",
            "https://drive.google.com/uc?export=view&id=14DbKY2Bh2m2D5HB9kGUn5-5rAgn1xMXL",
            "https://drive.google.com/uc?export=view&id=1fwUvJY0SRFJsrrG6h6cbiFUxpgTfMALg",
            "https://drive.google.com/uc?export=view&id=1mwQb3Ez_rdC8JQ0J1dvrAL43BOHG0JKD",
            "https://drive.google.com/uc?export=view&id=1NF8rfwfi074IWilOanZ0mHBHOgi3q2c1",
            "https://drive.google.com/uc?export=view&id=1k9okvp7STwBQT_GvtQo7wC_xtZAMrdrF",
            "https://drive.google.com/uc?export=view&id=1S1rzLhYNv8y_E6xzzfxOqIR-haaa71PR",
            "https://drive.google.com/uc?export=view&id=1xNVpCva2_15cxSZgBdADGlxrW6K5tVo5",
            "https://drive.google.com/uc?export=view&id=1RgGF1Lp70jbYYcZh-KufbX5mF5ScrZoP",
            "https://drive.google.com/uc?export=view&id=1qiajIe_zQjMsdc3yLYuHV_2bvRRAE_6V",
            "https://drive.google.com/uc?export=view&id=1A8wERdlR2eMjkSPJu8k6AXUATo7LLDOt",
            "https://drive.google.com/uc?export=view&id=1-FIZvQ5ktn0gnjJsBQxHafTH3lZdCrra",
            "https://drive.google.com/uc?export=view&id=1z3gXp8apVRNlaLTk91yuCmc-kg55iFQz",
            "https://drive.google.com/uc?export=view&id=1RCVEsOixJqkb8Npz0Z3bM9WWh-mLb3Pt",
            "https://drive.google.com/uc?export=view&id=11WPBLONFwp0wh2QLam2ryU07PQ2yzHMN",
            "https://drive.google.com/uc?export=view&id=1_xU-odRLqCRNnKqUZww_Gx08t-TwWlMi",
            "https://drive.google.com/uc?export=view&id=1XRAxKtpvdtZ9nWYtjyJNp6JkrR1pqHoY",
        ]
        data_list = [
            {
                "nama": "Kakak 1",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 2",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 3",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 4",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 5",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 6",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 7",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Kakak 8",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 9",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 10",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 11",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 12",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 13",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 14",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 15",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 16",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 17",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak 18",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
# Tambahkan menu lainnya sesuai kebutuhan

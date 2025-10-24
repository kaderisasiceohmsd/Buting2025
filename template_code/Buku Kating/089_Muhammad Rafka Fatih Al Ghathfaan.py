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
            "https://drive.google.com/uc?export=view&id=1XYDd1Rr86kjtgHgPNIpLcCbC3SZOoAz5",
            "https://drive.google.com/uc?export=view&id=1CPslOldmQc7GjJAv5h8RPqYoYlWJHFfM",
            "https://drive.google.com/uc?export=view&id=1AmyGNpbTLa29cRfu9tvXwiTZJNzptNdT",
            "https://drive.google.com/uc?export=view&id=1xOPWsPpQWKodPH69mGGO1Q7FdC9MptiA",
            "https://drive.google.com/uc?export=view&id=1Tq-qxTqy65Mds0hsooD6rYrWSDAzhU9c",
            "https://drive.google.com/uc?export=view&id=17NoXPhjfKhQEXj_a4c5EOT6oE5lwpVJG",
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
                "kesan": "Abangnya keren,berwibawa,kecee abiis",  
                "pesan":"Semoga burung murainya juara bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya seriuus tapi juga menyenangkan",  
                "pesan":"Tutor SQL bang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Ayres kost",
                "hobbi": "Jajan",
                "sosmed": "@celisabethh_",
                "kesan": "Kakanya lucu,asyik,dan menyenangkan",  
                "pesan":"Always happy kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakanya lucuu dan kalem",  
                "pesan":"Semangat terus yaa kakak"
            },
            {
                "nama": "Eksanty F Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Kelagian Kecil, Pahawang",
                "alamat": "Pesawaran",
                "hobbi": "Ngambilin Lanyard",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakanya asikk dan chill",  
                "pesan":"Jangan sering sering ngambilin lanyard yaa kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Gya kost",
                "hobbi": "Cute",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakaknya baik,lucu,dan menyenangkan",  
                "pesan":"jangan sering sering cute yaa kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WgorwbrSRZ8R99yuCLYJcU0GwvdGwiew",
            "https://drive.google.com/uc?export=view&id=1Y2zwTaYCrjMVXJ1xTut1-qbAk8vGn8to",
            "https://drive.google.com/uc?export=view&id=1_k8DwfIdQYxyd9Goqb9aUiZvHYahbjd9",
            "https://drive.google.com/uc?export=view&id=13bL97eZ5vZokVk_JlgLGk8gaD7ybFeJI",
            "https://drive.google.com/uc?export=view&id=1iyiaV1kKU3baIDlzEnHiHBtFf2D8lLxZ",
            "https://drive.google.com/uc?export=view&id=1uvnSXQTvDCJUVJx9D_6QVn0AWo-TgsUM",
            "https://drive.google.com/uc?export=view&id=150MT0UZCFhULCWoSGkVHoF4GRO7Q7_px",
            "https://drive.google.com/uc?export=view&id=1rGgzGuua2-IAmZS7Eu-pP6TZ985msFMu",
            "https://drive.google.com/uc?export=view&id=1VMbG0th2kbg8OtNtL0DSrXMunaMmtBYp",
            "https://drive.google.com/uc?export=view&id=1R2ybzuJKgxb1JUT2Ext8pAoERUWhjNxs",
            "https://drive.google.com/uc?export=view&id=1yGwWhWp5l9ARA84TtCG0pNDkKsfXji12",
            "https://drive.google.com/uc?export=view&id=1LI8yc6x36B6mbpd4ZAX88sl9LmOWQiaY",
            "https://drive.google.com/uc?export=view&id=1CbvRJcVbhSDJGAdWr2JtsRI_3jc7sqgA",
            "https://drive.google.com/uc?export=view&id=1VJSYYLLXdvTr05J5H3KAGrX02hZkvy6K",
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
                "kesan": "Abangnya tegas tapi perhatian",  
                "pesan":"Terus jadi contoh baik buat adik-adiknya bang"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "kalo badmood liat zaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "awalnya aku takut sama kakaknya tapi ternyata kakaknya baik banget",  
                "pesan":"tetap rendah hati selalu yaa kak"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin Alat Pancing",
                "sosmed": "@renishapg",
                "kesan": "kakaknya lucu,kece,dan random juga",  
                "pesan":"semoga sukses selaluu kak"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Wakatobi",
                "hobbi": "Bowling",
                "sosmed": "@ansftynn",
                "kesan": "kakaknya lucu dan humble juga ternyata",  
                "pesan":"jago bangeet kak bisa main bowling"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "abang yang pinter dan rendah hati banget",  
                "pesan":"semoga bisa terus menjadi panutan bang"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Wai huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "kakaknya lucu tapi galak",  
                "pesan":"semoga tetap keren selalu kak"
            },
             {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "abangnya pinter ngomong dan bikin semua orang nyaman",  
                "pesan":"gunakan bakat ngomongnya buat hal hal besar yaa bang"
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain Makanan Baru",
                "sosmed": "@myrrinn",
                "kesan": "abangnya kalem dan berwibawa",  
                "pesan":"Semoga dilancarkan semua urusannya bang"
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "ngumpulin batu unik dipantai",
                "sosmed": "@berlyyanda",
                "kesan": "kakaknya punya senyum yang bikin suasana adem dan ternyata orang sumbar juga",  
                "pesan":"jangan lupa senyum selalu kak"
            },
             {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "20",
                "asal":"Teluk Mondawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "kakaknya baik,lucu,dan menyenangkan",  
                "pesan":"jangan sering sering galau kak"
             },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "abangnya suka bercanda tapi tahu batas",  
                "pesan":"Tetap jadi pribadi yang hangat dan asik yaa bang"
            },
             {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin ka wawa ngomong",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya orangnya simpel tapi berwibawa",  
                "pesan":"tetap jadi pribadi yang sederhana bang"
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML hero semua franco",
                "sosmed": "@Monica_tjg",
                "kesan": "kakaknya baik dan keren abieeez",  
                "pesan":"info mabar ml kak"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@",
                "kesan": "kakaknya baik dan kalem juga orangnya",  
                "pesan":"sukses selaluu kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-rqBQNFWKIHrH5GKkMx6vinchv3rfm0F",
            "https://drive.google.com/uc?export=view&id=1ENTACtVlidjfGXXXpeGS0U2t0o9apr3m",
            "https://drive.google.com/uc?export=view&id=1K5apxbX6AX7unsDUg-d5lv85nKiTaT0a",
            "https://drive.google.com/uc?export=view&id=15TUi7iKoUxcnLPzpexiggoPnYqjaPIrL",
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
                "kesan": "abang yang keren dan kecee abiiiizzz",  
                "pesan":"semoga tetap semangat bang jadi senat nya"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjanani",
                "kesan": "kakaknya kalem dan gak banyak ngomong",  
                "pesan":"jangan lupa istirahat yaa kak"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Denger musik sambil jalan",
                "sosmed": "@fathinahazzh",
                "kesan": "kakaknya baik,asik,dan kalem juga",  
                "pesan":"jangan lupa bahagia terus kak"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main",
                "sosmed": "@lia.h_264",
                "kesan": "kakaknya keren,gak banyak ngomong,dan ternyata kakak nim akuu",  
                "pesan":"semoga makin sukses dan semangat terus kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qkGtha5eTBUo1HhTDotJzHhjarwW1KQT",
            "https://drive.google.com/uc?export=view&id=1M4GQJ6rzne34zrLLV_WmJs7ihh1n84vP",
            "https://drive.google.com/uc?export=view&id=11qox7AxEQV0d_AbhaKA_eYDLZdj0GGQo",
            "https://drive.google.com/uc?export=view&id=1vg4ImifyFb4RLbTRwsiVERqa_6oeLt9H",
            "https://drive.google.com/uc?export=view&id=1WzWFYEOWVv5p2hPBYpcB9vUpWFmmn-ug",
            "https://drive.google.com/uc?export=view&id=1LFdQlMtX56BNA0V-KF6fqZ-UipSEqVgR",
            "https://drive.google.com/uc?export=view&id=1uD8IcWeSb_CQ0rSu7P9KtAiiYE8i7zmH",
            "https://drive.google.com/uc?export=view&id=1ah9PxnnCFLnJtGqv19X_OnC8KapPOgxi",
            "https://drive.google.com/uc?export=view&id=1sAjbQngvE2LRC_5jrK6fCAvRCT_qzacF",
            "https://drive.google.com/uc?export=view&id=1xw9r3D1iJt5RJx9800NYVwUUb0C-qoHg",
            "https://drive.google.com/uc?export=view&id=13Y08Y48s1G-thHmO31U48nC-IuZGEnGs",
            "https://drive.google.com/uc?export=view&id=1qroDcilj1M9WUCwhwFeepuFYn6Sj-atg",
            "https://drive.google.com/uc?export=view&id=1QAnGkg7NG0zZjmQiukvj0a69oSWOMzPu",
            "https://drive.google.com/uc?export=view&id=1CRTejmMPc5IvrM6u7E5iosVuNETcI6dx",
            "https://drive.google.com/uc?export=view&id=1--Rg0M3qjbAGL9gWLGlFGh6Vu-b40MIJ",
            "https://drive.google.com/uc?export=view&id=1t7R4X7qbAqikHOakz_nAgA0c3IcS_yS-",
            "https://drive.google.com/uc?export=view&id=11sCLZ1GMuEAXZ_0S0TJP5TpMdQe0UC-M",
            "https://drive.google.com/uc?export=view&id=1TvkwPNnSDs4BGdOr9dMTkUw4-ztNP3Az",
            "https://drive.google.com/uc?export=view&id=1csflafxu8MUPnoY0xvtGj095igb6neDv",
            "https://drive.google.com/uc?export=view&id=1U9osA-AYJsoQZkf6Y8_KXkJMowY3tdHP",
            "https://drive.google.com/uc?export=view&id=1vdz6tiYn8I0Tapr3APNgS7-50J3pegyM",
            "https://drive.google.com/uc?export=view&id=1AspOedgRdVEsrG1jygxDPgCFnm0-jz3g",
            "https://drive.google.com/uc?export=view&id=1UWkmFunkVPeclZPE5JgXVojADXuXC1up",
            "https://drive.google.com/uc?export=view&id=1ghBUFZwW2Z3GK8vevDGGzTMdjFd19x7r",
            "https://drive.google.com/uc?export=view&id=1RglP1D0Upmx8DxEWwHHyqXUCT-9DDBcm",
            "https://drive.google.com/uc?export=view&id=1GnQdQBswIyyH_Q2xx2vpFtU8VFPSeUIe",
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
                "kesan": "abangnya gak banyak ngomong tapi berwibawa",  
                "pesan":"tetap jadi pribadi yang rendah hati terus yaa bang"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya kalau marah tuh elegan",  
                "pesan":"semoga makin sabar dan bijak yaa kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main apapun",
                "sosmed": "@allyapasha_",
                "kesan": "kakak yang baik banget,sabar,dan kereen juga",  
                "pesan":"makasih banget yaa kak udah mau sabar ngehadapin kami"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "kontrakan GH",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky",
                "kesan": "abangnya aktif banget,kayak ngkk pernah capek",  
                "pesan":"jangan lupa istirahat yaa bang semoga sehat selalu"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Samping kost daffa",
                "hobbi": "Main Sudoku",
                "sosmed": "@arientakhsnl",
                "kesan": "kakaknya wibawanya berasa banget walau diem aja",  
                "pesan":"semoga aura positifnya makin terpancar kak"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jailin putri",
                "sosmed": "@daffahdynn_",
                "kesan": "abang yang serius,tegas,tapi bisa diajak bercanda juga",  
                "pesan":"semaoga selalu bisa jadi contoh bagi kami bang"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_nrp",
                "kesan": "abangnya keren dan berwibawa",
                "pesan": "semangat terus kuliahnya bang"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"pasar muara beliti",
                "alamat": "kost putri, gerbang barat samping sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "kakak yang baik,kalem,tapi bisa serius juga",  
                "pesan":"semangat terus kak belajarnya"
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Urip",
                "alamat": "Belwis",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "abangnya berwibawa dan jago ngoding",  
                "pesan":"semangat terus dan sehat selalu bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma fam",
                "hobbi": "ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "abang yang tegas tapi baik bangeet",  
                "pesan":"semoga sukses teruss bang"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "maju jaya kost",
                "hobbi": "yapping sampe bete",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakaknya cuek tapi sebenarnya perhatian banget",  
                "pesan":"sehat terus kak dan tetap semangat"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Lari",
                "sosmed": "@sahid22_",
                "kesan": "abang yang paling kece,dan keren bangeet",  
                "pesan":"semoga ilmunya terus bermanfaat bang"
            },
            {
                "nama": "Ali Aristo Muthahhari parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "nangka 4, sukarame",
                "hobbi": "Main game + kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya kalem dan santai",  
                "pesan":"tetap jaga vibe itu keren banget bang"
            },
            {
                "nama": "Gusti Putu Ferazka D",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "mentor akuu yang baik bangett,random,dan perhatian banget",  
                "pesan":"jangan bosen bosen ngehadapin tingkah laku kita yaa kak"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya rapi banget,tiap penampilan selalu kece",  
                "pesan":"semoga kece selaluu kak"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kaka ini santai dan chill",  
                "pesan":"info daki gunung di roblox kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul9",
                "kesan": "abangnya lucu dan menyenangkan",  
                "pesan":"jangan keseringan main gamenya bang"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "abangnya nggak banyak bicara,tapi sekali ngomong langsung kena",  
                "pesan":"terus jadi pribadi yang berisi kayak gitu yaa bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.lapas raya no 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "kakaknya lucuu dan keren bangeet",  
                "pesan":"sehat selaluu kak"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Bikin project, ngoleksi data",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnya suka ngelucu tapi juga bisa serius pas butuh",  
                "pesan":"tetap jadi penyeimbang dimanapun itu bang"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Padang Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "abangnya mukanya serius banget tapi bisa asik juga",
                "pesan": "semangat terus bang"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakanya lucuu bangeet",  
                "pesan":"semoga harinya bahagia terus kak"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Lempar Batu",
                "sosmed": "@m.ridwan_22",
                "kesan": "abangnya baik dan cool",  
                "pesan":"stay kalem terus yaa bang"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "abang yang lucuu humoris bangeet",  
                "pesan":"jangan lupa istirahat dan tetap fokus bang"
            },
            {
                "nama": "Uliano Wiliam Purba ",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main musik, ngoding, menanam anggrek",
                "sosmed": "@nano.wlm",
                "kesan": "mukanya sereem tapi ternyata orangnya menyenangkan",  
                "pesan":"tetaap semangat bang"
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Bengong",
                "sosmed": "@rewinanaaa",
                "kesan": "kakaknya baik banget",  
                "pesan":"semangaat terus yaa kak"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jjk89Q6uOnVCIdJWqcHc3KnrMYj78WYa",
            "https://drive.google.com/uc?export=view&id=1OvT8Y6Z3Hx8iZjKFqnXa9YpbSchxWQxa",
            "https://drive.google.com/uc?export=view&id=10EtXZC9q11f6iTb4j7lt5Wpw6s4uI9eq",
            "https://drive.google.com/uc?export=view&id=13A5HF5aejT9av6b10-TP_fHixJ2-v_-y",
            "https://drive.google.com/uc?export=view&id=1WCOBFGgDqjFetrS5yNVDhHzP80FSGbWB",
            "https://drive.google.com/uc?export=view&id=16KA0twhpJnMLlVYTOTC3mqUYV7P_j2W-",
            "https://drive.google.com/uc?export=view&id=1hldtL3hGVUl0Y-zFqyrqEcQLKP5LdWHN",
            "https://drive.google.com/uc?export=view&id=1T7sYWCWGgzm1eyircfbGc2qIxiMtEPrm",
            "https://drive.google.com/uc?export=view&id=1xudpUWxgtyEfTrdZUJnlHZuo-h9PHX-d",
            "https://drive.google.com/uc?export=view&id=197p4Axdb0P9viBO4b6DpXedvQZyYV3tQ",
            "https://drive.google.com/uc?export=view&id=1xliOvAPZM6Y8CjOq2z_4CpcdsBDpI6mv",
            "https://drive.google.com/uc?export=view&id=1tGFxGSt7KnDFId8ktzJCGOx6pMPdRBBv",
            "https://drive.google.com/uc?export=view&id=1qXO5TxQS51MkxfAbOnBy84gc9e278ILF",
            "https://drive.google.com/uc?export=view&id=1Pe76joTM6YPIpiSDDyXsyzUZ6AP2Ki-6",
            "https://drive.google.com/uc?export=view&id=1PAN2IeXuQrrboT5g_zDbuUrS-rH7zMrl",
            "https://drive.google.com/uc?export=view&id=1E3akAZgRC8zteH6RhZHGDM4RPGnjFbkH",
            "https://drive.google.com/uc?export=view&id=1jhYu-qbJcQJFz2d3FzmhYsZOH_TN0pbf",
            "https://drive.google.com/uc?export=view&id=1wgkeOOCFTEs-KBaQWuz1J4zqSerqWWl_",
            "https://drive.google.com/uc?export=view&id=19sYokfuPTv8_Xa_-_qNZO-sRjdseGnG5",
            "https://drive.google.com/uc?export=view&id=1sOQCsngvs9e2anhxuzygjmkT8sCU4ZNJ",
            "https://drive.google.com/uc?export=view&id=1z3trPDJ8JS4cli1tNeLWDVJ7Tm5XaGT7",
            "https://drive.google.com/uc?export=view&id=1JbTMXvDop8jIxjL8DMVuXhy3-ucRV300",
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
                "kesan": "Abangnya asik dan humble bisa diajak diskusi bareng",
                "pesan":"Jangan patah semangat bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@junitaa.0406",
                "kesan": "Kakaknya baik dan humble banget",  
                "pesan":"Jangan lupa makan yaa kak"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya rajin bangeet",  
                "pesan":"Semoga cepat lulus yaa bang"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya kalem,lucu",
                "pesan":"Jaga kesehatan selaluu kak"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Abangnya mudah diajak bergaul dan simpel",
                "pesan":"Semangat terus bang dan semoga kuliahnya lancar"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Abangnya punya energi positif",
                "pesan":"Terus pancarkan energi baik itu yaa bang" 
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tj. Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya baik,gak banyak ngomong,dan kalem",
                "pesan":"Tetap semangat bang"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "jl. Manggis 1",
                "hobbi": "Nonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "kakanya baik dan gak neko neko",  
                "pesan":"semangat terus kak belajarnya"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "kakanya selalu ceriaa teruus",
                "pesan":"terus bagiin kebahagiaan itu kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abangnya keren dan gokill abiis",
                "pesan":"Always keren yaa bang"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya baik dan menyenangkan juga",
                "pesan":"Keren banget kakaknya bisa ngedance"    
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jl. Raden Saleh",
                "hobbi": "jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya keren bangeet",
                "pesan":"Tetap semangat kak"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan Bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "kakanya kalem dan cool",  
                "pesan":"Tutor main piano dong kak"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakaknya lucuu dan asyiik urang awak ternyata",
                "pesan":"Sukses selalu kak tapi jangan keseringan tidur"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama ITERA TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kakaknya mudah bergaul dan chill",
                "pesan":"Semoga dimudahkan urusannya selalu kak"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Muka abangnya kayak orang jago ngoding banget",
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya lucuu dan asik juga diajak ngobrol",
                "pesan":"Jaga kesehatan selalu yaa kak"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Abang yang keren,asik,dan bisa banget buat diajak diskusi",
                "pesan":"Semangat terus bang semoga dilancarkan urusan kedepannya"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya kalem dan asyik",
                "pesan":"Tutor catur yang jago dong bang"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakaknya selalu berusaha membuat suasana nyaman",
                "pesan":"Jangan patah semangat yaa kak"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya lucuu abiis",  
                "pesan":"Semangat terus kak belajarnya"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya kalem gak banyak ngomong",
                "pesan":"Kapan kapan ayo futsalan bareng bang"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()
       

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1niEcPcxPj7q6GYBbkHx_N0OnoFCDxbuf",
            "https://drive.google.com/uc?export=view&id=1KORT1LBEr3O65bv_zPMAn8fxHP7OVuFU",
            "https://drive.google.com/uc?export=view&id=1JbeDi9X67lilywnT4gPg4oDrFDaqdu0q",
            "https://drive.google.com/uc?export=view&id=17ZyJ7giZN2fT28OBqgX-CxsnzX4ZoPje",
            "https://drive.google.com/uc?export=view&id=1khSSrTwwrH6JPw009FR_SgTg5opk0TXi",
            "https://drive.google.com/uc?export=view&id=1sfZhB5yu4IAp47Ot4aYZZ6CLRhl_Qe76",
            "https://drive.google.com/uc?export=view&id=1HUdCvFh8HvhH0pRgM59pp36GrwXd6fn8",
            "https://drive.google.com/uc?export=view&id=1vOD2k_EtwlSRK6Db9-3Jrh6DVdPY_XY5",
            "https://drive.google.com/uc?export=view&id=17Q1r20-N-MwEiPnsKG9sIdGKBSC3RR3N",
            "https://drive.google.com/uc?export=view&id=1uQ_69Ib-WEZTuJzabD0qLA3-PlbfbE0O",
            "https://drive.google.com/uc?export=view&id=1QZZ9832C9C5mfjX1q8wak5pYdlhmSS4c",
            "https://drive.google.com/uc?export=view&id=1HiWBFMBUdep7j16Cy9uHOCKdRswa_mmR",
            "https://drive.google.com/uc?export=view&id=1xORWxYSp-DwYZArm8g8OxxiKAflKu49L",
            "https://drive.google.com/uc?export=view&id=1m3hHbYNoK7__Fdlut6sXSWBfNe9BRFWm",
            "https://drive.google.com/uc?export=view&id=1vR8AzfCNIiXFz0jz4LIAvoyKHEybmU8_",
            "https://drive.google.com/uc?export=view&id=1Qbj4gDhtDXLMFWlX5czLf4bMwOgOurm2",
            "https://drive.google.com/uc?export=view&id=11VIn2rJES87FWYghn_CGLQZcexqIYKfB",
            "https://drive.google.com/uc?export=view&id=1MoILZJLrv1qRATzvzqVu-qu5vx7C8nZH",
            "https://drive.google.com/uc?export=view&id=1AP8fZh0KRCumBi8qygCaWM-SN2nC-yvz",
            "https://drive.google.com/uc?export=view&id=17tuWApn9BZRGJEmtGntz9ugPXSmjZiAH",
            "https://drive.google.com/uc?export=view&id=1VtzdCB553Zbkq58lzbwhdYmbG-JYV8RF",
            "https://drive.google.com/uc?export=view&id=16jFkKtrvmM2rTlcn2l1gkTGosU4XjgYt",
            "https://drive.google.com/uc?export=view&id=1XfIE6ywAAIc17r08wxMghog5u75Qk511",
            "https://drive.google.com/uc?export=view&id=1Gv15dd1U9o-lCeARkMXULd-u7PmQVkHV",
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "Abangnya asyik tapi berwibawa",
                "pesan":"Terus jadi contoh bagi kami yaa bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya baik dan humble bangeet",
                "pesan":"Sukses terus kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya ramah dan seruu",
                "pesan":"Semangat terus kak ngejalanin hidupnya"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "kakanya asik dan chill bangeet",
                "pesan":"Semoga sehat terus kak"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya gokill dan lucu juga",
                "pesan":"Jangan sering sering ngelamun bang"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakak yang lucu dan asikk bangeet",
                "pesan":"Jangan lupa istirahat yaa kak"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakaknya humoris dan lucuu",
                "pesan":"Info dataset kak"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak yang baik dan humble",
                "pesan":"Kalau jalan jalan ajak aku juga yaa kak"
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abangnya seru dan mudah buat diajak ngobrol",
                "pesan":"Semangat terus bang kuliahnya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak yang selalu bahagia dan ketawa terus",
                "pesan":"Semoga hidupnya bahagia selalu yaa kak"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya keren dan asik juga",
                "pesan":"Sehat sehat terus yaa kak"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya gokiil bangeet",
                "pesan":"Semoga harinya selalu cerah yaa kak"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya keren,tegas,dan gokil lah pokoknya",
                "pesan":"Tetap semangat bang"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakaknya asik dan menyenangkan juga",
                "pesan":"Always happy yaa kak"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Orangnya seruu dan menyenangkan",
                "pesan":"Semoga bahagia terus yaa kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya ramah dan baik",
                "pesan":"Tutor badmin dong bang"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya kalem tapi bisa diajak ngobrol bareng",
                "pesan":"Sehat selalu yaa bang"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya gokiil asyik banget",
                "pesan":"Sukses selalu yaa kak"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya menyenangkan dan urang awak juga",
                "pesan":"Terus jadi pribadi yang baik yaa kak"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya baik dan lucu abiis",
                "pesan":"Tetap semangat yaa kak"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya asik dan lucuu bangeet",
                "pesan":"Semangat teruus kakakk"
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya bawaannya ceria dan bahagia terus",
                "pesan":"Semoga bahagia terus yaa kak"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya ramah dan baik banget",
                "pesan":"Semangat kuliahnya bangg"#
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Asyik dan menyenangkan banget",
                "pesan":"Semoga dimudahkan segala urusan kak"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Vt0QiVMxwckzGVC1GfERr2F3MyFm_1_t",
            "https://drive.google.com/uc?export=view&id=1fMMwDSomGRgfwIq6OnuqoEz84MVjfKKE",
            "https://drive.google.com/uc?export=view&id=1iiMZlQw_mu7zuuel2sqje-YJTLL0rGu_",
            "https://drive.google.com/uc?export=view&id=19YEXZYAQJNSurnAbKGybBjkndo_02eFm",
            "https://drive.google.com/uc?export=view&id=1PJiyU8MJkDALMzzteTxkiXEMMMh_Ugk0",
            "https://drive.google.com/uc?export=view&id=1eUQ65fitxAIGd6txMjhmuOvn4YiUOH9k",
            "https://drive.google.com/uc?export=view&id=1Uji66oY2KaxAGghOVnfCJb63ViAxHsqF",
            "https://drive.google.com/uc?export=view&id=1YsvBuTH7w-ar-Dfmgv8Qse7NS0Bo_G99",
            "https://drive.google.com/uc?export=view&id=190suL3SAujRFSTmxd6rd2UtHIc9ebNfr",
            "https://drive.google.com/uc?export=view&id=1O79CUVRFYKB-raP2rUxNkQVLqDLZftWw",
            "https://drive.google.com/uc?export=view&id=1hB2U0QlLN5nsb8SG9QrXKZe7pUb4jazp",
            "https://drive.google.com/uc?export=view&id=1btHVR09DAsWlW2w5RXKHcmS4CVauMZsw",
            "https://drive.google.com/uc?export=view&id=19u_qHtsmJqSp1BtlzUmgqZQT0YScUyXQ",
            "https://drive.google.com/uc?export=view&id=1178HReSyCq7ze23JMB_WsB_3BRj-JVQx",
            "https://drive.google.com/uc?export=view&id=13JIaQjbpAwnFCveACtoIyI4VrJdgFLJF",    
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
                "kesan": "Kakaknya baikk dan kereen",
                "pesan": "Semoga mengajinya konsisten kak"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya seruu,lucu,dan menyenangkan",
                "pesan": "Semangat terus mancingnya kak dan semangat terus"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya kalem dan seruu",
                "pesan": "Semangat kak memanahnya"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Masakin aku kak sekali sekali"
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya serius tapi juga santai",
                "pesan": "Semoga menang balapannya bang"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya lucuu,dan kereen bangeet",
                "pesan": "Semoga nanti bisa buka toko kue kak"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "kakanya serius tapi juga bisa ramah",
                "pesan": "Keren banget kak bisa berkuda"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalghani73",
                "kesan": "Abangnya baik dan ramah",  
                "pesan":"Sehat dan sukses terus bang"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya asik dan kece banget",
                "pesan": "Semangat terus olahraganya bang"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya kalem dan ramah",
                "pesan": "Semangat terus bang nyanyinya"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya lucuu,asik,dan sangat sangat ramah",  
                "pesan":"Kuliahnya semoga lancar terus kak"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya kalem dan lucu",
                "pesan": "Semangat main musiknya kak"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya kalem,baik,dan ramah",
                "pesan": "Semoga lebih semangat lagi bang"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya lucuu,asikk",
                "pesan": "Keren banget kak bisa main alat musik"
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Rubik Mirror",
                "sosmed": "@zhrptsl",
                "kesan": "kakanya lucuu,seru,dan asik",  
                "pesan":"Keren banget bisa main rubik kakaknya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YolzMdayWceQt2NHLLa90N28f7u61ReD",
            "https://drive.google.com/uc?export=view&id=1QAz63w7vTB2Nn1f5b2kCWPN7YIhodj0P",
            "https://drive.google.com/uc?export=view&id=104jTcMKThL7H4DVY82rGLcsD1bA2qObp",
            "https://drive.google.com/uc?export=view&id=1v5MsGFKKub1BhB3-12ANPypd1fIOwY-1",
            "https://drive.google.com/uc?export=view&id=1RwfuWvBXxmp-9IHSuizQBGYgKf0XCZQU",
            "https://drive.google.com/uc?export=view&id=1x2Gs8SQC2xabJDpecFeql4Uc7ZcMKXJU",
            "https://drive.google.com/uc?export=view&id=1h2srZ3fn5PV9ES80KzqueN4ubsg-Sieb",
            "https://drive.google.com/uc?export=view&id=1y_YHuPTx3LpPs7OermE84IihQPMEOHf8",
            "https://drive.google.com/uc?export=view&id=1dheuMq5ZNv0Cm0lwwazc0CsHpfCipl0M",
            "https://drive.google.com/uc?export=view&id=1JqTKNwmedTXYnw_SRcNc3S7QnLbhJ8sq",
            "https://drive.google.com/uc?export=view&id=1Rzcaix6Kqv-SkAaAti6n8cutE3ET3EwV",
            
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
                "kesan": "Abangnya asik dan keren banget",
                "pesan": "Semangat terus abangg"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya baik dan lucu bangeet",
                "pesan": "Semoga dilancarkan kuliahnya kak"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya baik dan ramah banget",
                "pesan": "Info parfum paling harum bang"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya keren dan lucuu",
                "pesan": "Semangat terus kak joggingnya"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Kakaknya asik dan seruu",
                "pesan": "Jaga terus kesehatannya kak"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya bener bener baik",
                "pesan": "Semangat kak joggingnya"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya menyenangkan dan ramah",
                "pesan": "Semangat terus bang belajarnya"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya baik dan suka snyum",
                "pesan": "Info drakor paling bagus kak"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakaknya orangnya seru banget",
                "pesan": "Sukses selalu yaa kak"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya ceria dan lucuu",
                "pesan": "Jaga kesehatan terus yaa kak"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakanya baik,menyenangkan dan asyiik",
                "pesan": "Semangat dan sukses terus kak"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16rY3pqBcmbZ7H0c6TWiDg0nVleD5tz7G",
            "https://drive.google.com/uc?export=view&id=1uRIVheNP1fHav3lljasdxCbQ-9JX-5D_",
            "https://drive.google.com/uc?export=view&id=1nqk7Oo33KaT8tcvI82hLdDa7jUW5FKrB",
            "https://drive.google.com/uc?export=view&id=1gmLzqyyJb_KwdeIpH2IzeuSGDT7QXXaL",
            "https://drive.google.com/uc?export=view&id=1yWQta5wkEMSweih5t1clXHK0AEkQlW-i",
            "https://drive.google.com/uc?export=view&id=165fR7zOwwQZapmRmsy2UcadHxN5eutBn",
            "https://drive.google.com/uc?export=view&id=1tTyMJX6qmLxGBq69lWlFXw_gQCk7Wayv",
            "https://drive.google.com/uc?export=view&id=1K8Mp42mjdhlLc1nwj7tNXazTTF3AeHCy",
            "https://drive.google.com/uc?export=view&id=1bE4Yu8rQvUaPTYL2tCsGvjzGr21PnoF_",
            "https://drive.google.com/uc?export=view&id=1p9WjSPqBuoVcwNV1D1QGpBrL86Ob1Inn",
            "https://drive.google.com/uc?export=view&id=1rw_7ugIMFjDt0Ls6nAfMzizKlu8RCQ13",
            "https://drive.google.com/uc?export=view&id=1TNBAPq-nr1JGnnQgkNrSi4LLPxonlokQ",
            "https://drive.google.com/uc?export=view&id=1z6jhLQtMAu66-EbY7DyvrPtXoy29W0ib",
            "https://drive.google.com/uc?export=view&id=1x_Zi2EHTN8swoMud1z9CkcLE2rOQFgAF",
            "https://drive.google.com/uc?export=view&id=1tQPXfaI2AbsYaWdHEQCT67yuJC19Q_pJ",
            "https://drive.google.com/uc?export=view&id=10xPCnqipqTxBBI_KOxp5Hg393dKFkP68",
            "https://drive.google.com/uc?export=view&id=1L0DxYiESjdp_iDjYiCpjzBl3mgU6Vlwn",
            "https://drive.google.com/uc?export=view&id=1O0LKrZqogSfbP67T1rT4MnUHVAaltx2Z",
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
                "kesan": "Kakaknya asik dan lucuu bangeet serta berwibawa",
                "pesan": "Sukses dan ceria terus yaa kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Kakaknya menyenangkan banget",
                "pesan": "Info makan makan kak"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Abangnya keren dan kece bangeet",
                "pesan": "Tutor billiard dong bang"
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abang yg selalu pegang kamera terus",
                "pesan": "Sehat dan sukses selalu bang"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya asyik dan keren bangeet",
                "pesan": "Semoga sehat selalu bang"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakaknya kereen abiis",
                "pesan": "Semangat terus yaa kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya baik dan ramah banget",
                "pesan": "Tetap semangat kak"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakaknya lucuu dan gokiil",
                "pesan": "Semangat terus kak kuliahnya"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Gokil banget kak",
                "pesan": "Semoga sukses selalu kak"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya asiik bangeet",
                "pesan": "Lancar terus ya kak kuliahnya"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya humble dan baik banget",
                "pesan": "Jaga kesehatan terus yaa kak"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya pintar dan lucuu bangeet",
                "pesan": "Sukses terus kedepannya kak"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya lucu dan menyenangkan",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Kakaknya asik dan mudah bergaul",
                "pesan": "Semangat terus bang kuliahnya"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya sangat baik dan ramah",
                "pesan": "Semangat terus dan semoga sukses kak"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakaknya asiik bangeet",
                "pesan": "Jangan lupa jaga kesehatan ya kak"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya keren dan menginspirasi",
                "pesan": "Semoga sukses terus kak"
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
                "pesan": "Selalu jaga kesehatan ya kak"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
# Tambahkan menu lainnya sesuai kebutuhan


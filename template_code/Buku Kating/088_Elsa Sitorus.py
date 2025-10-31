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
            "nav-link-selected": {"background-color": "#FF6F00"},
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
            "https://drive.google.com/uc?export=view&id=1d2_8X8OVUjh_HDAlm9PUcBxMSNVxz0wf",
            "https://drive.google.com/uc?export=view&id=1A9HyDvFYCGg_L6Vue6a5nNA6WuW4bWaL",
            "https://drive.google.com/uc?export=view&id=1tfD1JCtXw13niRVdky0JEQ4rntmUQPyc",
            "https://drive.google.com/uc?export=view&id=1ERDwvQS4Eoy1b6XaFDUaEsVQ-JHKNTfz",
            "https://drive.google.com/uc?export=view&id=1dPCUOlbN2CAN9Y_8KuCHxXNWNXf4ICz4",
            "https://drive.google.com/uc?export=view&id=1nVrTBVWzCWpXVi7eDJI9D_QSegsh89_6"
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@erendraa",
                "kesan": "Ssosok pemimpin yang kece, liat bang Rendra jadi pengen jadi Kahim juga",  
                "pesan":"semangat bang, tetap jadi orang hebat !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "Keliatannya kayak preman tapi sebenarnya baik",  
                "pesan":"semangat bang, jangan capek jadi orang baik !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak yang baik baget, lucu dan sangat baik",  
                "pesan":"Tetap jadi orang keren yang jadi panutan kak !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya cakep banget, dan pembawaanya addem banget",  
                "pesan":"Tetap semangat kak untuk jadi orang sukses !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Asik banget, suka banget denger kak Eksanty yapping, happy vibes banget",  
                "pesan":"Semangat kuliahnya kak, tetap jadi orang keren yang nyebarin kebahagiaan buat orang lain !!!"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya cakep banget, terus happy vibes",  
                "pesan":"Semangat kuliahnya kak, tetap jadi orang keren dan jangan capek buat bertumbuh jadi orang yang semakin keren !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19OFfw-MrCdSA0PmcygXBhLojQBCV5Kat",
            "https://drive.google.com/uc?export=view&id=1liYV-DxrQ8dxHFHWFHA4aokTpq_GFJMd",
            "https://drive.google.com/uc?export=view&id=1znnWOVL0Mc_0-o0tV7eX8tCxzDpi3c1f",
            "https://drive.google.com/uc?export=view&id=1snuxlRu6IX1zX10zOgrQNRSzwaqcUcyC",
            "https://drive.google.com/uc?export=view&id=1KT95G6iC1MJBQgt1COaUr8On7PFFaYBD",
            "https://drive.google.com/uc?export=view&id=1_Uzidz9yUkSeItRPheD_LnpKgSB0QQRI",
            "https://drive.google.com/uc?export=view&id=1Pm5pW0RsQsR12386Fw4iHSQ4XCn2tUlb",
            "https://drive.google.com/uc?export=view&id=1Ak2yJTDp1cVmKoy-IwDNazVVrnuFu3MW",
            "https://drive.google.com/uc?export=view&id=1twCCnbf7A2kEt179EskvodJ0TuoN1wvW",
            "https://drive.google.com/uc?export=view&id=1QnGOqcfo0dkadkLkDiYFaYvgszcXq2Ln",
            "https://drive.google.com/uc?export=view&id=1jLAoyR0z7rvC5PoyseGKBhd7YUERfJ89",
            "https://drive.google.com/uc?export=view&id=1DnG3fWzrWa8SXLB5IbwVR2D45GQ-iclv",
            "https://drive.google.com/uc?export=view&id=1kdpj8lUHmYVEelcZV-x_rWttBuQmx61K",
            "https://drive.google.com/uc?export=view&id=1lKGjglB0tYJGyGShfIwpID0cWukfMhxY",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto", 
                "nim": "122340022",
                "umur": "21",
                "asal":"Nusa Kambangan",
                "alamat": "Lapas, Belwis",
                "hobbi": "Melarikan diri",
                "sosmed": "@jeremia_s_",
                "kesan": "Vibesnya cowok cool gitu, tapi ternyata absurd juga ",  
                "pesan":"Semangat bang, pertahankan image coolnya !!!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Kakaknya lucu banget, happy vibes banget",  
                "pesan":"Semangat kak, jangan capek buat nyebarin virus kebahagiaan buat orang-orang !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Keliatannya pendiem, terus vibes cewek kalcer",  
                "pesan":"Semangat kak, apapun yang etrjadi hari ini jadikan pelajaran untuk di hari esok !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Kakaknya kalem banget, vibes kakak kakak kuliahan banget",  
                "pesan":"Tetap bertumbuh jadi orang baik ya kak, semnagat kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "Pinter banget, OZT",  
                "pesan":"Semangat bang, jangan capek jadi orang keren, tetap tumbuh jadi orang yang keren kayak sekarang !!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Cantik banget, suka warna rambutnya",  
                "pesan":"Semangat kak, apapun keadaannya tetap jalanin dengan senyum terbaik kakak di hari itu !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "Abang baleg terkecee, asik banget gaboong",  
                "pesan":"Semangat bangg, tetap jadi bang Givaro yang keren, setiap harinya jangan lupa upgrade diri jadi orang yang semakin keren !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Kayaknya abangnya pendiem",  
                "pesan":"Semangat bang, seberapa sulit keadannya bantai aja bang, jangan kasih kendor !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Aura cewek cantiknya kerasa banget",  
                "pesan":"Semangat kakak, kalo capek boleh berenti dulu tapi nanti lanjut lagi dengan versi yang lebih baik !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak satu ini kece banget, semua kepanitiaan maupun organisasi dibantai habiss",  
                "pesan":"Semangat kak juee, jangan lupa istirahat !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang batak yang keren, bataknya kerasa banget pliss",  
                "pesan":"Semangat bang, kalau capek inget aja pasti ada yang lebih capek !!!"# 1
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Vibes orang baiknya kerasa",  
                "pesan":"Semangat bang, tetap menjadi orang baik !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "-",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Baik banget dan sosok kakak yang sangat mengayomi",  
                "pesan":"Semangat kakak, jangan capek bantai semuanya !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Baik banget dan ramah abis",  
                "pesan":"Semangat kak, jangan kendor semangatnya !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hgKJIjyCnwbrM6SYm-HRUR-kX030byn7",
            "https://drive.google.com/uc?export=view&id=1s5V3dl84qL0juqIwlxe-uRwVN5XJfhEN",
            "https://drive.google.com/uc?export=view&id=1LhXmGs2O6bHuWA-Zsipl8_FzprzYM0Ry",
            "https://drive.google.com/uc?export=view&id=1koV-R8W6ZylHnL5uCxHQMSJw6RQ_fl1y",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Tanya Caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Keren banget, PANUTAN ",  
                "pesan":"Semangat bang, tetap menjadi salah satu orang keren di dunia ini, dan tetap bertumbuh menjadi orang keren diantara orang keren lainnya !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "Vibes orang pinter banget",  
                "pesan":"Semangat kak, jangan kendor semangatnya !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "Pinter banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya asik banget",  
                "pesan":"Tetap senyum apapun hal yang terjadi hari ini, besok, dan seterusnya !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Am4qvI2T-yngjlz7wjXMPDoz2NYiOOr9",
            "https://drive.google.com/uc?export=view&id=1oQkiuWWvArihB2T4vZ86IcrN5sz64wuD",
            "https://drive.google.com/uc?export=view&id=1KPbnWVb_UwpwFbYRowkPD--6WLi9ZpyR",
            "https://drive.google.com/uc?export=view&id=1MtcC1Ijs-aka8U6yVNxYB4XIrmDjHkSO",
            "https://drive.google.com/uc?export=view&id=176o7YzFGqa8XMazKoQjxsSJIphpumGiX",
            "https://drive.google.com/uc?export=view&id=1dZLxabpQZsIvVc6ogGobMrPYLNzBQLdX",
            "https://drive.google.com/uc?export=view&id=1F_oakMe7QrQa5uGq2WRaDoajfK_Mp3Nj",
            "https://drive.google.com/uc?export=view&id=1lO9GR8Ir1pHsnX3yAdwWni0ilczhRQiU",
            "https://drive.google.com/uc?export=view&id=1J6Ta6ZTbRY8ysJrbZYc0ibG_yuT2YcrM",
            "https://drive.google.com/uc?export=view&id=1h-0cUeOmz59d-Utq4Muuke1KmBtJTYVj",
            "https://drive.google.com/uc?export=view&id=11moWb96SqunK7qeVcqboWGCXEnMe6hLv",
            "https://drive.google.com/uc?export=view&id=1i5ffEqoAnvX7iNJxwiioZ4nCyVgw1AFS",
            "https://drive.google.com/uc?export=view&id=19Rq99EOQg5k4_hgkALuSLkSXODSzpO-l",
            "https://drive.google.com/uc?export=view&id=1H3xzxchkjGJhLSJLFXY1LbA9bezYjjdG",
            "https://drive.google.com/uc?export=view&id=1LduknrIJZSEMGNn7jKAv8jehGFkO3eE2",
            "https://drive.google.com/uc?export=view&id=1aPKR0iVjgRLpVLSULrgo5QBK_UYuCRDo",
            "https://drive.google.com/uc?export=view&id=1wC95F4jQkXZBME6q9S03BrdHaXlK_oOP",
            "https://drive.google.com/uc?export=view&id=1SI7Qd5HTFWW-gVXKSYBXAnQji31mAv-j",
            "https://drive.google.com/uc?export=view&id=1yfv_lYVZgqe71MSxlDLgjUpYnhoU2-ck",
            "https://drive.google.com/uc?export=view&id=1vwntvR0q5vK31_2FV4nm1645o4s-rkJs",
            "https://drive.google.com/uc?export=view&id=17RoMaEkGlnbU3dFoNtYoep8RCHhMwwq5",
            "https://drive.google.com/uc?export=view&id=1Za1OMzwmYZgIjRYeI1gnbdnIRrEzcTv_",
            "https://drive.google.com/uc?export=view&id=1YusIKlZs3j7MCYBZQRWbcxbRTsf89OPW",
            "https://drive.google.com/uc?export=view&id=1Zkpa7u3P_p11Ly17eOuS1egUA69bxg1m",
            "https://drive.google.com/uc?export=view&id=1UrrBDpYnU6thLcmwVVREdSsw1CblN-ni",
            "https://drive.google.com/uc?export=view&id=115c_F24rWpqS7lTB8z964DLVE0mPlB9c",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Keliatannya kocak terus, tapi ternyata tersimpan sosok pemimpin yang keren ",
                "pesan": "Semangat bang, tetap menjadi sumber kebahgaiaan buat orang lain !!!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "Cantik banget ",
                "pesan": "Jangan lupa senyum kak setidak menyenangkan apapun kehidupan yang lagi dijalani !!!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Orangnya tegas, tapi sebenarnya baik ",
                "pesan": "Tetap menjadi seorang pemimpin yang benar benar pemimpin kak, always jadi panutan !!!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Gacor parah gadak lawan, panutan banget ",
                "pesan": "Tetap bertumbuh jadi orang yang bermanfaat bagi orang lain bang, apapun yang abang jalanin saat ini semoga menjadi titik terang buat hidup abang dan jadi inspirasi buat orang lain !!!"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Orangnya keliatan jutek tapi kalau senyum ternyata semanis dan secantik itu ",
                "pesan": "Tetap menajdi orang yang menginspirasi kak, apapun keadaannya jangan lupakan apa yang jadi motivasi kakak untuk bertahan saat ini !!!"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Baik banget, kalo disapa always senyum dan ramah ",
                "pesan": "Semangat bang, apapun kondisinya tetap bertumbuh jadi orang yang semakin baik !!!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Yang keliatannya galak tapi aslinya berhati malaikat ",
                "pesan": "Terimakasih bang karena udah jadi orang baik, tetap menjadi bang Fajar yang baik !!!"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "Keliatannya galak, tapi ternyata lucu dan menyenangkan banget ",
                "pesan": "Tetap jadi orang keren dan jangan lupa selalu menebarkan kebaikan dimanapaun dan kapanpun !!!"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "Vibesnya galak banget ",
                "pesan": "Semangat bang, apapun yang mau abang gapai saat ini tetap usahakan dengan segala usaha terbaik yang abang punya !!!"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Kalau di rangkaian tegas banget, tapi pas praktikum baik banget gaboong ",
                "pesan": "Terimakasih bang sudah menjadi orang baik, terimakasih waktu itu gadipersulit praktikum susulan, tetap menebarkan kebaikan ya bang !!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Keliatannya judes banget, kadang takut buat nyapa ",
                "pesan": "Sesulit apapun jalannya tetap lewatin dengan hati, pikiran, dan ssegala hal baik yang kakak punya !!!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "Vibes oreang sibuk ",
                "pesan": "Semangat bang, jangan lupa istirahat !!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Auranya kayak orang pendiem, tapi ternyata asik diajak gosipin matkul ",
                "pesan": "Jangan lupa makan bang, tetap hidup untuk segala hal yang abang impikan !!!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "Cantik banget, lemah lembut ",
                "pesan": "Semangat kakak cantik, terus bahagaia dengam apa yang kakak punya kemarin, sekarang, dan yang akan dataang !!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Keliatannya judes, tapi jujurly cantik banget ",
                "pesan": "Semangat kakak, jangan lupa bahagia !!!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Baik banget kakak ini, makasih udah jadi orang baik kak ",
                "pesan": "Semangat kuliahnya kak, apapun yang sedang kakak jalani jangan lupa bahagia kak !!!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "Asik banget ",
                "pesan": "Semangat bang, jangan lupa untuk kasih ruang buat diri sendiri !!!"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "Vibesnya orang serius banget ",
                "pesan": "Terus bertumbuh jadi versi terbaik dari diri abang, semangat bang !!!"# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Serem ",
                "pesan": "Semangat bang, jangan lelah untuk berubah menjadi versi yang lebih baik !!!"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "Attractive banget ",
                "pesan": "Semangat kak, terus bertumbuh menjadi orang keren !!!"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abangnya asik parah ",
                "pesan": "Semangat bang, terus menebarkan cirus kebaikan dimanapun dan kapanpun !!!"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Pembawaan orang serius banget ",
                "pesan": "Semangat bang, jangan lupa bahagia hari ini !!!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "Bauk banget, udah kenal mulai natal Sains Data ",
                "pesan": "Terimakasih kak udah jadi orang baik, tetap ajdi orang baik ya kak !!!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Humble banget ",
                "pesan": "Semangat bang, jangan lupa senyum hari ini !!!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Kocak banget ",
                "pesan": "Tetap jadi orang baik dan ceria yang menebarkan virus bahagia untuk siapapun !!!"# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Baik banget ",
                "pesan": "Semangat kuliahnya kak, jangan lupa tersenyum hari ini !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c6R1Uph1zTN-b4h_erHgKZRxmWGofCnP",
            "https://drive.google.com/uc?export=view&id=1qZvCNsqndkkaPyh7zPfuHXcD0vx1XZ9P",
            "https://drive.google.com/uc?export=view&id=1htJQUqfBDK9A2SZIx_jPBSx5s9naYqQi",
            "https://drive.google.com/uc?export=view&id=1XsOyz1tSpcfnUmZvv6FILFme2mzvvO5j",
            "https://drive.google.com/uc?export=view&id=1H6qW3yZBHPs8dr3CmEMRpnzqz7wT1NhU",
            "https://drive.google.com/uc?export=view&id=1wmB2XLN0fmfMSLddIYfprgSP6X-u-lhS",
            "https://drive.google.com/uc?export=view&id=1Nph0WKEQyDEpf8sfapCfgyu0tO-Ng06w",
            "https://drive.google.com/uc?export=view&id=1YRg49rveDFp8ScpEIZnlQghNERnfxOGN",
            "https://drive.google.com/uc?export=view&id=17rbOsrh3X6YsA2xJ8PwPfixGzSccGZDj",
            "https://drive.google.com/uc?export=view&id=1VlstTEnvdqUyMxDWMg5AK69mtWa86Cn1",
            "https://drive.google.com/uc?export=view&id=1CR4Crv7aHH4eXifsE1jUsCW81oNpCqHf",
            "https://drive.google.com/uc?export=view&id=1UtwhyU_tPUthWCPEQMctW8eS3Dg-ki5G",
            "https://drive.google.com/uc?export=view&id=1LMr8p5RKB-6vGGkpu-ftrr5TSwUvc9CI",
            "https://drive.google.com/uc?export=view&id=1F34X3IHNfjaLXOuPb7lIMz4f91QIlOVX",
            "https://drive.google.com/uc?export=view&id=1tX3IEZ8H4EgKMqArG1t3Omw8mfP9zDxZ",
            "https://drive.google.com/uc?export=view&id=19gOVs0nRoVoC6f0pkaXH96psgzyQ3i48",
            "https://drive.google.com/uc?export=view&id=19-mVehpj62zmErYTd803O2eCBIUsr0eu",
            "https://drive.google.com/uc?export=view&id=1HXLCrgdVjgpSlE2Pq90xnFouCYhRAyTn",
            "https://drive.google.com/uc?export=view&id=1qIv0tFZdb1CfbO5GB_Z3MTXiGSCVd9CR",
            "https://drive.google.com/uc?export=view&id=1XFI8x1Q95SWdFyMdopxeZWFBdXs5DrgP",
            "https://drive.google.com/uc?export=view&id=19nS4pUiKuVlgU3YwQ3xzbs7l3FlImIdR",
            "https://drive.google.com/uc?export=view&id=1ADfyWQBvtDB-UmOIf6zevAT3oA8d4dUA",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123440083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Aura orang pinternya kerasa banget ",
                "pesan": "Semangat bang, tetap jadi orang yang kece ya !!!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "Baik banget, aura keibuannya keras, sangat menygayomi ",
                "pesan": "Semangat kak, semoga cepet wisuda !!!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Keren banget, ada vibes modelnya ",
                "pesan": "Semangat bang, semoga bisa menjadi duta masa depan !!!"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kalem banget ",
                "pesan": "Tetap semnagat kak, tetap menjadi orang baik kakak !!!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Duta kerenn ",
                "pesan": "Semangat bang, jangan capek bantai semester 5 nya !!!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kocak parah, asik banget ",
                "pesan": "Semangat terus bang menyebarkan kebaikan !!!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Tadi fotonya kebalik sama bang Razin maap ya bang, mirip soalnya ",
                "pesan": "Tetap semnagat buat jadi orang sukses bang !!!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "Aura cewek kuatnya kerasa banget ",
                "pesan": "Semangat kakak cantik untuk menjadi orang yang lebih baik !!!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Baik pake banget, ramahnya juga pake banget ",
                "pesan": "Semangat kak etaaa, semoga cepet lulusnya !!!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Cewek keren ",
                "pesan": "Semangat kak, tetap menjadi orang keren ditengah orang keren lainnya !!!"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "Judes tapi cantiknya candu ",
                "pesan": "Semangat kakak cantik, jangan lupa istirahat !!!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "Kakaknya pendiem banget ",
                "pesan": "Semangat kak, tetap hidup dengan segala yang kakak punya !!!"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kalem banget ",
                "pesan": "Tetap jadi cewek cantik yang membawa kebahagiaan buat orang lain kak !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "Judes tapu lucu ",
                "pesan": "Semangat kakak, jangan lupa bahagia hari ini !!!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Sangat inspiratif ",
                "pesan": "Semangat bang, teetap jadi orang yang memberikan pelajaran hidup buat orang lain !!!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Pertama kenal di esef, terus baik pake banget ",
                "pesan": "Semangat kakak, tetap jadi orang baik ditengah bayaknya orang baik lainnya !!!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "Gacor parah ",
                "pesan": "Semangat bang, semoga menjadi seorang pemimpin yang berhasil memimpin !!!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Pinter banget dan kalem ",
                "pesan": "Jangan lupa kasih runag buat diri sendiri bang !!!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Humble banget ",
                "pesan": "Semangat kak, tetap jadi orang yang ramah kesemua orang!!!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Inspiratif banget ",
                "pesan": "Semangat kak, jangan lupa kasih senyuman terbaik kakak hari ini !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Tadi fotonya sempet ketuker sama bnag naufal maaf ya bang ",
                "pesan": "Semangat bang, jangan lupa kasih ruang buat mengeluh ahri ini !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hZYGs5CcSnK8pe4cwFUp-Ezth-rn2LLW",
            "https://drive.google.com/uc?export=view&id=1GLz5aQdZ2TIhPAY9WvdWmzSrvSngVwC4",
            "https://drive.google.com/uc?export=view&id=1neJjFDTIN9fBkkMOM5ibZWYSfzULG5Ho",
            "https://drive.google.com/uc?export=view&id=1uFkqJdBd_BtDZLsEaeHK20uBk4X-ePir",
            "https://drive.google.com/uc?export=view&id=1CV4jcZMygheVDFH-77iiNgIGfKf7ZME_",
            "https://drive.google.com/uc?export=view&id=1-XaBWKGJP9GubUQ0_xLOWSPFSnh1iHv-",
            "https://drive.google.com/uc?export=view&id=1M_Nwj8GDSS23beJ54jg-2CzLLGdRb_fm",
            "https://drive.google.com/uc?export=view&id=1Q0QAzew2qPj4hvs3j9OBDadV8A1Sf7Vu",
            "https://drive.google.com/uc?export=view&id=1XE4EA6RuXmq4he5rje7ebQQJnacq93F2",
            "https://drive.google.com/uc?export=view&id=10RowwQZe2q03sBKUkPkgAZ7K4btMLsgf",
            "https://drive.google.com/uc?export=view&id=1rYCeymzLQkXwzRZ-9WnjAfye5D_k7nfV",
            "https://drive.google.com/uc?export=view&id=1FTCYLaV3MJOM1e1AvNKCZWcILcmhoj-0",
            "https://drive.google.com/uc?export=view&id=1TE8uwQ7zSHG6w-7EN1mUuyRGsspVPU4T",
            "https://drive.google.com/uc?export=view&id=1Gzn2gf9n3mb5Nbk0KyLpGIXli4umN6ax",
            "https://drive.google.com/uc?export=view&id=1Ug1K8T9u38ettBnd2Vtnzj9dW4rAhIsZ",
            "https://drive.google.com/uc?export=view&id=1qZ8GKEEaQUNK-knFnagPzGRqNTJZ6IYG",
            "https://drive.google.com/uc?export=view&id=1_P5pbhBxYp1pBm_-d9E4oxyLH3OSN845",
            "https://drive.google.com/uc?export=view&id=1YdABXue0clBkDwL_WTAZCCMqB9IGmpGB",
            "https://drive.google.com/uc?export=view&id=1eyliSsHeQWgc_HEBOzCzstoTeGd0kQvM",
            "https://drive.google.com/uc?export=view&id=1_qZPS04HPTpROkIydyEM_CNxk6kFNd4a",
            "https://drive.google.com/uc?export=view&id=1-7fNuyGA8w2ZVMn4rZQRDTv-k3VWX19p",
            "https://drive.google.com/uc?export=view&id=1ghu96D4Qg62HOfUHAucUJyv5e_vkiWhe",
            "https://drive.google.com/uc?export=view&id=1Z-0HQb9OItsqbhlCiMYduuw_k2AB-_i9",
            "https://drive.google.com/uc?export=view&id=1LprEvh4VKrQdH6xGhLUFEW99ByozYPle",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnya ganteng banget",
                "pesan": "Semangat bang, tetap jadi pemimpin yang baik !!!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Keliatannya jutek, tapi kalau disapa rama banget",
                "pesan": "Semangat kak, tetap ramah ya kak kalau disapa !!!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Cantik banget",
                "pesan": "Semangat kak, jangan lupa bahagia hari ini !!!"
            },
           {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Keliatannya galak banget",
                "pesan": "Terimakasih kak waktu grand opening udah dibantu bawa minumku karena aku baru dari medis !!!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kayaknya pendiem",
                "pesan": "Semangat bang, jangan capek untuk jadi orang sukses !!!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Manis banget",
                "pesan": "Semangat kak, jangan lupa untuk menebarka kebaikan hari ini !!!"
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Vibesnya kalem banget",
                "pesan": "Semangat kak, jangan lupa untuk kasih istirahat untuk diri sendiri !!!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "Cantik parah gaboong",
                "pesan": "Tetap bahagia kak apapun yang terjadi hari ini !!!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Ketuplak esef",
                "pesan": "Ditunggu acara keren selanjutnya bang !!!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "Baik banget",
                "pesan": "Semangat kak, tetap jadi orang baik !!!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "Kakak Duta, baik banget",
                "pesan": "Semangat kak, jangan capek untuk jadi orang hebat ditengah banyaknya orang hebat diluar sana !!!"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "Ramah dan baiknya gadak lawan",
                "pesan": "Jangan lupa kasih waktu untuk bahagiain diri sendiri kak !!!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Absurd banget",
                "pesan": "Semangat bang, jangan capek untuk jadi pemimpin yang baik !!!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "Cantik  banget",
                "pesan": "Jangan lupa senyum hari ini kak !!!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "Lucu banget",
                "pesan": "Jangan lupa untuk tetap bahagia hari ini kak !!!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "Vibesnya humble banget ",
                "pesan": "Semangat kuliahnya bang, bantai semuanya bang !!!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Ga bisa digambarin pakai kata-kata ",
                "pesan": "Gatau mau bukang apa, cuman mau bilang makasih banyak bang karena uda jadi orang baik, jangan capek ya bang untuk jadi orang baik, tetap jadi orang baik ditengah orang baik lainnya ya bang !!!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak Cantikk ",
                "pesan": "Terimakasih kakak udah jadi sosok kakak yang baik, tetap jadi orang humble ya kak, jangan lupa bahagia diatas segala yang kakak jalani sekarang !!!"
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Atractive abis ",
                "pesan": "Jaangan lupa bahagia kak !!!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Cantik banget ",
                "pesan": "Semangat kak, jangan lupa istirahat !!!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Cantik banget ",
                "pesan": "Jaangan lupa makan ya kak !!!"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "keren banget ",
                "pesan": "Tetap jadi orang keren kak !!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Banyak yang bilang aku mirip abang(salah satunya bang Rendra), padahal enggak ",
                "pesan": "Semangat bang, tetap jadi orang hebat !!!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "Baik pake banget ",
                "pesan": "Semangat kak, jangan lupa untuk bahagia hari ini !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Tp93V4r2y9F0XLfyzOMr4B6sv-NvCS2k",
            "https://drive.google.com/uc?export=view&id=1J6d29mUw2ES5y3h-I8Dpf_Wxrmz6wPjw",
            "https://drive.google.com/uc?export=view&id=1nNCKAXz3IY-ynFmm8cgB24FzFV58gqyr",
            "https://drive.google.com/uc?export=view&id=1l9sm6MH9Ydhrux8cdrI4TyoF95pOr6s6",
            "https://drive.google.com/uc?export=view&id=1l9sm6MH9Ydhrux8cdrI4TyoF95pOr6s6",
            "https://drive.google.com/uc?export=view&id=1FeZcF9tSerKQKf2FS0p002hVcDvxOP06",
            "https://drive.google.com/uc?export=view&id=1llQDdt8RS-FB1fdGyD_DzThnWQMuodPM",
            "https://drive.google.com/uc?export=view&id=1huC1pqCmIRgmLfDwieSApYXQFWVMb1OV",
            "https://drive.google.com/uc?export=view&id=1oGaqmXdjWObUDcMtmxz5V8DWxxdh1X7P",
            "https://drive.google.com/uc?export=view&id=1knmJEd7AGcn4ITWzwJtdHLsfCyRu7331",
            "https://drive.google.com/uc?export=view&id=1xrQ9HalpHRyztT8KvRl_z4PFerSDdXnr",
            "https://drive.google.com/uc?export=view&id=17hxz6KTJHbp-gEPGsK18cDsp9wtbJwN7",
            "https://drive.google.com/uc?export=view&id=1S9Jz0xcl4dVYQwGTf2GtVQ5av2sUFhHz",
            "https://drive.google.com/uc?export=view&id=1AMDe6d9lFqj_VdylrfV-q_vLIpK5jzoS",
            "https://drive.google.com/uc?export=view&id=1ncrzlgU19qmZ2Eyl7Pk3gKp1infZIh0I",
            "https://drive.google.com/uc?export=view&id=1PowmGLKvwhAOMyjBbCQ7qC46IyMvXzav",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Balam",
                "hobbi": "mengaji",
                "sosmed": "@ranniku",
                "kesan": "Vibensya independent woman banget ",  
                "pesan": "Tetap jadi orang kece kak !!!" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Wanita kuat ",  
                "pesan": "Semangat kakak  yang kuntuk segala yang kakak jalani sekarang !!!" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Cantik banget ",  
                "pesan": "Semangat kuliahnya kak, bahagia terus !!!" # 3
            },
            {
                "nama": "Rendy",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "Keren banget ",  
                "pesan": "Semangat bang, jangan capek untuk melayani !!!" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Humble banget ",  
                "pesan": "Tetap jadi orang humble kak !!!" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "Gacor parah ",  
                "pesan": "Semangat abang abnag batak !!!" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Cantik banget ",  
                "pesan": "Jangan lupa sneyum hari ini kak !!!" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "Keliatannya jutek, tapi ternyata ramah banget ",  
                "pesan": "Jangan lupa bahagia kak !!!" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "Lucu banget ",  
                "pesan": "Seamangat danusan bang !!!" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Vibes orang ambis ",  
                "pesan": "Semangat kuliahnya bang, jangan lupa bahagia !!!" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Asik Parah ",  
                "pesan": "Jangan capek untuk jadi orang humble bang !!!" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Baik bangett ",  
                "pesan": "Semnagat kak, jangan lupa tutor ADS nya !!!" # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "keren banget bang ",  
                "pesan": "semangat terus kuliahnya bang !!!" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "Baik sekali ",  
                "pesan": "Jangan lupa bahagia kak !!!" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Cantik banget ",  
                "pesan": "Jangan lupa bahagia kak !!!" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fR4Rzf5TT0jJs_tMO6HWQrfC_IE-keYM",
            "https://drive.google.com/uc?export=view&id=1oyEQCOq942RayWNyl1E0xZma8osY-Fqv",
            "https://drive.google.com/uc?export=view&id=191PqBnt9ap1-kj4hTEY7qg3zq3eL8B3B",
            "https://drive.google.com/uc?export=view&id=1XznuA-q3LGp5IZYZTtJIzSZvOYzHXXgM",
            "https://drive.google.com/uc?export=view&id=1dpIGNsB9cmZOFlJqJQb_laN1vh4Rxuvi",
            "https://drive.google.com/uc?export=view&id=15rMtUwJH5cxetCWK9siZRIrFNzZbgc7J",
            "https://drive.google.com/uc?export=view&id=1mDilWA_NyPTUn9EjfNh9LnvdLSE-KGkk",
            "https://drive.google.com/uc?export=view&id=13TROmF2gaw4EfseKzUQlOXb4MnPhfw9Z",
            "https://drive.google.com/uc?export=view&id=1LOD56Zx5-Iss_IlxHQOA38GrghWU_-Js",
            "https://drive.google.com/uc?export=view&id=1aZEL8TCl4PuL83zwN5AAGRJTRsxDx6x1",
            "https://drive.google.com/uc?export=view&id=1XoKxrBOhLa0bdf_uStDFOz_eGATUhTXv",
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
                "kesan": "Ketuaaa ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel", 
                "sosmed": "@syalaishaa_31",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
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
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jati Mulyo",
                "hobbi": "sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 14
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()











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
            "https://drive.google.com/uc?export=view&id=1facqC5h5O0K4zmoXXsay0U-HlqWzqMb6",
            "https://drive.google.com/uc?export=view&id=1gGAQ6Wkw0I-XMBdPZ7GLIE0XQOJVPKAk",
            "https://drive.google.com/uc?export=view&id=1RLGL--fisT7O42uaF8-BicEvVtysL7UU",
            "https://drive.google.com/uc?export=view&id=119hABbvcr2QFIahM2KGPm88P8qw4pNRM",
            "https://drive.google.com/uc?export=view&id=1G7tT1YYHvWeZNXISvxnRc3hy3zjXc6Do",
            "https://drive.google.com/uc?export=view&id=1_M3yFRQWlTgGmdqhJ1Ih8RKt2AfJg1Fk",
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
                "kesan": "Bang Rendra keren banget, jago bikin lagu!",
                "pesan": "Semangat terus kuliahnya Bang!!!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Johannes suka banget baca dan rajin belajar SQL!",
                "pesan": "Terus semangat eksplor data dan kodingnya Bang!"
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Elisabeth lucu dan asik banget diajak ngobrol!",
                "pesan": "Jangan lupa istirahat dan tetap semangat ya kak Elisabeth!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza tenang tapi cerdas banget!",
                "pesan": "Tetap semangat kak Syadza!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty ramah banget dan suka cerita hal lucu!",
                "pesan": "Tetap jadi kakak yang ceria dan positif ya!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak Farahanum seru banget dan inspiratif!",
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qhqxoUyqFCnmn5MjrOga9CWmrxlg2pa1",
            "https://drive.google.com/uc?export=view&id=1nhG44Yf9LG6VjhLDdbx_lIvF4a1AvVOB",
            "https://drive.google.com/uc?export=view&id=17kz08pPVu15mOGiivNKmfNjhcE8GmjN1",
            "https://drive.google.com/uc?export=view&id=1v5UrXOuduIvxBnl3c1vAVBxLQvcdKEuk",
            "https://drive.google.com/uc?export=view&id=1Kh0s6LTRqOtIi7CWI7gsrn6gcu4SD6EJ",
            "https://drive.google.com/uc?export=view&id=12jJeWep97P9yYbH8AyW1S_dAPMOt6DJx",
            "https://drive.google.com/uc?export=view&id=1nUm3APcMLftKwS6gX3IcALPoTHMbEXdS",
            "https://drive.google.com/uc?export=view&id=1H7Wqg0mx5oOjdSMmYcyzpp11FhegUyVX",
            "https://drive.google.com/uc?export=view&id=1wMaJ6_UZ705wPHCLJe6iVLhFccaWP7NH",
            "https://drive.google.com/uc?export=view&id=15OexmIE_UaVggDMXxUHUlYRv0L3Ekzl1",
            "https://drive.google.com/uc?export=view&id=13z9ggaL_OUgevBYYtwtAzULY6pJe53pj",
            "https://drive.google.com/uc?export=view&id=17xWlh1Knxhqpjk2LapYj_2lQ9esbZiAR",
            "https://drive.google.com/uc?export=view&id=1XszkR-kyXo8qHaCZP3gi04UkOmGqSVbZ",
            "https://drive.google.com/uc?export=view&id=1Tqd46sxxISB17qcpIbybUJwJaVQuJplA",
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
# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1n7-mkDuBFJXIDyq-ZX4FFbLOgj1CmM3n",
            "https://drive.google.com/uc?export=view&id=1xFIgU9ZvNb5qQJt3ebzjQWF14wyZFRAU",
            "https://drive.google.com/uc?export=view&id=1LN4Hvl-Mj5LetNQvMPgMhS1fpQtfYB4c",
            "https://drive.google.com/uc?export=view&id=1IK3Uelukq9rie1KAh4W4aueypgBdJvAe",  
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
            "https://drive.google.com/uc?export=view&id=1LkQJS59AWj9VVByUfgdu98gcNw7rErrl",
            "https://drive.google.com/uc?export=view&id=1LfuxAxo010d2VhVaFPyIomuM5v8EXMQI",
            "https://drive.google.com/uc?export=view&id=11qDgBpalYLz3Issrd8Ia6rK_QUZxwujC",
            "https://drive.google.com/uc?export=view&id=1bmlSCJ23nehU5qPcmWUTZ9v_LNWFK4st",
            "https://drive.google.com/uc?export=view&id=1_Ddpau2_klP8bLZXLHV-wnQZfWRurwVW",
            "https://drive.google.com/uc?export=view&id=1P7LrgnqKCUDC1FW2O4tHYgGiGzUVDSrO",
            "https://drive.google.com/uc?export=view&id=1rXNiyCow51vZQdANkLXndyYxGrnhu2GW",
            "https://drive.google.com/uc?export=view&id=1Ha5d73L0_3ahDrB8-qiFe1Ds_lfbxRPI",
            "https://drive.google.com/uc?export=view&id=1pWQRF6-mVKNo-FTSlWH4oHL0bHaZFcYJ",
            "https://drive.google.com/uc?export=view&id=1gH7yueO8uRBKgSkxJ917hHuAduz4_ISj",
            "https://drive.google.com/uc?export=view&id=1IHVd904V4L2jHj0tTXbfuRLsGp21NSxx",
            "https://drive.google.com/uc?export=view&id=1X44xsX6-lNyy59tJdqglMHsV-Gdw-1R3",
            "https://drive.google.com/uc?export=view&id=1ejBCHVisZcgXbKxaDO9KuVEZcv0z7EIl",
            "https://drive.google.com/uc?export=view&id=1qKt9dcaVPjJJ54Q6ABvUMXcURMycUrVL",
            "https://drive.google.com/uc?export=view&id=1YPdKO0-eAZCIDHZhxAe1nBwgYD_Lkh3v",
            "https://drive.google.com/uc?export=view&id=1DbqQ-HDrIvEUysY2eQzQDKRkp73v3Ih-",
            "https://drive.google.com/uc?export=view&id=1KhtioBE0BjpamL22j6il0GGaacV9eMXb",
            "https://drive.google.com/uc?export=view&id=1vgfR2NSEICq3NgjlsJ4id9pSNHCNs2ML",
            "https://drive.google.com/uc?export=view&id=1bXdUBYF_xz5jbyi-CglPMxIwc8cL82fP",
            "https://drive.google.com/uc?export=view&id=1u3-VfELMy56dYIIdeVRYT-WOyCbb6v1T",
            "https://drive.google.com/uc?export=view&id=1snqwcOEblkC1--MdaEIe15soqVpU3wY8",
            "https://drive.google.com/uc?export=view&id=14c-T_Vqy9a3bX_a2imk0UjeGk4gm3ywn",
            "https://drive.google.com/uc?export=view&id=1WULtL3ZRQEtx5luINvESPdcKJfkcYjsT",
            "https://drive.google.com/uc?export=view&id=1pRb1_eCeWRnMrB5tJArgKKuf0FFZbalG",
            "https://drive.google.com/uc?export=view&id=1lXXqBE4CvB6Zo8f0KQX_ZO46Db-aWATi",
            "https://drive.google.com/uc?export=view&id=19mpv97nPR44kyZSIy89sSp0RXuVlU4rL",
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

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jAVdlfmm12DIFckvs4PokQkecWAw9qSp",
            "https://drive.google.com/uc?export=view&id=1RAHwvpecJJspPZjgn4msSXv1_T47EU8e",
            "https://drive.google.com/uc?export=view&id=18Td4iK394lvYXbbo-WK6n6cksYImJrdF",
            "https://drive.google.com/uc?export=view&id=1syspzcHOhE8Ww678RFbSc76TVz1FZz0Z",
            "https://drive.google.com/uc?export=view&id=1YmjEM--EKbR2KnX7q3b5m7nB7TNE0qbl",
            "https://drive.google.com/uc?export=view&id=17GYo5epfFmzKkEJ2DRcePvvM2Cr8Yi2g",
            "https://drive.google.com/uc?export=view&id=1YrEOIZPDBQ8PDM8A3Gf_Q-2PEej2Ytrp",
            "https://drive.google.com/uc?export=view&id=1JfX9ll-no69RUf8Biw66R14jqg7piQG6",
            "https://drive.google.com/uc?export=view&id=1BeB_N11GIjW7J1Yvi4yFy0QqhMnDIxHC",
            "https://drive.google.com/uc?export=view&id=1tG9aqFxCH0s0d7m4UNsCNN295R30Zf-w",
            "https://drive.google.com/uc?export=view&id=1voLDkdBfm5yM9kFK6WE2dx_xg9eSdZ9m",
            "https://drive.google.com/uc?export=view&id=11Jln63Y8oM60PdsqVZ8GyLNaBCWr7UyI",
            "https://drive.google.com/uc?export=view&id=1KbtEvusWJDqZVFNyFCwGVixpZI2a07G-",
            "https://drive.google.com/uc?export=view&id=1VeDxo-1ET3dWUZwoLi1wOmvoBhWMx39G",
            "https://drive.google.com/uc?export=view&id=1vL73e11IGP6EzyE8gWqKpFlr0Xq3NgEW",
            "https://drive.google.com/uc?export=view&id=16U0GBErS6m0KxgZ3lB7R5d08y_4fO03a",
            "https://drive.google.com/uc?export=view&id=1Z0YiiX5WsasuGoTvoxpIqDWVlqPeAC1Q",
            "https://drive.google.com/uc?export=view&id=1diIA_arm1_09eYjP93dsfbMZBaJ_iS8V",
            "https://drive.google.com/uc?export=view&id=1rKPM6Mze4OiYXnX0T8XpesfxLZivD-zw",
            "https://drive.google.com/uc?export=view&id=1V0VCBXz4eBtaIxxea8dAem_c-garoVgT",
            "https://drive.google.com/uc?export=view&id=1IvnPq4QpQIsR2ZGnoDr5OeuT7Of9VD0W",
            "https://drive.google.com/uc?export=view&id=1SS5wU-ZM4apUbwBthJn0-ZpW4C--_mcQ",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya seru banget",
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak rut asik diajak ngobrol",
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "124450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya seru dan mudah diajak ngobrol.",
                "pesan": "Semoga Abang semakin sukses dan tetap rendah hati."
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya lembut dan sopan dalam berbicara.",
                "pesan": "Semoga Kak terus bersemangat dan selalu bahagia."
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Abangnya ramah dan mudah membuat suasana jadi menyenangkan.",
                "pesan": "Semoga Abang selalu diberi semangat dan rezeki yang lancar."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya aktif dan seru ketika ngobrol.",
                "pesan": "Semoga Abang selalu sehat dan sukses ke depannya."
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya tenang dan memiliki pemikiran yang matang.",
                "pesan": "Semoga Abang terus menjadi pribadi yang inspiratif."
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakaknya ceria dan membawa suasana positif.",
                "pesan": "Semoga Kak terus bahagia dan dikelilingi hal-hal baik."
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya sopan dan menyenangkan diajak berdiskusi.",
                "pesan": "Semoga Kak selalu diberi kemudahan dalam setiap urusan."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya seru dan mudah beradaptasi.",
                "pesan": "Semoga Abang selalu bersemangat dan percaya diri."
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya energik dan selalu bersemangat.",
                "pesan": "Semoga Kak terus menebarkan energi positif."
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya bijak dan suka membantu.",
                "pesan": "Semoga Kak selalu diberi kesehatan dan kebahagiaan."
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakaknya tenang dan menyenangkan.",
                "pesan": "Semoga Kak selalu semangat menjalani hari-hari."
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "124450081",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450022",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "-",
                "kesan": "Abangnya tenang dan selalu terlihat santai.",
                "pesan": "Semoga Abang selalu sehat dan semangat menjalani kuliah."
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya ceria dan menyenangkan.",
                "pesan": "Semoga Kak selalu membawa keceriaan di mana pun berada."
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "Abangnya sopan dan mudah diajak bicara.",
                "pesan": "Semoga Abang selalu diberi kemudahan dalam segala urusan."
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya tenang dan berwawasan luas.",
                "pesan": "Semoga Abang terus berprestasi dan sukses selalu."
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakaknya lembut dan sopan berbicara.",
                "pesan": "Semoga Kak selalu sukses dan diberi kebahagiaan."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "-",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya humoris dan mudah akrab dengan teman.",
                "pesan": "Semoga Kak selalu ceria dan semangat terus."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya seru dan asik diajak ngobrol.",
                "pesan": "Semoga Abang selalu diberi kesehatan dan kesuksesan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    MIKFES()
elif menu == "Departemen Eksternal":
    def EKSTERNAL():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HHDQNF6__W37ypJlNNEJTiumvvBrBAK0",
            "https://drive.google.com/uc?export=view&id=1VQ6BSnxa6hnFHHJD68qV7xiRhOw7dovV",
            "https://drive.google.com/uc?export=view&id=19oeroEpzDOeJtjqAzTBfyumRbhDxAaty",
            "https://drive.google.com/uc?export=view&id=1-6NojrXPL_ustlWgkCzfagaw_tCxBUcR",
            "https://drive.google.com/uc?export=view&id=1dz0ATA7ROCLcy0K-PPlJ3xPjx5ihxvFn",
            "https://drive.google.com/uc?export=view&id=1dUfAoY6XBFHB2BQGX0aditpzA_zWStHP",
            "https://drive.google.com/uc?export=view&id=14O5DsKrm52ok7S_1Xj1Jl8q3Tfkj7yW6",
            "https://drive.google.com/uc?export=view&id=1Y-ALUAZFbzFl1yO2awdun4-RTiJu7Cst",
            "https://drive.google.com/uc?export=view&id=1Nwsz5BUYEdsBEtKpQDo4-adgGPyNGX25",
            "https://drive.google.com/uc?export=view&id=1kN5cbGhVNX2HbHlbGlBZT2Uqrgzq653q",
            "https://drive.google.com/uc?export=view&id=1Em_HyfHSdAKImezrcC_21__HRYdE7QDz",
            "https://drive.google.com/uc?export=view&id=1KuXqgT-JCfefmvP9zzjL14w1GhNWWQB-",
            "https://drive.google.com/uc?export=view&id=1lKKmqrAQA7jJ5I60YFSTHgGGEUyHmfnM",
            "https://drive.google.com/uc?export=view&id=19AOB2R62fcYabIF6NAzrLyCJxWqV-qD5",
            "https://drive.google.com/uc?export=view&id=1EKFR4ZJyfhZiEFMiih0-pSksKGXDmZ1O",
            "https://drive.google.com/uc?export=view&id=1Ko1rHCjz01ZiAufcchR6oSjLnU9HTyZd",
            "https://drive.google.com/uc?export=view&id=1pE153fc58gBzQPnCOFMMoii3FtAdylaD",
            "https://drive.google.com/uc?export=view&id=1wPROd8u_b-SP7aZEqIeu9-hCiT-DpQvu",
            "https://drive.google.com/uc?export=view&id=1Mz17kk0_7ODQxh6neHLm2Nlz5oshYxQ4",
            "https://drive.google.com/uc?export=view&id=1WekldABpGCTopJgvlWKMliCS5e7zQPs3",
            "https://drive.google.com/uc?export=view&id=1CVJGWvMLYYp_nmCIDiS04xhyWfncyg1Y",
            "https://drive.google.com/uc?export=view&id=1uCW6YfM9IKQB5c1yvcrChTgdqPjP6r0Z",
            "https://drive.google.com/uc?export=view&id=14yEGMh4sb6hFOpSZDUx-a8XtfOfNO-_p",
            "https://drive.google.com/uc?export=view&id=1KiJlCMbef3T6O1wSBm2qIZ9_jDMMo_8s",
            
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
                "kesan": "Bang Arafi punya seru dan selalu bikin suasana cair!",
                "pesan": "Terus tebarkan semangat dan tawa di setiap kegiatan ya kak, tetap semangat bang!"
              },
              {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana seru banget!",
                "pesan": "Tetap semangat dan terus tingkatkan rasa ingin tahunya ya kak!"
              },
              {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva, follow @cerebral.id_",
                "kesan": "Kak Mine keren bangett!",
                "pesan": "Tetap semangat dan terus menginspirasi ya kak!"
              },
              {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini ramah dan seruu!",
                "pesan": "Semoga impian keliling dunia tercapai ya kak wkwkwkwk!"
              },
              {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Bang Arya kalem tapi seru!",
                "pesan": "Jangan kebanyakan ngelamun bang, dunia nyata nungguin wkwkwkw!"
              },
              {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main-main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kak Mut ceria dan seru bangett!",
                "pesan": "Terus tebarkan keceriaan ya kak Mut dan tetap semangatt!"
              },
              {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia pinter banget dan suka eksplor hal baru!",
                "pesan": "Semoga makin jago di dunia data ya kak!"
              },
              {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla ceria dan suka banget jalan-jalan bareng temen!",
                "pesan": "Tetap jadi sosok yang fun dan bersemangat ya kak!"
              },
              {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Bang aldi seru dan suka belajar hal baru!",
                "pesan": "Terus asah kemampuan dan semangat belajarnya bang!"
              },
              {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea chill banget!",
                "pesan": "Tetap semangat kakk!"
              },
              {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam Naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak Cindy seru dan selalu ceria!",
                "pesan": "Jangan lupa traktir risol ayamnya ya kak hehehe!"
              },
              {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton reels Agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea lucu banget dan punya vibes positif dan pastinya seru banget!",
                "pesan": "Tetap jadi moodbooster bagi sekelilingmu ya kak dan tetap semangat!"
              },
              {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman jago musik dan keren banget!",
                "pesan": "Terus berkarya dan jangan berhenti bermusik ya bang!"
              },
              {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya seru banget dan suka bercanda!",
                "pesan": "Tetap ceria dan terus tebarkan tawa ya kak!"
              },
              {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kak Lulu seru banget dan selalu bikin suasana hidup!",
                "pesan": "Tetap jadi pribadi yang penuh energi positif ya kak!"
              },
              {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Bang Irvan keren, seru dan inspiratif banget!",
                "pesan": "Terus semangat memimpin dan jadi contoh yang baik bang!"
              },
              {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Bang Adit gokil, seru bangett!",
                "pesan": "Ajak ajak bang kalo nemu tempat keren, tetap semangat bang!"
              },
              {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya lucu banget dan humble!",
                "pesan": "Tetep jadi moodboster kak dan tetap semangat!"
              },
              {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla kalem banget tapi seruu!",
                "pesan": "Nikmati setiap waktu me timenya kak, tetap semangat kak!"
              },
              {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melin easygoing dan suka banget film!",
                "pesan": "apa tuh film favoritnya kak? tetap semangat ya kak!"
              },
              {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Ilmi asik banget diajak ngobrol dan santai!",
                "pesan": "Terus jadi pribadi yang menyenangkan dan ceria ya kak!"
              },
              {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak Izzah seru banget!",
                "pesan": "Boleh bagi bagi ga kak hasil bakingnya wkwkw!"
              },
              {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois seru dan suka jalan-jalan!",
                "pesan": "Tetap semangat bang!"
              },
              {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajahi desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kak Tarisya punya jiwa sosial tinggi dan seru banget!",
                "pesan": "Terus semangat berkontribusi dan menjelajah desa ya kak,ajak ajak sabi kali wkwkwk!"
              },
        ]
        display_images_with_data(gambar_urls, data_list)
    EKSTERNAL()
    
elif menu == "Departemen Internal":
    def INTERNAL():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Yh7K_9QSko0B1zFNPNdYeFHt68TahrrA",
            "https://drive.google.com/uc?export=view&id=1LzGJQUdGZh61j5cWizTtu5BQDqVqv0Y_",
            "https://drive.google.com/uc?export=view&id=1Ln2oCcrxxXtXpDplDy5_8opOY1dSGloq",
            "https://drive.google.com/uc?export=view&id=1LX9Z6aDYP4BrFJvhoBi-gVqeKhk2KPQT",
            "https://drive.google.com/uc?export=view&id=1LTeq8BjMD4ySmoOJUzeFtGemFwtLd80S",
            "https://drive.google.com/uc?export=view&id=1LQZZZPFkxsjx4eiWrDpN3Vya0SsB9PgT",
            "https://drive.google.com/uc?export=view&id=1LOFKTJNStJSf6FX_aNL46ZYxS1jQkn6o",
            "https://drive.google.com/uc?export=view&id=1L1Mo3SQax92wDvQ8AYC7gSZfhvFwanok",
            "https://drive.google.com/uc?export=view&id=1KkFhQQtAxzHb_AThhUwk30SJaT9JUec9",
            "https://drive.google.com/uc?export=view&id=1KrZ0QrXTw6QRADMMSxQ7JqvDI0LJx0sh",
            "https://drive.google.com/uc?export=view&id=1Lzf3ggcfzoUeLr5tpkQ2KJSMnFy_MXgK",
            "https://drive.google.com/uc?export=view&id=1LmjVdm5K2Krn8mPTW8Jdvg2fJUVCPHiG",
            "https://drive.google.com/uc?export=view&id=1Kx2pNfE8JbzBTULKQtEXpOzsqpmT86WS",
            "https://drive.google.com/uc?export=view&id=1Lle8_T5o6QZ9kUTthj-YuY5sFw2one6q",
            "https://drive.google.com/uc?export=view&id=1LfbNb6kBcxRMSb8XI4m1IsrpUmtxDmNq",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": 21,
                "asal": "Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "instagram": "@ranniku",
                "kesan": "Kak Rani orangnya lembut dan bijaksana.",
                "pesan": "Semoga selalu diberi kesehatan dan keberkahan dalam setiap langkah."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": 22,
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "instagram": "@renta.shn",
                "kesan": "Kak Renta orangnya tenang dan sopan.",
                "pesan": "Semoga selalu diberi kesabaran dan rezeki yang lancar."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": 21,
                "asal": "Brebes, Jateng",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "instagram": "@salwa.fhn",
                "kesan": "Kak Salwa lembut dan ramah banget.",
                "pesan": "Semoga selalu bahagia dan sukses terus ya Kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": 21,
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "instagram": "@reaxender",
                "kesan": "Bang Rendi suaranya keren dan berkarisma.",
                "pesan": "Semoga terus semangat berkarya dan tetap rendah hati bang!"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": 19,
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "instagram": "@zailanisatria",
                "kesan": "bang Zai aktif dan seru banget.",
                "pesan": "Semoga tetap semangat bang!"
            },
            {
                "nama": "M. Naufal Algahni",
                "nim": "123450116",
                "umur": 20,
                "asal": "Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "instagram": "@muhammadnaufalalghani",
                "kesan": "Bang Naufal asik diajak ngobrol.",
                "pesan": "Semoga makin sukses dan tetap rendah hati!"
            },
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450106",
                "umur": 18,
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "instagram": "@haikalsbln_",
                "kesan": "Bang Haikal seru dan keren banget.",
                "pesan": "Semoga selalu membawa keceriaan di setiap suasana!"
            },
            {
                "nama": "M. Hanif Zaki",
                "nim": "123450004",
                "umur": 20,
                "asal": "Padang",
                "alamat": "Perumnas, Way Kandis",
                "hobi": "Futsal",
                "instagram": "@hnfdzky_",
                "kesan": "Bang Hanif orangnya sopan dan kalem.",
                "pesan": "Semoga selalu diberkahi kesuksesan di setiap langkah!"
            },
            {
                "nama": "Sarah Warti",
                "nim": "123450057",
                "umur": 20,
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "instagram": "@sarahwrti",
                "kesan": "Kak Sarah anggun dan ramah.",
                "pesan": "Semoga selalu bahagia dan sukses di setiap perjalanan!"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": 19,
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "instagram": "@kerenmrtv",
                "kesan": "Kak Keren sesuai namanya, keren banget!",
                "pesan": "Semoga terus berprestasi dan menginspirasi banyak orang."
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": 19,
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "instagram": "@zhrptsr",
                "kesan": "Kak Zahra orangnya lembut dan sopan.",
                "pesan": "Semoga selalu semangat dan penuh kebahagiaan!"
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": 20,
                "asal": "Pekan Baru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "instagram": "@azzah.raaa_",
                "kesan": "Kak Azzahra punya aura positif banget.",
                "pesan": "Semoga selalu ceria dan makin sukses!"
            },
            {
                "nama": "May Thalita Dehlia",
                "nim": "123450009",
                "umur": 20,
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "instagram": "@may_dahlia12",
                "kesan": "Kak May selalu tampil cerah dan ramah.",
                "pesan": "Semoga terus jadi inspirasi bagi yang lain!"
            },
            {
                "nama": "Iqfinah Haula Halika",
                "nim": "123450076",
                "umur": 20,
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "instagram": "iqfinanhalikaa_",
                "kesan": "Kak Iqfinah imut dan kreatif banget.",
                "pesan": "Semoga semua impian Kakak bisa terwujud!"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": 20,
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "instagram": "@hanna_g_sinaga",
                "kesan": "Kak Hanna lucu dan supel.",
                "pesan": "Semoga terus membawa suasana ceria dan positif ke sekeliling!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    INTERNAL()
# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1M8m7cZeBTtWOekmDr9gQm7kRjRBAnFNE",
            "https://drive.google.com/uc?export=view&id=1M8zOl5dJqa1VRF89FYvlpXsc8IvKXj8w",
            "https://drive.google.com/uc?export=view&id=1MZPM6k9aLhmdP8kZ84gmfWzYUxdlP56d",
            "https://drive.google.com/uc?export=view&id=1MJwVB_U8OHxGINWZqKWGvwc0wZ2RAAFj",
            "https://drive.google.com/uc?export=view&id=1MP5l32xRGdrTDo-4JHvaqsmKujtPATww",
            "https://drive.google.com/uc?export=view&id=1MJ6-OqbWNsaiSuKnAHjBifbXbShF8hF_",
            "https://drive.google.com/uc?export=view&id=1MQt3dVhKZE_QxhZH5R2J-YBwJNAMDdzv",
            "https://drive.google.com/uc?export=view&id=1MJIpFK1cSzjR7QebnQLVxXICVvh9LEYX",
            "https://drive.google.com/uc?export=view&id=1YjfddCDdQAulUVejbCuapFQQ-PvLxAD5",
            "https://drive.google.com/uc?export=view&id=1MBZ9SOE9Bq_TLJ1E924ciuD7uV-8qRm3",
            "https://drive.google.com/uc?export=view&id=1MCvi4yMsRuhq2jagX_dLq8oG3GxNMqge",
        ]   
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@dananghk_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@syalaishaa_31",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@den_iki_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@anadiacrn_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@aprhtp_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@nabila_zazahra",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@dhafinrzqa13",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@deviirhyu",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@englirahmdhanii",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@_inayasari",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "instagram": "@nydiaaptr_",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

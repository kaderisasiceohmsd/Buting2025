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
            "https://drive.google.com/uc?export=view&id=1jadXsjq0zJJAJmA85zhkLE8c3mwBcmMe",
            "https://drive.google.com/uc?export=view&id=1eOntUFVQCxg3NEbmuGBC1YhpglyTSRap",
            "https://drive.google.com/uc?export=view&id=1rbyoJFqzvjdL6ILCNnPwSJGAPa1h2vAQ",
            "https://drive.google.com/uc?export=view&id=1VxYVZCRT9B3AAeuunwe1CN0j6ueZEpqm",
            "https://drive.google.com/uc?export=view&id=1Ii1bkzNvdvD97Qb7uj5fjm2-gZ4uw5uJ",
            "https://drive.google.com/uc?export=view&id=1yyKjX3kex6aydASrqFKDVcATnAeIBvdT"
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "keren banget bisa pegang posisi penting bangg",  
                "pesan":"Semangat terus bangg, semoga HMSD semakin jayaa!!!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "baca buku (dasar-dasar sql)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Ramah banget, gampang diajak ngobrol.",  
                "pesan":"Semoga kehidupan kuliahnya berjalan lancar bang"
            },
             {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19x    `",
                "asal":"Tanggerang",
                "alamat": "Airest Kost",
                "hobbi": "siram shopee",
                "sosmed": "@celisabethh_",
                "kesan": "Hobbynya ngawur, tapi megang posisi penting",  
                "pesan":"Semoga lancar kehidupan kuliahnya"
            },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Udah hobi membaca, punya posisi penting pula",  
                "pesan":"Semoga lancar-lancar saja kehidupannya"
            },
              {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTTi",
                "alamat": "rajabasa",
                "hobbi": "baca buku , saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Walau hobbynya ngawur, tapi bisa berada di posisi penting haha",  
                "pesan":"Semoga tidak ada masalah yang menghampiri"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"kota Padang,Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Bisa ada diposisi ini aja udah keren banget",  
                "pesan":"Semoga ga banyak masalah menghampiri"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y7m-Sr8LIFIepfzCLHdiU1ON3UDK4tEx",
            "https://drive.google.com/uc?export=view&id=1qX0d5wzq1VSg6JBtkh_xAmhSWJwXTI9G",
            "https://drive.google.com/uc?export=view&id=1MAs68fTCWheFxmOqMAVqK4oIcrNzwVkg",
            "https://drive.google.com/uc?export=view&id=19G2sffqer1LENuojEglhaNRzFdb4WvXW",
            "https://drive.google.com/uc?export=view&id=1fQHJ6-1E_1J0d6kyQD9ytUyLop9Ahdiw",
            "https://drive.google.com/uc?export=view&id=1qkEiJiBku7pxtniRpV-HZnf8DeI7a1G5",
            "https://drive.google.com/uc?export=view&id=1vGV3RT_SCxcFliMXP3J4fL26tSiAb3K9",
            "https://drive.google.com/uc?export=view&id=1NB5G6DK152RZVIqbhRFLMV2sFY_xQFJ6",
            "https://drive.google.com/uc?export=view&id=1vYv5bR6s2DBWCTKo-M5sKD05iJ-xxxx3",
            "https://drive.google.com/uc?export=view&id=1a5_AnTo9fB8t3kCfJqELCWNTVrwIyKiC",
            "https://drive.google.com/uc?export=view&id=1eaGb9hhCR-S1yw43Beb5cSU2bTUlyaHs",
            "https://drive.google.com/uc?export=view&id=15VUs1hcvBOe1dEZFOtdH9fBvj4EFuJ6G",
            "https://drive.google.com/uc?export=view&id=1iTAqkaIv_P6xY2z69SagVlrvdWJhSgiV",
            "https://drive.google.com/uc?export=view&id=1FuwEBGx2ETAOAr2NV4VciRmHJHhFOhv2"
        ]
        data_list = [
           {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "B2 , NO 2",
                "hobbi": "Zumba di pln setiap jumat pagi",
                "sosmed": "@jeremia.s",
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto, Jawa Timur",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "Senang bisa kenal dengan kakak.",
                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Muara Enim, Sumatera Selatan",
                "alamat": "C2",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Semangat terus dan jangan mudah menyerah!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Semoga kita bisa bertemu lagi."
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bangka Belitung",
                "alamat": "Kobam",
                "hobbi": "Nongkrong di gedung f",
                "sosmed": "@fer_yulius",
                "kesan": "Sangat berkesan, orangnya humble.",
                "pesan":"Tetap jadi pribadi yang menginspirasi!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan pancing",
                "sosmed": "@Renishapg",
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way halim",
                "hobbi": "Bengong",
                "sosmed": "@dhruchyo",
                "kesan": "Senang bisa kenal dengan kakak.",
                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way huwi",
                "hobbi": "Menggodai Abang Cimol",
                "sosmed": "@fby.wlndr",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Semangat terus dan jangan mudah menyerah!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@givarooo",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Semoga kita bisa bertemu lagi."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "Mengukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Sangat berkesan, orangnya humble.",
                "pesan":"Tetap jadi pribadi yang menginspirasi!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Kalimantan Utara",
                "alamat": "Belwis",
                "hobbi": "Sibuk",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Gang Sakung",
                "hobbi": "Main  PadelX    ",
                "sosmed": "@iamridhomanik",
                "kesan": "Senang bisa kenal dengan kakak.",
                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Ketapang, Kalimantan Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Semangat terus dan jangan mudah menyerah!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekan Baru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Semoga kita bisa bertemu lagi."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X1NTJtTCq5uRLo-C6UO1HAl3aXrKDdSa",
            "https://drive.google.com/uc?export=view&id=1C0QJ78RYQNbGe08EA5Yes09mnmPDERSl",
            "https://drive.google.com/uc?export=view&id=1B4-nVlQRbeLZ7mFqtU2-T0SODaZowSET",
            "https://drive.google.com/uc?export=view&id=1mx9OkDIxjtR73GazpmnxOsUNCLn_Tri8"
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "tanya caesar",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XsoNYeZqAuuLv7I3xqFCtEZs25P3SL8G",
            "https://drive.google.com/uc?export=view&id=1iH5EkdMSTs0LapVGlGk8vgH-vRqA4ZAM",
            "https://drive.google.com/uc?export=view&id=1aFMjWAwB3ZVYO3DHM3BIjNocqTFxuRSC",
            "https://drive.google.com/uc?export=view&id=1wp9M31pVhnc0aXfE2p5i6jtYGYfaCyob",
            "https://drive.google.com/uc?export=view&id=1CqaPKOwCNXWN9i8HBCa7J_NaDcqx-6-3",
            "https://drive.google.com/uc?export=view&id=1iE-Fag6-IjJ4_GRvyHBXf_F6957WaHuo",
            "https://drive.google.com/uc?export=view&id=1GmvEQ-YumFPOFzf-3wAcx_mLj3aweyJo",
            "https://drive.google.com/uc?export=view&id=1TLd0s3X3pQwBZhwWSc11sxNmBu00LCwo",
            "https://drive.google.com/uc?export=view&id=1ijOZw29mvlBE_7j9bd73yikVMO-TxQov",
            "https://drive.google.com/uc?export=view&id=1SVfUDcDdBZm-0IUbxFNpESkU2M_eNPvw",
            "https://drive.google.com/uc?export=view&id=1k09ALkTf_9zOQWrhu6A3Z1h5LdHPqjcr",
            "https://drive.google.com/uc?export=view&id=1BOu6sjo_xrZtUKEeHEnlYaupEnXh4u1T",
            "https://drive.google.com/uc?export=view&id=1juvMn1t3SD77w9Vx6FTlysJBa5EXqxUb",
            "https://drive.google.com/uc?export=view&id=1Km6l8bfJwglbuLP3JGsdh-p-iUzJrAmj",
            "https://drive.google.com/uc?export=view&id=1CRqEzqKirGWBPx7DCU4e6Kag72YG15Rt",
            "https://drive.google.com/uc?export=view&id=1RUsJ2sNsKAfIma4xIEZTOEsmDaYWQ5qX",
            "https://drive.google.com/uc?export=view&id=17Iz37I-aBzNBN6siHCrSuVNA2ZB_7gZB",
            "https://drive.google.com/uc?export=view&id=1HgLihs0uUEaEKkd5YrqxhTgdcTkZn8lA",
            "https://drive.google.com/uc?export=view&id=1QrcoAX4X2TriX2SuYTSX3WhnanSpm_rB",
            "https://drive.google.com/uc?export=view&id=1KmN9AWql2tVt--AH9ldoj5jIxLPRkXQp",
            "https://drive.google.com/uc?export=view&id=1n3OGtqwwXX9x6uVHgFb51FSr5H6oxkH6",
            "https://drive.google.com/uc?export=view&id=18rShJldXUAksJJtD9LHF77m3SltSfM1e",
            "https://drive.google.com/uc?export=view&id=1HM9vEmCuw3ZTkiqkqwN8vnp_TsDBxbSO",
            "https://drive.google.com/uc?export=view&id=1Xh1MB3zguA8YSKaeg203xwA0I37mW8ZL",
            "https://drive.google.com/uc?export=view&id=1PrxhmIhBM3c4TgjrH3ohSK0oT0aiY8Z6",
            "https://drive.google.com/uc?export=view&id=18Nr8BiTVYUlA84XHicuho4V9yBtndZBV"
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Kakak sangat berwibawa dan mengayomi.",
                "pesan": "Mohon bimbingannya selalu, Kak. Sehat dan sukses terus!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Terima kasih atas bimbingannya selama ini, Kak.",
                "pesan": "Semoga kami bisa meneladani semangat kakak."
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Sikapnya tegas dan disiplin, menjadi panutan bagi kami.",
                "pesan": "Terima kasih atas ilmunya, semoga kakak sehat selalu."
            },
             {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Senang mendapat arahan dari kakak, sangat memotivasi.",
                "pesan": "Semangat terus dalam menjalankan amanahnya, Kak!"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Pembawaannya tenang dan bijaksana.",
                "pesan": "Sukses selalu untuk kakak, ditunggu arahan selanjutnya."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Kakak sangat berwibawa dan mengayomi.",
                "pesan": "Mohon bimbingannya selalu, Kak. Sehat dan sukses terus!"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Terima kasih atas bimbingannya selama ini, Kak.",
                "pesan": "Semoga kami bisa meneladani semangat kakak."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Sikapnya tegas dan disiplin, menjadi panutan bagi kami.",
                "pesan": "Terima kasih atas ilmunya, semoga kakak sehat selalu."
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Senang mendapat arahan dari kakak, sangat memotivasi.",
                "pesan": "Semangat terus dalam menjalankan amanahnya, Kak!"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Pembawaannya tenang dan bijaksana.",
                "pesan": "Sukses selalu untuk kakak, ditunggu arahan selanjutnya."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak sangat berwibawa dan mengayomi.",
                "pesan": "Mohon bimbingannya selalu, Kak. Sehat dan sukses terus!"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

# MIKFES
if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-Y4ozSnSR54NeVQ-yL8QNMhleexNUjgp",
            "https://drive.google.com/uc?export=view&id=1-Q83_-aScxMmKi3ssIFlyPY31B69GyPM",
            "https://drive.google.com/uc?export=view&id=1Vo9wl4WFqSMVQ0C2lpCrpxn5Ni_wF3hP",
            "https://drive.google.com/uc?export=view&id=1h6pjjAB0COPn5L0zZCGRzfGW1VV3Pr6Z",
            "https://drive.google.com/uc?export=view&id=1CFDbYLQOrODfW9SBkU5SGSwZCUhwO_58",
            "https://drive.google.com/uc?export=view&id=1QI2EN5UU3zfQkyJDDG4Tp1nINMZfTKEm",
            "https://drive.google.com/uc?export=view&id=1KnNhGTWIScjBMZMsRwpR_7hrEI4yrhfk",
            "https://drive.google.com/uc?export=view&id=16QgqnL-fzboLPkNPmXtEr7P_yiabQ9LP", 
            "https://drive.google.com/uc?export=view&id=1ohv65eZOl5ifSdAkh6IpJrUvOPwKyFSs",
            "https://drive.google.com/uc?export=view&id=1OSWUwlHIElcC5318h0IuTRtujt8FPKo4",
            "https://drive.google.com/uc?export=view&id=1qHdYmrGn5h0lPEpGYtP2_Uhq1R7c3lT9",
            "https://drive.google.com/uc?export=view&id=1jbcWbOPunmEVH0F2OqY3Ecb2yVQ7BSCh",
            "https://drive.google.com/uc?export=view&id=174LNB_mRmSGDU-Jdg-sZTQpgRRO_kdEt",
            "https://drive.google.com/uc?export=view&id=1trdwmQ2e-iTGZ81oCIWtJLkY8PVfVcHH",
            "https://drive.google.com/uc?export=view&id=1vwGpMoSnQuBXGMYnHrUHEM9_u2glk546", 
            "https://drive.google.com/uc?export=view&id=13BbOsXvUrmKFYhQORa5FDtyomXCahbVT",
            "https://drive.google.com/uc?export=view&id=1tcSMl-xSiu0s79bOQpGoDppG9BUa-_4o",
            "https://drive.google.com/uc?export=view&id=1_GZrnqPOyTkYGpWORpmeKw22jzNV_nNa",
            "https://drive.google.com/uc?export=view&id=1mFuzxhGEx51WRbepLZ1t7QPkRrlo-Yv1",
            "https://drive.google.com/uc?export=view&id=1wmcQoMD7e4GqyjD3CSYsFdNSAscE77cs",
            "https://drive.google.com/uc?export=view&id=1tS-qrrkOkWixsj_1_AjYDvMh10hP6CBe",
            "https://drive.google.com/uc?export=view&id=1vgeNYsORtZUYx4tklPfkYiWroQRXAaA4"
        ]
        data_list = [
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Selalu semangat dan enerjik, nular ke kita semua.",
                "pesan": "Jangan bosan ngajarin kita hal baru!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Punya cara komunikasi yang enak dan mudah dimengerti.",
                "pesan": "Terima kasih sudah sering jadi jembatan antara kami dan pengurus atas."
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Tegas tapi asik, selalu punya solusi di saat genting",
                "pesan": "Tetap jadi panutan ya, semangatt."
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Selalu semangat dan nggak pernah setengah-setengah kalau kerja.",
                "pesan": "Jangan pernah berubah, Kak. Energi Kakak luar biasa"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Selalu semangat dan enerjik, nular ke kita semua",
                "pesan": "Jangan bosan ngajarin kita hal baru, bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Sosok yang tegas, tapi tetap bisa diajak ngobrol santai",
                "pesan": "Terima kasih sudah banyak membimbing. Semoga makin sukses ke depannya."
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Punya jiwa kepemimpinan, tapi tetap membaur.",  
                "pesan": "Terus jaga cara memimpin yang santai tapi tegas itu, Bang."
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Terorganisir dan punya komitmen tinggi.",
                "pesan": "Terima kasih udah ngajarin pentingnya konsistensi dalam organisasi!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Ramah dan suka ngajak ngobrol duluan.",
                "pesan": "Terima kasih sudah banyak memberikan ruang untuk kami berkembang."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Kreatif dan punya gaya yang khas.",
                "pesan": "Semoga bisa terus berkarya dan berkembang di jalur yang Abang pilih."
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Salah satu kakak yang paling aktif dan total kalau udah pegang program kerja.",
                "pesan": "Terus semangat berkarya ya, Kak. Kami banyak belajar dari etos kerja Kakak"
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Tegas, tapi tetap santai dan enak diajak diskusi.",
                "pesan": "Semoga tetap jadi panutan dan sukses ke depannya"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano, Nyanyi, Ngehalu",
                "sosmed": "@bee_0115",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Teliti dan profesional dalam mengurus kegiatan.",  
                "pesan": "Terima kasih sudah menunjukkan standar kerja yang baik"
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Punya wawasan luas dan selalu berbagi insight baru.",
                "pesan": "Semoga terus tumbuh jadi pribadi yang berdampak luas"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Tenang, dewasa, dan selalu berpikir jernih.",  
                "pesan": "semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Seru, dekat dengan semua kalangan, dan tetap profesional.",  
                "pesan": "Semoga tetap jadi sosok yang mengayomi dan adaptif."
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Disiplin dan konsisten, jadi contoh buat kami.",
                "pesan": "Terus pertahankan integritas itu, Bang. Kami banyak belajar dari Abang"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main catur",
                "sosmed": "@giofaniars_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan": "Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Aktif, kreatif, dan energik di setiap kegiatan.",
                "pesan": "Terus tebarkan semangat kepedulian itu ke mana pun melangkah."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jalan airan 1",
                "hobbi": "Futsal",
                "sosmed": "@gustriana.d_",
                "kesan": "Tenang dan bisa ngontrol keadaan",
                "pesan": "Tetap semangat menginspirasi lewat karya-karya nyata, Kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan": "Terima kasih atas semua pelajarannya, bang semangat!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jya6oNvMnIMNsgKB94N5PpWCXnn-gmjn",
            "https://drive.google.com/uc?export=view&id=11pGpxlAk1yCiFgDTMuDn3P3WR0xSlxxx",
            "https://drive.google.com/uc?export=view&id=16jpCqUBxQ3elTK3VWKDRWXc5LWEMGQ21",
            "https://drive.google.com/uc?export=view&id=1O7OGxeokz_VnqjYETLBqlTfCye5PvJhG",
            "https://drive.google.com/uc?export=view&id=1n-yG4iq-y8BxZZ4TYuj6F4kbzFGhZaiL",
            "https://drive.google.com/uc?export=view&id=14EDGD4CpLfQwOFpH7PlxdqYsr9qaHdDg",
            "https://drive.google.com/uc?export=view&id=1gBuR8rai_cuQf6sGlfl4kAbLGMXu-pvO",
            "https://drive.google.com/uc?export=view&id=1yl73nEvr_y5QuOtcHhTl6ZTASSuHbB7S",
            "https://drive.google.com/uc?export=view&id=18gfoJBNSpsqETwrcWIvZ_RpP-xJ4MYn4",
            "https://drive.google.com/uc?export=view&id=1MG0WuChx_hqYhKj_h5vVY-u7iCYYsbwa",
            "https://drive.google.com/uc?export=view&id=1ksfN4YELvDEkjgwXJxkMke5hy7bSDq0m",
            "https://drive.google.com/uc?export=view&id=1ywLBqNSDBuMXoJhuHnm4a3Z_mjj6uvdp",
            "https://drive.google.com/uc?export=view&id=148PP5W0Q6gMlWt5C9SAV4KZPfyxrLkFT",
            "https://drive.google.com/uc?export=view&id=1vTP-2tusItno5UETJ-h5N0wYtKRw0W73",
            "https://drive.google.com/uc?export=view&id=1H-bo1xeXoahhlXyej6Ogz_GBD4g3tyxi",
            "https://drive.google.com/uc?export=view&id=1c-Hfyq0zCLmP7hvDjjfzdG0cztS1cJt0",
            "https://drive.google.com/uc?export=view&id=1-9l3ZFoaJsDUieRxxZVTFRKMRJ9SMqx-",
            "https://drive.google.com/uc?export=view&id=1cwAA5NtnHk1C0TzX77U0GpYamoseZ_bH",
            "https://drive.google.com/uc?export=view&id=1VOuDRMTPhlOleMZ4aQIqVq06qHZVyo0f",
            "https://drive.google.com/uc?export=view&id=1QBKygxB8Y1doCSopAzAiLEqxwQyGnMcg",
            "https://drive.google.com/uc?export=view&id=1QaCi3hW_FyEvhipl54qZ2D8XQ3U2SrxU",
            "https://drive.google.com/uc?export=view&id=19RLAfnnBuFdSBnRPwjA7Y07Xod2palcW",
            "https://drive.google.com/uc?export=view&id=113Do2bNJU_02jZAzn6QccB2p0s1CHA1k",
            "https://drive.google.com/uc?export=view&id=1ODhlva61FZL6W7va81_LXYyzT9UPjne4"
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
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1TXfrXBSxUwvJ6mJvattEKaIzaWVx1z7W",
        "https://drive.google.com/uc?export=view&id=1PHzjP7WEAvITVlqyADlxV0ADlPdI1eGi",
        "https://drive.google.com/uc?export=view&id=1aGpfpXjSi0Ua_Va6GEm_4ktoXusJDIgi",
        "https://drive.google.com/uc?export=view&id=1JxRmCvXM6ZAnAiA88pF-Ft8DLGaUcECl",
        "https://drive.google.com/uc?export=view&id=12b24vgLTxdlFZJ_VoiHbcXvewjCGMsMx",
        "https://drive.google.com/uc?export=view&id=1M4Qua2u8LfeEl-aL3Ua93j0ukBKjNjqy",
        "https://drive.google.com/uc?export=view&id=1NpP9v5NrGbLSjPH2Zowb9laRJL7UQ1gc",  # zailani satria
        "https://drive.google.com/uc?export=view&id=1kLBkeo8DROBq4V8sogEH_kzcK13AQgav",
        "https://drive.google.com/uc?export=view&id=1HcVQaLvArv2YzV2iKIApv04T5PGbydAS",
        "https://drive.google.com/uc?export=view&id=1MEdZZGvAOEi3cSDPYPH8WhLcU4Ibi0MQ",
        "https://drive.google.com/uc?export=view&id=1G2h33epUZPwBO3Idze7x--LhuKgO3LF9",
        "https://drive.google.com/uc?export=view&id=1G2h33epUZPwBO3Idze7x--LhuKgO3LF9",
        "https://drive.google.com/uc?export=view&id=15CG1tUniiI_1Q8NB8KVhp_sxR76zPKne",
        "https://drive.google.com/uc?export=view&id=1nmCpDDXDt1CRAewE5h0yQIv5JnffCe6R",
        "https://drive.google.com/uc?export=view&id=1PHzjP7WEAvITVlqyADlxV0ADlPdI1eGi",
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
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "blm",
                "umur": "blm",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "brp",
                "umur": "gatau",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fJpZ5WNpPgRDmTsndstZKHCFmzDJh_ZU",
            "https://drive.google.com/uc?export=view&id=1lW2-w_r3MMjNjOFHpvn5DlvmS4DN4Ztu",
            "https://drive.google.com/uc?export=view&id=1IxHk7jAVVyobTs7ZkBAVK623j7fIEZHD",
            "https://drive.google.com/uc?export=view&id=1pgaAMR1G8Bs4UIKPTml_-5RgVbtvnQ5X",
            "https://drive.google.com/uc?export=view&id=1no2RT5-s-p9inurLtmakb7rHsDXxQpKF",
            "https://drive.google.com/uc?export=view&id=1oOlF_CLqGFWtCQNNoAsv3uHWpatgOYaD",
            "https://drive.google.com/uc?export=view&id=1c00uyRFX28w9rciZm5ngiwe1AAm4fz_U",
            "https://drive.google.com/uc?export=view&id=1WEooTWv3yiUs6g01qCMT6x0lZKO2Lrve",
            "https://drive.google.com/uc?export=view&id=1Q1Xh3fGjslhatkBVGt6KkOHBtzC91W8z",
            "https://drive.google.com/uc?export=view&id=1oOlF_CLqGFWtCQNNoAsv3uHWpatgOYaD",
            "https://drive.google.com/uc?export=view&id=15YgIKAyr0OtcxQXGTdZpxXrCIFZThSix"
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "dananghk_",
                "kesan": "Kakaknya asik dan seru.",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Senang bisa berkenalan dengan kakak.",
                "pesan": "Semoga sukses selalu kuliahnya!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Kakaknya ramah dan baik.",
                "pesan": "Sehat selalu ya, kak."
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif.",
                "pesan": "Semangat terus kuliahnya, kak!"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Senang bisa bertemu dengan kakak.",
                "pesan": "Semoga semua urusannya dilancarkan."
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Sukses selalu untuk kakak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Kakaknya asik diajak diskusi.",
                "pesan": "Terima kasih atas bimbingannya, kak."
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya, kak!"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu, kak!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya sangat ramah.",
                "pesan": "Jaga kesehatan selalu, kak!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Terima kasih kak atas bantuannya.",
                "pesan": "Semangat dan sukses selalu!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12M9OiOVstWfmpyNOCevqyFPRLfu_Ms3U",
            "https://drive.google.com/uc?export=view&id=13rPkM-SMmYwntA8D_gZetSliOSAaaUdV",
            "https://drive.google.com/uc?export=view&id=13vN9DUGdnNQyRAu6fG0_HmZ_AHcoVhBW",
            "https://drive.google.com/uc?export=view&id=1XnqibHQdDK6Q9L4UtvLUnBSq0YNb62VN",
            "https://drive.google.com/uc?export=view&id=1G5EGQvXYpO3InP2yDcmxls52pLJvU8zQ",
            "https://drive.google.com/uc?export=view&id=1riHfX0eWiGzAHe-jGAEiO7lxrp532CvZ",
            "https://drive.google.com/uc?export=view&id=1fGYEhqpMDdMMIIxK7XTAyGT0MAztUp3R",
            "https://drive.google.com/uc?export=view&id=1t7nbrovUhgdh3XAVyHCKPxx1xpto4ePB",
            "https://drive.google.com/uc?export=view&id=11Or3EjWgZxae3SlTI2wyQPbZUSoem__m",
            "https://drive.google.com/uc?export=view&id=1nD2FnK20A_2AMNJnMB8PXIg7sZG43FJV",
            "https://drive.google.com/uc?export=view&id=1zG75AWwduhfGqU9IkeT4Xe-PcD5PxZEl",
            "https://drive.google.com/uc?export=view&id=1kV0Gcj6FCtrXeEy4vM-t3-kKiyOwxVPM",
            "https://drive.google.com/uc?export=view&id=1FmUbJa0Mwo56juivjInlCBPkm1Hq62gR",
            "https://drive.google.com/uc?export=view&id=16f1WIKgfTUq0-CW4vfhlHfNTFdQxZzFE",
            "https://drive.google.com/uc?export=view&id=1S2qWgcTlGzohVOU-cV_FVgGoQ4_2JkzF",
            "https://drive.google.com/uc?export=view&id=1EkrNkQYMOLkJbBjwinmDDMKcHIMxLe10",
            "https://drive.google.com/uc?export=view&id=1guqZPG-yvP2hF3apLIm-eugpCGUGgQb1",
            "https://drive.google.com/uc?export=view&id=1jwAXOxJCMWCyYsOaIqb01tZawnxj3VbE"
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
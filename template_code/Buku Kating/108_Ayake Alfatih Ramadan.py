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
            "https://drive.google.com/uc?export=view&id=1voYollQhPbcXDCLm898HZQb7Z1QzhC1n",#1
            "https://drive.google.com/uc?export=view&id=1Dl0mMA59pqJURkgqckrKFKjEya71CW-B",#2
            "https://drive.google.com/uc?export=view&id=1BTrI5ooalrYQFJWSM77gRoqUVbt8Tjjd",#3
            "https://drive.google.com/uc?export=view&id=1fajnHNJQr555X3wIgoctGAFM8pbQjEMQ",#4
            "https://drive.google.com/uc?export=view&id=1r5mSildwsO3T5wJ8YVx62BVR1I8cwpIE",#5
            "https://drive.google.com/uc?export=view&id=1_4PkCRSFwId69_ZiuD1ZjchlZbyI5mkw",#6
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Pemimpin yang berwibawa dan kompeten",  
                "pesan":"Semoga terus menjadi pemimpin yang bukan hanya dihormati tetapi juga dicintai"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Pribadi yang suka berterus terang",  
                "pesan":"Hajar terus tugasnya bang joo"# 2
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kos",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini random banget, lucu",  
                "pesan":"semangat nahan pipisnya kak"# 3
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Pasti aslinya susah dibaca",  
                "pesan":"Semangat terus membacanya kak "# 4
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng,Bali",
                "alamat": "Asrama TB 5",
                "hobbi": "Nahan eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Bahagia banget kak",  
                "pesan":"Semangat nahan eeqnya kak"# 5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Gokil banget sih kak",  
                "pesan":"semangat terus kuliahnya kakak"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fAo-5cjU_Wm-GalF0pJg45N0C5ZL1Ovv",#1
            "https://drive.google.com/uc?export=view&id=1PX4eHc9nB1S7eBsIY6LoD8xoNqAMyVKt",#2
            "https://drive.google.com/uc?export=view&id=1jSCDLzvp0pSg1rX59W_4XBed_IEQunDg",#3
            "https://drive.google.com/uc?export=view&id=1dDTS8K4SXel7qwngykl-kRvTKztApFPI",#4
            "https://drive.google.com/uc?export=view&id=1xfzMvdlwkNgYh_D0lkHrM3aCcIC6dCfR",#5 
            "https://drive.google.com/uc?export=view&id=1k_r__QlBHtBoNkQRSYUj8lTwlyt67_xj",#6 
            "https://drive.google.com/uc?export=view&id=1kgTgww2z0ti1zxqxSuInnve344xRrSMe",#7
            "https://drive.google.com/uc?export=view&id=1cBsr4GWSA9jrO8OEksTkKDJpXXTGrUxQ",#8
            "https://drive.google.com/uc?export=view&id=1E2wti1CQeKHIdOTJtWgxw758PWPmD8KZ",#9
            "https://drive.google.com/uc?export=view&id=",#10kosong
            "https://drive.google.com/uc?export=view&id=141Zbqnyhfpmsvon6s4lWHCUALDDqzOFH",#11
            "https://drive.google.com/uc?export=view&id=1X1vnGHmk2knQIZZHAd2oeDQ2z5fMVkwZ",#12
            "https://drive.google.com/uc?export=view&id=1jyNNanChittd51MSh_zRskyGYQP2uEQs",#13
            "https://drive.google.com/uc?export=view&id=109sHDuK9-pJnLkzUxRl9hPfckX8Qr9J8",#14
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Yapping",
                "sosmed": "@Jeremia_s_",
                "kesan": "Palu diketuk peraturan baru",  
                "pesan":"Jadi ga sabar nih ditraktir gacoannya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450xxx",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak merupakan orang yang sangat berdedikasi tinggi",  
                "pesan":"Teruslah menjadi panutan bagi kami"# 2
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi morse",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak merupakan seseorang yang disiplin dan bertanggung jawab",  
                "pesan":"Konsisten terus kak"# 3
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Aura keadilannya kelihatan banget kak",  
                "pesan":"Semangat terus menegakan keadilan kak"# 4
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini sangat menyenangkan",  
                "pesan":"Pertahankan profesionalitasmu kak"# 5
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Kakak sangat aktif dan komunikatif",  
                "pesan":"Teruslah berkontribusi dengan ide ide brilianmu kak"# 6
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way Halim",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Aura OZT nya wow banget kak",  
                "pesan":"Semoga menjadi wisudawan ipk 4.0 kak"# 7
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Seseorang yang selalu hadir di setiap kegiatan",  
                "pesan":"Sebarkan terus semangatmu ke yang lain kak"# 8
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "Seseorang yang sangat bisa diandalkan",  
                "pesan":"Teruslah berkembang kak"# 9
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Seseorang yang sangat memperhatikan penampilannya",  
                "pesan":"Jadikan ketelitianmu sebagai inspirasi kami kak"# 10
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakak nya lucuuu",  
                "pesan":"Semangat terus kuliahnya kakak"# 11
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Sipaling jago bahasa php",  
                "pesan":"Tebarkan ilmunya ke kami kak"# 12
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini tegas dan disipin dan ga neko neko",  
                "pesan":"Semangat terus kak kuliahnyaaaa"# 13
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Seseorang pemberi semangat dan mengarahkan kami untuk tetap berjuang sampai detik ini",  
                "pesan":"Teruslah menjadi seorang panutan bagi semua orang"# 14
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yJ0DJM3JfluP7Jm3C2OhiEEu6uWAKAHO",#1
            "https://drive.google.com/uc?export=view&id=1pzpaqAhm8xxYKsNY09tIypJYaOEjO3ZT",#2
            "https://drive.google.com/uc?export=view&id=1xUHQMEQdEaOVcHqgDAm2cRpNe_8FR5SK",#3
            "https://drive.google.com/uc?export=view&id=1t1IVn8dQqz5iovVzlofwap18Zk91bJZf",#4
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Tanya caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Penghubung himpunan yang bijak",  
                "pesan":"Teruslah mengambil keputusan dengan bijaksana"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakak ini loyal terhadap tim",  
                "pesan":"Teruslah menginspirasi semua orang kak"# 2
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Seseorang yang produktif",  
                "pesan":"Teruslah menciptakan hal baru kak"# 3
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Seseorang yang bisa diandalkan ",  
                "pesan":"Teruslah berikan dedikasimu kak"# 4
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ys1NE1IRUAXx8Zdwp-GIfA9Y675M4_vN",#1
            "https://drive.google.com/uc?export=view&id=1ZLKLwSqAnf4L-U9xPpeQ-ZlyMKDHLq7j",#2
            "https://drive.google.com/uc?export=view&id=1g2W7pfeHn3dKiIVtlvnMqGrDJytgHo9a",#3
            "https://drive.google.com/uc?export=view&id=1dvk22VUflvQGr4uJjk_7Xx8awsSztSoR",#4
            "https://drive.google.com/uc?export=view&id=143drYqHyA0p6JiACMU0V9guGOCIegRcs",#5
            "https://drive.google.com/uc?export=view&id=1anTegx0U-hpmSzGUzhlw6YzNz6ZapFlS",#6
            "https://drive.google.com/uc?export=view&id=1YoLsMRiiv6axzqo8XIhAseaGHjX50y6a",#7
            "https://drive.google.com/uc?export=view&id=1iayk6BeXBCDBw6qEC3Dysh9jjIc9PBVM",#8
            "https://drive.google.com/uc?export=view&id=1uZYoEbuyonX4vXqFZtKeFP9Z9LDxgPwG",#9 
            "https://drive.google.com/uc?export=view&id=1_EH-ljUi4Q2TDdDsGkAlaZI1epFR9a08",#10
            "https://drive.google.com/uc?export=view&id=1R8714ERP-THQnhRobautiTmsDVfEWrzn",#11
            "https://drive.google.com/uc?export=view&id=1qR9TSGFTI5ylAHGV0c7zUp6AHELA-dcC",#12
            "https://drive.google.com/uc?export=view&id=1hR4Pjs2bkMwrH3OP_p-DngbPMLy7dEt5",#13
            "https://drive.google.com/uc?export=view&id=1M8QPJcqmEfu0XZ-oK9YpB17OH0pJvxM-",#14
            "https://drive.google.com/uc?export=view&id=1xoGabdbttIhznysTsQetZyyzPeCIaZ18",#15
            "https://drive.google.com/uc?export=view&id=1UOsTI03fUuaP6R9vlxvH5GejUuSddRJu",#16
            "https://drive.google.com/uc?export=view&id=1gjoCUxknaZcjKrK-rh32U9n9V4ln1w8O",#17
            "https://drive.google.com/uc?export=view&id=1wDVvx8y1CX2oORU23AAHiqv4YBfIih0b",#18
            "https://drive.google.com/uc?export=view&id=1jQ5lBWSb196WxlyK3YKR-a_6zrZdGzW2",#19
            "https://drive.google.com/uc?export=view&id=1LDGMpNLthJY59BYp1AiSYVMC6GRcfkdW",#20
            "https://drive.google.com/uc?export=view&id=1rB1QXVBpJuPAk6izcxZiffqfWSVNhr7g",#21
            "https://drive.google.com/uc?export=view&id=1uAhKqVmL-CZK2WdeaSIch1Ut7ZmhHyb9",#22
            "https://drive.google.com/uc?export=view&id=1LYQlBOnohfkRMryK5EZwI1pdFHdTnHdR",#23
            "https://drive.google.com/uc?export=view&id=1jTGKEJpm4jRryobu2SipHytdWSRh0lBD",#24
            "https://drive.google.com/uc?export=view&id=1chIs3uynOyFcsUg0gDteOvEVzKoc7juu",#25
            "https://drive.google.com/uc?export=view&id=1AKDWaE4fBUiH1J7s3vWgH2bLKiRm3aJx",#26
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri Sukarame",
                "hobbi": "Jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "",  
                "pesan":""# 2
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinanaaa",
                "kesan": "",  
                "pesan":""# 3
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis,Pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "",  
                "pesan":""# 4
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "",  
                "pesan":""# 5
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""# 6
            },
            {
                "nama": "Ulliano Wiliam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano,ngoding",
                "sosmed": "@ullianowlm",
                "kesan": "",  
                "pesan":""# 7
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "",  
                "pesan":""# 8
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung,Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game,Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "",  
                "pesan":""# 9
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "main roblox seru kak",  
                "pesan":""# 10
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untunng",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "",  
                "pesan":""# 11
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaa",
                "kesan": "",  
                "pesan":""# 12
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jl. Airan",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""# 13
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha",
                "kesan": "",  
                "pesan":""# 14
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tanggerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky_",
                "kesan": "",  
                "pesan":""# 15
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blocblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "",  
                "pesan":""# 16
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jahilin miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "",  
                "pesan":""# 17
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Gitar,Main game,Badminton",
                "sosmed": "@ginda_mrp",
                "kesan": "",  
                "pesan":""# 18
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "Nyanyi",
                "sosmed": "@natasyamavisca",
                "kesan": "",  
                "pesan":""# 19
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "",  
                "pesan":""# 20
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "",  
                "pesan":""# 21
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang Berbicara",
                "sosmed": "@vany.salsabila",
                "kesan": "",  
                "pesan":""# 22
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "",  
                "pesan":""# 23
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "",  
                "pesan":""# 24
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "",  
                "pesan":""# 25
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Ngehina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "",  
                "pesan":""# 26
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",#1
            "https://drive.google.com/uc?export=view&id=",#@
            "https://drive.google.com/uc?export=view&id=",#3
            "https://drive.google.com/uc?export=view&id=",#4
            "https://drive.google.com/uc?export=view&id=",#5
            "https://drive.google.com/uc?export=view&id=",#6
            "https://drive.google.com/uc?export=view&id=",#7
            "https://drive.google.com/uc?export=view&id=",#8
            "https://drive.google.com/uc?export=view&id=",#9
            "https://drive.google.com/uc?export=view&id=",#10
            "https://drive.google.com/uc?export=view&id=",#11
            "https://drive.google.com/uc?export=view&id=",#12
            "https://drive.google.com/uc?export=view&id=",#13
            "https://drive.google.com/uc?export=view&id=",#14
            "https://drive.google.com/uc?export=view&id=",#15
            "https://drive.google.com/uc?export=view&id=",#16
            "https://drive.google.com/uc?export=view&id=",#17
            "https://drive.google.com/uc?export=view&id=",#18
            "https://drive.google.com/uc?export=view&id=",#19
            "https://drive.google.com/uc?export=view&id=",#20
            "https://drive.google.com/uc?export=view&id=",#21
            "https://drive.google.com/uc?export=view&id=",#22
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
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": " ",  
                "pesan":" "# 2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": " ",  
                "pesan":" "# 3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": " ",  
                "pesan":" "# 4
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": " ",  
                "pesan":" "# 5
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": " ",  
                "pesan":" "# 6
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": " ",  
                "pesan":" "# 7
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": " ",  
                "pesan":" "# 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": " ",  
                "pesan":"   " # 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": " ",  
                "pesan":" "# 10
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": " ",  
                "pesan":" "# 11
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": " ",  
                "pesan":" "# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": " ",  
                "pesan":" "# 13
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":""# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "",  
                "pesan":""# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": " ",  
                "pesan":" "# 16
            },
            { 
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": " ",  
                "pesan":" "# 17
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": " ",  
                "pesan":" "# 18
            },
            
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",  
                "pesan":""# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "",  
                "pesan":""# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "",  
                "pesan":""# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": " ",  
                "pesan":" "# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",#1
            "https://drive.google.com/uc?export=view&id=",#@
            "https://drive.google.com/uc?export=view&id=",#3
            "https://drive.google.com/uc?export=view&id=",#4
            "https://drive.google.com/uc?export=view&id=",#5
            "https://drive.google.com/uc?export=view&id=",#6
            "https://drive.google.com/uc?export=view&id=",#7
            "https://drive.google.com/uc?export=view&id=",#8
            "https://drive.google.com/uc?export=view&id=",#9
            "https://drive.google.com/uc?export=view&id=",#10
            "https://drive.google.com/uc?export=view&id=",#11
            "https://drive.google.com/uc?export=view&id=",#12
            "https://drive.google.com/uc?export=view&id=",#13
            "https://drive.google.com/uc?export=view&id=",#14
            "https://drive.google.com/uc?export=view&id=",#15
            "https://drive.google.com/uc?export=view&id=",#16
            "https://drive.google.com/uc?export=view&id=",#17
            "https://drive.google.com/uc?export=view&id=",#18
            "https://drive.google.com/uc?export=view&id=",#19
            "https://drive.google.com/uc?export=view&id=",#20
            "https://drive.google.com/uc?export=view&id=",#21
            "https://drive.google.com/uc?export=view&id=",#22
            "https://drive.google.com/uc?export=view&id=",#23
            "https://drive.google.com/uc?export=view&id=",#24
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
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": " ",  
                "pesan":" "# 2
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": " ",  
                "pesan":" "# 3
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": " ",  
                "pesan":" "# 4
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": " ",  
                "pesan":" "# 5
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": " ",  
                "pesan":" "# 6
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": " ",  
                "pesan":" "# 7
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": " ",  
                "pesan":" "# 8
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": " ",  
                "pesan":" "# 9
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": " ",  
                "pesan":" "# 10
            },
            {
                "nama": "khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": " ",  
                "pesan":" "# 11
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": " ",  
                "pesan":" "# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": " ",  
                "pesan":" "# 13
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": " ",  
                "pesan":" "# 14
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": " ",  
                "pesan":" "# 15
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": " ",  
                "pesan":" "# 16
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": " ",  
                "pesan":" "# 17
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": " ",  
                "pesan":" "# 18
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": " ",  
                "pesan":" "# 19
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": " ",  
                "pesan":" "# 20
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": " ",  
                "pesan":" "# 21
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": " ",  
                "pesan":" "# 22
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": " ",  
                "pesan":" "# 23
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": " ",  
                "pesan":" "# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()
elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1v5u_huaSJnIrLKhxeUz1r5pexgIBfShH",#1
            "https://drive.google.com/uc?export=view&id=1jMzGNFyPRG0126KJ7dyy3D003w-XO8on",#2
            "https://drive.google.com/uc?export=view&id=1yKXqxL2exek3szWT_Y0p4r57MdlQipKL",#3
            "https://drive.google.com/uc?export=view&id=1Vh1jUPuzcTTkQeHmRmepUC5NBNBvE9zS",#4
            "https://drive.google.com/uc?export=view&id=1v92OQxj8YdqrAWEQc_X_x25u_lRjZZQm",#5
            "https://drive.google.com/uc?export=view&id=1Ihj7-mAgTCdJUQDBvW_wsn6DGu0jBHqd",#6
            "https://drive.google.com/uc?export=view&id=144rkLmERta1a6J2yFWRwPluxmpR517_X",#7
            "https://drive.google.com/uc?export=view&id=1v5L6pHsPt_UnqNVEURgmP-kxzxOMhQ_x",#8
            "https://drive.google.com/uc?export=view&id=12lnyD6LBxO_wnYGMvWzJGhTnpq-Eg4ug",#9
            "https://drive.google.com/uc?export=view&id=1ZDpQlRlcrxARTkR5iaxChBfrK3OFuaDv",#10
            "https://drive.google.com/uc?export=view&id=1GNGhPlIXQa6ibHtBx-QwMHquCBWx4Iid",#11
            "https://drive.google.com/uc?export=view&id=13S6DkS1a00sME_OkC4UUc7-GVZG1cx1Z",#12
            "https://drive.google.com/uc?export=view&id=1MPCQb7qAAJCrCBzFS4vpTOmTEf03RAkX",#13
            "https://drive.google.com/uc?export=view&id=1zPt3bm-3gT2vG8wLWP0emdRD1R9m2LV7",#14
            "https://drive.google.com/uc?export=view&id=1MVjKzGnJNOKkIABlkimjU-_LnVV025sH",#15
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
                "kesan": "Skena habiezz",  
                "pesan":"Teruslah memberi tampilan unik kak"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Tomboy",  
                "pesan":"Kasih tips dong kak biar ga galau mancing"# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Penasaran masakannya",  
                "pesan":"Jangan lupa bagi bagi makanan kak"# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Zumba itu apa ya kak",  
                "pesan":"Ajrin main zumba dong kak"# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "Kriminanl keren",  
                "pesan":"Jangan sampai bosan menghitung kerikilnya bang"# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Baking ini apa ya kak",  
                "pesan":"Ajarin kami baking dong kak"# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Tegas,Kalem",  
                "pesan":"Sehat terus ka "# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Ustadz banget dan mirip rigen bang",  
                "pesan":"Tebarkan terus kebaikanmu bang, sasageyoo"# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "wibu",  
                "pesan":"Semangat olahragannya bang"# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Suaranya bagus banget kak",  
                "pesan":"Jangan lupa kasih lihat hasil lukisannya bang"# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Humoris, lucu,dan penyemangat",  
                "pesan":"Cicaknya jangan sampe dikedipin kak"# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "jago banget main musiknya kak",  
                "pesan":"Kasih denger kami suara musik nya kak"# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Kiper no bobol",  
                "pesan":"Jangan lupa jaga berat badan bang"# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "humoris",  
                "pesan":"semangat kuliahnya kak"# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Jago banget main rubik miror nya kak",  
                "pesan":"Besok main rubik mayor ya kak"# 15
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Bp0GKH2H4KduJ2zM1Ld8rHY5Gp2DYE20",#1
            "https://drive.google.com/uc?export=view&id=14NM8mIpht_nj89Bnu8tQLrV-nhju5qgQ",#@
            "https://drive.google.com/uc?export=view&id=12LwjdwSsTVdN1THri-pliKKKtPwwpvkz",#3
            "https://drive.google.com/uc?export=view&id=16yBuf6vlkZdn6j_jwr6aTML9CVO2lVO9",#4
            "https://drive.google.com/uc?export=view&id=1i2YAH4QBfU1vYgxrJ6egSghs7Wot7qHn",#5
            "https://drive.google.com/uc?export=view&id=1Ejk1rCUiK9CdoWlgytBb9I23nLNJjau0",#7
            "https://drive.google.com/uc?export=view&id=1EIUqa2-nWtalWCk6i97eKrgn67EX4n95",#8
            "https://drive.google.com/uc?export=view&id=1IWKNa5UTxGU0gJXHIHYpAu0fVBib3adD",#9
            "https://drive.google.com/uc?export=view&id=1NIxrXoOMQVdpUq6ObWnz4S20J9tjjXs9",#10
            "https://drive.google.com/uc?export=view&id=1ABKaOKrRH-qu4NsBzzfRJu5N7Z0Uq_HR",#11
            "https://drive.google.com/uc?export=view&id=1wIkSyD-VQh-4GtoZyl5IJyA-LP_itljI",#11
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_",
                "kesan": "Pemimpin yang tegas dan berwibawa",  
                "pesan":"Ajakin aku jogging kak"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Baik kalem dan inspiratif",  
                "pesan":"Ifo novel terbaik kak"# 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "Beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Tegas dan berwibawa",  
                "pesan": "Beliin aku parfum bang biar kita sama sama wangi"# 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Humoris banget orangnya",  
                "pesan":"Sehat selalu kak"# 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton Drama Short di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Pintar dan kalem",  
                "pesan":"Jaga kesehatan dan semangatnya kak"# 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Gokil",  
                "pesan":"Semangat kuliahnya kak"# 6
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Baik, pinter",  
                "pesan":"Semangat belajarnya bang"# 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Humoris,cantik",  
                "pesan":"Jangan lupa kasih tau drakor terbaik kak"# 8
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg.Perwira 2",
                "hobbi": "Menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Ramah,ceria",  
                "pesan":"Jangan lupa film nya ditonton kak"# 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Random",  
                "pesan":"tentukan menu masakan besok kak"# 10
            },
            {
                "nama": "Ndya Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Pinter,Rajin",  
                "pesan":"Tetap main yang positif ya kak"# 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()
elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iUagTx921MYB3TEJtnkaZgDo6p21JEmM",#1
            "https://drive.google.com/uc?export=view&id=13VvI9v_MQs7PTN17lQTZ9fzi69MDFhfa",#2
            "https://drive.google.com/uc?export=view&id=1fzUsBfR6rwHfU3xWibDiDeddPoM4VoMC",#3
            "https://drive.google.com/uc?export=view&id=1z-TdRcjciYCzLJzy45d6pMabAcZiF3-I",#4
            "https://drive.google.com/uc?export=view&id=1It_Nav1Fk4O2uKKK8oENCv-7ClrInbV9",#5
            "https://drive.google.com/uc?export=view&id=1d7uAcBW5XWdX_3WZLqdDW44WWpvn90vB",#6
            "https://drive.google.com/uc?export=view&id=1HRQXwg_FExcyEik8nWcworn_ViDV8tmp",#7
            "https://drive.google.com/uc?export=view&id=1I8D735EjjwoD7Sl4s1JqCaYhjmUFdqWh",#8
            "https://drive.google.com/uc?export=view&id=15PxPLxwaw4qSrdxjbd6-UFlFIl0jgi9P",#9
            "https://drive.google.com/uc?export=view&id=1S7Fp0lkW0H6qtW-eYf5-Qs4h07O4_J18",#10
            "https://drive.google.com/uc?export=view&id=1bM6JgGcyE8nZoYYU8ImRm_MfTX6npEwD",#11
            "https://drive.google.com/uc?export=view&id=17ZB76YToxI593QdvWsZMLLmJNrTtUtFH",#12
            "https://drive.google.com/uc?export=view&id=1i-eFuyYbGKBx3SiKAPBt-7syxnNJ30p0",#13
            "https://drive.google.com/uc?export=view&id=1EQLdjsn-hDDqChgiREQuLaP9_yUZxHL3",#14
            "https://drive.google.com/uc?export=view&id=1OFr9wXcmzwngKuSmKxBf-HMaTd-cZ8eU",#15
            "https://drive.google.com/uc?export=view&id=1HXu1WXdercRVLTkSJUBuMNoU71dhmF-1",#16
            "https://drive.google.com/uc?export=view&id=1mbCJQNVHwpBHPOyEo510GAYW3JXn2EEg",#17eigi
            "https://drive.google.com/uc?export=view&id=1mbCJQNVHwpBHPOyEo510GAYW3JXn2EEg",#18
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
                "kesan": "Solid dan penuh semangat serta menggemaskan",  
                "pesan": "Terus jaga semangat dan kebersamaannya kak"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "Santai dan inspiratif",  
                "pesan": "Teruslah berkreasi tanpa takut gagal"# 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Profesional",  
                "pesan": "Teruslah explor gaya barunya bang"# 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Gacor dan kalem",  
                "pesan": "Hati hati motorannya bang"# 4
            },
            {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Inovatif selalu punya gaya baru",  
                "pesan": "Semangat olahraganya bang"# 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "sipaling dokumentasi",  
                "pesan": "semangat menyimpan semua kenangan dalam hidup ini kak"# 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Pemberi konsep baru",  
                "pesan": "Semangat menemukan konsep baru dari belajarmu kak"# 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Menghibur",  
                "pesan": "Semangat menciptakan nada baru kak"# 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Lucu,pintar,humoris",  
                "pesan": "share lagu terbaik menurutmu dong kak"# 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Cantik,kalem",  
                "pesan": "Jangan lupa bagi gambar bagusnya kak"# 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Pintar masak",  
                "pesan": "Kembangkan menu kreatif lainnya kak"# 11
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "Pintar,kreativ dan humoris",  
                "pesan": "Spill dong kak lagu yang sering di dengar"# 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Jago banget main gamenya kak",  
                "pesan": "Ajakin datasena main roblox kak"# 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Genius",  
                "pesan": "bagi dong kak ilmunya"# 14
            },
            {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Punyas banyak skill terpendam",  
                "pesan": "Kembangkan terus skillmu kak"# 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Jago ngolah gambar",  
                "pesan": "bagi dong kak gambar yang menarik"# 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "bagus banget lukisannya kak",  
                "pesan": "Ajarin ngelukis dong kak"# 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menyanyi",
                "sosmed": "@roms.slbn",
                "kesan": "Suaranya bagus banget kak",  
                "pesan": "Asah terus suara bagusnya kak"# 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan

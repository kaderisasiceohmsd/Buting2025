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
            "https://drive.google.com/uc?export=view&id=14IrtKlH2ueg1CeXPL6st2FscLscAJ2SY",
            "https://drive.google.com/uc?export=view&id=1ox1yK7cFvulq44RL5ljUbsR4Dy08S5-Y",
            "https://drive.google.com/uc?export=view&id=1WdcP0ZL92Vobb1SAYr8O4hdQdbVvzwaj",
            "https://drive.google.com/uc?export=view&id=1gHbfG95RPgOT-cT6c9jMejieNYZj0ioe",
            "https://drive.google.com/uc?export=view&id=1IqPH3oeHcEIpFYkCdn3Iq9KBlz3pIxwP",
            "https://drive.google.com/uc?export=view&id=1ZD5ybZV18rNhZHIQuhPjz1Pyi4MOUDQL",

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
                "kesan": "Bang Rendra , Seru, asik mempunyai jiwa pemimpin yang bijaksana dan bertanggungjawab",  
                "pesan":"semangat dan terus bang, jadilah menjadi seorang yang humble terus bang!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan. Lapas Raya",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya abang!!!"# 2
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal": "Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {

               "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia, sangat memotivasi",
                "pesan":"semangat terus kuliahnya kakak !!!"# 5
            },
            {

                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "asikkk banget, kakanya chill, dilihat dari hobinya kakak asik ",  
                "pesan":"Semoga selalu dimudahkan dan semangat kuliahnya kakak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cute Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "baik, motivasi dan suka senyum dan humble,asikk",
                "pesan":"semangat terus kuliahnya kakak !!!"
         },  
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xiyxnQ14j_juLL8brNS_3Y-QiwQqmsXf",
            "https://drive.google.com/uc?export=view&id=18zYDQWjfR7PoQAQUpdRU63TDtNiGSbeX",
            "https://drive.google.com/uc?export=view&id=1W394vnpowF15bJyek5QRJRnZTXKlb-Qn",
            "https://drive.google.com/uc?export=view&id=1VfNy1c5VshwdNgur2SamAYNt383sPwcv",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "tanya caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "bang bintang asik banget saya termotivasi dengan komunikasi dan publik speaking yang bagus nya!",  
                "pesan":"semangat terus bang bintang!!!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "kak Nadya seruu,asik,dan humble",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "live instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakak baik,masyaallah,asik,seru pokoknya deh",  
                "pesan":"semangat kuliahnya kak, dan jaga kesehatannya !!!"
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak asikk, kalo ngobrol asik dan mudah mencairkan suasana",  
                "pesan":"semangat terus kuliahnya kakakk!!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bqeZ-lYhmv-rshKV8fsapTPlZJKcUuec",
            "https://drive.google.com/uc?export=view&id=1ptcOemievT6sp1NYon1skGYZx9BuExUa",
            "https://drive.google.com/uc?export=view&id=1xfRk-ghB89_dBQe4ynTUpHpmPOEFQuaJ",
            "https://drive.google.com/uc?export=view&id=1QZgF9oOVwWdAL-mAO_CSVyzxWUTJYiA3",
            "https://drive.google.com/uc?export=view&id=1VYefom_pA6MgFHVYmsFfdBHqOvq-R-yV",
            "https://drive.google.com/uc?export=view&id=1--35MkOMJmSKLKRY6Jl4e8WyQhQPnk4x",
            "https://drive.google.com/uc?export=view&id=1IS7x5oe1sg8up_p79_ZCOPBQlnh_sLM4",
            "https://drive.google.com/uc?export=view&id=1_PS65zznXr5QrYpK9vLeTDpEhrCdaFPq",
            "https://drive.google.com/uc?export=view&id=1XZK5ABQIUZTGTfKme7JUYozQvZMBnV8s",
            "https://drive.google.com/uc?export=view&id=107g2m-x7Su3KixQ_HESppvp6S2RSsVTf",
            "https://drive.google.com/uc?export=view&id=1RGtFTRkW_l7Zn9Q_6YJdyJfTOuvHX4NE",
            "https://drive.google.com/uc?export=view&id=1HYQkcP8zN8otJqDw3seFEjIz_C_5A0U3",
            "https://drive.google.com/uc?export=view&id=1oL8PZ5DmD0Yr2aLzdsdjSt_W-yiSMIgt",
            "https://drive.google.com/uc?export=view&id=17Xg3OaH6sel05K6GddM3Yj0vncA4Y_2M",
            "https://drive.google.com/uc?export=view&id=1O8RNVTePB2TWv0D5Zjw9xZ-ZSMJvKqPD",
            "https://drive.google.com/uc?export=view&id=17v0rXIAC2F1z3B9Hnz2WBtfnOyHPBJv1",
            "https://drive.google.com/uc?export=view&id=1l0kWcdtdENkwNBE_rQh1zsOTKGo7Y6Ug",
            "https://drive.google.com/uc?export=view&id=1Kol9-VEijz0kWdDNSkLUYLX9iUafnZTD",
            "https://drive.google.com/uc?export=view&id=1MxnkMSnI8NgnrZiKtNRipbS5ucrhj5wl",
            "https://drive.google.com/uc?export=view&id=1b_qLGwU0aOz1qinVgq7upQikMSIG5iu0",
            "https://drive.google.com/uc?export=view&id=1eCv--ntX77-K_JAXKUo5erH92mpMm4IP",
            "https://drive.google.com/uc?export=view&id=1gzFZFbFyRDUfHRde1NOiiBLq0D2NkfbP",
            "https://drive.google.com/uc?export=view&id=1pISr-he9jVaAWxWA-71KQvMFMT6ugC9H",
            "https://drive.google.com/uc?export=view&id=1x_8-e81RxO3sg_cFPLbvsnLTFBpMUmWj",
            "https://drive.google.com/uc?export=view&id=104D5ShvbGKXxCUYt5Ndy0Dqg8eaCT9vg",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal": "Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "bang ferdy,asikk,baik,berwibawa,kerenn bangttt",
                "pesan": "Mohon bimbingannya selalu, bang. Sehat dan sukses terus!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "korpri",
                "hobbi": "mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "tegas,baik dan terimakasih kak atas bimbingannya",
                "pesan": "Semangat terus kak kuliahnya!."
            },
           {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapasha_",
                "kesan": "Mempunyai jiwa pemimpin,tegas dan disiplin,baik menjadi motivasi bagi saya.",
                "pesan": "Terima kasih atas ilmunya dan bimbingannya kak, semangat terus kakk!!"
            },
      {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Membaca",
                "sosmed": "@ahmad.rizky__",
                "kesan": "sangat soft spoken,ramah, baik,dan memiliki jiwa ambisi yang tinggi dan aestetik.",
                "pesan": "Semangat terus dalam menjalankan ambisinya, bang!"
            },
        {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Deket Kost Dapa",
                "hobbi": "Cari Ribut",
                "sosmed": "@arientakhsnl_",
                "kesan": "Pembawaannya tenang dan bijaksana,baik, dan tegas.",
                "pesan": "Sukses selalu untuk kakak, ditunggu arahan selanjutnya."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kost arienta",
                "hobbi": "Jahilin Orang sampe nangisr",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang sangat berwibawa dan mengayomi,baik dan tegas.",
                "pesan": "semangat kuliahnya bang,terimakasih bimbingannya!"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Hobinya Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Baik,tegas,suka memberikan arahan dan tegas .",
                "pesan": "semangat kuliahnya kak, sukses selalu!"
            },
           {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "Membaca",
                "sosmed": "@natasyamavisca",
                "kesan": "Sikapnya tegas dan disiplin, baik,dan ramah.",
                "pesan": "Terima kasih karena sudah carrying kepada kami kak!."
            },
          {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Suka Ngader",
                "sosmed": "@nobelnizam",
                "kesan": "Baik, ramah dan tegas.",
                "pesan": "Semangat terus dalam menjalankan amanahnya, bang!"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "Pembawaannya bijaksana,tegas,berwawasan dan keren banget bang",
                "pesan": "Sukses selalu bang, semangat kuliahnyaa!!"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Airan",
                "hobbi": "Marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak sangat berwibawa,mengayomi, dan baik.",
                "pesan": "Mohon bimbingannya selalu, Kak. Sehat dan sukses terus!"
            },
             {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "Abang ini baik,ramah dan suka senyum, terusa juga mengayomi.",  
                "pesan":"semangat terus kuliahnya bang!!!"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang!!!"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakak asikk, hobinya sangat menarikk.",
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Apa aja",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kesan pertama aku lumayan segan,karena kakak aku kira galak ternyata baik,manis,dan lembut",  
                "pesan":"senyum teruss ya kak,semangat kuliahnya kakk!!!"
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
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "bang maul,baik,ramah,dan kalo ngomong soft",  
                "pesan":"semangat bang kuliahnya !!!"
            },
           {
                "nama": "Daffa Ahmad Noval",
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
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "kak erma baik,asik,dan seruu",  
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
                "kesan": "abang ini gamers sekali,asik,cool dan ramah",  
                "pesan":"semangat game nyaa bang dan sukses selaluu!!!"
            },
             {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "bang kevin juga lumayan misterius,tapi asik,baik,seru",  
                "pesan":"semangat terus kuliahnya bang,jaga kesehatannya!!!"
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
                "kesan": "abang chill,seru dan asik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang!!!"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "misterius,cool,tapi aslinya ternyata baik dan asik",  
                "pesan":"semangat terus kuliahnya bang!!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=147K8BCKAbggQd6Tbo9r88BcNuHNWAjan",
            "https://drive.google.com/uc?export=view&id=1MQxZhOl0zvuCxAzxthpZJkhZYfGMQ-vs",
            "https://drive.google.com/uc?export=view&id=1lfBTEBBGvv7SypeByqBn1EhHlOVpdxiF",
            "https://drive.google.com/uc?export=view&id=1B-hPyUmbTrSGg7tsifidXxuSLXg8orL6",
            "https://drive.google.com/uc?export=view&id=1RbqLoJCa_q1OPRZYHo_8buy_FYcdmVfr",
            "https://drive.google.com/uc?export=view&id=1DmqF2LtTzq7N4o8rjESeohTJxPewTagz",
            "https://drive.google.com/uc?export=view&id=14lLH92FHff7T7tkqnUYC_2Vc_c8GhAzW",
            "https://drive.google.com/uc?export=view&id=1bja2MU5lg9VIXu1rTbKtcel8rlQ9VOlm",
            "https://drive.google.com/uc?export=view&id=1aOC1IlOy4BVAuWZtgX-1C_Jz4yj6Wij_",
            "https://drive.google.com/uc?export=view&id=1p3gVpFhjNoIw7hJSo6_prNHBvo2EOAjZ",
            "https://drive.google.com/uc?export=view&id=1LpD-suuXw5eTgnTxJg3HiYv5iK_VKcBj",
            "https://drive.google.com/uc?export=view&id=1ocIBTIt0Fh0TVM-pdAyWc72HlQKb4Eyd",
            "https://drive.google.com/uc?export=view&id=10Eo3FJuQKeBSpSkC4_jfDTrZLXyXWDnP",
            "https://drive.google.com/uc?export=view&id=1OlqM214PJzuvmlTB72UmEwGHP0KAz7Ln",
            "https://drive.google.com/uc?export=view&id=1P3PSSz8bblBmI6UCKQ5yYaSAmpixPYsc",
            "https://drive.google.com/uc?export=view&id=1SJgjmCe4sXncypaf0Taj4NtvmYRELz6r",
            "https://drive.google.com/uc?export=view&id=1NHWLoZGtEZ6yc_kID_AG9R9zAJ3QMWKL",
            "https://drive.google.com/uc?export=view&id=1ADzArbqFbJ8vkKOY2BzQBUy7PDaE4KP7",
            "https://drive.google.com/uc?export=view&id=13NrhjqeV_GNBidgViBZaJvlY1NfdOl1U",
            "https://drive.google.com/uc?export=view&id=1JUxQDMGGWQMP9ii8EV5510E96-NG09j0",
            "https://drive.google.com/uc?export=view&id=1F9xqreQoGT2Vnc8SFxIF_cMxnOrGvLRL",
            "https://drive.google.com/uc?export=view&id=1qBmNfJMx6tm8fq2PTFrsPmwOfuj4J7Ri",
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
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
               "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
             {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
           {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
           {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
           {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bumi Sari Natar",
                "hobbi": "Menari,Mendengarkan Musik, Dance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
             {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
           {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Mainn Piano,mendengarkan musik, Ngehalu",
                "sosmed": "@bee.",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
             {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
           {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "mentor kuu inii, asik bangett,seru,ramah,tapi sekarang dia sedang sibuk huubu",
                "pesan":"Semnagattt banggg, kerenn bangett!!"
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EFu8juBNLelcodJUp148Z8N9Fth4YKej",
            "https://drive.google.com/uc?export=view&id=1rIDh30bxJz_0RPCUJfCv0kTjeGwKcEFp",
            "https://drive.google.com/uc?export=view&id=1PsXxQ1AcNbPfg8eJ0qPmRsl34kvYWdh3",
            "https://drive.google.com/uc?export=view&id=11yTYSeMAcjaM1LkQP0-grkTApYUeryaf",
            "https://drive.google.com/uc?export=view&id=1dYxUgLwqxCMefavFnjKfF9_KAzkGI-j8",
            "https://drive.google.com/uc?export=view&id=1XKzLLbgx4x6EXtBBho97-ALN1PC0c-h6",
            "https://drive.google.com/uc?export=view&id=1oayhk4PnI4U9HybBaFi-srxqWo7K0xKq",
            "https://drive.google.com/uc?export=view&id=1gFiu9vO29HXV6eoisWK9FtIZXYmY8s42",
            "https://drive.google.com/uc?export=view&id=14-Z8Wyec2bjSgFP4PMNmcSwLwZNiChmj",
            "https://drive.google.com/uc?export=view&id=17HzyBqKzbfTVOtmdo7uCJpxBlItXbsJR",
            "https://drive.google.com/uc?export=view&id=15y0Y7mN7N7K3VWKDqsg0pXoSJvNbEJQG",
            "https://drive.google.com/uc?export=view&id=1NWrnpOQ2CJfKgb9K-DMMX39DYtsAJ1yH",
            "https://drive.google.com/uc?export=view&id=1eLNkUy3Bo7MRR5eR3Kyv50pxBjppjezg",
            "https://drive.google.com/uc?export=view&id=1oJxSSY0TvQ6OhaWMhf3zpWpzMKAap4Q5",
            "https://drive.google.com/uc?export=view&id=1YkAl8b7mpRDpGDYrS1xTQFf7Mf4uMWRK",
            "https://drive.google.com/uc?export=view&id=1bJX4Z0ke-860XpFlPZs_odQ7Uj3PLbPO",
            "https://drive.google.com/uc?export=view&id=1QpnTH0kgoBxHKGEqAA6Es2eOsT_qewTJ",
            "https://drive.google.com/uc?export=view&id=1B0FFMI_LCO2AoFUfcIMP6ZXkIL7dME9V",
            "https://drive.google.com/uc?export=view&id=10KJuvblJnt_fJVmV7N-mxNKeYqq12sFm",
            "https://drive.google.com/uc?export=view&id=1RP8RbIiM5HR0Y75daBUFqKj3PNviznXN",
            "https://drive.google.com/uc?export=view&id=1yfhjfubQd2hv2XXlWFTgr0EJQr4CXowF",
            "https://drive.google.com/uc?export=view&id=1MMeJIw1NaXB1ZXbaxZKwyRC_ZunFhwX1",
            "https://drive.google.com/uc?export=view&id=1h1I4s7FhRenlEAqnGsQYf81Ie6bFLfdw",
            "https://drive.google.com/uc?export=view&id=1F298CG16N3-gFOIIuhO9sXAiEqsmqvAj",
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
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
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
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15Wm7Ml9aPjTePPSbJZh50I39GBFuDZ3y",
            "https://drive.google.com/uc?export=view&id=1SerxWfodIICX_XLR_spHo8KjdDNSt4Uk",
            "https://drive.google.com/uc?export=view&id=1PUsCMfzy1RfVS7QQMSz9zZDDXs21YImd",
            "https://drive.google.com/uc?export=view&id=1MkngPl6q_wYH2QVeA9PdvRwLQlmaVMpl",
            "https://drive.google.com/uc?export=view&id=1gH8v_gE00Hr4vOQ0Yh8NDY5THqBkLehp",
            "https://drive.google.com/uc?export=view&id=1NNLrTSTiQwqUz51RNHWf4ySFJ5fikYeZ",
            "https://drive.google.com/uc?export=view&id=1LzUxDf2VUbYXesCCTaxL-fKFlSumo3aD",
            "https://drive.google.com/uc?export=view&id=1dAzyguL5ttFFujGygfQvtZExJzPtotr9",
            "https://drive.google.com/uc?export=view&id=1Wygn3B9C7t87okH7wKYGiOwCReMIV4C_",
            "https://drive.google.com/uc?export=view&id=1kvPXYJD4eUsHGGymrMY-cqzfEVOn8e7E",
            "https://drive.google.com/uc?export=view&id=1yjI7IgMGRMYs284OdZWpUMBrNIvirJ2-",
            "https://drive.google.com/uc?export=view&id=1TOWuiDfCbHpccYrZG7VGUey-I-A2la82",
            "https://drive.google.com/uc?export=view&id=19dytdPKaybu8mB7rYoSVbd9wRPnJq3C-",
            "https://drive.google.com/uc?export=view&id=1kVDK2BmU0nEC5kJK8YkfiB4c3g-pDqCZ",
            "https://drive.google.com/uc?export=view&id=16BchNAcl9tMi9_dXyCLuombKokFkmbKb",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
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
                "alamat": "Jl. Senopati Raya",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            },
           {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Kulineran With May",
                "sosmed": "@azza.rrr_",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
           {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Kotabaru",
                "hobbi": "Hiking",
                "sosmed": "@rexanderr",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Jatimulyo",
                "hobbi": "Mancing",
                "sosmed": "@haikalsbln_",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
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
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Tanjung Karang",
                "hobbi": "Kulineran With Azza",
                "sosmed": "@mai_12",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Bersenandung",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kemampuan kakak dalam mencairkan suasana, kerenn,lucuuu,dan asikk.",
                "pesan":"Semangat selalu dan ceriaa terus yaa, Kak!"
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Abang sangat act of servis dalam kebutuhan suatu kegiatan, ramah dan baik",
                "pesan":"Semoga Abang selalu bisa menjadi motivasi Semangat terus!"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450107",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Musik",
                "sosmed": "@Sarahwsti",
                "kesan": "cantik dan ramah, Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semanggattt dan Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "1234450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda",
                "hobbi": "Main Rubik",
                "sosmed": "@zhrptsl",
                "kesan": "kerenn kak, 19 tahun sudah semester 5,kakak lucuu, dan ramah.",
                "pesan":"Semangat selalu kak dalam kuliah dan menjalankan program di internal, Kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iH0nqnzC2seAfFJVzXYRzferNx_MhE-w",
            "https://drive.google.com/uc?export=view&id=1zAuSBbQItxHXmNUoBkkWnPQZAXoLCJsU",
            "https://drive.google.com/uc?export=view&id=1Nwnxnz7VcwzyxINxBZcj-KYhkHWC61IA",
            "https://drive.google.com/uc?export=view&id=10CFG2qM3bDp0S2BxmcM8eV9DjMSdl0S3",
            "https://drive.google.com/uc?export=view&id=1ECuOqRNE43zrOHCoyJ3CMSQT9w3LOr1I",
            "https://drive.google.com/uc?export=view&id=1AGjXoxhrqYAFo2MiIAeKWl7dMqMbWqzG",
            "https://drive.google.com/uc?export=view&id=15yUiKTmsSUXC6xFQRyhW8oXEEd7oUiqL",
            "https://drive.google.com/uc?export=view&id=19_1QPF-pIivhhgmyM-xWmQ37L12LdZKQ",
            "https://drive.google.com/uc?export=view&id=1Sm5nARoivFIWmAkP5aKJujLUT8V10Soe",
            "https://drive.google.com/uc?export=view&id=1re2rFSyVAz9JlaHhMZMhanqaa7QGzOTE",
            "https://drive.google.com/uc?export=view&id=1VxnKIubj7q92WG1ulBXp8kHd11p4PFng",
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

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1V-4NXUOQjeZ4OPWu2lE-H8QT3xkEJ3fM",
            "https://drive.google.com/uc?export=view&id=1KVh1P5xwwZYF81BcGIrLoNbMNvmoWR5V",
            "https://drive.google.com/uc?export=view&id=1Kg9tVxxlMVQ2smgOFFt9uNrmeiz8vV_B",
            "https://drive.google.com/uc?export=view&id=1ObMh2GJZ8z8nF4NDgUCJIswy2X5yVdVB",
            "https://drive.google.com/uc?export=view&id=1zt-UvnKHoDVFC_QBSC5I8-rlnCVbYwu_",
            "https://drive.google.com/uc?export=view&id=1CtmArG-0rj4pPqibdGza_lUsaqpxmcp1",
            "https://drive.google.com/uc?export=view&id=1FEmWpmWinvEYOYuJyPDmJfYhGasXgOIr",
            "https://drive.google.com/uc?export=view&id=1EUBAfknMXzqAp2Y8FPrpiTVIS1JYgGJ-",
            "https://drive.google.com/uc?export=view&id=1mW_SCGXnJQ1QSXuegOhjHrF4lz9swyFF",
            "https://drive.google.com/uc?export=view&id=1ZZYRKmPhtN8i5cjfOoUe7EYbIB-NuKCO",
            "https://drive.google.com/uc?export=view&id=1-KqeAXxljcPAQAdMHAMZNBQcnm-rG4NA",
            "https://drive.google.com/uc?export=view&id=1iwm109rQt4ppRTU8YeXnhFDhV9X-o4-I",
            "https://drive.google.com/uc?export=view&id=14ywWUWqyYXRAGYfQNLpO-OBut0Xco86F",
            "https://drive.google.com/uc?export=view&id=1Jn0hsr7B4wpH_PTi8qqoccnfrTTAJOH5",
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
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "123456789",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Senang bisa kenal dengan kakak.",
                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
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
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Semoga kita bisa bertemu lagi."
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Sangat berkesan, orangnya humble.",
                "pesan":"Tetap jadi pribadi yang menginspirasi ! "
            },
            {
                "nama": "Renisha Putri Giani ",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Senang bisa kenal dengan kakak.",

                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Semangat terus dan jangan mudah menyerah!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Semoga kita bisa bertemu lagi."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Sangat berkesan, orangnya humble.",
                "pesan":"Tetap jadi pribadi yang menginspirasi!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Senang bisa kenal dengan kakak.",
                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Semangat terus dan jangan mudah menyerah!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Semoga kita bisa bertemu lagi."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XHtU4yAXd1rBJFdc6UgCe2hwnuTeoXbH",
            "https://drive.google.com/uc?export=view&id=1LVhaPuY8dRmjVFlyqGugCGs0AO7jsexd",
            "https://drive.google.com/uc?export=view&id=1UjBIdbSYyaXbw9Gut4Mq20945XAFodnG",
            "https://drive.google.com/uc?export=view&id=1wjcRrNzvfwUaeX-uemlGKMM-1hIkNu6h",
            "https://drive.google.com/uc?export=view&id=145pJS7Y4r1vM8HV7UBoaNbiAc1BYrJKq",
            "https://drive.google.com/uc?export=view&id=1OTpoGuEpu7ndb5U2YXKxvZXEfyK2m1hm",
            "https://drive.google.com/uc?export=view&id=1_viYyF4ZMVzgCft0ifqQbOzwJGX3XeBd",
            "https://drive.google.com/uc?export=view&id=1Ix0vYaz3lD4t-rIGV3r4jWiWVt4zwmMI",
            "https://drive.google.com/uc?export=view&id=17bgI8vLY3LpUUGWFIQj-aYVON19YmgxZ",
            "https://drive.google.com/uc?export=view&id=1DAKnc5qhoVqzunuJDUFVY4_i7Cn7gtaC",
            "https://drive.google.com/uc?export=view&id=1i19sW03wzTo_s-_f5zeTQeBdyHkB6K8M",
            "https://drive.google.com/uc?export=view&id=1bOM6-jttC--q0_EEo8Xm_bJbyvOVqcBK",
            "https://drive.google.com/uc?export=view&id=1L4WniT25EubaulNV5p9phmYIbVWEgcUR",
            "https://drive.google.com/uc?export=view&id=1LKBgKrtkIX5h0hwFqE09N-HSqq9DW1y6",
            "https://drive.google.com/uc?export=view&id=1_eu8klmdINYnLMcPsQkq50IH2ifEz6rl",
            "https://drive.google.com/uc?export=view&id=1g9QCpg4pA4U7VlRyLZURCY2I5Ci1pt-O",
            "https://drive.google.com/uc?export=view&id=1g7O4jGs7rx9hA5ENWOhgRovikUpZN4en",
            "https://drive.google.com/uc?export=view&id=1A1eVCR-DYVA-_wpmUVL9BnaVmPQ7yMre",
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
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

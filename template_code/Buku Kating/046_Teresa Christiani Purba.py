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
            "https://drive.google.com/uc?export=view&id=1c_2F_iGzRg2seugBGGI8JpBgzoneugV3",
            "https://drive.google.com/uc?export=view&id=1KrJI82A-1YmWrDKfmjq7usyyccns6HvK",
            "https://drive.google.com/uc?export=view&id=1cLruvxQNTZpa6kpOiH_7MvwLHR2mvVh-",
            "https://drive.google.com/uc?export=view&id=1bmdzvgOrJiECsmLpXYCyhEbbBtT2uRUP",
            "https://drive.google.com/uc?export=view&id=12U-_OOhExinyp-DeRuxKcrOu-Y-rlv2P",
            "https://drive.google.com/uc?export=view&id=10H0QsQhJRyaQkY6cJz62m2xsfOKkbjmC",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Kahim kerennn, baik, ramah dan asikk parahhh",  
                "pesan":"Jaga kesehatan yaa bang, semangatt terosss"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Baikk bangett  sih banggg, murah senyummm",  
                "pesan":"Jangann lupa minum air putih yyangg banyakk bangg"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabeth_",
                "kesan": "Kakanyaa lucuu poll, imutt",  
                "pesan":"Semogaa lancarr terus kuliahnya kakkk"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakanyaaa  manis bangett senyumannyaa",  
                "pesan":"GAS TERUSSS, semangattt yaa kaa"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "12245001",
                "umur": "19",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "asikkk parahh, selaluu  ceria  orangnyaa",  
                "pesan":"Sehatt sehatt yaa kaaa"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"kota Padang,Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Cute Jenderal",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakanyaaa baik bangettttttttttt",  
                "pesan":"Jaga kesehatannn yaa kakakuu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16iiYTgoXAs-ED16sa0bOVJW69xh0_OTe",
            "https://drive.google.com/uc?export=view&id=1uChi9Zkt9VUf6OUkwriEo2U1D60MPR_0",
            "https://drive.google.com/uc?export=view&id=1b3ZPQORiM4O9HazJMSSF_gwDqKWi3C8e",
            "https://drive.google.com/uc?export=view&id=1nhJPrBZUzLeXHQ70qpT23jRaxrisMRC2",
            "https://drive.google.com/uc?export=view&id=1VKD9MRa0_qGi-Y-GsTMrdyzKqZ-cJCB8",
            "https://drive.google.com/uc?export=view&id=19xz6rfSX9kQbwViIyj7RebcKjVcNviZw",
            "https://drive.google.com/uc?export=view&id=1RbnhnzWqSzhADufsS1bDN2QH55_RTSXZ",
            "https://drive.google.com/uc?export=view&id=1rxZsTCFNjqZEcHpXK2pPbWbXLFfIipHZ",
            "https://drive.google.com/uc?export=view&id=1mq49BX6idRdqAWBUq2BkcbLBgceCcIWs",
            "https://drive.google.com/uc?export=view&id=19NniOf_7kJjZ75V9-v2L-YtJuYvG18Pg",
            "https://drive.google.com/uc?export=view&id=18G8ll2_aaCJTiBPcpHu8RAYaCIz3F9WE",
            "https://drive.google.com/uc?export=view&id=1UX079iFdxnCUMme_stQ2kQ6kf0w5Nsuo",
            "https://drive.google.com/uc?export=view&id=1eyy1dlmXXJWRQASpXizy2ICRnWsLcJPH",
            "https://drive.google.com/uc?export=view&id=1CRCeeUcyFpT4ZDHGBcdbRYH6XoC0xubn",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Yapping",
                "sosmed": "@jeremia_s_",
                "kesan": "Asprakk terbaikk",  
                "pesan":"Tetapp semangattt"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit ",
                "sosmed": "@_.dheamelia",
                "kesan": "Cantikkk bangett kaa, manis, mukanya kaya abis mandi segerr",  
                "pesan":"Lancarr teruss kuliahnyaa kaaa"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Murah senyummm, humble banget",  
                "pesan":"Semangatt  kuliahnyaa kaa"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@anisafitriyani_",
                "kesan": "Kakanyaa imutt bangett",  
                "pesan":"Jangan luppaa minum air putih yangg banyak yaa ka"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Behh abanng ozt, keren bangett bangg",  
                "pesan":"Gass teruss bangg"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@fby.wlndr",
                "kesan": "Imupp bangett kakanyaaa",  
                "pesan":"Lancarr  teruss kuiahya ka"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Seru banget ngobrol sama kaka ini",  
                "pesan":"Jaga kesehatan yaa bang"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Kerenn banget  abang ini , vibes nya keliatan keren terus",  
                "pesan":"Jangan luppa minum air putih yaa bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakanyaa ramah banget, murah senyummm",  
                "pesan":"Semoga kakanya  diberi kelancaran terus sama Tuhan"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@j__eesie",
                "kesan": "Kakan kerenn banget bisa jadi duta genre ITERA",  
                "pesan":"Tingkkatkann teruss kaaa"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Gg.Sekuntum",
                "hobbi": "Main Pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnyaa lucu  banget, asik diajak ngobroll",  
                "pesan":"Tetaapp semangatt yaa bang!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Bang Yulius vibes-nya adem banget.",  
                "pesan":"Semoga selalu dikelilingi orang baik juga ya, Kak."# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tanjung",
                "kesan": "Gak pernah sombong padahal pinter banget.",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngajakin sahroni tiktokan",
                "sosmed": "@wannashwaa",
                "kesan": "Mentorr terbaikk, tercantikk, terimutt seiteraaa  rayaaa",  
                "pesan":"Jaga kesehatann yaa kakakkuuu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17kePFLb_zrkl3cVPEPpgLI5dpYD6pK-Z",
            "https://drive.google.com/uc?export=view&id=1hZkdChBX67wWH5_abigNsat_f1mw_mq1",
            "https://drive.google.com/uc?export=view&id=1OK4CTEQ8TH5kvJIkzOocvYtWUVxoWkM8",
            "https://drive.google.com/uc?export=view&id=1nJhCQcBfUEix9IpDgK_4Pi6b0f3B3ImP",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnyaa  kaya namanyaa twinkle bintang yang bersinarr terus",  
                "pesan":"Semangatt menjalani semester  akhir bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakanyaa kalemm banget, tenang kaya airr di danau",  
                "pesan":"Jaga keesehatan kaa, walaupunn dikejar ddeadline"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakartaa",
                "alamat": "Asrama TB 1",
                "hobbi": "Main ice skating",
                "sosmed": "@fathinahazizah",
                "kesan": "Kakaaa tutorr yang palinng the best forever",  
                "pesan":"Semangatt teruss jadi penutor ALE kamii kaaa"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret  belwis",
                "hobbi": "Rebahan",
                "sosmed": "@liahanaaa",
                "kesan": "Kakanyaa imutt bangett, senyumnyaa juga maniss",  
                "pesan":"Semangatt terus mennyamppaikan aspirasi kaaa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nBAVunNLwbR9sRF96ufkLUsi2mQOYMQq", #Ferdy Kevin Naibaho
            "https://drive.google.com/uc?export=view&id=1kfFTpdk8j4rzmfIAM6wc2gu5eddztCl6", #Nisrina Nur Afifah
            "https://drive.google.com/uc?export=view&id=1pzonN8oZfO4cmgC3kSPa3iH5oU81WOAF", #Allya Nurul Islami Pasha
            "https://drive.google.com/uc?export=view&id=1tapw7QTmDQFKpuW2wznrkUiIVek53Co4", #Ahmad Rizky
            "https://drive.google.com/uc?export=view&id=1cVoP2D-yGOXnqzfC8IFgH8bE3twouIEy", #Arienta Khusnul Ananda
            "https://drive.google.com/uc?export=view&id=1IIZEbghFyBJI3m31aq589L2ddJnrcpb-", #Daffa Hadyan Navista
            "https://drive.google.com/uc?export=view&id=1O1iJZshAApRevhbvB25FQ97drwqKSXiP", #Ginda Fajar Riadi Marpaung
            "https://drive.google.com/uc?export=view&id=15PPPg2WJ1wKvSk3XLAYJrFXkovzBuTpn", #Natasya Amavisca
            "https://drive.google.com/uc?export=view&id=1EAAzgvsTKy3oBAW44Brn4k1bUj-AMokm", #Nobel Nizam F.
            "https://drive.google.com/uc?export=view&id=1_9e-4S_nBcDQo-2yUnLaqbwstg4FS7FT", #Nurul Alfajar Gumel
            "https://drive.google.com/uc?export=view&id=1nfuaOS4QH8M4oQZUUQLALXT-pQu66lgb", #vany salsabila putri
            "https://drive.google.com/uc?export=view&id=1ReaM0hDPWgUSFg77-t6YoeUDfNrc-BmM", #Ahmad Sahidin Akbar
            "https://drive.google.com/uc?export=view&id=1jjsSKMMC02X7ZTCsAOO33LOjyMu-WDzr", #Ali Aristo Muthahhari Parisi
            "https://drive.google.com/uc?export=view&id=1ZXyQ6dOFXvLoEXJKYdBnFDLqB1C4S-wB", #Gusti Putu Ferazka
            "https://drive.google.com/uc?export=view&id=1RcyXaA_JosHyH4BdDzfSo48UXCSzS2_L", #Kharisma Mustika Sari
            "https://drive.google.com/uc?export=view&id=1rUTDXmZlACp9Mr5mIMVv2TRTo9UtxGGw", #Rosalia Siregar (belum ada foto)
            "https://drive.google.com/uc?export=view&id=1aq3PchLqaZ0TpOK40R5nRiqJaro2jGAa", #sahid maulana
            "https://drive.google.com/uc?export=view&id=1RpzO1o821orRsGrx7sBi08mlTSmL0sya", #Daffa Ahmad Naufal
            "https://drive.google.com/uc?export=view&id=19AwXQfrQqy71OChneuyYKzrstoJ9qaDd", #Erma Daniar Safitri
            "https://drive.google.com/uc?export=view&id=1_2XPnsxG1DutdrvkQF4qiv8oLgNOg67M", #Ihsan Maulana Yusuf
            "https://drive.google.com/uc?export=view&id=10hItvyIIKT0O0vE8WaSfFPJji5nesDKx", #Kevin Antoni Junior
            "https://drive.google.com/uc?export=view&id=1zWP9kYIemXeE1vKtf2ZY8v7wzBxLYPdT", #Lidia Natasyah Marpaung
            "https://drive.google.com/uc?export=view&id=1MYAkHbqQC2Q4ZZfM3_gf--p0pKeAIv9q", #Muhammad Ridwan
            "https://drive.google.com/uc?export=view&id=1pA19jRqK2MfTJezvs7zLmnb2KRTleoni", #Benget Sidabutar
            "https://drive.google.com/uc?export=view&id=1PgBb3cVnKpYl8041K2IAB7MtAZSHOkDv", #Uliano Wilyam Purba
            "https://drive.google.com/uc?export=view&id=1wyvALcrYvuKaDK4_gDF91Lf9FxTLvDEg", #Rewina Audrya Melva Sari
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
                "nama": "Allya Nurul Islami Pasha",
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
                "nama": "Ahmad Rizky",
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
                "nama": "Arienta Khusnul Ananda",
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
                "nama": "Daffa Hadyan Navista",
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
                "nama": "Ginda Fajar Riadi Marpaung",
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
                "nama": "Natasya Amavisca",
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
                "nama": "Nobel Nizam F",
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
                "nama": "Nurul Alfajar Gumel",
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
                "nama": "Vany Salsabila Putri",
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
                "nama": "Ahmad Sahidin Akbar",
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
                "nama": "Ali Aristo Muthahhari Parisi",
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
                "nama": "Gusti Putu Ferazka",
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
                "nama": "Kharisma Mustika Sari",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1N-nR92cEa2_HSP0ultWh3Y6MrBcj5mUj",
            "https://drive.google.com/uc?export=view&id=1FhkbGRP3L0oiQtyEwOnlPKHjbHeL-TpD",
            "https://drive.google.com/uc?export=view&id=1K28PKAiKJUu0UFyHB-h1w0t8I1HjF3As",
            "https://drive.google.com/uc?export=view&id=1ZcqLKbdrxo12EqRdKue9myv3S5WzIjK5",
            "https://drive.google.com/uc?export=view&id=1tu2FtHJyfW-qiZrhCL2PRyZEjs0PumRw",
            "https://drive.google.com/uc?export=view&id=1Df7tZvXxcRQjQ5TVXuWQszpT-8HxuA8L",
            "https://drive.google.com/uc?export=view&id=1ezPRRN9A4eRSbYjIUoOb1FmPKnEZdRCp",
            "https://drive.google.com/uc?export=view&id=1ofHk_DPspQ4nK30jzALDn1gA3Tb8i47F",
            "https://drive.google.com/uc?export=view&id=1IULf_NROsBF49HEHhNIk1LNqusOgU71C",
            "https://drive.google.com/uc?export=view&id=13eV8-2jbzyfGOu3UoR8RZw3zY0ARPzJH",
            "https://drive.google.com/uc?export=view&id=1YY-W4GY7Afqa1F2HAMnZY0Fdrf3E3GJj",
            "https://drive.google.com/uc?export=view&id=18UXb3Nz6CzLvY4qVEbn5xBby5uPzxcFL",
            "https://drive.google.com/uc?export=view&id=134BupekX4pvptWbya8aCU3lsSwk5Vbg3",
            "https://drive.google.com/uc?export=view&id=15R1EJ9rx7JJWkWDymtOJ6tKYPE3-C90E",
            "https://drive.google.com/uc?export=view&id=1huZoGxMxeEEglv7naUHzhrhh-zboA3D0",
            "https://drive.google.com/uc?export=view&id=1s5DCQNIFJi_BcnXGmcI8Syfkmp_Udfg5",
            "https://drive.google.com/uc?export=view&id=1CZpyYC1z-PPa7kxhMk7F_dB0qrDv9XZs",
            "https://drive.google.com/uc?export=view&id=1FgmD36zbg6BNUBZALJk_-uo_VVWEVUwd",
            "https://drive.google.com/uc?export=view&id=1Lb7vEYi9FcMzwendriPIETizI4mxclIw",
            "https://drive.google.com/uc?export=view&id=1sd7j3mU15yns28Ur68twEbzXjA2Af2R3",
            "https://drive.google.com/uc?export=view&id=1cdS9Livypyx6cTIdaSTuHMQiBf6NBid2",
            "https://drive.google.com/uc?export=view&id=1AIP73L2iETzkKMr7AidN67VyQrvib-gi",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123340083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@randaandriana_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep . Riau",
                "alamat": "Nangka 3",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Jl.Permadani, Sukarame",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "18",
                "asal":"Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "18",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@notfall.s",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, Bandar lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@keyashafi_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "18",
                "asal":"Lampung Selatan ",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
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
                "nama": "Fairuz Ary Syifa",
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
                "nama": "Tanty Widiyastuti",
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
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KUOFRw6vv3ur-vmv79xCOdxim80N80wx", #Arafi Ramadhan Maulana
            "https://drive.google.com/uc?export=view&id=14wo3H0DrTM8jfreejiAXLOn42Z9UTgcZ", #Yohana Manik
            "https://drive.google.com/uc?export=view&id=1BIVOiJJnM8w96eTR78tDt5mWBdAi9T9P", #Ratu Keisha Jasmine Deanova
            "https://drive.google.com/uc?export=view&id=1m_E57NOtfdBOxYUTLy6hef2Yaj4uqB2W", #Arini Puteri Elandra
            "https://drive.google.com/uc?export=view&id=1mlAmHYJ6q3LHImzMAPX-HRQo_iPVTRiG", #Arya Muda Siregar
            "https://drive.google.com/uc?export=view&id=1XqsTZvkyGFVgZ_LECF7OQqGOKBgFXsog", #Khoirul Muttoharoh
            "https://drive.google.com/uc?export=view&id=1AZA2A1YvofWmwGrFJppJs6aRnILXg8L4", #Lutfia Aisyah Putri
            "https://drive.google.com/uc?export=view&id=1DPwYHeI-n6AXiWRPXGr3E6Pso01bnjD0", #Nabyla Sharfina
            "https://drive.google.com/uc?export=view&id=1IQZTNxkMNaMcZ2RAw8PCRrzxFZyvR8VE", #Syahrialdi Rachim Akbar
            "https://drive.google.com/uc?export=view&id=1rVDV6bJkjbDoCi4S84VLxgwkuNAzMFUa", #Dea Mutia Risani
            "https://drive.google.com/uc?export=view&id=1N9ZawAmOAo4Os3n68u03dUu8MIfBanbe", #Cindy Laura Manik
            "https://drive.google.com/uc?export=view&id=1W3Jggv9oSb0i43w08O2SSJNEKf3YspcK", #Dea Amanda
            "https://drive.google.com/uc?export=view&id=1x9t_7oDG6_cjHNEUsNB673vvEKxpvvWN", #Desman Velius Halawa
            "https://drive.google.com/uc?export=view&id=1dV7urLBohuYdfRPHTKnw5U-sqlhcSQYI", #Devyna Sonya Palupi Sanjaya
            "https://drive.google.com/uc?export=view&id=18nz9WghzIAyrrZB1W0TsQ_oThVUs4A08", #Luthfia Laila Ramadhani
            "https://drive.google.com/uc?export=view&id=1f-89S-dVeiajDgJKzxUgGooFacP3lkzH", #Irvan Alfaritzi
            "https://drive.google.com/uc?export=view&id=1jwyZ94GPsqdri_eNdfJQ8YFGtDCDNDIk", #Aditya Taufiqurrohman
            "https://drive.google.com/uc?export=view&id=1IM5WdNpjbsw0-QnIp2hku9W5KmLCaWZP", #Fathya Intami Gusda
            "https://drive.google.com/uc?export=view&id=1zyMtCkyjQBYFY3lG66Dm3jR-mAfaWLaW", #Khazanatil Ilmi
            "https://drive.google.com/uc?export=view&id=1FZxBm7j7-_BNfrKt6eYXN1QKVUkb1_OA", #Melinza Nabila
            "https://drive.google.com/uc?export=view&id=1DQoolBob6w7k-fqZNLVMwwa4vG7eAZ5J", #Nayla Shafira Roza
            "https://drive.google.com/uc?export=view&id=1BXh5zDsQuKTrHk6kZEDBTSI4_c5snzak", #Nurul Izzah Istiqomah
            "https://drive.google.com/uc?export=view&id=10fnsxyXjv5e4uh8IFkMoGQVSMAdc3k39", #Qois Olifio
            "https://drive.google.com/uc?export=view&id=14QIlilAPwgxSp4GIlqQdb8TxceSYkGb0", #Tarisya hidayatul rahmi
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "12240093",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()
elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qcH8kLzT-iFC3SA-yH71cRXYNBWn0cVY", #Rani Puspita sari
            "https://drive.google.com/uc?export=view&id=1YxTXVVtEOq6c5PFkLxf4RPsocA3ND48N", #Renta Siahaan
            "https://drive.google.com/uc?export=view&id=1kTubYYUVaOUOjqUdjwhNDvh08nSnpdGw", #Salwa Farhanatussaidah
            "https://drive.google.com/uc?export=view&id=1UEZTsHznF9R1oYAhzqA4Oi2BIox3mziC", #Azzahra Putri Kamilah
            "https://drive.google.com/uc?export=view&id=1olzGITzFGiq6PkMsn88f1KwRO70ax4P8", #Haikal Fransisko Simbolon
            "https://drive.google.com/uc?export=view&id=1jTuP60HJZ6y4OaN5AInIhh_oCU4GHmPM", #Iqfina Haula Halika
            "https://drive.google.com/uc?export=view&id=1WP5Hngx2sF0ZCe3fUA9DXoOqPgUd1F0H", #May Talitha Dahlia
            "https://drive.google.com/uc?export=view&id=1bfe7SA2idxO41Yxgrab6xig7GjAiJKLe", #Muhammad Naufal Alghani
            "https://drive.google.com/uc?export=view&id=1nPnrMLLIYR1116FRdjPI5Qtgw6eMh2c5", #Zailani Satria
            "https://drive.google.com/uc?export=view&id=17T6oWyDD8cs-1eOYbbGIn1v4VNrTcw_I", #Rendi Alexander Hutagalung
            "https://drive.google.com/uc?export=view&id=1-iMFAhtkibIXqd8hDVN9BCt2_CJOK1Lo", #Hanna Gresia Sinaga
            "https://drive.google.com/uc?export=view&id=1si8O_ydBJCOf9GCHCFqk3OcdLKPRSWR0", #Keren Marito Lumban Gaol
            "https://drive.google.com/uc?export=view&id=1Lo-zw9rwVL_4ANX1PDTA4q0CW9WjHmGz", #Muhammad Hanif Dzaky Arifin
            "https://drive.google.com/uc?export=view&id=1iaQXdb3PIXj2U4U2qXXWCKE8c27_rhSU", #Sarah Wasti
            "https://drive.google.com/uc?export=view&id=1OigExG5Lk3_i0RDINb1PFFXfEEH81B3U", #Zahra Putri Salsabilla
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
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
                "nama": "Renta Siahaan",
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
                "nama": "Salwa Farhanatussaidah",
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
                "nama": "Azzahra Putri Kamilah",
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
                "nama": "Haikal Fransisko Simbolon",
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
                "nama": "Iqfina Haula Halika",
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
                "nama": "May Talitha Dahlia",
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
                "nama": "Muhammad Naufal Alghani",
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
                "nama": "Zailani Satria",
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
                "nama": "Rendi Alexander Hutagalung",
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
                "nama": "Hanna Gresia Sinaga",
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
                "nama": "Keren Marito Lumban Gaol",
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
                "nama": "Muhammad Hanif Dzaky Arifin",
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
                "nama": "Sarah Wasti",
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
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Xrj-XOH52uhaR5LPMNSZlmuiz8vDh6LF", #Danang Hilal Kurniawan
            "https://drive.google.com/uc?export=view&id=1TEq_NOtHC1iLWaxHLkhLVybC7r6i21vA", #Syalaisha Andina Putriansyah
            "https://drive.google.com/uc?export=view&id=1XAmM4JkF1YrBfqnhEDnCehRAlmRnnPqe", #Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=1P9PvP02aB9P7SZL-7ioBOge7xJNxJC1d", #Anadia Carana
            "https://drive.google.com/uc?export=view&id=1OtJ85ltLu42BkBox0VVuKjffs-LaTL39", #Aprilia Dewi Hutapea
            "https://drive.google.com/uc?export=view&id=1x2N2z1IpZQdr4azz0eOyHuBA0D-HXFCn", #Nabila Zakiyah Zahra
            "https://drive.google.com/uc?export=view&id=13Y9Df9W8sOYyLQpGToG8HoUMP24m9Wn7", #Dhafin Razaqa Luthfi
            "https://drive.google.com/uc?export=view&id=1PgF9SkwGTKuFLiHCycjNhj04Q9Rl4_fv", #Devi Rahayu
            "https://drive.google.com/uc?export=view&id=19cmKL90K5REukuaOF3S59Rs3P9VqSA_R", #Enggli Rahmadhani
            "https://drive.google.com/uc?export=view&id=1HMvCnguKk8U9HVyZ2hPUge-HPnwVB3QH", #Hanifah Inaya Sani
            "https://drive.google.com/uc?export=view&id=1V09alEH-h87o-BnTnMf_hRcf2EAzgQkA", #Nydia Manda Putri
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
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
                "nama": "Syalaisha Andina Putriansyah",
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
                "nama": "Ahmad Rizqi",
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
                "nama": "Anadia Carana",
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
                "nama": "Aprilia Dewi Hutapea",
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
                "nama": "Nabila Zakiyah Zahra",
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
                "nama": "Dhafin Razaqa Luthfi",
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
                "nama": "Devi Rahayu",
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
                "nama": "Enggli Rahmadhani",
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
                "nama": "Hanifah Inaya Sani",
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
                "nama": "Nydia Manda Putri",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()
elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iKn45RTFt11Bl2QFLlg0nFAY4U-pYIHD", #Patricia Leondrea Diajeng Putri
            "https://drive.google.com/uc?export=view&id=10mtwIk6sSj0lc2oGB8Fa_i9pVllkIHjP", #Rahma Neliyana
            "https://drive.google.com/uc?export=view&id=18_g5QMBYDkyEGAtPyWp024i36PlOzT_u", #Khoirul Anam
            "https://drive.google.com/uc?export=view&id=1UFyl-NndaCmVdrBzcvzlXkDynRWyNKBG", #Labo John Noel Napitupulu
            "https://drive.google.com/uc?export=view&id=1tt-D2eobfOOmuGswv30J1xRqL2Xoj4AV", #Rafi Diva Efangga
            "https://drive.google.com/uc?export=view&id=1l_nKIn0Mbqir_gmZFgHRn2Jt_Nmgnjoi", #Refa Destiny Pranata
            "https://drive.google.com/uc?export=view&id=1DvVN5lDkhyAAMzEvPZEFd03Aoj9VqmFM", #Try Yani Rizki Nur Rohmah
            "https://drive.google.com/uc?export=view&id=1D3NwgwlfQ7zAU5Ryu1ArtNAcryLJKYnG", #Aliya Ammara Ananta
            "https://drive.google.com/uc?export=view&id=1IHHDcVeqPvkhhn58GIwY9_QWLz1E_mx5", #Donna Maya Puspita
            "https://drive.google.com/uc?export=view&id=1WhKtFYYMVra3NkVU1mY0j5Sm3j96mX7k", #Feby Angelina
            "https://drive.google.com/uc?export=view&id=1ot-SYJn8DAdG8yxjbB4GsRNtv5n6GZ3Z", #Hafsa Fazila Arradhi
            "https://drive.google.com/uc?export=view&id=1l80o4pctgaAxFffyFiw5KDH0oyH64oev", #Nayla Salsabila Fathianisa
            "https://drive.google.com/uc?export=view&id=1J6c_Z4hVdCq2oMoXVffCasdUcFHr3Se_", #Sania Dwi Ayu Lestari
            "https://drive.google.com/uc?export=view&id=1TEMbQwpMW4Cfj4fcPc_MAKq9lm65iiBy", #Akmal Faiz Abdillah
            "https://drive.google.com/uc?export=view&id=1UDmXlkK6Rr79wkFRF-1SK7Qv1R8gu1ba", #Raihana Adelia Putri
            "https://drive.google.com/uc?export=view&id=1Zu5Q7yJEmH6u-OK9mevYm-5Xs9cD_DLm", #Citra Agustin
            "https://drive.google.com/uc?export=view&id=16_TCCyzLo99Xdjp2J8A2n0LlsPaE3JKQ", #Eigi Artamevia
            "https://drive.google.com/uc?export=view&id=1IQpx7MYOJ0gSAMmXpY23tOZDPxOWdW1q", #Romauli Oktavia Silaban
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
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
                "nama": "Rahma Neliyana",
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
                "nama": "Khoirul Anam",
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
                "nama": "Labo John Noel Napitupulu",
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
                "nama": "Rafi Diva Efangga",
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
                "nama": "Refa Destiny Pranata",
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
                "nama": "Try Yani Rizki Nur Rohmah",
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
                "nama": "Aliya Ammara Ananta",
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
                "nama": "Donna Maya Puspita",
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
                "nama": "Feby Angelina",
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
                "nama": "Hafsa Fazila Arradhi",
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
                "nama": "Nayla Salsabila Fathianisa",
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
                "nama": "Sania Dwi Ayu Lestari",
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
                "nama": "Akmal Faiz Abdillah",
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
                "nama": "Raihana Adelia Putri",
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
                "nama": "Citra Agustin",
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
                "nama": "Eigi Artamevia",
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
                "nama": "Romauli Oktavia Silaban",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan

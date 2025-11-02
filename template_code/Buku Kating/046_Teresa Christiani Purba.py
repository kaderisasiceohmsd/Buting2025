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
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Sukarame",
                "hobbi": " jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakanyaa manis  bangettt, suka liat kalau kakanya  senyum",  
                "pesan":"Semanagatt teruss kuliahnyaa  yaa kaa!!!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakanyaa super duper baikkkkk",  
                "pesan":"Semangatt menjalanii harinyaa yaa kakakuu !!!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Behh abang yang satu ini keren bangettt uda jadii sekjen pplk",  
                "pesan":"Jangann lupa tetap jaga kesehatann ya bangg"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main BlockBlast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kaknnyaa baik banget murah senyum  jugaa",  
                "pesan":"semangatt menjalani semester kuliahnyaa kaaa"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Orang",
                "sosmed": "@daffahdynn_",
                "kesan": "Abangnyaa  lucu, asikkk ga sombong",  
                "pesan":"Semangattt dterus bang jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "GH Belwis",
                "hobbi": " Badminton,",
                "sosmed": "@ginda_mrp",
                "kesan": "Abangnyaa ramah bangett seriusss",  
                "pesan":"Jangan luppa minuum air putihh yaa bang"# 1
            }, 
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "kakanyaa imutt, lucuuu dan asikk",  
                "pesan":"Sehatt selaluu kkak!"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekabaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel baikk banget, apalagi pas jadi asprak pks kami",  
                "pesan":"semangat teruss ya bangg"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Asprakk terbaikkk",  
                "pesan":"Naikinn nilai praktikum ADS pliss bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakanyaa asikk poll",  
                "pesan":"Jagaa kesehatann ya kaa!!!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Abangnyaa murahh senyum baik bangett",  
                "pesan":"Jangan lupa minum air  putihh bangg!!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnyaa kece badai",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakaa nim kuu, cantik baik,  ramah ",  
                "pesan":"sehatt teruss yaa kakaa!!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scrooll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakanyaa lucu imutt bangett",  
                "pesan":"semangat terus kuliahnya kakakuuu !!!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakanyaa  immutt, humble baik",  
                "pesan":"Pendidikan memang nomor satu, tapi jangan lupa jaga kesehatan yaa ka !!!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahidmaulana",
                "kesan": "Abangnya  waktu wawancara baik bangettt",  
                "pesan":"Jangan pernah menyerah bang, tetap  semangat"# 1
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Abbangnyaa asikk plus seru banget, berwibawa juga",  
                "pesan":"Jangan lupa jaga kesehatann yaa bang"# 1
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
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakanyaa maniss, cantikk, baik rammah pake lengkapp",  
                "pesan":"Tetap semangatt jangan menyerahh kaa"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Abangnya  humoris, humble, lucuu",  
                "pesan":"Apapun yang terjadi tetap seperti ini yaa bang"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "19",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Abangnya keliatann garangg, tternyataa baik bangeett",  
                "pesan":"Tetap jadi oorang baik yaa bang  selamanya"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakanyaa imutt bangett , ramahhh",  
                "pesan":"Semogaa lancar  terus kuliahyaaa kaka cantiii !"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Bang benget  asikk orangnyaa, humble",  
                "pesan":"Bahagia selalu yaa bang, dilancarkan segala urusannya"# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano",
                "sosmed": "@ullianowlm",
                "kesan": "Kagett ternyata semarga sama bang  Ulianoo",  
                "pesan":"Sehat sehatt bangg, jangan lupa  minum airr putih"# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakanyaa aktif banget  keliatan disemua kepanitian",  
                "pesan":"Tetap semangattt kakaaa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17mdDn8CSd_t5FhPy7t4iajQoIUPbfJLS",
            "https://drive.google.com/uc?export=view&id=1xV7YYX9nu_GWSAiYj3_q-9wXLjg45bXi",
            "https://drive.google.com/uc?export=view&id=1Oa95aIU-dzCcXqk1y82ulsWmDAsNea4d",
            "https://drive.google.com/uc?export=view&id=1nF5gHfefZMRMXqmqYRpa4DxrX57aZsdX",
            "https://drive.google.com/uc?export=view&id=1-wS-a4e120E6uN78ceP2eV9Ztki0s14H",
            "https://drive.google.com/uc?export=view&id=1gI1gQTjdDS6INtrFqEMo055gd_VcFIOj",
            "https://drive.google.com/uc?export=view&id=1t0vZjKIVx6eQmaL4lTgOkYxIfxBV_AuO",
            "https://drive.google.com/uc?export=view&id=160eWonIk8pXTq6-V_TQ2NmsgFreoAYrV",
            "https://drive.google.com/uc?export=view&id=1Ery0Eeaynd3eaOhZxOfQhhUFDJ0v-nGU",
            "https://drive.google.com/uc?export=view&id=1otazR0mxW658nOyWWlZWfIAtnBQ77rtd",
            "https://drive.google.com/uc?export=view&id=1L3oVPQoTQWAXU0wqL-KobWBF0KocRxpt",
            "https://drive.google.com/uc?export=view&id=1L1IWAS9vzrS-oQSRP1RLE49g9VJWdTTa",
            "https://drive.google.com/uc?export=view&id=1mZalV9N-a4ggUUdkJ9VwFvRe5XKBh4k2",
            "https://drive.google.com/uc?export=view&id=1Xn1hpgbSviv75D5jnL7s6vvSqO9y6-Z5",
            "https://drive.google.com/uc?export=view&id=1a78_rvyD8Wmsok9Fl8o9feoaVabHbIVV",
            "https://drive.google.com/uc?export=view&id=1MEAvr2cNyEVJHeVMxVKCnnbFocjtGXKK",
            "https://drive.google.com/uc?export=view&id=1THZ_Anrt-xxbtaCwTOwQOHtEx6-55bpI",
            "https://drive.google.com/uc?export=view&id=15blr8-GjTxL7AcIVNXFjbhu4kdKvDwXy",
            "https://drive.google.com/uc?export=view&id=1pqdDOlmYuj6ypiXbMkThxsntUmF0OtWg",
            "https://drive.google.com/uc?export=view&id=1DXghgiovVkHZRv9J3fbQkFxE75IgY5X8",
            "https://drive.google.com/uc?export=view&id=14jJrIdMKtCaKIekpgrh6_WTAGFvTThdR",
            "https://drive.google.com/uc?export=view&id=1lGwUvb0W1t492QzL4eWzAryzByJfFdUD",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123340083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya cara ngomongnyaa jelas bangettt",  
                "pesan":"Jaga kesehatan yaa bang"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep . Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca abstrak jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakanyaaaa murah senyumm, terus enak diajak  ngobrol",  
                "pesan":"Jangan lupa minum air putih yang banyak kaa"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Jl.Permadani, Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnyaa keceee badai, kerenn",  
                "pesan":"Semangatt terus kuliahnyaa yaa kaa"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakanyaa imuttt bangettt, seru dan ramahhh",  
                "pesan":"Tetapp semangatt dan terus berkembang kaaa"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnyaa keren bisa jadi  duta genreee",  
                "pesan":"Tetappp kerenn terosss"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnyaa asik, seruu dan enaak diaajak ngobrolll",  
                "pesan":"Tetap jaga kesehatan yaa bang"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik,",
                "sosmed": "@notfall.s",
                "kesan": "Abangnyaa kerenn, jagooo ngodingg",  
                "pesan":"Semangatt teruss kuliahnya bangg"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakanyaa baikk, humble dann selalu ceriaa",  
                "pesan":"Jangan lupa minum air putihh yang banyakk kaa"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakanyaa keren banyakk hobinyaa",  
                "pesan":"Teruss semangatt dann tetap ceriaa yaa kaa"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, Bandar lampung",
                "hobbi": "Dengerin musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnyaa kaem tapi tetap seruuu",  
                "pesan":"Semogaa kuliahnyaa diilancarkannn"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "18",
                "asal":"Lampung Selatan ",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakanyaa lucuu banngettt",  
                "pesan":"Semangatt teruss yaa kaaa kuliahnyaa"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakanyaa seruuu bangettt, asikk , cantikk",  
                "pesan":"Jaga kesehhatann yaa kaakaa"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main piano dan menyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakanyaa lucuu, imuttt",  
                "pesan":"Jangan lupaa minumm airr putihh yaa ka"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakanyaa cantik, kalem tapi tetapp asikk",  
                "pesan":"Jaga terus kesehatanyaa yaa ka"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Keren banget  kalau kakanya  nge mc",  
                "pesan":"Semangkaa eh semangatt  teruss yaa kaa"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abangnyaa ramah banget murahh senyummm",  
                "pesan":"Jangan lupa banyak minum air putiih yaa bang"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakanyaa baik, ramah , dan murahh senyumm",  
                "pesan":"Jangan lupa minumm air putihh yaa kakaaa"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Main game",
                "sosmed": "@biokcb",
                "kesan": "Abangnyaa seruu pokoknyaa",  
                "pesan":"semangat menjalannii semsterrnyaa bangg!!!"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "OZT kerennbangett siihh bngg",  
                "pesan":"semogaa meningkatt terus prestasinya bangg"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Mainn catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakanyaa imuttt bangettt",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "kakanyya vibes wanita karir",  
                "pesan":"jangan lupa jaga kesehatan yaa ka!!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Bangg razin mirip pakk tirtaa, kerenn",  
                "pesan":"Semangattt teruss bangg!!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1B82GZrNsmlm07KUfCk2rUgh0IyLqNVJx", #Arafi Ramadhan Maulana
            "https://drive.google.com/uc?export=view&id=1z8FJeGu3J4ieWrf2EaUuWzx3zTV6Jwvj", #Yohana Manik
            "https://drive.google.com/uc?export=view&id=16Nm0HpBb4B9fiLqqVBrpWbkIZ00JCAvQ", #Ratu Keisha Jasmine Deanova
            "https://drive.google.com/uc?export=view&id=11spKFc8u67-dR0EHXXNdlMFfwX5WqJqR", #Arini Puteri Elandra
            "https://drive.google.com/uc?export=view&id=1j0PhGtc3BrWGTuaL417onqmDD2tEigae", #Arya Muda Siregar
            "https://drive.google.com/uc?export=view&id=1Yh6gOD-N1u650XWpo2F4TYK4CGh4I3hO", #Khoirul Muttoharoh
            "https://drive.google.com/uc?export=view&id=1q2wbDyXv38yziHEPFP0N_iz6KkhyELFF", #Lutfia Aisyah Putri
            "https://drive.google.com/uc?export=view&id=10vtlrduy7AJyjLjxzy7U28hLXuGFmrXD", #Nabyla Sharfina
            "https://drive.google.com/uc?export=view&id=1-1hwlweOY5j7HW_lFiEx3MnNiWkeLW04", #Syahrialdi Rachim Akbar
            "https://drive.google.com/uc?export=view&id=16RtpylHsCoUN9TfKbXxUHVQo3wQ2-IpX", #Dea Mutia Risani
            "https://drive.google.com/uc?export=view&id=1ExxhtAe0KyQjXW7RoAJBE--slDD3Yuen", #Cindy Laura Manik
            "https://drive.google.com/uc?export=view&id=1X0lFMdMWgkdZPO7glfd-x0sAfuKeHl49", #Dea Amanda
            "https://drive.google.com/uc?export=view&id=1atu9MHuy-iL4LYe2CkzFR55L2VeiiUqJ", #Desman Velius Halawa
            "https://drive.google.com/uc?export=view&id=1m3Ck-NCa0sbCyD5qlLOX-MEWruYGGWUE", #Devyna Sonya Palupi Sanjaya
            "https://drive.google.com/uc?export=view&id=1Wix_gAa7kxp36XfPH95lw6QflNIyyDmQ", #Luthfia Laila Ramadhani
            "https://drive.google.com/uc?export=view&id=1v9CXL0SUdr46KhpfEvOae4FpxLk6n3kR", #Irvan Alfaritzi
            "https://drive.google.com/uc?export=view&id=1g7zXc8opvDrx_rRf-iZ1RFFL-pMy0gAs", #Aditya Taufiqurrohman
            "https://drive.google.com/uc?export=view&id=1mqABW1JiS_S3X2BGhvkhZWjkA1RXlFI7", #Fathya Intami Gusda
            "https://drive.google.com/uc?export=view&id=1hYpeSyNZC7675Pg1mDkO2H2aSMX2J5ok", #Khazanatil Ilmi
            "https://drive.google.com/uc?export=view&id=17jntrRCNqkSMjGXHar1fx1EvTQEM7x_N", #Melinza Nabila
            "https://drive.google.com/uc?export=view&id=1HBlUXUUqQTMJ275a3tmWbJYylbBEZmv_", #Nayla Shafira Roza
            "https://drive.google.com/uc?export=view&id=1-a6IwGCBuzU5AOSKeGVhF9MZc9HWiRck", #Nurul Izzah Istiqomah
            "https://drive.google.com/uc?export=view&id=1JgDJ2lNN4zVB78xjAuZMJ_KL2s3feKwf", #Qois Olifio
            "https://drive.google.com/uc?export=view&id=1ojAYsir5DwaA2U-Y15V_tonrMq8FGsGn", #Tarisya hidayatul rahmi
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnyaa asikk orangnyaa, humble",  
                "pesan":"jangan luppa minum air putih yaa bang!!!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl.  idup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "cantikk bngtt Kakanyaa ",  
                "pesan":"Jangann lupa minum air putihh ka !!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakanyaa maniss bangettt",  
                "pesan":"semangat terus kaa !!!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan jalan",
                "sosmed": "@elandraa_i",
                "kesan": "Kakanyaa asikk powlll",  
                "pesan":"Jangann lupa minum air putih yang banyak kka"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnyaa seruu bangettt",  
                "pesan":"Semangatt teross bangg !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung barat",
                "alamat": "Sukarame",
                "hobbi": "Mainn mainn",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakanyaa cwantikk polll",  
                "pesan":"Jagaa kesehatannnya yaa kaa !!!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "18",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari datase",
                "sosmed": "@lutfiaisyh",
                "kesan": "Aselii kakanyaa maniss bangettt",  
                "pesan":"Semangatt kakaa!!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakanyaa imutt bangett, ngeliat kakanyaa jadi ingatt adikku terus mirip bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
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
            "https://drive.google.com/uc?export=view&id=1v8RIkTvF5n-0Q1GdwTPX_5IRN9yQ0-rX", #Rani Puspita sari
            "https://drive.google.com/uc?export=view&id=1Vnp2wMrie4MDq4_Q8Qi7aFEaV-eMoZiW", #Renta Siahaan
            "https://drive.google.com/uc?export=view&id=1yyRVbJKt-S474Cug9QuYLnBhyaWBtJE4", #Salwa Farhanatussaidah
            "https://drive.google.com/uc?export=view&id=1S7SFzR4-qIugoSfcC0S-nViNhc2EORW2", #Azzahra Putri Kamilah
            "https://drive.google.com/uc?export=view&id=1jQaYyaC-Oj-TUw2spitvvx8NGf2zdWqN", #Haikal Fransisko Simbolon
            "https://drive.google.com/uc?export=view&id=1wjqs4Pc9g7cUBqbTqgFSc49r1AXpZhzF", #Iqfina Haula Halika
            "https://drive.google.com/uc?export=view&id=1_KLtFdnuE85uIbwJwZFNPvMWxrsC2bhv", #May Talitha Dahlia
            "https://drive.google.com/uc?export=view&id=1dyK1i5VBzq3-SWYVLXV9Lldrc3PpJmub", #Muhammad Naufal Alghani
            "https://drive.google.com/uc?export=view&id=1pa0mB_UyHOZ60obtNvjjkNfawFnmbgI0", #Zailani Satria
            "https://drive.google.com/uc?export=view&id=1wgaOqqK0FZX3GbRH0W1tjm5XuDtPk1DG", #Rendi Alexander Hutagalung
            "https://drive.google.com/uc?export=view&id=19m5t9RWZ4MUntsHZ9kKWkVln496g_h-P", #Hanna Gresia Sinaga
            "https://drive.google.com/uc?export=view&id=1wAYKnmnwM8v-KRVkNKXuo3pmWwkNCUAq", #Keren Marito Lumban Gaol
            "https://drive.google.com/uc?export=view&id=1CvL2ED3iXkzBWkFtZT4_p1ui3J_7w4u4", #Muhammad Hanif Dzaky Arifin
            "https://drive.google.com/uc?export=view&id=1CG_WnurJZGTYQCgiErmN05xC9IJ1YceY", #Sarah Wasti
            "https://drive.google.com/uc?export=view&id=1wBAbHDGImTZp_8nkk7jonReI1k_8ZHGR", #Zahra Putri Salsabilla
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
                "kesan": "Kakanyaaa baik plus pluss pluss",  
                "pesan":"Jagaa kesehatann ka!!!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakanyaa imutt bangeyyy pliss",  
                "pesan":"Semangatt teruss ka!!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakanyaa ceria bange orangnyaa lucuu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Masak",
                "sosmed": "@azza.rrr_",
                "kesan": "Baguss bangett suaranya kaa, pas nyanyi lagu FG SD 2025",  
                "pesan":"semangat tKAKAAAAA !!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Humoris bangettt abangnyaaa",  
                "pesan":"Jagaa kesehatan yaa bangg!!!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakanyaa imutt, ramah murahh senyummm",  
                "pesan":"selaluu sehatt terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakanyaa ternyataa seru dan asikk polllllllllll",  
                "pesan":"Selaluu jagaa kesehatan yaa kaa!!!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Aabangnyaa lucu, kalem, tapi tetep asikk",  
                "pesan":"semangat terus kuliahnya bang, lancar selaluu !!!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Seru abangnyaa, asikk diajak ngobrol",  
                "pesan":"semangat terus kuliahnya banggg!!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnyaa kalem tapi lucu bangeettt",  
                "pesan":"semangat terus kuliahnya bang!!!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kaaa hanaa, lucu positive vibes bangeett",  
                "pesan":"Semangatt kaka hanaa !!!"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi Pemda",
                "hobbi": "Main Music",
                "sosmed": "@kerenmrtv",
                "kesan": "Suaranyaaaa baguss pol kaaa ccantiikk",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Aabangnyaa asikk orangnyaa, seruu",  
                "pesan":"semangat terus kuliahnya abangkuhh !!!"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Bagusss bangett hobiinyaa kakakkkuuu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi Pemda",
                "hobbi": "Main rubik",
                "sosmed": "@zhrptsl",
                "kesan": "Kakanyaaaa imutt, lucu bangeett",  
                "pesan":"semangat dan lancarr truus kuliahnya ka !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wUCWIT0Fl5E3pG3KM1NjgjXthE7FRvDs", #Danang Hilal Kurniawan
            "https://drive.google.com/uc?export=view&id=1OwW2gJ_iy5qlMgalQPjJ1aZshd6EPg12", #Syalaisha Andina Putriansyah
            "https://drive.google.com/uc?export=view&id=1iWj4T_oYaRH6qZfSbnTFdC9zOkLHmaIn", #Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=1tM7xJt3aZ3KaXrC2uZ-7IAiOz2_SgCrf", #Anadia Carana
            "https://drive.google.com/uc?export=view&id=1RzsCiYcnNsvXydpHTXj1RcioUYAJrSUP", #Aprilia Dewi Hutapea
            "https://drive.google.com/uc?export=view&id=1GbrV75UJs2IznsKQGo0lLP81ryXbagfb", #Nabila Zakiyah Zahra
            "https://drive.google.com/uc?export=view&id=1K9R8MrvaAeeOgejeZxdX9p-3hKY3Eijv", #Dhafin Razaqa Luthfi
            "https://drive.google.com/uc?export=view&id=1faRCY4YdCbIrooAU_AFacW3tmd0rgJSY", #Devi Rahayu
            "https://drive.google.com/uc?export=view&id=1vDKDzHow3XEyFfES_9B3COBW4SfQplUa", #Enggli Rahmadhani
            "https://drive.google.com/uc?export=view&id=1XrzjZPcyO-zIwixGKiN_j4jhR5BixCM3", #Hanifah Inaya Sani
            "https://drive.google.com/uc?export=view&id=1jBvltlaMRgEL27G0o3TxxM-m3zT9WSBf", #Nydia Manda Putri
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
                "kesan": "Abangnya keren, baik, humble",  
                "pesan":"Sehat selalu bang!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Cantik banget kak",  
                "pesan":"Jangan lupa minum air putih"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "Beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Kece banget bang",  
                "pesan":"Jaga kesehatan ya bang"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "122450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya asik, humble banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton drama pendek di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Kakaknyaa cantikk bangett aslii",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak ini asikkk bangeyy",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@idhafinrzqa13",
                "kesan": "Abangnyaa kalemm tapi ttetep  asikpolll",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakanyaa maniss bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "kakanyaa canntikk bangetttt  ",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak risol",
                "sosmed": "@_inayasanii",
                "kesan": "Kerenn bangett kakanya  bisa jualan risooll yangg  banyakk",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakanyaa seru kecee pol",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()
elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sPpyml-wbAOVRWnloyTZLJrf5T8Wx6vM", #Patricia Leondrea Diajeng Putri
            "https://drive.google.com/uc?export=view&id=14SDAiNO9zE9ded06gnSaUVUUceDs4VUy", #Rahma Neliyana
            "https://drive.google.com/uc?export=view&id=11N7931G-ytNm419eHuoh13kOiTqmuMSr", #Khoirul Anam
            "https://drive.google.com/uc?export=view&id=1U0G4NS0iIIzTb6yY-2EJkqopY20lbBXj", #Labo John Noel Napitupulu
            "https://drive.google.com/uc?export=view&id=1CBlUsg9ZwTyy3dG-LO-6hou5-2_VuINI", #Rafi Diva Efangga
            "https://drive.google.com/uc?export=view&id=1EnSrPih2fk2yuIEzeLGXfFNDwHt7rUqY", #Refa Destiny Pranata
            "https://drive.google.com/uc?export=view&id=1WwjKBDoQkCqLYvzbvnncNifoJ0lkNmuH", #Try Yani Rizki Nur Rohmah
            "https://drive.google.com/uc?export=view&id=1E2t_U_hAiZFEB3vLZRTe-EneEcYgDIfp", #Aliya Ammara Ananta
            "https://drive.google.com/uc?export=view&id=1uObcd3a8r6ZwMjoQ40e1vgodzo-K9mMS", #Donna Maya Puspita
            "https://drive.google.com/uc?export=view&id=12702WpQ4d3b1QU9gy6071-_MxlPn6IFa", #Feby Angelina
            "https://drive.google.com/uc?export=view&id=1VyOtSSmAjMxFO_HEvNuBDDdj2YJoEhP_", #Hafsa Fazila Arradhi
            "https://drive.google.com/uc?export=view&id=1ApRt2lt3Qas2cQLF3hN--rP6zE9Ne-rA", #Nayla Salsabila Fathianisa
            "https://drive.google.com/uc?export=view&id=13JwCFrX0Dn4n13_IEI07yhgKd7min4FJ", #Sania Dwi Ayu Lestari
            "https://drive.google.com/uc?export=view&id=198X_YXSdVzOt_OXUbcBsYStT6ffcy6fb", #Akmal Faiz Abdillah
            "https://drive.google.com/uc?export=view&id=1KFisKIIKdZuDQo4XwPW3uaTvxBW6FPx4", #Raihana Adelia Putri
            "https://drive.google.com/uc?export=view&id=1VoKserse-B4ZOnOWGcqQ_1BcQjeaLi-O", #Citra Agustin
            "https://drive.google.com/uc?export=view&id=135eUlFo-veQ0357j_PyEoIVVo_0ffkOj", #Eigi Artamevia
            "https://drive.google.com/uc?export=view&id=1MSQLIQwfEl2e_0V9VJ_QBCoyqIVbdK8J", #Romauli Oktavia Silaban
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakanyaa seru manis banget senyumanyaa",  
                "pesan":"Semangatttt!!!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@i",
                "kesan": "Kakanyaaaa keren ppolll",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Abangnyyaa berwibawa bangettt",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abangnyaa jadi pdd teruss  keren poll",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Kakak ini asikk poll",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar  Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi  gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakanyaa maniss bangettt pplliss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": " Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakanyaa seruu abiss ",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": " Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jalan Lapas Raya",
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
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatra Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan

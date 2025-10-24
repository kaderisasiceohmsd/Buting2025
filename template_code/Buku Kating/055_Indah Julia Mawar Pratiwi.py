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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FPTzkly5unPxNHexzIRCiIPWbteFH6y1",
            "https://drive.google.com/uc?export=view&id=1p7xC49P8N_cds2f1guvFRyKJ4bvVItss",
            "https://drive.google.com/uc?export=view&id=1lpw7-1I2RLL-FiURUqguG-cvCpajxmvc",
            "https://drive.google.com/uc?export=view&id=1W1KIzBfTWg3RKn3Se_7ZqwaGIwMWVLr6",
            "https://drive.google.com/uc?export=view&id=1SQou4nMgEhw1P_JsE9BdiXJ7_ma2Ioge",
            "https://drive.google.com/uc?export=view&id=1LPXEqFaidwPG-G9mQR8dbBTLCHDLnJPm",
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
                "kesan": "Sangat berwibawa dan keren banget",  
                "pesan":"Semangat bang menjalani hidup sebagai ketua dan semoga sukses kedepannya"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "baca buku (dasar-dasar sql)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Ramah dan humble banget bang jo",  
                "pesan":"Semoga kehidupan kuliahnya berjalan mulus"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Airest Kost",
                "hobbi": "siram shopee",
                "sosmed": "@celisabethh_",
                "kesan": "Kak claudia ramah dan murah senyum",  
                "pesan":"Semoga dimudahkan jalan kedepannya kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya asik dan keliatan banget kutu bukunya",  
                "pesan":"Semoga diberikan kesehatan selalu kak"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "rajabasa",
                "hobbi": "baca buku , saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Dari hobbynya anak pramuka banget nih kak",  
                "pesan":"Semangat terus kak buat kedepannya, semoga cepet lulus"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"kota Padang,Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya ramah dan enak buat diajak sharing",  
                "pesan":"Semoga kuliahnya diberi kemudahan terus kak, semangattt"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1y_yZbztdguDUO8tV22Una4f8yOZK2Ha3",
            "https://drive.google.com/uc?export=view&id=1ddH14KnPYmTLUnhRt-VWrwwWiubmsqii",
            "https://drive.google.com/uc?export=view&id=1qOrORuzeWHXogXi1x-YMO9He7FRMKGow",
            "https://drive.google.com/uc?export=view&id=1fCNu9fD08HewdjXM7iCuBb6Vo1avq5xH",
            "https://drive.google.com/uc?export=view&id=1QmNwuNCv7uAoKjxeJoNwO5uUtg-zcXEB",
            "https://drive.google.com/uc?export=view&id=1_d6PhkwFpp7VV-S1ZsJva7haAqQs0zq3",
            "https://drive.google.com/uc?export=view&id=1vMchhND0vH-agB1Kpv1iW8frZV-SbpIK",
            "https://drive.google.com/uc?export=view&id=164HALJ0bX3L90RDLEovSkYtGLpP7-hzZ",
            "https://drive.google.com/uc?export=view&id=1j0TSYOxwyyYTIZ7z3M9DAmHTazMFpvXa",
            "https://drive.google.com/uc?export=view&id=1ueWUpqphcBJcpOR5orUR15JL_z28f8xs",
            "https://drive.google.com/uc?export=view&id=1z-hGVDt2gQQLS8SrfsEwWaYS6_I0tSE6",
            "https://drive.google.com/uc?export=view&id=1_r9tcPwP0dlrnk949cuyFmxL8ihD9Dw6",
            "https://drive.google.com/uc?export=view&id=16J9GkdhqV41M7wdmo58McQtJl4_mF5TM",
            "https://drive.google.com/uc?export=view&id=1n-RjtDkSa1V2bIi9-sWplgodu-a__qR-",
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
                "kesan": "Abangnya asik dan ramah.",
                "pesan":"Sukses selalu untuk kuliahnya bang, semoga cepet lulus!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya ramah dan ceria, senang bisa kenal dengan kakak",
                "pesan":"Jangan lupa jaga kesehatan ya kak, kalo cape istirahat"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya baik dan ramah banget",
                "pesan":"Sukses selalu untuk kuliahnya ya kak, semangatt!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Orangnya seru dan baik banget",
                "pesan":"Semangat terus kuliahnya kak, jangan menyerah!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Pembawaannya positif dan menyenangkan",
                "pesan":"Semoga kita bisa ketemu dan sharing lebih banyak lagi bang"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Sangat berkesan, orangnya humble dan baik banget",
                "pesan":"Tetap jadi pribadi yang menginspirasi ya bang!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Bang Dharu orangnya menginspiratif, senang bisa kenal dengan bang dharu",
                "pesan":"Jangan lupa jaga kesehatan, bang"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kak Feby orangnya seru dan baik banget",
                "pesan":"Semangat terus ya kak, jangan menyerah!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Pembawaannya positif dan menyenangkan",
                "pesan":"Semangat bang buat kuliahnya"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Sangat berkesan, orangnya humble dan murah senyum",
                "pesan":"Tetap jadi pribadi yang baik dan menginspirasi ya kak!"
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
                "pesan":"Semangat dan sukses selalu untuk kuliahnya ya kak!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Senang bisa kenal dengan bang ridho",
                "pesan":"Semangat terus bang buat kuliah kedepannya"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Orangnya seru, baik dan humble banget",
                "pesan":"Semangat terus ya kak, jangan menyerah!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Pembawaannya positif dan menyenangkan",
                "pesan":"Semoga kita bisa bertemu dan sharing lagi ya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e0SN1rX8v8nKEbRrQpxg-bfd01gfqTAa",
            "https://drive.google.com/uc?export=view&id=1moMVxkc25SoVVV5njfbipMM7ZpsVMy1x",
            "https://drive.google.com/uc?export=view&id=1rV5L0WX01-l5DfpE24EKs6X-tww5kB04",
            "https://drive.google.com/uc?export=view&id=1yr0JQzmm7oTY6oVEXZPTDfOm32E7OYQ3",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kobam, Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Bintang baik banget, ramah dan humble banget",  
                "pesan":"semangat terus kuliahnya ya bang, semoga cepet lulus !!!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "Kak nad baik banget, mau bantu apapun yang bisa dilakuin",  
                "pesan":"semangat ya kak kuliahnya, jangan begadang terus, jangan lupain gweedy imup :)"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak fathinah asik orangnya, suka belajar dengan kakak",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selalu"
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
                "pesan":"Semangat kak kuliahnya, kalo cape istirahat"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HjJJMWa0BlJ0L6y0IfJLBbC3194b_BiV",
            "https://drive.google.com/uc?export=view&id=1_ciZILRLVeEnJd78oZGWO9KAos4KTm1B",
            "https://drive.google.com/uc?export=view&id=1DJFowdy-G6T6sEEiBkY7UAaQSSgdDTVO",
            "https://drive.google.com/uc?export=view&id=1m8OmcKVc_DEfX1D-FnorX9qjZGOxHTqv",
            "https://drive.google.com/uc?export=view&id=1fkKteCVsJSE7Nl9xgQEoeu9czarDZHK7",
            "https://drive.google.com/uc?export=view&id=1sgp9TTAWUqqfkGY62-5JL8Nw8LOMI7Qh",
            "https://drive.google.com/uc?export=view&id=1f6KVgCA-rNP9x15qPDmnFM5-5wAtNwaO",
            "https://drive.google.com/uc?export=view&id=1G198dJ2XlghxYr36isep3-tTZUR_ktNC",
            "https://drive.google.com/uc?export=view&id=1DRkldsHVQxJFljsk8NRBrnOcjkK9w-9F",
            "https://drive.google.com/uc?export=view&id=1A_vuoEXTiaf49hwnh7t7i0vgPw4zIyaR",
            "https://drive.google.com/uc?export=view&id=1hVJTTpeAef5HioDrCDBFN9IYdjaKdFmU",
            "https://drive.google.com/uc?export=view&id=1nxewAGbKMKR9hgCxQZXVYIOwMunjRvqF",
            "https://drive.google.com/uc?export=view&id=1wfe1w3l7gWt88sShzm4m-OIGrAv2CWLb",
            "https://drive.google.com/uc?export=view&id=1czy7wMLdhB5OmMjQJVCGMWAI1YtAuFJB",
            "https://drive.google.com/uc?export=view&id=1kVUxaVPbhYiJO6YEEN54j8ipsBMdB-K-",
            "https://drive.google.com/uc?export=view&id=1pmvQB64heVBxzr913-5QATtARijNI1GW",
            "https://drive.google.com/uc?export=view&id=1l5i2QvfCTxYhucfmFFivRCVeqFJFUe4m",
            "https://drive.google.com/uc?export=view&id=1mvtbRequAP07lMlLU63eVVeGKGRu5xIv",
            "https://drive.google.com/uc?export=view&id=1BAYNKBE6nbNq4px2KXaj4PY3G8_LgljR",
            "https://drive.google.com/uc?export=view&id=1DEGc-9RiqFZ0Dv_qS_hFts-DV_knwMM0",
            "https://drive.google.com/uc?export=view&id=1RuOleahPzAS75wXNerPls34tU4F_F0Lq",
            "https://drive.google.com/uc?export=view&id=1CuZCGDEzm7rIM2TF4YdwLpOpyBmUf4gj",
            "https://drive.google.com/uc?export=view&id=1cf-M7Rh37O_LZG-YWxhbyqYHTsdAj1dv",
            "https://drive.google.com/uc?export=view&id=1rRRBV6q90V9pjDAXANlrYlt1n5K_pYfS",
            "https://drive.google.com/uc?export=view&id=1Tz-kZQB7ZFYV_c8wVrP1xAJHVye6GTQq",
            "https://drive.google.com/uc?export=view&id=1qCeO33v9PWGc7Gc16QKwp4_9YJeb3A_f",
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
                "kesan": "Abangnya sangat berwibawa, dan keren banget",
                "pesan": "Lancar terus bang kuliahnya. Sehat dan sukses terus!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya ramah dan asik juga orangnya",
                "pesan": "Semoga kuliahnya dilancarkan terus kak, semangat kakkk"
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Abangnya lucu tapi pinter, bikin suasana jadi hidup",  
                "pesan":"Jangan lupa istirahat di tengah kesibukan ya, Bang. Semangat terus!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Abangnya tenang tapi kalau udah ngobrol, insight-nya dalam banget.",  
                "pesan":"Terus jadi inspirasi, Bang. Semoga semua impian abang tercapai"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakaknya manis tapi tegas, sosok yang bisa diandalkan banget",
                "pesan": "Tetap jadi contoh buat adik-adik, Kak. Semangat dan sehat selalu!"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakaknya rame dan ceria, selalu bawa vibes positif",  
                "pesan":"Terus tebarkan energi baiknya ya, Kak. Jangan pernah berubah!"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Abangnya asik kalau diajak bercanda juga seru.",  
                "pesan":"Semoga abang selalu diberi kelancaran di kuliah dan urusan lainnya!"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Abangnya punya semangat yang tinggi banget, salut sih!",  
                "pesan":"Terus pertahankan semangatnya, Bang. Jangan gampang nyerah ya!"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Abangnya santai tapi peduli, enak banget diajak ngobrol.",  
                "pesan":"Tetap rendah hati ya, Bang. Sukses selalu di jalan abang sendiri!"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya pintar dan punya cara berpikir yang keren",  
                "pesan":"Terus asah kemampuan abang, semoga makin sukses ke depannya!"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakaknya sopan dan selalu bantu kalau ada yang butuh",  
                "pesan":"Semoga kebaikan kakak dibalas berkali lipat. Tetap rendah hati ya, Kak!"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya elegan dan kalem, tapi kocak kalau udah deket",  
                "pesan":"Jangan berubah, Kak. Dunia butuh orang sepositif kamu!!"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakaknya enerjik dan punya semangat tinggi banget",  
                "pesan":"Teruslah jadi sosok yang nyebarin semangat buat sekitar ya, Kak!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya humble banget, gampang akrab sama siapa pun",  
                "pesan":"Terus semangat ngejar mimpi, Bang. Kamu pasti bisa!"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Abangnya cerdas dan berwawasan luas, enak banget buat diskusi",
                "pesan": "Semoga makin sukses dan gak bosan berbagi ilmu ya, Bang!"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakaknya perhatian dan bisa jadi tempat curhat yang baik",
                "pesan": "Terima kasih udah selalu support, Kak. Semoga bahagia terus!"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abangnya punya gaya khas banget, lucu tapi bijak",
                "pesan": "Jangan kehilangan sisi kocaknya, Bang. Dunia butuh abang yang ceria!"
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
                "kesan": "Kakaknya dewasa banget, tapi tetap ramah dan enak diajak cerita",
                "pesan": "Semoga semua yang kakak perjuangkan berjalan lancar ya!"
            },
            {
                "nama": "Nobel Nizam Fatihrizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abangnya kalem tapi kalau udah ngomong, ngena banget",
                "pesan": "Terus jadi pribadi yang keren dan rendah hati, Bang!"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Kakaknya kalem tapi peduli banget sama orang sekitar",
                "pesan": "Semoga kakak selalu bahagia dan terus menebar kebaikan!"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya cheerful banget, bikin suasana gak pernah sepi",
                "pesan": "Tetap ceria ya, Kak. Dunia lebih hidup kalau ada kamu!"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya lembut tapi berani, keren banget sih",  
                "pesan":"Terus semangat ya, Kak. Kamu hebat dengan caramu sendiri!"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Abangnya supel banget, gampang bikin orang ketawa",  
                "pesan":"Terus jadi sosok yang positif, Bang. Semangat terus!!"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakaknya perhatian dan baik banget, gak pernah pelit senyum",  
                "pesan":"Jangan berubah ya, Kak. Semoga selalu dikelilingi orang baik juga!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Abangnya sederhana tapi punya jiwa pemimpin yang kuat",  
                "pesan":"Semoga abang makin sukses dan terus menginspirasi yang lain!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ciuXgT0LiuxZ0eJZg7N7z_dPXY191scL",
            "https://drive.google.com/uc?export=view&id=1TTIyX-SixATlQhYVBUykBlGLtOZQTRsQ",
            "https://drive.google.com/uc?export=view&id=1dsXTL-Nlv25D3O-KdIoGZbAWxcn9sLl9",
            "https://drive.google.com/uc?export=view&id=1kF8yyf-uglDCcq4j1-EeGBD-Gb9681fm",
            "https://drive.google.com/uc?export=view&id=1Ff95YJjn_gMbi-MrZ2BapCBuoSPWzKb9",
            "https://drive.google.com/uc?export=view&id=1ILrbtF0Co25aQb9TB5gj9PRKxbe5j7B-",
            "https://drive.google.com/uc?export=view&id=1iw7Zkhf0vZjs6rUTpExMEVDU7E3FhnKh",
            "https://drive.google.com/uc?export=view&id=1dPENnAcAHYhcF6BhvY8U91PrYRW2lJZ6",
            "https://drive.google.com/uc?export=view&id=1rkYH9CTUbtma_f8YM4Igk2LY1yBEHbNk",
            "https://drive.google.com/uc?export=view&id=1411rFrURGu_aVf49yvymTdaP4nPuYsRy",
            "https://drive.google.com/uc?export=view&id=1zcMQ0zTTua2D1NTRxYKqex5tknEE0lnR",
            "https://drive.google.com/uc?export=view&id=1DWVs1-u8Q9NUTluHm14RyTkGWX0M4O20",
            "https://drive.google.com/uc?export=view&id=1e8_ESEQGDhCSkBTUea1y0UG1Zv-9YlFy",
            "https://drive.google.com/uc?export=view&id=1cKWdcaE09dJb6lYFeZSDUDpEj65wBirh",
            "https://drive.google.com/uc?export=view&id=1hsm7C538vY7yYOERCOzEq1tZt0zzAmBw",
            "https://drive.google.com/uc?export=view&id=1x9ZnWh-2Hs6riey02xTCr92-lOKhlx2r",
            "https://drive.google.com/uc?export=view&id=1T8LL01F_iI7UHT-raUAtEuBWj9xB0FRv",
            "https://drive.google.com/uc?export=view&id=1u8B7nEp27bogaRQr7lwLYi0bY3OzISqR",
            "https://drive.google.com/uc?export=view&id=1265S-Q3c0jzCftAu1Abk_o6rFhvlDFm2",
            "https://drive.google.com/uc?export=view&id=13aF6uqWAE15MBtFDSfUMws20r47kAZAY",
            "https://drive.google.com/uc?export=view&id=1IdWNpON7LMZh9VY7ohs9RFGR0zGN_kC1",
            "https://drive.google.com/uc?export=view&id=19m7pEk-hP5aK-xRPam-5EPYvF2NavDkj",
            "https://drive.google.com/uc?export=view&id=1kF8yyf-uglDCcq4j1-EeGBD-Gb9681fm",
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
                "kesan": "Abangnya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, bang!"
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
                "kesan": "Abang sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, bang"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya, semangat ngodingnya juga!!!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Marleta keren banget, multitalenta dan kalem juga",
                "pesan": "Semangat terus ya kak! Jangan lupa istirahat di tengah kesibukan"
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
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi",
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
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah, dan asik banget",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, bang"
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
                "pesan":"Terima kasih atas semua pelajarannya, bang!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Abangnya tenang tapi asik, selalu punya cara buat nyambung obrolan.",
                "pesan": "Sukses terus bang, semoga langkah abang selalu tepat kayak main catur!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Abang Fabio easy going dan gampang bikin suasana jadi santai.",
                "pesan": "Tetap semangat bang! Jangan lupa main gamenya jangan kebanyakan"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kak Rahma kalem tapi selalu perhatian sama sekitar.",
                "pesan": "Semangat terus ya kak! Tetap sabar dan semangat ngejar mimpi."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kak Gustriana ceria banget dan punya aura positif.",
                "pesan": "Semoga kuliahnya lancar dan makin sukses ke depannya kak!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Abang Aqil sportif dan punya semangat tinggi, enak diajak kerja bareng.",
                "pesan": "Semangat terus bang! Jangan lupa jaga stamina juga di tengah sibuk kuliah."
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kak Aisyah lembut, humble, dan punya aura menenangkan.",
                "pesan": "Tetap semangat ya kak! Semoga semua impian kakak bisa terwujud."
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kak Tanty seru dan apa adanya, selalu bikin suasana jadi hidup.",
                "pesan": "Sukses terus kak! Tapi jangan tidur terus juga ya"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah lucu, rame, dan spontan banget — bikin suasana jadi gak kaku.",
                "pesan": "Semangat terus kuliahnya kak, dan jangan terlalu sering random chat sama GPT"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abang Naufal kalem dan berwawasan luas, enak diajak ngobrol.",
                "pesan": "Tetap semangat bang, semoga musiknya selalu jadi penyemangat!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main piano, Nyanyi, Ngehalu",
                "sosmed": "@bee_0115",
                "kesan": "Kak Fabiolla energik dan punya semangat tinggi buat belajar.",
                "pesan": "Sukses terus ya kak! Semoga makin jago main bola dan makin pinter juga!"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kak Fairuz lembut dan perhatian, enak banget diajak ngobrol santai.",
                "pesan": "Semangat terus kak! Jangan lupa istirahat biar gak tidur terus"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RnEbMrUPZ9WHP-Kx1FaIVWpYumolHXb9",
            "https://drive.google.com/uc?export=view&id=1db5M9Cc4mWp438u6JMytg6CluEPPtJD4",
            "https://drive.google.com/uc?export=view&id=1-9ByDmGPmbJtm2qA-pzUG-noBSwrBEHV",
            "https://drive.google.com/uc?export=view&id=1ACmthsYreaor1_u6IhzM-ecNx61LFhF6",
            "https://drive.google.com/uc?export=view&id=1EaweKMfSKAIn9gWElcAGJwBtRrW0OUgg",
            "https://drive.google.com/uc?export=view&id=1JFglaiP1xc3iZVG59lEul742ClqYd2uR",
            "https://drive.google.com/uc?export=view&id=1kCn-TWR8ynKZwychAD9C4Ky47PV0GfXK",
            "https://drive.google.com/uc?export=view&id=1etXMLO5lM-TOVMc7MSqYVgWmy6jVgS_R",
            "https://drive.google.com/uc?export=view&id=1u-0ROjbU9BS5sUK3uBfIElC-HqPxDks3",
            "https://drive.google.com/uc?export=view&id=1KcR7MzUPflkomrnNbqSatwD8SkEF1pF5",
            "https://drive.google.com/uc?export=view&id=1ZGHG4Z4EaTSXgOG8a2dbG2F6i0R0R1Mr",
            "https://drive.google.com/uc?export=view&id=1sDtPEiWrzDlMlz3Yo9mFWf3BOKbChyl5",
            "https://drive.google.com/uc?export=view&id=1VBhSPxkFBxRw0QxrKibK9NIw4NOo242t",
            "https://drive.google.com/uc?export=view&id=1NG8EYqq2eyKPpGiJExJWZiLoshsrvEB_",
            "https://drive.google.com/uc?export=view&id=1c0x7dMa2AF1BYMfxdu_j10AFE1rckc8w",
            "https://drive.google.com/uc?export=view&id=1Ka47WDfNic0cXs1idlQj1xdqcrppmeBN",
            "https://drive.google.com/uc?export=view&id=1_LgkMofmxmCbLQgHRSlJvNWnqxUumV9d",
            "https://drive.google.com/uc?export=view&id=1vPBR2DT5ckQscNHBIx1d6V-Z_gWI2mba",
            "https://drive.google.com/uc?export=view&id=1OduPS-Vv5JVi2YcFdPgOIW7copFGKzMT",
            "https://drive.google.com/uc?export=view&id=1JvJfKfMPhpXiDgNSxrFst7qaq8FTsF_b",
            "https://drive.google.com/uc?export=view&id=14vt-YV67c_WpTCRPHahIrH5-hbnzanbr",
            "https://drive.google.com/uc?export=view&id=1Y0DPrRNNIjFr3pvUlwgGloMk5Nek0TkT",
            "https://drive.google.com/uc?export=view&id=1hr1IK58b8PDrK-aSj35-9fdNSN7DjxnM",
            "https://drive.google.com/uc?export=view&id=1PgP_KoK_b8eMHQu8B7Ogk7ySdmrfcumS",
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
                "kesan": "Abangnya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, bang!"
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
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi",
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
                "kesan": "Abangnya humble banget dan enak diajak cerita",
                "pesan":"Sukses selalu untuk Abang Irvan ke depannya!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing",
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
                "kesan": "Kak Luthfia ceria dan gampang bikin suasana rame",
                "pesan":"Semoga semua cita-cita Kakak tercapai dengan lancar!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya pembawaannya positif dan menenangkan",
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
                "kesan": "Kak Cindy orangnya asik dan gampang diajak diskusi",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abang Desman baik dan sabar banget kalau bantu orang",
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
                "kesan": "Kak Nurul pekerja keras dan konsisten dalam setiap hal yang dilakukan",
                "pesan":"Teruslah berkarya dan jangan pernah berhenti mengejar mimpi, Kak"
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Sangat berkesan, pembawaannya positif",
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
                "kesan": "Abang Qois memiliki semangat tinggi dan pandai membawa suasana jadi menyenangkan",
                "pesan":"Pertahankan semangat dan teruslah jadi pribadi yang inspiratif, Bang"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melinza sopan, disiplin, dan selalu memberikan contoh yang baik",
                "pesan":"Semoga segala usaha Kakak membuahkan hasil yang memuaskan"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea penuh inisiatif dan punya rasa tanggung jawab yang tinggi",
                "pesan":"Terus semangat dalam menapaki perjalanan hidup dan kariernya, Kak"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kak mut sosok yang hangat, ramah, dan selalu menjaga hubungan baik dengan semua orang",
                "pesan":"Semoga Kakak selalu diberi kebahagiaan dan kesuksesan di setiap langkah"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla berkepribadian lembut namun tegas ketika dibutuhkan",
                "pesan":"Teruslah menjadi inspirasi bagi banyak orang, Kak"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abang Arya kalem dan bijak, selalu bisa membawa suasana tenang dalam tim",
                "pesan": "Semoga setiap usaha dan kerja keras Abang membuahkan hasil terbaik"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abang Adit sosok yang cerdas, terencana, dan bisa diandalkan",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, bang"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kak Tarisya sopan, rendah hati, dan menyenangkan untuk diajak bekerja sama.",
                "pesan": "Semoga segala cita-cita dan impian Kakak bisa tercapai dengan lancar"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini memiliki semangat belajar yang tinggi dan selalu berpikiran terbuka",
                "pesan":"Pertahankan semangat itu, Kak, dan teruslah jadi pribadi yang menginspirasi"
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abang Syahrialdi santun dan berkarisma, mudah membuat orang nyaman di sekitarnya",
                "pesan":"Semoga semakin sukses dan terus jadi teladan yang baik, Bang"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia punya semangat belajar tinggi dan selalu berusaha memberikan yang terbaik",
                "pesan":"Semoga langkah Kakak selalu diberi kemudahan dan keberkahan"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla anggun, sopan, dan selalu menebarkan energi positif",
                "pesan":"Teruslah menjadi sosok yang membawa inspirasi bagi orang lain, Kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kAzwQKBO6FXCtEe4l3o1_QLeCWiPTqM3",
            "https://drive.google.com/uc?export=view&id=1iFKYqFZLlYn3a-sHWE9osyjVMCTyPNyv",
            "https://drive.google.com/uc?export=view&id=1VgVU0QYdW0dKABTEGcW_A0h5YMdYgzPk",
            "https://drive.google.com/uc?export=view&id=1IhwdQjwPUN9Ix_SYHiZXOwfU0Sg6AfU3",
            "https://drive.google.com/uc?export=view&id=10YFhSrDwcy9xqTgeB6dNFd7NCL0tuGR0",
            "https://drive.google.com/uc?export=view&id=1oS2t9xMkeQ_AGcjYREX5dHCDe3O1VF6o",
            "https://drive.google.com/uc?export=view&id=1oPPOZM4Qu0bAieh0hSiYcEMHlq4ZyHhI",
            "https://drive.google.com/uc?export=view&id=1OFgQtqcaHme2YS9CRx6XX8UiTcRqt-zg",
            "https://drive.google.com/uc?export=view&id=1VNVvkpO98CPQZoXIoZtv0p_g0_l04S3Z",
            "https://drive.google.com/uc?export=view&id=1OZuEcVdPKv4XF57cJv6SeTa1sAdQxCTp",
            "https://drive.google.com/uc?export=view&id=1zHSZGsaZHN1IS20xM8MgWGQFxBud26e2",
            "https://drive.google.com/uc?export=view&id=17KNwcOX_ZcpowFVUGg4vHeWcSRe30kH0",
            "https://drive.google.com/uc?export=view&id=1ByKSniaLFlkga_9OyQZ7eSvZB3RF_cU9",
            "https://drive.google.com/uc?export=view&id=1fhBM6NIj9FIhqaWBB9z1Q1d82q-WUOEr",
            "https://drive.google.com/uc?export=view&id=1nzgF6r5MjmosJTBdIG_7t89r04wgW3VG",
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
                "kesan": "Kak Rani memiliki pribadi yang lembut, perhatian, dan selalu membawa suasana nyaman bagi orang di sekitarnya",
                "pesan":"Teruslah menjadi sosok yang menenangkan dan menginspirasi banyak orang, Kak. Semoga semua langkah Kakak selalu dimudahkan"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta orangnya ramah, terbuka, dan mudah bergaul, membuat suasana kerja jadi lebih hangat",
                "pesan":"Semoga Kak Renta selalu diberi semangat dalam menjalani tanggung jawab dan terus menebarkan energi positif"
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
                "kesan": "Kak Hanna pribadi yang ceria dan bersemangat, membuat suasana kerja terasa menyenangkan",
                "pesan":"Teruslah membawa keceriaan itu ke mana pun Kak Hanna melangkah, dan semoga selalu dikelilingi kebahagiaan"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak Iqfina sosok yang teliti dan berkomitmen tinggi terhadap tanggung jawabnya",
                "pesan":"Semoga semangat Kak Iqfina selalu terjaga dan segala impian dapat tercapai satu per satu"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang Haikal berjiwa aktif dan selalu punya ide-ide segar yang membangun suasana positif",
                "pesan":"Pertahankan semangat Abang yang kreatif dan jangan pernah berhenti berkarya, ya Bang"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abang Zailani sosok yang disiplin dan tangguh, tapi tetap rendah hati dalam berinteraksi",
                "pesan":"Semoga Abang selalu diberikan kekuatan dan keberhasilan dalam setiap perjuangan"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak May sosok yang anggun, ramah, dan mudah membuat orang merasa nyaman di dekatnya",
                "pesan":"Semoga Kak May terus menjadi pribadi yang membawa ketenangan dan inspirasi bagi banyak orang"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kak Azzahra penuh semangat dan selalu menunjukkan dedikasi tinggi dalam setiap kegiatan",
                "pesan":"Jangan pernah kehilangan semangat dan keyakinan, Kak. Langit masih luas untuk Kakak jelajahi"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah pribadi yang berbakat dan kreatif, terutama dalam hal seni dan musik",
                "pesan":"Teruslah berkarya dan gunakan bakat Kakak untuk menginspirasi banyak orang"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak Keren selalu tampil ceria dan membuat suasana jadi lebih hidup",
                "pesan":"Semoga keceriaan Kakak selalu menular ke orang lain dan membawa keberkahan dalam setiap langkah"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abang Hanif orangnya santai tapi tetap bertanggung jawab dan bisa diandalkan",
                "pesan":"Teruslah berproses dan berikan yang terbaik dalam setiap kesempatan, Bang"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Bang Naufal memiliki semangat tinggi dan selalu ingin belajar hal baru",
                "pesan":"Semoga Abang terus berkembang dan menjadi pribadi yang semakin hebat setiap harinya"
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Jalan Durian 19",
                "hobbi": "Mengetik",
                "sosmed": "@zhresti",
                "kesan": "Kak Zahra memiliki pembawaan yang tenang, sopan, dan selalu menjaga sikap dalam setiap keadaan",
                "pesan":"Teruslah menjadi contoh kebaikan bagi orang di sekitar, Kak. Semoga Kakak selalu dilimpahi kebahagiaan dan kesuksesan"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hJETIynZo0kqgJZ1KeakN1OTY-gL6nCY",
            "https://drive.google.com/uc?export=view&id=1ZBMayJ5NuwhpKsN2Hg5mr4g5BD4xQkvW",
            "https://drive.google.com/uc?export=view&id=1P1Dn_OD__jvWhrHN51hF9HS0LEqPrwWM",
            "https://drive.google.com/uc?export=view&id=1YhafFTlId1tHNa5SHyqJGXE-YzzT_sL5",
            "https://drive.google.com/uc?export=view&id=1jWMVDUsfWIXA5WMTvPauZALVnajyXcrl",
            "https://drive.google.com/uc?export=view&id=1FytO-YaP1i6qGwH-itGiplI6TpgTEJBN",
            "https://drive.google.com/uc?export=view&id=1LbkM2l_6yRecDXtAhwVys4RP9EWbcD7P",
            "https://drive.google.com/uc?export=view&id=1cGFhqGIeiJ1Z0k3YSMxGyEWlzoEvL5Yi",
            "https://drive.google.com/uc?export=view&id=1-S0rBUtppgmbxBcKlfpOmMDekiLvhSlI",
            "https://drive.google.com/uc?export=view&id=1M-thj7DjqvuxmLATTOANrlNIWl8bJWcZ",
            "https://drive.google.com/uc?export=view&id=1wnFg8owFLQRYdXAr5Mv31h3NQxrFFZD_",
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
                "kesan": "Abang Danang orangnya ramah, terbuka, dan selalu menciptakan suasana nyaman di sekitar",
                "pesan": "Teruslah menjadi pribadi yang penuh semangat dan tulus dalam setiap hal yang dikerjakan, Bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kak Syalaisha punya kepribadian lembut dan sopan, membuat setiap pertemuan terasa menyenangkan",
                "pesan": "Semoga Kak Syalaisha selalu diberi kelancaran dalam kuliah dan terus menjadi inspirasi bagi banyak orang"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abang Rizqi sosok yang tenang dan menyenangkan, mudah diajak bicara dan selalu positif",
                "pesan": "Semoga Abang terus diberi semangat untuk berkembang dan mencapai semua cita-cita"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kak Anadia selalu tampil percaya diri dan membawa energi positif di setiap kesempatan",
                "pesan": "Teruslah bersemangat mengejar impian, Kak. Jangan berhenti jadi sumber inspirasi bagi sekitar"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Kak Aprilia pribadi yang ceria dan rendah hati, selalu menyambut orang dengan senyum hangat",
                "pesan": "Semoga setiap langkah Kakak dipenuhi kebahagiaan dan keberhasilan"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kak Nabila sosok yang perhatian dan tanggap terhadap orang lain, membuatnya mudah disukai banyak orang",
                "pesan": "Teruslah jadi pribadi yang membawa ketenangan dan semangat untuk orang-orang di sekitar, Kak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Bang Dhafin cerdas dan selalu terbuka untuk berbagi ilmu, membuat suasana belajar jadi menyenangkan",
                "pesan": "Semoga Abang terus semangat dan sukses dalam perjalanan akademik maupun kehidupan pribadi"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kak Devi orangnya lembut dan sopan, tapi tetap aktif dan bersemangat dalam berorganisasi",
                "pesan": "Semoga Kak Devi terus bahagia dan diberi kemudahan dalam segala urusan"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kak Engeli sosok yang humoris dan mudah akrab, membuat suasana jadi lebih hidup",
                "pesan": "Semoga Kakak selalu dikelilingi orang-orang baik dan diberi jalan yang terbaik untuk masa depan"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak Hanifah memiliki pembawaan tenang dan selalu menebarkan aura positif ke sekitarnya",
                "pesan": "Teruslah menjadi sosok yang menenangkan dan menginspirasi, Kak"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kak Nydia adalah pribadi yang ceria, komunikatif, dan penuh semangat",
                "pesan": "Semoga Kakak selalu sukses dan tetap menjadi pribadi yang menyenangkan untuk semua orang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14iz1CY7y_tD0d8Bajh89s2D5BdF1H7vB",
            "https://drive.google.com/uc?export=view&id=1McTjQjqoEkNmY1p1TXaWnjoMuBEtBpIr",
            "https://drive.google.com/uc?export=view&id=1D6Pa938OIQcLftwDFDM-sx1EZriWZYtd",
            "https://drive.google.com/uc?export=view&id=1nYeZYEUmBPHIBBD2hlTJe92fejnE695G",
            "https://drive.google.com/uc?export=view&id=12TtCVbMZGUlygLuYnm-lpSz_dvyQd2s8",
            "https://drive.google.com/uc?export=view&id=1ENET44eVG1JR4U3GwcRQXoS6ihdLjs7V",
            "https://drive.google.com/uc?export=view&id=1u3UcUXl2C5llbVGcMGEwL95hMUSFoAX3",
            "https://drive.google.com/uc?export=view&id=1u3UcUXl2C5llbVGcMGEwL95hMUSFoAX3",
            "https://drive.google.com/uc?export=view&id=1PjimAMKGrwNsEsw64_xJQVsK4m17EYOw",
            "https://drive.google.com/uc?export=view&id=1jsl-53mJGq-gY2tfLA3T6gflnpTNx7p2",
            "https://drive.google.com/uc?export=view&id=1uNF-knrAFB6zkfIJICjwTzzw46k9LkL9",
            "https://drive.google.com/uc?export=view&id=1uY6U-AoxDWXk1NaV1djEpxsBNzOWcPyx",
            "https://drive.google.com/uc?export=view&id=1T_5B_oC4UWKkN0woM-wYozBcw6BZ2BrF",
            "https://drive.google.com/uc?export=view&id=1nUBaSFc2YIwskqwnSdbeEOy2og_WKD6a",
            "https://drive.google.com/uc?export=view&id=1xkg2b0r76X1zhTkr3N3Q5VfgmHSqyvz2",
            "https://drive.google.com/uc?export=view&id=1Beun24Ywo5V2OfdXA6d2Lges6Wpr3lTa",
            "https://drive.google.com/uc?export=view&id=1GnrptoxWiFilb5iwpdvB-KS93ERYfqF1",
            "https://drive.google.com/uc?export=view&id=14_QN-bwB3dEsJ9wZYkReoD8dK81aKIP7",
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
                "kesan": "Kak Patricia pribadi yang berani dan penuh ide kreatif, selalu memberikan energi baru di setiap momen",  
                "pesan":"Teruslah berkarya dan menebarkan semangat positif, Kak. Dunia menunggu karya terbaikmu!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Rahma sosok yang dewasa dan penuh tanggung jawab, selalu memberi contoh yang baik",  
                "pesan":"Semoga segala usaha dan kerja keras Kak Rahma selalu berbuah manis"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kak Try Yani dikenal rajin dan konsisten, sosok yang bisa diandalkan dalam setiap tugas",  
                "pesan":"Teruslah jadi pribadi yang disiplin dan rendah hati, Kak. Semangat selalu!"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abang Akmal orangnya tenang tapi punya selera humor yang bikin suasana cair",  
                "pesan":"Semoga Abang terus berkembang dan menjadi sosok yang semakin hebat ke depannya"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Bang Anam berwibawa dan mudah diajak bekerja sama, selalu mengutamakan kebersamaan",  
                "pesan":"Teruslah jadi panutan bagi adik-adik, Bang. Semoga sukses menyertai setiap langkah Abang"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Bang Rafi energik dan penuh semangat, selalu membawa aura positif dalam tim",  
                "pesan":"Pertahankan semangat dan kerja keras Abang. Sukses besar menanti di depan"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Romauli penuh semangat dan selalu berusaha menampilkan yang terbaik dalam setiap kegiatan",  
                "pesan":"Semoga Kak Romauli terus berproses dan berkembang jadi pribadi yang makin luar biasa"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak Eigi sosok yang lembut dan kreatif, punya pandangan menarik terhadap banyak hal",  
                "pesan":"Teruslah berkarya dan tebarkan keindahan lewat apa pun yang Kak Eigi lakukan"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra selalu membawa ketenangan dan sikap positif dalam setiap situasi",  
                "pesan":"Semoga Kak Citra selalu diberi kebahagiaan dan kesuksesan di setiap langkahnya"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kak Aliya pribadi yang ceria dan penuh semangat, membuat suasana di sekitar jadi menyenangkan",  
                "pesan":"Teruslah bersinar dengan keceriaanmu, Kak. Dunia butuh energi seperti itu"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kak Hafsa dikenal sabar dan penyayang, sosok yang tulus dalam membantu orang lain",  
                "pesan":"Semoga kebaikan Kak Hafsa selalu kembali berlipat ganda dan membawa keberkahan"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa pribadi yang unik dan punya gaya tersendiri, mudah diingat karena kehangatannya",  
                "pesan":"Jangan pernah berhenti jadi diri sendiri, Kak. Dunia butuh sosok seautentik Kakak"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kak Feby punya semangat besar dan kreatif dalam berpikir maupun bertindak",  
                "pesan":"Teruslah berkreasi dan jangan takut untuk melangkah lebih jauh, Kak"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kak Raihana lembut dan peduli, selalu membuat suasana terasa lebih nyaman",  
                "pesan":"Semoga Kak Raihana terus diberi kebahagiaan dan kesuksesan di setiap langkah"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania selalu membawa suasana ceria dan membuat orang lain merasa diterima",  
                "pesan":"Teruslah jadi sumber semangat bagi sekitarmu, Kak"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kak Nayla kalem tapi berwawasan luas, selalu punya cara pandang yang bijak",  
                "pesan":"Semangat terus kak kuliahnya, semoga sehat selalu"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kak Dona sosok yang hangat dan penuh perhatian, membuat orang lain mudah merasa dekat",  
                "pesan":"Teruslah menyebarkan kebaikan dan semangat, Kak. Dunia butuh energi positif seperti Kak Dona"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Bang Labo orangnya santai tapi tangguh, selalu bisa diandalkan dalam banyak situasi",  
                "pesan":"Semoga Abang terus sukses, tetap rendah hati, dan selalu membawa pengaruh baik untuk sekitar!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

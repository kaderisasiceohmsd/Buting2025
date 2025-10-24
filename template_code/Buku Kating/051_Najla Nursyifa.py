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
            "https://drive.google.com/uc?export=view&id=154kH_9W5qc3vr_kF_3rFlj0COJUIjTHz", 
            "https://drive.google.com/uc?export=view&id=1StMrKjc4OGjHIDbxVR847IK1nS3Tw2xz", 
            "https://drive.google.com/uc?export=view&id=1S4Z-05PzS09Zyv_2uVz3GuNIf0qZlrH4", 
            "https://drive.google.com/uc?export=view&id=1ztnvvgw0bBIjy7knuEEHkcnkgMx6JmCI", 
            "https://drive.google.com/uc?export=view&id=1W7ekc_re8sGfuEvcdO8BhqEgAwU7gNgw", 
            "https://drive.google.com/uc?export=view&id=1y5Wpq1OLmQ7TdDoztHprIphROKOxR-rl", 
        ]
        data_list =[
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Abangnya humble banget",  
                "pesan":"Semoga terus jadi pemimpin hebat di mana pun nanti"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "JL. Lapas",
                "hobbi": "Baca buku sql",
                "sosmed": "@johanneskrisjnn",
                "kesan": "Abangnya berwibawa tapi gak bikin takut",  
                "pesan":"Semoga selalu diberi kelancaran di setiap langkahnya"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal": "Badui dalem",
                "alamat": "Ayres Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh",
                "kesan": "Kakaknya ramah banget, jadi gak canggung kalau ngobrol",  
                "pesan":"Semoga sukses terus kak!"# 1
            },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak keren, tapi tetap rendah hat",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
             {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "18",
                "asal": "Wakatobi, Sulawesi Utara",
                "alamat": "Mutun, Paseweran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya kelihatan tegas tapi sebenernya baik banget",  
                "pesan":"semangat ngejar impiannya kak!"# 1
            },
                {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumatera Barat",
                "alamat": "Gya kost korpri",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya lucu dan receh banget",  
                "pesan":"Tetap jadi sosok seru yang bisa diandalkan!"# 1
            }, 
        ]
        
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fOf-BYWOpXfY3jZQGHXrppUV1XCalWlf", 
            "https://drive.google.com/uc?export=view&id=1I_e1GGxhsaEaFUZszUguMkyYGGtR8002", 
            "https://drive.google.com/uc?export=view&id=1MLSwDB9tYZV6-V-1rJvtXZeYYPHzfSfG", 
            "https://drive.google.com/uc?export=view&id=1WBolNcjo7yJcyndRNKqN2E2haNQ44fAi", 
            "https://drive.google.com/uc?export=view&id=1H6-KKqlEXA_pBAI02QPRabyeoVw8sxLX", 
            "https://drive.google.com/uc?export=view&id=1kdghNEpQX-ArjFPNcix-cz6Szh5b6Xhc", 
            "https://drive.google.com/uc?export=view&id=1ibfWd1F2i_a-24xnPASKXGtmKUWwGUhY", 
            "https://drive.google.com/uc?export=view&id=1vKyhRC35PpYReIWkqzbZ2acHiX1D5HIJ", 
            "https://drive.google.com/uc?export=view&id=1BgRhaTLQAzdpWRUWovUD8hrhHM3Io70Y", 
            "https://drive.google.com/uc?export=view&id=1rmqtqC_4QVJ4iqXF9YS50faXupnrhFCY", 
            "https://drive.google.com/uc?export=view&id=120Wz37NvuAnMAOauHrSYOAV3uPBGTs8t", 
            "https://drive.google.com/uc?export=view&id=12dPPk6HpXxY5McuuWQsRacyfgUplf3YQ", 
            "https://drive.google.com/uc?export=view&id=1-dS7gekMceVzL5PRwIOMh58v9MJz5gwE", 
            "https://drive.google.com/uc?export=view&id=1Av3S02wBxl8fZuG_DOSIhTo81wH-_6Uk", 
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Lapas , Belwis",
                "hobbi": "Zumba di pln setiap jumat pagi",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya lowkey tapi keren banget",  
                "pesan":"Semoga sukses dan bisa jadi inspirasi buat kami"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Mojokerto",
                "alamat": "Teluk",
                "hobbi": "MSuka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak humble banget",  
                "pesan":"Semoga dikelilingi hal baik"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@rnshism",
                "kesan": "Kakaknya friendly dan asik banget",  
                "pesan":"Semoga hal baik selalu berdatangan"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya asik dan baik juga",  
                "pesan":"Selalu jaga kesehatan kak!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@dhruchyo",
                "kesan": "Abangnya pinter banget tapi gak sombong",  
                "pesan":"Semoga ilmunya makin berkembang terus ya, bang!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg cabe",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya lucu tapi bisa serius juga",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Abangnya selalu positif dan semangat",  
                "pesan":"Semoga semangat itu gak pernah padam ya, bang!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya berwibawa tapi tetap approachable",  
                "pesan":"Terus jadi inspirasi buat kami semua!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya baik banget dan asik",  
                "pesan":"Semoga sukses dimasa depan kak"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya asik dan chill",  
                "pesan":"Tetap semangat kak menjalani kuliahnya"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridho",
                "kesan": "Abangnya selalu keliatan kalem tapi asik",  
                "pesan":"Jangan lupa makan!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya bikim kagum",  
                "pesan":"Tetap semangat bang kuliahnya!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya peka banget sama sekitar",  
                "pesan":"Semoga kehidupannya dipermudah"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Pekanbaru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya cerewet tapi perhatian",  
                "pesan":"Makasih udah jadi sosok yang selalu peduli"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FhDVNj7OLOSDCuPU-BnX6PKmP2Lz4uJ0", 
            "https://drive.google.com/uc?export=view&id=1AoST77ETgf5M6pHAYxKz0CN6ovIomi5t", 
            "https://drive.google.com/uc?export=view&id=1SdYFo9_Nwxdd69I772ZTpvfdMkdRFrdf", 
            "https://drive.google.com/uc?export=view&id=1jaiMtjV4tt0OG6bXLZEeoQr-_4yJcFG8", 
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya aktif banget di mana-mana",  
                "pesan":"Semoga hal baik terus berdatangan!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "belakang indomaret belwis",
                "hobbi": "Main roblox",
                "sosmed": "@nadiaanjani",
                "kesan": "Kakaknya lucu dan baik banget",  
                "pesan":"Semoga selalu semangat kak!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya humble banget dan baik!!",  
                "pesan":"Makasih kak udah ngajar ale!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik dan ramah",  
                "pesan":"Semoga bisa terus jadi inspirasi buat banyak orang!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
  
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qIUz3W8okBFAorK3IvVqcbRf1iLV4G-y", 
            "https://drive.google.com/uc?export=view&id=13Lht7BfGKREit-4HjrHtxN22Il6sqbok", 
            "https://drive.google.com/uc?export=view&id=1wksTmaKXJAAH50nKkvHrN16GApwhc114", 
            "https://drive.google.com/uc?export=view&id=1qwqrM6eqsF3mJaP1NtqtQsSfIToGhMuF", 
            "https://drive.google.com/uc?export=view&id=1i2VG81B4vL78c0bNAd-GXoJEZuYO1SGM", 
            "https://drive.google.com/uc?export=view&id=17gWncFgemlkDFnXIDSSRuhyjmzDeVLII", 
            "https://drive.google.com/uc?export=view&id=1CVvlJBrpOv4QahQngpMO_0xiVwzS6GpP", 
            "https://drive.google.com/uc?export=view&id=1WELyiRa3PDx_5kyqz2jvBfpzMjAzX11G", 
            "https://drive.google.com/uc?export=view&id=17wXXzG4ZuEkbdY71gvo6nkd2J2o0DI0j", 
            "https://drive.google.com/uc?export=view&id=1H6sEjvx-Fr2HKcCoPJcUduZS4RhUi98b", 
            "https://drive.google.com/uc?export=view&id=12KgiVCih1l9i1uJoLiVisVq5PnvZrvVy", 
            "https://drive.google.com/uc?export=view&id=12BCYOZ0KKhqsGDgVIgYVwXIlbLPR1XSd", 
            "https://drive.google.com/uc?export=view&id=170HBzNlazOSHSgQhxceI2LH6PzShw7e-", 
            "https://drive.google.com/uc?export=view&id=1NB58mf2edPsQUQFITAqqSUVs2lr78arB", 
            "https://drive.google.com/uc?export=view&id=1TpdMIbqxi7072PWSIeylW7fr7j-F2WPq",   
            "https://drive.google.com/uc?export=view&id=15VZdhn-Zr0O7DsugpTw2A-NMLRER4p7z", 
            "https://drive.google.com/uc?export=view&id=1Hq5Lxiq9IkVsYN6xuzhQlXLB4DZmAKrM",
            "https://drive.google.com/uc?export=view&id=1Ib9G16WOWhOzBcvqLYe2-qmm-C7bgG32", 
            "https://drive.google.com/uc?export=view&id=1Nnf_lWM_sGE3sfY9tRH4XpORME1cke-P", 
            "https://drive.google.com/uc?export=view&id=1pfVI1BQJdTf3C1R_8JJ7oGkILuzviCn3", 
            "https://drive.google.com/uc?export=view&id=1Ok3PSs9HmE1cm3Ab_nBuSrDgs2Y5GhiX", 
            "https://drive.google.com/uc?export=view&id=1aQ3guawPQNw6_TKvsqmgoka55UCTipJK",     
            "https://drive.google.com/uc?export=view&id=1utgwo-Pwtq5E9_N7EyRz05WDDd7lNzqu", 
            "https://drive.google.com/uc?export=view&id=1udchb1OSD8Wx3X9jUobphG0uEzowFmbq", 
            "https://drive.google.com/uc?export=view&id=1UJnIll1mBRnbTqbwjEY-C099vvga4uAR", 
            "https://drive.google.com/uc?export=view&id=1S2dUHHuU-YSCv6k2Pw9VDhsy_iMfeNTg",  
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "..",
                "asal":"..",
                "alamat": "..",
                "hobbi": "..",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya selalu tenang di setiap situasi.",  
                "pesan":"Terima kasih udah ngajarin disiplin dengan sabar"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya perhatian",  
                "pesan":"Semoga selalu sukses di tiap langkahnya kak!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Ngekader 24",
                "sosmed": "@allyapasha_",
                "kesan": "Serem pas ngader, lembut pas ngobrol",  
                "pesan":"Makasih udah dorong kami keluar dari zona nyaman kak!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "orangnya pintar dan pemikirannya terbuka banget",  
                "pesan":"Semoga terus sukses dan semakin banyak menginspirasi"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Sebelah kost bang Dapa",
                "hobbi": "Liatin Haikal",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakaknya tenang tapi tegas",  
                "pesan":"Semoga semua kerja keras kakak gak sia-sia"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gg.sakum",
                "hobbi": "Sebelah kost kak Arin",
                "sosmed": "@daffahdynn_",
                "kesan": "Abangnya perhatian dan penuh semangat",  
                "pesan":"Terima kasih udah selalu dorong kami buat lebih baik"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Abangnya punya pembawaan kalem",  
                "pesan":"Semoga selalu dikelilingi orang-orang baik"# 1
            }, 
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kostan putri gerbang barat sebelah sawah",
                "hobbi": Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakaknya punya aura positif dan baik!",  
                "pesan":"Semoga kakak terus jadi inspirasi buat sekitar"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Gg. Pewira",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Kakaknya tegas tapi adil",  
                "pesan":"semangat belajarnya bang!"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Fam",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Abangnya humoris tapi bijak juga",  
                "pesan":"Terima kasih udah jadi sosok yang tulus dan peduli"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya perhatian dan asik",  
                "pesan":"Semoga semua niat baik kakak dibalas yang terbaik"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "Abangnya paling jago badminton dan humoris",  
                "pesan":"Sukses terus dimasa depan bang!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung,Lampung Timur",
                "alamat": "Nangka 4",
                "hobbi": "Main Game, Kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya santai, asik diajak ngobrol",  
                "pesan":"Jangan lupa jaga kesehatan juga ya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya selalu punya energi positif dan asikk",  
                "pesan":"Semoga selalu jadi inspirasi buat banyak orang"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya lucu tapi kalem",  
                "pesan":"Semoga makin banyak keberkahan"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakaknya baik banget dan asik",  
                "pesan":"Semangat narinya ka, semoga sukses"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "1224500109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jalan Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya asik diajak ngobrol",  
                "pesan":"Selalu jaga kesehatan bang!"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Bebersih kos",
                "sosmed": "@ahmadnaufal_",
                "kesan": "Abangnya baik dan chill",  
                "pesan":"Semoga terus jadi panutan banyak orang!"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "122450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "Ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya asik dan positif vibes",  
                "pesan":"terus semangat ngejar impian!"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "122450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Joki strava",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abangnya ramah dan baik",  
                "pesan":"semangat jalani hari harinya bang!"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "122450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertani",
                "sosmed": "@kevinaj__",
                "kesan": "Kirain abangnya galak ternyata asik",  
                "pesan":"Semoga nilai kuliahnya memuaskan"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "122450013",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Semoga dikelilingi orang baik terus kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "122450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton yt pak tamaro",
                "sosmed": "@ridwan122",
                "kesan": "Abangnya humoris dan asik juga",  
                "pesan":"Semoga semua kerja kerasnya gak sia-sia!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "122450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Abangnya lucu banget sering ketawa",  
                "pesan":"Semoga selalu diberi kesehatan dan semangat bang!"# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "kerjain soal MTK",
                "sosmed": "@liano.wan",
                "kesan": "Keliatan galak tapi aslinya baik dan asik",  
                "pesan":"Semoga semua usaha dibalas keberhasilan ya bang!"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "122450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl.Ratu, Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@rewinaaa",
                "kesan": "Kakak baik dan asik",  
                "pesan":"Semoga langkah kecil kakak terus berdampak besar!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MoE_wwXR5al-Bz3VGTzwJHSuLL8HfDGf", 
            "https://drive.google.com/uc?export=view&id=1doyFBIoxIaNYRpFvCRTut2r-O2yHvBdh", 
            "https://drive.google.com/uc?export=view&id=1LEpyVqOQIYLsKw1TVoPYkz7lYxsM2o28", 
            "https://drive.google.com/uc?export=view&id=1lPNDz17mav-2s-iuput59YoD36cxVgLJ", 
            "https://drive.google.com/uc?export=view&id=1ezVIAdXYd5bCznZjOEbkHaZGZSD0oaYc", 
            "https://drive.google.com/uc?export=view&id=1CJ0aPJis1hp3d7fECcXkARGSDJYCTHFW", 
            "https://drive.google.com/uc?export=view&id=17hjiK1ouOuWAUCu3uw5MYEbVs6W7dZWf", 
            "https://drive.google.com/uc?export=view&id=1PT3Y_cGoJ_xFmIvziVgrM0phI_gAUO-N", 
            "https://drive.google.com/uc?export=view&id=1OgiSBXRSScRyCuvic2wYcboR5L-Kzlgm", 
            "https://drive.google.com/uc?export=view&id=1uYIF0yVG9pjsNooJ7dDggKS4zZ8oG2Fq", 
            "https://drive.google.com/uc?export=view&id=1qTR1eH-54q12r-irP8Xu0CSIS5LjnKAq", 
            "https://drive.google.com/uc?export=view&id=1qUbrY1AFBlani--Bn0kucrccoe1l4-TC", 
            "https://drive.google.com/uc?export=view&id=1-MI9FVczXP6XlYEBvclpw4O_QoDl73lL",
            "https://drive.google.com/uc?export=view&id=1sktJ5tX9_0tLLo4SdI4s3Hr-dKd9ARLY", 
            "https://drive.google.com/uc?export=view&id=10qwIkHuLV61btVtTcdI06tE8CtuufV8L", 
            "https://drive.google.com/uc?export=view&id=1xnRO-ijZAnlHS2Hq2WrNHWO_KgCMeRB0", 
            "https://drive.google.com/uc?export=view&id=13S16_-aExQ02g87pFkoNFIK5NMtwvu89", 
            "https://drive.google.com/uc?export=view&id=1K3_meeMXK2vrAORYmDVi9ilCmdE5ABqv", 
            "https://drive.google.com/uc?export=view&id=1QQCCMjZC3iU1BeMByrtiTACqwgR_f1lm", 
            "https://drive.google.com/uc?export=view&id=1_uVflCplCzI1_0epqSp5T2dJUD42S-Bx", 
            "https://drive.google.com/uc?export=view&id=1sq5c4EUqT_mLCLFgRDR3Z7IQax3lEbWy", 
            "https://drive.google.com/uc?export=view&id=1D18mfYTAR2w08v3zd9_cLo4XR_hXXu5m", 
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123340083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya ramah dan pembawaannya santai",  
                "pesan":"Semoga semua hasil kerja keras kakak dibalas yang terbaik"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep . Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya positif vibes banget",  
                "pesan":"Selalu jaga kesehatan kak!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadani, Sukarame",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya santai dan baik juga",  
                "pesan":"Semoga yang diharapkan tercapai bang!"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. lapas,Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya kalem dan tenang vibesnya",  
                "pesan":"Semoga dikelilingi orang baik kak!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnya baik dan asik juga",  
                "pesan":"Semoga semua usaha diberi kelancaran ya bang!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya kalem tapi tegas",  
                "pesan":"Semoga sukses terus dan bisa jadi inspirasi buat kami!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya santai dan ramah juga",  
                "pesan":"Semoga selalu diberi kelancaran di setiap langkahnya!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak humble banget, enak diajak cerita",  
                "pesan":"semangat jalani hari harinya kak!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya ramah banget dan baik",  
                "pesan":"Semangat dan semoga impiannya tercapai ka!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Pramuka",
                "alamat": "Bandar lampung",
                "hobbi": "Dengerin musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya punya aura tenang dan dewasa",  
                "pesan":"Semoga selalu bahagia dan diberi kelancaran"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya punya vibe positif yang menenangkan",  
                "pesan":"Semoga energinya gak pernah pudar ya kak!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya keliatan kalem tapi hangat",  
                "pesan":"Semoga selalu dikelilingi orang-orang baik kak!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "Main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakaknya baik ngajarin saat praktikum",  
                "pesan":"Semoga hal baik juga selalu nyamperin kakak"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "12345004",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakaknya baik dan keliatan sabar banget",  
                "pesan":"Semoga kakak selalu dikasih kebahagiaan"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kakaknya ceria banget dan ramah",  
                "pesan":"Semoga makin banyak hal baik yang tercapai"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abangnya berwibawa tapi tetap humble",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4m",
                "hobbi": "Isengin orang",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya baik banget dan suka nolongin aku",  
                "pesan":"Semoga hal baik juga selalu nyamperin kakak"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl Teratai no 27A, Kedaton",
                "hobbi": "Jalan jalan, Main game, Tidur",
                "sosmed": "@biyokcb",
                "kesan": "Abangnya humble banget dan asik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123440065",
                "umur": "20",
                "asal":"Kotabumi, Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya chill dan easygoing",  
                "pesan":"Semoga makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123440003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakaknya keliatan ceria dan ramah",  
                "pesan":"Semoga terus bahagia dan dimudahkan segalanya"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123440102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": " Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya pembawaannya adem banget",  
                "pesan":"Semoga selalu dikasih ketenangan di setiap langkah"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123440096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "Kakaknya sopan dan santai banget orangnya",  
                "pesan":"Semoga terus jadi pribadi yang nyenengin kayak gini"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dv3HPu15RVFqPYWAh_BnfZWSW4V9cLtm",
            "https://drive.google.com/uc?export=view&id=1tt7ZQsEgZbLdD1TN2IrIQKKmeMRbOoiV", 
            "https://drive.google.com/uc?export=view&id=1Xw3xqX5LZX7UhXI-DNYy08BMjfIsft2z", 
            "https://drive.google.com/uc?export=view&id=1R5vtW-Op6yjfyDROlIBNKNmBVt0tDFdX", 
            "https://drive.google.com/uc?export=view&id=1MMy90BKupObyILsDyVVrgXR3qM-U_Cvc", 
            "https://drive.google.com/uc?export=view&id=1_QNbS9XiX8G9tkIFcWsJzxJcCjI8w_H1", 
            "https://drive.google.com/uc?export=view&id=1QWn0sPm00ajxA7TZ5ZJ4SrzENYRkZLH1", 
            "https://drive.google.com/uc?export=view&id=1rEQ2DfyHqKDaNejg7orapgBl03bBSRct", 
            "https://drive.google.com/uc?export=view&id=1XF6E0nQC-thfrpLG7daREISya9cxh01L", 
            "https://drive.google.com/uc?export=view&id=1OMa7XT6YAm_O38qaIHl_Ops9O0jiZc5R", 
            "https://drive.google.com/uc?export=view&id=1HpdYPHSgXicaKhUeWMl_QAWpQYQUb4d-", 
            "https://drive.google.com/uc?export=view&id=1r4BnVO30MwoHEX24WUbHtx4xr8GLw8JK", 
            "https://drive.google.com/uc?export=view&id=17WatBmu-7YXpE5h77pbXcOck3SDJrbpe", 
            "https://drive.google.com/uc?export=view&id=1eNKOO53FdaVEKf1cACl9qMFooYBY64F2", 
            "https://drive.google.com/uc?export=view&id=1p-U9DeiIkq5yqdm_yDaNUxOMoUlbj5kk", 
            "https://drive.google.com/uc?export=view&id=1I76oaBAW4dhOMgszMFdvWbge89dFwbyL", 
            "https://drive.google.com/uc?export=view&id=1tLJFIBvFDJFKQyxZ_gRJn_C5X1FHvsa7", 
            "https://drive.google.com/uc?export=view&id=1653zQLkclgL0xG797Bqs--UKw7VCGE9Y", 
            "https://drive.google.com/uc?export=view&id=1aqrXY2UM9A8NDKXV02ndq29izRqyzV9l", 
            "https://drive.google.com/uc?export=view&id=1lbK7pfgP6y9tSd5zYNyO-NjTQiJN_BUd", 
            "https://drive.google.com/uc?export=view&id=1v95jHmHII1TDhc3fbFWPYmmFYPZIV4L5", 
            "https://drive.google.com/uc?export=view&id=10FcgJ1Cu8HAaPPSp2el-bii5rbC7fUZW", 
            "https://drive.google.com/uc?export=view&id=13hCKcbRoKhzZrqdltFD2pxheH3ZZy0YM", 
            "https://drive.google.com/uc?export=view&id=1cI7kxa59RQvt4lXIIKYth82H0izlNn1P", 
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "21",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnya berwibawa tapi tetap humble",  
                "pesan":"Semoga selalu bahagia dan diberi kelancaran"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya baik dan asik banget",  
                "pesan":"Semoga makin sukses dan bahagia selalu"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya lucu dan easygoing",  
                "pesan":"Semoga yang diinginkan tercapai"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya keliatan dewasa tapi tetap asik",  
                "pesan":"Semoga terus bahagia dan dimudahkan segalanya kak"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnyanya baik dan easygoing banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya keliatan ceria dan ramah",  
                "pesan":"Semoga selalu diberi kesehatan dan semangat"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakaknya friendly banget",  
                "pesan":"Semoga kakak terus dikelilingi orang-orang baik"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya keliatan sopan dan murah senyum",  
                "pesan":"Semoga yang diinginkan tercapai"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abangnya humble dan asik banget",  
                "pesan":"Semoga selalu dikelilingi kebahagiaan"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya keliatan sopan dan positif",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya kalem dan sopan banget",  
                "pesan":"Semoga kakak makin sukses"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya vibes-nya positif banget, yareuu",  
                "pesan":"Semoga semua usaha kakak berbuah manis"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya asik, pinter dan gokil",  
                "pesan":"Semoga makin sukses dan semangat bang!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakaknya pembawaannya tenang tapi nyenengin",  
                "pesan":"semangat nge aspraknya kak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl.Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak energik banget",  
                "pesan":"Semoga kakak makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abangnya baik dan keliatan sabar banget",  
                "pesan":"Semoga selalu bahagia dan diberi kelancaran"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Abangnya humble dan asik",  
                "pesan":"Semangat dan semoga diberi kemudahan"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya baik dan easygoing banget",  
                "pesan":"Semoga semua urusan kakak selalu lancar"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakaknya positif vibes banget dan humoris",  
                "pesan":"Semoga makin sukses dan bahagia selalu"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya cantik, ramah dan murah senyum",  
                "pesan":"Semoga kakak terus dikelilingi orang-orang baik"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya vibes-nya adem banget",  
                "pesan":"semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya menyenangkan dan ramah",  
                "pesan":"Semoga kakak makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya keliatan ceria dan ramah",  
                "pesan":"Semoga semua kerja kerassnya gak sia-sia"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "Kakak baik banget dan humble",  
                "pesan":"Terimakasih ka udah tutor ale"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()
  
if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19n6P6jdwse1v96lqqs9xLWDCQrMaJ5BD", 
            "https://drive.google.com/uc?export=view&id=1BPcUsQpAszXtCTwOqNT2eSK_-EqUD5iE", 
            "https://drive.google.com/uc?export=view&id=1XQEOM5LlyS3kOIKsprg2RGz74K9jo1Cy", 
            "https://drive.google.com/uc?export=view&id=1sER4avmUZDHkzioBR2k8iX4L6ZGOCJnK", 
            "https://drive.google.com/uc?export=view&id=195h-F76jnEHE1dZWPPmUMtZiSnV-Dn6r", 
            "https://drive.google.com/uc?export=view&id=1UQ8ST_IfFzO9p0dSftQsOZjaQfyH-L6R", 
            "https://drive.google.com/uc?export=view&id=1Dvy_MKX17ZK6jaUGpIJmBofVjIoBa1oO", 
            "https://drive.google.com/uc?export=view&id=1YWSTeRU7aHdq2e65wUaJwnCFLeuya-qj", 
            "https://drive.google.com/uc?export=view&id=1kpe-tUGr9xwXCDb5QDyWYcPEgEZtyP7A", 
            "https://drive.google.com/uc?export=view&id=1cGG5WF909vJHeIIZ7kkFJUS5bJy5nypS", 
            "https://drive.google.com/uc?export=view&id=1mKqL4iQhx3EBj6kshzwKHImNUHQd_fSp", 
            "https://drive.google.com/uc?export=view&id=1wY7gOrGM0gokiTZjhJbAlXHweZN_Kik6", 
            "https://drive.google.com/uc?export=view&id=15v4AzWJCoEKOTld9DxcwFMKijQ2ONi7S", 
            "https://drive.google.com/uc?export=view&id=1KaNNnqkX0SrDmuIt2UZJpVWkc1q8oyhg", 
            "https://drive.google.com/uc?export=view&id=1sc03EPrIavPCaAmgmzZmVOZ3JLTxN66a", 
        ]
        data_list = [
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Style kakaknya kece abis",  
                "pesan":"Terima kasih udah jadi sosok yang peduli"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":" Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": " Airan Raya",
                "hobbi": " Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
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
                "nama": "Saraf Wasti",
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
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c28aN4C_N_9aZargajCrChf5T3kkLAUT", 
            "https://drive.google.com/uc?export=view&id=1YpuQT0WGacnFYzD7QuMpPbhtB5vJWzk7", 
            "https://drive.google.com/uc?export=view&id=1yYwyWDVXZKhhmI6II3OcT00n191xO7U4", 
            "https://drive.google.com/uc?export=view&id=1qssPqDz8bALxVhMm-9JF_o-EsIQhRMKE", 
            "https://drive.google.com/uc?export=view&id=1BfQNQrsvgpE0vKgfhSJ1sfe9_63nt2My", 
            "https://drive.google.com/uc?export=view&id=1CHB-7B2Iw9MIUi6z1zMIJmChlkqQgb82", 
            "https://drive.google.com/uc?export=view&id=1NPduj9Hk38oAJ4jZqEicZaDPC5_AYWZ0", 
            "https://drive.google.com/uc?export=view&id=1Jgg-bztd0qbS50tIG-7IuK_ouOrax0Mj", 
            "https://drive.google.com/uc?export=view&id=1rufCAtAWPw7hYMXiX_7ZT0vQwP5JeQNN", 
            "https://drive.google.com/uc?export=view&id=1orO9zGqu8jGTP9ZMdbzjUjkHlfXs8s5H", 
            "https://drive.google.com/uc?export=view&id=1AHsXG7i16c-mVIXVB4LO2GXBCnuVc3Kq", 
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "Beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Menonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. perwira 2",
                "hobbi": "Menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RSO8nBnBms5z0f9-ZJ1vayDrv0jRKL6E", 
            "https://drive.google.com/uc?export=view&id=1D3N7eNxHIiRqNr_9JWXy9pPjZXBcZsBD", 
            "https://drive.google.com/uc?export=view&id=1YFU2rH3mHd08KfMx-N7RQQWQ7hfA1-rB", 
            "https://drive.google.com/uc?export=view&id=1N8Gb62waeSyk79tiXTcNnTOhv54nOVCh", 
            "https://drive.google.com/uc?export=view&id=1yeznLoo6K2CGA1v4EweoYypJpGfNwEt_", 
            "https://drive.google.com/uc?export=view&id=100ONpvG6mhntC24eCfzehBUus60oTb2T", 
            "https://drive.google.com/uc?export=view&id=1gq5aDVeOmrbzbudjZdBlGfVtSEWaiaTb", 
            "https://drive.google.com/uc?export=view&id=1AEJ1XnVPFugCUGYq3VOsCRymlNhrDITU", 
            "https://drive.google.com/uc?export=view&id=1AjoI0KeVPY979dCnM5BCSDY4H_n24UGz", 
            "https://drive.google.com/uc?export=view&id=1b3zt-Dh8gKHEDvr8sLoBiAFe9jmjGBp8", 
            "https://drive.google.com/uc?export=view&id=1ncDn6Vf9pohInOXNhmUn_-oOM0pTwkQw", 
            "https://drive.google.com/uc?export=view&id=1f8mQheTVoVjBprk64NSe1AmQmXb6eRrm", 
            "https://drive.google.com/uc?export=view&id=1CAfPOdQZ4p_d5Uiez_ScaQkln4vvSJQO", 
            "https://drive.google.com/uc?export=view&id=1QWh_hZoaXsS0WZ88fWhTsf821Qz0kf-5", 
            "https://drive.google.com/uc?export=view&id=1g8vaPR2juJ3WXlQwd88hdKq1yHwYU8Fy", 
            "https://drive.google.com/uc?export=view&id=1E6Vf3d1ptwBkc8xjFRdc-Vgs9AGTMxnv",
            "https://drive.google.com/uc?export=view&id=1B5DijAV1vWfW2HBhdoL_bX-1aWxoLxYd", 
            "https://drive.google.com/uc?export=view&id=1rSajHs8zZOlrEzkoVQmWni3nXlPSIhFD",
          
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jati Mulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "jl. Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "jl.pangeran senopati raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labukan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumbar",
                "alamat": "jl.Lapas, kec.Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak ",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()



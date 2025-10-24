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
            "https://drive.google.com/uc?export=view&id=1Vh9yORUBjpTWf55CLU6DaNh-Z6g3bhfY", #Bang Rendra
            "https://drive.google.com/uc?export=view&id=1rVgFdEby2AagklU-9qSm91C4JOXSpu2r", #Bang Jon
            "https://drive.google.com/uc?export=view&id=14Cim2M_BwRlSJFm9uEJJyf7wSNRIGvAR", #Kak Elisabeth
            "https://drive.google.com/uc?export=view&id=1Cx1EaGmGEIoANS2FjvE-iu95nWuWL8vn", #Kak Syadza
            "https://drive.google.com/uc?export=view&id=1XpiU-5bNuHUYQ5wNATCYFhwSCwnMSSs5", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=13kvIrF97xxPsOrZfkkt7OCjg8LpZDdnP", #Kak Farahanum
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Bang Rendra humbel banget, asik kalo ngobrol",
                "pesan":"semangat terus banggg"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjon",
                "kesan": "Abang ini asik banget ",  
                "pesan":"Semangat tugas akhirnya kak"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy Dalem",
                "alamat": "Ayres Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini asik dan rame bangett",  
                "pesan":"semangat kak kuliah sama organisasinya !!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini kalem banget",  
                "pesan":"semangat teruss kak organisasi dan kuliahnyaaa !!!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tik tok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini keren  banget sumpahh",  
                "pesan":"semangat semangat semangatt semangat jadi orang keren kak !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumbar",
                "alamat": "Gya Kost Korpri",
                "hobbi": "Cute Jendral",
                "sosmed": "@farahanumafifahh",
                "kesan": "Cntik bangett",  
                "pesan":"semangat menjalani hari hari kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iHZGu1q7MfvM_hkywykjdjrVrA5ckrNw", #Bang Jemi
            "https://drive.google.com/uc?export=view&id=1GjRZ2z2egRiJ7ExfyN9okpY0Qh5Z8kag", #Kak Dhea
            "https://drive.google.com/uc?export=view&id=1iyRZ29NJrxgn9uC5_ZA3sb11tgjdRLiO", #Kak Renisha
            "https://drive.google.com/uc?export=view&id=1XhpT_Dy-nn-az-RIiTwQhRzbBip8syuH", #Kak Anisa
            "https://drive.google.com/uc?export=view&id=1FipXC151dTKIphWOJh2BBeIoyyhJ9n49", #Bang Dharu
            "https://drive.google.com/uc?export=view&id=1hxzhwgRAJQa6O8de-uE1MGJUi82ytRt1", #Kak Feby
            "https://drive.google.com/uc?export=view&id=1-9Leqk1tpf97E9JaM9ltEJEdZ2cSUKU_", # givaro
            "https://drive.google.com/uc?export=view&id=1nTJnmXPVwH-0i0XY1Z37hoRvob_S4uuu", #Bang Mirzan
            "https://drive.google.com/uc?export=view&id=1dj5J3AVOCpP8BSZ9CmmQ5ARm1V975ZBY", #Kak Berliana
            "https://drive.google.com/uc?export=view&id=1wqepwu2JF4CleV7fyJlysI95VpAUjsF5", #Kak Juesi
            "https://drive.google.com/uc?export=view&id=1Fr6LZgS_e3x4S7Zv3raPV5XDBgrJEMHG", #Bang Ridho
            "https://drive.google.com/uc?export=view&id=1scRcrWpX7cLVkAjELGTJPIwPr217NcQc", #Bang Feryadi
            "https://drive.google.com/uc?export=view&id=1UCMWirIFSETLCxyffDHg_2ehFOI4q4z6", #Kak Monica
            "https://drive.google.com/uc?export=view&id=17j7RLivu-ZFLd3FRUDOirNg-f79OeLR2", #Kak Nashwa
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "nonton orang kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "abang 22, bang Jeremia keren banget, keliatan tegas dan bijak waktu ngobrol",
                "pesan": "Semoga makin sukses ya bang, terus jadi sosok yang inspiratif!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "lomba ga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak Dhea orangnya ramah dan punya aura positif yang menular banget",
                "pesan": "Semoga selalu bahagia dan semua hal baik datang ke kak Dhea!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha orangnya lembut dan sopan, tapi juga seru kalau diajak ngobrol",
                "pesan": "Semoga kakaknya selalu lancar kuliah dan makin sukses terus ya!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Main bola, belajar",
                "sosmed": "@i",
                "kesan": "Kak Anisa semangatnya keren banget, orangnya juga asik dan gampang akrab",
                "pesan": "Terus semangat ya kak, semoga cita-citanya tercapai!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live Putri Padang",
                "sosmed": "@dhruchyo",
                "kesan": "Abang Dharu santai tapi punya aura tangguh gitu, enak diajak ngobrol juga",
                "pesan": "Semoga selalu diberi jalan terbaik dan makin berprestasi bang!"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kak Feby vibes-nya positif banget, orangnya juga lucu dan gampang nyambung",
                "pesan": "Semoga rezekinya lancar dan selalu dikelilingi hal-hal baik ya kak!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi, Lampung",
                "hobbi": "dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Abang Givaro asik banget, gayanya chill tapi tetap berwibawa",
                "pesan": "Semoga makin sukses dan bisa terus ngelakuin hal-hal keren!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya kalem banget, pembawaannya tenang tapi tetep friendly",
                "pesan": "Semoga selalu diberi kemudahan dan kebahagiaan dalam setiap langkah!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kak Berliana punya semangat yang nular, selalu ceria dan ramah banget",
                "pesan": "Semoga terus bahagia dan makin banyak hal baik yang datang ya kak!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kak Juesi nyenengin banget, gayanya santai tapi sopan",
                "pesan": "Semoga makin banyak kesempatan bagus yang datang buat kak Juesi!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main paddle",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang Ridho enerjik dan keliatan semangat banget, seru diajak ngobrol",
                "pesan": "Semoga karier dan kuliahnya makin lancar terus ya bang!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal": "Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi badge Google Cloud",
                "sosmed": "@fer_yulius",
                "kesan": "Abang Feryadi berwibawa banget, keliatan bijak dan tegas",
                "pesan": "Semoga semua urusannya dimudahkan dan selalu sukses ke depannya!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica ceria banget, enak diajak ngobrol dan humble juga",
                "pesan": "Semoga kuliahnya lancar dan makin semangat terus ya kak!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Farakan",
                "hobbi": "nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa punya pembawaan yang adem, enak banget dilihat dan diajak ngobrol",
                "pesan": "Semoga makin sukses dan selalu dikelilingi orang-orang baik!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aY4rkqcTQUKHC5yh0pQLVc1f244uVLHE",
            "https://drive.google.com/uc?export=view&id=1wA13TEORYp690XiiIE22ZJE2jJRViA6B",
            "https://drive.google.com/uc?export=view&id=1VRkEBpNciL131w_C_XrFEwnIpmBUKing",
            "https://drive.google.com/uc?export=view&id=1PdLc2oAVZQDiyOU_LkIbkGaT1XoVgGif",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Dengar lagu, nyanyi, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Bintang asik banget, kalo ngobrol wawasannya luas banget",
                "pesan": "Semoga makin keren dan sukses di semua hal, semangat semester 7 nya bang!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak Nadya vibes-nya lembut tapi tetep ceria, baikk banget orangnya",
                "pesan": "Semoga semua yang dicita-citain bisa tercapai, dan hari hari kakak bahagia!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main ice skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah punya aura calm tapi tetep fun, adem bnaget liatnya!",
                "pesan": "Semoga selalu dilancarin urusannya dan makin sukses tiap harinya!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomart Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Lia kalem tapi berkarisma, asikk banget kalo ngobrol",
                "pesan": "Semoga kuliahnya lancar terus dan makin banyak hal baik yang datang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11FQfgXrPeYHylQXWULa2TSpbDM2QTX-w", # Bang ferdy
            "https://drive.google.com/uc?export=view&id=1hjRL93ym-cpmuoXTq8jbtSoiFDiktdju", # Kak Nisrina
            "https://drive.google.com/uc?export=view&id=18mUYFHCkhIkEB_JZm3kR8xBI3CAXvtuj", # Kak Allya
            "https://drive.google.com/uc?export=view&id=19k8u84AWasQYmtvf95i3_TL1sxO7hlcz", # Bang Ahmad
            "https://drive.google.com/uc?export=view&id=1ijVfPWvXnhVsBEvgulFE49C7yTPPzSso", # Kak Arin
            "https://drive.google.com/uc?export=view&id=1cpjBjHoz5qwEtHC0Sw_ATGutnth49AZQ", # Bang Daffa
            "https://drive.google.com/uc?export=view&id=1j__twXKRMVbhWU-qZOJVZPr42iwNssql", # Bang Ginda
            "https://drive.google.com/uc?export=view&id=1bKAKUWK65omtD8AONP5HS0QmlKf80emb", # Kak Natasya
            "https://drive.google.com/uc?export=view&id=1iV7L2SaqO6B4a9PpT89HrnxadAp0v2io", # Bang Nobel 
            "https://drive.google.com/uc?export=view&id=1khKRl95oMDaB4ugvf8jNTccEpZ4r1P-U", # Bang Aji
            "https://drive.google.com/uc?export=view&id=11hiDeqKw_kccB6J7XMs39B_CC39m3St9", # Kak Vany
            "https://drive.google.com/uc?export=view&id=12jW0cdNMxvEvT2qQawPo6wVdI-OmPo4-", # Bang Sahidin
            "https://drive.google.com/uc?export=view&id=1oubq5cjBgG0GsEb6gTEEQ6MWSGiP013F", # Bang Ali
            "https://drive.google.com/uc?export=view&id=1RNwiY55qxI5KyKAO1iTTp-mGmsTq-3Rz", # Kak Gusti
            "https://drive.google.com/uc?export=view&id=16jXewXXIpinzbjjXCbeTjTFbky9MeeZe", # Kak Kharisma
            "https://drive.google.com/uc?export=view&id=1BLAqhX31F4fflnf11RoxCDJbJLPgYDb3", # Kak Rosalia
            "https://drive.google.com/uc?export=view&id=1RttimXZga9viQso7wjEsOXmmF09SP23N", # Bang Sahid
            "https://drive.google.com/uc?export=view&id=1yhV9A5_lEZC_HabbmouzLmu_D-A7Gs7p", # Bang Daffa A
            "https://drive.google.com/uc?export=view&id=1zr9TCZWtneSqhko2rHkEIMl8pCFf9yWX", # Kak Erma
            "https://drive.google.com/uc?export=view&id=1WsM82_E9jj4hea0ItcfQeq3P9IIqWLqp", # Bang Ihsan
            "https://drive.google.com/uc?export=view&id=1XbJogtT5DK5RkGZuts40JbxXGhzL_eUI", # Bang Kevin A
            "https://drive.google.com/uc?export=view&id=1nDEgDYUPgr_Yi5RjGk2MNO-MzKbQv0Vn", # Kak Lidia
            "https://drive.google.com/uc?export=view&id=1B4jOtJPR13N7zdLzSGta2kMurpGfifY9", # Bang ridwan
            "https://drive.google.com/uc?export=view&id=1gzMcTQcyRuwisn73In4PYEOTTkLEMnr7", # Bang Uliano
            "https://drive.google.com/uc?export=view&id=1AjJs8BzSRQrmDV0UtLN0Z6qZ67OdZ4z8", # Kak Rewina
            "https://drive.google.com/uc?export=view&id=1ywubKjfE5q1ecwXWzHOCOJ2EfS5XHniJ", # Bang Benget
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Bang kevin kelihatannya tegas, tapi aslinya baik dan ramah banget",  
                "pesan":" semangat bang semester 7 nya"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "jalan jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak afifah cantik banget, kalau senyum mirip sama kakak kelas SMA ku",  
                "pesan":"murah senyum terus ya kak"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kak alya pembawaannya tegas, tapi aslinya baik dan peduli bangett",  
                "pesan":"Semangat ya kak alya, semoga selalu dikelilingi hal hal baik"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tanggerang Selatan",
                "alamat": "Kontrakan GH",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang Ahmad murah senyum banget",  
                "pesan":"Sukses terus bang"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Kost Orange",
                "hobbi": "Ngekader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arin bagus banget kalo make up, outfitnya juga elegan banget",  
                "pesan":"Semangat kak arin kuliahnya, semoga hari harinya menyenangkan"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jailin orang sammpe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Bang Daffa walau keliatannya galak, tapi aslinya baikk bangett",  
                "pesan":"semangat terus bang daffa menjalani smester 5 nya,, semoga lanjar terus urusannya"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main Game",
                "sosmed": "@ginda_mrp",
                "kesan": "Bang Fajar asik orangnya mah ramah",  
                "pesan":" sukses terus bang, semoga selalu dikelilingi hal hal baik"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kostan putri gerbang barat sebelah sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Kak Natasya asikk kalo ngobrol dan baikk banget",  
                "pesan":"semangat terus ya kak natasya menjalani smester 5 nya semoga lancar teruss"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngader",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel profesional banget, bisa menempatkan sikap dengan pas sesuai situasi,saluttt",  
                "pesan":"Semangat terus ya bang, semoga lancar terus segala urusannya"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Fam",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Bang aji tuh bener bener profesional banget, tau kapan waktunya buat tegas, ramah, dan baik",  
                "pesan":"Sukses terus ya bang Aji, semoga kakir kedepannya terus merokett"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vani cantik, baikk banget aslinya mahh",  
                "pesan":"Semola selalu dikelilingi hal hal baik dan mudah semua urusannya kak"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya ramah bangett",  
                "pesan":"Sukses terus ya banggg"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung timur",
                "alamat": "nangka 4",
                "hobbi": "main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya ramah bangett",  
                "pesan":"sukkses terus ya bang semangat kuliahnyaa"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "kak gusti Ramah banget, murah senyum",  
                "pesan":"semangat kuliahnya kak dan semoga dipermudah segala urusannya "# 1
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450079",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak kharisma cantik banget, ramah lagi",  
                "pesan":"semangat terus ya kak kuliahnyaa"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kak rosa ramah bangett",  
                "pesan":"Semoga hari hari kakak selalu baaik baik sajaa ya"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jalan Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya ramah bangettt, enak kalo diajak ngobrol",  
                "pesan":"Sukses terus ya bangg"# 1
            },
{
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat":"Abangnya humbel banget kalo ngobrol juga asik ",  
                "pesan":"semangat ya bang kuliahnya dan semoga selalu dikelilingi hal hal baik"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "Kakr Daniar ramah banget, humbel banget padahal baru kenal ",  
                "pesan":"Sukses terus yaa kak terutama di bidang tarinyaa"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Belwis",
                "hobbi": "Joki Strava",
                "sosmed": "@ihsan.myusus",
                "kesan": "Bang Ihsan Super Ramah bangettt, Jadinya ga canggung walaupun baru kenal",  
                "pesan":"Semdoga selalu dipermudah segala urusannya ya bangg "# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Panjang Selatan",
                "hobbi": "Terjun Payung",
                "sosmed": "@kevinaj__",
                "kesan": "Bang kevin pembawaannya cool, tapi tetep ramah",  
                "pesan":"Semangat terus ya bangg kuliah dan menjalani hari harinya"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kaknya kalem,baik dan ramah bangett",  
                "pesan":"Semoga selalu dikelilingi hal hal baik ya kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton Anak Tari Perform",
                "sosmed": "@m.ridwan_22",
                "kesan": "Abangnya biaik dan ramah bangett",  
                "pesan":"Semangat terus kulliahnya bang"# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngerjain Soal MTK",
                "sosmed": "@liano.wlm",
                "kesan": "Bang Liano walaupun pembawaannya tegas, tapi ternyata baikk kokk",  
                "pesan":"Semoga diperlancar dan selalu didkelilingi orang orang baik ya bang"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Ratu, Bandar Lampung",
                "hobbi": "Nonton Anime",
                "sosmed": "@rewinanaa",
                "kesan": "Kak rewina baik bangget, ramahhh",  
                "pesan":"Semoga kak rewina diperlancar segala urusannya"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Bang benget tuh devinisi serba bisa dan ada dimana mana",  
                "pesan":" Semangattt terus ya banggg bengett, semoga sukses terus mudah urusannya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LtknA1fvm80lsqwy2KcWpFbryIXHYeJS", # Bang Randa
            "https://drive.google.com/uc?export=view&id=1fDgHxRmDeWx3vG3NxqrU4mC8OnLBBbSU", # kak rut junita
            "https://drive.google.com/uc?export=view&id=1NcWN18nepvode-eZao-nrNrhZribugWy", # bang regi
            "https://drive.google.com/uc?export=view&id=15BqCrk9Vbh_NqocEYiQ7Z9gu0HtDauIX", # kak aisyah
            "https://drive.google.com/uc?export=view&id=1WRKuokfXHY3zkMDVhH3qx95hd1cIb3Gy", # Bang Fadil
            "https://drive.google.com/uc?export=view&id=1-ZTamxEkMYs1xOfX-8VxYDYO_kqkvBU5", # Bang Aqil
            "https://drive.google.com/uc?export=view&id=1byA8WMX4mhymYerjDTqakdObhbts4ixm", # Bang Naufal
            "https://drive.google.com/uc?export=view&id=1S8YCrSMeQepr75NzQLIeW58y5Alqajzg", # Nak Nadia
            "https://drive.google.com/uc?export=view&id=1pYJeYQaAKpRN4SDdNLbFmKF0DnPWQdnw", # kak Marleta
            "https://drive.google.com/uc?export=view&id=1Ssdmz_sMmtxsti5OfJsJU6iByN50gEMO", # Bang Akeyla
            "https://drive.google.com/uc?export=view&id=10mWxrp1P0vgrcNmgzo2N-lJjHIaNT3M7", # Kak Anggi
            "https://drive.google.com/uc?export=view&id=1KqUBip2p4G7d3X1FCz57x7HLqSfeoiz4", # kak efi
            "https://drive.google.com/uc?export=view&id=1uTwW_g7tyKV5JdPBA1Cn-e_JBX28vfRm", # kak fabiolla
            "https://drive.google.com/uc?export=view&id=16m6EB7UrkH2IL02PFirZLxpgljpnLCzq", # kak fairuz
            "https://drive.google.com/uc?export=view&id=1ypVhPbd6wPunic17CGmzqUsWAU0MUb8V", # kak tanty
            "https://drive.google.com/uc?export=view&id=132u1iyQDRtqL30KtSSvgYifWZ-YnfUjs", # Bang Eggi
            "https://drive.google.com/uc?export=view&id=1f4lFXVuI011fYMyRf1nMm0RvYyvAAl-r", # Kak Afifah
            "https://drive.google.com/uc?export=view&id=1TSFWj4saF6uiz2WQz3qY7K33B0egXtYf", # Bang Fabio
            "https://drive.google.com/uc?export=view&id=1c9vrZOpFD1GCU1vrR-52ZzpJCbqz7zIT", # Bang Giovani
            "https://drive.google.com/uc?export=view&id=1X6984zwyARp97PZWLGGj0wnhuIRssH5L", # Kak Rahma
            "https://drive.google.com/uc?export=view&id=12BJSQjUPezrnzbF0gFWMwluRw5OK1UE4", # Kak Rahmah
            "https://drive.google.com/uc?export=view&id=16Yz5sNGK9jD7DaHFE2Wcw2JTS_V-ekJ-", # Bang Razin
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "1222450083",
                "umur": "22",
                "asal":"Serang,Baten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berenang",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa ramah dan baik banget, jadi ga canggung waktu pertama kenal",  
                "pesan":"Semangat ya bang kuliahnya, dan semoga selalu dikelilingi hal hal baik", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak junita Ramah juga baik bangett walaupun baru ketemu",  
                "pesan":"Semoga selalu mudah urusannya dan dikelilingi orang orang bbaik ya kak", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "Bang regi keren bangettt, definisi pinterr",  
                "pesan":"Sukses terus bang, semoga karirnya terus merokettt", # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Seneng banget bisa ketemu kakak NIM sebaik kak Aisyahh",  
                "pesan":"Semangat terus ya kak kuliahnya, dan semoga selalu dikelilingi hal hal baik", # 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Bang fadil pinter bangett ramah lagii",  
                "pesan":"Sukses terus ya bang, semoga karirnya makin naikk", # 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang aqil baik dan ramah bangett",  
                "pesan":"sEmoga mudah semua urusan dan tercapai cita cita mu ya bang", # 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "Bang Naufal kalem, baik dan ramah banget",  
                "pesan":"Semoga lancar terus ya bang urusannya dan lulus cepat", # 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kak Nadia Asik banget kalo ngobrol",  
                "pesan":"selalu semangat menjalani hari harinya ya kak", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "Kak marletta cantik, baik dan ramah bangettt",  
                "pesan":"jangan berubah ya kak, tetep jadi orang yang ramahh", # 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234500119",
                "umur": "20",
                "asal":"Pramuka, Bandar Lampung",
                "alamat": "Perum Bukit Alam Permai 3, Blokk C, No.9",
                "hobbi": "Dengrin musik",
                "sosmed": "@keyashafi_",
                "kesan": "Bang Akeyla jugaa kalem, baik, ramah lagiii",  
                "pesan":"Semangat ya bang kuliahnya, semoga semester ini ipk nya 4 amin", # 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bummisari Kec.Natar",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kak anggi super ramah banget, jadi ga canggung walaupun baru kenal",  
                "pesan":"Semangat terus kak anggiii, semoga selalu mudah urusannya", # 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Sale, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi baik banget apalagi kalo ngajar tutor, sabarr banget",  
                "pesan":"Semangat terus ya kak Efi kuliah dan menjalani hari harinya", # 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kak Fabiola udah cantik,ramah, baikk lagii aku dikasih penaa..makasih ya kak",  
                "pesan":"Semangat terus kak kuliahnya semoga kakak juga selalu dikelilingi orang orang baik", # 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kak Firuz positif vibes banget adem liatnya",  
                "pesan":"Semangat ya kak fairuz kuliahnyaa", # 1
            },
             {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kak Tanty ceria dan asik banget pembawaannya",  
                "pesan":"Semangat dan Sukses terus ya kak Tanty, Jangan bosen jadi orang keren kakk", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "Bang Eggi keren banget, apalagi kalo njelasin codingan kalo praktikum",  
                "pesan":"Sukses terus bang, semoga karir kedepannya baguss", # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang (main game)",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah Baik dan ramah bangett",  
                "pesan":"Semangat ya kak kuliahnyaa", # 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer),tidur,jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "bang Fabio Ramah bangettt, asik juga kalo diajak ngobrol",  
                "pesan":"Semoga lancar semua ya bang urusannya dan jangan bosen jadi orang asik bang", # 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@giofaniars_",
                "kesan": " Bang Giovani baik, juga ramahh",  
                "pesan":"Semangat terus ya bang, semoga lancar terus urusannya", # 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kak Rahma Ramah dan baik banget",  
                "pesan":"Semangat terus ya kak kuliahnya", # 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "kak Rahmah bik dan sabar banget, apalagi kalo ngajarin tutor",  
                "pesan":"Semangat terus ya kak kuliahnya, semoga dikelilingi hal hal baik", # 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450102",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans Sakum,Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "Abangnya baik dan ramah bangett",  
                "pesan":"Sukses terus ya bang, semoga lancar urusannya", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13OsF7JM6lE-H4eWeIuQT5G5qjU_HUWK5", # Bang Arafi
            "https://drive.google.com/uc?export=view&id=1TQTIeoNWgcK2t64c5c_gGfI6WDW1oOCP", # kak yohana
            "https://drive.google.com/uc?export=view&id=1Yqb2yO-Ew6GCEj4oXfTzbodX7puY-vQP", # kak Ratu
            "https://drive.google.com/uc?export=view&id=1f1-dKLSOls4laekRpHxPfv2PeWbbYLx9", # kak Arini
            "https://drive.google.com/uc?export=view&id=1RQB7Wk5d0xnQiBArlbc3pYeKNQlSdP13", # Bang Arya 
            "https://drive.google.com/uc?export=view&id=1tx0VeC5y6hx7HFi8M_OhOwsRM8sAge9z", #Kak Khoirul
            "https://drive.google.com/uc?export=view&id=1tlupeVvaNgWWF9NZzsLqJxqskaYrxDBc", # Kak Lutfia
            "https://drive.google.com/uc?export=view&id=1yCP_K0jRXozIB-7sJTthAwmljyS86BkJ", # Kak Nabyla
            "https://drive.google.com/uc?export=view&id=1i1FmPc90a5BaVLGJnVxAByUOjhg4fpho", # Bang Syahrialdi
            "https://drive.google.com/uc?export=view&id=1YpCSpX3kJ1cCQTnl-856j5BC3hDGNmg5", # Kak Dea M
            "https://drive.google.com/uc?export=view&id=14KieA_F0lIvP9Ggm48t4dv7JAccOH9Dj", # Kak Cindy
            "https://drive.google.com/uc?export=view&id=1UJdGyWy66TQmW3YXmiZyoXE3GSvVcFAa", # Kak Dea A
            "https://drive.google.com/uc?export=view&id=1AcBZH_q80apERIZUx5vdDUXROsQv7_zw", # Bang Desman
            "https://drive.google.com/uc?export=view&id=1fequD65JMcikikOXPe7NPCH3lHJS4_-e", # Kak Sonya
            "https://drive.google.com/uc?export=view&id=1mYA1M4R4X2NS4rBNxCuOD7c-GJtgXR0m", # Kak Lutfi
            "https://drive.google.com/uc?export=view&id=1vCMUQZ5EU_0h-NIlCcyboqw0gSriXvYJ", # Kak Irvan
            "https://drive.google.com/uc?export=view&id=1S0OMsP-zYAhQMGpSTbunt-0k2mHRha-8", # Bang Adit
            "https://drive.google.com/uc?export=view&id=17mQ9lWajmwo_qr76aAYf3pWsT3VVws3E", # Kak Fathya
            "https://drive.google.com/uc?export=view&id=1ryECN8QbEXLBFEm4IOT18HCHMd3ewM3N", # Kak Khazanatil
            "https://drive.google.com/uc?export=view&id=1curJ_OftvlaxHC8t3HnzCC7qBOiyyyaq", # Kak Melinza
            "https://drive.google.com/uc?export=view&id=1IF1D3quNxJay32hGC23e20HyDIZS3OBq", # Kak Nayla
            "https://drive.google.com/uc?export=view&id=1K15gZRGJJ3Lw_YmGIKpdzCk4RCB_uYYF", # Kak Nurul
            "https://drive.google.com/uc?export=view&id=1U_Fi23EJC67SAYmy56p1Y8WRH_iZh2JZ", # Bang Qois
            "https://drive.google.com/uc?export=view&id=1GAALmLR3Y5b4cXr5fV4dm795kRW2k6QU", # Kak tarisya
        
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Warjo",
                "hobbi": "Makan Warjo",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Bang Arafi cool gitu, tapi tetep ramah bangett",  
                "pesan":"Semangat ya bang kuliahnyaa"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana ramah dan humbel bangett",  
                "pesan":"Semangat terus ya kak kuliahnya, semoga semester ini ipknya memuaskan"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "Kak Ratu humbel, dan enak kalo ngobrol",  
                "pesan":"semoga mudah semua urusannya ya kak dan selalu dikelilingi orang orang baik"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "Kak arini catik, baik dan ramah bangettt",  
                "pesan":"Semangat selalu yaa kak jadi orang yang ceria"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya Humbel dan ramah banget",  
                "pesan":"Semangat ya bang kuliahnyaaa"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Khoirul baik dan ramah banget banget banget",  
                "pesan":" Semoga tercapai semua ya kak wish list nya"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Luthfi Manis banget kalo senyum, udah gggitu ramah lagi",  
                "pesan":"Terus baik dan ramah ke orang orang ya kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla manis banget, kalo njelasin pas tutor sabar banget",  
                "pesan":"Semangat terus ya kak kuliahnya, semoga semester ini ipk nya memuaskan"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@",
                "kesan": "Bang Syahrialdi humbel dan ramah banget",  
                "pesan":"Sukses terus ya bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea ramah dan humbel banget",  
                "pesan":"Semangat ya kak kuliahnya"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak Cindy humbel banget trus ramah lagi",  
                "pesan":" Sukses terus buat kak cindy, lancar kuliahnya"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak dea super ceriaa, baik ramahh banget pokoknya mah",  
                "pesan":"Semangat terus ya kak kuliahnya semoha hari hari selalu berpihak ke kakak"# 1
            },
            {
                "nama": "Desman Velius Halaws",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman walaupun keliatannya galak, tapi peduli dan baik banget aslinya",  
                "pesan":"Semangat dan sukses terus ya bang kuliahnya"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya Ramah banget, enak juga kalo ngobrol",  
                "pesan":"jangan bosen jadi orang keren ya kak"# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak lutfi best banget pokoknya mah, baik,cantik, care, asikk juga kalo ngobrol ga canggung",  
                "pesan":"Semangat semangat kak lulu menjalani huru hara semester 5 ini, Semoga semester ini ipk nya 4!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kak Irvan ramah dan humbel banget, jadi ga canggung",  
                "pesan":"Semoga semester ini memuaskan ya bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "Bang Adit orangnya humoris banget",  
                "pesan":"Semangat terus ya bang kuliahnya, semoga semester ini ipk nya 4"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya baik dan ramah banget",  
                "pesan":"Semoga hari harinya menyenangkan ya"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Khanza baik banget dan ramah jadi ga canggung",  
                "pesan":"Semoga semester ini ga mengecewakan ya kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melinza ceria banget pembawaannya",  
                "pesan":"Semanat terus jalani hari harinya ya kak"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "kak Nayla Seru banget kalo diajak ngobrol",  
                "pesan":"Semoga semester ini ga mnegecewakan ya kak"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak izzah baik banget, ramah lagi",  
                "pesan":"Semoga wish list nya terkabul semua ya kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang qois humbel banget",  
                "pesan":"semangat ya bang kuliahnya"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kak Tarisya Ramah banget, baik, sabar apalagi pas ngasprakk",  
                "pesan":"Sukses terus ya kak, semoga selalu dikelilingi orang orang baik"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen Internal":
    def DepartemenInternal():
         gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HSTFBOQr7EQyVjwHfWeVoXIbK53zoL34",
            "https://drive.google.com/uc?export=view&id=1xeyJtUYLprvxuy3gtgUzuiguFaGwj-4o",
            "https://drive.google.com/uc?export=view&id=1R9FmlCqcBZ8RTKYozyYV5yTx6fsrSJa8",
            "https://drive.google.com/uc?export=view&id=1Wl6DBWbFX95HYQNSHQIU3karW1qDILBc",
            "https://drive.google.com/uc?export=view&id=1hI7SGO0iAdtORVb1CqGgZ63mdEoLLBUM",
            "https://drive.google.com/uc?export=view&id=1OyCM7DAHbNaJgNWvqxmqd9Xw13XeUJ2L",
            "https://drive.google.com/uc?export=view&id=18Gvku-gNIugSi4Wu4kBRAezg2q7F54Ob",
            "https://drive.google.com/uc?export=view&id=1MeH3aP1Gg0XvWQT6PC5_2WyNeEQmoKKB",
            "https://drive.google.com/uc?export=view&id=1Oe1gHBwJABYl8aLguSQ2jGhCnP2JV3I2",
            "https://drive.google.com/uc?export=view&id=1Em2n9Xyocln5qMXGX2YQ2iAF3nVSWVeC",
            "https://drive.google.com/uc?export=view&id=1tjat8XzdRb-Y-h2RAjxbRSt4ROpC6jPm",
            "https://drive.google.com/uc?export=view&id=1VrlEsFQK_EdjLMmkseMf9LiwXF-XsaFi",
            "https://drive.google.com/uc?export=view&id=1PPpYE3DN72SrzGfV-RBC4_buXgT3rN_0",
            "https://drive.google.com/uc?export=view&id=1ht2jVCeTDZUa3hTlT85fQI5HyIN77sqV",
            "https://drive.google.com/uc?export=view&id=1gg3KOXW9xT-STspq8GBIPut9MfAtzIEU",
         ]
         data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "12245030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kak Rani keren banget gaya berpenampilannya",  
                "pesan":"Semoga kak Rani selalu bahagia dan sukses di masa depan" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "kelihatannya tomboy, ternyata kalem cewe banget",  
                "pesan":"semangat terus kak renta kuliahnya!"# 1
            },
            {
                "nama": "Salwa Farhanatusaiidah",
                "nim": "12245055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa lembut banget orangnya, enak banget diajak cerita",  
                "pesan":"sukses terus kak salwa, mudah diperlancar kuliahnya!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azza.raaa_",
                "kesan": "baik banget, ramah lagi ",  
                "pesan":"Tetap semangat menjalani hari harinya kak!"# 1
            },
            {
                "nama": "Haikal fransisko Simbolon",
                "nim": "122450106",
                "umur": "18",
                "asal":"Tulang Bawang",
                "alamat": "Sukabumi",
                "hobbi": "Membersihkan rumah",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang Haikal ternyata asik, awalnya keliatan serius gitu",  
                "pesan":"sukses terus dan bahagia bang haikal!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450076",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak Iqfina cantik dan punya vibe yang lembut banget",  
                "pesan":"Semoga Kak Iqfina selalu lancar urusannya"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450009",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak May tipe tipe positive vibes banget",  
                "pesan":"sehat terus dan makin sukses ya kak"# 1
            },
            {
                "nama": "Muhammad Naufal Afghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@Muhammadnaufalafghani73",
                "kesan": "Abangnya kalem banget, tapi seru kalo udah ngobrol",  
                "pesan":"Semangat terus kuliahnya Bang Naufal!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya asik dan ramah banget",  
                "pesan":"sukses terus buat bang zailani!"# 1
            },
            {
                "nama": "Rendi Alezander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@lexanderr",
                "kesan": "Abang Rendi kalem dan ramah bangett",  
                "pesan":"semangat terus ya bang rendi kuliahnya!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna ceria banget suasana langsung cair kalo ada kak Hana",  
                "pesan":"Jadi orang yang selalu ceria terus ya kak Hana!"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak Keren beneran keren, gayanya simple tapi manis",  
                "pesan":"Lancar terus dan dipermudah urusan kuliahnya ya kak!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hifzky",
                "kesan": "Abang Hanif santai banget orangnya, gampang diajak ngobrol",  
                "pesan":"pokoknya semoga lancar terus ya bang segala urusannya!"# 1
            },
            {
                "nama": "Sarah wasti",
                "nim": "122450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah humbel banget asik",  
                "pesan":"Semoga Kak Sarah selalu sehat dan baik baik saja"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "Main Rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kak Zahra manis banget, baik lagi",  
                "pesan":"Sukses terus ya Kak Zahra!"# 1
            },
        ]
         display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
    
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17wcXgbNHdXuW9SP4iH7OSSm1dJNS7L1k", 
            "https://drive.google.com/uc?export=view&id=1LDfDHzw62EioXjKtH0k3_fKmwroTa1Xi", 
            "https://drive.google.com/uc?export=view&id=1QCBmro_I_hGfB3_E8VjW17Wsssrkwwr8",  
            "https://drive.google.com/uc?export=view&id=1ytTWe2Y5HzrTJ6Dviq7mftCyRyvqbXve", 
            "https://drive.google.com/uc?export=view&id=1L-sXR3zf_vZBlu0MSCHrc4x5Nm4YIVFd",  
            "https://drive.google.com/uc?export=view&id=1z2MMrFnRuOVqiq5bTv8xz7fGDwccnKqN",  
            "https://drive.google.com/uc?export=view&id=1PeFDaXtF5T8r_2K9sRPIr5yOhEQgiYIG",  
            "https://drive.google.com/uc?export=view&id=1_7YntLwi392FRPMqSFs9g58cq7Y-qGUp",  
            "https://drive.google.com/uc?export=view&id=1VfgJxxUYBuxxB-Qry9krffYz0o76Gsbd",  
            "https://drive.google.com/uc?export=view&id=1cc1-2KZWKEoLez0MQrhU_Ebv0e_G1vcd", 
            "https://drive.google.com/uc?export=view&id=1pphhQjQkHmjndxqyeU8NMb9fRYpXFz0D",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Balam",
                "alamat": "Belakang PB",
                "hobbi": "Joging",
                "sosmed": "@dananghk_",
                "kesan": "Abang ini asik banget kalo ngobrol, topiknya ga habis habis",  
                "pesan":"Teruslah berkarya dan semangat menciptakan hal-hal luar biasa! !!!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450012",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "kakaknya kalem banget",  
                "pesan":"semangat terus kakkk !!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki_",
                "kesan": "Abangnya asiq",  
                "pesan":"Sukses terus kakk!"#,
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Joging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakak vibe positif banget",  
                "pesan":"keep slay with you positive energy!!!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton dramashort di fb",
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
                "sosmed": "@nabila_azazahra",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
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
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gang perwira 2",
                "hobbi": "Nontol alur cerita film",
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
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()
elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jSq-blwFU5hSnlCkU7FuZ2eMg2ds8F3k",
            "https://drive.google.com/uc?export=view&id=1GtzQdBDZPpi8RyOYuQ6clqv2FE0zebSA",
            "https://drive.google.com/uc?export=view&id=1DVywv7q03PDhBBhQjouplJmWfC5LX5KM",
            "https://drive.google.com/uc?export=view&id=1SsrzOVXZgcsxdvAg94kRuL0P3WbS0mF9",
            "https://drive.google.com/uc?export=view&id=1XdtsmjH_I2jDwcp0j-VC9IB4xkFBJJkY",
            "https://drive.google.com/uc?export=view&id=1T7tcSk-ZRHOczNmep3oEoBaMcyPBRdLy",
            "https://drive.google.com/uc?export=view&id=1u0fmG3-sHyDxVCLF--y7w88FGxdU6lFN",
            "https://drive.google.com/uc?export=view&id=1X5xjLSAz-gzd-pk1WxXV0Si4ADy-cow3",
            "https://drive.google.com/uc?export=view&id=1W2JkrwEYqfBWZ9ZFD7BmNcdiAWlo3_W4",
            "https://drive.google.com/uc?export=view&id=1KwisY6kn9jnJVWLcKFKN8HBb-SNr6nFy",
            "https://drive.google.com/uc?export=view&id=1PzyUB6WA7aKATPJ0F90XNXn4jNcD_85M",
            "https://drive.google.com/uc?export=view&id=1wkAT0IMaL6rN1m_imYxCDb6gjLMyNHuC",
            "https://drive.google.com/uc?export=view&id=1C2eFX6SrDu1WWDRgORETgwquBuLm4JSa",
            "https://drive.google.com/uc?export=view&id=1JIV1RS4BioN-Frxm6YcHxAPlGJBFgVRI",
            "https://drive.google.com/uc?export=view&id=1kB7C7GPM2TWMW0iWJ580SxwZfw4ngO_G",
            "https://drive.google.com/uc?export=view&id=15dd60O9obwxhnytgwhu55l7x7PofG-0s",
            "https://drive.google.com/uc?export=view&id=15CVEvicnwk-xKM8v2dsZ_2jqHmxzI7ST",
            "https://drive.google.com/uc?export=view&id=1OgX_qt0dlYu33bfEvHSKZjB2m7SBX2nK",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya cantik, asikk seruu, dan vibe nya ceria terus",  
                "pesan":"Semangat terus ya kak patricia jadi pribadi yang ceria terus"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Rahma orangnya baik banget dan sangan on point outfitnya",  
                "pesan":"Semoga selalu dipermudah semua urusannya!"# 1
            },
            {
                "nama": "Khoriul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam__",
                "kesan": "Abangnya seru, santai kalo ngobrol",  
                "pesan":"Semangat terus ya banggg!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Hui",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Bang labo bener bener tak terpisahkan dari kamera",  
                "pesan":"semangat terus ya bang jadi PDD nya, hasil fotonya bang labo bagus baguss!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan":" abangnya asik bangett",  
                "pesan":"Semangat terus ya bang!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa asik banget",  
                "pesan":"Semangat terus ya kak, semoga hal hal baik selalu mengelilingi kakak!"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122350020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaa",
                "kesan": "Kakaknya pintar banget dan keliatan rajin!",  
                "pesan":"Semoga terus jadi sosok yang semangat dan rendah hati ya kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kak Aliya ramah banget dan humbel banget",  
                "pesan":"Sukses terus ya kak buat kedepannya!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna kalem dan sopan, kalo njelasin tutor mudah dimengerti",  
                "pesan":"Semoga hal hal baik selalu mengelilingi kakak!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kak Feby manis banget, pembawaannya ceria dan positif",  
                "pesan":"Semoga terus ya kak kuliah serta menjalani hari harinya!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kak Hafsa keliatan sabar banget dan punya aura tenang",  
                "pesan":"Tetap semangat ya kak! Semoga semua impiannya tercapai"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas, Jati Agung",
                "hobbi": "Dengar musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla lembut dan ramah banget, enak diajak ngobrol santai",  
                "pesan":"Semoga kuliahnya lancar dan makin berprestasi ya kak!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania seru banget, pembawaannya asik",  
                "pesan":"Tetap semangat jalani hari harinya ya kak"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangnya kalem tapi lucu, asik banget pas diajak ngobrol",  
                "pesan":"Sukses terus ya bang, dan selalu disertai kebahagiaan!", # 1
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana kelihana baikk banget",  
                "pesan":"Semangat terus ya kak, semoga selalu dikelilingi hal hal baik!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra kreatif banget, dan selalu punya ide ide menarik",  
                "pesan":"Terus berkarya ya kak! Dunia butuh banyak orang kreatif kayak kakak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah balau residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak Eigi punya vibe kalem dan manis banget",  
                "pesan":"Semoga terus bahagia dan selalu dikelilingi orang orang baik!"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Romauli ceria banget, bikin suasana cair",  
                "pesan":"Terus semangat ya dan pantang menyerah ya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan







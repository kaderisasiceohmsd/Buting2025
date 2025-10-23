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
                "kesan": "Abang ini humbel banget",
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
            "https://drive.google.com/uc?export=view&id=1nTJnmXPVwH-0i0XY1Z37hoRvob_S4uuu", #Bang Mirzan
            "https://drive.google.com/uc?export=view&id=1dj5J3AVOCpP8BSZ9CmmQ5ARm1V975ZBY", #Kak Berliana
            "https://drive.google.com/uc?export=view&id=1wqepwu2JF4CleV7fyJlysI95VpAUjsF5", #Kak Juesi
            "https://drive.google.com/uc?export=view&id=1wqepwu2JF4CleV7fyJlysI95VpAUjsF5", #Bang Ridho
            "https://drive.google.com/uc?export=view&id=1scRcrWpX7cLVkAjELGTJPIwPr217NcQc", #Bang Feryadi
            "https://drive.google.com/uc?export=view&id=1UCMWirIFSETLCxyffDHg_2ehFOI4q4z6", #Kak Monica
            "https://drive.google.com/uc?export=view&id=17j7RLivu-ZFLd3FRUDOirNg-f79OeLR2", #Kak Nashwa
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "Nonton orang kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini sumpah asik banget dan sangat friendly",  
                "pesan":"Terus jadi sumber semangat untuk sekelilingmu bang !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "Lomba ga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya humbel banget",  
                "pesan":" Teruslah menjadi pilar yang kuat ya kak!!!"# 1
            },
            {
                "nama": "Kakak CCc",
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
                "nama": "Kakak CCc",
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
                "nama": "Kakak CCc",
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
                "nama": "Kakak CCc",
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
    baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aY4rkqcTQUKHC5yh0pQLVc1f244uVLHE", #Bang Bintang
            "https://drive.google.com/uc?export=view&id=1wA13TEORYp690XiiIE22ZJE2jJRViA6B", #Kak Nadya
            "https://drive.google.com/uc?export=view&id=1VRkEBpNciL131w_C_XrFEwnIpmBUKing", #Kak Fatin
            "https://drive.google.com/uc?export=view&id=1PdLc2oAVZQDiyOU_LkIbkGaT1XoVgGif", #Kak Lia hana
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Lagu, Nyari, Baca, Game, Rapat",
                "sosmed": "@bintangtwingkel",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Sukarame",
                "hobbi": "denger lagu",
                "sosmed": "@nadiaanjani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Belakang Indomart belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11FQfgXrPeYHylQXWULa2TSpbDM2QTX-w", # Bang ferdy
            "https://drive.google.com/uc?export=view&id=1hjRL93ym-cpmuoXTq8jbtSoiFDiktdju", # Kak Nisrina
            "https://drive.google.com/uc?export=view&id=18mUYFHCkhIkEB_JZm3kR8xBI3CAXvtuj", # Kak Allya
            "https://drive.google.com/uc?export=view&id=19k8u84AWasQYmtvf95i3_TL1sxO7hlcz", # Bang Ahmad
            "https://drive.google.com/uc?export=view&id=1ijVfPWvXnhVsBEvgulFE49C7yTPPzSso", # Kak Arin
            "https://drive.google.com/uc?export=view&id=1cpjBjHoz5qwEtHC0Sw_ATGutnth49AZQ", # Bang Daffa
            "https://drive.google.com/uc?export=view&id=1rlvpfWQ39rTbgOIShKzwPVMqOY7psVM9", # Bang Ginda...
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
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@afifahhnsrn",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
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
                "sosmed": "@daffahdynn_",
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
                "sosmed": "@ginda_mrp",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kostan putri gerbang barat sebelah sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@nobelnizam",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Fam",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabilaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22__",
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
                "sosmed": "@ali_parisi3",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450079",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jalan Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""# 1
            },
{
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Jl. Korpri Raya",
                "hobbi": "nontonin anak tari latihan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "----",  
                "pesan":"---"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Belwis",
                "hobbi": "Joki Strava",
                "sosmed": "@ihsan.myusus",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Panjang Selatan",
                "hobbi": "Terjun Payung",
                "sosmed": "@kevinaj__",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton Anak Tari Perform",
                "sosmed": "@m.ridwan_22",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngerjain Soal MTK",
                "sosmed": "@liano.wlm",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Ratu, Bandar Lampung",
                "hobbi": "Nonton Anime",
                "sosmed": "@rewinanaa",
                "kesan": "---",  
                "pesan":"---"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LtknA1fvm80lsqwy2KcWpFbryIXHYeJS", # Bang Randa
            "https://drive.google.com/uc?export=view&id=1fDgHxRmDeWx3vG3NxqrU4mC8OnLBBbSU", # kak rut junita
            "https://drive.google.com/uc?export=view&id=13i7hxQX9MQRPUzZ-dhwLXcqMdOxJoYxj", # bang regi...
            "https://drive.google.com/uc?export=view&id=15BqCrk9Vbh_NqocEYiQ7Z9gu0HtDauIX", # kak aisyah
            "https://drive.google.com/uc?export=view&id=1WRKuokfXHY3zkMDVhH3qx95hd1cIb3Gy", # Bang Fadil
            "https://drive.google.com/uc?export=view&id=1-ZTamxEkMYs1xOfX-8VxYDYO_kqkvBU5", # Bang Aqil
            "https://drive.google.com/uc?export=view&id=1byA8WMX4mhymYerjDTqakdObhbts4ixm", # Bang Naufal
            "https://drive.google.com/uc?export=view&id=1S8YCrSMeQepr75NzQLIeW58y5Alqajzg", # Nak Nadia
            "https://drive.google.com/uc?export=view&id=1pYJeYQaAKpRN4SDdNLbFmKF0DnPWQdnw", # kak Marleta
            "https://drive.google.com/uc?export=view&id=1Ssdmz_sMmtxsti5OfJsJU6iByN50gEMO", # Bang Akeyla
            "https://drive.google.com/uc?export=view&id=10mWxrp1P0vgrcNmgzo2N-lJjHIaNT3M7", # Kak Anggi
            "https://drive.google.com/uc?export=view&id=1gUG7zKzBIF3njeiezclLMPY39gO3l9I8", # kak efi...
            "https://drive.google.com/uc?export=view&id=1uTwW_g7tyKV5JdPBA1Cn-e_JBX28vfRm", # kak fabiolla
            "https://drive.google.com/uc?export=view&id=16m6EB7UrkH2IL02PFirZLxpgljpnLCzq", # kak fairuz
            "https://drive.google.com/uc?export=view&id=1ypVhPbd6wPunic17CGmzqUsWAU0MUb8V", # kak tanty
            "https://drive.google.com/uc?export=view&id=132u1iyQDRtqL30KtSSvgYifWZ-YnfUjs", # Bang Eggi
            "https://drive.google.com/uc?export=view&id=1f4lFXVuI011fYMyRf1nMm0RvYyvAAl-r", # Kak Afifah
            "https://drive.google.com/uc?export=view&id=1TSFWj4saF6uiz2WQz3qY7K33B0egXtYf", # Bang Fabio
            "https://drive.google.com/uc?export=view&id=1c9vrZOpFD1GCU1vrR-52ZzpJCbqz7zIT", # Bang Giovani
            "https://drive.google.com/uc?export=view&id=1IQ9KrRwlu5kXaNuTtPfOc-6-41QBWHek", # Kak Rahma...
            "https://drive.google.com/uc?export=view&id=12BJSQjUPezrnzbF0gFWMwluRw5OK1UE4", # Kak Rahmah
            "https://drive.google.com/uc?export=view&id=1Y7eax6u2FMp_KLKZvDj9eAwweurxUTYs", # Bang Razin...
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
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234500119",
                "umur": "20",
                "asal":"Pramuka, Bandar Lampung",
                "alamat": "Perum Bukit Alam Permai 3, Blokk C, No.9",
                "hobbi": "Dengrin musik",
                "sosmed": "@keyashafi_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bummisari Kec.Natar",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Sale, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "-",  
                "pesan":"", # 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":"", # 1
            },
             {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang (main game)",
                "sosmed": "@fifah.zy",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer),tidur,jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@giofaniars_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450102",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans Sakum,Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "",  
                "pesan":"", # 1
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
            "https://drive.google.com/uc?export=view&id=1dvyhEZmAmETF_0dseV_hLliSxDbY_Boy", # Bang Syahrialdi...
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
            "https://drive.google.com/uc?export=view&id=1CX0IzYa8NNIX7ac2vfbxKy9LnycmaDyA", # Kak Melinza
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
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Desman Velius Halaws",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=163LOxuOp1KtaEtMLvF0rOoHv6h9ps9KG", 
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
    
# Tambahkan menu lainnya sesuai kebutuhan


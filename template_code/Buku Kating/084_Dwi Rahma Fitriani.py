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
                "kesan": "Abang ini humbel banget
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
elif menu == "Departemen SSD":
    def Departemen SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aY4rkqcTQUKHC5yh0pQLVc1f244uVLHE", #Bang ...
            "https://drive.google.com/uc?export=view&id=1wA13TEORYp690XiiIE22ZJE2jJRViA6B", #Kak ...
            "https://drive.google.com/uc?export=view&id=1VRkEBpNciL131w_C_XrFEwnIpmBUKing", #Kak ...
            "https://drive.google.com/uc?export=view&id=1PdLc2oAVZQDiyOU_LkIbkGaT1XoVgGif", #Kak ...
            "https://drive.google.com/uc?export=view&id=1aY4rkqcTQUKHC5yh0pQLVc1f244uVLHE", #Bang ...
            "https://drive.google.com/uc?export=view&id=1wA13TEORYp690XiiIE22ZJE2jJRViA6B", #Kak ...
            "https://drive.google.com/uc?export=view&id=1VRkEBpNciL131w_C_XrFEwnIpmBUKing", #Kak ...
            "https://drive.google.com/uc?export=view&id=1PdLc2oAVZQDiyOU_LkIbkGaT1XoVgGif", #Kak ...
            "https://drive.google.com/uc?export=view&id=1aY4rkqcTQUKHC5yh0pQLVc1f244uVLHE", #Bang ...
            "https://drive.google.com/uc?export=view&id=1wA13TEORYp690XiiIE22ZJE2jJRViA6B", #Kak ...
            "https://drive.google.com/uc?export=view&id=1VRkEBpNciL131w_C_XrFEwnIpmBUKing", #Kak ...
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
                "sosmed": "@"nabila_azazahra,
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
                "sosmed": "@"nydiaaptr,
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen SSD()
    
# Tambahkan menu lainnya sesuai kebutuhan



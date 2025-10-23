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
            "https://drive.google.com/file/d/18CoDoIWaZFtKUFpBXyKAzLw5lWV3VdTK",
            "https://drive.google.com/file/d/1uNfDpbSf5kzgmff9LgV_iUhM554EgePb",
            "https://drive.google.com/file/d/1QObl1wKZHPA5SKXzwTCXWO6cTy2tUuPm",
            "https://drive.google.com/file/d/1asdYyYQVLf2mF04l7_hSteVBUONaS9XZ",
            "https://drive.google.com/file/d/1fOoFtYfB6IUgdspQftmKEUedLUPKO_2R",
            "https://drive.google.com/file/d/1HrgGlsWjQ7VLu6aqe77KxhdasC0_ySXK",
        ]
        data_list = [
            {
                "Nama": "Rendra Eka Prayoga",
                "Nim": "122450112",
                "Umur": "21",
                "Asal":"Bekasi",
                "Alamat": "Pulau Damar",
                "Hobbi": "Beli donat kentang",
                "Sosmed": "@erendraa",
                "Kesan": "Abangnya keren dan luwes banget kalau ngejelasin apa pun itu topiknyaa, kerenn ",  
                "Pesan":"Semangat terus kuliahnya bang rendra !!!"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "Nim": "122450043",
                "Umur": "20",
                "Asal":"Tangerang",
                "Alamat": "Jl. Lapas Raya",
                "Hobbi": "Baca buku dasar-dasar",
                "Sosmed": "@johannneskrijnnn",
                "Kesan": "Awalnya aku ngira bang jo tu galak ternyata ngga terlaluu and ",  
                "Pesan": "Semangat terus kuliahnya bang joo !!!"
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "Nim": "122450001",
                "Umur": "19",
                "Asal":"Rote, NTT",
                "Alamat": "Rajabasa",
                "Hobbi": "Baca buku, suka pramuka",
                "Sosmed": "@eksantyfebriana",
                "Kesan": "Kak eksanty lucuu and materi yang dipaparin sama kakaknyaa mudah dimengerti",  
                "Pesan":"Semangat terus kuliahnya kak !!!"
            },
            {
                "Nama": "Farhanum Afifah Ardiansyah",
                "Nim": "122450056",
                "Umur": "21",
                "Asal":"Padang, Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobbi": "Tidur",
                "Sosmed": "@farahanumafifah",
                "Kesan": "Kakaknya asik and cantik banget",  
                "Pesan":"Semangat terus kuliahnya kakak !!!"
            },
            {
               "Nama": "Elisabeth Claudia Simanjuntak",
                "Nim": "122450123",
                "Umur": "19",
                "Asal":"Tangerang",
                "Alamat": "Airest Kost",
                "Hobbi": "Siram shopee",
                "Sosmed": "@celisabeth_",
                "Kesan": "Kakaknya lucu and cantik banget",  
                "Pesan":"Semangat terus kuliahnya kakak !!!"
            },
            {
               "Nama": "Syadza Puspadari Azhar",
                "Nim": "122450072",
                "Umur": "18",
                "Asal":"Palembang",
                "Alamat": "Belwis",
                "Hobbi": "Membaca",
                "Sosmed": "@puspadrr",
                "Kesan": "Kakaknya lucu, seru, terus humble banget",  
                "Pesan":"Semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/file/d/1orU1NkojPe5QryKER6g6A2QWs-JjzMZg/view?usp=drive_link",
            "https://drive.google.com/file/d/1U0AmH4wtaygu3J_wj5R19RuP5jotM09B/view?usp=drive_link",
            "https://drive.google.com/file/d/1uFvPz81jGe8Z3dpoe2ClUR4LVxarhQNc/view?usp=drive_link",
            "https://drive.google.com/file/d/1RsFFiZ7jp2hzSwmHYps3glsHZa7-d45q/view?usp=drive_link",
            "https://drive.google.com/file/d/1GueNEwzEjswnl-Ekc-bCjBkJbRusjMDP/view?usp=drive_link",
            "https://drive.google.com/file/d/1bLdPHKLtM5siey0nJiMkArjKdk2AG0DI/view?usp=drive_link",
            "https://drive.google.com/file/d/1YOgr4bGAvGr9e__yP3YLcW01IZWLQR9g/view?usp=drive_link",
            "https://drive.google.com/file/d/1w2jxC4zZGXgMum_CwnnN9yh360U43J-U/view?usp=drive_link",
            "https://drive.google.com/file/d/18M4AzZEMEOgHMgwS2H-qIGz6ekISm-Xo/view?usp=drive_link",
            "hhttps://drive.google.com/file/d/1vEpi_SEuSY73VWITgTIbwod-ThwaQh_6/view?usp=drive_link",
            "https://drive.google.com/file/d/1V7wexXMcv70psGDSH7WZyH6_ff6i9jV2/view?usp=drive_link",
            "https://drive.google.com/file/d/1eQYoBIDHlV-ZL0fXOHcpclK1VCWg_OA_/view?usp=drive_link",
            "https://drive.google.com/file/d/1aBf9VsuxRDVAp9wcFEMOI00rPZyU0UEU/view?usp=drive_link",
            "https://drive.google.com/file/d/1logMMosiGdM1rA5yhQ6PCMEqw-nx94_D/view?usp=drive_link",
        ]
        data_list = [
            {
                "Nama": "Jeremia Susanto",
                "Nim": "122450022",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Yapping",
                "Sosmed": "@Jeremia_s_",
                "Kesan": "Kakaknya bener-bener mengayomi dan jawaban yang dikasih juga mudah dimengerti.",
                "Pesan":"Bismillah sempro ya bangg!"
            },
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "Nim": "123450060",
                "Umur": "19",
                "Asal":"Medan",
                "Alamat": "gang sekuntum",
                "Hobbi": "Main pedal",
                "Sosmed": "@iamridhomanik",
                "Kesan": "Abangnya asik dan lucuu.",
                "Pesan":"Semangat kuliahnya bang."
            },
            {
                "Nama": "Feby Wulandari",
                "Nim": "123450042",
                "Umur": "17",
                "Asal":"Bekasi",
                "Alamat": "Way huwi, Bandar Lampung",
                "Hobbi": "Main karambol",
                "Sosmed": "@fby.wlndr",
                "Kesan": "Kakaknya humble, seru dan baik banget.",
                "Pesan":"Semangat terus kuliahnyaa kakk!"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "Nim": "122450118",
                "Umur": "21",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobbi": "Tidur",
                "Sosmed": "@myrrinn",
                "Kesan": "Pembawaannya abangnya positif vibe.",
                "Pesan":"Semangat kuliahnya bangg."
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "Nim": "123450077",
                "Umur": "17",
                "Asal":"Aceh",
                "Alamat": "Belwis",
                "Hobbi": "Tiktokan bareng sahroni",
                "Sosmed": "@nshaysk",
                "Kesan": "Kakaknya alwayss senyum.",
                "Pesan":"Keep smilingg kakk."
            },
            {
                "Nama": "Feryadi Yulius",
                "Nim": "122450087",
                "Umur": "21",
                "Asal":"Bandung",
                "Alamat": "Way kandis",
                "Hobbi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "Sangat berkesan, orangnya humble.",
                "Pesan":"Tetap jadi pribadi yang menginspirasi!"
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "Nim": "123450073",
                "Umur": "19",
                "Asal":"Sibolga",
                "Alamat": "Belwis",
                "Hobbi": "Nonton",
                "Sosmed": "@monica_tjg",
                "Kesan": "Orangnya humble, seru dan baik banget.",
                "Pesan":"Semangat terus dan jangan mudah menyerah!"
            },
            {
                "Nama": "Renisha Putri Giani",
                "Nim": "122450079",
                "Umur": "22",
                "Asal":"Teluk, Bandar Lampung",
                "Alamat": "Teluk, Bandar Lampung",
                "Hobbi": "Tidur",
                "Sosmed": "@Renishapg",
                "Kesan": "Kakaknya cantik, asik dan ramah.",
                "Pesan":"Semangat untuk kuliahnya ya!"
            },
            {
                "Nama": "Anisa Fitriyani",
                "Nim": "122450019",
                "Umur": "19",
                "Asal":"Lubuk Linggau",
                "Alamat": "Pringsewu",
                "Hobbi": "Hafalin sandi Morse",
                "Sosmed": "@ansftynn_",
                "Kesan": "Orangnya seru dan baik banget.",
                "Pesan":"Semangat terus dan jangan mudah menyerah!"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "Nim": "",
                "Umur": "20",
                "Asal":"Chiwidew, Jawa Barat",
                "Alamat": "Pesawaran",
                "Hobbi": "Pawat Piwit",
                "Sosmed": "@_.dheamelia",
                "Kesan": "Senang bisa kenal dengan kakak.",
                "Pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "Nama": "Berliana Enda Putri",
                "Nim": "124450065",
                "Umur": "21",
                "Asal":"Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Nyanyi",
                "Sosmed": "@berlyyanda",
                "Kesan": "Sangat berkesan, orangnya humble.",
                "Pesan":"Tetap jadi pribadi yang menginspirasi!"
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "Nim": "123450085",
                "Umur": "19",
                "Asal":"Sumatera Utara",
                "Alamat": "Way huwi",
                "Hobbi": "Dengerin Lany",
                "Sosmed": "@j_eesie",
                "Kesan": "Kakaknya humble, asik dan ramah.",
                "Pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "Nim": "123450023",
                "Umur": "18",
                "Asal":"Way halim, Bandar Lampung",
                "Alamat": "Way halim, Bandar Lampung",
                "Hobbi": "Nyuci baju",
                "Sosmed": "@dhruchyo",
                "Kesan": "Abangnya pinter banget.",
                "Pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "Nama": "Givaro Ananta",
                "Nim": "123450078",
                "Umur": "20",
                "Asal":"Teluk Betung",
                "Alamat": "Teluk Betung",
                "Hobbi": "Dengerin Spotify",
                "Sosmed": "@givarooo",
                "Kesan": "Pembawaannya positif dan menyenangkan.",
                "Pesan":"Semoga kita bisa bertemu lagi."
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/file/d/15WZU6uG8OmqmpkbShcZ95petjREXa0yi/view?usp=drive_link",
            "https://drive.google.com/file/d/1FfKJZVEmcceQk4FeXHcZIWVjWMd-jnF9/view?usp=drive_link",
            "https://drive.google.com/file/d/1UL-UBp_og4uzCnmdhTQ-IYC3FiYwi7Y7/view?usp=drive_link",
            "https://drive.google.com/file/d/1UcKIETL4mqUOWZXeMQD90M_sY8QvMRgf/view?usp=drive_link",
        ]
        data_list = [
            {
                "Nama": "Rian Bintang Wijaya",
                "Nim": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "-",
                "Hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "abangnya asik, humble, suka perunggu juga yoai",  
                "pesan":"tetep humble bang!"
            },
            {
              "nama": "Lia Hana Ichisassmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kaknya inspiratif banget, bikin pengen berkembang terus!",  
                "pesan":"Terima kasih udah jadi role model yang luar biasa kak"  
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakaknya asik seru",  
                "pesan":"Semoga selalu tenang dan sabar hadapi dunia perkuliahan"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "kakaknya baik, lucu, imup",  
                "pesan":"tetep humble kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/file/d/1LzRGbQPcMtpeniqjFXmL2GbA03U29AlJ/view?usp=drive_link",
            "https://drive.google.com/file/d/1z_GqvkHBRAJFF3uy8lj8E1YCy0a2aarP/view?usp=drive_link",
            "https://drive.google.com/file/d/1io6ZiKUfqpzKrSP9zeMLY4OwndWEK_rG/view?usp=drive_link",
            "https://drive.google.com/file/d/1J9PrPyA4kQj42-L0xkA1sNtID45gc5rR/view?usp=drive_link",
            "https://drive.google.com/file/d/1-2dBE-cq8pUfi0ew-CzIb4CAJ8H6wwoA/view?usp=drive_link",
            "https://drive.google.com/file/d/1gSRrIjMgqP1eoLVPd30zHfHzmOLUWdsv/view?usp=drive_link",
            "https://drive.google.com/file/d/1J8U3DQ84hc_rM424maqp4NGXM-ka3r84/view?usp=drive_link",
            "https://drive.google.com/file/d/1KdmyEz511GLQ115Ix-ogO8TMUyuWh81E/view?usp=drive_link",
            "https://drive.google.com/file/d/1gwbvm5S6BpQuWGw5nOY8KJojQo48jasd/view?usp=drive_link",
            "https://drive.google.com/file/d/1KOKcgD1JMB3TLwoeEQtfHQOv_SbEfl9f/view?usp=drive_linkX",
            "https://drive.google.com/file/d/15lIWo5iYSDEUdK3EGeg-uw_XkaSZVU3k/view?usp=drive_link",
            "https://drive.google.com/file/d/1tElvCW4GaYsXS-eEw59qY1J4Q9Qy9-Pf/view?usp=drive_link",
            "https://drive.google.com/file/d/1ygSxQE3YqaUOg7JbnL6cQHCuh6iDPYSU/view?usp=drive_link",
            "https://drive.google.com/file/d/1ra90NS3d0W5-ppW2KEdPuyiB9-gmBCFw/view?usp=drive_link",
            "https://drive.google.com/file/d/1M-MBIPIlPxLyaGK9uaYm41oUigb7Q4oF/view?usp=drive_link",
            "https://drive.google.com/file/d/1kuq4qHg-ejNd1tqDV1trahkQ310S9OSA/view?usp=drive_link",
            "https://drive.google.com/file/d/1BXmcVoALNOIKRaUuVSR57he7FkGviXep/view?usp=drive_link",
            "https://drive.google.com/file/d/1CTPGMhzjuMMJ9Fz3SyRtrYR3s2oI0C-y/view?usp=drive_link",
            "https://drive.google.com/file/d/1HgArG36CXE6veeT3jluYN2j-dbjyuUDj/view?usp=drive_link",
            "https://drive.google.com/file/d/146bZ7PIj60Wv_j8IWufSY2e_MsnK0S6A/view?usp=drive_link",
            "https://drive.google.com/file/d/1uWfm_ieS5fFcNwinO7eBOcTz5PgQ82_Y/view?usp=drive_link",
            "https://drive.google.com/file/d/1LimBVEBTZNV3Oe4HC2w3dwtX02CYEfmG/view?usp=drive_link",
            "https://drive.google.com/file/d/1rOxskZBzL1jH1_93vQWnYjO4jkPxdIIH/view?usp=drive_link",
            "https://drive.google.com/file/d/1l9ljGout9jbrh1xJJ5kV1g5XccE3RiCv/view?usp=drive_link",
            "https://drive.google.com/file/d/1l9ljGout9jbrh1xJJ5kV1g5XccE3RiCv/view?usp=drive_link",
            "https://drive.google.com/file/d/1zTcd6CsB35mD8LqeOf3zZxkni_TsOs7i/view?usp=drive_link",
        ]
        data_list = [
            {
                "Nama": "Ferdy Kevin Naibaho",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "",
                "Kesan": "Abangnya lucu pas di fg.",
                "Pesan": "Sukses selalu ya, Bang!"
            },
            {
                "Nama": "Daffa Ahmad Noval",
                "Nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
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
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
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
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak!"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
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
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Nobel Nizam Fathirizki",
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
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/file/d/1ZNI54EABQuN4hlnX8jPwBZYeGYe-eSdz/view?usp=drive_link",
            "https://drive.google.com/file/d/1wx6DNOP8SlWSxChhJEB_4ND7RFUXSk_s/view?usp=drive_link",
            "https://drive.google.com/file/d/17kBJFaY0PLsGOOmSl41X12gRHuMkcPoi/view?usp=drive_link",
            "https://drive.google.com/file/d/17kBJFaY0PLsGOOmSl41X12gRHuMkcPoi/view?usp=drive_link",
            "https://drive.google.com/file/d/1HcpXGyzv2eBeFEBvrxKc0VaGrPV3dO7r/view?usp=drive_link",
            "https://drive.google.com/file/d/1cJg6ZlXPZztmUmS3qHq_c_iEXCIJ8ms5/view?usp=drive_link",
            "https://drive.google.com/file/d/1BfB80QhkIcjgZTilutxQ7gp6gLFDfr2C/view?usp=drive_link",
            "https://drive.google.com/file/d/1iB05mCp1GlOcDxx60L6KOzczZ63YZ9aM/view?usp=drive_link",
            "https://drive.google.com/file/d/1K_CLh9rD3C2iNYNR-2vKTPtDFvY6_D2s/view?usp=drive_link",
            "https://drive.google.com/file/d/1txDW9_Av70lDetUPF1mqqqtHOlSnhPKj/view?usp=drive_link",
            "https://drive.google.com/file/d/1fQMMiCAX8sNAmR3f5uf4vCb_ugOCGT2E/view?usp=drive_link",
            "https://drive.google.com/file/d/1KfEFN45bvETHlrg1a4D1cLOONgGQRWPp/view?usp=drive_link",
            "https://drive.google.com/file/d/11ZguLm7C3jSu1r1N_57iW_q27sTXUx2b/view?usp=drive_linku",
            "https://drive.google.com/file/d/1NA_oTHs7MFsqj8hIz8gofZLs0Z1jGygl/view?usp=drive_link",
            "https://drive.google.com/file/d/1cFRFQElbbiCIr_qNp5S7jZLp7Q-Lt6LS/view?usp=drive_link",
            "https://drive.google.com/uc?export=view&id=1Ky50zlRJ85v3ydpmu5Eq7P6IsRO6qRlp",
            "https://drive.google.com/file/d/1549xfhJxfZoCxGZG-9x4zL-RpTyObxZy/view?usp=drive_link",
            "https://drive.google.com/file/d/1FUVWP-tUSIvHAVtQYG-C2cuQUb1bKL73/view?usp=drive_link",
            "https://drive.google.com/file/d/11hDAeB6vmRdbcH6JeF1rYfu-_aMDBa2o/view?usp=drive_link",
            "https://drive.google.com/uc?export=view&id=17AU4aIRMfGAvfc9nEx2W2ieHFy69rVDd",
            "https://drive.google.com/file/d/1WVLk61jO4bPrf7pNXfqSeDncnVeIVw43/view?usp=drive_link",
            "https://drive.google.com/file/d/1cksTQ2tLDjNFvGrykkz05KfjapzHZUcb/view?usp=drive_link",
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
                "nama": "Fabiolla Charissa Putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
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
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
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
                "nama": "Tanty Widiyastuti",
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
                "nama": "Anggi Puspita Ningrum",
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
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/file/d/1IXita2upy6igRGq7kNBv9nXmdpxQuWDe/view?usp=drive_linkq",
            "https://drive.google.com/file/d/1xV9X0htFnwooK_4U5NXPVA1fM0axncOx/view?usp=drive_link",
            "https://drive.google.com/file/d/130v_FlS3kIfcBaL3W0oTK6QEBLaNKgSK/view?usp=drive_link",
            "https://drive.google.com/file/d/1k3EUA8kheaZAVs2gOrU87chCdBPLM3VA/view?usp=drive_link",
            "https://drive.google.com/file/d/15WPPnLij0fMLGOZ2ngqjTMgDgRqokVVQ/view?usp=drive_link",
            "https://drive.google.com/file/d/1KcPWt1aHRXK68zUAgolJ0V6sdMFdGUHy/view?usp=drive_link",
            "https://drive.google.com/file/d/1zxRwpPFCSEaLZTso_VVCU_R-hNp9guXH/view?usp=drive_link",
            "https://drive.google.com/file/d/1oi76zR2OPEFlX4DqypKOFJnGGw1XCES6/view?usp=drive_link",
            "https://drive.google.com/file/d/1k1DdfQmTbWfNE-UElCu5FhB4nwPbk3Ru/view?usp=drive_link",
            "https://drive.google.com/file/d/1d3Tw2dhgTZY6iWClH8MZDmCsdgqgWR9u/view?usp=drive_link",
            "https://drive.google.com/file/d/1-uFAttN9wrMW_dIkXoGhsO8b6GvKejd3/view?usp=drive_link",
            "https://drive.google.com/file/d/1YPAnNXyEnLeytCrk_4wT_C5voLNP_bj6/view?usp=drive_link",
            "https://drive.google.com/file/d/1DKdlVWf_j8DoJQiuaCQp2EqpeE70WORj/view?usp=drive_link",
            "https://drive.google.com/file/d/1Z8UppkQlt2qFS267swRHjbH222UU2N8G/view?usp=drive_link",
            "https://drive.google.com/file/d/10mHiz_gNUyoOYxn0pTidhqpKyy76knb5/view?usp=drive_link",
            "https://drive.google.com/file/d/1ZEl41yOCcfU0DslJwcBaeyNOWl0jkL0A/view?usp=drive_link",
            "https://drive.google.com/file/d/1R7PCTJg1GZmgp8H88UrtQLIS81SSAHem/view?usp=drive_link",
            "https://drive.google.com/file/d/1viHakxRak0ghxjqK5i60P9BdfaYg76W1/view?usp=drive_link",
            "https://drive.google.com/file/d/14wFDy8kAzLpb24AVL92fM68YmgRqOdab/view?usp=drive_link",
            "https://drive.google.com/file/d/1wNchYR58mer8dWr7AyRH2mrfwzJmsHMk/view?usp=drive_link",
            "https://drive.google.com/file/d/17iCKS8OGQzQ08xwD5i2viQ6K1UEMyyp4/view?usp=drive_link",
            "https://drive.google.com/file/d/1oPWpRPKGDXP-MGVxu509GKwEurdF-sRA/view?usp=drive_link",
            "https://drive.google.com/file/d/1oPWpRPKGDXP-MGVxu509GKwEurdF-sRA/view?usp=drive_link",
            "https://drive.google.com/file/d/1oPWpRPKGDXP-MGVxu509GKwEurdF-sRA/view?usp=drive_link",
        ]
        data_list = [
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
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/file/d/10tPPRcWiX23HNaMEnEUdNyiOFLvD1FJw/view?usp=drive_link",
            "https://drive.google.com/file/d/1kw4dYNXlexMo14ILmD398Q4xl37161nf/view?usp=drive_link",
            "https://drive.google.com/file/d/18obacBsaZ_8nU5besp5I-WyqDj_pTeZ2/view?usp=drive_link",
            "https://drive.google.com/file/d/1wM2AQNhTlzxthAUE_CsiiSlyaJqu7GU1/view?usp=drive_link",
            "https://drive.google.com/file/d/1YFJ2EGFo-i-HwttudcDsGPN-Cf69Qx6l/view?usp=drive_link",
            "https://drive.google.com/file/d/1QwQ0ZsEvlA96qR2A77LKK3vYfDp1XYwY/view?usp=drive_link",
            "https://drive.google.com/file/d/1HWBUeGfXC88HsFMO1t8NOabrSAw4mFlz/view?usp=drive_link",
            "https://drive.google.com/file/d/1MLR2c3ytR5QRnJaZVdelQTjAGucdhUXL/view?usp=drive_link",
            "https://drive.google.com/uc?export=view&id=1b5hddOAd1hFhpkggGaK34--v0AU89D3f",
            "https://drive.google.com/uc?export=view&id=1T8HbfLmz7vVDuu7ryDsyLOAWv6kiV-sj",
            "https://drive.google.com/uc?export=view&id=1BnsFmkU4dC0Jd1h_2zA2h_x2_MYlqRCt",
            "https://drive.google.com/uc?export=view&id=1RvBpeOAUhIeq7ytyBh7oWpCSVOH444QT",
            "https://drive.google.com/uc?export=view&id=11GV77ZqIVPjqnoF0DPxNtAxHr8TssmCT",
            "https://drive.google.com/uc?export=view&id=1IAYYeTAdk5dJA5l9363ZPVn9GgVP2AdM",
            "https://drive.google.com/uc?export=view&id=11LOQp43VlkN-ajzEHXVwCMk8JGDcRfw-",
            
        ]
        data_list = [
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kakaknya baik dan supel.",
                "pesan": "Sukses selalu ya, Kak."   
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Senang bisa kenal sama kakak.",
                "pesan": "Sukses terus buat ke depannya ya, Kak!"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakaknya seru dan suka membantu.",
                "pesan": "Semangat terus kuliahnya, Kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Kakaknya humble dan mudah diajak ngobrol.",
                "pesan": "Semangat terus ya, Kak, jangan sungkan sapa kami."
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Senang bisa satu himpunan sama kakak.",
                "pesan": "Semoga urusannya dipermudah selalu, Kak."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya asik dan seru.",
                "pesan": "Semoga urusan kuliahnya lancar selalu, Kak."
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya asik untuk diajak diskusi.",
                "pesan": "Lancar-lancar ya, Kak, kuliahnya."
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik dan friendly.",
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik banget dan ramah.",
                "pesan": "Sehat dan semangat terus ya, Kak!"
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya baik dan seru.",
                "pesan": "Semangat terus, Kak!"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya ramah banget.",
                "pesan": "Sehat dan bahagia selalu, Kak!"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asik banget.",
                "pesan": "Sehat selalu, Kak!"   
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kesan pertamanya positif banget, Kak.",
                "pesan": "Semoga kita bisa makin akrab ya, Kak."
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/file/d/1EruslUjbF53rdQy9WKLPb3G0fBnIA3iE/view?usp=drive_link",
            "https://drive.google.com/file/d/148FOFav0tGCYx_gCaMOc6dAokiinO8-L/view?usp=drive_link",
            "https://drive.google.com/file/d/1dC_asfQfLceJnpm5qPAKU52QIb4gUWXP/view?usp=drive_link",
            "https://drive.google.com/file/d/1f7fU5ar7MRJY5OwFq56qAwHlBF5aCqPM/view?usp=drive_link",
            "https://drive.google.com/file/d/11KWGejO9fW3KTp9zoPVFL5sxb4OLj39H/view?usp=drive_link",
            "https://drive.google.com/file/d/1BXJxn0HnJ-K_mDbR6loOUv98gCRe14eg/view?usp=drive_link",
            "https://drive.google.com/file/d/1482cqHfQjcsNGCeIR7-K1yjU1Vm03JPR/view?usp=drive_link",
            "https://drive.google.com/file/d/1bZ7A6ZB9Unve0j2C1_httYlhOCjoWQmO/view?usp=drive_link",
            "https://drive.google.com/file/d/1NcssizptgD1Kjox8Gqcf2LkwrApvXlyD/view?usp=drive_link",
            "https://drive.google.com/file/d/1l6vIco9t3AZyRQri000IpDusIoOs3SXg/view?usp=drive_link",
            "https://drive.google.com/file/d/1f9YYvtSmIeYspsuKBmtVVU3eUYdzNJb2/view?usp=drive_link",
            
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
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Semangat terus ya, kak!"
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
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "kakanya asik dan seru diajak ngobrol",
                "pesan": "Semoga sukses selalu ya kak!"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gwTymYwQzjgUezyDQ9zO0CECJ8ReNIBz",
            "https://drive.google.com/uc?export=view&id=10A1dsOYuvXFBk7reEtG37bwIH-KRSYxX",
            "https://drive.google.com/uc?export=view&id=1q1HUnkaZ9_e4Hip_36Eo4bnxt6xFOX7N",
            "https://drive.google.com/uc?export=view&id=1qKa576aRVwfw4ud5OEIiNsB-j6n1kQPl",
            "https://drive.google.com/uc?export=view&id=1348u5gBZ41MHLWI435PS9j4pQFMbQKgG",
            "https://drive.google.com/uc?export=view&id=1F5iY7m4gNG-UZTl9MJ1UsfNdv3FnC8Id",
            "https://drive.google.com/uc?export=view&id=10pa2TCMEMWVCrP4sQF3RbccdrR6YH5QQ",
            "https://drive.google.com/uc?export=view&id=1r8004aIocwrpDszsGPW0srmxTpgRw_vB",
            "https://drive.google.com/uc?export=view&id=14_KhYmCKb4lwtf0ukaSQ-7qN1-sAjCoK",
            "https://drive.google.com/uc?export=view&id=1rYWjxvDaTeL2eoLDYl48aaxCP3ply7Yf",
            "https://drive.google.com/uc?export=view&id=1yOTtD1H-EM_C2ACev3uwCNZx2SbBOmbJ",
            "https://drive.google.com/uc?export=view&id=1000E4pEcgRevoSNX2h7VvlHmyoN-WRgM",
            "https://drive.google.com/uc?export=view&id=1FtvpsWVnx_gI3uJqsbre5xrEW5Fh1qcg",
            "https://drive.google.com/uc?export=view&id=1rCV0Ec3U1BZRCf_hpXa1dYGKr7LbNpDU",
            "https://drive.google.com/uc?export=view&id=195ikhN8V8pwVG9ZlvwR79I0uN6-ojqlt",
            "https://drive.google.com/uc?export=view&id=1oL6bdeCmZuVXOGXY_9Vrw-LbPJRk0U0F",
            "https://drive.google.com/uc?export=view&id=1BMfg9j9xXHSMMw3v14TyKiOWQXHVV9_t",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya asik diajak diskusi",
                "pesan": "Lancar terus ya kak kuliahnya!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Terima kasih sudah berbagi ilmu",
                "pesan": "Semoga sukses di masa depan!"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya seru dan pintar",
                "pesan": "Sukses terus untuk karirnya nanti."
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Belajar sama kakaknya jadi menyenangkan",
                "pesan": "Semoga lancar terus kuliahnya!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya sangat membantu dan baik",
                "pesan": "Tetap semangat, kak!"
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Orangnya asik dan mudah bergaul",
                "pesan": "Semangat terus kak kuliahnya!"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Pengalamannya keren dan menginspirasi",
                "pesan": "Teruslah berkarya, kak!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget",
                "pesan": "Sukses untuk ke depannya, kak!"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Sangat berkesan bisa diajar kakak",
                "pesan": "Semoga sehat selalu, kak."
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya keren dan inspiratif",
                "pesan": "Semoga apa yang dicita-citakan tercapai."
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Senang bisa belajar bareng kakak",
                "pesan": "Semoga sukses selalu menyertai."
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Kakaknya friendly dan baik hati",
                "pesan": "Sehat dan sukses selalu, kak!"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Sukses selalu ya, kak!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Seru banget bisa kenal kakak ini",
                "pesan": "Semoga sehat dan sukses selalu"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya ramah dan humble",
                "pesan": "Terima kasih atas bimbingannya, kak."
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Suasananya jadi asik kalau ada kakak ini",
                "pesan": "Jangan lupa jaga kesehatan ya, kak."
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya sangat welcome dan ramah",
                "pesan": "Semangat terus dan semoga sukses!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Penjelasannya mudah dimengerti",
                "pesan": "Semangat terus kak, jangan menyerah!"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
# Tambahkan menu lainnya sesuai kebutuhan

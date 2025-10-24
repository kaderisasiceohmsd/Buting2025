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
            "https://drive.google.com/uc?export=view&id=1cMi8jAXuAmBPWGNBO1JQAHKIhoCv0Xzg",
            "https://drive.google.com/uc?export=view&id=14_QP8CzoW32XMkVWB0LmRhD_IRy6IJGJ",
            "https://drive.google.com/uc?export=view&id=1WMlMQ6JvN2PACplOQ3m88zp2MLZzJAn8",
            "https://drive.google.com/uc?export=view&id=1RWiOzhAjZK3IaPasSAoNvtuQ5e37VNfg",
            "https://drive.google.com/uc?export=view&id=19MDD0kNuhnhsNMHPx-UecxigYjC3hcQ4",
            "https://drive.google.com/uc?export=view&id=1ieMF5Q6siovyHaUJi6dpdRO13SIljVS4",
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
                "kesan": "Suaranya emas, berwibawa, dan keren",  
                "pesan":"Sehat selalu dan jangan pernah menyerah Bang Rendra"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren banget karena selalu terlihat full power dan tidak pernah lelah",  
                "pesan":"Semangat terus Bang Jo, lancar kuliahnya"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Vibesnya menyenangkan, keren banget, dan lucu",  
                "pesan":"Lancar kuliahnya Kak, jaga terus kesehatannya"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Terlihat seperti orang yang serius dan baik",  
                "pesan":"Sehat selalu Kak supaya lancar kuliahnya"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Keren banget Kak, vibesnya seperti girlboss",  
                "pesan":"Semangat terus dan lancar perkuliahannya sampai ke depannya juga"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Seperti tidak bisa ditebak tapi keren banget",  
                "pesan":"Tetap keren Kak, jangan lupa beristirahat dan jaga kesehatan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YGRk9dZRJ701LZb_S6S87hERBbaLqOaT",
            "https://drive.google.com/uc?export=view&id=1yrvtIF8BUmiaWeEnAEMxQC8-foL_2cnD",
            "https://drive.google.com/uc?export=view&id=16tWH0hofQphyEfgTEAVznfvymWWyi2ES",
            "https://drive.google.com/uc?export=view&id=1QQ5lYAKNA3F_tNGYnu2PDRifi-32Cx-o",
            "https://drive.google.com/uc?export=view&id=16w_5OE2qD7fIEEHvFqnyrmFJzjqeW1Xq",
            "https://drive.google.com/uc?export=view&id=1IIZyey2F-9aRKVk_lRWbE7c97pe-9_gQ",
            "https://drive.google.com/uc?export=view&id=1XwC6rkbHV2NZ9-4qVE06zSr8jAYTMwzb",
            "https://drive.google.com/uc?export=view&id=1yYobXnLPnvBnQnbwmSBCfiA7H0QbnsZH",
            "https://drive.google.com/uc?export=view&id=1Y-tdjApZ6aWO5WlmwItgW88sXZ1QLuh8",
            "https://drive.google.com/uc?export=view&id=1JRo7Hk6q1AGf4zxbbu8ljjj8WQbxrl7g",
            "https://drive.google.com/uc?export=view&id=1MmP9wx9-T1MC4JdBcY056qZp_XiGahbu",
            "https://drive.google.com/uc?export=view&id=1fRja2E0JwcsNSIxZE75WweDuEf52L50m",
            "https://drive.google.com/uc?export=view&id=1MAOwPssWUeJkKgLIW-dPMup1gNwGsEYh",
            "https://drive.google.com/uc?export=view&id=16fxSEsNSf3pbGvIKVjnYUwyQwB2-dWag",
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
                "nim": "",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Senang bisa kenal dengan kakak.",
                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Renisha Putri Giani",
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
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Sangat berkesan, orangnya humble.",
                "pesan":"Tetap jadi pribadi yang menginspirasi!"
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

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rVr_0gSsIwKWB87BBt_zdwvFvIajNAyF",
            "https://drive.google.com/uc?export=view&id=1dfOEIoeckD1UWjvTihEwY-PHVLAWVn1h",
            "https://drive.google.com/uc?export=view&id=116HSJukz-VIvO64MyEVQ-vTif92nGbfu",
            "https://drive.google.com/uc?export=view&id=1k1WrdtMYds1GF1nUwRDBTNdn5i62Ee69",
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
                "kesan": "Abangnya sangat bijak dan keren",  
                "pesan":"Semoga lancar-lancar urusannya"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Keren banget kakaknya",  
                "pesan":"Semoga dipermudah urusannya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Enak banget pas ngajar tutor",  
                "pesan":"Sehat-sehat kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asli pembaik",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ehrDoYj5D67pTx0bfrmhjicQ5A8fsWNX",
            "https://drive.google.com/uc?export=view&id=1exi3e_Ntj2Z0Z_7Ft12zs072FHbCpOyJ",
            "https://drive.google.com/uc?export=view&id=1sZlTdjgGTYMhAdlix0P23iOx_-jIvt7B",
            "https://drive.google.com/uc?export=view&id=17wj6KstkfhPmU6v0Pr9rYX7njp9g34mk",
            "https://drive.google.com/uc?export=view&id=1EBaLW8VR6BEK_isVjfQDkR5uLHFmEKhC",
            "https://drive.google.com/uc?export=view&id=1Ii5fpRhR0NLrV1pczAz7MSb8BFmT2s86",
            "https://drive.google.com/uc?export=view&id=1QV2RvBcw_zHnRtXJ9ftCgo97SLdIYqgE",
            "https://drive.google.com/uc?export=view&id=199gyUvNLQh1kkpKi92Zvy7wiWB1JI4CW",
            "https://drive.google.com/uc?export=view&id=1LHuJ7burtWi8zTcHAIBFHrn5c-3RlqW1",
            "https://drive.google.com/uc?export=view&id=1qz6XhWb8qGV85OhDdA8KvoHaEqwSNCOF",
            "https://drive.google.com/uc?export=view&id=1HbAiv90guk7xDdX1yUlF_atc6p9aoLKQ",
            "https://drive.google.com/uc?export=view&id=1CSGhV8C9LqY1iixHBrORXn96qlh3NVsW",
            "https://drive.google.com/uc?export=view&id=1Sq1l37iHvlmIvHyV_-6OU9Vp9qdnQYjR",
            "https://drive.google.com/uc?export=view&id=1mMzdDiOBe1AKKx2VI3QPKbT5yea589PB",
            "https://drive.google.com/uc?export=view&id=1gtnlzj8oI1Jjgnnu7ZOnA_0WWTztmp3V",
            "https://drive.google.com/uc?export=view&id=1X7R0_dwPgdfbakcDcCgJ1j2EPYu5EikC",
            "https://drive.google.com/uc?export=view&id=1V7UC59jJB0CSzHxZcvpKJGxJoHgPvi7c",
            "https://drive.google.com/uc?export=view&id=1RE1zCQQyq7LRv6GZpKlypv3ctDNnmT3W",
            "https://drive.google.com/uc?export=view&id=18Q8yro81HlsOVZ14Ayrzd6gz99O9o59G",
            "https://drive.google.com/uc?export=view&id=1GxQsYVU8qK_ZJp19paEOXixMsSAaIweb",
            "https://drive.google.com/uc?export=view&id=1zL3urjuhcokJmPxvOJbSK4N_sXXdMkFc",
            "https://drive.google.com/uc?export=view&id=1shlTut4Vw18XjLrORHqCjZkIaZjnRjEg",
            "https://drive.google.com/uc?export=view&id=10z2e3oLf668Q3ZPrqvJPWDzBQ5IuPt0o",
            "https://drive.google.com/uc?export=view&id=1QjAoALyMRtPqW1TWXwF_fCqM9Vl0dGJg",
            "https://drive.google.com/uc?export=view&id=1zL3urjuhcokJmPxvOJbSK4N_sXXdMkFc",
            "https://drive.google.com/uc?export=view&id=1I6q8mpxlf3zA-l9dmO9ql2A1ElghAc2d",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
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
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
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
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
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
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
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
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
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
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
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
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
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
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
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
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
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
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tQZVBywjw_14XJc62C6G2P3nsMDxjSz3",
            "https://drive.google.com/uc?export=view&id=1laATQmDJnDMuDWXEpSgnJTGChIMfCzYZ",
            "https://drive.google.com/uc?export=view&id=1CNS3K63NR-hcGqPNOBAIjmtsRpY0WAPA",
            "https://drive.google.com/uc?export=view&id=17lo5IxDlSaZi4LH3iIDnXOrQu0bXWt11",
            "https://drive.google.com/uc?export=view&id=1nit0FbWfeqy_3o_aUb40WihaqQOBDfZi",
            "https://drive.google.com/uc?export=view&id=11FRsu4WrecjQmKBIFnICaWThRIqyC57u",
            "https://drive.google.com/uc?export=view&id=1ZGhQM5qQermhuZldmmToNmLSH1DZL4pt",
            "https://drive.google.com/uc?export=view&id=1KbgPXBfdRvmK47fyJmnqUOSXMH0KGcoU",
            "https://drive.google.com/uc?export=view&id=1izSZ315doiyY5RdoX7ctYji03hQghZDN",
            "https://drive.google.com/uc?export=view&id=1oNx5D73blydeBZ_G3LNz7A25HhPSz9zL",
            "https://drive.google.com/uc?export=view&id=1OKhmEuIaCD5g-eJgXr-RWfQadScVl-U6",
            "https://drive.google.com/uc?export=view&id=163AK0bDBy4csCr_9zBngjmxLhBRI1GD_",
            "https://drive.google.com/uc?export=view&id=1YFGQ_tThXv-by_7w1vsonP69lDgYSauc",
            "https://drive.google.com/uc?export=view&id=1ZBG72Hrd8IXFat7qckIaf0neLtEJHssc",
            "https://drive.google.com/uc?export=view&id=13p84ZobH_PwUaSIR8x3bVBkxjuVdfid5",
            "https://drive.google.com/uc?export=view&id=1LmYObD5kemvh37kKL5muKgsIzEU3caes",
            "https://drive.google.com/uc?export=view&id=1t9tmuyEs8eh42IZslL8NZC_gIxUu571Y",
            "https://drive.google.com/uc?export=view&id=1KE4kBe8SG1hteu_gDMUmYv54YhDgWgBL",
            "https://drive.google.com/uc?export=view&id=1d9LdhA6jGXksd8EpXaQGAnsojla99DU8",
            "https://drive.google.com/uc?export=view&id=1ez3Mx1j8c6Xwa8bqu4QEmtmoP6s0Njm6",
            "https://drive.google.com/uc?export=view&id=1kSiXkhcQ9EEvuMCC-tnjK5p5KHu6Dw1T",
            "https://drive.google.com/uc?export=view&id=1ynP42kWkQeRqldk6gIix8J6CN2pAbGne",
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "nim": "123450024",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "JL. Gajah Mada, Tanjungkarang",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
            "https://drive.google.com/uc?export=view&id=16nx2UPlec9x-2kT6XrnCmMpFiX_e65gs",
            "https://drive.google.com/uc?export=view&id=1nPY29PYS-UGG4wrbwBiY4rygAIXgFXJj",
            "https://drive.google.com/uc?export=view&id=1HJi7DAJqCZ4hkzsHaRWdZtebMtnvoO7E",
            "https://drive.google.com/uc?export=view&id=1YlxJh2BVs4hLAzYJq8jTdcvH1OoZ5SPq",
            "https://drive.google.com/uc?export=view&id=1hpkRbMzQi98lUHGcUX2DLSXn3eF1jChE",
            "https://drive.google.com/uc?export=view&id=1-zydBVj17b55arujC2fgMSFK_ibT67Uj",
            "https://drive.google.com/uc?export=view&id=10GvRHTu0PQbKyLUm6-IdZlebSaHoX3Jp",
            "https://drive.google.com/uc?export=view&id=1b-imPx6naSoRW6seXEtnGi4_Nq1D1xNf",
            "https://drive.google.com/uc?export=view&id=13YtLOg5KFN8psU77WgjxR6aNI6_YrTIM",
            "https://drive.google.com/uc?export=view&id=1F60NvESlbShfSxZFkoVb1A5peCPGHL5-",
            "https://drive.google.com/uc?export=view&id=1bXAPRQuyfwzgo0DadSb3YtRhPDeVLejC",
            "https://drive.google.com/uc?export=view&id=15O-ctnCmb1BE9GkcKB-QJJA6JVLpkGX3",
            "https://drive.google.com/uc?export=view&id=1XcCO96gRqTdjDxGzoyr94WZZhRrdoDE_",
            "https://drive.google.com/uc?export=view&id=19MLk4m-9z6vsQ5GpKWxSFzJfoelekzAK",
            "https://drive.google.com/uc?export=view&id=1vNk5lnhV2tk2hyOGuTLfqPTp0AQ3lRZy",
            "https://drive.google.com/uc?export=view&id=1aPV9RI__oK3wPREOHuuD-9fzNkJ3kqMZ",
            "https://drive.google.com/uc?export=view&id=1r3mOToOZquKEA4Sfr9puS1AdNL60P5iy",
            "https://drive.google.com/uc?export=view&id=1sSsL0JvWiPPDj-mEuCMoHT8QIjpMu85v",
            "https://drive.google.com/uc?export=view&id=1gTWjxi8gzWUpqqBnV9PUIhWIbsQ8EtfH",
            "https://drive.google.com/uc?export=view&id=128XG-LmLlaRwrcU1z4MtDAUo8GzaqXn2",
            "https://drive.google.com/uc?export=view&id=1JH4yi3L8Wp-8KPVO5vnt8ZLQyTO-eR11",
            "https://drive.google.com/uc?export=view&id=1qP9hTAQEmrI59VWeOG_mJVFG7QZMnROe",
            "https://drive.google.com/uc?export=view&id=10LExoLuTMD88ENH4sXG12QeTRWOO8dgL",
            "https://drive.google.com/uc?export=view&id=1_RvnFc_bgBN142NhoKube247c9wsVBMQ",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abang ini keren dan kalem",  
                "pesan":"Semakin semangat bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini seru dan asik",  
                "pesan":"Semangat terus kak!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak asik dan seruu",  
                "pesan":"Makin positif ya kak!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak baik dan seru",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abang seru dan positive vibes abis",  
                "pesan":"Tetap semangat bangg!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak seru, baik, dan santai",  
                "pesan":"Semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak santai dan kalem",  
                "pesan":"Semangat terus kuliahnya!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak baik dan keren",  
                "pesan":"Semoga tercapai cita-citanya kak!"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abang santai & kalem",  
                "pesan":"Semangat terus bang jadi asprak dan kuliahnya!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak baik, dan positive vibes",  
                "pesan":"Semakin positive vibes kak!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Keren banget kak dutanya!",  
                "pesan":"Semangat terus kak dutaa & kuliahnya!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya lucu dan positif vibes banget ",  
                "pesan":"Semakin-makin dah ya kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abang sigma dan cool parah!",  
                "pesan":"Stay sigma bang, tetep cool!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak baik dan asik",  
                "pesan":"Makin chill ya kak!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakak baikk dan keren!",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abang cihuyyy abis",  
                "pesan":"Semangat terus bangg jadi kadivnya dan kuliahnya!"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Abang santai banget",  
                "pesan":"Stay calm and enjoy the ride bang!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak kalem dan asik",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak asik dan baik!",  
                "pesan":"Semangat terus kakakk kuliahnya!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak baik dan keren",  
                "pesan":"Semangat Kak Untuk segala apapun yang dilakukan!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Kakak baoik dan ramah banget",  
                "pesan":"Semangat terus kak kuliahnya dan cita-citanya!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Baik abnget kakak nya",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang keren dan ramah!",  
                "pesan":"Stay cool dan chill bang!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kakaknya santai dan keren abis",  
                "pesan":"Semangat terus kak dan lancar selalu urusannya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IKRAWzBOC_0OkKqX8n8P9-Z9IHD0-kFS",
            "https://drive.google.com/uc?export=view&id=1MpIYqDbNdqcFk_FeRJoSqkwMqsSn_2jL",
            "https://drive.google.com/uc?export=view&id=173fz_J5RoAL4gDcxLkimgUH_x5VnK69_",
            "https://drive.google.com/uc?export=view&id=1vG3WNwn1f-Chc87GQdbr_eSTYGvryPDK",
            "https://drive.google.com/uc?export=view&id=16UGe5vzaJC1qvBXpbTvfvlNXNC2Ww2gD",
            "https://drive.google.com/uc?export=view&id=1C4Jr9YeIUXgqEeWxoYv45D1tsLtLkkN0",
            "https://drive.google.com/uc?export=view&id=1pk0gSHEuHiFhTd-1Vu4TpoKxbx0qls8_",
            "https://drive.google.com/uc?export=view&id=1K4LuukGrNckynSJ7TR4Vowm793LQatkP",
            "https://drive.google.com/uc?export=view&id=1-ieNNhyykjsfpDSUcNsQDZty1EVmWw8P",
            "https://drive.google.com/uc?export=view&id=1-oO0GHCqJm61Sv_Dk_tgqHPdiC1gSkUi",
            "https://drive.google.com/uc?export=view&id=1DmXB3UHYq2lAR6kso0glFSpBtL4SiDpd",
            "https://drive.google.com/uc?export=view&id=1BbusgRFfILgaceY9daHa_nLbCefNrJXa",
            "https://drive.google.com/uc?export=view&id=1vrwxqLn5MBz9Xzais5pKe-bT9BXmev-G",
            "https://drive.google.com/uc?export=view&id=1rqg1Uu3C_AOIYFclLilIiqkyeP-Y7pF5",
            "https://drive.google.com/uc?export=view&id=1qAw8u7FKXF20rHBTFyv2s3saRcOpm4qH",
        ]
        data_list = [
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
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Kakaknya baik banget.",
                "pesan": "Sehat selalu ya, Kak."
            },
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
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik dan friendly.",
                "pesan": "Semoga lancar-lancar semua urusannya, Kak."
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
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen Rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakaknya ramah dan asik.",
                "pesan": "Sukses terus, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1owwz7obpgkAJ4xHSib_ew7pq58lhXcCq",
            "https://drive.google.com/uc?export=view&id=1qG2psdRvGTnLwEQ-q5b-Rn0geD6dO7W3",
            "https://drive.google.com/uc?export=view&id=136SSj_Hwy1xBXDLTMbtn-GtMSFh1822Z",
            "https://drive.google.com/uc?export=view&id=1ZvSpgkP9EuvAJo9GRSsYhW8_R8xNPFWa",
            "https://drive.google.com/uc?export=view&id=195xPKi7e5cxKB3TW1PzwtPRtc5-81Udb",
            "https://drive.google.com/uc?export=view&id=11bB1DUsYl5PMKf6RBDsBqq-43HwpJwEY",
            "https://drive.google.com/uc?export=view&id=12QJrnpyjNI4C6wEUTnFpfsoFTU1wNRHJ",
            "https://drive.google.com/uc?export=view&id=1T9VmMvbxbVdjI7hETSZU6wRUlupEsF39",
            "https://drive.google.com/uc?export=view&id=1vm-8tSAp1ro9PBXNtsMR4P1zzpmsvnDP",
            "https://drive.google.com/uc?export=view&id=1S7C2tNvRkYCZKd2Dr7Q3XUz6Wjc9Udbe",
            "https://drive.google.com/uc?export=view&id=1BvF0LYMfUKrWtEHhFGwH2AdFXvNsYRhB",
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

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CSROWhB5Eh7Xw7XTNNazUB0iYs03fMgI",
            "https://drive.google.com/uc?export=view&id=1b_h4Yjx-_Ii_HJZPTbrkq4LAvWD5Kg0_",
            "https://drive.google.com/uc?export=view&id=17v2XkJp8Eo812M5hU9pcOee6-NdQvFjR",
            "https://drive.google.com/uc?export=view&id=1quDx5zgiQptd3sce5gCvqblD-ouugRqs",
            "https://drive.google.com/uc?export=view&id=1cZW1-6nm-Td2an2CDu20vXF1isTKlNp1",
            "https://drive.google.com/uc?export=view&id=15gd_d1SkXmWZ3gmvSSdi3WvxioS0Qv0n",
            "https://drive.google.com/uc?export=view&id=10bYT0R69Ht6827S2bdH7kRPKPwB6TbI6",
            "https://drive.google.com/uc?export=view&id=1nxBXmDLcWz52MuDJr9e7Mt9aQxMjzfmD",
            "https://drive.google.com/uc?export=view&id=16cF18ZVx9ajP0efm1jIu0NiVVIJlg1xf",
            "https://drive.google.com/uc?export=view&id=1hWWPOZ0EtLDxmiz9xZ_Qya9HstB88gaa",
            "https://drive.google.com/uc?export=view&id=12rcs8W6wTozZVrhWEzW-Qjt63M7tbbq5",
            "https://drive.google.com/uc?export=view&id=1YvFhKo5A3D2_YQQOnCVrKI0RdpB3toRS",
            "https://drive.google.com/uc?export=view&id=1AbZUT1DSV6w6V8_ivRy16SiRW1pSv-0v",
            "https://drive.google.com/uc?export=view&id=1sGO3gvJj0QOhwlbK7oRHPY6bn_not6qJ",
            "https://drive.google.com/uc?export=view&id=1DF71Q_yK2DH1yKMblHMsUBRhXZaP3Ztu",
            "https://drive.google.com/uc?export=view&id=1Vp5moqTOmH7GUEps9ojWqlBnDhD_V8BN",
            "https://drive.google.com/uc?export=view&id=1MLUXMzS8AlmokqabmtaKsBAzYe4FAmlP",
            "https://drive.google.com/uc?export=view&id=199KABczkDzfeOcucqnFT1FvaNDLLysE6",
        ]
        data_list = [
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
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

# Tambahkan menu lainnya sesuai kebutuhan

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
            "nav-link-selected": {"background-color": "#ffb6c1"},
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
            "https://drive.google.com/uc?export=view&id=1biESKZqHibdLD6f4Fb_fUCPJR2TTSnuB",
            "https://drive.google.com/uc?export=view&id=1gAmmAa_ntZB4jrguUIf65IOPhRhTxOly",
            "https://drive.google.com/uc?export=view&id=1ZJHhtUcTsaz-_t6pf0ZZ-P8B1TFB5pk6",
            "https://drive.google.com/uc?export=view&id=12iB_fI4Io7kppmD6t7-DJRZ0chUXzNDE",
            "https://drive.google.com/uc?export=view&id=1DDjNxp7v7vfyF-GdpnvDIihhJwTMdHED",
            "https://drive.google.com/uc?export=view&id=1iglyvCa7f3GdlTaXpPOED4ECP6-qXmKE",
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
                "kesan": "Abangnya mirip papaku",  
                "pesan":"Semangat kuliahnya bang "
            },
            {
                "nama": "Johannes Krisjon Sitilonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku (Dasar-Dasar SQL)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya keren, pembawaannya menarikk banget, dan baik +++ ",  
                "pesan":"Sehat selalu yaa bangg, terus jadi penyemangatt"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya lucuu",  
                "pesan": ""# 1
            },
            {
                "nama": "Syadza Puspandari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku saku pramuka",
                "sosmed": "@ekshantyfebriana",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang, Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RKUQR7Sq3KIKW2z2Y6Htchqe-wT8rLHT",
            "https://drive.google.com/uc?export=view&id=1jjGBzRma01tsdiX5l7Xbnef8lME3vc_U",
            "https://drive.google.com/uc?export=view&id=1DXNeuJ5S6pitm-h1p0WaLtZUuxTrtCCg",
            "https://drive.google.com/uc?export=view&id=1dfJqtJBgYMIR1KJExp3XJ1rYXcATDNK7",
            "https://drive.google.com/uc?export=view&id=10CHiPVdTKtOjJ81zx3PxIhGZJHh7vwGH",
            "https://drive.google.com/uc?export=view&id=1iYHPoWQ9xMg76GUMAMAFLfpNaITrx6_d",
            "https://drive.google.com/uc?export=view&id=1MP0jlPDqzi3ql0Sl7GxE2VG4lRfn12Od",
            "https://drive.google.com/uc?export=view&id=15Iuv3tN3RejR_zNBHz5RYmWFhgCnE_eU",
            "https://drive.google.com/uc?export=view&id=1XBtyBDTwNoJPonvcVMefyHkkUf3wc9z7",
            "https://drive.google.com/uc?export=view&id=1e1Tk9yTcEV-N40gNk4rYK6BQbRK6a9jF",
            "https://drive.google.com/uc?export=view&id=1TSgWOSvGH0n-bFD9Te5_42LuCiL6ugv8",
            "https://drive.google.com/uc?export=view&id=1fR7ea7XUp_KPDPuFc9OHNeaB5A2gTyrY",
            "https://drive.google.com/uc?export=view&id=1mOi4wYP3MxKp9FrAvkgKF1mTnyPY22wk",
            "https://drive.google.com/uc?export=view&id=1nu12DbvQbxbDMxHIdvHXt9C1EROCci99",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"B2, NO 2",
                "alamat": "Pulau Damar",
                "hobbi": "Zumba di pln setiap jumat pagi",
                "sosmed": "@jeremia.s",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto, Jawa Timur",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan pancing",
                "sosmed": "@-",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Muara Enim, Sumatera Selatan",
                "alamat": "C2",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Dharu Cahyo Aji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Bengong",
                "sosmed": "@dhruchyo",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Menggodai Abang Cimol",
                "sosmed": "@fby.wlndr",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@givarooo",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Mengukir sabun",
                "sosmed": "@berlyyyanda",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Kalimantan Utara",
                "alamat": "Belwis",
                "hobbi": "Sibuk",
                "sosmed": "@j__eesia",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Gang Sakung",
                "hobbi": "Main  Padel",
                "sosmed": "@ianridhomanik",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal": "Bangka Belitung",
                "alamat": "Kobam",
                "hobbi": "Nongkrong di gedung f",
                "sosmed": "@fer_yulius",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Monika Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Ketapang, Kalimantan Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monca_tjg",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pekan Baru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pb1uSGMPl2dwoYIkm4J9XhfAKDARWJj6",
            "https://drive.google.com/uc?export=view&id=1hR8pnbZtBelVtQXVXPQCLCfvv7ZlpipB",
            "https://drive.google.com/uc?export=view&id=1DnNVEOx-LMhxslGHc35Nj2Yzb9PeMvzs",
            "https://drive.google.com/uc?export=view&id=1CdWK3wMZdqbIGnx9JAHP1zPIKy1Y6ei8",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "-",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Lia Hana Ichisassmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f1RadtfwCMXMUJSsQB7QyiVaxkUH898r",
            "https://drive.google.com/uc?export=view&id=1xzqDLDEtNCMjn6UNc2c_1bkQmFPadp75",
            "https://drive.google.com/uc?export=view&id=1s-nm0SRGb3pADl56ZSISxXMcoPllY-fU",
            "https://drive.google.com/uc?export=view&id=1Fs9cbQ3RjDDg4TB5kpi6-Ja-wbZQ6c-f",
            "https://drive.google.com/uc?export=view&id=1greRFBeVcvJV3QbRCdMAi1bAvKWjC_zF",
            "https://drive.google.com/uc?export=view&id=1JK35Asi0XZPcz_UTGYcZ03J7QUjFws9e",
            "https://drive.google.com/uc?export=view&id=1rMckCAhl-LMzKqJPi5XZVBThXOMXtbcC",
            "https://drive.google.com/uc?export=view&id=1faJSKGK8JVOZM9gVfZzEuvjfTDok4N6i",
            "https://drive.google.com/uc?export=view&id=1v1UelcHZPmsaqLgDFPeLzN5bWsxNFIE7",
            "https://drive.google.com/uc?export=view&id=1cMn4OmPSVIFybiPHmieZGGinMslOTk8d",
            "https://drive.google.com/uc?export=view&id=1FVsquGm547BU3xno_MyFaqT7ulrQ5lt3",
            "https://drive.google.com/uc?export=view&id=1Np3DSYBEGq3u1UgBitJDf_Ny7P6aF0kw",
            "https://drive.google.com/uc?export=view&id=154oX7H7y9GHbsi3bw_rfJbUU26gwjzNQ",
            "https://drive.google.com/uc?export=view&id=1C0sXEFiLScSx6rNys4dtY30A8lU4LeW0",
            "https://drive.google.com/uc?export=view&id=1V7PqvtMsmWSSgUYUsoZD1DPCfChawtN8",
            "https://drive.google.com/uc?export=view&id=1EAp4oM3QRtQEC1DymvHFwXORXkyLxYMo",
            "https://drive.google.com/uc?export=view&id=1KN7MEK-ZHD_E85ND6ayPiet6CyqQTfE-",
            "https://drive.google.com/uc?export=view&id=1JBY0bYsiOPyf92RspdDFkQ6rUqZbgDfl",
            "https://drive.google.com/uc?export=view&id=1dykVpP6VTa4HZ9ZHvDGenFxEVuDUrB8y",
            "https://drive.google.com/uc?export=view&id=1vizzno5rZKaJg6Zv9GCZq9nPaOFobx9v",
            "https://drive.google.com/uc?export=view&id=18yE59Im3mDlOItbQzVF2snbL02mVQayW",
            "https://drive.google.com/uc?export=view&id=1NEA02rvjxWZiXIDSXFkjoiPiSbm0bWhF",
            "https://drive.google.com/uc?export=view&id=1HwcDKOeAu9xna7ReMm7jHG9qWvnt0-_g",
            "https://drive.google.com/uc?export=view&id=1WbRqFYPhJUojnW18trxMhadldrtTy53R",
            "https://drive.google.com/uc?export=view&id=1DotoW71FlXDLFRjslR6KIWSr9oLXmNZv",
            "https://drive.google.com/uc?export=view&id=13mwRTbDNO42WjUny6bM3kyV83feGcUrd",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ferdy_kevin",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@afifahhnsrn",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "123450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira",
                "hobbi": "Main",
                "sosmed": "@alyapasha_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ahmad.rizky___",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "sebelah  kos bang dapa",
                "hobbi": "Liatin Haikal",
                "sosmed": "@arientakhsnl_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "sebelah kos kak arin",
                "hobbi": "Isengin Fislam",
                "sosmed": "@daffahdynn_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Cikarang",
                "alamat": "Sama kek bang ahmad",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Gg. Perwira",
                "hobbi": "Ngakader",
                "sosmed": "@berlyyyanda",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450022",
                "umur": "-",
                "asal": "Sumatra Barat",
                "alamat": "-",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@vany.salsabilaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@sahid22",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ali_parisi3",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Waydadi",
                "hobbi": "Tidur",
                "sosmed": "@verazkaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@risma.mustika_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "-",
                "sosmed": "@ahmadnaufa_ll",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Makan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Makan Beling",
                "sosmed": "@kevinaj__",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450023",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Main Badminton",
                "sosmed": "@m.ridwan_22",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Berenang, ngoleksi figura & kartu anime",
                "sosmed": "@rewinanaaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Uliano Wiliam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Main piano, nanem anggrek, ngoding dan nyari kesalahan anak 24",
                "sosmed": "@ilano",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rG8xyEe9wU5Iemr8YFT5gGHWwgsO3QZR",
            "https://drive.google.com/uc?export=view&id=15oHa031-FwBGs3F4uoeY28r6mnvpNGD-",
            "https://drive.google.com/uc?export=view&id=1UXScXusQT4rAm3nh0c1l2KTErAYtumTl",
            "https://drive.google.com/uc?export=view&id=1Iy-w2iwqJpYN7UBQgpD0d8E7OVA-_bgx",
            "https://drive.google.com/uc?export=view&id=1jTOYe-5XQv7BTQXxhsnnJ6eL_9NKaRCJ",
            "https://drive.google.com/uc?export=view&id=1HThc-CSeBrOuZOMFRl7CCb_DWvr13hQQ",
            "https://drive.google.com/uc?export=view&id=13kg0lBRHD9UgKxLmSbbWRtqjH4D_OpEU",
            "https://drive.google.com/uc?export=view&id=1fFIzxpMkBHJ_5lNLMnUNpBqg05SKm5wY",
            "https://drive.google.com/uc?export=view&id=17_AYocaB3zkMlipasN_wfDPh_ZTbuX7u",
            "https://drive.google.com/uc?export=view&id=1J0b6fd5HbE4xl2fmpJYNOUWSYB4rg7Uy",
            "https://drive.google.com/uc?export=view&id=1PBpdvHmqq52tx6oqgwDEvRfM-6sWzB1L",
            "https://drive.google.com/uc?export=view&id=1z38TNt_cYrW931kUrrHUgFGRc1ttpzFa",
            "https://drive.google.com/uc?export=view&id=175VPWyJaAOiZ4Dzdrb3BxTJkeHJwTEbS",
            "https://drive.google.com/uc?export=view&id=1JD52SZ5X5ZpS-euPWNB9SXNi5TS7oMDU",
            "https://drive.google.com/uc?export=view&id=1_IwScb0mCGeqbNieMMO-WgUWUv2oujhp",
            "https://drive.google.com/uc?export=view&id=1cLIIpJtUrXtN1Mbvl1D8_gjKErSjf2AN",
            "https://drive.google.com/uc?export=view&id=1bJruIYAlgMsy-BP1DQsRYuXNaSw7uJNv",
            "https://drive.google.com/uc?export=view&id=1qw-aKa8XbGyENdvJM4RUJITXsq194hnm",
            "https://drive.google.com/uc?export=view&id=1ZRrF9OZakZ41JOx-F2qAOyTTcWELwjIw",
            "https://drive.google.com/uc?export=view&id=1NKRaS4Gaj9V8vuONw2T89q_-jFfFQaCT",
            "https://drive.google.com/uc?export=view&id=1iXpRoWgstBBkLMW5Hr4aLBIDT7wLF9tB",
            "https://drive.google.com/uc?export=view&id=1V3X_Shu3ZdggliK9X7vzweSvSwcEuwrc",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "-",  
                "pesan":"-"#2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta ",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@mregiiii_",
                "kesan": "-",  
                "pesan":"-"#3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "__",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "122450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Gg. Sakum Jl. Kaswari",
                "hobbi": "Main Baskok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@notfall.s",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jln. Manggis 1",
                "hobbi": "Nonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Pramuka, Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@keyashafi_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Jl. Seputih, Bumi Sari Natar",
                "hobbi": "Menari, mendengarkan musik, dance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano, Nyanyi, Ngehalu",
                "sosmed": "@bee_0115",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Padang, Sumatra Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Roblox dan Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tunty",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumatra Barat",
                "alamat": "Jl. Hasan IV, Airan",
                "hobbi": "Isengin Orang",
                "sosmed": "@fifah.zy",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "122450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No.27A, Kedaton",
                "hobbi": "Jadi PJ Kelas",
                "sosmed": "@biyokcb",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jalan Airan 1",
                "hobbi": "Balapan Random",
                "sosmed": "@gustriana.d_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razynhfd",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CaSdHeSSev4ausXuOENzYhIhi5zcUVGV",
            "https://drive.google.com/uc?export=view&id=1WycJFtgSeKDW8gfeRYE9nMXb66-xBTX-",
            "https://drive.google.com/uc?export=view&id=17B5aggm40EGzJIcqjoulpw6bl-bL6Qtb",
            "https://drive.google.com/uc?export=view&id=1ftdVU4BOHio8fDrT-hl4dKzBxsOhv48d",
            "https://drive.google.com/uc?export=view&id=1PNDXUXddNVDPQTqO3yD8Zb-6rW_CmTyc",
            "https://drive.google.com/uc?export=view&id=1sfbdAyXgCMFar4VPny_M8cjm2lg8zimy",
            "https://drive.google.com/uc?export=view&id=1m7g4qo0afG2JwYGBRxwIs-PV-3Rwasbn",
            "https://drive.google.com/uc?export=view&id=11vmrvLEgPHZVoMvT7eF9WGkgDoDRX9P0",
            "https://drive.google.com/uc?export=view&id=1pAJ1Ywl5eIwWV1tvBk6vniVLa6kNjs2a",
            "https://drive.google.com/uc?export=view&id=1r5gKKfFr59kmlSP3IPilu53ZKczQe5k0",
            "https://drive.google.com/uc?export=view&id=1Y9TDBAk4hh8wOooogELscpgX-xk5Er7B",
            "https://drive.google.com/uc?export=view&id=1N5g5p50YdNufYQkQewxzjF_izzeeVePU",
            "https://drive.google.com/uc?export=view&id=1Wfg__HUhugDwZiQC42Qk4vPmcZi5aEUf",
            "https://drive.google.com/uc?export=view&id=1JwJOaCp64X-j_7Z8UzcXsypW0inMpOua",
            "https://drive.google.com/uc?export=view&id=1YEOFg218PqTzciQXuCbW5xTkwMorixRF",
            "https://drive.google.com/uc?export=view&id=1-Q0OJUpyLq5OUkrEfbMuYH8nVdQnnLfv",
            "https://drive.google.com/uc?export=view&id=15D706O32zD4gEy7cUSm34e6FiW8UyPG-",
            "https://drive.google.com/uc?export=view&id=1nogE2JZqQCwVKxqfMBu9w8dB5TVea_On",
            "https://drive.google.com/uc?export=view&id=1uYqnYNFU9fxQGpLcyalXYmeX_YgJNjvI",
            "https://drive.google.com/uc?export=view&id=1EKRO9tdAcyl0xORR_vKpqFj9GytAbthe",
            "https://drive.google.com/uc?export=view&id=1z99ByvmfrfdOj33IqFBnXUqaeEdPMFz7",
            "https://drive.google.com/uc?export=view&id=1aMxl-9fBoZr44DbgL9Eai2hZbYOAD1ju",
            "https://drive.google.com/uc?export=view&id=1A9I2CRN-SlnkAYPCkpvtwolW-fCgWzVP",
            "https://drive.google.com/uc?export=view&id=1z99ByvmfrfdOj33IqFBnXUqaeEdPMFz7",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@ferdy_kevin",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jln. Hidup",
                "hobbi": "Balajar",
                "sosmed": "@yo_anamnk",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "-",  
                "pesan": "@aryamudasiregar"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal": "Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "Beli risol ayam Naya ",
                "sosmed": "@cindylauura",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "Nonton reels AGZ",
                "sosmed": "@deaamnd3_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "Gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_Tq90",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafirarz",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "-",  
                "pesan": "-"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Tarisya hidayatul rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LTUd3RnZnQ_cWC9pYPor60Dajz1cQZXY",
            "https://drive.google.com/uc?export=view&id=1mRwI2SCpN-YVtOU6vEXSH5YnwGhhgjoC",
            "https://drive.google.com/uc?export=view&id=1LZqb_6RLyWCcRcprkPrh-g3MIlVtzvxl",
            "https://drive.google.com/uc?export=view&id=1i-TZ1Dt9GDYyX2pG8UQY53GJMEm-5UDi",
            "https://drive.google.com/uc?export=view&id=1wi_4Rle7f56V4FtZrldTms5dLhkbjEMK",
            "https://drive.google.com/uc?export=view&id=1y0E4sKCNjkjRDm9nqBlFnIgbQ2EGMsJw",
            "https://drive.google.com/uc?export=view&id=1eTwbl3pwJiMvaHLeDadd81c2rwgzXfky",
            "https://drive.google.com/uc?export=view&id=1ZTDpTOQZxZ22sGUuv0aRzJS6yMTlV2ay",
            "https://drive.google.com/uc?export=view&id=1GGMupOm6AmsAyeBepmGcx7Y9YMElRAo2",
            "https://drive.google.com/uc?export=view&id=188TL9FxP3wW4c9NUfVP1nOAjfp1dGvG_",
            "https://drive.google.com/uc?export=view&id=16IS_zHCNScugM0j72UAxDtI7AebFYZ39",
            "https://drive.google.com/uc?export=view&id=1doG16qO588ZHyPd6smYCvMb6HTNjLumD",
            "https://drive.google.com/uc?export=view&id=1mwY9NUmrS77ugmmmorlxfotV_tdeNhmu",
            "https://drive.google.com/uc?export=view&id=1-d8HxRcziMu7_S5iaeWhKw5KPGdbcWda",
            "https://drive.google.com/uc?export=view&id=1OnWj2AubRki6rDi4WIzA2TqYWUGLK_YT",
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
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Menjahit",
                "sosmed": "@sarahwati",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Jalan Durian 19",
                "hobbi": "Mengetik",
                "sosmed": "@zhresti",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Kota Baru",
                "hobbi": "Hiking",
                "sosmed": "@rexsander",
                "kesan": "-",  
                "pesan":"-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pb1uSGMPl2dwoYIkm4J9XhfAKDARWJj6",
            "https://drive.google.com/uc?export=view&id=1m0tqFP1HW85QibV9OlIG4iKQiJlatxsm",
            "https://drive.google.com/uc?export=view&id=1XsFSlxzTNytO63YsfJKWd8Ztmh0VMQFw",
            "https://drive.google.com/uc?export=view&id=1hPzPcRrL9UPVlm0QEh-k63Xa0XacWYLd",
            "https://drive.google.com/uc?export=view&id=1BxvmRj02-D-lpYa2pmqq9BOQAsvZZn3w",
            "https://drive.google.com/uc?export=view&id=1ijeqecXPST7hR1Bn4HV2wiKTG1qhfF9R",
            "https://drive.google.com/uc?export=view&id=1GGrY0X7Y-HHT6ybCj8efo9Cbrbxbudwx",
            "https://drive.google.com/uc?export=view&id=1E_xJb5jZbgMnTZEI9e2x8JgtMlVSx_zw",
            "https://drive.google.com/uc?export=view&id=1n82quEk2xLQ__Gl_hfLw8AW6-ox70l5c",
            "https://drive.google.com/uc?export=view&id=1OTbmrzJcspAMkL0O7W_bM3HxIZX8G-Ak",
            "https://drive.google.com/uc?export=view&id=1pDDJHRrnATGWQT893g64JVYzlC_j_AW5",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Olahraga",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya keren banget, banyak ilmu baru yang didapet dari abangnya. Dan dapet pencerahan juga hehe",  
                "pesan":"Semangat berkaryaaa dan semangat berprestasi yaa banggg!!!!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya baikk",  
                "pesan":"Semangat kuliahnya dan semangat menamatkan novelnya kaka"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya kerenn, sering termotivasi",  
                "pesan":"Semangat mencetak prestasinya bang"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya soft spoken",  
                "pesan":"Semangat ya kak kuliahnyaa"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton",
                "sosmed": "@aprhtp_",
                "kesan": "Kakaknya lucu dan imup",  
                "pesan":"Semangat mencerahkan hari ya kakk"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya tegass, aku suka cara bicaranya",  
                "pesan":"Semangat kakk untuk kuliahnyaaa"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya keren, semua pertanyaan dijawab",  
                "pesan":"Semangat yaa bang kedepannya"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya asikk",  
                "pesan":"Semangat kak kuliahnyaa"
            },
            {
                "nama": "Engli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "Menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakaknya baikk",  
                "pesan":"Semangat terus kuliah dan jalani harii kak!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya lucuuu, imutt, cantikk dan baik bangett<33",  
                "pesan":"Semangat terus kak kuliahnyaaa, pengen beli lagii risol jumbo sama dimusum mentai punyaa kak nayaaa"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakaknya tegas, keren banget.",  
                "pesan":"Semangat terus kak kuliahnya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NreIDZLP6yWf8gbTwKfHy8gK-5_a_AFy",
            "https://drive.google.com/uc?export=view&id=19wKC-fDukwrPnfTJr0XdoVwlukWl2PFB",
            "https://drive.google.com/uc?export=view&id=1iay70vJudZTD3g4nNuIHE2hYsydvQFSO",
            "https://drive.google.com/uc?export=view&id=1UBJqkg1ciHNA-1foI431NEu58-BLIXYx",
            "https://drive.google.com/uc?export=view&id=10pDeP6NlYTWERflRbmrF5e3FGIecWTFD",
            "https://drive.google.com/uc?export=view&id=1FbHGU9LzlPM-zoIV46yfR52ZYRIjnJJz",
            "https://drive.google.com/uc?export=view&id=1iIbFRZC3adpdfD7_Px_z_C8D-VrWnbwg",
            "https://drive.google.com/uc?export=view&id=1LOPjT-pfMffJD6WxMlC3gjRk6YEVHyBz",
            "https://drive.google.com/uc?export=view&id=1nMvQS9Bslgd2XVW6fb0JW3B_BAh0_h_D",
            "https://drive.google.com/uc?export=view&id=1Wf-0-mL7Yve6zn6HQ3zhJE6DoA8zKsIc",
            "https://drive.google.com/uc?export=view&id=1JWUOddsYzlJhiX8DApiUwccyKz4vLUgv",
            "https://drive.google.com/uc?export=view&id=1AgdFcJUyVEbfi5kOpe5MJk24tCsWvdgf",
            "https://drive.google.com/uc?export=view&id=1KCI4QNydeNByZ6UjJQqcxjlP_02w9WXU",
            "https://drive.google.com/uc?export=view&id=1f6IyeSiE3iAv8K0_MUs8E-8s7sh2WVHF",
            "https://drive.google.com/uc?export=view&id=1m7_ptGDGxWohtWwD8X4niS_iV9_gs7Sx",
            "https://drive.google.com/uc?export=view&id=1ICqhOreJEe8U28Mqn7O6HPnHk1IcI0E2",
            "https://drive.google.com/uc?export=view&id=1DTk1fhSLD2lSuxoXPYtRD0F7VP9BZbYL",
            "https://drive.google.com/uc?export=view&id=1_9_wxsymMmVs2zFRDXGSfupIj3HI-P_n",
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
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "-",  
                "pesan":"-"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakaknya kalem, ramah, dan kelihatan baik.",  
                "pesan":"Senyum kakak manis, terus tersenyum ya kak! "
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya manis, imut, gemesinn",  
                "pesan": "Teruslah mewarnai ITERA pakai baju colourfull kakak itu ya!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menyanyi",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya menarik banget, aku suka kacamata dan rambut kakak",  
                "pesan": "Semangat kuliahnya kakk, teruslah jadi diri sendiri."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


# Tambahkan menu lainnya sesuai kebutuhan

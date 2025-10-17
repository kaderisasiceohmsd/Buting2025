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
            "https://drive.google.com/uc?export=view&id=1Wdk7Bk508P1gditPG0vD57_oujk9CxmU",
            "https://drive.google.com/uc?export=view&id=1YxNN2OfjmXz7QyruVPdl3CG9OeANkHY8",
            "https://drive.google.com/uc?export=view&id=1DkvvEpUErdrTCN4sJxBIVI8wKHabLSWY",
            "https://drive.google.com/uc?export=view&id=1loX0Pw1SZQUbDdhY2ZQfm53e3pVX4WIy",
            "https://drive.google.com/uc?export=view&id=1hUJcxsj0-6qfOetuXoum6aZniJ0TAUMk",
            "https://drive.google.com/uc?export=view&id=1LoMezQxhT0kAdatAtgkRbLiBg9i4jLTp",
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
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Johannes Krisjon Sitilonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku (Dasar-Dasar SQL)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabethh_",
                "kesan": "-",  
                "pesan":"-"# 1
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
            "https://drive.google.com/uc?export=view&id=1U-4FiFTLlB2_JLwKhj9_KSwscoRgvA2v",
            "https://drive.google.com/uc?export=view&id=1iV72ffulfCF4PuFGjgE8djdjphZin3a1",
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
    def PSDA():
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
            "https://drive.google.com/uc?export=view&id=1YC18MCFbcNy5M6DOMbVPo0dqBlllC6eH",
            "https://drive.google.com/uc?export=view&id=1V7PqvtMsmWSSgUYUsoZD1DPCfChawtN8",
            "https://drive.google.com/uc?export=view&id=1EAp4oM3QRtQEC1DymvHFwXORXkyLxYMo",
            "https://drive.google.com/uc?export=view&id=1KN7MEK-ZHD_E85ND6ayPiet6CyqQTfE-",
            "https://drive.google.com/uc?export=view&id=1JBY0bYsiOPyf92RspdDFkQ6rUqZbgDfl",
            "https://drive.google.com/uc?export=view&id=1dykVpP6VTa4HZ9ZHvDGenFxEVuDUrB8y",
            "https://drive.google.com/uc?export=view&id=1vizzno5rZKaJg6Zv9GCZq9nPaOFobx9v",
            "https://drive.google.com/uc?export=view&id=18yE59Im3mDlOItbQzVF2snbL02mVQayW",
            "https://drive.google.com/uc?export=view&id=000",
            "https://drive.google.com/uc?export=view&id=1HwcDKOeAu9xna7ReMm7jHG9qWvnt0-_g",
            "https://drive.google.com/uc?export=view&id=1WbRqFYPhJUojnW18trxMhadldrtTy53R",
            "https://drive.google.com/uc?export=view&id=1DotoW71FlXDLFRjslR6KIWSr9oLXmNZv",
            "https://drive.google.com/uc?export=view&id=1i7eWGVIO8GmcORPzHmqaIpnTIedT4qFK",
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
    Psda()

if menu == "Departemen MIKFES":
    def MIKFES():
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
                "umur": "22,
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
                "pesan":"-"# 1
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
                "pesan":"-"# 1
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
                "asal":"Padang, Sumatra Barat",
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
    MIKFES()




# Tambahkan menu lainnya sesuai kebutuhan

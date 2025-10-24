import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubahh
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
            "https://drive.google.com/uc?export=view&id=1PWgd0d1WJPGmFzMpzzNN3ypwf1pKuJ1S",
            "https://drive.google.com/uc?export=view&id=1zE20P-0mF1v7LxjdNIACEW-Hrem77e4i",
            "https://drive.google.com/uc?export=view&id=1PDzfXOK_kR5_74WfAHu0BshwB3a4WZac",
            "https://drive.google.com/uc?export=view&id=1yoKRqF42sV3Efktym-3wZDpAEZ05X6U0",
            "https://drive.google.com/uc?export=view&id=1c5nSdoeT6-hAzX7GQ9LZ294CDK61mCb3",
            "https://drive.google.com/uc?export=view&id=1CPR_jNy2qkHbQ0p9OM4ElfVyoYRANyXm",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Bang rendra aura nya berwibawa sekalii",  
                "pesan":"Semangat terus bang Rendraa, semoga diberi kesehatan selalu dan semoga TA nya lancarr  !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Johannes seru dan asik bet bangg",  
                "pesan":"Semangat terus bang Jo semoga sehat sehat selalu bang !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Airas kost",
                "hobbi": "Nyemil",
                "sosmed": "@celisabethh_",
                 "kesan": "Kak elisabeth keren banget kakk dan seru",  
                "pesan":"Semangat terus ya kak Elisabeth, semoga diberi kelancaran segala urusan"# 1
            },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza cool banget !!",
                "pesan": "Semangat ya kak Syadza,semoga sehat selaluu dan semoga lancar selalu dalam segala urusannya !"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "Ngelas-ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty keren banget dan baik",
                "pesan": "Semangat terus kakk, sama tutorin cara baca zodiac dong kakk hehe"
            },
              {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "Kiya kost",
                "hobbi": "Domino, Qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak Farahanum positive vibes banget!",
                "pesan": "Semangat terus ya kak, semoga lancar segala urusannya dan diberikan kesehatan selalu !"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iDl4JLIP3XjfS8Sy9uSBLnHHsTQ9YdPm",
            "https://drive.google.com/uc?export=view&id=178FuYOTx-INMe_TxClkQWB66szatuWJB",
            "https://drive.google.com/uc?export=view&id=13vQ2zF-uXuXsVwyW-4g3AXG9TgFM8tcC",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1YzLGRDTe1oIGzh98DTgddflSvTJQp69Z",
            "https://drive.google.com/uc?export=view&id=11VxCJ04eN1w6R9WM8QRBHGXOx39XB8Sy",
            "https://drive.google.com/uc?export=view&id=1qJsfTKMyswbhancS5N0wJjzJKUuG2Knm",
            "https://drive.google.com/uc?export=view&id=1XiqbhEt76FGMa9BD8-lElS5BNw9Qe8pj",
            "https://drive.google.com/uc?export=view&id=11mz6oZEOlV-JDcRNtfbMKcHJtiZtaVx7",
            "https://drive.google.com/uc?export=view&id=1mX22eYo55tcsCJSb7MBngyGiK_Hfgpn4",
            "https://drive.google.com/uc?export=view&id=1cqn8es4SWHIAoaV4TkX-bWBxVuFBjW58",
            "https://drive.google.com/uc?export=view&id=1D9z5SgIGDPfHoVgXMb7aaA7a-5r5QWmE",
            "https://drive.google.com/uc?export=view&id=1YfzzgwyF0UL5H4H-410P4A3qDkRZHAyN",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Tanjung Merawa",
                "hobbi": "Suka main voli sama Feby",
                "sosmed": "@jeremia_s_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Kak Anisa asik banget!",
                "pesan": "Semangat terus kuliahnya kak Anisa, sukses selalu!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1s-VhFSDT2U-ax1-WvGgl2JFQ_FfTA2m-",
            "https://drive.google.com/uc?export=view&id=1fT_LxnS1tkIGOHtUqLQ6ev2gIvxcHbsR",
            "https://drive.google.com/uc?export=view&id=12n9SBdSFhixhiClQWSvfTSzGG2klfDyT",
            "https://drive.google.com/uc?export=view&id=1Qo7OC1zTTTBtK6fd3L-t58fnLAi-Z8bm",  
        ]   
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Belajar",
                "sosmed": "@bintangtwinkle",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19guvmp56YeIZmyeFQ5QENPW_H9jm-sae",
            "https://drive.google.com/uc?export=view&id=1poKBbCdNJla_1WFXwOI-hPO27vFsHSmX",
            "https://drive.google.com/uc?export=view&id=1VlaDNUQ8tFEp1jKKrOPps7-vZGPyF7Fz",
            "https://drive.google.com/uc?export=view&id=1M3gvSslU922RWezd6QZ9Zx-bU7IqMeb7",
            "https://drive.google.com/uc?export=view&id=1dkfw4jv5Vr_VPPFeJyUgCguWGhurZPtk",
            "https://drive.google.com/uc?export=view&id=1E29u_nHaVhg3TRkTXLaau0CTir5ukN8H",
            "https://drive.google.com/uc?export=view&id=19Genc8srgIv-na_jDNEroLKonZI6IOe7",
            "https://drive.google.com/uc?export=view&id=117RT_H2b7fbpL3l1nF5CC0fumlSpn_O1",
            "https://drive.google.com/uc?export=view&id=1qiJPvNFUdllVcyX_dkgg0jTdLNuUA9Xe",
            "https://drive.google.com/uc?export=view&id=1EmfSTSoHxQQmPGyI9IXy7GwnM733z9Xl",
            "https://drive.google.com/uc?export=view&id=1RPgp8_hnodE7vEgyWqdSy93aY0CJI_4l",
            "https://drive.google.com/uc?export=view&id=1Fw0S1Pd5ANe0xge_9BipVvYtsvKYf6Qt",
            "https://drive.google.com/uc?export=view&id=1EH0xRJ_9lqQ7SY8AhAI1H9OnbImR6vnf",
            "https://drive.google.com/uc?export=view&id=1JLN29TeEG9147rTK-TUD5jXOzzpAjB7A",
            "https://drive.google.com/uc?export=view&id=1p09yrbCC6Ehm8pg_AjaO_e0086yjXovC",
            "https://drive.google.com/uc?export=view&id=1YwvWEsbxA7XUiBUMDWSrSbIUbXbZ4i83",
            "https://drive.google.com/uc?export=view&id=1jvWRneqs6FUeTfam_4DwgGacdUw1QVxE",
            "https://drive.google.com/uc?export=view&id=1-ZSeHbPqbCo5A_nJixJwGBWEYRi7VK62",
            "https://drive.google.com/uc?export=view&id=1nJoG_tjq9ifNT8WHsiCBpQ0USW521--4",
            "https://drive.google.com/uc?export=view&id=19iiGjkJYBNoRe8EgEG3tyjdGciQC31Ma",
            "https://drive.google.com/uc?export=view&id=1mWVA14ME_Pcpm0FhR1SCgLQh3TQxOXqQ",
            "https://drive.google.com/uc?export=view&id=1x8UXCC9LXBUxMqDqD_LJsm3GAiS6N2lo",
            "https://drive.google.com/uc?export=view&id=1RP3cDableBg2cSqM4oRgNV2keikffXzl",
            "https://drive.google.com/uc?export=view&id=1hgKmLAAzfXlztHAralDZNUitF4KIl1Go",
            "https://drive.google.com/uc?export=view&id=1-i8Owp2tMVTg4bQBnoJVHEi6pBsoKIh0",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Ngekader 24",
                "sosmed": "@Allyapasha_",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Tangerang selatan",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "5 km dari pantai kedu",
                "alamat": "deket kost bang dapa",
                "hobbi": "cari kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "rahim ibu",
                "alamat": "samping kost arienta",
                "hobbi": "jahilin yulia",
                "sosmed": "@daffahdynn_",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "19",
                "asal": "lubuk linggau",
                "alamat": "kost putri gerbang barat",
                "hobbi": "ngitungin duit",
                "sosmed": "@natasyaamavisca",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Samping kost kak alya",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma family",
                "hobbi": "ngasprak",
                "sosmed": "@j_gumel_17",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "airan raya",
                "hobbi": "ngoding di macbook",
                "sosmed": "@vany.salsabila",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "1224450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22_",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Sukarame",
                "hobbi": "Main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@farazka",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@risma.mustika_",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "rosaliasiregar_",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi": "Main Video Game",
                "sosmed": "@sahid_maul19",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "-",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerjain Tugas",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi pita pink",
                "sosmed": "@d_aniar",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Gangguin Kak Dea",
                "sosmed": "@ihsan.yusuf",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Ngomongin Kak Dea",
                "sosmed": "@kevinaja",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dia_natzzyaa",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nyuruh Kak Dea diam",
                "sosmed": "@m.ridwan_22",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "jl. Raden saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Benget Sidabutar",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "-",
                "pesan": "-"
              },
              {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Ibu Kota Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Cari GPT",
                "sosmed": "@rewinanaaa",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1n9K0yKNuKjUOdqrDXWlAQqJHDpoIIiSu",
            "https://drive.google.com/uc?export=view&id=1Ro7GeJhFwVmp7211qgNa8qvrAPrUtriK",
            "https://drive.google.com/uc?export=view&id=1HylddKvqVZ7x6b7m9gY2dChulOTryN3b",
            "https://drive.google.com/uc?export=view&id=19uNGuuYThf1q0mW5nZWAQJ6zPScI-kwM",
            "https://drive.google.com/uc?export=view&id=1TKGt2pOQnjZYrkO6YDj1J-yxCVqley5w",
            "https://drive.google.com/uc?export=view&id=10GJ9ozXu_RhmZiMuRFZYMqpZ0lvWAP9c",
            "https://drive.google.com/uc?export=view&id=1U9dAsOgeETzhDJAXRfSNQfBuGtq_Vazw",
            "https://drive.google.com/uc?export=view&id=1ogWjCxHvwitnXxW8_N1iPBUqw1scYK2J",
            "https://drive.google.com/uc?export=view&id=1siNiGY8nwUAtboQZrGIVNAcU-OR6g4Hl",
            "https://drive.google.com/uc?export=view&id=1VcDVNQxkKoQ7b1sp87XIWp3YeDbLmL3_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1zjHxSFBWhSB0rXPmk6hMbmBc7_vYPjDQ",
            "https://drive.google.com/uc?export=view&id=1fOTq1vaV3nYQ_S-99MGGc6Ft8GgA3m5N",
            "https://drive.google.com/uc?export=view&id=1ppMyXnboxh8tmYzHqhdSuwutFkLKReVq",
            "https://drive.google.com/uc?export=view&id=1QKycQnJEBLU8r-o-iRWCp3sp3VtfpbLR",
            "https://drive.google.com/uc?export=view&id=1l2lPikqqGoBwn7Q1o8NiDs6m1hqtGIfk",
            "https://drive.google.com/uc?export=view&id=1llaq0tru79dhah1CFqibXjWb7c95_EBh",
            "https://drive.google.com/uc?export=view&id=1S1speLYTZO53LIaguLsXfrYk--HXHDq7",
            "https://drive.google.com/uc?export=view&id=17oYBPaxDWDbgGp-OVwsfueG-H1ufuSxR",
            "https://drive.google.com/uc?export=view&id=1ifqfO10kIQH9ItVk4DSdEUduwEi_ke1X",
            "https://drive.google.com/uc?export=view&id=1MxoAXQ6L1ypoomSXvzDbZHYMCa-wLPNo",
            "https://drive.google.com/uc?export=view&id=1ePvRlRBYvwAjkcJ0eoQZO9sPukq0SQyb",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@@randaandriana_",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "124450081",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@tunty_i",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "",  
                "pesan":""# 1
            },

        
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
    
if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                  "nim": "122450002",
                  "umur": "20",
                  "asal": "Spanyol",
                  "alamat": "Asrama",
                  "hobbi": "Bank BSI",
                  "sosmed": "@arafiramadhanmaulana",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Yohana Manik",
                  "nim": "122450126",
                  "umur": "20",
                  "asal": "Usul",
                  "alamat": "Jl. Hidup",
                  "hobbi": "Belajar",
                  "sosmed": "@yo_anamnk",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Ratu Keisha Jasmine Deanova",
                  "nim": "122450106",
                  "umur": "21",
                  "asal": "Bogor",
                  "alamat": "Way Kandis",
                  "hobbi": "Nyetrika baju",
                  "sosmed": "@jasminednva, follow @cerebral.id_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Arini Puteri Elandra",
                  "nim": "123450069",
                  "umur": "20",
                  "asal": "Lampung",
                  "alamat": "Teluk, Bandar Lampung",
                  "hobbi": "Jalan-jalan berkeliling dunia",
                  "sosmed": "@elandraa_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Arya Muda Siregar",
                  "nim": "123450063",
                  "umur": "21",
                  "asal": "Bandar Lampung",
                  "alamat": "Rawa Laut",
                  "hobbi": "Ngelamun",
                  "sosmed": "@aryamudasiregar",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Khoirul Muttoharoh",
                  "nim": "123450021",
                  "umur": "20",
                  "asal": "Lampung Barat",
                  "alamat": "Sukarame",
                  "hobbi": "Main-main",
                  "sosmed": "@khoirulmuttoharoh",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Lutfia Aisyah Putri",
                  "nim": "123450074",
                  "umur": "17",
                  "asal": "Swiss",
                  "alamat": "Pemda",
                  "hobbi": "Nyari dataset",
                  "sosmed": "@lutfiaisyh",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Nabyla Sharfina",
                  "nim": "123450008",
                  "umur": "19",
                  "asal": "Bengkulu",
                  "alamat": "Jalan Lapas Raya",
                  "hobbi": "Jalan-jalan",
                  "sosmed": "@bylaash",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Syahrialdi Rachim Akbar",
                  "nim": "123450093",
                  "umur": "20",
                  "asal": "Lampung",
                  "alamat": "B. Lampung",
                  "hobbi": "Baca",
                  "sosmed": "@syahrialdi_rchm",
                  "kesan": "-",
                  "pesan": "-"
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
                  "pesan": "-"
                },
                {
                  "nama": "Cindy Laura Manik",
                  "nim": "123450112",
                  "umur": "20",
                  "asal": "Sumatera Utara",
                  "alamat": "Belwis",
                  "hobbi": "Beli risol ayam Naya",
                  "sosmed": "@cindylauura",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Dea Amanda",
                  "nim": "123450006",
                  "umur": "21",
                  "asal": "Sumatera Barat",
                  "alamat": "Korpri",
                  "hobbi": "Nonton reels Agz",
                  "sosmed": "@deaamnd3_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Desman Velius Halawa",
                  "nim": "123450114",
                  "umur": "21",
                  "asal": "Nias",
                  "alamat": "Asrama TB 3",
                  "hobbi": "Bermusik",
                  "sosmed": "@dsmannhal_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Devyna Sonya Palupi Sanjaya",
                  "nim": "123450007",
                  "umur": "20",
                  "asal": "Pringsewu",
                  "alamat": "Like crowded",
                  "hobbi": "Gibah sama Lulu",
                  "sosmed": "@devynasonyaa",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Luthfia Laila Ramadhani",
                  "nim": "123450004",
                  "umur": "19",
                  "asal": "Tambun",
                  "alamat": "Jl. Raden Saleh",
                  "hobbi": "Nyubitin Ketang",
                  "sosmed": "@Luthfiaarmdhni",
                  "kesan": "-",
                  "pesan": "-"
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
                  "pesan": "-"
                },
                {
                  "nama": "Aditya Taufiqurrohman",
                  "nim": "123450032",
                  "umur": "21",
                  "asal": "Sukabumi",
                  "alamat": "Belwis",
                  "hobbi": "Open the new map",
                  "sosmed": "@Ty_Tq90",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Fathya Intami Gusda",
                  "nim": "123450095",
                  "umur": "19",
                  "asal": "Tangerang Selatan",
                  "alamat": "Sukarame",
                  "hobbi": "Minta tolong Adit",
                  "sosmed": "@fatthyaa_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Nayla Shafira Roza",
                  "nim": "123450017",
                  "umur": "20",
                  "asal": "Bandar Lampung",
                  "alamat": "Kedamaian",
                  "hobbi": "Me time",
                  "sosmed": "@n.shafirarz",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Melinza Nabila",
                  "nim": "123450122",
                  "umur": "20",
                  "asal": "Bandar Lampung",
                  "alamat": "Kedamaian",
                  "hobbi": "Menonton film",
                  "sosmed": "@melynznb",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Khazanatil Ilmi",
                  "nim": "123450053",
                  "umur": "20",
                  "asal": "Padang",
                  "alamat": "Korpri Raya",
                  "hobbi": "Nonton",
                  "sosmed": "@khazanatil_ilmi05",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Nurul Izzah Istiqomah",
                  "nim": "123450054",
                  "umur": "20",
                  "asal": "Batam",
                  "alamat": "Gang Nalim",
                  "hobbi": "Baking",
                  "sosmed": "@izzah_tq",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Qois Olifio",
                  "nim": "123450067",
                  "umur": "21",
                  "asal": "Batam, Kepri",
                  "alamat": "Gang Sakum",
                  "hobbi": "Ngabisin bensin",
                  "sosmed": "@qoisolifio_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Tarisya Hidayatul Rahmi",
                  "nim": "123450052",
                  "umur": "21",
                  "asal": "Sumatera Barat",
                  "alamat": "Korpri",
                  "hobbi": "Jelajahi desa Lamsel",
                  "sosmed": "@tari_sya23",
                  "kesan": "-",
                  "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1QInbkW2T_-8-b7_z8Cl-40j3-Slslgxa",
            "https://drive.google.com/uc?export=view&id=1Xxweg051d6Gsakf6KuZVrrF8Qp6GasXn",
            "https://drive.google.com/uc?export=view&id=1RxjMmYb1zGcXVMiEM9BmrnhJVJcBu57T",
            "https://drive.google.com/uc?export=view&id=18VRdCVxsXmr-nfVw7lF1Rhmjnq_Sr9jn",
            "https://drive.google.com/uc?export=view&id=1muSLV-t9Tt4qxC-O2gWIucgP2rm5hb7H",
            "https://drive.google.com/uc?export=view&id=1nLUXqCha47MbSJu2N3QclQf09ff0eLxm",
            "https://drive.google.com/uc?export=view&id=17-jEJTuZOBG6FgC9DB-wYpbpqiuvhqV9",
            "https://drive.google.com/uc?export=view&id=1qk4Z1tVKmD_ZUlBgLMIz2ZXuadUrI8Vc",
            "https://drive.google.com/uc?export=view&id=1pyetGcRborBlDX1RQQxWlQvjedJpfhbM",
            "https://drive.google.com/uc?export=view&id=1uuNBsFqsMyDl0zgsI5OdElYQi-QqQBwG",
            "https://drive.google.com/uc?export=view&id=105ATz5AQb2WqYFKvKEAe0_6zoi8HIYVV",
            "https://drive.google.com/uc?export=view&id=1JfdS5LOQ6sP5xPvxIN4yo1kb0eP2AqSK",
            "https://drive.google.com/uc?export=view&id=1pB6kYGmPhp4Xw5oX0u3fwgOd5jUjACL-",
            "https://drive.google.com/uc?export=view&id=1YpIobniIfApCDsjRnGJS0bLQyDroj6rT",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azza.rrr_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "18",
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": "-",
                "pesan": "-"
            },
             {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": "-",
                "pesan": "-"
            },
             {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "-",
                "pesan": "-!"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwsti",
                "kesan": "K-",
                "pesan": "-"
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": "-",  
                "pesan":"-"# 1
            },
     
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                  "nim": "122450085",
                  "umur": "22",
                  "asal": "Bandar Lampung",
                  "alamat": "Belakang PB",
                  "hobbi": "Jogging",
                  "sosmed": "@dananghk_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Syalaisha Andina Putriansyah",
                  "nim": "122450021",
                  "umur": "22",
                  "asal": "Tangerang",
                  "alamat": "Sukarame",
                  "hobbi": "Baca novel",
                  "sosmed": "@syalaishaa_31",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Ahmad Rizqi",
                  "nim": "122450138",
                  "umur": "20",
                  "asal": "Padang",
                  "alamat": "Airan",
                  "hobbi": "Beli parfum",
                  "sosmed": "@den_iki_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Anadia Carana",
                  "nim": "123450019",
                  "umur": "20",
                  "asal": "Palembang",
                  "alamat": "Lampung Selatan",
                  "hobbi": "Jogging",
                  "sosmed": "@anadiacrn_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Aprilia Dewi Hutapea",
                  "nim": "123450040",
                  "umur": "20",
                  "asal": "Lampung Selatan",
                  "alamat": "Lampung Selatan",
                  "hobbi": "nonton dramashort di fb",
                  "sosmed": "@aprhtp_",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Nabila Zakiyah Zahra",
                  "nim": "122450139",
                  "umur": "21",
                  "asal": "Bandar Lampung",
                  "alamat": "Way halim",
                  "hobbi": "jogging",
                  "sosmed": "@nabila_zazahra",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Dhafin Razaqa Luthfi",
                  "nim": "122450133",
                  "umur": "21",
                  "asal": "Bandar Lampung",
                  "alamat": "Sukarame",
                  "hobbi": "Belajar",
                  "sosmed": "@dhafinrzqa13",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Devi Rahayu",
                  "nim": "123450010",
                  "umur": "20",
                  "asal": "Bandar Lampung",
                  "alamat": "Way kandis",
                  "hobbi": "nonton drakor",
                  "sosmed": "@deviirhyu",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Enggli Rahmadhani",
                  "nim": "123450043",
                  "umur": "20",
                  "asal": "Sumatera Barat",
                  "alamat": "gg.perwira 2",
                  "hobbi": "nonton alur cerita",
                  "sosmed": "@englirahmdhanii",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Hanifah Inaya Sani",
                  "nim": "123450123",
                  "umur": "20",
                  "asal": "Bandar Lampung",
                  "alamat": "Korpri",
                  "hobbi": "Masak",
                  "sosmed": "@_inayasari",
                  "kesan": "-",
                  "pesan": "-"
                },
                {
                  "nama": "Nydia Manda Putri",
                  "nim": "123450018",
                  "umur": "20",
                  "asal": "Bandar Lampung",
                  "alamat": "Tanjung karang",
                  "hobbi": "Main",
                  "sosmed": "@nydiaaptr_",
                  "kesan": "-",
                  "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
    
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
             "https://drive.google.com/uc?export=view&id=10qGqjz-9dIAo9cFjmdKUGlAv7Gtcfc7Q",
            "https://drive.google.com/uc?export=view&id=1p0YJBniDrUlHmKZWOY_q4iU2frTUzm2j",
            "https://drive.google.com/uc?export=view&id=1ipH_PRzWGObIquk6pLe0cFXtwg7Ttqos",
            "https://drive.google.com/uc?export=view&id=1hQ76VSqnb35CGn-Gac2qNdFMQEiyFui8",
            "https://drive.google.com/uc?export=view&id=1YsDJTRWBUNcHDPmqBJpZekXXaOmXMgUi",
            "https://drive.google.com/uc?export=view&id=1g3lXgG2urY4F64-o13yt2bkkakN6QIWP",
            "https://drive.google.com/uc?export=view&id=1_sqmb_ia3jAfZE4JE7dhFqgQYTAoIEPt",
            "https://drive.google.com/uc?export=view&id=1LnMTMgelYsDjSWTKQ5jK0JqmmicCv9Op",
            "https://drive.google.com/uc?export=view&id=1cCoGpLMfagA8OUQmqZsnDJ6dHXF-1g0F",
            "https://drive.google.com/uc?export=view&id=1DH5WoOADghL8fZUxA6MiZVmrBpREZc1b", 
            "https://drive.google.com/uc?export=view&id=1RfLYeNC78rjdVw3Pn7GrKN9TvyRN0Xry",
            "https://drive.google.com/uc?export=view&id=1u-PIXk62VWHImK8wLMOian9x37Cd_Iw_",
            "https://drive.google.com/uc?export=view&id=1lzHc861QpXjUYi7Tr4610pUzFl4wAFyG",
            "https://drive.google.com/uc?export=view&id=1mIvTZXGe67bfZ_RgzWCC2zTfCCYM1ZHI",
            "https://drive.google.com/uc?export=view&id=1teoKjnaH5BWAZAvwX6VeKdRfbqa-_WTp",
            "https://drive.google.com/uc?export=view&id=1b6LW-ukMHgPTNCimjI3tBeWdvBpydJIM",
            "https://drive.google.com/uc?export=view&id=1iJ-e2j53-ikVWPQA2vBeKeTk_b5IMEId",
            "https://drive.google.com/uc?export=view&id=1_a_gShJ3nqTiZxYHbXD4GyufUXTV_OXy",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "jl.Kresna, korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way huwi",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kota bumi, Lampung utara",
                "alamat": "jl.pangeran senopati raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaamara",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donamaya.p",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuan ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumatera barat",
                "alamat": "jl.Lapas, kec.Jati Agung",
                "hobbi": "mendengarkan musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main hp",
                "sosmed": "@i",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan raya 1",
                "hobbi": "membaca, menulis, memasak",
                "sosmed": "@nltg._",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "",
                "pesan": "!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "",
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

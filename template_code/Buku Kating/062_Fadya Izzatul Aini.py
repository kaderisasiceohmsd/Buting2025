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
            "https://drive.google.com/uc?export=view&id=1AzeiVtl4rvlK9sBzrdFvLijKl0PPn15b",
            "https://drive.google.com/uc?export=view&id=1YILA8Ut8mJUNQj8sUP8sz8PCv2JKYS7w",
            "https://drive.google.com/uc?export=view&id=1i7slmf4-hrrND6_UECKwytzpKfaHdwnH",
            "https://drive.google.com/uc?export=view&id=1wboeoZ89ayhPnQoLecWWtbaMxQ1tBgVK",
            "https://drive.google.com/uc?export=view&id=17kRkp2xCjQELIZx2KzEnkAKn2bHL8P7E",
            "https://drive.google.com/uc?export=view&id=1BJn3iRQhaixFVrnZR_58F_moLPIX03X4",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli dona kentang",
                "sosmed": "@_erendraa",
                "kesan": "Kaget ternyata suara bang rendra persis kaya juicy luicy waktu FG",  
                "pesan":"Semoga semakin keren kedepannya bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Awal liat bang Jo kaya serem",  
                "pesan":"Sukses terus kedepannya bang"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy dalem",
                "alamat": "Ayres kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh_",
                "kesan": "Seru banget kak abet lucuu!",  
                "pesan":"Makasih udah jadi orang lucu kak!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya keliatan kalem tapi anggun banget!",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "Awal liat kakaknya kaya galak, tapi ternyata asik",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Gya Kost Korpri",
                "hobbi": "Cute Jenderal",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak cantik banget",  
                "pesan":"Tips cantiknya dong kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1paE6lqTk1PRTGJtRx9rcPo-Rbq2m_GYI",
            "https://drive.google.com/uc?export=view&id=1DRXox8aXDga8soQQ-nIgnyEViLHt7xjO",
            "https://drive.google.com/uc?export=view&id=1uA6r27yFrmd2Md_kIGC5ylaDRV5yUqKg",
            "https://drive.google.com/uc?export=view&id=1Ui7byH68LMruM44rHHcDyH47wHaKZRBa",
            "https://drive.google.com/uc?export=view&id=1vBN020_JwAuFr-wEj1Tbh9i2jeNdO-C2",
            "https://drive.google.com/uc?export=view&id=1wqycwR9qNo6WIfwXf6Hg77YJWsiSfK-X",
            "https://drive.google.com/uc?export=view&id=178JS1YVbWKYvSY6gBs5u9X05BlQMGTEq",
            "https://drive.google.com/uc?export=view&id=19OFrMs9jDegXS86I5GQewzJRfs5MCrGL",
            "https://drive.google.com/uc?export=view&id=1x6VCp0stjnK1-mCeRz4x3SGnHksd9bCy",
            "https://drive.google.com/uc?export=view&id=10aa45v9xE3lz7sGQtdJJvBdaYY6K9LNw",
            "https://drive.google.com/uc?export=view&id=1z1QaNyBzJVRkaLyHTP5eKiSES-178KHo",
            "https://drive.google.com/uc?export=view&id=1flJrz8VH_1GrTSY1lLlenGcXq-rjkt_a",
            "https://drive.google.com/uc?export=view&id=15SLwaJuilDHc37GXebuhQlLQ2wl-yJiz",
            "https://drive.google.com/uc?export=view&id=1zAceYcYSfMzjp19Etz2SVzAWl4Fngzv0",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "12250022",
                "umur": "21",
                "asal":"Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "Nontonin orang kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "Asik banget bisa belajar dari abang",  
                "pesan":"Semoga selalu bermanfaat untuk sekitar"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "Lomba ga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Ternyata sama-sama gasuka makan ikan karna gamau ribet",  
                "pesan":"Semoga kita nemuin ikan tannpa duri yang enak ya kak"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Tidur",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya lucu banget malu-malu",  
                "pesan":"Semangat terus kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Ubud",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan baru",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semoga terus jadi energi positif"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "Abangnya seru dan bikin suasana rame",  
                "pesan":"Tips untuk jadi asiknya kak"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya ramah dan peduli",  
                "pesan":"Tetap semangat di organisasi dan kuliah ya kak!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "Abangnya humble banget",  
                "pesan":"Tetap semangat ya bang!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya keren banget",  
                "pesan":"Semangat ngerawat kucingnya bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya ramah banget",  
                "pesan":"Tips nyanyi dong kak"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya positive vibes banget, lucu juga",  
                "pesan":"Semangat kuliahnya kak jue"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Gh",
                "hobbi": "Main padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Kakaknya asik banget",  
                "pesan":"Sukses terus bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "Koleksi bath google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "Keren abangnya suka koleksi google cloud",  
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya seru banget ternyata hobinya sama-sama main ML",  
                "pesan":"Tutorial jago franco nya dong kak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Kota Tarakah",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lucu banget",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Wr8xUDJzxsYhQQxPtrx2So4l7O3fbJIh",
            "https://drive.google.com/uc?export=view&id=1tMzoaxJg1XULdI3eoCFJHWsayA86GoMC",
            "https://drive.google.com/uc?export=view&id=18VSbSmxOlbtjz17n8V1_CvHs2ir2AUjI",
            "https://drive.google.com/uc?export=view&id=1siqRqCEsYOBjiRo1LfOO0BMs1BAYoGa-",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Dengar lagu, nyanyi, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kaget ternyata suara bang rendra persis kaya juicy luicy waktu FG",  
                "pesan":"Semoga semakin keren kedepannya bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Awal liat bang Jo kaya serem",  
                "pesan":"Sukses terus kedepannya bang"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main ice skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "Seru banget kak abet lucuu!",  
                "pesan":"Makasih udah jadi orang lucu kak!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomart Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya keliatan kalem tapi anggun banget!",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11InFfSyhx79U4PVAl5jOaehFlTDhWVfb",
            "https://drive.google.com/uc?export=view&id=10D9fH65ADWQ7o5S9eYmVmbP8gRohcLKF",
            "https://drive.google.com/uc?export=view&id=1sD1_AKeAOvkItbfgZGXDhkbxK67vNuud",
            "https://drive.google.com/uc?export=view&id=1poKTs__iOpF_Hui4sfPsJoKgWyBcxORI",
            "https://drive.google.com/uc?export=view&id=1jhBNGqOyA27Ep-KDbVozV8ni_ptSP8Xp",
            "https://drive.google.com/uc?export=view&id=1_djgPqNFtwl9-5l3bn_Qx0CzHNhDe_S0",
            "https://drive.google.com/uc?export=view&id=1rlvpfWQ39rTbgOIShKzwPVMqOY7psVM9",
            "https://drive.google.com/uc?export=view&id=1aUZqq1l99d7loZh78W0jopp1yiXOP875",
            "https://drive.google.com/uc?export=view&id=1dvyhEZmAmETF_0dseV_hLliSxDbY_Boy",
            "https://drive.google.com/uc?export=view&id=14ANPmm6BLUT7yO_9iA91wqq2foLbTZ5P",
            "https://drive.google.com/uc?export=view&id=1yQ6O9kvvM1_iTCopetF9pzlNgi8IhJwP",
            "https://drive.google.com/uc?export=view&id=13ajqmjLLh9wzllnAYOgkHdo5sABuFYqR",
            "https://drive.google.com/uc?export=view&id=114lsgwTs_0jsWA9Qh50jOCqM4eHZwd8j",
            "https://drive.google.com/uc?export=view&id=1E7M11nynotJwlwBaoFtHwbqlFdxaIsZ8",
            "https://drive.google.com/uc?export=view&id=11dOkxEolKuiziGcNv0TnwivLq2hvul84",
            "https://drive.google.com/uc?export=view&id=1dy9OR1HH4DnnlL_hL5GBKzRFzX2ygJDS",
            "https://drive.google.com/uc?export=view&id=1O6l2NOmQBio49mz66mQydeBJfPT1mp2i",
            "https://drive.google.com/uc?export=view&id=1aQAcLRxH7n1E1BlKgvCKVdN8ycAGJP53",
            "https://drive.google.com/uc?export=view&id=1V4SrV1ePIO2egHqFs8oXUzrkwJr7hbpg",
            "https://drive.google.com/uc?export=view&id=1CX0IzYa8NNIX7ac2vfbxKy9LnycmaDyA",
            "https://drive.google.com/uc?export=view&id=1SrWUVIUdXVWLdWVu45LSknz8v6ne-QLM",
            "https://drive.google.com/uc?export=view&id=1np1hweUafd_PLVkgJESMnhmTBJlRuYWC",
            "https://drive.google.com/uc?export=view&id=1NFes1MM-V-qBw3N2TjgvMFpQrFYzIzZS",
            "https://drive.google.com/uc?export=view&id=1xHL1iP-Lo8hogkERtBE2WBTUn_MBO3bR",
            "https://drive.google.com/uc?export=view&id=1sVkiTbWDPoThmrQyeB2W_D4vybl7p1PZ",
            "https://drive.google.com/uc?export=view&id=1AzXtnahP1NCFJAD2x9JUS0HRXI5EMVb_",
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
                "kesan": "",  
                "pesan":""# 1
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
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UT9g0ZJ6e0ADgVKmG5J55OzueJmKDTnP",
            "https://drive.google.com/uc?export=view&id=1KeQgznPyUmOm9yEQQr6hcwcCrOesKISA",
            "https://drive.google.com/uc?export=view&id=18jaQwcuuNz74AnWmPKoSPdZsu_RgUJVx",
            "https://drive.google.com/uc?export=view&id=1XJTl4TVByGnX-qc8n9uEnMJfQQjFYl6O",
            "https://drive.google.com/uc?export=view&id=16JUbCPAHo2cnnKjOl91PUBC30LwCXTyg",
            "https://drive.google.com/uc?export=view&id=11nlnl8i_M5wLuhGGUd5FpVzd7oUXQdgl",
            "https://drive.google.com/uc?export=view&id=15diYaxAkWDtNa0eIUGIwEu46LB23RLyb",
            "https://drive.google.com/uc?export=view&id=1Hi_iVNNwsPVydy1yE0ReAIVYjh0tkyOO",
            "https://drive.google.com/uc?export=view&id=1MpXR_lGGfw-ecSDfXv9bANL3ICjMxqOC",
            "https://drive.google.com/uc?export=view&id=1AKmtrnfLwFsR6p_OdtIQDqIPrkKi11yQ",
            "https://drive.google.com/uc?export=view&id=1rVa7V2xZe-CQ2CZdI-R7Cf-YqTMkSAWo",
            "https://drive.google.com/uc?export=view&id=18y2xOY7KOjdtd4q_s7Q2AkiKywIMICqt",
            "https://drive.google.com/uc?export=view&id=1bZOdERsXAqOM-PWF4Zi-W591Wk0HTn8C",
            "https://drive.google.com/uc?export=view&id=1VlBaUdPPEzIwbAE4Bvj8wDJrLGE1Nc9J",
            "https://drive.google.com/uc?export=view&id=1O_Zb6WwAMXTGGwfjlK2-fgPJparPQahL",
            "https://drive.google.com/uc?export=view&id=19sZVd2IgAcZb8VDDzt0GGgPdos2jU1pi",
            "https://drive.google.com/uc?export=view&id=1kJK_eTjTpwNtQJzdQge-cgZ9BZJ1eDkL",
            "https://drive.google.com/uc?export=view&id=1JlQlRZIZz0iLvxaGG5c6W-KYuX2XdFQy",
            "https://drive.google.com/uc?export=view&id=17N8vztHDP2ZS3CMbMJ50gObGMHmEZhY4",
            "https://drive.google.com/uc?export=view&id=1o8Q0JO3yJmz_0Eqc3Vd075c0pwQMnpzF",
            "https://drive.google.com/uc?export=view&id=1xKHXPThab99GBAMLzDesOfjsv3QHBI-R",
            "https://drive.google.com/uc?export=view&id=1thcXa4wKTobEWZw7i6M2GJTBqCmyNAOW",
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
    
# Tambahkan menu lainnya sesuai kebutuhan





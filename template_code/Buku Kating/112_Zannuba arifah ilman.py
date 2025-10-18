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
            "https://drive.google.com/uc?export=view&id=1zB922JL0a6sDLnyn6umxK5ums-w64Tvf",
            "https://drive.google.com/uc?export=view&id=1F30JiHkBq5-Yl1fuu8Olhetaw-YOjR3m",
            "https://drive.google.com/uc?export=view&id=1x84rTwL2J_ey7ceBb7XEMUZpuu7wjWVy",
            "https://drive.google.com/uc?export=view&id=1p97BZLsbMy64f8jRYXKKj5TCbFZHa7T-",
            "https://drive.google.com/uc?export=view&id=11FSht2R1pIQdd7x9iHv7zsIjAJXx0yaV",
            "https://drive.google.com/uc?export=view&id=1l9nAafVWnigsdhxJNykfKFig5exIg-vz",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Pulau Damar",
                "sosmed": "@_rendraa",
                "kesan": "keren banget bangg",  
                "pesan":"semangat terus kuliahnya Abang nim kuu !!!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerangi",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "wooww keren banggg",  
                "pesan":"semangat kuliahnya bang!!!"
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "asik + seru  banget diajak ngobrol !",
                "pesan": "Jangan lupa istirahat dan tetap semangat ya kakaakk!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "vibes nya tenang bangeett kaakkk!",
                "pesan": "Tetap semangat kaakkk!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "lucuu bangeett kak eksantyy!",
                "pesan": "semangaat kuliahnya kak!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "seruuu banget!",
                "pesan": "Semangat terus kuliahnya kakk!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1L4HxwAmb4enH605R6JJSwPcxb4a_4sVg",
            "https://drive.google.com/uc?export=view&id=1PX2L35T9stU63JXqgkjlEWILWoTPtX0S",
            "https://drive.google.com/uc?export=view&id=1V9YWe61012iEPlSDpMJyr9ZL2k3fTa3D",
            "https://drive.google.com/uc?export=view&id=1IpYPwE3RiN0Hz4Fn9RPmADJDAsHL7YQy",
            "https://drive.google.com/uc?export=view&id=1TasNwAMAZf8tbMYa8rA2zxN6Ut4rdWpJ",
            "https://drive.google.com/uc?export=view&id=1k7SdR1FXNDht4E3vnvJIBfpHZXBnC-AG",
            "https://drive.google.com/uc?export=view&id=1_GzbbEvZcw8bisKW6NTFAyvKew1Dk41F",
            "https://drive.google.com/uc?export=view&id=13Y_Ab47zJKRpsDVBQUyW3klc-KK1HS_g",
            "https://drive.google.com/uc?export=view&id=1pqNmcEShMqsmF1R9z-pk9uwb2z-OLSx9",
            "https://drive.google.com/uc?export=view&id=1Ta-huQAZg36fM6nn3UNd76FlmkbaZmyx",
            "https://drive.google.com/uc?export=view&id=1aOOyLLZboMb92EqM9jhhPiwgDXTidwx6",
            "https://drive.google.com/uc?export=view&id=1XOmVMY5tlGhL2Ne-DRgBGhs-3qCxHYOz",
            "https://drive.google.com/uc?export=view&id=1cR4Khq-QcWCylVdDq9QoV92ZtJUBqxEn",
            "https://drive.google.com/uc?export=view&id=1rjyJppTntvLeN0-SpQDV-RZ0TkzVJ9EZ",
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
                "kesan": "orangnya seru banget!",
                "pesan": "Semangat terus kuliahnya Bang, sukses selalu!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "lucu banget kak dhea!",
                "pesan": "Tetap semangat ya kak Dhea!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha selalu ceriaf banget!",
                "pesan": "Terus tebarkan semangat positifnya kak Renisha!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "asik banget kak Anisa!",
                "pesan": "Semangat terus kuliahnya kak Anisa!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Bang Dharu santai tapi rajin pluss aktif bangett banget!",
                "pesan": "Tetap semangat terus Bang!"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "Kak Feby seru banget!",
                "pesan": "Terus ceria dan semangat terus ya kak Feby!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro kalem dan seru!",
                "pesan": "semangat kuliahnya Bang!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan pecinta kuliner sejati !",
                "pesan": "semangat teruss bang !"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kak Berliana unik banget dan punya hobi yang lucuu!",
                "pesan": "Terus semangaatt ya kak Berliana!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kak Juesi cantiikk bangettt!",
                "pesan": "Semangat terus ya kak Juesi!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho keren banget!",
                "pesan": "Semangat terus ya Bang Ridho!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Bang Feryadi lucu dan suka bercanda!",
                "pesan": "semangaatt bangg!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica seruu bangeet!",
                "pesan": "Semangat terus kak Monica!"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa kalem banget auranya kak,sukaa banget liatnyaa!",
                "pesan": "Tetap semangaatt kak Nashwa!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Dkl0IdGBMkq9C-73NNveU7VKPtUsLmKL", 
            "https://drive.google.com/uc?export=view&id=1pwPDVVJzMmaamTWjSDUqbVuqbcdUvhHw", 
            "https://drive.google.com/uc?export=view&id=19udtqUdfwKfKB_bS6MMdDDbM9RL-Izlv", 
            "https://drive.google.com/uc?export=view&id=1ryZ6ZCGWX7OB2XbrlOIvlEPglWrbMJFx", 
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
                "kesan": "Bang Bintang pinter bangett bang!",
                "pesan": "Semangat belajarnya Bang!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kak Nadya santai tp seruu!",
                "pesan": "Semangaatt kuliahnyaa kaakk!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah lucu banget!",
                "pesan": "Tetap semangaatt ya kak!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Lia seeruu banget!",
                "pesan": "Semangat terus kuliahnya kak Lia,!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1N44ytCf_zDOM--Zxnr6dN_aPKIZzDvVt",
            "https://drive.google.com/uc?export=view&id=1J9JLMxUrWqRYi9m_fw3vNCqSmLMM1z3j",
            "https://drive.google.com/uc?export=view&id=1aoV2eCJiPqKqOzGuy-u3Gyt8yFQi2lTl",
            "https://drive.google.com/uc?export=view&id=14dHavsZcLVxCdmjHUQznMEtaLlbt8baE",
            "https://drive.google.com/uc?export=view&id=1lvWFNsBc_Zg1g9KiD-lh3OtjgirRN0TZ",
            "https://drive.google.com/uc?export=view&id=1k4bWEO8W8EtWDrfHMwwetcOLcsQtosA9",
            "https://drive.google.com/uc?export=view&id=1nKg9oRhQ-aM7jytagHCuC-eCuRFCDr-y",
            "https://drive.google.com/uc?export=view&id=1ILVQk5D4ll00YL0m89lv3vMwVRHKzDov",
            "https://drive.google.com/uc?export=view&id=10zK--9cLgM8hCe6ajN06HPFnbnECfDxU",
            "https://drive.google.com/uc?export=view&id=1trW_QDvdx2CP41JDuhJypAPDp1ETRgBw",
            "https://drive.google.com/uc?export=view&id=1mNw6RZuF3DawasD5jM3jOH-UMOinamWa",
            "https://drive.google.com/uc?export=view&id=1zoExijYP0W_KKjnwOIu93Tdq8LR9x4bt",
            "https://drive.google.com/uc?export=view&id=1N7O4d6XEkRwUT9WJ8KJFz_O9ctw_GMrQ",
            "https://drive.google.com/uc?export=view&id=1FoGEn1wqN_mpZVEB6BlAjwE7IYxFZxqn",
            "https://drive.google.com/uc?export=view&id=1_fm-uphDc3LS3ugt8R_gbnMKb8Pbzjzt",
            "https://drive.google.com/uc?export=view&id=16lNK2ZW6Mq0QPlh65UHlqFSxqycTZ_03",
            "https://drive.google.com/uc?export=view&id=1rNXmJwrICuxDqQt3V7-a0Z7-DV2feZN3",
            "https://drive.google.com/uc?export=view&id=13A4gV9DJYf6a3uEpdON9mRCrIUiZs2RA",
            "https://drive.google.com/uc?export=view&id=1oHHcvm_XY2SlEWxpeWTXfTQ5NA1I2U2J",
            "https://drive.google.com/uc?export=view&id=1Vd3bcARgkehKYsmmnD9JyWfk2WXjMQTw",
            "https://drive.google.com/uc?export=view&id=1h71tEpRnrwJbxi2qnp3xWA2ky7XlSOc8",
            "https://drive.google.com/uc?export=view&id=1UpUTeaTwkJEe2BnU2MhjCBfF-vPs58MW",
            "https://drive.google.com/uc?export=view&id=12z2lcCUAyBhPDyCsIslzVYlUwwOkjmMr",
            "https://drive.google.com/uc?export=view&id=1uS1g2yjb-5m-BSNkHjgIxPodTu9toDhh",
            "https://drive.google.com/uc?export=view&id=14mf47nK89udbaBAzJ3JoVRyuajsoFvCl",
            "https://drive.google.com/uc?export=view&id=1mFgX1XNnJvY7X8mkjEDMDJWkwUufF_fC",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@afifahhnsrn",
                "kesan": "cantiikk kak,suka liatnyaaa",  
                "pesan":"semangat truusss kak"# 1
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@allyapasha_",
                "kesan": "kereenn kak allyaaa",  
                "pesan":"semangaattt kak"# 1
            },
              {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ahmad.rizky__",
                "kesan": "kereenn bang",  
                "pesan":"semangaatt truuss banggg"# 1
            },
           {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@arientakhsnl_",
                "kesan": "kereenn kak ",  
                "pesan":"semangaatt kuliahnyaa kakk"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@daffahdynn_",
                "kesan": "kereenn bangg",  
                "pesan":"pliss tips ngerawat rambut nya bangg hehehe"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": ": @ginda_mrp",
                "kesan": "bang fajarr kerenn",  
                "pesan":"semangaatt teruuss bangg"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "suka liat kak natasya,gx ngebosenin soalnyaa",  
                "pesan":"semangaatt truuss kakk"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@nobelnizam",
                "kesan": "kereenn banggg",  
                "pesan":"semangaatt truuss kuliahnyaa bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ji_gumel17",
                "kesan": "kereenn banggg",  
                "pesan":"semangaattt truuuss banggg"# 1
            },
            {
                "nama": "vany salsabila putri",
                "nim": "123450022",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kerenn kak",  
                "pesan":"semangaatt kuliahnya kakk"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@shahid22_",
                "kesan": "asik bangg",  
                "pesan":"sukses selalu bangg"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ali_parisi3",
                "kesan": "keren bang",  
                "pesan":"semangat dan sukses selalu bang "# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@feraztaaa",
                "kesan": "kereenn kak",  
                "pesan":"semangaatt truuuss kakk"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": " 123450034",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@rismaa.mustika_",
                "kesan": "vibesnya kaleemmm",  
                "pesan":"semangat truss kak"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@rosaliasiregar",
                "kesan": "baiikk bangeettt kaakk",  
                "pesan":"semangaatt kuliahnya kakakk"# 1
            },
            {
                "nama": "Sahid Maulana",
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
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ahmadnoval_11",
                "kesan": "baik bangeett bangg",  
                "pesan":"semangaatt kuliahnya bangg"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@d__aniar",
                "kesan": "baiikk bangeett kakk",  
                "pesan":"semangaatt kuliahnya kakk"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ihsan.yusuf",
                "kesan": "baikk bangeet bang ihsann",  
                "pesan":"semangaatt truuss bang kuliahnyaa"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": " 123450109",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@kevinaj_",
                "kesan": "kereenn banggg",  
                "pesan":"semangaatt kuliahnya bangg"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@dla_natzzyaa",
                "kesan": "baiik bangeet kak",  
                "pesan":"semangaatt kuliahnya kak lidiaaa"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ridwan122",
                "kesan": "baiikk bangeet bang",  
                "pesan":"semangaatt kuliahnyaa bangg"# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ullianowlm",
                "kesan": "kereenn bangg",  
                "pesan":"semangaat kuliahnya bangg"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@sidabutar.26",
                "kesan": "baiikk bangeett bangg",  
                "pesan":"semangaatt kuliahnya bang"# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@rewinanaaa",
                "kesan": "baiik bangeet kak rewinaa",  
                "pesan":"semangatt kuliahnyaa kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RslUNDAIYZxI1nunkqT8YzXSF2zZNgWx",
            "https://drive.google.com/uc?export=view&id=1TSFlbWlPru8D2vkMvWgNASKkpsnmHXva",
            "https://drive.google.com/uc?export=view&id=1t-XJm1EyJI-fg11vo50hpFWGIPn7QJpQ",
            "https://drive.google.com/uc?export=view&id=10glnGnlv8E2Ae3i2QWRfuFrPREnAYGxY",
            "https://drive.google.com/uc?export=view&id=1GwTzNObivMHaqISaCMTFEvTlLjwkqV2z",
            "https://drive.google.com/uc?export=view&id=133g7gMBWuY_CvpPQltLJho9kDATUYEaG",
            "https://drive.google.com/uc?export=view&id=1Tv9Gp4DpZ_2eiLylbS8fpmTW12MZKi7C",
            "https://drive.google.com/uc?export=view&id=1GxuQpVhqk_vxQNd4FA4o5jLgrJzC-sKQ",
            "https://drive.google.com/uc?export=view&id=1VYkjA5SkhM9GbBK2vxomG_O0WFXEFZfz",
            "https://drive.google.com/uc?export=view&id=1OK_zDQIpLKr5_4HwT-9aCxr0NureRkSt",
            "https://drive.google.com/uc?export=view&id=1QZJkj1w2Utup6ppZXQvc-PJmDBMil4xH",
            "https://drive.google.com/uc?export=view&id=1Z9fHcHaGt5cywbdsS23jWeQXA1S4inuA",
            "https://drive.google.com/uc?export=view&id=1rIJDbhOItNgET8O_cdCu9OXK4-MTKvni",
            "https://drive.google.com/uc?export=view&id=1N3GKBZymd962xgL4N8nt8EBs5d7q1giN",
            "https://drive.google.com/uc?export=view&id=1bG2AwuGGLmjrffHUrsFZolwWYFxttDeT",
            "https://drive.google.com/uc?export=view&id=1UZRdCyvgk_X43bQPxKpvvAB030Mt0mGo",
            "https://drive.google.com/uc?export=view&id=1vDp0TDodK1z--OuOjXvbht4kp9XRs0xH",
            "https://drive.google.com/uc?export=view&id=1hxduKzL3rKjkKLrYn6z7j0T6PTJmFU4H",
            "https://drive.google.com/uc?export=view&id=1UOjVXskTQMpwhSLPvgbgfMVpJaPMk4uC",
            "https://drive.google.com/uc?export=view&id=1Ai9FabxsBP6Hz-Dpj6LdBjSoq-GSjWQO",
            "https://drive.google.com/uc?export=view&id=1cusHRr0lJtlmFjylOcO2nGLwORiS10ZQ",
            "https://drive.google.com/uc?export=view&id=1ck4Hj0mfeM9HqNORB0l4ODXjZcuhFz0f",
        ]
        data_list = [
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@randaadriana_",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@Junitaa.0406",
                "kesan": "baik bangeett kak",
                "pesan":"Semangaatt kuliahnya kak!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@mregiiii_",
                "kesan": "kereenn bangg",
                "pesan":"semangaatt kuliahnya bangg"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
               "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya asik dan seru bangeett",
                "pesan":"Semangat terus kuliahnya ya, Kak!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
               "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@fadilalfarizzi",
                "kesan": "bang fadiill kereenn.",
                "pesan":"Semangaatt kuliahnya bangg"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
               "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@muhammadqil1111",
                "kesan": "baiikk bangeett bangg",
                "pesan":"semangaatt kuliahnya bangg!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@notfall.s",
                "kesan": "baiikk bangett bangg",  
                "pesan":"semangat terus kuliahnya bangg !!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
               "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@adiaafrj",
                "kesan": "Kereenn kakkk",
                "pesan":"Semangat terus kuliahnya Kak!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
               "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@marletacornelia",
                "kesan": "baiikk bangeett kakkk.",
                "pesan":"semangaatt kuliahnya kakk"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@keyashafi_",
                "kesan": "kereenn bangeett",
                "pesan":"semangaatt kuliahnya kakk"
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@anggi_yllow2318",
                "kesan": "lucuu kak anggiii",
                "pesan":"semangaatt kuliahnya kak!"
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@eeffiidefi",
                "kesan": "baiikk bangettt kakk efi",
                "pesan":"semangaatt kuliahnya kakk!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
               "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "ramah bangget kak",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_fairuzary",
                "kesan": "kak faaii seruuu,asiik baiikk jugaa",  
                "pesan":"semangat terus kuliahnya kak faaii !!!"# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@tunty_i",
                "kesan": "asiikk abngeet kak tantyy",
                "pesan":"semangaatt kak kuliahnyaa!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_egistr",
                "kesan": "baiik banget bang",  
                "pesan":"semangat terus kuliahnya baanggg!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@fifah.zy",
                "kesan": "baiikk abnget kak afifah",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@biokcb",
                "kesan": "baik banget bang",
                "pesan":"Sukses selalu bangg!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@giofaniars",
                "kesan": "baikk bangett bang",
                "pesan":"Semangat terus kuliahnya bangg!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@rhmaoktvia",
                "kesan": "sangaatt baiik ",
                "pesan":"Jangan lupa jaga kesehatanyaa  Kak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@gustriana.d_",
                "kesan": "baiikk bangeett kak rahmaa",
                "pesan":"semangaatt kuliahnya kaakkk."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "   ",
                "asal":"     ",
                "alamat": "   ",
                "hobbi": "     ",
                "sosmed": "@razyn.hfd",
                "kesan": "sangaatt baiikk bang razan",
                "pesan":"semangaaatt bangg kuliahnyaa!"
            },
         
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
    
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HT0kYh68GR1M__7kPibNqja562ADfB4h",
            "https://drive.google.com/uc?export=view&id=1qkrJzO_rYiLIa4DrDAXH6GN-XnN45oY3",
            "https://drive.google.com/uc?export=view&id=1J1oLo581O_MzW9fpvQCC0A0UaTG7hkZ8",
            "https://drive.google.com/uc?export=view&id=1bwz751nwso2OU7pBlrH8P9o__5qYnvHg",
            "https://drive.google.com/uc?export=view&id=1w0HdMy3ZFxYd3FZNNdqvEGPoqj_5uG-a",
            "https://drive.google.com/uc?export=view&id=1WYU0IW0ilJig-V6_Wh-elCuKxaaPBVMR",
            "https://drive.google.com/uc?export=view&id=1r8pQl2jzRWLLT9p_BgxPT8Zoe-QrpHO7",
            "https://drive.google.com/uc?export=view&id=1AZJ7C_h_aAy6ut15tN3jpqZrj6Mfv8W4",
            "https://drive.google.com/uc?export=view&id=1lup3tx7gp5X0rz4lq2GnTXe-43UT6LlC",
            "https://drive.google.com/uc?export=view&id=1-6bsbGoMhgC1ScLIH_ATaGqh59Pik7b1",
            "https://drive.google.com/uc?export=view&id=1bVUIVKStvmPQ7o6acLFpaJ1iGw4ZcLwO",
            "https://drive.google.com/uc?export=view&id=1ruIUAnisxej9_adAQubOrOLGzGgPi8oy",
            "https://drive.google.com/uc?export=view&id=1hPeT82GlDIFxEatZOUFHVl6teIwL_AqQ",
            "https://drive.google.com/uc?export=view&id=1CKGdytzB0fXzbuFHZj4f2SFPQUgUAzp0",
            "https://drive.google.com/uc?export=view&id=1imI2YBvjdZWiXO4WFvfWKnRb0X4yG-yO1",
            "https://drive.google.com/uc?export=view&id=1rCYFY9biuQnY9N_02sqAKcafUfrZCvNa",
            "https://drive.google.com/uc?export=view&id=1KlyImw7nf8dD80InObTpuFohn4XEWYeM",
            "https://drive.google.com/uc?export=view&id=12eoYNdWRolbL2zECp12Q0UyEuzoVkj-V",
            "https://drive.google.com/uc?export=view&id=1RRy7Kdfoing8RIeWIKCd0Tz9oL98VDvG",
            "https://drive.google.com/uc?export=view&id=1axnlS2qD4bjAwTKrGrn3MqR_Ls_7bOIV",
            "https://drive.google.com/uc?export=view&id=1Pxz2iajW-HDbNMcO2xUyjM4Y72PlHG2i",
            "https://drive.google.com/uc?export=view&id=1Z9oeQhJ-pfxE7gF9RZGyN1jbrB73j9hh",
            "https://drive.google.com/uc?export=view&id=1pXGY9PdvIm_cZzJD_7XhDhbwwrzb7cv5",
            "https://drive.google.com/uc?export=view&id=1_bNHG4JtMc07HsUhJIvpWZBaTfFXV8dW",
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "baiikk abangnyaa",
                "pesan":"Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "seruuu bangeett kak yohana",
                "pesan":"semangaattt kak kuliahnyaa!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "lucuu bangeett kak.",
                "pesan":"Semangat terus kuliahnya Kak!"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "seruu bangeett kak arini.",
                "pesan":"semangaatt kak kuliahnyaaa!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "baiikk bangeeett",
                "pesan":"Sukses selalu  ke depannya!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "kereenn bangeett",
                "pesan":"semangaaattt kuliahnyaa!"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Senang bisa kenal dengan kakak, ramah bangeett.",
                "pesan":"semangaatt kuliahnyaaa!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "baiikk bangeett",
                "pesan":"semangaatt kak kuliahnyaaa."
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "kerenn bangg",
                "pesan":"Semangat terus kuliahnya bangg!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "kereenn kakkk",
                "pesan":"semangaattt kuliahnya kaakk"
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
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "baikk bangeettt,ceria truuss,gx ada capeknya pokoknya kak dea ini heheh",
                "pesan":"semangat kak kuliahnya,sehat selaluu,sukses kedepanyaa,jan bosen ama bayessian ya kak hehe"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "keren bangeett pokoknyaa",
                "pesan":"semangaatt kuliahnyaa bangg"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "kak sonyaaa baiikk bangett ramah jugaa",
                "pesan":"semangaatt kuliahnyaa kak!"
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "baiikk bangeett",
                "pesan":"semangaatt kak kuliahnyaa."
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "kereenn bangeett",
                "pesan":"Sukses selalu untuk bang depannya!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "seruu bangeett bangg.",
                "pesan":"semangaattt bangg."
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "seruu bangeett kakk",
                "pesan":"semangaattt kak kuliahnyaa!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "kereennn bangeet kaakk",
                "pesan":"Semangat terus untuk kuliahnya Kak!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "baiikk bangett",
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
                "kesan": "fiixx ini kak ilmii lucuu bangeettt.",
                "pesan":"semangaatt kak kuliahnyaa"
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "baiikk bangeett",
                "pesan":"semangaatt kuliahanya kak!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "baiikk bangeeett",
                "pesan":"semangaatt kuliahnyaa!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "kereennn kakk",
                "pesan":"semangaatt kak kuliahnyaa"
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
    
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vs4hv3NgwONvXcLgL9OK3R2TV9Bfzw_C",
            "https://drive.google.com/uc?export=view&id=1i7CGjyC-MSampZYz5mSImr3FcWcLeTki",
            "https://drive.google.com/uc?export=view&id=1p0ZQbuMmBVh6u7-umsjm3sNF_sJ0s4XQ",
            "https://drive.google.com/uc?export=view&id=1ojfIJZ1Ngcyr5mM9YICsj6ZzMayzOsry",
            "https://drive.google.com/uc?export=view&id=1-XSXV36V8YD5MAil9jStPbTjhBcVTo3Q",
            "https://drive.google.com/uc?export=view&id=1SFTMeApHbjDMw6_fb09RlKMlYjIPVM15",
            "https://drive.google.com/uc?export=view&id=1epxBoWsOIC-w6t4xl7G5qe-qbhV5Kusg",
            "https://drive.google.com/uc?export=view&id=1Y11_0q6P_tAITd5K141stifim4uK1csO",
            "https://drive.google.com/uc?export=view&id=1OMWgH6kjmsbv_PwH5mX_Uj6D1aRUGKek",
            "https://drive.google.com/uc?export=view&id=1hbCJNo4mtq7E1CKcb-huF_MPp13y1al4",
            "https://drive.google.com/uc?export=view&id=1nlD5LBhq6lPCRR-Vs9V4_UVT809OjyHP",
            "https://drive.google.com/uc?export=view&id=1d2s2tMFsSZAS_QmJy0SU1eH4_e9DVtlp",
            "https://drive.google.com/uc?export=view&id=1jEkY1VHZi6F0vCSa8BSJejX9jA5rn38C",
            "https://drive.google.com/uc?export=view&id=1Cet6et6I_iCUtyeRWgwrIK9TyNkw_Pye",
            "https://drive.google.com/uc?export=view&id=1aisOA0widguF2CQ7fZMAqa1I9bZc7qkJ",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "   ",
                "asal": "   ",
                "alamat": "    ",
                "hobbi": "     ",
                "sosmed": "@rannipu",
                "kesan": "baiikk bangeett",
                "pesan": "Sehat dan semangat terus Kak!"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya asik dan seru bangeettt.",
                "pesan": "semangaattt kuliahnyaa kakak "
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "baiikk bangeett",
                "pesan": "Sukses terus buat ke depannya Kak!"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya ramah banget.",
                "pesan": "semangaatt kak!"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "18",
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": "seruu bangeett bangg",
                "pesan": "Semangat terus kuliahnyaa baanggg!"
            },
             {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asik banget.",
                "pesan": "Sehat selalu Kak!"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": "Kesan pertamanya positif banget, Kak.",
                "pesan": "Semoga kita bisa makin akrab ya, Kak."
            },
             {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": "wooww kereenn",  
                "pesan":"semangaatt kuliahnyaa bang"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "baikk bangeett.",
                "pesan": "semangaattt kuliahnyaa"
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "baiikk bangeett",
                "pesan": "Semangat terus ya bangg"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kak hanaa friendly.",
                "pesan": "semangaatt kuliaaahh nya kak hannaaa."
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya baik dan seru.",
                "pesan": "Semangat terus Kak!"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "baiikk banget bang hanif,lucu jugaa",
                "pesan": "Semangaatt bang kuliahnyaaa"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya asik untuk diajak diskusi.",
                "pesan": "Lancar-lancar ya, Kak, kuliahnya."
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": "baikk bangett kak",  
                "pesan":"semangaat kuliahnyaaa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
    
 # Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vF1hA0-btPNP7YOOFpmeyNd4IjlT7hfB",
            "https://drive.google.com/uc?export=view&id=1n8LEfPPTaKRXx4wDSIO8RuUzFCDgDfPy",
            "https://drive.google.com/uc?export=view&id=16Ukh6QWA61zZMdDhLJfa-F1N7L6EnOgP",
            "https://drive.google.com/uc?export=view&id=1MuPVzLa2DdBBRh0KVZ0nXgF_CC-k84Ml",
            "https://drive.google.com/uc?export=view&id=1euB3vvZKGDLe8akZrlgoIFaGZz_faH70",
            "https://drive.google.com/uc?export=view&id=1W_u0vM4im4on-GUcI5QQ0Ilv2PcGAyTq",
            "https://drive.google.com/uc?export=view&id=1Q16q6RzdagMpBRB6D_LhZpvc_dNs1KtH",
            "https://drive.google.com/uc?export=view&id=1tE-3Bvja0JESWG1WW23mI94xTXw7CX74",
            "https://drive.google.com/uc?export=view&id=1_ABkFHRUUMjpKVwTvMn1RroFiq8CGLpY",
            "https://drive.google.com/uc?export=view&id=1XG6zE_fOPJ7XTZEyZcg1Kp-UwVL9scnv",
            "https://drive.google.com/uc?export=view&id=1vcKGlXpUfDYkoRLhOHaoLDoPLa7eVRMx",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "dananghk_",
                "kesan": "serruu bangg",
                "pesan": "Semangat terus bangg!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": " ",
                "asal": "  ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "syalaishaa_31",
                "kesan": "asiikk bangeett.",
                "pesan": "semangaatt kuliahnya!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "den_iki__",
                "kesan": "ramah dan baik bangeett",
                "pesan": "Sehat selalu ya bangg"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": " ",
                "asal": "  ",
                "alamat": "  ",
                "hobbi": " ",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya keren bangeett",
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "aprhtp_",
                "kesan": "baiikk banget kak",
                "pesan": "Semoga semua urusannya dilancarkan kak."
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": " ",
                "asal": "  ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "nabila_zazahra",
                "kesan": "seruuuuu",
                "pesan": "Semangaatt kuliahnyaa kakak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "dhafinrzqa13",
                "kesan": "lucuu bangg heehe",
                "pesan": "semangaatt kuliahnya bangg"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya kak!"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "englirahmdhnii",
                "kesan": "Seru banget kak",
                "pesan": "Semoga sukses selalu kak!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya sangat ramah bangeett",
                "pesan": "Jaga kesehatan yaa kak!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "  ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "nydiaaptr_",
                "kesan": "seruu kak",
                "pesan": "Semangat kuliahnya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lm77jB2vAs2r2sgSprHY-V2P5oeDcz9D",
            "https://drive.google.com/uc?export=view&id=1vagViR1cOb1yrTkDKdnHajRH130QT23pj",
            "https://drive.google.com/uc?export=view&id=1hVkOtXgVR030lVbKDcPhf0pRn4R4r1Lm",
            "https://drive.google.com/uc?export=view&id=1QhoTqcZ1zja_7ku5k2rMBquwd7PnrKq_",
            "https://drive.google.com/uc?export=view&id=1_JLWIv_ZfgCfcOQB4VkoTaKFYKiDhA4r",
            "https://drive.google.com/uc?export=view&id=1p-KODV2rg4t7DI6ApTHuChPyi_fJE-DG",
            "https://drive.google.com/uc?export=view&id=1azK4x5-Bbq3b3dOtU8y2VY3dD9oRDEpG",
            "https://drive.google.com/uc?export=view&id=1bbyCphiekh-B9O-JzSskBp5pZOzyx-MT",
            "https://drive.google.com/uc?export=view&id=1nzBENsML-OqDeA5fw2-OVnt-2v83WJaa",
            "https://drive.google.com/uc?export=view&id=1VsvPTE5809Sqp9buaxXKEDAuxLN4IUtE",
             "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1E2eHn1T97NY0Neb4CblFBPHSbfgXDOag",
            "https://drive.google.com/uc?export=view&id=19Odu2_M8mHow3cQV52ea6JJI71rPzn55",
            "https://drive.google.com/uc?export=view&id=1HGHZ_cv-KEjr87Z_Hqlz3BqmoWJA_1Oe",
            "https://drive.google.com/uc?export=view&id=1qFdb3BuVJYRCfGxizfpK59vklwdM74Rb",
            "https://drive.google.com/uc?export=view&id=1YFj_SuzCmDLMx9A7Q8AR8S_Xy4TUpir-",
            "https://drive.google.com/uc?export=view&id=1yK_vFWv5ViCGl6KPwpjjCU2VjdPu9ff7",
            "https://drive.google.com/uc?export=view&id=19M4rDly1jH1l9oKv_wkF6ZIq53KevOdp",
            "https://drive.google.com/uc?export=view&id=1_xRbojpM6a4Jc9Mu9WyrGUZSJ2R9zMop",
            "https://drive.google.com/uc?export=view&id=1rX165GgXAyJdEOKisObNKt0cCwrY6p3C",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak ciaa asik++seruu bangeett",
                "pesan": "sehaatt selaluu kakk!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@rahmanellyana",
                "kesan": "pinterr bangeett",
                "pesan": "semangaatt kuliahnya kakk!"
            },
             {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@mananam_",
                "kesan": "baikk dan sabar bangett ngajarin nyaa",
                "pesan": "semangaatt truss bangg!"
            },
            {
            
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@noe_rruuu",
                "kesan": "lucuuuu",
                "pesan": "semangaaatt kuliahnya bangg!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@rafidivaefangga",
                "kesan": "Seru banget bangg",
                "pesan": "semangaatt bangg"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@refadp_",
                "kesan": "seruu banget kak",
                "pesan": "semangatt kak kuliahnyaa"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@tryyaniciaaa",
                "kesan": "seruu bangeet kak",
                "pesan": "Tetap semangat kak!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@aliyaamara",
                "kesan": "kereenn kak",
                "pesan": "Semangat kuliahnya kak!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@donamaya.p",
                "kesan": "Terima kasih sudah berbagi ilmu kak",
                "pesan": "Semoga sukses di masa depaann kaakk!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@writtenbyangel",
                "kesan": "baiikk bangeett kak",
                "pesan": "semangaatt kuliahnya kak!"
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
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@naylasalsabilaa",
                "kesan": "baiikk bangeett kak",
                "pesan": "semangaatt kuliahnya kak!"
            },
             {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@saniayyllstr",
                "kesan": "baiikk bangeett kak",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "baiikk bangeett bangg",
                "pesan": "semangaatt kuliahnya bangg!"
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@nltg._",
                "kesan": "baiikk bangeett kak",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@citrastin",
                "kesan": "baiikk bangeett kak",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@eigirtmv",
                "kesan": "baiikk bangeett kak",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@roms.slbn",
                "kesan": "baiikk bangeett kak",
                "pesan": "semangaatt kuliahnya kak!"
            },
           
           
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
    

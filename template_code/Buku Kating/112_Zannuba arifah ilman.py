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
                "umur": "  ",
                "asal":"   ",
                "alamat": "    ,
                "hobbi": "     ",
                "sosmed": "@randaadriana_",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "  ",
                "asal":"   ",
                "alamat": "   ",
                "hobbi": "    ",
                "sosmed": "@Junitaa.0406",
                "kesan": "baik bangeett kak",
                "pesan":"Semangaatt kuliahnya kak!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "   ",
                "asal":"   ",
                "alamat": "    ",
                "hobbi": "     ",
                "sosmed": "@mregiiii_",
                "kesan": "kereenn bangg",
                "pesan":"semangaatt kuliahnya bangg"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "   ",
                "asal":"    ",
                "alamat": "     ",
                "hobbi": "    ",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya asik dan seru bangeett",
                "pesan":"Semangat terus kuliahnya ya, Kak!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "  ",
                "asal":"   ",
                "alamat": "    ",
                "hobbi": "    ",
                "sosmed": "@fadilalfarizzi",
                "kesan": "bang fadiill kereenn.",
                "pesan":"Semangaatt kuliahnya bangg"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "  ",
                "asal":"     ",
                "alamat": "     ",
                "hobbi": "   ",
                "sosmed": "@muhammadqil1111",
                "kesan": "baiikk bangeett bangg",
                "pesan":"semangaatt kuliahnya bangg!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "   ",
                "asal":"    ",
                "alamat": "     ",
                "hobbi": "     ",
                "sosmed": "@notfall.s",
                "kesan": baiikk bangett bangg",  
                "pesan":"semangat terus kuliahnya bangg !!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "  ",
                "asal":"    ",
                "alamat": "    ",
                "hobbi": "    ",
                "sosmed": "@adiaafrj",
                "kesan": "Kereenn kakkk",
                "pesan":"Semangat terus kuliahnya Kak!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "  ",
                "asal":"   ",
                "alamat": "   ",
                "hobbi": "    ",
                "sosmed": "@marletacornelia",
                "kesan": "baiikk bangeett kakkk.",
                "pesan":"semangaatt kuliahnya kakk"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "   ",
                "asal":"    ",
                "alamat": "    ",
                "hobbi": "     ",
                "sosmed": "@keyashafi_",
                "kesan": "kereenn bangeett",
                "pesan":"semangaatt kuliahnya kakk"
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "  ",
                "asal":"    ",
                "alamat": "     ",
                "hobbi": "    ",
                "sosmed": "@anggi_yllow2318",
                "kesan": "lucuu kak anggiii",
                "pesan":"semangaatt kuliahnya kak!"
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "   ",
                "asal":"    ",
                "alamat": "     ",
                "hobbi": "     ",
                "sosmed": "@eeffiidefi",
                "kesan": "baiikk bangettt kakk efi",
                "pesan":"semangaatt kuliahnya kakk!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim":"  ",
                "umur": "   ",
                "asal":"    ",
                "alamat": "    ",
                "hobbi": "    ",
                "sosmed": "@",
                "kesan": "ramah bangget kak",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "  ",
                "asal":"    ",
                "alamat": "   ",
                "hobbi": "   ",
                "sosmed": "@_fairuzary",
                "kesan": "kak faaii seruuu,asiik baiikk jugaa",  
                "pesan":"semangat terus kuliahnya kak faaii !!!"# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "  ",
                "asal":"    ",
                "alamat": "    ",
                "hobbi": "    ",
                "sosmed": "@tunty_i",
                "kesan": "asiikk abngeet kak tantyy",
                "pesan":"semangaatt kak kuliahnyaa!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "   ",
                "asal":"    ",
                "alamat": "    ",
                "hobbi": "    ",
                "sosmed": "@_egistr",
                "kesan": "baiik banget bang",  
                "pesan":"semangat terus kuliahnya baanggg!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "  ",
                "asal":"    ",
                "alamat": "     ",
                "hobbi": "    ",
                "sosmed": "@fifah.zy",
                "kesan": "baiikk abnget kak afifah",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "   ",
                "asal":"    ",
                "alamat": "K    ",
                "hobbi": "    ",
                "sosmed": "@biokcb",
                "kesan": "baik banget bang,
                "pesan":"Sukses selalu bangg!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "  ",
                "asal":"    ",
                "alamat": "    ",
                "hobbi": "    ",
                "sosmed": "@giofaniars",
                "kesan": "baikk bangett bang",
                "pesan":"Semangat terus kuliahnya bangg!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "  ",
                "asal":"    ",
                "alamat": "   ",
                "hobbi": "     ",
                "sosmed": "@rhmaoktvia",
                "kesan": sangaatt baiik ",
                "pesan":"Jangan lupa jaga kesehatanyaa  Kak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "  ",
                "asal":"    ",
                "alamat": "   ",
                "hobbi": "    ",
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


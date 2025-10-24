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
            "https://drive.google.com/uc?export=view&id=1pugYjo5CN9_eRBpmQp5frktDHbFVWbXM",
            "https://drive.google.com/uc?export=view&id=1OszRW3I7c3WLqE0NPriygKiXWHm9kGbg",
            "https://drive.google.com/uc?export=view&id=1Q3FWl5uvutvwx3Z5fN_FWJmiSe4V_PXS",
            "https://drive.google.com/uc?export=view&id=1b5ogEd2e_Q7xrDovGrkfZ0i3g5FGK3gg/",
            "https://drive.google.com/uc?export=view&id=1acCvoBAL1FfWEO7-EndHo3r4BvWBzWvS",
            "https://drive.google.com/uc?export=view&id=1-bXkFt_W6cYH-BGv_x70uLvpCxpikJlr",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat":"Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "Tegas, humble",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Asik banget",  
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Ramah,cheerful banget",  
                "pesan":"Sehat selalu kakak"# 1
            },
            {
                "nama": "Syadza Puspadari AZhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat":"Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kalem dan pendiem",  
                "pesan":"Semoga kuliahnya lancar kakak"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "12245001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Vibesnya independent woman, bendahara banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Asik,ramah",  
                "pesan":"Sehat selalu kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=118gPPBbpkf3_AHV207boNVBbO0cd3-zP",
            "https://drive.google.com/uc?export=view&id=1NWBOc2XVLaGEt2if7HgHJIm7zReZ_7jf",
            "https://drive.google.com/uc?export=view&id=1Nk3druWfSAphpA87BUjdTYxels4SD3ba",
            "https://drive.google.com/uc?export=view&id=1q_VJyRVkL1VACoTtDB4tdy0RwPf98cX6",
            "https://drive.google.com/uc?export=view&id=17ybaHAMmfFWPagKdFaRtwO5i2ggQc7zh",
            "https://drive.google.com/uc?export=view&id=1-HFQ_rgU704fWl9IpDsVIG5nE30N9JgZ",
            "https://drive.google.com/uc?export=view&id=1ksy0s0yTsfLsPsMQP6XfLJnnpbsQUwyu",
            "https://drive.google.com/uc?export=view&id=1RmkjoSBZxRAtNYtVFS4Z_p71UcECol9e",
            "https://drive.google.com/uc?export=view&id=1YZUOnzsupMJ0b6FcCuFyKYq6tzsEgUXF",
            "https://drive.google.com/uc?export=view&id=1LR5ORmmErZuB_Grjdz3wsH9Nauqj84V7",
            "https://drive.google.com/uc?export=view&id=1ynj4CusiWEDMM-9Zn4umf-yoU19iPwq8",
            "https://drive.google.com/uc?export=view&id=1h2FykmvMKIllW5mVTWvl97pmgHlhhwvR",
            "https://drive.google.com/uc?export=view&id=1EAYHi8QP6wD_6fLDEx6KG1fKVthxKOcl",
            "https://drive.google.com/uc?export=view&id=17F0Bv7914SddE8xKeI9XkzGlMgTtSDrd",

        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Nusa Kambangan",
                "alamat": "Lapas, Belwis",
                "hobbi": "Melarikan diri",
                "sosmed": "@jeremia_s_",
                "kesan": "Asik dan humble banget",  
                "pesan":"Semoga lancar sempronya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": " 122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak Dhea lucu banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kalcer dan skena banget",  
                "pesan":"Semangat kuliahnya kakak"# 1
            },
             {
                "nama": " Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Coquette banget bajunya (pinky)",  
                "pesan":"semangat kuliahnya kakak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": " 123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Pinter (gak heran ozt soalnya)",  
                "pesan":"Sehat selalu bang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek Cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Outfit sama rambutnya lucu banget sukaaaa",  
                "pesan":"Sehat selalu kakak"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@givarooo",
                "kesan": "Ramah",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Terlihat introvert",  
                "pesan":"Sehat selalu bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "Mengukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Keliatannya kalem",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": " 123450085",
                "umur": "19",
                "asal":"Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Ceria bangett",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik",
                "kesan": "Humble, lucu",  
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Kalcer banget",  
                "pesan":"Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": " Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Terlihat kalem dan pendiem",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Baru",
                "alamat": "Belwis",
                "hobbi": "Menyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Ceria dan aktif banget",  
                "pesan":"Semangat dan bahagia selalu kak wawa"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lvzlSxNKFoq2Qo6xw_CnSsw8XXES19wh",
            "https://drive.google.com/uc?export=view&id=1ic9__NdJXPgSkBCZrB6WHslKlykWEVgS",
            "https://drive.google.com/uc?export=view&id=11VEzJUk0YQ0rWYPkAzwZ0RsOyYrRyLuU",
            "https://drive.google.com/uc?export=view&id=1mgWmY0yXV8MU4nvP78qB-9pp07-vIjAu",
            
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Asik, jokesnya lucu banget",  
                "pesan":"Semoga kuliahnya lancar selalu bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@nadyaanjaani",
                "kesan": "Cantik banget",  
                "pesan":"semangat kuliahnya kakak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kalem dan pinter",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Suara kak Lia lucu",  
                "pesan":"Sehat selalu kakak"# 1
            },
        
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LQojj1dEbnqL_U5NmmrBqzbrGPh-saK_",
            "https://drive.google.com/uc?export=view&id=1Q9irvxf6E5qGp_lVt-0HIn-v15WmL8Iw",
            "https://drive.google.com/uc?export=view&id=1IrveFlA2MkuX1Df7MClWxBeTPFuZo43Z",
            "https://drive.google.com/uc?export=view&id=1KpZStvfnThAsP9UHHGOulfwhpDbFWk7S",
            "https://drive.google.com/uc?export=view&id=1O4jOKZG16YcLqKiP0gkgAvN3XSXPDIKO",
            "https://drive.google.com/uc?export=view&id=1FsNH1350rvlUSddDuUFIBDD1gG5MITL2",
            "https://drive.google.com/uc?export=view&id=1BREple48AIds7CYmro1X2pmp0dLoaAzV",
            "https://drive.google.com/uc?export=view&id=1X3mOpKv1Lxdg1KJ8KlgRqkzow-1nMf9Y",
            "https://drive.google.com/uc?export=view&id=1dXZ-waNrBDEirbeBvg3Apyu-4GqFkNE4",
            "https://drive.google.com/uc?export=view&id=1G-SQ5neDGJrdrpo-pyukXQ9D1yvtgHuN",
            "https://drive.google.com/uc?export=view&id=1xHrz1274FT7kfOx9qUT7OOA_Q6H-02Jy",
            "https://drive.google.com/uc?export=view&id=1jxHP-0sWb24GdXktntkUWDPLk45Wka5T",
            "https://drive.google.com/uc?export=view&id=1KkE3uok1VD7WFgB2kAoTD475IWx_Yx31",
            "https://drive.google.com/uc?export=view&id=1I-bPbtdtmJEW-FWuuE_Xmz3HDAmhaOKO",
            "https://drive.google.com/uc?export=view&id=1ZXElqLW-8eaakE2BtxVIMhCCz-dFsLOx",
            "https://drive.google.com/uc?export=view&id=1b2qMWkMNtR7K4AANR8CZtjbvrdnmZG_-",
            "https://drive.google.com/uc?export=view&id=1VG4PEjLxopfu1b1ZL72e19u7D1i0rvVi",
            "https://drive.google.com/uc?export=view&id=1wdkoS0eqmlRvbC7IGjJsvVaW3mWII2ES",
            "https://drive.google.com/uc?export=view&id=110s2lpLeH5UFzHB8I-4eX0_5nXnF6uQa",
            "https://drive.google.com/uc?export=view&id=1vh2x__DZ8iuG3XIse9G8WfzPbIogRWNQ",
            "https://drive.google.com/uc?export=view&id=1AfAx1jZ_Hkjk2rMZ038vWru7oyddXw4p",
            "https://drive.google.com/uc?export=view&id=1FDckZTaWHOik9sFPTIYnJ2HuiMUYciln",
            "https://drive.google.com/uc?export=view&id=10IijA0VDY5XqgihU9koFrqLcrNQSDS38",
            "https://drive.google.com/uc?export=view&id=1LWlZGpnwssrKRBUIi2BTuOs3XmVzBxuC",
            "https://drive.google.com/uc?export=view&id=1HhJn6nKrMwMbK5G5SL225JlfW2v7oqIc",
            "https://drive.google.com/uc?export=view&id=1AwV3cRXffvTYNmmMS1HTYZZtoxqGI5RL",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": " 122450107",
                "umur": "",
                "asal":"",
                "alamat":"",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Tegas, keren",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat":"Korpri, Sukarame",
                "hobbi": "Jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Cantik banget",  
                "pesan":"Sehat selalu kak"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat":"Belwis",
                "hobbi": "Healing",
                "sosmed": " @allyapsha_",
                "kesan": "Tegas, vibenya cewe mandiri banget",  
                "pesan":"Semangat dan sehat selalu kak"# 1
            },
            {
                "nama":"Ahmad Rizky",
                "nim":"123450050",
                "umur":"20",
                "asal":"Tangerang",
                "alamat":"GH Belwis",
                "hobbi":"Main bola",
                "sosmed":"@ahmad.rizky___",
                "kesan": "Public speakingnya bagus bangettt, keren",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat":"Deket kos dapa",
                "hobbi": "@arientakhsnl_",
                "sosmed": "@arientakhsnl_",
                "kesan": "Tegas, humble, keren",  
                "pesan":"Semoga kuliahnya lancar kak"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat":"Sebelah kos Arienta",
                "hobbi": "Jailin orang sampai nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Tegas, humble",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat":"Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Tegas, humble, banyak hobi",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat":"Kos putri gerbang barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "Keren ditambah hobinya belajar makin keren",  
                "pesan":"Seha selalu kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat":"Sebelah kos kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "Jago ngoding",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat":"Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "Tegas, humble",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat":"Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Tegas,peka",  
                "pesan":"Sehat selalu kak"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat":"Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "Humble banget, ramah",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat":"Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kulineran kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Agak pendiem tapi lucu",  
                "pesan":"Sehat selalu bang, semangat"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat":"Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Ramah banget",  
                "pesan":"Semangat selalu kakak"# 1
            },
            {
                "nama": " Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat":"Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Humble, kakak NIM ",  
                "pesan":"Semangat dan sehat selalu kakak"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat":"Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakaknya lucu",  
                "pesan":"Semangat terus kakak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat":"Jl. Airan",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Tegas, kalau ngobrol to the point",  
                "pesan":"Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat":"Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Tegas",  
                "pesan":"Sehat selalu bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat":"Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Ceria, yang pasti jago dance",  
                "pesan":"Semangat kuliah dan dancenya kak"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": " 123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat":"Belwis, Pemda",
                "hobbi": "Nangkep lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Abangnya asik banget, seru",  
                "pesan":"Semangat dan sehat selalu bang"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat":"Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Sangat kalcer",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat":"Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kalem dan terlihat introvert",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat":"Belwis",
                "hobbi": "Ngehina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Humble banget",  
                "pesan":"Sehat selalu bang"# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat":"Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Tegas,banyak hobi",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat":"Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Humble dan kocak banget",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kalem dan pendiem banget",  
                "pesan":"Semangat terus kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()


if menu == "Departemen MIKFES":
    def Mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HmMXg0OcQSu2RBbptfG7NL6-k_ipw5Ay",
            "https://drive.google.com/uc?export=view&id=1847Pe6WVtV35FygvWko8_wrAjbgWKCn4",
            "https://drive.google.com/uc?export=view&id=11OWds_kkZQjuK1epu6z3AQkWt6jdAepZ",
            "https://drive.google.com/uc?export=view&id=1uP_wWzDYiCj-CtTF8NvcEms0Wlz2l-BA",
            "https://drive.google.com/uc?export=view&id=1VWF_0yt9skse9YQZjNEszx0gVckmNijZ",
            "https://drive.google.com/uc?export=view&id=1zZuTJsTy7YrxYU0gckItGzr5ZEYERai3",
            "https://drive.google.com/uc?export=view&id=1lrBJucJ0UZr2fucG1da255k7-SXagQ7R",
            "https://drive.google.com/uc?export=view&id=18v-sKv1mGhwdjUhJcUx0y-tD75-KrTja",
            "https://drive.google.com/uc?export=view&id=1aghKhrRHDfARE4UCHJL-uI6ea_CtNydB",
            "https://drive.google.com/uc?export=view&id=10E4OkpIoUtyT8Fo6ZtG_rRIV0-MhCX9y",
            "https://drive.google.com/uc?export=view&id=1gcx5d4Fhamn8Onkvjry3Y2HflOaJIHdh",
            "https://drive.google.com/uc?export=view&id=1LwGflZ5STX2UKfpvHZFneaFcoBoETQA9",
            "https://drive.google.com/uc?export=view&id=18ITR4PmgiLIBetLbJ5ORXnpYxffr-jSe",
            "https://drive.google.com/uc?export=view&id=1LGLa5VXANe3sFY9z87FafRDBT-hn_8ky",
            "https://drive.google.com/uc?export=view&id=1mbEIU8fDK7r5FL9zdMZGW2eYsbFbmTaY",
            "https://drive.google.com/uc?export=view&id=1qBcdoahqPHVmB1ZiHpG0RqYQHUsz6nd-",
            "https://drive.google.com/uc?export=view&id=1__gELBzIvzpXxTkUUGVJFQ5NZvFbZ0EU",
            "https://drive.google.com/uc?export=view&id=1N79SnjeMFcmkUFwzpJl0jYkgQtpckEXQ",
            "https://drive.google.com/uc?export=view&id=1euCmzAYe-JIZvmiVX2lCQmCPSoTAhc0d",
            "https://drive.google.com/uc?export=view&id=1-FFXfLcG9UcQVR2WyvhHMYhMxP-_FA7q",
            "https://drive.google.com/uc?export=view&id=1y1dFsiF9Rmzyx2fd1-8BFFWgeMRDVRRZ",
            "https://drive.google.com/uc?export=view&id=1QxNRe0j-QhRFx2zUSGDmEbU88RAwFdvi",
        ]
        data_list = [
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang,Banten",
                "alamat":"Sukarame",
                "hobbi": "Tidur Berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Kelihatan banget pinternya",  
                "pesan":"semangat terus bang semoga lancar kuliahnya"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat":"Jl.Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Ramah, seru dan hobinya keren",  
                "pesan":"Sehat selalu kakak"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat":"Sukarame",
                "hobbi": "Dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Keren banget",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat":"Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Pinter dan aktif",  
                "pesan":"Sehat selalu kakak"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Fore",
                "hobbi": "Segala a100",
                "sosmed": " @fadilalfarizzi",
                "kesan": "Public speakingnya bagus banget, jago gitar juga",  
                "pesan":"Semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat":"GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Tegas, keren",  
                "pesan":"Sehat selalu bang, semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat":"Bandar Lampung",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "Keren, humble",  
                "pesan":"Sehat terus bang, semangat kuliahnya"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat":"Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@adiaafrj",
                "kesan": "Terlihat kalem dan pendiem",  
                "pesan":"Sehat selalu kak, lancar kuliahnya"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat":"Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Keren dan ceria, kayaknya ekstrovert",  
                "pesan":"Semoga harinya bahagia selalu kak"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keyashafi_",
                "kesan": "Keliatannya kalem karena gak terlalu banyak ngomong pas wawancara",  
                "pesan":"Sehat selalu bang, semoga harinya bahagia selalu"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat":"Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Positif vibes",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat":"Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Keren",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat":"Pesawaran, Lampung",
                "hobbi": "Main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kalem",  
                "pesan":"Bahagia selalu kak"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat":"Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Cantik, keren",  
                "pesan":"Bahagia selalu kak"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat":"Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Tegas, keren, to the point banget",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat":"Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Pinter",  
                "pesan":"semangat terus bang semoga kuliahnya lancar selalu"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat":"Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Keren,humas able",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Kedaton",
                "hobbi": " Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Kocak dan seru",  
                "pesan":"semangat terus bang, sukses dan sehat selalu"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat":"Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Pinter, kalem",  
                "pesan":"Sehat dan sukses selalu bang"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat":"Lapas Raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Lucu, imut",  
                "pesan":"Bahagia selalu kak"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat":"Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kalem, pendiem",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat":"Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Lucu, keren",  
                "pesan":"Semangat dan sehat selalu bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Mikfes()

if menu == "Departemen Eksternal":
    def Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1F5no_4Xs5lElyYRa2d8nLhkFlUj6i15V",
            "https://drive.google.com/uc?export=view&id=1WV9GmZKftrb-Gd-1OCAOQwayKKxTmSob",
            "https://drive.google.com/uc?export=view&id=1X7cIKtTKuZCsmh4Fh5ozOZ2BbVWOGvL9",
            "https://drive.google.com/uc?export=view&id=1dBmlc8yp5qlEpYns4QD_wvhHtvG3TpxW",
            "https://drive.google.com/uc?export=view&id=1dt13Sh96qvqmoMsLPvI1cHzhCSWHE6UF",
            "https://drive.google.com/uc?export=view&id=10wTCP0RiJ6fIIH5_qDRMQJRUmpqErDwX",
            "https://drive.google.com/uc?export=view&id=1f3PD5rNoJ1_Osxivr-AjO0EYV2b3CiV0",
            "https://drive.google.com/uc?export=view&id=15K0-Duv7mxFv9aJfWWy7YQ24EHHE4JUs",
            "https://drive.google.com/uc?export=view&id=1VcfvG4ezH57vgDfjgluQ4BSjZ5eOuSA1",
            "https://drive.google.com/uc?export=view&id=1R0oHw-FDwNPVzosBNDT0oOL2bYiaYodT",
            "https://drive.google.com/uc?export=view&id=1NgWSQf0ORnblCwiXCRXOxgZuM6g_R_E0",
            "https://drive.google.com/uc?export=view&id=1mHslDtOpxcnTe73oLWEVa9IuHQYBAypJ",
            "https://drive.google.com/uc?export=view&id=1worhsaTH5u99AHMa2oActNcM0bJaCYbP",
            "https://drive.google.com/uc?export=view&id=1mkN3Bdwqdu0Bv6VGKNkEWi4rDUxUrseu",
            "https://drive.google.com/uc?export=view&id=1MoJvG97faoYO6MBq4euL538coHwy3TeJ",
            "https://drive.google.com/uc?export=view&id=1lS0xebRk8AYTQxR2To8zzdZr0X-bksMb",
            "https://drive.google.com/uc?export=view&id=1JnEaT-hcxSrob2OYd01JTMUWW1lj2rho",
            "https://drive.google.com/uc?export=view&id=1iq5P1rbIHvCYNAsneqX4ZB3REf4GvyLd",
            "https://drive.google.com/uc?export=view&id=1z7TIb9LDs3sWMbLQ_Esl-FsxFioSzIDZ",
            "https://drive.google.com/uc?export=view&id=1hFWILYwWUAd1mUD4U0dIisK7Jnu-Tl4A",
            "https://drive.google.com/uc?export=view&id=1bt5EsjLk9cRzZR5K5cJjcnLokLTmvpMO",
            "https://drive.google.com/uc?export=view&id=1DDuI92kPBultL_Haq2pImufPUtzQlUyg",
            "https://drive.google.com/uc?export=view&id=142h0P3fpIto1ts51DMA_Vk9oO_8RcXoZ",
            "https://drive.google.com/uc?export=view&id=1PS1xgxUXHiuPHSJGblZI6F2CVc1_CqHw",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat":"Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Terlihat asik dan ramah",  
                "pesan":"Semoga lancar kuliahnya bang, semangatt"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat":"Jl.Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya baik, ramah juga",  
                "pesan":"Sehat selalu kakak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat":"Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Cantik",  
                "pesan":"semangat terus kuliahnya kak, lancar selalu"# 1
            },
            {
                "nama": " Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat":"Teluk,Bandar Lampung",
                "hobbi": "Jalan-jalan keliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Strong independent woman banget vibesnya",  
                "pesan":"Bahagia dan sehat selalu kakak"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat":"Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Asik dan baik banget",  
                "pesan":"Semoga kuliahnya lancar bang, semangat selalu"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat":"Sukarame",
                "hobbi": "Main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Tegas, keren, lucu",  
                "pesan":"Sehat selalu kakak, semoga kuliahnya lancar"# 1
            },
            {
                "nama":"Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat":"Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Manis",  
                "pesan":"Sehat terus kakak, semangat kuliahnya"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat":"Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Cantik, humble",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat":"Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Humble,asik dan seru",  
                "pesan":"Semoga harinya bahagia selalu bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat":"Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Keliatannya ekstrovert",  
                "pesan":"Sehat selalu kak, semoga harinya bahagia selalu"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": " 123450112",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat":"Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Keren, cantik, duta",  
                "pesan":"Bahagia selalu kak, semoga bisa jadi salah satu winner dutit 2025"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": " 123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat":"Korpri",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Keren, cantik, baik, humble",  
                "pesan":"Bahagia selalu kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat":"Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Keren, tegas tapi tetep humble",  
                "pesan":"Bahagia selalu bang"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat":"Like crowded",
                "hobbi": "Gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Seru, ceria banget",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat":"Jl. Raden Saleh",
                "hobbi": "Nyubitin ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Baik banget, keren",  
                "pesan":"Bahagia dan sehat selalu kakak "# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat":"Sukarame",
                "hobbi": "Main badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Ramah, lucu",  
                "pesan":"Semangat selalu bang"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": " 123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat":"Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Seru, kocak ramah pula",  
                "pesan":"semangat kuliahnya bang, bahagia selalu"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat":"Sukarame",
                "hobbi": "Minta tolong adit",
                "sosmed": " @fatthyaa_",
                "kesan": "Baik, ramah",  
                "pesan":"semangat terus kakak semoga kuliahnya lancar selalu"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat":"Korpri raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Keren, ramah banget, seru, kelihatannya ekstrovert",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "melynznb",
                "kesan": "Cantik",  
                "pesan":"semangat terus kakak, sukses dan sehat selalu"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafiraz",
                "kesan": "Cantik, keren",  
                "pesan":"Sehat dan sukses selalu kakak"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat":"Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Lucu, cantik",  
                "pesan":"Bahagia selalu kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat":"Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Keren",  
                "pesan":"Bahagia selalu bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat":"Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Lucu, keren, cantik",  
                "pesan":"Semangat dan sehat selalu kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Eksternal()
            

if menu == "Departemen Internal":
    def Internal ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1d14e7g73FMHxrCRijcajDvcehei1J_Yw",
            "https://drive.google.com/uc?export=view&id=1P5nsoKUlPUkJv2E9gDUL-e4W59unFVRe",
            "https://drive.google.com/uc?export=view&id=11xDotoN8W2qwWLO0ErEB-l2K9dc_Rfmc",
            "https://drive.google.com/uc?export=view&id=10O0lyTWyt6rkKGGmx5talZ1yI54jpgH7",
            "https://drive.google.com/uc?export=view&id=1-oYXmdb8dAEGmiM5_RRG7VM8hdHG3Q6l",
            "https://drive.google.com/uc?export=view&id=1jDP01_zrKs-nYkPNq7onuyCI8qy87NY4",
            "https://drive.google.com/uc?export=view&id=192Z38AFq-1oug5nJoWGkUzarLV2USD7O",
            "https://drive.google.com/uc?export=view&id=1DssEPoDrWKFQD-IRlF1PqLnBuGYa7Y1Z",
            "https://drive.google.com/uc?export=view&id=1ENJgWWsAKZmVARRfTT6OJSwiazWyOmHy",
            "https://drive.google.com/uc?export=view&id=1O9Crd3u7RqljpNTinhV6KJ3_hQD0RhH8",
            "https://drive.google.com/uc?export=view&id=1cNtIJNLrYbaTlX85oRCSK4kLT2z54xVn",
            "https://drive.google.com/uc?export=view&id=1ob6T5-_8K1ziuhWgPi1ZSz8K9q1P1mg2",
            "https://drive.google.com/uc?export=view&id=1dr3w3mWefdjPjbBlQ_d300xIIaA_MTcp",
            "https://drive.google.com/uc?export=view&id=15NpdMrpeK7WlcNGGjfJmHHtXdH6I4nDi",
            "https://drive.google.com/uc?export=view&id=1u-S2xEA-oFhpz-mGj9pi9IKslwU2u7jB",   
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat":"Balam",
                "hobbi": "Mengaji",
                "sosmed": "@ranniku",
                "kesan": "Kak Rani keliatan skena banget penampilannya, sukaa",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat":"Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta rambutnya keren",  
                "pesan":"Maaf pernah manggil kak Renta abang"# 1
            },
            {
                "nama": "Rendy Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat":"Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Bang Rendy kayak soft spoken banget",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": " 123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat":"Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hana asik banget, seru dan rame kalau udah ngomong",  
                "pesan":"semangat kuliahnya kakak"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": " 123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat":"Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat":"Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": " 123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat":"Tanjung Seneng",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat":"Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": " 122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat":"Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat":"Gerbang Barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan",
                "alamat":"Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat":"Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": " 123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat":"Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": " 123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat":"Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": " @muhammadnaufalalghani73",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": " 123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat":"Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Internal()

if menu == "Departemen SSD":
    def SSD ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vAATNhzvC9wEwR0iQueG3xpkHQOb9mQI",
            "https://drive.google.com/uc?export=view&id=18dvFvpORkbwAlYv7KwtprQv3RYrZ0UGB",
            "https://drive.google.com/uc?export=view&id=1yrYx1w6K2baNFUcYiPGB_nOr1raRpZBf",
            "https://drive.google.com/uc?export=view&id=1EerfMuwqgOrt0paBumw31gRwqdGScOLJ",
            "https://drive.google.com/uc?export=view&id=1be-HZHgY-F_lWy6v5wUnRlMf7ZTNDWqQ",
            "https://drive.google.com/uc?export=view&id=1Yi59WysL2YQqp5hkk_P-crNqlC6UCaE_",
            "https://drive.google.com/uc?export=view&id=1C3tSPvGOGIYOUm2lkIMdrV93xxeh-Pav",
            "https://drive.google.com/uc?export=view&id=1K5NoqXMnRu9UukglmQMYq0I0otxei_X-",
            "https://drive.google.com/uc?export=view&id=1IjlAd8wCWLbvSgPGyc-7esiVue9yigTE",
            "https://drive.google.com/uc?export=view&id=1CY7qyKW3BhEsuNhX7BiOwNuQnBYevD4g",
            "https://drive.google.com/uc?export=view&id=1tjb1oBs7r0pjHWp0XEuZI7gV-aAc8Opv",
           
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Bandar Lampung",
                "alamat":"Belakang PB",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_",
                "kesan": "Ramah dan suka senyum",  
                "pesan":"Semangat kuliah dan lombanya bang"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat":"Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Terlihat kalem dan pendiema",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat":"Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki__",
                "kesan": "Gak terlalu banyak omong, cenderung to the point",  
                "pesan":"semangat terus bang, lancar kuliahnya"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": " 123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat":"Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anandiacrn_",
                "kesan": "Lucu dan seru banget orangnya",  
                "pesan":"Bahagia selalu kak"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat":"Lampung Selatan",
                "hobbi": "Nonton Drama Short FB",
                "sosmed": "@aphrhtp_",
                "kesan": "Cantik",  
                "pesan":"semangat terus kaka,semoga ceria selalu yaaa"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat":"Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kece",  
                "pesan":"Mantep banget kak"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat":"Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Baik, ramah",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": " 123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Cantik dan lucuu",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat":"Gg. Perwira 2",
                "hobbi": "Menonton Alur Cerita Film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Baik, ceria",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Seru dan rame orangnya",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Ramah",  
                "pesan":"semangat terus kakak kuliahnya"# 1
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    SSD()

if menu == "Departemen Medkraf":
    def Medkraf ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Q1M3Q-yfxhFpcQ7XvMfVQLx9gnv2WjhF",
            "https://drive.google.com/uc?export=view&id=1IDHQIg_J-ZDV1gnT7-G9HSSrM-OS8-uN",
            "https://drive.google.com/uc?export=view&id=1hnjMfpIfGufnQsMqOIh-T_pg_rRiQhgN",
            "https://drive.google.com/uc?export=view&id=1va1qliNxkgMjmuL4OZPsb0DPaf9MvrEu",
            "https://drive.google.com/uc?export=view&id=1OJgLLpZQ1u9EdnGitBV5Pi9XBjwHK1OE",
            "https://drive.google.com/uc?export=view&id=1Sjmffo0wgN7JUYnG3cPBqovnFcHCzvwk",
            "https://drive.google.com/uc?export=view&id=1RvltU0koylHAXdQdwJPcuNkwjLOjQoBm",
            "https://drive.google.com/uc?export=view&id=1AY_OT_ZiKF3lPO9-RgJCDHe08pb4MdcC",
            "https://drive.google.com/uc?export=view&id=1LNG4pVYaDBSH9NL-YLKc3ogtg4FiaqhY",
            "https://drive.google.com/uc?export=view&id=13BA_r0z9zqKZR9owfUnJuC7Fhnw5QXGR",
            "https://drive.google.com/uc?export=view&id=1mkNhGZIuLpQ6txZ7Lde6NiZm0wtWTkPX",
            "https://drive.google.com/uc?export=view&id=1Tuz43Nim-DbkghuWNCrO3zDhUWReWJWm",
            "https://drive.google.com/uc?export=view&id=1dO3YdasQ9hKcK8T3t7bfKmiGTgicrN30",
            "https://drive.google.com/uc?export=view&id=1X5YlTp7hZORRGK9E2c2ROioy5Wok4cxf",
            "https://drive.google.com/uc?export=view&id=1OfR2UXg-hgFAjEo5gOd-fOyydQ_QoTRI",
            "https://drive.google.com/uc?export=view&id=1cfgoQ2WR78IEJrYvzSHy2XojLlg71CwK",
            "https://drive.google.com/uc?export=view&id=1QW8eG3dxJANVA8AH842qPA66LQamf8vA",
            "https://drive.google.com/uc?export=view&id=1ly56W-iPALobdBeXUuiMdv_GToXLEVOB",
           
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat":"Jatimulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Sangat ceria, seru dan lucu. energi kak patricia kayak gak ada habisnya",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat":"Korpri, Sukarame",
                "hobbi": "Gym,masak",
                "sosmed": "rahmaneliyana",
                "kesan": "Cantik dan lucu",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat":"Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam",
                "kesan": "Abangnya asik, seru kalau diajak ngobrol",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat":"Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "PDD 23 banget, ramah, tinggi",  
                "pesan":"Lancar semua urusan ya bang"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat":"Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Seru kalau udah diajak ngobrol",  
                "pesan":"semangat terus bang, sehat selalu"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat":"Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakaknya asik",  
                "pesan":"semangat terus kak, sehat selalu"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat":"Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Kakaknya asik",  
                "pesan":"semangat terus kak, sehat selalu"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"kotabumi, Lampung Utara",
                "alamat":"jl.pangeran senopati raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Ramah dan humble",  
                "pesan":"Sehat dan bahagia selalu kak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat":"Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Pinter dan rajin",  
                "pesan":"Semoga kuliahnya lancar kak, bahagia selalu"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Cantik dan asik banget kakaknya",  
                "pesan":"semangat terus kak, semoga kuliahnya baik"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak cantik dan baik",  
                "pesan":"Bahagia selalu kakak"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh",
                "alamat":"jl.Lapas, kec.Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat":"Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat":"Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangnya baik, ramah, humble",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat":"Airan Raya 1",
                "hobbi": "Membaca, menulis,memasak",
                "sosmed": "@n1tg._",
                "kesan": "Terlihat pendiam",  
                "pesan":"semangat terus kak, sehat selalu"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat":"Natar",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Seru, baik",  
                "pesan":"Bahagia dan sehat selalu kak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat":"Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Cantik, btw aku juga dari krui kak hehehehe",  
                "pesan":"Sehat selalu kak"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat":"Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Asik banget",  
                "pesan":"semangat terus kak, semoga kuliahnya lancar selalu"# 1
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()


    















# Tambahkan menu lainnya sesuai kebutuhan

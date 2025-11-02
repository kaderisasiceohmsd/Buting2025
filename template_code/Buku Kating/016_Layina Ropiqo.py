
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
            "https://drive.google.com/uc?export=view&id=1WQOU1XgHWuhuqejkLu_HKjU5gAb4F-pS",
            "https://drive.google.com/uc?export=view&id=1SdgYKOKfyiNqrdNc18ss5HEJGkmSQKXq",
            "https://drive.google.com/uc?export=view&id=13hS7Qn82zZxqwHNTzA5TUg74vy-uRt8l",
            "https://drive.google.com/uc?export=view&id=1UPIP0PY4PtBQjjbmaaRce0MA5SCSIV3V",
            "https://drive.google.com/uc?export=view&id=1e6iKrDmoxcF2UCvDbNGtR0sl9RG7G9E5",
            "https://drive.google.com/uc?export=view&id=1EFxH-yQUhwBEpoIaDOnQYgLOgfb5Veej",
        ]
        data_list = [
            {
                "nama"   : "Rendra Eka Prayoga",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama"   : "Johannes Krisjon Silitonga",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama"   : "Elisabeth Claudia Simanjuntak",
                "nim"    : "122450123",
                "umur"   : "24",
                "asal"   : "Baduy Pedalaman",
                "alamat" : "Agres Kos",
                "hobbi"  : "Makan Kuaci",
                "sosmed" : "@celisabethh_",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Syadza Puspadari Azhar",
                "nim"    : "123450072",
                "umur"   : "21",
                "asal"   : "Palembang",
                "alamat" : "Belwis",
                "hobbi"  : "Membaca",
                "sosmed" : "@puspadrr",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Eksanty Febriana Sukma Islamiaty",
                "nim"    : "123450001",
                "umur"   : "21",
                "asal"   : "Wakatobi, Sulawesi Tengah",
                "alamat" : "Mutun, Pesawaran",
                "hobbi"  : "Ngomenin Tiktok Cewek Cantik",
                "sosmed" : "@eksantyfebriana",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Farahanum Afifah Ardiansyah",
                "nim"    : "123450056",
                "umur"   : "21",
                "asal"   : "Padang, Sumatera Barat",
                "alamat" : "Gya Kos, Korpri",
                "hobbi"  : "CUTE Jen",
                "sosmed" : "@farhanumafifahh",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14OP05UHw9bs6tg2bMt9tyv2re6ctd1ai",
            "https://drive.google.com/uc?export=view&id=1l-J8qqMPVv_Dq-DmV38uhHyVPNVf2Uqe",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=12WQGqORIOEra70Ykk2HKuk6kPtR54GeK",
            "https://drive.google.com/uc?export=view&id=1v5Dc6gMh4xip0XUTRy5mjgoPG-kzHCCW",
            "https://drive.google.com/uc?export=view&id=1GIhCnOCMq6U025dw9VTrZrFvZLh1HSJi",
            "https://drive.google.com/uc?export=view&id=1vmcOo1RkeipQ50Er-T7HHGxoAhrGHlAq",
            "https://drive.google.com/uc?export=view&id=1R8vLBUHO-hfyqiNA2NZ2IwK1ApwFVVaA",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=13DbtrrtOtw4JnsUKcLd3S4Q8E36sWyF2",
            "https://drive.google.com/uc?export=view&id=1jeCc5ImUJx8gGGe4_GvKOyt2Na5Wp85R",
            "https://drive.google.com/uc?export=view&id=1HVbp1PZxRWLYrmx_W7zlwVIbgdKiBR_d",
            "https://drive.google.com/uc?export=view&id=1bVADCH1npjcRMnA2f8jTyBqB6w7ONytC",
            "https://drive.google.com/uc?export=view&id=1KIZOv7BNdVNgEqT_mLdM-pjBn3f2XdVY",
        ]
        data_list = [
            {
                "nama"   : "Jeremia Susanto",
                "nim"    : "122450022",
                "umur"   : "21",
                "asal"   : "Bandar Lampung",
                "alamat" : "B2, No 2",
                "hobbi"  : "Zumba di PLN setiap jumat pagi",
                "sosmed" : "@jeremia.s",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama"   : "Dhea Amelia Putri",
                "nim"    : "122450004",
                "umur"   : "20",
                "asal"   : "Mojokerto, Jawa Timur",
                "alamat" : "Teluk",
                "hobbi"  : "Suka buat setan minder",
                "sosmed" : "@_.dheamelia",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama"   : "Renisha Putri Giani",
                "nim"    : "122450079",
                "umur"   : "22",
                "asal"   : "Teluk",
                "alamat" : "Teluk",
                "hobbi"  : "Jualan pancing",
                "sosmed" : "@",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama"   : "Anisa Fitriyani",
                "nim"    : "122450019",
                "umur"   : "20",
                "asal"   : "Muara enim, Sumatera Selatan",
                "alamat" : "C2",
                "hobbi"  : "Belajar Mengaji",
                "sosmed" : "@ansftynn_",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama"   : "Dharu Cahyoaji Sasongko",
                "nim"    : "123450023",
                "umur"   : "18",
                "asal"   : "Bandar Lampung",
                "alamat" : "Way Halim",
                "hobbi"  : "Bengong",
                "sosmed" : "@dhruchyo",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama"   : "Feby Wulandari",
                "nim"    : "123450042",
                "umur"   : "20",
                "asal"   : "Bekasi",
                "alamat" : "Way Huwi",
                "hobbi"  : "Menggodai abang cimol",
                "sosmed" : "@fby.wlndr",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama"   : "Givaro Ananta",
                "nim"    : "123450078",
                "umur"   : "20",
                "asal"   : "Lampung Barat",
                "alamat" : "Sukabumi",
                "hobbi"  : "Mendengarkan musik",
                "sosmed" : "@givarooo",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama"   : "Mirzan Yusuf Rabbani",
                "nim"    : "122450118",
                "umur"   : "21",
                "asal"   : "Jakarta",
                "alamat" : "Korpri",
                "hobbi"  : "Istirahat",
                "sosmed" : "@myrrinn",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama"   : "Berliana Enda Putri",
                "nim"    : "122450065",
                "umur"   : "21",
                "asal"   : "Surabaya",
                "alamat" : "Belwis",
                "hobbi"  : "Mengukir sabun",
                "sosmed" : "@berlyyyanda",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama"   : "Juesi Apridelia Saragih",
                "nim"    : "123450085",
                "umur"   : "19",
                "asal"   : "Kalimantan Utara",
                "alamat" : "Belwis",
                "hobbi"  : "Sibuk",
                "sosmed" : "@j__eesia",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Ridho Benedictus Togi Manik",
                "nim"    : "123450060",
                "umur"   : "19",
                "asal"   : "Medan",
                "alamat" : "Gang Sakung",
                "hobbi"  : "Main pedel",
                "sosmed" : "@ianridhomanik",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
             {
                "nama"   : "Feryadi Yulius",
                "nim"    : "122450087",
                "umur"   : "21",
                "asal"   : "Bangka Belitung",
                "alamat" : "Kobam",
                "hobbi"  : "Nongkrong di gedung F",
                "sosmed" : "@fer_yulius",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama"   : "Monica Patricia Tanjung",
                "nim"    : "123450073",
                "umur"   : "19",
                "asal"   : "Ketapang, Kalimantan Barat",
                "alamat" : "Belwis",
                "hobbi"  : "Memanah",
                "sosmed" : "@monca_tjg",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Wan Nashwa Alhasni Yuska",
                "nim"    : "123450077",
                "umur"   : "20",
                "asal"   : "Pekan baru, Riau",
                "alamat" : "Belwis",
                "hobbi"  : "Nyapa angin",
                "sosmed" : "@nshaysk",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18hbeh6VRlDNYiPRuu-gSRaxMGIZFwjHh",
            "https://drive.google.com/uc?export=view&id=1Vy8ZiNJ1uMeP3SIuXcAj4EmdXutmbq-H",
            "https://drive.google.com/uc?export=view&id=1BTqmlMXkTqW2zT-ejKWtrEwPZHt6gAvP",
            "https://drive.google.com/uc?export=view&id=1kBQ2kSU7anaU0zbpg1Z0DEFUqgnM8sll",
        ]
        data_list = [
            {
                "nama"   : "Rian Bintang Wijaya",
                "nim"    : "122450094",
                "umur"   : "20",
                "asal"   : "Palembang",
                "alamat" : "Tanya Caesar",
                "hobbi"  : "Padel",
                "sosmed" : "@i",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama"   : "Nadya Ratu Anjani",
                "nim"    : "123450089",
                "umur"   : "20",
                "asal"   : "Jakarta",
                "alamat" : "Belakang Indomaret Belwis",
                "hobbi"  : "Maen Roblox",
                "sosmed" : "@i",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama"   : "Fathinah Nur Azizah",
                "nim"    : "123450072",
                "umur"   : "20",
                "asal"   : "Jakarta",
                "alamat" : "Asrama TB 1",
                "hobbi"  : "Like Instagram",
                "sosmed" : "@i",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama"   : "Lia Hana Ichisasmita",
                "nim"    : "123450083",
                "umur"   : "20",
                "asal"   : "Bandar Lampung",
                "alamat" : "Sukarame",
                "hobbi"  : "Dengerin lagu",
                "sosmed" : "@i",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1v7_TugMNDohNn6UzFhDnNWYrtI5C9FLW", # Ketua
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Sekre
            "https://drive.google.com/uc?export=view&id=1Am4CkzFMmBQ7KA5bozrNMa3bVH7e-1_a", # Kader
            "https://drive.google.com/uc?export=view&id=1DakRsLOtzcUpvcVTX78R8Vgu4qeSt_QU",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1HnwfvsuowuJ3XI5haZDrVso05gDsN0iw",
            "https://drive.google.com/uc?export=view&id=1nONNhWLeiMEue91rYERX975trE7u-vl1",
            "https://drive.google.com/uc?export=view&id=1bdxJvsjCtDtj8fYobKDXtgnZLt6Se-aV",
            "https://drive.google.com/uc?export=view&id=1CKFPOAxZVh-SEpwJn9iM2XAM7QwsZjj7",
            "https://drive.google.com/uc?export=view&id=1ongA0PXCyPw97qXGQLZJbnDXMiwk0H44",
            "https://drive.google.com/uc?export=view&id=1RhAbCC3u1Alv6jgDXoGrCC-zac_t45Lp",
            "https://drive.google.com/uc?export=view&id=1-F1PIECRIoZRyvEztVrKFHAZWw9tOLOZ", # Mankom
            "https://drive.google.com/uc?export=view&id=13NKIQX_8sbFHzFH1v8yiL_OfW9WXyTLK",
            "https://drive.google.com/uc?export=view&id=1Wpqa_Mfu9pFTv1yMxiYXggScgtjparEe",
            "https://drive.google.com/uc?export=view&id=1-Ikdw_getIAT_CmpWkh0BxFvAIo9h8fj",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1n7zYC3CHqYXJvOxjhobhWVl6_LwvF1dc",
            "https://drive.google.com/uc?export=view&id=1Uo_8_mvxyMeTfoiDzPDW8pIkztdbSI1_", # Manjakat
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  
            "https://drive.google.com/uc?export=view&id=1HN_KK9b3jWuihdGmupdYg4IMg0VaNS_c",
            "https://drive.google.com/uc?export=view&id=1k0Am0OgOJlkn2SjbEwfdzAziMpHzwIFb",
            "https://drive.google.com/uc?export=view&id=18VFjY8F742YEbU1YCSLDDfqJ_benRI7Q",
            "https://drive.google.com/uc?export=view&id=1_7rd-ngR55UZJopBAb0I3Ns4BSBzdWb_",
            "https://drive.google.com/uc?export=view&id=1YLFBPxvkE7PsuG1026nB7ZZH2iY0VuKP",
        ]
        data_list = [ 
             {
                "nama"   : "Ferdy Kevin Naibaho",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"# 1
            },
             {
                "nama"   : "Nisrina Nur Afifah",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Allya Nurul Islami Pasha",
                "nim"    : "123450033",
                "umur"   : "21",
                "asal"   : "Sumatera Barat",
                "alamat" : "Gg. Pewira",
                "hobbi"  : "Main",
                "sosmed" : "@alyapasha_",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Ahmad Rizky",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Arienta Khusnul Ananda",
                "nim"    : "123450097",
                "umur"   : "20",
                "asal"   : "Kalianda",
                "alamat" : "Sebelah kost bang Dapa",
                "hobbi"  : "Liatin Haikal",
                "sosmed" : "@arientakhsnl_",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Daffa Hadyan Navista",
                "nim"    : "123450025",
                "umur"   : "21",
                "asal"   : "Sumatera Barat",
                "alamat" : "Sebelah kost kak Arin",
                "hobbi"  : "Isengin Fislam",
                "sosmed" : "@daffahdynn_",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
            {
                "nama"   : "Ginda Fajar Riadi Marpaung",
                "nim"    : "123450103",
                "umur"   : "20",
                "asal"   : "Cikarang",
                "alamat" : "Sama kayak bang Ahmad",
                "hobbi"  : "Banyak",
                "sosmed" : "@ginda_mrp",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
            {
                "nama"   : "Natasya Amavisca",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama"   : "Nobel Nizam F",
                "nim"    : "123450117",
                "umur"   : "20",
                "asal"   : "Bandar Lampung",
                "alamat" : "Gg. Pewira",
                "hobbi"  : "Ngekader",
                "sosmed" : "@nobelnizam",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Nurul Alfajar Gumel",
                "nim"    : "122450022",
                "umur"   : ".....",
                "asal"   : "Sumatera Barat",
                "alamat" : ".....",
                "hobbi"  : "Mancing Keributan",
                "sosmed" : "@ji_gumel17",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Vany Salsabila Putri",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Ahmad Sahidin Akbar",
                "nim"    : "122450044",
                "umur"   : "21",
                "asal"   : "Tulang Bawang",
                "alamat" : "Sukarame",
                "hobbi"  : "Bulu Tangkis",
                "sosmed" : "@sahid22",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Ali Aristo Muthahhari Parisi",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Gusti Putu Ferazka",
                "nim"    : "12345006",
                "umur"   : "20",
                "asal"   : "Bekasi",
                "alamat" : "Way Dadi",
                "hobbi"  : "Tidur",
                "sosmed" : "@ferazkaa",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Kharisma Mustika Sari",
                "nim"    : "123450034",
                "umur"   : "20",
                "asal"   : "Way Kanan",
                "alamat" : "Untung",
                "hobbi"  : "Scroll Tiktok",
                "sosmed" : "@rismaa.mustika_",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Rosalia Siregar",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Sahid Maulana",
                "nim"    : "122450109",
                "umur"   : "22",
                "asal"   : "Depok, Jawa Barat",
                "alamat" : "Airan",
                "hobbi"  : "Game",
                "sosmed" : "@Sahid_maul19",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Daffa Ahmad Naufal",
                "nim"    : "122450137",
                "umur"   : "21",
                "asal"   : "Jakarta",
                "alamat" : "Korpri",
                "hobbi"  : "Bersihin Jendela",
                "sosmed" : "@ahmadnaufal_11",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Erma Daniar Safitri",
                "nim"    : "123456789",
                "umur"   : ".....",
                "asal"   : ".....",
                "alamat" : ".....",
                "hobbi"  : "....",
                "sosmed" : "@i",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Ihsan Maulana Yusuf",
                "nim"    : "123450110",
                "umur"   : "20",
                "asal"   : "Sumatera Barat",
                "alamat" : "Pemda",
                "hobbi"  : "Servis Laptop",
                "sosmed" : "@ihsan.myusuf",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Kevin Antoni Junior",
                "nim"    : "123450109",
                "umur"   : "20",
                "asal"   : "Bandar Lampung",
                "alamat" : "Panjang",
                "hobbi"  : "Menanam Padi",
                "sosmed" : "@kevinaj__",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Lidia Natasyah Marpaung",
                "nim"    : "123450015",
                "umur"   : "20",
                "asal"   : "Medan",
                "alamat" : "Pemda",
                "hobbi"  : "Merajut",
                "sosmed" : "@dla_natzzyaa",
                "kesan"  : "kakaknya baik 😊",  
                "pesan"  : "semangat terus kuliahnya kak !!!"# 1
            },
             {
                "nama"   : "Muhammad Ridwan",
                "nim"    : "12345091",
                "umur"   : "20",
                "asal"   : "Kota Gajah",
                "alamat" : "Belwis",
                "hobbi"  : "Badminton",
                "sosmed" : "@m.ridwaan_22",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
             {
                "nama"   : "Uliano Wilyam Purba",
                "nim"    : "122450098",
                "umur"   : "19",
                "asal"   : "Depok",
                "alamat" : "Jl. Raden Saleh",
                "hobbi"  : "Ngoding, dan Bermain Musik (Angklung)",
                "sosmed" : "@_",
                "kesan"  : "Abangnya keren 😎",  
                "pesan"  : "semangat terus kuliahnya bang !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ovnbm23OC1bHqx-7Oqp4vwtV7ya5Wr4k",
            "https://drive.google.com/uc?export=view&id=1AyZ8O0dJdENQObr_phuq6MMM07udMOzw",
            "https://drive.google.com/uc?export=view&id=1hLrFXuOaV8WcGrsebIVl4IyvB_TnauGJ",
            "https://drive.google.com/uc?export=view&id=1gx5JA-eKAlySIBTKQC0pezBBfuC7JDnX",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1cOCAJsQgR0-HpayeTzhqaSCX2nDacBP3",
            "https://drive.google.com/uc?export=view&id=1IZDbSx0BNtVjjf_c6Q_vJjoPgwRWjprS",
            "https://drive.google.com/uc?export=view&id=1bVQwjZQpZwvxfvXr8uTup5lsbHrIsrYE",
            "https://drive.google.com/uc?export=view&id=1cZ8VLkTYfyVRJrDqXx-jqsnVO8b5-UQR",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1pXSfTA6kkyMAdmjl2vj121BjuoCuj7Yb",
            "https://drive.google.com/uc?export=view&id=1W84JwPs4A1it5kkQdgMCSUPUyEz66H1J",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1o9kpUckhidvUxMPUbvpU7ex-KXQobqhw",
            "https://drive.google.com/uc?export=view&id=1bRZPlztzNq6YmEeg_MHfADkZBwzAL2Va",
            "https://drive.google.com/uc?export=view&id=17aEVuCeiETy73HeDJiRIMo6zHy-uuVxL",
            "https://drive.google.com/uc?export=view&id=1CiviFzFP7_h1BFReeBbueqv9OVbKPJOw",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1uRoraLSXiOFKqYUqh3BKtlmBgfMA72nc",
        ]
        data_list = [
            {
                "nama"   : "Randa Andriana Putra",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Rut Junita Sari Siburian",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Muhammad Regi Abdi Putra Amanta",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Aisyah Musfirah",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Fadil Prasetyo Alfarizzi",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Muhammad Aqil Ramadhan",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Muhammad Naufal Ramadhan",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Nadia Faraj Alyafaatin Simbolon",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Marleta Cornelia Leander",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Akeyla Fairuz Shafi",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Anggi Puspita Ningrum",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Efi Defiyati",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Fabiolla Charissa Putri",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Fairuz Ary Syifa",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Tanty Widiyastuti",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Eggi Satria",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Afifah Fauziah",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Fabio Banyu Cyto",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Giofani Aristyo",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Rahma Oktavia Albar",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Rahmah Gustriana Deka",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama"   : "Razin Hafid Hamdi",
                "nim"    : "122450000",
                "umur"   : "18",
                "asal"   : "Bekasi",
                "alamat" : "Gg.sakum",
                "hobbi"  : "Mainn Bola, Belajar",
                "sosmed" : "@i",
                "kesan"  : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"  : "semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak A",
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
                "nama": "Kakak B",
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
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak A",
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
                "nama": "Kakak B",
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
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak A",
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
                "nama": "Kakak B",
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
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak A",
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
                "nama": "Kakak B",
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
    Departemen_Medkraf()

# Tambahkan menu lainnya sesuai kebutuhan
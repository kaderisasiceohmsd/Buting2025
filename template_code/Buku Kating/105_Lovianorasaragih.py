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
    kesekjenan()


if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/file/d/1caD2ghFiCmmgf-8zwFzttqX34SwFnift",
            "https://drive.google.com/file/d/1jlszDhveixiuVEK6-MCOvrQjm5MJjTh4",
            "https://drive.google.com/file/d/1bWBtoGDU4WhTYsugWklLWWDm-aHU1YVv",
            "https://drive.google.com/file/d/1ZSPLT6X2X-Ux_XgWTdLOTIn2O9txk2Kj",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "",
                "hobbi": "Mancing",
                "sosmed": "@",
                "kesan": "bang bintang orang nya humoris, sewaktu wawancara kami banyak ketawa karena lelucon dari beliau, beliau orang nya tegas dan bisa membedakan mana waktunya bercanda dan mana waktunya serius",  
                "pesan":"semangat terus kuliahnya bang, kuliah dibawa santai aja jangan pusing pusing"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450045",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger Lagu",
                "sosmed": "@i",
                "kesan": "Kakak nya cantik banget, kalau senyum lucu matanya ga keliatan, terus orang nya lembut bgt gitu sama ramah juga dan mudah tersenyum, vibesnya kaya cewe humble dan baik hati",  
                "pesan":"tetap ramah kaya sekarang ya kak, jangan lupa jaga kesehatan, jangan telat makan!!"# 1
            },
            {
                "nama": "Fatina Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "dengerin musik sambil jalan",
                "sosmed": "@i",
                "kesan": "kaka nya cantik banget apalagi kalau senyum, imut gitu terus vibesnya kaya cewe muslimah bgt",  
                "pesan":"tetap jadi tipe orang yang baik dan ramah ya kak!!"# 1
            },
            {
                "nama": "Lia Hana Icihai Sasmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jarta",
                "alamat": "Belakang indomaret Belwis",
                "hobbi": "Main",
                "sosmed": "@i",
                "kesan": "kaka nya lucu bgt kalau senyum matanya ga keliatan jadi keliatan imut gitu, terus kalau kami ngomong kakaknya yang bener bener merhatiin bgt gitu, jadi terharu ",  
                "pesan":"semangat kuliah nya ya kak, jangan lupa istirahat, jangan terlalu dipaksain kalau udah cape istirahat aja"# 1
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
# Tambahkan menu lainnya sesuai kebutuhan

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

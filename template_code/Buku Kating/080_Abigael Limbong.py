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
            "https://drive.google.com/uc?export=view&id=1hZbI0a_yhAqV1RdwIL4CJIGTtSBIPemI",
            "https://drive.google.com/uc?export=view&id=1grNZb11aTtYpOSPonOiUmQlcNTB09b0H",
             "https://drive.google.com/uc?export=view&id=1GXCNA6quUoo_vjS_L811AGxkFGClMnO3",
             "https://drive.google.com/uc?export=view&id=1nArmCr2GocuPpRPn2_MAv5rE3VeFnW_L",
            "https://drive.google.com/uc?export=view&id=16flvDqA6svuZU2m9exztomyQ125idHuN",
             "https://drive.google.com/uc?export=view&id=1lNhLE1H1NkTbbFi6N7hpPb7Wren3ulSj",
        ]
        data_list = [
            {
                "nama": "Kakak Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Makan Pisang",
                "sosmed": "@_erendraa",
                "kesan": "Kakak ini tegas dan ketawanya menular hahaha, asik banget!",  
                "pesan": "semoga selalu sukses dimana pun berada kakak !!!"# 1
            },
            {
                "nama": "Kakak Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini lucu banget parah!",  
                "pesan": "semoga lancar kuliahnya kakak!!!"# 1
            },
              {
                "nama": "Kakak Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini senyumnya manis, jadi suka deh!",  
                "pesan": "semoga sehat selalu kakak!!!"# 1
            },
              {
                "nama": "Kakak Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini pendiam tapi lucu, manis deh!",  
                "pesan": "Semoga sukses selalu kakak !!!"# 1
            },
            {
                "nama": "Kakak Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini tegas sekaligus lucu dalam satu waktu, sukaaa!",  
                "pesan":"Jangan lupa jaga kesehatan kakak !!!"# 1
            },
             {
                "nama": "Kakak Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini seru banget diajak ngobrol, suka deh",  
                "pesan": "Jaga kesehatan terus kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GssFMzoRbCwkWiQDvoT5E_IkjtR8uAJu",
            "https://drive.google.com/uc?export=view&id=1KV23gXma6AWwl7U8ZRjLdgTe_FWHoahO",
             "https://drive.google.com/uc?export=view&id=14w3iUtKO_YUypsET8QYnIvd13kHid53C",
             "https://drive.google.com/uc?export=view&id=151L2RoWLX0NHM4ga_oJayPcR3pmV_JZV",
            "https://drive.google.com/uc?export=view&id=15yOWLJSgO1GleNpPjQWJ38grdKQ7YOqa",
             "https://drive.google.com/uc?export=view&id=1VfZ-PSvsNHI03AsBgZvauo9_q8aH35P-",
            "https://drive.google.com/uc?export=view&id=1DVyXlMwFf4TNja5MZUCRVve7Z9uFzJlk",
            "https://drive.google.com/uc?export=view&id=1kXxgMLoBHNE2Qe9fJ58F8VHrNk7eY86E",
            "https://drive.google.com/uc?export=view&id=1S4cdEXqkmL73XmQZZANTi_hF0vTXVzmE",
            "https://drive.google.com/uc?export=view&id=1TpuYU3vt-9JFsE1076z5qjoK258VNocr",
            "https://drive.google.com/uc?export=view&id=1hDUdmPT1jS1sIAz2RtQaBGoHSs_nSh31",
            "https://drive.google.com/uc?export=view&id=1SdocdhBPqOJB-44b3P1w6S6K-t1Xb3Am",
            "https://drive.google.com/uc?export=view&id=1q8ezJRhP1GKjOdC02cWcRIlVs6Gv1QhA",
            "https://drive.google.com/uc?export=view&id=1m60QTcZLXNseW7awAieINFi1EgkD5PXc",
        ]
        data_list = [
            {
                "nama": "Kakak Jeremia Susanto",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Renisha Putri Giani",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Annisa Fitriyani",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Dharu Cahyoaji Sasongko",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan":" "# 1
            },
             {
                "nama": "Kakak Feby Wulandari",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Givaro Ananta",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Mirzan Yusuf Rabbani",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Ridho Benedictus Togi Manik",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Feryadi Yulius",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": " ",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bJiSw9OQ_B3IGAMnMYqkdUaFyXtl12ai",
            "https://drive.google.com/uc?export=view&id=1kQ_UKG693TchnUWBrQi43H3spdJ3dbo_",
             "https://drive.google.com/uc?export=view&id=1LzasgfP-hAMih41Y1hvI1ENm_yK8Ave2",
             "https://drive.google.com/uc?export=view&id=1nSNh-fkhR2vR8B40mIoRq4BKEFUVePWE",
        ]
        data_list = [
            {
                "nama": "Kakak Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini suka suasana santai tapi sopan, sangat unik!",  
                "pesan": "semoga semuanya dipermudah kakak !!!"# 1
            },
            {
                "nama": "Kakak Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini cantik banget, pangling lihatnya!",  
                "pesan": "semoga akademik nya diperlancar kakak!!!"# 1
            },
              {
                "nama": "Kakak Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini independent women looks banget, jadi inspirasi aku!",  
                "pesan": "semoga sehat selalu ya kakak!!!"# 1
            },
              {
                "nama": "Kakak Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini pendiam tapi lucu, manis deh!",  
                "pesan": "Semoga kuliahnya lancar selalu ya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

# Tambahkan menu lainnya sesuai kebutuhan


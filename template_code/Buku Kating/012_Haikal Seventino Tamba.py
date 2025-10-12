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
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_WB-NQPJkRrss8lPdH1Ci6h0idlOAOqT",
            "https://drive.google.com/uc?export=view&id=1HGA0CUrN0ae4Xjq5KgYLZvUuQMLDYsoL",
            "https://drive.google.com/uc?export=view&id=1AYrddRJ6ZoZMAmNa8VyAN8SvNeeM6zkb",
            "https://drive.google.com/uc?export=view&id=1Qy2fYRpPfvWd2bob3cowe7iK5w45CGhf",
            "https://drive.google.com/uc?export=view&id=1QjZQ8Jpktnr3A_yODp677gOQizoU4kXX",
            "https://drive.google.com/uc?export=view&id=1PN_-OJtGFpi9nK-GkjPjTz4rQIv3u-AH",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Eksanty F. Sukma Islamiaty",
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
                "nama": "Farahanum Afifah Ardiansyah",
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
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VV-UMjrLh6Mf8ZddtIN5etmWHa6pQ9Qf",
            "https://drive.google.com/uc?export=view&id=1LV3--Cx04GdfMLbI3uKFvsgjnQOEyE1I",
            "https://drive.google.com/uc?export=view&id=1pDQnGwnZ5kOEg-eJO5qsmXTTXN-gJboh",
            "https://drive.google.com/uc?export=view&id=1y7-pA5gAcW4iqdJDLs0lRFAp-ZHA_S4D",
            "https://drive.google.com/uc?export=view&id=1IL7aXgCeFnPodip01b-6Pgkn8FbuVqUI",
            "https://drive.google.com/uc?export=view&id=1qSyu-jCfFI-o1TAqeKEwUPnuUyXdT2HH",
            "https://drive.google.com/uc?export=view&id=1eMZWzh3GHByVVHko57VGSCoe5uikZ5ED",
            "https://drive.google.com/uc?export=view&id=1MzKseHR-QS0tWvOVNmLX26FLRVe7Esu2",
            "https://drive.google.com/uc?export=view&id=1VYnC0TIWhKfqI_dlqfcs_o2U05Mg2Ceh",
            "https://drive.google.com/uc?export=view&id=1AnpppechrkiE8RJcJRdwboRDlQ6tJl-f",
            "https://drive.google.com/uc?export=view&id=124GLVqtY4OAVmVR1vehWvCpM1-wZNNzS",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Eksanty F. Sukma Islamiaty",
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
                "nama": "Farahanum Afifah Ardiansyah",
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
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11bi2dbfC31wYoaQY4y1OGrtjHl0NuNNt",
            "https://drive.google.com/uc?export=view&id=1n2Brbge63t-kgfyQpDVLACZM83Et4Ogh",
            "https://drive.google.com/uc?export=view&id=1hIktfWN7u1z1rWaxOHBU-axdPgFzE2i9",
            "https://drive.google.com/uc?export=view&id=1sI19IKU-rqTLh6zx8HhUPB0DBpIFRePr",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
    Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1B4Cju3iOJo0UlGgiK0j1f5FqeDpUunVc",
            "https://drive.google.com/uc?export=view&id=1kBnCMjAF_sOPq8-_3-u78ZWBpavlI6td",
            "https://drive.google.com/uc?export=view&id=1YzwTnsBKVkpuyZHW_Z5x9rQjkA9aVXPZ",
            "https://drive.google.com/uc?export=view&id=19a4THVFJD-VO4Bj0vqpWOdnFEFojkmF2",
            "https://drive.google.com/uc?export=view&id=15yA6VqfEXA_dpobtETXsdcWvL8hMyTkf",
            "https://drive.google.com/uc?export=view&id=1u1Ns4bU3rjub_wjrocF7R3gaXcLqVnd-",
            "https://drive.google.com/uc?export=view&id=1j_YXEhCnjLbyKlLzQP0uGjULOvgX0MoW",
            "https://drive.google.com/uc?export=view&id=1_yWmebiu7FAmrFvwRsBLRRCjaejmjNPh",
            "https://drive.google.com/uc?export=view&id=1S4oOT3rFraGReo9UZ21PBtBE5T91aF7d",
            "https://drive.google.com/uc?export=view&id=1bW3dW2DraOxBHuhRQg4WPwokOvjJUOaw",
            "https://drive.google.com/uc?export=view&id=1_XxF5WsUzI4lIs-K4nZ9LZCvv2xn_p8T",
            "https://drive.google.com/uc?export=view&id=1YcmFg-1dI6MaZT6cI4mH52pPnS0Sn1cG",
            "https://drive.google.com/uc?export=view&id=1hBPf8e9_28XBYUGzFh90SXv_0qBhMF8U",
            "https://drive.google.com/uc?export=view&id=1F6TPZA17FV3jA2WXoEwsCDXMwtsezsYd",
            "https://drive.google.com/uc?export=view&id=14jY6GeVpA9w0Tk-sZ5mLl3YcvntrvQc-",
            "https://drive.google.com/uc?export=view&id=1Bi_r-C_Vqe4JXJkuHAasomEQgIy-16ab",
            "https://drive.google.com/uc?export=view&id=1VlSwjFMQhunEdUFcv4c8uMVR_W4TexZO",
            "https://drive.google.com/uc?export=view&id=1jgEDKMXqJkPMNu8qkk70A0hf0bGfNcUW",
            "https://drive.google.com/uc?export=view&id=1oYEusnV101ccDcQPLoOoKT1rsCBFzl3G",
            "https://drive.google.com/uc?export=view&id=1njqrQ71JJjdPZFAP1CLOtPfAkXiJRWi1",
            "https://drive.google.com/uc?export=view&id=1NZUPEePH2GzzikmUUVIZcFuYsoxLePLF",
            "https://drive.google.com/uc?export=view&id=1Wr7qLish-iokII7WtURBaWRyy0LgCZ2i",
            "https://drive.google.com/uc?export=view&id=1PgqJ6Xu8WtPJsCnzQ6jqAOrcjAjziiC2",
            "https://drive.google.com/uc?export=view&id=1cx24Bo1mvnSPS8YS1SCu1kFIlO_Hkepi",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",

        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Eksanty F. Sukma Islamiaty",
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
                "nama": "Farahanum Afifah Ardiansyah",
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
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gSYkrxPmG-xs0HAlK-TUoWuOizMnwTVQ",
            "https://drive.google.com/uc?export=view&id=1frAjl8bEEdFBovycir7eaKk0-gSKkof_",
            "https://drive.google.com/uc?export=view&id=14b6YL1hihi05GM8dv0fvimZ7bMGvuAFP",
            "https://drive.google.com/uc?export=view&id=1evKwlESkMjSaeSUODpI8YsHJp95EuAJX",
            "https://drive.google.com/uc?export=view&id=1ik2yqMvpnbbDIJRh2MybsbEcngJr52ra",
            "https://drive.google.com/uc?export=view&id=15Zh5X9Hi0aI68Zi95UwP6QnfHedaR9hD",
            "https://drive.google.com/uc?export=view&id=1lpXwk9ivPl3rIa7r26IwXM7o_a6mjoPE",
            "https://drive.google.com/uc?export=view&id=1ZngTckxRwkWcUycToZcnzBiaNj7OeM9Z",
            "https://drive.google.com/uc?export=view&id=16WgmAzCcrxfLONhnW64NLOIdOT8V2XYN",
            "https://drive.google.com/uc?export=view&id=167sSYVQjQAAegFdvdBRtpWyXaN2Ewis",
            "https://drive.google.com/uc?export=view&id=1WEhLKDq5uOEJYXV6CuzZRcA61bbJeWVo",
            "https://drive.google.com/uc?export=view&id=1pgfT9qwwxUvgdDmaZx9BVVKXhAHa1Sf7",
            "https://drive.google.com/uc?export=view&id=1y2qMqAsmhJXsEjzYuk9w49Y0Sz4c4BF2",
            "https://drive.google.com/uc?export=view&id=1HW73JV00NPjN1jMgjv_trjPUxT1E_VAb",
            "https://drive.google.com/uc?export=view&id=10-V-21q-aRQ5W7odvtT9vonbLCaHHpvI",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Eksanty F. Sukma Islamiaty",
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
                "nama": "Farahanum Afifah Ardiansyah",
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
    DepartemenMIKFES()
elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17dddvI3xPAd8NXG6ykfbRn60-zuHbmV2",
            "https://drive.google.com/uc?export=view&id=13DhBwONB40QqRjsPy2gijhZasUfnRScs",
            "https://drive.google.com/uc?export=view&id=1Z-Gsosi9PCV-YYMlRXxEkgrpALQbOnuW",
            "https://drive.google.com/uc?export=view&id=16A99-avAX8lotrrh6XjsOZLmDP0RkoGM",
            "https://drive.google.com/uc?export=view&id=1_U-zd2iy8xoH9l3_34QL7MDGA3SOB8zy",
            "https://drive.google.com/uc?export=view&id=1PynEKmKiz6bRwpSK-29aq1I9K1QhHtZA",
            "https://drive.google.com/uc?export=view&id=1xA1DMrXMoIIjV0HczaT90PTL16zRNOl7",
            "https://drive.google.com/uc?export=view&id=1e7rbR6wHeMXP6fYtT1pSWcvdo71-QEYh",
            "https://drive.google.com/uc?export=view&id=1IL3Tn49YNH7oWu_liDcOa1LZPIJ1p94J",
            "https://drive.google.com/uc?export=view&id=1LY123azxldzhmA0-8RJV6J_RdxZ0CT3M",
            "https://drive.google.com/uc?export=view&id=1Su7Ip1y5istQY5CxxYQSakxJ3_niANTl",
            "https://drive.google.com/uc?export=view&id=1i2gH6IQx7xR0tWT1djVtKXBARDOHoLL4",
            "https://drive.google.com/uc?export=view&id=1ZIr-ns0hbYxpXC7noJlsN44QJ2ewW5f3",
            "https://drive.google.com/uc?export=view&id=1LbHU6zB_iw7bPVI3IMyRism0xONWNQJM",
            "https://drive.google.com/uc?export=view&id=1b2qmvDQehY6tC5ro3mLXUx5-COVDUxsG",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Eksanty F. Sukma Islamiaty",
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
                "nama": "Farahanum Afifah Ardiansyah",
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
    DepartemenInternal()
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QBofuizBMIDilRZhxwa8XOT2AC8X5HM5",
            "https://drive.google.com/uc?export=view&id=1PoS8k0JsZvbri9l0Yt2T4OiQKjVdODLx",
            "https://drive.google.com/uc?export=view&id=1jGP6MMdzQ9_vu7c7fiQalsLJsU9qWwcT",
            "https://drive.google.com/uc?export=view&id=1s731J1qE689sO3iTAIxc3xm3ArXt4FRU",
            "https://drive.google.com/uc?export=view&id=1xZjkql4YHDxqV-6kOuReK-py3qcFAxtm",
            "https://drive.google.com/uc?export=view&id=13ObdS5lUXShQ-TIvugdA88JNXtI7m0Ny",
            "https://drive.google.com/uc?export=view&id=1CVi8BgqfKEqtt_eM__uwdXij947ggZdV",
            "https://drive.google.com/uc?export=view&id=1-cpqNbRABqdmSEKr4fozQqQ9ya7-M8u9",
            "https://drive.google.com/uc?export=view&id=1dTaaGPPTxqbQqck2x5nSTNEoX5e1NqiQ",
            "https://drive.google.com/uc?export=view&id=1Yg4nAsK5RTBwPy9yjS5vgyEoIyjjjsbE",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Eksanty F. Sukma Islamiaty",
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
                "nama": "Farahanum Afifah Ardiansyah",
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
    DepartemenSSD()
elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pZ86rav6B7u5r0EMww6c5vZCOsObPe0Q",
            "https://drive.google.com/uc?export=view&id=1Gis3pvtPkdN4weHiRjs29he8F4M0XxYl",
            "https://drive.google.com/uc?export=view&id=1IqRlXMABmg5OV31NyY0kBJcFuE8BANLM",
            "https://drive.google.com/uc?export=view&id=1z7dIV5sXhCszKMIzLdGvbvLTjcj4z05U",
            "https://drive.google.com/uc?export=view&id=1XMTxHe2mRXEaLVWLVdN6hL3YRHPIiF7R",
            "https://drive.google.com/uc?export=view&id=11H8ZHFs3qzfen0sr1uCT_FNmL-QtcO9a",
            "https://drive.google.com/uc?export=view&id=19bKBw01Po6i6Mh2qBeuusbK7av-gsrLn",
            "https://drive.google.com/uc?export=view&id=1nfoTqp6LnvtMkdXZk4J9Q5ueFiKs0l3v",
            "https://drive.google.com/uc?export=view&id=1sJKYFQXvVpWmWLZT5gMt5TvSTplwnlsr",
            "https://drive.google.com/uc?export=view&id=1PdRadHuoNBTRYrgOB6XgyAkMM3nx_KKF",
            "https://drive.google.com/uc?export=view&id=1Vz4SF07jNikYsZ7fInLWS-IxUTaFuZ9T",
            "https://drive.google.com/uc?export=view&id=1M7MeLZZ8L3wTEy63S8p-ZWqLuvB0eoWb",
            "https://drive.google.com/uc?export=view&id=1kkk2nilDCOQu0IyKYOyXKzr2DffGUnak",
            "https://drive.google.com/uc?export=view&id=1IMJ75kwBge9_qSAp_QeNN-Sr1jl8qtfF",
            "https://drive.google.com/uc?export=view&id=1KWEUbWUMFxjLA5TiBOwTI52d5cPSbSqu",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
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
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
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
                "nama": "Syadza Puspadari Azhar",
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
                "nama": "Eksanty F. Sukma Islamiaty",
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
                "nama": "Farahanum Afifah Ardiansyah",
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
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan

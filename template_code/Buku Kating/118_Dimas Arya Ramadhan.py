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
            "https://drive.google.com/uc?export=view&id=1xMvE_pLzylMrTdOXh__H67OBNLilsMt_",
            "https://drive.google.com/uc?export=view&id=1t01AaDDojMaVPbnx7SUiu3Jo33psbSfX",
            "https://drive.google.com/uc?export=view&id=1ChE0uFJps3Gq8uW4FDPQhBoyUtTkTWmp",
            "https://drive.google.com/uc?export=view&id=1y2GtPSrRCcOAuD58hsH37PNvAFG8koDT",
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
            "https://drive.google.com/uc?export=view&id=1RiSPHKEpEh2ZbJXiv-Horc0xPUWyKHyc",
            "https://drive.google.com/uc?export=view&id=1Kb_uZtko2y0AEuQEPFhsMGpIetX8tPrZ",
            "https://drive.google.com/uc?export=view&id=1nf-azSQKdXkhYc1cZLyZ_zdgeTmbIkkC",
            "https://drive.google.com/uc?export=view&id=1Yxk88Ed1D6c41zsw4hUZggdWXU5vRTWL",
            "https://drive.google.com/uc?export=view&id=1TeV4yyD1t0fIUeq5XPc0t3nS1BjsaIbP",
            "https://drive.google.com/uc?export=view&id=1Tol2zD49TgIPLcfGaAi--LdhiP1zdjnt",
            "https://drive.google.com/uc?export=view&id=13iwCDdSJhuDz5Px1gRyjUeBEoXfJOnTv",
            "https://drive.google.com/uc?export=view&id=1I86LE4ZPcRvFpSyRJkANCPU9RTJNgBai",
            "https://drive.google.com/uc?export=view&id=1_gYz_dKfxXWGwfwnsbaPKzqQxGryW03I",
            "https://drive.google.com/uc?export=view&id=1IofieIE0bmUQ9pKuMqmXR_Rue0v2wKbd",
            "https://drive.google.com/uc?export=view&id=1T4vhkntx5H0UYevDhHindfqiRo3708At",
            "https://drive.google.com/uc?export=view&id=1nC26N2Ot5561b8l9xdut3NAQ5tZuUNfK",
            "https://drive.google.com/uc?export=view&id=1UC8oQd_pixTrb6NcoyQjQcXluVJIOm9P",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
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
                "nama": "Dhea Amelia Putri",
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
                "nama": "Anisa Fitriyani",
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
            "https://drive.google.com/uc?export=view&id=136IUapnrHa1QLJHSwCWIeo50o3RcwdIp",
            "https://drive.google.com/uc?export=view&id=1uZNcipAknrldg__dyrgO4EmGclopr8mg",
            "https://drive.google.com/uc?export=view&id=1CCH6IHZdo5Kt-5qhaoNF6HiLVmvpUKTV",
            "https://drive.google.com/uc?export=view&id=1ToZUuWPNWhcQq59WkQO5aNZ2EgX62K8w",
            
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
    Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CQCScAosYO6Hcx7WQ5xugJMeX_GRmkFX",
            "https://drive.google.com/uc?export=view&id=1mOq2MUgK8zkrgZTSH6DSBVWrpaJM-YRa",
            "https://drive.google.com/uc?export=view&id=1Jx-AltKcfXZvYHgm7JyEG7Rt4n9hf1V4",
            "https://drive.google.com/uc?export=view&id=1eFyNNyW79aJqTAemt8noIWtK62lEc7LT",
            "https://drive.google.com/uc?export=view&id=1VZF0Fg1yJ6o-Ndt8m7Q-dj6XvTJwwnr-",
            "https://drive.google.com/uc?export=view&id=16rvEtU1b3BOCn4WCkRiy5WOMP-m5FfHY",
            "https://drive.google.com/uc?export=view&id=1N2nVOsHnfquecf8PczUFtaKrLkvT4ndh",
            "https://drive.google.com/uc?export=view&id=1DQNkX8ThW7zg1lcS6VM8RHjdkH5enfi7",
            "https://drive.google.com/uc?export=view&id=1e9xdqLgW9Tqz351Zcxgyriv41A6lzqSW",
            "https://drive.google.com/uc?export=view&id=1TfLtfV9HnIU_HhcPyb9dTNBL4xj7DxyL",
            "https://drive.google.com/uc?export=view&id=1qPCx7XYhyvtwNqeLO3EDpbGzBlY9yUw0",
            "https://drive.google.com/uc?export=view&id=1G_7j_f6noBu03igEWZu-n8qGA2AHmi8Y",
            "https://drive.google.com/uc?export=view&id=1NQnkigmkZWpToeeh-7JhVLb6EG1zkACF",
            "https://drive.google.com/uc?export=view&id=1Mz5Y8kj3wIjHFE8qfK0oGumxzPduOhGw",
            "https://drive.google.com/uc?export=view&id=1NXL4gre4-s2ad9bLADpcr6dfyyPtNaOX",
            "https://drive.google.com/uc?export=view&id=1OqSaI--RUKzz2vZ5ctfCh-A73L5AUXwF",
            "https://drive.google.com/uc?export=view&id=1GkhT2gGvXVt9XGEdKPZb7-6hefMDmyXy",
            "https://drive.google.com/uc?export=view&id=1Ggt6CpinaA1G_QZoJBzDCHqPPTOKrqQt",
            "https://drive.google.com/uc?export=view&id=1c6APLNbcunMsoWLaLziDoS7c3doIO8n4",
            "https://drive.google.com/uc?export=view&id=1UQ5sXLnF5U6uy47dxSIpNFQ3sFW0vRVQ",
            "https://drive.google.com/uc?export=view&id=12km0nj9023D0v0ojrWnpzcR-IykCevC2",
            "https://drive.google.com/uc?export=view&id=1K6L9sagqUSY6lxWKevAOWQU4J-3wlaGV",
            "https://drive.google.com/uc?export=view&id=15py_9C6BujUwYD2l6wzaiA8n0m7xoMWg",
            "https://drive.google.com/uc?export=view&id=1hMRtFB2ybZtEP-A_yX9k0K-QoiaRSBsG",
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
            "https://drive.google.com/uc?export=view&id=1-IIOTZ9Jw3Wpdpo9gmsxjj9yYaU2iO9-",
            "https://drive.google.com/uc?export=view&id=1T5m77aDduYFgRmJOJxzwQqT_XwwQhsiJ",
            "https://drive.google.com/uc?export=view&id=1ltDKfzUihoHVI6pkgvDsXMriyqmUOtjd",
            "https://drive.google.com/uc?export=view&id=1zHs1xnjPh4KiLp6eUeoGXiDhBb8uPSCF",
            "https://drive.google.com/uc?export=view&id=1u2IMCW4uCmO44s8xZ64Sz8VOcWjdaYGM",
            "https://drive.google.com/uc?export=view&id=1Mxw8qDkgbU61tgyejigSVsJ7Q-gbxKHE",
            "https://drive.google.com/uc?export=view&id=1HfaLy-k9s7GqKXZ77ef50fEt9SOeF6N2",
            "https://drive.google.com/uc?export=view&id=1UERFA1hGPmf1Ixq9APeEPnMJac-FIWB6",
            "https://drive.google.com/uc?export=view&id=1jaHAgR-Klw84ix6cUXr2OGsDVa0qFuo4",
            "https://drive.google.com/uc?export=view&id=1UStg1iCneXp8EVxktYl9R5Rm5RVqyeeE",
            "https://drive.google.com/uc?export=view&id=1OME1GaPP52N6P1vWmKbteUPeMgwgvebB",
            "https://drive.google.com/uc?export=view&id=1crVpsWitdlTA6iJvLSG_iUGy7d0pTtP4",
            "https://drive.google.com/uc?export=view&id=1kBckMXvwkAEVlH33oTDhmD2CoTloO13y",
            "https://drive.google.com/uc?export=view&id=
            "https://drive.google.com/uc?export=view&id=
            "https://drive.google.com/uc?export=view&id=
            "https://drive.google.com/uc?export=view&id=
            "https://drive.google.com/uc?export=view&id=
            "https://drive.google.com/uc?export=view&id=
            "https://drive.google.com/uc?export=view&id=
            "https://drive.google.com/uc?export=view&id=
            "https://drive.google.com/uc?export=view&id=
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
            "https://drive.google.com/uc?export=view&id=1HF8rq7dguk89sdJa2N5S8bHWgQxRCv1k",
            "https://drive.google.com/uc?export=view&id=1kGWXk7BbcbvQ9z9GhOgY9Ji9aO_hK3T1",
            "https://drive.google.com/uc?export=view&id=1xyIC1f3l9pEYUyXHY-XKfpMUnqfGanQI",
            "https://drive.google.com/uc?export=view&id=1VRyNvKXKXWCTa2wlQleYSyI99hiEzYue",
            "https://drive.google.com/uc?export=view&id=1jLWLGpKof_mXSf0f8E3owbRyQ6lj_mxi",
            "https://drive.google.com/uc?export=view&id=1Hja8NK82J-pOh36bN7bFSZG0gY_ex7IZ",
            "https://drive.google.com/uc?export=view&id=14pv1PwcQDx8L1GOCarxnH84gnkzwB9UW",
            "https://drive.google.com/uc?export=view&id=149f2hwvqUNZiN7t7ltmLbyQVLlPpEQ3h",
            "https://drive.google.com/uc?export=view&id=1aNgbV6J34MDpG-acdWxpxQcV_frs8MsJ",
            "https://drive.google.com/uc?export=view&id=1V7AmzkjDFkyXoUdva8hh-BE3vtlTyl4E",
            "https://drive.google.com/uc?export=view&id=1Q2A0xS1Z_DbnmK65CMm_TjCncoHNf-UA",
            "https://drive.google.com/uc?export=view&id=1hU-q9cLOQBEu3ho_31VXFQLVq3rzEWb1",
            "https://drive.google.com/uc?export=view&id=1zz-Hsydg5wfOFZQIiNm56nqg1XVVuQ9M",
            "https://drive.google.com/uc?export=view&id=11YME-upTb3qibrl6PkUnCW01pdwKfnSP",
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
            "https://drive.google.com/uc?export=view&id=1EQoHi_8fZCTrAlUYqhQmz6NkcvPFSc1R",
            "https://drive.google.com/uc?export=view&id=1cGzpDKSZIs7kajDtAOojeLQDhQonIGuV",
            "https://drive.google.com/uc?export=view&id=1QNP7b4sGmgvE184voGYqb5Fbc3G_AHho",
            "https://drive.google.com/uc?export=view&id=16hPakw_J_UwHZGShPVyHamiA_qzqIl9l",
            "https://drive.google.com/uc?export=view&id=1e5CZxhBalboOIscv3W_Yq30eOyN7OCUK",
            "https://drive.google.com/uc?export=view&id=1wAzaH7FIN-fGnDfOQ6EKsV-lVgrTnLDQ",
            "https://drive.google.com/uc?export=view&id=1QtMygnJfPs6iHu-VBlvZ8sxNLNzbA2e-",
            "https://drive.google.com/uc?export=view&id=1g8zl3iipD8oVu7OSAmbUrxnrcr9Wb_Q9",
            "https://drive.google.com/uc?export=view&id=1Ng33ZZqq-utgXIn6PcTdF5_wTHghf4bh",
            "https://drive.google.com/uc?export=view&id=1HD0ynLqtzfQXf2RkPuboQIEOmxJbTBrG",
            "https://drive.google.com/uc?export=view&id=190OpCX_txM6qdHQqnarOesLfVF_g7qgn",
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
            "https://drive.google.com/uc?export=view&id=1mAUvSkus38OfiiZrhKR8xF2ptz9p61B5",
            "https://drive.google.com/uc?export=view&id=15c_8H2tRJS9S8NDhTI_qsCdjmG4-nPd2",
            "https://drive.google.com/uc?export=view&id=1K376cj0H5eUCf4TcgT05GRVH8oRGeben",
            "https://drive.google.com/uc?export=view&id=1jz15_i8UVTHwjFP9hc9FJQ3mVYtPqWGc",
            "https://drive.google.com/uc?export=view&id=1DllubXQl3Mq5aJV7tvdDREaGETlZhx6y",
            "https://drive.google.com/uc?export=view&id=18KE94DsVSeoK76edK_cBkuDVWU5fkAp3",
            "https://drive.google.com/uc?export=view&id=1g6mjXMl9CeZo_w6JW7y0GJSBs-oGYa09",
            "https://drive.google.com/uc?export=view&id=1UM2NKlyCPROLrd5uWa44muFVnUXxaYwy",
            "https://drive.google.com/uc?export=view&id=1EWJdsY49NQv9lEuaxkvI-k77D1y3_EMp",
            "https://drive.google.com/uc?export=view&id=1Tf4NN-q4bQ7vZ7Y7J3F8UqcM4cXkd3hn",
            "https://drive.google.com/uc?export=view&id=1Fc4oTdCQITwfk0RJ7zv4PjxZz44LXLUn",
            "https://drive.google.com/uc?export=view&id=18314jQVWkYbK7Yysx79JN2ZgA_hR9-BL",
            "https://drive.google.com/uc?export=view&id=10y0N-3P1d7UqCdbMM_sBHAjYHzE2b7BN",
            "https://drive.google.com/uc?export=view&id=1GsjgEjAX-2r_PIsTEGkh_EcKPm0d7mIL",
            "https://drive.google.com/uc?export=view&id=1hUolIGOB85Q-seJ6mcapBXzMgvzH0xCa",
            "https://drive.google.com/uc?export=view&id=18g30O2CMq1kv4XmSSiVI9byXMFgudiPo",
            "https://drive.google.com/uc?export=view&id=10sw-rWfw3IhQpD_ugXkYm2NUMINB6Njb",
            "https://drive.google.com/uc?export=view&id=1chEEqBkZYP2Q_kIzslQuRtKdkb9cXCJe",
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



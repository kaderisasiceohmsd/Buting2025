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
if menu == "MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zDyb2jWOrSIUjefaMx8Qjq2NqK1BAtqD", #1
            "https://drive.google.com/uc?export=view&id=1okA5q5l6knMfJqYkeG5BmW4ywpYvrd1N", #2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3
            "https://drive.google.com/uc?export=view&id=1oplAcBSKO7YHI1CZwxx-BZJeoXCTXmiJ", #4
            "https://drive.google.com/uc?export=view&id=1rYBE8o6ocWkk1TukUdL-pgPV9JaTszne", #5
            "https://drive.google.com/uc?export=view&id=1exf_Gj41yxjWWf8daLBY_ggY-JvGw-SJ", #6
            "https://drive.google.com/uc?export=view&id=1G5S2q2WQ6DoQJ6I05s111vxPH7VXI75u", #7
            "https://drive.google.com/uc?export=view&id=14JpMF10-GAjGz_UpqQDg5E1iG5ziQwuM", #8
            "https://drive.google.com/uc?export=view&id=1ghrY9X9HsI1kXUTMU-aMD5mJ2BLCjx7X", #9
            "https://drive.google.com/uc?export=view&id=1iqPURv0FE8Q82UiH0VNS3fg74C5lQ5hT", #10
            "https://drive.google.com/uc?export=view&id=1w1SGEil3cSe4cBiwj1Kgfx8ycFsccyht", #11
            "https://drive.google.com/uc?export=view&id=1pIQMzYQXFljXHf39fYzk_03gjE-CYTGo", #12
            "https://drive.google.com/uc?export=view&id=1HLjJ11WiTejwxPSWZ7FUPxLB3oA5Cv41", #13
            "https://drive.google.com/uc?export=view&id=1TrAe8nBZwmytx5oroOou0rcgSKsJR-_u", #14
            "https://drive.google.com/uc?export=view&id=15sr1oF49UG60CfxeWzxbUhTs4ZJH6WhV", #15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #16
            "https://drive.google.com/uc?export=view&id=1MmxJdkzyUTwe-0IzNJtshA0iysOUP7Z0", #17
            "https://drive.google.com/uc?export=view&id=1b_VjtsD-Fu7vUyiBa-o7vSUY8kUHkefk", #18
            "https://drive.google.com/uc?export=view&id=1PyqkcO5Vd7jAI2HLX_i0ldvD8ofM-8wH", #19
            "https://drive.google.com/uc?export=view&id=1ykVfNXmRGD1a99OsjtZ64CpRv1ptxPrE", #20
            "https://drive.google.com/uc?export=view&id=1HxfjKjMGGRJlDGpeSBAsOjDPZENFGMmO", #21
            "https://drive.google.com/uc?export=view&id=19FzoXx61BGZereezGqQZZEfnzWZ_7_Jv", #22
        ] 
        data_list = [
            {
                "nama": "Kakak Randra Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kak Randa asik, wawasannya luas",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
            {
                "nama": "Kakak Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak Rut asyik dan keren",  
                "pesan":"Lancar-lancar kuliahnya kak Rut"# 2
            },
            {
                "nama": "Kakak Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak Regi kadiv PSD keren",  
                "pesan":"Semangat Kak Regi, terus menginspirasi"# 3
            },
            {
                "nama": "Kakak Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak Aisyah keren cara berbicaranya",  
                "pesan":"semangat menjalani semester 5 kakak"# 4
            },
            {
                "nama": "Kakak Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak Fadil keren banget jadi duta genre",  
                "pesan":"Semoga selalu kece ya kak fadil"# 5
            },
            {
                "nama": "Kakak Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak Aqil keren gacor",  
                "pesan":"Semoga hobinya bisa dikurangi ya kak, biar sehat hehe"# 6
            },
            {
                "nama": "Kakak Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "Kakak Naufal pendiam sekali",  
                "pesan":"Semoga sehat selalu dan bahagia"# 7
            },
            {
                "nama": "Kakak Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak Nadia Keren banget",  
                "pesan":"Selalu keren ya kak"# 8
            },
            {
                "nama": "Kakak Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3,
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak marleta murah senyum",  
                "pesan":"semangat kak semester 7 nya semoga lulus tepat waktu" # 9
            },
            {
                "nama": "Kakak Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Kakak Akeyla namanya bagus",  
                "pesan":"Sehat-sehat kak di pramuka"# 10
            },
            {
                "nama": "Kakak Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak Anggi kita sam sama dari Natar",  
                "pesan":"Semangat kak pp Natar-Iteranya"# 11
            },
            {
                "nama": "Kakak Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak Efi keren banget",  
                "pesan":"Kakak Efi semangat ya"# 12
            },
            {
                "nama": "Kakak Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kakak Fabiolla kita sama NIM akhirnya",  
                "pesan":"Semangat selalu kak fabiolla"# 13
            },
            {
                "nama": "Kakak Fairus Ary Syifa",
                "nim": "123450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 14
            },
            {
                "nama": "Kakak Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@i",
                "kesan": "",  
                "pesan":""# 15
            },
            {
                "nama": "Kakak Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Kakak Eggi hebat",  
                "pesan":"Semangat kuliahnya kakak hebat!"# 16
            },
            { 
                "nama": "Kakak Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak Afifah asyik bangett",  
                "pesan":"Semangat kak ngobrolnyaa"# 17
            },
            {
                "nama": "Kakak Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Fabio keren abis",  
                "pesan":"semangat terus kak jadi pj bu Febri"# 18
            },
          
            {
                "nama": "Kakak Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 19
            },
            {
                "nama": "Kakak Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 20
            },
            {
                "nama": "Kakak Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 21
            },
            {
                "nama": "Kakak Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Gio keren banget",  
                "pesan":"semangat Caturnya kak"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

# Tambahkan menu lainnya sesuai kebutuhan


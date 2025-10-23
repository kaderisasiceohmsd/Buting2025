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
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",

"https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
            },{
                "nama": "kakak",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "kakak",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UCrPkKll25KftLtrxDqGrhPQd8fUY84r",
            "https://drive.google.com/uc?export=view&id=1dNocmy7U8KZOmPAwzCc-ffs23EVnTCGG",
            "https://drive.google.com/uc?export=view&id=1vfgXyD8Fahp893KefZnGV63X94lJnaQM",

"https://drive.google.com/uc?export=view&id=1UDclbvlMenx5HNhZM0KT-rgbgGB1NWsg",
            "https://drive.google.com/uc?export=view&id=1zUwjHlPJ3H2JOPolWaNWIEFS4eWI0HbT",
            "https://drive.google.com/uc?export=view&id=1LJwMswvXWXzDf8Jly1Zua6HURSWTRUBH",

"https://drive.google.com/uc?export=view&id=1Md0W4i0x-lqe3Iw72vNSYrrq92yjaauK",

"https://drive.google.com/uc?export=view&id=1JrXmw0S7h0sykzH2YWvUteshArgZoLUq",

"https://drive.google.com/uc?export=view&id=1mBg7JCOLyHb8f_Oeo2GGBwlEM6HlXwiQ",

"https://drive.google.com/uc?export=view&id=1QTGYhv8pq1j-jv1lR16Get6fhzeXTaNj",

"https://drive.google.com/uc?export=view&id=1QQlNngVVbOm04USYFABOP64w3aTUDheN",

"https://drive.google.com/uc?export=view&id=1VU3C2syGZivNabwQvYudPed3-Y7zkjLk",

"https://drive.google.com/uc?export=view&id=1MqYbBVPSEcxJ1l1r9RUhQUhsf9kuYxAA",

"https://drive.google.com/uc?export=view&id=1ft_nCaZhdOdPKae1bygxCza62jNJ76dr",
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
                "kesan": "--",
                "pesan": "--"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "--",
                "pesan": "--"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "--",
                "pesan": "--"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",

"https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
            },{
                "nama": "kakak",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "kakak",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",

"https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
            },{
                "nama": "kakak",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "kakak",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",

"https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
            },{
                "nama": "kakak",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "kakak",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
    mikfes()


if menu == "Departemen Eskternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",

"https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
            },{
                "nama": "kakak",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "kakak",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",

"https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
            },{
                "nama": "kakak",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "kakak",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
    internal()


if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",

"https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
            },{
                "nama": "kakak",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "kakak",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
    ssd()


if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",

"https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
            },{
                "nama": "kakak",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Keren abisss",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "kakak",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
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
    medkraf()


# Tambahkan menu lainnya sesuai kebutuhan

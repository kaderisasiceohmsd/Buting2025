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
                "kesan": "Waktu baru liat bang rendra, keliatan berwibawa",  
                "pesan": "Semoga sehat selalu ya bang, Semangat kuliahnya.." # 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang jo asik, keren",  
                "pesan": "Semangat mengejar gelar S.Si.D nya Bang Jo.."# 1
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
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

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ePFq5fup7onWqO9tZf5fk_4MVd-6RvxH",
            "https://drive.google.com/uc?export=view&id=1ePFq5fup7onWqO9tZf5fk_4MVd-6RvxH",
            "https://drive.google.com/uc?export=view&id=1ePFq5fup7onWqO9tZf5fk_4MVd-6RvxH",
            "https://drive.google.com/uc?export=view&id=1ePFq5fup7onWqO9tZf5fk_4MVd-6RvxH",
         
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
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "-",
                "pesan": "-"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
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
            },
            {
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

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T2_7W9o0ibNMKyuG3g1Xx6fx-Mtv8peS",
            "https://drive.google.com/uc?export=view&id=1srTxXfXNoZ9Nxb_P61I-rcxWQC3xe5FD",
            "https://drive.google.com/uc?export=view&id=1JYgOiFwXSucSd4yktBb-K7WGH91oxHh8",
            "https://drive.google.com/uc?export=view&id=18aQZErSHQALSYPO169v4SP3Y48HJAZiP",
            "https://drive.google.com/uc?export=view&id=1netI0pYHLoyjvmMtV1zZartv7aUsx5VH",
            "https://drive.google.com/uc?export=view&id=19hSJ02l8q-lWOaWwM5N-RYpR_G58E9QM",
            "https://drive.google.com/uc?export=view&id=1yatJrlDW1mpa6IXfD62owLiAmf0SBhs7",
            "https://drive.google.com/uc?export=view&id=1HXYieJ-wWKYXfvi8o_k_KqXTEDD5A1u7",
            "https://drive.google.com/uc?export=view&id=1iBfVK9FDwgA6qdWKxDwggu9xqnvs3Eaw",
            "https://drive.google.com/uc?export=view&id=1y51-bSHl90Qvyv5apPj1H0GTBxVvAkeT",
            "https://drive.google.com/uc?export=view&id=1rGNNRGxDhY_zH3kKPq1eBd5eYKpvZKhO",
            "https://drive.google.com/uc?export=view&id=1TDta7gTq90DgLLURqZVEd6K7py7PgEYy",
            "https://drive.google.com/uc?export=view&id=1rqgwU8SzSZEBvlriLJFH7hDcb98_slPR",
            "https://drive.google.com/uc?export=view&id=1jYe3ZADVn6kxX_43QuVkH3eRP3pKfX3L",
            "https://drive.google.com/uc?export=view&id=1C1Q-1RBV7bhQcja3rNwzu1TI7Tgs5eeq",
            "https://drive.google.com/uc?export=view&id=1eO13kRh3J3ORG90iBbSqIrS2jlZz-eQg",
            "https://drive.google.com/uc?export=view&id=1OCVAeubucWuXsh4_iGdXjV0awfNCCxB0",
            "https://drive.google.com/uc?export=view&id=1lmOM0Z_Fyay-j3uurVsF0-sZAzwFSWut",
            "https://drive.google.com/uc?export=view&id=1ucv9HdHO3oPu6BKgkcYhbpPOWwq5iAg-",
            "https://drive.google.com/uc?export=view&id=1FfL0XOboJyMzD82LVIaQGuu1K4WUpriy",
            "https://drive.google.com/uc?export=view&id=1NnbXFc36cpIpNWubcM7JqhFbLDBwmP7p",
            "https://drive.google.com/uc?export=view&id=1rKxF4TgNdpoTXoNynes5NOlWZ0zWvn3o",
        ]
        data_list = [
            {
                {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "124450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "124450081",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450022",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "-",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "-",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "",
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()


elif menu == "Departemen Eskternal":
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
            },
            {
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

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14ihH9e-VGZfBANPqeJyGJFt2oJurLDjx",
            "https://drive.google.com/uc?export=view&id=1iRDWwMlHQ6xuZu5oLMNi7caqbfW5khhh",
            "https://drive.google.com/uc?export=view&id=1LrL7SRv1KcyxXARVDmXE_9wOMNXvCOeQ",
            "https://drive.google.com/uc?export=view&id=113sCl7bBb2A6EOVE8NyJBe6ZtiLTLf36",
            "https://drive.google.com/uc?export=view&id=1YqAgR_DwbiK_HM1dciAblVkMCJHfApGk",
            "https://drive.google.com/uc?export=view&id=1ZVEYbMjty3dds_0t6Ad1Um0TRen1GtMy",
            "https://drive.google.com/uc?export=view&id=1N9omfiwYyJHd9YK-UzOxjoA-MWASfqHA",
            "https://drive.google.com/uc?export=view&id=19kjZKLkZ-oieWHqpl-VqWhn8Ua8xusph",
            "https://drive.google.com/uc?export=view&id=1Bqh-TKm1cCTrBrZJDitgWzjxmIGf9qGw",
            "https://drive.google.com/uc?export=view&id=1GulBmkMhwAq5a7DfajZ9s0Fu0K3SgwsR",
            "https://drive.google.com/uc?export=view&id=1lmeH4-3wxYNmkruyKKLvEaW9nkwm5ZF8",
            "https://drive.google.com/uc?export=view&id=1TUuLWOry637oXpLn_8x34Rf-1oBVT8AV",
            "https://drive.google.com/uc?export=view&id=1RCL3ANsSs97wE-m-3SksdmzkGRMJVqkO",
            "https://drive.google.com/uc?export=view&id=139IHk-DDHlM4guIKQMBasrmdOI4IQs0o",
            "https://drive.google.com/uc?export=view&id=1HadYpoI2_Pdh4AKG72TE6WR3vhAKogU9",
        ]
        data_list = [
            {
                {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": 21,
                "asal": "Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@ranniku",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": 22,
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": 21,
                "asal": "Brebes, Jateng",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa.fhn",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": 20,
                "asal": "Pekan Baru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azzah.raaa_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450106",
                "umur": 18,
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Iqfinah Haula Halika",
                "nim": "123450076",
                "umur": 20,
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "iqfinanhalikaa_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "May Thalita Dehlia",
                "nim": "123450009",
                "umur": 20,
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Naufal Algahni",
                "nim": "123450116",
                "umur": 20,
                "asal": "Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": 19,
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": 21,
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@reaxender",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": 20,
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": 19,
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Hanif Zaki",
                "nim": "123450004",
                "umur": 20,
                "asal": "Padang",
                "alamat": "Perumnas, Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Sarah Warti",
                "nim": "123450057",
                "umur": 20,
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwrti",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": 19,
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": "",
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen SSD":
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
            },
            {
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


elif menu == "Departemen Medkraf":
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
            },
            {
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

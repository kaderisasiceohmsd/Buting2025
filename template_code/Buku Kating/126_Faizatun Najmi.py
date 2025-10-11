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
            "https://drive.google.com/uc?export=view&id=1GIz1zURUYL7QEY5NEJA2RUVJuDUsBKl4",
            "https://drive.google.com/uc?export=view&id=1oW7buiEZ4QoqgaIfUbl_O70WDf_pTvGN",
            "https://drive.google.com/uc?export=view&id=11aBqimw88Kauum7ggBIT7RZP66anqk6Qx",
            "https://drive.google.com/uc?export=view&id=1q7TO3ydblV7a9pzpLyC96OT_qXOYVvOV",
            "https://drive.google.com/uc?export=view&id=1imWWzIxJy_cxWq2bF5Mkms49zbi6RuLI",
            "https://drive.google.com/uc?export=view&id=1lHcbOCn0FdIX5MssKW7tFfvTkjc2H7Ra",
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
            "https://drive.google.com/uc?export=view&id=1OTFKqyl_8C7cQ2AOKl_L5uO6GZYb16DK",
            "https://drive.google.com/uc?export=view&id=1Z30bmcDSBEvfUSgwC3fEwqY2C5CV85Ps",
             "https://drive.google.com/uc?export=view&id=1Kdf_7oK6i13mnf_E1JmMNvYo46F1tHiU",
             "https://drive.google.com/uc?export=view&id=1gNCTYOCKmcb_KB8sP0gLg1QmhzdoEcnA",
            "https://drive.google.com/uc?export=view&id=1QPB7SY61zv2j0XIvvYC6bTvwX2v60JBr",
             "https://drive.google.com/uc?export=view&id=1PdfUUdGk1YINdnHtp_O-6aJTRTtTZENs",
            "https://drive.google.com/uc?export=view&id=19RXZ0pgF-lNT61e-b-slxYzNR5Ed5il5",
            "https://drive.google.com/uc?export=view&id=1m0tZVbvyBg9UENhNVX5K4gDQze5IgOjE",
            "https://drive.google.com/uc?export=view&id=1xzxEa95mxQBPwyMyaY7w2Deahailq7Im",
            "https://drive.google.com/uc?export=view&id=19PYlzTi6SA-lBfobX4wleytAhAWOUklc",
            "https://drive.google.com/uc?export=view&id=1qFOLiqsMoYWaDpCyE9UY6Hqt6t6X45E9",
            "https://drive.google.com/uc?export=view&id=1oUe1ZE7atbEEagsyMIaxxOSlcHJTkrnt",
            "https://drive.google.com/uc?export=view&id=1o-vYxzUOo-gOowyNasJ2GaMZiXVD5URM",
            "https://drive.google.com/uc?export=view&id=1LMY6NoDI4xr4-e3_oPkfjxdHiPe84bC6",
        ]
        data_list = [
            {
                "nama": "Kakak Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "Kakaknya manis, lucu ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya"# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "Kakak nya baik, seru ",  
                "pesan": "Sehat selalu kak, dilancakan semuanya "# 1
            },
              {
                "nama": "Kakak Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya keren dan asik ",  
                "pesan": "Semoga dilancarkan urusannya kak "# 1
            },
              {
                "nama": "Kakak Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kakaknya keren ",  
                "pesan": "Semoga urusannya diperlancar "# 1
            },
            {
                "nama": "Kakak Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Kakaknya keren banget ",  
                "pesan":"Semoga diperlancar semuanya  "# 1
            },
             {
                "nama": "Kakak Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya cantik dan lucu ",  
                "pesan": "Semangat kak, diperlancar semuanya "# 1
            },
              {
                "nama": "Kakak Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Kakaknya keren banget ",  
                "pesan": "Semoga dilancarkan semuanya kak "# 1
            },
              {
                "nama": "Kakak Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1d6G2AlNF85-ZSOjtF8a6an2bVm-wI1xB",
            "https://drive.google.com/uc?export=view&id=1I8tqnO-V_8VeEwnt6s3_AQb34VzK9VyF",
             "https://drive.google.com/uc?export=view&id=1FyXfLR6RBt-lXmSRAfhAdYXPToUItfDu",
             "https://drive.google.com/uc?export=view&id=1Q375ArjKLKncdGOrIKMcLSidsMOVLV0N",
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
                "kesan": "Kakak bintang tegas namun keren public speakingnya",  
                "pesan": "semoga rencana-rencana selalu dimudahkan kak"# 1
            },
            {
                "nama": "Kakak Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak Nadyaa tips cantik dong",  
                "pesan": "Semoga kakak sehat dan selalu cantik ya kak"# 1
            },
              {
                "nama": "Kakak Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak Azizah keren banget aku suka deh",  
                "pesan": "Tetap keren ya kak"# 1
            },
              {
                "nama": "Kakak Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini manis senyumnyaa",  
                "pesan": "Selalu bahagia ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HkttMenIbEWaGoyYsIwMXtLnEn8cPM08",
            "https://drive.google.com/uc?export=view&id=1GtHMvTqexf4Zm5wJlJ8F-Qy5Miqo76h9",
            "https://drive.google.com/uc?export=view&id=1acnzyhqmQtsnlRvhaWzbSP796gPK97k3",
            "https://drive.google.com/uc?export=view&id=1Jarb0f8BEIvFNfHd18P59Y3XqZKQTvzx",
            "https://drive.google.com/uc?export=view&id=1C3wYEOieh7VqG_CewEH4NYhnlZxlQn0-",
            "https://drive.google.com/uc?export=view&id=118rckWm4nA_eAEc2LPNspB0Kz7M4qz9l",
            "https://drive.google.com/uc?export=view&id=1tb-BTOKmDs4qJoH91BfO5pLu9bIzhCZw",
            "https://drive.google.com/uc?export=view&id=1-5pT9V7OJgo8st1f-ArNjaoi_WuJFlcu",
            "https://drive.google.com/uc?export=view&id=1Gk2aJOEfuGRGWIEYrBgN9KX2292D0F8E",
            "https://drive.google.com/uc?export=view&id=19WILuqz2uevVFaB0wQdyAMBNo-oPhFsQ",
            "https://drive.google.com/uc?export=view&id=1wpnE3gqq1KQGTCtcoB5iA6QDt3GHqLZe",
            "https://drive.google.com/uc?export=view&id=1gvgksEywBshbUKD-g7bl7rrEUABVnRbT",
            "https://drive.google.com/uc?export=view&id=1MwZMV7F3tMEfcEdPSTe2UdbGqWkj4DfX",
            "https://drive.google.com/uc?export=view&id=10tcexUTzPEamAh7SL4QsJoVzFdc4rRHO",
            "https://drive.google.com/uc?export=view&id=1htui9sOAuD_svtXUP6UBJogCkeFZQDKG",
            "https://drive.google.com/uc?export=view&id=1HKM2sOTIHj8WT9MryXTcaIsS5PxTFJMf",
            "https://drive.google.com/uc?export=view&id=1mj5jkENJS7rM8hUUgbJjHI0tKzYAiR4O",
            "https://drive.google.com/uc?export=view&id=1M-7F3Xy0oPxP-n_1x0IR-dvHiC7py61g",
        ]
        data_list = [
            {
                "nama": "Kakak Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Kakak Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "",  
                "pesan": ""# 1
              },
              {
                "nama": "Kakak Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "",  
                "pesan": ""# 1
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "",  
                "pesan": ""# 1
            },
              {
                "nama": "Kakak Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "",  
                "pesan": ""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

# Tambahkan menu lainnya sesuai kebutuhan

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
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Makan Pisang",
                "sosmed": "@_erendraa",
                "kesan": "Kakak ini tegas dan ketawanya menular",  
                "pesan": "semoga selalu sukses dimana pun berada kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
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
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya aktif banget, suka ngelawak",  
                "pesan": "semoga sehat selalu kakak!!!"# 1
            },
              {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini pendiam tapi lucu, manis deh!",  
                "pesan": "Semoga dipermudah bimbingan skripsinya kak !!!"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya extrovert abiss, humble banget",  
                "pesan":"semangat skripsinya kak !!!"# 1
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
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
                "nama": "Jeremia Susanto",
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
                "nama": "Dhea Amelia Putri",
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
                "nama": "Renisha Putri Giani",
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
                "nama": "Anisa Fitriyani",
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
                "nama": "Dharu Cahyoaji Sasongko",
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
                "nama": "Feby Wulandari",
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
                "nama": "Givaro Ananta",
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
                "nama": "Mirzan Yusuf Rabbani",
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
                "nama": "Berliana Enda Putri",
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
                "nama": "Juesi Apridelia Saragih",
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
                "nama": "Ridho Benedictus Togi Manik",
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
                "nama": "Feryadi Yulius",
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
                "nama": "Monica Patricia Tanjung",
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
                "nama": "Wan Nashwa Alhasni Yuska",
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
                "nama": "Rian Bintang Wijaya",
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
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
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
            "https://drive.google.com/uc?export=view&id=1SWEcVnEbV-3-f3N3PKJiHWaQ6qct2ed4",
            "https://drive.google.com/uc?export=view&id=1C3wYEOieh7VqG_CewEH4NYhnlZxlQn0-",
            "https://drive.google.com/uc?export=view&id=118rckWm4nA_eAEc2LPNspB0Kz7M4qz9l",
            "https://drive.google.com/uc?export=view&id=1tb-BTOKmDs4qJoH91BfO5pLu9bIzhCZw",
            "https://drive.google.com/uc?export=view&id=1-5pT9V7OJgo8st1f-ArNjaoi_WuJFlcu",
            "https://drive.google.com/uc?export=view&id=1Gk2aJOEfuGRGWIEYrBgN9KX2292D0F8E",
            "https://drive.google.com/uc?export=view&id=19WILuqz2uevVFaB0wQdyAMBNo-oPhFsQ",
            "https://drive.google.com/uc?export=view&id=1585EpQJtGG9NNlAerX9J6tbTR4gGmPbz",
            "https://drive.google.com/uc?export=view&id=1gvgksEywBshbUKD-g7bl7rrEUABVnRbT",
            "https://drive.google.com/uc?export=view&id=1K4ZIm_8tHhhoMnowu7IxzsDkgYQWnIAO",
            "https://drive.google.com/uc?export=view&id=10tcexUTzPEamAh7SL4QsJoVzFdc4rRHO",
            "https://drive.google.com/uc?export=view&id=1htui9sOAuD_svtXUP6UBJogCkeFZQDKG",
            "https://drive.google.com/uc?export=view&id=1HKM2sOTIHj8WT9MryXTcaIsS5PxTFJMf",
            "https://drive.google.com/uc?export=view&id=1mj5jkENJS7rM8hUUgbJjHI0tKzYAiR4O",
            "https://drive.google.com/uc?export=view&id=1M-7F3Xy0oPxP-n_1x0IR-dvHiC7py61g",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "kakaknya ceria banget, lucu, manis",  
                "pesan": "selalu ceria ya kak, semangat terus kuliahnya"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "kakaknya lucu banget, orangnya asikk",  
                "pesan": "semangat ya kak kuliahnya"# 1
            },
              {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "kakaknya keren banget, baik",  
                "pesan": "semnagat terus kak, kesehatannya dijaga selalu"# 1
              },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "kakaknya ramah, baik banget",  
                "pesan": "semangat kuliahnya kak"# 1
            },
              {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "kakaknya baik banget",  
                "pesan": "semangat terus ya kak, sukses selalu"# 1
            },
              {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "kakaknya cantik, baik, lucu",  
                "pesan": "semangat ngontennya kak, kesehatannya jangan lupa dijaga"# 1
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
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "kakaknya manis, imut",  
                "pesan": "semangat ya kak kuliahnya, jaga kesehatan"# 1
            },
              {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "kakaknya humble, baik, lucu",  
                "pesan": "sukses selalu ya kak!"# 1
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "kakaknya lucu banget, manis",  
                "pesan": "semangat terus ya kak"# 1
            },
              {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kakaknya cantik, imut, baik",  
                "pesan": "sukses selalu kak, tetap semangat"# 1
            },
              {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "kakaknya keren bangettt",  
                "pesan": "semangat ngonten dan kuliahnya kak"# 1
            },
              {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "kakaknya baik, cantik",  
                "pesan": "semangat kuliahnya kak"# 1
            },
              {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "kakaknya lucu, suka ngelawak",  
                "pesan": "tetap semangat ya kak"# 1
            },
              {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "kakaknya imut, senyumnya manis bangett",  
                "pesan": "semangat dan sukses selalu kak"# 1
            },
              {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "kakaknya cantik, baik, ramah",  
                "pesan": "jaga kesehatan ya kak, tetap semangat pokoknya"# 1
            },
              {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "kakaknya manis bangett, suka menghibur",  
                "pesan": "tetap semangat ya kak kuliahnya"# 1
            },
              {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "kakaknya cantik, baik, mudah senyum",  
                "pesan": "sukses selalu kak, dan semangat teruss"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O1f-5n8_-vCex9C3Vv8l4J2UeWX-EiRL", #1
            "https://drive.google.com/uc?export=view&id=13Cq0zti-OTxAAQn5gYy22cGScvf9jrbY", #2
            "https://drive.google.com/uc?export=view&id=1Hk3DsR2FY9nDMAuuJSoFJFczJnnmZIhx", #3
            "https://drive.google.com/uc?export=view&id=1P81qADuVsuG-n3y9f7fIF7Naxa-5E5B7", #4
            "https://drive.google.com/uc?export=view&id=18I_3hNFAxm_huZii5bF71nMSlqdJzz9V", #5
            "https://drive.google.com/uc?export=view&id=1lMrBTYRHrFZtxxxv-K4hMhHBzO9sGBYm", #6
            "https://drive.google.com/uc?export=view&id=1adnavYPK9XaGpKpHAun-mR3YaiTht-pB", #7
            "https://drive.google.com/uc?export=view&id=1nfr_uMVaEujVl19FGlI54Qwn1HncTx58", #8
            "https://drive.google.com/uc?export=view&id=1NuK1q8w7zZZ7petj8Rbb_wfaOGh8PbBr", #9
            "https://drive.google.com/uc?export=view&id=1J4NaC1CjEjUKR5owSYUmBKYS5HdNCntQ", #10
            "https://drive.google.com/uc?export=view&id=12e-pJkGCX12OpqIdhSuRKwasmDTjREQD", #11
            "https://drive.google.com/uc?export=view&id=1JuE6W7bRpJH6uUsof6_oCyGNVRvoC0Mz", #12
            "https://drive.google.com/uc?export=view&id=1y7rg19GfeQLxgoWzY2HzViDpi7wMg8A_", #13
            "https://drive.google.com/uc?export=view&id=1arYbmUOovH8l4ljRNI2X4eVu_K8HE_C3", #14
            "https://drive.google.com/uc?export=view&id=10rUtAU2MyZe81xQC0egEPTpcXRSQXiM6", #15
            "https://drive.google.com/uc?export=view&id=1sFs5Vo8_FaSjUU2xGAj_RE7iUM8ShdL6", #16
            "https://drive.google.com/uc?export=view&id=1dMdVC1dCvBBP57RhtX0SB9Npn4FGsdlz", #17
            "https://drive.google.com/uc?export=view&id=1vw6z5IWKRQhcIDEonunLhQ0LmVow6j-v", #18
            "https://drive.google.com/uc?export=view&id=1k3ZDml_MKpamKjaAf-4kBitGcJ48KXhc", #19
            "https://drive.google.com/uc?export=view&id=1W30SxzdJ8xV7MtLa0Gi-YHugSlC1axRb", #20
            "https://drive.google.com/uc?export=view&id=1xX-HQemVx1hLWKgTCzxrnBofZOLmshbH", #21
            "https://drive.google.com/uc?export=view&id=1tFC8TgrgnR7P4X1zemTgttyz2xvGIgUM", #22
        ] 
        data_list = [
            {
                "nama": "Randra Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "kakaknya seru, asik dan bisa diajak cerita apa aja  ",  
                "pesan":"Semoga capeknya terbayar dengan hasil yang memuaskan "# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "kakaknya suka bercanda tapi bisa diandalkan",  
                "pesan":"Tetap jadi sosok yang menyenangkan ya, kak! "# 2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak orangnya ramah banget, baik banget ",  
                "pesan":"Semoga sukses terus, Tetap jaga kesehatan"# 3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak punya aura positif yang menular.",  
                "pesan":"Terus jadi penyemangat untuk orang di sekitar ya, kak!"# 4
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakaknya lucu banget, selalu bikin suasana cair. ",  
                "pesan":"Semoga makin sukses dan tetap rendah hati."# 5
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakaknya baik, ramah banget ",  
                "pesan":"Semoga selalu dikelilingi orang-orang baik seperti kakak."# 6
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@notfall.s",
                "kesan": "kakaknya keren banget ",  
                "pesan":"Semangat terus kuliahnya kak "# 7
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakaknya cantik, baik, lucu ",  
                "pesan":"Tetap semangat ya kak kuliahnya "# 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "kakaknya cantik, manis banget kalau senyum ",  
                "pesan":"Semoga apa pun yang dikerjakan selalu diberi kelancaran. " # 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "kakaknya baik banget, ganteng, ramah ",  
                "pesan":" "# 10
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakaknya lucu, aktif banget, ramah",  
                "pesan":"semangat terus ya kak semester 5 nya"# 11
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "kakaknya sabar banget, baik, ramah ",  
                "pesan":"Sukses terus kak, semoga lancar semester 5 nya"# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "kakaknya murah senyum, ramah, baik",  
                "pesan":"Hati-hati terus ya kak PP dari pesawaran ke Itera"# 13
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "kakaknya baik banget, sabar banget ngasih arahan",  
                "pesan":"sukses selalu ya kak, semoga diperlancar semuanya"# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@i",
                "kesan": "kakaknya humoris, suka bikin orang tertawa",  
                "pesan":"Terus tebarkan tawa di mana pun kakak berada"# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "kakaknya keren banget, pinter",  
                "pesan":"semoga diperlancar segala urusannya "# 16
            },
            { 
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "kakaknya ramah, baik, cantik",  
                "pesan":"semoga kuliahnya lancar, jangan lupa jaga kesehatan ya kak"# 17
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Kakaknya punya selera humor yang khas banget ",  
                "pesan":"semangat terus ya kak gapai mimpi-mimpinya "# 18
            },
          
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakaknya lucu, gampang senyum.",  
                "pesan":"Semoga semester 5 nya lancar ya kak."# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakaknya punya semangat belajar yang luar biasa.",  
                "pesan":"Semoga ilmu kakak terus bermanfaat bagi banyak orang."# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "kakaknya mirip pak Tirta",  
                "pesan":"semangat kuliahnya, jangan lupa jaga kesehatan kak"# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@",
                "kesan": "kakaknya selalu tenang walau lagi ribet  ",  
                "pesan":"semoga lancar kuliahnya "# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pHn3RtbQecYOMob1MbNJqLE01_0hl5Sq", #1
            "https://drive.google.com/uc?export=view&id=1DbPpnHuFk1iFyN_O89BymObw17iyEorP", #2
            "https://drive.google.com/uc?export=view&id=1xIZ8AZnPa8JhhHMXXepI55WYQs6Jjksd", #3
            "https://drive.google.com/uc?export=view&id=1LARQQLdirO15DMXReP9AnOS6ZqLtiXrw", #4
            "https://drive.google.com/uc?export=view&id=11dw5BENoTBvnS6rKk0Mz0YxEhUX8xk1a", #5
            "https://drive.google.com/uc?export=view&id=12qgPrpBVyd_8IJp0A5O8AQHeVNkgdEbk", #6
            "https://drive.google.com/uc?export=view&id=144QXmQgJ2b1SrK04Ld31nPPdm0lfsyXP", #7
            "https://drive.google.com/uc?export=view&id=1I3hYTuwYI4wAW2MeYhMgNMr0nb3p6TSo", #8
            "https://drive.google.com/uc?export=view&id=1_o4mCy_45Ny8m2U902n71QwkHJdWTN6H", #9
            "https://drive.google.com/uc?export=view&id=1vH26a2vctsjS_wa8897hzOgrwmhUGNrU", #10
            "https://drive.google.com/uc?export=view&id=1nw_qGAOyUjuXeUOB7jnWW8rpq0aCnnVO", #11
            "https://drive.google.com/uc?export=view&id=1kkm2gCJWUIpwgEcLkAjsa9FA1oPa1Jcr", #12
            "https://drive.google.com/uc?export=view&id=1qIJ7aWFeqD33HwuPKzYS_eF3sC68JAIe", #13
            "https://drive.google.com/uc?export=view&id=1eVw0ism9oo_RsX53m0QnlKIaGsuxzdAS", #14
            "https://drive.google.com/uc?export=view&id=1f2XSibAWe8Tc6E7GC23dFwiZnR_ehvjj", #15
            "https://drive.google.com/uc?export=view&id=1m2WGjIHkRbVPqsIV481IMlqyIHPGm0r_", #16
            "https://drive.google.com/uc?export=view&id=1bBG00QFWWicKA0VK_0V293Tv1nIl_PlI", #17
            "https://drive.google.com/uc?export=view&id=1U2zauAsX1iGaV8Zh3UqisK1X6eZ5-sA4", #18
            "https://drive.google.com/uc?export=view&id=1oHVmrCgtRigZN7ksEzCx9jU787q4H7wK", #19
            "https://drive.google.com/uc?export=view&id=1oV-ZLFmMXvrksKyaKQXf81JQDYWHuXkN", #20
            "https://drive.google.com/uc?export=view&id=1QYeiymp2FT2aExUKUIeZSLjUcrUZOBgt", #21
            "https://drive.google.com/uc?export=view&id=19eGf4keJLy-hAcGLTmkj4lmW7fSXeOoJ", #22
            "https://drive.google.com/uc?export=view&id=1_9TcBjDxH5cJ8E7dglkfLzwKsfvaVQTP", #23
            "https://drive.google.com/uc?export=view&id=1-SlZXNx592kDyY09K95X8dAlmXFoDCZX", #24
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Kakaknya sosok yang disiplin tapi tetap asik. ",  
                "pesan":"Semoga diperlancar segala urusan "# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kakaknya penuh semangat, ramah, baik",  
                "pesan":"Semoga skripsinya lancar ya kak"# 2
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "kakaknya baik, lucu, suka senyum",  
                "pesan":"sehat selalu kak, semangat terus kuliahnya "# 3
            },
            {
                "nama": "Devyna Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "kakaknya penyabar banget, selalu kasih semangat",  
                "pesan":"semangat terus juga kak, semoga diperlancar segala urusan"# 4
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "kakaknya manis banget kalau senyum ",  
                "pesan":"semaangat terus ya kak, jangan lupa kesehatannya dijaga"# 5
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "kakaknya cantik, baik, ramah ",  
                "pesan":"sehat selalu kak, semoga diperlancar segala urusannya"# 6
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "kakaknya baik, ramah, suka ngelawak ",  
                "pesan":" semangat terus kuliahnya, tetap jaga kesehatan"# 7
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "kakaknya suka ngelawak, gampang senyum, ramah ",  
                "pesan":"ceria selalu kak, semangat terus kuliahnya"# 8
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "kakaknya asik, keren banget ",  
                "pesan":"semangat selalu menjalani kuliahnya kak"# 9
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "kakaknya ramah, baik, suka senyum ",  
                "pesan":"semoga sukses selalu kak, kesehatannya dijaga "# 10
            },
            {
                "nama": "khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "kakaknya baik, keren banget, ramah ",  
                "pesan":"semangat terus menjalani perkuliahannya kak"# 11
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakaknya lucu, imut",  
                "pesan":"sehat selalu kak dan tetap semangat "# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "kakaknya baik, suka ngelawak ",  
                "pesan":"semangat kuliahnya kak, tetap jaga kesehatan"# 13
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "kakaknya cantik, baik, lucu ",  
                "pesan":"ceria selalu kak, tetap jaga kesehatan"# 14
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "kakaknya maniss banget, ramah",  
                "pesan":"bahagia selalu kak, semangat terus "# 15
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "kakaknya humble, baik, ramah",  
                "pesan":"semangat terus kak, tetap jaga kesehatan"# 16
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "kakaknya cantik, positive vibes",  
                "pesan":"semangat selalu kak, jangan lupa jaga kesehatannya"# 17
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "kakaknya baik, cantik, manis banget",  
                "pesan":"jaga kesehatannya ya kka, jangan lupa semangat terus"# 18
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "kakaknya maniss kayak gula",  
                "pesan":"semangat terus kak, kesehatannya dijaga selalu"# 19
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "kakaknya baik, ramah",  
                "pesan":"jangan terlalu sering melamun kak, jaga kesehatan selalu "# 20
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "senyum kakaknya manis banget",  
                "pesan":"bahagia selalu kak, jangan lupa jaga kesehatannya"# 21
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "kakaknya humoris, suka bikin orang ketawa",  
                "pesan":"sehat selalu kak, semangat terus kuliahnya "# 22
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakaknya manis banget, baik, lucu ",  
                "pesan":"semangat selalu kak, jangan lupa jaga kesehatannya"# 23
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya penyabar banget, baik, ramah ",  
                "pesan":"semangat ya kak kuliahnya, semangat belajarnya "# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dpb_HcDVPi9v7d9K2CcN_38jMG615tI9", #1
            "https://drive.google.com/uc?export=view&id=1W51jjpFJ5HFxZpaDj9UlsaI8Dt2tCEqO", #2
            "https://drive.google.com/uc?export=view&id=1egeuBRQU0A3Y4lwhI-oCy6LKp-C_9fVW", #3
            "https://drive.google.com/uc?export=view&id=1dOa5q9xtQ7mo3yKzOf7u5xRWMzGAu-vN", #4
            "https://drive.google.com/uc?export=view&id=1XewgAmfigcjx1-iWG3jxU99q5sY-B266", #5
            "https://drive.google.com/uc?export=view&id=1Okp5sAs4ef2Gzt7nosHKqacvRwoPkpEK", #6
            "https://drive.google.com/uc?export=view&id=16o0ptjD-GXx--NJ4W18gCerVEVL3_je2", #7
            "https://drive.google.com/uc?export=view&id=1yC_ZSDbUN9aK60KuirmmDCq5aPi6hqeA", #8
            "https://drive.google.com/uc?export=view&id=1XXA9Gb9uhrt3MBGmaT2FztHo28WKXVOF", #9
            "https://drive.google.com/uc?export=view&id=1l3Itu6r1NejCY26GvclEsjZmya57RJAL", #10
            "https://drive.google.com/uc?export=view&id=1tPBHEp9SFHV4f6Ywp42NU0d3_KxoU6as", #11
            "https://drive.google.com/uc?export=view&id=1ZyFOfXNT1Hgfe3Kd5ohNTJFFQxxLJ7Ln", #12
            "https://drive.google.com/uc?export=view&id=1S20ov5mQqUrmRFQ4LxLwo-gbrWHRODVj", #13
            "https://drive.google.com/uc?export=view&id=1R1YkZPYMoHbbDU1i6gAs7yGmMQGIDxDz", #14
            "https://drive.google.com/uc?export=view&id=1Ao-Iwr8JuYB2mw_B1CY4dy-0gwv7y6RI", #15
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": "kakaknya cantik banget, lucu, tegas",  
                "pesan":"semangat terus kak menggapai mimpi-mimpinya "# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "kakaknya cantik, agak pendiam, baik",  
                "pesan":"semangat terus ya kak kuliahnya "# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "kakaknya cantik, baik banget",  
                "pesan":"semangat terus kak kuliahnya, jangan lupa jaga kesehatannya "# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "kakaknya manis banget, humble ",  
                "pesan":"sehat selalu kak, dan tetap semangat kuliahnya "# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "kakaknya lucu, suka ngelawak",  
                "pesan":"tetap ceria ya kak, sehat selalu "# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "kakaknya ramah, baik",  
                "pesan":"tetap jaga kesehatan ya kak, semangat terus"# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "nama kakaknya bagus banget ",  
                "pesan":"semangat terus ya kak!!! "# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "kakaknya agak pendiem, baik, kalem orangnya",  
                "pesan":"semangat terus ya kak, jaga kesehatan selalu "# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "kakaknya baik, ramah, ga banyak ngomong",  
                "pesan":"tetap semangat kuliahnya dan jaga kesehatan selalu"# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "kakanya keren banget, multitasking",  
                "pesan":"semangat terus ya kak, semoga mimpi-mimpinya tercapai "# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakanya humoris banget, humble, suka ngelawak",  
                "pesan":"ceria selalu kak, semangat terus kuliahnya"# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "kakaknya cantik, manis, aktif",  
                "pesan":"jaga kesehatan terus ya kak, semangat selalu"# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "kakanya lucu, baik, keren",  
                "pesan":"semangat selalu kak, jangaan lupa dijaga kesehatannya"# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "kakaknya manis, selalu ceria",  
                "pesan":"semangat terus kak, ceria selalu "# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "kakaknya baaik, ramah, agak pendiam",  
                "pesan":"jaga kesehatannya ya kak, tetap semangat"# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()
# Tambahkan menu lainnya sesuai kebutuhan


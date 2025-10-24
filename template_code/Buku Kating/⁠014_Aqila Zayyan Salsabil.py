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
           "https://drive.google.com/uc?export=view&id=1aYgsQKjkvBIhf8HSjlEc7oUdgpnVxvDQ",
            "https://drive.google.com/uc?export=view&id=1TmY_Y-cpZ50srBkidcOxBsVjXABNOq5q",
            "https://drive.google.com/uc?export=view&id=1ED9Cnzz4PqBhuYkg33iuil0Qk0tZqJ5g",
            "https://drive.google.com/uc?export=view&id=1kcuQNN0pXTZBCfhUZvBS6DEYQ4dtvou7",
            "https://drive.google.com/uc?export=view&id=1LsArrs4gQoI7dqXi5p7YeOjak8nCtvEo",
            "https://drive.google.com/uc?export=view&id=1yENowFyxVpWIfe7XcZInm5D2Ol9GcG9_",
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
                "kesan": "abangnya lucu dan bisa membaur dengan yang lain, kahimnya asik!",  
                "pesan": "semoga dipermudah untuk segala urusan kelulusan ya bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abang sekjen juga asik banget, 99% jokesnya nyambung bang",  
                "pesan": "selamat karena bentar lagi wisuda bang jo!"# 1
            },
              {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "kakak baikk, aku suka ngobrol sama kakak, karena vibesnya ramahh^^",  
                "pesan": "semogaa cepet lulus jugaa kaa ebeth!"# 1
            },
              {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya yang paling pendiem dibanding yang lainnyaa",  
                "pesan": "semoga cepet lulus juga yaa kaa, dipermudah segala urusan!"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "suka banget juga sama kak eksanty, jokesnya lucu-lucu bangettt",  
                "pesan": "tetep selalu jadi orang yang ceria ya kaa, kakak lucu banget ga boong"# 1
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "kakaknya baik dan ramah, vibesnya ramah ademm",  
                "pesan": "semoga selalu dikelelingi oleh orang yang baik ya kaa"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1daLQFjqLm3ERfVQ2jr0FoqzH_eLq38sX",
            "https://drive.google.com/uc?export=view&id=1YstTaL6OAQcO-GmoM5JvIVizudmGvSlX",
             "https://drive.google.com/uc?export=view&id=1ZJdlQeyThEqYHTC19rnT01E0JlYldiAa",
             "https://drive.google.com/uc?export=view&id=1ApdpZChp5IpSgrfO1EghXm48jxWIql7b",
            "https://drive.google.com/uc?export=view&id=1oJuFpYvalJ-c-8R_uALoJOOtyGqwpr40",
             "https://drive.google.com/uc?export=view&id=1NfNwRH6DxpXOWNHvNcsGeWQrv2uadSQi",
            "https://drive.google.com/uc?export=view&id=1Lt7YtFpV2nby18bbuk4mo0jjB-vDvouW",
            "https://drive.google.com/uc?export=view&id=15pl1N89wZV0sCTR-urdUI45uC_Uu8joe",
            "https://drive.google.com/uc?export=view&id=1HdbvNJ3rwR2bsEMPV5fzDTTwE7Ppt81n",
            "https://drive.google.com/uc?export=view&id=1kPOQZJlCt2CqAjCVduAVxenn1PRwbvo5",
            "https://drive.google.com/uc?export=view&id=1Fcu8yg0r2-cmpxtttNo6-LI7aABYa9TM",
            "https://drive.google.com/uc?export=view&id=17VSDwsmhVQb6y2uYDyggI0JCXbIWbEtX",
            "https://drive.google.com/uc?export=view&id=1FiUHFTE4J5GWxvBpMqlDs2Sx2hu_xB_B",
            "https://drive.google.com/uc?export=view&id=1u2Vv8L6ZCm-2cGKSMr2HeOh6G95NOkVY",
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
                "kesan": "abangnya lucu dan lampunggg bgtt, btw saya jg orang lampung kok bang (ga rasis)",  
                "pesan": "semoga dipermudah sempronya bang jere!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "ka dhea juga LUCU BGT GABOONG, moodbooster kaa sumpah",  
                "pesan": "sehat selalu ka dheaa, terus nge jokes ya kaa"# 1
            },
              {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "kakak reni kalcer, vibesnya kaya kakak-kakak suka pake outfit skena",  
                "pesan": "semangat menjalani semester akhirnya kaa"# 1
            },
              {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kakaknya kalem dan pemalu..?",  
                "pesan": "semangat selalu menjalani harinya kak nisaa cantik^^"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "abang ozt yang keren",  
                "pesan":"semoga selalu mendapatkan nilai yang memuaskan ya bangg!"# 1
            },
             {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "kak, pertama kali ketemu itu aku langsung salfok karena kakaknya lucu + rambutnya LUCU",  
                "pesan": "rambutnya lucu banget kaa, dirawat ya kak!"# 1
            },
              {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "kesan ketemu bang givaro, pasti jutek, kalem dsb. Ternyata ga sekalem itu ya bang",  
                "pesan": "jaga kesehatan bang gitato"# 1
            },
              {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "abangnya kalem dan lebih suka merhatiin orang ngomong",  
                "pesan": "semoga abang bisa menjadi listener yang lebih baik lagi"# 1
            },
              {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "kakaknya kalem tapi kayanya ga sekalem itu deh kak..?",  
                "pesan": "jangan pernah luntur senyumnya yaa kak1"# 1
            },
              {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "kakaknya jugaa selalu ceria dan bisa membangun suasana menyenangkan",  
                "pesan": "semoga kakak selalu dikelilingi oleh orang-orang yang baik ya kaa"# 1
            },
              {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": " abangnnya pasti suka ngejokes bapak-bapak (kesan pertama kali meet)",  
                "pesan": "semaangat semester 5 nya bang"# 1
            },
              {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "wah abangnya jago ngoding (karena megang laptop)",  
                "pesan": "semoga abangnya makin jago ngodingnya bangg"# 1
            },
              {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "kakaknya pendiem, tipe yang manut-manut ajaa",  
                "pesan": "bahagia terus ya kaaa><"# 1
            },
              {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "orangnya ceria dan juga ekspresif banget",  
                "pesan": "semangat untuk kehidupan semester 5 nya kak!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1icIG7N7ICDMtxZYhjJZmLrJfXMiSa5C5",
            "https://drive.google.com/uc?export=view&id=1JjEXcyZjb6AK7S2bRJXCM7O_CBPx-xJv",
            "https://drive.google.com/uc?export=view&id=1UbL6RWfm4qkGhSJrhrBs_xXr5LCMPYAr",
            "https://drive.google.com/uc?export=view&id=1yPxhiyinaG2yUY-zX3ZeaEbjP-7OyGn3",
            "https://drive.google.com/uc?export=view&id=1qob7p8H6xEARxXKJpYlqCvREGhR1_yfx",
            "https://drive.google.com/uc?export=view&id=1uKMaVLHRcasyf2ATHKPe8ewBcBUuAPyr",
            "https://drive.google.com/uc?export=view&id=1u03IDkWwGebmBddZJs16-HQkmriOZqcD",
            "https://drive.google.com/uc?export=view&id=1ryfkcILT1yiKWZO--61gzZ7cep56qfLD",
            "https://drive.google.com/uc?export=view&id=1XxkA_wcO2-kceKzcwOpoghTNpcFeYhW_",
            "https://drive.google.com/uc?export=view&id=1f4W5Cfo8J0bw_c2d9M3D6xPoB7AoDzSB",
            "https://drive.google.com/uc?export=view&id=1NT9kOZaAiSkufGUeZPQG_cRC6m0IOgS4",
            "https://drive.google.com/uc?export=view&id=1BC7Ut0tlPNeSN8XuJIZ__Oc3BBbu0QJj",
            "https://drive.google.com/uc?export=view&id=1vKYDmdEWgBtDI5MIcCp8eIcdHRU7By4I",
            "https://drive.google.com/uc?export=view&id=1sJq1IhF16wca6Qd-g0IA7vOi0XMx5Dz0",
            "https://drive.google.com/uc?export=view&id=1A3g_v8bXHHNYyP5Y12sJSkHuFuMHG52t",
            "https://drive.google.com/uc?export=view&id=1nbrHkeidXr2gXX68RjFsvsop_aVWsDI1",
            "https://drive.google.com/uc?export=view&id=1i991ckcgbQBTUHvWnllq8MWsn_XLt6yK",
            "https://drive.google.com/uc?export=view&id=1wKtqc2UMy3A56zrdfXMMYvn0rnyj1iMw",
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
                "kesan": "kakanya cantik dan ceriaaa terus girly banget!",  
                "pesan": "selalu sebarkan energi positifnya kak cia!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "ramah dan baik banget, walaupun keliatannya aga jutek aslinya mah enggaa",  
                "pesan": "kakak CP yang paling ramah, terimakasih kak!"# 1
            },
              {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "abangnya lucu suka ngomong -aman banget-",  
                "pesan": "semoga beneran aman banget disetiap situasi ya bang!"# 1
              },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "abangnya baik dan jokesnya suka garing? (maaf bang)",  
                "pesan": "semoga selalu lucu ya bang jokesnya"# 1
            },
              {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "abangnya ramah dan baik banget",  
                "pesan": "makasi ya bang udah tetep senyum walaupun kating yang lain lagi marah-marah"# 1
            },
              {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "kakanya baik dan ramah?! (semua kating medkraff ramah semua)",  
                "pesan": "semangatt semester 5 nya kak!"# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "udah cantik, berprestasi lagi kak!",  
                "pesan": "semoga selalu tetap ramah ya kak, kakanya udah paket lengkap!"# 1
            },
              {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "baik dan orangnya gaenakan tapii ga sekalem itu kan kak aslinya?",  
                "pesan": "semangat kak semester 5 nya, sebentar lagi semester 6 ^^"# 1
            },
              {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "kakak yang baik dan pengertian banget, cara ngomongnya juga lemah lembut",  
                "pesan": "kakak selalu keren dengan versi diri kakak sendiri!!"# 1
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "kakaknya sepertinya introvert?",  
                "pesan": "sehat selalu kaka kontenn, jaga kesehatan kaa"# 1
            },
              {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kakaknya baikk dan ramahh, suka banget!",  
                "pesan": "semoga dikelilingi orang-orang yang baik hatinya juga ya ka!"# 1
            },
              {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "kakanya baik tapi sedikit pendiem.. ambivert?!!",  
                "pesan": "spill info magang dimana kak"# 1
            },
              {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "kakaknya aslinya baik cuman kalau ga senyum jutek banget kaa keliatannya",  
                "pesan": "jangan pernah luntur senyumnya ya kaa"# 1
            },
              {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "abangnya lucu, nyambung banget jokesnya sama bang labo dan bang anam",  
                "pesan": "tetep jadi orang yang lucu ya bang1"# 1
            },
              {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "kakaknya pendiam dan kalem, tipe yang umi..",  
                "pesan": "jangan luap self reward hari ini ya kak"# 1
            },
              {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "aku bingung kakaknya beneran ga kalem atau kalem beneran..",  
                "pesan": "tutorial jaga image kaa"# 1
            },
              {
                "nama": "Kakak Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "outfitnya colourfull banget, AKU SUKA, cantik banget kak, ramah lagii",  
                "pesan": "semogaa cantik dan energi positifnya bisa menular ka!"# 1
            },
              {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "kaget banget pas tau kakak itu kakak NIM akuu",  
                "pesan": "mohon bimbingannya ka kedepannya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tdcgSxPPuFutKqz5kP0Ryev1uCDiMZh5",
            "https://drive.google.com/uc?export=view&id=1hHoU6JkS_PX2FDEgDZdsDEXjtNysBOGi",
            "https://drive.google.com/uc?export=view&id=1xAOBD0YitQ_uOMgH7XjDPCMkqbsnVUzN",
            "https://drive.google.com/uc?export=view&id=15yednctGdaZfPX7nItra_ysDLDDjsldg",
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
                "kesan": "bang bintang selalu jadi mood booster tim kesenatoran!",  
                "pesan": "tetep jadi bang bintang yang bisa membangun suasana ya bang, teriamaksi banyak bang^^"# 1
            },
            {
                "nama": "Kakak Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakanya yang paling kalem diantara tiga kakak abang yang ono",  
                "pesan": "sehat selalu ka nadyaa!! semangat selalu!"# 1
            },
              {
                "nama": "Kakak Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakak azizah, aku kira paling kalem ternyata dugaanku salah",  
                "pesan": "semoga tetap bahagia selalu ya kaa! semangat kaa!!"# 1
            },
              {
                "nama": "Kakak Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "kakak hana aku kira awalnya jutek banget, ternyata enggaa, ramah dan supelll",  
                "pesan": "semoga selalu dikelilingi oleh orang-orang baik dan tulus ya kaa!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13n4izlu9Ucuz2qNPayIv2zmNVuSjEPKC", #1
            "https://drive.google.com/uc?export=view&id=1tfx_CF5NiEV9WWFOg8e-R3XLeVaHcyXL", #2
            "https://drive.google.com/uc?export=view&id=1SCqnWPCNX0tWU-qgp_4DqHOVOTTxh12g", #3
            "https://drive.google.com/uc?export=view&id=1uePsfLTzn1yTNZOOcOauJe4uL4qa9vU9", #4
            "https://drive.google.com/uc?export=view&id=1_wyfhsoE72-u4iUEiwHpLlHkA4z3OjyH", #5
            "https://drive.google.com/uc?export=view&id=1QuH52Y-7R5_YbCnaaDbms_GXFHzaLw0e", #6
            "https://drive.google.com/uc?export=view&id=1ah64tqTVoLx597YmBW2VRauDwafRxcVq", #7
            "https://drive.google.com/uc?export=view&id=1KTlFpBXmgyG4uVZMefrXS1G6B-yiJcXb", #8
            "https://drive.google.com/uc?export=view&id=1heqKU0jZplABWfinup5NzPa0YCKuMiOV", #9
            "https://drive.google.com/uc?export=view&id=14Z0unWKHNhQshO4z7CgMHvPipc3ytGTg", #10
            "https://drive.google.com/uc?export=view&id=1bju7jTkx56PnSLlEcZZGx1EomsooTUDi", #11
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": "abangnya ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya"# 1
            },
            {
                "nama": "Kakak Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakak nya baik, seru ",  
                "pesan": "Sehat selalu kak, dilancakan semuanya "# 2
            },
              {
                "nama": "Kakak Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "Kakaknya keren dan asik ",  
                "pesan": "Semoga dilancarkan urusannya kak "# 3
            },
              {
                "nama": "Kakak Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya keren ",  
                "pesan": "Semoga urusannya diperlancar "# 4
                   },
              {
                "nama": "Kakak Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": " ",  
                "pesan": " "# 5
            },
            {
                "nama": "Kakak Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya keren banget ",  
                "pesan":"Semoga diperlancar semuanya  "# 6
            },
             {
                "nama": "Kakak Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakaknya cantik dan lucu ",  
                "pesan": "Semangat kak, diperlancar semuanya "# 7
            },
              {
                "nama": "Kakak Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya keren banget ",  
                "pesan": "Semoga dilancarkan semuanya kak "# 8
            },
              {
                "nama": "Kakak Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": " ",  
                "pesan": " "# 9
            },
              {
                "nama": "Kakak Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": " ",  
                "pesan": " "# 10
            },
              {
                "nama": "Kakak Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": " ",  
                "pesan": " "# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ME5jA0he-vo7cQY6pWKLUut8e7uNuFmX", #1
            "https://drive.google.com/uc?export=view&id=1Qh2RTRSS3Zqvz6xQx_RWeHCCAIGDJmFH", #2
            "https://drive.google.com/uc?export=view&id=14OiFvgjmYeotRPDjitvTU0UjN9MJTkwp", #3
            "https://drive.google.com/uc?export=view&id=1N8UxzsE6vI-dgvXklol3LCkS_inCU2dp", #4
            "https://drive.google.com/uc?export=view&id=1mIcHJUT-gYBsWOpJ5kJS_mQBaZcBq0Ob", #5
            "https://drive.google.com/uc?export=view&id=14gQGH8TK20dUwx0SYgnYqFEFUFnoRK9h", #6
            "https://drive.google.com/uc?export=view&id=19XATiuR9DLNj6zgixjgRg8qh_fGfph-z", #7
            "https://drive.google.com/uc?export=view&id=1eopJ637r9TkGBLD-3MOOFhU_GVpTA_Ov", #8
            "https://drive.google.com/uc?export=view&id=17SgooVdkH5vod2B5cgHaZnS7_iZ2oM-n", #9
            "https://drive.google.com/uc?export=view&id=1lBP8RGW_LLtS3dTuX_em4-t78LYCD1IQ", #10
            "https://drive.google.com/uc?export=view&id=1S7InnJ910V6sa01F4vK4ghIZ9d745cTp", #11
            "https://drive.google.com/uc?export=view&id=10oYpQhahIrC49cMs1uiFNTSGbXS9oMXh", #12
            "https://drive.google.com/uc?export=view&id=1acoS_rHgOKYr4SKHhj4W9WETAg2QOjrc", #13
            "https://drive.google.com/uc?export=view&id=1lBP8RGW_LLtS3dTuX_em4-t78LYCD1IQ", #14
            "https://drive.google.com/uc?export=view&id=1dR728MJfxBwOP0c4v0yOVANvROT36vIL", #15
            "https://drive.google.com/uc?export=view&id=1gauqs2ifDhDdQvaQey23phCQjMq0QcI0", #16
            "https://drive.google.com/uc?export=view&id=1zWtnGVGYp0Q9eD0p8BVZ0Xj89YqDepBO", #17
            "https://drive.google.com/uc?export=view&id=1IHftC-5pteVfcT7qBrozOOXsJvpDyyyu", #18
            "https://drive.google.com/uc?export=view&id=1XHOHPHLQ9FfiI4kQCwxKPPt1TQMw3uez", #19
            "https://drive.google.com/uc?export=view&id=1sxsWt9h2jhjkFNUCrm-0iLiXglr5qxew", #20
            "https://drive.google.com/uc?export=view&id=1KC5-Co8dNZH61kJ8_s4ALuDTpYx5rebJ", #21
            "https://drive.google.com/uc?export=view&id=1_8jPIj5qjaaScrra5XAClulmEZMqDiBW", #22
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
                "kesan": "abangnya kalem dan ga banyak ngomong walaupun ketua",  
                "pesan":"semangat semester akhirnya bang!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "kakaknya orangnya sederhana dan apa adanya",  
                "pesan":"semangattt kaa, semoga cepet sempro!"# 2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "kakaknya open dan asik juga, ternyata ga sekaku ituu ngobrl sama orang pinter",  
                "pesan":"makasih ya kakk"# 3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "masyaallah banget kaa, udah cantik pinter lagi",  
                "pesan":"tetep istiqomah yaa kak aisyah!"# 4
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "keliatan abangnya orang baik, ditamabah abangnya juga suka nge jokes",  
                "pesan":"semangat selalu bang fadil!"# 5
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "bang aqil orangnya asik karena tipe-tipe orang yang suka nge jokes bapak-bapak",  
                "pesan":"semangatt semester 5 nya bang!!"# 6
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "kalau sama orang baru abangnya pendiem dan kalem",  
                "pesan":"semoga selalu  diberikan kemudahan dalam setiap urusan bang!"# 7
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "kakaknya baikk dan ramah lemah lembut",  
                "pesan":"semoga selalu dikelilingi oleh orang-orang tulus ya kak!"# 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "kakaknya orangnya ceria dan sangat ekspresif",  
                "pesan":" semoga selalu diberikan kemudahan dalam setiap urusan ka!" # 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "abang keyla pendiem dan kalem, kadang doang senyumnya",  
                "pesan":"jangan lupa jaga kesehatan ya bang!"# 10
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kak anggi yang lucu dannn ramahh, suka banget ngobrol sama kak anggi",  
                "pesan":"sehat-sehat terus ya kaa!!"# 11
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "kakaknya pemaluu",  
                "pesan":"semoga selalu diberikan kemudahan dalam setiap urusan ya ka!"# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "kakaknya baikk dan ramah walaupun aku banyak mau pas minta foto:(",  
                "pesan":"sehat-sehat terus kaa! terus jadi kating yang ramah ya ka!"# 13
            },
            {
                "nama": "Kakak Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakaknya cantik, kaya effortless untuk cantikk,, suka banget postur mukanya!",  
                "pesan":"semangattt kadiv pusdatnya duta!^^"# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main Game dan Makan",
                "sosmed": "@tvnty_",
                "kesan": "kak tanty yang punya vibes -kakak pertama-",  
                "pesan":"semangat selaluu kak tantyy, next kita senam apa lagi yah?"# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "abangnya lucu dan aktraktif",  
                "pesan":"semoga sehat selalu dan disertai keberuntungan ya bang!"# 16
            },
            { 
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "kakaknya kalau lagi diem jutek banget, tapi kalau dah senyum manisnya keluar hehe",  
                "pesan":"semangatt terus kaa di kepanitiannya!"# 17
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "abang ini lucu nya lucu banget, jokesnya nyambung, terus ya lucu aja intinya",  
                "pesan":"jangan berantem terus sama kak sonya ya bang!"# 18
            },
          
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl.Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "kakanya stel kalem dan pemaluu",  
                "pesan":"jangan lupa sayangi terus mata kakak ya kaa!^^"# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "kakanya pendiem bangett, aku jadi sungkan ka..",  
                "pesan":"semangat terus kaa cantik!"# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "abangnya suka banget ketawa-ketiwi, aktraktif?",  
                "pesan":"semangat bang, semoga bisa jadi data engineer"# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giovaniars_",
                "kesan": "abangnya keren banget, walaupun begitu tetep rendah hati!",  
                "pesan":"semoga bisa survive di semester 5 ini ya bang, semangat!!"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nACW6LSJlwBUy56BqWIa0fvOzIhSPaq0", #1
            "https://drive.google.com/uc?export=view&id=1_fW93tU9dOYuq_DuKg1msHukc0Fh_pK8", #2
            "https://drive.google.com/uc?export=view&id=17g3LL6YgY3eB8r1bxe4_7Z1qOOy-sAD2", #3
            "https://drive.google.com/uc?export=view&id=1o0vU9jXpJ-IHb1CsEf2nYo9rr5Or5-Ad", #4
            "https://drive.google.com/uc?export=view&id=1cDpiskznj1rtZnd6JGHWizrDGk2aUCvw", #5
            "https://drive.google.com/uc?export=view&id=1Z0gzLSZrKXZUM4Mmp0nJsTx7irN9z-FZ", #6
            "https://drive.google.com/uc?export=view&id=171HmKUZ-PIzFiA-F4qq0ePjP6iE2TP8a", #7
            "https://drive.google.com/uc?export=view&id=1UcPn5-dx7HWnDT5w-ZVvkQcOb6I00Y3V", #8
            "https://drive.google.com/uc?export=view&id=1v6hncXKRsI7zFyXhJmI0w-XYTE9lRTlr", #9
            "https://drive.google.com/uc?export=view&id=1TcBSwto36kmR-xf-dtzLzBdQg4uowIGP", #10
            "https://drive.google.com/uc?export=view&id=11W4GI0rgaQ78ff0gnuQVfpDy1EVW3tfZq", #11
            "https://drive.google.com/uc?export=view&id=14cn0ph-FxHhSbkVjZ7r4x-AMZe4XPO_7", #12
            "https://drive.google.com/uc?export=view&id=1O1GWoEHAh2yP9RHCg0eUrJV0itkukY_X", #13
            "https://drive.google.com/uc?export=view&id=1qbPzBebQRb4HjUOvSKJU5gBTV1DqPU1K", #14
            "https://drive.google.com/uc?export=view&id=1eVuqCeraHcQV681nOK2YJM_vgTlYI2sO", #15
            "https://drive.google.com/uc?export=view&id=1dMfNxiapBFCinRifl4yGeor0doP-FIGH", #16
            "https://drive.google.com/uc?export=view&id=1u9ktVjFbJXu61r7Zmn_oKSD8GaEmM0sJ", #17
            "https://drive.google.com/uc?export=view&id=1c4Z9Xn4kIQCRK0xyTmvZtZLIMd7hByNH", #18
            "https://drive.google.com/uc?export=view&id=173HLe0VXbK0lPyvJi2VFVTtGe04oasO1", #19
            "https://drive.google.com/uc?export=view&id=1VwafeFwDlf0tzCkOwICLLV5HQOPkxIRf", #20
            "https://drive.google.com/uc?export=view&id=132KoMKHn-Hb5WIWavEsuQ_PzZYBsTrpL", #21
            "https://drive.google.com/uc?export=view&id=13iGaiJAfPhzND5jljmzOKH1g7A07Dnwq", #22
            "https://drive.google.com/uc?export=view&id=17Eb_j0bvGIX6xjrAfJ6Ly_4djm--42MU", #23
            "https://drive.google.com/uc?export=view&id=1bKqyBBkHyyGnF3Jo2crzViIUch_gKyaP", #24
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
                "kesan": "abangnya terlihat disegani yang lainnya",  
                "pesan":"semangat semester akhirnya bang rafi!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kakaknya terlihat humble dan open",  
                "pesan":"semoga selalu sehat dan dikelilingi oleh orang baik ya ka"# 2
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "kakaknya keliatan banget tipe yang lemah lembut",  
                "pesan":"semoga bahagia selalu ka deaa"# 3
            },
            {
                "nama": "Devyna Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "super baik banget, awalnya ngira bakal kaku..",  
                "pesan":"semoga selalu dipermudah urusannya mentor ku! semoga dunia selalu berpihak kepada kakak!^^"# 4
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "kakaknya maniss senyumannya cantik",  
                "pesan":"jangan pernah luntur senyumnya ya kaaa!"# 5
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": " ga nyangka sains data punya mahasiswi bule",  
                "pesan":"semangat selalu kaa cindy, semoga bisa awet ya ci "# 6
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "abangnya suka marah-marah (funfact ya bang?)",  
                "pesan":"semoga sehat selaluu bang desman!"# 7
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "kakaknya sangat ekspresiff, suka banget kalau kakaknya udah jadi mc",  
                "pesan":"semangat selalu kaka heboh><"# 8
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya kalem dan ga banyak tingkahh",  
                "pesan":"semoga selalu dikelilingi oleh orang yang baik ya bang"# 9
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "kakaknya tipe yang kakak banget..",  
                "pesan":"sehat selalu ya kaa! semangatttt"# 10
            },
            {
                "nama": "khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "kakaknya terlihat jutek, namun aslinya ga sejutek ituu",  
                "pesan":"jangan luntur senyumnya ya kaa!"# 11
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakaknya pendiem dan kalem banget, kaya ukhti-ukht",  
                "pesan":"tetap istikomahh ya kaa nurul!"# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "abangnya seru tapi terkadang suka kagok",  
                "pesan":"tentu"# 13
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "kak melll, kesan pertamanya tuh kakak orangnya yang lemah lembut",  
                "pesan":"semoga dipermudah dalam setiap uruan kak mei!"# 14
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "orangnya dari raut wajah memang jutek tapi aslinya baikk",  
                "pesan":"sehat selalu kak nayla!"# 15
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "bang adit orangnya isenggg terus suka banget nge ceng2in orang",  
                "pesan":"sehat selalu bang adit, semnagat jadi pengmas!"# 16
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "mukanya terlihat ke ibuan",  
                "pesan":"semoga selalu disertai keberuntungan ka!"# 17
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "kelihatannya kakak orangnya tegas",  
                "pesan":"semangat jadi pengmasnya kak ratu!!"# 18
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "senyumnya manis banget ka",  
                "pesan":"jangan sampe senyumnya luntur ya kak!"# 19
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "abangnya posturnya terlihat sangat tegas",  
                "pesan":" jangan lupa makan sehat ya bang, 4 sehat 5 sempurna!"# 20
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "muka kakaknya jutek tapi aslinya baik banget!, beneran baik banget",  
                "pesan":"semangattt semester 5 nya kak arini!^^"# 21
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "abangnya jarang marah, lebih suka membaur dengan yang lain",  
                "pesan":"tetap ceria selalu yaa bang aldi!"# 22
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakaknya kalem dan lemah lembut",  
                "pesan":"be ur self kaa, semoga selalu dipermudah segala urusan yaa"# 23
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya lucu bangettt, effortless untuk canti",  
                "pesan":"balikkan punya, terlalu remuk untuk dimiliki"# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rXBQyBPrz4-tmdpWoNYtUeAx8j_vGeLo", #1
            "https://drive.google.com/uc?export=view&id=1Ff50qEl4JbBvdFexY4RzfZ3aitD-o560", #2
            "https://drive.google.com/uc?export=view&id=1wHW35fH8gEyzomYIQUxhSoI2BAS5JpAn", #3
            "https://drive.google.com/uc?export=view&id=1snSXrQM1Gp3wOp1W8O9PxXj8KxdWyMiI", #4
            "https://drive.google.com/uc?export=view&id=1JRouZp2uakUi_Cz1oCxlVYbFhm9hfhLd", #5
            "https://drive.google.com/uc?export=view&id=1iOCFSqObO6KcRuC4UJYdYopX_1QEDnq8", #6
            "https://drive.google.com/uc?export=view&id=1jK7LGu2wilPgkLmktRXDGKtFkpyjiaws", #7
            "https://drive.google.com/uc?export=view&id=1NGh4cU9t401FE_QY04whRykPwx4q1-7M", #8
            "https://drive.google.com/uc?export=view&id=11NWwc3-a-7--id3_IfXmKj0JHJw3BtrU", #9
            "https://drive.google.com/uc?export=view&id=1gGfvbuXF6Pb3tfrugNDhf55qQJlvh8TE", #10
            "https://drive.google.com/uc?export=view&id=14VGeiQtg-MU9DQJFkt86FB-GpGXSZkuh", #11
            "https://drive.google.com/uc?export=view&id=1wM20tRFuGb_66fXSc-IPlpYqMnpPH6iU", #12
            "https://drive.google.com/uc?export=view&id=19ziizmXoGPU78MZr59xSXsO6pss2soMN", #13
            "https://drive.google.com/uc?export=view&id=1HlZEXJ-XpsG8bjl3iDcENVNM_1QqI_L0", #14
            "https://drive.google.com/uc?export=view&id=1s5zmCY7YSfmiQkQu0EvBhczS9ibIToXf", #15
        ]
        data_list = [
            {
                "nama": "Kakak Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": " ",  
                "pesan":" "# 2
            },
            {
                "nama": "Kakak Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": " ",  
                "pesan":" "# 3
            },
            {
                "nama": "Kakak Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": " ",  
                "pesan":" "# 4
            },
            {
                "nama": "Kakak Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": " ",  
                "pesan":" "# 5
            },
            {
                "nama": "Kakak Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": " ",  
                "pesan":" "# 6
            },
            {
                "nama": "Kakak May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": " ",  
                "pesan":" "# 7
            },
            {
                "nama": "Kakak Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": " ",  
                "pesan":" "# 8
            },
            {
                "nama": "Kakak Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": " ",  
                "pesan":" "# 9
            },
            {
                "nama": "Kakak Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": " ",  
                "pesan":" "# 10
            },
            {
                "nama": "Kakak Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": " ",  
                "pesan":" "# 11
            },
            {
                "nama": "Kakak Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": " ",  
                "pesan":" "# 12
            },
            {
                "nama": "Kakak Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": " ",  
                "pesan":" "# 13
            },
            {
                "nama": "Kakak Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": " ",  
                "pesan":" "# 14
            },
            {
                "nama": "Kakak Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": " ",  
                "pesan":" "# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1k6svcVj09SDp-6Q9ZFGJWBHVrBYUl5RE", #1
            "https://drive.google.com/uc?export=view&id=1sGOLaAaPc_lYwGMgf-5XnfRZa4xUM7bt", #2
            "https://drive.google.com/uc?export=view&id=1yOwlHHes1P7ef1cF-3z4vEGn6rIiBs5-", #3
            "https://drive.google.com/uc?export=view&id=1cIlJ2FKEMgNlA4Mzu3rq7Fc5_6iUgQQV", #4
            "https://drive.google.com/uc?export=view&id=1zhZOWIPNbEd1qc_TvajvW6Ntw6-MJaow", #5
            "https://drive.google.com/uc?export=view&id=1LW9FPnDqN3P6sfTIyJdSZvPKC_iRrW_A", #6
            "https://drive.google.com/uc?export=view&id=1UmKqmYQDqzci4q9EmxIh_L21zlNAA7ML", #7
            "https://drive.google.com/uc?export=view&id=1CbpU6H_-IVjoTmYOqCtX2TJIaXrI8Flk", #8
            "https://drive.google.com/uc?export=view&id=1GicN6bOyHjLgpA1_i76htOwceOFa2TGo", #9
            "https://drive.google.com/uc?export=view&id=1NHtTFBB5j-wE2NSAikqLAkYCyd3T9Sqe", #10
            "https://drive.google.com/uc?export=view&id=11SOjNjDQK9EjJFORB3iN3Sm1FBKkWTGx", #11
            "https://drive.google.com/uc?export=view&id=15X7L6BSeZztzfWp38mhElyAZ_k8FbPUG", #12
            "https://drive.google.com/uc?export=view&id=175TISOneHHZSjvqUCo5i3qjpHzbspkGw", #13
            "https://drive.google.com/uc?export=view&id=1ZmjcMKsJSSachbqGC2wHphfM8sy9n8SF", #14
            "https://drive.google.com/uc?export=view&id=18w3GzuJ0fPp7H-xTBCzddY9TvwD2xio1", #15
            "https://drive.google.com/uc?export=view&id=1YI0MIzmh8oWj9Yq7t0K-OLrHbJsIoYOF", #16
            "https://drive.google.com/uc?export=view&id=1Ti1yCy5-HKUriJx_ZjUdhPTZYO5GWExa", #17
            "https://drive.google.com/uc?export=view&id=1ngMALKq3FUBhFbvTjlyAmRY0J1DYTyEr", #18
            "https://drive.google.com/uc?export=view&id=1izX-JqbDPArgL6QBy9OsW73RTuUz8kwm", #19
            "https://drive.google.com/uc?export=view&id=1VBKtUs4P-cwnQThgdKil6G2IinN5RL7H", #20
            "https://drive.google.com/uc?export=view&id=1vmvx_AxqoY7DLSqc2lS8R3vFT80ON1g7", #21
            "https://drive.google.com/uc?export=view&id=1Xf5SQ0TWK0lhBeIccaADkhVmuK3tN1Aj", #22
            "https://drive.google.com/uc?export=view&id=1Ye6sUQZg-4ZRsX456pDnvs_UDEsbRYXq", #23
            "https://drive.google.com/uc?export=view&id=1TYbPqcgyNBSMe3WIutTsrVZZyejhifNl", #24
            "https://drive.google.com/uc?export=view&id=1ZmWneBdN46Fxl1EIJfRaqCvwzJYmHVfl", #25
            "https://drive.google.com/uc?export=view&id=1jJVYvQNtp3O4CjB1HbRJOLokWyWITQFk", #26
            
        ]
        data_list = [
            {
                "nama": "Kakak Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": "keren Kak Ferdy jadi kadep",  
                "pesan":"Semangat terus jadi kadepnya kak "# 1
            },
            {
                "nama": "Kakak Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "kak afifh cantik dan baik",  
                "pesan":"Semangat kuliahnya kakak sekdep"# 2
            },
            {
                "nama": "Kakak Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "Kak pasha tegas",  
                "pesan":"Semangat kak semester akhirnya"# 3
            },
            {
                "nama": "Kakak Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Kereen banget",  
                "pesan":"Semangat Kak Ahmad, tetap mengudara"# 4
            },
            {
                "nama": "Kakak Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "kak arienta keren",  
                "pesan":"semangat kak dan bahagia selalu"# 5
            },
            {
                "nama": "Kakak Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Kak daffa keren",  
                "pesan":"keren terus ya kak"# 6
            },
            {
                "nama": "Kakak Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Hobinya banyak, keren deh",  
                "pesan":"Semangat terus untuk menekuni hobi"# 7
            },
            {
                "nama": "Kakak Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "kakaknya ramah",  
                "pesan":"semangat kuliahnya kak"# 8
            },
            {
                "nama": "Kakak Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "keren banet jago koding",  
                "pesan":"semoga jadi data engineer ya bang"# 9
            },
            {
                "nama": "Kakak Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "tegas dan berwibawa",  
                "pesan":"sehat selalu ya kak"# 10
            },
            {
                "nama": "Kakak Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakaknya tegas namun kalau ketawa lucu",  
                "pesan":"jangan marah-marah terus ya kak, jaga kesehatan"# 11
            },
            {
                "nama": "Kakak Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "Kak Sahid ramah dan bersemangat, selalu aktif di setiap kegiatan.",
                "pesan": "Terus jaga semangat dan tetap rajin latihan voli ya kak" # 12
            },
            
            {
                "nama": "Kakak Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Kak Ali keren",
                "pesan": "Semoga dompetnya sering tebal biar bisa kulineran terus ya kak" # 13
            },
            
            {
                "nama": "Kakak Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kak Rosalia lucu dan ceria banget",
                "pesan": "Tetap jadi pribadi ceria" # 14
            },
            
            {
                "nama": "Kakak Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "-",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma murah senyum",
                "pesan": "Semoga makin sukses dan tetap rendah hati ya kak" # 15
            },
            
            {
                "nama": "Kakak Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Ferazka chill banget",
                "pesan": "Tidurnya jangan kelamaan, tetap semangat ikut kegiatan ya kak" # 16
            },
            
            {
                "nama": "Kakak Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Kak Sahid keren",
                "pesan": "Semoga makin jago main game" # 17
            },
            
            {
                "nama": "Kakak Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Kak Daffa keren",
                "pesan": "Terus semangat kuliahnya" # 18
            },
            
            {
                "nama": "Kakak Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "Kak Ihsan seru banget",
                "pesan": "Terus semangat kak, semoga lelenya makin banyak yang ketangkap!" # 19
            },
            
            {
                "nama": "Kakak Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "Kak Rewina calm tapi perhatian banget ke teman-teman.",
                "pesan": "Terus semangat dan jangan lupa isi hari dengan musik favoritmu!" # 20
            },
            
            {
                "nama": "Kakak Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "Kak Benget jago banget main futsal",
                "pesan": "Terus latihan dan tetap rendah hati di setiap pertandingan kak!" # 21
            },
            
            {
                "nama": "Kakak Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "Kak Uliano multitalenta banget dan punya karakter unik.",
                "pesan": "Terus kembangkan bakatmu dan semoga makin produktif dalam hal positif!" # 22
            },
            
            {
                "nama": "Kakak Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "Kak Kevin tinggi",
                "pesan": "Terus semangat nge-dribble kehidupan dan jangan lupa istirahat kak" # 23
            },
            
            {
                "nama": "Kakak Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "Kak Erma enerjik dan ceria banget",
                "pesan": "Terus menari dalam semangat dan jangan berhenti berkarya kak" # 24
            },
            
            {
                "nama": "Kakak Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kak Lidia lembut",
                "pesan": "Semoga makin aktif dan sukses di setiap langkahnya kak" # 25
            },
            {
                "nama": "Kakak Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Kak Ridwan kece bgt",
                "pesan": "Semoga makin semangat main badminnya kak" # 26
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    psda()
# Tambahkan menu lainnya sesuai kebutuhan

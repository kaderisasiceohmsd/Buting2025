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
                "nama": "Kakak Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": "Kakaknya manis, lucu ",  
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
                "umur": ".",
                "asal": ".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": ".",
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
            "https://drive.google.com/uc?export=view&id=1s0ba1MhgCyx-eoHiyXwhO0mCnlq1X7Aw", #1
            "https://drive.google.com/uc?export=view&id=1Luf4CRx-DyMsDmsF57pCgN7o_N6W0KlZ", #2
            "https://drive.google.com/uc?export=view&id=1irf6dxSz6Pn3WIf7MyctOB9R4IxpgiyG", #3
            "https://drive.google.com/uc?export=view&id=1gKmoUen2c-_GFT6fON2iJIgFRd1By0ej", #4
            "https://drive.google.com/uc?export=view&id=1oqjaBWCsdg4UUULxQS2QDWDgR_vqmqPl", #5
            "https://drive.google.com/uc?export=view&id=1EX9oo_yMVvd1VNFc1beQ-JW4BC0aWxWn", #6
            "https://drive.google.com/uc?export=view&id=1gnHAHtlCyD7AB2nebXYngINKNM-H9KkT", #7
            "https://drive.google.com/uc?export=view&id=1T_m-JS_zfIgc4jBhYH295QUThF5UUq3L", #8
            "https://drive.google.com/uc?export=view&id=1tDpL1oR4Ck0cNeEs5yrtdKDoft5tOLKR", #9
            "https://drive.google.com/uc?export=view&id=1FlS5NshIUgIpnh41RsP-ncMK-oqjwBTM", #10
            "https://drive.google.com/uc?export=view&id=1ICCNIQRvIdLbI4SDUMQ7mmCa44udowad", #11
            "https://drive.google.com/uc?export=view&id=1Iy8gqI06jXdd5y30rI4tFZJHFEbCBZ0c", #12
            "https://drive.google.com/uc?export=view&id=1ATGa_CXHduMvTdPYqf1DT7W5196NLzrF", #13
            "https://drive.google.com/uc?export=view&id=1TPJY3gJW5b2GtdgsXXvHi7_HUVAgc97g", #14
            "https://drive.google.com/uc?export=view&id=1v8oiQj-mmNHC2h1ngd8Wkd9mWW2f2OED", #15
            "https://drive.google.com/uc?export=view&id=1uPG4hEOhwAT-pN06lLgE3f_C4Q35Dips", #16
            "https://drive.google.com/uc?export=view&id=1UQu1LjjbAOd2VYPG4mYmSJ7au7r4dtRL", #17
            "https://drive.google.com/uc?export=view&id=1WdmPXDO3LxlZG15BcjuK-V1kaJTX2EJ9", #18
            "https://drive.google.com/uc?export=view&id=1U1-AFcOk-T0tpChelkVmzPFoY-kmBmAk", #19
            "https://drive.google.com/uc?export=view&id=1ul6zC5kpCz7I9NUQEHcfNHUkZSzwtCaI", #20
            "https://drive.google.com/uc?export=view&id=1VAmsfXC5oqa991brymuJS4tTVoIxpTrn", #21
            "https://drive.google.com/uc?export=view&id=1fcT6eu2cXQD1MAhwEpiv9cBit3bMY3MW", #22
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
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": " ",  
                "pesan":" "# 2
            },
            {
                "nama": "Kakak Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": " ",  
                "pesan":" "# 3
            },
            {
                "nama": "Kakak Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": " ",  
                "pesan":" "# 4
            },
            {
                "nama": "Kakak Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": " ",  
                "pesan":" "# 5
            },
            {
                "nama": "Kakak Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": " ",  
                "pesan":" "# 6
            },
            {
                "nama": "Kakak Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": " ",  
                "pesan":" "# 7
            },
            {
                "nama": "Kakak Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": " ",  
                "pesan":" "# 8
            },
            {
                "nama": "Kakak Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": " ",  
                "pesan":"  " # 9
            },
            {
                "nama": "Kakak Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": " ",  
                "pesan":" "# 10
            },
            {
                "nama": "Kakak Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": " ",  
                "pesan":" "# 11
            },
            {
                "nama": "Kakak Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": " ",  
                "pesan":" "# 12
            },
            {
                "nama": "Kakak Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": " ",  
                "pesan":" "# 13
            },
            {
                "nama": "Kakak Fairuz Ary Syifa",
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
                "kesan": " ",  
                "pesan":" "# 16
            },
            { 
                "nama": "Kakak Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": " ",  
                "pesan":" "# 17
            },
            {
                "nama": "Kakak Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": " ",  
                "pesan":" "# 18
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
                "sosmed": "@",
                "kesan": " ",  
                "pesan":" "# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UtQGdRzj2nZGPiahdFcSjreaDMUlBhTZ", #1
            "https://drive.google.com/uc?export=view&id=1OPMxuJAl3-_TmwQv3D6V0NvO-eHXyKAJ", #2
            "https://drive.google.com/uc?export=view&id=13RE_xzzr-eeapag7XUqLHnzmbrUl1GAc", #3
            "https://drive.google.com/uc?export=view&id=1wJx8pIgdQ5kg7TtYbIaPXVrvNUGmj66A", #4
            "https://drive.google.com/uc?export=view&id=1TGQ5kHmi33i8e9GGaFQf-5ftqzP45J0C", #5
            "https://drive.google.com/uc?export=view&id=17rO4nJfSrjyhocg4Mhx9FMLDqGhkbh0H", #6
            "https://drive.google.com/uc?export=view&id=1nRToAisUcSLg0pfLFzlVFglgjjk5O7U5", #7
            "https://drive.google.com/uc?export=view&id=1JIR3OI2WXNWD6Qn7qxtV2g-W7hnBEPEo", #8
            "https://drive.google.com/uc?export=view&id=1XOPuJb531cPEoI13FyK9tZML93FYDW91", #9
            "https://drive.google.com/uc?export=view&id=1ieiUCi8pcxYiF_wolVBu5sHQmHBoDpy2", #10
            "https://drive.google.com/uc?export=view&id=1_E2Gu74N5tJs32HnktB8585-NlZkjtdY", #11
            "https://drive.google.com/uc?export=view&id=1RmiDkXC-c5Dg2WbJLkg8aCLDiIiNHoIf", #12
            "https://drive.google.com/uc?export=view&id=1PsCUI1GTI9JTUrVAZGPm5hyTrHX6HAVJ", #13
            "https://drive.google.com/uc?export=view&id=1iBlmtG6q8iz228H188ULpWhV-xJE3uQd", #14
            "https://drive.google.com/uc?export=view&id=15zRodBritb0x_o7mTLj0yv8yFQw2egA-", #15
            "https://drive.google.com/uc?export=view&id=1UpGaXXhDOpUPxpOITFkIIeBeSvVjQb7L", #16
            "https://drive.google.com/uc?export=view&id=1mLhcW81BODxSFgOs1oSsfihHa2r2pVH-", #17
            "https://drive.google.com/uc?export=view&id=14mEVPrWhgtAgdufi2AOsjK3lM4EtUJnU", #18
            "https://drive.google.com/uc?export=view&id=1pMK5_auxffisC7BI26sWrulc2kTTFIFp", #19
            "https://drive.google.com/uc?export=view&id=1qp_UNq_FIQrqnbt0wuFOS7sLpvt1jGWx", #20
            "https://drive.google.com/uc?export=view&id=1PcJrC_RDlIUzcY_7XiTbGZwKQU4iF8Cu", #21
            "https://drive.google.com/uc?export=view&id=16yw1B-es_wg0Z6smNW_HmNG01yTFfxt1", #22
            "https://drive.google.com/uc?export=view&id=1HXbtXAfiWPL-UNabcmkWTz70gq6ykwlm", #23
            "https://drive.google.com/uc?export=view&id=1cnh4Ps4sccxzwRbKkIwNchUb64UMdmhK", #24
        ]
        data_list = [
            {
                "nama": "Kakak Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": " ",  
                "pesan":" "# 2
            },
            {
                "nama": "Kakak Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": " ",  
                "pesan":" "# 3
            },
            {
                "nama": "Kakak Devyna Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": " ",  
                "pesan":" "# 4
            },
            {
                "nama": "Kakak Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": " ",  
                "pesan":" "# 5
            },
            {
                "nama": "Kakak Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": " ",  
                "pesan":" "# 6
            },
            {
                "nama": "Kakak Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": " ",  
                "pesan":" "# 7
            },
            {
                "nama": "Kakak Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": " ",  
                "pesan":" "# 8
            },
            {
                "nama": "Kakak Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": " ",  
                "pesan":" "# 9
            },
            {
                "nama": "Kakak Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": " ",  
                "pesan":" "# 10
            },
            {
                "nama": "Kakak khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": " ",  
                "pesan":" "# 11
            },
            {
                "nama": "Kakak Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": " ",  
                "pesan":" "# 12
            },
            {
                "nama": "Kakak Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": " ",  
                "pesan":" "# 13
            },
            {
                "nama": "Kakak Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": " ",  
                "pesan":" "# 14
            },
            {
                "nama": "Kakak Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": " ",  
                "pesan":" "# 15
            },
            {
                "nama": "Kakak Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": " ",  
                "pesan":" "# 16
            },
            {
                "nama": "Kakak Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": " ",  
                "pesan":" "# 17
            },
            {
                "nama": "Kakak Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": " ",  
                "pesan":" "# 18
            },
            {
                "nama": "Kakak Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": " ",  
                "pesan":" "# 19
            },
            {
                "nama": "Kakak Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": " ",  
                "pesan":" "# 20
            },
            {
                "nama": "Kakak Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": " ",  
                "pesan":" "# 21
            },
            {
                "nama": "Kakak Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": " ",  
                "pesan":" "# 22
            },
            {
                "nama": "Kakak Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": " ",  
                "pesan":" "# 23
            },
            {
                "nama": "Kakak Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": " ",  
                "pesan":" "# 24
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
# Tambahkan menu lainnya sesuai kebutuhan

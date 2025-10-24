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


elif menu == "Baleg":
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

elif menu == "Senator":
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

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1leWjYgQIThK1NDeyEfL56J1jTsTgYB5H", #1
            "https://drive.google.com/uc?export=view&id=11So3aImCSdyQLGaTVDoWrNviOhMz83vf", #2
            "https://drive.google.com/uc?export=view&id=1uCf-aumx8RuguCgAG_RaUrBqKfzHQtFt", #3
            "https://drive.google.com/uc?export=view&id=10Pw8o2UbRRa7oAMvrBYBsK76RAfVVZRB", #4
            "https://drive.google.com/uc?export=view&id=1rbn-E5-BVRunjMQW4ygpQk-tc2s_ZPyb", #5
            "https://drive.google.com/uc?export=view&id=1yjrwixixpUu89q0RhGFUb2qXGPDu0M-C", #6
            "https://drive.google.com/uc?export=view&id=1iLeNpp-va7-uTGudGZVsQ118YkcVl485", #7
            "https://drive.google.com/uc?export=view&id=1yxNr6kf8wa36h1dWdUluWVpcgV8PamFF", #8
            "https://drive.google.com/uc?export=view&id=19y4hIVZxcYJJWEIukq98A7q5pqvfTzDL", #9
            "https://drive.google.com/uc?export=view&id=1JKPmvYS7yOhPg7YIfo1n0CImqorzzVnT", #10
            "https://drive.google.com/uc?export=view&id=1ifyskHqqpP_aRXnliMmuoMdTwW5e4vJx", #11
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
                "kesan": "abangnya seru dan bisa membangun suasana, selain itu prestasinya oke banget",  
                "pesan": " Semoga dilancarkann sampai tahap sempronya dan selanjut-lanjutnya bangg!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakaknya pemaluu",  
                "pesan": "Semogaa bisa cepet-cepet lulusss ya kaa!"# 2
            },
              {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "abangnya bisa membangun suasana dan ternyata hobi abang yang ngoleksi parfum berkesinambungan dengan funfact saya?",  
                "pesan": "semoga dilancarkan sampai lulus ya bang!"# 3
            },
              {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya keliatan banget inimah azig parahh",  
                "pesan": "semoga kakaknya bisa azig selamanya"# 4
                   },
              {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "kakanya sepertinya introvert? atau ga ekstrovert tapi pemaluu",  
                "pesan": "jangan lupa makan 4 sehat 5 sempurna kak!"# 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "kakaknya ramahhh dan terlihat sangat girly",  
                "pesan":"Semoga selalu diberikan kesehatan kaka baik!"# 6
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnya lucu dann sebetulnya sangat aktif?",  
                "pesan": "Semangat terus bang, walaupun kayanya suka excited sendirian?"# 7
            },
              {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya lucuu apalagi kalau senyum kaya di foto kita ini?",  
                "pesan": "Semoga selalu dikelilingi oleh orang-orang baik ya kaa!"# 8
            },
              {
                "nama": "Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "kakaknya kalem dan girly jugaa",  
                "pesan": "jangan luntur ya kaa senyumannyaa!"# 9
            },
              {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "kaaakkk keren banget dari dulu udah berani untuk jualannn sendiri",  
                "pesan": "kak, ajarin bikin risol yang enak?"# 10
            },
              {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "kakak nydia girly nan lemah lembut",  
                "pesan": "jangan lupa untuk selalu jaga kesehatan dan semangattt teruss kaka^^"# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

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

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UFgQh6tn_TUk_Kmz3bGcwe5jSFWtVTIp", #1
            "https://drive.google.com/uc?export=view&id=1_fW93tU9dOYuq_DuKg1msHukc0Fh_pK8", #2
            "https://drive.google.com/uc?export=view&id=17g3LL6YgY3eB8r1bxe4_7Z1qOOy-sAD2", #3
            "https://drive.google.com/uc?export=view&id=1o0vU9jXpJ-IHb1CsEf2nYo9rr5Or5-Ad", #4
            "https://drive.google.com/uc?export=view&id=17Eb_j0bvGIX6xjrAfJ6Ly_4djm--42MU", #5
            "https://drive.google.com/uc?export=view&id=1Z0gzLSZrKXZUM4Mmp0nJsTx7irN9z-FZ", #6
            "https://drive.google.com/uc?export=view&id=171HmKUZ-PIzFiA-F4qq0ePjP6iE2TP8a", #7
            "https://drive.google.com/uc?export=view&id=1UcPn5-dx7HWnDT5w-ZVvkQcOb6I00Y3V", #8
            "https://drive.google.com/uc?export=view&id=1v6hncXKRsI7zFyXhJmI0w-XYTE9lRTlr", #9
            "https://drive.google.com/uc?export=view&id=1TcBSwto36kmR-xf-dtzLzBdQg4uowIGP", #10
            "https://drive.google.com/uc?export=view&id=1W4GI0rgaQ78ff0gnuQVfpDy1EVW3tfZq", #11
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
            "https://drive.google.com/uc?export=view&id=1cDpiskznj1rtZnd6JGHWizrDGk2aUCvw", #23
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
                "kesan": "kakaknya kalem dan lemah lembutt",  
                "pesan":"be ur self kaa, semoga selalu dipermudah apapun urusannya!"# 5
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
                "kesan": "kakaknya manis dan senyumannya cantik sekali!",  
                "pesan":"jangan pernah luntur ya kaa senyumannyaa^^"# 23
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
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xuKj4Jk_JSsZUqbYfZwjlX9j94igyrC5", #1
            "https://drive.google.com/uc?export=view&id=1-EbuHG8gptK7_zZtTYvN99AdxtTo05gB", #2
            "https://drive.google.com/uc?export=view&id=1lcLmENlLt0TOq9Xwe95G_ZeBuTl8RJoE", #3
            "https://drive.google.com/uc?export=view&id=1AFE7FIq4WI17MRm3jambprAOFkSis-hN", #4
            "https://drive.google.com/uc?export=view&id=1o-yn_bVH98ZHN9R8DMLPaWAlcumlCAVw", #5
            "https://drive.google.com/uc?export=view&id=13ik74DtdAUYrs_av4c6YWVxNhppsPI5i", #6
            "https://drive.google.com/uc?export=view&id=1Fik8_aq1oeUje8Pdesn9Swb3cvH3R1qF", #7
            "https://drive.google.com/uc?export=view&id=1ksGaRZDJ9H_2iTQ4SRnwJEQ_91pXE14d", #8
            "https://drive.google.com/uc?export=view&id=1TJ-pMtzCxJNHGGFJE-qgUELlA21wRdYU", #9
            "https://drive.google.com/uc?export=view&id=13w6EtcQzFZWafpdlkLEHW8nUXRRNTd-P", #10
            "https://drive.google.com/uc?export=view&id=1_TCGTOS2sw2AjaJFpfNbcxiHEQyW3GvM", #11
            "https://drive.google.com/uc?export=view&id=1nR5-CcRN7rauJtpjEouPCmZZAa1Vh54P", #12
            "https://drive.google.com/uc?export=view&id=16j1a-7t-OAD8e6uwdBxKC9Xk_SnsrP3X", #13
            "https://drive.google.com/uc?export=view&id=1nQYPuJtRA1xcE2CKqTIpNUM8WZCxguT1", #14
            "https://drive.google.com/uc?export=view&id=1cMct3bht86CDzB-_2rcggTZQ1iKjsPbX", #15
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
                "kesan": "kak ranii cantik sekali dan pembawaannya tenang tapi tegas",  
                "pesan":"semoga sehat selalu kak rani cantik^^"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "suka banget vibesnya kak renta, baikk dan effortless to be pretty girl",  
                "pesan":"maaf ya kaa, awalnya ngira laki-laki karena pp nyaa:("# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "kak salwa ada aura ke ibuannya hehe, gatau kenapa kak tapi aku yakin kakak orangnya hatinya lembut!",  
                "pesan":"semangat selalu ka salwa, semoga cepet-cepet sempro ya ka!"# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "ka zahra adem banget liatnya, tipe yang ngomong lemah lembut",  
                "pesan":"semoga selalu dikelilingi oleh orang-orang tulus dan baik hatinya kak!"# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "bang haikal walaupun mukanya galak tapi aku yakin hatinya pasti kaya marshmallow",  
                "pesan":"jangan lupa jaga kesehatan ya bang!"# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "kakak baikk vibesnya kakak-kakak yang -haiii adikk-",  
                "pesan":"jangan lupa jaga kesehatan kak! makann 4 sehat 5 sempurna hehe"# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "kalau ga senyum kakak jutek bangett tau kaa, tapi kalau udah senyum manis banget ga boong no hoax",  
                "pesan":"jangan lupa untuk sering-sering senyum ya kak! cantik senyumannya^^"# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "abang naufal lucu, ga serem sama sekali malah lebih ke lucu ",  
                "pesan":"semoga dipermudah survive di semester 5 ini ya bang!"# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "abang zailani baik dan suka ketawa",  
                "pesan":"pacarnya cantik banget bang, akur-akur ya bang!"# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "bang rendi kayanya orangnya pendiem yaaa",  
                "pesan":"semangat terus banggg, harus semangat 45!!!!"# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kak hanna syuperrr energic dan ekspresiff, kayanya kalau kita ngobrol bisa sampe satu gedung lorong juga denger kak hehe",  
                "pesan":"selalu ceria ya kak! moodbooster banget, lucuu!!"# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "kakak cantikkk, cantik sekalii, diam aja cantik? ramah juga lagi",  
                "pesan":"semoga dapat pasangan yang setara ya kak! kalau ga waw aku kecewa"# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "bang haniff kalem dan lucu?!",  
                "pesan":"semnagattt terus bangg hanif!!"# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "kakaknya cantik dan lucuuu",  
                "pesan":"semangatt terus kak survive semester 5 nya!"# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "kak zahra si maniss dan imutt",  
                "pesan":"jangan lupaa untuk selalu jaga kesehatan yaa kakk!!"# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EApI5_yYi7cfGrkXuj9_FB67WBjOGFDi", #1
            "https://drive.google.com/uc?export=view&id=1_UcBXq1R4Zl8dPgugfgFsWvy9DNqj0Zc", #2
            "https://drive.google.com/uc?export=view&id=1wPDyAGiqxstWUvcO8qun4ee6TkJyb7hF", #3
            "https://drive.google.com/uc?export=view&id=1C9-nEEwE9QrukMSU8JuCJIMlugF-nfmM", #4
            "https://drive.google.com/uc?export=view&id=1ioN7y6EzAcv7i2Z29_w3VYZJJ7unbOI1", #5
            "https://drive.google.com/uc?export=view&id=1AjpGZwz3W_TrO_Pnz-R4O3jhsO3Ne_H2", #6
            "https://drive.google.com/uc?export=view&id=1c85e-q7y8DtwPEVCnsVV-f0oOj0Pojn9", #7
            "https://drive.google.com/uc?export=view&id=1p5cUa-BtiHz84WA1hzKLJXrSMDzfpnAc", #8
            "https://drive.google.com/uc?export=view&id=1PjdX1CJhmXzFzt_KmcL6qnanhnj2rtHG", #9
            "https://drive.google.com/uc?export=view&id=14vQeYVBM0xOW05j25XalOd4IlwCqBC4h", #10
            "https://drive.google.com/uc?export=view&id=1BlbxGZteUa1dO7pMbQXeI6p7iUdZ1eNv", #11
            "https://drive.google.com/uc?export=view&id=1AWisDxHg4i-KLtlaEeth2Vs-i0_lPWua", #12
            "https://drive.google.com/uc?export=view&id=15RifzNgkxzieVEO9EE6nu1PfD0KI-FBp", #13
            "https://drive.google.com/uc?export=view&id=1SfKKMpASryfFUnmT6FB74H7ZjVE-8Zii", #14
            "https://drive.google.com/uc?export=view&id=1Q9ThTUgccWKl2qxrELnKPLyp_4_y_kjS", #15
            "https://drive.google.com/uc?export=view&id=1GcUDZONpSKR1-ybf5nqlyji9KpEcDUPb", #16
            "https://drive.google.com/uc?export=view&id=1IhCLurujFg-r9kU-t0j_mTvLIWd0QRX_", #17
            "https://drive.google.com/uc?export=view&id=11gCIvvfUSwuPz3zcYrClgYDV7cRdbp1I", #18
            "https://drive.google.com/uc?export=view&id=1zaxbOq6F00oqKMULhaEHkfarKmZYT_LK", #19
            "https://drive.google.com/uc?export=view&id=1hOescYUGDiOAovr81izr3NQ4T4pgNzCJ", #20
            "https://drive.google.com/uc?export=view&id=1wgfZU8287WvkEGedm7_9CvMGWFnAf-Pc", #21
            "https://drive.google.com/uc?export=view&id=1tHMYVg9LFu8EhsyCJDSaGj1q0U6maqo_", #22
            "https://drive.google.com/uc?export=view&id=1Ew3z_ZvxH599Gywpl3orhu-ImQMMft_s", #23
            "https://drive.google.com/uc?export=view&id=1m1kIoJg4wcgI1fdflQuEP2iRGsLFHiz2", #24
            "https://drive.google.com/uc?export=view&id=1VgNB3bU4R8jzT-_S6fIQaiJNh3KisT_Z", #25
            "https://drive.google.com/uc?export=view&id=1nYa8tpnvg5aBRwjbDsXRWz9CkVXuKPuP", #26
            
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "keren banget bang bisa sejauh ini mimpin dept yang menaungi kaderisasi",  
                "pesan":" semangat terus bang, semoga selalu dikelilingi keberuntungan dan orang-orang baik!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri Sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "selalu suka ngeliat ka fifah, effortless to be pretty",  
                "pesan":"senyumnya jangan luntur ya kaa, cantik banget soalnya!^^"# 2
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "kak alya punya wangi yang khas, kalau udah nyium wangi itu pasti -oh itu kak alya-",  
                "pesan":"semangatt ka alya, kakak keren banget bisa profesional gitu!"# 3
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "bang ahmad keren banget bisa sejauh ini!",  
                "pesan":"tetep jadi bang ahmad yang rendah hati ya bang! semangatt terus bang!"# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "kak arin cantik! aslinya baik banget cuman harus professional ya ka hehe",  
                "pesan":"semangat kakak sekree, sehat selalu ya kak!"# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "bang daffa walaupun marah-marah, tapi aku ga pernah kesel, satu-satunya diantara yang lain",  
                "pesan":"semangat terus bang dap, sehat selalu ya bang!"# 6
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "bang fajar keren dan baik, orangnya tenang",  
                "pesan":"bang, terimakasih ya udah jarang marah ke saya^^"# 7
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "kakaknya receh, kayanya yang paling gabisa nahan ketawa",  
                "pesan":"semangattt kak nataa semoga sehat selaluu!!"# 8
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "bang nobel keren bisa sampai jadi penutor buting dll",  
                "pesan":"semoga jadi data engineer ya bang"# 9
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "bang fajar tegas dan berwibawa, tapi tetep toleran",  
                "pesan":" semoga selalu ya bangg jaga kesehatannyaa!!"# 10
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakaknya tegas kalau ketawa lucu",  
                "pesan":"makasi banyak ka vany, pas waktu aku nangis kaka yang paling care diantara yang lainnya, walaupun kakak hobinya marah-marah tapi aku tau aslinya kakak itu hati selembut marshmallow hehe, makasi banyak ya kak itu sangat membekas di aku kak, sehat selalu ka vany cantik! (gabisa emot love)"# 11
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "bang Sahid ramah dan bersemangat, selalu aktif di setiap kegiatan",
                "pesan": "Terus jaga semangatnyaa ya bangg!!" # 12
            },
            
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "bang ali vibesnya ramah",
                "pesan": "semoga abang bisa jadi data enggineer" # 13
            },
            
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kak Rosalia baik dan ekspresif",
                "pesan": "selalu jaga semangatnya ya kaaakk!!" # 14
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "-",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak kharisma awalnya aku ngiranya jutek, tapi ternyata emangg gitu kalau lagi ga senyum",
                "pesan": "jangan luntur senyumnya ya kak, kakak manis kalau senyum soalnya!" # 15
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kak fera cantik sekali, cocok sama kacamatanya!",
                "pesan": "semoga selalu dikelilingi oleh orang-orang yang baik ya ka" # 16
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "bang sahid supel, dan bisa bergaul dengan siapapun",
                "pesan": "next time perlukah kita lanjutkan membahas tentang kenapa aktuaria UI ga dapet kerja?" # 17
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Kak Daffa keren dan ternyata orangnya receh",
                "pesan": "semoga cepet-cepet lulus ya bangg!" # 18
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "bang Ihsan suka gangguin orang",
                "pesan": "bang, nama saya aqila, bukan ale..." # 19
            },
            
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "Kak Rewina orangnya kalem tapi terlihat peduli sama orang-orang disekitarnya",
                "pesan": "Terus semangat dan semoga kakak bisa dikelilingi oleh orang-orang yang tulus ya kaa!" # 20
            },
            
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "bang Benget jago banget main futsal + kalau ngejokes lucu terus",
                "pesan": "Terus latihan dan terus nge jokes ya bang! moodbooster tongkrongan abang ini" # 21
            },
            
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "bang Uliano multitalenta banget dan punya karakter unik",
                "pesan": "karena abang masuk manjakat bidang paino, jadi pengen denger bang ulliano main piano" # 22
            },
            
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "bang kevin baik dan jarang marah-marah",
                "pesan": "semoga selalu sehat sentosa ya bang!" # 23
            },
            
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "Kak Erma enerjik dan ceria banget",
                "pesan": "semoga tetep diberikan kesehatan sehingga bisa beraktivitas dengan normal ya ka!" # 24
            },
            
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kak Lidia lembut dan ramah",
                "pesan": "Semoga makin aktif dan sukses di setiap langkahnya kak!" # 25
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "bang ridwan orangnya kalem",
                "pesan": "Semoga selalu diiringi dengan keberuntungan ya kak!" # 26
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    psda()
# Tambahkan menu lainnya sesuai kebutuhan

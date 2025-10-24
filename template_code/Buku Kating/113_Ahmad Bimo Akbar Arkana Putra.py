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
            "https://drive.google.com/uc?export=view&id=1PGCujq4cU5mLL_VRWhYon7PsfpmXuFKt",
            "https://drive.google.com/uc?export=view&id=1D7Iv0GSp-hGAgawIyYBJO1mwPtNxPTYe",
             "https://drive.google.com/uc?export=view&id=1qgyM8h0GXq8Wt2eHtv75OC2iSqSz_nf2",
             "https://drive.google.com/uc?export=view&id=1hfl-sS9oYd0qCUWO8B-AZo-a2nx479RG",
            "https://drive.google.com/uc?export=view&id=1bunSFnO26S67bDso7Bp4hJdMoKdKLl_m",
             "https://drive.google.com/uc?export=view&id=166RRCEq7Kp4976s3ZZkjtXkM4mvQm3SD",
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
                "kesan": "abang ini ternyata asik disamping seriusnya, gokil banget!",  
                "pesan": "sukses selalu buat bang rendra, semoga apa yang diharapkan tercapai"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abang ini kocak banget, tapi pas serius juga keren!",  
                "pesan": "semoga segala urusannya dilancarkan semua ya bang"# 1
            },
              {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya cantik dan manis, asik juga kalau diajak ngobrol!",  
                "pesan": "panjang umur dan sehat selalu buat kakaknya"# 1
            },
              {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "ini pendiam tapi lucu, manis deh!",  
                "pesan": " sukses selalu buat kak syadza, semoga apa yang diharapkan tercapai"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "ini kucu dan kocak bangett, cocok banget di pairing sama bang jo!",  
                "pesan":"semangat terus buat kakaknya,semoga apa yg diharapkan dapat tercapai ya kak!"# 1
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "kakaknya asik dan kucu, bikin gak ngantuks",  
                "pesan": "Jaga kesehatan terus !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LRVcgyxwXRcK0E9hPi-ZqUuIjcpCgMu6",
            "https://drive.google.com/uc?export=view&id=19dMH__sGXaRQqLQY3VmC-fTrC8aWrut3",
             "https://drive.google.com/uc?export=view&id=1Be3OqSk9ALM8RAnUGB_4D6XFinBWQysx",
             "https://drive.google.com/uc?export=view&id=1o01eTs77dtVWrkoq2lcxoTfbSdJG58l6",
            "https://drive.google.com/uc?export=view&id=1PZrT9VDUVq6ZrOedCG7B8YE8t-hDJHLL",
             "https://drive.google.com/uc?export=view&id=1Uv0DzIQDPb1byuF56ToTZG28hO9oJO0y",
            "https://drive.google.com/uc?export=view&id=1ddLl1IBjmTMvjwijc0RTKfgrnoVdaN57",
            "https://drive.google.com/uc?export=view&id=1jE6k91N2fF7mwjRaWD1TcDp38bkMkMwv",
            "https://drive.google.com/uc?export=view&id=1W7CZC9DpO42dLJySxlbE2UJJJ_atHUpp",
            "https://drive.google.com/uc?export=view&id=1RXMeTijGoLYDw_o9lZD-I0GtELFK2iCL",
            "https://drive.google.com/uc?export=view&id=11qi_JaUaZ-VOk57pbP7BcCqpLat7X5CG",
            "https://drive.google.com/uc?export=view&id=12IuT0_kXci-EAYxMz5PVEtsHj1SDRyAG",
            "https://drive.google.com/uc?export=view&id=1204jBYdUXynkel5kUQ7Up7r1crAtoaKr",
            "https://drive.google.com/uc?export=view&id=1WolkB1r9LudKuhsJP4HHijkgECJCjv0Z",
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
                "kesan": "abangnya chill, tapi kalo lagi menjelaskan jadi serius. sering melawak tapi aura pemimpinnya tetap ada",  
                "pesan": " sehat selalu buat abangnya"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "kakaknya lucu deh, asik juga",  
                "pesan": "Sehat selalu kak, dilancakan semuanya "# 3
            },
              {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "kece dan keren ini",  
                "pesan": "semangat terus buat kak putri "# 1
            },
              {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kakaknya terlihat pendiam, tapi setelah beberapa saat asik juga ternyata",  
                "pesan": "sehat dan sukses selalu buat kakaknya "# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "awal liat abang ini pas pplk, aura orang pinternya kerasa banget, bikin saya termotivasi ",  
                "pesan":"terus melangkah maju dan berkembang ya bang "# 1
            },
             {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya lucu dan manis kayak cewe anime2,pas menjelaskan materinya juga enak banget penjelasannya",  
                "pesan": "semangat terus yaa buat kak feby wulandary"# 1
            },
              {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "kece dan keren banget abang satu ini, gokil abis",  
                "pesan": "Sukses dan sehat selalu ya bang "# 1
            },
              {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "kalo kata cewe2 di kelompokku abang tipe2 cowo ghibli, pada saat wawancara abang ini juga chill banget",  
                "pesan": " semangat terus bang, semoga apa yang dicita-citakan tercapai"# 1
            },
              {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "kakaknya asik dan lucu, saat wawancara juga banyak menjawab",  
                "pesan": "sehat dan sukses selalu ya kak"# 1
            },
              {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "kakaknya asik dan manis, aura ceria nya kerasa banget. kakaknya juga baik dan ramah ",  
                "pesan": "semangat terus buat kakaknya dan sukses selalu ya kak "# 1
            },
              {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "tidak banyak bicara awalnya, tapi seiring waktu berjalan, abang ini ternyata asik, sering ngejokes2 ",  
                "pesan": " sehat dan sukses selalu bang ridho"# 1
            },
              {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": " abangnya kece dan keren, saat menjawab pertanyaan juga abang ini menjawab dengan terstruktur penjelasannya",  
                "pesan": "sehat selalu dan semoga di perlancar semua urusannya ya bang"# 1
            },
              {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "kakaknya asik dan baik ",  
                "pesan": " sehat dan sukses buat kak monika "# 1
            },
              {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "pertama kali liat kak wan pas pplk, baik dan perhatian orangnya. ",  
                "pesan": "sehat dan sukses selalu buat kak wan, semangat terus ya buat kuliahnya"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19Bg9SgI-DkZHrshnBaAJIWsklRAi_7VC",
            "https://drive.google.com/uc?export=view&id=1jpCDSTIDVHjSuaJFqClYJjYxE6dP6uX4",
             "https://drive.google.com/uc?export=view&id=1obfPJyEBdw5WiSWfkWbl-6RngVXipdAn",
             "https://drive.google.com/uc?export=view&id=1eK7GaXn_3NhplVEa9i81BH_f26OH7uTv",
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
                "kesan": "pertama kali ngelihat bang bintang pas pplk 2024, lucu dan care banget orangnya.baik dan seru juga.pas tau ternyata adalah senator.makin kagum lagi saya . pas menjelaskan sesuatu pasti terstruktur dan mudah dimengerti penjelasannya",  
                "pesan": "sehat dan sukses selalu buat bang bintang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya baik dan asik, pada saat wawancara juga ini memberikan penjelasan yang mudah dimengerti!",  
                "pesan": "semangat dan sukses selalu buat kak nadya"# 1
            },
              {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "ini overall aku liatnya kayak wanita independen. kayak tipe cewe yang apa2 bisa sendiri!. lucu dan manis juga kakaknya",  
                "pesan": "semoga apa yang dicita - citakan tercapai ya kak!"# 1
            },
              {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "ini awalnya aku kira pendiam, tapi makin lama asik dan kucu juga !",  
                "pesan": "semangat terus buat kak hanaa!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EWlAIbAbCZxwU7HCled91IK1wY4BUrQA", #1
            "https://drive.google.com/uc?export=view&id=1Hct6z7R17GsYum3UQG2TSJDNlQXii5eu", #2
            "https://drive.google.com/uc?export=view&id=169VtIv9MeIMIlLNuSs6WUhNsCF0YJVaT", #3
            "https://drive.google.com/uc?export=view&id=1qKRzI7cO-HoDyC3HSfjigTTKLx5n0di1", #4
            "https://drive.google.com/uc?export=view&id=1hsR28wn2YsabNB4uIboSfzeRoOI5niAC", #5
            "https://drive.google.com/uc?export=view&id=1caJm7fc1ggPNcIgXQYNfggmH2Ps_N546", #6
            "https://drive.google.com/uc?export=view&id=11mCv9mo_PJE7_n5muTtXd2OtRbcLOWUI", #7
            "https://drive.google.com/uc?export=view&id=10lwQQ1llOVTomhbzzLZkdimtwFxyvyXR", #8
            "https://drive.google.com/uc?export=view&id=1dtG0GOzKrep_199Jac0ymZwWFaxs1ZGA", #9
            "https://drive.google.com/uc?export=view&id=1upmYWMUWl4HqVTOkc_HOfEJYyTbUXQJB", #10
            "https://drive.google.com/uc?export=view&id=1kxlxlBhDIdE6JWtCUawnGA2gyLcCSO3l", #11
            "https://drive.google.com/uc?export=view&id=1mxPR0EgW_bQuAi7Pzr_6T2FO1gHXPK_r", #12
            "https://drive.google.com/uc?export=view&id=1NpXIhwalk4mXg_UpNse3htz5uenbWu5J", #13
            "https://drive.google.com/uc?export=view&id=1d-S4u5iwNm7jUMOXt1WxAhC2U-FxoKIr", #14
            "https://drive.google.com/uc?export=view&id=1ZCn3xsar6L2JSQ11yyI9nRW1_elzqaLi", #15
            "https://drive.google.com/uc?export=view&id=1hsyklE50AaCC9Hy5B4k6UxF57B7tlhmV", #16
            "https://drive.google.com/uc?export=view&id=1xkh5kyka72Rq0Tvfu9GB29L54NjINMHT", #17
            "https://drive.google.com/uc?export=view&id=1mTNS_-XZqaNsTOzfa-q4elwhJU1r8D3s", #18
            "https://drive.google.com/uc?export=view&id=1c4LWBfOqbnp_5LfSKmvQGwgNG_rxHx1S", #19
            "https://drive.google.com/uc?export=view&id=17FJQ9fc0BDJzWw4nNQrNRL4uqM1r2GsE", #20
            "https://drive.google.com/uc?export=view&id=1sDH2PeupmbjbaTqFjwAeTVWq01CfIP28", #21
            "https://drive.google.com/uc?export=view&id=1MQbFtI0aangnQiIMm66lHESOyDrPGBJW", #22
            "https://drive.google.com/uc?export=view&id=1dNhZPYBOkpey-r6HhHlheEMim1tVadvV", #23
            "https://drive.google.com/uc?export=view&id=1PAGy2aKCXwE7EYtpCuOP-2tFRCCe3mfT", #24
            "https://drive.google.com/uc?export=view&id=1DYXXPs9OCxQAwb3O0OlsXK5CFX3OMN2o", #25
            "https://drive.google.com/uc?export=view&id=1e4QM7z_yKyGRBn7QgWIA86gf546qSadi", #26
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21 ",
                "asal":"medan ",
                "alamat": "tanjung seneng ",
                "hobbi": "futsal ",
                "sosmed": "@ferdy_kevin ",
                "kesan": "tampang abang ini chill banget, tapi kalau sudah serius tegas . ",  
                "pesan":"sukses dan selalu bang ferdy "# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20 ",
                "asal":"jawa barat ",
                "alamat": "korpri ",
                "hobbi": "mikir ",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya manis dan cakep, tapi pas kaderisasi agak galak, bikin segan . tapi diluar itu kak nisrina baik dan ramah  ",  
                "pesan":"semangat terus kak, sukses dan sehat selalu kak "# 2
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "pertama kali melihat pas pplk bareng bang bintang, kakaknya care dan lucu. tapi pas kader tegas dan berwibawa. bikin segan dan sedikit takut. tapi diluar itu kak alya baik dan ramah  ",  
                "pesan":"sehat dan sukses selalu kak allya,semoga jalan di depan dipermudah dan diperlancar "# 3
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "bang ahmad ini selalu bikin kagum, mulai dari pemikiran2 nya dan integritasnya. abangnya ramah dan perhatian . ",  
                "pesan":"sehat dan sukses selalu bang ahmad "# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "kakaknya pas kader serem , tapi pas diluar baik dan ramah juga. ",  
                "pesan":" semangat buat kak arienta kuliahnya ,sehat dan sukses selalu "# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "abang ini pertama kali ngeliat asik dan lucu, pas masuk kader baru keliatan tegas dan seremnya, tapi diluar itu bang daffa humble dan baik",  
                "pesan":"sehat dan sukses selalu bang daffa "# 6
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "bang fajar orangnya chill keren juga gayanya ",  
                "pesan":"semangat dan semoga cepat lulus ya bang "# 7
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "kakaknya baik dan perhatian, tapi pas di kader tegas juga ",  
                "pesan":"semangat terus buat kak natasya , semoga diperlancar semua urusannya "# 8
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "kece parah abang ini, tegas juga pas nge kader. diluar itu abangnya baik dan perhatian. jago ngoding juga. memang asli keren abang ini ",  
                "pesan":"sehat dan sukses selalu bang , semoga semuanya diperlancar urusannya. skill sulap kartunya kemarin buat lebih keren lagi dong bang. masih bisa ketahuan tricknya "# 9
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "bang aji ini orangnya humble dan perhatian juga.  ",  
                "pesan":"semangat terus bang aji "# 10
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "baik hati dan pengertian ",  
                "pesan":" semangat terus buat kak vany "# 11
            },
             {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "abangnya humble banget, murah senyum juga. plus chill dan nyantai gayanya ",
                "pesan": "semangat dan sukses selalu bang " # 12
            },
             {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya chill dan cool juga ",
                "pesan": "semoga cepat lulus ya bang kuliahnya " # 13
            },
            
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": " ",
                "pesan": " " # 14
            },
            
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya agak serem. tapi pas diajak ngobrol asik dan murah senyum juga ",
                "pesan": "jangan lupa senyum ya kakk, manis soalnya " # 15
            },
            
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya chill habis, kalau senyum manis banget ",
                "pesan": "semangat ya kak , semoga urusan kaka semuanya diperlancar " # 16
            },
            
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "abangnya enak banget kalau diajak ngobrol. sabar banget kalau lagi ngejelasin sesuatu ",
                "pesan": "semangat buat abangnya " # 17
            },
            
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "tegas dan berwibawa ",
                "pesan": "sehat dan sukses selalu ya bang  " # 18
            },
            
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "abangnya keren dan kece. asik juga sifatnya.  ",
                "pesan": "semangat buat abngnya sehat dan sukses selalu " # 19
            },
            
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "baik dan pengertian ",
                "pesan": "sehat selalu kak" # 20
            },
            
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "orangnya lucu dan ada aja gebrakannya. disamping itu abangnya baik juga ",
                "pesan": "semangat dan sukses selalu bang benget " # 21
            },
            
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "abangnya serem banget kalo lagi marah . tapi diluar itu orangnya baik dan pengertian ",
                "pesan": "semangat terus bang liano " # 22
            },
            
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "abangnya keren dan asik ",
                "pesan": "tetap semangat bang " # 23
            },
            
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "kakaknya manis dan lucu. saya yakin kakakk orangnya humble dan baik ",
                "pesan": " dance nya keren banget kak " # 24
            },
            
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakaknya baik dan pengertian ",
                "pesan": "sehat selalu kak " # 25
            },
            
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "gokil dan kece ",
                "pesan": "semoga diperlancar semua bang urusannya " # 26
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15OSSQJMZek8KdRBtEKIBue69lUna6BCD", #1
            "https://drive.google.com/uc?export=view&id=18Rhi6jjm4xKlrpW2ZaxTFzHdl_Obdf9s", #2
            "https://drive.google.com/uc?export=view&id=1YNbzD5JsBygGFUPaCkoQhKSvlXgjoDox", #3
            "https://drive.google.com/uc?export=view&id=13WJw2Lr73bHvK4LflWxCXl9cwaLT66qL", #4
            "https://drive.google.com/uc?export=view&id=1LH3OVdv67A2Qpy50i8cgX4bpme0p3ehC", #5
            "https://drive.google.com/uc?export=view&id=1RLkKuLxaQZdZ_rwLkJbtDFIuP6GCd0aM", #6
            "https://drive.google.com/uc?export=view&id=1xs7aqc0k_qVLLQt-jTnU7A8p2zShE8TD", #7
            "https://drive.google.com/uc?export=view&id=10Rrf2jOeeh8Duoj0EZAOOJezL82M-3Qj", #8
            "https://drive.google.com/uc?export=view&id=1y42GlJxP20Wwu0xNpl2D7FjfySwgz9Uk", #9
            "https://drive.google.com/uc?export=view&id=1skIcsJf3zO8TschLv1EGWW79Fi8Znoa_", #10
            "https://drive.google.com/uc?export=view&id=1Isy_NYqS30TzD77sge3uQwR5WORUdwu5", #11
            "https://drive.google.com/uc?export=view&id=1mN4vAoF7m25V3ZjmxmwYry6YDeyfIjio", #12
            "https://drive.google.com/uc?export=view&id=1gOm11k3JodEqwiilvQ-1r2GtRd4ZlSfv", #13
            "https://drive.google.com/uc?export=view&id=13krtaBCDjmw5gBwed9rV9z9coI3s78cY", #14
            "https://drive.google.com/uc?export=view&id=1olGeWWsh34fhKFaoCAwyXpeOu-kpP_eM", #15
            "https://drive.google.com/uc?export=view&id=1KpaAG6urHTOriibdHWcHf0o5lfKlBJ0q", #16
            "https://drive.google.com/uc?export=view&id=1zZrujMTJuQUKO1UvTuqvqqVQanJ8144d", #17
            "https://drive.google.com/uc?export=view&id=1xCzLE8-iN_7SB8eoxcuaz3KQqeL4Nj9D", #18
            "https://drive.google.com/uc?export=view&id=17UTHtbTnyCQQNrwoCSSLLc14bPg4Yojh", #19
            "https://drive.google.com/uc?export=view&id=1muzDENwqAY-dzHV4IIJzFtk-YI6f_ngj", #20
            "https://drive.google.com/uc?export=view&id=1OLOME-yl8b63ArhRXph0fmSXzihd2aOu", #21
            "https://drive.google.com/uc?export=view&id=1He3sInCXYg1E6t68KqG3tBGWejb7oF0X", #22
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
                "kesan": "abannya cheerfull dan murah senyum ",  
                "pesan":"semangat dan sukses selalu bang "# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "baik dan pengertian  ",  
                "pesan":"sehat selalu kak "# 2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "tegas dan berwibawa ",  
                "pesan":"semoga dilancarkan segala urusannya ya bang"# 3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "19",
                "asal":"bengkulu",
                "alamat": "jl,lapas.belwis",
                "hobbi": "maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "manis , baik dan pengertian ",  
                "pesan":"semangat kuliahnya ya kakk "# 4
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "pintra, sangat menginspirasi, dan lucu ",  
                "pesan":" terus maju bang "# 5
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": " tinggi banget, kocak dan asikjuga abangnya ",  
                "pesan":"sehat selalu ya bang "# 6
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "keren dan kece ",  
                "pesan":" jangan lupakan kami ya bang "# 7
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "tenang dan memiliki kesan independen woamn ",  
                "pesan":"semangat terus kak "# 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "humble dan asik kakaknya ",  
                "pesan":" sukses selalu kak " # 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": " chill dan cool, ramah juga ",  
                "pesan":" gas terus bang, jangan lupa istirahat "# 10
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "pengertian dan charming  ",  
                "pesan":"sehat selalu buat kak anggi "# 11
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "baik dan pengertian ",  
                "pesan":"panjang umur dan sehat selalu ya kak "# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": " cantik ,manis dan kalem ",  
                "pesan":" semoga segala urusannya diperlancar ya kak "# 13
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakaknya manis dan anggun",  
                "pesan":" semoga sukses selalu ya kak"# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kakaknya kelaitannya lemah lembut dan murah senyum",  
                "pesan":"Semoga kakaknya lulus tepat waktu dan mendapatkan nilai terbaik"# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Abangnya baik banget mau ngasih ilmu ngoding, belajar sama abangnya ngoding jadi simple ",  
                "pesan":"terima kasih buat ilmunya bang "# 16
            },
            { 
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": " Kakaknya vibes positif pake banget",  
                "pesan":"Semangat terus buat kakaknya jangan patah semangat "# 17
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "asik ,lucu,dan unik. paket lengkap deh pokoknya ",  
                "pesan":" Semoga keinginannya tercapai dalam waktu dekat "# 18
            },
          
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakaknya baik banget dan perhatian",  
                "pesan":"Semangat terus bang semoga banyak prestasi yang menghampiri"# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya tipe yang langsung asik deh kayaknya",  
                "pesan":" Semangat terus ya kak di dunia perkuliahannya"# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya baik banget mau bantuin dan ngasih tau banyak hal tentang website",  
                "pesan":"terima kasih buat sharing2 nya bang"# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya kalem banget ",  
                "pesan":" semangat terus ya bang"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1p4CK9kMKjrRcWpuAeo64XfnUpm2VmftB", #1
            "https://drive.google.com/uc?export=view&id=1ZW_x5oUWuj4QXgYJGT8dLvz28t4x4dew", #2
            "https://drive.google.com/uc?export=view&id=1gBgsMIExJ5uHOZmMl-Dd038pwZCB7uCF", #3
            "https://drive.google.com/uc?export=view&id=1WLA3AmqCs4X9TFnpTvDblJVkoxO_xlq3", #4
            "https://drive.google.com/uc?export=view&id=1-eoCaOY_94mKBcUVLNNusX5_sodU7S3F", #5
            "https://drive.google.com/uc?export=view&id=1qx3T2sErYefRZtn_RkJtLx3WeTByGG0n", #6
            "https://drive.google.com/uc?export=view&id=1DgH1wuui3sSrT2rweno9vfXlZxnPBxPB", #7
            "https://drive.google.com/uc?export=view&id=1Xka578kRqGugOJSAAzXHot5iac82Dw1r", #8
            "https://drive.google.com/uc?export=view&id=112UI8Kp4UtHpnwGU9LOgHBZxNFAu3yRO", #9
            "https://drive.google.com/uc?export=view&id=11ERhjQ7QJXcffabO-hvDR9Q2yW3I4wBQ", #10
            "https://drive.google.com/uc?export=view&id=1iBYM0Mme5Gleb13fI0gs5PtPw_zoSD1M", #11
            "https://drive.google.com/uc?export=view&id=1IX1MBRduubs5PbJcs30TXWCcvDSsX5W0", #12
            "https://drive.google.com/uc?export=view&id=1SG6XfhX8Tl8VCBZ5kfj0_pQhmsKPUarE", #13
            "https://drive.google.com/uc?export=view&id=180yRSFcTf9MFFuPIiCzYTAztg-_w5Isi", #14
            "https://drive.google.com/uc?export=view&id=1OUZ_reCbzW7q4qY94j2yY8NzBGjUpLeN", #15
            "https://drive.google.com/uc?export=view&id=1GlDHPrPGrkOlaBSOk_KmX76VaCfclHrb", #16
            "https://drive.google.com/uc?export=view&id=1bcr-fJ5Am_X85fjgbD1eMdRdU1mPtvyE", #17
            "https://drive.google.com/uc?export=view&id=1Vwg-h0NCdadnVU29XC8z1erEkDDmz0t0", #18
            "https://drive.google.com/uc?export=view&id=1Cg8zEd5eldwPwaMHPfr0Wzd5H2BJOE-u", #19
            "https://drive.google.com/uc?export=view&id=1H70f1A9Rg1uKI1ohtBxe2xgzQjmw6ZP6", #20
            "https://drive.google.com/uc?export=view&id=18JZguqhX2OCtmYivYmalygb8k32Xgx5H", #21
            "https://drive.google.com/uc?export=view&id=1M4wNDLKkikMaWr4_8lQsiKEEg32I6TL1", #22
            "https://drive.google.com/uc?export=view&id=1MKjWGG1yuzk7doYZoe51qWwFgejhxb7q", #23
            "https://drive.google.com/uc?export=view&id=1DThVLTB-3gPBY3pTPyFqEvnSpd6fLLuq", #24
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulan",
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
                "nama": "Yohana Manik",
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
                "nama": "Dea Mutia Risani",
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
                "nama": "Devyna Sonya Palupi Sanjaya",
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
                "nama": "Luthfia Laila Ramadhani",
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
                "nama": "Cindy Laura Manik",
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
                "nama": "Desman Velius Halawa",
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
                "nama": "Dea Amanda",
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
                "nama": "Irvan Alfaritzi",
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
                "nama": "Fathya Intami Gusda",
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
                "nama": "khazanatil ilmi",
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
                "nama": "Nurul Izzah Istiqomah",
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
                "nama": "Qois Olifio",
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
                "nama": "Melinza Nabila",
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
                "nama": "Nayla Shafira Roza",
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
                "nama": "Aditya Taufiqurrohman",
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
                "nama": "Tarisya Hidayatul Rahmi",
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
                "nama": "Ratu Keisha Jasmine Deanova",
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
                "nama": "Khoirul Muttoharoh",
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
                "nama": "Arya Muda Siregar",
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
                "nama": "Arini Puteri Elandra",
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
                "nama": "Syahrialdi Rachim Akbar",
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
                "nama": "Lutfia Aisyah Putri",
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
                "nama": "Nabyla Sharfina",
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
            "https://drive.google.com/uc?export=view&id=1oLV2h7keJ8wN5z0OPHIRkqNsm0aEL3-O", #1
            "https://drive.google.com/uc?export=view&id=1DJrddHEJZZrN9pRr42yOGE4FyounAQnA", #2
            "https://drive.google.com/uc?export=view&id=1StpemQIrH9FRxoENfrSpvLv8wcLvEoBO", #3
            "https://drive.google.com/uc?export=view&id=1iSiG6Yn83SqLseWvX-3eDpoBdXLOC24t", #4
            "https://drive.google.com/uc?export=view&id=1ZaCdM0yBtT4CldJ5X8TDDRQy11mobiKy", #5
            "https://drive.google.com/uc?export=view&id=16qk5kXvMs5nq3S-QlkVsVn2KP0HzVyBQ", #6
            "https://drive.google.com/uc?export=view&id=1tiaq_WvVYhbobm1ysSpuEH21oaaWBKfH", #7
            "https://drive.google.com/uc?export=view&id=1cX69QcX5Kfr2tPu0x86dw33e18v8IJgT", #8
            "https://drive.google.com/uc?export=view&id=1UotkNRMNy9rFgr73NeLHT8bA2YFK-T81", #9
            "https://drive.google.com/uc?export=view&id=1q4Fm6xrQiRd31zP2FLr38TkHytMvux4c", #10
            "https://drive.google.com/uc?export=view&id=1oAu0sbRw4ZqIHf4fpsDayUaSNJ4nYPaP", #11
            "https://drive.google.com/uc?export=view&id=1a5gKdbg2GiES7DXzZirV7mQMGbvS2T8y", #12
            "https://drive.google.com/uc?export=view&id=1VumK5aAcXhUiwJrbpqlHuNlQkcyH0Mk8", #13
            "https://drive.google.com/uc?export=view&id=1ZpSVpou_hYSM_TEN172Hu_czzC2lGRaC", #14
            "https://drive.google.com/uc?export=view&id=18w-t_w5Wl82ZbT4w2hcjUa7J1ZEDVhdm", #15
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
                "kesan": "  kakaknya humble dan ramah banget",  
                "pesan":" semangat ngejalanin semester-semester akhirnya kak, jangan sampai stress ya kak"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": " kakaknya kerenn banget ",  
                "pesan":" semangat untuk terus berkembang ya kak"# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya vibes positif banget ",  
                "pesan":" tetap selalu jadi orang yang memilki vibes positif ya kak"# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "hobinya keren ",  
                "pesan":" semangat untuk terus berkembang ya kak"# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": " Abangnya keren, cool, awalnya ngira serius aslinya abangnya murah senyum ",  
                "pesan":"  Semangat terus bang jangan tinggalkan ibadah"# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya kalem banget tapi murah senyum ",  
                "pesan":" Semangat terus buat kakaknya dan sehat sehat terus ya kak "# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakaknya kalem banget tapi murah senyum ",  
                "pesan":" Semangat terus buat kakaknya dan sehat sehat terus ya kak"# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Abangnya tipe softboy gitu ",  
                "pesan":"Semangat menjalani hari harinya bang "# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "  Abangnya ramah banget dan murah senyum",  
                "pesan":" Semangat terus bang semoga cepat lulus bang"# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya baik banget, dan tipe lemah lembut ",  
                "pesan":"Semangat terus bang semoga cepat lulus bang "# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik banget, seru seru semua games yang kakak bawakan ",  
                "pesan":"  Jaga kesehatan dan jangan sampai tinggalkan ibadah ya kak"# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Kakaknya lucu, manis, cantik ",  
                "pesan":"Makasih kak udah ada di dunia ini semoga kita ketemu lagi ya kak "# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Kakak Hanif jiwa introvertnya menguar banget, sama seperti saya ",  
                "pesan":"Sehat selalu ya kakak, semoga semua dipermudah! "# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": " Kakak Sarah jago main musik, tambah keren sekligus tambah cantik",  
                "pesan":"Semoga selalu diberikan kebahagiaan ya kakak! "# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": " Kakak Zahra, manis sekali",  
                "pesan":"Kakak Zahra, manis sekali "# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VEPe_ENBpKo5MfA9NIjrGJCDf9mJcUo-", #1
            "https://drive.google.com/uc?export=view&id=1rin2xakvobKuG2Iav8fDxazEot14v8XA", #2
            "https://drive.google.com/uc?export=view&id=1e-fjP22c_hej4xQCzlj-DWRTZkNUIaw8", #3
            "https://drive.google.com/uc?export=view&id=1h-YJFzjlzEwrQU470Wle3h193Vdaf6bw", #4
            "https://drive.google.com/uc?export=view&id=1goTpNY-pUaSBgr39ADNd3Xc21WecK2k5", #5
            "https://drive.google.com/uc?export=view&id=1pmCwwvTiudMts5Um4v_tuYQui37EeykX", #6
            "https://drive.google.com/uc?export=view&id=17hq-c3lpCI-ypNR57s-OGe_tfeG37KSO", #7
            "https://drive.google.com/uc?export=view&id=1b98zXsJCkhpqNsUSsFVsNKY5fmedGc07", #8
            "https://drive.google.com/uc?export=view&id=1b98zXsJCkhpqNsUSsFVsNKY5fmedGc07", #9
            "https://drive.google.com/uc?export=view&id=1h-YJFzjlzEwrQU470Wle3h193Vdaf6bw", #10
            "https://drive.google.com/uc?export=view&id=1RxxLdOxD7CK7ps_jruJ9A9sjX5-KeH_0", #11
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
                "kesan": " abangnya lucu suka fllexing, tapi beneran keren kok bang ",  
                "pesan": " selalu jadi inspirasi buat banyak orang ya bang "# 1
            },
            {
                "nama": "Kakak Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": " kakaknya keliatan kalem dan pendiam orangnya ",  
                "pesan": " semangat terus ya kak, dikit lagi wis-udah "# 2
            },
              {
                "nama": "Kakak Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": " abangnya keren banget ",  
                "pesan": " jangan terlalu sering keluar malem bang, nanti meriang "# 3
            },
              {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": " kakaknya keren banget, kaya tomboy gitu vibesnya ",  
                "pesan": "jangan lupa istirahat juga ya kak setelah aktivitas yang melelahkan"# 4
                   },
              {
                "nama": " Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "kakaknya pasti intropet ",  
                "pesan": "hati hati penipuan di facebook ya kak "# 5
            },
            {
                "nama": " Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": " kakak ini agak mirip sama kak nydia dimataku ",  
                "pesan": " jangan lupa makan dan istirahat yang cukup kak  "# 6
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": " abangnya keliatan kalem dan pendiam ",  
                "pesan": "semangat kuliah dan organisasinya bang "# 7
            },
              {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": " kakaknya imut dan gemessin banget ",  
                "pesan": " jangan lupa jaga kesehatan ya kak, jangan sering-sering begadang untuk marathon drakor ya kakk "# 8
            },
              {
                "nama": "Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "kakaknya maniss banget, ga ekspek hobinya ml ",  
                "pesan": "semangat main mlnya kak, tapi tugasnya jangan lupa ya kak "# 9
            },
              {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "kakaknya keren, bisa ngehasilin duit sendiri ",  
                "pesan": "semnagat jual risolnya kak, semoga laku "# 10
            },
              {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "kakak ini imup banget, tapi keliatan kalem orangnya ",  
                "pesan": "jangan sampai lupa waktu ya kak mainnya hehe "# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QA0IUeFauFNm8_J74LGlNGb_AYdO1EMU",
            "https://drive.google.com/uc?export=view&id=16nEUitzlosZx8_6r1bYaqRACjZdiDsUQ",
            "https://drive.google.com/uc?export=view&id=1gJ0mOM-l-IlFA9x7dr62PwYAICNDs120",
            "https://drive.google.com/uc?export=view&id=1y127jLkjqjEPPd5DUKGOS_Yb0LznI1x3",
            "https://drive.google.com/uc?export=view&id=1ag9S1az1JENtw_Bahrn7ccYFlBT_9b51",
            "https://drive.google.com/uc?export=view&id=1267piU4fe6O73uyRE7Ae_V7wDIRfNHCT",
            "https://drive.google.com/uc?export=view&id=1CovHMh5EF2JeINVcRawECzs1nKRznRVG",
            "https://drive.google.com/uc?export=view&id=1zo3I6CuXfvrZEIl-XVWfLyTgEtmpFb_o",
            "https://drive.google.com/uc?export=view&id=1RI7DJC1AwrxTe83H1EmIJYKjbl7SRUEK",
            "https://drive.google.com/uc?export=view&id=1rVK8Qb_P6-IMsLMVBTu3xgW_LxyfLkoq",
            "https://drive.google.com/uc?export=view&id=1CBOk4dEQCAHJbp6XfNgJ_R_P1bXiMqkN",
            "https://drive.google.com/uc?export=view&id=1GfQt7CQ1Ewi63uOsBHDzjTpdU-H0_m3P",
            "https://drive.google.com/uc?export=view&id=11Mk2EVErSwzJbiGxtbr4mQ4HBbzjRLaz",
            "https://drive.google.com/uc?export=view&id=1FfWUXTlM69VQE64xkUrUG3A3QxXn8SBg",
            "https://drive.google.com/uc?export=view&id=1LDZgOzEDQU73C9tgXng7-dUr5oi9tbGj",
            "https://drive.google.com/uc?export=view&id=1S6bX7iB3ZtFctk0paF78kFndMu1W6x99",
            "https://drive.google.com/uc?export=view&id=1WCvWh3EwkO0bjKLE-fW6k4KQsAIAZZg5",
            "https://drive.google.com/uc?export=view&id=15W-mmej5QJprrr1RZ2WN17tCt32POyge",
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
                "kesan": "kak cia ceriaa bangett",  
                "pesan": "bahagiaa selaluu kak"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "cantik gentle gituu",
                "pesan": "sukses selalu ya kak"# 1
            },
              {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Keren banget bang",  
                "pesan": "nilainya A semua ya bangg"# 1
              },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "keren sekali pembawaanya",  
                "pesan": "jaga kesehatan bang"# 1
            },
              {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Kerennnn tapi pembawaanya ada kocaknya",  
                "pesan": "coba ngejokes gitu bang"# 1
            },
              {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": " Sangat humblee",  
                "pesan": "semangat kuliahnya!"# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "girly sekalii, anggunly",  
                "pesan": "tetap semangat berjuang kak"# 1
            },
              {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "keren banget waktu jadi mc GO",  
                "pesan": "semangat terus kak"# 1
            },
              {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "sangatt positive vibesss",  
                "pesan": "bahagia selalu, jangan sedih sedih"# 1
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "kak feby lucuu lucu gaya fotonya",  
                "pesan": "suksesss ya kaaak"# 1
            },
              {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "baikkk bangettt",  
                "pesan": "jangan bosan jadi orang baik ya kak"# 1
            },
              {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "pasti aesthetic orangnya",  
                "pesan": "jangan lupa istirahat kak"# 1
            },
              {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Cantikk sekali kak",  
                "pesan": "bahagia selalu ya kak"# 1
            },
              {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Terlihat malu malu",  
                "pesan": "banyakin ngejokes coba bang"# 1
            },
              {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "cantik, baik lagi, kurang apalagi",  
                "pesan": "hidup lebih baik kak kedepannya"# 1
            },
              {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "manlyyyy",  
                "pesan": "ayo maknai hidup ini"# 1
            },
              {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "lucuu banget warna warni",  
                "pesan": "selalu senyum ya kak"# 1
            },
              {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "sangat imut",  
                "pesan": "bahagia selalu kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

    

# Tambahkan menu lainnya sesuai kebutuhan

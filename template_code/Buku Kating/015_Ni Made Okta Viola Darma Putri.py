import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19AaOD5P-LhEs9l5sKSdjeC3baBjX_zzF",
            "https://drive.google.com/uc?export=view&id=1xZ6QEy4hGtLqbQaJz7Uih0w4o6MMiGoZ",
            "https://drive.google.com/uc?export=view&id=1FXEqM07xDHKFKNDNVv8ksI0ZNWJjUkJu",
            "https://drive.google.com/uc?export=view&id=1FZHqM62XNiiZzzpYpiGHj2MFdVH07ug0",
            "https://drive.google.com/uc?export=view&id=1fZmMslOvOFzyzFEg_rdJj7z3jx6xBg_L",
            "https://drive.google.com/uc?export=view&id=1jhGMkREWeA9C5H9euCXg6C4tRJlm0toI",
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
                "kesan": "Baik, Public Speakingnya bagus, Keren",  
                "pesan": "Semangat TA nya bang semoga lulus tepat waktu "# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren, Baik, Tegas ",  
                "pesan": " Semangat bang joo TA nya, semoga lulus tepat waktu dan jangan lupa untuk selalu jaga kesehatan"# 1
            },
                {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kak elisabeth orangnya Seru, asik,keren,cantik, humble",  
                "pesan": "Kakak semangat ya kuliahnya, semoga selalu diberi kelancaran,kemudahan dan keberuntungan dalam segala hal, kakak keren!"# 1
            },
                {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya cantik mirip sheila dara, manis, baik, ramah, positive vibes ",  
                "pesan": "Semangat kakak cantik kuliahnya, sehat selalu ya kaa "# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Tegas, first impression nya kakak keliatan galak hehe, cantik",  
                "pesan":"Semangat kakak lancar lancar kuliahnya"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Cantik,ramah, baik",  
                "pesan": "Semangat kakak kuliahnya, good luck! "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16iLuxKf1h6H5nMktXERqq1x5pMbsGmD9",
            "https://drive.google.com/uc?export=view&id=1JJHII1iN_InhtU76bRxXIT5oLonYblCu",
            "https://drive.google.com/uc?export=view&id=1q2izGDbkJnysDIxyXCxA3AzAZ5-28wPA",
            "https://drive.google.com/uc?export=view&id=1WXTf9xSgLEbKPOvOST_gVTBgAGEZdU29",
            "https://drive.google.com/uc?export=view&id=1A3k9ooQ6hj_rX8NYC88nFMXRnMpQn20-",
            "https://drive.google.com/uc?export=view&id=1igNLsJAg3ztFdAPIAwZthR_DEpc9320a",
            "https://drive.google.com/uc?export=view&id=1VQK1RpNH0h_V58pgESNsyoXLFCZE7j9L",
            "https://drive.google.com/uc?export=view&id=1YuNIKiIL5LlK-U51u44tGP9XIjQHfnWw",
            "https://drive.google.com/uc?export=view&id=1XiZozRNtT42mP7hihMgQmJcNEOpCcYPg",
            "https://drive.google.com/uc?export=view&id=1mwk6RMUotPIO9_vSpkiRH2V1fLIot3cq",
            "https://drive.google.com/uc?export=view&id=1VoydZ_J0BnruE6hTBZwqCatzgE8YXGOg",
            "https://drive.google.com/uc?export=view&id=10TIEGqyL-HZnRgbrT8Kq60Y68l14845a",
            "https://drive.google.com/uc?export=view&id=1bQmEY5ygKGziukH7ybVhXf114YLzyEFB",
            "https://drive.google.com/uc?export=view&id=1bEzpVFoXkP02rg5KPANtwOe_C4_dvjMN",
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
                "kesan": "Pintar,wangi, baik, ramah,keren ",  
                "pesan": "Sukses selalu bang jeremi!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "cantik, baik,ramah ",  
                "pesan": "Lancar selalu ya kak kuliahnya, aelalu jaga kesehatan!"# 1
            },
                {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Cantik, imut,ramah,baik",  
                "pesan": "Semangat kak kuliahnya semoga kakak selalu dikelilingi hal-hal baik!"# 1
            },
                {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Baik, cantik, ramah, manis",  
                "pesan": "Sukses selalu kak, semoga kuliahnya lancar!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Pintar,baik,ramah, asik ",  
                "pesan":"Semangat bang semoga kelak jadi orang sukses, kalo udah jadi orang suskses info loker ya bang hehe ^.^"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "kakak imutt kiyutttt, cantik, baik, ramah, kiyowoooo, babyface",  
                "pesan": "Kakak semangat yaa kuliahnyaa, still kiyowo gemas imut kiyut yaa kak^.^"# 1
            },
                {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Baik, Ramah, Pintar",  
                "pesan": "Semangat bang kuliahnya, jangan lupa bersyukur hari ini! "# 1
            },
                {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "baik,ramah, keren ",  
                "pesan": "Sukses selalu bang, lancar lancar kuliahnya!"# 1
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
                "kesan": "Cantik, baik,ramah",  
                "pesan": "Semangat kak kuliahnya, semoga semuanya lancar! "# 1
            },
                {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "Baik, ramah, pendiam ",  
                "pesan": "Jangan lupa makan bang, selalu jaga kesehatan ya bang"# 1
            },
                {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Baik, ramah, asik ",  
                "pesan": "Semoga hari hari abang selalu berwarna"# 1
            },
                {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "cantik, baik, ramah ",  
                "pesan": "Kakak semoga kebruntungan selalu menyertai kakak, jangan lupa bersyukur kak! "# 1
            },
                {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "Kak wawa kesayangan pandas!!! cantikkk, baikkk, ramah, penyayang,asik banget, mentor terbaik!!",  
                "pesan": "Kak wawa sehat sehat yaa, terimakasih sudah menjadi mentor kelompok pandas yang bertanggung jawab dan terbaik!! semoga kak wawa selalu dikelilingi hal-hal baik dan selalu dalam lindungan Tuhan, we love u kak wawa^,^ "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lbEahIpusvmTZmRbtRePA0XP1qwJUdIX",
            "https://drive.google.com/uc?export=view&id=1v5_9Lbus4gePBm3jDDaNnfjzA7MHzKht",
            "https://drive.google.com/uc?export=view&id=1kaXeJjmdaJ1DeYPYWoxEM4_XVLj4iIaN",
            "https://drive.google.com/uc?export=view&id=1Tt5LmemOdeh6HJwS_b1z-pYj5UgE2wF8",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kobam",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Pintar, keren, punya pemikiran yang kritis, baik dan ramah ",  
                "pesan": "Semangat bang kuliahnya semoga selalu diberikan kelancaran dan kemudahan dalam segala hal"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "Cantik, ramah, baik, kalem ",  
                "pesan": "Kakak sehat selalu yaa, jangan lupa makan yang teratur! "# 1
            },
                {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Pintarrrr, baik, ramah, cantikkkkk ",  
                "pesan": "Semangat kak jadi asisten tutornya, penjelasan dari kakak lebih mudah dipahami, suka banget diajarin sama kakak, sehat selalu ya kak! "# 1
            },
                {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Cantik, baik, ramah, keren ",  
                "pesan": "Bahagia selalu yaa kak! "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=d/1QH8vZ9UBOJJ0JD3t3a7VhBWM4mNenI6w", #1
            "https://drive.google.com/uc?export=view&id=1M_wVT9V0HyZ6VF2_yRs0tQjw7eIH6Mv1", #2
            "https://drive.google.com/uc?export=view&id=112-bRuNqqGpWdrCmil7WunIKAwyo4bS8", #3
            "https://drive.google.com/uc?export=view&id=1zyEkwSeCH-l4-4cd4Nz4_xSZ_ATibdBQ", #4
            "https://drive.google.com/uc?export=view&id=1oYKfKymL16vnTV3W_E6cH5yJae9TYUAc", #5
            "https://drive.google.com/uc?export=view&id=1-TAQwi6NJFR1tuokay_87-MMw13jaqlY", #6
            "https://drive.google.com/uc?export=view&id=1H5hmzincRplnoQxT8-y7HsBq8eLLViAZ", #7
            "https://drive.google.com/uc?export=view&id=1v17lGnsljaNH_TnHZcuu5tAhSuduKigv", #8
            "https://drive.google.com/uc?export=view&id=1yjOmBGu52WYuGs0sy0TN7zk4evHXN00F", #9
            "https://drive.google.com/uc?export=view&id=1cqG8oYhTLdEupQVD41kncRfVRFQxth0p", #10
            "https://drive.google.com/uc?export=view&id=1JYfmzaMdBHMHR5Y6x8ArsN6xjtgqrg5F", #11
            "https://drive.google.com/uc?export=view&id=1B9iS58wSNmUMgGNfXeW66VQuqbgES1z-", #12
            "https://drive.google.com/uc?export=view&id=1WkrcrSy8y-3PLOqnb76-RsO6stKnYQdS", #13
            "https://drive.google.com/uc?export=view&id=1ZlTa098SdohtjSHnwD-BrkGNuzGYxpel", #14
            "https://drive.google.com/uc?export=view&id=1OR0b_YcqEelTvz6R_CC5BtRQVo1M44Ak", #15
            "https://drive.google.com/uc?export=view&id=12iphGYUV6VREALIhtfwQ88fpQ7lTzRdH", #16
            "https://drive.google.com/uc?export=view&id=14y7HfPcXC5i9VYGWF_YDPhpvoGW2KtEV", #17
            "https://drive.google.com/uc?export=view&id=1iniwzG5h8v0gOuSALL73NBGBUgsVTKcc", #18
            "https://drive.google.com/uc?export=view&id=1ZPnHIdXUOhjnCUuvnLr61XP_PzgLi8D7", #19
            "https://drive.google.com/uc?export=view&id=1L_llTrl9kLhXtEOUUQcbvjE5bPD9hzDi", #20
            "https://drive.google.com/uc?export=view&id=1i_HtKO7yNfsdHPrZ0Hh1IKatgtXjQPVJ", #21
            "https://drive.google.com/uc?export=view&id=17WTyxJWbMmD7SCF3lo9Ix6KLkxlLzp2I", #22
            "https://drive.google.com/uc?export=view&id=1e5v5mVvOCkqS0I9u1wsXHMSnGJgLPbpy", #23
            "https://drive.google.com/uc?export=view&id=1MDGnfS8wut-PxcD7EY29QFqdSOgJhqOo", #24
            "https://drive.google.com/uc?export=view&id=1M_KMRpZSbs7FLnyL8nhvRIvRbtfNAfQq", #25
            "https://drive.google.com/uc?export=view&id=1ttD_lj6sH3paecVnwmyBJU6kxjDAVMmq", #26
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20 ",
                "asal":"Jawa Barat ",
                "alamat": "Korpri ",
                "hobbi": "Mikir ",
                "sosmed": "@afifahhnsrn",
                "kesan": "Galak tapi baik, cantik, keren, kece ",  
                "pesan":"Semangat kak jadi sekretarisnya!!"# 2
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": " ",  
                "pesan":" "# 3
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": " ",  
                "pesan":" "# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": " ",  
                "pesan":" "# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": " ",  
                "pesan":" "# 6
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": " ",  
                "pesan":" "# 7
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": " ",  
                "pesan":" "# 8
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": " ",  
                "pesan":" "# 9
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": " ",  
                "pesan":" "# 10
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": " ",  
                "pesan":" "# 11
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": " ",
                "pesan": " " # 12
            },
            
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": " ",
                "pesan": " " # 13
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
                "kesan": " ",
                "pesan": " " # 15
            },
            
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": " ",
                "pesan": " " # 16
            },
            
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": " ",
                "pesan": " " # 17
            },
            
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": " ",
                "pesan": " " # 18
            },
            
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": " ",
                "pesan": " " # 19
            },
            
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "Ramah, baik,humble ",
                "pesan": "Jaga kesehatan ya kak, kalau sakit jangan lupa minum obat " # 20
            },
            
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": " ",
                "pesan": " " # 21
            },
            
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": " ",
                "pesan": " " # 22
            },
            
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": " ",
                "pesan": " " # 23
            },
            
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": " ",
                "pesan": " " # 24
            },
            
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": " ",
                "pesan": " " # 25
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": " ",
                "pesan": " " # 26
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1d4HXJvaNAj-iv5TkEQVPozkwQ-Ig597c", #1
            "https://drive.google.com/uc?export=view&id=1rWTEJp6EmxoUkSRCyWzA_s9auQsKjuWt", #2
            "https://drive.google.com/uc?export=view&id=1mnTyh0SB7f5Ds7Z7QucPZng7J4jJwebh", #3
            "https://drive.google.com/uc?export=view&id=1QJOIUZS2ayeGp-rbjpjQBPv8bOHqD1wX", #4
            "https://drive.google.com/uc?export=view&id=", #5
            "https://drive.google.com/uc?export=view&id=115TaMUXAIsmY_r1-QzSno4ZUygcn3hI-", #6
            "https://drive.google.com/uc?export=view&id=1zfErFOdbl4kTkNUx46-sYIhnIbFfNnjK", #7
            "https://drive.google.com/uc?export=view&id=1K3xdU30jk7W6vfo6As7TygWbgPUghm75", #8
            "https://drive.google.com/uc?export=view&id=1FuyCKjZo6RetNu-Ne0LvvdoYNqP0XgE6", #9
            "https://drive.google.com/uc?export=view&id=1ZHyEihAw3ezgtCcMoHSxncS5y6ySezU_", #10
            "https://drive.google.com/uc?export=view&id=1Jhhh8dbGz69pK0LgP-Y4hCu5SFJ1DOS0", #11
            "https://drive.google.com/uc?export=view&id=1uspzS0iP1E6isOAGnJge5I7g-GCTjMNh", #12
            "https://drive.google.com/uc?export=view&id=1gqFEKMdLEsUOLrKaTog3cWll3pjNHwfL", #13
            "https://drive.google.com/uc?export=view&id=1mwF56JW_dSOG938UV3jnDbPWZytv3jMO", #14
            "https://drive.google.com/uc?export=view&id=1HhOzK4DB0djCPhHbaYx_vyas6esURFLR", #15
            "https://drive.google.com/uc?export=view&id=1T7ENlCQSLCjL1ftno3bmjG1qpRa1X7y2", #16
            "https://drive.google.com/uc?export=view&id=1sqJjDHTHq98ds99ROo0dhZth0tuWCQ16", #17
            "https://drive.google.com/uc?export=view&id=1gUwfSdlWLkMqh2YSYxcrKBYlMwdQu4ik", #18
            "https://drive.google.com/uc?export=view&id=1_080xXYl7V16ek1aNFbkiexOftzqXBvq", #19
            "https://drive.google.com/uc?export=view&id=1Zc9N7Po_r756wSJMh5xFbOx5AtRkTUlG", #20
            "https://drive.google.com/uc?export=view&id=1xVBhSyNNx75Dnxslc1Qm9oVmM6iFGozj", #21
            "https://drive.google.com/uc?export=view&id=1ZubyCttalCaK48J8gtgD17QT02qkO_pO", #22
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
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
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
                "nama": "Muhammad Regi Abdi Putra Ananta",
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
                "nama": "Aisyah Musfirah",
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
                "nama": "Fadil Prasetyo Alfarizzi",
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
                "nama": "Muhammad Aqil Ramadhan",
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
                "nama": "Muhammad Naufal Ramadhan",
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
                "nama": "Nadia Faraj Alyafaatin Simbolon",
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
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": " ",  
                "pesan":"   " # 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
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
                "nama": "Anggi Puspita Ningrum",
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
                "nama": "Efi Defiyati",
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
                "nama": "Fabiolla Charissa Putri",
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
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":""# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "",  
                "pesan":""# 15
            },
            {
                "nama": "Eggi Satria",
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
                "nama": "Afifah Fauziah",
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
                "nama": "Fabio Banyu Cyto",
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
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",  
                "pesan":""# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "",  
                "pesan":""# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "",  
                "pesan":""# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": " ",  
                "pesan":" "# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KWSDfD3fH1PEfQELWL9LrEIOMR0lniBT", #1
            "https://drive.google.com/uc?export=view&id=1QvG3TlTlOW_56Gn22fJ8fqW1gTa1ybTN", #2
            "https://drive.google.com/uc?export=view&id=1Mp5-3QimuS5RqXnT1O4mHfMKn_9uClXa", #3
            "https://drive.google.com/uc?export=view&id=1KTi7D2-S81o3uUTpR9Z-7XMOXC2qdix_", #4
            "https://drive.google.com/uc?export=view&id=1xbFbgweKffn-ux6A7R5YFYKwX4ufnkiM", #5
            "https://drive.google.com/uc?export=view&id=192oMQGcFuOVSa2FmNlRHqSP5-TBVcPNQ", #6
            "https://drive.google.com/uc?export=view&id=1oTRWjKteH5Z_TfDjb1bQyOEa-66eursK", #7
            "https://drive.google.com/uc?export=view&id=166xutKZjyAJH5o1-bJJTmMDW4kyhvJpZ", #8
            "https://drive.google.com/uc?export=view&id=1S5rjXxA9Hr1zQCc0z6RlBGFOKDnqbdyr", #9
            "https://drive.google.com/uc?export=view&id=1aC9CZbTV-1VDENIu-eCrFs4jJ0Fs3I8R", #10
            "https://drive.google.com/uc?export=view&id=1GGuQL5IQCprElclQTi9an5tj7aKuqrg1", #11
            "https://drive.google.com/uc?export=view&id=1uitCEEQJ2ibHij6C7Q9oNI3uD7slv3dO", #12
            "https://drive.google.com/uc?export=view&id=1M4Oxv0VhPSocbSFJIc1nH2ia4VfoikTd", #13
            "https://drive.google.com/uc?export=view&id=1StRXrF_-SjqxCGVnVXFi3wtMgYsDTTyb", #14
            "https://drive.google.com/uc?export=view&id=1TvyrYqjc96FuVlMp86OgnFyRTotY8-An", #15
            "https://drive.google.com/uc?export=view&id=1d_jSx_tPsJ-uWqWCeBKpIZrrvO7jOXzk", #16
            "https://drive.google.com/uc?export=view&id=1Ifw-YjRtdSjxiJzlVR5Nz2nsj6vfg0OB", #17
            "https://drive.google.com/uc?export=view&id=1HhIetpQtuH-RGLI3_EF0ZNlnth3iFDbk", #18
            "https://drive.google.com/uc?export=view&id=1Lk_FqlM-8G3TXQjObmB5ZOOtad3svuRQ", #19
            "https://drive.google.com/uc?export=view&id=1-K1XPe1vbOOh-ugrYwVTHEQbCshlzZqd&usp", #20
            "https://drive.google.com/uc?export=view&id=1M4Oxv0VhPSocbSFJIc1nH2ia4VfoikTd", #21
            "https://drive.google.com/uc?export=view&id=1bJyftJEpxH61p-7Me0-R1-3lZymNsp1G", #22
            "https://drive.google.com/uc?export=view&id=1F8RRrWcfcaegR6jy9tbj9_ASwMX_-lyF&usp", #23
            "https://drive.google.com/uc?export=view&id=1CbTDoqPQFH-W0w1b8_m1GOy1b5Yfmjm7", #24
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
            "https://drive.google.com/uc?export=view&id=1H8619V4M2oXssboyO1X0uFvkPXVuVxXn", #1
            "https://drive.google.com/uc?export=view&id=1afl50CwCqO5fT5QIY1p7idgk_4mD2YY_", #2
            "https://drive.google.com/uc?export=view&id=1WnNAMFzAxy0QTffh2nxCBCAMEfojLaNZ", #3
            "https://drive.google.com/uc?export=view&id=1nBd9eZr8M-hRFUFBDKnoeVflQqjHdjal", #4
            "https://drive.google.com/uc?export=view&id=1SR1bCy-iJloMPXb11M8XlgfIhaLPqE89", #5
            "https://drive.google.com/uc?export=view&id=1-wBuOzDzz1eMwerhcX0V3NbuFYi4nCds", #6
            "https://drive.google.com/uc?export=view&id=14OKwwwyUMol90WoCFqmGs46T8Vk9LPeB", #7
            "https://drive.google.com/uc?export=view&id=1HW4PjEfsm4LDJfHch-ppHaImYePpvxUm", #8
            "https://drive.google.com/uc?export=view&id=1xh5r-0isx8NECJgNm3ySmQB8R69wY4JC", #9
            "https://drive.google.com/uc?export=view&id=1PnYg9a0voPLP5Y-IbXXjF3WviXLQnYwg", #10
            "https://drive.google.com/uc?export=view&id=1YEQiP76IP8Js9bLP8H4bzJj-QAzb0f1F", #11
            "https://drive.google.com/uc?export=view&id=1nMIm1x3NSVbYBw7m-8cLDRaIqv1Df2oO", #12
            "https://drive.google.com/uc?export=view&id=1ML7LIgf8P_QHop-zBx4NoxcAeP_909bh", #13
            "https://drive.google.com/uc?export=view&id=1ghkZVhNxfPFyoHhpm2Vp78x2x9XlMiuA", #14
            "https://drive.google.com/uc?export=view&id=1SHK-JVnIgLvebcxImJfPrD73kmz_oH7a", #15
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
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Renta Siahaan",
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
                "nama": "Salwa Farhanatussaidah",
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
                "nama": "Azzahra Putri Kamilah",
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
                "nama": "Haikal Fransisko Simbolon",
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
                "nama": "Iqfina Haula Halika",
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
                "nama": "May Talitha Dahlia",
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
                "nama": "Muhammad Naufal Al Ghani",
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
                "nama": "Zailani Satria",
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
                "nama": "Rendi Alexander Hutagalung",
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
                "nama": "Hanna Gresia Sinaga",
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
                "nama": "Keren Marito Lumban Gaol",
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
                "nama": "Muhammad Hanif Dzaky Arifin",
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
                "nama": "Sarah Wasti",
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
                "nama": "Zahra Putri Salsabila",
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

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15JgBCKrG6Uup4GaRdomRPosKoAv49Zdz",
            "https://drive.google.com/uc?export=view&id=1Oa7wPqbgz7F9BOQ7XYe5tLXYmg97fzKQ",
            "https://drive.google.com/uc?export=view&id=1Us4CmTu-7sf3YUo5NB2bfAkA4ommHlB8",
            "https://drive.google.com/uc?export=view&id=1negaGw7a8Yphvc2yQI1jOwx95gq_JgTd",
            "https://drive.google.com/uc?export=view&id=1571U3VJamdpW3I3Puv9I2p2CLU6YXNPH",
            "https://drive.google.com/uc?export=view&id=1RNmZXYJs5oCnVW5wd7YndIsAR5Lt5KEI",
            "https://drive.google.com/uc?export=view&id=yuT5hdIgA1WaQZNTz6MhWrSCchPIP7o-",
            "https://drive.google.com/uc?export=view&id=153m9qtomhFmBnXTR0emr2s27p-uAhpHU",
            "https://drive.google.com/uc?export=view&id=10srcQHkdmGCJSFG9D-DQLpGW9a7tuaeq",
            "https://drive.google.com/uc?export=view&id=1XcWeBLEQ6aVFt8OcVjc6qudps9GZlkl3",
            "https://drive.google.com/uc?export=view&id=1T-epWpxcH4JZY3OiFKhCOpF09oNz880r",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "  ",  
                "pesan": "  "# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "  ",  
                "pesan": "  "# 2
            },
                {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "  ",  
                "pesan": "  "# 3
            },
                {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "  ",  
                "pesan": " "# 4
                        },
                {
                "nama": "Aprilia Dewi Hutapea",
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
                "nama": "Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "  ",  
                "pesan":"    "# 6
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "  ",  
                "pesan": " "# 7
            },
                {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "  ",  
                "pesan": "  "# 8
            },
                {
                "nama": "Enggli Rahmadhani",
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
                "nama": "Hanifah Inaya Sani",
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
                "nama": "Nydia Manda Putri",
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

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zk_RbW1NZbgzwHBnfs2zPCV-d9tBctfE",
            "https://drive.google.com/uc?export=view&id=1bL7oA-cFhLnwlXbAe9mUUX1xaG2NuyrL",
            "https://drive.google.com/uc?export=view&id=19WG8zkYwzttFX7ICpwwJ8ZGT_7_pLUnl",
            "https://drive.google.com/uc?export=view&id=1hZ2323GbL03ZTvDUvZRHnV5Jkmm9HVSD",
            "https://drive.google.com/uc?export=view&id=1bbFOx04LRnkEDy-2aiwdxPzn_SNP-Q0E",
            "https://drive.google.com/uc?export=view&id=1gcyuEhMc0XCQ8ozrjMUmCxnDGCW1JAQt",
            "https://drive.google.com/uc?export=view&id=17VuJ6jbReD8QkRSZrayOKn6J7bGIko7Z",
            "https://drive.google.com/uc?export=view&id=1pRZ3AAC6mQCNXxQBD3X_8nqnIiczPtfK",
            "https://drive.google.com/uc?export=view&id=1NHBklhJVWj2zkihQiyce5Yedbgmaq2AT",
            "https://drive.google.com/uc?export=view&id=1ssMJpVWJwpOZa4XOn_INsa2XG6wV4PlT",
            "https://drive.google.com/uc?export=view&id=1PcCFq3w8Cm5pkUBc5b-lRejgeoIdbIq7",
            "https://drive.google.com/uc?export=view&id=16wAlxhCluFJKLznAiGoCL5ovfUFTPO2g",
            "https://drive.google.com/uc?export=view&id=1GmusQlgVqqbnnhXgikcNFe9Jq6BSPMXW",
            "https://drive.google.com/uc?export=view&id=1k8yX_PQU2UHljPTTKOC00UHwVgxB3A_Y",
            "https://drive.google.com/uc?export=view&id=1CEpmcQRbWMt06CO0qKXzY8ASq6Qr2_aI",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1ArBWL786glsmIDhFK0wkk1c839oZKYsp",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
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
                "kesan": "",  
                "pesan": ""# 1
            },
            {
                "nama": "Rahma Neliyana",
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
                "nama": "Khoirul Anam",
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
                "nama": "Labo John Noel Napitupulu",
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
                "nama": "Ravi Diva Efangga",
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
                "nama": "Refa Destiny Pranata",
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
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
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
                "kesan": "",  
                "pesan": ""# 1
            },
                {
                "nama": "Donna Maya Puspita",
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
                "nama": "Hafsa Fazila Arradhi",
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
                "nama": "Nayla Salsabila Fathianisa",
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
                "nama": "Sania Dwi Ayu Lestari",
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
                "nama": "Akmal Faiz Abdillah",
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
                "nama": "Raihana Addelia Putri",
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
                "nama": "Citra Agustin",
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
                "nama": "Eigi Artamevia",
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
                "nama": "Romauli Oktavia Silaban",
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




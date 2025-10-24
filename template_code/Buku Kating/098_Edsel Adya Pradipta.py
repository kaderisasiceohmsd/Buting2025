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
            "https://drive.google.com/uc?export=view&id=1yS7lQsll_0ENDuY-AsM6kOMPx_MCcHac",
            "https://drive.google.com/uc?export=view&id=1boC8m4yb92UyPI2duv-C9PYbwfnDJz_-",
            "https://drive.google.com/uc?export=view&id=17WiPAOnWWma3UKKWp-40NVO9KFdX-8bG",
            "https://drive.google.com/uc?export=view&id=148r58Nsl8DU34mKedxcK4PuZSPxbLOQz",
            "https://drive.google.com/uc?export=view&id=1fd8IvGMfIFbzwrSSKx3p9Bpzf8kdWETo",
            "https://drive.google.com/uc?export=view&id=1k6R7cCCge8i9fn4His-kF8wdx9N1WFbG",
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
                "kesan": "Kakak ini tegas sekaligus asik",  
                "pesan": "Semangat terus bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini lucu dan asik",  
                "pesan": "Sukses selalu bang"# 1
            },
              {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini senyum nya lucu",  
                "pesan": "Semangat terus kak!"# 1
            },
              {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini lucu!",  
                "pesan": "Sehat selalu kak!"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini lucu dan seru!",  
                "pesan":"Sukses terus kak!"# 1
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini seru dan asik",  
                "pesan": "Semangat terus kak!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1whidEGR-QVLSsdMVpSd5DBmNk_JeAoCx",
            "https://drive.google.com/uc?export=view&id=1lbjPlqnJU9m9Mvusvhy2MFndqipQ_Gjq",
            "https://drive.google.com/uc?export=view&id=1oC7amaKjPEPx0oVKOawQwyb-_s2lzqk-",
            "https://drive.google.com/uc?export=view&id=1YeXHITaHo0bd5XXGJKlVSahSgPMlYsmB",
            "https://drive.google.com/uc?export=view&id=1p47Wt5qO-gcadiH3W2XoLu1fxrhxKoZf",
            "https://drive.google.com/uc?export=view&id=10xOOM10saou1g8rErnfbpWRVwiOnplH3",
            "https://drive.google.com/uc?export=view&id=1up8xqAqurKHBUC-nCg5INorifN2DOSNh",
            "https://drive.google.com/uc?export=view&id=1qPFvluxdqHsz7yB97UGUFYHXdNrkcQM7",
            "https://drive.google.com/uc?export=view&id=1MMgJbj3kbAOMUIpeCgBDxucq1JB7CO_t",
            "https://drive.google.com/uc?export=view&id=1zpUZZHDbJw8PCqb2CqaW4G16Ak_vsAmq",
            "https://drive.google.com/uc?export=view&id=10ByyUdlmRKwIDquSqHkeRYAZ1ZsLnlup",
            "https://drive.google.com/uc?export=view&id=1a0UrOErpHyfgbd-nC2o2FH-WalCTg0-B",
            "https://drive.google.com/uc?export=view&id=1rtoyomRXK3Sw6J2zxI1gA0NCbdyJrMAb",
            "https://drive.google.com/uc?export=view&id=1YXyvvhqMXcHbEL-y0sqDBAVGhksSNXnG",
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
                "kesan": "Kakak ini lucu dan juga tegas!",  
                "pesan": "Sukses terus bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "Kakak ini asik",  
                "pesan": "Sehat selalu kak!"# 1
            },
              {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakak ini baik dan asik",  
                "pesan": "Semangat terus kak!"# 1
            },
              {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini lucu",  
                "pesan": "Sukses terus kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Kakak ini keren dan pinter",  
                "pesan":"Semangat terus bang"# 1
            },
             {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini lucu, suka style nya",  
                "pesan": "Sehat selalu kak"# 1
            },
              {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Kakak ini keren!",  
                "pesan": "Semangat terus bang"# 1
            },
              {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik!",  
                "pesan": "Sukses terus bang"# 1
            },
              {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini lucu",  
                "pesan": "Sehat selalu kak"# 1
            },
              {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan": "Sukses terus kak"# 1
            },
              {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "Kakak ini keren",  
                "pesan": "Semangat terus bang"# 1
            },
              {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini seru",  
                "pesan": "Semoga dilancarkan segala urusannya kak"# 1
            },
              {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan": "semangat terus kak"# 1
            },
              {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "Kakak ini baik dan seru",  
                "pesan": "Sukses selalu kak"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14NpemPscFkr4Zs-aPeuhhGGrZsHl4ag_",
            "https://drive.google.com/uc?export=view&id=19050QnKgxnnZPwWRv5q-sKFd7YYLOC17",
            "https://drive.google.com/uc?export=view&id=1i1pP89bdPzHMKB3kpgLdBnETOGN6rviw",
            "https://drive.google.com/uc?export=view&id=1Ka_LNlHlpZxpDoZlS1XP-_ZV7JWgkiL2",
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
                "kesan": "Kakak ini keren banget",  
                "pesan": "Sukses terus bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini jago bahasa inggris",  
                "pesan": "Sehat selalu kak"# 1
            },
              {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini baik dan lucu",  
                "pesan": "Sukses terus kak"# 1
            },
              {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini lucu",  
                "pesan": "Semangat terus kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XN1lbskMDNVUBX2xd4bK-VGiE-If6qEZ", #1
            "https://drive.google.com/uc?export=view&id=1tqMNJ2FMWdXYCBcrVo29K8yTeXLjoFl-", #2
            "https://drive.google.com/uc?export=view&id=1q8FtJ2_ulVPq5B67Km47Wgiaj5ZCjXbx", #3
            "https://drive.google.com/uc?export=view&id=1rDwyX58nUFXk1Kw1XXJQdhmthHcDRLd0", #4
            "https://drive.google.com/uc?export=view&id=1gUq-t4TZuA5xAemInRhqotwY7jG0U0U7", #5
            "https://drive.google.com/uc?export=view&id=1MTYxFDb278WtpM0c7YlFHnx_aACUd3OB", #6
            "https://drive.google.com/uc?export=view&id=1sqbpNNTfSWYjTaRHdw6K4rTJgJrcrFkX", #7
            "https://drive.google.com/uc?export=view&id=1rhk3d6uaoLKSbuYG5w3NAWLI297Nquo9", #8
            "https://drive.google.com/uc?export=view&id=1yed_9MQRwoVC4VU9zkSxWTPI-HsKXcDK", #9
            "https://drive.google.com/uc?export=view&id=1WkkKRR7u5k4Y4VRAiBrmvB3FArWbqiyw", #10
            "https://drive.google.com/uc?export=view&id=16VZ-YHRMGLeHlcQ53iqrJksSsIO1HGoB", #11
            "https://drive.google.com/uc?export=view&id=1pUEHJi1nkWfCZWn3xJGK17n0xVuzcu5i", #12
            "https://drive.google.com/uc?export=view&id=1YjnguXLrUj7LepENOWV90jxrL7bgYGu3", #13
            "https://drive.google.com/uc?export=view&id=1DgnoBCURINfvLYL3hTWzPhjr2EJcLMP7", #14
            "https://drive.google.com/uc?export=view&id=1R302ygndieim8z9-b3p8OdVcSxbPB7as", #15
            "https://drive.google.com/uc?export=view&id=1lKYRZA8Ck7xkqidhrYozNhBOf569Kldq", #16
            "https://drive.google.com/uc?export=view&id=1bfKTl-IlbNZIqxnpwRW22AdQRtH4WGvx", #17
            "https://drive.google.com/uc?export=view&id=1B_jmHH9xOEmN-lOOu6FoX3kbF_cpRy9x", #18
            "https://drive.google.com/uc?export=view&id=1uBEBX0w4Abo5B_a17D20Wq87iwEHk2K5", #19
            "https://drive.google.com/uc?export=view&id=1Iy7lWiC0_x0O8ZZZ_lP68rJTmeYQ4EIJ", #20
            "https://drive.google.com/uc?export=view&id=13Qfs2Uo9GXX-7NxydaRgF-STmBjKO8QT", #21
            "https://drive.google.com/uc?export=view&id=1JmXhZyXz753EGJiACwrIz6ofsBN3z9k4", #22
            "https://drive.google.com/uc?export=view&id=1eNk5JocDHOXdXbm_ajWPW0uD32haL9O4", #23
            "https://drive.google.com/uc?export=view&id=1UYVb5tDJr60dESz4jWWDFdhWQ1t8WCLJ", #24
            "https://drive.google.com/uc?export=view&id=1_PuGl-NWvNsWUVmSjtSvlp5xzRZBn1EF", #25
            "https://drive.google.com/uc?export=view&id=1DhjlSWx1mO98Xuyr818be_0AqxuZRsgx", #26
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
                "kesan": "Abangnya keren, asik",  
                "pesan":"Sukses terus bang"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Jalan-jalan",
                "sosmed": "@i",
                "kesan": "Kakaknya lucu",  
                "pesan":"Semangat terus kak"# 2
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "Kakaknya profesional, tegas",  
                "pesan":"Semangat terus ya kak"# 3
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky_",
                "kesan": "Abang ini keren banget!",  
                "pesan":"Sukses terus bang!!"# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakak ini lucu",  
                "pesan":"Semangat terus kak"# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang ini keren, tegas, profesional banget",  
                "pesan":"Semangat terus bang!"# 6
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Abang ini keren, Tegas",  
                "pesan":"Semoga sukses selalu bang"# 7
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
                "kesan": " ",
                "pesan": " " # 20
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
            "https://drive.google.com/uc?export=view&id=1EmEQBOfMwlv6h7MTA-vnuDXULkF1iYAG", #1
            "https://drive.google.com/uc?export=view&id=1-4PYAtGMiHagZ7huSd8OIreHKQFAQ6M4", #2
            "https://drive.google.com/uc?export=view&id=1l0DsounTZVmxpzSf0PHtOXCJIRy8XwLz", #3
            "https://drive.google.com/uc?export=view&id=1o15qz2DQEjOYtqDTYfLs6zTGBvLzFkVz", #4
            "https://drive.google.com/uc?export=view&id=1vz9dUtMs8-69dEw1qWeohrrssz68A_UT", #5
            "https://drive.google.com/uc?export=view&id=1hev_4OCeN1OUu2AQFo_jzZaJ_ceShjny", #6
            "https://drive.google.com/uc?export=view&id=1nIHd3-OkGOdpyx4c3cSBa6kB9LppNDJc", #7
            "https://drive.google.com/uc?export=view&id=1muSKRP1XZv_vjMgkIUtDvki0gqpi4TEt", #8
            "https://drive.google.com/uc?export=view&id=1bZmnFpbY7vc9w0lopEir8NKj4fQMcws-", #9
            "https://drive.google.com/uc?export=view&id=1V2FuvHFDzJtm4cbocR9HR_bsSSS6XK42", #10
            "https://drive.google.com/uc?export=view&id=1ToZPY_nVntUEy3JXxQzI7EvrWc5aPTTK", #11
            "https://drive.google.com/uc?export=view&id=1NJFxEatsPN8sjDWDIb2_mmO4d5lbVXdh", #12
            "https://drive.google.com/uc?export=view&id=1o0RHXUm0BtKPE0g2nQAhrQUswMAntclG", #13
            "https://drive.google.com/uc?export=view&id=14ncieBvvIWMiTn_hqErwe-h5vCyIm10u", #14
            "https://drive.google.com/uc?export=view&id=1UNzq1tLuHa7PLrUR-Sfl-FWUcOxJMtrS", #15
            "https://drive.google.com/uc?export=view&id=1Pbid62m3uhGLpjlRmZKbL7Ge7CKtYb49", #16
            "https://drive.google.com/uc?export=view&id=1dN8HQAruIm8njDH17PnMvohnby7T_AsD", #17
            "https://drive.google.com/uc?export=view&id=1amaka-7yW9SVTGqd2xqn_IG3sGN7zU2f", #18
            "https://drive.google.com/uc?export=view&id=1Bt3QR1VBDj6y65q87gR-luTvgvFpjLki", #19
            "https://drive.google.com/uc?export=view&id=1bady_d6jvhBOJnPCRaNjOP5nuJUa0sw3", #20
            "https://drive.google.com/uc?export=view&id=1UTlNXMemmuWcfJVAsnf1kKAR2x4Y6TYM", #21
            "https://drive.google.com/uc?export=view&id=1QrrWqOuEeeTJH2bACKCAH3ep-wKWGA1l", #22
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak A",
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
                "nama": "Kakak B",
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
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak A",
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
                "nama": "Kakak B",
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
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1v5aSshnpQ52x2M9eiYbAiIHfXlAsi5xB", #1
            "https://drive.google.com/uc?export=view&id=14oVZ7BokIji1Nu78Y-vN3iJ7hwrpLlu_", #2
            "https://drive.google.com/uc?export=view&id=1wP2VPcZigocu-JBEBhZo6eVkP8tpA8GI", #3
            "https://drive.google.com/uc?export=view&id=1r6LICCp1HqR37NuHKcRLiPP2Uoo0oxdR", #4
            "https://drive.google.com/uc?export=view&id=1YOzgSl5Kglc3PbAHZVeK9dXsQp1WN_dP", #5
            "https://drive.google.com/uc?export=view&id=18dQnTi_1iaINAs3VjZzPO-txynWyGWQY", #6
            "https://drive.google.com/uc?export=view&id=1MmO9MhK5Vg04z0emBqmfP8dlCg0s6Bar", #7
            "https://drive.google.com/uc?export=view&id=1nsNXzhg1MsKf8DHuOLvtemp2LCyN5WTQ", #8
            "https://drive.google.com/uc?export=view&id=12CDrjNQ18SYIurDh8by2V4vUh8XOXkdY", #9
            "https://drive.google.com/uc?export=view&id=107m0rzE6blHXyTAA8ap9XtZHy0ZDR3SK", #10
            "https://drive.google.com/uc?export=view&id=1R87R9I8MCxlX3XkQvSdNW0BEsVJBDOyy", #11
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

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_pqVv7G7qorc_1zB_F7LDA3biIlUwdu0",#1
            "https://drive.google.com/uc?export=view&id=1fLb7v9V11voVZ7Q5zLiWXqsLjaZ7Xkv0",#2
            "https://drive.google.com/uc?export=view&id=1YAJPlS5hBLF4MFaOGy-Hl_V2ucXJUvlK",#3
            "https://drive.google.com/uc?export=view&id=1i2KVOp19_l3dPBToAFLB3u60esKb7aVG",#4
            "https://drive.google.com/uc?export=view&id=1ELMhuqcuPXEOihlmESdG4EPnBfSuVs8Z",#5
            "https://drive.google.com/uc?export=view&id=1U46YaoZnvE8eb8gvGeK1456jHCnpTNB9",#6
            "https://drive.google.com/uc?export=view&id=1Ud1ACAyfyqG6cpBcQ4enHataeWoz8Fzv",#7
            "https://drive.google.com/uc?export=view&id=1mJLJ6DESV1apY7941l3AAwE7DhIeoAHz",#8
            "https://drive.google.com/uc?export=view&id=13v15omMVyak5stG12IbnYAXhWr0C_RXd",#9
            "https://drive.google.com/uc?export=view&id=14KmeodSsLpuRtpkWeyKjj872PDgYOTeM",#10
            "https://drive.google.com/uc?export=view&id=1nzVtqM6TJ9VOy_tI1yM7Ol5qHFoFN_0u",#11
            "https://drive.google.com/uc?export=view&id=1R55jI44MoadJpmDUxkUV-RzDuCaLkLNB",#12
            "https://drive.google.com/uc?export=view&id=1rw73f2fOVJf05e0rhltYa3sgYPiJXaUW",#13
            "https://drive.google.com/uc?export=view&id=1JdFdpUogRu1vR-BU_BSVZgS8Kk0wSiwV",#14
            "https://drive.google.com/uc?export=view&id=104K265YFy7XEj5KHY60xcUT2UpTcZg5I",#15
            "https://drive.google.com/uc?export=view&id=1g5oS1xjX4X88PLMQOEp0ZiXEGgNNNxcr",#16
            "https://drive.google.com/uc?export=view&id=1izPEw7b9aj9Allzxmk98Z2bRFkF-oJaO",#17
            "https://drive.google.com/uc?export=view&id=1Wqrc_8pE2cMu3mZ9Lq7BCyg0nmrS5UVl",#18
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
                "kesan": "Kakak ini lucu, asik, tapi tetep profesional",  
                "pesan": "Semangat terus kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini asik, seru",  
                "pesan": "Jaga kesehatan selalu kak!"# 2
            },
              {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Abang ini keren, asik",  
                "pesan": "Sukses selalu bang!"# 3
              },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Abang ini kadang lucu kadang garing (?)",  
                "pesan": "Jangan menyerah bang!"# 4
            },
              {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Abang ini baik, seru",  
                "pesan": "semangat terus bang"# 5
            },
              {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "Kakak ini lucu, baik",  
                "pesan": "Sukses selalu kak"# 6
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "124450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitia",
                "kesan": "Kakak ini keren banget, hobinya belajar, pasti pinter",  
                "pesan": "Semangat terus belajarnya kak!"# 7
            },
              {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kakak ini baik, kalem",  
                "pesan": "Semangat kak, jangan nyerah!"# 8
            },
              {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini ramah banget",  
                "pesan": "Jaga kesehatan ya kak"# 9
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini lucu, agak pendiem ya?",  
                "pesan": "Semangat kuliahnya kak!"# 10
            },
              {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak ini lucu, ramah",  
                "pesan": "Semoga sukses selalu kak"# 11
            },
              {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "Kakak ini keren, asik juga",  
                "pesan": "Semangat terus kak!"# 12
            },
              {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini lucu, asik, seru",  
                "pesan": ""# 13
            },
              {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abang ini keren, banyak masukkan yang aku dapat dari abang ini",  
                "pesan": "Terimakasih bang, semangat terus, jangan bosen sama dunia desain!"# 14
            },
              {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini seru, desainnya bagus-bagus",  
                "pesan": "Semoga sehat selalu kak!"# 15
            },
              {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakak ini asik, rumahnya di Natar juga sama kayak aku, tapi dia lebih jauh",  
                "pesan": "Semangat terus kak,  aku tahu kok PP Itera - Natar itu butuh energi lebih"# 16
            },
              {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "Kakak ini baik, Desainnya jago bagus bagus juga desainnya",  
                "pesan": "Sukses selalu kak!"# 17
            },
              {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini lucu, seru, asik di ajak ngobrol, gak bakal bosen kalo ada kakak ini",  
                "pesan": "Semangat terus kuliahnya kak!"# 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


# Tambahkan menu lainnya sesuai kebutuhan



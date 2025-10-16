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
            "https://drive.google.com/uc?export=view&id=14HGAyw0Kh44vLVH3b_uRypM6bpGzXV4L",
            "https://drive.google.com/uc?export=view&id=1_RHN-ZtRL6hB5YMPHcqAMHqboHO2aO6M",
            "https://drive.google.com/uc?export=view&id=14u7N_mKR8li-hPvzH9rIELEqveFq1ki6",
            "https://drive.google.com/uc?export=view&id=1jveA2Aj04qXbqyFF6DqlmQ9EADCseAQn",
            "https://drive.google.com/uc?export=view&id=1EOgxCCGUQe1CRcLbnUZqVju0uwFwsXfX",
            "https://drive.google.com/uc?export=view&id=12bKFwlul9tBO7MhaOtZTC0eRGQTYPGKO",
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
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": " ",  
                "pesan":" "# 1
            },
             {
                "nama": "Kakak Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": " ",  
                "pesan": " "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SIZQWnW86RBFzAhlxZJDAFByUa_bLUAq",
            "https://drive.google.com/uc?export=view&id=1m3IZtgHB-S3CpWySSPv0VFWCQuAv9-cH",
            "https://drive.google.com/uc?export=view&id=1h1gZJbMJYe7RtIoYp0v2iZwaBzi1jhXT",
            "https://drive.google.com/uc?export=view&id=15gThKRX2Un1l0fvYByYvdEkghyCPKFkv",
            "https://drive.google.com/uc?export=view&id=13lZjoEC6SkZgDxWRhoznPBuGfjIdAvNM",
            "https://drive.google.com/uc?export=view&id=1NVLqSXpEkbSXYmzElvutJtkY3Menqf1Y",
            "https://drive.google.com/uc?export=view&id=1iW5WMrSU7x5Elx5SsNLCXnL4sqFFfnMB",
            "https://drive.google.com/uc?export=view&id=1hEya_NrIEo6l_5GcjcKhBu09BVBZ0K5c",
            "https://drive.google.com/uc?export=view&id=1XjEP9NNmwtUVfVmhJyWrIKWyagqq9KUi",
            "https://drive.google.com/uc?export=view&id=1zU5dayTnrumr3XY2pbfKQCSXCSMB4FFU",
            "https://drive.google.com/uc?export=view&id=1xMakceiyWW5P17-WPQF7wbSRSCImxm8u",
            "https://drive.google.com/uc?export=view&id=1jFjgSBCkgVNDvQQFLSvynmaFc5Do9TP4",
            "https://drive.google.com/uc?export=view&id=1RGrgaxHlaSgZTKNZ-YwU0ZMWguT0ibOb",
            "https://drive.google.com/uc?export=view&id=1Px-ZVwVlZuXCYqQJ-vRqgJajCymISTAc",
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
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": " ",  
                "pesan":"  "# 1
            },
             {
                "nama": "Kakak Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": " ",  
                "pesan": " "# 1
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
            "https://drive.google.com/uc?export=view&id=1eFa-Jbmkvt0LC1BKs44SgJsD9GKP7RPM",
            "https://drive.google.com/uc?export=view&id=1B9EJfCS0m-w6GvJUUvPBD3jC1V0twn8d",
            "https://drive.google.com/uc?export=view&id=1F5KATtVQvtvXlkISpgsNEsLe-AFAs0as",
            "https://drive.google.com/uc?export=view&id=10PzSHPtiHTKMVtCVZDiv2meMZfQrM2ET",
        ]
        data_list = [
            {
                "nama": "Kakak Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kobam",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": " ",  
                "pesan": " "# 1
            },
            {
                "nama": "Kakak Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": " ",  
                "pesan": " "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nbPQsbKmoCVgyXtjlfUd4uGHQdMq5-Qo", #1
            "https://drive.google.com/uc?export=view&id=1cgpxcNxXUtjDViwpKrXigz4eNxrs85_X", #2
            "https://drive.google.com/uc?export=view&id=1ormaBl5jtFD0kLIXDD2fOyXxKK6hIbPC", #3
            "https://drive.google.com/uc?export=view&id=1Y0SEf-AL8xZvhWnziMDFHUzhX4iWm53N", #4
            "https://drive.google.com/uc?export=view&id=1432_MkX0X5Jaza3Osy8IFNRfqWjYdTCf", #5
            "https://drive.google.com/uc?export=view&id=11JSfLS1fn0la8yJF9sb8Jh0j1lkNY4ks", #6
            "https://drive.google.com/uc?export=view&id=1dYtl3AU6cY34E_0qA65qed8Eo5SDA1mG", #7
            "https://drive.google.com/uc?export=view&id=16X-4PWgh7fJOvAAXwXUm0JbxbDhfpUyK", #8
            "https://drive.google.com/uc?export=view&id=18A_tuf9rokWfsx5QELP4kISjraqYrIls", #9
            "https://drive.google.com/uc?export=view&id=1ONSeWLHFVUXXLVlFWEZ9ge_06epwyRnc", #10
            "https://drive.google.com/uc?export=view&id=101MqkqKkoU6ao_guwYhp2TEA-FPDAtk8", #11
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #12
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #13
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #14
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #16
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #17
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #18
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #19
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #20
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #21
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #22
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #23
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #24
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #25
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #26
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
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Kakak Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": " ",  
                "pesan":" "# 2
            },
            {
                "nama": "Kakak Allya Nurul Islami Pasha",
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
                "nama": "Kakak Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": " ",
                "sosmed": "@ahmad.rizky___",
                "kesan": " ",  
                "pesan":" "# 4
            },
            {
                "nama": "Kakak Arienta Khusnul Ananda",
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
                "nama": "Kakak Daffa Hadyan Navista",
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
                "nama": "Kakak Ginda Fajar Riadi Marpaung",
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
                "nama": "Kakak Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":" ",
                "alamat": " ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": " ",  
                "pesan":" "# 8
            },
            {
                "nama": "Kakak Nobel Nizam Fathirizki",
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
                "nama": "Kakak Nurul Alfajar Gumel",
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
                "nama": "Kakak Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": " ",  
                "pesan":" "# 11
            },
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
                "nama": "Kakak Arafi Putra Maulan",
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
            "https://drive.google.com/uc?export=view&id=1g1BRbT-_6_EcDjPSbES3E_VOoC0WzC5X", #1
            "https://drive.google.com/uc?export=view&id=1kuLRMKtIc0-da3p-PC8IHV7BMCpWrpS8", #2
            "https://drive.google.com/uc?export=view&id=1qHWIIsLCO3_svFvR05r6f6mrnl1h-IOM", #3
            "https://drive.google.com/uc?export=view&id=1n7PPuYOajJp9VVc52VDwEFM3O-dD4Xxo", #4
            "https://drive.google.com/uc?export=view&id=1whS_zP80UiJ-i0W6Hy1FEHmAf31-cHxw", #5
            "https://drive.google.com/uc?export=view&id=1If-VO0k0k9x6lfDfdsXVZJVmlEnZnKVk", #6
            "https://drive.google.com/uc?export=view&id=1UOpGcZx7xZ5u-WXhEqeArzUg3hyk3x97", #7
            "https://drive.google.com/uc?export=view&id=1GDQgLVZF2EPkZ91u5yf7VpotEdv0TUgW", #8
            "https://drive.google.com/uc?export=view&id=17vXuGpIX32NGdVXrG4Ky-mQankigRwjn", #9
            "https://drive.google.com/uc?export=view&id=1VaMzkxbPaZvbX5HO2AhNCfN1ZNyIznAb", #10
            "https://drive.google.com/uc?export=view&id=13MiYdXwUOfUmFCrRTnPP3vAPnEwNrRT6", #11
            "https://drive.google.com/uc?export=view&id=1tOAfXQEgM57w5yqmZs3A-Z5y9L8I5Dov", #12
            "https://drive.google.com/uc?export=view&id=1oxi1PUUe1HcXJYOe52vSfdX_6sJrxc8m", #13
            "https://drive.google.com/uc?export=view&id=1KmTz62O8y0YJCnJYLMqHTArzMWZMC68k", #14
            "https://drive.google.com/uc?export=view&id=1qHWIIsLCO3_svFvR05r6f6mrnl1h-IOM", #15
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
            "https://drive.google.com/uc?export=view&id=1bD47SFe_i1YUF5uYDV6YXNUVWofw-DD3",
            "https://drive.google.com/uc?export=view&id=1BuQb-31Mcy62fRWpWBKigiFdVkMcV4Nu",
            "https://drive.google.com/uc?export=view&id=1nZZXgoGGmERY8Wl_UaXmpzRuA76r861i",
            "https://drive.google.com/uc?export=view&id=1-4IYo_st4YBMX7mDaAUTgzuZ-FyKX59E",
            "https://drive.google.com/uc?export=view&id=1wzIj5owESXeQm9K4NT8POs0Mc0QvRdRQ",
            "https://drive.google.com/uc?export=view&id=18X0zMGj1Lg8fvI2-8Oi9aEH3b1BE0F6w",
            "https://drive.google.com/uc?export=view&id=1Arfq31V3PKzqNFCcpFFDVbJ68Qa2mthb",
            "https://drive.google.com/uc?export=view&id=1pLVcbebIthwDbP2xai964Dz7bJQxb4gk",
            "https://drive.google.com/uc?export=view&id=1GZ-ZzVL2yWrEZWw4G10M1TR8aGnaBuA2",
            "https://drive.google.com/uc?export=view&id=1pYEos4hyBsYAOA-SXDzTYupCVcgjycyw",
            "https://drive.google.com/uc?export=view&id=1ZyO5SB8WTTivJknwY0PpxuJJbmFnMUBu",
            "https://drive.google.com/uc?export=view&id=1x4x462BL4Ad8P4K9YXBmhPH7pbYdvTJR",
            "https://drive.google.com/uc?export=view&id=1cvhjdIrVheNMvl4-tZSDg3VfRzZ92Ga9",
            "https://drive.google.com/uc?export=view&id=114zIoIYOvJymlPg7EfgAYd1TgPjlYWEW",
            "https://drive.google.com/uc?export=view&id=1BVF5_NvfqUUQ1TnyvGnkmV-SlbG8e8nK",
            "https://drive.google.com/uc?export=view&id=1lagNrwBM3n5DCHYAmh1mImd72SOVgDyj",
            "https://drive.google.com/uc?export=view&id=1MHDOmpo14wXFQjUQLYqjYlmKg38aqFl0",
            "https://drive.google.com/uc?export=view&id=1-1_wW4DgnXFHMBsxycLzRuB7U32JZT1w",
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

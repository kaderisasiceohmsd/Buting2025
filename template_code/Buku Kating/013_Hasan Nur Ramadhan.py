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
            "https://drive.google.com/uc?export=view&id=1GKTwT8EvCQ7I5oXlatNOilOg8lPmh081",
            "https://drive.google.com/uc?export=view&id=1mvTntsUWPu9qK_At0ALeLX1HCZUiwxB0",
            "https://drive.google.com/uc?export=view&id=1UuKIKl6ZPDhSrm0AD3vKREMDdudiZ4Cz",
            "https://drive.google.com/uc?export=view&id=1GLfY4IpBWjBj2f7lZgU9wU4oXvDT4XUs",
            "https://drive.google.com/uc?export=view&id=1OWNVjEW0lpGJI9cGsAv6DJgiwhwaUDpu",
            "https://drive.google.com/uc?export=view&id=1BbXlSzGCSMaDYfpH7BSJwaPQcVvv1IQ2",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "abang ini sangat ramah dan asik",  
                "pesan":"semoga sukses selalu abang dalam menjalani kuliahnya !"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "JL. Lapas",
                "hobbi": "Baca buku sql",
                "sosmed": "@johanneskrisjnn",
                "kesan": "orangnya asik dan seru banget, displin, dan juga tegas",  
                "pesan":"semoga abang bisa menggapai mimpi abang"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabeth_",
                "kesan": "suka dengan kakak ini karena dia baik dan bersemangat ",  
                "pesan":"semoga kakak dapat mencapai prestasi yang besar baik dalam akademik maupun non akademik"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@puspadrr",
                "kesan": "kalem, cool, dan berwibawa",  
                "pesan":"semoga kakak sukses terus kak!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "18",
                "asal":"Wakatobi, Sulawesi Utara",
                "alamat": "Mutun, Paseweran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "orangnya anggun dan berwibawa",  
                "pesan":"sukses terus kak, semoga bisa cepet dapet gelar S.Si.D"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumatera Barat",
                "alamat": "Gya kost korpri",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@farahanumafifahh",
                "kesan": "ramah dan humble, tipikal kakak yang asik diajak ngobrol",  
                "pesan":"semangat berjuang kak, sukses terus ya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rjmAIoXNbwLjdxCbHzZMkzsY1QcOZXC4",#jeremia susanto
            "https://drive.google.com/uc?export=view&id=1qUWNp1r3nsc_Q0mvM11ScgoLOOuzRi71",#Dhea Amelia Putri
            "https://drive.google.com/uc?export=view&id=1vbhUWXQbf2-8X0nqVMJ4enmhhcUgbS3e",#Renisha Putri Giani
            "https://drive.google.com/uc?export=view&id=1OHnRuGy3P0Owu9xwES1M6O2FRaWZcjOZ",#Anisa Fitriyani
            "https://drive.google.com/uc?export=view&id=1jEzX3nsaZqjouTezzRi4xa7f6gEXPuwN",#Dharu Cahyoaji Sasongko
            "https://drive.google.com/uc?export=view&id=1SWkaRJDNSn7SmM1b7KKZvWLso9LUrogg",#Feby Wulandari
            "https://drive.google.com/uc?export=view&id=1Jk_j88-Y9sUAbWmOiNfJK5MsxUXWKwck",#Givaro Ananta
            "https://drive.google.com/uc?export=view&id=119nEalasBivLw7UYllFrmH1-hXSLODve",#Mirzan Yusuf Rabbani
            "https://drive.google.com/uc?export=view&id=1z1sUwhFGI5MYoAaCK_ToJgnBlbfZ_vmD",#Berliana Enda Putri
            "https://drive.google.com/uc?export=view&id=1qxzGfACTz4ubJU6i2xQneIsD4ycQ_NRJ",#Juesi Apridelia Saragih
            "https://drive.google.com/uc?export=view&id=1g2oh1dwDDHQqwyB8YbYC3Q-WdYuOCGHg",#Ridho Benedictus Togi Manik
            "https://drive.google.com/uc?export=view&id=1afgrKWhRlj2WKHiG4bh8aSixmoq8I0d4",#Feryadi Yulius
            "https://drive.google.com/uc?export=view&id=1lGPL0UEl15sTjTqoWLRlpSN9xHvHntIo",#Monica Patricia Tanjung
            "https://drive.google.com/uc?export=view&id=13w-HAQdkT80xzgKOyvnlJPbAq3FWg0m9",#Wan Nashwa Alhasni Yuska
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Lapas , Belwis",
                "hobbi": "Zumba di pln setiap jumat pagi",
                "sosmed": "@jeremia_s_",
                "kesan": "abangnya ramah dan asik banget, jadi betah ngobrol lama dengan dia",  
                "pesan":"semangat bang semoga dipermudah TA nya"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Mojokerto",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "kakak ini sangat berwibawa",  
                "pesan":"semoga sukses selalu kak!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "kakak ini sangat baik",  
                "pesan":"semangat dan sehat terus kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kakak ini sangat baik dan ramah",  
                "pesan":"sehat dan sukses terus kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@dhruchyo",
                "kesan": "abang ini sangat pintar dan asik",  
                "pesan":"semoga jaya selalu bang!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak ini sangat imutz dan kalem",  
                "pesan":"semoga cita-cita kakak bisa tercapai"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "abang ini penuh dengan wibawa dan tanggung jawab",  
                "pesan":"semangat bang semoga bisa meraih lebih banyak prestasi lagi!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini penuh dengan aura dan wibawa",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya sangat baik, dan penuh pengertian",  
                "pesan":"semangat kak, semoga kakak bisa lulus tepat waktu"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini baik dan memiliki karakter yang menyenangkan",  
                "pesan":"semoga kakak sukses selalu!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang ini sangat baik, asik, dan ramah tehadap kami yang adik tingkatannya",  
                "pesan":"semangat bang, kami membutuhkanmu"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya asik dan ramah banget.",  
                "pesan":"semoga kakak sehat selalu dan lancar kuliahnya."# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya asik dan baik banget",  
                "pesan":"sehat selalu kak!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Pekanbaru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "mentor kesayangan",  
                "pesan":"semoga kakak sukses dan sehat selalu "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bbHEPSlCNpi5ia-mHeqhkWba5KSrTmxi",#rian bintang wijaya
            "https://drive.google.com/uc?export=view&id=1DaTAnF0XxTnkAx6TKFjp38mPVN8aYimJ",#Nadya Ratu Anjani
            "https://drive.google.com/uc?export=view&id=1nkJmqYfOLO52o7qZB2klOxxKoDJzRXU1",#Fathinah Nur Azizah
            "https://drive.google.com/uc?export=view&id=1CJappB1EJZZjA52l-77rMyGbC0K1QjK4",#Lia Hana Ichisasmita

        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya asik dan ramah banget",  
                "pesan":"sehat-sehat bang, semoga sukses selalu "# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
               "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "belakang indomaret belwis",
                "hobbi": "Main roblox",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya baik dan ramah banget",  
                "pesan":"tetap tersenyum kak :)"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakaknya baik dan sangat ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "kakaknya baik dan bijak",  
                "pesan":"sukses selalu ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fFrmMIxVJd65AcU3ZvZqJMHXn9fRHb11", #Ferdy Kevin Naibaho
            "https://drive.google.com/uc?export=view&id=1nK6z7Ok9wb-_JggmY--5s_Tp5Cwuds-e", #Nisrina Nur Afifah
            "https://drive.google.com/uc?export=view&id=1tye5d3yMWsV4qEFWRe9-R2zfvxYJ9mVr", #Allya Nurul Islami Pasha
            "https://drive.google.com/uc?export=view&id=1uOJQ-MtDj2WPapNjAVfs7LnzxTR2lRx0", #Ahmad Rizky
            "https://drive.google.com/uc?export=view&id=1YN02viSNtFK0Ak6nXMrQHzCz1o7aRQBV", #Arienta Khusnul Ananda
            "https://drive.google.com/uc?export=view&id=1I4PpFq9ecWHq7qN0xRpcPCSbeWTMC8MC", #Daffa Hadyan Navista
            "https://drive.google.com/uc?export=view&id=1AzRtpFTqUOzmpCs938PNYzOo3Y-ajuw4", #Ginda Fajar Riadi Marpaung
            "https://drive.google.com/uc?export=view&id=1Y1i6VQ9c2FlZYCYdtXDvsi_S4nIv-GwU", #Natasya Amavisca
            "https://drive.google.com/uc?export=view&id=1EDi0iODuY4Vumhf7fKCkBicqH5RrTtqn", #Nobel Nizam F.
            "https://drive.google.com/uc?export=view&id=1Gsr4yk6cMsyh4Ja0g-kQSfFOecksHiy8", #Nurul Alfajar Gumel
            "https://drive.google.com/uc?export=view&id=1xqKv2_ZnM6jNyOJeEPw_VyBok03F7EcR", #vany salsabila putri
            "https://drive.google.com/uc?export=view&id=11jx72mKccHFGqhQ1lzz0dtbCOS_av2rT", #Ahmad Sahidin Akbar
            "https://drive.google.com/uc?export=view&id=1Ousbfbd-_x6Sp0TUEIGy5Sj36Mb9ngrq", #Ali Aristo Muthahhari Parisi
            "https://drive.google.com/uc?export=view&id=1AyonuvwXzPXBHFs5D2jC2lKnfs8Trwak", #Gusti Putu Ferazka
            "https://drive.google.com/uc?export=view&id=1StCWadfL4rGiFMGCnvwbaiP5MHgnGaWE", #Kharisma Mustika Sari
            "https://drive.google.com/uc?export=view&id=1yps0Ok2V78lip9zhe31JJKokPe_qfQer", #Rosalia Siregar (belum ada foto)
            "https://drive.google.com/uc?export=view&id=1naHP0ciju1Ip0_aKp2wRt2I9mvSeirFn", #sahid maulana
            "https://drive.google.com/uc?export=view&id=17HIXBqbt5mEAhg7Q9DhvfN9f6jDmdACt", #Daffa Ahmad Naufal
            "https://drive.google.com/uc?export=view&id=1x73_g8xgoMOPzG3JWMxdc6OstZXXPmUw", #Erma Daniar Safitri
            "https://drive.google.com/uc?export=view&id=1fMVTtXYYZ8pVnzgcuufSxFUd7QHbRJtr", #Ihsan Maulana Yusuf
            "https://drive.google.com/uc?export=view&id=1F93XApfEA-tahpgxug9GQvhvWyPtgd5G", #Kevin Antoni Junior
            "https://drive.google.com/uc?export=view&id=1mGYX1p0ZIONnd9n-pUGEIjLKmBxIA7NO", #Lidia Natasyah Marpaung
            "https://drive.google.com/uc?export=view&id=11Zb5HIHFvFjzzpJXTehPs-ItcdETz7ph", #Muhammad Ridwan
            "https://drive.google.com/uc?export=view&id=1_wa78qgrBDydTyFXIlG5TncqZ0EdKjpV", #Benget Sidabutar
            "https://drive.google.com/uc?export=view&id=17HDj2UwNvtWBIthHg37ZOC2z2iOsfALV", #Uliano Wilyam Purba
            "https://drive.google.com/uc?export=view&id=1WzzT-zTOshkOq1wnAhl_OrmmjINJ7LNm", #Rewina Audrya Melva Sari
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "berwibawa, tegas, dan cool",  
                "pesan":"semangat berjuang dan sukses selalu bang"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakak penuh dengan semangat",  
                "pesan":"Jangan pernah kendor semangatnya, Kak!!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "kakanya sangat berwibawa",  
                "pesan":"semangat terus kak, sehat sehat ya!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Gh Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "abangnya asik dan ramah banget serta sangat berwibawa",  
                "pesan":"semoga bisa mencapai prestasi yang lebih banyak lagi"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kos dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "kakak ini sebenernya baik, tapi waktu kader harus professional",  
                "pesan":"Jangan sampai lowbat ya, Kak! Jaga kesehatan!"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "abang ini asik apalagi waktu suporteran",  
                "pesan":"jangan lupa jaga kesehatan ya bang!"# 1
            },
            {
                 "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat":"Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "abangnya sangat baik kepada kami dan pengertian ",  
                "pesan":"semoga abang sukses selalu"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat":"Kos putri gerbang barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "waktu di kelas kakaknya aktif banget",  
                "pesan":"sehat sehat kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat":"Sebelah kos kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "jago banget soal komputasi",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat":"Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "aura wibawanya kerasa banget",  
                "pesan":"semoga sehat selalu bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat":"Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "tegas dan tanpa kompromi",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "abangnya baik dan ramah banget",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat":"Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kulineran kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "pendiam tapi asik",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat":"Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "kakaknya ramah dan baik",  
                "pesan":"sukses terus kk"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat":"Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "humble dan ramah",  
                "pesan":"semangat kakak!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "122450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "pernah ditolongin waktu di medis",  
                "pesan":"sehat terus kak, kalo kakak sakit siapa yang nolong di medis"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat":"Jl. Airan",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "abangnya humble, baik, dan pengertian, to the point juga",  
                "pesan":"semangat terus bang semoga sukses selalu"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Bebersih kod",
                "sosmed": "@ahmadnaufal_",
                "kesan": "berwibawa dan coach",  
                "pesan":"sukses selalu bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat":"Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "ceria dan jago nari",  
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "122450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Joki strava",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnya asik dan ramah banget",  
                "pesan":"semoga sehat selalu bang"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "122450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertani",
                "sosmed": "@kevinaj__",
                "kesan": "abangnya cool dan ramah banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "122450013",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakak ini kalem banget",  
                "pesan":"semoga sukses selalu"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "122450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton yt pak tamaro",
                "sosmed": "@ridwan122",
                "kesan": "abangnya ramah dan baik banget",  
                "pesan":"semangat bang "# 1
            },
            {
                "nama": "Benget Sidabutar",
               "nim": "122450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "abnagnya jenaka dan asik banget",  
                "pesan":"semangat bang"# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "kerjain soal MTK",
                "sosmed": "@liano.wan",
                "kesan": "abangnya tegas banget",  
                "pesan":"jangan galak galak bang"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "122450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl.Ratu, Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@rewinaaa",
                "kesan": "kalem dan pendiem",  
                "pesan":"semangat kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XiyCeJTvYHkDgCmtKOG0W--CwWrYi2Nu", #Randa Andriana Putra
            "https://drive.google.com/uc?export=view&id=1OfyOfBjGmK7PLKNcPnuCfhFvwTap6djX", #Rut Junita Sari Siburian
            "https://drive.google.com/uc?export=view&id=1_JeWAFnqSCe12-Iu9t8Xfb4kRvCmV2Xa", #Muhammad Regi Abdi Putra Amanta
            "https://drive.google.com/uc?export=view&id=1UEoUL_MDESCsSvQhIwXW5Fr42O7yFvwk", #Aisyah Musfirah
            "https://drive.google.com/uc?export=view&id=14R5WnmNILqIwOsj4n6iq1alK2gaBV-bw", #Fadil Prasetyo Alfarizzi
            "https://drive.google.com/uc?export=view&id=1SZB0PN7s-BrsqizmSQKMwaa2Rw7PC8np", #Muhammad Aqil Ramadhan
            "https://drive.google.com/uc?export=view&id=1uAdTR4gZE0xSQ0LcxuqmkMuRSam6x5QR", #Muhammad Naufal Ramadhan
            "https://drive.google.com/uc?export=view&id=1RGb9qNAMMWdlK-VQBIHLI4v_WY_vtYZR", #Nadia Faraj Alyafaatin Simbolon
            "https://drive.google.com/uc?export=view&id=19Q0CVH5I0Oo_IXO33rczxwgfKUfhfTjG", #Marleta Cornelia Leander
            "https://drive.google.com/uc?export=view&id=1yRVj7D--wtwzrBWCwcicTXRDyuaq2wMP", #Akeyla Fairuz Shafi
            "https://drive.google.com/uc?export=view&id=12iiagfcSGz3WTBsj24lRrrMZrkCv61Vg", #Anggi Puspita Ningrum
            "https://drive.google.com/uc?export=view&id=12iiagfcSGz3WTBsj24lRrrMZrkCv61Vg", #Efi Defiyati
            "https://drive.google.com/uc?export=view&id=1FCuqsVs2LoM6M9EDVZY_-6pqWHHmSoU1", #Fabiolla Charissa Putri
            "https://drive.google.com/uc?export=view&id=1A45-BSRLXHC_pnH54DNzoVXo2T6_zkoS", #Fairuz Ary Syifa
            "https://drive.google.com/uc?export=view&id=1ZBPuxr2Qn-eWUM4lrKKkt0KtFqQoAjo8", #Tanty Widiyastuti
            "https://drive.google.com/uc?export=view&id=1FcnjNxNdPWPQSdYb66q7rgJKXpiAJbxL", #Eggi Satria
            "https://drive.google.com/uc?export=view&id=14ReNw68CLKnyj6LmoQPfgdH2eOL7shOe", #Afifah Fauziah
            "https://drive.google.com/uc?export=view&id=19gZe4RC4_CUgeUr9yTipFLhkb1KIhQ8s", #Fabio Banyu Cyto
            "https://drive.google.com/uc?export=view&id=1h5j1_eTwlVCdveMEiZkwCZHWXGf10Ln_", #Giofani Aristyo
            "https://drive.google.com/uc?export=view&id=1r1xtE_cagZmbuzOC4xI9Tm8IuU5MEDUM", #Rahma Oktavia Albar
            "https://drive.google.com/uc?export=view&id=1RhmjjOOzaajkB2yBK17E7kc1pbUCpD9r", #Rahmah Gustriana Deka
            "https://drive.google.com/uc?export=view&id=1jKwY1PBB5nylUaXjvrFXHA2wxJqmoGyT", #Razin Hafid Hamdi
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123340083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep . Riau",
                "alamat": "Nangka 3",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Jl.Permadani, Sukarame",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat":"Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat":"GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat":"Bandar Lampung",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat":"Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat":"Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keyashafi_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat":"Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat":"Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat":"Pesawaran, Lampung",
                "hobbi": "Main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat":"Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat":"Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat":"Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat":"Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Kedaton",
                "hobbi": " Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Giofani Aristyo",
                 "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat":"Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat":"Lapas Raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat":"Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                 "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat":"Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w2hv5qTtnA8W-zqw0e8oTJhRmXJjDzMG", #Arafi Ramadhan Maulana
            "https://drive.google.com/uc?export=view&id=1DSl0Sqkeqr4rsLwmm3BvLl_ASRTnPFBf", #Yohana Manik
            "https://drive.google.com/uc?export=view&id=12eVtuD7rBjY2jrp17IPspiQXWToAlhiF", #Ratu Keisha Jasmine Deanova
            "https://drive.google.com/uc?export=view&id=1v72mB69Hjd7tU8v0knAljW_7WeVTgi6J", #Arini Puteri Elandra
            "https://drive.google.com/uc?export=view&id=1jVBKBnEcp8xxi6ks8DkGjvHCmWuMLGYI", #Arya Muda Siregar
            "https://drive.google.com/uc?export=view&id=1D1wxSu7gyhJzn-wuoejMnot_TdKT248w", #Khoirul Muttoharoh
            "https://drive.google.com/uc?export=view&id=1gWX3VIfhUHCOWhWTDU55ve5JQA2aG-rX", #Lutfia Aisyah Putri
            "https://drive.google.com/uc?export=view&id=1pb6NHRiNwSBqVzWvDJzNg5F7hgI9AI5Y", #Nabyla Sharfina
            "https://drive.google.com/uc?export=view&id=1wdLZjCRDDpZv4kwGoJQg50ozx93fSJsB", #Syahrialdi Rachim Akbar
            "https://drive.google.com/uc?export=view&id=1YhI6wpC_ciECRhkrZgpLVGColL2o2OnP", #Dea Mutia Risani
            "https://drive.google.com/uc?export=view&id=1KQ1jN9LkNFM_x3DS5o8Wupjgkt_2jj8R", #Cindy Laura Manik
            "https://drive.google.com/uc?export=view&id=1xj71YWgU261RxGP9te6yFWCf4e4nfCVo", #Dea Amanda
            "https://drive.google.com/uc?export=view&id=1i-NZJ9xtUtXFU4f87k69TOmPc1RMDEeX", #Desman Velius Halawa
            "https://drive.google.com/uc?export=view&id=10NQs0y9MGKkeTITDf6VqgV3aLuyHQ3rx", #Devyna Sonya Palupi Sanjaya
            "https://drive.google.com/uc?export=view&id=1Frzo9_dnbW77Caf_mnxs0n9bHF0-4WMc", #Luthfia Laila Ramadhani
            "https://drive.google.com/uc?export=view&id=1glXKHURH5reJ-0hy16VnORG3GM9oGPUH", #Irvan Alfaritzi
            "https://drive.google.com/uc?export=view&id=1xhroZguQOFZF4IZYu05EE6NVgFrvuytw", #Aditya Taufiqurrohman
            "https://drive.google.com/uc?export=view&id=1aAemHK0SLZL0vJplp4byvvJj1tVP2tiH", #Fathya Intami Gusda
            "https://drive.google.com/uc?export=view&id=1zTCCSXEsCLe1j-SNCkyABtukQjgoCDJR", #Khazanatil Ilmi
            "https://drive.google.com/uc?export=view&id=1axkjMTS2jbPP6odk0i_ND6iO1UtaVck-", #Melinza Nabila
            "https://drive.google.com/uc?export=view&id=19QVrAFQD-iVe2mMe1hdEvdMu3JTDc4oH", #Nayla Shafira Roza
            "https://drive.google.com/uc?export=view&id=1MBOxhcEjOPbaK9aGaAqVGros5kD_d-NF", #Nurul Izzah Istiqomah
            "https://drive.google.com/uc?export=view&id=16NICprI2L4Sl9zkYxwznamuTDZObygnH", #Qois Olifio
            "https://drive.google.com/uc?export=view&id=1Hc75fjSCEoXDLrKKopf_FSwlb7Skamym", #Tarisya hidayatul rahmi
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat":"Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Gg.sakum",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                 "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl.Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()
elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1s7ouybeYWR-FSB2rjtYW7WDNKpgUNXud", #Rani Puspita sari
            "https://drive.google.com/uc?export=view&id=1NWCYA2x7qM47aHPNJClVLGDT6jIM8x_s", #Renta Siahaan
            "https://drive.google.com/uc?export=view&id=1NWCYA2x7qM47aHPNJClVLGDT6jIM8x_s", #Salwa Farhanatussaidah
            "https://drive.google.com/uc?export=view&id=1ShXYobcdGmMTlpTHBnJR7g39H1_zSNVY", #Azzahra Putri Kamilah
            "https://drive.google.com/uc?export=view&id=1t1T2WYgA7J3eJgHB1xqt1PEbk-cxh8lq", #Haikal Fransisko Simbolon
            "https://drive.google.com/uc?export=view&id=1HiFWFGj9LKIhsrSjNzHEE9gCUtTiuR_b", #Iqfina Haula Halika
            "https://drive.google.com/uc?export=view&id=13RjEGZt3ZeFzPAtElVK6_5n08R7X7JN_", #May Talitha Dahlia
            "https://drive.google.com/uc?export=view&id=1z7jt0ZQQcLob0uEPO_Ed9UKvPtJso-Jv", #Muhammad Naufal Alghani
            "https://drive.google.com/uc?export=view&id=1SAhn6tVdo97-VPjdEEdX01wIgZum3Djt", #Zailani Satria
            "https://drive.google.com/uc?export=view&id=1nYvmuJ6BRDNyDQEH2tIYjhj3VOrnLsGP", #Rendi Alexander Hutagalung
            "https://drive.google.com/uc?export=view&id=1SP7IzcUyODdqB0inH646hc7Pk4RKLro0", #Hanna Gresia Sinaga
            "https://drive.google.com/uc?export=view&id=1uoYfZTBcdXCFsD1p0CtlonzXN7o2bXtT", #Keren Marito Lumban Gaol
            "https://drive.google.com/uc?export=view&id=1wMr3ct9z8UlZ0PZpRRTDtwjny5HSyd-n", #Muhammad Hanif Dzaky Arifin
            "https://drive.google.com/uc?export=view&id=1wB24QPsnHivqH6CQlZ9OZfWOyeL7jYLq", #Sarah Wasti
            "https://drive.google.com/uc?export=view&id=1gcIhVG3gonSb1AFHf7TU53cjSY8adPme", #Zahra Putri Salsabilla
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat":"Balam",
                "hobbi": "Mengaji",
                "sosmed": "@ranniku",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat":"Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
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
                "nama": "Azzahra Putri Kamilah",
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
                "nama": "Haikal Fransisko Simbolon",
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
                "nama": "Iqfina Haula Halika",
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
                "nama": "May Talitha Dahlia",
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
                "nama": "Muhammad Naufal Alghani",
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
                "nama": "Zailani Satria",
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
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat":"Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": " 123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat":"Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
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
                "nama": "Muhammad Hanif Dzaky Arifin",
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
                "nama": "Sarah Wasti",
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
                "nama": "Zahra Putri Salsabilla",
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
    DepartemenInternal()
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yV__fu-g4S72333ZCLsJ4ZuR1ItPjoKx", #Danang Hilal Kurniawan
            "https://drive.google.com/uc?export=view&id=1RlokvYONJbrKqRhaS6KyMeGvrMDuZ6NN", #Syalaisha Andina Putriansyah
            "https://drive.google.com/uc?export=view&id=1fPHuWWzVmNN3rTpbPnn-DWRil9p3CANK", #Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=1NBQlC4M4t2v9DKE3IYX4gX6Zrotin3P5", #Anadia Carana
            "https://drive.google.com/uc?export=view&id=15uQduhhNoyoVhZTSuyreEd-8EoTtOOrH", #Aprilia Dewi Hutapea
            "https://drive.google.com/uc?export=view&id=1RkP4tdRsZMWeNV0XPVx1NWfPWNUahbCG", #Nabila Zakiyah Zahra
            "https://drive.google.com/uc?export=view&id=1PypVVHasT_9rZlj-JBGrIuStAXIx0HSR", #Dhafin Razaqa Luthfi
            "https://drive.google.com/uc?export=view&id=1Y-ZJEJILsScR7nt3yYSUyd1ENwAhDHQs", #Devi Rahayu
            "https://drive.google.com/uc?export=view&id=1eLHL307Dejox4vKBoSn5RgtOOepq-O12", #Enggli Rahmadhani
            "https://drive.google.com/uc?export=view&id=1A-6tYJFL1ChTQRJgwzUtGCSvS3cd_6H9", #Hanifah Inaya Sani
            "https://drive.google.com/uc?export=view&id=1INsZTOta6ddoUd9AtaGfDeXlgal-moz0", #Nydia Manda Putri
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "Beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Menonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. perwira 2",
                "hobbi": "Menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()
elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ukPczcb3wKjk3zxKv9BNKj2StqX7F3Lf", #Patricia Leondrea Diajeng Putri
            "https://drive.google.com/uc?export=view&id=1_A5752cNkmRYPCNo9dRInDbtf-4LeytQ", #Rahma Neliyana
            "https://drive.google.com/uc?export=view&id=1MZgc4gj5jdqUQ3RqQOBescmJhJTLcSSn", #Khoirul Anam
            "https://drive.google.com/uc?export=view&id=1-7WlgJdETLsut6ZLZLeBXTPtOYZocxpH", #Labo John Noel Napitupulu
            "https://drive.google.com/uc?export=view&id=1GaBGrq6ZgS7W-a3_7CD6vRyBbNs6LLDs", #Rafi Diva Efangga
            "https://drive.google.com/uc?export=view&id=1QmN0r7TMI7sLhluAb1rh9rjf-oWkKL0e", #Refa Destiny Pranata
            "https://drive.google.com/uc?export=view&id=1tGn7M8r--1byDG9g5lJ1hGIP1mh1_E1M", #Try Yani Rizki Nur Rohmah
            "https://drive.google.com/uc?export=view&id=12hJoupU7N2OPdh98sIcZ8WkEcSuFr1Yz", #Aliya Ammara Ananta
            "https://drive.google.com/uc?export=view&id=1mgk3xqXHbTy6bUigvO6iw5kuQ1DN0HcV", #Donna Maya Puspita
            "https://drive.google.com/uc?export=view&id=1mluDp8YThaIxAUJ9EV4U1trqmpMciSc2", #Feby Angelina
            "https://drive.google.com/uc?export=view&id=1Axbyi7l_EKMnLpxthsyiR1wbr_NeoIQj", #Hafsa Fazila Arradhi
            "https://drive.google.com/uc?export=view&id=1A2GbfoXcvPPO_MdVd9bulp-Vy29nDeAf", #Nayla Salsabila Fathianisa
            "https://drive.google.com/uc?export=view&id=1n1MOPhl-SyUx3KvWc6aish5E3Clk4I80", #Sania Dwi Ayu Lestari
            "https://drive.google.com/uc?export=view&id=1V39dQ2UgiVqteWfPO9l1gzxhKKaAV2qS", #Akmal Faiz Abdillah
            "https://drive.google.com/uc?export=view&id=1-NxbZc3CGMGMxxSE-RbQ-icOigw9QQjE", #Raihana Adelia Putri
            "https://drive.google.com/uc?export=view&id=1u8Wnj9zpsiZeG9ml1hyeXAbpXrc3XIiP", #Citra Agustin
            "https://drive.google.com/uc?export=view&id=1akiW80lztWJHhVV0mf6TvMhMzBW8eAPF", #Eigi Artamevia
            "https://drive.google.com/uc?export=view&id=1yJqdRG4pTZAaStPQKn9BBr2enmECVSIg", #Romauli Oktavia Silaban
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jati Mulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "jl. Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "jl.pangeran senopati raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labukan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumbar",
                "alamat": "jl.Lapas, kec.Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak ",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan

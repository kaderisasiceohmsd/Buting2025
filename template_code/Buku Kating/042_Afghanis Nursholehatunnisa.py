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
            "https://drive.google.com/uc?export=view&id=1i4FHB6rSaMMToSXtV4e-1BPn5-mNhIyt",
            "https://drive.google.com/uc?export=view&id=182YSPvotTZ6y2CvXhQCSfSdGjgf9zhQ5",
            "https://drive.google.com/uc?export=view&id=1rhqSdSKz9ASNIJd7TATKaWUvW7i7ImBU",
            "https://drive.google.com/uc?export=view&id=1Jaj-KQy4Ogv23jNaFmNpmh-ABSkNQN0q",
            "https://drive.google.com/uc?export=view&id=1OLMMCaslFHbH6sLdnf0I0sReXyqm1ysV",
            "https://drive.google.com/uc?export=view&id=1CtVZsPsrEAqYcidDmSaD3svKwdB_t_1V",
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
                "kesan": "Public speaking dan suaranya bagus! berwibawa tapi lucu, panutan",  
                "pesan":"sukses terus bang dan semoga cepat lulus kuliahnya ya!!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku sequel",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Walaupun abangnya jahil tapi seru banget, ",  
                "pesan":"semangat kuliahnya bang, semoga cepat lulus !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Badui dalem",
                "alamat": "Ayrest Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak ini ramah banget, selalu ceria dan murah senyum ",  
                "pesan":"semangat kuliahnya kakak cantik, selalu tebarin senyum ya!!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya positive vibes banget, kalem, pendiem dan manis",  
                "pesan":"Selalu tebarkan energi positifmu ya kakak maniesz!!!"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "12245001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Utara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakak ini bisa menempatkan posisi kapan bercanda dan serius, tegas dan humble",  
                "pesan":"kakak keren bangett, semangat kuliahnya ya !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Gya kost korpri",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Sangat positive vibes, humble dan lucuu",  
                "pesan":"semoga segala urusan kakak dipermudah ya, semangat kakak cantik!!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VohUQlmq4LfQnTXsyroWp9-6s1sx40Or",
            "https://drive.google.com/uc?export=view&id=1-JiP7-Ey5sOL_g663UMwIn2PXmOWXJ1G",
            "https://drive.google.com/uc?export=view&id=1rkkw5D3kxHbJSvGwxXhH-Dt2iRHdIrKT",
            "https://drive.google.com/uc?export=view&id=1RBnJ0s8wDEFbNIkG8aaWhtHCMGxbkRVC",
            "https://drive.google.com/uc?export=view&id=12UFosd0D1mhWLzRQzHfPvjg3Wp9HJU8z",
            "https://drive.google.com/uc?export=view&id=1T30pUWtXHfY_70tmq5BOPr1GkkOyGeCr",
            "https://drive.google.com/uc?export=view&id=1WUc4tF9wE3riQu3Md8HBuLQqgEoLp463",
            "https://drive.google.com/uc?export=view&id=1qI5vHXzFjBaqLDhYa5pgbZQAr_q_cmnc",
            "https://drive.google.com/uc?export=view&id=1GQ_5EV2fBgPbUckYZZ422K0DGvgCgmy5",
            "https://drive.google.com/uc?export=view&id=180RQpC_g09lN0r60dc-ani5ioHEgbb4N",
            "https://drive.google.com/uc?export=view&id=1LsLYmot9jE1isslfu47Scvm46rlY0Dsy",
            "https://drive.google.com/uc?export=view&id=1fr0jucnW0dfOaRnakv82sjmeRaxPknP4",
            "https://drive.google.com/uc?export=view&id=1JpuGDkiE0nw7lUeXR4e-fpfBO2B7NUqn",
            "https://drive.google.com/uc?export=view&id=18w5Asd9Q8cLizApZ8xIAhr0nf5i3i7Qy",
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
                "kesan": "Public speakingnya bagus banget, perhatian, dan bijak",  
                "pesan":"semoga apa yang dicita-citakan terwujud ya bang, sukses selalu yaa!!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Mojokerto",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya asik banget, humble, random dan stylish banget",  
                "pesan":"semangat terus menjalani harinya kak, selalu jadi kakak yang ceria yaa!!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakak ini kalem, ramah, baik hati",  
                "pesan":"semangat kuliahnya kakk, jaga kesehatan yaa !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini asik, perhatian, baik hati",  
                "pesan":"lancar terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "pinterr bangett, cerdas, selalu berprestasi ",  
                "pesan":"sukses terus yaa, semoga selalu berprestasi !!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak NIM-ku yang cantik dan menggemaskan, stylish, dan keren banget",  
                "pesan":"semoga dipermudah segala urusan dan kuliahnya kakak cantik !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "baik banget, pengertian dan perhatian, suka menolong, ",  
                "pesan":"terus sebarkan kebaikan ya bang, dan semoga dibalas segala kebaikanmu !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya pendiem, dan kalem tapi suka ngegame",  
                "pesan":"semangat bang, semoga harimu berwarna!!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini random banget, selalu ada gebrakan, asik dan kocak banget",  
                "pesan":"selalu jadi pribadi yang periang dan ceria ya kak, semangat terus kak!!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini positive vibes, baik hati, ramah",  
                "pesan":"semangat dan sukses selalu kakak cantik !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya lucu, random, asik dan baik ",  
                "pesan":"semoga segala urusan diperlancar ya bang, goodluck !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini baik, kalem dan ramah",  
                "pesan":" semangat kuliahnya bang, sukses selalu!!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "122450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini kalem, pemalu, dan lucu",  
                "pesan":"semangat kuliahnya kak, semoga bahagia selalu !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Pekanbaru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Mentor kesayanganku yang lucu, baik hati, perhatian, asik",  
                "pesan":"semoga kakak bahagia dan sukses selalu ya, love you kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12jpsmRCuRORL79dXQo133qHLHdjGzKJR",
            "https://drive.google.com/uc?export=view&id=1MpZ6yJkR-GSU1uh73au4Lz9WnJPjBfhR",
            "https://drive.google.com/uc?export=view&id=1uIB4DiZnc8KSL5AySQM4h17bz_mS15ZX",
            "https://drive.google.com/uc?export=view&id=1A8okF1ifc5chqMdIhGZmsqPMqgD1QYxG",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Gg.sakum",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "abang ini berwibawa, bijak, cerdas, public speakingnya bagus, tegas",  
                "pesan":"semoga segala urusan dipermudah ya bang, semoga cepat lulus !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "belakang indomaret belwis",
                "hobbi": "Main roblox",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini positive vibes, cantik, ramah",  
                "pesan":"selalu tebarkan energi positif ya kakak cantik!!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini lembut, positive vibes, cerdas, ramah",  
                "pesan":"vibes kakaknya adem banget!!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini ramah, asik, baik",  
                "pesan":"semangat dan sukses terus kak!!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hblQaxNadhGP8B8JV3AMxq1TL54e7hYL", #Ferdy Kevin Naibaho
            "https://drive.google.com/uc?export=view&id=1qMSuubgQVIO-kaPCX7hl_1ygawJWfiv2", #Nisrina Nur Afifah
            "https://drive.google.com/uc?export=view&id=1ZoVhWQmZqCyg_X0-seS-7sKZgNksKjYh", #Allya Nurul Islami Pasha
            "https://drive.google.com/uc?export=view&id=1_IIzBJnyajXAHZ_AwuXG4r7FMCSy2md4", #Ahmad Rizky
            "https://drive.google.com/uc?export=view&id=1MytBjycgZYZivtB5fLVQpXiHvOm_GDDU", #Arienta Khusnul Ananda
            "https://drive.google.com/uc?export=view&id=1Xsq_UmBIJhW2oR14rozzNbioIpt85a_e", #Daffa Hadyan Navista
            "https://drive.google.com/uc?export=view&id=14yYj4rutY0iWPzaP2g3zQTLn6b88bBLp", #Ginda Fajar Riadi Marpaung
            "https://drive.google.com/uc?export=view&id=16umYauuwQCDQLeHKpO_Sv5KSJNar8Rqp", #Natasya Amavisca
            "https://drive.google.com/uc?export=view&id=1X66GdbcnOTijJqT1tyooU2a2AML-U0QS", #Nobel Nizam F.
            "https://drive.google.com/uc?export=view&id=1J0oQw0EJRRwkgxi53P1nMlRskNshKS-c",
            "https://drive.google.com/uc?export=view&id=1J0oQw0EJRRwkgxi53P1nMlRskNshKS", #Nurul Alfajar Gumel
            "https://drive.google.com/uc?export=view&id=1vQoXpseE_O0QAqUUhd2V0XQ-l6XUtJ_e", #vany salsabila putri
            "https://drive.google.com/uc?export=view&id=1q9uoCBcaA-RKVHkjjWfIP6CrXTCe_EmB", #Ahmad Sahidin Akbar
            "https://drive.google.com/uc?export=view&id=1w_f6VHcb3jOsdnVgGdPLW6R-ceHmSMcz", #Ali Aristo Muthahhari Parisi
            "https://drive.google.com/uc?export=view&id=1buBjU82r5EGRYhAa15wSybuVp15K7IqD", #Gusti Putu Ferazka
            "https://drive.google.com/uc?export=view&id=1pQQPJx-KJzmt8-aVGZJPQ7jOBNLFXN6a", #Kharisma Mustika Sari
            "https://drive.google.com/uc?export=view&id=1X6RJV7zeVcz6rm9PYVJW_nw6Tk8X0Iet", #Rosalia Siregar (belum ada foto)
            "https://drive.google.com/uc?export=view&id=1QjmBiZlu_Z3H2lUsXWaGY-IFh3BDe7y3", #sahid maulana
            "https://drive.google.com/uc?export=view&id=1jgcKNAwf1vjdenjWyoK8QLnu0sgMGwJZ", #Daffa Ahmad Naufal
            "https://drive.google.com/uc?export=view&id=17qQBnLMqEq6d4520CCNcRDEBStG314o9", #Erma Daniar Safitri
            "https://drive.google.com/uc?export=view&id=11kMC47dqXQ-sWbs3jlLIRLJ8cPGGCfuB", #Ihsan Maulana Yusuf
            "https://drive.google.com/uc?export=view&id=1J7fi8cB4tuWm7wWQoCI6i9Ooml-Q15-4", #Kevin Antoni Junior
            "https://drive.google.com/uc?export=view&id=1yGZ7Cz_dRjAfIXVlZSDbbskcmCbot3OL", #Lidia Natasyah Marpaung
            "https://drive.google.com/uc?export=view&id=1nUaquK714vG9Yyj2j30bxUuuMNb1XgvM", #Muhammad Ridwan
            "https://drive.google.com/uc?export=view&id=1jwBEIfOrFzaAN1C2CfbH-0nFRHyOOLsW", #Benget Sidabutar
            "https://drive.google.com/uc?export=view&id=1D2XKQe50uUbt8_Heh8pXOOXlf-Z0Tbue", #Uliano Wilyam Purba
            "https://drive.google.com/uc?export=view&id=1PsvAxQi1uvOiRri5ZdmXtCKjCwg1ruQ3", #Rewina Audrya Melva Sari
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Abang ini tegas, ",  
                "pesan":"semangat dan sukses selalu ya bang !!!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":"Semangat dan bahagia selalu kak!!!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "",  
                "pesan":"semoga segala urusan kakak dipermudah ya.. semangat terus kak"# 3
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "keren, ",  
                "pesan":"semoga segala urusan abang dipermudah ya! goodluck "# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": " ramah",  
                "pesan":"semangat menjalani harinya kak, jaga kesehatan ya"# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "tegas, ramah ",  
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
                "kesan": "abangnya baik banget, perhatian ",  
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
                "kesan": "tegas,  ",  
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
                "kesan": "abagnya baik, rama ",
                "pesan": " " # 26
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
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1N-nR92cEa2_HSP0ultWh3Y6MrBcj5mUj",
            "https://drive.google.com/uc?export=view&id=1FhkbGRP3L0oiQtyEwOnlPKHjbHeL-TpD",
            "https://drive.google.com/uc?export=view&id=1K28PKAiKJUu0UFyHB-h1w0t8I1HjF3As",
            "https://drive.google.com/uc?export=view&id=1ZcqLKbdrxo12EqRdKue9myv3S5WzIjK5",
            "https://drive.google.com/uc?export=view&id=1tu2FtHJyfW-qiZrhCL2PRyZEjs0PumRw",
            "https://drive.google.com/uc?export=view&id=1Df7tZvXxcRQjQ5TVXuWQszpT-8HxuA8L",
            "https://drive.google.com/uc?export=view&id=1ezPRRN9A4eRSbYjIUoOb1FmPKnEZdRCp",
            "https://drive.google.com/uc?export=view&id=1ofHk_DPspQ4nK30jzALDn1gA3Tb8i47F",
            "https://drive.google.com/uc?export=view&id=1IULf_NROsBF49HEHhNIk1LNqusOgU71C",
            "https://drive.google.com/uc?export=view&id=13eV8-2jbzyfGOu3UoR8RZw3zY0ARPzJH",
            "https://drive.google.com/uc?export=view&id=1YY-W4GY7Afqa1F2HAMnZY0Fdrf3E3GJj",
            "https://drive.google.com/uc?export=view&id=18UXb3Nz6CzLvY4qVEbn5xBby5uPzxcFL",
            "https://drive.google.com/uc?export=view&id=134BupekX4pvptWbya8aCU3lsSwk5Vbg3",
            "https://drive.google.com/uc?export=view&id=15R1EJ9rx7JJWkWDymtOJ6tKYPE3-C90E",
            "https://drive.google.com/uc?export=view&id=1huZoGxMxeEEglv7naUHzhrhh-zboA3D0",
            "https://drive.google.com/uc?export=view&id=1s5DCQNIFJi_BcnXGmcI8Syfkmp_Udfg5",
            "https://drive.google.com/uc?export=view&id=1CZpyYC1z-PPa7kxhMk7F_dB0qrDv9XZs",
            "https://drive.google.com/uc?export=view&id=1FgmD36zbg6BNUBZALJk_-uo_VVWEVUwd",
            "https://drive.google.com/uc?export=view&id=1Lb7vEYi9FcMzwendriPIETizI4mxclIw",
            "https://drive.google.com/uc?export=view&id=1sd7j3mU15yns28Ur68twEbzXjA2Af2R3",
            "https://drive.google.com/uc?export=view&id=1cdS9Livypyx6cTIdaSTuHMQiBf6NBid2",
            "https://drive.google.com/uc?export=view&id=1AIP73L2iETzkKMr7AidN67VyQrvib-gi",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123340083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya cerdas, keren dan humble",  
                "pesan":"sukses terus bang, semangat ya!!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep . Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini perhatian, cerdas, humble",  
                "pesan":"semoga hidupmu selalu indah kak!!!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadani, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Public speakingnya bagus, keren, cerdas dan memotivasi",  
                "pesan":"tolong ajarin aku public speaking yang bagus bang!!!"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat":"Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Pinter dan aktif",  
                "pesan":"Sehat selalu kakak"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Public speaking bagus, cerdas, dan humble",  
                "pesan":"semangat terus bang, sukses selalu !!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya cerdas, tegas tapi lucu",  
                "pesan":"semoga segala urusannya dipermudah ya bang, goodluck!!!"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@notfall.s",
                "kesan": "abangnya kalem, pendiem, cerdas",  
                "pesan":"semangat dan bahagia selalu ya bang !!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak ini positive vibes dan kalem",  
                "pesan": "terus sebarkan energi positif ya kak !!!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main musik",
                "sosmed": "@marletacornelia",
                "kesan": "kakaknya mirip bu lindaa, cantik, ramah",  
                "pesan":"sukses selalu ya kak !!!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, Bandar lampung",
                "hobbi": "Mendengar musik",
                "sosmed": "@keyashafi_",
                "kesan": "abangnya kalem, pendiem, positive vibes",  
                "pesan":"semangat dan bahagia selalu ya bang!!!"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak ini baik hati, ramah, dan perhatian",  
                "pesan":"semangat menjalani harinya ya kak!!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "kakaknya ramah, baik hati",  
                "pesan":"semangat ya kakak kuliahnya !!!"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kakaknya lucu, baik hati, murah senyum",  
                "pesan":"kakak lucu sekalii, semangat terus kak !!!"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakak ini positive vibes, dan anggun",  
                "pesan":"suka banget sama vibes kakak, adem banget  !!!"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kakak ini ramah, humble, perhatian",  
                "pesan":"sukses terus ya kak, semangat!!!"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan":"abangnya kalem, baik hati, dan cerdas",  
                "pesan":"sukses selalu bang, semoga segalanya dipermudah!!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini baik, ramah, seru ",  
                "pesan":"semoga kakak bahagia dan semangat selalu !!!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@biyokcb",
                "kesan": "abangnya asik, ramah, lucu, cerdas",  
                "pesan":"sukses dan semangat selalu ya bang, goodluck!!!"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123440104",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya cerdas, pinter, kalem",  
                "pesan":"sukses selalu bang, semoga makin berprestasi !!!"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakak ini kalem, lucu, ramah",  
                "pesan":"semangat kuliahnya ya kakak !!!"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123440102",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini kalem, baik, ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "abang ini kalem, pendiem, jarang bicara",  
                "pesan":"semoga bahagia selalu bang!!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()
elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KUOFRw6vv3ur-vmv79xCOdxim80N80wx", #Arafi Ramadhan Maulana
            "https://drive.google.com/uc?export=view&id=14wo3H0DrTM8jfreejiAXLOn42Z9UTgcZ", #Yohana Manik
            "https://drive.google.com/uc?export=view&id=1BIVOiJJnM8w96eTR78tDt5mWBdAi9T9P", #Ratu Keisha Jasmine Deanova
            "https://drive.google.com/uc?export=view&id=1m_E57NOtfdBOxYUTLy6hef2Yaj4uqB2W", #Arini Puteri Elandra
            "https://drive.google.com/uc?export=view&id=1mlAmHYJ6q3LHImzMAPX-HRQo_iPVTRiG", #Arya Muda Siregar
            "https://drive.google.com/uc?export=view&id=1XqsTZvkyGFVgZ_LECF7OQqGOKBgFXsog", #Khoirul Muttoharoh
            "https://drive.google.com/uc?export=view&id=1AZA2A1YvofWmwGrFJppJs6aRnILXg8L4", #Lutfia Aisyah Putri
            "https://drive.google.com/uc?export=view&id=1DPwYHeI-n6AXiWRPXGr3E6Pso01bnjD0", #Nabyla Sharfina
            "https://drive.google.com/uc?export=view&id=1IQZTNxkMNaMcZ2RAw8PCRrzxFZyvR8VE", #Syahrialdi Rachim Akbar
            "https://drive.google.com/uc?export=view&id=1rVDV6bJkjbDoCi4S84VLxgwkuNAzMFUa", #Dea Mutia Risani
            "https://drive.google.com/uc?export=view&id=1N9ZawAmOAo4Os3n68u03dUu8MIfBanbe", #Cindy Laura Manik
            "https://drive.google.com/uc?export=view&id=1W3Jggv9oSb0i43w08O2SSJNEKf3YspcK", #Dea Amanda
            "https://drive.google.com/uc?export=view&id=1x9t_7oDG6_cjHNEUsNB673vvEKxpvvWN", #Desman Velius Halawa
            "https://drive.google.com/uc?export=view&id=1dV7urLBohuYdfRPHTKnw5U-sqlhcSQYI", #Devyna Sonya Palupi Sanjaya
            "https://drive.google.com/uc?export=view&id=18nz9WghzIAyrrZB1W0TsQ_oThVUs4A08", #Luthfia Laila Ramadhani
            "https://drive.google.com/uc?export=view&id=1f-89S-dVeiajDgJKzxUgGooFacP3lkzH", #Irvan Alfaritzi
            "https://drive.google.com/uc?export=view&id=1jwyZ94GPsqdri_eNdfJQ8YFGtDCDNDIk", #Aditya Taufiqurrohman
            "https://drive.google.com/uc?export=view&id=1IM5WdNpjbsw0-QnIp2hku9W5KmLCaWZP", #Fathya Intami Gusda
            "https://drive.google.com/uc?export=view&id=1zyMtCkyjQBYFY3lG66Dm3jR-mAfaWLaW", #Khazanatil Ilmi
            "https://drive.google.com/uc?export=view&id=1FZxBm7j7-_BNfrKt6eYXN1QKVUkb1_OA", #Melinza Nabila
            "https://drive.google.com/uc?export=view&id=1DQoolBob6w7k-fqZNLVMwwa4vG7eAZ5J", #Nayla Shafira Roza
            "https://drive.google.com/uc?export=view&id=1BXh5zDsQuKTrHk6kZEDBTSI4_c5snzak", #Nurul Izzah Istiqomah
            "https://drive.google.com/uc?export=view&id=10fnsxyXjv5e4uh8IFkMoGQVSMAdc3k39", #Qois Olifio
            "https://drive.google.com/uc?export=view&id=14QIlilAPwgxSp4GIlqQdb8TxceSYkGb0", #Tarisya hidayatul rahmi
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "abangnya ramah, tegas, dan baik",  
                "pesan":"sukses selalu bang, semangat !!!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini asik, ramah dan baik",  
                "pesan":"semangat dan bahagia selalu ya kak !!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini baik, ramah dan positive vibes",  
                "pesan":"terus sebarkan energi positifmu kak, semangat !!!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini ramah, tegas dan tinggi cantik",  
                "pesan":"semangat jalani harinya kak !!!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "abangnya baik, lucu dan ramah",  
                "pesan":"semoga lancar selalu, semangat !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak ini positive vibes, ramah",  
                "pesan":"semangat dan lancar terus kak !!!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak ini lucu, asik, random",  
                "pesan":"semoga dipermudah segala urusan ya kak !!!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini baik hati, ramah, cerdas dan murah senyum",
                "pesan":"kakak cantik dan positive vibes banget !!!"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "abang ini asik, ramah, perhatian",  
                "pesan":"semangat menjalani kuliahnya bang, lancar selalu ya !!!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini asik, ramah dan baik",  
                "pesan":"semangat terus ya kakak !!!"# 1
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
                "kesan": "abang ini baik, ramah, tegas, perhatian",  
                "pesan":"semangat terus kuliahnya bang!!!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak ini asik, ramah, baik, aktif",  
                "pesan":"semangat dan bahagia selalu kak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl.Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini asik banget, ramah, selalu ceria",  
                "pesan":"semoga kakak bahagia dan lancar selalu ya !!!"# 1
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
                "kesan": "Abang ini baik, asik, ramah, suka bercanda",  
                "pesan":"semangat dan lancar selalu ya bang !!!"# 1
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
                "kesan": "Kakak ini cantik, ramah, lemah lembut",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
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
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()
elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qcH8kLzT-iFC3SA-yH71cRXYNBWn0cVY", #Rani Puspita sari
            "https://drive.google.com/uc?export=view&id=1YxTXVVtEOq6c5PFkLxf4RPsocA3ND48N", #Renta Siahaan
            "https://drive.google.com/uc?export=view&id=1kTubYYUVaOUOjqUdjwhNDvh08nSnpdGw", #Salwa Farhanatussaidah
            "https://drive.google.com/uc?export=view&id=1UEZTsHznF9R1oYAhzqA4Oi2BIox3mziC", #Azzahra Putri Kamilah
            "https://drive.google.com/uc?export=view&id=1olzGITzFGiq6PkMsn88f1KwRO70ax4P8", #Haikal Fransisko Simbolon
            "https://drive.google.com/uc?export=view&id=1jTuP60HJZ6y4OaN5AInIhh_oCU4GHmPM", #Iqfina Haula Halika
            "https://drive.google.com/uc?export=view&id=1WP5Hngx2sF0ZCe3fUA9DXoOqPgUd1F0H", #May Talitha Dahlia
            "https://drive.google.com/uc?export=view&id=1bfe7SA2idxO41Yxgrab6xig7GjAiJKLe", #Muhammad Naufal Alghani
            "https://drive.google.com/uc?export=view&id=1nPnrMLLIYR1116FRdjPI5Qtgw6eMh2c5", #Zailani Satria
            "https://drive.google.com/uc?export=view&id=17T6oWyDD8cs-1eOYbbGIn1v4VNrTcw_I", #Rendi Alexander Hutagalung
            "https://drive.google.com/uc?export=view&id=1-iMFAhtkibIXqd8hDVN9BCt2_CJOK1Lo", #Hanna Gresia Sinaga
            "https://drive.google.com/uc?export=view&id=1si8O_ydBJCOf9GCHCFqk3OcdLKPRSWR0", #Keren Marito Lumban Gaol
            "https://drive.google.com/uc?export=view&id=1Lo-zw9rwVL_4ANX1PDTA4q0CW9WjHmGz", #Muhammad Hanif Dzaky Arifin
            "https://drive.google.com/uc?export=view&id=1iaQXdb3PIXj2U4U2qXXWCKE8c27_rhSU", #Sarah Wasti
            "https://drive.google.com/uc?export=view&id=1OigExG5Lk3_i0RDINb1PFFXfEEH81B3U", #Zahra Putri Salsabilla
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
                "kesan": "stylenya keren, skena abiss",  
                "pesan":"semangat dan sukses selalu ya kakak skenaa"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat":"Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "keren, kalem, ramah",  
                "pesan":"semoga segala urusannya dipermudah ya kak"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": " 122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat":"Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakak ini pendiem, kalem",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat":"Gerbang Barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Kakak ini asik, positive vibes banget",  
                "pesan":"vibes kakaknya adem banget"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan",
                "alamat":"Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "ramah, tegas, asik, jago main musik",  
                "pesan":"semangat dan sukses selalu ya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat":"Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini asik, lucu, ramah",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": " 123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat":"Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak ini tegas, seru, ramah",  
                "pesan":"semoga kakak bahagia selalu ya"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": " 123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat":"Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": " @muhammadnaufalalghani73",
                "kesan": "abang ini lucu dan kocak",  
                "pesan":"semangat dan lucu selalu ya"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": " 123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat":"Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "abang ini asik, ramah",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Rendy Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat":"Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "abang ini soft spoken banget dan positive vibes",  
                "pesan":"semangat terus bang, terus sebarkan energi posiitif"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": " 123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat":"Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak ini asik banget, heboh dan ramai, bisa menjai penyair suasana",  
                "pesan":"semangat kuliahnya kakak, semoga sehat dan bahagia selalu "# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": " 123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat":"Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Kakak ini asik, ramah, perhatian",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat":"Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Abang ini baik, kalem",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": " 123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat":"Tanjung Seneng",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Kakak ini kalem dan pendiem",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat":"Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak ini lucu dan positive vibes",  
                "pesan":"semangat terus kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Xrj-XOH52uhaR5LPMNSZlmuiz8vDh6LF", #Danang Hilal Kurniawan
            "https://drive.google.com/uc?export=view&id=1TEq_NOtHC1iLWaxHLkhLVybC7r6i21vA", #Syalaisha Andina Putriansyah
            "https://drive.google.com/uc?export=view&id=1XAmM4JkF1YrBfqnhEDnCehRAlmRnnPqe", #Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=1P9PvP02aB9P7SZL-7ioBOge7xJNxJC1d", #Anadia Carana
            "https://drive.google.com/uc?export=view&id=1OtJ85ltLu42BkBox0VVuKjffs-LaTL39", #Aprilia Dewi Hutapea
            "https://drive.google.com/uc?export=view&id=1x2N2z1IpZQdr4azz0eOyHuBA0D-HXFCn", #Nabila Zakiyah Zahra
            "https://drive.google.com/uc?export=view&id=13Y9Df9W8sOYyLQpGToG8HoUMP24m9Wn7", #Dhafin Razaqa Luthfi
            "https://drive.google.com/uc?export=view&id=1PgF9SkwGTKuFLiHCycjNhj04Q9Rl4_fv", #Devi Rahayu
            "https://drive.google.com/uc?export=view&id=19cmKL90K5REukuaOF3S59Rs3P9VqSA_R", #Enggli Rahmadhani
            "https://drive.google.com/uc?export=view&id=1HMvCnguKk8U9HVyZ2hPUge-HPnwVB3QH", #Hanifah Inaya Sani
            "https://drive.google.com/uc?export=view&id=1V09alEH-h87o-BnTnMf_hRcf2EAzgQkA", #Nydia Manda Putri
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
                "kesan": "abangnya cerdas, berprestasi, aktif banget",  
                "pesan":"semangat dan berprestasi selalu ya bang!!!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini positive vibes, kalem, manis",  
                "pesan":"terus sebarkan energi positifmu ya kak!!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "Beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "abang ini kalem, pendiem dan wangi",  
                "pesan":"semangat dan sukses selalu bang!!!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik, humble, murah senyum",  
                "pesan":"semangat menjalani harinya kak !!!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini lucu, kalem",  
                "pesan":"semangat terus kuliahnya kak !!!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak ini asik, humble, periang",  
                "pesan":"semangat dan bahagia selalu kak !!!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abang ini kalem dan pendiem",
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
                "kesan": "Kakak ini ramah, kalem dan pendiem",  
                "pesan":"sehat dan sukses selalu kak!!!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. perwira 2",
                "hobbi": "Menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "semoga lancar selalu urusannya kak",
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
                "kesan": "Kakak ini asik, cantik, baik, pintar berbisnis",  
                "pesan":"semangat dan sukses selalu ya kakak cantik!!!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()
elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yp6JD4XYR30bEqPHA7WuprBp23USieh8", #Patricia Leondrea Diajeng Putri
            "https://drive.google.com/uc?export=view&id=14HOr2ZXw5c80eIqPOoCxtguG0He65VK7", #Rahma Neliyana
            "https://drive.google.com/uc?export=view&id=1y6C_EZ3xgnIVsOvpD9p5ZlreiTISoff4", #Khoirul Anam
            "https://drive.google.com/uc?export=view&id=1XU6skXVG8BWd6DBeQEbZILqp5Efm5LZI", #Labo John Noel Napitupulu
            "https://drive.google.com/uc?export=view&id=1uPrTRV5uwLLH3vOXR5K71uddobK17Tt1", #Rafi Diva Efangga
            "https://drive.google.com/uc?export=view&id=1Ye6bB_wpHFMqVqdnlKz5jxJ6WfqHkkkc", #Refa Destiny Pranata
            "https://drive.google.com/uc?export=view&id=1fl5y4pCNbt_EW8zW85JojFyYvUO7p53w", #Try Yani Rizki Nur Rohmah
            "https://drive.google.com/uc?export=view&id=13AEvXeUZ51pxvlOMro3_bIVmS7x6Nmk3", #Aliya Ammara Ananta
            "https://drive.google.com/uc?export=view&id=11wgCQ0jsZmuJBPtFgreyB06Fk_DyYJUv", #Donna Maya Puspita
            "https://drive.google.com/uc?export=view&id=1J_3JDHxu7vw6BHOsAzvaRkZB_-0wuxCG", #Feby Angelina
            "https://drive.google.com/uc?export=view&id=16YWtxVfvVLn18sC3S6VY8g4J2VzS8JRN", #Hafsa Fazila Arradhi
            "https://drive.google.com/uc?export=view&id=1RDo7W-XfV9Z-RYuwbdLxBrQxzwDWbzLJ", #Nayla Salsabila Fathianisa
            "https://drive.google.com/uc?export=view&id=", #Sania Dwi Ayu Lestari
            "https://drive.google.com/uc?export=view&id=1GvwChImQWXh2nLsgU3xGbtOzgLw9pe6U", #Akmal Faiz Abdillah
            "https://drive.google.com/uc?export=view&id=1qukdzG96nt6Xqkl3CqVfJjOOqiH4gpJ-", #Raihana Adelia Putri
            "https://drive.google.com/uc?export=view&id=1dxDUMdlZj5nub0mW-Gg2LE2PgKpD4BY3", #Citra Agustin
            "https://drive.google.com/uc?export=view&id=1J9a2rlMivr4wWNSTTnf8mWfzd25fid3w", #Eigi Artamevia
            "https://drive.google.com/uc?export=view&id=1i5QV0IzaS7P-u_Mh1QxDcnkWbzjM-9e7", #Romauli Oktavia Silaban
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
                "kesan": "Kakak ini baik hati, cantik, ramah, murah senyum, selalu ceria",  
                "pesan":"vibes kakaknya positif banget, kalau deket kakak bawaannya happy !!!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "jl. Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini asik, baik hati, ramah",  
                "pesan":"semangat dan lancar terus ya kak !!!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "Kakak ini kalem, pendiem, baik",  
                "pesan":"semangat kuliahnya bang, semog sukses selalu !!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "abangnya asik dan chill banget, ramah",  
                "pesan":"semoga bahagia selalu bang, semangat !!!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Kabangnya baik hati, asik, ramah, perhatian",  
                "pesan":"semangat dan lancar selalu ya bang!!!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "kakaknya baik hati, kalem",  
                "pesan":"semangat kuliahnya kakk!!!"# 1
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
                "kesan": "Kakaknya positive vibes, cerdas, penjelasannya mudah dipahami",  
                "pesan":"semoga dipermudah segala urusannya kak !!!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini baik hati, asik, ramah",  
                "pesan":"semangat kuliahnya kak !!!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labukan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak ini kalem, lucu, dan ramah",  
                "pesan":"semangat dan lancar kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumbar",
                "alamat": "jl.Lapas, kec.Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakak ini asik, baik dan ramah",  
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
                "kesan": "Kakak ini cantik, baik dan tegas",  
                "pesan":"semoga bahagia selalu kak, semangat!!!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "abang ini kalem, ramah",  
                "pesan":"semangat dan lancar terus ya bang!!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak ",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini ramah, dan lucu",  
                "pesan":"semangat terus ya kakak !!!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kakak ini kalem, baik dan ramah",  
                "pesan":"semangat terus kak!!!"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakak ini baik, ramah, lemah lembut, lucu",  
                "pesan":"semoga kakak bahagia selalu, semangat kakk!!!"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini ramah, stylish",  
                "pesan":"semangat dan lancar terus urusannya ya kak!!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan

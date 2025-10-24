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
            "https://drive.google.com/uc?export=view&id=1b4JhMNu3Zyu6383g5CgOEtPlQj5Bbt7x", #bang rendra
            "https://drive.google.com/uc?export=view&id=1zQiFPyvJEeA4Q5CO85FvlrClEMwLb4bo", # bang johannes
            "https://drive.google.com/uc?export=view&id=1SJM6A8WNOfWz9aj_W1kCQQPpLbS2-dcv", # kak elisabeth
            "https://drive.google.com/uc?export=view&id=1nD-pcs-BlEjQ7dxWGNAaSoy7adRl9fRn", # kak syadza
            "https://drive.google.com/uc?export=view&id=1Pl3LirI44_xw3fTsrF8qHsqfsFRWkmGF", # kak eksanty
        ]
        data_list = [
           {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Inspiratif, keren, dan berjiwa pemimpin",  
                "pesan":"Wish you all the greatest bang!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya keliatan asik bangett",  
                "pesan":"semoga lancar terus kuliahnya ya bang!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy dalem",
                "alamat": "Airest Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh",
                "kesan": "Kakanya lucu dan asik bener",  
                "pesan":"I hope everything's great will come to your life kaa"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Ramah dan selalu ngasih vibes positif",  
                "pesan":"Semangat selalu ya kaakkkk"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "vibes kakaknya cool betul",  
                "pesan":"Semoga semua hal baik terus ngikutin kakak!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumbar",
                "alamat": "Gya Kost Korpri",
                "hobbi": "Cute Jenderal",
                "sosmed": "@farahanumafifah",
                "kesan": "kakanya cantik dan easy-going sekali!",  
                "pesan":"Semoga semua hal baik mengikuti kakak dimanapun kakak beradaa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
         gambar_urls = [
             "https://drive.google.com/uc?export=view&id=1NbwgauoR54c36umgFQSYwZuj-F249n5d",#bang jeremia
             "https://drive.google.com/uc?export=view&id=1SoyES7Vp5veCn-VNWNLHnEKu1XWlchyj",#kak dhea
             "https://drive.google.com/uc?export=view&id=1EZmz6gPVnjmmhZTZLVlfy7la_JnVCgns",#kak renisha
             "https://drive.google.com/uc?export=view&id=1c32InZOhxhGRneQmOItYYNI08wH5kRWq",#kak anisa fitriani
             "https://drive.google.com/uc?export=view&id=1tMjXi3gtAAgeQHAWLsvCXvuw7MHpJUA2",#bang dharu
             "https://drive.google.com/uc?export=view&id=1SEOR3p-UtLLE6O2WysAj70oCro351Pl-",#kak feby
             "https://drive.google.com/uc?export=view&id=16DPU22eL9GlgZc74eQPKmN9UK_gNTzqe",#bang givaro
             "https://drive.google.com/uc?export=view&id=1eGdccQamCImOv52eXnlWKmXG1mSZmo8h",#bang mirzan
             "https://drive.google.com/uc?export=view&id=1r7u-xV12F4FMdnruc4Pi5q-zPSMs4hGn",#kak berliana
             "https://drive.google.com/uc?export=view&id=1aK4J2xc0hh9v4K8BudmUuqLusMv9v6on",#kak juesi apridelia
             "https://drive.google.com/uc?export=view&id=1WvUihyfsaicbyblCyVheLmymP5K4uUNj",#bang ridho benedictus
             "https://drive.google.com/uc?export=view&id=16GFvj8GqM1eDY5ADME97KvwPipQvd4W3",#bang feryadi yulius
             "https://drive.google.com/uc?export=view&id=11m89S_gCzcc-oH3lIj47C1S3CIE2d4JG",#kak monica patricia
             "https://drive.google.com/uc?export=view&id=1bktd5WVue_Oh8GIC5RIC8xHyu1RKA1NW",#kak wan nashwa
         ]
         data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450000",
                "umur": "18",
                "asal":"Nusa Kambangan",
                "alamat": "lapas, Belwis",
                "hobbi": "Melarikan diri",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya periang banget! seru lagiii!!!",  
                "pesan":"May everything's great came to your path bang!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "lomba ga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya positive vibes sekali",  
                "pesan":"semangat terus kuliahnya kakk"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "kakanya kerennn",  
                "pesan":"Semoga kakak bahagia selalu!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Ubud",
                "alamat": "Bandar Lampung",
                "hobbi": "mencari kesibukan baru",
                "sosmed": "@ansftynn_",
                "kesan": "kakanya cool bet !",  
                "pesan":"Semangat terus kuliahnya ya kaa"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "122450023",
                "umur": "18",
                "asal":"Balam",
                "alamat": "way halim",
                "hobbi": "Nonton live Putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "abangnya lucu banget dan super friendly!!",  
                "pesan":"may goodness always be with you bangg"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "122450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak Sawah",
                "sosmed": "@fby_wlndr",
                "kesan": "Kakaknya super kawaii!",  
                "pesan":"Semangat selalu ya kaa"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "122450078",
                "umur": "20",
                "asal":"lambar",
                "alamat": "Sukabumi",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "kakanya keren banget !",  
                "pesan":"be happy as always ya banggg"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerawat Kucing",
                "sosmed": "@myyrinn",
                "kesan": "Kakanya cool",  
                "pesan":"May wellness be with you sebagai sesama pecinta kucing kakk"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya positive vibes sekali dan canti bangett",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "122450085",
                "umur": "19",
                "asal":"Sumut",
                "alamat": "Belwis",
                "hobbi": "Lupa balas chat",
                "sosmed": "@j_essie",
                "kesan": "kakanya canti bangett dan ramah sekali!",  
                "pesan":"semoga kuliahnya lancar terus ya kakk"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "122450000",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "main pedel",
                "sosmed": "@iamridhomanik",
                "kesan": "Kakanya asik banget dan seru jugaa",  
                "pesan":"Wish you always be happy bangg"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi batch google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "vibes abangnya tegas dan cool",  
                "pesan":"Semoga selalu bahagia dan sukses ke depannya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@monica_tjg",
                "kesan": "kaka keliatan positif sekalii",  
                "pesan":"semoga tetap semangat selalu ya kakk"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Farakan",
                "hobbi": "nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "terlihat tenang dan hepi",  
                "pesan":"Semoga terus berprestasi kakk"# 1
            },
         ]
         display_images_with_data(gambar_urls, data_list)
         Baleg()

if menu == "Senator":
    def Senator():
         gambar_urls = [
             "https://drive.google.com/uc?export=view&id=1PybOF7fo2v5InsKqRArHMDmZHRUZL2yC", #bang bintang
             "https://drive.google.com/uc?export=view&id=1cCPOYioianS6ao9XUNqjv-ZtyhmY_eLz", #kak nadya
             "https://drive.google.com/uc?export=view&id=1PQpkK44Rtv9lXrwW3-XD1cQO3Pyoch5L", #kak fathinah
             "https://drive.google.com/uc?export=view&id=1uPL5w6slTl4S35AIj8l66Ir0eDa8WBQw", #kak lia
             ]
         data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Dengar lagu, nyanyi, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang rendra vibesnya kok kaya sal priadi ya...",  
                "pesan":"Semoga semua urusan perkuliahannya dilancarkan bangg"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@nadyaanjaani",
                "kesan": "ka nadya positive vibes banget!",  
                "pesan":"Sukses selalu kedepannya kakk"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main ice skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakanya keliatan sweet banget ",  
                "pesan":"kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomart Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya keliatan kalem tapi anggun yaa",  
                "pesan":"Semangat selalu kuliahnya ya kaaa"# 1
            },
        ]
    display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id= ", #bang randa
            "https://drive.google.com/uc?export=view&id= ", #rut
            "https://drive.google.com/uc?export=view&id= ", #regi
            "https://drive.google.com/uc?export=view&id= ", #aisyah
            "https://drive.google.com/uc?export=view&id= ", #fadil
            "https://drive.google.com/uc?export=view&id= ", #aqil
            "https://drive.google.com/uc?export=view&id= ", #naufal
            "https://drive.google.com/uc?export=view&id= ", #nadia
            "https://drive.google.com/uc?export=view&id= ", #marleta
            "https://drive.google.com/uc?export=view&id= ", #akeyla
            "https://drive.google.com/uc?export=view&id= ", #anggi
            "https://drive.google.com/uc?export=view&id= ", #efi
            "https://drive.google.com/uc?export=view&id= ", #fabiolla
            "https://drive.google.com/uc?export=view&id= ", #fairuz
            "https://drive.google.com/uc?export=view&id= ", #tanty
            "https://drive.google.com/uc?export=view&id= ", #eggi
            "https://drive.google.com/uc?export=view&id= ", #afifah
            "https://drive.google.com/uc?export=view&id= ", #fabio
            "https://drive.google.com/uc?export=view&id= ", #giofani
            "https://drive.google.com/uc?export=view&id= ", #rahma
            "https://drive.google.com/uc?export=view&id= ", #rahmah
            "https://drive.google.com/uc?export=view&id= ", #razin
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "1222450083",
                "umur": "22",
                "asal":"Serang,Baten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berenang",
                "sosmed": "@randaandriana_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234500119",
                "umur": "20",
                "asal":"Pramuka, Bandar Lampung",
                "alamat": "Perum Bukit Alam Permai 3, Blokk C, No.9",
                "hobbi": "Dengrin musik",
                "sosmed": "@keyashafi_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bummisari Kec.Natar",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Sale, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "-",  
                "pesan":"", # 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":"", # 1
            },
             {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang (main game)",
                "sosmed": "@fifah.zy",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer),tidur,jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@giofaniars_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "",  
                "pesan":"", # 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450102",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans Sakum,Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "",  
                "pesan":"", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",#arafi
            "https://drive.google.com/uc?export=view&id=",#yohana
            "https://drive.google.com/uc?export=view&id=",#ratu
            "https://drive.google.com/uc?export=view&id=",#arini
            "https://drive.google.com/uc?export=view&id=",#arya muda
            "https://drive.google.com/uc?export=view&id=",#khoirul
            "https://drive.google.com/uc?export=view&id=",#lutfia
            "https://drive.google.com/uc?export=view&id=",#nabyla
            "https://drive.google.com/uc?export=view&id=",#syahrialdi
            "https://drive.google.com/uc?export=view&id=",#dea mutia
            "https://drive.google.com/uc?export=view&id=",#cindy
            "https://drive.google.com/uc?export=view&id=",#dea amanda
            "https://drive.google.com/uc?export=view&id=",#desman
            "https://drive.google.com/uc?export=view&id=",#devyna
            "https://drive.google.com/uc?export=view&id=",#luthfia
            "https://drive.google.com/uc?export=view&id=",#irvan
            "https://drive.google.com/uc?export=view&id=",#aditya
            "https://drive.google.com/uc?export=view&id=",#fathya
            "https://drive.google.com/uc?export=view&id=",#khazanatill
            "https://drive.google.com/uc?export=view&id=",#melinza
            "https://drive.google.com/uc?export=view&id=",#nayla
            "https://drive.google.com/uc?export=view&id=",#nurul izzah
            "https://drive.google.com/uc?export=view&id=",#qoiz
            "https://drive.google.com/uc?export=view&id=",#tarisya

        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Warjo",
                "hobbi": "Makan Warjo",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Desman Velius Halaws",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
         gambar_urls = [
             "https://drive.google.com/uc?export=view&id=1Kky8LR7kjygZxDJrV9yhrD6fcM4_KiRA", # kak rani
             "https://drive.google.com/uc?export=view&id=", # Kak renta
             "https://drive.google.com/uc?export=view&id=1OikB9JxgOVlh2Ji_lFCZpeLYoPvs-qI9", # kak salwa
             "https://drive.google.com/uc?export=view&id=1PWEi5yLfM5oUNHntIENQca8eBpn0vO16", # kak azzahra putri
             "https://drive.google.com/uc?export=view&id=1ksHWESJwLLBe1NXPraz8CzZwZYXyICYc", # bang haikal
             "https://drive.google.com/uc?export=view&id=1Ku7jV47F-UHi78c5MWPxnj3clDDpALSj", # bang naufal afghani
             "https://drive.google.com/uc?export=view&id=18F0IKJBtLu7m1y9qv9GAdfWvuPWlqLJd", # kak iqfina haula
             "https://drive.google.com/uc?export=view&id=1UsDmS4nOrdEW3sz_GR4Jbr_XGwtr0IB2", # kak may talitha
             "https://drive.google.com/uc?export=view&id=1E_WLYxs9_JkYsgBSBhUQrnJAVaO2xd0I", # bang zailani satria
             "https://drive.google.com/uc?export=view&id=123FhoN6J2P8FkyfdW1YVSeTudbagV1DZ", # hanna gresia
             "https://drive.google.com/uc?export=view&id=14likRIYYAb34Dq5kDh3dGsPdQKPKoGYE", # kak keren marito
             "https://drive.google.com/uc?export=view&id=16DQMW3NZUq5qhta6fvnwkeCCKsCdD7F9", # kak sarah wasti
             "https://drive.google.com/uc?export=view&id=1wK5KJ5jNwDF0LRFsPRFsOCkZoJrMZEDw", # kak zahra putri
             "https://drive.google.com/uc?export=view&id=1vl8LR_JAG5PGvkQ5RYH9Hb7RJWsZy79-", # bang Hanif Dzaky
         ]
         data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "12245030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya asik banget, gampang diajak ngobrol!",  
                "pesan":"Semoga makin sukses dan jangan lupa main ke kampus ya, Kak!",
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya punya aura positif yang nular banget",  
                "pesan":"Makasih udah selalu semangatin kita waktu susah nugas!"# 1
            },
            {
                "nama": "Salwa Farhanatusaiidah",
                "nim": "12245055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya humble banget, nggak jaim sama sekali!",  
                "pesan":"Semoga selalu bahagia dan sukses di dunia kerja nanti kakk!!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azza.raaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "Jangan bosan bagi-bagi ilmu ke junior ya, Kak!"# 1
            },
              {
                "nama": "Rendi Alezander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@lexanderr",
                "kesan": "Bangnya keren dan inspiratif banget!",  
                "pesan":"Terus jadi contoh baik buat generasi selanjutnya ya!"# 1
            },
            {
                "nama": "Haikal fransisko Simbolon",
                "nim": "122450106",
                "umur": "18",
                "asal":"Tulang Bawang",
                "alamat": "Sukabumi",
                "hobbi": "Membersihkan rumah",
                "sosmed": "@haikalsbln",
                "kesan": "Bangnya lucu tapi tetep keren, paket lengkap pokoknya",  
                "pesan": "Sukses terus dan semoga kariernya lancar!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450076",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya ceria dan bikin suasana jadi hidup!",  
                "pesan":"semangat selalu kuliahnya kakk"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450009",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Naufal Afghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@Muhammadnaufalafghani73",
                "kesan": "abanngnya kalem bangettt",  
                "pesan":"semngat terus kuliahnya bangg"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Bangnya bijak banget, ngomongnya selalu menenangkan",  
                "pesan":"Semoga selalu diberi kesehatan dan rezeki yang lancar, Bang"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kak hana lucuu banget!",  
                "pesan":"stay positive as always ya kakkk"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerenmrtv",
                "kesan": "kakaknya keren kaya namanya!!",  
                "pesan":"semangat terus kuliahnya ya kakk"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hifzky",
                "kesan": "Bangnya punya semangat yang luar biasa",  
                "pesan":"Sukses terus dan semoga kariernya lancar ya bangg!"# 1
            },
            {
                "nama": "Sarah wasti",
                "nim": "122450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya pinter banget, tapi tetep down to earth!",  
                "pesan":"Jangan bosan bagi-bagi ilmu ke junior ya, Kak!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "Main Rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kakaknya vibes-nya tenang banget, adem kalau ngobrol",  
                "pesan":"Semoga selalu dikelilingi hal-hal baik ya kak!"# 1
            },
        ]
         display_images_with_data(gambar_urls, data_list)
         Departemen_Internal()

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=", #Danang
            "https://drive.google.com/uc?export=view&id=", #Syalaisha
            "https://drive.google.com/uc?export=view&id=", #Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=", #Anadia
            "https://drive.google.com/uc?export=view&id=", #Aprilia
            "https://drive.google.com/uc?export=view&id=", #Nabila
            "https://drive.google.com/uc?export=view&id=", #Dhafin
            "https://drive.google.com/uc?export=view&id=", #Devi
            "https://drive.google.com/uc?export=view&id=", #Enggli
            "https://drive.google.com/uc?export=view&id=", #Naya
            "https://drive.google.com/uc?export=view&id=", #Nydia
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Balam",
                "alamat": "Belakang PB",
                "hobbi": "Joging",
                "sosmed": "@dananghk_",
                "kesan": "Bang Danang seru banget diajak ngobrol, banyak hal baru yang saya dapat",  
                "pesan":"Terus berkarya ya bang dan semangat kuliahnya!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450012",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya lembut dan punya aura yang menenangkan",  
                "pesan":"Terus semangat kak!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki_",
                "kesan": "fashionable banget abangnya!",  
                "pesan":"Sehat dan bahagia selalu bang"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Joging",
                "sosmed": "@anadiacrn_",
                "kesan": "Ka nadia asik banget orangnyaaa",  
                "pesan":"Semangat terus kak kuliahnya!!!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton dramashort di fb",
                "sosmed": "@aphrhtp_",
                "kesan": "kakanya keren banget deh !",  
                "pesan":"Semangat terus kuliahnya kak plus jangan lupa jaga kesehatan!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_azazahra",
                "kesan": "Kak nabila asik benerrr!",  
                "pesan":"Semoga makin sukses selalu kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya kalem kalem ",  
                "pesan":"Tetap semangat dan terus jadi inspirasi bang!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya seru banget!!",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya ya kak!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gang perwira 2",
                "hobbi": "Nonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakaknya cantik dan anggun banget",  
                "pesan":"Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak naya baikkk dan asik banget",  
                "pesan":"Tips bikin risol seenak kemarin dong kak! hehe"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kak nydia asik dan friendly sekali!",  
                "pesan":"Semoga selalu diberi kelancaran dalam tiap langkahnya ya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=", #Patricia
            "https://drive.google.com/uc?export=view&id=", #Nely
            "https://drive.google.com/uc?export=view&id=", #Anam
            "https://drive.google.com/uc?export=view&id=", #Labo
            "https://drive.google.com/uc?export=view&id=", #Rafi
            "https://drive.google.com/uc?export=view&id=", #Refa
            "https://drive.google.com/uc?export=view&id=", #Try Yani
            "https://drive.google.com/uc?export=view&id=", #Aliya
            "https://drive.google.com/uc?export=view&id=", #Donna
            "https://drive.google.com/uc?export=view&id=", #Feby
            "https://drive.google.com/uc?export=view&id=", #Hasfa
            "https://drive.google.com/uc?export=view&id=", #Nayla
            "https://drive.google.com/uc?export=view&id=", #Sania
            "https://drive.google.com/uc?export=view&id=", #Akmal
            "https://drive.google.com/uc?export=view&id=", #Raihana
            "https://drive.google.com/uc?export=view&id=", #Citra
            "https://drive.google.com/uc?export=view&id=", #Eigi
            "https://drive.google.com/uc?export=view&id=", #Roma

        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya Friendly dan asik banget diajak ngobrol!",  
                "pesan":"Semoga selalu kebahagiaan menyertai di setiap langkahnya kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak nelly ramah dan seru banget",  
                "pesan":"Terus semangat kuliahnya dan tetap jadi pribadi yang lembut ya!"# 1
            },
            {
                "nama": "Khoriul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam__",
                "kesan": "Abangnya seru banget",  
                "pesan":"Semangat terus, Bang!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Hui",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya keren banget",  
                "pesan":"Terus berproses ya bang!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Bang Rafi keren bangetttt",  
                "pesan":"Semangat para pejuang PDD !!!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "kakanya baikkk banget",  
                "pesan":"Terus percaya pada diri sendiri ya kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122350020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaa",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Tetap semangat menimba ilmu kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kakaknya positive vibes banget",  
                "pesan":"Terus semangat dan bahagia selalu kak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya lembut dan manis banget",  
                "pesan":"Semoga semua harapan dan cita-citanya tercapai ya kak!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kakaknya lucu banget",  
                "pesan":"Semangat terus kuliah ya kak!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya punya vibes yang ceria!",  
                "pesan":"Semoga bisa ketularan energi positivnya kakaaa"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas, Jati Agung",
                "hobbi": "Dengar musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Ka nayla kalem kalem jugaa orangnya",  
                "pesan":"terus jadi inspirasi buat orang ya kak"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania ramah bangett dan asik diajak bicara",  
                "pesan":"Semoga kaka sukses selaluuu"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "kalem kalem gitu abangnya",  
                "pesan":"Jangan pernah menyerah ya banggg"# 1
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "vibes kakanya kalem seru gituu",  
                "pesan":"semoga selalu semangat mnenjalani hari-harinya kak"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra keren selalu yaaa",  
                "pesan":"Kasih tips jago lukis dong kakk"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah balau residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak eigi ramah, baik, dan cantik banget",  
                "pesan":"Always be happy ya kakk"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Romauli cantik bangettttt",  
                "pesan":"Semoga selalu semangat dan sukses terus kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
# Tambahkan menu lainnya sesuai kebutuhan


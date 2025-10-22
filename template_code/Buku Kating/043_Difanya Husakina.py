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
    st.markdown("""
    <div style="
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #2c3e50;
        background: linear-gradient(90deg, #f8f9fa 0%, #e8e8e8 100%);
        padding: 20px;
        border-radius: 15px;
        width: 90%;
        margin: 60px auto 30px auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        letter-spacing: 0.5px;
    ">
        Anda telah mencapai akhir halaman<br>
        <span style="font-weight:500; font-size:18px; color:#555;">(tidak ada apa-apa disini)</span>
    </div>
""", unsafe_allow_html=True)
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lR5iM3C-cu91XJbKODMIHrW_7-ItsevY",
            "https://drive.google.com/uc?export=view&id=1Xcc1wn8tP_M6tFipQUuFzxUANKDIDwZH",
            "https://drive.google.com/uc?export=view&id=1J1JDTkQ_gdCiTskAE4wjWqsOKKLEsBQI",
            "https://drive.google.com/uc?export=view&id=1Pzpsrgm1-YRlAzluz-BAGjtEyKbCJECU",
            "https://drive.google.com/uc?export=view&id=1V1OoOcepglDtm5i-ooHtzHIJdBZxttYN",
            "https://drive.google.com/uc?export=view&id=1cwsbwUTnmRM2wKcf20TrQKsP8c67hk5l",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_rendraa",
                "kesan": "Bang Rendra keren banget dan berwibawa",  
                "pesan":"semangat terus kuliahnya bang! bahagia terus!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku sql",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Jo lucu dan seru",  
                "pesan":"Sehat selalu bang, semangat terus kejar cita-citanya!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cute Kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya lucu banget dan cantikk",  
                "pesan":"Semangat kuliahnya kakak, bahagia selalu ya kakk!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak baik dan lucuuu",  
                "pesan":"Semangat ya kak jalani hari-harinyaa"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Asrama TB. 4",
                "hobbi": "Nahan eek",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakak lucu banget, asyik jugaa",  
                "pesan":"sehat selalu kakak, be happy yaa kakk!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "21",
                "asal":"Baduy dalam",
                "alamat": "Ayresh kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabeth",
                "kesan": "kak abeth lucuu cantikk",  
                "pesan":"semangat ya kak kuliahnyaa, bahagia selalu kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Fobk4gFjQFMhU5Z4A22qGs5-L_hIFNdT",
            "https://drive.google.com/uc?export=view&id=1GZGqxVtbDwC1gct1N4Q8qgJ2KQEZXn5w",
            "https://drive.google.com/uc?export=view&id=1JKOJE-hdgdn6luSYIiJiehlWP5tLN0Xu",
            "https://drive.google.com/uc?export=view&id=11adzLX32rejzdFWg0TBoMKkrmAANImOO",
            "https://drive.google.com/uc?export=view&id=1dvA9EPLHbTFUFtpb53Pw2FHmcvXCmx87",
            "https://drive.google.com/uc?export=view&id=1Zib4umIP7JltFubm-vj_RvlP00Iio68P",
            "https://drive.google.com/uc?export=view&id=167uZv_kPVsHEhOWcWLGyOaIIXyq5fBTK",
            "https://drive.google.com/uc?export=view&id=1KsUnoswcL34ZSszhu2ZVSVblHb1hmjI_",
            "https://drive.google.com/uc?export=view&id=1HAl8Pf9O6vI4I96YubkbYnFUgqVUVyDE",
            "https://drive.google.com/uc?export=view&id=1160PSdOsvG6J72lolTjT9DlxiKKFIe1R",
            "https://drive.google.com/uc?export=view&id=1umijqisUlEch8W8bGGiRYEfXLQMQ9qHy",
            "https://drive.google.com/uc?export=view&id=1hFPjlWId38qJu0-kNQd1IPRJnRZJJes2",
            "https://drive.google.com/uc?export=view&id=1aJYriypSdXi6fu1XRonURrMjIdIt56YL",
            "https://drive.google.com/uc?export=view&id=16sXhFtMUG6t1KFvm-QXMLnaWXjoDLxlg",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Pilates",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya asik banget, ramah bangett",  
                "pesan":"jangan lupa bahagia bangg, semangat semester 7 nya!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Braga",
                "alamat": "Kedaton",
                "hobbi": "Makan lontong sate",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea lucuu cantikk",  
                "pesan":" keep shining ya kakk!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur, jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "kak Renisha imutt bangettt",  
                "pesan":"keep smiling kakk, senyum kakak lucuu"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Natar",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Masyaallah kak, kakak cantikkk",  
                "pesan":"bahagia selalu kakk, semangat terus kuliahnyaa!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Bang Dharu keren bangett, sangat memotivasi",  
                "pesan":"jangan lupa istirahat ya bangg, semangattt"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kak Feby lucuu, imuttt",  
                "pesan":"be happy ya kakk, jangan lupa semangattt"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin bang mirzan main kucing",
                "sosmed": "@givarooo",
                "kesan": "abang terkece, terkeren, termantep, ter the best",  
                "pesan":"jangan lupa istirahat bang, semangat semester 5 nya"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya baikk, kerenn",  
                "pesan":"kapan kapan spill kucingnya bang"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Catur",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak cantikkk, keren lagii",  
                "pesan":"keep smiling kakk, jangan lupa bahagia dan semangat terus ya kakkk"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandiama",
                "alamat": "Way Huwi",
                "hobbi": "Minum air putih 8x sehari",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya kerenn, ketemu di materi teknik persidangan kakaknya bikin salfokk",  
                "pesan":"semangat terus ya kakk, keep chasing ur dream kakk!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Nyanyi tabola bale",
                "sosmed": "@iamridhomanik",
                "kesan": "abangnnya lucuu",  
                "pesan":"bahagia selalu ya bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Koleksi Stiker",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya kerennn",  
                "pesan":"semangat terus yo bang jalani kuliahnyo"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Papua Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "kakaknya maniss lucuu",  
                "pesan":"be happy kakakk"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "kakaknya cantikk, keren jugaa",  
                "pesan":"keep shining kak, jaga kesehatan ya kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uWTlawbdJ83nx5jitia0Wlo4FrcR0UXn",
            "https://drive.google.com/uc?export=view&id=1wFV6I8E8I3pR1G5pkF4IkOZwSJA_0trn",
            "https://drive.google.com/uc?export=view&id=1WenP1yw4JtrE1_F8a0sUW9VsQjvdf1H8",
            "https://drive.google.com/uc?export=view&id=1FMd8daMk9apLZhA7UJQCbcj-Tx4dQIXj",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Denger lagu, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Rian lucu banget, humoris, keren",  
                "pesan":"Semangat terus bangg, happy terus ya bangg, janlup istirahat bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu, maen roblox",
                "sosmed": "@nadyaanjanani",
                "kesan": "Kak Nadya baikk, cantikk, imuttt",  
                "pesan":"Bahagia selalu kakk, jangan lupa makann, jaga kesehatan dan semangat ya kakk"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Ice Skating",
                "sosmed": "@fathinahazzh",
                "kesan": "Kakaknya seruuu, asyikk",  
                "pesan":"Semangat yaa kakk, jangan lupa bahagia!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya lucuuu, seru jugaaa",  
                "pesan":"keep positive kakk, always happy ya kakkk!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HFbYTeLMKRVO0w3SKdFjLdbXXvOWH98p",
            "https://drive.google.com/uc?export=view&id=1gSoHNq8reNppvYsC7Wg90ezNhAJpuIU4",
            "https://drive.google.com/uc?export=view&id=1X_ckwN3O3t1GRKYycWpCY2sxOisg9Evm",
            "https://drive.google.com/uc?export=view&id=1vOAdQjpkGs-j6Ax0h_f_luDtFT9sARc0",
            "https://drive.google.com/uc?export=view&id=1lEf9YVKynOrw5EDdl5agRQZjnLaHns4v",
            "https://drive.google.com/uc?export=view&id=1loO2Tf3iZCWz1_oT08Mn7JuraZbH8k1v",
            "https://drive.google.com/uc?export=view&id=1oAyKcj5zRYQeNNdTODX00S8Auw7p-JmA",
            "https://drive.google.com/uc?export=view&id=1uYM8_WQ02r9ZI8cIQvpwvTcvy7koU0hj",
            "https://drive.google.com/uc?export=view&id=1x0VDyhcxtHirBLIFNh3XoBWYvvUomVhZ",
            "https://drive.google.com/uc?export=view&id=1j3apO-81VY9Ma93ypw4ZIZnyedC2G9x0",
            "https://drive.google.com/uc?export=view&id=1af4udBWCjnbsWgD6nbMujI7_iBGfeQV4",
            "https://drive.google.com/uc?export=view&id=1NOPagzh1BljEAYV55GPl_R8dsRZdxKMI",
            "https://drive.google.com/uc?export=view&id=1BCAFYof-1g-fT5JgLjebvC0UC-6n4iSU",
            "https://drive.google.com/uc?export=view&id=1nZmdaytLxTdJsQcszcqcEgXdG0wZbsH4",
            "https://drive.google.com/uc?export=view&id=1vSYjaATcCBH95r1dVXqcLueLXWnmU3LH",
            "https://drive.google.com/uc?export=view&id=1sRYtgEslOITV0I0ZTjP2-rE8L3vUDIY-",
            "https://drive.google.com/uc?export=view&id=1u03CCmC79pHooxux_Q6cauXnlLIXPUtx",
            "https://drive.google.com/uc?export=view&id=1pN08m3bnnv0Q5M2pviHrVwZVhe3KJzSC",
            "https://drive.google.com/uc?export=view&id=10PSoCNTJwa4c-EQf7jY23DnstJqyGJo6",
            "https://drive.google.com/uc?export=view&id=1b2rShUKGqmHQPQerOuuUXyCdVWxGjHiH",
            "https://drive.google.com/uc?export=view&id=1jVaCshyGZoa6IvgbDZnHNyg7NTcLvVGb",
            "https://drive.google.com/uc?export=view&id=1t1Q18360iYlGQRgpmBlOfN-mCWz_oy3r",
            "https://drive.google.com/uc?export=view&id=1WtGKV4TzZrMwYGMm2KNqyVsvYDVE-wcn",
            "https://drive.google.com/uc?export=view&id=1j_fqjiIL_PeAUxEjjE79AEyFXi5tfl9c",
            "https://drive.google.com/uc?export=view&id=1hZy9iZp2-HGPRFRQnbwcnqjauI_2M3se",
            "https://drive.google.com/uc?export=view&id=1uWTlawbdJ83nx5jitia0Wlo4FrcR0UXn",
            
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ferdy_kevin",
                "kesan": "Bang Kevin keren, berwibawa",  
                "pesan":"Semangat semester 7 nya bang, good luck for your bright future bang!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Afifah cantikk, keren jugaa",  
                "pesan":"Be happy always kakakk, jangan lupa istirahat!!!"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kak Allya keren, hebat bangett, dan jadi panutann",  
                "pesan":"Jangan lupa jaga kesehatan ya kak, semangat semester 7 nya, be happy kakk!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang Ahmad keren",  
                "pesan":"Semangat bang buat tiap langkahnya, good luck bang!"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak arien cantikk bangettt, senyumnya maniss",  
                "pesan":"be happy kakk, keep chasing ur dream kakk!"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang kerenn lucu jugaa",  
                "pesan":"Sukses terus bangg, kee[ your fire alive bangg!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Abang keren abisss",  
                "pesan":"Semangat terus bangg"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "Kak Natasya cantikk bangett, baikk, kerennn",  
                "pesan":"Always be happy kakk, semangat terus kakk, jangan lupa istirahatt"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel keren, baik jugaa",  
                "pesan":"Semangat semester 5 nya bangg, sehat selalu bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Abangnya keren, hebatt",  
                "pesan":"Semangat terus bang, jangan lupa istirahat!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang Berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany keren pake bangett, baik bangett, cantikkk",  
                "pesan":"semangat terus ya kakk, sehat selalu kakakk!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "Abangnya keren",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "ALi Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "Abang baik",  
                "pesan":"Bahagia selalu bang!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak cantikk, lucuu",  
                "pesan":"Jangan lupa bahagia kakk"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya seruu, keren jugaa",  
                "pesan":"Semangat terus kak semester 5 nya!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakak cantikk",  
                "pesan":"semangat terus kakk!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "Abang baik keren",  
                "pesan":"Bahagia selalu bang, semangat!"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main ML(Mechine Learning)",
                "sosmed": "@ahmadnaufal_",
                "kesan": "Abang keren, asik",  
                "pesan":"Semangat terus bang, jangan lupa jaga kesehatan!"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakak asikk dan lucuu",  
                "pesan":"semangat terus kakak cantikk"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Bikin sticker",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abang asik, keren, chill",  
                "pesan":"Jaga kesehatan bang, semangat!"# 1
            },
            {
                "nama": "Kevin Antoni JUnior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Berdiri, Nyantai",
                "sosmed": "@kevinaj_",
                "kesan": "Abang ini asik seru gaul abis pokoknya",  
                "pesan":"Stay gaul bang!"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak ini asik santai, lucuu, hobinya sama kayak akuu",  
                "pesan":"semangat terus kak kuliahnya kak, bahagia selalu ya kakk!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Abang kocak, seru, santai",  
                "pesan":"Keep positive bang!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@sidabutar.26",
                "kesan": "Keren bang, lucu, asik juga",  
                "pesan":"Tetap semangat bang Benget, happy terus bang!"# 1
            },
            {
                "nama": "Wuliano Wiliam Purba",
                "nim": "123450098",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngoding",
                "sosmed": "@liano.wlm",
                "kesan": "Abang cool, keren",  
                "pesan":"Semangat bang semester 5 nya!"# 1
            },
            {
                "nama": "Rewina Audiya Melvasari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Ratu dibalau",
                "hobbi": "Gambar doodle",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakak baik banget, lucu",  
                "pesan": "Bahagia selalu kakk, semangat teruss"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jQ8vn9EUDeEkhhikuHz5WfyRQvXBT46r",
            "https://drive.google.com/uc?export=view&id=12kcqPJzzeVSU0KgorOUzn_OJlcj2i_k0",
            "https://drive.google.com/uc?export=view&id=14uZWIUAMSR0gtMWmZD_verPTT27F06lS",
            "https://drive.google.com/uc?export=view&id=1HWd-OKYqqtraNW6-DkhD12qSZ8E60kAD",
            "https://drive.google.com/uc?export=view&id=1byIgp4AIy6rZpSLkW7Nh4XW4sCx1F-PN",
            "https://drive.google.com/uc?export=view&id=1Suhv6DV8dE2MAekNBbxFwQGGFIZGDhR5",
            "https://drive.google.com/uc?export=view&id=1XW43unSq_K3XJwgi04al781jvcbLYHHv",
            "https://drive.google.com/uc?export=view&id=1u9uJk0phkgYcbi6NQUR2LhANcoJRFme5",
            "https://drive.google.com/uc?export=view&id=1x-C1ESF7L2qqjLQ8iJA_HdtmcBt9v_Y9",
            "https://drive.google.com/uc?export=view&id=1NNXalXOoJeJctGSx9XpdGjFeTvygn8v2",
            "https://drive.google.com/uc?export=view&id=16hrbaCZjWqAenr03waYStzxD4AXlvl7q",
            "https://drive.google.com/uc?export=view&id=1LajCwz3tjzj-LdDgHjlG7GHshVJOa2xV",
            "https://drive.google.com/uc?export=view&id=1nhDsR_bGoT3hXmr_yEpszfFsxI7EQ8di",
            "https://drive.google.com/uc?export=view&id=11df-B4TzOtwgTjkpLJENHZVRtzb_Xezc",
            "https://drive.google.com/uc?export=view&id=13bfXrF6Is4_xFARTcecyn_SeRpQsCAdR",
            "https://drive.google.com/uc?export=view&id=1tn0PRbq6XyxCM3jm2rgDn0p18p5yFu1x",
            "https://drive.google.com/uc?export=view&id=1XpmUuaBFyUejoXlcwcjLza5wPGimsqtO",
            "https://drive.google.com/uc?export=view&id=14TjuD5zxghRXdJPEcH6cItYGCGieB3Lj",
            "https://drive.google.com/uc?export=view&id=1CG4tU9aAydXdwryLCiZ3FptdAP2kUKTm",
            "https://drive.google.com/uc?export=view&id=1oC-aj3C2vIy37XJyARmzvFeJDtmcQE1O",
            "https://drive.google.com/uc?export=view&id=1FESMg78HTPbt6twvFioXnuZ3cJU_U943",
            "https://drive.google.com/uc?export=view&id=170GXa7MT57u8SkO5cbERbz5Z1SmydUkv",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur, berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Bang Randa asik, baik juga",  
            "pesan":"Tetep semangat bang kuliahnyua, jangan lupa istirahat!!"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Kakaknya lucuu, seru jugaa",  
                "pesan":"Bahagia selalu kakakk, keep smiling!"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Bang Regi kerenn",  
                "pesan":"Semangat terus ya bang ngejalanin semester 7 nya"# 1
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishashi",
                "kesan": "Kak Aisyah lucu, imut cantikk",  
                "pesan":"Bahagia selalu kakakk, semangatt!"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segair midea",
                "hobbi": "Fore",
                "sosmed": "@fadilafarizzii",
                "kesan": "Bang Fadil keren banget sihh, Duta hebattt",  
                "pesan":"Semangat terus Bang, tetap bersinar!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Bang Aqil juga kerennn bangett",  
                "pesan":"Semangat terus bang, jangan lupa istirahat dan jaga kesehatan"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Denger musik, nonton",
                "sosmed": "@notfall.s",
                "kesan": "Bang Naufal chill abis, asyik jugaa",  
                "pesan":"Semangat terus ya bang kuliahnya!!"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakaknya cantik, baik juga",  
                "pesan":"Tetap semangat dan bahagia selalu kakk!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya asyikk, cantiik banget seruu",  
                "pesan":"Sehat selalu kakak, jangan lupa bahagia dan semangat!"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin musik",
                "sosmed": "@keylashafi_",
                "kesan": "Bang Keya asyik, seru dan baik ",  
                "pesan":"Semangat terus semester 5 nya bang!"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kak Anggi asyik bangett, seruu k-pop abisss",
                "pesan":"Bahagia selalu kakakk, semangat terus ya kak!"#1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi orangnya baik bangett",
                "pesan":"Semangat terus ya kak kuliahnya, jangan lupa istirahat"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@pebby_olla525",
                "kesan": "Kak Fabiolla baik banget, asprak ter the best pokoknyaa",
                "pesan":"Semangat terus ya kak kuliahnyaa, Jangan lupa bahagia selalu!"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakaknya cantik bangett, baik dan kalem",
                "pesan":"Semangat terus kakak, jangan lupa istirahat ya kak"# 1
            },
            {
                "nama": "Tanty Widyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kakaknya kerennn, cantik, chill, lucuu dan sangan baik",
                "pesan":"jangan lupa istirahat dan tidur yang cukup kakak"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Bang Eggi keren, baik banget lagi",
                "pesan":"Semangat bang, jangan lupa dijaga kesehatannya!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah baikk, lucu juga orangnya",
                "pesan":"Bahagia selalu ya kakakk!!!"# 1
            },
             {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@i",
                "kesan": "Bang Fabio keren, asyiki, sangat chill",
                "pesan":"Bahagia selalu bangg, jangan lupa istirahat dan tidur yang cukup!"# 1
            },
             {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abang seru keren juga saudara pamungkass",  
                "pesan":"Bahagia selalu bang, jangan lupa istirahat!"# 1
            },
             {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakaknya cantik dan lucuuu",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
             {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak ini asik, baik, cantikkk",
                "pesan":"Bahagia selalu kakakk, jangan lupa istirahat!"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abang keren, baikk jugaa",  
                "pesan":"Bahagia selalu bang, jangan lupa senyum hari ini!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11kaIRA36ni7bMt-oEE_damZqy-z47HJF",
            "https://drive.google.com/uc?export=view&id=1WVw421A4UGIsavR7SEFfnX7st98Pn1Ch",
            "https://drive.google.com/uc?export=view&id=12jAkagXNfx03qtMjDoy1GIXTyEM68gjW",
            "https://drive.google.com/uc?export=view&id=19kJordOBFp4F-6WnbztJ1Gh1pn37LyHB",
            "https://drive.google.com/uc?export=view&id=1_r6QCte-b2WGLT5-DwLPsM0SPIAsVj3d",
            "https://drive.google.com/uc?export=view&id=1mj0_TxEJiJPC9hRqNyykTsKL_aVD6ozs",
            "https://drive.google.com/uc?export=view&id=1efcewoDtknKkxxOGf4gvgplJeR5PDups",
            "https://drive.google.com/uc?export=view&id=1ItH_h5_cq5fZzeHBOWILhxWMJUCyDo1Z",
            "https://drive.google.com/uc?export=view&id=1fkv5vmXyoLDm--bHt8P3S-TJU-GSnjjn",
            "https://drive.google.com/uc?export=view&id=1Be26exZ4wSxW_QCV0VlbvYAaRI9TVkyL",
            "https://drive.google.com/uc?export=view&id=1Cx56Xw-MXy2bCCEKbAedcbl2rFPk5Jr-",
            "https://drive.google.com/uc?export=view&id=1qJNaXGqqfFAhSfwyzT87SGf4lVrDJCu-",
            "https://drive.google.com/uc?export=view&id=12KwhTIZDTrH0ah2lxEouaCH4EPudSBlb",
            "https://drive.google.com/uc?export=view&id=12hS0pHq3TOOi_WGIiuKcf1ZE7zxH05Sw",
            "https://drive.google.com/uc?export=view&id=1JcHorGVJvJFcWaPmcKos3HYWd4fpSy4h",
            "https://drive.google.com/uc?export=view&id=1pjshzLASeGUGnK9LikNo7t4dc55Ff2E6",
            "https://drive.google.com/uc?export=view&id=1pjshzLASeGUGnK9LikNo7t4dc55Ff2E6",
            "https://drive.google.com/uc?export=view&id=19KoXVWMtTheHSJGY9kA71Vzo1tzo9Bcj",
            "https://drive.google.com/uc?export=view&id=1Ix2mW-FQLrF9CFpZzbiFPkypPmNG1dPG",
            "https://drive.google.com/uc?export=view&id=14Xdem1Q5vTK8GutLC4HbcsBPPsB8MwdP",
            "https://drive.google.com/uc?export=view&id=1n5ib4YnPJzCyFxJEME7T-4oS-LBQQBPH",
            "https://drive.google.com/uc?export=view&id=15DetCyFHL1qWfynr9x-hHewh4Mn_cm3L",
            "https://drive.google.com/uc?export=view&id=1L-2pgYC66QNdEJS1nvqyzFpeqZ9ATw4I",
            "https://drive.google.com/uc?export=view&id=14qol2YVM3O8k9nyI5gK9nM7vWwXDrh5m",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abang ini santuy, keren, kalem",  
                "pesan":"Semakin gacorr bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini seru asik dan gacor",  
                "pesan":"Semangat terus kak!!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak lucu, dan seruu",  
                "pesan":"Semakin positif kak!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak baik, dan seru",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abang seru positive vibes",  
                "pesan":"Tetap semangat bangg!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak seru, baik, dan kalem",  
                "pesan":"semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak santai, kalem",  
                "pesan":"Semangat terus kuliahnya!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak baikk, dan kalem",  
                "pesan":"Semoga tercapai cita-citanya kak!"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abang santai & kalem",  
                "pesan":"Semangat terus bang jadi asprak dan kuliahnya!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak baik, seru, positive vibes",  
                "pesan":"Semakin positive vibes kak!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya cantik banget, keren banget dutanya!",  
                "pesan":"Semangat terus kak dutaa & kuliahnya!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya lucu dan positif vibes banget ",  
                "pesan":"YAREEEUUUU!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abang gacor, cool abiez!",  
                "pesan":"Stay Gacor bang, tetep cool!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak baik, seruuuu!",  
                "pesan":"Kakak cantikk, dan baikk banget!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakak baikk, dan kecee!",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abang cihuyyy, kece!",  
                "pesan":"Semangat terus bangg jadi kadivnya dan kuliahnya!"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Abang gacor, cool abiez!",  
                "pesan":"Stay Gacor bang, tetep cool!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak kalem dan seruuu!",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakak imut, dan baik!",  
                "pesan":"Semangat terus kakakk kuliahnya!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak cantik, keren dan kece!",  
                "pesan":"Semangat Kak Untuk segala apapun yang dilakukan!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Kakak kereeen bangett, kece abiez!",  
                "pesan":"Semangat terus kak kuliahnya dan cita-citanya!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kecee banget kak nurul!",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang keren dan kalem!",  
                "pesan":"Stay cool dan kece abiez bang!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kak Tarisya keyenn bangett!",  
                "pesan":"Semangat terus kak Tarisya, dan lancar terus untuk segala yang dihadapi kak!"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FONMIbMzeNcSCHv1r9N0iF8Y35PWdkh6",
            "https://drive.google.com/uc?export=view&id=1t7gjzzksY848oU2v8yGMbM2XrF_nvpB2",
            "https://drive.google.com/uc?export=view&id=1NdVLtPCjNdQICQ31FtWMTF5okTwBiUtA",
            "https://drive.google.com/uc?export=view&id=1oEuB3YasOGzQUegjnsjrr-3e3FTkptSy",
            "https://drive.google.com/uc?export=view&id=16UrGfbiU7nEEjnBXDGyIAiSSBi9jnARq",
            "https://drive.google.com/uc?export=view&id=1aBhyaGx_iMsuI0hd06d7bjUFTqr9jnhL",
            "https://drive.google.com/uc?export=view&id=1IWiOnG5Q1sWtT8zl1l459wMKDbVlx9Zf",
            "https://drive.google.com/uc?export=view&id=1GKQCasxzSq6VsVlMVzMRVycFzGO61f6h",
            "https://drive.google.com/uc?export=view&id=1N-K8vPA3P-RBUlgvY-ke0fQAYg_xGwqK",
            "https://drive.google.com/uc?export=view&id=17jAIW0zBd8qyUaiQEEH8AqW-vs7ipBma",
            "https://drive.google.com/uc?export=view&id=1_Bj5gULpQmjHQQ-nkwuQup8k8xMBAezH",
            "https://drive.google.com/uc?export=view&id=1Tg_rAkN1MXZjon_bFqJnco1g8NeUYbAV",
            "https://drive.google.com/uc?export=view&id=17FsISJ1V7GV9Id4ZTie3I95bTC7L0eyv",
            "https://drive.google.com/uc?export=view&id=1jaUqG7MzQRxh2GxUtPasbML3ROKu3mac",
            "https://drive.google.com/uc?export=view&id=1lLNt7p44-PlDf1BNA8w8ShO7GItvR30F",
        
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakak ini seruu",  
                "pesan":"semangat terus jadi kadepnya kak!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak ini lucu keren",  
                "pesan":"semangat terus kaaakkk!!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@sal_fhn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abang ini kalem dan keren",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakak ini asik, lucu",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang chill, asik",  
                "pesan":"keep gacor bang!!!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak ini lucu dan keren",  
                "pesan":"semangat terus kuliahnya kakak!!!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "Abang kalem",  
                "pesan":"semangat terus kuliahnya bang naufal!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatriaaa",
                "kesan": "Abang santai dan kece",  
                "pesan":"semangat terus kuliahnya bangg!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakak seru lucu humoris asik",  
                "pesan":"tetap selalu positif kak, sukses kuliahnya!"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "kakak seruuu",  
                "pesan":"semangat terus kuliahnya kak keren!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Abang kerenn jago futsal",  
                "pesan":"semangat terus kuliahnya bangg!"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Musik",
                "sosmed": "@sarahwsti",
                "kesan": "kakak lucu seru",  
                "pesan":"semangat terus kuliahnya kakk!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak imut santai",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tuK6iJYKaMT6NQ8DPNtHELXDwPUOhFFF",
            "https://drive.google.com/uc?export=view&id=1PT78QVsuiDIEnyYdAV_5VzUaAUP2BXMM",
            "https://drive.google.com/uc?export=view&id=1CghGYAe22DLHA1fglHnVrMXdCIZMBgL6",
            "https://drive.google.com/uc?export=view&id=1tYyOhTOnbdQzr8WuwIqqHCR34Bjm8qcn",
            "https://drive.google.com/uc?export=view&id=1ptwZIW54J94Ck_Doifa6oSCbONBanrYM",
            "https://drive.google.com/uc?export=view&id=1kVf5K9wXRU7ZER5jg6YLODgF6I5c18gj",
            "https://drive.google.com/uc?export=view&id=1dMLDfIt_a5c45fVOxdJxp-No-Pow4HNa",
            "https://drive.google.com/uc?export=view&id=1EwICTc1BouwoLsSYAuSfS6a8YiwUi2bp",
            "https://drive.google.com/uc?export=view&id=1gzdx79kp5xRGjbbgJ3vEzzkcdKVwz6ub",
            "https://drive.google.com/uc?export=view&id=1YlTn11KpAOXWyZ3M6AKKiaIEvt4Pdmza",
            "https://drive.google.com/uc?export=view&id=1y8KuWmeZOc_52iIL8zhZKrRx3ftqtk7d",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Bisnis Startup, Jogging",
                "sosmed": "@dananghk_",
                "kesan": "Abang keren role model banget",  
                "pesan":"semangat terus bang berinovasinya!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum, foto-foto pemandangan",
                "sosmed": "@den_iki__",
                "kesan": "Abang cool kece abiez photogenic",  
                "pesan":"stay cool bang!"# 1
            },
             {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik abis!",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
             {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakak ini lucu dan seru",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
             {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Joggin juga",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak ini asik, seru",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang kalem, baik",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
             {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg perwira 2",
                "hobbi": "Nonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakak ini asik lucu seru",  
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
                "kesan": "kakak lucu santai",  
                "pesan":"semangat terus masaknya kak!!!"# 1
            },
             {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak baik, lucu dan seru",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1i20rTVtOwHqW23l4cgDYscNOr4X2Mh7d",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",
            "https://drive.google.com/uc?export=view&id=1nRgTrP2gdaCKkrOZj-4T_58ub4dMZoPU",

        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jati Mulyo",
                "hobbi": "Sleepcall",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak cantik, slay, seru, dan energik",  
                "pesan":"semangat terus jadi kadep nya kak patricia!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jl. Kresna Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini seruuu!",  
                "pesan":"semangat teruss kakak rahma!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard & Volly",
                "sosmed": "@mananam_",
                "kesan": "Abang Kadiv cool & kece abiez",  
                "pesan":"Sukses terus bang!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik & fotografi",
                "sosmed": "@noerruu",
                "kesan": "Abang kece dan fotografer abis",  
                "pesan":"Semangat terus bang jadi pdd buat HMSD ADYATAMA!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Abang Gokill dan keren parah!",  
                "pesan":"Semangat terus bang & Sukses terus!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak imup & Seru",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {   
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak kadiv kece dan keren abiez",  
                "pesan":"semangat terus jadi kadivnya kak!"
            },
            {
                "nama": "Aliya Anmara Amanta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammra",
                "kesan": "Kakak cantik & Calm",  
                "pesan":"Keep positive dan semangat terus kak!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini asik & pintar",  
                "pesan":"semangat terus kuliah dan jadi astut nya kak!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kakak slay, dan keren",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak cantik & kece",  
                "pesan":"Tetep Kece terus kakk!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumateraa Barat",
                "alamat": "Jl. Lapas, Kecamatan Jati Agung",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa_",
                "kesan": "Kakak cantik dan keyenn",  
                "pesan":"Semangat terus kak semoga tercapai segala cita-citanya!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak baik, dan keren",  
                "pesan":"semangat terus main robloxnya kak!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Abangg kadiv terkeren, kece & cool abiez",  
                "pesan":"Semakin mengudara dan semangat terus bang!!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kerennn banget pokoknya kaka ini",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
                        {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kakak kece dan vd banget!",  
                "pesan":"semangat terus nge-designnya kak!!"# 1
            },
                        {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kerennn & kece banget designnya kakak ini",  
                "pesan":"semangat terus kuliah dan sukses terus kak!"# 1
            },
                        {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "KAKAK VD TERKEREN & SLAY & KACIW & DABESTT BANGET DEH POKOKNYA!",  
                "pesan":"SUKSES TERUS KAK, MAKIN JAGO DESIGNNYA, SEMANGAT TERUS KULIAHNYA KAK!"# 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
       

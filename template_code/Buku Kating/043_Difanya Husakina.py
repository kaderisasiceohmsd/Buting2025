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
                "pesan":"Semangat terus kuliahnya bang! bahagia terus!"# 1
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
                "kesan": "kakak lucu banget, asyik jugaa, energinya banyakkk sekalii",  
                "pesan":"Sehat selalu kakak, be happy yaa kakk!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "21",
                "asal":"Baduy dalam",
                "alamat": "Ayresh kost",
                "hobbi": "Nahan pipis",
                "sosmed": "@celisabeth",
                "kesan": "kak abeth lucuu cantikk, ektrovert abiss",  
                "pesan":"Semangat ya kak kuliahnyaa, jangan lupa istirahat"# 1
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
                "pesan":"Bahagia selalu kakk, semangat terus kuliahnyaa!"# 1
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
                "kesan": "Abang terkece, terkeren, termantep, terbaik, terpinter, ter the best, tercare ama kelompoknya, ter ter ter semuaa",  
                "pesan":"Jangan lupa istirahat bang, dijaga kesehatannya bang, makasih uda jadi mentor terbangett bagi Anova, kita bangga punya abang sebagai mentor, infokan discord with anova"# 1
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
                "pesan":"Kapan kapan spill kucingnya bang"# 1
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
                "pesan":"semangat terus kakak cantikk, keep chasing ur dream kakk!"# 1
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
                "pesan":"Tetap bersinar kakak maniss"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Way Huwi",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@nshaysk",
                "kesan": "Kakak wawa kiyowooo, imupp",  
                "pesan":"Jangan lupa makan kakakkk"# 1
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
                "kesan": "Kak Nadya baikk bangett, cantikk, imuttt, sekretaris terkeren dutaaa",  
                "pesan":"Happy terus kak Nadyaaa, jangan lupa jaga kesehatan dan istirahat, langgeng terus ama bang Gipayo"# 1
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
                "pesan":"Semangat yaa kakk, jangan lupa bahagia kakak cantikkk!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang indomaret belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya lucuuu, seru jugaaa, positif vibes bangett",  
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
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Afifah cantikk, keren jugaa",  
                "pesan":"Be happy always kakakk, jangan lupa istirahat kakak cantikik!!!"# 1
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
                "pesan":"Jangan lupa jaga kesehatan ya kak, semangat terus ya kak semester 7 nya, be happy kakk!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang Ahmad keren sangat memotivasi, ambisius",  
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
                "hobbi": "Menghibur Zidane",
                "sosmed": "@daffahdynn_",
                "kesan": "Bang Daffa kerenn, lucu jugaa, asyikk, semangatnya ga pernah habiss",  
                "pesan":"Sukses terus bangg, keep your fire alive bangg!"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Bang Fajar baikk, keren jugaa",  
                "pesan":"Semangat terus kuliahnya bangg, jangan lupa untuk istirahat bangg"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Nyantai",
                "sosmed": "@natasyamavisca",
                "kesan": "Kak Natasya cantikk bangett, baikk banget juga kak Nata iniii, kerennn",  
                "pesan":"Always be happy ya kakk, sukses terus, sehat selalu kak Nata cantikkk"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel keren, baik jugaa, pinter ngoding",  
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
                "kesan": "Abangnya keren, hebatt, ketuplak terhebattt",  
                "pesan":"Semangat terus bang jalani kegiatannyaa, jangan lupa istirahat!"# 1
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
                "pesan":"semangat terus ya kakk, sehat selalu kakakk cantikk!"# 1
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
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "ALi Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kulineran kalau ada duit",
                "sosmed": "@ali_parisi3",
                "kesan": "Abang baik gacor",  
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
                "kesan": "Kakak cantikk, lucuu, imup",  
                "pesan":"Jangan lupa bahagia kakk, sehat selalu kakk"# 1
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
                "pesan":"Semangat terus kak semester 5 nya, sukses terus kakk!"# 1
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
                "pesan":"Jangan lupa jaga kesehatan kakakk!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen game",
                "sosmed": "@sahid_maulana",
                "kesan": "Abang baik, keren",  
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
                "pesan":"Semangat terus bang, jangan lupa istirahatt!"# 1
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
                "pesan":"keep shining kakak cantikk"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Bikin sticker",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abang asik, keren, chill, asprak baikk",  
                "pesan":"Jaga kesehatan bang, terus semangat ngasprak alpronya!"# 1
            },
            {
                "nama": "Kevin Antoni JUnior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Berdiri, Nyantai",
                "sosmed": "@kevinaj_",
                "kesan": "Abang ini asik seru gaul abis pokoknya, sangar",  
                "pesan":"Stay gaul bang, jaga terus semangatnya!"# 1
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
                "pesan":"Keep ur spirit ahead bangg!"# 1
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
                "pesan": "Bahagia selalu kakak cantikk, semangat teruss"# 1
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
                "pesan":"Jangan lupa makan ya kakk, semangatt!"# 1
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
                "pesan":"Semangat terus ya bang kuliahnya, keep ur spirit bangg!!"# 1
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
                "pesan":"Tetap semangat dan bahagia selalu kakak imuttt!"# 1
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
                "pesan":"Semangat terus ya kak kuliahnya, keep smiling kak"# 1
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
            "https://drive.google.com/uc?export=view&id=1Bt0GI2VLHhegiDFYaOJBFVxEaKPvj3wz",
            "https://drive.google.com/uc?export=view&id=1LGc6x8uCCjpqtMlEPWqwa0RAZssm8Cul",
            "https://drive.google.com/uc?export=view&id=1jAvsmPU0n7reg5l4zKTXpO-Yc75GBpzs",
            "https://drive.google.com/uc?export=view&id=1MpAX51eYgXRedfZFrPGNceb_z0pHJR0Q",
            "https://drive.google.com/uc?export=view&id=19TQOGGa1oXpIC_d3X-w2yEIcN3YC8veR",
            "https://drive.google.com/uc?export=view&id=1reDDDrwNomrWrpUMCLknYcAiseB0wfo-",
            "https://drive.google.com/uc?export=view&id=1ZKFenbTVmwWmcfuuQUVauN8GYvYplN__",
            "https://drive.google.com/uc?export=view&id=1cFJIDvLUO7vk8UjIemt23u79nVFKmtzG",
            "https://drive.google.com/uc?export=view&id=1EIIXRISFNcnvhq6RweyiwBAPHcUzTlFq",
            "https://drive.google.com/uc?export=view&id=18kOMXm0X_l9-mtxRnypCPO0oAEAhYCk0",
            "https://drive.google.com/uc?export=view&id=1d-EyFbDy48TOxhU0Rf-mvDb6fo0Bw-NP",
            "https://drive.google.com/uc?export=view&id=1uUwc-xEidSiRIDYLHpowjVH_9NgAqud7",
            "https://drive.google.com/uc?export=view&id=1tKB06CaqZsFd_8yIZpar0sPH1EZJfzb2",
            "https://drive.google.com/uc?export=view&id=1hs4_RNv92zi5RtRBP3D7qf2t0BcdvPo6",
            "https://drive.google.com/uc?export=view&id=12puZdW0MI4T2kVX0y9HLyAWulGVJv7KJ",
            "https://drive.google.com/uc?export=view&id=1hFaFu8HUli-oRpCpZh5p251aGBvYM4Th",
            "https://drive.google.com/uc?export=view&id=1ukvenkx0pMjz3m6OZKRiUp-mDGsGUtYV",
            "https://drive.google.com/uc?export=view&id=15cJ7ojYHh7H30W6ywMFBJccAjo3cTJwb",
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
                "kesan": "Abang ini keren, baik, berwibawa banget sih menurutku",  
                "pesan":"semangat terus ya bang kuliahnya, bahagia selalu!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana baik, lucuu imut dan asyikk",  
                "pesan":"Keep smiling kakak, semoga sukses yaa!!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kak Mine menurut aku keren bangett, hebat, cantik dan sangat berprestasi",  
                "pesan":"Tetap bersinar ya kakk, semangat teruss, cerebral nya hebat bangett!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini keren, baik jugaa",  
                "pesan":"Be happy kakak, semangat terus kuliahnya!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Bang Arya baik, gacor",  
                "pesan":"Terus semangat bang, jangan lupa istirahat!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya lucuu, imutt, cantik",  
                "pesan":"Bahagia selalu kakak, jangan lupa makan dan dijaga kesehatannya!"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak santai, baik dan sayikk",  
                "pesan":"jangan lupa bahagia hari ini kakk! semangatt"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya cantik bangett, maniss",  
                "pesan":"Sukses terus ya kak, keep smiling!"# 1
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abangnya keren, baik",  
                "pesan":"Semangat semester 5 nya bang!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya positif vibes banget, baik juga, dan ceria",  
                "pesan":"Semoga sukses ya kakk, jangan lupa bahagia!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kak cindy cantikk, duta terkeren menurut aku!",  
                "pesan":"Semangat terus kak duta nya, jangan lupa istirahatt!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea asyikk, semangat terus dan ceria",  
                "pesan":"keep posistif kakk, bahagua selalu kak deaa!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Asprak kerenn, baik dan seru!",  
                "pesan":"Jangan lupa dijaga kesehatannya bang!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya juga asprak ter the best sih, baik banget!",  
                "pesan":"Kakak cantik jangan lupa istirahat yaa, semoga sukses kakak!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya baikk, asyik!",  
                "pesan":"Bahagia selalu ya kakk"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abangnya baikk, keren jugaa!",  
                "pesan":"Sehat selalu bang, semangat semester 7 nya!"# 1
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Bang Adit chill banget, asyik jugakk cihuy abis dah!",  
                "pesan":"Semangat terus bang, bahagia selalu ya bang adittt"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya lucuu, baik!",  
                "pesan":"Jangan lupa dijaga kesehatannya kak:)"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kakaknya imut, lucuu, gemass!",  
                "pesan":"Sehat selalu kakak!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakaknya kerenn, pinter, cantik bangett!",  
                "pesan":"Semangat kak ngejer cita-citanyaa!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "Kakaknya lucuu dan asyikk!",  
                "pesan":"Keep spirit kakk, jangan lupa istirahatt!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak Nurul kerenn, cantik baik!",  
                "pesan":"Bahagia terus ya kak, semoga sukses!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois kecee, keren dan baik!",  
                "pesan":"Sehat selalu bang, semangatt!"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kak Tari baik bangett, cantikk dan lembutt!",  
                "pesan":"Semangat kak astutnyaa, bahagia selalu kak!"# 1
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1n5ZpBpsf2ooqNbiL5nPn37Dyd04Fx-Ar",
            "https://drive.google.com/uc?export=view&id=1bRZ06lbBu0lE3QmnEEv792iW47uq7IcJ",
            "https://drive.google.com/uc?export=view&id=1Kyirsk2dD9Q7iOPudHPYj3ANKgdceNI0",
            "https://drive.google.com/uc?export=view&id=1OoUSqPpJulORYr1aA1DOZsZWpkstopPV",
            "https://drive.google.com/uc?export=view&id=1cenFq_VLADu2pmbGs4rL6Wtomm4uE7FF",
            "https://drive.google.com/uc?export=view&id=1n4hAJLZPkndUavOvmqZbGQdn9anYtpwj",
            "https://drive.google.com/uc?export=view&id=1Av7FFx-HYAp4tskaH5ATonUrrRWx-KUj",
            "https://drive.google.com/uc?export=view&id=1HDGA4kTKLrKpCT8h94kDKFPS6oK8A3GM",
            "https://drive.google.com/uc?export=view&id=1uQIdgAy4DTOwXKINDBemgs3o2zacHiKM",
            "https://drive.google.com/uc?export=view&id=1ryKY9j5ZgP4WrokD4j9w4uI3uQHb_bCk",
            "https://drive.google.com/uc?export=view&id=1HeQ4B4a5I298d1Jw0B8eGcAQuWo07bRZ",
            "https://drive.google.com/uc?export=view&id=1w5vYIGG5K5rvTdDxB7lHMDXSZeJPTns4",
            "https://drive.google.com/uc?export=view&id=1jzYmTCTDZLmRaSJiSjMwmDOMDAKENUjC",
            "https://drive.google.com/uc?export=view&id=1y5zr20YOpWcrSskjip7fTKXpKBuzwBNv",
            "https://drive.google.com/uc?export=view&id=1c5rEXn5sf3rI5x15xAnVPb9BrZHIWgYR",
        
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
                "kesan": "Kakaknya kece abisss, cantikk",  
                "pesan":"Semangat terus kak semester 7 nya, sukses terus kak!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Pangerang Senopati Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Ranta kerenn, gacorr dan cihuyy",  
                "pesan":"Bahagia selalu kak, jangan mudah menyerah!!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@sal_fhn",
                "kesan": "Kak Salwa asyik, masyaallah baik",  
                "pesan":"Bahagia selalu kakak, jangan lupa istirahat ya kak!!"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Bang Rendi asyikk, seru dan baik",  
                "pesan":"Sehat selalu bang, jangan lupa jaga kesehatan ya bangg!!!"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "Kak Zahra lucuu, imut dan baik masyaallah",  
                "pesan":"Bahagia selalu kakak, semangat kuliahnya!!!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kotabaru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang Haikal seru, baik",  
                "pesan":"Keep going bang, jangan lupa istirahat!!!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asyik lucu poll masyaallah",  
                "pesan":"Keep smiling kak, jangan lupa makann!!!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakaknya keren dan gacor banget",  
                "pesan":"Bahagia selalu kakk, keep smilingg!!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Lampung Selatan",
                "alamat": "Sabahbalau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani13",
                "kesan": "Abangnya baik, lucu",  
                "pesan":"sehat selalu bangg jangan lupa istirahat!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatriaaa",
                "kesan": "Bang Zailani pinter, asyik dan sangat baikk",  
                "pesan":"Semangat terus kuliahnya bang, tetep keren bangg!"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna lucu bangett, asyikknya pake bangett",  
                "pesan":"Sukses terus ya kak, bahagia selalu kakakk!"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "Kak Keren cantikk kiyowoo",  
                "pesan":"Sehat selalu kakakk cantikk!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Bang Hanif kerenn, seru dan baikk",  
                "pesan":"Jangan lupa bahagia hari ini bangg"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah lucuu, cantikkk dan chill",  
                "pesan":"Semangat terus kakak kuliahnyaa, sukses selalu kak!"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda Way Huwi",
                "hobbi": "Main rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Kak Zahra kiyowoo, lucuu dan imutt",  
                "pesan":"Bahagia terus kakk, jangan lupa istirahat yang cukup!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Xa3LQBleYoqzCujjbwmwKYppelN0qWOb",
            "https://drive.google.com/uc?export=view&id=1PT78QVsuiDIEnyYdAV_5VzUaAUP2BXMM",
            "https://drive.google.com/uc?export=view&id=1CghGYAe22DLHA1fglHnVrMXdCIZMBgL6",
            "https://drive.google.com/uc?export=view&id=1tYyOhTOnbdQzr8WuwIqqHCR34Bjm8qcn",
            "https://drive.google.com/uc?export=view&id=1ptwZIW54J94Ck_Doifa6oSCbONBanrYM",
            "https://drive.google.com/uc?export=view&id=1kVf5K9wXRU7ZER5jg6YLODgF6I5c18gj",
            "https://drive.google.com/uc?export=view&id=1dMLDfIt_a5c45fVOxdJxp-No-Pow4HNa",
            "https://drive.google.com/uc?export=view&id=1ZHWVWpAdOFGR_99iiX4zJFE6_22PhbEI",
            "https://drive.google.com/uc?export=view&id=115ZVcqSefHp-2JsmwRxXgUQ89mzxK_oI",
            "https://drive.google.com/uc?export=view&id=1IchQ8tcnj3r2QrZVdIbOQMq4kDrENPxD",
            "https://drive.google.com/uc?export=view&id=1RJ5L4082pK7rZCuFIva5W1IfwuUF5PHQ",
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
                "kesan": "Bang Danang terkerenn sihh, pinter bangett, dan baik banget nganterin aku pas verbekk",  
                "pesan":"Makasih banyak ya bang, sukses terus bangg, keep shining bangg!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya baikk, masyaallah lucuu",  
                "pesan":"Bahagia selalu kakk!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum, foto-foto pemandangan",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya kerenn, gacorr",  
                "pesan":"Tetep semangat bang!"# 1
            },
             {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya baik, kiyowo!",  
                "pesan":"Jangan lupa istirahat kakk!!"# 1
            },
             {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakaknya lucuu imutt",  
                "pesan":"Semangat semester 5 nya kak!"# 1
            },
             {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Joggin juga",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya kiyowoo cantikk",  
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
                "kesan": "Bang Dhafin baikk, pinter dan keren",  
                "pesan":"Sukses terus bangg!!"# 1
            },
             {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kak Devi baiknya kebangetann, asyik dan seruu",  
                "pesan":"Terimakasih banyak kakk, Jangan lupa istirahatt!!"# 1
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg perwira 2",
                "hobbi": "Nonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kak Enggli cantikk, imutt",  
                "pesan":"Jangan lupa istirahat ya kakk!!"# 1
            },
             {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak Hanifah baikk, lucuu dan cantik banget",  
                "pesan":"Jangan lupa kesehatannya dijaga kak!"# 1
            },
             {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakaknya baik, ramah, cantiikk",  
                "pesan":"keep smiling kak, bahagia selalu!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12pqsfQuSwLYzGCC5tBAwLO8DdaAf45n_",
            "https://drive.google.com/uc?export=view&id=1eJf8o_9ZjvPj8wHDsuzs06gbQnyTygal",
            "https://drive.google.com/uc?export=view&id=1S9FVPoVmTYsbWl1m1Nf-KSO-dPpGbhSZ",
            "https://drive.google.com/uc?export=view&id=1Ki7yRrzYNcoI999z747psSLonkSia7qS",
            "https://drive.google.com/uc?export=view&id=1YsCcnpTISkqhF235_aOJbv3j1QI6TH6n",
            "https://drive.google.com/uc?export=view&id=1dUsCrFWMhQas5w43go44MoZBK5T7kb9G",
            "https://drive.google.com/uc?export=view&id=1wJ1dfrLaPlOKdaNcmeApFSgr0M5l4yp9",
            "https://drive.google.com/uc?export=view&id=17WLFQfoDElivoCMLgWEtGvURwIHOZW7G",
            "https://drive.google.com/uc?export=view&id=1NB0kq2Tv1tEAAl8vgunO7x8um-6z3aZF",
            "https://drive.google.com/uc?export=view&id=1peYbCf0rZaWPMdDgEGw_wVhMry6HKFh9",
            "https://drive.google.com/uc?export=view&id=1s1r6-tGVf9hEbPsvxx5cwT3sEUjA3bVY",
            "https://drive.google.com/uc?export=view&id=1YIZFjxFU212b67qYFrUMHXs9nrf2CB7x",
            "https://drive.google.com/uc?export=view&id=1xk_dAqqp79YX2VbAs0A5dg2veG2ZTtlO",
            "https://drive.google.com/uc?export=view&id=1HJfa7m2c0jJX6JLY3wZAiCfcrCX8Pz0L",
            "https://drive.google.com/uc?export=view&id=1dikjRRPEKSgYgqmtN9aVPEN0WwqqtaT6",
            "https://drive.google.com/uc?export=view&id=1BDDCwpzum0QdjwsgZDEbU0DLOcA7w2i5",
            "https://drive.google.com/uc?export=view&id=1qiYbWALMIBkb1cmcVc0AmCv6yE9mjXQ8",
            "https://drive.google.com/uc?export=view&id=1kKLzpbzsdR7dYFxmo8kHUOkjXoipEcv1",

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
                "kesan": "Kak Cia energinya banyak bangett, ekstrovert abiss, cantikk",  
                "pesan":"Bahagia selalu kak Cia jangan lupa istirahatt yupp!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jl. Kresna Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kak Neli baik bangett, seruu poll!",  
                "pesan":"Keep smiling kakakkkk, jaga terus kesehatannya!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard & Volly",
                "sosmed": "@mananam_",
                "kesan": "Bang Anam keren bangett, hebatt",  
                "pesan":"Sukses terus bangg!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik & fotografi",
                "sosmed": "@noerruu",
                "kesan": "Bang Labo kerenn, dokum garis kerass",  
                "pesan":"Semangat terus bang semester 5 nyaa, tetep keren terus bang!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaevangga_",
                "kesan": "Bang Ravi kerenn, baikkk!",  
                "pesan":"Semangat terus bang, semangat juga jadi kasub pemiranyaa!"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa imutt, keren dehh",  
                "pesan":"Semangat kak dokumnyaa, bahagia selalu ya kakk!"# 1
            },
            {   
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kak Cia baikk bangett, seruu dan asyikkk, cantiknya masyaallah bangett",  
                "pesan":"Semangat terus kakak kuliah semester 7 nyaa walaupun cuma 2 hari hehe!"
            },
            {
                "nama": "Aliya Anmara Amanta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammra",
                "kesan": "Kak Ale keren cantikk, medpart terkerenn, asyikkk jugaa",  
                "pesan":"Hehe jangan trauma aku bonceng ya kakk, semangattt terus di pmpd!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna seru abisss, asyikk dan keren poll",  
                "pesan":"Bahagia selalu kak donaa, jangan lupa istirahat ya kak donaa!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kak Feby juga seruu abiss, gacor pake bangett",  
                "pesan":"Sukses terus kak Febyy, jaga kesehatannya kakak cantikk!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kak Hafsa baikk bangett, seru abiss, Asprak terbaikk",  
                "pesan":"Semangat terus kegiatannya kak Hafsaa!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumateraa Barat",
                "alamat": "Jl. Lapas, Kecamatan Jati Agung",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa_",
                "kesan": "Kak Nay lucukkk, super sibukk, asyikk, cantik, imupp, kerenn",  
                "pesan":"Kak Nay jangan lupa istirahat, semangat terus km nya kakk, infokan closingan kak!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania ter the bestt, cantik, imut, gemas, lucu, seru, keren",  
                "pesan":"Bahagia selalu kak Saniaa, jangan lupa dijaga kesehatannyaa, langgeng terus ama abang tse kak hehe, info closingan!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Bang Akmal kadiv kecee",  
                "pesan":"Sukses terus bang, sehat selaluu!!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kakaknya lucuu, imut gemass",  
                "pesan":"Bahagia terus ya kakk, keep shiningg!"# 1
            },
                        {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra kerennn poll!",  
                "pesan":"Semangat terus kuliahnya kakk!"# 1
            },
                        {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak Eigi kiyowoo, lucuu cantikk",  
                "pesan":"Semangat terus kak design nyaa, bahagia selalu ya kakk"# 1
            },
                        {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Roma asyikk bangettt, kadiv pdd terkecee!",  
                "pesan":"Sukses terus ya kakkk, jangan lupa istirahattt!"# 1
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()
       

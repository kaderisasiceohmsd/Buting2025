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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=190J1gnLDQp0mMPYSxJD_8P24BJl6cgFP",
            "https://drive.google.com/uc?export=view&id=1shT9ghQShr9vL-nVV0gjZIC-2aOm6EGU",
            "https://drive.google.com/uc?export=view&id=1UCBv18SF7stIzRj9OJfxj-L3-nFvk6o6",
            "https://drive.google.com/uc?export=view&id=1oFwmK_mBYaKsrDLOInvKH72ZUgvix81c",
            "https://drive.google.com/uc?export=view&id=1ok5PvYqNpnx1CRfq78jnPHI33R25MHJe",
            "https://drive.google.com/uc?export=view&id=1UEq0wL7mEFxizZsQnRL_m5HEGT6CDc_E",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Setiap ngeliat abangnya, rasanya kayak liat senior yang bisa dijadiin panutan. Abangnya ramah tapi tetap berwibawa.",  
                "pesan": "Semoga langkah abang ke depannya selalu lancar, terus nyebarin energi positif kayak biasanya ya!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas Raya",
                "hobbi": "baca buku (dasar-dasar sql)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya keren banget, disiplin tapi nggak kaku. Kalau ngomong tuh selalu bikin orang semangat dan termotivasi.",  
                "pesan":"Semoga semua usaha abang dibalas dengan hasil terbaik. Teruslah jadi inspirasi buat adik-adik di bawah, ya!"
            },
             {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Airest Kost",
                "hobbi": "siram shopee",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya seru banget, selalu bisa bikin suasana cairnwalau lagi tegang. Rasanya setiap ngobrol pasti ada aja hal lucu yang bikin ketawa.",  
                "pesan":"Semoga tetap jadi pribadi yang lebih ringan tapi bermakna ya kak, jangan pernah kehilangan semangat dan kebaikan yang bikin orang nyaman di sekitar kakak!"
            },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya keliahatan tegas, tapi sebenarnya perhatian banget sama adik tingkat.",  
                "pesan":"Semoga kakak terus jadi sosok kuat yang juga lembut hatinya, karena kombinasi itu jarang banget."
            },
              {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "rajabasa",
                "hobbi": "baca buku, saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya kalem banget tapi selalu hadir di momen penting. Kayak diam-diam tapi berkesan.",  
                "pesan":"Semoga kakak selalu dikelilingi hal-hal baik, dan tetap jadi sosok tenang di tengah ributnya dunia."
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"kota Padang,Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya rapi banget, dari gaya sampai cara ngomong. Keliatan banget kalau orangnya teratur.",  
                "pesan":"Semoga semua kerapian dan disiplin kakak ini bawa kesuksesan besar ke depannya ya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1taDThCmFalaAq32rSb3Vr546SHBn7TsG",
            "https://drive.google.com/uc?export=view&id=1XI6Riuz8Ufc3ErqXnc78iYfjGfKWlU1s",
            "https://drive.google.com/uc?export=view&id=1joYRwXZAa1IHnE-myBZmC6aSADqg1--H",
            "https://drive.google.com/uc?export=view&id=1cZ18GIgucF7sVb5IE3OrkILTIiRYi_SA",
            "https://drive.google.com/uc?export=view&id=1Zte-dE5mcN7TGJ3Ofj6-J9wgpYtts5Ei",
            "https://drive.google.com/uc?export=view&id=1ZcJheP6pObA6yYl9OMy4aGAGmkwrAC70",
            "https://drive.google.com/uc?export=view&id=1Tx9NM2iqYifdYPw315xzTWJnS-0ZrMec",
            "https://drive.google.com/uc?export=view&id=1t7-XtB0ph2WAfxvknVOpw0KKV-U5YoFD",
            "https://drive.google.com/uc?export=view&id=1l99961ZUX7ul-AEC6YkCJi1nUyUVFXWg",
            "https://drive.google.com/uc?export=view&id=1TN8QezWSmEhAcBLTP7bgzBAT2u5rbo0x",
            "https://drive.google.com/uc?export=view&id=19nbuO-JWHr5E2It0n7gmv6MjbKXLzNJh",
            "https://drive.google.com/uc?export=view&id=1f0SbVXoj5BHp1U2vLVy04SdFZSgV0Ezv",
            "https://drive.google.com/uc?export=view&id=1mg5ypXo45S6-jbj45N9M_rtny2hyJtfu",
            "https://drive.google.com/uc?export=view&id=1u0qUC_kfF-g4cIGcE9Q0Pgyyc7MWt0be",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Yapping",
                "sosmed": "@Jeremia_s_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Kalimantan Utara",
                "alamat": "Belwis",
                "hobbi": "Sibuk",
                "sosmed": "@j_eesie",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sakung",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "",
                "pesan":""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ou04R3utaEJiNXqTEemThcK8VHI7BL1o",
            "https://drive.google.com/uc?export=view&id=1pzDkPPXFDIQFFX43nfzcbHa9dnn8df5K",
            "https://drive.google.com/uc?export=view&id=1w5xvwszcIvl0XWmZ25wzMWvWr20QNOTm",
            "https://drive.google.com/uc?export=view&id=14nX5n1HJc_V-1FhjFAQnI_Q2hpsmRPfi",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "tanya caesar",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "",  
                "pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CQvf6tM3dqJpQKe6H-Lm1jm-_Z7GYQJp",
            "https://drive.google.com/uc?export=view&id=1A4rjvqFIvTZuvRlFvvjppX9mIVHn5jR0",
            "https://drive.google.com/uc?export=view&id=1fBllod1XLH9YX7QGwKO1K6TvemBb1fS4",
            "https://drive.google.com/uc?export=view&id=1U7Ls7p9cdoxXGqCEvC3ta2YBEfb_22WF",
            "https://drive.google.com/uc?export=view&id=1mwPvvDPb0_LpvldKoFaBzP5K1KKncjJH",
            "https://drive.google.com/uc?export=view&id=1FC89mBMDzN7o5ga3BiCVEPPZv084aKp3",
            "https://drive.google.com/uc?export=view&id=1At3x_Sj9OG3pMMZX14c1WB-HHOzPj7ST",
            "https://drive.google.com/uc?export=view&id=1NuMNUG-Xpk50U3s-uC8yyADEF1WgKqJ4",
            "https://drive.google.com/uc?export=view&id=1FKCfsq19CAnp4POs7oRoZxL9ZsXf8APu",
            "https://drive.google.com/uc?export=view&id=1D9qL5VCgwsHQLC4UXv8tUtmSqFaXV0Al",
            "https://drive.google.com/uc?export=view&id=12_IiONpJD2xVNpp5M_q2hAkqNasqaqD-",
            "https://drive.google.com/uc?export=view&id=1HzxjsO4tI5oA9Tx_727hrvhuqE3U2aiT",
            "https://drive.google.com/uc?export=view&id=1QR4RDWux0s9ZfbZjnQpJKmk98BAehQDk",
            "https://drive.google.com/uc?export=view&id=1sRcS21fM8wnqjje59dODQwWT6Oz1Ku9j",
            "https://drive.google.com/uc?export=view&id=1Gh8PwzIwmbyKdfp2WVv_-1AIZE-lN7r1",
            "https://drive.google.com/uc?export=view&id=1svNWTH4PILzDClxxX4fFxLF_0dQNwsBB",
            "https://drive.google.com/uc?export=view&id=1YK9pVihw_B8UP3-bId_65ush2GSaFtG1",
            "https://drive.google.com/uc?export=view&id=1Bbqlt4SRAL9YeahdLJsXe3Omxlh0G3LF",
            "https://drive.google.com/uc?export=view&id=13d7XbKKboXcWYTiBs9hAFEvAmRJ0gkHp",
            "https://drive.google.com/uc?export=view&id=1yWhiAuaXWPIED2RhmIkfV3lEYH5TY2sN",
            "https://drive.google.com/uc?export=view&id=1NdhFyVQM6cJXXJFVVUrsBR7NydFeP6K0",
            "https://drive.google.com/uc?export=view&id=13WSIyZBYZC9jg4Y8Ai9j1aV0nvfQgApj",
            "https://drive.google.com/uc?export=view&id=1Dz0YhYRGKaunhuCi7OK8YOczOdJL3c7-",
            "https://drive.google.com/uc?export=view&id=1A5i2gsEAZ9HHCOf7YBjyYsJyPtgMvGN_",
            "https://drive.google.com/uc?export=view&id=1jh24_Q3JDf7nD1ZJdke42hQ6Kdpi5ltl",
            "https://drive.google.com/uc?export=view&id=1Xp5agNll5Tl977PjRxIjkpyku2GnqZME",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Sebelah kos bang daffa",
                "hobbi": "Liatin Haikal",
                "sosmed": "@arientakhsnl_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kos kak arienta",
                "hobbi": "Isengin Fislam",
                "sosmed": "@daffahdynn_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Terima kasih atas bimbingannya selama ini, Kak.",
                "pesan": "Semoga kami bisa meneladani semangat kakak."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Gg. Perwira",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 55",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan Beling",
                "sosmed": "@kevinaj_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "",  
                "pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17edM9BDkkDfCmZP3wczgClCVGqSmb7G3",
            "https://drive.google.com/uc?export=view&id=1rDYMhKTLYgLoPMnxw-NJIVJ8JGVXHKtC",
            "https://drive.google.com/uc?export=view&id=1qqwazdTfCv7UIW9JOz6dxUNcYA39QhXE",
            "https://drive.google.com/uc?export=view&id=1dVpOc4275cZZPBZzEziu6LVHl-dEAIeS",
            "https://drive.google.com/uc?export=view&id=1pj4fVj5FhHPxzeHXYqTKGWD-YDbrMzdG",
            "https://drive.google.com/uc?export=view&id=1Venk3U18aui97gkUBU3QiPk7tj48ipY9",
            "https://drive.google.com/uc?export=view&id=1w1qatRSByYeUsq0HqPucuLrXpOlaB9Tt",
            "https://drive.google.com/uc?export=view&id=1Moej14-6H3oHbfcFGanX8oG9HM9RsavL",
            "https://drive.google.com/uc?export=view&id=1WEP6FkjoNoPvQyyI5YNqqG8l-w0y3Yjb",
            "https://drive.google.com/uc?export=view&id=1CGyOL9lfGGcWe31pkyXaMgfZQRx_a9hg",
            "https://drive.google.com/uc?export=view&id=14B5KQpvauaot_VnSkr3ZP4ut32iUvwCZ",
            "https://drive.google.com/uc?export=view&id=16xjAUTTPdqwmdPBf5e4oHuuJ4gh2g3Y0",
            "https://drive.google.com/uc?export=view&id=1LVVKlGXW56dNoBc4VFPGsT5SAMIKGAFB",
            "https://drive.google.com/uc?export=view&id=1ashw-FSGZZKTJUKck4crRsHTjjttimbu",
            "https://drive.google.com/uc?export=view&id=1RRXqfy7JDDnHYDTjOnnH6ktJXdhxZqj8",
            "https://drive.google.com/uc?export=view&id=1Gl6swFA-X284ZFb-n_EP8rmfg7kgN1SO",
            "https://drive.google.com/uc?export=view&id=1P0F-VnHVrbRRM3o5KBZ-CiE-Xd0devrh",
            "https://drive.google.com/uc?export=view&id=1ibeVtBqjl9ZiHiFyNKuESxMjL7iNlYh_",
            "https://drive.google.com/uc?export=view&id=1YXBaCe_pvmGcO1YVX1HJRjwEwnlrwMKv",
            "https://drive.google.com/uc?export=view&id=1osJEPikdHNyRrTlJzv2eqTW6AveXvy8c",
            "https://drive.google.com/uc?export=view&id=1r1hGvMuB8Lys8FnwazjKI7MtzEy87Kyd",
            "https://drive.google.com/uc?export=view&id=1O7uoQmxYVRuyySIyWP1MtSgSMIYN3mqw",
        ]
        data_list = [
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "",
                "pesan":""
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
                "pesan":""
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main piano, Nyanyi, Ngehalu",
                "sosmed": "@bee_0115",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12op-VE9vpqBb7vn5xTEzjKGPxILNFZ50",
            "https://drive.google.com/uc?export=view&id=1HRg9yviq4yn3kGBzxAyuG6f2NLX740rR",
            "https://drive.google.com/uc?export=view&id=1aaGuDybOSMKlYAVgvYFpXLma7UgZQyYZ",
            "https://drive.google.com/uc?export=view&id=1f3ybdfE8vxL8rLhS03nYBi49DfWD8YBV",
            "https://drive.google.com/uc?export=view&id=1N7uLNAyafhKf1jwIYkxp3rAAPWh9amEk",
            "https://drive.google.com/uc?export=view&id=1RW0FBWAcy-Vzm5NEl6kyP2mCmtWIB5Lz",
            "https://drive.google.com/uc?export=view&id=12vtfjAByi0ldDF9ouiumrbmiP0mKdPLp",
            "https://drive.google.com/uc?export=view&id=1tlaoXeQTLuvspA-22fWwOKZJTd8hLJJW",
            "https://drive.google.com/uc?export=view&id=1oADq5A0NoW717_MC6FDnnS896KK3miVa",
            "https://drive.google.com/uc?export=view&id=1Z4XuIc4a4imdrJVtwD_YVkFsTOCBAj6i",
            "https://drive.google.com/uc?export=view&id=1JWYbpTdta2M0PeXkGJ9yPNiW6GaPX6b8",
            "https://drive.google.com/uc?export=view&id=1jSBqLmn1e3-wv9iFeKbwY438BVTdd6GO",
            "https://drive.google.com/uc?export=view&id=1F_6y1-yTjkeU29zTVXKDqVQr_nGf7Hi6",
            "https://drive.google.com/uc?export=view&id=1kysSM2rjTfAxCA8cGMQsGsBFBLdbFqdK",
            "https://drive.google.com/uc?export=view&id=1SfuL_jPAhJVyXs-DYu936e8d8HSCLWRC",
            "https://drive.google.com/uc?export=view&id=1wY7hdH8kzm7w4QjPMA0pnDwi5U3WtXZf",
            "https://drive.google.com/uc?export=view&id=1LwRaSFINFDo90SS_SvqoYh21S3No0OIF",
            "https://drive.google.com/uc?export=view&id=1OLfA3jZqCGwaW7LbFOtjpADrDZdsnmxg",
            "https://drive.google.com/uc?export=view&id=1If-9n1R7rWj4dqAtZtZPg5TyDgn75Tlm",
            "https://drive.google.com/uc?export=view&id=1t0JydAh4iLKOfGksQwcvXzUk-B_hm7Xp",
            "https://drive.google.com/uc?export=view&id=124x04deTErlGVcf0V8FBEkM98E-L6wFC",
            "https://drive.google.com/uc?export=view&id=14jEdMlzfHXqZByNvLIe8FPJGAR9GVjrT",
            "https://drive.google.com/uc?export=view&id=13P_ITLwchucG1aiwTmRiQ15JunnSBKt3",
            "https://drive.google.com/uc?export=view&id=1Gh6ZnGQpXG33k5AMfE5v5daEWgPVstyt",
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "",
                "pesan":""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1y5WezX0F63-wP2AqAl7V0bySgEAADeEl",
            "https://drive.google.com/uc?export=view&id=1cLQo07ZKTu3MlGqZYc2H8Fv7ieW_QKbX",
            "https://drive.google.com/uc?export=view&id=1-bJI8B7aSYYZZt6XMCpMv2-gpBzx6Yne",
            "https://drive.google.com/uc?export=view&id=1uNBtLDXPLP4l8l722nfaVM1pZcxLQsbe",
            "https://drive.google.com/uc?export=view&id=1uNfU84qu3_X1cpVZIqdx_W5JidbYrzvm",
            "https://drive.google.com/uc?export=view&id=1v-M12qCKsHgqWJKf2Ci7AwS34HmeqnMD",
            "https://drive.google.com/uc?export=view&id=1JVumhqw1dLeCa1kE_50PKXVi1u6FhAzv",
            "https://drive.google.com/uc?export=view&id=1cctf8fUK2MazbVaQSdl5w4fh9NqGw-Xv",
            "https://drive.google.com/uc?export=view&id=1-VEqjEiItceODuBN6JujsLK0rGePfYHa",
            "https://drive.google.com/uc?export=view&id=1bytBJNykYTW_YPBIJuE5H36nAEIG7f5t",
            "https://drive.google.com/uc?export=view&id=1ipAfMVxcnRCaTVbps6h4Zdb--0xhifO6",
            "https://drive.google.com/uc?export=view&id=1S8tSa4drfz1ht4zlKwHBN9QKyeoQ0MdG",
            "https://drive.google.com/uc?export=view&id=17G51wmsKKWc36OieM7vBWvDPG24JydT5",
            "https://drive.google.com/uc?export=view&id=1ApJhi33CVehTS7pvLyyDA1v2SvM2uHOM",
            "https://drive.google.com/uc?export=view&id=1Rsyw24I4LV41rQ479Sko5P9KGTohbnUZ",
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
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Jalan Durian 19",
                "hobbi": "Mengetik",
                "sosmed": "@zhresti",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",
                "pesan":""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TSnn_ULuqdYZFefW6qpyh7suPqjMKKND",
            "https://drive.google.com/uc?export=view&id=1gqMZb6cPf7ySESEeCV-4yVN2O6lr-cgi",
            "https://drive.google.com/uc?export=view&id=1-EADLS8qRY2ZrNOXyJbHTkUnjwf--KgF",
            "https://drive.google.com/uc?export=view&id=11TUDmrRKFDvjfEMr-pHJSLoLzolSX5z2",
            "https://drive.google.com/uc?export=view&id=1joeG7yxGCip81DXMphzqc0VnpnOsVj3p",
            "https://drive.google.com/uc?export=view&id=1-x06IjAyYvGQ6Fw0fzjCQRsNWEt1_yE2",
            "https://drive.google.com/uc?export=view&id=1P_PnHJSMV-ANqOjta8n-3ZFSLUDwxuj2",
            "https://drive.google.com/uc?export=view&id=1gz0LVOxRUz1LTQmThBaA1JnMo3Uvqsfl",
            "https://drive.google.com/uc?export=view&id=1oYVQONOFKT59dclhUkzNAeUImgT8ij17",
            "https://drive.google.com/uc?export=view&id=1U05HVsV71mHaM2oKjggqUkxh4eyED-BH",
            "https://drive.google.com/uc?export=view&id=1QNnXQHyQqhXxy1YahN4OL7EJH-txJJSB",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "dananghk_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "",
                "pesan": ""
            },
            {
                 "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ilnHMYPAFGgRWd7AX5aLBnsj5G9zBbH4",
            "https://drive.google.com/uc?export=view&id=148WpaNGBPNCbsBnHauPQQqh0D6WNmc2t",
            "https://drive.google.com/uc?export=view&id=1ZvME00SblJ0kHLbBxGT_hUua0kyB_WM_",
            "https://drive.google.com/uc?export=view&id=1wykdInRckjuNq-R8Pk_3lJztZ9IH7uws",
            "https://drive.google.com/uc?export=view&id=1WeZfjiov9M5HDdxWsjIG6MpN4OgtWzDx",
            "https://drive.google.com/uc?export=view&id=1kTKYQjzcpZD1NP6AHZyztFy65_gJt8Cv",
            "https://drive.google.com/uc?export=view&id=1WlH5yKMmth26YinPB11OR6gjhsehpEO6",
            "https://drive.google.com/uc?export=view&id=1GUAC9lQpkvLwdVs-eUBgtjcfuOgUVDzn",
            "https://drive.google.com/uc?export=view&id=1iaaYTJrkWB77SFqkzTmQmuE5ce9bxVOP",
            "https://drive.google.com/uc?export=view&id=1ZPHI-1F507c4CYxgrmXdCCyfYc4s_Tvu",
            "https://drive.google.com/uc?export=view&id=1lVHvhuImPzuwdEJnDWYA-lFUo4lBAWGc",
            "https://drive.google.com/uc?export=view&id=1KvfrA6am1eL-QgFyL_GG3dLKsdUt1t2H",
            "https://drive.google.com/uc?export=view&id=1upKpp9DGuMPx6hTwEjh4ppOK7KK2flEw",
            "https://drive.google.com/uc?export=view&id=1ZuKMqpAJYqqdVcO5Inqs-EWUO3kegsVN",
            "https://drive.google.com/uc?export=view&id=130j_MthJBfFfR66O_wdkR5lXnErGBKaD",
            "https://drive.google.com/uc?export=view&id=1bKJlKzLX1OfKB28rkTGOHRm_93tmZYJX",
            "https://drive.google.com/uc?export=view&id=1DSQogEo0SaLTS-O14nbewZNUiB8pkeDc",
            "https://drive.google.com/uc?export=view&id=1t4swZcXAglNIfrkgbAw3GiLlAAgc0nZW",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Menyanyi",
                "sosmed": "@roms.slbn",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "",  
                "pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

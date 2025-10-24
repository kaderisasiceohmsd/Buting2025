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
            "https://drive.google.com/uc?export=view&id=1IdC8HXCMnnk_AvhAT2mDYK4Etj7_q8Uh",
            "https://drive.google.com/uc?export=view&id=1G_mmpQh9_6krU1_1toH6CF45SwMT4rQZ",
            "https://drive.google.com/uc?export=view&id=1nkWwcvRDIkWvATSNtXtKhtkkdmHh6gUV",
            "https://drive.google.com/uc?export=view&id=1FQRv080mF9qlGRxE3KKko2aMf0sJoo2u",
            "https://drive.google.com/uc?export=view&id=1-7bhYQv3IEfQk302LGfPGEUvWB1rIa-U",
            "https://drive.google.com/uc?export=view&id=18YfvU7rIhJFeeoo9wXcRz10baKvY-vLB",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450122",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Abangnya keren, asik dan berwibawa",  
                "pesan":"Semangat terus bang selama menjabat sebagai Kahim"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya tegas tapi bisa asik juga",  
                "pesan":"Semangat nyusun TA nya, Bang Jo !!!"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya baik dan juga usil",  
                "pesan":"Jangan keseringan nahan pipis kak, nanti jadi penyakit"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya pendiam, dana juga murah senyum",  
                "pesan":"Semoga lancar dalam segala hal nya, kak"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya punya selera humor dan jokes yang unik",  
                "pesan":"Semoga nanti bisa main ke BUleleng ya, kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cute kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya asik dan juga apa adanya",  
                "pesan":"Selalu jadi orang baik dan ramah ke semua orang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kesXyvLIoAKGYmrH5pwW6mqY8XEjI9uv",
            "https://drive.google.com/uc?export=view&id=1QNsaQD4EU80kB1Hh3Yba5BuB63ye7CKD",
            "https://drive.google.com/uc?export=view&id=1uo65ca6ZMel9JrJI6X5JTFuj58XXRYtv",
            "https://drive.google.com/uc?export=view&id=14N-ruTgPbkGW5yUo629XHt0c5ajM8_WV",
            "https://drive.google.com/uc?export=view&id=1N39_qKn4__CnDNl54JfRvgBAEZhUCYF1",
            "https://drive.google.com/uc?export=view&id=1b4qPequInoR2y8QLSo-nTgSoMGmkgEgH",
            "https://drive.google.com/uc?export=view&id=1nwGJPWVbaFrytW_1Pd7d4Ecwqw61G-HR",
            "https://drive.google.com/uc?export=view&id=1MvpzVEQGZPwbd6FvB3fMMzbugl3zLjMr",
            "https://drive.google.com/uc?export=view&id=1zAAUhEaQ92Sy7PT4akh16U1cDRMrt0PK",
            "https://drive.google.com/uc?export=view&id=19t6R8OYEEcEZ3UH8ECAxrTe7_m8Rsa5c",
            "https://drive.google.com/uc?export=view&id=1Fhz6DSUUw-w1nyX1--OPSjcO098_xvcI",
            "https://drive.google.com/uc?export=view&id=16O9t6Y4F3PLau_7f6ssmO2KUxsAOQGYi",
            "https://drive.google.com/uc?export=view&id=1A-26MjHCDLNEg4_S0mBKscOhOwYMMIy9",
            "https://drive.google.com/uc?export=view&id=1W-0vr37H7rw4_1HGXaHKk1XvrZHaLHHA",
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
                "kesan": "Abangnya asik dan juga gampang diajak ngobrol",
                "pesan":"Sukses selalu kuliahnya, Bang"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya baik, asik juga",
                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Orangnya seru, humble, dan baik banget.",
                "pesan":"Semangat dan sukses selalu, Kak"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi morse",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya baik, dan juga kalem",
                "pesan":"Semangat terus menjalani hari-harinya, Kak"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way Halim, Bandar Lampung",
                "alamat": "Way Halim, Bandar Lampunng",
                "hobbi": "Nyuci Baju",
                "sosmed": "@dhruchyo",
                "kesan": "Abangnya baik, dan juga ramah",
                "pesan":"Tetap jadi pribadi yang murah senyum"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way Huwi, Bandar Lampung",
                "hobbi": "Main Karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya baik, ramah, juga sering ngelive di tiktok",
                "pesan":"Semangat ngelive dan juga jaga kesehatannya, kak"
            },
            {
                "nama": "Ghivaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Salah satu orang yang menginspirasi",
                "pesan":"Jangan lupa jaga kesehatan, Bang."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya cukup pendiam, tapi asik",
                "pesan":"Semangat dan sukses selaluu, Bang."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "1224500065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya asik, seru waktu diajak ngobrol, dan juga murah senyum",
                "pesan":"Sukses selalu, dan juga semangat menghadapi hari-harinya, Kak"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "12345085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Sangat berkesan, orangnya humble, cantik, sering ngajak bercanda, salah satu orang yang terlibat di cerita penting hidup aku, layaknya seorang kakak kepada adiknya",
                "pesan":"Tetap jadi pribadi yang humble, peduli ke sesama, dan yang terpenting jangan lupa selalu bahagia. ekhemmm Bingxue satu bisa kali kak, hehe"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Gang Sekuntum",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya Baik, Pendiam, dan ramah ke semua orang",
                "pesan":"Selalu jadi pribadi yang pantang menyerah"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Baca Buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya asik dan juga ramah",
                "pesan":"Jangan lupa jaga kesehatan, Bang."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Orangnya baik, dan kalem banget.",
                "pesan":"Semangat terus kuliahnya, Kak!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Ealaaa Daplok kuhhh yang paling Humble dan Baik Hati",
                "pesan":"P! Mantai Kak bareng 29, hehe."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oFovOX0KQZ2JhVIzQE6A-oPkhJaSJtbw",
            "https://drive.google.com/uc?export=view&id=16k7k9uQ0RYmQtnWO8LcoVqKxGI0yJDBt",
            "https://drive.google.com/uc?export=view&id=1xE0-kXO_TaJEziRttw_8IdYz-k0AhIhL",
            "https://drive.google.com/uc?export=view&id=1qlycjEYpnq4mQsIzfzVmbDEXaRvGKhh6",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "tanya caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya seru dan juga bisa diajak bercanda",  
                "pesan":"semangat selalu bang dalam menyampaikan Aspirasi massa Sains Data!!!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakaknya cukup pendiam dan juga cantik",  
                "pesan":"semangat terus menjalani hari-harinya, Kak !!!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya asik dan juga positif vibes",  
                "pesan":"semangat terus jadi manusia baik !!!"
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik dan juga bisa diajak bercanda",  
                "pesan":"semangat dan jangan menyerah kak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1d06i7HmC0psXDR4Wob5ipTBh6cfAkQvn",
            "https://drive.google.com/uc?export=view&id=1MjpSyIvyP5OFHypqhv4tvSTsMaSFXtol",
            "https://drive.google.com/uc?export=view&id=1dGJ4j09Y-HGle-70l30p22z8xUWp6uqz",
            "https://drive.google.com/uc?export=view&id=1tMNOTcHfMtKan1ky35AC-QTJOCIbfdQo",
            "https://drive.google.com/uc?export=view&id=13mRmRNN9mKM7j8_ABTYJ2GsgeNESb7k6",
            "https://drive.google.com/uc?export=view&id=11GXI-KjTxPV2JH32BNjAeCe7LkU_rBES",
            "https://drive.google.com/uc?export=view&id=16Tin3jDmd5AzgFgGmjOTfvFvlucIGwwi",
            "https://drive.google.com/uc?export=view&id=17G0E30Rk6stk2RzRV2N0r9Wxxt0qm7nf",
            "https://drive.google.com/uc?export=view&id=1BYQjqBgn03H5Zi9RaMupUKdnQkGxv7oO",
            "https://drive.google.com/uc?export=view&id=1PK0fDqhAkj4uUmpsQnjZzSYa4jnHpmWz",
            "https://drive.google.com/uc?export=view&id=1SnONFBviBSY8uOwHWMAaVYBIGmFkTiXZ",
            "https://drive.google.com/uc?export=view&id=115hBiuyfFcd2WUiPDqHkWkG3-ViikdEn",
            "https://drive.google.com/uc?export=view&id=1N3-pQnJ98jkcJw_EIj2DoukG0Dqskjny",
            "https://drive.google.com/uc?export=view&id=1FviLjfQW5AGucNCBKScY6tnGP2H3vFUT",
            "https://drive.google.com/uc?export=view&id=1S3ZASHJj6TDWytFm8ZpGlD5qssKkffxZ",
            "https://drive.google.com/uc?export=view&id=1bvjbhL6YN3ubn-KidW94bcBkZ7LpKs5v",
            "https://drive.google.com/uc?export=view&id=1FYNXWCT404H9D0Wg1fJfUcyMFk-nNLLm",
            "https://drive.google.com/uc?export=view&id=1ETO-GYdcYqIXmSW_ypH5lMD8DIjZZ-zN",
            "https://drive.google.com/uc?export=view&id=1WA-VbcFyTJY7Rpg-kpH4YjHaWjLDLIUl",
            "https://drive.google.com/uc?export=view&id=1fJ6DsAX3xxpiYoZ9hvOyzWokyTHppaqC",
            "https://drive.google.com/uc?export=view&id=1_-L8zMOPzrYzJkbW1GvMWBVpJ_XTo15j",
            "https://drive.google.com/uc?export=view&id=17iXZJPPF2kp5M6PduPokzflmGGusJU3i",
            "https://drive.google.com/uc?export=view&id=1h5DMaB5_uE_wapM3jk1ehOC9I8BZPbEX",
            "https://drive.google.com/uc?export=view&id=1EgINIyQJh2LYtOqVYGGWJ0C217FNRFtX",
            "https://drive.google.com/uc?export=view&id=1GFeghvPmh7a_29osniaKHRQUISNPAwUF",
            "https://drive.google.com/uc?export=view&id=1ycip_SGXMNczaTrUueI61gD8gkLf2iwg",
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
                "kesan": "Kakak sangat berwibawa dan mengayomi.",
                "pesan": "Mohon bimbingannya selalu, Kak. Sehat dan sukses terus!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Terima kasih atas bimbingannya selama ini, Kak.",
                "pesan": "Semoga kami bisa meneladani semangat kakak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Pertama kali ngobrol banyak bareng kak allya di angkringan. Diluar kaderisasi, ternyata kak Allya seru juga diajak diskusi, selalu memberikan arahan atas pendapat dan saran yang diajukan",  
                "pesan":"Tetap jadi pribadi yang selalu menginsiprasi banyak orang dan semangat terus menjalani hari-harinya, Kak."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Salah satu orang yang menginspirasi dengan segala pendapat pribadinya",
                "pesan": "Semangat selalu, dan juga semoga impian menjadi Presma tahun ini terwujud, Bang"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Pertama kali kenal kak Arin karena satu organisasi. Kakaknya baik, ramah, punya senyum yang manis, juga selalu langganan jadi sekretaris di setiap kegiatan",
                "pesan": "Sukses selalu untuk kakak, dan juga semangat selalu kak"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Aslinya bang Dapa humoris, sering ngajak bercanda semua orang",
                "pesan": "Selalu jadi pribadi yang humoris dan juga selalu jadi pribadi yang rendah hati."
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Abangnya Baik, Ramah, dan juga bisa membimbing adik-adiknya",
                "pesan": "Semoga selalu menjadi pribadi yang membimbbing dan membantu banyak orang."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakaknya humble, baik, juga ramah ke semua orang.",
                "pesan": "Jaga kesehatan dan semangat seallu kuliahnya, Kak."
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abangnya baik, dan juga perhatian ke adik-adik tingkatnya",
                "pesan": "Selalu humble dan juga selalu mengayomi orang lain, Bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Tegas dan juga bisa diajak bercanda santai",
                "pesan": "Sukses selalu, dan semangat menggapai impiannya, Bang."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak nya kalem, dan punya aura positif",
                "pesan": "Selalu jaga kesehatan dan semangat selalu, Kak"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voly",
                "sosmed": "@shahid22_",
                "kesan": "Abangnya kalem tapi pinter banget.",  
                "pesan":"Semoga makin sukses ke depan."
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang. Nangka 4, Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Nyantai tapi tetap produktif banget.",  
                "pesan":"Jangan lupa jaga kesehatan"
            },
            {
                "nama": " Gusti Putu Ferazka",
                "nim": " 123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Ceria, lucu, dan penuh semangat.",
                "pesan": "Tetap jadi diri sendiri ya."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Baik banget dan selalu bantu.",
                "pesan": "Terima kasih atas kebaikannya."
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakaknya disiplin dan konsisten banget.",
                "pesan": "Pertahankan sifat hebat itu ya.."
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Enak banget diajak ngobrol santai.",
                "pesan": "Semoga makin sukses ke depan."
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Bijak banget pas kasih saran.",
                "pesan": "Semoga selalu diberi kelancaran."
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jalan Lapas Raya No. 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya sopan, ramah, dan santai.",
                "pesan": "Jangan lupa istirahat yang cukup."
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450111",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkep lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Baik banget dan gak sombong.",
                "pesan": "Semoga selalu jadi contoh baik."
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Kalem tapi tetap berwibawa banget.",  
                "pesan":"Sukses selalu di masa depan."
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Ramah banget sama semua orang.",  
                "pesan":"Terus tebarkan energi positifnya ya, Kak"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Humoris tapi tetap tanggung jawab",  
                "pesan":"Jangan pernah berubah ya, Bang"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Abangnya pendiam, baik, dan juga humoris",  
                "pesan":"Selalu Bahagia dimanapun itu, Bang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakaknya baik, ramah, dan juga pendiem",  
                "pesan":"Semangat terus dan jangan pantang menyerah, Kak"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Tegas, detail, dan to the point jika menyampaikan sesuatu",  
                "pesan":"Selalu rendah hati dan selalu membimbing adik-adiknya ke hal yang lebih baik, Bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Q9BfRcvjtkH2bj2QxvQJQzODKyjmadPb",
            "https://drive.google.com/uc?export=view&id=1hBZ2usqU83qBfDb4rL8NqBSTI2dtgJCi",
            "https://drive.google.com/uc?export=view&id=1UAM7aO3VqN7EaS8beWlu5B5I1AdYC19V",
            "https://drive.google.com/uc?export=view&id=11RyacacRF5gdY-qPWkSU8dxKWWiRlsFi",
            "https://drive.google.com/uc?export=view&id=1J-74jRrrmvlZLmITQk24Xxxga1HtdAbw",
            "https://drive.google.com/uc?export=view&id=1s2-D9Fc9zyAUg7-cRmJzK1ZxRYKK6iR3",
            "https://drive.google.com/uc?export=view&id=10A2NLu3QJ0oALnjgg_8yhL65fOePZDwK",
            "https://drive.google.com/uc?export=view&id=13ZPEogx4T9h9XtbSAs3fs97x3k-3Lg3Q",
            "https://drive.google.com/uc?export=view&id=1DZno3fECb4NZ1ejue5iYqMMtBqiuDCAz",
            "https://drive.google.com/uc?export=view&id=1dmyHMS-3G2SxAOZnnzBCNifjP-4kaIx1",
            "https://drive.google.com/uc?export=view&id=1omXcFajdPTIsnOhGdii6GTlwyzOQfKHS",
            "https://drive.google.com/uc?export=view&id=1i9cwbMjSIX4abxJwrN1TPr7_0r9Pd_d4",
            "https://drive.google.com/uc?export=view&id=1prBP4cefUAOUMhivZITzMXqBgZtbnOXQ",
            "https://drive.google.com/uc?export=view&id=12CTye5i7aEkiTHIh3cPuNAcdUZqNcO0l",
            "https://drive.google.com/uc?export=view&id=1xMuiCQnPYLLE8p8qsXj2FuyUGo50XtAz",
            "https://drive.google.com/uc?export=view&id=1YJjtlo_cN44_mRYreL_LAqYZQABngnsN",
            "https://drive.google.com/uc?export=view&id=1cXyag9iieLDAu1lj1o7Zp2GmLtOZxQwR",
            "https://drive.google.com/uc?export=view&id=1yqnfSijS_R_3bMx6HZcryEsBfkYNozor",
            "https://drive.google.com/uc?export=view&id=1Dvds_vjE2MZ7IQiLFZ7kySAq2YlDoQ1e",
            "https://drive.google.com/uc?export=view&id=1o36J8nfT-7P_WbJordRxcFjHkfCnbvjx",
            "https://drive.google.com/uc?export=view&id=1KOW04ZYmqDvIEZZoy4RrOoteamQw6lmO",
            "https://drive.google.com/uc?export=view&id=1idPBoJHJyaDzGlf8CDDIZvtQpIoT8X21",
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
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ciu_1KXc0PqdBjJwKlgNRFXLVPmmfee3",
            "https://drive.google.com/uc?export=view&id=1TmTVSJvMC5YWy_6BQVb2qZPTcN-gh1qn",
            "https://drive.google.com/uc?export=view&id=1vCdyqfOvWT4Z-LVoaNrP0O0yI8a7pXaI",
            "https://drive.google.com/uc?export=view&id=1Tz3Nz4LybjYSp785QjU5HX7BbK6v3V7-",
            "https://drive.google.com/uc?export=view&id=16chYqSDsZlH0Z8pLW0MdP_kKvabUEAbA",
            "https://drive.google.com/uc?export=view&id=1prgtL_YhuPfNySFjWTXmf2xVdpTXnXPX",
            "https://drive.google.com/uc?export=view&id=1T2twHTF3FrP75P5b1eswVEjUl7iS2VNq",
            "https://drive.google.com/uc?export=view&id=1wLDB9HAtYKxmHe7HW6bgmfJAQw5EeIVk",
            "https://drive.google.com/uc?export=view&id=1OqN0d3bqudR0fvJAfOPjzezO9B5_gIcH",
            "https://drive.google.com/uc?export=view&id=1OMKj1n27uqSpDJAlyTIm_750QL5kCglF",
            "https://drive.google.com/uc?export=view&id=1f563X_ZEcOMgI7YaD8WIB_grDCAq-BR_",
            "https://drive.google.com/uc?export=view&id=1ptJdJ6gDMRb9CjTnAqj_It9cDoYIKZLo",
            "https://drive.google.com/uc?export=view&id=1NKN53DYW7k6IWdsV_k3G6VM-dOcUgtLg",
            "https://drive.google.com/uc?export=view&id=1_RtxTblWnxGtdu452T2TnHzLkVNC84qL",
            "https://drive.google.com/uc?export=view&id=16sv_NB_t3vDZOL81QVXcKOSMngu-tdi_",
            "https://drive.google.com/uc?export=view&id=1a3L5mJu7Zxk-uxwlAiGwKd6VGT_mOVyU",
            "https://drive.google.com/uc?export=view&id=1mf_NceDM0ncl-AkwVHb7F6wxGD2SkEkA",
            "https://drive.google.com/uc?export=view&id=1nttt3gMQEzYEnPUPX0DHUqrYU4XJ0r6e",
            "https://drive.google.com/uc?export=view&id=1Z03g_1HQpl_wI63GO8z2EbUxGP78FmlB",
            "https://drive.google.com/uc?export=view&id=1SzCgs14BSGrdb0NtWuKjZQSArJa7c2LL",
            "https://drive.google.com/uc?export=view&id=1WJdc9sf6is-0ITGWBrU7mbQ5DWCgxib-",
            "https://drive.google.com/uc?export=view&id=1xtykxoEXN906HlL859XgiaV2ZD-MrhYJ",
            "https://drive.google.com/uc?export=view&id=1CxiBqS2pAQGnpvGPdHdhXgY5og2H5T56",
            "https://drive.google.com/uc?export=view&id=1YLN8t9g6n6Yaj7HOml9qwJW0M_X-SIsN",
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
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Wly6PKT3LwZYCR8mfOqwPp4SFbjmx_aQ",
            "https://drive.google.com/uc?export=view&id=1ywiTPrCMs9b2zzt4ZM6UCbMl3vt6w-1g",
            "https://drive.google.com/uc?export=view&id=1fEBN6cVBTCU_DUGRlp024CeH-LIFlhMO",
            "https://drive.google.com/uc?export=view&id=1zXNijIPHCJVm25QBcf7kVLSBpsySfsJ4",
            "https://drive.google.com/uc?export=view&id=1u84_3PNnnuU6GSOLO9-Asr9V-DxhV7v9",
            "https://drive.google.com/uc?export=view&id=1MRyfeogoxRZHGf_rfnQolR2Jm81OtnHE",
            "https://drive.google.com/uc?export=view&id=17wgdIQpPqTl1UXATT95aQ4BTRiPqfxQY",
            "https://drive.google.com/uc?export=view&id=1tph33UDF5itGLHJvLJS42bs88Z5wKuqH",
            "https://drive.google.com/uc?export=view&id=1msj0hLLXvMWyhFY1ta-FOwLTm9Ryg6T-",
            "https://drive.google.com/uc?export=view&id=1QBKNsl85dApWDq4nCIi0_mSFtyWFma8S",
            "https://drive.google.com/uc?export=view&id=12LrVQVwjU_B-oQ99vv5WKo9zDpoy3oQc",
            "https://drive.google.com/uc?export=view&id=1uL6laBTEEulid_M4T0xjCDviNqU-Tqqq",
            "https://drive.google.com/uc?export=view&id=1NXQtHfki51MRGc9mO9Ulo64sDfG7m-UL",
            "https://drive.google.com/uc?export=view&id=12EdBV7hb15rLGR2LdJ6FMZjRCg1upatd",
            "https://drive.google.com/uc?export=view&id=1AUioEIwJYkMf2G5yWbSMMyfHmE1ygyYo",
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
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Selalu menjadi penengah dan penguat bagi kami semua di internal.",
                "pesan":"Terima kasih telah menjadi garda terdepan untuk kesejahteraan kami."
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota.",
                "pesan":"Semoga kakak selalu bisa menjadi perekat bagi kami semua. Semangat terus!"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "-",
                "umur": "-",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "-",
                "kesan": "Terima kasih sudah membuat suasana internal himpunan menjadi hangat dan nyaman.",
                "pesan":"Teruslah jaga kehangatan dan kekeluargaan di himpunan kita, Kak."
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "-",
                "umur": "-",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "-",
                "kesan": "Kemampuan kakak dalam menjaga soliditas tim internal sangat luar biasa.",
                "pesan":"Semangat selalu dalam menjalankan program kerja untuk internal kita, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TPEVO0HRgwmNbqpxEyBSpLdKxyWwK1nJ",
            "https://drive.google.com/uc?export=view&id=14DYjMioyko1_TGkfVnBKYwm5g-M5MQke",
            "https://drive.google.com/uc?export=view&id=1xAndcxmSi1Y_-F5lFzRmu44XgFhUv9Ct",
            "https://drive.google.com/uc?export=view&id=1CkZI5Q1YPGbHc9QoUGmqROSgqUl82kkV",
            "https://drive.google.com/uc?export=view&id=1mT8_Qsl42hLe_1qkwDBjzU7FhFd-6qyl",
            "https://drive.google.com/uc?export=view&id=1DVcK0EjnJ7AuXZpAz9gOj1uXfOKffd-8",
            "https://drive.google.com/uc?export=view&id=1vDhVvp1jTAFA1Lbi6atU9P51DHHZjsfD",
            "https://drive.google.com/uc?export=view&id=1cArklQIkVRtR6NrYLmAtPBP83U135EAZ",
            "https://drive.google.com/uc?export=view&id=1DThmwKOiYi_nm7VgUJHyIv-ubeFNkp1_",
            "https://drive.google.com/uc?export=view&id=118UMYY923z-0HtWTtUETKUYzcujw_9yj",
            "https://drive.google.com/uc?export=view&id=1XmTC7z4VAv6SqiPtxh9HJ0krUgFbAW-x",
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
                "kesan": "Kakaknya asik dan seru.",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Senang bisa berkenalan dengan kakak.",
                "pesan": "Semoga sukses selalu kuliahnya!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Kakaknya ramah dan baik.",
                "pesan": "Sehat selalu ya, kak."
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif.",
                "pesan": "Semangat terus kuliahnya, kak!"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Senang bisa bertemu dengan kakak.",
                "pesan": "Semoga semua urusannya dilancarkan."
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Sukses selalu untuk kakak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Kakaknya asik diajak diskusi.",
                "pesan": "Terima kasih atas bimbingannya, kak."
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya, kak!"
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu, kak!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya sangat ramah.",
                "pesan": "Jaga kesehatan selalu, kak!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Terima kasih kak atas bantuannya.",
                "pesan": "Semangat dan sukses selalu!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YS81_QP0li5fcLpTKCI3neKLO4Ko7jBs",
            "https://drive.google.com/uc?export=view&id=1qWxRoCVFI1qOT219TBTJQ9cy3TKa8gFQ",
            "https://drive.google.com/uc?export=view&id=1TAoej5aJQQv4WUDExzwCI-ByQXP--Z4k",
            "https://drive.google.com/uc?export=view&id=1nsQPaddQeTTdUjov1naisUumLQBeqsgP",
            "https://drive.google.com/uc?export=view&id=1f-oY55tpfo9N2tH51cpQd8DJ7z_n_8Ux",
            "https://drive.google.com/uc?export=view&id=1L3PHkh7o-K_yxWPDvK6y0XiAviSQVCxu",
            "https://drive.google.com/uc?export=view&id=1wHaIVQAT8opaWYfvyRhp3UhFMs3dFtp6",
            "https://drive.google.com/uc?export=view&id=1ntM9I0LPM9p4JWdnyRfB5-tAmqMYC2on",
            "https://drive.google.com/uc?export=view&id=1VmubPz7QTXcTOoT_qojYnwnRQ83_tbcM",
            "https://drive.google.com/uc?export=view&id=1Uc8UrJvgksDGvk9xlSHVAP-cJ3cpChFV",
            "https://drive.google.com/uc?export=view&id=1RlCgIT4EiM0OE0lplqHFKup4tM7SpBxx",
            "https://drive.google.com/uc?export=view&id=1ROcEbZVvqOIvGLQyiSPxmRE1xVy9B__a",
            "https://drive.google.com/uc?export=view&id=1i1SObt680VStkbboyUzF5VJj2LWMHD7P",
            "https://drive.google.com/uc?export=view&id=11N7OvD5iTM3zaihc7XqS1rPwrrg10-4T",
            "https://drive.google.com/uc?export=view&id=1-zf80ej3rBaAXZ80hQMZbmUDLSFBnXYO",
            "https://drive.google.com/uc?export=view&id=1dCBKN1PXV9WsZgc99a05Bz24F2xuyRCP",
            "https://drive.google.com/uc?export=view&id=1L-ahrLnVTv8FMOG5wwOOS-8SwKonQOma",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

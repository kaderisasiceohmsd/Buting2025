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
                "alamat": "Jl.Lapas Raya",
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
                "asal":"Nusa Kambangan",
                "alamat": "Lapas, Belwis",
                "hobbi": "Melarikan diri",
                "sosmed": "@Jeremia_s_",
                "kesan": "Abangnya asik dan juga gampang diajak ngobrol",
                "pesan":"Sukses selalu kuliahnya, Bang"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
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
                "hobbi": "Jualan Pancing",
                "sosmed": "@Renishapg",
                "kesan": "Orangnya seru, humble, dan baik banget.",
                "pesan":"Semangat dan sukses selalu, Kak"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukkan",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya baik, dan juga kalem",
                "pesan":"Semangat terus menjalani hari-harinya, Kak"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci Baju",
                "sosmed": "@dhruchyo",
                "kesan": "Abangnya baik, dan juga ramah",
                "pesan":"Tetap jadi pribadi yang murah senyum"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya baik, ramah, juga sering ngelive di tiktok",
                "pesan":"Semangat ngelive dan juga jaga kesehatannya, kak"
            },
            {
                "nama": "Ghivaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin rido main padel",
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
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya cukup pendiam, tapi asik",
                "pesan":"Semangat dan sukses selaluu, Bang."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "1224500065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya asik, seru waktu diajak ngobrol, dan juga murah senyum",
                "pesan":"Sukses selalu, dan juga semangat menghadapi hari-harinya, Kak"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "12345085",
                "umur": "19",
                "asal":"Teluk kuandama",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j_eesie",
                "kesan": "Sangat berkesan, orangnya humble, cantik, sering ngajak bercanda, salah satu orang yang terlibat di cerita penting hidup aku, layaknya seorang kakak kepada adiknya",
                "pesan":"Tetap jadi pribadi yang humble, peduli ke sesama, dan yang terpenting jangan lupa selalu bahagia. ekhemmm Bingxue satu bisa kali kak, hehe"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya Baik, Pendiam, dan ramah ke semua orang",
                "pesan":"Selalu jadi pribadi yang pantang menyerah"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya asik dan juga ramah",
                "pesan":"Jangan lupa jaga kesehatan, Bang."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Orangnya baik, dan kalem banget.",
                "pesan":"Semangat terus kuliahnya, Kak!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Rantauprapat",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
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
                "alamat": "Tanya caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya seru dan juga bisa diajak bercanda",  
                "pesan":"semangat selalu bang dalam menyampaikan Aspirasi massa Sains Data!!!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan musik",
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
                "hobbi": "Live instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya asik dan juga positif vibes",  
                "pesan":"semangat terus jadi manusia baik !!!"
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
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
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "Terima kasih atas bimbingannya selama ini, Kak.",
                "pesan": "Semoga kami bisa meneladani semangat kakak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solo",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapasha_",
                "kesan": "Pertama kali ngobrol banyak bareng kak allya di angkringan. Diluar kaderisasi, ternyata kak Allya seru juga diajak diskusi, selalu memberikan arahan atas pendapat dan saran yang diajukan",  
                "pesan":"Tetap jadi pribadi yang selalu menginsiprasi banyak orang dan semangat terus menjalani hari-harinya, Kak."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Membaca",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Salah satu orang yang menginspirasi dengan segala pendapat pribadinya",
                "pesan": "Semangat selalu, dan juga semoga impian menjadi Presma tahun ini terwujud, Bang"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Deket kos Dapa",
                "hobbi": "Cari ribut",
                "sosmed": "@arientakhsnl_",
                "kesan": "Pertama kali kenal kak Arin karena satu organisasi. Kakaknya baik, ramah, punya senyum yang manis, juga selalu langganan jadi sekretaris di setiap kegiatan",
                "pesan": "Sukses selalu untuk kakak, dan juga semangat selalu kak"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jahilin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Aslinya bang Dapa humoris, sering ngajak bercanda semua orang",
                "pesan": "Selalu jadi pribadi yang humoris dan juga selalu jadi pribadi yang rendah hati."
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Hobinya banyak",
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
                "hobbi": "Membaca",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakaknya humble, baik, juga ramah ke semua orang.",
                "pesan": "Jaga kesehatan dan semangat seallu kuliahnya, Kak."
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Suka ngader",
                "sosmed": "@nobelnizam",
                "kesan": "Abangnya baik, dan juga perhatian ke adik-adik tingkatnya",
                "pesan": "Selalu humble dan juga selalu mengayomi orang lain, Bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "Tegas dan juga bisa diajak bercanda santai",
                "pesan": "Sukses selalu, dan semangat menggapai impiannya, Bang."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Airan",
                "hobbi": "Marah",
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
                "asal":"Lampung Timur",
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
                "hobbi": "Apa aja",
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
                "hobbi": "Ngapain aja",
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
            "https://drive.google.com/uc?export=view&id=11352cyvSdUmKq4Qlv8k_L_beMISP27nk",
            "https://drive.google.com/uc?export=view&id=1H_Z911iKtWpa47em12oKpahhNpb6jiFm",
            "https://drive.google.com/uc?export=view&id=1MIqG8SNo5BwxA8tKXG7FeFWlSOqgSFQD",
            "https://drive.google.com/uc?export=view&id=16NRKDawOrq0R5qhGKNkpg6vygA9CCxoC",
            "https://drive.google.com/uc?export=view&id=18HdQ6VvQkIXX7IG5r9JNRl4ohzVQaQcZ",
            "https://drive.google.com/uc?export=view&id=1TgBn2qj0SI6E5ViwSsq0Bfv0KAzS5cio",
            "https://drive.google.com/uc?export=view&id=1Gzh1u2pHxVyTyMWt2PsG6yhPDYBY7tfG",
            "https://drive.google.com/uc?export=view&id=18aCc4994FGu67NB2axp5hzAL0y0Ii6c2",
            "https://drive.google.com/uc?export=view&id=1Fhh24jyYY3L4T7ty7d4qMkA3ophl8fq9",
            "https://drive.google.com/uc?export=view&id=1p-twrbQNMSc8loYiBoTeYbg24dfnoDE1",
            "https://drive.google.com/uc?export=view&id=1KwnPS2ltH9HW-jTPbJt8YX59dByaN5kO",
            "https://drive.google.com/uc?export=view&id=1U3-rqsh5lH3J9VTebiNj_fBQGxbIqXNC",
            "https://drive.google.com/uc?export=view&id=1FM2xUfy489q1a00rcVoJINEeq5oBiilA",
            "https://drive.google.com/uc?export=view&id=1uGh1MrwSkhpGQSLJQn60KwoLSr5VgSST",
            "https://drive.google.com/uc?export=view&id=1KLishoQV1Df7pU8761U-D8XQzjaugGcT",
            "https://drive.google.com/uc?export=view&id=1tNuZX3PWgR0EFY0WwEZpyRjpp59A8RYG",
            "https://drive.google.com/uc?export=view&id=1K8giG8VS4sCCxdN09TiWNGXc2Tqv029E",
            "https://drive.google.com/uc?export=view&id=1kTI2xXm_5o_0Tq0ju12H0qzkNlvTS61z",
            "https://drive.google.com/uc?export=view&id=1V7VZgJxYOnpBMbDPNmKIyc1WVIwfudMl",
            "https://drive.google.com/uc?export=view&id=1VoHejzPVeiQHsjIgeDKfwERk8vjzLFEV",
            "https://drive.google.com/uc?export=view&id=1KwnPS2ltH9HW-jTPbJt8YX59dByaN5kO",
            "https://drive.google.com/uc?export=view&id=1eY8a9dTDX9ijuvpoOIrv-rECYDuv1dXv",
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
                "kesan": "Keliatan cool, tapi ramah aslinya",
                "pesan":"Tetap jadi panutan yang keren, Bang!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Kakaknya tenang, bikin suasana adem banget.",
                "pesan":"Tetap jadi contoh yang baik ya, Kak."
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Seorang Mentor sekaligus seorang Abang yang selalu sopport adiknya disaat sedang berjuang mencapai impiannya, walaupun pada akhirnya kalah",
                "pesan":"Makasih ya bang udah selalu support dan juga terimakasih sudah selalu mengarahkan ke hal-hal baik. Sehat selalu, Bang Regi."
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
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
                "kesan": "Abangnya keren, tapi tetap rendah hati.",
                "pesan":"Semoga sukses terus ke depannya."
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Pertama kenal bang fadil dari DuGen, awalnya canggung dan males ngobrol karena keliatan ga welcome dari mukanya. Tapi setelah kenal lebih deket, kaget dikit. Hobi nya asbunin orang. Saya satu diantara banyaknya orang yang jadi korban keasbunan beliau"
                "pesan":"Selalu rendah hati dan juga selalu jadi orang yang bisa mengayomi ya, Bang."
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya agak serius tapi perhatian juga.",
                "pesan":"Jangan lupa santai kadang-kadang ya."
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "JL. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya pendiem, tapi aslinya baik.",
                "pesan":"Semangat terus dan jaga kesehatan."
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya ramah, gampang diajak ngobrol.",
                "pesan":"Jangan lupa istirahat yang cukup."
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kakaknya lucu, suka bikin suasana cair",
                "pesan":"Terus jadi kakak panutan ya!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan Bernyanyi",
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
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin musik, dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
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
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": " Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19BUsmOHwoyUQgthpzw07RlI32LH_rEff",
            "https://drive.google.com/uc?export=view&id=1Dv_dIkl2gxx9ZA9m8W_S1YrQdRSG5_T6",
            "https://drive.google.com/uc?export=view&id=1eVpLNEgKTZh3dqL13fWIHLSrCsvtIUsO",
            "https://drive.google.com/uc?export=view&id=1ASL760I2lzw3fb4efxNXh9oeLf0DYdjb",
            "https://drive.google.com/uc?export=view&id=1CgGY7ZI0jbSwKaaMBbpY_WnR1TUD2Jwj",
            "https://drive.google.com/uc?export=view&id=1hUHJ3jgnwt_EN4FPInJTzQARazBn922R",
            "https://drive.google.com/uc?export=view&id=1j1yCo4A4wqBXt8iIde2xSoqimFUKYVAK",
            "https://drive.google.com/uc?export=view&id=12StSJlTHmMrQ6fw4a3_HVro1RM0AoCXc",
            "https://drive.google.com/uc?export=view&id=1Iino7GWcZm9G29gomDeAEJ-ygaOeqIE4",
            "https://drive.google.com/uc?export=view&id=1Rfk1bukeTfiebYT7nbGbMOZ183bXXl-Y",
            "https://drive.google.com/uc?export=view&id=146L5dKfweh06_noLOyYrm6EYWsJrPpm0",
            "https://drive.google.com/uc?export=view&id=1PJexJ5JWmMP4jWLY2GrnW8TWSmRcu70p",
            "https://drive.google.com/uc?export=view&id=19JG-7YSaFtytS1SHvpAMWwkTKAqpDVR0",
            "https://drive.google.com/uc?export=view&id=1TXt9pZZliVPW26eJCHHxIiXzfr3n6mA7",
            "https://drive.google.com/uc?export=view&id=1pGka6Xooux5rTG2pNBtok8-jxCDb2KyU",
            "https://drive.google.com/uc?export=view&id=1xreoK1to7EGtTOBXD_fnkO2Lu3TOolgX",
            "https://drive.google.com/uc?export=view&id=1J7PKIT2b9RbheArdiTgEGU8_vzAbss9p",
            "https://drive.google.com/uc?export=view&id=1wloFICt5rXG6ozOi5BJo-dTjb5to0aKi",
            "https://drive.google.com/uc?export=view&id=1iFHDG61Rnsis0IUm0xQ8sdNLt12yQ1o8",
            "https://drive.google.com/uc?export=view&id=1gvDzS3rnip0Ja67JQnC8alMxyb-X5IX-",
            "https://drive.google.com/uc?export=view&id=1WEmsQatK5L7PPvxoGID_Bi3r14uVz49t",
            "https://drive.google.com/uc?export=view&id=19p2xuiU3nZZuSQzRR2G02RaxH1wYMJIs",
            "https://drive.google.com/uc?export=view&id=1tZ2cDslJyGj54dnObTdow4r3ugh2k-4U",
            "https://drive.google.com/uc?export=view&id=10oNvm_V3OKTSv5_LdURykXYdDZ_MiA-9",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Sebelah warjo",
                "hobbi": "Memancing",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "Abangnya pendiem, tapi aslinya baik",
                "pesan":"Semangat terus dan jaga kesehatan, Bang."
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sukabumi, Jawa Barat",
                "alamat": "Depan GH",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya lembut tapi tegas juga.",
                "pesan":"Semangat terus dan jaga diri"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Menerbitkan Artikel",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya ramah, gampang diajak ngobrol.",
                "pesan":"angan lupa istirahat cukup ya, Kak."
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Cibitung",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Gangguin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya kalem, tapi lucu juga.",
                "pesan":"Semoga hari-harinya selalu bahagia."
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Hasan 1, Sukarame",
                "hobbi": "nonton AGZ",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya ceria, bikin suasana jadi hidup.",
                "pesan":"Tetap semangat dan positif terus, Kak."
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya perhatian dan baik banget.",
                "pesan":"Makasih udah banyak bantu ya, Kak!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "21",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bengong di embung c",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakaknya tenang, bikin suasana adem.",
                "pesan":"Tetap sabar dan semangat terus!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3, ITERA",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya cuek, tapi peduli banget.",
                "pesan":"Jangan berubah, tetap keren ya, Bang."
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya seru, gampang akrab juga.",
                "pesan":"Semoga sukses terus ke depannya."
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450024",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya manis dan enak diajak ngobrol.",
                "pesan":"Semoga selalu diberi kebahagiaan!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Travelling",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya tenang, bikin suasana adem.",
                "pesan":"Tetap sabar dan semangat terus, Kak!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya bijak, tenang, dan sabar.",
                "pesan":"Semoga selalu bahagia, Bang hebat!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "nonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya cantik, tapi nggak sombong.",
                "pesan":"Semoga sukses terus ke depannya, Kak."
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Tetangganya kak Yo",
                "alamat": "samping mie aceh",
                "hobbi": "banyak",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya sopan, enak diajak diskusi.",
                "pesan":"Makasih udah banyak bantu ya, Bang."
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "menjejak desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakaknya ceria, senyumnya bikin semangat.",
                "pesan":"Jangan capek jadi penyemangat kami, Kak."
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya kalem, bikin nyaman suasananya.",
                "pesan":"Semoga sehat selalu ya, Kak!"
            },
            {
                "nama": "Khanzanatil ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khanzanatil_ilmi05",
                "kesan": "Kakaknya humoris tapi tetap sopan.",
                "pesan":"Tetap ceria dan rendah hati, Kak."
            },
            {,
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Mencari jurnal scopus",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya anggun tapi juga lucu.",
                "pesan":"Tetap semangat dan percaya diri, Kak."
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya manis, senyumnya nular banget.",
                "pesan":"Jangan lupa jaga diri ya, Kak."
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya cantik, tapi nggak sombong.",
                "pesan":"Semoga sukses terus ke depannya, Kak!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abangnya pendiem, tapi aslinya baik.",
                "pesan":"Semangat terus dan jaga kesehatannya, Bang."
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakaknya ceria, bikin suasana jadi hidup.",
                "pesan":"Tetap semangat dan positif terus"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya sabar banget sama adik tingkat.",
                "pesan":"Makasih udah ngarahin dengan baik, Kak."
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "122450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Rafting",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya nyantai tapi bisa diandalkan.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Bang.."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1darXychxG3h8ib7ilD8B7xBh-YvaAIF0",
            "https://drive.google.com/uc?export=view&id=1TTNZ8hecWbu9imw3OYTDYZIKXN8K0AIw",
            "https://drive.google.com/uc?export=view&id=1OEXP7lTPLfe6XJ83s7QzGQzvsXyAlXnG",
            "https://drive.google.com/uc?export=view&id=1s0-pSFz4bMKsUszl9W1zpC-kPwjsnYDn",
            "https://drive.google.com/uc?export=view&id=1u4uo8mjK6sx-wZBugWrCIiaogZngDSfp",
            "https://drive.google.com/uc?export=view&id=1OVJowZlSWvOEPF9GWF5HlZvdJXx61CtN",
            "https://drive.google.com/uc?export=view&id=1kaoEboYizDjqr6LuBVraE5jM3fOuDTP3",
            "https://drive.google.com/uc?export=view&id=1Y4EjZfjln1jgQNMhscpipqoHUZzibqdJ",
            "https://drive.google.com/uc?export=view&id=192vo6QZ1SovGAiu3bJs71vxqUUKWQJto",
            "https://drive.google.com/uc?export=view&id=1OE_yJ97Rf5arxoaBE94W7BBjbZrj4COS",
            "https://drive.google.com/uc?export=view&id=17FEw6mT9kXh3-fCosChp5buQvHGctL24",
            "https://drive.google.com/uc?export=view&id=1EzTOl7cp-lMNSmA2pU1Mm-PLBomCy5XJ",
            "https://drive.google.com/uc?export=view&id=1LtZxz2nez_v8eKBBlOCb6r-OXvdLO1cc",
            "https://drive.google.com/uc?export=view&id=1Dcwmzs5mzUnqLgypqRMNRcZw9PsSqMi4",
            "https://drive.google.com/uc?export=view&id=1Mk_3yUdJvEizMVEeqHq9TXk2NqLZ_hNn",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya tenang tapi perhatian banget.",
                "pesan":"Terus jadi inspirasi buat kami."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Senopati Raya",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya kalem, tapi nyenengin banget.",
                "pesan":"Tetap bahagia dan semangat terus, Kak."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya perhatian sama semua orang.",
                "pesan":"Makasih udah baik banget, Kak!"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Tanjung Karang",
                "hobbi": "Kulineran with Azza",
                "sosmed": "@mai_12",
                "kesan": "Kakaknya gampang akrab sama siapa aja.",
                "pesan":"Jangan lupa istirahat ya, Kak."
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Kulineran with May",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakaknya ceria, bikin nyaman ngobrolnya.",
                "pesan":"Semoga selalu bahagia dan sukses."
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya kalem tapi suka bercanda.",
                "pesan":"Tetap semangat jalani harinya ya."
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Jatimulyo",
                "hobbi": "Mancing",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya kalem, bikin suasana adem.",
                "pesan":"Terus jadi contoh yang baik ya, Bang!"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Abangnya sabar, nggak pernah marah.",
                "pesan":"Semoga selalu diberi kesabaran, Bang."
            },
            {
                "nama": "Zailani Satria",
                "nim": "124450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya cuek tapi peduli banget.",
                "pesan":"Semangat menjalani kesehariannya, Bang."
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Kotabaru",
                "hobbi": "Hiking",
                "sosmed": "@rexsander",
                "kesan": "Abangnya asik, punya vibe tenang banget.",
                "pesan":"Semoga hari-harimu selalu bahagia."
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450107",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya cantik dan kalem banget.",
                "pesan":"Semoga kariernya makin cemerlang."
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya sopan dan penuh semangat.",
                "pesan":"Jangan lupa istirahat cukup ya, Kak."
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya pendiem tapi aslinya lucu.",
                "pesan":"Semangat terus dan jangan capek"
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Bersenandung",
                "sosmed": "hanna_g_sinaga",
                "kesan": "Kakaknya asik, gampang nyambung ngobrolnya.",
                "pesan":"Semoga selalu bahagia dan sehat."
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda",
                "hobbi": "Main Rubik",
                "sosmed": "@zhrptsl",
                "kesan": "Kakaknya rajin dan tanggung jawab banget.",
                "pesan":"Semoga capai semua mimpinya ya, Kak"
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

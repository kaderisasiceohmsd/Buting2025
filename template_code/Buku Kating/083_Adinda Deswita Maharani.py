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
            "https://drive.google.com/uc?export=view&id=1FEDXhyeJ4ivPhJRZ7yygAWJ3HdhpYUH1",
            "https://drive.google.com/uc?export=view&id=1Ge16oTzJKfc1Hk-uM7VeNz9oCyGJF885",
            "https://drive.google.com/uc?export=view&id=1qPYpCJGRO_pjg0HWU6iKM4tCAitB9S0v",
            "https://drive.google.com/uc?export=view&id=1HVpuV9vdDTqhZWQYYe2S9zu1yRSgaSUC",
            "https://drive.google.com/uc?export=view&id=15TM8eIRM0---HBnc-vLZfI_qj1SxC57s",
            "https://drive.google.com/uc?export=view&id=1j-lA_Kr7neMfAjM2DNCqrgCZFs2kkSKH",
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
                "kesan": "Keren dan berwibawa banget, sangat mengayomi",  
                "pesan":"Semangat terus Bang menjadi ketua, semoga sukses nantinya"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Pemikirannya keren banget, sangat berwibawa",  
                "pesan":"Semoga kehidupan kuliahnya berjalan mulus"# 1
            },
             {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Moodbooster parah, lucu banget kakaknya bikin ketawa",  
                "pesan":"Semoga hari-harinya selalu penuh hal baik"# 1
            },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak positive vibes banget",  
                "pesan":"Semoga makin banyak hal baik yang diraih ke depannya"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Dari hobinya aja udah keliatan kakak lucu banget, moodbooster",  
                "pesan":"Semoga perkuliahannya berjalan lancar tanpa hambatan"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakaknya baik dan ramah banget, murah senyum",  
                "pesan":"Semoga semua target kak cepet tercapai!"# 1
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10g5zsF_sZBMvXQJ3yFWqbasNcCnrGQcy",
            "https://drive.google.com/uc?export=view&id=1gLG4jTu1CL5gIMsSBMnMx29Wad5wL0va",
            "https://drive.google.com/uc?export=view&id=1E8bF8oSTJ1GTsX9HPU8lEiqhKuKbVw06",
            "https://drive.google.com/uc?export=view&id=1UlTyS90gDLTF56Th1eIUwbVicutNCIr9",
            "https://drive.google.com/uc?export=view&id=11A8KoGTWlUGNouFP5FQWRUWObh6tn8vN",
            "https://drive.google.com/uc?export=view&id=1qnam_NFeqg491NkJYfGfsu1fzhuRXYHg",
            "https://drive.google.com/uc?export=view&id=1OhXR1nuCojD1FtYefPf7rzvsx7oKrC44",
            "https://drive.google.com/uc?export=view&id=145AFsG1UI08zWuA1BgqS_r_XGV0XLTZk",
            "https://drive.google.com/uc?export=view&id=1_TNgBApRxTHMHpEk2mHf0ucaoMqjucwU",
            "https://drive.google.com/uc?export=view&id=1few38C7Smn03p2rLgOICSvZ9R_R7EUBb",
            "https://drive.google.com/uc?export=view&id=1_U4wF8ere0teE6ORb4Mmc046fdEF_Wmd",
            "https://drive.google.com/uc?export=view&id=1zxjX-vn38csvAXusN9wPW0-t00KndB96",
            "https://drive.google.com/uc?export=view&id=1zi5Iycqmo_Ja5rS_MCAzlKibBlhYe98D",
            "https://drive.google.com/uc?export=view&id=1KE56zIS0LZCjzjuAF83xviuqR-eBlC_M",
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
                "kesan": "Abangnya asik dan ramah.",
                "pesan":"Sukses selalu ya "
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Seru orangnya.",
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
                "kesan": "Kakaknya asik dan lucu.",
                "pesan":"Sukses selalu untuk semuanya ya kak!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Semangat terus dan jangan mudah menyerah!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Senang bisa kenal.",
                "pesan":"Jangan lupa jaga kesehatan bang."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Orangnya seru dan baik banget.",
                "pesan":"Semangat terus dan jangan mudah menyerah!"
            },
             {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Pembawaannya positif dan menyenangkan.",
                "pesan":"Semoga kita bisa bertemu lagi."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya seru dan santai, ngobrolnya enak banget.",
                "pesan": "Semoga terus sukses dan makin banyak hal baik yang dicapai."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya humble banget, gampang diajak ngobrol.",
                "pesan":"Semoga studinya lancar terus ke depannya."
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya asik dan ramah.",
                "pesan":"Semoga semua rencana dan cita-citanya tercapai."
            },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya asik, punya cara ngomong yang to the point.",
                "pesan":"Semoga langkah-langkahnya selalu dimudahkan."
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Ramah banget, gak susah diajak ngobrol walau baru kenal.",
                "pesan":"Semoga terus jadi pribadi yang rendah hati dan menyenangkan."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya punya vibe kalem tapi tetap keren.",
                "pesan":"Semoga semua impian dan targetnya bisa terwujud."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya komunikatif, gampang banget nyambung obrolannya.",
                "pesan":"Semoga makin banyak hal baik yang datang ke depan."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10pKX06mcgDL6X1HJ2-jQ33nCSXPe0Cos",
            "https://drive.google.com/uc?export=view&id=1wJCsN2Tbgn4kxVfu6IkrbazBHAwWwoiV",
            "https://drive.google.com/uc?export=view&id=1LxvginnWNzlSAqIOlxvwLomVyhKYeJec",
            "https://drive.google.com/uc?export=view&id=1QNKwgmKn8mBdg6BKS3KK5j6mlriBNjXW",
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
                "kesan": "Asik dan terbuka banget, bikin ngobrolnya gak canggung.",  
                "pesan":"Semoga makin sukses dan terus jadi inspirasi buat juniornya.

13."# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya punya cara berpikir yang matang dan bijak.",  
                "pesan":"Semoga terus berkembang dan selalu dimudahkan dalam setiap langkah."# 1
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya sopan dan beretika banget, respect!",  
                "pesan":"Semoga karier dan kehidupannya makin stabil dan maju."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zf5fuYBK5gvrJucp19BW__SI0Lx830K_",
            "https://drive.google.com/uc?export=view&id=1oV0yobqB3H9dHYVab6kdqwkot4amDh8X",
            "https://drive.google.com/uc?export=view&id=1J_gkzMJT5AslOK1dJdcKuucb1uhBtlsQ",
            "https://drive.google.com/uc?export=view&id=1MQ-VaZLRWuANBUxLRsIrm_NTQTJENa-_",
            "https://drive.google.com/uc?export=view&id=1EyNV1ZITrJoqh0QJ2c3xnOO2tsXyqKQ-",
            "https://drive.google.com/uc?export=view&id=1r7sD94WipNOK8f38po1LAAaVizpwt7qL",
            "https://drive.google.com/uc?export=view&id=1zGeBuPCul-3k9ZTskA16yusbPyU3lfNs",
            "https://drive.google.com/uc?export=view&id=1zF7nRglbuBMSGTCM7gdtmt2nNQML2pVV",
            "https://drive.google.com/uc?export=view&id=1wCZjJzYsPYTDTSS9wTiqEu60Y6mPRbjl",
            "https://drive.google.com/uc?export=view&id=1Eq5Yke_onucp3Q8udvBS6l9PqhFml65i",
            "https://drive.google.com/uc?export=view&id=1X2IC_SxYxnA3CjpO8I4olTibzf01II6f",
            "https://drive.google.com/uc?export=view&id=1F62ucZn54RUXDz1rMboA7AJBBoj3tZiv",
            "https://drive.google.com/uc?export=view&id=1Sug3tsNrfhgUbsehagHrbm4L5J7pRGdg",
            "https://drive.google.com/uc?export=view&id=1SzW9Ju08fizPNaWcTYbl1T-w6KW8gZsF",
            "https://drive.google.com/uc?export=view&id=1w2xfTLjR0B3CMvNckRIAY6fQM6FFfjRD",
            "https://drive.google.com/uc?export=view&id=1Abe6yKBbR-XuBTpq3XmbJjw_34lsYSb8",
            "https://drive.google.com/uc?export=view&id=12hIiWDPmU6YiLBUDzgQfBNLQU3Zxt-V2",
            "https://drive.google.com/uc?export=view&id=1DwRoEMJxmBFyf6jGfkCECkpvigMiwfql",
            "https://drive.google.com/uc?export=view&id=14KtafGUD4p2jJAhJFnBJpZQfB5Gs58yJ",
            "https://drive.google.com/uc?export=view&id=13I-DbLmX3ZHcmfti3CqkJYuFCHIZUiha",
            "https://drive.google.com/uc?export=view&id=1Ya6B6Yx7C5GHyk_MbPMKUG2TYGkuVujA",
            "https://drive.google.com/uc?export=view&id=14hFXuoObYa-S-CCqhRXV-UDAGk4jrt9V",
            "https://drive.google.com/uc?export=view&id=1NYyoxfawri_llW_L8HUde9rlJTnsbjv5",
            "https://drive.google.com/uc?export=view&id=13840rdXcLsGH1EfhR3kePIYWqRqiC654",
            "https://drive.google.com/uc?export=view&id=1aPiVPeZwhS1QRFBn4j13bOmWyFW-La4D",
            "https://drive.google.com/uc?export=view&id=1xWQKQEOuyd1fhknaXw6ajiNXPSldnT4y",
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
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Sikapnya tegas dan disiplin, menjadi panutan bagi kami.",
                "pesan": "Terima kasih atas ilmunya, semoga kakak sehat selalu."
            },
             {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Senang mendapat arahan dari kakak, sangat memotivasi.",
                "pesan": "Semangat terus dalam menjalankan amanahnya, Kak!"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Pembawaannya tenang dan bijaksana.",
                "pesan": "Sukses selalu untuk kakak, ditunggu arahan selanjutnya."
            },
             {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Kakak sangat berwibawa dan mengayomi.",
                "pesan": "Mohon bimbingannya selalu, Kak. Sehat dan sukses terus!"
            },
              {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Pembawaannya kalem tapi tetap mudah diajak komunikasi.",
                "pesan": "Semoga segala urusannya selalu dimudahkan."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Sikapnya tegas dan disiplin, menjadi panutan bagi kami.",
                "pesan": "Terima kasih atas ilmunya, semoga kakak sehat selalu."
            },
              {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Senang mendapat arahan dari kakak, sangat memotivasi.",
                "pesan": "Semangat terus dalam menjalankan amanahnya, Kak!"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Ramah dan terbuka, enak diajak ngobrol walau baru kenal.",
                "pesan": "Sukses selalu untuk kakak, ditunggu arahan selanjutnya."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak sangat berwibawa dan mengayomi.",
                "pesan": "Semoga semua target yang direncanakan bisa tercapai."
            },
             {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Kakaknya komunikatif dan nyenengin pas diajak ngobrol.",  
                "pesan":"Semoga terus jadi pribadi yang positif dan menginspirasi."# 1
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakaknya kelihatan bijak dan dewasa dalam berbicara.",  
                "pesan":"Semoga harinya selalu lancar dan penuh keberuntungan."# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Sopan, enak diajak ngobrol, dan kelihatan rendah hati.",  
                "pesan":"Semoga makin sukses dan tetap jadi pribadi yang baik."# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Gaya bicaranya jelas dan sopan, keren banget.",  
                "pesan":"Semoga terus sukses dan selalu diberi kemudahan."# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kalem tapi tetap menyenangkan pas ngobrol.",  
                "pesan":"Semoga hari-harinya selalu lancar dan penuh semangat."# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Ramah tapi tetap berwibawa, keren banget sih.",  
                "pesan":"Semoga makin sukses dan tetap rendah hati selalu"# 1
            },
             {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Sopan dan berwibawa, kelihatan punya karakter kuat.",  
                "pesan":"Semoga langkahnya selalu dimudahkan di tiap proses."# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya tenang tapi tetap punya aura ramah.",  
                "pesan":"Semoga segala urusannya selalu dipermudah dan dilancarkan."# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Pembawaannya santai tapi tetap profesional.",  
                "pesan":"Semoga makin sukses dan terus jadi inspirasi buat adik tingkat."# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Ramah dan punya cara bicara yang enak didengar",  
                "pesan":"Semoga semua harapan dan impiannya bisa terwujud."# 1
            },
             {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakaknya kalem, tapi jelas punya pemikiran yang matang.",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Kakaknya cool tapi tetap easy going.",  
                "pesan":"Semoga ke depannya makin banyak kesempatan baik yang datang."# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakaknya punya kesan tenang tapi tetap menyenangkan.",  
                "pesan": "Semoga terus jadi pribadi yang positif dan menginspirasi."# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "Semoga terus diberi kemudahan di setiap langkah."# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Kakaknya punya pembawaan yang kalem dan berkarakter.",  
                "pesan":"Semoga makin sukses dan tetap rendah hati."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1y5Z1eCpaMnuHkOOGBbo4PDeUUz9gyUa6",
            "https://drive.google.com/uc?export=view&id=1ljM-Ul_VqR2P3ZjS7AOH1a9wVwVmp4-1",
            "https://drive.google.com/uc?export=view&id=16Xa7uUp1ocmxyc8qvQLUuOH94LHNnwTp",
            "https://drive.google.com/uc?export=view&id=1z_l62uI24YoQ90SfDXYgKiZ-VA-bGgAh",
            "https://drive.google.com/uc?export=view&id=1Nr-wZSBSPHOs4dfkLR9zOmFoZf877Ye6",
            "https://drive.google.com/uc?export=view&id=1miiwYc-ehjnVkngrTdsvZwnnYP48_KzC",
            "https://drive.google.com/uc?export=view&id=1YIs1BeJUR8qgdMWiHmXiWrIKVxmNPHqQ",
            "https://drive.google.com/uc?export=view&id=1SGJNm5DcPnZD4eDstaFqSl4J22C3kRvJ",
            "https://drive.google.com/uc?export=view&id=1AOmLvLZ5EuimjGCoVdSnm-PWKyGPyJaF",
            "https://drive.google.com/uc?export=view&id=19MKUnhqtsqOfYTrauRALaSHisATMKrkv",
            "https://drive.google.com/uc?export=view&id=1DDwiaRjP9AyuvJ2iIDLLg1LfSCcbqO99",
            "https://drive.google.com/uc?export=view&id=1f-LS7PA5nPXg_aCFiseZ1xB73ZKGCkyU",
            "https://drive.google.com/uc?export=view&id=15XSM7mgPjDSkixi8FiLFvpA_PCL3Re9p",
            "https://drive.google.com/uc?export=view&id=1H5LOmyfEbXUWo-XDHops8JZI1pcMpQ4E",
            "https://drive.google.com/uc?export=view&id=1lp0puX6raq8M0JhCwpmbO-oeJ376V_Zr",
            "https://drive.google.com/uc?export=view&id=1QeGTdgIejvMElqiVeRmFSYSuvjC5LXCg",
            "https://drive.google.com/uc?export=view&id=1aWcD-lelyLwdiMvcxVkOCe1KKMQ_GrGI",
            "https://drive.google.com/uc?export=view&id=1YWSI0mtbrolALayAn3zyN9HFe42Q4ITn",
            "https://drive.google.com/uc?export=view&id=1kAEy1tHom2iZkRb-dW7z4f55y_glNHgF",
            "https://drive.google.com/uc?export=view&id=1J9Dc1yJL5FBtvzmLWxKntz00qMMW--_g",
            "https://drive.google.com/uc?export=view&id=13CpSIqPmZrTHdX4SfmAKwmOOMJmd08k4",
            "https://drive.google.com/uc?export=view&id=1n5EH0WcdgIzFF33n7kPwn9IboyX8tqRP",
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
                "kesan": "Kakaknya terlihat bijak dan terbuka pada hal-hal baru.",  
                "pesan":"Semoga selalu dikelilingi hal-hal baik ke depannya."# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Punya pembawaan yang sopan tapi tetap santai.",  
                "pesan":"Semoga tetap semangat dan terus jadi contoh yang baik."# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Humble banget, meski kelihatan sibuk tapi tetap responsif.",  
                "pesan":"Semoga semua kesibukannya berjalan lancar dan produktif."# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya punya vibe positif, enak banget diajak ngobrol.",  
                "pesan":"Semoga hari-harinya selalu dipenuhi hal baik."# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Kakaknya chill tapi tetap fokus, keren sih.",  
                "pesan":"Semoga karier dan kuliahnya makin lancar terus."# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Kakaknya tenang tapi tetap enak diajak ngobrol, gak bikin canggung.",  
                "pesan":"sSemoga semua hal baik selalu ngikutin di setiap langkahnya."# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Kakaknya sopan, tanggapan-tanggapannya juga nyenengin.",  
                "pesan":"Semoga semua rencana yang disiapkan bisa tercapai dengan baik."# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya kelihatan tanggung jawab dan fokus banget.",  
                "pesan":"Semoga terus semangat dan makin sukses ke depannya."# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini hobbynya keren banget",  
                "pesan":"Mau playlist nya dong kakk"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Sopan dan kelihatan berprinsip, mantap banget.",  
                "pesan":"Semoga makin banyak pencapaian baik yang datang."# 1
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya nyenengin, gak ribet, dan terbuka banget waktu wawancara.",  
                "pesan":"Semoga terus sukses dan diberi kemudahan di setiap langkahnya."# 1
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Pembawaannya adem, bikin suasana jadi tenang.",  
                "pesan":"Semoga semua hal yang direncanain bisa berjalan lancar."# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakaknya keren, punya cara berpikir yang dewasa dan realistis.",  
                "pesan":"Semoga terus berkembang dan makin sukses di bidangnya."# 1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Ramah banget, meski sibuk tetap nyempetin waktu buat ngobrol.",  
                "pesan":"Semoga selalu diberi kesehatan dan kelancaran rezeki."# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Enak diajak diskusi, tanggapannya jelas dan sopan.",  
                "pesan":"Semoga makin sukses dan terus menginspirasi orang lain."# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Punya gaya ngomong yang santai tapi tetap rapi.",  
                "pesan": "Semoga terus jadi pribadi yang konsisten dan sukses."# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya disiplin dan terarah, kelihatan banget fokusnya.",  
                "pesan":"Semoga hasil dari kerja kerasnya selalu membuahkan hal baik."# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Santai tapi tetap punya kesan tegas, keren.",  
                "pesan":"Semoga makin sukses dan selalu diberi kemudahan jalan."# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakaknya ramah, ngobrolnya sopan tapi gak kaku.",  
                "pesan":"Semoga ke depannya makin banyak hal baik yang tercapai."# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakaknya punya aura positif dan tenang banget.",  
                "pesan":"Semoga terus bahagia, sukses, dan selalu dimudahkan."# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya punya pembawaan kalem tapi tetap berkarisma.",  
                "pesan":"Semoga selalu diberi kelancaran di setiap langkahnya."# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tTSRf4wb9FGRM-8GB2UsWAsfpEygWNNa",
            "https://drive.google.com/uc?export=view&id=1Mo_iyFeeNk6cUiuXDaF1E7gQXpiUZklT",
            "https://drive.google.com/uc?export=view&id=15POoVepGeSbrMFUAJVpLE-kCF3y1miAn",
            "https://drive.google.com/uc?export=view&id=1eMKBWmLz_9V9AGL3h_HwYc2S93HgJq4S",
            "https://drive.google.com/uc?export=view&id=1_-6Uf_t282ePD7O8fsjD6YQQacgMZ_2v",
            "https://drive.google.com/uc?export=view&id=1QVM2RC80TZCdqCfaC7TidbJmTNyu7v0t",
            "https://drive.google.com/uc?export=view&id=1YivL88g05_LxedBTZxosn-1aAisM6ZLl",
            "https://drive.google.com/uc?export=view&id=1XY4R-kFws4S-wANW76MP-QVjAHZ941bC",
            "https://drive.google.com/uc?export=view&id=1BMBIIGobW_Rc2lDY3lUgMe4hTtRbLqiM",
            "https://drive.google.com/uc?export=view&id=1hJGX42-vIXXIEmqfUqZQnzOcpRi-9RAX",
            "https://drive.google.com/uc?export=view&id=1oXJtnJQOZxXP8LWcrEa1SMFe5DStj4aK",
            "https://drive.google.com/uc?export=view&id=18eeX641KA86KQkwz3Fk1Fv6LoojvVv91",
            "https://drive.google.com/uc?export=view&id=1yNDNy3sMT_Kfb2eN-M6ZqXzpUtntbvT_",
            "https://drive.google.com/uc?export=view&id=18MIY84B-mmQkrT3KWNg1KKdJvfujCidK",
            "https://drive.google.com/uc?export=view&id=1K6IA0bxLZxDlbIPsVvxqfeqRNtp4LGq_",
            "https://drive.google.com/uc?export=view&id=1jn8mnNsriVrIS7GAunsiKPQ6jK-9qhlz",
            "https://drive.google.com/uc?export=view&id=16NlhvCI611IFax5l8VjcO3WvXlIgqdJ_",
            "https://drive.google.com/uc?export=view&id=1MB0LeV828JbIiY_UmqZKjfOoS97sRsef",
            "https://drive.google.com/uc?export=view&id=1fhlWoE-eEb9VXN7SH8My8wtkKHUdeUqZ",
            "https://drive.google.com/uc?export=view&id=1hjFEJ4CbaEePhYaCmkiKt5Uex_YcoAtq",
            "https://drive.google.com/uc?export=view&id=1EfwGkyTfqO-mjGHKrz-QdkoPTt8HQEi5",
            "https://drive.google.com/uc?export=view&id=1D2xwLqPBnLA3b3TkgiqxeRSQn1VRRpIO",
            "https://drive.google.com/uc?export=view&id=1Vy5yiMViGWUp_BKZ0dhUQvho3PWgogwm",
            "https://drive.google.com/uc?export=view&id=1tpUY70WMDwzi3xNiI4ZnFpXEfKTWkiKr",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "Sopan dan nyenengin, gak susah diajak komunikasi.",  
                "pesan":"Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Keren banget kak hobby nya",  
                "pesan":"Semoga semua urusan kuliah dan kerjaan berjalan lancar."# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya kelihatan bijak dan tenang waktu jawab pertanyaan.",  
                "pesan":"Semoga langkah-langkahnya selalu diberi kemudahan."# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya lowkey tapi punya kesan kuat dan positif.",  
                "pesan":"Semoga terus sukses dan selalu bahagia dalam perjalanan hidupnya."# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Gaya bicaranya tenang, bikin suasana wawancara gak tegang.",  
                "pesan":"Semoga semua rencananya berjalan sesuai harapan."# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakaknya berwibawa tapi tetap approachable.",  
                "pesan":"Semoga makin banyak hal baik yang datang ke depan."# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Santai, sopan, dan kelihatan punya tanggung jawab besar.",  
                "pesan":"Semoga selalu diberi kelancaran dalam setiap urusan."# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya punya vibe positif dan aura tenang banget.",  
                "pesan":"Semoga terus jadi pribadi yang inspiratif buat orang lain."# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Pembawaannya rapi dan sopan, kesannya dewasa banget.",  
                "pesan":"Semoga makin sukses dan kariernya terus naik."# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya responsif dan terbuka, bikin ngobrolnya lancar.",  
                "pesan":"Semoga ke depannya makin banyak pencapaian besar."# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kalem tapi tetap bisa bikin suasana santai.",  
                "pesan":"Semoga semua urusannya berjalan lancar tanpa hambatan."# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya enak banget diajak ngobrol, gak bikin tegang.",  
                "pesan":"Semoga sukses terus dan tetap rendah hati."# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Santai tapi tetap kelihatan fokus dan berpendirian.",  
                "pesan":"Semoga semua usahanya selalu berbuah hasil terbaik."# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Ramah dan nyenengin, gak banyak basa-basi tapi tetap sopan.",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakaknya tenang dan berwibawa, kesannya dewasa banget.",  
                "pesan":"Semoga terus sukses dan semua tujuannya tercapai."# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Sopan, kalem, tapi tetap terbuka waktu ngobrol.",  
                "pesan":"Semoga semua hal baik selalu nyertai hari-harinya."# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakaknya santai tapi tetap kelihatan profesional.",  
                "pesan":"Semoga makin sukses dan selalu diberi kemudahan."# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Ramah dan gampang diajak ngobrol, gak bikin canggung.",  
                "pesan":"Semoga karier dan studinya terus lancar."# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakaknya kelihatan tenang dan sabar banget.",  
                "pesan":"Semoga semua urusannya berjalan sesuai rencana."# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Sopan dan punya cara jawab yang bijak.",  
                "pesan":"Semoga makin sukses dan selalu dikelilingi energi positif."# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya punya vibe yang tenang tapi tetap menyenangkan.",  
                "pesan":"Semoga semua hal baik selalu menghampiri setiap langkahnya."# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Pembawaannya rapi dan berkarakter, keren sih.",  
                "pesan":"Ditunggu open PO nya kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakaknya chill tapi tetap berwibawa",  
                "pesan":"Semoga terus berkembang dan makin banyak hal baik yang datang."# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakaknya kelihatan fokus dan tangguh.",  
                "pesan":"Semoga terus diberi kekuatan dan semangat dalam menjelajahi lamsel."# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Tenang tapi punya kesan kuat, karismatik banget.",  
                "pesan":"Semoga hari-harinya selalu lancar dan produktif."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HFdf0nLqmS3oHIXOH85M9nXuamBMsQrH",
            "https://drive.google.com/uc?export=view&id=1jWlTlCo3M9-rFFib-iLccsPHDbW5Fmhm",
            "https://drive.google.com/uc?export=view&id=1t9tYoKdEg8PGTfgGiZjpbFuOfUNn98HI",
            "https://drive.google.com/uc?export=view&id=1XhUFMMo9hWHofMEgbxLoneYkC16nYw-8",
            "https://drive.google.com/uc?export=view&id=1ZcPsZLrJIFuHYMowWZa5oZDYBU9sIZeU",
            "https://drive.google.com/uc?export=view&id=1xQ8O7M9jJFmPv-Qt7VLMq234dLqv9A3j",
            "https://drive.google.com/uc?export=view&id=12N7pl4vyQznE8NN9fHzdsDNCLG960zTl",
            "https://drive.google.com/uc?export=view&id=1f0K9l4dzzM2WKa5s6IkU0s8nTWvRKgfG",
            "https://drive.google.com/uc?export=view&id=1TPQBQTi956uQzNRpZbbf7YQJ_dWAFYmJ",
            "https://drive.google.com/uc?export=view&id=1R2hk6ywHk6dJ-vyQQsVK9dVYVYDMMoBj",
            "https://drive.google.com/uc?export=view&id=1GLneli_EkVPEsPkslChw7ohzNvufbmwH",
            "https://drive.google.com/uc?export=view&id=1rUZtXQ25xg5KBcnBnnEB7b_cScrWf-lf",
            "https://drive.google.com/uc?export=view&id=1UbxWASOpCtZA1vU2Wxh8nVkgstvbfQYr",
            "https://drive.google.com/uc?export=view&id=1V-39Ljb8SFMMij6kQdH26UcSM1-q75ry",
            "https://drive.google.com/uc?export=view&id=1bxol8iOvITladKaMZnOuafRmk28G_tYU",
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
                "kesan": "Tenang, Kalem.",  
                "pesan":"Keren kak hobby nya"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya simple tapi tetap berkesan.",  
                "pesan":"Semoga makin sukses dan tetap rendah hati."# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya kalem, sopan, dan punya aura positif banget.",  
                "pesan":"Mantap kak hobby nya, salah satu sunnah Rasullullah"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.raaa_",
                "kesan": "Ceria, Riang, Gembira",  
                "pesan":"Keren kak hobby memasak, saya pasang gas masih takut"# 1
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Kakaknya kalem dan punya cara bicara yang tenang.",  
                "pesan":"Semoga ke depannya makin sukses dan diberi kemudahan dalam segala hal."# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya punya aura positif yang bikin suasana nyaman.",  
                "pesan":"Semoga langkah-langkahnya selalu dimudahkan dan diberkahi."# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Keliatan sporty banget",  
                "pesan":"Keren kak hobby nya, salah satu sunnah Rasulullah"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Sopan dan santai, kelihatan easy going banget.",  
                "pesan":"Semoga makin sukses dan selalu semangat ngejar impian."# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Hobinya anak semester akhir",  
                "pesan":"Lakukan yang terbaik"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi Pemda",
                "hobbi": "Main rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Keren banget hobinya",  
                "pesan":"Keep Going"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1l4prjM3zaL3Ge-kODWeqvJTSeVZSfFgs",
            "https://drive.google.com/uc?export=view&id=1iLdFZ_EJdDAThAbLIeBzmfxgBWEXB8_V",
            "https://drive.google.com/uc?export=view&id=1thTh6UVtt-igaQzbydGJCyTqglHgTc_e",
            "https://drive.google.com/uc?export=view&id=1ONB1B8ZJTkWV880KywMW3P_Ykp5Hc4X6",
            "https://drive.google.com/uc?export=view&id=1f-HmI_1g9FRYqGvLPGeVNN8cy280uhSt",
            "https://drive.google.com/uc?export=view&id=15yJauyKIUalhTnk61VVxbXTkuPpVDose",
            "https://drive.google.com/uc?export=view&id=1wO4eLeGS6Wigg-rx6_eeJtrhqq1HuAH4",
            "https://drive.google.com/uc?export=view&id=1x5raBX-E7JBHPfBYzaUU92BCB0NoBHYy",
            "https://drive.google.com/uc?export=view&id=1lEJ56CCWQcYx1rpQAKeEST9vZ8q5tmMn",
            "https://drive.google.com/uc?export=view&id=1veY9sa1TFZruYA9Z3Fwab73Wo9RCLSlx",
            "https://drive.google.com/uc?export=view&id=1Frd96Ybb2ltnQ_SJDpN_PrfMjDlofgc-",
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
                "nama": "Engeli Rahmadhani",
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
            "https://drive.google.com/uc?export=view&id=1HohyZFb70bXFSQxHFsu_-K4KVQUYe7qR",
            "https://drive.google.com/uc?export=view&id=1ieViFj4qKqHU3kQdesEOeLDYxzNmwhjK",
            "https://drive.google.com/uc?export=view&id=1uab4WA2XYKkr23kB0wnQXxykzWvJPx36",
            "https://drive.google.com/uc?export=view&id=14khOxxXT_4G9VgAVv2mWoL3SH4SkKdZM",
            "https://drive.google.com/uc?export=view&id=1QVrN2VxYkcOUfKwi4VaYuoWoflHA22AQ",
            "https://drive.google.com/uc?export=view&id=1k93hD7v14m4L0LvfmkeDO-iQf1ffX6J6",
            "https://drive.google.com/uc?export=view&id=1kdro-Pw5b5HwSKto5dnDSTkndNg-Ck8H",
            "https://drive.google.com/uc?export=view&id=1OFl5D6BdHDhVfLStS9P1FnSZ-rjECvzO",
            "https://drive.google.com/uc?export=view&id=14eCWapsjtI_PDEtit-LUSg3qCgqiL-7W",
            "https://drive.google.com/uc?export=view&id=1gPHuJHtxDbeCMRFJpOIeOxMCcwoiGUCJ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@i",
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
                "sosmed": "@rafidivaefangga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

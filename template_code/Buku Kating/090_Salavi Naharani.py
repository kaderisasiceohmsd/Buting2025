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
            "https://drive.google.com/uc?export=view&id=19vybQZr9mz0WOY6Il1ElD1CGhE7kPwxT",
            "https://drive.google.com/uc?export=view&id=1Z7rMay3chRvVm9IRS8YiEV9t63v3Hws2",
            "https://drive.google.com/uc?export=view&id=127v5oPEojUoTG-fSERPi44ZMZkgsm16U",
            "https://drive.google.com/uc?export=view&id=1IR19hPg5BSFfRiVqhEHn40DqONnItZfH",
            "https://drive.google.com/uc?export=view&id=1a4jojPsXNztYmqlsVJsTh57Y4-Htt6Ww",
            "https://drive.google.com/uc?export=view&id=127v5oPEojUoTG-fSERPi44ZMZkgsm16U",
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
                "kesan": "Sangat berwibawa, keren, positive vibes",  
                "pesan":"Semoga amanah dan semangat kuliahnya"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren banget, postive vibes",  
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
                "kesan": "asik, lucu, dan baik hati",  
                "pesan":"Semoga lancar kuliah dan kariernya"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Lucu, baik, postive vibes",  
                "pesan":"Lancar selalu kuliah dan suskses kariernya"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Lucu, bikin ketawa terus",  
                "pesan":"Lancar kuliahnya dan sehat selalu."# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Keren, baik, lucu, asik",  
                "pesan":"Sukses selalu dan diperlancar kariernya"# 1
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X7SSUjHXbS60-HQSIuOvz6K-EfNeRzxi",
            "https://drive.google.com/uc?export=view&id=1gxONcOafqflWA9y_qxPzSO3S9p0nn_w2",
            "https://drive.google.com/uc?export=view&id=1vQ7LYcVQLeTZPRRVWLOz8cJjgx9c1PMv",
            "https://drive.google.com/uc?export=view&id=1hhEOlyA1i-a7YNBhEeVmBDk1fxXhustz",
            "https://drive.google.com/uc?export=view&id=11_w56W2d0q-Q-_tO-xryO4lS9rS7e9Bk",
            "https://drive.google.com/uc?export=view&id=1idzFP54BHTUHWgj4u-ynUBQVvqa1aC-Q",
            "https://drive.google.com/uc?export=view&id=16u_U51mFGxr9tTMM5d5dbFJx_8G_A-dS",
            "https://drive.google.com/uc?export=view&id=1F1Fif8huz50Y5k9b6XdmaIkVOxJVQ9aw",
            "https://drive.google.com/uc?export=view&id=1cLsSJ4pdhn5lEsGT5vm_hRPrfwhiAebK",
            "https://drive.google.com/uc?export=view&id=1HU3WUVEodPVZmzferjUxO5qbyo40LOr3",
            "https://drive.google.com/uc?export=view&id=139ZUqRuQ9CCSABCO5L_qkN5Y-OiiMgPW",
            "https://drive.google.com/uc?export=view&id=106E9H46PWTpecQ6akq0wgIj8A-cPKflS",
            "https://drive.google.com/uc?export=view&id=1-P0247vStMjz0bLx5luV9yfAv2Hrrl2U",
            "https://drive.google.com/uc?export=view&id=1qeqcuPA71gf0nq12z8P_X_VB0zOBt8fp",
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
                "kesan": "Pembawaannya seru dan asik diajak ngobrol.",
                "pesan": "Semoga semua target dan cita-cita abang tercapai ya!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Orangnya ceria dan selalu bikin suasana ramai.",
                "pesan":"Lancar selalu kuliah dan kariernya"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Baik, sopan, dan enak diajak ngobrol.",
                "pesan":"Semoga langkah menuju masa depan selalu dipermudah!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Baik, sopan, dan gampang akrab sama orang baru.",
                "pesan": "Semoga semua rencana kakak berjalan lancar!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Orangnya cerdas dan ozt.",
                "pesan":"Makin sukses kuliah dan kariernya"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Friendly, cantik, dan energinya positif.",
                "pesan": "Semoga selalu percaya diri mengejar mimpi!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Ramah dan enak diajak diskusi berbagai hal.",
                "pesan": "Tetap semangat! Semoga kuliahnya semakin lancar."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Keliatan smart dan punya vibe yang kalem.",
                "pesan":"Semoga sukses terus dalam bidang yang abang tekuni!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Baik hati dan selalu terlihat percaya diri.",
                "pesan":"Semoga sukses dalam setiap perjalanan karier ke depan!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Gayanya estetik, kepribadiannya menarik.",
                "pesan":"Gayanya estetik, kepribadiannya menarik.",
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Ramah dan punya semangat yang kuat.",
                "pesan":"Sehat selalu, lancar kuliahnya dan sukses kariernya"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Humble dan wawasannya luas banget.",
                "pesan":"Semoga makin banyak kesempatan baik yang datang ke Abang!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Sopan, ramah, dan vibes-nya selalu positif.",
                "pesan":"Semoga kuliah berjalan mulus dan kariernya gemilang!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Kece, ceria, dan seru diajak ngobrol.",
                "pesan":"Tetap semangat bangun masa depan yang cerah ya kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1elYxQdimcEJwctEdx5p2JKZi-jMROnZy",
            "https://drive.google.com/uc?export=view&id=1I1eEFsYtEq67cqQxYh_sN9gr22LV4k3s",
            "https://drive.google.com/uc?export=view&id=1Q9oB9WZxc6tQpXntURf6yjq8KNnRfMUa",
            "https://drive.google.com/uc?export=view&id=1Q6rVdx1rtPAvdId9w7ON26eLG4h5aD3y",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya seru dan baik",  
                "pesan":"Semangat kuliahnya dan sukses kariernya bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakaknya postive vibes dan pembawaanya tenang",  
                "pesan":"Lancar selalu kuliah dan sukses kariernya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Seomga selalu lancar kuliahnya dan sukses kariernya"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya seru dan baik",  
                "pesan":"semangat terus kuliahnya kak dan sukses kariernya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tLJvcpT8-9opP3Hg_VM9SoDkfsJxv0DG",
            "https://drive.google.com/uc?export=view&id=13MkvL0lSifR3DYg_pWfe86qcdLpDxZ2c",
            "https://drive.google.com/uc?export=view&id=10zMJQPXkgh8kEzezjSTjR3i0dUryqrhI",
            "https://drive.google.com/uc?export=view&id=1MCc4rU-PLP9eRygKSwvIi3d5L5lvGx-X",
            "https://drive.google.com/uc?export=view&id=11m6HhXLZSDQ4bUiR0GqcVPpXhSaV-a-Y",
            "https://drive.google.com/uc?export=view&id=17COLtzTtCUnnu-xxjKSxzT3eYvBM4z-V",
            "https://drive.google.com/uc?export=view&id=1-65MVdGf3gvn4E4SOhuad05TFyMssjBr",
            "https://drive.google.com/uc?export=view&id=1ME3sXuIqFgnq6uDjr6yHQV47FnemHjSO",
            "https://drive.google.com/uc?export=view&id=1pIdGtbQ-f2GvwYCLmNYx57_OytzS-JmO",
            "https://drive.google.com/uc?export=view&id=1O6i7fsD3a1KQA8cqwgb44Y4pmYN5Yl-V",
            "https://drive.google.com/uc?export=view&id=1ow8uOfb1sdgj7lyp28WiC18U5V2LmRFd",
            "https://drive.google.com/uc?export=view&id=1UPnP72AlH9RD3hLY3TL7DFnfAvd3q9LH",
            "https://drive.google.com/uc?export=view&id=11MZ_puNvNEshBDipJdM-uK44KgUkBL9m",
            "https://drive.google.com/uc?export=view&id=1lvLk2xHtqWv7G_RY4NEDiXbHlBC0hI_q",
            "https://drive.google.com/uc?export=view&id=13ZmnlyBZBPFYXCqpbjYDPq-fJoeEVdx8",
            "https://drive.google.com/uc?export=view&id=1xvoY98SUXsxgTlF8gS7H254CB_RgKn3f",
            "https://drive.google.com/uc?export=view&id=1ScDZ4xc7_Vp9rKAlTI368GzYIWLOzfP6",
            "https://drive.google.com/uc?export=view&id=1eKyi7d7Zc_fYavofGOCwpf67AIDnOroY",
            "https://drive.google.com/uc?export=view&id=1jVEohqk8qqm_Fgedwrc1eyBVBucNsPRQ",
            "https://drive.google.com/uc?export=view&id=13Ydr7b61fnUUN4KNMFnzILCJfJcTMVHL",
            "https://drive.google.com/uc?export=view&id=1zr3b9Oa0Er3ffil7dybNE3DaY4suBxKs",
            "https://drive.google.com/uc?export=view&id=1ZFL1sge-PvHCm_mav93s1xCpYkK3SWRs",
            "https://drive.google.com/uc?export=view&id=1FJLExfmgUw77Q2lakLCHvVeBvAvAzzL9",
            "https://drive.google.com/uc?export=view&id=1nNI4pIqJHUwQdhZn6f23S5vJyf5Q_hp0",
            "https://drive.google.com/uc?export=view&id=12Es26-6eT9YQd5TDu597akF6Tjxz-6Qy",
            "https://drive.google.com/uc?export=view&id=1msDx2yTnbtH3Tam2s464_f1BjjBwn-i2",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya positive vibes dan sangat berwibawa",
                "pesan": "Lancar selalu untuk kuliah dan kariernya bang"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya postive vibes dan baik",
                "pesan": "Semoga selau lancar kuliahnya dan sukses untuk kariernya"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakaknya keren dan inspiratif banget",
                "pesan": "Semoga makin sukses dan bahagia terus"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Abangnya tenang tapi tegas",
                "pesan": "Semoga semangatnya nggak pernah padam"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakaknya lucu tapi tetap berwibawa",
                "pesan": "Semoga selalu sukses di semua hal yang dikerjakan"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abangnya sangat berwibawa dan mengayomi.",
                "pesan": "Semoga semua urusannya selalu dimudahkan dan sukses"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Pembawaanya tenang dan berwibawa",
                "pesan": "Semoga sukses di setiap langkah yang diambil"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakaknya pembawaanya tenang tapi tegas.",
                "pesan": "Sukses terus dalam semua kegiatan yang diikuti"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Kakaknya tenang dan bijak",
                "pesan": "Semoga lancar kuliahnya dan sukses besar nanti"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Pembawaannya tenang dan berwibawa.",
                "pesan": "Semoga karier dan kuliahnya selalu lancar"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya punya vibe positif banget",
                "pesan": "Semoga selalu bahagia dan penuh semangat setiap hari"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Abangnya keren dan seru",  
                "pesan":"semangat terus kuliahnya bang dan sukses kariernya"# 1
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya seru dan ramah",  
                "pesan":"Lancar selalu kuliah dan kariernya"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakaknya ramah dan enak diajak ngobrol",  
                "pesan":"Sukses terus buat karier dan kuliahnya"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"Semoga selalu lancar kuliah dan juga kariernya"# 1
            }, 
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakaknya postive vibes dan baik",  
                "pesan":"semangat terus kuliahnya kakak dan sukses untuk kariernya"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya baik dan asik banget.",  
                "pesan":"Semoga semua yang dicita-citakan tercapai"# 1
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Abangnya seru dan ramah",  
                "pesan":"Semangat kuliahnya dan sukses untuk karier kedepan bang"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya santai tapi tetap profesional",  
                "pesan":"Lancar selalu kuliahnya dan semoga semua impian tercapai"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Abangnya ramah",  
                "pesan":"Sukses selalu untuk kedepannya bang"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Abangnya tenang tapi tetap tegas kalau perlu",  
                "pesan":"Sukses selalu untuk setiap langkah dan keputusan diambil"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakaknya baik dan humble",  
                "pesan":"Sukses terus buat karier dan kuliahnya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Abangnya lucu dan asik banget.",  
                "pesan":"Semoga hari-harinya selalu menyenangkan"# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakaknya keren dan baik",  
                "pesan":"Sukses selalu untuk kedepannya kak"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Abangnya ini asik dan ramah ",  
                "pesan":"Sukses selalu untuk kuliah dan kariernya bang"# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Hobbinya keren dan abangnya seru",  
                "pesan":"Semangat kuliahnya dan sukses untuk karier kedepan bang"# 1
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16-dwTBWcbBQfHjGcnUYEiX7-JgKf0DeA",
            "https://drive.google.com/uc?export=view&id=1ruJZoHc_YH49u_KfF1HMptbwU7DpVlBE",
            "https://drive.google.com/uc?export=view&id=1KejHpc-JsixVMScSo_qSurtgpfUrmixB",
            "https://drive.google.com/uc?export=view&id=11_w2MT2jTf-41OP8Yn_bNeLHRIbKeUdX",
            "https://drive.google.com/uc?export=view&id=1xl4LUkBNWttmxXnJ1oYTcURDR0HWjFaN",
            "https://drive.google.com/uc?export=view&id=1tVt_KIsK0TNzAR5J2B_IbALdtWWTHFT2",
            "https://drive.google.com/uc?export=view&id=1QRa9erlPV180WZEFIw4CtNXhcYoThXaD",
            "https://drive.google.com/uc?export=view&id=1fjT-VCaYQNtYlZIM9a8AywYhTA9Psbpv",
            "https://drive.google.com/uc?export=view&id=1DBjUUD3pj2IAD1uMKSAM6Qb-yWh7qp1N",
            "https://drive.google.com/uc?export=view&id=1S1_TBB_UoY2FKpasZt_7Pj8fVKIewWJF",
            "https://drive.google.com/uc?export=view&id=1B_AsINqDDaTCksxFORRcQBBjqWkdyoK2",
            "https://drive.google.com/uc?export=view&id=1910xWvGqgsOFpIRDsmGyTxWq0-HAgyOb",
            "https://drive.google.com/uc?export=view&id=1-DF3CzyHrPQGBDLtSwGm7R5FIMoj7c9x",
            "https://drive.google.com/uc?export=view&id=1kS5loIdHY4eLaG5PGfnLr7c-MRN0t5XY",
            "https://drive.google.com/uc?export=view&id=1InZmBCfa2D_OEFtipa0wvnLmbQkQlVRc",
            "https://drive.google.com/uc?export=view&id=1i4Cq-Ir6Lam5Rc2f4nTYq4E18tPPKp_M",
            "https://drive.google.com/uc?export=view&id=1_bNV-yGrL-0I5P6IXGJhtTu3tspYpY3f",
            "https://drive.google.com/uc?export=view&id=12bOyrnwTswEJtIlEDlEsrlCxDKRNT-eU",
            "https://drive.google.com/uc?export=view&id=16Tm-7gZ3k8T7VxulOdFzC1x69QCrECpQ",
            "https://drive.google.com/uc?export=view&id=1AVNF0M0yzuyAUpg9KkBamQY8qYa2cPm1",
            "https://drive.google.com/uc?export=view&id=13NuY9IpGYt4wOmHNFzRsrJH29CDqOwzU",
            "https://drive.google.com/uc?export=view&id=1Qmnocrs3itllPD3BE4jIr54ooOgGqZ2V",
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
                "kesan": "Ramah dan mudah akrab sama siapa aja, enak diajak ngobrol.",
                "pesan":"Semoga makin sukses dan cepet lulus kuliahnya"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Orangnya kalem tapi keren, punya aura positif.",  
                "pesan":"Semoga selalu bahagia dan dimudahkan jalannya."# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya humble banget, dan baik hati.",  
                "pesan":"Semangat terus kuliahnya, semoga IPK makin naik"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Baik dan mudah berbaur, vibe-nya menyenangkan.",  
                "pesan":"Semoga semua urusan kuliahnya diperlancar selalu."# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Humoris, asik, dan selalu bikin vibes jadi hidup.",
                "pesan":"Tetap semangat menjalani kuliahnya bang dan kegiatan lainnya!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Seru dan punya energi positif, kelihatan passion-nya kuat.", 
                "pesan":"Semoga langkahmu selalu dipermudah dan makin sukses."# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Positive vibes terus, pembawaannya kalem tapi keren.",  
                "pesan":"Semoga kuliah lancar dan mimpi-mimpinya tercapai."# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kalem dan menyenangkan, enak jadi teman cerita.",  
                "pesan":"Jangan lupa istirahat juga ya kak, semangat terus kuliahnya!"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Asik diajak ngobrol dan kelihatan berbakat di banyak hal.",  
                "pesan":"Semoga semakin sukses dan selalu bahagia."# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abang mentor super baik, asik dan perhatian.",  
                "pesan":"Semoga langkahnya selalu dimudahkan dan dikelilingi kebahagiaan."# 1
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Seru, ceria, dan sama-sama suka dunia per-kpop-an.",  
                "pesan":"Semangat terus kuliahnya dan tetap jadi diri sendiri yang ceria!"# 1
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik, pembawaanya tenang dan ramah.",  
                "pesan":"Semangat kuliahnya kak, jangan lupa jaga kesehatan juga."# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn piano, dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Baik dan ramah, bikin orang nyaman berada di dekatnya.",  
                "pesan":"Semoga semua urusan diperlancar dan tetap semangat kuliahnya!"# 1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Sikapnya santai tapi tetep asik diajak ngobrol.", 
                "pesan":"Semoga semua yang dicita-citakan bisa terwujud."# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kakaknya seru punya energi positif, dan bikin nyaman.", 
                "pesan":"Semangat terus kukiahnya kak, semoga selalu diperlancar."# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Ramah, seru, dan keren.",
                "pesan":"Semoga sukses selalu dalam kuliah dan karier ke depannya."# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya baik, ramah dan seru",  
                "pesan":"Semoga semua rencana baiknya disegerakan tercapai ya!"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Asik dan gampang akrab sama siapa pun.", 
                "pesan":"Semoga setiap langkahnya dipermudah dan selalu diberi kelancaran."# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Baik dan sopan, pembawaannya santai tapi nyaman.", 
                "pesan":"Tetap fokus dan semangat, semoga kuliahnya lancar terus!"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakaknya baik dan positive vibes",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Orangnya tenang dan baik banget.",  
                "pesan":"Semoga semua rencana baiknya berjalan lancar."# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya baik dan positive vibes.",  
                "pesan":"Semoga selalu dimudahkan kuliahnya."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FDe6ePUBWXNt_m3BmnXZUoFvOSfa2ETm",
            "https://drive.google.com/uc?export=view&id=1N2wn4YSgETpb2tKHpNpci0RRnC8e9Mxa",
            "https://drive.google.com/uc?export=view&id=1uxXG2gFiUVrjRPLVukxu-N6a2aP7ncuk",
            "https://drive.google.com/uc?export=view&id=1mfP1YHbN4IKe4WSO8SDZRqu-gXT8ZYY_",
            "https://drive.google.com/uc?export=view&id=1P39Z9X3hyeCQ2FVHlc6m-ps0NXpkwm2Q",
            "https://drive.google.com/uc?export=view&id=1WbXHrw0Nf-V806mONZjDBbLAMN7v7SwB",
            "https://drive.google.com/uc?export=view&id=1L7WN8vH27I-XHU-oa5R2Ht7CJyPtizpH",
            "https://drive.google.com/uc?export=view&id=1M_kJ5wI0nRsZc0ch8-gEzYDrXxxI7qWi",
            "https://drive.google.com/uc?export=view&id=1uxXG2gFiUVrjRPLVukxu-N6a2aP7ncuk",
            "https://drive.google.com/uc?export=view&id=1ejUIDcD3Zx8saqPOYF9WozHL1cW_vTiW",
            "https://drive.google.com/uc?export=view&id=1EwAJHAOdQwrlfbcKKr5asE8owb-gkoib",
            "https://drive.google.com/uc?export=view&id=1UFxBRFKyRy-hvTwmB7EhnwcQp1DSWWlL",
            "https://drive.google.com/uc?export=view&id=1dU5S-3H0G5qcNcSgqJi6t4xZPzAudRiZ",
            "https://drive.google.com/uc?export=view&id=1KzqC8BJhhE5s5NDYpOu7Y833Ud7Bd_ef",
            "https://drive.google.com/uc?export=view&id=1r1fHEuIfA7qNmxIf1D8ph5VkUsnnsxyi",
            "https://drive.google.com/uc?export=view&id=1oza8C0ooD8USbHcfPeBJWppVpXQQ-Eys",
            "https://drive.google.com/uc?export=view&id=11S5pn2FJAjIKYORdSVhnVKDHEsn1-FJW",
            "https://drive.google.com/uc?export=view&id=1TUkdKfGxXD28JkRxH6p2SR3aN3boRRjp",
            "https://drive.google.com/uc?export=view&id=1ajvuXCddgNPItsMEAx0IKmxL5n6AgJ1V",
            "https://drive.google.com/uc?export=view&id=1jjetky9F1zuIAGDhyETMKz2Okd6wU4Ns",
            "https://drive.google.com/uc?export=view&id=1KukDiHQRlc-TUKkQx89B4YFvgT8S2BXb",
            "https://drive.google.com/uc?export=view&id=1OsuX5eghB9Gv03JJZJRVADqpM6SXyQon",
            "https://drive.google.com/uc?export=view&id=17KA4cQKKy79AplN6oAPnXvSv1BffGx_Z",
            "https://drive.google.com/uc?export=view&id=16kvdwKavLsllQp3PtBKVEzr4lzlX5d_X",
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
                "kesan": "Bang Arafi orangnya keren, asik dan enak diajak ngobrol.",  
                "pesan":"Semangat terus kuliahnya bang, semoga semua lancar dan banyak pengalaman berharga."# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana, tenang dan fokus, enak kalau diajak diskusi.", 
                "pesan":"Tetap semangat belajar dan jaga kesehatan ya kak, dan bahagia selalu."# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kak kei orangnya asik, keren dan speaking skillsnya bagus banget.",  
                "pesan":"Semoga kuliahnya lancar dan banyak momen menyenangkan di perjalanan kakak."# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak pembawaannya tenang, terlihat tegas tapi juga seru.",  
                "pesan":"Jangan lupa istirahat disela sibuknya kak, jaga kesehtan, dan tetap semangat kuliahnya."# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Bang Arya, santai, asik diajak ngobrol kalau lagi rileks.",  
                "pesan": "Tetap konsisten ya, semoga kuliah dan target abang tercapai satu per satu."# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Supel dan gampang bergaul, ramah dan lucu.",  
                "pesan":"Semoga semangatnya selalu terjaga dan lancar kuliahnya, semangat juga ngeaspraknya kak"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak yang sangat ramah, baik hati dan lucu banget.",  
                "pesan":"Tetap semangat kuliahnya dan semua cita-cita segera tercapai."# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla, santai dan asik, dan seru diajak ngobrol.", 
                "pesan":"Tetap semangat ya kak, semoga kuliahnya lancar dan menyenangkan."# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Bang Syahrialdi, terlihat pendiam tapi juga seru, enak diajak ngobrol kalau sudah kenal.", 
                "pesan":"Semoga terus berkembang dan semua urusan kuliah dipermudah."# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea, ramah dan adem, baik banget membimbing anak magang.",  
                "pesan":"Semoga semua target kuliahnya tercapai dengan lancar, dan lulus dengan IPK sempurna!"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakak duta sangat ramah, dan baik juga seru diajak diskusi.",  
                "pesan":"Semoga selalu diberi kemudahan dan kebahagiaan selama kuliah dan tugas yang lain juga."# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea, ceria dan enjoy, asik buat temen ngobrol santai dan diskusi.",  
                "pesan":"Semoga proses belajarnya lancar dan banyak momen seru di kampus."# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman, talenta musiknya keliatan, tegas tapi seru saat kumpul.",  
                "pesan":"Terus asah bakatnya bang dan semoga kuliah serta kreativitasnya berkembang lancar."# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak sonya asprak dari TPB, sangat baik dan ramah, selalu membantu.",  
                "pesan":"Semoga selalu semangat dan dapat banyak peluang baik selama kuliah."# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kak Lulu, hangat dan ramah, enak jadi temen diskusi bareng.",  
                "pesan":"Semoga langkah kakak di kampus selalu dimudahkan dan penuh keberhasilan."# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Bang irvan terlihat pendiam tapi ternya seru dan asik.",  
                "pesan":"Semoga performa akademik dan hobi abang keduanya berjalan lancar."# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Bang Adit, gampang akrab dan kreatif, sering bawa suasana seru disekitar.", 
                "pesan":"Semangat eksplor hal barunya bang dan semoga kuliahnya penuh kemudahan."# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya, ramah dan menyenangkan, seru banget orangnya.", 
                "pesan":"semangat terus kuliahnya, semoga apa yang dicita- citakan sefera tercapai. "# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Khazanatil, terlihat pendiam dan sabar tapi seru diajak ngobrol.",  
                "pesan":"Semoga segala urusan kuliah dimudahkan dan selalu diberi semangat."# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melinza, hangat dan asik, sangat ramah.",
                "pesan":"Semoga selalu diberi kesempatan baik dan kelancaran dalam kuliahnya."# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla, terlihat tenang dan mandiri.",  
                "pesan":"Jaga kesehatan ya kak, semoga kuliah dan rencanamu berjalan mulus."# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak Izzah, terlihat kreatif dan sabar, dan baik hati.",
                "pesan":"Semoga bakat baking kakak bisa terus berkembang dan kuliah berjalan lancar."# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois, energik dan supel, asik diajak ngobrol.", 
                "pesan":"Semoga selalu semangat dan urusan kuliah dipermudah."# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "KakTarisya, kakak astut baik hati, dan selalu sabar ngajarin.",  
                "pesan":"Semoga selalu dapat kesempatan seru dan kuliahnya tetap lancar."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17B2-UflGfyPKV789-d2FA28xXrmwE6fy",
            "https://drive.google.com/uc?export=view&id=17AMLE59eCpLUQ_zjnaVRU0R4AEnWosNv",
            "https://drive.google.com/uc?export=view&id=1m2zcMAVnaVXgjwKG8PeHQ6dT8zGrxLHW",
            "https://drive.google.com/uc?export=view&id=1qsXL4V9Y7E8xu-wC2O2hsGKEf_QJaTCB",
            "https://drive.google.com/uc?export=view&id=1PTBQ2Dp07wgqtrYMgogL8K8ky59krvRZ",
            "https://drive.google.com/uc?export=view&id=1Vrf_oy7k5G1va-EhOYxFRNDTONn9PQ6B",
            "https://drive.google.com/uc?export=view&id=10mLHKXjlW2_6hzEOAhnXkp2gmsAygRhM",
            "https://drive.google.com/uc?export=view&id=1HmCFzi-XfXwEVWAU2dNmydd-PvvJWlCH",
            "https://drive.google.com/uc?export=view&id=1TrpZbgXDYqAx3HqEy9ZOl-kg-ic9delH",
            "https://drive.google.com/uc?export=view&id=1qAejhg-6OhivH67JgseuhwxypwQkIuVE",
            "https://drive.google.com/uc?export=view&id=1ANYDfzhIDt8MWt17TPtupKFgZNw2ndxV",
            "https://drive.google.com/uc?export=view&id=1MOAS7TJXos4bu3740O32n0gy5HGBhmiI",
            "https://drive.google.com/uc?export=view&id=1zHpMu9-UavpuaodovGJp_U6UxzRXxcx7",
            "https://drive.google.com/uc?export=view&id=1Fzusg-OHuw8FdyNKNdhgml1EFpmKtWCQ",
            "https://drive.google.com/uc?export=view&id=1WfVszu8Gd6MnLXdsg_dteyQ__y5TBMPF",
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
                "kesan": "Kak Rani cantik, keren dan pembawaanya tenang, apalagi hobinya positif banget.",
                "pesan":"Semoga selalu diberi kelancaran dalam belajar dan makin semangat ya kak."# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta kayaknya tipe yang menikmati hidup pelan tapi pasti, kelihatan tenang banget.",  
                "pesan":"Terus fokus di tujuan, semoga hasil baik selalu datang ke kakak."# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa anngun dan cantik, hobinya juga keren.", 
                "pesan":"Semoga kuliah dan hobi memanahnya sama-sama melesat tepat sasaran!"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kak azzahra positive vibes, ramah dan sangat baik.",  
                "pesan":"Jangan berhenti berkarya ya kak, semoga makin ahli dan sukses kuliahnya."# 1
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang Haikal pembawwanya tenang tapi kelihatan aktif.",  
                "pesan":"Sehat selalu dan semoga segala urusannya diperlancar."# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak Iqfina tipe orang terlihat sabar, asik, dan ramah.", 
                "pesan":"Semoga setiap resep yang dicoba dan setiap tugas kuliah berjalan manis hasilnya."# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak May punya vibes yang tegas, hobinya keren banget.",  
                "pesan":"Semoga terus percaya diri dan selalu dapat pengalaman baik di kampus."# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "Muhammadnaufalafghani73",
                "kesan": "Bang Naufal asik diajak ngobrol, dan baik banget.", 
                "pesan":"Semoga tetap semangat dan kuliahnya tidak kalah seru dari anime favorit!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Bang zailani orangnya ramah selalu senyum, baik hati.",  
                "pesan":"Semoga selalu sehat, dan kuliah lancar tanpa halangan."# 1
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Bang rendi pembawaanya sangat tenang dan berwibawa.",  
                "pesan":"Semoga bakat bernyanyi dan kuliahnya jalan bareng sampai sukses bareng juga."# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna kelihatan seru dan unik, sampai hobinya pun anti-mainstream.", 
                "pesan":"Tetap jadi diri sendiri dan jalani kuliah dengan semangat ya kak."# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak Keren sesuai namanya, keren banget dan musikal juga.",  
                "pesan":"Semangat kuliahnya kak dan jangan lupa jaga kesehatan."# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Bang Hanif kelihatan suportif banget, dan baik hati.",  
                "pesan":"Pertahankan semangatnya bang, semoga target kuliah tercapai tepat waktu."# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah terlihat lembut tapi berbakat musik, keren banget.",
                "pesan":"Semoga terus berkembang dan selalu menemukan lingkungan yang suportif."# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way huwi",
                "hobbi": "Main rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kak zahra kakak kelas waktu sma baik banget sampe sekarang.",  
                "pesan":"Jangan lupa makan, jaga kesehatan dan bahagia selalu ya kak."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bA-1AyTj4pAHRUgzGdCRi50VyleEdBae",
            "https://drive.google.com/uc?export=view&id=1YzYz3LrOhvjp057OvS5i0w_3YbidROX9",
            "https://drive.google.com/uc?export=view&id=1dzWg5sUDcUyLhpTfdXoH5YJl1TjfNQQS",
            "https://drive.google.com/uc?export=view&id=1VHxnrD56I2R_TuRJv-PNoybp0RjFifQt",
            "https://drive.google.com/uc?export=view&id=19w3jGfd9xDQ5pWg7WZiXAUUKV6gMOiiV",
            "https://drive.google.com/uc?export=view&id=1txeQxx1qG_3ZAgbhEK7rrQUW3_BH6-CS",
            "https://drive.google.com/uc?export=view&id=1dL-_S1tvgjh3rb1EcKPAiskU-cuzel3R",
            "https://drive.google.com/uc?export=view&id=1GgaXn-ydnf2hGvxYOd_cw_FQF_A7tG2k",
            "https://drive.google.com/uc?export=view&id=142zSd91eBCBZ9uZN5CmYl2ggmiHJnbcg",
            "https://drive.google.com/uc?export=view&id=1L_VedQ55F-ANc0jS0rUkA0N5nemb2gF",
            "https://drive.google.com/uc?export=view&id=1QhycUM0mYrTvu4xBk-lVR9TDkjMgyOhE",
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
                "kesan": "Abangnya aktif banget, dan enak diajak ngobrol.",
                "pesan": "Semoga selalu penuh semangat dan kuliahnya lancar terus ya bang!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Kakaknya ramah dan nyenengin kalau diajak bicara.",
                "pesan": "Semoga setiap langkah kakak menuju tujuan dipermudah!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Kakaknya baik dan sopan banget, dan keren.",
                "pesan": "Semoga sehat selalu dan tetap semangat kuliahnya bang!"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya kelihatan keren dan energik, bisa jadi inspirasi.",
                "pesan": "Semoga kuliahnya lancar dan makin sukses ke depannya!"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Nyaman diajak ngobrol dan keliatan ceria banget.",
                "pesan": "Semoga semua urusan kakak dimudahkan dan selalu happy!"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya baik dan seru, bikin suasana jadi positif.",
                "pesan": "Semoga sukses terus dan tetap semangat ngejar mimpi ya kak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Asik banget diajak ngobrol, wawasannya luas.",
                "pesan": "semoga makin sukses ke depannya bang!"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya friendly dan keliatan rendah hati.",
                "pesan": "Semangat terus kuliahnya, jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Englli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Seru bisa berkenalan sama kakak, vibes-nya positif.",
                "pesan": "Semoga langkah-langkah kakak selalu dimudahkan menuju kesuksesan!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya ramah dan sopan banget, bikin nyaman ngobrolnya.",
                "pesan": "Jaga kesehatan dan semoga lulus dengan IPK memuaskan."
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Kakaknya baik dan seru diajak ngobrol.",
                "pesan": "Sukses ya kak dalam setiap rencana yang lagi diperjuangkan!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lYoc8MpDtutiDooOen7mlqZft1sk0zwi",
            "https://drive.google.com/uc?export=view&id=1iRrvMDAefvGhy707MnZSjIzLWnIuVent",
            "https://drive.google.com/uc?export=view&id=1-BQqUDhQpHrxSxOgd_wRTcJIQ9c68eoc",
            "https://drive.google.com/uc?export=view&id=1A5QzeIC2gI_DTmH6cTAQbD1LG5x5y8Ki",
            "https://drive.google.com/uc?export=view&id=1D1VTaf5H7b2wDZEAOu4VPxJuAcMXBFlo",
            "https://drive.google.com/uc?export=view&id=1WCX7hnmCrlkZCBK789UcBk-zvb2aelob",
            "https://drive.google.com/uc?export=view&id=19zrFMVIMj3aFOiNcziWwGgJmhcliebpJ",
            "https://drive.google.com/uc?export=view&id=19zrFMVIMj3aFOiNcziWwGgJmhcliebpJ",
            "https://drive.google.com/uc?export=view&id=10cpDfPW7X3jY-NeDh8rJTZZTPI3XQS4U",
            "https://drive.google.com/uc?export=view&id=1qgdN746BjQ1ZH69vDFUi8hj3SV7-BXgG",
            "https://drive.google.com/uc?export=view&id=1w33-af6fKQfWJIhfFPo7V4jQEEMoAAyX",
            "https://drive.google.com/uc?export=view&id=1g6uHmFspEudkvyE8XZYnve5IhjMQDm0J",
            "https://drive.google.com/uc?export=view&id=1kbxTux08fgOamrxpVhR8xR58jeyksaXS",
            "https://drive.google.com/uc?export=view&id=1AR3P1noQ61FeqnCiL0ktJUFCRKGV-eas",
            "https://drive.google.com/uc?export=view&id=1ggQ28Xslv7HwCOOv4MSgL33mJQ4B1k8k",
            "https://drive.google.com/uc?export=view&id=1MwLOFxPFZCryHpmvLBP3PBGZSNZ2kj7s",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1dyNyI_ln38vH8EPgES2i61l749FSJeP0",
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
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
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
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

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
            "https://drive.google.com/uc?export=view&id=1FF80KFAiQ2733ua4GPvtK_gHXgKbm5dj",
            "https://drive.google.com/uc?export=view&id=1kISSWK5q8LLNX6nQiLyJnM8lEz5Qdj7F",
            "https://drive.google.com/uc?export=view&id=1aSskObn61W0RjRjMQq5el4InKoZ4R9Vi",
            "https://drive.google.com/uc?export=view&id=1-JD6iUgJjOP_i30OXuNfHN0kXGIiIp5B",
            "https://drive.google.com/uc?export=view&id=1noE-dXXyaZdhp4q_7_oPyz7QK6_TE0OJ",
            "https://drive.google.com/uc?export=view&id=1W-nqeYcDr2F1EQRcG-Z7e2WW7Jdav4X9",
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
                "kesan": "Kahim keren",  
                "pesan":"Semangat terus bang semoga cepat lulus"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl.Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Keren banget karna ngajarin ilmu data sains",  
                "pesan":"Semoga kehidupan kuliahnya berjalan mulus"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cutekahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakanya cantik",  
                "pesan":"Semoga kakak ingat kita selalu"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya keren banget bisa diposisi ini",  
                "pesan":"Semoga lancar selalu buat kakak apapun itu"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak seru banget lucu",  
                "pesan":"Bahagia selalu buat kakak"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Kakanya kocak dan lucu seruu banget",  
                "pesan":"Semoga lancar dan bahagia selalu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vCdKZgrMef-HEitk5owcN75SelJdXUl8",
            "https://drive.google.com/uc?export=view&id=1pz7XO5rrBKBwxywjYQ7PQSIXGy82F66w",
            "https://drive.google.com/uc?export=view&id=1JEPqyVx0kgQYHGetxX9sLGpoTn_FqNKu",
            "https://drive.google.com/uc?export=view&id=1yyi-RuaLYm_-2R_qQMaTiD6zdzH7n-iV",
            "https://drive.google.com/uc?export=view&id=15BC_oF_5_D1KO2EnQWFauVreXm0HuZaS",
            "https://drive.google.com/uc?export=view&id=1b2SLar5FiWGc9QKn4rfI1YftFOjyKKlt",
            "https://drive.google.com/uc?export=view&id=1flcTX6Qg-2Ns8JXCbuj9nYGrR6ZlUDpy",
            "https://drive.google.com/uc?export=view&id=1bSoTJ_1Gb6YPD99ePApuza40zSkG0eG6",
            "https://drive.google.com/uc?export=view&id=1f_5gIKxaf0P3W8CUdJxjHPoLkxyzk48t",
            "https://drive.google.com/uc?export=view&id=1s5MjuPVdDieBnYMLF3sf8x4LnD6LVVL4",
            "https://drive.google.com/uc?export=view&id=1ycTy_w1MgH-TlyScoNezEqACrg3qNgOi",
            "https://drive.google.com/uc?export=view&id=1XZPGIVOjTyEl8KL3yZ0O4gVanQxJHAif",
            "https://drive.google.com/uc?export=view&id=1ym_5u0PFEXNhtyAhEZgCHOJ8tm4U9MEg",
            "https://drive.google.com/uc?export=view&id=1CrYBQ5ktZZd_gbU2aj14tumgxj5nssdb",
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
                "kesan": "Abangnya asik dan ramah banget",
                "pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakanya seru banget",
                "pesan":"Sehat selalu buat kakanya"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "Kakanya lucu dan seru banget",
                "pesan":"Semangat terus kakak sehat selalu"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya lucu",
                "pesan":"Semoga sehat selalu bang"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Sangat seru dan menyenangkan",
                "pesan":"Tetap semangat semoga abang bisa lulus tepat waktu"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "Kakaknya ramah dan seru banget",
                "pesan":"Semangat kakak kuliahnya"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Pinter, Kalem, Senang bisa kenal abangnya",
                "pesan":"Tutor cara belajarnya dong bang hehe"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakanya asik dan seru banget",
                "pesan":"Semangat terus buat kakanya"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "Abangnya ramah banget, Positive vibes",
                "pesan":"Semangat terus buat abangnya"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "kakanya kalem dan orangnya humble",
                "pesan":"Tetap semangat kuliahnya ya kak"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya ramah dan menyenangkan sekali",
                "pesan":"Sukses selalu untuk kuliahnya ya!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya ramah banget",
                "pesan":"Jangan lupa makan jaga kesehatan abang"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Orangnya seru dan menyenangkan sekali",
                "pesan":"Semangat terus buat kakaknya"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Pembawaannya seru dan menyenangkan sekali",
                "pesan":"Sehat selalu buat kakak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pEbhz4ztQd_VIMF7IIQLPD1FpkmfptXP",
            "https://drive.google.com/uc?export=view&id=1V22iTmQwocQmhdabJcBO5MYQ8PFZdEw3",
            "https://drive.google.com/uc?export=view&id=1BcqLj2K8t5nj7Hw5npk7tVBNY3QdoR1H",
            "https://drive.google.com/uc?export=view&id=1FPS_oaylE9BijB0kr-GqlA1iXwzlds7T",
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
                "kesan": "Abangnya humble, orangnya seru banget pas ngobrol",  
                "pesan":"semangat terus kuliahnya bang bintang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakaknya ramah banget, selalu tersenyum",  
                "pesan":"semangat terus kuliahnya kakak sukses buat kedepannya"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "like instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik, seru dan ramah banget",  
                "pesan":"semangat terus kuliahnya kakak jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Lagu",
                "sosmed": "@lia.h_264",
                "kesan": "kakanta ramah banget, seru, pembawaannya positive vibes banget",  
                "pesan":"jangan lupa makan kak, semangat terus kuliahnya kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19iEOdMMclcNGpP2DGd_gnfxF5LHlnUsa",
            "https://drive.google.com/uc?export=view&id=1oVornqMxE_X2dJkRzYBMDyT1jf2TzNM1",
            "https://drive.google.com/uc?export=view&id=1OFbqzsZgdRH4tEfD2URXr9GWAt_tmzbp",
            "https://drive.google.com/uc?export=view&id=18vfkzMRPMkO3O7oguilxU1vH3Yt9Cmhp",
            "https://drive.google.com/uc?export=view&id=1A2Vqalh8uvBjhTyRxILP8jtn7IVYPzWM",
            "https://drive.google.com/uc?export=view&id=1HeGtZ4ptBSQ-e4SEVuNnmyTVV9aYgxRy",
            "https://drive.google.com/uc?export=view&id=140VWEcaIi6k5ncEajAJIzd3J20YgUDL6",
            "https://drive.google.com/uc?export=view&id=1Hj125N1MrQgfENqEhFlYvE6U7cgGh9FN",
            "https://drive.google.com/uc?export=view&id=10dv75BEP3EPkhcZnVBtczYLpKMwXd6ub",
            "https://drive.google.com/uc?export=view&id=1XS8rwOU3pf0z0By3Tac4v9YiV4MUERzy",
            "https://drive.google.com/uc?export=view&id=16GXqLZ3aDRIVzFalR8e567Aj1BzpSz7P",
            "https://drive.google.com/uc?export=view&id=1qT9qm-dwjPBF5c5pIr55G04scdFLCVl7",
            "https://drive.google.com/uc?export=view&id=1WLtodkCcNSS_fF-S7IFrOSt8ZwHOc6Kp",
            "https://drive.google.com/uc?export=view&id=1yEWfBlFtyxHob015SiOPsMkFPufqWmer",
            "https://drive.google.com/uc?export=view&id=1moQxWSTx8tFBi-E7clp6IQSRpjjNO_s0",
            "https://drive.google.com/uc?export=view&id=1aVD7PcARAF3uOjsOwfN_CK8hRK9wBVfT",
            "https://drive.google.com/uc?export=view&id=1p0nlQBSfH_SUlyca01xSDfm1WTl3sPYK",
            "https://drive.google.com/uc?export=view&id=1lmfp5PzuUcHGkWabKDQ-7g93Zi2rBg99",
            "https://drive.google.com/uc?export=view&id=11249kTjqCfOiMMaiqoBsXZWhyqnPLs2a",
            "https://drive.google.com/uc?export=view&id=1mBqEYVHLYM0DTu3ZkjjaNwjIL1S6rYqk",
            "https://drive.google.com/uc?export=view&id=1kA_US0X-SHDbpcRG8pwCCl96jx5T2I3j",
            "https://drive.google.com/uc?export=view&id=1U5dcDwzcBbHZNMSX04shkEdltp43_ZyC",
            "https://drive.google.com/uc?export=view&id=1NRI-hRARVviCq_2Fl6S0hEZ0fnsKzK0o",
            "https://drive.google.com/uc?export=view&id=1FTShxDxq36WxfvjByIOIHquq5VeCcJQ2",
            "https://drive.google.com/uc?export=view&id=1OugIOZwM7vdBVMY2QQbymRZTPGvWj4f7",
            "https://drive.google.com/uc?export=view&id=1z2K5kWLrw3Omb01RiKzAwT0LV45JkHGb",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "22",
                "asal": "Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "Futsal",
                "sosmed": "ferdy_kevin",
                "kesan": "Abangnya ramah dan tampak berwibawa.",
                "pesan": "Mohon bimbingannya selalu, bang. Sehat dan sukses terus buat kedepannya"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakanya cantik, ramah, dan selalu tersenyum",
                "pesan": "Semoga sukses buat kedepanya kak fifa, jangan lupa jaga kesehatan kakak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Sikapnya tegas dan disiplin, Orangnya juga baik dan ramah banget",
                "pesan": "Terima kasih atas ilmunya,Jangan lupa makan selalu jaga kesehatan semoga kakak bahagia selalu"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Abangnya sangat memberi banyak motivasi, berwibawa, tegas",
                "pesan": "Semangat terus dalam menjalankan amanahnya, Semoga sukses dan sehat selalu"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakaknya ramah, walau kadang terlihat tegas",
                "pesan": "Sukses selalu untuk kakak, jangan lupa jaga kesehatan"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "Abangnya selalu aktif kegiatan, tangguh, dan penuh semangat",
                "pesan": "Semoga semangatnya terus menular ke kami, Mohon bimbingannya selalu ya bang, Sehat dan sukses terus"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Abangnya inspiratif banget, selalu kasih motivasi",
                "pesan": "Semoga masa depan abang penuh kesuksesan, jangan lupa jaga kesehatan bang"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Sikapnya tegas dan disiplin, Kakaknya rajin banget",
                "pesan": "Semoga semangatnya gak pernah padam kak, semoga kakak sehat selalu"
            },
            {
                "nama": "Nobel Nizam Fathiriski",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Kakak keren dan berwibawa, sangat memotivasi",
                "pesan": "Semoga sukses di dunia kerja dan tetap rendah hati, Semangat terus dalam menjalankan amanahnya bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Abangnya simpel tapi pemikirannya luar biasa, Pembawaannya tenang dan bijaksana",
                "pesan": "Semoga terus jadi inspirasi, Sukses selalu bang, ditunggu arahan selanjutnya"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya peduli banget, sangat berwibawa dan mengayomi",
                "pesan": "Terima kasih udah bantu kami menyesuaikan diri, Mohon bimbingannya selalu kak, Sehat dan sukses terus"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "Abang yang ini asik, bisa bikin suasana tegang jadi lucu",  
                "pesan":"semangat terus kuliahnya bang,Semoga selalu bahagia dan ceria"# 1
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya tampil sederhana tapi berwibawa",  
                "pesan":"Semoga kesederhanaannya selalu jadi ciri khas yang indah bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakak suka bercanda tapi tetap profesional",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya tenang tapi tegas, keren banget",  
                "pesan":"Semoga selalu kuat dan bahagia kak, semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakak sosok yang konsisten dan disiplin.",  
                "pesan":"Semoga rezeki dan sabarnya makin bertambah, semangat terus kuliahnya kakak."# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya selalu kasih contoh yang baik dalam bersikap",  
                "pesan":"Terima kasih sudah jadi panutan buat kami, semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Abangnya berwibawa banget, tapi tetap ramah.",  
                "pesan":"Terus jadi panutan ya bang, semoga kariernya makin cemerlang."# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya ramah dan suka senyum yang bikin suasana adem.",  
                "pesan":"Semoga senyum itu gak pernah pudar kak, semangat terus kuliahnya kakak "# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Abangnya ramah, humoris tapi tetap profesional.",  
                "pesan":"Semoga tetap konsisten dan sukses selalu, semangat terus kuliahnya semoga sukses kedepanya."# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Abangnya selalu kasih contoh yang baik dalam bersikap.",  
                "pesan":"Semangat terus kuliahnya bang, Terima kasih sudah jadi panutan buat kami."# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak selalu membawa suasana positif dan asik.",  
                "pesan":"Tetaplah menyebarkan energi baik kak, jangan lupa selalu jaga kesehatan."# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Abangnnya berwibawa banget, tapi tetap ramah banget.",  
                "pesan":"Terus jadi panutan ya bang, semoga kariernya makin cemerlang."# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakak kalem, murah senyum dan baik banget.",  
                "pesan":"Semoga selalu bahagia dan terus menginspirasi."# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Kakak kelihatan tegas, tapi baik dan ramah banget",  
                "pesan":"Semoga terus jadi sosok yang kuat, sukses buat kedepannya bang."# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Abangnya cool, tegas, keren banget",  
                "pesan":"Terus pertahankan sikap profesionalnya bang, semangat terus buat kedepannya."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DhYKSnEAYPKjrsak0Rh6JwqsxLIEEyBl",
            "https://drive.google.com/uc?export=view&id=1m7AUumXTgPcbHR834g2M3GVxW-pBZUMz",
            "https://drive.google.com/uc?export=view&id=1YcjhwP1jsUaTadeSCj1hkXigHmnda9yq",
            "https://drive.google.com/uc?export=view&id=1Em9pQsAsBIyJjKzjtCYw9EyBbShOloeK",
            "https://drive.google.com/uc?export=view&id=1QiQSqwT2gfY3JnPc4OF7OMBAQW13OIw5",
            "https://drive.google.com/uc?export=view&id=1x9Ywo-fWOKkncfSzDShqFcmVTNaLqSIP",
            "https://drive.google.com/uc?export=view&id=1wVX9GUM8d8lqmv6JXfADyypW0rkcHi14",
            "https://drive.google.com/uc?export=view&id=1rq-3SKeh308I7EsSRCnq6AJ9yeiqxcUc",
            "https://drive.google.com/uc?export=view&id=1ge-APJNxH63OcWU-AwJmVKdgLv7_-OlA",
            "https://drive.google.com/uc?export=view&id=1NdOulBLDjEDpLCmpbtTxvPwCQLdkEvVB",
            "https://drive.google.com/uc?export=view&id=1jSC6NurS4-mC2foyg_0ALvc44z1CP5cT",
            "https://drive.google.com/uc?export=view&id=1SM4GXDuicAao-YfenEaZd3bPMtB6cgaS",
            "https://drive.google.com/uc?export=view&id=1lKl0rcCwoe-x0E-7oQJApjKd2sOvAWMS",
            "https://drive.google.com/uc?export=view&id=13gAHynM9zcMNpU6YDH5WMxLDJbA1mcs4",
            "https://drive.google.com/uc?export=view&id=1D5X-2wqi-_Ry09L-f2JoB1Z9cQ6fStS8",
            "https://drive.google.com/uc?export=view&id=1CHyMIMViGnpN6U8sME1lHRrHdnQDoq1j",
            "https://drive.google.com/uc?export=view&id=1v8O8JCwzKYWgBRT9cB6clUnmjBXY6BaD",
            "https://drive.google.com/uc?export=view&id=10W344Ym07WHVhNtY-Qd5nWTt5MsWuqlo",
            "https://drive.google.com/uc?export=view&id=1Aka6z2cUzhwyAyK1xnxWaD2byhfdl5UW",
            "https://drive.google.com/uc?export=view&id=1paJ04wNa8vzgiPXoKQ6MHB9kwiDKqSZZ",
            "https://drive.google.com/uc?export=view&id=1Y8AMgMVeO4qVjMH9UI9HkU8n1oeALPLk",
            "https://drive.google.com/uc?export=view&id=1PPneCu_wtZzKPruHHkpO_hlS8c9yv4Rm",
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
                "kesan": "Abangnya pinter dan keren banget",  
                "pesan":"Semoga sukses memimpin didunia kerjanya, bahagia dan sehat selalu bang."# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Kakaknya kalem, murah senyum, dan ramah banget",  
                "pesan":"semangat terus kuliahnya kak semoga cepat lulus."# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya ceria banget, dan banyak memberi motivasi",  
                "pesan":"semoga sehat dan bahagia selalu bang jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya kalem banget, orangnya ramah, pembawaannya positif banget",  
                "pesan":"semangat terus kuliahnya kak semoga kakak bisa lulus tepat waktu"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Abang asprak, pinter, ramah dan baik hati",  
                "pesan":"Semoga sukses kedepannya bang, jangan lelah bimbing kaminya"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Abangnya positive vibes, orangnya baik dan ramah banget",  
                "pesan":"Semangat terus bang kuliahnya semoga bisa lulus tepat waktu"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya ramah banget, pembawaannya ceria, orangnya humble, kenalnya gara gara bang keya",  
                "pesan":"semoga bahagia selalu bang, jangan lupa jaga kesehatan, jangan lupa makan"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya kalem tapi seru banget",  
                "pesan":"Semoga sehat dan bahagia selalu, sukses buat kedepannya kak"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya hamble banget, murah senyum, pokoknya ramah banget",  
                "pesan":"Semoga bisa lulus tepat waktu kak bahagia dan selalu senyum yaaa"# 1
            },       
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Bang keya itu baik banget, pengetian dan pembawaannya adem banget",  
                "pesan":"Makasi bang udah bimbing markov, semoga abang bisa lulus tepat waktu, sukses dan bahagia selalu ya bang"# 1
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya ramah, baik dan pembawaannya ceria selalu",  
                "pesan":"semoga sehat selalu, sukses terus kak"# 1
            },        
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya kalem, cantik, baik, ramah banget",  
                "pesan":"Jangan lupa makan kak, sehat dan bahagia selalu"# 1
            },    
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Gg.sakum",
                "hobbi": "Main piano, nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakaknya positive vibes, orangnya baik, ramah banget, orangnya kalem banget",  
                "pesan":"Semoga bisa lulus tepat waktu ya kak, sehat dan bahagia selalu kak"# 1
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Orangnya kalem, tapi ramah banget",  
                "pesan":"Semangat terus kak menjalani hari harinya, jangan lupa jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kakaknya asik, seru kalo ngobrol, orangnya ramah banget",  
                "pesan":"Semoga kakak bisa lulus tepat waktu, bahagia dan sukses buat kedepannya kak"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abangnya kalem, tapi seru, baik dan ramah banget",  
                "pesan":"Semangat terus bang kuliahnya, jangan lupa jaga kesehatan selalu"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya kalem, baik dan oranganya positive vibes",  
                "pesan":"Semangat kuliahnya kak, bahagia dan sukses buat kedepannya"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Abangnya humble, seru banget kalo ngobrol, orangnya asik",  
                "pesan":"Semangat terus bang buat kedepannya, jangan lupa teraktiran kepantainya buat markov"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Abang ozt, pinter, baik dan ramah banget",  
                "pesan":"Jangan lupa jaga kesehatan bang, jangan lupa makan, bahaiga selalu, sukses buat kedepannya"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakaknya positive vibes banget",  
                "pesan":"Semangat terus kak, jangan lupa selalu jaga kesehatan"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Orangnya baik dan ramah banget",  
                "pesan":"Semoga bahagia dan sukses selalu buat kakak"# 1
            }, 
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya kalem dan baik banget",  
                "pesan":"Semangat terus bang, sehat dan bahagia selalu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UhZsvfkH26Aj1DvPMDOxmsvN_CIG254k",
            "https://drive.google.com/uc?export=view&id=1-Y-vURASfA7-MgPxz7tk8Vt1Z0NIxX6o",
            "https://drive.google.com/uc?export=view&id=1NFyYIGWVY90DzdwrdjMR3pJGtXDZ3wou",
            "https://drive.google.com/uc?export=view&id=1_OMUPZFWSr1-IOl8YotCaLUzojd-X57b",
            "https://drive.google.com/uc?export=view&id=1h5jFluM1G-VwBMGWaPeMwKJ_m9plm2Cc",
            "https://drive.google.com/uc?export=view&id=1uOoW6gZNUX37Yt0q3QFEjKD3Ut5PBgF4",
            "https://drive.google.com/uc?export=view&id=1s3n_2g_Qj6pTQTFWOtyKPvPHcI2CQb8S",
            "https://drive.google.com/uc?export=view&id=11eldzSrcM-L7ApiGWNljVG7DQfJvlKFU",
            "https://drive.google.com/uc?export=view&id=1Zvv7_hOSYs-PXATeFttwBWtrv5quWhNr",
            "https://drive.google.com/uc?export=view&id=14DbQwYxYNRj8bhaBIsLkAhtaTWxDPqxd",
            "https://drive.google.com/uc?export=view&id=1tdU4nkEgYDVwETqPewjb6ofDm8USUbZV",
            "https://drive.google.com/uc?export=view&id=1m90RwZLlHj0l3dhegkOnOx-Zhg2ZI07q",
            "https://drive.google.com/uc?export=view&id=1V_AvOjVUyone_SElL5AGjp5Y_qjGdBa7",
            "https://drive.google.com/uc?export=view&id=1WjV-bg1Zc2gebPCKIxrKoy8WLmEXmnHb",
            "https://drive.google.com/uc?export=view&id=1XQ_iPZAh2n4GoloMx4Za6vP7Axcq_Fc3",
            "https://drive.google.com/uc?export=view&id=1TbuWtcHkt3CJ-kRGlIay4R47hk0nwEOf",
            "https://drive.google.com/uc?export=view&id=1aSTdBkte9OQoDcmUrwpc96E7viyM7hct",
            "https://drive.google.com/uc?export=view&id=1GnBSyZY-9acgdaI7rNnImvu7kuie7LS_",
            "https://drive.google.com/uc?export=view&id=1l0AhZnLZSEXNhSZe9SMbB6cohuheqJgc",
            "https://drive.google.com/uc?export=view&id=1TrcKkXQQw2e5YJkt_KWtOVaU2WMo4bxl",
            "https://drive.google.com/uc?export=view&id=1DMt2szutMAYDSVbKHiLyNryUf0jYFGOp",
            "https://drive.google.com/uc?export=view&id=1w48tbcP8OK744l1c7DMDKRPioqFs_Ly9",
            "https://drive.google.com/uc?export=view&id=1etkDp0XoOiK2Xb2zGl9FNJr1pPfXJ0a1",
            "https://drive.google.com/uc?export=view&id=1CXYPaS8BzwaOaYoMQvGfhVpM80clT1kF",
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
                "kesan": "Abangnya selalu tampil rapi dan berwibawa",  
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
                "kesan": "Kakaknya baik, ramah, dan pembawaanya ceria",  
                "pesan":"Semoga kakak bisa lulus tepat waktu, sukses terus buat kedepannya kak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak kelihatannya santai, tapi diam-diam kerja keras banget",  
                "pesan":"Semoga sukses dan tetap elegan di setiap langkah kakak"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya seru, humble dan baik banget",  
                "pesan":"Semangat terus kuliahnya kakak, Jangan lupa selalu jaga kesehatan"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya ramah dan baik banget",  
                "pesan":"Semangat terus buat kedepannya bang, sukses selalu bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakaknya ramah, baik, dan pengertian banget",  
                "pesan":"Semoga kakak bisa lulus tepat waktu, jangan lupa selalu jaga kesehatan, jangan lupa makan kak"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakaknya baik, kalem, dan ramah banget",  
                "pesan":"Jangan lupa makan, semoga bahagia selalu dan sukses buat kedepannya kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak tutor, pinter, baik dan ramah banget",  
                "pesan":"Semangat terus kak kuliahnya, jangan cape cape ya tutorin kita nya"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abangnya baik, tegas dan bijaksana",  
                "pesan":"Semoga tetap konsisten dan sukses selalu"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya keren, baik banget, ramah dan seru banget",  
                "pesan":"Semangat terus kuliahnya kakak, semoga bisa lulus tepat waktu"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakak duta cantik, kalem, positive vibes",  
                "pesan":"Semangat terus kak, jangan lupa jaga kesehatan, sukses dan bahagia selalu"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya baik, ramah, mc pplk 2024, seru banget diajak ngobrol",  
                "pesan":"Semoga lancar selalu apa yang menjadi keinginan kakak, bahagia dan sukses buat kedepannya"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya baik, ramah, dan tegas",  
                "pesan":"Semangat terus bang kuliahnya, jangan lupa makan, sukses buat kedepannya"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakaknya ramah banget, orangnya seru dan ceria banget",  
                "pesan":"Semoga kaka bisa lulus tepat waktu dan bahagia selalu"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakaknya kocak banget, seru, baik dan ramah banget",  
                "pesan":"Bahagia selalu kak luluk, jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya kalem pendiem, berwibawa, tapi seru orangnya",  
                "pesan":"Semoga bahagia selalu dan sukses buat kedepannya bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Bang Adit itu orangnya humble dan buat suasana jadi seru",  
                "pesan":"Semoga bisa lulus tepat waktu ya bang, bahagia dan sukses selalu buat kedepannya"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak fathya orangnya seru, baik, dan ramah banget",  
                "pesan":"Semagat terus kuliahnya kak, semoga bisa lulus tepat waktu"# 1
            },        
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya pendiem, kalem tapi murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, bahagia dan sehat selalu"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak lembut tapi tegas, keren banget",  
                "pesan":"Terus pertahankan sikap profesional dan hangatmu ya kak"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya positive vibes, ramah banget",  
                "pesan":"Semangat terus kak, sukses buat kedepannya"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya keliatan kalem dan baik banget, orangnya ramah",  
                "pesan":"Jangan lupa selalu jaga kesehatan, sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya baik, ramah banget, positive vibes",  
                "pesan":"Jangan lupa selalu jaga kesehatan bang, tidur tepat waktu ya bang"# 1
            },    
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakak tutor, pinter, baik dan ramah banget",  
                "pesan":"Jangan cape cape ya kak tutorin kami semoga sukses dan bahagia selalu kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UKKqOB6aZYOelIK9NUAth5jqZIc4R-nD",
            "https://drive.google.com/uc?export=view&id=1L0rGk6BaM9TZO51fFCZ15oB3srM7i7mO",
            "https://drive.google.com/uc?export=view&id=1u1S7bwKKL2G9RJgSIYmOYHTpmL-TDTkm",
            "https://drive.google.com/uc?export=view&id=1aIchpLXkWIOMa5mycH_9_jwB9_HP8xX1",
            "https://drive.google.com/uc?export=view&id=1PW_PGMB_fW6cb6NIpH75nlVGOUXFhYLm",
            "https://drive.google.com/uc?export=view&id=1zy6Qgjr8gwIGDBZO4h2eTv4Sz7ZCjqsA",
            "https://drive.google.com/uc?export=view&id=1eXR4cUbM4pg574CyLRDe8rJqCyZSSHcY",
            "https://drive.google.com/uc?export=view&id=1bjol8o_N10sWHTpGAQjNVBvG3fHwSS0G",
            "https://drive.google.com/uc?export=view&id=1MtO7_DqbJZBnh494tDvbdDJJVpcTMyg4",
            "https://drive.google.com/uc?export=view&id=1UAT5Rqrj0ZEVvPkdObyKTGROKeQBrNSc",
            "https://drive.google.com/uc?export=view&id=1XHh5CMpKL-KQeydLesikTwZwNofEHXiV",
            "https://drive.google.com/uc?export=view&id=1wqgAbZkzfvOjRfarYP4VKb3pYkoTzDyl",
            "https://drive.google.com/uc?export=view&id=1GzRktz_ZW7l45HgstUxTGIi4a2WsZ04-",
            "https://drive.google.com/uc?export=view&id=1X0E190pnQvw6uZddvzR69S4kH9u3r0bq",
            "https://drive.google.com/uc?export=view&id=1pnl7OJMeMxykiwmZhRnzWAc3hbO5vSQK",    
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
                "kesan": "Kakaknya keren banget, baik banget, apalagi hobinya mengaji masyaallah banget deh",  
                "pesan":"Ngaji bareng yuk kak, semoga bahagia dan sukses buat kedepannya kak"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Orangnya santai, pembawaanya adem banget, dan baik banget",
                "pesan":"Semangat terus kak jangan pantang menyerah"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya humble, hobinya keren, orangnya ceria dan baik banget",  
                "pesan":"Semoga apa yang diinginnya tersemogakan ya kak"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Orangnya ramah dan ceria banget",  
                "pesan":"Sukses buat kedepannya, semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya keliatan serem, tapi pas uda kenal orangnya huble dan baik banget",  
                "pesan":"Sehat selalu bang, semoga apa yang abang inginkan tersemogakan"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya ramah dan positive vibes banget",  
                "pesan":"Semangat terus kak menjalani hari harinya semoga bahagia selalu"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Orangnya tegas dan keren",  
                "pesan":"Semangat terus kak, jangan lupa senyum buat hari harinya"# 1
            },    
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo",
                "alamat":"Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhamadnaufalalghani",
                "kesan": "Orangnya seru, Kakak kelas SMP SMA tapi bang nopalnya lupa hehe",  
                "pesan":"Semoga sehat selalu dan bahagia terus buat bang nopal"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya terlihat dewasa, baik dan ramah banget",  
                "pesan":"Semangat terus bang kuliahnya, jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Keren banget hobinya, orangnya juga posotive vibes",  
                "pesan":"Jangan lupa jaga kesehatan bang, bahagia selalu"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya ramah banget, orangnya bisa buat susana jadi ceria",  
                "pesan":"Semoga kakak bisa lulus tepat waktu, bahagia selalu kak"# 1
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
                "pesan":"Semangat teus kuliahnya kak"# 1
            },    
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya cool, pendiem, tapi baik banget",  
                "pesan":"Semoga bahagia selalu bang"# 1
            },   
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Orangnya baik, ramah dan pembawaannya positif banget",  
                "pesan":"Semangat terus kak jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda",
                "hobbi": "Main Rubik Mirror 3x3",
                 "sosmed":"@zhrptrsl",
                "kesan": "Kakaknya cantik, ramah dan positive vibes",  
                "pesan":"Semoga sukses buat kedepanya kak, bahagia selalu ya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VL4B0VipFI5FEBYGIAuB_UySoyyXnpq-",
            "https://drive.google.com/uc?export=view&id=1PeDoOAiRkLj8eNa6Xq84C9ZAprQsp69P",
            "https://drive.google.com/uc?export=view&id=1yXR-4e2Z3wCQL5oWc3Td8yQN3ynyzZoF",
            "https://drive.google.com/uc?export=view&id=1VTYWAWefvVw0hdUc8DRk9ns_9HO3R9WQ",
            "https://drive.google.com/uc?export=view&id=1mCdXYsm0LmHgYyjvKEel7sn833-C9cD0",
            "https://drive.google.com/uc?export=view&id=1eOiHhdZUL5K05p4lOStwC1j2Lm913jhU",
            "https://drive.google.com/uc?export=view&id=167KmDZynRL0J9qGGy-I9xLnru8DYpRCs",
            "https://drive.google.com/uc?export=view&id=1vi8Kyh0Y7eVD4B9Jek8O3vKEMZCi6uM9",
            "https://drive.google.com/uc?export=view&id=1aIEsWD5dS0ZD91kxoQNSsEi4ajgzOc3R",
            "https://drive.google.com/uc?export=view&id=12j5RNNsCW0Wu5XovavEI2M2Vbi5cnWoi",
            "https://drive.google.com/uc?export=view&id=1KEdwvg7lAb8ORZIKvBRkGUm8fjO3Wfb8",
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
                "kesan": "Abangnya seru dan menginspirasi",
                "pesan": "Semangat terus bang, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Kakaknya ramah dan kakak yang kembar itu",
                "pesan": "Semangat terus kuliahnya kak bahagia selalu"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Abangnya baik dan ramah banget",
                "pesan": "Sehat selalu ya bang semoga sukses kedepannya"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif",
                "pesan": "Semangat terus kuliahnya, kak"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Kakaknya kalem ,baik dan positive vibes",
                "pesan": "Semoga semua urusannya dilancarkan dan bahagia selalu kak"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya ramah banget dan seru",
                "pesan": "Sukses selalu untuk kakak semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Abangnya seru dan ramah banget",
                "pesan": "Terima kasih atas bimbingannya bang semoga sukses buat kedepanya"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum",
                "pesan": "Semangat terus ya kak kuliahnya semoga sehat dan bahagia selalu"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Kakaknya kalem dam murah senyum",
                "pesan": "Semoga sukses selalu kak"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya sangat ramah dan positive vibes",
                "pesan": "Jaga kesehatan selalu kak semangat terus kuliahnya"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Kakaknya ramah banget orangnya juga seru",
                "pesan": "Semangat dan sukses selalu buat kedepanya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GNd3YWYcarsmYO6vcvreWaO6RJDRA8Pm",
            "https://drive.google.com/uc?export=view&id=1gb_DwlxEK55q7vfVeAnScYPjHoD1lzSr",
            "https://drive.google.com/uc?export=view&id=1lKx7A8IyvRKYbmt1qbmvljuo6QCpGm_b",
            "https://drive.google.com/uc?export=view&id=1yQpdicUAjVDYAXbFdNdTeMruLa0W_4hT",
            "https://drive.google.com/uc?export=view&id=1Nt4kkCciVBkFChygWhyHGhIlzlAGuoXL",
            "https://drive.google.com/uc?export=view&id=1-QMS59CWEkdAsRkHe-H6t_tfx8F6J8aI",
            "https://drive.google.com/uc?export=view&id=1jKAFeOQozDIyNJudgt21KBD8FcXMKQ3X",
            "https://drive.google.com/uc?export=view&id=122LL5hArCgqy6HbNcM_oxbz2Qdi3s5LS",
            "https://drive.google.com/uc?export=view&id=1A5qJCMqGCb90XmPO61uH9O6ESoRnCYgg",
            "https://drive.google.com/uc?export=view&id=1YQRUJwXPFhsEC3LzGisZbDD9rK1ZCEAJ",
            "https://drive.google.com/uc?export=view&id=1Ll5y-3igsgIj9E7LdPJi2VfMnu31XSuh",
            "https://drive.google.com/uc?export=view&id=1YwXqtGHkMFka5S8J5x3t3xfulAhg-sAP",
            "https://drive.google.com/uc?export=view&id=1o9iHbZXNCvh2KYuo7FZIsmcwBy8IegFG",
            "https://drive.google.com/uc?export=view&id=1F3eUfCR_2u_lXhSNZAORXTm7VPjtJ_8V",
            "https://drive.google.com/uc?export=view&id=1ZbypjmrEcLYzSZt7_3O6_HYo2UiO1BDM",
            "https://drive.google.com/uc?export=view&id=1lEnkVTY79f0m5-ck8NTTmraOTRm8lw8J",
            "https://drive.google.com/uc?export=view&id=1KfUf5x4u3UrrkoEP8h9TUioW3Gx_lHys",
            "https://drive.google.com/uc?export=view&id=1HaWxSho0m2x2o6QIuyoNw2opuMEzvwA0",
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
                "kesan": "Kakaknya asik banget, buat suasana jadi ceria",  
                "pesan":"semangat terus kuliahnya kakak bahagia selalu"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@rahmanellayana",
                "kesan": "Kakak asik banget, orangnya ramah dan murah senyum",  
                "pesan":"semangat terus kuliahnya kak semoga bisa lulus tepat waktu"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Abangnya keliatan pendiam, tapi kalo ngobrol ternyata orangnya seru",  
                "pesan":"semangat terus kuliahnya bang sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@neorruuu",
                "kesan": "Abangnya murah senyum dan baik banget",  
                "pesan":"Jangan lupa jaga kesehatan bang bahagia selalu"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya baik dan ramah banget",  
                "pesan":"Semoga bahagia dan sukses buat kedepannya bang"# 1
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
                "pesan":"Semangat terus kuliahnya kakak Jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya cantik, murah senyum dan baik banget",  
                "pesan":"Semoga bisa lulus tepat waktu kak"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakaknya cantik ramah dan murah senyum",  
                "pesan":"Semoga sehat dan bahagia selalu kak"# 1
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kakaknya baik banget ramah, buat suasana jadi seru",  
                "pesan":"Semoga sehat dan sukses buat kedepannya kak"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya positive vibes dan ramah banget",  
                "pesan":"Senang banget bisa kenal kakak"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak nya seru dan baik",  
                "pesan":"Jangan lupa makan kak, selalu jaga kesehatan yaa"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya cantik banget, orangnya ramah",  
                "pesan":"Semoga bisa lulus tepat waktu kak"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya keliatan tegas dan bijaksana",  
                "pesan":"Semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Abangnya ramah dan murah senyum",  
                "pesan":"Semoga bahagia dan sukses selalu bang"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya asik dan pembawaannya seru banget",  
                "pesan":"Semangat kak jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakaknya ramah dan baik banget",  
                "pesan":"Semoga bisa lulus tepat waktu ya kak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya cantik, positive vibes dan seru banget",  
                "pesan":"Semoga yang disemogakan tersemogakan ya kak"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya asik dan ramah banget",  
                "pesan":"Semangat terus kuliahnya kak"# 1
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

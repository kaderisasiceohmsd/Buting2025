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
            "https://drive.google.com/uc?export=view&id=1mzyXrhcGtywCNOFRMv1RunL2mRNmN98r",
            "https://drive.google.com/uc?export=view&id=1oVmneA0iW4Uv3mLe5HGbUlUUUPD-Wzep",
            "https://drive.google.com/uc?export=view&id=11fr9pOIi4N2namnfT9gUU8615qQcpbaq",
            "https://drive.google.com/uc?export=view&id=1w5qyTf4J9ZnR3Y8ZAbPK7_4VYCK4szdJ", 
            "https://drive.google.com/uc?export=view&id=1nDHKitP2tpiAXAbYhhi4YwlpsrNPFDgI", 
            "https://drive.google.com/uc?export=view&id=1-Fg49yZaVf1fwVa9LI88W1_oVIektQsu", 
        ]   
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Bang rendra keren banget,punya ability buat baca zodiak orang",  
                "pesan":"Semangat yaa bang kuliahnya, semoga dilancarin semua urusannya"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang johannes seru orangnya,santai tapi tetep keliatan tegas",  
                "pesan":"Semangat ya bang kuliahnya, sukses terus bang!"# 1
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Elisabeth ramah sekalii, positive vibes as always",  
                "pesan":"Semoga makin banyak kesempatan baik yang datang ke kakak yaa"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza waktu itu datengnyaa telat jadi belum ngobrol banyakk, tapi kakak kalem banget",
                "pesan": "Semangat ya kak Syadza, jangan lupa minum hihi"
            },
               {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty lucuu orangnya, pembawaannya seruu",
                "pesan": "Sukses terus buat perjalanan selanjutnya yaa kak"
            },
              {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, cute kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak Farahanum asikk orangnya, supel juga!",
                "pesan": "Semangat terus ya kak! tetap semangat ngelakuin hal-hal baik."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w7d1rJfhcL882sVcBxNsC-qp95mB3QrP",
            "https://drive.google.com/uc?export=view&id=15mVZ4e7PHX1g4SYqgEfCRb2qvnPLUlXc",
            "https://drive.google.com/uc?export=view&id=1nUALdUq6cwkNtURq5dnGYudlKlgyKfOd",
            "https://drive.google.com/uc?export=view&id=1AI_saLTlqEUy3HYmRzxwb8PvVzzOVhGx",
            "https://drive.google.com/uc?export=view&id=1c1K0w88u5BKMGD3WLpEtEjrCTUa4h_Da",
            "https://drive.google.com/uc?export=view&id=1jcaVz62lBmqeCdHiOxLvLJkextD3EnoJ",
            "https://drive.google.com/uc?export=view&id=1kGMRXO1OUV2wizYFwN5ZII-7dxdgemnC",
            "https://drive.google.com/uc?export=view&id=1kMPJSAIYskvFgqJdgx__khhD83iG2m71",
            "https://drive.google.com/uc?export=view&id=1zdPevThMZTLj3hOJOkpNmzm4-J4zh6HZ",
            "https://drive.google.com/uc?export=view&id=1mwOVsw44f3nZWETI_2PS5tjo0az5XqFz",
            "https://drive.google.com/uc?export=view&id=1JDqIsM7QcDwMnkqR7lixYD6vXdoIcz1M",
            "https://drive.google.com/uc?export=view&id=1UzvDVJuLpdBsDWYcPrPPzX-qy2LY37vp",
            "https://drive.google.com/uc?export=view&id=1Lhzs1leV8ugV--HhAt2eTMTR8k5hL62Y",
            "https://drive.google.com/uc?export=view&id=1ROnqkqSyhtZKGshlvypNlw2kUbsq74_Z",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Tanjung Merawa",
                "hobbi": "Suka main voli sama Feby",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jeremia keren banget, orangnya tenang dan keliatan berwibawa",
                "pesan": "Semoga makin banyak pencapaian hebat yang diraih"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea orangnya lucu, murah senyum",
                "pesan": "Semoga ke depannya semua rencananya berjalan lancarr"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Kak renisha bikin suasana jadi rame terus, nggak pernah ngebosenin",
                "pesan": "Semangat terus ya kakk kuliahnyaa, semoga sukses selalu"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@ansftynn_",
                "kesan": "Kak anisa murah senyumm, ramah banget orangnya",
                "pesan": "Semoga lancar luncur ya kak kuliahnya"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Bang dharu pinter abiess",
                "pesan": "Semangat bang, semoga apa yang diimpikan tercapai"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "Kak feby cute banget kaya animee, seru juga kakaknya",
                "pesan": "Semangat yaa kakk kuliahnya, jangan lupa istirahat"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Bang givaro seruu bangett orangnya",
                "pesan": "Semangat terus ya bang kuliahnya, jangan lupa istirahat juga"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya kritis banget setiap nanggepin pertanyaan",
                "pesan": "Semangat bang, semoga nanti bisa lulus tepat waktu"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kak berliana asik banget orangnya",
                "pesan": "Semoga selalu bahagia dan tetap jadi sosok yang ceria dan bikin semangat ya kak!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kak jue kakak tersibuk ni, baik banget orangnyaa",
                "pesan": "Jangan lupa istirahat ya kak, luangin waktu juga untuk diri sendiri, self reward"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang ridho ramah bangett, asik juga orangnya",
                "pesan": "Semangat ya bang kuliahnya, jangan lupa istirahat"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Abangnya lumayan pendiem, belum keliatan yappingnya",
                "pesan": "Semangat bang, semoga diem diem lulus beasiswa ke luar negeri ya bang"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica baik banget yaampun",
                "pesan": "Semoga apa yang disemogakan, tersemogakan ya kak"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak imupp kenal waktu lagi tes skd kedinasan hihii, baik banget kakak satu ini",
                "pesan": "Semangat ya kak kuliahnya, jangan lupa istirahat yang cukup"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
    # Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XPG0Y9NNaTacEiG-Zf_qiVFqUyJ2r2sp",
            "https://drive.google.com/uc?export=view&id=1Vn4eqxCP5AYIFCX3oipwKm2zOq7i",
            "https://drive.google.com/uc?export=view&id=1xb0-I7AbqbYx9bsSMgMSwUVHdkX2he9A",
            "https://drive.google.com/uc?export=view&id=1mYi64P58L-fKz40xffCzLiKVtN4Pr_gL",
             ]   
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Belajar",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang bintang selalu punya pandangan yang luas dan bijak banget",
                "pesan": "Semoga bisa terus jadi panutan dan inspirasi buat kami semua ya bang"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Ramah dan gampang diajak ngobroll",
                "pesan": "Semangat ya kak kuliahnya"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "Jagoo banget ngedesainnya, kakaknya seruu juga",
                "pesan": "Semoga dipermudah segala urusannya ya kak"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "Kak lia punya vibes yang calming",
                "pesan": "Semangat kak kuliahnyaaa"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
    # Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Djvy80ie_uYU5Dhhvf8fa2rFeJ9ZdeYe",
            "https://drive.google.com/uc?export=view&id=1iBIzT5pX-r8IQywA9hiJFS2Nchce-3jS",
            "https://drive.google.com/uc?export=view&id=1uncI5Gg0pY_ogZB1uGHjPI3waWbAKU2c",
            "https://drive.google.com/uc?export=view&id=1RMQubpkW6Wnf7xMg0Xw17HreqDiovICN",
            "https://drive.google.com/uc?export=view&id=1idg4Ss2XUkXEOMThUOwjYu9XGDwK2NAF",
            "https://drive.google.com/uc?export=view&id=15f0qbpnacISLc1Q8rNdUbJkGRxysTmo-",
            "https://drive.google.com/uc?export=view&id=1nIov3gAck3mSyO0f8mRHFio4yL_EXNks",
            "https://drive.google.com/uc?export=view&id=1xtXqCfJDg37EN3x2mQ_UhYfNhI1whU1l",
            "https://drive.google.com/uc?export=view&id=1E8drD8r71-0NJbe_Xc10bAH24Hb4QheM",
            "https://drive.google.com/uc?export=view&id=1AcSWEEmb8LO8yQKXwu7Gx3bY5kF85xPP",
            "https://drive.google.com/uc?export=view&id=1kBC5C2-axVcd0jhaDnns4SSrqq3wlPUV",
            "https://drive.google.com/uc?export=view&id=18sqeFVt2BXjauuQThILztIiaZo10Z-cB",
            "https://drive.google.com/uc?export=view&id=1LKryIJYYIFDnntBbUxh3F7yg33k5v6tj",
            "https://drive.google.com/uc?export=view&id=1eQxcFkQwinLpiXxViqyt_BPELdNcQIYh",
            "https://drive.google.com/uc?export=view&id=1pj6QR97vEez42yvVHHaD2cS-_vZj4vUI",
            "https://drive.google.com/uc?export=view&id=1oy9EiaDj7zFlZjRdGefFLjIJ2fl5ztl6",
            "https://drive.google.com/uc?export=view&id=1GgSZ-TtZv3WHwR-1bRVcMan9Hgwb-WtF",
            "https://drive.google.com/uc?export=view&id=1mLiAKrMudiX667F_2tTDMkq_mF3ETl5N",
            "https://drive.google.com/uc?export=view&id=1apbrGK_BuTP5YksUGArZjDXorpEYM5PO",
            "https://drive.google.com/uc?export=view&id=147DPDr-AvyxM1Q0QhGqWxfgVrNGZJPWx",
            "https://drive.google.com/uc?export=view&id=1R0RGKVvLWAKt8nwTusHyeWAZC2hXUNXf",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1kyg2P5d53BPAhKVkgTRJSL1JZtjGXnhE",
            "https://drive.google.com/uc?export=view&id=1uSC2q2vk6gma75x-e9qmo0ISUnGfO0QO",
            "https://drive.google.com/uc?export=view&id=1gzvV-uxPpO00idZRIfE_kk_4JmR5CVH4",
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
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakakanya punya positive vibes, easygoing juga orangnya",
                "pesan": "Semoga dilancarkan segala urusannya ya kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "ngekader 24",
                "sosmed": "@allyapasha_",
                "kesan": "Kak allya orangnya tenang tapi tegas, keren banget cara kakak ngatur situasi",
                "pesan": "Semangat kak kuliahnya, jangan lupa istirahat yang cukup ya kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Bang ahmad selalu punya cara berpikir yang matang dan bijak",
                "pesan": "Terima kasih udah sering ngasih insight yang ngebuka pikiran kami bangg"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "cari kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak arienta orangnya tegas dan keliatan tangguh juga",
                "pesan": "Semoga kuliahnya lancar dan hasilnya memuaskan ya kakk"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Yulia",
                "sosmed": "@daffahdynn_",
                "kesan": "Bang daffa itu supel dan gampang banget akrab sama siapa pun",
                "pesan": "Semoga ke depannya semua rencananya berjalan lancar ya bang"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Bang fajar itu tenang dan berwibawa banget orangnya",
                "pesan": "Semangat kuliahnya ya bang, jangan lupa istirahat yang cukup"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "ngitungin duit",
                "sosmed": "@natasyamavisca",
                "kesan": "Kak natasya pinter kalkulasi uang",
                "pesan": "Semangat kak kuliahnya, semoga banyak hal-hal baik yang datang"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Selalu perhatian sama detail dan orang di sekitar.",
                "pesan": "Semangat terus bang kuliahnyaa"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "Abangnya kritis banget dan punya wawasan yang luas",
                "pesan": "Semangat ya bang kuliahnya, semoga dimudahkan urusannya"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "ngoding di macbook",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany orangnya kalem tapi tegas",
                "pesan": "Semangat kak kuliahnya, jangan lupa istirahat"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@shahid22_",
                "kesan": "Bang sahid orangnya lucu tapi tetap profesional",
                "pesan": "Semoga selalu bisa bawa suasana positif ke mana pun pergi bang"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya orangnya lucu bangett",
                "pesan": "Semangat bang belajarnya, semoga bisa lulus tepat waktu nanti ya bang"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kakak gampang banget nyatu sama siapa pun, humble banget",
                "pesan": "Terus jaga sikap rendah hatinya, Kak, itu keren bangett"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak selalu kasih kesan positif setiap kali ngobrol",
                "pesan": "Semoga dilancarkan semua urusannya ya kak"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakaknya ternyata bocil roblox jugaa, seruu orangnya",
                "pesan": "Semangat ya kuliahnya kak, nanti kapan kapan kita hiking bareng di rosblok"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya selalu kelihatan tenang tapi punya pemikiran yang kuat",
                "pesan": "Sukses selalu ya, bang!, Jangan lupa istirahat"
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerjain Tugas",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Abangnya keliatannya kalem banget, soalnya belum banyak ngobrol",
                "pesan": "Semoga tetap jadi pribadi yang rendah hati ya bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "Kakak selalu punya aura positif, jadi bikin orang nyaman di sekitar Kakak",
                "pesan": "Semoga tetap bisa nyebarin energi baik itu ke semua orang yaa kakk"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Bang ihsan komunikatif banget orangnya dan gampang bikin suasana cair",
                "pesan": "Semangat yaa bang kuliahnya, jangan lupa istirahat"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngomongin Kak Dea",
                "sosmed": "@kevinaj_",
                "kesan": "Abangnya asik banget kalo diajak ngobrol",
                "pesan": "Semoga terus bisa ngasih pandangan yang menuntun kami ke arah yang baik ya bang"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak orangnya ramah banget, meskipun kita jarang interaksi langsung",
                "pesan": "Semangat teruss kak pokoknya kuliahnya"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nyuruh Dea Diam",
                "sosmed": "@ridwan122",
                "kesan": "Abangnya seruu orangnya",
                "pesan": "Semangat ya bang kuliahnya, semoga dilancarkan urusannya"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Liat Shoppe tapi ga beli",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakak orangnya baik sekalii selalu bantuin kalo ada yang kesusahan",
                "pesan": "Terima kasih kak kebaikannya, semoga banyak hal hal baik diluar sana yang dateng ke kakak"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main BOla",
                "sosmed": "@sidabutar.26",
                "kesan": "Abang punya pembawaan yang menenangkan tapi tetap berwibawa.",
                "pesan": "Semangat bang kuliahnya, sehat selalu"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Abang orangnya tegas banget",
                "pesan": "Semangat terus bang kuliahnya, jangan lupa minum"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LmIMMax9eD4e56pgpOR4AjZMqxUyKju_",
            "https://drive.google.com/uc?export=view&id=1rRtA6Z1bvWGjQSka61DTBCRApGWcU63i",
            "https://drive.google.com/uc?export=view&id=1GutsAVYTPwQ6fcENCKjHNXmdYJDRdUdK",
            "https://drive.google.com/uc?export=view&id=1L4UmgoonblQLUIczosh6nc8bzRvVC4cf",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1EDWOZB1sYbQw0ZOHdDXDeNujME3QOq4R",
            "https://drive.google.com/uc?export=view&id=1UlfyU_FOxwq9KaY6eRMsg1er6XIXmvub",
            "https://drive.google.com/uc?export=view&id=1dTTceBFgXPlsioQLQIOaCcIiORhvuGn8",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1KqmTjzHf_eG05RfXA0h8RAgvlSb2nS7K",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1ArUw6cVX5jlxnRwB9kpfg1Y6Kf7r6Hfh",
            "https://drive.google.com/uc?export=view&id=1sIhqVWlqje9-uK4AONlMFLVsota-BQXT",
            "https://drive.google.com/uc?export=view&id=1Epbiuc1mapm1yE2vdOVDeAADfm96uxxs",
            "https://drive.google.com/uc?export=view&id=1HcSg49i9JbTBxUQTTbxxrR0234zP9wUp",
            "https://drive.google.com/uc?export=view&id=12FzIvT8xVV6MOgMkN_jSd7IW-uaAFDwb",
            "https://drive.google.com/uc?export=view&id=1gtsBKfQcy2HmdPKa-zkBmuFa8RT0_i1c",
            "https://drive.google.com/uc?export=view&id=12_ho_kY6fykdQDD9qA-a3VEp8fPh2jnL",
            "https://drive.google.com/uc?export=view&id=1J5hRtH6aiOu_45WLnpf0gD7BWIb7ndWo",
            "https://drive.google.com/uc?export=view&id=1Hp1A7EnsTKwhMlfOgP28ajxrHlZ5YJtd",
            "https://drive.google.com/uc?export=view&id=1bgmsFVbtnl6f6_CLEb3OUb2R3Eiv00-g",
                    ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya seru banget, banyak cerita lika liku perkuliahan",
                "pesan": "Semoga dipermudah semua urusannya bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Ramahh banget kakaknyaa, asik juga diajak ngobrol",
                "pesan":"Semangat ya kak kuliahnya, jangan lupa minum"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "124450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Banyak banget hal baru yang aku dapet dari bang regi",
                "pesan": "Makasih udah mau cerita cerita dari awal, sukses terus buat kegiatannya"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak pinter banget masyaallah, tiap ada pertanyaan, jawabannya keren",
                "pesan": "Semangat ya kak, semoga apa yang diseogakan tersemogakan"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Abang ini keren bangett, bisa balancing waktu",
                "pesan": "Jangan lupa istirahat ya bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang aqil sepuh koding",
                "pesan": "Perbanyak bantu orang yang kesusahan"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya kalemm banget, mungkin karena belum ngobrol banyak aja",
                "pesan": "Sukses terus bang untuk kedepannya"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kak nadia seruu bingitss",
                "pesan": "Semoga makin sukses dan tetep jadi sosok keren yang rendah hati ya kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kak marleta sweet banget orangnya",
                "pesan" : "Jangan berubah ya, kak. Udah pas banget auranya"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya kalemm, introvert coded ini",
                "pesan": "Semangat terus bang kuliahnya sampai akhir"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kak anggi asikk banget orangnya, enak diajak ngobrol",
                "pesan": "Semoga sehat selalu ya kak anggi"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak astut kuu yang paling kece, pinter banget masyaallah",
                "pesan": "Semoga pinternya nular ke aku ya kak aamiin"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kak fairuzz cantik banget auranya shining shimmering splendid",
                "pesan": "Ayoo kak kapan-kapan kita mainn"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "124450081",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Asrama ITERA TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kak tanty seruu bangett orangnya, kalo ada kakak jadi rame suasananya hihi",
                "pesan": "Semangat kak tanty kuliahnya, semoga bisa lulus tepat waktu ya kak nanti"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450022",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "-",
                "kesan": "Bang eggi baik bangett, sabar juga ngadepin orangg",
                "pesan": "Sehat selalu ya bang, jangan lupa istirahat"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak satu ini lucuu bangett orangnya ekspresif",
                "pesan": "Semangat kak kuliahnya, jangan lupa minum"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "Bang fabio kalem banget orangnya",
                "pesan": "Semangat terus bang, Istirahat jangan lupa"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Bang gio pinterr bangett, kaya albert einstein",
                "pesan": "Semangat bang gio, jangan lupa sarapan"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakaknya baik sekalii orangnya, lovs it",
                "pesan": "Semangat kak rahma menjalani kehidupan dewasa ini.."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "123450102",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak astut kuu yang paling sabarr ngadepin manusia kaya kami wkwk",
                "pesan": "Jaga kesehatan ya kak, jangan sampai sakit"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Bang razin introvert coded, atau mungkin memang belum banyak ngobrol aja ya bang",
                "pesan": "Semoga tercapai semua keinginannya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
    
if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Kakak selalu bisa menyampaikan pendapat dengan jelas dan terarah.",
                "pesan": "Semoga terus bisa jadi panutan dalam cara berkomunikasi yang bijak."
            },
          {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak tanggap banget kalau ada hal penting yang harus segera diurus.",
                "pesan": "Terima kasih udah selalu jadi sosok yang sigap dan bisa diandalkan."
            },
          {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva, follow @cerebral.id_",
                "kesan": "Kakak punya pandangan yang luas dan realistis soal kerja tim.",
                "pesan": "Semoga tetap bisa jadi sumber arahan yang menuntun banyak orang."
            },
          {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak tegas tapi tetap menghargai orang lain, keren banget.",
                "pesan": "Terus jaga keseimbangan itu ya, Kak, karena nggak semua orang bisa begitu."
            },
          {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kakak punya kemampuan organisasi yang rapi banget.",
                "pesan": "Semoga ke depannya bisa terus berbagi ilmu soal manajemen waktu dan kerja."
            },
          {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main-main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakak selalu totalitas dalam setiap kegiatan.",
                "pesan": "Semoga semangat itu nggak pernah luntur meskipun kesibukan makin banyak."
           },
          {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak punya ketenangan yang bikin suasana kerja jadi lebih terkendali.",
                "pesan": "Terus jaga ketenangan itu, Kak, karena itu hal yang berharga banget."
            },
          {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak nggak banyak bicara, tapi tindakan Kakak selalu berarti.",
                "pesan": "Semoga tetap jadi contoh lewat kerja nyata, bukan cuma kata-kata."
             },
          {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Kakak punya logika berpikir yang kuat dan rasional.",
                "pesan": "Terus gunakan cara berpikir itu buat bantu arah organisasi ke hal-hal yang baik."
              },
          {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak selalu berusaha nyelesain tugas sampai tuntas.",
                "pesan": "Terima kasih udah ngasih contoh tentang tanggung jawab yang konsisten."
            },
          {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam Naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakak bisa ngejaga profesionalitas meskipun suasana lagi santai.",
                "pesan": "Semoga bisa terus jadi teladan dalam hal sikap dan komitmen."
              },
          {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton reels Agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakak punya kemampuan membaca situasi dengan cepat.",
                "pesan": "Terus pertahankan kepekaan itu, Kak, karena penting banget di banyak hal."
             },
          {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak punya gaya kerja yang praktis dan efisien.",
                "pesan": "Semoga bisa terus nginspirasi buat kerja cerdas, bukan cuma kerja keras."
             },
          {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak sabar banget, terutama kalau lagi koordinasi sama banyak pihak.",
                "pesan": "Terima kasih udah ngajarin cara menghadapi tekanan dengan tenang."
               },
          {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakak punya cara berpikir yang terstruktur dan detail.",
                "pesan": "Semoga terus bisa bantu adik-adik belajar ngatur kerjaan dengan lebih rapi."
            },
          {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kakak punya selera yang khas, beda tapi menarik.",
                "pesan": "Semoga keunikannya terus kebawa sampai nanti, Kak."
              },
          {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakak gampang bikin orang nyaman tanpa banyak usaha.",
                "pesan": "Semoga ketulusan itu nggak berubah meski waktu terus jalan."
               },
          {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak punya cara sendiri buat menikmati hal-hal kecil.",
                "pesan": "Semoga kebiasaan itu terus ada, biar hidup tetap ringan."
              },
          {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakak punya vibe yang matang tapi tetap hangat.",
                "pesan": "Semoga makin banyak orang baik yang Kak temui di perjalanan."
              },
          {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak kelihatan sederhana tapi punya pemikiran dalam.",
                "pesan": "Semoga pikiran baik itu terus tumbuh dan menuntun ke hal-hal besar."
              },
          {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakak punya senyum yang tulus banget jarang loh yang gitu.",
                "pesan": "Semoga hidup Kakak dipenuhi hal-hal yang bikin senyum itu tetap ada."
              },
          {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakak punya cara ngomong yang tenang tapi jelas banget.",
                "pesan": "Semoga Kakak selalu bisa nyampaikan hal-hal penting dengan caranya sendiri."
              },
          {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak punya aura yang adem tapi tetap berkarisma.",
                "pesan": "Semoga ketenangan dan karisma itu selalu nyatu di tiap langkah Kakak."
             },
          {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajahi desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakak punya pembawaan yang tenang dan bikin nyaman dilihat.",
                "pesan": "Semoga kesehariannya selalu seadem itu juga ya, Kak."
             },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": 21,
                "asal": "Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@ranniku",
                "kesan": "Kakak punya cara jalan yang tenang tapi percaya diri, kelihatan banget karakternya.",
                "pesan": ": Semoga langkah Kakak ke depan selalu mantap dan nggak goyah."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": 22,
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak punya ekspresi yang susah ditebak tapi justru itu yang bikin menarik.",
                "pesan": "Semoga selalu ada hal-hal seru di balik ekspresi datar Kakak itu."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": 21,
                "asal": "Brebes, Jateng",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa.fhn",
                "kesan": "Kakak punya gaya ngomong yang halus tapi punya bobot.",
                "pesan": "Semoga selalu bisa nyampein hal penting dengan cara yang tetap tenang."
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": 20,
                "asal": "Pekan Baru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azzah.raaa_",
                "kesan": "Kakak kelihatan tegas, tapi masih punya sisi lembut yang kerasa banget.",
                "pesan": "Semoga dua sisi itu tetap seimbang, Kak, karena itu yang bikin khas."
            },
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450106",
                "umur": 18,
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakak selalu kelihatan siap di situasi apa pun, kayak nggak gampang goyah.",
                "pesan": "Semoga keyakinan itu tetap jadi pegangan Kakak terus ke depan."
            },
            {
                "nama": "Iqfinah Haula Halika",
                "nim": "123450076",
                "umur": 20,
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "iqfinanhalikaa_",
                "kesan": "Kakak punya gaya santai yang natural, nggak dibuat-buat.",
                "pesan": "Tetap jadi orang yang senyaman itu ya, Kak, dunia butuh yang tulus."
            },
            {
                "nama": "May Thalita Dehlia",
                "nim": "123450009",
                "umur": 20,
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak nggak banyak ngomong, tapi kehadirannya tetap kerasa.",
                "pesan": "Semoga tetap bisa nunjukin pengaruh besar tanpa harus banyak bicara."
            },
            {
                "nama": "M. Naufal Algahni",
                "nim": "123450116",
                "umur": 20,
                "asal": "Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": "Kakak punya pembawaan yang rapi tapi tetap santai.",
                "pesan": "Semoga hidup Kakak terus seimbang antara serius dan santai."
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": 19,
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kakak punya pandangan yang luas, tapi nggak pernah sombong.",
                "pesan": "Semoga tetap rendah hati meskipun tahu banyak hal."
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": 21,
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@reaxender",
                "kesan": "Kakak punya cara sendiri buat ngadepin sesuatu, dan itu unik.",
                "pesan": "Terus pertahankan cara khas itu ya, Kak, karena itu yang bikin beda."
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": 20,
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak punya vibe yang adem tapi tetap berani ngomong kalau perlu.",
                "pesan": "Semoga Kakak selalu bisa jaga keseimbangan antara tenang dan tegas."
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": 19,
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakak punya cara tertawa yang khas banget, gampang keinget.",
                "pesan": "Semoga banyak hal lucu dan ringan yang terus bikin Kakak ketawa kayak gitu."
            },
            {
                "nama": "Muhammad Hanif Zaki",
                "nim": "123450004",
                "umur": 20,
                "asal": "Padang",
                "alamat": "Perumnas, Way Kandis",
                "hobi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Kakak punya kesan misterius tapi tetap bikin penasaran.",
                "pesan": "Semoga di balik misterinya, Kakak selalu nemuin hal-hal baik buat diri sendiri."
            },
            {
                "nama": "Sarah Warti",
                "nim": "123450057",
                "umur": 20,
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwrti",
                "kesan": "Kakaknya ceria banget, selalu nyebarin senyum ke semua orang.",
                "pesan": "Semoga selalu bahagia dan terus semangat ngejar mimpi-mimpi kak!"
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": 19,
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": "Kakak punya gaya jalan dan cara ngomong yang kalem tapi berwibawa.",
                "pesan": "Semoga Kakak selalu dikelilingi hal-hal yang seimbang kayak diri Kakak sendiri."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@dananghk_",
                "kesan": "Kakak punya pembawaan yang kalem tapi matanya selalu fokus.",
                "pesan": "Semoga ketenangan itu terus jadi kekuatan Kakak ke mana pun pergi."
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakak punya tawa yang khas banget, gampang bikin orang ikut senyum.",
                "pesan": "Semoga hidup Kakak selalu punya alasan buat ketawa kayak gitu lagi."
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@den_iki_",
                "kesan": "Kakak kelihatan santai, tapi dari caranya ngomong keliatan banyak mikir dulu.",
                "pesan": "Semoga cara hati-hati itu terus bantu Kakak milih hal-hal baik."
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak punya gaya yang simpel tapi selalu keliatan pas di tiap suasana.",
                "pesan": "Semoga kesederhanaan itu terus jadi ciri khas Kakak."
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@aprhtp_",
                "kesan": "Kakak pendiam tapi ekspresinya kadang nyelip lucu tanpa sengaja.",
                "pesan": "Semoga sisi spontan itu nggak ilang, Kak, justru itu yang bikin hidup ringan."
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakak punya tatapan yang dalam, kayak selalu ada hal yang dipikirin.",
                "pesan": "Semoga semua hal yang Kakak pikirin pelan-pelan jadi hal yang baik."
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakak punya vibe tenang tapi kuat, kayak nggak gampang keganggu.",
                "pesan": "Semoga keteguhan itu tetap ada bahkan di hari-hari yang berat."
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "-",
                "asal": "-",
                "alamat": "",
                "hobbi": "-",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak punya gaya ngomong yang lembut tapi tetap tegas.",
                "pesan": "Semoga keseimbangan itu terus kebawa di tiap langkah Kakak."
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@englirahmdhanii",
                "kesan": "Kakak punya cara senyum yang tulus banget, kerasa dari jauh.",
                "pesan": "Semoga Kakak selalu dikelilingi hal-hal yang bikin senyum itu tetap muncul."
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@_inayasari",
                "kesan": "Kakak terlihat kalem, tapi kadang celetukannya nyeleneh dan bikin ketawa.",
                "pesan": "Jangan ilangin sisi lucu itu ya, Kak, pas banget buat nyantai."
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak punya gaya jalan yang ringan, kayak nggak pernah diburu waktu.",
                "pesan": "Semoga langkah Kakak selalu ringan juga di jalan yang Kakak pilih."
             },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak ciaa asik banget dan seruu bangeett",
                "pesan": "sehaatt selaluu dan selalu ceria kakk!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@rahmanellyana",
                "kesan": "pinterr bangeett dan ramah banget",
                "pesan": "semangaatt kuliahnya kakk!"
            },
             {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@mananam_",
                "kesan": "baikk dan sabar bangett ngajarin nyaa",
                "pesan": "semangaatt truss bangg!"
            },
            {
            
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@noe_rruuu",
                "kesan": "keren banget dan seru banget juga",
                "pesan": "semangaaatt kuliahnya bangg!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@rafidivaefangga",
                "kesan": "Seru banget abangnya dan ramah banget juga",
                "pesan": "semangaatt kuliahnya bangg"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@refadp_",
                "kesan": "seruu banget kakaknya dan asik banget",
                "pesan": "semangatt kak kuliahnyaa, besok tepuk doa bareng ya kak wwkkwkw"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@tryyaniciaaa",
                "kesan": "seruu bangeet kak dan ramah juga",
                "pesan": "Tetap semangat kak kuliahnya!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@aliyaamara",
                "kesan": "kereenn kakaknya dan seru juga",
                "pesan": "Semangat kuliahnya kak!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@donamaya.p",
                "kesan": "Kakaknya seru banget dan ramah juga",
                "pesan": "Semoga sukses di masa depaann kaakk!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@writtenbyangel",
                "kesan": "baiikk bangeett kakaknya dan asik bangettt",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget suka bantuin kalau kesusahan ngerjain praktikum alpro",
                "pesan": "Sukses untuk ke depannya, kak dan selalu berbuat baik!"
            },
             {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@naylasalsabilaa",
                "kesan": "baiikk bangeett kakaknya dan seru juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
             {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@saniayyllstr",
                "kesan": "baiikk bangeett kakaknya dan seru",
                "pesan": "semangaatt kuliahnya kak dan bahagia selalu kak!"
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "baiikk bangeett abangnya dan ramah juga",
                "pesan": "semangaatt bang!"
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@nltg._",
                "kesan": "baiikk bangeett kakaknya dan ramah juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@citrastin",
                "kesan": "baiikk bangeett kak dan asik juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@eigirtmv",
                "kesan": "baiikk bangeett kakaknya dan ramah bangett",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@roms.slbn",
                "kesan": "baiikk bangeett kak, asik juga dan ramah bangett",
                "pesan": "sukses terus kedepannya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

    

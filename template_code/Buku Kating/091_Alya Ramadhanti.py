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
            "https://drive.google.com/uc?export=view&id=18YoNwweOfqz20s4gYUpHxSuCq8Dw-H9o",
            "https://drive.google.com/uc?export=view&id=1w_xUFLAwvrgH4mMnvk6RSLdSaqkGUfiI",
            "https://drive.google.com/uc?export=view&id=1c__78nzIlcv5o01-a-DqBfpVIkBl-DJ-",
            "https://drive.google.com/uc?export=view&id=1RYh2EU69y1gKYAVP7cDynlB6KQ4ShyZr",
            "https://drive.google.com/uc?export=view&id=1w0SmJMxnk8jG1HcRrWM0bekc8tVAzWys",
            "https://drive.google.com/uc?export=view&id=1W0iZ_fRryYquLAhpUFxdJ3z0xnVV5Eh1",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@erendraa",
                "kesan": "keren banget banggg bisa jadi kahim ",  
                "pesan":"semoga selalu semangat dan bahagia!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "abangnya gokil tapi bijak, seru banget",  
                "pesan":"semoga tetap jadi inspirasi!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak ini asik bangett",  
                "pesan":"semoga kebahagiaannya gak pernah habis!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak aktif dan semangat banget",  
                "pesan":"semoga semua impiannya terwujud!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak seru banget tiap ngobrol",  
                "pesan":"semoga sukses selalu!"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kak keren tapi rendah hati",  
                "pesan":"semoga tetap ceria selalu!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dtlnfnQhgOhDRoS5Yruwkee7vkSSP4KA",
            "https://drive.google.com/uc?export=view&id=1Sa_Iw01VpbVyviv1TTHm967o60rHB9A2",
            "https://drive.google.com/uc?export=view&id=10Hl744yBcRhoSnE3P5tcVPtEoyzhKdgX",
            "https://drive.google.com/uc?export=view&id=1YPvl56cBcMQDV-iDnbjD4Sr-yZZsMciV",
            "https://drive.google.com/uc?export=view&id=1T6VB6MP2aVEeU95IODGQZz0wvMDifrWH",
            "https://drive.google.com/uc?export=view&id=1daepOOQFpJe7ZT3znM6nVopCGqWLp8xL",
            "https://drive.google.com/uc?export=view&id=1BbeBViL_QKEeFWE364L_2nUTshDTklKq",
            "https://drive.google.com/uc?export=view&id=1SnjGWmLfsT3VLrakVRIXdsNaWv_Ssde0",
            "https://drive.google.com/uc?export=view&id=1VzORbHUQHW9xSYhUzJXkZMV25frOgedy",
            "https://drive.google.com/uc?export=view&id=13c4ZpKAfY4HlXsAZuxp0SISwawNFxMNG",
            "https://drive.google.com/uc?export=view&id=1lyBGnQcBCadeHlArbjbW2243yky0plsX",
            "https://drive.google.com/uc?export=view&id=1zw3D2J-zv0vpVGGmle0RabO0w8db-v9M",
            "https://drive.google.com/uc?export=view&id=123fM4xlv3NFEiPt00aZ7HsD9hZMFLQ9_",
            "https://drive.google.com/uc?export=view&id=1IkjItL7ajT84tO3_5rXxlG6ti4nNzZU_",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122340022",
                "umur": "21",
                "asal":"Nusa Kambangan",
                "alamat": "Lapas, Belwis",
                "hobbi": "Melarikan diri",
                "sosmed": "@jeremia_s_",
                "kesan": "keren banget banggg bisa jadi kadiv",  
                "pesan":"semangat terus kuliahnya bangg" # 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Seru banget kenal kakak",  
                "pesan":"semoga selalu semangat dan bahagia!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya humble banget",  
                "pesan":"semoga semua cita-citanya tercapai!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Kakaknya inspiratif banget",  
                "pesan":"semoga tetap jadi inspirasi!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "Abang gokil tapi bijak",  
                "pesan":"sukses selalu abang!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Asik banget ngobrol sama kak",  
                "pesan":"semoga selalu sehat dan bahagia!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "Abangnya berwibawa tapi gak kaku",  
                "pesan":"Terus pertahankan sikap positifnya ya abang!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya selalu semangat dan gak pernah nyerah.",  
                "pesan":"Semoga semangatnya terus nular ke kami!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kak keren, aktif, dan tangguh banget.",  
                "pesan":"Tetap semangat ngejar cita-citanya!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "Kaknya lucu, bikin kegiatan jadi seru.",  
                "pesan":"Semoga gak pernah kehilangan keceriaan itu ya kak!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya tegas tapi adil banget.",  
                "pesan":"Semoga makin banyak prestasi diraih."# 1
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya punya semangat tinggi banget.",  
                "pesan":"Teruskan semangat itu, abang pasti sukses!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450123",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Kak aktif banget, semangat terus ya!",  
                "pesan":"Semoga semua kerja keras kak terbayar nanti."# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak suka bercanda tapi bijak juga.",  
                "pesan":"Tetap jadi sosok yang menyenangkan kayak sekarang."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w-nmax4eh4nwTowPqHUt6vAN8TtFMPHW",
            "https://drive.google.com/uc?export=view&id=13zNx2hMn1qDWO2pBlsWXDsWyvOfc9EB_",
            "https://drive.google.com/uc?export=view&id=1T3WF7mloShuLtTdDAQ-5NeMWAmI3c0XR",
            "https://drive.google.com/uc?export=view&id=1HzoAAUPPgo9J9Nzo9Kacm5hj2opvnlC2",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Tanya Caesar",
                "hobbi": "Padel",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya seru banget!",  
                "pesan":"semangat terus kuliahnya abang!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "Ramah dan gampang akrab.",  
                "pesan":"Sukses selalu ya kak!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "Asik dan sabar banget.",  
                "pesan":"Semoga semua capaiannya makin tinggi!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kak inspiratif banget",  
                "pesan":"semoga makin berprestasi terus!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DEySMq_Q3XXwMm88UFta1hsyAuu6iKTp",
            "https://drive.google.com/uc?export=view&id=1gMgAM3UExvm7YtIFaJu7KxZH4uokk116",
            "https://drive.google.com/uc?export=view&id=1iRVv9k04xOLAQx8KztttZrZHLNwxakJE",
            "https://drive.google.com/uc?export=view&id=1TxotVbF0qO1yk28JJFR6OM0Bf6MW8s-J",
            "https://drive.google.com/uc?export=view&id=1KlYaQ7rCSBvbAzopEinBcLg2I9lZZKxK",
            "https://drive.google.com/uc?export=view&id=1yjC2zizSAVpKSbdMIXYT1QBwfoTNBcWo",
            "https://drive.google.com/uc?export=view&id=1wIEkHkDb0FuvX1pSTx5vDwdcn0D0viK7",
            "https://drive.google.com/uc?export=view&id=14BygTBlFY8wdeKCLrraBbVN3sh4sqkXS",
            "https://drive.google.com/uc?export=view&id=19oKDRn8_dvT0mAZOQpw_wSTRAQUPl7TY",
            "https://drive.google.com/uc?export=view&id=1OBuTyR4Fr9CgTfqXKYHwzOb-rV24p2N7",
            "https://drive.google.com/uc?export=view&id=1m0Eij6emH7iVMK_Dbba8CBh_vvF5ZJ7y",
            "https://drive.google.com/uc?export=view&id=12e_j2DgVIqaAcgn0TsgLlLrX9TFW3ChK",
            "https://drive.google.com/uc?export=view&id=1dDUCtoIaS93zrkLitAvvV9gtCEHoCsmM",
            "https://drive.google.com/uc?export=view&id=1n_oP9BPN6uDzxTXIlDk9PKcJBBGG_9Hw",
            "https://drive.google.com/uc?export=view&id=1IOG0kRkFxvaMx2DBA56TOL9QWsDyiwYP",
            "https://drive.google.com/uc?export=view&id=1rcDxsPPJihMooXck_rklsoXjhT7iIhRz",
            "https://drive.google.com/uc?export=view&id=1_e8zUF3qwfVUSKSbTAuMUL3fClCGB3g-",
            "https://drive.google.com/uc?export=view&id=1Xid8SlT_jmzzNh6ghiH-RUyvURfq6hIX",
            "https://drive.google.com/uc?export=view&id=1Xid8SlT_jmzzNh6ghiH-RUyvURfq6hIX",
            "https://drive.google.com/uc?export=view&id=1i9iLZxd7AdwICLutme7rM4QXyEicY7EG",
            "https://drive.google.com/uc?export=view&id=1IfktzCVAf0peghC_fNWtGkz1YTMmNLrJ",
            "https://drive.google.com/uc?export=view&id=15jp-HB5091Q6SPBs-gdgy4heFaIrdBk4",
            "https://drive.google.com/uc?export=view&id=1EKfLS5O84FYJrBA9lUU0YmNDt0bOT4XU",
            "https://drive.google.com/uc?export=view&id=1mrEAbcFevvFMQd_aCIyw5nusfYCrW4tl",
            "https://drive.google.com/uc?export=view&id=1PlU9798oAuhYQ-aS_Eoj8bZbzTpTbuVw",
            "https://drive.google.com/uc?export=view&id=1D__GR6aRpNG3rDTb4PTEcGFOl0UDC22n",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Nangis dan Ketawa",
                "sosmed": "@afifahhnsrn",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "GH",
                "hobbi": "Ngekader",
                "sosmed": "@ahmad.rizky__",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Airan",
                "hobbi": "Cari Kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Panjang",
                "alamat": "Panjang",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Main PS",
                "sosmed": "@nobelnizam",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Si8gma Fam",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kosan Elite Airan",
                "hobbi": "Jalan-jalan Cari Cowok",
                "sosmed": "@vany.salsabilaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahidzz_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur Aja",
                "sosmed": "@ferazkaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Maen Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Maen Game",
                "sosmed": "@sahid_maulana",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngomelin panitia sainfest",
                "sosmed": "@ahmadnaufal_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Maen piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis, Pemda",
                "hobbi": "Pemasok Tugas",
                "sosmed": "@ihsan.myusuf",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natsyyaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "-",
                "pesan": "-"
            },
             {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen Mikfes":
    def Departemen_Mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wTSVEaT82xsHEc5cqxcQ3x_oysJ-y1sP",
            "https://drive.google.com/uc?export=view&id=1Jy4AJr-u5rU5uAGYx_ZVedp0ojXuYFFL",
            "https://drive.google.com/uc?export=view&id=11JNOPt-MelVTfNV4nYuKuvhC9m16FpXs",
            "https://drive.google.com/uc?export=view&id=1RMvC_DcJdcNv_iSwbUtzAfaUFyECCkvT",
            "https://drive.google.com/uc?export=view&id=1nIAlzS1eoRVR57TCLR5cXXLY16FyGYo_",
            "https://drive.google.com/uc?export=view&id=1ybk0VrWseKLtuogs0sRXKn90dqMW0XgS",
            "https://drive.google.com/uc?export=view&id=1O76K-v_5PNuvYxeqPqZI5WZ2jcillEV9",
            "https://drive.google.com/uc?export=view&id=13V99gSF94fkzYP2w92Wbv6TtdTxoaWRO",
            "https://drive.google.com/uc?export=view&id=1CB6xZZw2z8OAJXtS7jhv_s8viKshV4VQ",
            "https://drive.google.com/uc?export=view&id=1obQS8H_Qmgo95YZhEEjFPxFpf2Ofg7pt",
            "https://drive.google.com/uc?export=view&id=1uuKfcbiNfH0bw3QOS0X37SFHVYxfYnXT",
            "https://drive.google.com/uc?export=view&id=1f16zuPtkWoKE6NqJhcHJlzKlO5IvHkP5",
            "https://drive.google.com/uc?export=view&id=1kXyJh_8_DLGGxHPeN2mUM4h01c4IU-sq",
            "https://drive.google.com/uc?export=view&id=1pevPMz9_AEB4veaOEIngqor6GqgLNNio",
            "https://drive.google.com/uc?export=view&id=19lpklmtvTLPS4rgqSUMxqlWLpMeYfXU4",
            "https://drive.google.com/uc?export=view&id=16dQk1lwfeLhKtceXd5r59csXVNzJYDLR",
            "https://drive.google.com/uc?export=view&id=1HCm1U-fI0qeoqv666w371QmFJ4XSTcoC",
            "https://drive.google.com/uc?export=view&id=1NOIQgbXOC-jMDBqlzPcbC5ytMFxemGlu",
            "https://drive.google.com/uc?export=view&id=1JNZlzjbjXA0GOi2CGmeFj8Sc7w-G_pUC",
            "https://drive.google.com/uc?export=view&id=1OY-t6oaM98WEhtbpfxHLMoMwOdVI-d2e",
            "https://drive.google.com/uc?export=view&id=1AgPvNSkdZmxXOdvdSPCi-70mNpYygiXe",
            "https://drive.google.com/uc?export=view&id=1wYAQ0PA35WLe41QfhnPoIkG5OUC2Egpx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "123440083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "keren banget banggg bisa jadi kadiv ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya humble dan enak diajak diskusi. ",
                "pesan": "Tetap semangat terus ya kak!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Seru diskusi bareng abang, nggak pernah bikin tegang.",
                "pesan": "Sukses selalu buat abang"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kaknya inspiratif banget. ",
                "pesan": "Terus semangat dan bahagia selalu!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Bikin suasana divisi jadi seru. ",
                "pesan": "Terus sebarkan semangat positifnya ya!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya lucu, tapi juga profesional. ",
                "pesan": "Semoga makin keren ke depannya!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Katingnya asik banget, ngajarin dengan sabar.",
                "pesan": "Tetap semangat terus ya kak!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "Ramah dan suportif banget.",
                "pesan": "Jangan lupa istirahat juga ya kak!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kaknya easy-going banget.",
                "pesan": "Terus semangat dan bahagia selalu!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Kaknya disiplin tapi asik.",
                "pesan": "Terus jadi contoh yang baik ya kak!"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kaknya asik diajak ngobrol",
                "pesan": "Semoga semangatnya nular ke kami"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "Kakaknya sabar banget ngajarin ALE",
                "pesan": "Makasih udah sabar bimbing kami"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "Kak Fabiolla keren banget, selalu terlihat berwibawa dan sopan!",
                "pesan": "Semangat terus kuliahnya kak, semoga semua impianmu tercapai!"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kak Fairuz lucu dan santai banget, tapi tetep berwawasan luas! ",
                "pesan": "Terus semangat kuliahnya kak, jangan lupa istirahat juga ya"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "Kak Tanty seru dan easy going banget, bikin suasana rame jadi asik! ",
                "pesan": "Tetap jadi pribadi yang ceria dan semangat terus kuliahnya ya, kak!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Bang Eggi asik banget dan selalu bisa bikin suasana jadi santai! ",
                "pesan": "Semangat kuliahnya kak, semoga makin sukses"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah unik banget, random tapi selalu bikin ketawa",
                "pesan": "Tetap jadi kakak yang seru dan semangat terus ngejar cita-citanya!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "Bang Fabio keren dan easy going banget, enak diajak ngobrol!",
                "pesan": "Semangat terus kuliahnya kak, semoga sukses"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Bang Gio keren dan tenang banget",
                "pesan": "Semoga makin sukses dan tetap rendah hati ya, bang!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kak Rahma kalem tapi tangguh, selalu terlihat ceria dan positif!",
                "pesan": "Semangat terus kuliahnya kak, semoga semua urusan dipermudah!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Kak Rahmah lucu banget dan suka bikin suasana jadi rame",
                "pesan": "Tetap semangat kuliahnya kak, semoga selalu bahagia!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Bang Razin baik banget",
                "pesan": "Semangat terus kuliahnya kak, semoga sukses di setiap langkah!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xuRbH7RBb-WesJrYAyWks77SGowD8kSm",
            "https://drive.google.com/uc?export=view&id=1B4jYyzREMl-rvQ31lBpSPx-aopf48XPH",
            "https://drive.google.com/uc?export=view&id=1hkAMb1Eyw-7Tl3MXrnLmQPTlTqJGLTK1",
            "https://drive.google.com/uc?export=view&id=1DDJ_yc6mOkswc4Q1sFSt4Rt4iV7rp18L",
            "https://drive.google.com/uc?export=view&id=1pNvkOceLzSEE8bKaz9BtHrzjOzTUSuMM",
            "https://drive.google.com/uc?export=view&id=1fb4QCEQBxUP0SNWZaxV5LNPohcsWm4wm",
            "https://drive.google.com/uc?export=view&id=1O50ToGgciBi40CTcBxTExLAillqQvOey",
            "https://drive.google.com/uc?export=view&id=1APTTnlSG3q_JTQH9UFP7LWYaopFWcdbL",
            "https://drive.google.com/uc?export=view&id=1jGXU05kvBKB-Q7Cm8hvjnl29wambAHjz",
            "https://drive.google.com/uc?export=view&id=1IwHdVr-lDusAYy56HIAdUdRc4rurx286",
            "https://drive.google.com/uc?export=view&id=1vcSMGpASTyvuoX0cR8OHCDLROu7gjWMG",
            "https://drive.google.com/uc?export=view&id=1isV_Nf87FCAbt5kRO0-CmjZidqVZXVgn",
            "https://drive.google.com/uc?export=view&id=12J_D5e2aEc9P7ph5218Bgyv2b4EJHK05",
            "https://drive.google.com/uc?export=view&id=1zgjsokxSu6W86Kb5_6PSOrLQ-h4MyfPd",
            "https://drive.google.com/uc?export=view&id=1aLjnf9pSDiI8Rp9sSR8w7dQoPVIkj27B",
            "https://drive.google.com/uc?export=view&id=1g70v6Hs6WRG5RzPC5-7BdUPObGRp7I_c",
            "https://drive.google.com/uc?export=view&id=1OzQu8U-mL33iInqEuW-hufExTBDfqT5V",
            "https://drive.google.com/uc?export=view&id=1Wdq8IN8eB3cPaSrRuClmtN46VUoqC2MK",
            "https://drive.google.com/uc?export=view&id=1h-l76junFuWXAv3X9Lti9xGLJH28YH7N",
            "https://drive.google.com/uc?export=view&id=10r5zpY8dV4PQfp7bbCa7fcdO0aC0iuO1",
            "https://drive.google.com/uc?export=view&id=18rO8OZgGKWuUdHSeZvsnVpoz2v3mf3YA",
            "https://drive.google.com/uc?export=view&id=1wyx5blccugjsiiCKwmucSKqTI-eQepmT",
            "https://drive.google.com/uc?export=view&id=1-RZn6xBaaGyE4Qpt4cnc9S_6NP4Vzw95",
            "https://drive.google.com/uc?export=view&id=1qWm9IXj4Fu6uqfqFjBYB5oQGcy7oonXB",
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
                "kesan": "Bang Arafi kadiv yang kalem tapi tetep asik dan bikin suasana nggak kaku",
                "pesan": "semangat terus kuliahnya bangg!!!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana keliatan rajin dan semangat bangett",
                "pesan": "Jangan capek belajar ya kak, semoga semua usahanya membuahkan hasil"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini lucu banget dan namanya cantik banget kek orangnyaa",
                "pesan": "Tetap jadi diri sendiri dan terus menebar energi positif ya kak"
            },
           {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arin keliatannya tegas tapi ternyata baik banget dan ceriaa",
                "pesan": "Semoga suatu hari beneran bisa keliling dunia seperti hobinya!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abang nya santai banget pembawaannya",
                "pesan": "Semoga tetap semangat dan makin sukses di kuliah maupun hidup!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Mut beneran imut seperti namanyaa, asik jugaa",
                "pesan": "Terus jaga semangat dan jangan lupa istirahat di tengah kesibukan"
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakaknya murah senyum dan ceria banget",
                "pesan": "Semoga makin jago ngulik data dan sukses di bidang yang disukai!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabila sabar banget pas ngajarin tutor",
                "pesan": "Tetap semangat dan jangan lupa istirahat di tengah aktivitas padat ya kak"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abangnya baik banget da tenang pembawaannya",
                "pesan": "Semoga sukses terus bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "Kakaknya humple parahh, cantikk jugaa",
                "pesan": "Semoga kuliahnya lancar dan tetap semangat meski ngantuk melanda!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "Kak cindy canntik, dan baik banget",
                "pesan": "Semangat selalu kakk, sukses yaa"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "Kak Dea vibes-nya kalem tapi lucu banget kalau udah ngobrol.",
                "pesan": "Tetap semangat kuliahnya dan jangan lupa bahagia ya kak"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman ternyata baik banget dan seruu, video main gitarnya sering masuk fyp bangg",
                "pesan": "Semoga terus berkembang dan bisa tampil di panggung besar nanti"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "Kak Sonya asprak cantikk dan sabar banget pas ngajarin",
                "pesan": "Semangat terus kak, tutor jago dong kak"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "Kak Luthfia lucu dan suka ngelucu, bikin suasana jadi cair banget.",
                "pesan": "Semangat terus dan jangan suka nyubit Ketang lagi ya kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "Bang Irvan kadep pengmas yang walopun keliatan diem tapi keren banget dan baik  ",
                "pesan": "Semoga makin sukses dan tetap semangat main badminton terus"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Bang Adit mentor yang udah seakrab itu sama kita kita, kocak banget orangnya tapi selalu fokus kalo udah serius, sering dengerin cerita jugaa open minded bangett",
                "pesan": "Teruslah belajar dan berani buka peta baru dalam hidupmu, bang"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fatya awalnya suka ketuker namanya sama kak tarisya, sejauh ini ternyatab asik banget, sabar bannget pas ngajarin jadi mc",
                "pesan": "Semoga kuliahnya lancar dan bisa jalan jalan terus sama bang adit ya kak!"
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "Kak ilmi orangnya seru parahh, kocaak jugaa, gampang banget akrab sama adek adeknya  dan keliatan energi nya gaperna abis ya kak",
                "pesan": "Terus semangat dan ceria selalu ya kak"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melin dari awal liat udah salfok cantik banget, terus pembawaannya tenang banget dan asik pas di ajak ngobrol ",
                "pesan": "Semangat kaka modelll"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla humble banget dan murah senyum, asik juga pas diajak ngobrol",
                "pesan": "Semangat kakak, infokan tempat me time yang enak dong kak"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak izzah yang menurutku paling kalem dan pembawaannya tenang banget tapi kalo ada saat yang serius keren banget jelasinnya ",
                "pesan": "Semangat kuliahnya, dan semogaa bisa buka toko kue ya kaa"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois orangnya keliatan kalem dan serius tapi ternyata kalo udah bercanda asik banget dan mudah mencairkan suasana ",
                "pesan": "Semangat terus abangg, hati hati dijalan kalo lagi ngabisin bensin"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "Kak Tarisya baik baik baikk bangett, kalo liat tu bawaannya tenang banget dan keren banget klo udah lagi jelasin suatu hal, apalagi pas ngasprak sabar banget ngajarin satu satuu",
                "pesan": "Semangat terus ya kak, semoga hal hal baik selalu menyertai"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1onkp3-kadlPvQYO5LcRVY6ORe9ng60ME",
            "https://drive.google.com/uc?export=view&id=1lWIFm3a9dep8hUCsJZnC0Qr07T706RxH",
            "https://drive.google.com/uc?export=view&id=1mUl4-ZLVDgvfr5aA_KoD8w4kGkLajbZJ",
            "https://drive.google.com/uc?export=view&id=1NPM7bqjhVI1kvfnWyMFEZVLkQw5uOj6_",
            "https://drive.google.com/uc?export=view&id=19Yryw9UqAgfIt5XEAU3VXew8oRBGFsTf",
            "https://drive.google.com/uc?export=view&id=1cKgHOiQhm0RXPLNTQyau2VpdON1DEQMl",
            "https://drive.google.com/uc?export=view&id=1iACV61NMMcy0Q-KWNpJgMxL_1yzwWs_t",
            "https://drive.google.com/uc?export=view&id=1ODP2Xnr5wLinfpR4UZ7NrJ9h-ab77OVC",
            "https://drive.google.com/uc?export=view&id=1AOAgmHszjeqwwltndqH7wkJ9RuwDrj1t",
            "https://drive.google.com/uc?export=view&id=1uctjkiJ4vLpu8lVCShGwamEBYAhEys6s",
            "https://drive.google.com/uc?export=view&id=1VxFloyY_n2HEPmUzHQ8fD34aG2I5z_Ed",
            "https://drive.google.com/uc?export=view&id=1k6BPXp1JQ7N-yANWnCp2tnFQVPLc2h9u",
            "https://drive.google.com/uc?export=view&id=1Ca8FzITurVEjQEqwNa35VbUHb0knlZi0",
            "https://drive.google.com/uc?export=view&id=15s-xgEWE2cW_kKpFM-v_r2vxV4mXIrEy",
            "https://drive.google.com/uc?export=view&id=1z6Y-WAXHtVp0E7_XrOr8ybC-uWzHIHLe",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Balam",
                "hobbi": "mengaji",
                "sosmed": "@ranniku",
                "kesan": "Kak Rani orangnya seru dan asik banget ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta asik dan terbuka banget, suka ngajarin hal-hal baru. ",  
                "pesan": "Terus jadi sosok yang humble dan inspiratif ya kak!" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa lembut tapi tegas, keren banget cara bicaranya. ",  
                "pesan": "Semoga makin sukses dan tetap semangat ngejar cita-cita!" # 3
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "Kak Rendy orangnya kreatif banget ",  
                "pesan": "Terus kembangkan bakatmu, kak!" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kak Azzahra ramah dan lucu banget, gampang bikin suasana cair. ",  
                "pesan": "Semoga semua impianmu tercapai dan makin sukses di masa depan!" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "Bang Haikal orangnya asik dan humoris, selalu bisa bikin orang ketawa. ",
                "pesan": "Tetap semangat kuliahnya" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak Iqfina lucu, enerjik, dan selalu ceria, bikin suasana rame.",  
                "pesan": "Semangat terus kuliahnya, semoga makin rajin dan sukses selalu" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "Kak May orangnya baik ",  
                "pesan": "semangat terus kuliahnya kak" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "Bang Naufal pendiam tapi punya banyak ide keren, lowkey smart! ",  
                "pesan": "Semoga karier dan kuliahnya berjalan lancar terus, Bang" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Bang Zailani aktif dan punya semangat tinggi, panutan banget. ",  
                "pesan": "Tetap rendah hati dan terus berprestasi ya Bang!" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Kak Hanna orangnya asik banget suka bercanda ",  
                "pesan": "Terus semangat ngejar impianmu dan jangan lupa istirahat ya kak" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Kak Keren orangnya ramah dan gampang akrab sama siapa aja. ",  
                "pesan": "Semoga makin percaya diri dan selalu bahagia di setiap langkah" # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "Bang Hanif lemah lembut banget tapi asik",  
                "pesan": "Semoga sukses terus di kuliah dan tetap jaga semangatnya ya Bang" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "Kak Sarah punya vibe positif, selalu senyum dan sopan banget. ",  
                "pesan": "Tetap semangat kuliahnya dan jangan lupa jaga kesehatan, kak" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Kak Zahra kalem tapi punya aura ceria yang bikin nyaman. ",  
                "pesan": "Semoga makin sukses dan terus jadi kebanggaan banyak orang" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DqSpArxKe0k5suujGUund78y91fHEze2",
            "https://drive.google.com/uc?export=view&id=17Y2essZKUK4GuI-EupbPkziSX3F8Llr",
            "https://drive.google.com/uc?export=view&id=1XFvEyctiXr78AQvFXWFWEAVMp8OVXFHD",
            "https://drive.google.com/uc?export=view&id=1a33r5PyXB968awhT1GYOanQ-fK4z-aqg",
            "https://drive.google.com/uc?export=view&id=1w8D5UMWTqzXJv1eQS05fgzg7GolM4I3y",
            "https://drive.google.com/uc?export=view&id=1slo_7CCzmrsBtcIQDwq33G_0LuXiemrq",
            "https://drive.google.com/uc?export=view&id=1xtTMdNMymYdA-3UD6rOZ36eSUhAYOd68",
            "https://drive.google.com/uc?export=view&id=1gKjTn9togGoifETi4iSRduGl4jUK_Li6",
            "https://drive.google.com/uc?export=view&id=1upalc0jJS5XePMAvB2ywzp0ETM6RQ-pI",
            "https://drive.google.com/uc?export=view&id=1jLiyG2MvELlLdHu-Tyw32TCf0nody74D",
            "https://drive.google.com/uc?export=view&id=1j7RMChU7l_2AazW74jhglVcNopgxiczn",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya seru banget dan selalu kelihatan semangat, vibes-nya positif terus! ",
                "pesan": "Tetap jaga semangat kuliahnya ya bang, semoga sukses terus!"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kak Syalaisha orangnya kalem tapi asik diajak ngobrol, selalu terlihat tenang.",
                "pesan": "Semangat terus ya kak, semoga semua urusannya lancar!"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "keren banget banggg bisa jadi contoh stylish dan berwibawa!",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "Kakaknya friendly banget, gampang akrab sama siapa aja. ",
                "pesan": "Tetap jadi pribadi yang ceria dan positif ya kak!"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "Orangnya ramah, bikin suasana nggak kaku.",
                "pesan": "Semangat terus ya kak April, semoga kuliahnya lancar dan sukses selalu!"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kak Nabila punya aura tenang dan elegan, enak banget diajak ngobrol santai. ",
                "pesan": "Semoga sukses di segala hal yang kakak jalanin!"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakaknya pinter dan fokus, tapi tetap santai kalau diajak bercanda.",
                "pesan": "Tetap semangat ngejar mimpi dan jangan lupa istirahat juga"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Selalu senyum dan ramah, bikin suasana sekitar jadi adem ",
                "pesan": "Semoga segala urusan kak Devi dimudahkan dan sukses selalu!"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "Kak Enggli suka banget cerita hal-hal seru ",
                "pesan": "Terus jadi kakak yang ceria dan inspiratif ya!"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak Inaya kalem tapi peka banget sama sekitar, sosok yang bisa diandalkan. ",
                "pesan": "Semoga selalu diberi kelancaran di kuliah dan kehidupan, kak!"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "Kak Nydia punya kepribadian yang ceria, rame tapi tetap sopan. ",
                "pesan": "Terus semangat dan semoga makin sukses di masa depan!"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wFXEE9kZ1qfpPO71Z2cLsOEgLacwCjEc",
            "https://drive.google.com/uc?export=view&id=1Eepu_d_wI10OvPHYxeurLr-Sf0YAExfm",
            "https://drive.google.com/uc?export=view&id=1yCJgyjsqz4JocBiB3kcE8vX80JwaCZEd",
            "https://drive.google.com/uc?export=view&id=15Wxwu9D9S3zXgikCa1CIu3NH8tpDlfnL",
            "https://drive.google.com/uc?export=view&id=1iBj0exKcuQ8P77r4o2kNTWnJk4fPrpFE",
            "https://drive.google.com/uc?export=view&id=1J5ZskXxbDsfcBlaB45mBdg5y1ExsRDnd",
            "https://drive.google.com/uc?export=view&id=1sGVQBffSQHY_NXqWNkwbG1k7ImaCTaAr",
            "https://drive.google.com/uc?export=view&id=1isfI0EEBmyIFkW_qEVRsO3VKu3mpQKez",
            "https://drive.google.com/uc?export=view&id=1NEeW_dEKiSjn1D6zUjCYKV04HQStXJ2P",
            "https://drive.google.com/uc?export=view&id=1FJvFNnfva2EEn_QJDLuGKJFxu8nW4asm",
            "https://drive.google.com/uc?export=view&id=1BAczIkmIXHAyBQTEjHh_UiqzMvd-FolT",
            "https://drive.google.com/uc?export=view&id=15Gusu8p3kcdNEtf7PK3XQNmdlWnwpTfE",
            "https://drive.google.com/uc?export=view&id=1Ul9FFsTu2bD_NMNxKoM-6ZIFexdnRxpz",
            "https://drive.google.com/uc?export=view&id=1FkTtUzyLj0XwYmZ_hBIzY5wdsQITIHwz",
            "https://drive.google.com/uc?export=view&id=1L_6FSCPlrbY_Svco57pAWmn7lgNJhMwy",
            "https://drive.google.com/uc?export=view&id=1NHQIw37dBAWtnREZCTJoCMNzqCbmq0G-",
            "https://drive.google.com/uc?export=view&id=1HkjE3uXzuA30HKOT_MAJ43Jwn6ux5alw",
            "https://drive.google.com/uc?export=view&id=1uTGeSw4QjNVbo02eKH9CntU__i8O46T8",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jati Mulyo",
                "hobbi": "sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak Cia anggun dan pinter banget, selalu tampil percaya diri.",
                "pesan": "Semangat terus kuliahnya kak, semoga selalu diberi kelancaran dan kebahagiaan!"   # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kak Patricia keren banget, gayanya kalem tapi berkarisma! ",
                "pesan": "Semangat terus kuliahnya kak, semoga sukses dan makin hebat!"   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "Bang Anam asik, santai tapi tetap fokus kalau diajak bahas hal penting. ",
                "pesan": "Semangat terus kuliahnya bang, semoga semua target bisa tercapai!"   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "Bang Noel orangnya keren, kalem tapi seru kalau udah kenal.",
                "pesan": "Tetap semangat kuliahnya bang, semoga makin sukses dan bahagia selalu!"   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "Bang Rafi asik, santai tapi tetap fokus kalau diajak bahas hal penting.",
                "pesan": "Terus semangat di kuliah dan kegiatan lainnya bang, sukses selalu!"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa kreatif banget, selera gelangnya unik dan keren! ",
                "pesan": "Semangat terus kuliahnya kak, semoga makin berkilau ke depannya!"   # 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Kak Try Yani rajin dan selalu semangat belajar, inspiratif banget! ",
                "pesan": "Semoga ilmunya bermanfaat dan kuliahnya lancar sampai lulus, kak!"   # 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kak Aliya punya bakat musik yang keren",
                "pesan": "Tetap semangat kuliahnya dan terus kembangkan bakatmu ya, kak!"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna lembut dan kalem ",
                "pesan": "Semangat terus kuliahnya kak, semoga semua cita-citanya tercapai!"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kak Feby stylish banget, vibes-nya tenang tapi berkelas!",
                "pesan": "Semoga kuliahnya lancar dan selalu dikelilingi hal-hal baik, kak!"   # 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kak Hafsa rajin dan jago banget masak, calon chef nih ",
                "pesan": "Terus semangat kuliahnya kak, semoga sukses di semua hal!"   # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla lembut dan manis banget, selalu terlihat positif! ",
                "pesan": "Tetap semangat ya kak, semoga semua mimpinya bisa terwujud!"   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania ceria banget dan selalu bawa vibes positif ke sekitar! ",
                "pesan": "Semangat terus kuliahnya kak, tetap jadi pribadi yang menyenangkan!"   # 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Bang Akmal chill banget, tapi tetap tanggung jawab kalau ada tugas.",
                "pesan": "Tetap semangat kuliahnya bang, semoga sukses dan makin keren!"   # 14
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana rajin banget, apalagi kalau soal baca dan nulis!",
                "pesan": "Semoga selalu semangat belajar dan terus jadi inspirasi kak!"   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "Kak Citra punya jiwa seni yang kuat ",
                "pesan": "Semoga makin sukses dan terus berkarya lewat karya senimu kak!"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "Bang Eigi kreatif dan penuh ide ",
                "pesan": "Terus semangat kuliahnya bang, semoga semua impianmu terwujud!"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Bang Romauli energik banget ",
                "pesan": "Semangat terus kuliahnya bang, semoga makin bersinar dan sukses selalu!"   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()











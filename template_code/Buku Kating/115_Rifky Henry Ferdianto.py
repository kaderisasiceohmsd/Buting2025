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
            "https://drive.google.com/uc?export=view&id=1_WB-NQPJkRrss8lPdH1Ci6h0idlOAOqT",
            "https://drive.google.com/uc?export=view&id=1HGA0CUrN0ae4Xjq5KgYLZvUuQMLDYsoL",
            "https://drive.google.com/uc?export=view&id=1AYrddRJ6ZoZMAmNa8VyAN8SvNeeM6zkb",
            "https://drive.google.com/uc?export=view&id=1Qy2fYRpPfvWd2bob3cowe7iK5w45CGhf",
            "https://drive.google.com/uc?export=view&id=1QjZQ8Jpktnr3A_yODp677gOQizoU4kXX",
            "https://drive.google.com/uc?export=view&id=1PN_-OJtGFpi9nK-GkjPjTz4rQIv3u-AH",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Makan Pisang",
                "sosmed": "@_erendraa",
                "kesan": "Pisangnya jangan lupa, bang.",
                "pesan": "Sukses terus, ketua!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kutu buku sequel sejati.",
                "pesan": "Bagi-bagi ilmunya, bang!"# 1
            },
                {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Jahilnya ngangenin, kak.",
                "pesan": "Jangan berhenti gangguin kita, ya."# 1
            },
                {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Ratu tidur, tapi gerak cepat.",
                "pesan": "Semangat terus, kak!"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Setia kawan sampai jurang.",
                "pesan": "Hati-hati di jurang, kak."# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Galak-galak sayang sama kahim.",
                "pesan": "Kurangi cuteknya dikit, kak."# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1y7-pA5gAcW4iqdJDLs0lRFAp-ZHA_S4D",
            "https://drive.google.com/uc?export=view&id=124GLVqtY4OAVmVR1vehWvCpM1-wZNNzS",
            "https://drive.google.com/uc?export=view&id=1rMo8qlFfj6yYMenxjb3E6dqFmjef7fx6",
            "https://drive.google.com/uc?export=view&id=1AnpppechrkiE8RJcJRdwboRDlQ6tJl-f",
            "https://drive.google.com/uc?export=view&id=1LV3--Cx04GdfMLbI3uKFvsgjnQOEyE1I",
            "https://drive.google.com/uc?export=view&id=1VYnC0TIWhKfqI_dlqfcs_o2U05Mg2Ceh",
            "https://drive.google.com/uc?export=view&id=1IL7aXgCeFnPodip01b-6Pgkn8FbuVqUI",
            "https://drive.google.com/uc?export=view&id=1pDQnGwnZ5kOEg-eJO5qsmXTTXN-gJboh",
            "https://drive.google.com/uc?export=view&id=1p6T2IM4_ExOYznt7p3Lys396x0RxX_kW",
            "https://drive.google.com/uc?export=view&id=1qSyu-jCfFI-o1TAqeKEwUPnuUyXdT2HH",
            "https://drive.google.com/uc?export=view&id=1VV-UMjrLh6Mf8ZddtIN5etmWHa6pQ9Qf",
            "https://drive.google.com/uc?export=view&id=1aWgWknqVMOG_J1TDtTA33GLhkZHmcP8R",
            "https://drive.google.com/uc?export=view&id=1eMZWzh3GHByVVHko57VGSCoe5uikZ5ED",
            "https://drive.google.com/uc?export=view&id=1MzKseHR-QS0tWvOVNmLX26FLRVe7Esu2",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "Napi paling kece se-Nusakambangan.",
                "pesan": "Jangan kabur jauh-jauh, bang."# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "Tutur katanya adem banget.",
                "pesan": "Ajari kita sopan santun, kak."# 1
            },
                {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Juragan pancing dari Teluk.",
                "pesan": "Bagi kailnya satu, kak."# 1
            },
                {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Si paling sibuk cari kesibukan.",
                "pesan": "Santai dikit boleh kali, kak."# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Fanboy AGZ garis keras.",
                "pesan": "Jangan lupa nonton, bang!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Jagoan nguleg cabai bekasi.",
                "pesan": "Sambelnya mantep, kak!"# 1
            },
                {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Teman pedel paling setia.",
                "pesan": "Semangat nemenin ridho, bang!"# 1
            },
                {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Istirahat adalah koentji.",
                "pesan": "Jangan kebanyakan istirahat, bang."# 1
            },
                {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Seniman sabun dari Belwis.",
                "pesan": "Ukiran sabunnya keren, kak!"# 1
            },
                {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Pecinta wave to earth.",
                "pesan": "Lagunya asik-asik, kak."# 1
            },
                {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "Raja pedel dari GH.",
                "pesan": "Ajak kita main, bang!"# 1
            },
                {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Pengamat warna baju handal.",
                "pesan": "Baju aku warna apa, bang?"# 1
            },
                {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "Si manis pemakan gula merah.",
                "pesan": "Bagi gula merahnya, kak."# 1
            },
                {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "Suka nyapa angin, ramah.",
                "pesan": "Anginnya sapa balik ga, kak?"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sI19IKU-rqTLh6zx8HhUPB0DBpIFRePr",
            "https://drive.google.com/uc?export=view&id=11bi2dbfC31wYoaQY4y1OGrtjHl0NuNNt",
            "https://drive.google.com/uc?export=view&id=1n2Brbge63t-kgfyQpDVLACZM83Et4Ogh",
            "https://drive.google.com/uc?export=view&id=1hIktfWN7u1z1rWaxOHBU-axdPgFzE2i9",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kobam",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Tidur adalah prioritas.",
                "pesan": "Mimpinya indah ya, bang."# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "Playlist-nya selalu oke.",
                "pesan": "Bagi playlist-nya dong, kak."# 1
            },
                {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Melamun tapi tetap keren.",
                "pesan": "Jangan lama-lama ngelamunnya, kak."# 1
            },
                {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Master Roblox Indomaret Belwis.",
                "pesan": "Mabar roblox kapan, kak?"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1D0NTsse0U7qTFSEXBpssQjii2FI3xgZ8", #1
            "https://drive.google.com/uc?export=view&id=1cx24Bo1mvnSPS8YS1SCu1kFIlO_Hkepi", #2
            "https://drive.google.com/uc?export=view&id=1S4oOT3rFraGReo9UZ21PBtBE5T91aF7d", #3
            "https://drive.google.com/uc?export=view&id=15yA6VqfEXA_dpobtETXsdcWvL8hMyTkf", #4
            "https://drive.google.com/uc?export=view&id=1_yWmebiu7FAmrFvwRsBLRRCjaejmjNPh", #5
            "https://drive.google.com/uc?export=view&id=1kBnCMjAF_sOPq8-_3-u78ZWBpavlI6td", #6
            "https://drive.google.com/uc?export=view&id=1YzwTnsBKVkpuyZHW_Z5x9rQjkA9aVXPZ", #7
            "https://drive.google.com/uc?export=view&id=1u1Ns4bU3rjub_wjrocF7R3gaXcLqVnd-", #8
            "https://drive.google.com/uc?export=view&id=19a4THVFJD-VO4Bj0vqpWOdnFEFojkmF2", #9
            "https://drive.google.com/uc?export=view&id=1B4Cju3iOJo0UlGgiK0j1f5FqeDpUunVc", #10
            "https://drive.google.com/uc?export=view&id=1j_YXEhCnjLbyKlLzQP0uGjULOvgX0MoW", #11
            "https://drive.google.com/uc?export=view&id=1oYEusnV101ccDcQPLoOoKT1rsCBFzl3G", #12
            "https://drive.google.com/uc?export=view&id=1njqrQ71JJjdPZFAP1CLOtPfAkXiJRWi1", #13
            "https://drive.google.com/uc?export=view&id=1dbwZSu6LcSzOEcWVCtb6mtIwy3AIC2ry", #14
            "https://drive.google.com/uc?export=view&id=1PgqJ6Xu8WtPJsCnzQ6jqAOrcjAjziiC2", #15
            "https://drive.google.com/uc?export=view&id=1Wr7qLish-iokII7WtURBaWRyy0LgCZ2i", #16
            "https://drive.google.com/uc?export=view&id=1NZUPEePH2GzzikmUUVIZcFuYsoxLePLF", #17
            "https://drive.google.com/uc?export=view&id=1YcmFg-1dI6MaZT6cI4mH52pPnS0Sn1cG", #18
            "https://drive.google.com/uc?export=view&id=1hBPf8e9_28XBYUGzFh90SXv_0qBhMF8U", #19
            "https://drive.google.com/uc?export=view&id=1bW3dW2DraOxBHuhRQg4WPwokOvjJUOaw", #20
            "https://drive.google.com/uc?export=view&id=1VlSwjFMQhunEdUFcv4c8uMVR_W4TexZO", #21
            "https://drive.google.com/uc?export=view&id=14jY6GeVpA9w0Tk-sZ5mLl3YcvntrvQc-", #22
            "https://drive.google.com/uc?export=view&id=1F6TPZA17FV3jA2WXoEwsCDXMwtsezsYd", #23
            "https://drive.google.com/uc?export=view&id=1jgEDKMXqJkPMNu8qkk70A0hf0bGfNcUW", #24
            "https://drive.google.com/uc?export=view&id=1_XxF5WsUzI4lIs-K4nZ9LZCvv2xn_p8T", #25
            "https://drive.google.com/uc?export=view&id=1Bi_r-C_Vqe4JXJkuHAasomEQgIy-16ab", #26
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": "PSDA paling misterius.",
                "pesan": "Semangat terus, bang!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "Kakak PSDA yang kalem.",
                "pesan": "Sehat selalu, kak!"# 2
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "Healing terus, tapi kerja beres.",
                "pesan": "Ajak kita healing, kak."# 3
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Anak bola dari GH.",
                "pesan": "Gocekannya mantap, bang."# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Siap ribut, tapi asik.",
                "pesan": "Jangan galak-galak, kak."# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Jailnya bikin nangis, tapi seru.",
                "pesan": "Maafin kita ya, bang."# 6
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Hobinya banyak, multitalenta.",
                "pesan": "Keren banget, bang!"# 7
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "Anak rajin dari gerbang barat.",
                "pesan": "Bagi semangat belajarnya, kak."# 8
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "Akamsi paling jago kader.",
                "pesan": "Kaderin kita dong, bang."# 9
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "Marah-marah tanda sayang.",
                "pesan": "Sabar ya, bang Gumel."# 10
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Marahnya lucu, kak.",
                "pesan": "Jangan marah-marah terus, kak."# 11
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "Smash volinya kenceng, bang.",
                "pesan": "Ajari kita voli, bang."# 12
            },
            
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Jago kuliner kalau ada uang.",
                "pesan": "Traktir kita kapan, bang?"# 13
            },
            
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Teman mabar Roblox-nya kak Lia.",
                "pesan": "Mabar bertiga yuk, kak."# 14
            },
            
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Scroll TikTok jalan terus.",
                "pesan": "Bagi FYP-nya, kak."# 15
            },
            
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Tidur adalah jalan ninjanya.",
                "pesan": "Mimpi indah ya, bang."# 16
            },
            
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Gamers sejati dari Airan.",
                "pesan": "Rank apa sekarang, bang?"# 17
            },
            
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Si pembuat onar 23.",
                "pesan": "Jangan cari masalah terus, bang."# 18
            },
            
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "Jagoan nangkap lele Belwis.",
                "pesan": "Bagi lelenya, bang."# 19
            },
            
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "Musik adalah hidupnya.",
                "pesan": "Selera musiknya keren, kak."# 20
            },
            
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "Futsalnya jago, bang.",
                "pesan": "Kapan-kapan main bareng, bang."# 21
            },
            
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "Multitalenta, jago berantem juga.",
                "pesan": "Jangan berantem terus, bang."# 22
            },
            
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "Anak basket dari Panjang.",
                "pesan": "Dunk-nya keren, bang!"# 23
            },
            
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "Dance-nya asik banget, kak.",
                "pesan": "Ajari kita nge-dance, kak."# 24
            },
            
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Jangan merajuk terus, kak.",
                "pesan": "Senyum dong, kak!"# 25
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Smash badminton-nya mantap.",
                "pesan": "Mabar badminton yuk, bang."# 26
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1h8sSg76KYnJE4B0pOtfGAZLdGClT4NBm", #1
            "https://drive.google.com/uc?export=view&id=1gyxIZK9IL5JyQwp3WnBJaewxyGkCFa8D", #2
            "https://drive.google.com/uc?export=view&id=1vLF1tETWgrunOZkKgTfb2rIDIn193zvh", #3
            "https://drive.google.com/uc?export=view&id=1lpXwk9ivPl3rIa7r26IwXM7o_a6mjoPE", #4
            "https://drive.google.com/uc?export=view&id=1f-qI4L_jdNNDRPjv_eUGmt_YmsBBF7hg", #5
            "https://drive.google.com/uc?export=view&id=1QDDzKvgtr8NnubbrZ-znUEfP1cv1Ooyp", #6
            "https://drive.google.com/uc?export=view&id=1gSYkrxPmG-xs0HAlK-TUoWuOizMnwTVQ", #7
            "https://drive.google.com/uc?export=view&id=18nq16zUMmQATFCilhjcMrcSAK3nt7j1v", #8
            "https://drive.google.com/uc?export=view&id=1ik2yqMvpnbbDIJRh2MybsbEcngJr52ra", #9
            "https://drive.google.com/uc?export=view&id=1ik2yqMvpnbbDIJRh2MybsbEcngJr52ra", #10
            "https://drive.google.com/uc?export=view&id=1l-hmrK1ELpPOBJUSTB8LWndHv3vJJruj", #11
            "https://drive.google.com/uc?export=view&id=1x6MtZQL354ffAsxan7AbWApDBdtXviB_", #12
            "https://drive.google.com/uc?export=view&id=1aIYmw6yFan4sxXNHe3WlUng5HCjsWoIu", #13
            "https://drive.google.com/uc?export=view&id=1M25TStGPAp4HVGkwpgJBGBTpieoM1BTu", #14
            "https://drive.google.com/uc?export=view&id=1a5SaY-tMqishLvbrCyh2QDz1yrkZz3yn", #15
            "https://drive.google.com/uc?export=view&id=1o8nI-h66VmkTlFTMGKLoJUC7R4YhD5UN", #16
            "https://drive.google.com/uc?export=view&id=19ZqAr4v4bRJ_PMljSgwWj0YeR0gvw9-l", #17
            "https://drive.google.com/uc?export=view&id=15Zh5X9Hi0aI68Zi95UwP6QnfHedaR9hD", #18
            "https://drive.google.com/uc?export=view&id=14b6YL1hihi05GM8dv0fvimZ7bMGvuAFP", #19
            "https://drive.google.com/uc?export=view&id=1nVQ5YkL9yfE8OBZLFUUdR-YOmbixaYVR", #20
            "https://drive.google.com/uc?export=view&id=1_t6bsJVF1yOL_7ByVfHcC0DUjTWAJgCs", #21
            "https://drive.google.com/uc?export=view&id=1evKwlESkMjSaeSUODpI8YsHJp95EuAJX", #22
        ] 
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Tidur dan berkembang biak.",
                "pesan": "Berkembangnya jangan cepat-cepat, bang."# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Si kutu buku Mikfes.",
                "pesan": "Buku barunya apa, kak?"# 2
            },
            {
                "nama": "Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Musik adalah teman setia.",
                "pesan": "Selera musiknya asik, bang."# 3
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak Mikfes yang misterius.",
                "pesan": "Sukses selalu, kak!"# 4
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Duta Fore Segar Miden.",
                "pesan": "Bagi kopinya, bang."# 5
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Ngerokok dulu, kerja kemudian.",
                "pesan": "Jangan banyak-banyak, bang."# 6
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "Pendengar musik sejati.",
                "pesan": "Spill lagunya, bang."# 7
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Si paling hobi nonton film.",
                "pesan": "Rekomendasi film dong, kak."# 8
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Musiknya keren banget, kak.",
                "pesan": "Mainin lagu buat kita, kak."# 9
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Musik hidupnya, Pramuka rumahnya.",
                "pesan": "Lagunya asik-asik, kak."# 10
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Multitalenta, jago nge-dance.",
                "pesan": "Keren banget, kak!"# 11
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Rajin membaca, panutan.",
                "pesan": "Bagi tips rajin baca, kak."# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Suaranya merdu, pianonya indah.",
                "pesan": "Nyanyiin kita lagu, kak."# 13
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Tidur adalah hobi utamanya.",
                "pesan": "Jangan tidur terus, kak."# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Ratu tidur asrama TB 4.",
                "pesan": "Semangat ya, kak!"# 15
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Hobinya bernafas, luar biasa.",
                "pesan": "Jangan lupa bernafas, bang."# 16
            },
            { 
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Jahil dan random abis.",
                "pesan": "GPT-nya salam balik, kak."# 17
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "PJ paling sabar se-ITERA.",
                "pesan": "Semangat PJ-nya, bang!"# 18
            },
            
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Jagoan catur dari Lapas.",
                "pesan": "Skak mat, kak!"# 19
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Tukang repotin kak Tanty.",
                "pesan": "Kasihan kak Tanty-nya."# 20
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Anak futsal Belwis.",
                "pesan": "Gol-in terus, bang!"# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Pemain catur handal Pemda.",
                "pesan": "Ajarin kita catur, bang."# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GXR82jXiq8dTPKayJ7bJkrLKWgnxsmh4", #1
            "https://drive.google.com/uc?export=view&id=1xrTipLVt8FhuRSksEBsiuJ50cDaSq7S9", #2
            "https://drive.google.com/uc?export=view&id=1JCo47aC1u3k7fi5JjnMEq10vqNziAkYa", #3
            "https://drive.google.com/uc?export=view&id=1aBnvNKRJHHZvtewLEqTH3_9Q0Lsc7k3l", #4
            "https://drive.google.com/uc?export=view&id=1N9cOgP1MfzsRayw4pCJEas9uNxXDbqPt", #5
            "https://drive.google.com/uc?export=view&id=1W2wCcE7CA5T5XhsZh2_bPz4svDkmidt7", #6
            "https://drive.google.com/uc?export=view&id=1oMgDGqBwmq0-MgwvkHtgpETf3vP9Hrvv", #7
            "https://drive.google.com/uc?export=view&id=1R6Bx8XKy9_aDyI6gVnYlAYXeQUB_6ZSr", #8
            "https://drive.google.com/uc?export=view&id=1Fjc-fk7O9CCgGipA55T8pJgRTZVEKCKs", #9
            "https://drive.google.com/uc?export=view&id=1c-73XzGXiwxJd5C-R6q93qE_eT66naR4", #10
            "https://drive.google.com/uc?export=view&id=1I_A_8-Rh8LxeU-BfuxGMeplPkv-TVgta", #11
            "https://drive.google.com/uc?export=view&id=1nQxKpqrdblDhzuQqjFhnIa7rFFXfxRfR", #12
            "https://drive.google.com/uc?export=view&id=1rJuFdlTxzu5aKKWHALAXWTh1lOFyXszp", #13
            "https://drive.google.com/uc?export=view&id=1pLsCwLs8UyShO1UPEPFzpLxh6CtSbtY1", #14
            "https://drive.google.com/uc?export=view&id=1JHDhvbMx884zkoqwdy-jZQVWyHsD3x8j", #15
            "https://drive.google.com/uc?export=view&id=1LUIpURjKInLF4JmtKnVLXBGkAVBbnUrc", #16
            "https://drive.google.com/uc?export=view&id=1XyqeC25u13Y1a4DZs3pLlSdDKZTixJ_K", #17
            "https://drive.google.com/uc?export=view&id=1K63jdHMKkn81FTiLE9l7ZiANhcEkxXyr", #18
            "https://drive.google.com/uc?export=view&id=1Q_RcZH970_vfa2-tdM5DRpTpVj_xNnUQ", #19
            "https://drive.google.com/uc?export=view&id=1s-b8-zBLfYcz63Asrx0itwS6SRXhC3Pu", #20
            "https://drive.google.com/uc?export=view&id=1ObztpmcleDlLAid1H4uXbnsTf2JrLkfL", #21
            "https://drive.google.com/uc?export=view&id=1NF2ByUPpRhHk5VF93_c01YslgLlktjY3", #22
            "https://drive.google.com/uc?export=view&id=1cSQKIxFAC7z4NBENvIQ1vzBIxqP2GpuD", #23
            "https://drive.google.com/uc?export=view&id=17NQRIZHjW1EST6iIvJnGCAGdapY9G-f8", #24
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulan",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Orang Spanyol nyasar ke asrama.",
                "pesan": "Hola, bang! Semangat BSI-nya."# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Asal usulnya jelas, kok.",
                "pesan": "Jalan hidupnya lurus, kak."# 2
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Tidur adalah koentji sukses.",
                "pesan": "Jangan lupa bangun, kak."# 3
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "Ratu JJ dan ngasprak.",
                "pesan": "Template JJ-nya keren, kak."# 4
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Pencubit ketang paling gemas.",
                "pesan": "Ketangnya sakit ga, kak?"# 5
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Pelanggan setia risol naya.",
                "pesan": "Bagi risolnya, kak."# 6
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Musisi Nias dari TB 3.",
                "pesan": "Musiknya mantap, bang."# 7
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Fans berat reels AGZ.",
                "pesan": "AGZ-nya ditonton terus, kak."# 8
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Badminton dan musik = hidup.",
                "pesan": "Mabar badminton kapan, bang?"# 9
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "Si paling sering minta tolong.",
                "pesan": "Adit-nya sabar ya, kak."# 10
            },
            {
                "nama": "khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Hobi nonton, matanya sehat.",
                "pesan": "Bagi rekomendasi tontonan, kak."# 11
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Jago baking dari Gang Nalim.",
                "pesan": "Bagi kuenya dong, kak."# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bensinnya habis terus, bang.",
                "pesan": "Jangan boros bensin, bang."# 13
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Si paling update film.",
                "pesan": "Nonton bareng yuk, kak."# 14
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Me time adalah segalanya.",
                "pesan": "Jangan lupa kita, kak."# 15
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Penjelajah map sejati Belwis.",
                "pesan": "Udah sampai mana, bang?"# 16
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Penjelajah desa Lamsel.",
                "pesan": "Hati-hati di jalan, kak."# 17
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Jago nyetrika, rapi terus.",
                "pesan": "Setrikain baju kita, kak."# 18
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Main-main tapi kerjaan beres.",
                "pesan": "Ajak kita main, kak."# 19
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Ngelamun tapi tetap keren.",
                "pesan": "Mikirin apa, bang?"# 20
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Keliling dunia versi Teluk.",
                "pesan": "Oleh-olehnya jangan lupa, kak."# 21
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Rajin baca, panutan.",
                "pesan": "Buku apa yang dibaca, bang?"# 22
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Pencari dataset dari Swiss.",
                "pesan": "Dataset-nya ketemu ga, kak?"# 23
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Jalan-jalan terus, asik.",
                "pesan": "Ajak kita jalan-jalan, kak."# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xA1DMrXMoIIjV0HczaT90PTL16zRNOl7", #1
            "https://drive.google.com/uc?export=view&id=17dddvI3xPAd8NXG6ykfbRn60-zuHbmV2", #2
            "https://drive.google.com/uc?export=view&id=1Su7Ip1y5istQY5CxxYQSakxJ3_niANTl", #3
            "https://drive.google.com/uc?export=view&id=1b2qmvDQehY6tC5ro3mLXUx5-COVDUxsG", #4
            "https://drive.google.com/uc?export=view&id=16A99-avAX8lotrrh6XjsOZLmDP0RkoGM", #5
            "https://drive.google.com/uc?export=view&id=1ZIr-ns0hbYxpXC7noJlsN44QJ2ewW5f3", #6
            "https://drive.google.com/uc?export=view&id=1LbHU6zB_iw7bPVI3IMyRism0xONWNQJM", #7
            "https://drive.google.com/uc?export=view&id=13DhBwONB40QqRjsPy2gijhZasUfnRScs", #8
            "https://drive.google.com/uc?export=view&id=1_U-zd2iy8xoH9l3_34QL7MDGA3SOB8zy", #9
            "https://drive.google.com/uc?export=view&id=1IL3Tn49YNH7oWu_liDcOa1LZPIJ1p94J", #10
            "https://drive.google.com/uc?export=view&id=1PynEKmKiz6bRwpSK-29aq1I9K1QhHtZA", #11
            "https://drive.google.com/uc?export=view&id=1e7rbR6wHeMXP6fYtT1pSWcvdo71-QEYh", #12
            "https://drive.google.com/uc?export=view&id=1Z-Gsosi9PCV-YYMlRXxEkgrpALQbOnuW", #13
            "https://drive.google.com/uc?export=view&id=1i2gH6IQx7xR0tWT1djVtKXBARDOHoLL4", #14
            "https://drive.google.com/uc?export=view&id=1LY123azxldzhmA0-8RJV6J_RdxZ0CT3M", #15
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": "Anak kajian paling rajin.",
                "pesan": "Bagi ilmunya, kak."# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Jagoan mancing dari Sukarame.",
                "pesan": "Dapat ikan apa, kak?"# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Chef handal dari Airan.",
                "pesan": "Masakin kita dong, kak."# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Zumbanya asik banget, kak.",
                "pesan": "Ajak kita zumba, kak."# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "Penghitung kerikil profesional.",
                "pesan": "Kerikilnya ada berapa, bang?"# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Jago baking, kuenya enak.",
                "pesan": "Bagi resepnya, kak."# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Yoganya bikin badan lentur.",
                "pesan": "Ajari kita yoga, kak."# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Wibu sejati dari Sabah Balau.",
                "pesan": "Rekomendasi anime dong, bang."# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "Olahraganya rajin, badan sehat.",
                "pesan": "Olahraga bareng yuk, bang."# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Seniman lukis dari Belwis.",
                "pesan": "Lukisannya keren, bang!"# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Pawang cicak gerbang barat.",
                "pesan": "Cicaknya jangan dimarahin, kak."# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Musiknya asik, keren.",
                "pesan": "Main musik bareng, kak."# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Anak futsal Way Kandis.",
                "pesan": "Futsalnya jago, bang."# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Musiknya bikin adem, kak.",
                "pesan": "Mainin lagu buat kita, kak."# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Master rubik mirror Pemda.",
                "pesan": "Ajari kita main rubik, kak."# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PoS8k0JsZvbri9l0Yt2T4OiQKjVdODLx",
            "https://drive.google.com/uc?export=view&id=1s731J1qE689sO3iTAIxc3xm3ArXt4FRU",
            "https://drive.google.com/uc?export=view&id=1QBofuizBMIDilRZhxwa8XOT2AC8X5HM5",
            "https://drive.google.com/uc?export=view&id=1Yg4nAsK5RTBwPy9yjS5vgyEoIyjjjsbE",
            "https://drive.google.com/uc?export=view&id=1dTaaGPPTxqbQqck2x5nSTNEoX5e1NqiQ",
            "https://drive.google.com/uc?export=view&id=1xZjkql4YHDxqV-6kOuReK-py3qcFAxtm",
            "https://drive.google.com/uc?export=view&id=1jGP6MMdzQ9_vu7c7fiQalsLJsU9qWwcT",
            "https://drive.google.com/uc?export=view&id=1CVi8BgqfKEqtt_eM__uwdXij947ggZdV",
            "https://drive.google.com/uc?export=view&id=1P1wJzwhrZtMcGN3IOyA9B9CtMO8bBAzA",
            "https://drive.google.com/uc?export=view&id=13ObdS5lUXShQ-TIvugdA88JNXtI7m0Ny",
            "https://drive.google.com/uc?export=view&id=1-cpqNbRABqdmSEKr4fozQqQ9ya7-M8u9",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": "Jogging terus, sehat banget.",
                "pesan": "Ajak kita jogging, bang."# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Pecinta novel dari Sukarame.",
                "pesan": "Novel barunya seru, kak?"# 2
            },
                {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "Anak cafe tengah malam.",
                "pesan": "Jangan begadang terus, bang."# 3
            },
                {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Joggingnya sampai Lamsel.",
                "pesan": "Semangat joggingnya, kak!"# 4
                },
                {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "Penonton setia Facebook.",
                "pesan": "Nonton apa di FB, kak?"# 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Anak jogging Way Halim.",
                "pesan": "Kapan jogging bareng, kak?"# 6
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Belajar terus, pusing ga?",
                "pesan": "Semangat belajarnya, bang!"# 7
            },
                {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Pecinta drakor sejati.",
                "pesan": "Drakor baru apa, kak?"# 8
            },
                {
                "nama": "Engli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "Jagoan Mobile Legend.",
                "pesan": "Mabar ML yuk, bang."# 9
            },
                {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Chef handal dari Korpri.",
                "pesan": "Masakannya enak, kak!"# 10
            },
                {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Main terus, kapan belajarnya?",
                "pesan": "Ajak kita main, kak."# 11
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1y2qMqAsmhJXsEjzYuk9w49Y0Sz4c4BF2",
            "https://drive.google.com/uc?export=view&id=1HW73JV00NPjN1jMgjv_trjPUxT1E_VAb",
            "https://drive.google.com/uc?export=view&id=1ACS-XvDt3XonfFeF7OH2n5iHcQFmSb1h",
            "https://drive.google.com/uc?export=view&id=1ZngTckxRwkWcUycToZcnzBiaNj7OeM9Z",
            "https://drive.google.com/uc?export=view&id=167sSYVQjQAAegFdvdBRtpWyXaN2EwisE",
            "https://drive.google.com/uc?export=view&id=1qCrvnUNPtFIgGc9q43OzyryHNkccGS8b",
            "https://drive.google.com/uc?export=view&id=1WEhLKDq5uOEJYXV6CuzZRcA61bbJeWVo",
            "https://drive.google.com/uc?export=view&id=1Gis3pvtPkdN4weHiRjs29he8F4M0XxYl",
            "https://drive.google.com/uc?export=view&id=16WgmAzCcrxfLONhnW64NLOIdOT8V2XYN",
            "https://drive.google.com/uc?export=view&id=19bKBw01Po6i6Mh2qBeuusbK7av-gsrLn",
            "https://drive.google.com/uc?export=view&id=1pgfT9qwwxUvgdDmaZx9BVVKXhAHa1Sf7",
            "https://drive.google.com/uc?export=view&id=10-V-21q-aRQ5W7odvtT9vonbLCaHHpvI",
            "https://drive.google.com/uc?export=view&id=1nR6aU5DRhRwi8L7OZeVIQvBhaOBULRPr",
            "https://drive.google.com/uc?export=view&id=1IqRlXMABmg5OV31NyY0kBJcFuE8BANLM",
            "https://drive.google.com/uc?export=view&id=1XMTxHe2mRXEaLVWLVdN6hL3YRHPIiF7R",
            "https://drive.google.com/uc?export=view&id=1z7dIV5sXhCszKMIzLdGvbvLTjcj4z05U",
            "https://drive.google.com/uc?export=view&id=1gwDVqklqPsnOCqAtN4baP22Gqd2cqnQU",
            "https://drive.google.com/uc?export=view&id=11H8ZHFs3qzfen0sr1uCT_FNmL-QtcO9a",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "Musik adalah separuh jiwanya.",
                "pesan": "Playlist-nya keren, kak."# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "Nge-gym terus, badannya bagus.",
                "pesan": "Bagi tips nge-gym, kak."# 1
            },
                {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Anak volly dan billyard.",
                "pesan": "Smash-nya kenceng, bang."# 1
                },
                {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Motoran terus, bensin aman?",
                "pesan": "Hati-hati di jalan, bang."# 1
            },
                {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Olahraga terus, sehat selalu.",
                "pesan": "Semangat olahraganya, bang!"# 1
            },
                {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "Vlogger hits Kedaton.",
                "pesan": "Vlog-nya keren, kak!"# 1
            },
                {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@",
                "kesan": "Belajar terus, panutan.",
                "pesan": "Semangat belajarnya, kak!"# 1
            },
                {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Gitarannya bikin adem, kak.",
                "pesan": "Mainin lagu buat kita, kak."# 1
            },
                {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Musik adalah teman terbaiknya.",
                "pesan": "Lagunya asik-asik, kak."# 1
                },
                {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Inspirasi Pinterest-nya keren.",
                "pesan": "Bagi pin-nya dong, kak."# 1
            },
                {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Chef handal Labuhan Ratu.",
                "pesan": "Masakannya mantap, kak!"# 1
            },
                {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "Pecinta musik dari Kota Agung.",
                "pesan": "Selera musiknya oke, kak."# 1
            },
                {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Master Roblox dari Airan.",
                "pesan": "Mabar Roblox kapan, kak?"# 1
            },
                {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Rajin baca, kutu buku.",
                "pesan": "Bagi rekomendasi buku, bang."# 1
            },
                {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Multitalenta, jago masak nulis.",
                "pesan": "Keren banget, kak!"# 1
            },
                {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Pinterest adalah dunianya.",
                "pesan": "Bagi inspirasinya, kak."# 1
            },
                {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "Seniman lukis dari Krui.",
                "pesan": "Lukisannya indah, kak."# 1
            },
                {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "Suaranya merdu banget, kak.",
                "pesan": "Nyanyiin kita lagu, kak."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

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
            "https://drive.google.com/uc?export=view&id=1tTaP010gY2zVNguTppPA9fAbLSOE6yMs",
            "https://drive.google.com/uc?export=view&id=1ovw65YEG_3QG-aeI__CpYj05HZ34FFdl",
            "https://drive.google.com/uc?export=view&id=1aVeecorc2aNvAmS_eJHF-xliDxgaa6r0",
            "https://drive.google.com/uc?export=view&id=1cel5vZ4ohX3lk-QmF1CpPay0nqp_wxr0",
            "https://drive.google.com/uc?export=view&id=1VzhIucgqChbL1d3GO5Uf9QEQtN9vVDSe",
            "https://drive.google.com/uc?export=view&id=1DR4CrCpxqnQ7b8IFpVOxyDwYqxWK38a7",
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
                "kesan": "kelaitan berwibawa banget, tapi ternyata ada sisi asik nya juga",  
                "pesan":"Terus menorehkan hal yang baru buat himpunan"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "asik, seru, suka sharing juga tentang sains data",  
                "pesan":"Terus jadi orang yang baik, dan jangan berhenti berbagi"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "23",
                "asal":"Baduy Dalem",
                "alamat": "Agrest Kost",
                "hobbi": "Nahan Pipis",
                "sosmed": "@celisabethh_",
                "kesan": "Suka becanda ngawur",  
                "pesan":"Semoga amanah yang diemban terjalasanakan dengan baik"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Sekilas aga pendiem, tapi keliatan pinter deh",  
                "pesan":"Semoga selalu aman-aman aja dalam mengemban tugasnya"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Bulaleng, Bali",
                "alamat": "Asrama TB 4",
                "hobbi": "Nahan Eeq",
                "sosmed": "@eksantyfebriana",
                "kesan": "iseng, suka becanda, tapi tetep keliatan kalo orang penting",  
                "pesan":"Terus jadi orang yang humble dan baik"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang",
                "alamat": "Korpri",
                "hobbi": "Cute kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "lucu suka becanda, tapi keliatan santai juga",  
                "pesan":"Semoga selalu baik-baik aja"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FV5De7hi-EzpmcWa98ZM_lnpJ6qfM49Z",
            "https://drive.google.com/uc?export=view&id=1sWvyh4YOwCskGm1tSyuQKboxqezwZYoo",
            "https://drive.google.com/uc?export=view&id=1nNLuDZ3ZyQ2MT2_slcvOsRzfc6pvW1Zb",
            "https://drive.google.com/uc?export=view&id=1R6iGRFEcX1r8djJLsBXJztUBZtOaWxXQ",
            "https://drive.google.com/uc?export=view&id=1jmBcxPitHrRNSFy0B_3OseyGWBv9v4TG",
            "https://drive.google.com/uc?export=view&id=13lVtvK44S_Pps1iPjRgyHcAUBv9CoYW5",
            "https://drive.google.com/uc?export=view&id=12v6l7uZFPsirfxZ3GibBrdFllRUmfMJ-",
            "https://drive.google.com/uc?export=view&id=1kdPpTRhXLFme2cUgZhfYqbg_TwCMmUKj",
            "https://drive.google.com/uc?export=view&id=1tAs-cp2vWYSQn4vOX28gb49mqvrdD1LG",
            "https://drive.google.com/uc?export=view&id=1rWOgN8x5vPOS-Nk7Hli0HPooDBrnZF7z",
            "https://drive.google.com/uc?export=view&id=1r1t01FaOphG9lFymGiNcieSsDR2sSCL7",
            "https://drive.google.com/uc?export=view&id=1UoC7ntKWy2fDXDEJ3-z1wdOAOMrMc2zf",
            "https://drive.google.com/uc?export=view&id=1SCQaoZ89Wfp4_z0Honb5wxu8cXqJuHKF",
            "https://drive.google.com/uc?export=view&id=1BZq9MMjznSs7SiGAtfIMVEd5rclaNxVh",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Nusa kambangan",
                "alamat": "Lapas belwis",
                "hobbi": "Melarikan diri",
                "sosmed": "@Jeremia_s_",
                "kesan": "serius, keren tapi seru juga sering becanda",
                "pesan":"Semangat jadi ketua baleg nya"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia",
                "kesan": "keliatan baik terus ramah juga",
                "pesan":"Semoga selalu berhasil dalam hal apapun"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan pancing",
                "sosmed": "@Renishapg",
                "kesan": "kakanya keliatan baik",
                "pesan":"semoga kedepannya terus baik"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "keliatan baik tapi serius gitu",
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way halim",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "pinter banget terusd sering random",
                "pesan":"tetep jadi bang dharu yang biasanya bang"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way huwi",
                "hobbi": "Nguleg cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "lucu kakanya, suka kadang salah gitu",
                "pesan":"semangat terus kak di baleg"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Rido main Padel",
                "sosmed": "@givarooo",
                "kesan": "baik, ramah sering nanya juga",
                "pesan":"jadi baik terus bang"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "cool gitu, santai",
                "pesan":"tips nya biar bisa keren bang"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "seru kakanya, ramah juga",
                "pesan":"tetep baik dan ramah terus kak"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "mendengarkan wave to earth",
                "sosmed": "@j_eesie",
                "kesan": "sering senyum kalo ketemu",
                "pesan":"lancar lancar terus kak kedepannya"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "main padel",
                "sosmed": "@iamridhomanik",
                "kesan": "keliatan serius tapi masih ada sisi lawak nya",
                "pesan":"ajarin padel bang"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal":"Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin Warna Baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "humble, dingin, misterius",
                "pesan":"pengen juga di liatin warna bajunya"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "keliatan pinter, serius tapi masi asik",
                "pesan":"semangat jalanin hari hari kuliahnya kak"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Rantauprapat",
                "alamat": "Belwis",
                "hobbi": "nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "lucu, kadang gajelas, suka becanda, akrab sama sapa aja",
                "pesan":"kapan kumpul geng pplk lagi kak?"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BPtdfVOoasujuAjHwC2jsDBMYHEbHD9k",
            "https://drive.google.com/uc?export=view&id=1400QqS9CC6RURE9q-DpcZUWxhtIHUSIh",
            "https://drive.google.com/uc?export=view&id=18J3Mx1SSCnuh2sUAhDR6wwGfdwvAcEDR",
            "https://drive.google.com/uc?export=view&id=16jCXwKvcgi3VC89e7ERLBvbaeaNFKtBR",
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
                "kesan": "suka becanda, tapi tetep bisa serius",  
                "pesan":"ajarin biar bisa kaya abang dong"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "seru, sering ngajak cerita",  
                "pesan":"tetep jadi baik selalu ya kak"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "live instagram",
                "sosmed": "@fathinahnazzh",
                "kesan": "baik, ramah, suka nyapaa",  
                "pesan":"tetep jadi orang baik yang saya kenal kak"
            },
            {
                "nama": "Lia Hana Ichisasmita ",
                "nim": "123450083",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "kakanya serius, tapi masi ramah",  
                "pesan":"semangat terus jadi senat nya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZxhcHzJ3sdGKSkGdXiOS7pJpRgpk6gBd",
            "https://drive.google.com/uc?export=view&id=11UDQ7fP9FcJtw_800vvvBWTJ1gJB2uz0",
            "https://drive.google.com/uc?export=view&id=1zakFE48w652COa8x2YW5gOA3cWVG3Jp3",
            "https://drive.google.com/uc?export=view&id=12QSfxhLcdz6T39j7O7C2PuBtQT5DsEcn",
            "https://drive.google.com/uc?export=view&id=1xBTd8X3aDO12my6y3wdK7S4vyo3cJvA7",
            "https://drive.google.com/uc?export=view&id=1LKVSCTU3CP62-05P2DsyONnjwZrHiZJP",
            "https://drive.google.com/uc?export=view&id=1uXEW6uXvy2W3aasJX9B_4E8GEDHm_i5K",
            "https://drive.google.com/uc?export=view&id=1hxd5Kys5dIgxoZ8b6h5fKvJVc9ze-vVH",
            "https://drive.google.com/uc?export=view&id=1ufrmJO0KlK3NJ8nlWySpGvX3vtgEcK-d",
            "https://drive.google.com/uc?export=view&id=1oxekXMbtQNR-Z6XE8aqm4ce6HbxF9rGq",
            "https://drive.google.com/uc?export=view&id=18McbM66tQ0WfpGra3T5qxpLMeL2eBMKG",
            "https://drive.google.com/uc?export=view&id=1rzCWhiCQxr1rud9DI3eunt78w1pN3_K3",
            "https://drive.google.com/uc?export=view&id=1a0ogOxlCk4TXXvJNkeoUPz8AUHSC-3Gs", 
            "https://drive.google.com/uc?export=view&id=15-Os_HkT-zvmH760paV2WjCw52c91MHg",
            "https://drive.google.com/uc?export=view&id=1OhykpYhddyezE0YPtfZ1xQ4j63Vy8Y2x",
            "https://drive.google.com/uc?export=view&id=1hjKjrZXFDZXaEMJi0yh3L3GGT044eTJV",
            "https://drive.google.com/uc?export=view&id=1ONcADEcJBQ091ksZAiUheglygOKW1sgz",
            "https://drive.google.com/uc?export=view&id=1cRG9qKp17OSV4ULho_FUtQpy09VNQFFG",
            "https://drive.google.com/uc?export=view&id=15JjDl2-edr9nlAJC_ZPAHJY_hGwyy_-w",
            "https://drive.google.com/uc?export=view&id=1oMkS58oWMVCUAWHDfzCB6SPck8xrQC-w",
            "https://drive.google.com/uc?export=view&id=1qp1bRuySWTiqwjU-Io-2dTKcWG6U_EKS",
            "https://drive.google.com/uc?export=view&id=1e880wqgL73tjaC_aR9kJtmcDgsOsXvuG",
            "https://drive.google.com/uc?export=view&id=1CQrkHP3ybEAYR41WOgxnj0uU1e9m4M9-",
            "https://drive.google.com/uc?export=view&id=1b_wh6jOyzhaUIitYp4BhV8HjP_Jz1Ofz",
            "https://drive.google.com/uc?export=view&id=1cfiV31amhpOCG6bQZ6OVg3xXZbKTJQ21",
            "https://drive.google.com/uc?export=view&id=1ji3JggHVcmUN3wXS3fmlDzT3Hiumxw6w",
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
                "kesan": "bisa becanda bisa tegas",
                "pesan": "tetep jadi abang yang santai bang"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "jawa barat",
                "alamat": "korpri",
                "hobbi": "mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "tegas, serius",
                "pesan": "semoga bisa lebih humble kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Solo",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapasha_",
                "kesan": "serius, tegas, masi bisa becanda dikit ",
                "pesan": "semangat hari hari kedepannya kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Membaca",
                "sosmed": "@ahmad.rizky__",
                "kesan": "humble, ramah, suka baca",
                "pesan": "makasi untuk ilmu ilmu yang dikasi bang"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Cari ribut",
                "sosmed": "@arientakhsnl_",
                "kesan": "gabisa becanda, serius banget, tegas",
                "pesan": "semoga bisa lebih baik kak"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "masi bisa becanda dan santai",
                "pesan": "semoga tetep bisa ngasi ilmu yang baik bang"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Hobinya banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "baik, ramah, tegas juga",
                "pesan": "tetep ramah terus ya bang"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "Membaca",
                "sosmed": "@natasyamavisca",
                "kesan": "serius banget, susah becanda, tegas",
                "pesan": "lebih humble lagi ya kak"
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Suka ngader",
                "sosmed": "@nobelnizam",
                "kesan": "pinter, serius, jarang senyum",
                "pesan": "makasi ilmunya bang, semoga bisa lebih baik lagi"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "bawaannya tegas, terus serius banget, tapi masi bisa santai",
                "pesan": "sukses terus buat kedepannya bang"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Airan",
                "hobbi": "Marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "ramah dan juga sering senyum",
                "pesan": "semangat terus kak jadi bagian dari psda"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@shahid22_",
                "kesan": "pembawaannya lucu, asik, bapak vibes juga",  
                "pesan":"tetep humble terus bang"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "santai, baik, ramah",  
                "pesan":"kalo mau kulineran ajak ajak bang"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "bisa becanda, ekstrovert juga, sering tanya",  
                "pesan":"ajarin biar bisa ada vibes diri sendiri dong kak"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Apa aja",
                "sosmed": "@rismaa.mustika_",
                "kesan": "keliatannya serius, tegas juga, tapi masi bisa ramah",  
                "pesan":"semoga kedepannya baik terus ya kak"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "lucu karna suka menghasut",  
                "pesan":"kalo main roblox ajak ajak kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "pembawaannya santai, asik juga, bisa ngobrol",  
                "pesan":"keren bang masi bisa humble"
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "keliatan pinter segalanya",  
                "pesan":"makasi bang bua tilmu ilmu nya"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Ngedance",
                "sosmed": "@d__aniar",
                "kesan": "sering becanda, asik juga pembawaannya",  
                "pesan":"semangat terus kak nge dance nya, di tunggu perform selanjutnya"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "pembawaannya santai, ngobrol asik",  
                "pesan":"semangat terus bang kuliahnya kalo nangkep lele ajak ajak"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "pembawaannya serius, tapi ramah",  
                "pesan":"ajak ajak bang kalo main basket"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Ngapain aja",
                "sosmed": "@dla_natzzyaa",
                "kesan": "keliatan tepat waktu banget kakanya",  
                "pesan":"semangat kak jalanin hari harinya"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "santai, asik",  
                "pesan":"jangan sering sering ngejek bang"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "sering becanda, seru juga",  
                "pesan":"tetep keren terus bang"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "pembawaannya tegas, harus sesuai, tapi masih bisa becanda",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "kakanya kelaitan aga pendiem, tapi bisa asik",  
                "pesan":"semangat terus kak kedepannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mp1HIXpmUowf4fc0_n8oEAa5qzp8MNmv",
            "https://drive.google.com/uc?export=view&id=1zRCd_iz-X5NVPxvrJCSzjJ0rV8tRkWc8",
            "https://drive.google.com/uc?export=view&id=17C-xOTdQ8mN9hq79DflluvAaMC5GpcGu",
            "https://drive.google.com/uc?export=view&id=1UxOA_fegj3MGpTvqpZBCom_f-SxSAW6c",
            "https://drive.google.com/uc?export=view&id=1YORxAPvpgOK-1KzJbjPEmQnTsnGgZy5t",
            "https://drive.google.com/uc?export=view&id=1DZOwWR4NFIf1JmyFRwbeSLXNpyg4Pt-r",
            "https://drive.google.com/uc?export=view&id=14TPKxrx4ChY3i_N4xq5u5qy6Y1-nkfGx",
            "https://drive.google.com/uc?export=view&id=15rmrWwiXquMvKqhMOZijSHidUZ5iYMcF",
            "https://drive.google.com/uc?export=view&id=15EHkIazQTK5lNAxoJEOGOXSuP5x8RksX",
            "https://drive.google.com/uc?export=view&id=1hl-mMQqytBk1gN2CBdH5cX-wTK37gFlO",
            "https://drive.google.com/uc?export=view&id=1MyRUvrfCEenvp-4ZP9Yu8S2UPEQiaJo_",
            "https://drive.google.com/uc?export=view&id=10bbyBdrO8UauIWINBs2JJJKSH6Vr_jZl",
            "https://drive.google.com/uc?export=view&id=1eMGsGq3ktRdX_AdJb3mYZ9ARw2ZBti1w",
            "https://drive.google.com/uc?export=view&id=1zLvX3dK4hIwsXcthN_ri_s52KCRMBOYC",
            "https://drive.google.com/uc?export=view&id=1zCHwU65iIfZbLB_xnpnvGsXUsbmZ6cMb",
            "https://drive.google.com/uc?export=view&id=1igF9p0pPxZPRb4moIbQ1M1DkA_HYjaLI",
            "https://drive.google.com/uc?export=view&id=1n10UT5d2IfJpjEmWnX_NDU2cSZDV90Ld",
            "https://drive.google.com/uc?export=view&id=1cLrxTocqMmxpebONE9LApUO6j-wix_DT",
            "https://drive.google.com/uc?export=view&id=1Jna_7MBWrsdmHaYonhtCHYDTLt3ONil7",
            "https://drive.google.com/uc?export=view&id=1LS5bMUMQk2Pesl6EJcVuoAqrJS7RBxJe",
            "https://drive.google.com/uc?export=view&id=1P4yPO4r17Qk6LEjuH6Xu-dqYyrXMRswv",
            "https://drive.google.com/uc?export=view&id=1xg3t3XQTkzUnF3-HkCQ42iZVJPm9NvlU",
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
                "kesan": "abangnya seru sering cerita",
                "pesan":"keren terus bang, tetep humble, makasi buat ilmu yagn disampein bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "kakanya ramah, murah senyum",
                "pesan":"semangat kak untuk hari hari selanjutnya"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "ramah, murah senyum, banyak kasi tips",
                "pesan":"makasi bang baut ilmu yang udah di ajarin, tetep humble terus bang"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "seru kakanya, bisa becanda",
                "pesan":"btw masker nya merk apa kak?"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "abangnya asik bisa becanda, keliatan pinter banget",
                "pesan":"tetep jadi keren terus bang, semangattt"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "tegas, masi becanda",
                "pesan":"lebih humble lagi bang kedepannya"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "keren pembawaannya, aga misterius",  
                "pesan":"stay humble bang"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "seru pembawaannya bisa becanda juga ngobrol",
                "pesan":"semangat terus kak untuk hari hari kuliahnya"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Keliatan ramah banget dan murah senyum",
                "pesan":"semoga selalu baik baik aja ya kak kedepannya"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "santai, bisa becanda, asik, bisa semua deh",
                "pesan":"ajarin biar jadi keren gitu bang"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakanya sering tanya tanya, murah senyum juga",
                "pesan":"tetep jadi orang baik terus kak"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "pembawaannya aga serius tapi masi ramah",
                "pesan":"stay humble ya kak"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "santai pembawaannya ramah juga",  
                "pesan":"tetep ramah dan juga baik terus ya kak"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakanya bisa becanda ternyata",  
                "pesan":"semangat terus kaak unutuk hari hari nya"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "kakanya ramah, tapi tetep ada sisi tegasnya, sering tanya juga",
                "pesan":"tetep jadi ramah ya kak"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "bawaannya santai, tapi keliatan kalo pinter banget",  
                "pesan":"ajarin biar bisa santai bang"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "kakanya baik banget",  
                "pesan":"tetep jadi baik terus kak, semoga lancar terus kedepannya"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "asik, becandaan terus, keliatan pinter banget",
                "pesan":"tetep sukses terus bang, tetep jadi abang yang baik, makasi buat ilmu ilmu yang udah di ajarin"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "pembawaannya santai, aga berntakan tapi pinter banget",
                "pesan":"ajarin biar bisa pinter bang"
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
                "kesan": "kakanya ramah, baik",
                "pesan":"sering sering sharing kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren, keliatan pinter",
                "pesan":"ajarin biar pinter bangg"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rvyVt6XGlFytbG1URQuXHTkcQebJ5Uyq",
            "https://drive.google.com/uc?export=view&id=1mdCc5ccDPWKmupVC2rY6C6lnY3z8nvC_",
            "https://drive.google.com/uc?export=view&id=1GXmXQrCaifW64cCko2m27SiYeDaKHZMv",
            "https://drive.google.com/uc?export=view&id=1puwBv4wkt5GnNlPazYhgBJQ6Qi31_tFU",
            "https://drive.google.com/uc?export=view&id=1TDzOpa5-0qmwJbdOOX0PGlQmJ3ZT2_FN",
            "https://drive.google.com/uc?export=view&id=1c6cDtxNveqlC7Zuq9TXfgQdn8i0LUdA9",
            "https://drive.google.com/uc?export=view&id=1rwnIyFNWkeneyhZVXdaG-FrR3NO_kJO6",
            "https://drive.google.com/uc?export=view&id=1pwEfVw-6usEJLWc9Nc6jyEztPXEr1N2H",
            "https://drive.google.com/uc?export=view&id=1-E2n1L8FsFlGSBwRsogUzuETVUbv3UnR",
            "https://drive.google.com/uc?export=view&id=1LjpzSqUuQn2WeAVYQxUlP0ZWGgZYOYns",
            "https://drive.google.com/uc?export=view&id=1LGi7e5p9isctEoA1q0YO4J_AdlZtd2d3",
            "https://drive.google.com/uc?export=view&id=15w396iF-OR-7FkzIT2CQl4oEyXOpnkod",
            "https://drive.google.com/uc?export=view&id=1lpk9tFW8cxpFZz-3s4kS80Mn2CAAoFvS",
            "https://drive.google.com/uc?export=view&id=1gPMPcmQsDE4rVvUHJLVAu6EMCNqRQJXr",
            "https://drive.google.com/uc?export=view&id=1YOdqxuzygh3e-tDH83so6EgPZSOc0i9j",
            "https://drive.google.com/uc?export=view&id=1vyZF-Q3is1X31xjDF8-c7_OpZx2zqgaw",
            "https://drive.google.com/uc?export=view&id=1-XJlvVnBe7pU3l7rSeKOGYqXFhV5xBnZ",
            "https://drive.google.com/uc?export=view&id=1qzSgRmIxpWQxc7ViYWN8glERX3YYiToO",
            "https://drive.google.com/uc?export=view&id=14BrlbMZgDtv7g7oz3XMpPes714bt8iGy",
            "https://drive.google.com/uc?export=view&id=1Ot_pnNO6APb9JRE2_tbzbamSbAGpj3B-",
            "https://drive.google.com/uc?export=view&id=1CxH6FgVE6ojo51HTxweNy0mjZNR6tboR",
            "https://drive.google.com/uc?export=view&id=1xfc91tloOV348GmU8P3wt2ynqUP3hrDm",
            "https://drive.google.com/uc?export=view&id=1Tv-AeHPWhJfe6sXNfOixbF8e5fWLuVAz",
            "https://drive.google.com/uc?export=view&id=1ZDxwOXDslv0oCGiJhNWVKmAVt21iKqUD",
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Sebelah Warjo",
                "hobbi": "Memancing",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "seru bang arafi, bisa becanda bikin ketawa juga",
                "pesan":"tetep keren terus bang, sering sering ngajak jalan jalan"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sukabumi, Jawa Barat",
                "alamat": "Depan GH",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kak yo keliatan aga diem, tapi kalo lagi tetep seru kalo lagi waktunya",
                "pesan":"tetep humble terus kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Mencari jurnal Scopus",
                "sosmed": "@jasminednva",
                "kesan": "seru kak mine, asik, sering becanda, terus banyak ide ide",
                "pesan":"semangat teruss kakk buat kedepannya"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "jalan jalan",
                "sosmed": "@elandraa_",
                "kesan": "kak arini baik, sering kasi ilmu, sering sharing juga",
                "pesan":"makasi buat ilmu ilmu yang di ajarin kak"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampungt",
                "hobbi": "Rafting",
                "sosmed": "@aryamudasiregar",
                "kesan": "lucu, sering becanda",
                "pesan":"semangat terus bang hari hari nya"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "seru, bisa becanda",
                "pesan":"keren terus kakk"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"riau",
                "alamat": "Pemda ",
                "hobbi": "jalan-jalan",
                "sosmed": "@lutfiaisyh",
                "kesan": "ramah, baik, bisa becandaan",
                "pesan":"tetep ramah terus ya kak"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "seru sering sharing cerita cerita",
                "pesan":"tetep jadi baik kak, sering sering sharing lagi hehe"
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "baca apa aja",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "sering becanda, bisa serius bisa ketawa ketawa",
                "pesan":"tetep keren terus bang, semangat buat kedepannya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Menerbitkan Artikel",
                "sosmed": "@deaa.rsn",
                "kesan": "keren, terus sering cerita ",
                "pesan":"semoga yang di inginkan tercapai ya kak, artikel nya cepet terbit"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "Beli risol Naya",
                "sosmed": "@cindylauura",
                "kesan": "kakanya keliatan berwibawa",
                "pesan":"mau juga kak kalo beli risol kak naya"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Hasan I, Sukarame",
                "hobbi": "Menonton AGZ",
                "sosmed": "@deaamnd3_",
                "kesan": "kak dea seru, baik, kakak NIM juga",
                "pesan":"tetep jadi baik terus kak, stay humble ya kak"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "tegas orangnya, keliatan gabisa becanda padahal bisa",
                "pesan":"tetep murah senyum ya bang"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bengong di embung c",
                "sosmed": "@devynasonyaa",
                "kesan": "kak sonya baik, asprak tpb juga, sering sharing",
                "pesan":"semangat terus buat kedepannya kak, jangan bengong di embung kak"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Cibitung",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Gangguin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "seru asik jug kalo ngobrol",
                "pesan":"semangat buat hari hari kuliahnya kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Kopri",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@alfaritziirvan",
                "kesan": "keliatan seru, terus pinter gitu",
                "pesan":"sukses terus ya bang"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Tetangganya Kak Yo",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Banyak",
                "sosmed": "@Ty_Tq90",
                "kesan": "kalo ini jangan di tanya, seru, sering becanda, lawak juga",
                "pesan":"tetep jadi bang adit yang saya kenal bang"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "humble, seru juga",
                "pesan":"semoga semua tercapai ya kak keinginannnya"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "kakanya lucu, sering senyum",
                "pesan":"sehat sehat terus kak, semangat"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton Film",
                "sosmed": "@melynznb",
                "kesan": "baik, ramah, sering sharing",
                "pesan":"jadi orang baik terus ya kak"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Traveling",
                "sosmed": "@n.shafirarz",
                "kesan": "baik ramah",
                "pesan":"semangat terus kak, jangan lupa istirahat"
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@izzah_tq",
                "kesan": "kak izzah baik banget, ramah, murah senyum",
                "pesan":"tetep jadi kakak yang baik ya kak"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "keliatannya cool gitu, tapi ternyata ada sisi lucu nya",
                "pesan":"jadi humble terus ya bang"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak Desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "baik ramah juga",
                "pesan":"semangat kakk, jaga kesehatan juga"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19gPmNif_XJ47mIMB8V2b4kTWHrvH9Ckc",
            "https://drive.google.com/uc?export=view&id=11VPABvBNdzsZCGi-uulNlu_e7ETjApEu",
            "https://drive.google.com/uc?export=view&id=1f4W0LzQPkOfP4X5L6MdGFLGVa8ZhH9hL",
            "https://drive.google.com/uc?export=view&id=18iSd_8AFRTmj6J_YKE1I44aTljEa1n-p",
            "https://drive.google.com/uc?export=view&id=11x2jB6gZvKHoHmozOJj4KaScEgy77NdF",
            "https://drive.google.com/uc?export=view&id=12Vqn0ElAPMlE4fKcAPwCCK2Uk5NJGpGJ",
            "https://drive.google.com/uc?export=view&id=10kfh7Q6LYULdMOZgq3fM7XSJLn6Cj9Ge",
            "https://drive.google.com/uc?export=view&id=1JOONNFWbETis0h_cNaPozsQ0JwAZ3CS1",
            "https://drive.google.com/uc?export=view&id=12Tmz8ItlhyJV906htOTLR0zYpgADeGGe",
            "https://drive.google.com/uc?export=view&id=1NBUUjOtb8_s_KZ3jxbq2NX6qm3Klnuqe",
            "https://drive.google.com/uc?export=view&id=1xnvWFWk0riEWCi3jrY5iXaRNuXVcxYDe",
            "https://drive.google.com/uc?export=view&id=1ibkbHEvpoBxVjIhsk-PQzuAL5sdvfhsj",
            "https://drive.google.com/uc?export=view&id=1hn_pJKHx5OpapLu2sV6xO2yapHZI1wAO",
            "https://drive.google.com/uc?export=view&id=1Mr0HmVOK_VSIntrG3I1m9K6YCzOWR2XM",
            "https://drive.google.com/uc?export=view&id=1zXUf8OH4h2mPtAVobXtfZHL4TAdIEaD3",
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
                "kesan": "seru, ssering becanda, banyak cerita juga",
                "pesan":"tetep jadi baik terus kak, semangat"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Jl Senopati Raya",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "orang nya baik, ramah, keliatan sabar banget",
                "pesan":"semangat terus kak untuk hari hari perkuliahannya"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "kak salwa baik, lucu juga",
                "pesan":"semangat terus kak buat kuliahnya"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Kulineran with May",
                "sosmed": "@azza.rrr_",
                "kesan": "santai, asik juga",
                "pesan":"semoga yang di mau tercapai ya kak"
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Jatimulyo",
                "hobbi": "Mancing",
                "sosmed": "@haikalsbln_",
                "kesan": "kelaitan tegas, tapi masi bisa ramah",
                "pesan":"semangat terus kedepannya semoga bisa lebih humble"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "baik, perhatian, lucu juga",
                "pesan":"semangat kak hari hari nya"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Aceh ",
                "alamat": "Tanjung Karang",
                "hobbi": "Kulineran with Azza",
                "sosmed": "@may_dahlia12",
                "kesan": "keliatan tegas, tapi masih asik",
                "pesan":"lebih humble dan tetep jadi orang baik kak"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "asik ramah juga",
                "pesan":"keren terus bang"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "seru, sering cerita, kocak juga",
                "pesan":"semoga bahagia terus bang"
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Bersenandung",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kak hana seru, lucu, asik juga, kalo ngobrol labas terus",
                "pesan":"tetep jadi baik terus kak"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "kak keren baik",
                "pesan":"semangat terus kak, jaga kesehatan"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"KPadang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "pembawannya santai, ramah juga",
                "pesan":"tetep jadi baik bang"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Musik",
                "sosmed": "@sarahwsti",
                "kesan": "baik, lucu, seru juga",
                "pesan":"tetep jadi baik kak, jaga ksehatan juga kak"
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "1234450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda",
                "hobbi": "Main Rubik",
                "sosmed": "@zhrptsl",
                "kesan": "kakak kelas ternyata, seru orangnya",
                "pesan":"semangat terus kak untuk kuliahnya"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Kotabaru",
                "hobbi": "Hiking",
                "sosmed": "@rexanderr",
                "kesan": "bang rendi keren, toleransi",
                "pesan":"semangat jadi kadiv nya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e4ccq8zSYLqsb_irWttQ8OYKnL4qTZPQ",
            "https://drive.google.com/uc?export=view&id=1Lsj2TW1QXmKuW9OnapAvo8rxLr0KoaW3",
            "https://drive.google.com/uc?export=view&id=1cDiusmJ8Yk1E6Xd6pirzuZiOikh8lgDl",
            "https://drive.google.com/uc?export=view&id=1QMTwHG5ECXvKO-W3HXwOgn8izefEPTXR",
            "https://drive.google.com/uc?export=view&id=1zXAiguW1pp4E56lY7s_M-qYKJC9F-vaG",
            "https://drive.google.com/uc?export=view&id=1kbgUSth5qJUovVs453g6S8jx_3WWxcuz",
            "https://drive.google.com/uc?export=view&id=1b3ZOfuONWDoTg4RZzalUhxAytMrFViPj",
            "https://drive.google.com/uc?export=view&id=1ptcZ0gXVSDg8Bnw31q8blJ_YSJyZlGkr",
            "https://drive.google.com/uc?export=view&id=1_15z4OOYH4XVW2_64D1fhrLfDsohbFuX",
            "https://drive.google.com/uc?export=view&id=1-TUP4a24Kn6IE77fnYnOiRPxfrMuUK1e",
            "https://drive.google.com/uc?export=view&id=1qxDcbQ2kezoaazNfWkd8hFLJSiHDw2bC",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Olahraga",
                "sosmed": "dananghk_",
                "kesan": "selalu baik dari masuk itera, selalu kasih saran",
                "pesan": "tetep baik terus bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "keliatan baik ramah juga",
                "pesan": "semoga kuliahnya lancar terus"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "ramah kocak juga",
                "pesan": "lancar lancar kuliahnya bang"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "baik, keren juga",
                "pesan": "semoga kebaikan selalu menghampiri"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton",
                "sosmed": "aprhtp_",
                "kesan": "baik teru, ramah juga",
                "pesan": "semangat terus kak, semoga lancar kuliahnya"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "baik, asik juga",
                "pesan": "tetep jaga kesehatan ya kak, baik baik"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "seru, baik juga, keren",
                "pesan": "keren terus, ajarin bang"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "main  game",
                "sosmed": "deviirhyu",
                "kesan": "ramah, baik juga",
                "pesan": "semangat terus ya kak"
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gg. Perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "ramah, murah senyum, baik",
                "pesan": "sehat sehat terus kak, semangat kuliahnya"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "ramah, lucu juga, baikk",
                "pesan": "Jaga kesehatan selalu, kak!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Masak",
                "sosmed": "nydiaaptr_",
                "kesan": "kak nidya ramah, seru kalo ngobrolll.",
                "pesan": "Semangat dan sukses selalu!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uxDpGIhED-sC0ni-5rmqG07U91cSf5Go",
            "https://drive.google.com/uc?export=view&id=1CALu6ERA60fbSvYc2zCF4RrwuYdFp2vm",
            "https://drive.google.com/uc?export=view&id=1Dp8tQ6gsz6HqW-IHkWqSkYB1_pwHOAXh",
            "https://drive.google.com/uc?export=view&id=1vDjJaqNYHirA7dMZqliqAWTVYt70br7_",
            "https://drive.google.com/uc?export=view&id=1fqR4xjLEGt1Xbww6qg3JgQkddo4vkA4g",
            "https://drive.google.com/uc?export=view&id=1x-_99BXA49TCiTmUtGKT4u_OOzzfRYDY",
            "https://drive.google.com/uc?export=view&id=1tSL8cCAM6bhlIrugdLcSJuiUX3OqlWq2",
            "https://drive.google.com/uc?export=view&id=12NVDHrVxDeQYldjChkn7k-D5VNwi4ie7",
            "https://drive.google.com/uc?export=view&id=1-f-6z9f9wz5TXKb3GsYhBRoHWAYaiB07",
            "https://drive.google.com/uc?export=view&id=1EVK6jOkQAtio_5W-42toHbGOSMIDL2I8",
            "https://drive.google.com/uc?export=view&id=15zkGmIs7h983qk_NRLPR2LK4_9nqAq-y",
            "https://drive.google.com/uc?export=view&id=1X7AKiNiEwwO8hsX_HVOuJiZCUah77fli",
            "https://drive.google.com/uc?export=view&id=1RxsjcMs-iGHVs1OwUokp4BkictqQrOiN",
            "https://drive.google.com/uc?export=view&id=1XvNvAoiNby_gGOgPZH35OMbd7uzHRY4B",
            "https://drive.google.com/uc?export=view&id=1Fb6cL4dih4CVujvqKzrL9x9dRBbjf11r",
            "https://drive.google.com/uc?export=view&id=1d0Zj7NamRkTRHPCd9DCZkHl2e7PjPLBf",
            "https://drive.google.com/uc?export=view&id=1exS_zK8kuwG_tw-dh29TzNcfnd1ukZzL",
            "https://drive.google.com/uc?export=view&id=1uada49-INc2ZdeUjdfJrrR0wFk_Lpso_",
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
                "kesan": "extrofert level final bosss, kak cia ramah bangett",  
                "pesan":"semangat kuliahnya kak, jaga kesehatan"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "jl. Kresna, Korpri",
                "hobbi": "Gym, Masak",
                "sosmed": "rahmaneliyana",
                "kesan": "kak rahma asik, ramah, seru juga",  
                "pesan":"semangat kak, jangan lupa makan"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "bang anam baik, asik juga, enak diajak ngobroll",  
                "pesan":"semangat kuliahnya bang!"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "bang labo seru banget. kocak, terus baikk",  
                "pesan":"semangat kuliahnya bangg, sehat selalu"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "bang rafi seru, baik, kocakk",  
                "pesan":"sehat selalu bang, semangatt"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "seru, baik, ramah, enak diajak ngobroll",  
                "pesan":"sehat selalu kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakaknya seru, asik, baikk",  
                "pesan":"sukses selalu kak"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"kotabumi, Lampung Utara",
                "alamat": "jl.pangeran senopati raya",
                "hobbi": "main gitar",
                "sosmed": "@aliyaamara",
                "kesan": "kakaknya baik, ramah, asik",  
                "pesan":"semangat terus kak, jangan lupa makan"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "kak dona baikk, sabarr, lucu juga",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "kak feby lucu banget, asik, ramah juga",  
                "pesan":"sehat selalu kak, jangan lupa makan"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labukan Ratu",
                "hobbi": "masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kak hafsa baik, ramah, murah senyum",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "mendengarkan musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "kakaknya baik, ramah, murah senyum",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "asik, baik, murah senyum",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa makan"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "baik, seru, kocak",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "baik banget, ramah, murah senyum",  
                "pesan":"semangat kak, jaga kesehatan"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "baik, lucu, murah senyum",  
                "pesan":"semangat kak"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "SSabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "lucu, baik, ramah",  
                "pesan":"semangat kuliahnyaa!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "kak rom lucuu, ramah, murah senyum",  
                "pesan":"semangat kuliahnya kak romm"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

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
            "https://drive.google.com/uc?export=view&id=1u1LCtW3ON4m7k6fTGoF9mWMLLIFaJqVP", #Rendra Eka
            "https://drive.google.com/uc?export=view&id=1WOK2tNE9sRmAsyO-UOTObseBOwIZco7P", #Krisjon
            "https://drive.google.com/uc?export=view&id=1nECdc-7fYPK6criAUITGQw7QeU0lGivJ", #Elisabeth
            "https://drive.google.com/uc?export=view&id=1eo5f-T-VG0rbJucdmgP8lD0hC1BvKI62", #syadza puspa
            "https://drive.google.com/uc?export=view&id=1pKNUI6Ld4rq8u3ATu4N0F2g1p-xBvswF", #eksanty
            "https://drive.google.com/uc?export=view&id=1fEDYHlo87ItpNZGIC-a3CzqbBKljCeIK", #Farahanum
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Bang Rendra ramah, berwibawa, sama lucu",  
                "pesan":"Sukses terus, tetap semangat abangku"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abangku yang paling baik dan humbel, lucu juga, panutan dah pokoknya",  
                "pesan":"Semoga kuliahnya lancar-luncur sampe selesai"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy dalem",
                "alamat": "Airest Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh",
                "kesan": "kakak asik banget, baik, lucu juga",  
                "pesan":"Semoga dilancarkan kuliahnya kak"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Ramah pembawaanya positif banget",  
                "pesan":"Semoga semakin banyak hal baik mengikuti kakak"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak keren, humoris jugak",  
                "pesan":"semangat terus semester 7nya"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumbar",
                "alamat": "Gya Kost Korpri",
                "hobbi": "Cute Jenderal",
                "sosmed": "@farahanumafifah",
                "kesan": "baik banget, ramah juga, murah senyum",  
                "pesan":"semoga kakak selalu dikelilingi orang baik"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15bQyOMnn7BkvLOAtWTZFv-YO0Ly9-aMU", #Jeremia
            "https://drive.google.com/uc?export=view&id=1sBRu5AhzijYBo-ZyIh0tW2KUpNWVhPIE", #dhea
            "https://drive.google.com/uc?export=view&id=1u2_f9SEozbR1MRURg6C3IPO8ttIt05SC", #Renisha
            "https://drive.google.com/uc?export=view&id=1vumMvkXKPVv6ukvsxaIKKkLo70jTs5mH", #Anisa
            "https://drive.google.com/uc?export=view&id=1lJ-4LgcegBvwsKc_gRKipvJO8NXiE1gl", #Dharu
            "https://drive.google.com/uc?export=view&id=1Hky7SpONQihpldWS_HgUK-KaGoAj0TkN", #Febi
            "https://drive.google.com/uc?export=view&id=18OGc23l6YQvXMU6ctLWHgK8LusGu35ON", #Givaro
            "https://drive.google.com/uc?export=view&id=1zs-5WHhKFekCeXi5FMGjskCv30sZcGoa", #Mirzan
            "https://drive.google.com/uc?export=view&id=1nCfDNITPiv10nIpe2uYGGL02_eSgjf7w", #Berliana
            "https://drive.google.com/uc?export=view&id=1X02M5lOM6qGZCbc_F_fHT-fq0D1-X4V4", #Juesi
            "https://drive.google.com/uc?export=view&id=1AFXvtRFJcOeuB0Y8weHP5RgyRB6YEuzC", #Ridho
            "https://drive.google.com/uc?export=view&id=1EAq37k5aYI6lbZnyMUzTI9R8Rr_XmFPC", #Feriyadi
            "https://drive.google.com/uc?export=view&id=1Pz0A36PN5hmFByqXyiOQdSCJauCvtQ3X", #Monica
            "https://drive.google.com/uc?export=view&id=16Oc1WR6j4ERRxnie6jdOF4_f7vzCItF1", #Wan Naswa   

        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "nonton orang kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "Keren, berwibawa, tegas tapi lucu, panutanlah pokoknya",  
                "pesan":"semoga cepat sempro bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "lomba ga makan keerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "lucu, baik, keibuan banget",  
                "pesan":"Semoga selalu dimudahkan dalam urusannya"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "tidur",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya humble dan sopan.",  
                "pesan":"Semoga sehat selalu kak"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@anisftynn_",
                "kesan": "Kakak ini paling kalem di baleg",  
                "pesan":"banyak-banyak bersabar kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "abangnya punya semangat ga habis-habis",  
                "pesan":"Sukses selalu bang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya humbel, baik, lucu",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi,Lampung",
                "hobbi": "dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "abangnya santai tapi tetap berwibawa",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "Tenang tapi humble",  
                "pesan":"Semoga kebahagiaan selalu menyertai"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya seru dan lucu banget",  
                "pesan":"Semoga sehat selalu"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya lucu dan suka lupa nama orang",  
                "pesan":"Semoga terus berkembang kedepannya kak"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Mainn paddle",
                "sosmed": "@iamridhomanik",
                "kesan": "abangnya lucu banget dan selalu bikin ketawa",  
                "pesan":"Semoga selalu diberi keberkahan bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi batch google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "tegas dan berwibawa ",  
                "pesan":"semangat terus dalam beraktivitasnya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya lembut dan positif vibes banget",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Farakan",
                "hobbi": "nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lucu dan asikk banget",  
                "pesan":"Semoga selalu disertai kebahagiaan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ipgl-D4MmaYzjAsZDzFgFtkZkCiNyB_r", #Bintang
            "https://drive.google.com/uc?export=view&id=12v1zHDFmHicsFNUh9y_bi7jtgl2MSbaK", #Nadya
            "https://drive.google.com/uc?export=view&id=16Cr1CQ81htbjC8HVouEtTuvXsaTRUyQR", #Azizah
            "https://drive.google.com/uc?export=view&id=1baiixi18AH_KWl-U9H8BScj2R4d7d44K", #Hana
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Dengar lagu, nyanyi, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Keren banget rekor organisasi dan kepanitiaanya banyak banget",  
                "pesan":"jangan lupa jaga kesehatan bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Baik, ramah, humble juga",  
                "pesan":"Sukses terus kedepannya kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main ice skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakaknya pendiam",  
                "pesan":"semangat terus kedepannya kak"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomart Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya lucu sama murah senyum",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
         "https://drive.google.com/uc?export=view&id=1a5t9DefaF0Bdh4PBQjdGfSLKbPctwF9u", #Ferdy Kevin
         "https://drive.google.com/uc?export=view&id=1zQZZpQs1Sqqv-Sm85P_Yr8Fv6c17wbaL", #Afifah
         "https://drive.google.com/uc?export=view&id=1Qj3aUSiAorMSvbWV5qJ_93QdLm3-eht3", #Alya
         "https://drive.google.com/uc?export=view&id=1d4eA3ARpOBNgyDSnYYsvjeh-6U7syM9Y", #Ahmad
         "https://drive.google.com/uc?export=view&id=1OeQw3koIKqa5X4tZSEYg9Wiu_mtihM1A", #Arin
         "https://drive.google.com/uc?export=view&id=1k2c_2hq1hjWdWtyi5bSdyTg_8W3AWGEp", #Daffa
         "https://drive.google.com/uc?export=view&id=1W7o3O8LW4UP0oQWmKUE7kt55II4MrmVz", #Fajar
         "https://drive.google.com/uc?export=view&id=11txZlQr81q9SLmYF3RFHcmIAX1AXKGDT", #Natasha
         "https://drive.google.com/uc?export=view&id=15_dK9OqYRJ9k6807dfUhmAI_o5ZJnOby", #Nobel
         "https://drive.google.com/uc?export=view&id=1Jh7VDf6raeMI3dtgpLDH6OvRvz0JGW5y", #Aji
         "https://drive.google.com/uc?export=view&id=1Dg3_22Jll0tlLnlHt4Rqj9VeZ7IZABDv", #Vani
         "https://drive.google.com/uc?export=view&id=1RbaEnsSPVRX84wy5TGUK6I-sgwAH_iVE", #Sahid
         "https://drive.google.com/uc?export=view&id=1lC_a98rIqr66s_djdPWazGlImsL7pJ9r", #Paris
         "https://drive.google.com/uc?export=view&id=1Ve0DNYeFA6mYLhTLpehRN-G_E8f3W70B", #Raska
         "https://drive.google.com/uc?export=view&id=1KKile6zY9X9Z7aPgzXvSur9Noh8tz95x", #Kharisma
         "https://drive.google.com/uc?export=view&id=1vggRjtcRblvpQJVJS3i1shcqKaB9CCmo", #Ocha
         "https://drive.google.com/uc?export=view&id=1tEIPEJvhReR469dp1ScaqtqjKWGq38Mu", #Maul
         "https://drive.google.com/uc?export=view&id=1Kb2KEUyzoIYL6bDIrpG-2L8U0W0HtY7i", #Daffa Ahmad
         "https://drive.google.com/uc?export=view&id=1qyXFS1_oKNMekFjTgWwtgfREyr-AJ3qO", #Daniar
         "https://drive.google.com/uc?export=view&id=1zdYWKBmTuh93EWEetNyU7IoxQlWC-FHv", #Ihsan
         "https://drive.google.com/uc?export=view&id=1TNSDdI59O9ygjvsoR7vDtMcrbvbW4I-3", #Kevin
         "https://drive.google.com/uc?export=view&id=1sNhzyP-X1BWqQ_cgTG9dC9yd-jAIH3ES", #Lidia
         "https://drive.google.com/uc?export=view&id=1OM7rh7YGT9HFyPS3taKmTUVc69GAlQLI", #Ridwan
         "https://drive.google.com/uc?export=view&id=1Mb7pS1wCClxfRqX7bAdpH6bddhgaYSi-", #Liano
         "https://drive.google.com/uc?export=view&id=1grIZQMGUse5897z2EhjyTguj85dPShm-", #Benget
         "https://drive.google.com/uc?export=view&id=19NTqb5hThqHCuvIp8_h479AxPBXwI5Cm", #Rewina
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya keren banet, diam tapi berwibawa",
                "pesan":"semoga selalu siberikan kemudahan dalam segala hal bang"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri Sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya manis dan baik",  
                "pesan":"semangat menjalani semester akhirnya kak"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Baik,humbel banget,sama tegas juga, panutanlah pokoknya ",  
                "pesan":"Tolong bimbingannya lagi kedepannya kak"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "12340050",
                "umur": "20",
                "asal":"Tanggerang Selatan",
                "alamat": "samain kayak bang fajar",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "panutan banget selu jadi role model",  
                "pesan":"main ps lagi yok bang"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Kost Orange",
                "hobbi": "Ngekader",
                "sosmed": "@arientakhsnl_",
                "kesan": "kakaknya baik banget dari awal ketemu pas semester 1",  
                "pesan":"semoga selalu diiringi hal baik"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Airan",
                "hobbi": "Jailin miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "abang nim yang selalu membuat kagum",  
                "pesan":"semangat terus abangku jaga kesehatan juga"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main Game",
                "sosmed": "@ginda_mrp",
                "kesan": "Baik banet orangnya selalu jadi panutan dan role model",  
                "pesan":"jangan lupa istirahat bang"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kostan putri gerbang barat sebelah sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "kakaknya baik dan lucu juga",  
                "pesan":"Terimakasih roti marienya kemarin kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekan baru",
                "alamat": "wisma Emas setengah",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "seru banget kalo ngobrol sama abang satu ini, pemahamannya luas",  
                "pesan":"nanti ngobrol-ngobrol lagi ya bang"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Fam",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "bang aji baik sama rohanis banget",  
                "pesan":"semangat semester akhirnya bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kak vani baik banget, pengertian juga",  
                "pesan":"semangat terus kak, jaga kesehatan juga"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22__",
                "kesan": "abangnya asik dan murah senyum",
                "pesan":"semoga diberikan kelancaran dalam segala hal bang"#1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung,Lampung Timur",
                "alamat": "nangka 4",
                "hobbi": "main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "abannya lucu dan soft spoken banget",
                "pesan":"semangat terus kedepannya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "kakaknya baik banget",
                "pesan":"semangat terus menjalani hari-harinya kak" # 1
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450079",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya tegas tapi baik banget",
                "pesan":"semoga apa yang kakak inpikan tercapai", # 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kakanya lembut banget",
                "pesan":"semangt terus kedepannya kak" # 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jalan Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "abangnya kalem dan murah senyum",
                "pesan":"semoga selalu dikelilingi hal baik bang"
            },
            {
               "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Jl. Korpri Raya",
                "hobbi": "nontonin anak tari latihan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "abangnya asik dan berkarisma banget",
                "pesan":"semangat terus bang" # 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas raya No. 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "kakaknya jago tari",
                "pesan":"ajarin tari dong kak" # 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Joki strava",
                "sosmed": "@ihsan.myusus",
                "kesan": "abangnya lucu kalo marah",
                "pesan":"semangat terus abangku" # 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "PanjanG selatan",
                "hobbi": "terjun payung",
                "sosmed": "@kevinaj__",
                "kesan": "takut pas awal ketemu",
                "pesan":"infokan main basket lagi bang" # 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakaknya ramah banget",
                "pesan":"sehat selalu kak" # 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung tengah",
                "alamat": "Belwis",
                "hobbi": "nonton anak tari perform",
                "sosmed": "@m.ridwan_22",
                "kesan": "abangnya asik banget kalo diaajak ngobrol",
                "pesan":"semnagat terus bang" # 1
            },
            {
                "nama": " Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "jl. Raden Saleh",
                "hobbi": "ngerjain soal matematika",
                "sosmed": "@liano.wlm",
                "kesan": "abangnya pendiam tapi humbel",
                "pesan":"sehat-sehat bang" # 1
            },
            {
                "nama": " Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera utara",
                "alamat": "Belwiss",
                "hobbi": "main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "abangnya baik,lusu dan asik",
                "pesan":"jaga kesehatan bang" # 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Ratu, Bandar Lampung",
                "hobbi": "nonton anime",
                "sosmed": "@rewinanaa",
                "kesan": "kakanya baik banget",
                "pesan":"semoga diberi kelancaran semester 3nya kak" # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vkjXJenRg2yGBEUSsYwfKWg4hNVfeNcC", #Randa
            "https://drive.google.com/uc?export=view&id=1Vf6d0U0u_-O3t8SM2AGa6mu6lFx8NzBO", #Rut
            "https://drive.google.com/uc?export=view&id=1EU0eNjroGJewepyp_GSe25PdkkJvm7RH", #Regi
            "https://drive.google.com/uc?export=view&id=1lrrnX1ev_5W5NP8Q2VPDvYMSW_SO2O7C", #aisyah
            "https://drive.google.com/uc?export=view&id=1IaFHsGXW5Sgk8zd3XyrUq5QwXwYCEL0R", #Fadil
            "https://drive.google.com/uc?export=view&id=1AfejiWNyqG1Z_68JCnXwg4mZD92JlUIu", #Aqil
            "https://drive.google.com/uc?export=view&id=1oudaNw_Ve0we0q4L9FCv153w7RhS4D5A", #Naufal
            "https://drive.google.com/uc?export=view&id=16ZeQkaxVm8U17xS9SJyQTyhXdV8BRykM", #Nadia
            "https://drive.google.com/uc?export=view&id=1Cb0JOyldk4Dmrpx388X5Rb-9p73n9Krv", #Marleta
            "https://drive.google.com/uc?export=view&id=135anViqKyy6k_3a4GkGPSD5UN18p3y4v", #Akelya
            "https://drive.google.com/uc?export=view&id=1WrV8pUJUHFQW3TtKMUOd-_I8p2eM9EnY", #Anggi
            "https://drive.google.com/uc?export=view&id=1BzUPIkvIgMTphC2np4Slxpjri4BI0zJu", #Efi
            "https://drive.google.com/uc?export=view&id=1rH7ryWho-B0d7cblYOGcO0R7m-Aka8lQ", #Fabiola
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Fairuz
            "https://drive.google.com/uc?export=view&id=1DSF1bHkr9Cq8FCDvlcRdqsWj15Q3Keni", #Tanty
            "https://drive.google.com/uc?export=view&id=1exzEXPFuv2Zg8mfqRsUihdaCTCGnwyQX", #Eggi
            "https://drive.google.com/uc?export=view&id=1BRF2gFY2zNRu7hIRXeWTUhRr_ZtcmwIx", #Afifah
            "https://drive.google.com/uc?export=view&id=15hNTNoIq1-HtDog3FAUCXRlLz2M88n4q", #Fabio
            "https://drive.google.com/uc?export=view&id=1xlUU-pdbPSJkp_gv7wpfWYs49m3GygTu", #Gio
            "https://drive.google.com/uc?export=view&id=1LyJ9ai53yd-E7ZNRmtbkL7ysxdxvE4mE", #Rahma Okta
            "https://drive.google.com/uc?export=view&id=1aE46Eo9UwSITKPm7OI80fELvpbaI3wnf", #Rahmah
            "https://drive.google.com/uc?export=view&id=1_tW37Chzrxig9fao-Ua-_yjQfztq3S4p", #Razin
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "1222450083",
                "umur": "22",
                "asal":"Serang,Baten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berenang",
                "sosmed": "@randaandriana_",
                "kesan": "abangya murah senyum",
                "pesan":"semangat terus abangku" # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "kakaknya pendiem",
                "pesan":"semangat terus kak" # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "abangnya ganteng",
                "pesan":"tutor ganteng dong bang" # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. lapas,Belwis",
                "hobbi": "maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya sederhana tapi berkesan banget",  
                "pesan":"terus semangat ya kak, jangan pernah berubah!" # 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "abangnya keren banget duta genre",
                "pesan":"semangat terus bang" # 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "bang aqil lucu",
                "pesan":"semangat terus bang " # 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "abangnya pendiam",
                "pesan":"semnagat terus bang" # 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "kakaknya asik banget",
                "pesan":"semanget terus kak" # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "kakaknya murah senyum",
                "pesan":"semoga sehat selalu kak" # 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234500119",
                "umur": "20",
                "asal":"Pramuka, Bandar Lampung",
                "alamat": "Perum Bukit Alam Permai 3, Blokk C, No.9",
                "hobbi": "Dengrin musik",
                "sosmed": "@keyashafi_",
                "kesan": "abangnya pendiem dan baik",
                "pesan":"sehat-sehat bang" # 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bummisari Kec.Natar",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakaknya ramah",
                "pesan":"jaga kesehatan kak" # 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Sale, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "kaka sekum pplk"
                "pesan":"jaga kesehatan ka" # 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "kakaknnya murah senyum",
                "pesan":"sehat selalu kak" # 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakaknya baik",
                "pesan":"semangat kak" # 1
            },
             {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "kakanya lucu, imut, dan baik banget",
                "pesan":"inget untuk jaga kesehatan ya kak" # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "abnangnya keren betull",
                "pesan":"sehat selalu bang" # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang (main game)",
                "sosmed": "@fifah.zy",
                "kesan": "kakaknya baik banget",
                "pesan":"sehat terus kak" # 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer),tidur,jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "abangnya lucuk banget",
                "pesan":"sehat trus bang, jaga kesehatan" # 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@giofaniars_",
                "kesan": "panutan ozt",
                "pesan":"semangat terus bang pertahankan ipknya"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "kakanya baik banget",
                "pesan":"ajarin main catur dong kak" # 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "kakaknya asik"
                "pesan":"auoo balapan kak" # 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans Sakum,Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "abangny apendiem tapi asik",
                "pesan":"semoga diberi kemudahan bang" # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18k6HnB6knAo02J10mE8wLz8D7rnqUfy5", #Arafi
            "https://drive.google.com/uc?export=view&id=1Q5tSfeKVdizqKDtVZIe2tH2thbKndEQB", #Yohana
            "https://drive.google.com/uc?export=view&id=1bRiSGcJrgf2OcFe3lsd6eN4eeI94esHn", #Jasmine
            "https://drive.google.com/uc?export=view&id=1IBvN9xNvkJ30-ZYCQAc0crkph_slWaPh", #Arini
            "https://drive.google.com/uc?export=view&id=1Cf9tOQIA7_SVu2XNZhBcEp6qYJ3thHKB", #Arya
            "https://drive.google.com/uc?export=view&id=1mdCyWLSJ0ApiovYIdtRDexrZafTPsEbz", #Mut
            "https://drive.google.com/uc?export=view&id=1_qg8u3m4pwAASrtpKNexJJ7sm6w0Azu-", #Luthfia Aisyah
            "https://drive.google.com/uc?export=view&id=13gBBt7hSCWGZtDTJm1eqYBTPl84jz5vA", #Nablya
            "https://drive.google.com/uc?export=view&id=1tLuOAwLUngG638u6MkqNdv_m-JHyJeSh", #aldi
            "https://drive.google.com/uc?export=view&id=1DXwDpx06hfZAYwhNJ8C96o9CFU9nkWpz", #Dea
            "https://drive.google.com/uc?export=view&id=1CNZR8u8IRCf6ZSChGpJtm-xacuub2a2S", #Cindy
            "https://drive.google.com/uc?export=view&id=16YKC_OBRW0dOq5drTMi-IHG9TIG28EZx", #Dea
            "https://drive.google.com/uc?export=view&id=1uDzLaYMtxcTtEjN1V46s-6f24ffYBLPN", #Desman
            "https://drive.google.com/uc?export=view&id=1QIn926h2_H3KeHkqcK_iblbZPJXRvM1t", #Sonya
            "https://drive.google.com/uc?export=view&id=1CrmSKsKqdyiTWB7wLiBE42-Ad4DQXMaL", #Luthfia
            "https://drive.google.com/uc?export=view&id=1aNElLEyHViuqUp09rsoWoOZJd3PeIZXV", #Irvan
            "https://drive.google.com/uc?export=view&id=176vKv_ZmiRkQgvTJxlzA7jsBPXuYmJy5", #Aditya
            "https://drive.google.com/uc?export=view&id=1DsOv1UkrTVXrXSxVhvqz2ZCbFSV-vPId", #Fathya
            "https://drive.google.com/uc?export=view&id=1aWfbA0ArdKwK8ZqTrZ_k6_5kWqdj1s0v", #Ilmi
            "https://drive.google.com/uc?export=view&id=1452Jeofb06Cbs_br_apURc-TJk_XzkJW", #Melinza
            "https://drive.google.com/uc?export=view&id=1rEUBbqf-ByQDTC0y0eXg_sy_AZEmtqhD", #Nayla
            "https://drive.google.com/uc?export=view&id=1KKFV-rReSmbZWS1aQ-N76huwOqjay1aT", #Izzah
            "https://drive.google.com/uc?export=view&id=1nXLm11Cp3-y8vEnRn2hgfmXBaEzoUN0c", #Qois
            "https://drive.google.com/uc?export=view&id=10VHL2XkTbY07dW_4kqLKfUA00pN42Jo1", #Tarisya
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Warjo",
                "hobbi": "Makan Warjo",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Bang Arafi baik banget",  
                "pesan":"Semangat terus bang"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana positive vibes banget",  
                "pesan":"Sukses selalu kak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya seru banget",  
                "pesan":"Semoga terus jadi pribadi yang inspiratif dan menyenangkan"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Lancar terus kuliahnya kak"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya lucu banget",  
                "pesan":"Tetap semangat kuliahnya bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Khoirul enak diajak ngobrol",  
                "pesan":"Bahagia dan sukses selalu kak"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia lucu banget",  
                "pesan":"Tetap jadi orang yang semangat terus kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla lembut dan ramah banget",  
                "pesan":"Semoga selalu dikelilingi hal baik kak"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@",
                "kesan": "Abangnya baik banget",  
                "pesan":"Semoga makin sukses bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea seru dan baik banget kaya ibu peri",  
                "pesan":"Semangat kuliahnya kakak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak cindy cantik banget",  
                "pesan":"Bahagia terus kak"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea ramah banget",  
                "pesan":"Tips jadi MC kak"# 1
            },
            {
                "nama": "Desman Velius Halaws",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman baik banget",  
                "pesan":"Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya ramah dan baik banget",  
                "pesan":"Bahagia terus kak"# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak lulu ekstrovert parah tapi seru banget",  
                "pesan":"Lancar terus kuliahnya kak"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya keren banget",  
                "pesan":"Sukses dan sehat selalu bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "Abang santai tapi enak diajak diskusi",  
                "pesan":"Semoga sukses terus dan tetap rendah hati, Bang!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya lucu banget",  
                "pesan":"Semoga makin sukses dan tetap ceria bang"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Ilmi keliatannya kalem",  
                "pesan":"Semoga terus semangat belajar kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melin ramah dan lembut banget",  
                "pesan":"Bahagia selalu kak"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla seru banget diajak ngobrol",  
                "pesan":"Semoga terus berkembang kak"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semoga makin sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya asik banget",  
                "pesan":"Semoga terus semangat dan sukses kedepannya bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakaknya keren banget",  
                "pesan":"Tips pinternya dong kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen Internal":
    def DepartemenInternal():
         gambar_urls = [
             "https://drive.google.com/uc?export=view&id=1yvY_qNRMkhZCA3CKsJB13IFEuhpWQH2h", #Rani
             "https://drive.google.com/uc?export=view&id=1cZvcAZ9iAuytks2xBQlT-gPQAh38OU7Z", #Renta
             "https://drive.google.com/uc?export=view&id=1aIxIHmxxqGF6AncZ93HjfIhORCfdJLih", #Salwa
             "https://drive.google.com/uc?export=view&id=12EH8csoSlyVoN15Qo29DNs_JMVUZWaxW", #Azzahra
             "https://drive.google.com/uc?export=view&id=1V-RPRf2BizFWqFQoyonNBJ3I5nszB-cG", #Haikal
             "https://drive.google.com/uc?export=view&id=1cNdbIeSJNmMBMniDAIjCuqqgGoZpC4eo", #Iqfina
             "https://drive.google.com/uc?export=view&id=1kriJhv9lOS4EP30x6N0Pn0ysu_FCO06g", #May
             "https://drive.google.com/uc?export=view&id=1kwIkf8MOvb88-pReHdLgDjWXaitKhvQ0", #Naufal
             "https://drive.google.com/uc?export=view&id=1ktjS6LZGjYsHCOUsvTVcvXB4sfmL1KDD", #Zailani
             "https://drive.google.com/uc?export=view&id=1H9Tx1zHRskK1umjirEcFGJ2uP250iUsE", #Rendi
             "https://drive.google.com/uc?export=view&id=1opzroLjX4i5WlEjISUonkSICu3nOpINl", #Hanna
             "https://drive.google.com/uc?export=view&id=1u2WHDTIKGIJ1-YULZLogISBvzcvZCrPY", #Keren
             "https://drive.google.com/uc?export=view&id=1a24stIOVRpoDp685rHuK1VKREghF3IGW", #Hanif
             "https://drive.google.com/uc?export=view&id=1mzLB1zAKRVqShRVQKm_U_Ac901HX98QP", #Sarah
             "https://drive.google.com/uc?export=view&id=1a-8GKc3aE35xeEuLaZwtrH8AFSI0Wn0_", #Zahra
         ]
         data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "12245030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Suka banget liat outfit kak rani keren banget",  
                "pesan":"Semoga kak Rani selalu bahagia dan makin sukses kedepannya"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Abang ramah dan punya vibe yang tenang banget",  
                "pesan":"Semoga sukses selalu ya Bang!"# 1
            },
            {
                "nama": "Salwa Farhanatusaiidah",
                "nim": "12245055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa kalem dan sopan banget, enak diajak ngobrol",  
                "pesan":"Semoga semua cita-cita kak Salwa tercapai dan selalu sehat"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakaknya ramah banget",  
                "pesan":"Semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Haikal fransisko Simbolon",
                "nim": "122450106",
                "umur": "18",
                "asal":"Tulang Bawang",
                "alamat": "Sukabumi",
                "hobbi": "Membersihkan rumah",
                "sosmed": "@haikalsbln_",
                "kesan": "Kirain abangnya galak banget, ternyata baik",  
                "pesan":"Lancar terus kuliahnya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450076",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak iqfina cantik banget",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya ya, Kak!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450009",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak may keren dan keliatan tegas",  
                "pesan":"Sehat selalu kak"# 1
            },
            {
                "nama": "Muhammad Naufal Afghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@Muhammadnaufalafghani73",
                "kesan": "Abangnya kalem banget",  
                "pesan":"Tetap semangat kuliahnya bang"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya positive vibes banget",  
                "pesan":"Semoga sukses terus dan tetap semangat bang!"# 1
            },
             {
                "nama": "Rendi Alezander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@lexanderr",
                "kesan": "Abangnya baik banget",  
                "pesan":"Sukses selalu bang"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna ramah dan ceria banget",  
                "pesan":"Bahagia terus ya kak"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak keren cantik banget",  
                "pesan":"Tips cantiknya dong kak"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hifzky",
                "kesan": "Abang Hanif seru banget, enak diajak ngobrol",  
                "pesan":"Semoga sukses terus dan tetap rendah hati, Bang!"# 1
            },
            {
                "nama": "Sarah wasti",
                "nim": "122450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah keliatan lembut dan soft spoken",  
                "pesan":"Semoga selalu diberi kebahagiaan dan kesuksesan"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "Main Rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semoga terus semangat dan sukses kuliahnya"# 1
            },
        ]
         display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OKJeDVtRiSPdq_XX1Fus5bSlpjNz8gaD", #Danang
            "https://drive.google.com/uc?export=view&id=1u7nycVKRAvN9PUbTlNk6Fr8QYCRLoFPD", #Syalaisha
            "https://drive.google.com/uc?export=view&id=1ldUlvp2Rk4-cUTtuqARP6jhGFxLQCWoV", #Ahmad Rizqi
            "https://drive.google.com/uc?export=view&id=143FGcR_VsN7EE72i3RQttNePUKVwUJ8y", #Anadia
            "https://drive.google.com/uc?export=view&id=1K1CpCim1thZnm2N__oR9wJZ9Zj6wJTy1", #Aprilia
            "https://drive.google.com/uc?export=view&id=1ZolBhfDYPP57vPYYZS_xORs9WSueGo5Y", #Nabila
            "https://drive.google.com/uc?export=view&id=1p_kF2BBcigUtL5x9vesicMY2JIssaY4V", #Dhafin
            "https://drive.google.com/uc?export=view&id=1oDNYrV-9q86KqxX6k9M0nDHEE0eegsNP", #Devi
            "https://drive.google.com/uc?export=view&id=1uqpKwNVk5lppmwi0KHW71Afl1jWmfLDe", #Enggli
            "https://drive.google.com/uc?export=view&id=1mfCKlV7A8ujqPlbcptH3CBNhWLri01S4", #Naya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Nydia
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal":"Balam",
                "alamat": "Belakang PB",
                "hobbi": "Joging",
                "sosmed": "@dananghk_",
                "kesan": "Bang Danang seru banget diajak ngobrol, banyak hal baru yang saya dapat",  
                "pesan":"Terus berkarya ya bang dan semangat kuliahnya!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450012",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya lembut dan punya aura yang menenangkan",  
                "pesan":"Terus semangat kak!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki_",
                "kesan": "Outfit abangnya keren keren banget",  
                "pesan":"Sehat dan bahagia selalu bang"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Joging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat terus kak kuliahnya"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton dramashort di fb",
                "sosmed": "@aphrhtp_",
                "kesan": "Kakaknya tinggi dan cantik banget",  
                "pesan":"Semangat terus kuliahnya kak, jangan lupa jaga kesehatan!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_azazahra",
                "kesan": "Kakaknya ramah banget",  
                "pesan":"Semoga makin sukses dan bahagia selalu kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya keliatan kalem",  
                "pesan":"Tetap semangat dan terus jadi inspirasi bang!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya seru banget",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya ya, Kak!"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gang perwira 2",
                "hobbi": "Nontol alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakaknya cantik dan anggun banget",  
                "pesan":"Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak naya seru dan ramah banget",  
                "pesan":"Tips bikin risol enak dong kak"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Semoga selalu diberi kelancaran dalam kuliahnya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KuFKnRbqVIEyRnXmYiWa9ptlDOnGPJpm", #Patricia
            "https://drive.google.com/uc?export=view&id=1hvZE3smk8in0P7_cNISWEbcVn1v7xL8j", #Nely
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Anam
            "https://drive.google.com/uc?export=view&id=16o1hTvQCrxB5GG5VLXUPpsy4nY1ixWQA", #Labo
            "https://drive.google.com/uc?export=view&id=1rjlRnv40tfU8Th66vgHmm3ptTWJsWPTw", #Rafi
            "https://drive.google.com/uc?export=view&id=1PV0YIIVBRc-jM12Qx_KZdDZ29Yt_s-ou", #Refa
            "https://drive.google.com/uc?export=view&id=1DtpQuKH7BLcbKsZ4CYwq-allBwmivK-F", #Try Yani
            "https://drive.google.com/uc?export=view&id=1OqmUNBZZP6b4InBGZooQPh1EllSIvIw1", #Aliya
            "https://drive.google.com/uc?export=view&id=1RMuR49VHNNWE0UfrS07TzARHd1E61SZl", #Donna
            "https://drive.google.com/uc?export=view&id=1egzSb1a6GMmoOf5xY0tjHpAUWfX1mCmd", #Feby
            "https://drive.google.com/uc?export=view&id=1RS5oyMXwmUWCIfON5gean9IZLGTRpsLp", #Hasfa
            "https://drive.google.com/uc?export=view&id=19lT1uUm7DI3_NrwuzxXY01yUFBJk4XtZ", #Nayla
            "https://drive.google.com/uc?export=view&id=1dTS5l-BnNx0sLogF7WT_NmDAYsb5RQMB", #Sania
            "https://drive.google.com/uc?export=view&id=15KDuXA1SaSs4YFAH1Euht8LwlTv2CJw1", #Akmal
            "https://drive.google.com/uc?export=view&id=1aM7h0uctEExNqev5Pl-Kism58mgumAJJ", #Raihana
            "https://drive.google.com/uc?export=view&id=1qAamICFhi2d6W4HoxXpFbkMJlQozmu4M", #Citra
            "https://drive.google.com/uc?export=view&id=1Fb5OF4grSygvBUEHqQYJP4ro2LKx4AKh", #Eigi
            "https://drive.google.com/uc?export=view&id=1MeWmTHB_Y-cAFVu2CyXOd6pJyRLF6tEx", #Roma
            
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya easygoing dan enak banget diajak ngobrol",  
                "pesan":"Semoga selalu bahagia dan sukses di setiap langkahnya kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak nelly ramah dan seru banget",  
                "pesan":"Terus semangat kuliahnya dan tetap jadi pribadi yang lembut ya!"# 1
            },
            {
                "nama": "Khoriul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam__",
                "kesan": "Abangnya seru banget",  
                "pesan":"Semangat terus, Bang!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Hui",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya keren banget",  
                "pesan":"Terus berproses ya bang!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Bang Rafi baik banget",  
                "pesan":"Semangat PDD ya bang"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa baik banget",  
                "pesan":"Terus jadi diri sendiri dan percaya diri kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122350020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaa",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Tetap semangat menimba ilmu dan jangan lupa istirahat kak"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kakaknya positive vibes banget",  
                "pesan":"Terus semangat dan bahagia selalu kak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya lembut dan sopan banget",  
                "pesan":"Semoga semua harapan dan cita-citanya tercapai ya, Kak!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kakaknya cantik dan lucu banget",  
                "pesan":"Semangat terus kuliah dan tetap jadi pribadi yang positif!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya seru dan punya vibe ceria",  
                "pesan":"Terus tebar energi positifmu ya Kak!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas, Jati Agung",
                "hobbi": "Dengar musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla keliatannya kalem",  
                "pesan":"Tetap semangat dan terus jadi inspirasi buat orang ya kak"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania ramah banget",  
                "pesan":"Semoga makin sukses dan tetap membawa energi positif, Kak!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Bang Akmal keliatannya kalem",  
                "pesan":"Terus berproses dan jangan berhenti mengejar cita-cita ya bang!"# 1
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana keren banget",  
                "pesan":"Semangat mnenjalani hari-harinya kak"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra cantik banget",  
                "pesan":"Kasih Tips jago melukis dong kak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah balau residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak eigi ramah dan Baik banget",  
                "pesan":"Jaga kesehatan kak" # 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak roma lucu dan imut"
                "pesan":"Semoga sukses terus kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()

# Tambahkan menu lainnya sesuai kebutuhan






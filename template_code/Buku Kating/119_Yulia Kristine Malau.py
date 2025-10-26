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
            "https://drive.google.com/uc?export=view&id=1BVMhetrCZdaJ-p_0Tbz-ycNrQD9i-lVB",
            "https://drive.google.com/uc?export=view&id=1aUkWi1i7CrXA5ptPEbjmUtrhCoosgRr9",
            "https://drive.google.com/uc?export=view&id=1jmv2Nd3-S_70epLZokQVsrcAnk1cRaPv",
            "https://drive.google.com/uc?export=view&id=1E3xgR7opV8cgcam6EaO0jVRejBCzOroM",
            "https://drive.google.com/uc?export=view&id=1LskJNSBTT313Bb6GnHRVbNbRpXnyPYEC",
            "https://drive.google.com/uc?export=view&id=19kzS0pMvt8BmcVOxyi4b-PB-a7lTUCWn",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Bang Rendra keren banget",
                "pesan": "Semangat terus kuliahnya Bang!!!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Johannes keren banget!!",
                "pesan": "Terus semangat kodingnya Bang!"
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Elisabeth lucu!",
                "pesan": "Jangan lupa istirahat dan tetap semangat ya kak Elisabeth!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza tenang, pinterr bangett!",
                "pesan": "Tetap semangat kak Syadza!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty suka yapping, sya sukaaa!",
                "pesan": "Tetap jadi kakak yang ceriayaa, semangat kakakk!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak Farahanum seru banget!",
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JZ4CTStV6VJE1Hc5_kNVO5nh95c1rDst",
            "https://drive.google.com/uc?export=view&id=19vWTh328ai532S32nLZtJhYNnbF6T1xf",
            "https://drive.google.com/uc?export=view&id=1uEFATeIn4avSgHTJ_c6Vc2V40FdPu0CV",
            "https://drive.google.com/uc?export=view&id=1RITTI3S6jTsAL1ec-3Fj1XkBu_gmRogN",
            "https://drive.google.com/uc?export=view&id=1UOqFmnmwpFTu9zHxIqtMWBoWeJulb8me",
            "https://drive.google.com/uc?export=view&id=1aZQKYKZidYGkbyJGaKgabFAzx5NtiElB",
            "https://drive.google.com/uc?export=view&id=1HzQNe8kBesvYGJ2gaJQDgmpzvxEjENMp",
            "https://drive.google.com/uc?export=view&id=19iQ_mL_Kof4iM13VRwRjgbvJh4QJaN6q",
            "https://drive.google.com/uc?export=view&id=1btkpy4y7V4HZl68zJuyzm8IXRIsoqulP",
            "https://drive.google.com/uc?export=view&id=1HxwkEKkXL_BERfMpvLyP0H7xceFyQa1Q",
            "https://drive.google.com/uc?export=view&id=1U_EXB-fIL9dcAXO1A8tnlbdLboLO0K4C",
            "https://drive.google.com/uc?export=view&id=1YDLGSEU3Tq5lPWjbl8_7fklvZeFW4TMJ",
            "https://drive.google.com/uc?export=view&id=1mvYDD1-fEZgMBho7if4e_PqLl3iwxcMh",
            "https://drive.google.com/uc?export=view&id=1_TIcGpOv5NH49b2APOkbRMXNOqXG-8re",
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
                "kesan": "Bang Jeremia orangnyaa humble, senyum mulu",
                "pesan": "Semangat terus kuliahnya Bang, jaga kesehatan!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak Dhea nya seru!",
                "pesan": "Tetap semangat ya kak Dhea, jaga kesehatah!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha bikin adem!",
                "pesan": "Tetap jadi sumber inspirasi ya kak!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Kak Anisa awalnya pendiem tapi ternyata seru juga",
                "pesan": "Semangat terus kuliahnya kak Anisa!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Bang Dharu kocak dan humble banget",
                "pesan": "Tetap jadi lucu yaa kak!"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "Kakak lucu banget, rambutnya cantik",
                "pesan": "Jaga kesehatan yaa kakak!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro santai tapi keren banget",
                "pesan": "Semoga selalu tenang semangat kuliahnya Bang!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan seruuuu!!",
                "pesan": "Bang next time cobain bakso syukron all u can eat, enak!!!! rasa surga!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kak Berliana seruuu banget!",
                "pesan": "Semangat terus yaa kak, jaga kesehtan!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kak Juesi ramah dan lucu banget",
                "pesan": "Semangat terus ya kak Juesi, jaga kesehatan"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho sibuk tapi tetep sempet main padle!!",
                "pesan": "Keren Bang Ridho bisa bagi waktu antara organisasi dan hobi, jangan lupa ajak kami main juga ya kak. Hehee!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Bang Feryadi lucu dan chill!",
                "pesan": "Jaga Kesehetan ya kakk!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica pro banget kalau udah main ML!",
                "pesan": "Saya juga main ML Kak, only Estes. Next time main bareng ya kak hehe!"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa lucu, gemash gemash!",
                "pesan": "Jaga kesehatan yaa kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VMC-egFegqX-ZirzwVEUtYJ2sgxwsclX",
            "https://drive.google.com/uc?export=view&id=1CjRy-bOJoKa-fas5Wl5rzZVQ57stLUHx",
            "https://drive.google.com/uc?export=view&id=1KFDlzBDsntWL9dqfl9Cposyni6OEmOma",
            "https://drive.google.com/uc?export=view&id=1zQ0fy1w5o3Irn9bg-pEY1kowDNYgavqp",  
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
                "kesan": "Bang Bintang kalem, tapi keren",
                "pesan": "Semoga bisa menjadi twinkle bagi orang sekitar ya bang! Tetap semnangat dan jaga kesehatan!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kak Nadya ramah bangettttt!",
                "pesan": "Jaga kesehatan dan jangan lupa berterima kasih ke diri sendiri ya kak! Please dengerin lagu Always-Rex Orange County kakk!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah lucuuuu!",
                "pesan": "Nanti kita cari spot buat bengong bareng yukkkk kakkkk!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Lia chill banget dan suka tidur di waktu yang pas!",
                "pesan": "Saya juga hobi tidur kak, yang ngejekin hobi kitaa, sini saya yang majuuu!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
    
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1icWGkiyOVRHoGx1JgyAWsDCCnHQdBUkw",
            "https://drive.google.com/uc?export=view&id=1s2lku2ZVm65W9ouCNhwaa95ILs6Exc5x",
            "https://drive.google.com/uc?export=view&id=1gAcOm9JSr8ERY9qDyGxZcHlvAk0bDq50",
            "https://drive.google.com/uc?export=view&id=11gUWrTxhwlFYAYda-Zni9qE53FNgw--Y",
            "https://drive.google.com/uc?export=view&id=1uX1sJy7rTcftamGxDssDFQRafnO-zJ-W",
            "https://drive.google.com/uc?export=view&id=1GRx0LmmKYTvn2XH_4dwFQaLCH20KFe1m",
            "https://drive.google.com/uc?export=view&id=1NaXAmbqWN73M_ZUfGYRVjRfGNW2Dhq4x",
            "https://drive.google.com/uc?export=view&id=11OeHJillCHKSFIPNbgIkp5djlHYIdrXY",
            "https://drive.google.com/uc?export=view&id=1Vn-F14ps53fLPbU_e4oQorwW0QAR9qv1",
            "https://drive.google.com/uc?export=view&id=12lPfH0vRv_UxD_HsVd3FrjaPFMXu-X3m",
            "https://drive.google.com/uc?export=view&id=1fQbyZNvUfhGDaHms5YTSqij8xhrxcAiG",
            "https://drive.google.com/uc?export=view&id=1NcakgPmMKMXt4B32JEDAd073v7ODtCnm",
            "https://drive.google.com/uc?export=view&id=1veKbPsIal0vjVwgwKdf651WyrEMwYi9_",
            "https://drive.google.com/uc?export=view&id=12HndZ3opvA0MxmTmXTluQpG2tLOQ-4E5",
            "https://drive.google.com/uc?export=view&id=1PxBstO4aN9cd_L4_zvwFbZ9scL_kpDj1",
            "https://drive.google.com/uc?export=view&id=18yDi_hOkVVHdtlCC6W10MTeWDTkmfJ50",
            "https://drive.google.com/uc?export=view&id=10A9ospzruUO1hT_hjFX-nn11IuftDni0",
            "https://drive.google.com/uc?export=view&id=1RvoY8mnW9nQtpNNF4GcaGaOIml4K8Idr",
            "https://drive.google.com/uc?export=view&id=1Jm1efxxirXajkwAIWMcUsTLiqBC6sUtJ",
            "https://drive.google.com/uc?export=view&id=1_Fn070CYQSAspHO2I69PNoENT3u5ePtj",
            "https://drive.google.com/uc?export=view&id=1ka9l1vCqICOIEeUWpNlxK5FqMEQ7raJV",
            "https://drive.google.com/uc?export=view&id=1c2VWKBiY3I3ch8FCSqnY5CrolAdFDuUN",
            "https://drive.google.com/uc?export=view&id=1pJ6MLV75iEPO0dLfVEzhmHKOuxFqve3v",
            "https://drive.google.com/uc?export=view&id=1qEbaf9cXcMdR2TsEtZK20vmsVnJxdvxs",
            "https://drive.google.com/uc?export=view&id=11-vaxG7tPMf3aDGG_Ya4gFwXr2dGnKUL",
            "https://drive.google.com/uc?export=view&id=1XwjPqelNky3clcI8gMQO4MPWcFCuNEhz",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya asik banget",  
                "pesan": "semangat kuliahnya"
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Ngekader 24",
                "sosmed": "@Allyapasha_",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Tangerang selatan",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "5 km dari pantai kedu",
                "alamat": "deket kost bang dapa",
                "hobbi": "cari kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "rahim ibu",
                "alamat": "samping kost arienta",
                "hobbi": "jahilin yulia",
                "sosmed": "@daffahdynn_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "19",
                "asal": "lubuk linggau",
                "alamat": "kost putri gerbang barat",
                "hobbi": "ngitungin duit",
                "sosmed": "@natasyaamavisca",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Samping kost kak alya",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma family",
                "hobbi": "ngasprak",
                "sosmed": "@j_gumel_17",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Vany salsabila putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "airan raya",
                "hobbi": "ngoding di macbook",
                "sosmed": "@vany.salsabila",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "1224450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Sukarame",
                "hobbi": "Main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@farazka",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@risma.mustika_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi": "Main Video Game",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "-",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerjain Tugas",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi pita pink",
                "sosmed": "@d_aniar",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Gangguin Kak Dea",
                "sosmed": "@ihsan.yusuf",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Ngomongin Kak Dea",
                "sosmed": "@kevinaja",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dia_natzzyaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nyuruh Kak Dea diam",
                "sosmed": "@m.ridwan_22",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "jl. Raden saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Ibu Kota Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Cari GPT",
                "sosmed": "@rewinanaaa",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()
    
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zH6ORz9jpI92J8-kC5i_zgbsHkeINmXf",
            "https://drive.google.com/uc?export=view&id=1uSh_X4BKTsbLOv4dxoW4kSKTtWCUVbNp",
            "https://drive.google.com/uc?export=view&id=1ru3Oc6KoLrWbqo5dz04QoEVQf5KzAhkX",
            "https://drive.google.com/uc?export=view&id=1o-jMlSPBS02pId3hp-IccHQAH7LXLuXN",
            "https://drive.google.com/uc?export=view&id=1dPiCYSUmSN7y4Iz74F4NQWZCAq34Vaze",
            "https://drive.google.com/uc?export=view&id=1z2-o4s8go8oK93ARlmexUZocfWaMbR75",
            "https://drive.google.com/uc?export=view&id=1ebboe4UbvkgHkNjQDD0c2z0KpYPFwSv-",
            "https://drive.google.com/uc?export=view&id=1WW05BCyLvQMgmV82pUtPgFhJojM7yR0U",
            "https://drive.google.com/uc?export=view&id=1P2C7skgizXkBpBkYykD5dKzrczNAt9M6",
            "https://drive.google.com/uc?export=view&id=1ciQwu3DlDtP4azwoxdBlY6RagqSB4hx2",
            "https://drive.google.com/uc?export=view&id=1KGzV7NeSBi648zuK5cft3zAa78KIIgJy",
            "https://drive.google.com/uc?export=view&id=1xlKOYA2Kno_zw5L01RX1e_LRA2StLOb2",
            "https://drive.google.com/uc?export=view&id=12saRGTEWu3p_JSyGTpIYVodIZPj7Jvqk",
            "https://drive.google.com/uc?export=view&id=1ILCndFF0-SqsJGBzO6y2NoBGVkaCNcSR",
            "https://drive.google.com/uc?export=view&id=1B25KYImnF3G0DWwT4PkcCvx4-JhBdIwI",
            "https://drive.google.com/uc?export=view&id=1tNeK0HgI6-lton2vYd0jf3AO-pe092Rn",
            "https://drive.google.com/uc?export=view&id=1ekrbWCqEWQfz9Ez4iyPLqJVeIQuwp5lA",
            "https://drive.google.com/uc?export=view&id=1fTi0YGdAp6as_qd89iRpDxbpKo_rw4EN",
            "https://drive.google.com/uc?export=view&id=1tmZBJjiu8FZAM95er7rvJISdpgrP2i73",
            "https://drive.google.com/uc?export=view&id=1HLnm7Iv9tKcoU44cOSy49o43gzRy_GHg",
            "https://drive.google.com/uc?export=view&id=1gkWpB-3745qSu2lpmfy6X7PHSpbg9DAc",
            "https://drive.google.com/uc?export=view&id=1NcAhTcTrgcCPm-r-w6L47TahYIbpJxV9",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": " 123450024",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "JL. Gajah Mada, Tanjungkarang",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450022",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "",  
                "pesan":""# 1
            },

        
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_p4eNhoRLMVvDTcklAMsEQpMJViYh6dw",
            "https://drive.google.com/uc?export=view&id=1E4oYdF6R1oMC_6OLfQeXDyP_G1drn8M8",
            "https://drive.google.com/uc?export=view&id=1S1nb1d6ZZQObKmZ7zwmXhysTzJGfLw7-",
            "https://drive.google.com/uc?export=view&id=1O4Zn-xmN2wgqEuDi5QKQ4Qz4kEU9aGN-",
            "https://drive.google.com/uc?export=view&id=1DRHoFsMZfHlw1RnKDiR6WHC5PhhcwuEi",
            "https://drive.google.com/uc?export=view&id=1IxWk54b7A-4qmkyDY5RyD5lwbquYVc-p",
            "https://drive.google.com/uc?export=view&id=1sydBvy9iLKAtN0veBwF_P991McNKXJH_",
            "https://drive.google.com/uc?export=view&id=14Of23q1OL9hQ5vmIsQMzmn9I0Nq_Ozdw",
            "https://drive.google.com/uc?export=view&id=1oLOMeLiXpHCGZPp8-AinskDPMdEmYyJu",
            "https://drive.google.com/uc?export=view&id=1DwCy3-WLywhEKMPlzzmnr1NGLbn8vqyj",
            "https://drive.google.com/uc?export=view&id=1zny8Ixe-Qg0Wq9ihHx_KtUBKc5vTFyuv",
            "https://drive.google.com/uc?export=view&id=1JVZahatVdZJJaqej1u1TPLbYrzNIsJrM",
            "https://drive.google.com/uc?export=view&id=1Ct27QT4NJhy2-0bLZ9ktX0aK1KNeekHd",
            "https://drive.google.com/uc?export=view&id=1ICoxBcCXfM7he3BFyB6ptRBcqZz-0FIm",
            "https://drive.google.com/uc?export=view&id=1n7nd8903kITLoLmBQcvzvjRZNxUPJJPn",
            "https://drive.google.com/uc?export=view&id=1sErfqoeFCO4eVOs4h3bP_nupbsEx425R",
            "https://drive.google.com/uc?export=view&id=1IxWk54b7A-4qmkyDY5RyD5lwbquYVc-p",
            "https://drive.google.com/uc?export=view&id=1j6i6-ve6poD0Dm140aR6fVfbOu-_PR7B",
            "https://drive.google.com/uc?export=view&id=14vx9W2CwSxEnGUdq87AaSxu89WxgXMZq",
            "https://drive.google.com/uc?export=view&id=1bbckYrt72CnNfZxggP9tMadntvaGnW5w",
            "https://drive.google.com/uc?export=view&id=1afBPQa62irDnGqmuNWxQfIL09jx4oPqo",
            "https://drive.google.com/uc?export=view&id=1E479jTcVXhkGtpMkYT25xx-l45jQySgz",
            "https://drive.google.com/uc?export=view&id=1sFy40VVOuG7ZDFLCGnnvC7rLtCAkPv3d",
            "https://drive.google.com/uc?export=view&id=14ejKelku2d6LLc_MtJS-3EV679ELtFKu",
           
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
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": " ",
                "pesan":" "
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": " ",
                "pesan":" "
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": " ",
                "pesan":" "
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
    

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XjIW6-NrdlMTD9KTBFIkz-owoAkkt0Da",
            "https://drive.google.com/uc?export=view&id=1hMZ4qqvIf4SOXkQXMSkxe8xSsv_Lnkuj",
            "https://drive.google.com/uc?export=view&id=1iBKni-6SSNwGwrF039-EDMbxYri1NN6u",
            "https://drive.google.com/uc?export=view&id=1EoPxaD7LJ9nuJRjAAZqUG0TSlKk6CI50",
            "https://drive.google.com/uc?export=view&id=16dUQz8DsUW7JhmOV1Scx7QEDht4oRqq-",
            "https://drive.google.com/uc?export=view&id=165olgbs9RWu5fwnIBpe42qBqMMUgxuzc",
            "https://drive.google.com/uc?export=view&id=1S_7KgVXFIIZhGZGB8wi6aXrqA7DZHMCi",
            "https://drive.google.com/uc?export=view&id=1r7D5SH8uELL96PEDWFDlKvHQWsIA-Ghd",
            "https://drive.google.com/uc?export=view&id=1KqBS8FZ84_G6_T-oEeYN9A0QXWkB8bpc",
            "https://drive.google.com/uc?export=view&id=1wPeDBEr-3zLR98O4fqQQxijH-0mHv-iy",
            "https://drive.google.com/uc?export=view&id=1W9ClVBFCifrJH3amdR4VCmtuG3aZhItI",
            "https://drive.google.com/uc?export=view&id=1kFX-u6G0B9T4VJM_Eq7A9ls95N6PB1DY",
            "https://drive.google.com/uc?export=view&id=1-lsfxM4MvQdvht5Ij6_nkI9LliGTFRei",
            "https://drive.google.com/uc?export=view&id=1aBe5ICUAWHp_voPOxFiqdDISNZ_UJjhC",
            "https://drive.google.com/uc?export=view&id=1Ao0J9sxMWWsWVV0DI0MGkjlXTQ8qUOu1",
        
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": " ",
                "pesan": "  "
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azza.rrr_",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "18",
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": " ",
                "pesan": " "
            },
             {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "@iqfinahalikaa_",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": " ",
                "pesan": " "
            },
             {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan":  "",
                "pesan": " "
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwsti",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": " ",  
                "pesan":" "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
    
if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AK4ipkdWLEm7LRQwguPLUyNUpXZFpyzt",
            "https://drive.google.com/uc?export=view&id=1-qkV-Hh8EEmpzcMAdpeUP0mpmK48O4Oh",
            "https://drive.google.com/uc?export=view&id=1gX9cFQIi0hrptwq1ZRSgeLm8RtVPf-PC",
            "https://drive.google.com/uc?export=view&id=1gRBmnER5Ktpi73udaZXqBzfViFKNBh3x",
            "https://drive.google.com/uc?export=view&id=1c6ruao22f5ILC6GEjxNe66EMLv35Yf37",
            "https://drive.google.com/uc?export=view&id=1z1ogaZjVpdceq9JactkwtkPLAL-rQ6wW",
            "https://drive.google.com/uc?export=view&id=11qWBy8EnvsvY1e00zFwzdjQlA3Sp371-",
            "https://drive.google.com/uc?export=view&id=1zwgUldiR13RoKwixEi1o2P0WY5Ey3KNc",
            "https://drive.google.com/uc?export=view&id=1hI4jMicJhILH3vBDeEy4t9LcCNQMidfD",
            "https://drive.google.com/uc?export=view&id=1UxNfpIEaOm6z-GwQBGQc5QQWr40e_d3G",
            "https://drive.google.com/uc?export=view&id=1qhLUiml2LSWAjWCEox0Lz5y0ZsCE7GTR",
         
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
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": " ",
                "pesan": ""
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "",
                "pesan": " "
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": " ",
                "pesan": " "
            }
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
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jati Mulyo",
                "hobbi": "sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmanellyana",
                "kesan": " ",
                "pesan": " "
            },
             {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": " ",
                "pesan": " "
            },
            {
            
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "lucuuuu",
                "pesan": " "
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lmapung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "kotabumi, Lampung Utara",
                "alamat": "jl.pangeran senopati raya",
                "hobbi": "main gitar",
                "sosmed": "@aliyaamara",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "mendengarkan musik",
                "sosmed": "@donamaya.p",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "",
                "pesan": " "
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": " ",
                "pesan": " "
            },
             {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh , Sumbar",
                "alamat": "jl.Lapas, kec.Jati Agung",
                "hobbi": "mendengarkan musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": " ",
                "pesan": " "
            },
             {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "",
                "pesan": ""
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "membaca, menulis, memasak",
                "sosmed": "@nltg._",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": " ",
                "pesan": ""
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": " ",
                "pesan": " "
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": " ",
                "pesan": ""
            },
           
           
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
    

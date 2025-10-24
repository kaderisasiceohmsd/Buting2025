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
    






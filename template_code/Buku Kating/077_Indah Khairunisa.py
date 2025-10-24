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
            "https://drive.google.com/uc?export=view&id=1RADX3YweO96EwsFP7jIv0Wf2f5KAdLOr",
            "https://drive.google.com/uc?export=view&id=1Oe0C-Jq_qoxBmrRqL-M1bE1EQARhzprK",
            "https://drive.google.com/uc?export=view&id=1uxUvigYV_WuwUuFtPRbCTnnDGEHB7DUP",
            "https://drive.google.com/uc?export=view&id=1PcTWTSx5siMTie24EsiR6IVL9-FGxfiB",
            "https://drive.google.com/uc?export=view&id=183mDRcmxpQSpheICWkTLVaFw3UdNJ2fI",
            "https://drive.google.com/uc?export=view&id=1FoLncpQTwPBB-OHWyVZPwPQq6pXZMIaT",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli Donat Kentang",
                "sosmed": "@_erendraa",
                "kesan": "bang rendra paas awal liat orang nya keliatan banget asiknya, baik juga, keren parahh",  
                "pesan":"semoga kedepannya tetep jadi diri sendiri yang segacor ini, sukses dan semangat terus ya bang!!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang jo juga keren banget, pas awal liat itu pas riuh, gacor bangettt",  
                "pesan":"semoga kedepannya bisa jadi yang lebih aik dari yang sekarang, sukses dan semangat terus bangg!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simajuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy Dalem",
                "alamat": "Ayres Kost",
                "hobbi": "Makan Kuaci",
                "sosmed": "@celisabethh_",
                "kesan": "kak abeth lucuuuuu bangettt, dia vibes nya ceria banget, pas ngobrol waktu wawancara juga asik banget, sesama leo ini emang gacor banget",  
                "pesan":"semoga tetep ceria kayak gitu ya kakk, apapun masalahnya senyum adalah solusinya, semangatttt kakkk!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kak puspa baikk banget, kalem yaaa pas ketemu, suka pas kakaknya ngomong tuh lembut banget",  
                "pesan":"semoga di hari hari selanjutnya kakak masi bisa jadi diri sendiri, tetap senyum walau tugas datang terus, semangattt terus kakk!!"# 1
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Komenin tiktok cewek cantik",
                "sosmed": "@eksantyferiana",
                "kesan": "kak eksanty baikk banget, vibesnya itu aku suka banget, apalagi pas pemaparan materi itu",  
                "pesan":"semoga kakak di kedepannya tetap menjadi diri kakak yang seperti ini, senyum terus ya kak, senyum kakak tuh manis soalnya hehe!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Gya Kost Korpri",
                "hobbi": "Cute jendral",
                "sosmed": "@farahanumafifahh",
                "kesan": "kak hanum baikkk banget cuy, asik polll, aku suka ni sama yang vbesnya kayak gini, seruuu banget",  
                "pesan":"semoga tetep tersnyum walau dibantai tugas, kepanitian dan lainnya, tetep seangat dan sukses selalu kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JGSwIux900bzEWMedEGclvh8EabiMEln", #Jeremia
            "https://drive.google.com/uc?export=view&id=1VAiJ6d9lg9NiseWOOO94D2KRSWTmlGHF", #dhea
            "https://drive.google.com/uc?export=view&id=1JQT2l_QdTltmVSIk8041D08cOwo6BH5X", #Renisha
            "https://drive.google.com/uc?export=view&id=1rNdxOOs1LP_LnNRV6E1hAgv144NeX364", #Anisa
            "https://drive.google.com/uc?export=view&id=1nzeBEknz0rqaIVujEjEq4-CTtcHZLnUw", #Dharu
            "https://drive.google.com/uc?export=view&id=1GhRSA_h5BF-dlpSJY1rcRcHjFkSbpcTR", #Febi
            "https://drive.google.com/uc?export=view&id=1uwGNsGeOAKZOj3PlCuKtQ_8YoTzp18ZX", #Givaro
            "https://drive.google.com/uc?export=view&id=1gqbEOOzMQp5_Mzwmikx0w_3b1G-0jr6T", #Mirzan
            "https://drive.google.com/uc?export=view&id=1lMIqrlwEi7G-Y_IlITd_a-rVp3bP_9FD", #Berliana
            "https://drive.google.com/uc?export=view&id=1EbDKmhLa_IVWFQioWnhudgMR6OrSUb7d", #Juesi
            "https://drive.google.com/uc?export=view&id=1I6_4pfQjvMDKXrSpjju9py5Z3jYqEXnc", #Ridho
            "https://drive.google.com/uc?export=view&id=1CwIDZMm3moN3ALP9_KCkpT42XbSqIua2", #Feriyadi
            "https://drive.google.com/uc?export=view&id=1tENlh6xjRORBkcVqO0bDndo_xiDTBqkE", #Monica
            "https://drive.google.com/uc?export=view&id=1LMZZBUBmO8ReHeSCGrH45l5M782GZihD", #Wan Naswa   

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
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "lomba ga makan keerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "",  
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
                "pesan":"Semoga selalu dilancarkan kegiatannya"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "abangnya cool dan berwibawa.",  
                "pesan":"Semoga makin sukses,bang!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya humble",  
                "pesan":"Semoga selalu dilancarkan kegiatannya!"# 1
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
                "pesan":"semoga makin berkembang ke depannya"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "abangnya punya pembawaan yang tenang.",  
                "pesan":"Semoga selalu diberi kemudahan dan kebahagiaan"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya punya semangat positif yang keren",  
                "pesan":"Semoga selalu semangat dan penuh keberkahan"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya tenang dan menyenangkan",  
                "pesan":"Semoga terus berkembang dan berprestasi"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Mainn paddle",
                "sosmed": "@iamridhomanik",
                "kesan": "abangnya punya semangat positif yang keren",  
                "pesan":"Semoga selalu semangat dan penuh keberkahan"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi batch google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya terlihat tegas dan berkomitmen",  
                "pesan":"Semoga selalu bahagia dan sukses ke depannya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya punya semangat positif yang keren",  
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
                "kesan": "Kakaknya tenang dan menyenangkan",  
                "pesan":"Semoga terus berkembang dan berprestasi"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mdWfkZYEv9pKDJrNV8JBjkP5YlX6NdRQ", #Bintang
            "https://drive.google.com/uc?export=view&id=1ONOur7fziMw8CT3z4yBoKZgkLPCOhV6W", #Nadya
            "https://drive.google.com/uc?export=view&id=1Chp6zIr7BYdhe8-nndoaq7sm4NNCCEGG", #Azizah
            "https://drive.google.com/uc?export=view&id=1tQ_Pugo1_372TsnSHKxT0O8_ex2hbiLo", #Hana
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
                "kesan": "Kaget ternyata suara bang rendra persis kaya juicy luicy waktu FG",  
                "pesan":"Semoga semakin keren kedepannya bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Awal liat bang Jo kaya serem",  
                "pesan":"Sukses terus kedepannya bang"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main ice skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "Seru banget kak abet lucuu!",  
                "pesan":"Makasih udah jadi orang lucu kak!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomart Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya keliatan kalem tapi anggun banget!",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
        
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1D87dWJw9VhT38uFSzKOgUetaxAysVOJy",
            "https://drive.google.com/uc?export=view&id=1ZHOZvKqua23SqQd7gwUkGosnlzoqHVQS",
            "https://drive.google.com/uc?export=view&id=1pJGfHMm-UEBpmkne6z2Ed291rueYo5ag",
            "https://drive.google.com/uc?export=view&id=116lZ3ER4Zy2Ia6aXofyEnrkltIkhBl5l",
            "https://drive.google.com/uc?export=view&id=1Fhdv6YKODsHCILzKv68xydg8CHEM8Zix",
            "https://drive.google.com/uc?export=view&id=1_p0aIFYR6FfKaeeAJFXjin7M0ag6QplB",
            "https://drive.google.com/uc?export=view&id=1mAOE7GgvfhCnPpj2daQobBzRA0ojcQJl",
            "https://drive.google.com/uc?export=view&id=1kDJ0mfVi4evKXccvoBJSc4aJ2HsuUUH8",
            "https://drive.google.com/uc?export=view&id=1-RVjJiJt-5F-hob1x9ec9_sFcdTuHDt8",
            "https://drive.google.com/uc?export=view&id=1LQeke16OsQrMKTm5Ze9WP3HQ1trDa5bK",
            "https://drive.google.com/uc?export=view&id=1YXNSfydCeLVAPMZTPkgNiIN369YsexZP",
            "https://drive.google.com/uc?export=view&id=12YIShGMBFrqQGs1cZoB4vDRo2KujSxma",
            "https://drive.google.com/uc?export=view&id=14ILN2Y--Z8l3g8ktFQSzhcYhQrbVrfSb",
            "https://drive.google.com/uc?export=view&id=1V_r9bGwk5wryPBZ8XI0ALImFT_PIobE4",
            "https://drive.google.com/uc?export=view&id=1FBTK3aXH4F5uPxjR5RotximjcMjWFneu",
            "https://drive.google.com/uc?export=view&id=1GFpI3Uj0-9HiU7I9QAo3dMKb1OWmzmnt",
            "https://drive.google.com/uc?export=view&id=1TgYCgFHkT71UpZ3ZoMoWy8KM43KnnQoG",
            "https://drive.google.com/uc?export=view&id=16A2Rwjw99PRDwDt17zcegvJaJ2BJW55M",
            "https://drive.google.com/uc?export=view&id=11cxsbf5PY2XyzYINcQ1h_jgROLCo0zN0",
            "https://drive.google.com/uc?export=view&id=17acpksE0g7mm43QjLkr3fMmNuIbHYwvE",
            "https://drive.google.com/uc?export=view&id=1PFVhWDLY6ZIl598-CHs5UUas0YcchcwK",
            "https://drive.google.com/uc?export=view&id=1Ak_nND7KH4WzcrWVDsmnh7lq1b5981z3",
            "https://drive.google.com/uc?export=view&id=161yIBR-vveLXLcNBjMzNYTrTdLNtPY7M",
            "https://drive.google.com/uc?export=view&id=1EzyaymeKce3SBW8Iw9Pw4O0WwnFksuHa",
            "https://drive.google.com/uc?export=view&id=1dj5UNspA0rVxMwkvSuxltRie-1v_bb_y",
            "https://drive.google.com/uc?export=view&id=1XB9-1jh_BBN3O9iwFvAvlV73lNca4Z6N",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "bang ferdy berwibawa tapi tetap asik diajak ngobrol",  
                "pesan":"semoga terus jadi contoh baik buat banyak orang!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak fifah selalu positif dalam hal apa pun.",  
                "pesan":"tetep jadi orang baik ya kak"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "kak allya baik banget, dari awal aku ketemu pas pplk karena dia daplok ku, dia suka banget kasih kita motivasi biar kita th ngerti apa yang harus dan ngga harus kita lakuin",  
                "pesan":"semangat dan jangan sampe bosen ya kak untuk selalu ingetin kita, dan jangan lupa istirahat"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Kontrakan GH",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "bang ahmad asik, baik juga, bijak juga dalam berpikir",  
                "pesan":"terus kasih energi percaya diri nya ke kami ya bang, semangat terus banggg"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Kost Orange",
                "hobbi": "Ngekader",
                "sosmed": "@arientakhsnl_",
                "kesan": "kak arienta baik, pembawaannya tegas",  
                "pesan":"tetep jadi kakak yang sekarang yaa, semoga sehat terus yaa kak untuk bisa nasehati kami hehe"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "",
                "sosmed": "@daffahdynn_",
                "kesan": "ang daffa keren, suka banget liat rambutnyaa, gemoyy",  
                "pesan":"semoga bang daffa bisa tetep semangat ngejalanin harinyaa, sukses teruss bang"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game",
                "sosmed": "@ginda_mrp",
                "kesan": "bang fajar baikk, perhatian juga ke kami",  
                "pesan":"semoga bang fajar tetep semangat dan jangan sampai redup yaa"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kostan putri gerbang barat sebelah sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "kak natasya pinter, baik, tegas jugaa",  
                "pesan":"semoga positive vibe nya ngga ilang yaa kak!"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "bang nobel ini kocak, baik juga",  
                "pesan":"semoga semangat itu terus menyala sampai sukses"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Fam",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "bang aji disiplin banget soal waktu, aura nya positif banget",  
                "pesan":"semoga semangat nya ngga abis terus"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kak vany tuh kalem, tapi tegas",  
                "pesan":"tetap jadi pribadi yang menyenangkan"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22__",
                "kesan": "bang sahid semangat banget walau sibuk",  
                "pesan":"jangan lupa jaga kesehatannya bang, semangatt"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung,Lampung Timur",
                "alamat": "nangka 4",
                "hobbi": "main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "bang paris lucu, kalem",  
                "pesan":"semoga aura positifnya nular ke semua orang ya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "kak razka asik, baik, ternyata ngga se kalem itu",  
                "pesan":"semangatt yaa kak, kalau ketemu sama aku jangan bosen ya"# 1
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450079",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kak kharisma baik, kalem",  
                "pesan":"semoga semangat nya selalu membara dan menginspirasi ya kakk"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kakaknya baik, asik juga",  
                "pesan":"tetap jadi pribadi yang baik yaa kak kedepannya"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jalan Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "bang sahid yang ini juga baik, asik kalau diajak ngobrol",  
                "pesan":"semoga kedepannya tetep jadi pribadi yang asik ya bang"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Jl. Korpri Raya",
                "hobbi": "nontonin anak tari latihan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "bang daffa humble, seru juga ",  
                "pesan":"semoga tetep jadi orang yang menyenagkan dimanapun"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas raya No. 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "kak daniar baik, kalem sii pas ketemu",  
                "pesan":"terus berkarya kak, semangatttt"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Joki strava",
                "sosmed": "@ihsan.myusus",
                "kesan": "bang ihsan kocakk, lucu juga",  
                "pesan":"semoga tetep adi sosok yang asik kayak sekarag, semangat bangg"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "PanjanG selatan",
                "hobbi": "terjun payung",
                "sosmed": "@kevinaj__",
                "kesan": "bang kevin tuh pendiem, baik",  
                "pesan":"terus aktif dan produtif ya bang, biar makin sukses"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kak lidia baik, kalem",  
                "pesan":"tetap menjadi pribadi yang baik ya kak, semangatt!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung tengah",
                "alamat": "Belwis",
                "hobbi": "nonton anak tari perform",
                "sosmed": "@m.ridwan_22",
                "kesan": "bang ridwan baik, kocak",  
                "pesan":"jangan berhenti belajar, dunia butuh orang kayak abang"# 1
            },
            {
                "nama": " Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "jl. Raden Saleh",
                "hobbi": "ngerjain soal matematika",
                "sosmed": "@liano.wlm",
                "kesan": "bang liano baik, tegas juga, asik sihh",  
                "pesan":"semoga bisa tetep sabar ya dalam menghadapi kamii, semangatt ya bang"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera utara",
                "alamat": "Belwiss",
                "hobbi": "main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "bang benget kocak, baikkk",  
                "pesan":"semoga tetep semangat walau dunia sdg tidak baik baik saja hehe, sukses selaluu bang"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Ratu, Bandar Lampung",
                "hobbi": "nonton anime",
                "sosmed": "@rewinanaa",
                "kesan": "kak rewina kalem sih menurutku, baik juga",  
                "pesan":"semoga semangat dalam diri nya semakin menyala ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
    
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1C9WsTGhAfYnDusxHcYt1MxE41VW2NZwJ",
            "https://drive.google.com/uc?export=view&id=1mzREnXFmyAoLFN7q6CPv4nL3YhzblXO5",
            "https://drive.google.com/uc?export=view&id=13EbkT8i7cpULvMaEOi3_WmxyXkOaxtSA",
            "https://drive.google.com/uc?export=view&id=1RHyhFup6igH9Fpyoh4m3kNj2q2q7AjiM",
            "https://drive.google.com/uc?export=view&id=1kCygmDsuHEGE9X7u6xnnNX9oih0j-iEs",
            "https://drive.google.com/uc?export=view&id=1N7M3cbUhVTnfLxnACFVXbi4-oGI5zlKP",
            "https://drive.google.com/uc?export=view&id=1pxYFvnPceFvFdi-RQ0_5HzcIb7sDZ_ZB",
            "https://drive.google.com/uc?export=view&id=1_OtiOqDhBFP3sPYfIBGMb7_O0taitW8H",
            "https://drive.google.com/uc?export=view&id=1hWBUsGTv_a6ir4snokzv9o6jbr7iCrM-",
            "https://drive.google.com/uc?export=view&id=1EirKFgsJyFtacmS6AlM96nw4kXZXwFo9",
            "https://drive.google.com/uc?export=view&id=1mIUdxny6DLoKVjNPx-TmM_MT2IiOzm1e",
            "https://drive.google.com/uc?export=view&id=17heJHa7Bi8IIGutMJdyiaZV5ZZyqqPGE",
            "https://drive.google.com/uc?export=view&id=1s5pO4tsCQMx6G7l6qwLVsA97ntHlXmIS",
            "https://drive.google.com/uc?export=view&id=14aU_PrrqlWvVhIYNQ3slBBQlXbnyb9Mm",
            "https://drive.google.com/uc?export=view&id=1-lzPmNOSnSL8JNZutGpRUtROt3OQpukQ",
            "https://drive.google.com/uc?export=view&id=15ft2Gn_esf5erXcWhJeGjSqMNaW8XT5c",
            "https://drive.google.com/uc?export=view&id=1ffnfsTkRhOjYes6GnEnrFXjBCgXaHegr",
            "https://drive.google.com/uc?export=view&id=1yk1CecAsaUQ_K6pA_6IeD-L0GYAcaU7b",
            "https://drive.google.com/uc?export=view&id=1dx_nVzA_oE2T31LY9lB7NJmhHVHF0S80",
            "https://drive.google.com/uc?export=view&id=1qfyphj-Y9rVvQzam-oRT545BQlTtgj4T",
            "https://drive.google.com/uc?export=view&id=1q0v8XO16JyRUnZOHhmEnO1DRm4Nq6J1Z",
            "https://drive.google.com/uc?export=view&id=1djGa0tu24z25In8XQCguNYG0Yh9xTQMv",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang,Baten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berenang",
                "sosmed": "@randaandriana_",
                "kesan": "bang randa baikk, ramah terus lucu jugaa",  
                "pesan":"Semoga selalu semangat dan sukses terus ya bang", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak orangnya asik dan baik",  
                "pesan":"Semoga tetep jadi pribadi yang lebih baik dari ini yaa kak!", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya pintar, tutur kata nya lembut juga",  
                "pesan":"semoga abang terus jadi pribadi yang positif terus yaa bang", # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. lapas,Belwis",
                "hobbi": "maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya baik dan kalem banget",  
                "pesan":"terus semangat dan jangan lupa jaga kesehatan ya kak", # 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "bang fadil baik, pinter",  
                "pesan":"semoga pribadi yang tenag dari abang nya bisa menular ke kami", # 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "bang aqil baik, tenang tapi tegas, tapi kocak juga kadang",  
                "pesan":"Semoga semangat dari abangnya tetep membara sampai akhir nanti ya bang", # 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "abangnya asik dan baikk!",  
                "pesan":"Semangat terus yaaa, sukses selalu juga bang!", # 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kak Nadia keliatan kalem da enak diajak ngobrol",  
                "pesan":"semoga hidup nya penuh dengan motivasi yaa", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Marleta asik dan lucuuuu",  
                "pesan":"Semoga sukses dan sehat sealu ya kakk", # 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234500119",
                "umur": "20",
                "asal":"Pramuka, Bandar Lampung",
                "alamat": "Perum Bukit Alam Permai 3, Blokk C, No.9",
                "hobbi": "Dengrin musik",
                "sosmed": "@keyashafi_",
                "kesan": "bang keya baik, tenang gitu lohh aura nya",  
                "pesan":"semangat dan tetep jadi pribadi yang tulus ya bangg", # 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bummisari Kec.Natar",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kak Anggi baik banget, lucu jugaa",  
                "pesan":"Semoga makin semangat dan sukses selalu yaaaaaa", # 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Sale, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi baik, tenang terus lumayan kocak",  
                "pesan":"Semoga tetep jadi orang baik, makasi juga udah sabar ngajarin kita lmd kak", # 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kak Olla kalem banget, lumayan pendiem yaa",  
                "pesan":"semoga kakaknya bisa lebih ceria lagii dan semangatt terus ya kak", # 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kak Fairuz santai tapi asik juga",  
                "pesan":"semangat nya menyala lagi ya kak, jangan lupa untuk jaga kesehatan", # 1
            },
             {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "kak tanty lucuu banget, ceria jugaa",  
                "pesan":"Semoga selalu semanngat dan ceria kayk gini ya kakk", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "Bang Eggi asik dan baikk",  
                "pesan":"semangat terus dan sukses selalu ya bang", # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang (main game)",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah seru dan humble juga",  
                "pesan":"semoga tetap bahagia dan suksess teruusss", # 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer),tidur,jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "Bang Fabio asik, baik, humble juga",  
                "pesan":"semoga kedepannya bisa jadi pribadi yang lebih dari ini dan semangat terus bang", # 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@giofaniars_",
                "kesan": "Bang Gio orangnya baik terus tenang banget pembawaannya",  
                "pesan":"Terus semangat dan jaga kesehatan ya bang", # 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kak Rahma kalem, menyenangkan juga",  
                "pesan":"terus berkembang yaaa kak, semangattt kaks!", # 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "Kak Rahmah humble dan easy going",  
                "pesan":"tetap rendah hati yaaaps, dan tetep jadi sosok yang menyenangkan", # 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans Sakum,Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "Bang Razin orangnya kalem dan tenangg",  
                "pesan":"Semangan dan sukses terus ya bang", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1R5a80jOMfGqbPVmtQZKk9o86n9K7jFjp",
            "https://drive.google.com/uc?export=view&id=19ioqkr06y1PotU2RocisiK7ISgpszSMr",
            "https://drive.google.com/uc?export=view&id=1X2BoyFzX1bHogCOh8AfWgQ-ApFn7FaoO",
            "https://drive.google.com/uc?export=view&id=1a0XbKG563UplT6QsNMssWctQRspqrlLG",
            "https://drive.google.com/uc?export=view&id=1dDCcyU7YTeGHFlsYbPHP3KuijZSeJ3d5",
            "https://drive.google.com/uc?export=view&id=1PV6rHB3g_tc4w22iFMG2ojce6FeZs25W",
            "https://drive.google.com/uc?export=view&id=1Lh_RFpLJpOna_Aod4HPr6hTwNOB2NZVQ",
            "https://drive.google.com/uc?export=view&id=1trRc-XG0WQ_UU5HW_YxWkYMe1vG9pg20",
            "https://drive.google.com/uc?export=view&id=1So3jZpYuIp1ZNGcbKcGZ5lkFsBTcDrpw",
            "https://drive.google.com/uc?export=view&id=1rwxgZjVPYNp4RBcYYyPnMomqIrC7Gcfg",
            "https://drive.google.com/uc?export=view&id=1dDEPK0281jlyS-AjeC8mGc4Dwxk4Z7Bw",
            "https://drive.google.com/uc?export=view&id=1HXQGHUNaqVEUsdJkLIVhSu1Fdl4pkDQm",
            "https://drive.google.com/uc?export=view&id=1DaWv4ee19HvIuv42VIoFPOjM46GBTv5Y",
            "https://drive.google.com/uc?export=view&id=1bplbbqzpBcv9gIeZPhR9ihNNxP9Mpask",
            "https://drive.google.com/uc?export=view&id=1_hxyMF78JjbmLap7n2JdseQLO4MpDO_S",
            "https://drive.google.com/uc?export=view&id=1E268EDiaonxKnmys5LVxPFpm4VaabZtM",
            "https://drive.google.com/uc?export=view&id=1By4yVaZcZpxlzsVGK0eaJ8RYYzE68TJp",
            "https://drive.google.com/uc?export=view&id=1Ag4vX9i_i0GFdGEGJLNT1NGz7gNoPxVd",
            "https://drive.google.com/uc?export=view&id=18CunmQVWpCW2pIYyn1bmSLTC8eIsuaXk",
            "https://drive.google.com/uc?export=view&id=12XYl63BNT117HAFyGgv_anLzoci093ks",
            "https://drive.google.com/uc?export=view&id=1HUxHKXY1DqIXAxHOBxAmglCy3iI9uGX6",
            "https://drive.google.com/uc?export=view&id=1SgeDNLJm1927ni1tpBHC9G3wZoN3G5f5",
            "https://drive.google.com/uc?export=view&id=1jCXSKqRFQiyrAjj7IDeCSQt_jRlBMu_2",
            "https://drive.google.com/uc?export=view&id=1_RsDuGNT-9Ap2rzmb1rtsUOWHrCsgXqc",
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
                "kesan": "Bang Arafi baik, terus asik juga",  
                "pesan":"Semangat dan sukses terus ya bangg"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana kalem banget, baik juga",  
                "pesan":"Semangat terus kak"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya asik banget",  
                "pesan":"Semoga tetep semangat dan penuh senyum tiap harinya"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya baik dan tegas tpi lucuu",  
                "pesan":"sehat sehat ya kakk"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya baik banget",  
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
                "kesan": "Kak Khoirul asik banget",  
                "pesan":"semangat terus kakkk"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia gemes banget",  
                "pesan":"tetep jadi pribadi yang baik kayak sekarang ya kak, semangat"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla asik dan ramah banget",  
                "pesan":"semoga kebahagian selalu datang di kakak"# 1
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
                "pesan":"Semangat dan sukses terus bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea lucu, asik, baik banget, ih suka deh",  
                "pesan":"Semangat menjalani tiap semesternya dan sehat selalu kak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak cindy cantik banget, baik jugaa",  
                "pesan":"Bahagia terus kak dan sukses ya kak duta nyaa"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea ramah banget, baik, gemesinnnnn aw",  
                "pesan":"kak dea sabar sabar ya kalau ngajarin aku, makasii buat yang kemarin, sukses kak"# 1
            },
            {
                "nama": "Desman Velius Halaws",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman baik dan kocak banget",  
                "pesan":"Semangat kuliah nya dan jangan lupa untuk senyum"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya baik poll, terus pinter",  
                "pesan":"sukses terus ya kak, btw tips alpro kak"# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "heyy kak luluy, baik banget, ah lucu deh pengen di karungin biar ngga lari",  
                "pesan":"senyum itu penting dan satu lagi semoga yang disemogakan tersemogakan"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya keren dan baik banget",  
                "pesan":"Semangat dan sehat selalu bang"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "Abang santai dan baik banget, enak diajak ngobrol juga",  
                "pesan":"Semangat terus dan jangan lupa untuk tetep senyummm"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya baik banget, terus lucu juga",  
                "pesan":"Semangat kejer cita cita ya kak!!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Ilmi baik terus lucu, kocak juga",  
                "pesan":"semangat belajar kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melin cantik dan ramah banget",  
                "pesan":"semangat terus ya kak"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla baik banget, terus lucu juga",  
                "pesan":"Semangat dalam berkembang ya kak"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Semoga makin semangat dalam menjalani hari hari"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya kocak banget",  
                "pesan":"terus semangat dalam hal apapun"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kak tari baik dan bisa banget diajak seru seru an",  
                "pesan":"hehe kak kalo inget knit tetep inget kita bertiga yang duduk di barisan nomor 2 pas praktikum ads yaa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen Internal":
    def DepartemenInternal():
         gambar_urls = [
             "https://drive.google.com/uc?export=view&id=1Y8EWImFtQN0C_ZmSiRnmb-CPo6Wsxsb0",
             "https://drive.google.com/uc?export=view&id=1sVP5d5zspjFnxgFL7NaieECRqBQZGKsY",
             "https://drive.google.com/uc?export=view&id=1ZbTDR7Ayu5hvm-kZ5ResGvhts0skpaze",
             "https://drive.google.com/uc?export=view&id=1DjZead0CGDEJDkFwIOIG6sEPvHx-jZvW",
             "https://drive.google.com/uc?export=view&id=1i-TwZGpbQr14RhtMWHH9Ut6sf_YWSfmY",
             "https://drive.google.com/uc?export=view&id=1jyyO0MYmrIQx1USyq3wx0uKVx7ofr7uJ",
             "https://drive.google.com/uc?export=view&id=12088Q4r25pgEW_rywp8WHrZHmqLy9zs4",
             "https://drive.google.com/uc?export=view&id=1wGjndrMP8lmrjR2PiCDBlO_sX_nFZ7fM",
             "https://drive.google.com/uc?export=view&id=1c3pXFXP0QOznIhpDT3sIgKp_-Xb23dvN",
             "https://drive.google.com/uc?export=view&id=10trkmLw0qRwwear8sUOVxBnBKkXEX-8U",
             "https://drive.google.com/uc?export=view&id=1hqzojVs429bc-B32NHVnGQDjyxhWJicN",
             "https://drive.google.com/uc?export=view&id=1wuIkx9VgXDBDVj_rEdmE6kFlt2_QnQPx",
             "https://drive.google.com/uc?export=view&id=1kB3apxOIx8Rx1bU5ANmECf08sv2nYweH",
             "https://drive.google.com/uc?export=view&id=1e6YRRG5aiTDe-EHu0CtNu34CIL6hfsdZ",
             "https://drive.google.com/uc?export=view&id=1W4_vIfqjdi_Y9k-3JS7HIKtq8SaVX7Co",
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
                "kesan": "kak rani baik, terus keren jugaa",  
                "pesan":"Sukses dan sehat selalu ya kak"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "kakaknya baik banget",  
                "pesan":"Sehat sehat ya kak!"# 1
            },
            {
                "nama": "Salwa Farhanatusaiidah",
                "nim": "12245055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa kalem dan baik juga",  
                "pesan":"Semangat dan sehat terus ya kak"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azza.raaa_",
                "kesan": "Kakaknya baik banget",  
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
                "kesan": "bang haikal keliatan agak galak ternyata baik banget, asik juga",  
                "pesan":"semangat jalanin harinya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450076",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak iqfina baikkk poll",  
                "pesan":"Semoga selalu bahagia kak"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450009",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak may juga aku kira galak, ternyata baik, asik pula",  
                "pesan":"jangan lupa tersenyum ya kakkk"# 1
            },
            {
                "nama": "Muhammad Naufal Afghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@Muhammadnaufalafghani73",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Abangnya kocak banget",  
                "pesan":"Sukses terus bang"# 1
            },
             {
                "nama": "Rendi Alezander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@lexanderr",
                "kesan": "Abangnya baik dan lembut banget",  
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
                "kesan": "Kak Hanna ceria banget",  
                "pesan":"semangat jalanin hari nya sebagai anak data ya kak"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak keren tuh kayak namanya, keren bangettt",  
                "pesan":"semangat dan jangan lupa bersyukur hari ini"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hifzky",
                "kesan": "Abang Hanif seru banget",  
                "pesan":"Semoga sukses terus bang"# 1
            },
            {
                "nama": "Sarah wasti",
                "nim": "122450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah keliatan lembut dan kalem",  
                "pesan":"Semoga sehat selalu kak"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "Main Rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kakaknya lucu banget",  
                "pesan":"Semoga sukses kuliahnya"# 1
            },
        ]
         display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
    
elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1r5_lP_fkh7lpfk3HLnAiPWKxZl0MvyS_",
            "https://drive.google.com/uc?export=view&id=1MrT-BeYmD9Gb_eFLdHiiSh6ioVa7FaP4",
            "https://drive.google.com/uc?export=view&id=1NpRRMCijJF4OO3qg2Az7qlVxnyJGI--6",
            "https://drive.google.com/uc?export=view&id=1G9iE7x9gqHerQh2uBS3q6oZ-9uyEk89f",
            "https://drive.google.com/uc?export=view&id=10dDyxcLvy4pvWVEBTomuHNOXHrZZz1Nr",
            "https://drive.google.com/uc?export=view&id=1cW1-tuoyy6jypIxM0k7s2jYUiu7zK6Fg",
            "https://drive.google.com/uc?export=view&id=1oziyAjiabM-dknvitS14qC8MCivyuJ6c",
            "https://drive.google.com/uc?export=view&id=17Dn8e4Wds5NDBz_gYc81-istNue3edAu",
            "https://drive.google.com/uc?export=view&id=1pLFWA8wrDfzcILtjT0fiWyKxqlslSNsM",
            "https://drive.google.com/uc?export=view&id=1si_clyzA8805E9MW85wwc4PF4DHx2S3P",
            "https://drive.google.com/uc?export=view&id=1tJfXqB3fL2ox3tn_IjXZXF9Z9EXSMSJy",
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
                "kesan": "Bang Danang asik diajak ngobrol, baik juga",  
                "pesan":"semangat untuk kembangin karya nyaa yaa bang"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450012",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya baikk, lembut jugaa",  
                "pesan":"semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki_",
                "kesan": "katanya abang ini model? keren cuy",  
                "pesan":"sehat dan semangat ya bang"# 1
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
                "kesan": "Kakaknya baikk dan lucu",  
                "pesan":"Sukses terus kuliahnya kak"# 1
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
                "pesan":"Semoga makin sukses kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya kalem",  
                "pesan":"Tetap semangat bang"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya asik banget",  
                "pesan":"Semangat jalanin hari nya kak"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gang perwira 2",
                "hobbi": "Nontol alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakaknya baik dan kalem banget",  
                "pesan":"Sehat selalu kak"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak naya seru banget",  
                "pesan":"semangat kuliah nya dan jangan lupa senyum kakk"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kakak ini asik pollll",  
                "pesan":"Sehat sehat ya kakk, semangat!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sYplyZlMImsZQt361UYZkElZ-IzokhuG",
            "https://drive.google.com/uc?export=view&id=1XqtMQ4QEWo6XMxPLBKsjMsFr4e3SCgY3",
            "https://drive.google.com/uc?export=view&id=1dVzibfjlYJUWP-kT7xX-r5yAnchJvUKO",
            "https://drive.google.com/uc?export=view&id=1LayhcQyQwajxuiopNWnpWm-48UQTVszd",
            "https://drive.google.com/uc?export=view&id=11alLXTy-gQygrp7a66BLeDWzoYG3E7Kf",
            "https://drive.google.com/uc?export=view&id=1o2A2d__IF1qx07jcTPgZ8uel18Zdjioz",
            "https://drive.google.com/uc?export=view&id=1PqxYPfn5eCoBG7m6v6L_TZU_0wF-GldJ",
            "https://drive.google.com/uc?export=view&id=1xCf1UGHImjx1m8zQlzoPq1cPAphPzMCW",
            "https://drive.google.com/uc?export=view&id=1T9FxxjgotWSpd74tVtZdK52PmtoFMSPm",
            "https://drive.google.com/uc?export=view&id=1QozcVMzAgugyurZd499GeM94_Q8YHZLg",
            "https://drive.google.com/uc?export=view&id=1YsCiW5E6lhiv1ebrfVtNsyfqqGiaC_eU",
            "https://drive.google.com/uc?export=view&id=1TGis1akZZuNXMsCE3pjh70GZuT8Jnh-G",
            "https://drive.google.com/uc?export=view&id=1I6I5w3R-CHb2QKTKT-LLGwGYFpi3FnNV",
            "https://drive.google.com/uc?export=view&id=1Wy2MMUW8VIP49ulVZeRs3lab7feMZ54B",
            "https://drive.google.com/uc?export=view&id=1ANeASKScKQHG9xWNDRAVl-HwCrvIBe1H",
            "https://drive.google.com/uc?export=view&id=1DkafkFCgeM0GxxfneuLrAep9d0-BL2ew",
            "https://drive.google.com/uc?export=view&id=1RDofHgaLOdzi4omNGsQn2pjH_AgOwLcu",
            "https://drive.google.com/uc?export=view&id=1dulsnV2aRxN1SBHrbseJLiQAACQ9fNnK",
            
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
                "kesan": "Kakaknya asik banget jadi lebih enjoy kalau ngobrol",  
                "pesan":"Sehat terus yaa kak, jangan lupa istirahat"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak nelly ramah banget",  
                "pesan":"tetap jadi pribadi yang lembut ya!"# 1
            },
            {
                "nama": "Khoriul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam__",
                "kesan": "Abangnya kalem banget",  
                "pesan":"Sukses terus, Bang!"# 1
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
                "pesan":"terus rekam hal hal yang indah ya bang"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Bang Rafi baik dan kocak banget",  
                "pesan":"Semangat bang!"# 1
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
                "pesan":"Terus percaya diri ya kak"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122350020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaa",
                "kesan": "Kakaknya lucu banget",  
                "pesan":"jangan lupa istirahat kak"# 1
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
                "pesan":"Terus semangat dan sukses terus kak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya sopan banget",  
                "pesan":"terus berkembang yaa kak donaa!"# 1
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
                "pesan":"Semangat terus kuliah nya kakk"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya seru dan baik banget",  
                "pesan":"semangat menyala lagi ya kak!!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas, Jati Agung",
                "hobbi": "Dengar musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla keliatannya kalem dan baik",  
                "pesan":"Tetap semangat dan jangan lupa bersyukur"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania asik banget",  
                "pesan":"Semoga makin sukses ya kakkk"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Bang Akmal baik banget",  
                "pesan":"Terus berproses ya bang!"# 1
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana keren dan asik banget",  
                "pesan":"Semangat mengembangkan diri kak"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra kalem dan baik banget",  
                "pesan":"tips keren nya dong kak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah balau residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak eigi ramah dan baik",  
                "pesan":"be yourself ya kakk"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Romauli cantik dan gemesin",  
                "pesan":"tetep semangat dan ceria terus ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()





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
            "https://drive.google.com/uc?export=view&id=1JGSwIux900bzEWMedEGclvh8EabiMEln",
            "https://drive.google.com/uc?export=view&id=1VAiJ6d9lg9NiseWOOO94D2KRSWTmlGHF",
            "https://drive.google.com/uc?export=view&id=1JQT2l_QdTltmVSIk8041D08cOwo6BH5X",
            "https://drive.google.com/uc?export=view&id=1rNdxOOs1LP_LnNRV6E1hAgv144NeX364",
            "https://drive.google.com/uc?export=view&id=1nzeBEknz0rqaIVujEjEq4-CTtcHZLnUw",
            "https://drive.google.com/uc?export=view&id=1GhRSA_h5BF-dlpSJY1rcRcHjFkSbpcTR",
            "https://drive.google.com/uc?export=view&id=1uwGNsGeOAKZOj3PlCuKtQ_8YoTzp18ZX",
            "https://drive.google.com/uc?export=view&id=1gqbEOOzMQp5_Mzwmikx0w_3b1G-0jr6T",
            "https://drive.google.com/uc?export=view&id=1lMIqrlwEi7G-Y_IlITd_a-rVp3bP_9FD",
            "https://drive.google.com/uc?export=view&id=1EbDKmhLa_IVWFQioWnhudgMR6OrSUb7d",
            "https://drive.google.com/uc?export=view&id=1I6_4pfQjvMDKXrSpjju9py5Z3jYqEXnc",
            "https://drive.google.com/uc?export=view&id=1CwIDZMm3moN3ALP9_KCkpT42XbSqIua2",
            "https://drive.google.com/uc?export=view&id=1tENlh6xjRORBkcVqO0bDndo_xiDTBqkE",
            "https://drive.google.com/uc?export=view&id=1LMZZBUBmO8ReHeSCGrH45l5M782GZihD",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "Nonton Orang Kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "bang jere baik, vibesnya itu loh gacor banget",  
                "pesan":"semoga bang jere tetep jadi pribadi yang lebih baik, tetep semangat menjalani hari dan sukses selalu yaaa bang!!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "Lomba ngga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "kak dhea baik banget, positive vibes juga",  
                "pesan":"semoga kak dhea bisa jadi pribadi yang lebih gacor lagi, semangat dan sehat selalu kakkk"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Tidur",
                "sosmed": "@rnshism",
                "kesan": "Kak renisha baik banget, lucu jugaa",  
                "pesan":"semoga kakak nya tetep jadi versi diri dia, semangat dan sukses teruss ya kak, jangan lupa istirahat kakkkk"# 1
            },
            {
                "nama": "Annisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Ubud",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari Kesibukan Baru",
                "sosmed": "@ansftynn_",
                "kesan": "kakaknya baik, kalem (mungkin karena baru kenal)",  
                "pesan":"kak annisa semangat terus ya, tetep jadi diri sendiri, jangan lupa istiahat yaaa!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "abang abang keren, pinter, baik",  
                "pesan":"tetep semangat dan sehat selalu bang dharu!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak Sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "kak feby lucu banget, baik juga, humble",  
                "pesan":"semoga di hari selanutnya tetep ada senyum di wajah kakak"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "bang givaro asik, keren jga",  
                "pesan":"di kedepannya tetep emangat dan sukses selalu ya bang"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "bang mirzan baik, kalem sih soalnya pas ketemu itu agak pendiem",  
                "pesan":"semoga di hari seanjutnya tetep tersenyum walau tugas membantai, rapat tiap saat, semangat bang!"# 1
            },
            {
                "nama": "Berliana Enda Putra",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "Main paddle",
                "sosmed": "@iamridhomanik",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi batch google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Kota Tarakan",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mdWfkZYEv9pKDJrNV8JBjkP5YlX6NdRQ",
            "https://drive.google.com/uc?export=view&id=1ONOur7fziMw8CT3z4yBoKZgkLPCOhV6W",
            "https://drive.google.com/uc?export=view&id=1Chp6zIr7BYdhe8-nndoaq7sm4NNCCEGG",
            "https://drive.google.com/uc?export=view&id=1tQ_Pugo1_372TsnSHKxT0O8_ex2hbiLo",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Dengerin lagu, nyanyi, game, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "122450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "122450069",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        Senator()
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1D87dWJw9VhT38uFSzKOgUetaxAysVOJy", #bg ferdy
            "https://drive.google.com/uc?export=view&id=1ZHOZvKqua23SqQd7gwUkGosnlzoqHVQS", #ka nisrina afifah
            "https://drive.google.com/uc?export=view&id=1pJGfHMm-UEBpmkne6z2Ed291rueYo5ag", #ka pasha
            "https://drive.google.com/uc?export=view&id=116lZ3ER4Zy2Ia6aXofyEnrkltIkhBl5l", #bg ahmad
            "https://drive.google.com/uc?export=view&id=1Fhdv6YKODsHCILzKv68xydg8CHEM8Zix", #ka arienta
            "https://drive.google.com/uc?export=view&id=1_p0aIFYR6FfKaeeAJFXjin7M0ag6QplB", #bg daffa hadyan
            "https://drive.google.com/uc?export=view&id=1mAOE7GgvfhCnPpj2daQobBzRA0ojcQJl", #bg fajar
            "https://drive.google.com/uc?export=view&id=1kDJ0mfVi4evKXccvoBJSc4aJ2HsuUUH8", #ka natasya
            "https://drive.google.com/uc?export=view&id=1-RVjJiJt-5F-hob1x9ec9_sFcdTuHDt8", #bg nobel 
            "https://drive.google.com/uc?export=view&id=1LQeke16OsQrMKTm5Ze9WP3HQ1trDa5bK", #bg aji
            "https://drive.google.com/uc?export=view&id=1YXNSfydCeLVAPMZTPkgNiIN369YsexZP", #ka vany
            "https://drive.google.com/uc?export=view&id=12YIShGMBFrqQGs1cZoB4vDRo2KujSxma", #bg ahmad sahidin
            "https://drive.google.com/uc?export=view&id=14ILN2Y--Z8l3g8ktFQSzhcYhQrbVrfSb", #bg ali
            "https://drive.google.com/uc?export=view&id=1V_r9bGwk5wryPBZ8XI0ALImFT_PIobE4", #ka razka
            "https://drive.google.com/uc?export=view&id=1FBTK3aXH4F5uPxjR5RotximjcMjWFneu", #ka risma
            "https://drive.google.com/uc?export=view&id=1GFpI3Uj0-9HiU7I9QAo3dMKb1OWmzmnt", #ka oca
            "https://drive.google.com/uc?export=view&id=1TgYCgFHkT71UpZ3ZoMoWy8KM43KnnQoG", #bg sahid maulana
            "https://drive.google.com/uc?export=view&id=16A2Rwjw99PRDwDt17zcegvJaJ2BJW55M", #bg daffa ahmad 
            "https://drive.google.com/uc?export=view&id=11cxsbf5PY2XyzYINcQ1h_jgROLCo0zN0", #ka erma
            "https://drive.google.com/uc?export=view&id=17acpksE0g7mm43QjLkr3fMmNuIbHYwvE", #bg ihsan
            "https://drive.google.com/uc?export=view&id=1PFVhWDLY6ZIl598-CHs5UUas0YcchcwK", #bg kevin
            "https://drive.google.com/uc?export=view&id=1Ak_nND7KH4WzcrWVDsmnh7lq1b5981z3", #ka lidia
            "https://drive.google.com/uc?export=view&id=161yIBR-vveLXLcNBjMzNYTrTdLNtPY7M", #bg ridwan
            "https://drive.google.com/uc?export=view&id=1EzyaymeKce3SBW8Iw9Pw4O0WwnFksuHa", #bg uliano
            "https://drive.google.com/uc?export=view&id=1dj5UNspA0rVxMwkvSuxltRie-1v_bb_y", #bg benget
            "https://drive.google.com/uc?export=view&id=1XB9-1jh_BBN3O9iwFvAvlV73lNca4Z6N", #ka rewina
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
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@afifahhnsrn",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ahmad.rizky___",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Kost Orange",
                "hobbi": "Ngekader",
                "sosmed": "@arientakhsnl_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@daffahdynn_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ginda_mrp",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kostan putri gerbang barat sebelah sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@nobelnizam",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Fam",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabilaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22__",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ali_parisi3",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450079",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
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
                "asal":"Depok",
                "alamat": "Jalan Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
        DepartemenPSDA()
elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1D87dWJw9VhT38uFSzKOgUetaxAysVOJy", #bg ferdy
            "https://drive.google.com/uc?export=view&id=1ZHOZvKqua23SqQd7gwUkGosnlzoqHVQS", #ka nisrina afifah
            "https://drive.google.com/uc?export=view&id=1pJGfHMm-UEBpmkne6z2Ed291rueYo5ag", #ka pasha
            "https://drive.google.com/uc?export=view&id=116lZ3ER4Zy2Ia6aXofyEnrkltIkhBl5l", #bg ahmad
            "https://drive.google.com/uc?export=view&id=1Fhdv6YKODsHCILzKv68xydg8CHEM8Zix", #ka arienta
            "https://drive.google.com/uc?export=view&id=1_p0aIFYR6FfKaeeAJFXjin7M0ag6QplB", #bg daffa hadyan
            "https://drive.google.com/uc?export=view&id=1mAOE7GgvfhCnPpj2daQobBzRA0ojcQJl", #bg fajar
            "https://drive.google.com/uc?export=view&id=1kDJ0mfVi4evKXccvoBJSc4aJ2HsuUUH8", #ka natasya
            "https://drive.google.com/uc?export=view&id=1-RVjJiJt-5F-hob1x9ec9_sFcdTuHDt8", #bg nobel 
            "https://drive.google.com/uc?export=view&id=1LQeke16OsQrMKTm5Ze9WP3HQ1trDa5bK", #bg aji
            "https://drive.google.com/uc?export=view&id=1YXNSfydCeLVAPMZTPkgNiIN369YsexZP", #ka vany
            "https://drive.google.com/uc?export=view&id=12YIShGMBFrqQGs1cZoB4vDRo2KujSxma", #bg ahmad sahidin
            "https://drive.google.com/uc?export=view&id=14ILN2Y--Z8l3g8ktFQSzhcYhQrbVrfSb", #bg ali
            "https://drive.google.com/uc?export=view&id=1V_r9bGwk5wryPBZ8XI0ALImFT_PIobE4", #ka razka
            "https://drive.google.com/uc?export=view&id=1FBTK3aXH4F5uPxjR5RotximjcMjWFneu", #ka risma
            "https://drive.google.com/uc?export=view&id=1GFpI3Uj0-9HiU7I9QAo3dMKb1OWmzmnt", #ka oca
            "https://drive.google.com/uc?export=view&id=1TgYCgFHkT71UpZ3ZoMoWy8KM43KnnQoG", #bg sahid maulana
            "https://drive.google.com/uc?export=view&id=16A2Rwjw99PRDwDt17zcegvJaJ2BJW55M", #bg daffa ahmad 
            "https://drive.google.com/uc?export=view&id=11cxsbf5PY2XyzYINcQ1h_jgROLCo0zN0", #ka erma
            "https://drive.google.com/uc?export=view&id=17acpksE0g7mm43QjLkr3fMmNuIbHYwvE", #bg ihsan
            "https://drive.google.com/uc?export=view&id=1PFVhWDLY6ZIl598-CHs5UUas0YcchcwK", #bg kevin
            "https://drive.google.com/uc?export=view&id=1Ak_nND7KH4WzcrWVDsmnh7lq1b5981z3", #ka lidia
            "https://drive.google.com/uc?export=view&id=161yIBR-vveLXLcNBjMzNYTrTdLNtPY7M", #bg ridwan
            "https://drive.google.com/uc?export=view&id=1EzyaymeKce3SBW8Iw9Pw4O0WwnFksuHa", #bg uliano
            "https://drive.google.com/uc?export=view&id=1dj5UNspA0rVxMwkvSuxltRie-1v_bb_y", #bg benget
            "https://drive.google.com/uc?export=view&id=1XB9-1jh_BBN3O9iwFvAvlV73lNca4Z6N", #ka rewina
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
                "kesan": "",  
                "pesan":""# 1
            },
        ]
<<<<<<< HEAD
# Tambahkan menu lainnya sesuai kebutuhan
=======
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()







>>>>>>> 88fbeb601ece0a0846b4b7f18a69b475709c55e1

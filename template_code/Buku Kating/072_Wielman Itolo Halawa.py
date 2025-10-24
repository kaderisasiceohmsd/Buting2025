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
            "https://drive.google.com/uc?export=view&id=17i10zrZ1nMiSpfttAxNmyezE-6rhbNLy",
            "https://drive.google.com/uc?export=view&id=12tWWzpF3pdMrpdRkvzV0jHzzsazEILqs",
            "https://drive.google.com/uc?export=view&id=11DsLJXpJ9DyRd1MjC3xaOzGk1gFVy_o9",
            "https://drive.google.com/uc?export=view&id=1mQpkCwuhh5env0gs-FEd3x_4rtxq16FB",
            "https://drive.google.com/uc?export=view&id=1HxYdgOAZ1Mw2t_D8NsTHOcaDuQh74CWO",
            "https://drive.google.com/uc?export=view&id=1HktwkZDkgDR3Ly3Q3Vv7FbOKQ59nmH63",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "wawasannya luas, asik diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "baca buku dasar dasar sql",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abangnya asik, banyak ilmu yang saya dapat dari dia",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Aires Kost",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya asik, banyak bercandanya",  
                "pesan":"semangat kakak, semoga ilmu menjadi sekretarisnya dapat bermanfaat untuk proses perkuliahannya"# 1
            },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya keliatan ramah dan tipikal yang kalem",  
                "pesan":"semangat kakak NIM 72, semoga nanti bisa sharing banyak hal. lancar terus kuliahnya kak"# 1
            },
             {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "baca buku, saku pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini tegas, baik, dan pendengar yang baik",  
                "pesan":"keren bisa megang bendahara umum seperti ini, jaga kesehatannya kak"# 1
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang, Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "kakaknya full senyum, keren bisa mengemban jadi bendahara",  
                "pesan":"semangat terus kuliahnya kakak, bahagia selalu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wsIPSPK8DGNiOjaVkUJYTT-2rlcKXRAN",
            "https://drive.google.com/uc?export=view&id=18XgnFam9paD_yA85_ooj76LLmBIC2ufK",
            "https://drive.google.com/uc?export=view&id=1mucdbb_842kwROfb10u3s-Llqi0140ue",
            "https://drive.google.com/uc?export=view&id=1xS6fQqN3nRbs_upMFlf1F1DnLrIixOWc",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "",
                "hobbi": "mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "abangnya seru disjsk ngobrol, wawasannya luas dan suka bercanda",  
                "pesan":"semangat kuliahnya bang, jadilah bintang seperti nama abang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "kakaknya seru, baik banget, pendengar yang baik, kece, keren banget lah",  
                "pesan":"jaga kesehatannya kak, semangat perkulliahan dan bahagia selalu"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakaknya mau berbagi ilmu, pinter banget, wawasannya luas dan jago bahasa inggris",  
                "pesan":"semangat kakak NIM 72, semoga dilancarkan studinya hingga akhir dan dipermudah dalam setiap persoalan"# 1
            },
             {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret belwis",
                "hobbi": "rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "kakaknya baik, mengarahkan, realistis, suka bercanda",  
                "pesan": "bahagia selalu kak, tentu semoga studinya dapat selesai dengan baik, tetap jaga kesehatan kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AL6XsBDxYayyUp_6klxJZo95dTkrvRMq",
            "https://drive.google.com/uc?export=view&id=1jnbjIXZY7W-r29_u4j7iKDvvn3EGVWQ7",
            "https://drive.google.com/uc?export=view&id=1AZj_2ik1du3xJOSQBlvE6VAoSdlQeVQs",
            "https://drive.google.com/uc?export=view&id=10ewTRlFxtAdUA4xOhBLxJSWnjr3sFCMY",
            "https://drive.google.com/uc?export=view&id=1oftOV7Xot_PVicD7TYs3ntr_bTKKxEjT",
            "https://drive.google.com/uc?export=view&id=1kPhPfOJaVRfXFV4G-OZXeOah-39nvB5S",
            "https://drive.google.com/uc?export=view&id=1dW4tE6rbexYd5zsP7Htqqf18h5HTgbD9",
            "https://drive.google.com/uc?export=view&id=1hRa4e6xiJDS8h77DoKylE5DTY3ApkF5B",
            "https://drive.google.com/uc?export=view&id=1WPKW7kweeudUqs2k0UjVQhfcqz9wqe4-",
            "https://drive.google.com/uc?export=view&id=1eejaAoVM32w43zh8ajx2yqTLHuAspDrF",
            "https://drive.google.com/uc?export=view&id=13xFMrdZaxzA6B9fEgM7SAfib1eHthcHI",
            "https://drive.google.com/uc?export=view&id=1VPdw1fOWZilKgrABjPRD9GS69LWPefUj",
            "https://drive.google.com/uc?export=view&id=1ZhcgZ6cKYBZJyJ476OM7jmdi2eMCzxUC",
            "https://drive.google.com/uc?export=view&id=19QH8cowE3U2XwuMlxLbFd1GLQAIlwXsD",
        
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "B2 , NO 2",
                "hobbi": " Zumba di pln setiap jumat pagi",
                "sosmed": "@jeremia.s",
                "kesan": "abangnya asik, full senyum, humble",  
                "pesan":"semangat kuliahnya bang, sukses selalu"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto, Jawa Timur",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "keliatan ramah, baik dan bijak",  
                "pesan":"jaga kesehatannya kak, semangat perkulliahan."# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan pancing",
                "sosmed": "@Renishapg",
                "kesan": "kakaknya welcome banget, adaptasi lingkungannya bagus",  
                "pesan": "semoga bisa berjumpa di lain kesempatan"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Muara Enim, Sumatera Selatan",
                "alamat": "C2",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "kakaknya ramah jadi ga takut buat ajak ngobrol",  
                "pesan":"semangat dan pantang menyerah kak"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "positive vibes, tipikal yang ramah dan welcome",  
                "pesan": "sukses terus bang, jaga kesehatannya"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bangka Belitung",
                "alamat": "Kobam",
                "hobbi": "Nongkrong di gedung f",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya interaktif, berkesan dan serius",  
                "pesan": "bahagia selalu bang, selalu tebarkan sisi positifnya"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way halim",
                "hobbi": "Bengong",
                "sosmed": "@dhruchyo",
                "kesan": "walau hobi bengong tapi abangnya pinter banget, informatif dan keren ",  
                "pesan": "jaga kesehatannya bang, sukses selalu"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way huwi",
                "hobbi": "Menggodai Abang Cimol",
                "sosmed": "@fby.wlndr",
                "kesan": "kakaknya baik, suka bercanda",  
                "pesan": "semangat terus kak, sehat selalu"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@givarooo",
                "kesan": "baik, mengarahkan, positive vibes",  
                "pesan": "semangat terus bang, semoga dilancarkan hingga akhir studinya nanti"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Belwis",
                "hobbi": "Mengukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "ramah, orangnya humble.",  
                "pesan": "bahagia selalu kak, tentu semoga studinya dapat selesai dengan baik, tetap jaga kesehatan kak"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": " 123450085",
                "umur": "19",
                "asal":"Kalimantan Utara",
                "alamat": "Belwis",
                "hobbi": "Sibuk",
                "sosmed": "@j_eesie",
                "kesan": "kakaknya baik, humble dan ramah.",  
                "pesan": "bahagia selalu kak, sukses kuliahnya"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Gang Sakung",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "humble, full senyum dan soft spoken",  
                "pesan": "semangat terus bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Ketapang, Kalimantan Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monica_tjg",
                "kesan": "kakaknya baik, realistis dan serius",  
                "pesan": "Semangat terus dan jangan mudah menyerah"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pekan Baru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "kakaknya positive vibes, ramah dan asik diajak ngobrol",  
                "pesan": "Sehat selalu dan sukses perkuliahannya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zG7wsLkesy-aYwW4nKfxTOinUNANEaP9",
            "https://drive.google.com/uc?export=view&id=1CHD8YAdrfNJ6Tx-mUZok1fSR-PUdBJin",
            "https://drive.google.com/uc?export=view&id=1OiGElT4u2FHs4Mc2gLrdEE0bEONfhHMo",
            "https://drive.google.com/uc?export=view&id=1ZtL7iqn0oTHm5obEkZY0FadJFbZpLk3E",
            "https://drive.google.com/uc?export=view&id=1efuXk6wp_8KSUwB9uOuJ_cSy06muoCdF",
            "https://drive.google.com/uc?export=view&id=1uhM5GV0KJYznuiv8mIyootDMMiy6635Z",
            "https://drive.google.com/uc?export=view&id=1XGphH8ThO9PkIxb2IqdwKGVqrPZr63UY",
            "https://drive.google.com/uc?export=view&id=19d-1gWJxNxmuDwxyvMLvNsB_qbz7HiCv",
            "https://drive.google.com/uc?export=view&id=135bbCL7QGap6YyCDJ4203228EqkqvzFi",
            "https://drive.google.com/uc?export=view&id=1SAcso_ccRpJiwbh_RjNFeSnjSeccnUCl",
            "https://drive.google.com/uc?export=view&id=137nyZnIonknb9uplyP1p2jZbrKeyJ99x",
            "https://drive.google.com/uc?export=view&id=1-uS6LBaqlaRjybsxOPbk-wDxhFdtx8fJ",
            "https://drive.google.com/uc?export=view&id=1eyF-n8l5zG-Q_eIE1ArR0JeAFaXrTlRm",
            "https://drive.google.com/uc?export=view&id=1FDmnn2fMnpTVf0vvdPCmkUVUEelsTumu",
            "https://drive.google.com/uc?export=view&id=1gp3NJms0zQAoANiW7p-QnXPC2ShRBI7Z",
            "https://drive.google.com/uc?export=view&id=1RJHP--7oOMx115xOuzsra9smLDUvBkqN",
            "https://drive.google.com/uc?export=view&id=1KdMFwls6mYr5MZNzBwevJ7zjhjErsdex",
            "https://drive.google.com/uc?export=view&id=1rTKtnv9Mhpn6Hq1debzxOXik4Y8PGv7I",
            "https://drive.google.com/uc?export=view&id=1l2RgjPPKA-rsZYf9Q2pMLnuXHmnIuseJ",
            "https://drive.google.com/uc?export=view&id=1TpC_pvVCn5sd-ZcweIP88Y7gz3QKCpYh",
            "https://drive.google.com/uc?export=view&id=19hpUFu1JhJjp233khv8h84KsXMVDUiZM",
            "https://drive.google.com/uc?export=view&id=1eTB6g9V2UCCNLwnZGnGBSGCD8ywTabpr",
            "https://drive.google.com/uc?export=view&id=18mHVJIHVhq40nr289JdASyiArzZsf7bJ",
            "https://drive.google.com/uc?export=view&id=1bcgy6iIzgukcM0gCBjlwS35sou0cbMsA",
            "https://drive.google.com/uc?export=view&id=1gWNujTUkpMjFJsmrNS_I4Yn3Eifijkd3",
            "https://drive.google.com/uc?export=view&id=1--9lOAhnCasoEeP0-CO21-ICutkHstLS",
            "https://drive.google.com/uc?export=view&id=1CAkkwWJBAkLX4sxtFHGHgZBqbRdUynjs",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "124450107",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya kalem, tapi keliatan bijak dan humble ",  
                "pesan":"sehat selalu bang, semoga dilancarkan proses perkuliahannya hingga akhir"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya kece, asik diajak ngobrol",  
                "pesan":"semangat terus kak menjadi sekdep dan menjalani perkuliahannya "# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "kakaknya tegas, perhatian, profesional, kritis.",  
                "pesan":"terus menjadi teladan bagi orang lain kak, keren banget."# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@sahid22",
                "kesan": "aktif olahraga keren, abangnya humble",  
                "pesan":"jaga kesehatannya bang"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "cari masalah anak 23",
                "sosmed": "@ahmadnaufa_ll",
                "kesan": "abangnya asik diajak ngobrol",  
                "pesan":"semangat perkuliahannya bang"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "belwis",
                "hobbi": "main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "kritis banget, aktif organisasi, baik, wawasannya luas",  
                "pesan":"semangat terus disemua pekerjaan tangan yang akan abang lakukan, mohon arahannya karena saya berminat gabung debat juga"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "sebelah  kos bang dapa",
                "hobbi": "Liatin Haikal",
                "sosmed": "@arientakhsnl_",
                "kesan": "berkharisma, tenang tapi perhatian",  
                "pesan":"jangan lupa makan dan jaga kesehatannya kak"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "sebelah kos kak arin",
                "hobbi": "Isengin Fislam",
                "sosmed": "@daffahdynn_",
                "kesan": "aktif banget organisasi, vibesnya selalu semangat",  
                "pesan":"semangat terus bang, jaga kesehatannya juga"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sama kek bang ahmad, Kontrakan GH",
                "hobbi": "main, baca, bulutangkis, gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "abangnya asik, baik dan perhatian",  
                "pesan":"semangat perkuliahannya bang"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar muara beliti",
                "alamat": "kost putri gerbang barat",
                "hobbi": "belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "sikapnya tegas tapi sangat perhatian, merangkul",  
                "pesan":"terus menyebarkan hal-hal positif untuk orang disekitar kakak"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Gg. Perwira",
                "hobbi": "Ngakader",
                "sosmed": "@nobelnizam",
                "kesan": "tegas, perhatian dan selalu memastikan semuanya sesuai harapan",  
                "pesan":"semangat terus bang, sehat selalu"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450022",
                "umur": "-",
                "asal": "Sumatera Barat",
                "alamat": "-",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "abangnya stabil baik organisasi maupun akademik, keren",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak berwibawa, tenang dan berkharisma.",  
                "pesan":"jaga kesehatannya, bahagia selalu"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya baik, asik dan ramah",  
                "pesan":"semoga bisa berjumpa dan diskusi banyak hal"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Waydadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "kakaknya baik, full senyum dan kalem",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
                        {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@risma.mustika_",
                "kesan": "humble banget, kakaknya seru diajak ngobrol",  
                "pesan":"jaga kesehatan, bahagia terus kak"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "kakaknya tipe pendengar yang baik, seru banget",  
                "pesan":"semangat terus kak, hobinya roblok next kita mabar ya kak"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "abangnya humble, berkharisma dan pengingat yang baik",  
                "pesan":"semangat kuliahnya bang, semoga dilancarkan hingga akhir"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "dari awal ngelihat, memang vibes dancer banget",  
                "pesan":"pertahankan passion nari-nya kak, keren banget"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Makan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnya berbaur, humble dan baik banget",  
                "pesan":"semangat terus diperkuliahannya bang"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selatan",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj__",
                "kesan": "abangnya kalem, bakatnya baik dan ramah",  
                "pesan":"jaga kesehatannya, sehat selalu bang"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakaknya baik, mudah di ajak kerjasama",  
                "pesan":"semangat terus kak, semoga kuliahnya selesai dengan pencapaian memuaskan, AMIN"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450023",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Ngehina orang Bengkinang",
                "sosmed": "@m.ridwan_22",
                "kesan": "abangnya baik, humble dan berbaur",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Berenang, ngoleksi figura & kartu anime",
                "sosmed": "@rewinanaaa",
                "kesan": "kakaknya perhatian, aktif dan baik banget",  
                "pesan":"semangat terus kak, hobinya keren"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "abangnya baik banget dan pengertian",  
                "pesan":"semangat terus perkuliahannya bang"# 1
            },
            {
                "nama": "Uliano Wiliam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main piano, nanem anggrek, ngoding dan nyari kesalahan anak 24",
                "sosmed": "@ullianowlm",
                "kesan": "abangnya keren apalagi main pianonya, kalem tapi tegas",  
                "pesan":"semangat perkuliahannya bang, sehat selalu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lfs99m-GZnZfGiaxkqcAbmt2CfgIGcxZ",
            "https://drive.google.com/uc?export=view&id=1K0k_4fPWYMWe5m8sxV0SvbXwjpgC9-rY",
            "https://drive.google.com/uc?export=view&id=1HokuW12sHugDB_9zbxt2rz7ao0usOzan",
            "https://drive.google.com/uc?export=view&id=1aeLJXQpRVz6oIPdvlzCVRWThKzi-57Yr",
            "https://drive.google.com/uc?export=view&id=1hWLkzqHN1ZBhgm1UJBiCb82ggoq9JhxX",
            "https://drive.google.com/uc?export=view&id=1Rs7CsPOBoUukmXZwKflX4Uk_JiR7r2pR",
            "https://drive.google.com/uc?export=view&id=1VtgFjv7T6VOZy_OUUJ0GygupkcH8ONoS",
            "https://drive.google.com/uc?export=view&id=1d1E4ms66oCl4kDhFs0v3undMFoIOTX5A",
            "https://drive.google.com/uc?export=view&id=1fvCu7N35KmT2SEsfGnEzljh5swJOCAvj",
            "https://drive.google.com/uc?export=view&id=1n5KV9aGat9YSxEBKXkfJarDPFwBLhCs1",
            "https://drive.google.com/uc?export=view&id=1yc_4byVzIMDxGIkzORAWdmtFLoLFdPAg",
            "https://drive.google.com/uc?export=view&id=1DNB9FC6XsnXClD2vC1in9D0mbzo5xvby",
            "https://drive.google.com/uc?export=view&id=1jxFPt937kxpo7v4ISo7fPljZD8-aQwtZ",
            "https://drive.google.com/uc?export=view&id=1Msn2iKU9xCjaiT60qaZRxGz_DKhPoVEH",
            "https://drive.google.com/uc?export=view&id=1-cD6TCEi6fN43q3sdo09YqdVIalzMMEz",
            "https://drive.google.com/uc?export=view&id=157LqrPMKCNrVjcZvYOWcd1NxRKbVgKlJ",
            "https://drive.google.com/uc?export=view&id=1nK3ynOHz6eWfqFu5NEaDIjNyRd4ojwFk",
            "https://drive.google.com/uc?export=view&id=1SmRSH8H3wsbZ7g4pRdUMc8SWV5T6vqNk",
            "https://drive.google.com/uc?export=view&id=1-TsF66NcU2i2VvUdXP_aIYQ7tEaa7cGo",
            "https://drive.google.com/uc?export=view&id=1yxAAQ9xPKFvgRtR8iKgTCNDS033PuG0j",
            "https://drive.google.com/uc?export=view&id=1uYWqQPu8gmtmN0A0KyxGwveS60f56WJ3",
            "https://drive.google.com/uc?export=view&id=1R8iIU_ZSItA_rCUlMs8wjbGgaSjOCBpp",
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
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "keliatan pinter, orangnya ramah.",
                "pesan":"sukses selalu dan jaga kesehatannya kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Publick Speakingnya bagus, selalu tersenyum.",
                "pesan":"tetap menjadi teladan yang bagi banyak orang."
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "abangnya pinter, vibes ngodingnya sangat ketara",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya menyenangkan, keren dan duta juga",
                "pesan":"Sukses terus bang"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, bang."
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "pendegar yag baik banget, perhatian dan solutif.",
                "pesan":"makasih ya kak udah ngasih beberapa arahan sebelumnya"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "enak banget diajak diskusi, kakaknya asik terus pinter",
                "pesan":"Semangat terus kak, semoga dilancarkan perkuliahannya"
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "positive vibes, orangnya ramah.",
                "pesan":"di tunggu gelarnya nanti kak, semangat!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "abangnya keliatan pinter banget soal ngoding",
                "pesan":"bahagia selalu bang"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "abangnya pinter banget, teladan bagi banyak orang",
                "pesan":"Semangat terus bang, semoga suksesnya makin gemilang"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "abangnya humble banget, asik, dilain sisi juga pinter banget",
                "pesan":"tetap energic seperti ini bang, semangat"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakaknya baik, ramah dan perhatian.",
                "pesan":"jaga kesehatan dan bahagia selalu kak"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "kakaknya enak di ajak ngobrol/diskusi",
                "pesan":"jangan lupa makan kak, tetap semangat"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "positive vibes juga, rapi dan ramah",
                "pesan":"semangat di perkuliahanya bang"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "kakaknya ramah, soft spoken dan kalem.",
                "pesan":"semangat terus kak di perkuliahannya"
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "kakaknya tegas, tapi baik, energic dan ekspresif",
                "pesan":"sukses terus kak tanty"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "kakaknya baik, pendengar yang baik dan suka sharing-sharing",  
                "pesan":"sehat selalu kak, semangat terus kuliahnya"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "baik, humble dan kalem",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "Main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakaknya baik banget, soft spoken",  
                "pesan":"sehat selalu kak"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakak ini asik, ramah",  
                "pesan":"semangat terus kuliahnya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1chRpS-vd6DjzS0Q2FfD6HFrxVyv49nJU",
            "https://drive.google.com/uc?export=view&id=1mIC8jYDyJsqBcpEtP3f3MVmg3GapfYCW",
            "https://drive.google.com/uc?export=view&id=13SuVpd43Nw2Z9Juj2z6wQ9gCZarGmbnj",
            "https://drive.google.com/uc?export=view&id=1u4HYc_1TfpRGS0PYsKd5SqoxjKkbdQTG",
            "https://drive.google.com/uc?export=view&id=1yxeuVpdUEJx3Br_PbnIgM19mw5MR7SI3",
            "https://drive.google.com/uc?export=view&id=1AjWY-gjgyh7Jz74aJucQ58Z6lfBXoN8o",
            "https://drive.google.com/uc?export=view&id=1Io8eOl7r7_VcVpIi29OAY25s0Xwq2PkJ",
            "https://drive.google.com/uc?export=view&id=1li-8BKxQJiE1j1GMQ0BaF7pb2nc6ThJ7",
            "https://drive.google.com/uc?export=view&id=1We12yDCSoB-TWIwWLmxdRfUzVnFUINe0",
            "https://drive.google.com/uc?export=view&id=1c7Y3ZxvM-9KIuv7bR2D5Dg1eFQElh584",
            "https://drive.google.com/uc?export=view&id=1-Yf3jHV1wqZCGc0MZrbSqGMe3Et5TISG",
            "https://drive.google.com/uc?export=view&id=1WLAxg1tbKFjFA2TynvislxSu30ffRZBD",
            "https://drive.google.com/uc?export=view&id=1LXcktRYwAHnPGEig3hE-7FKhFPXtcAVA",
            "https://drive.google.com/uc?export=view&id=1tD37WpwSBXWiYUuqORkD02exIx_UBN8_",
            "https://drive.google.com/uc?export=view&id=1oulcgMA4Z2olp6LPvHbyVdn0p6C9v0zy",
            "https://drive.google.com/uc?export=view&id=1D6YgYzeKgNjTa5cVEGqYPriYNkGMO_PX",
            "https://drive.google.com/uc?export=view&id=1hw9yo26qvTcl2ElIF41w8Xmem0C9gi2J",
            "https://drive.google.com/uc?export=view&id=15jwWwTntDliX6NuaVAdqDSYFumlIh_X6",
            "https://drive.google.com/uc?export=view&id=1rGI5rX-VugHcrO-tcJQiSbN7a4JIfqoK",
            "https://drive.google.com/uc?export=view&id=1KMNQdNrh8g6P_LDjaJIm__RTo11HidQ0",
            "https://drive.google.com/uc?export=view&id=1REaN9Kp_yK7I69GYrv45vUscw0Ma2VhI",
            "https://drive.google.com/uc?export=view&id=1x7oxeFlUAuBrYwiheGz18jXR-YOjd2K4",
            "https://drive.google.com/uc?export=view&id=1umpYGQC31fufZ7lloPCbMVniGjk3Uvo6",
            "https://drive.google.com/uc?export=view&id=1cBBcJfQphTAlmfooRZlxgp1jQQGDNf4x",
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
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "positive vibes, selalu ceria",
                "pesan":"selalu bahagia kak, jangan pantang menyerah"
            },
             {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "kakaknya pinter banget, aktif dan pintar memanajemen waktu",
                "pesan":"semangat terus kak, jaga kesehatan ya!"
            },
             {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Oseru, ramah banget dan berbaur.",
                "pesan":"sehat selalu kak, semangat terus kuliahnya"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya asik, humble banget ke teman baru",
                "pesan":"semangat perkuliahannya bang, sehat selalu!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "kakaknya baik, full senyum dan ramah",
                "pesan":"selalu tersenyum kak, tebarkan sisi positif setiap harinya"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "kakaknya asik, ramah dan perhatian banget",
                "pesan":"sukses selalu kak, jaga kesehatan ya!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "baik banget, ingin bicara lebih banyak lagi",
                "pesan":"bahagia selalu kak, jaga kesehatan ya!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "kakaknya baik, selalu tersenyum dan dewasa.",
                "pesan":"semangat perkuliahanya kak!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "abangnya tegas, optimis dan aktif",
                "pesan":"jaga kesehatannya bang, next kalau pulang kampung ajakin ya bang"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "kakaknya baik banget, seru di ajak ngobrol",
                "pesan":"semangat terus perkuliahannya kak"
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "pembawaannya selalu tersenyum, humble.",
                "pesan":"selalu tersenyum untuk semua orang ya kak"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "abangnya kalem, ramah dan tenang",
                "pesan":"semangat perkuliahannya bang!, sukses terus", 
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya berbaur, ramah dan seru",
                "pesan":"jangan lupa makan kak, jaga kesehatan dan bahagia selalu"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "kakaknya ceria banget sesuai dengan eksternal",
                "pesan":"Selalu tebarkan sisi positifnya kak, semangat terus!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "kakaknya baik, tegas dan perhatian",
                "pesan":"semangat terus kak di perkuliahannya"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "kak nayla rramah dan welcome ke teman teman baru",
                "pesan":"semoga bahagia selalu kak"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "positive vibes banget, tenang dan ramah",
                "pesan":"sukses terus bang, semangat perkuliahannya"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "baik banget, pengertian dan aktif",
                "pesan":"jaga kesehatannya bang, semangatnya jangan pudar ya"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "positive vibes, ceria",
                "pesan":"semangat terus kak, ditunggu gelar sarjananya"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "kakaknya tegas, selalu tersenyum dan ramah",
                "pesan":"jaga kesehatannya kakak, terima kasih atas semua pelajarannya!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "abangnya tegas dan aktif.",
                "pesan":"jaga kesehatan ya bang, semoga perkuliahannya lancar"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakaknya bersemangat, baik banget dan mudah beradaptasi",
                "pesan":"semangat terus kak, bahagia selalu"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya selalu tersenyum, ceria dan ramah",
                "pesan":"selalu tebarkan hal positif yang kakak milik"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1m66fmwRUGylb9Dnep6NPNzQCMTF-PKcY",
            "https://drive.google.com/uc?export=view&id=1YrCxz9A0zi60NO032a9wJqhYxHNuCprC",
            "https://drive.google.com/uc?export=view&id=1nXnAc9pM7XVYR0i_8uuUfsAqCaBwmyaJ",
            "https://drive.google.com/uc?export=view&id=1mpGK4Gf37lqGukrBDV9f3k9a5R4Zg6on",
            "https://drive.google.com/uc?export=view&id=1dFITd7BKzsE7Jx1o8H_VlVDy1cbyPc8_",
            "https://drive.google.com/uc?export=view&id=1GtFrSU6Ksm8ketxa6t0cRjZLCdBAKWzm",
            "https://drive.google.com/uc?export=view&id=1g4RfZie0KnP3dgt7zUiNmO7wa1K7kuhM",
            "https://drive.google.com/uc?export=view&id=1m73IMho93_IL470PX-_vWOOoZHHt8yrV",
            "https://drive.google.com/uc?export=view&id=1pGN80dVgeWiWJAH5VHK-xeb7M4kTZilu",
            "https://drive.google.com/uc?export=view&id=1y9lhnQj_KpD_fP16btBcsQzREJQD0vQZ",
            "https://drive.google.com/uc?export=view&id=1J3UD8lc55W6siZZGbh2IO0gyLX9Czt9k",
            "https://drive.google.com/uc?export=view&id=19Fs8uCozHnyJAo5V4O3_6CBBe-glQkWH",
            "https://drive.google.com/uc?export=view&id=1asbWOCzQbMd9Z8MXBP3f5fEF5BT3O_KG",
            "https://drive.google.com/uc?export=view&id=1c-8bYrRRlWtSKWpEUIhEgLdE44OYQxvw",
            "https://drive.google.com/uc?export=view&id=1OIqtVE43EicHyry8DnMWLJ_EJ4QhPrDP",
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
                "kesan": "Kakaknya memiliki jiwa pemimpin",
                "pesan":"Terimakasih kak sudah membentuk tim internal yang ramah dan welcome bagi semuanya"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "awalnya ngira laki-laki juga, namun ternyata salah. kakaknya baik banget dan terbuka",
                "pesan":"semangat terus kak renta sekdep internal, keren banget"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "baik, ramah dan sangat nyaman diajak berbicara",
                "pesan":"semangat terus dalam perkuliahannya kak, jangan lupa makan"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "abangnya rohani banget, baik dan tenang",
                "pesan":"taat akan Tuhan terus ya bang, semangat"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakak sangat interaktif dan menarik untuk mendapatkan perhatian orang",
                "pesan":"semangat terus kak hanna, next pelayanan baren lagi ya"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "baik banget dan soft spoken banget",
                "pesan":"terus tersenyum kak, senyum berharga buat orang disekitar"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "jago olahraga, hobinya pun kece",
                "pesan":"semangat terus bang haikal"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "abangnya humble, sangat berbaur dengan yang lain",
                "pesan":"sehat selalu bang, sukses perkuliahannya"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "kakaknya kalem, perawakan tegas namun tetap ramah",
                "pesan":"semangat perkuliahannya kak, tetap tersenyum"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "bisa mengontrol emosinya dengan baik, ramah dan humble banget",
                "pesan":"tetap semangat kak, walaupun kegiatan kakak saat ini sangat padat"
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "keren banget, departemen internal bisa main piano dan gitar",
                "pesan":"Semangat dalam perkuliahan dan pelayanannya kak"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "jago nyanyi, baik dan rapi",
                "pesan":"semangat terus kak dalam perkuliahannya"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "kalem, keliatan ramah dan pendengar yang baik",
                "pesan":"semoga pengalaman di internal dapat dibawakan ke masa depan"
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "blm",
                "umur": "blm",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "abangnya ramah dan tenang",
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Jl. Durian 19",
                "hobbi": "Mengetik",
                "sosmed": "@rzhresti",
                "kesan": "kakaknya ramah, sesuai dengan departemennya internal",
                "pesan":"semangat kak, jaga kesehatan"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16DccF_2WlTKjvcCceDv-Vj90yfqnNz36",
            "https://drive.google.com/uc?export=view&id=1zJJBJJEnVbEmTELM8rjfGqdRgEEY8xe_",
            "https://drive.google.com/uc?export=view&id=1ix8VTt3u4ivBcmF68osDO8ZoAW0mGzrX",
            "https://drive.google.com/uc?export=view&id=1p1YfUNjmhZzTHmPAlqE2iEEJA9jGeQkl",
            "https://drive.google.com/uc?export=view&id=1STR_DjM-0Sqxbl7d7s7Vrq_IAHKvAxpI",
            "https://drive.google.com/uc?export=view&id=1BNwE7WSmeBwEyqheD2xuM6YX4tD6chPR",
            "https://drive.google.com/uc?export=view&id=1uwmOd5BKUMmfzkBqDYpRb4ug1BlqhZK-",
            "https://drive.google.com/uc?export=view&id=1BajmUYaAJpz7ky2IjeOSTon_07clIDSZ",
            "https://drive.google.com/uc?export=view&id=1CVJaEjPPxFM_cC0mhTV6-15bBKXB8OIz",
            "https://drive.google.com/uc?export=view&id=12dIuNMJFo7BhbDg6KDML_Rok9Q-XrSaM",
            "https://drive.google.com/uc?export=view&id=1wbm20kUu2VdDj1T4-Jt2K81qRJfJ8IsS",
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
                "kesan": "pnyer, aktif, realistis banget dan mengayomi.",
                "pesan": "semangat terus bang, sangat inspiratif"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "ramah, soft spoken dan tenang",
                "pesan": "bahagia selalu kak, semoga pengalaman SSD dapat digunakan di masa depan"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "abangnya ramah, jiwa bisnisnya dapat banget, akrab dan baik",
                "pesan": "sehat selalu bang, semoga dilancarkan studinya hingga akhir"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya keliatan ramah, humble dan asik",
                "pesan": "tetap tersenyum kak, membawa pengaruh buat sekitarnya"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "murah senyum, baik dan peduli",
                "pesan": "Semoga sukses kuliahnya kak, semangat"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Sukses selalu untuk kakak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "cepat mengenal dan berbaur dengan teman baru.",
                "pesan": "sehat selalu bang, jadilah inspirasi untuk adik-adik tingkat"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "kakaknya asik dan murah senyum.",
                "pesan": "semangat perkuliahannya kak, jaga kesehatan selalu!"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "sosok kakak yang asik dan ramah",
                "pesan": "tetap semangat kak dalam perkuliahannya"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya ceria, berbaur dan seru",
                "pesan": "selalu ceria seperti ini kak, semangat terus!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "kakaknya pendengar yang baik, seru dan pengertian",
                "pesan": "sukses terus kak, semangat kuliahnya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
    
if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aXw2G1iFlNfxxarID_vz708d-bssDICQ",
            "https://drive.google.com/uc?export=view&id=1W3u6U2SY0vxZI4LQ-3ybuoO0APhMqfvK",
            "https://drive.google.com/uc?export=view&id=1jQznbsU7nk4dKJyXkRdAas-LuddR1FQd",
            "https://drive.google.com/uc?export=view&id=1Z9htzCt6S6x-LWuB-QvnNcrWuffoTWtZ",
            "https://drive.google.com/uc?export=view&id=1b7Tz7TUcSAIXi8owXmAHVBNztYXYhbO8",
            "https://drive.google.com/uc?export=view&id=1cBkxD2vFCcPntrLHpxiuvbHX9O72DH6A",
            "https://drive.google.com/uc?export=view&id=1XnjAUTnIzcqA2sNYUlIDbXlg1lMMuFA-",
            "https://drive.google.com/uc?export=view&id=1TxhzHkDrYtJ9iNu4SLFF6orSvtXgcb4b",
            "https://drive.google.com/uc?export=view&id=1_PxjfAZW4qlb-mnTf1gxv8SXVEpULJQy",
            "https://drive.google.com/uc?export=view&id=1crndBDEIgPu07v7sZGowFPn8lRe94WEz",
            "https://drive.google.com/uc?export=view&id=1UcLAj5qKPgVU1HF7RGgRgOqf_b2lSVWQ",
            "https://drive.google.com/uc?export=view&id=1X-XIhOfeeB8-v2vty5kuF5XhXmj0Mekw",
            "https://drive.google.com/uc?export=view&id=1_0zI0O-wg3THiMpoLaNiiVrZQcWsqIz8",
            "https://drive.google.com/uc?export=view&id=1Vn4LRET-HY0sKAivltNnAcrbwPoSuSJB",
            "https://drive.google.com/uc?export=view&id=1VO4u-meQXUnhZDv6bfCYxH_POqGvNdQi",
            "https://drive.google.com/uc?export=view&id=1_vhGTK9ya3RZCC-7K4dALyXZ7BKFXQWn",
            "https://drive.google.com/uc?export=view&id=1_uKR5t9Q2bdAyPwCYdg3-L-A6VJy08tu",
            "https://drive.google.com/uc?export=view&id=1YaGy2yc1GGEaI9zJgroUZtmbWsG9kPYA",
    
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
                "kesan": "kakaknya asik banget, seru dan jago ngedit",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "ceria dan humoris, pasti menjadi moodbooster",  
                "pesan":"sehat selalu kak, jaga kesehatannya"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakaknya asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "abangnya asik saya suka belajar dengan dia",  
                "pesan":"sehat selalu bang, jangan lupa istirahat"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "humoris, baik dan asik",  
                "pesan":"jaga kesehatannya ya kak, lancar kuliahnya"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "kece banget bisa melukis, jago desain dan kreatif",  
                "pesan":"ajarin melukis kak, keren banget"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "kakaknya enak diajak berbincang, asik dan ramah",  
                "pesan":"semangat menjadi medkrafnya kak, jaga kesehatan selalu"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "kakaknya asik dan ramah",
                "pesan":"semangat terus kak, jaga kesehatan"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "asik, humoris dan ramah",  
                "pesan":"semangat kak, terus reminder penulisan nama kak hafsa"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "kakaknya seru dan asik diajak ngobrol",  
                "pesan":"bahagia selalu kak, semangat kuliahnya"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "kakaknya asik dan ramah",  
                "pesan":"semangat terus kuliahnya kakak, jaga kesehatannya"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi" : "Menulis, membaca, memasak",
                "sosmed" : "@nltg._",
                "kesan": "kakaknya ramah dan asik diajak ngobrol",  
                "pesan":"jaga kesehatannya kak, semangat kuliahnya"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "abangnya asik dan humoris",  
                "pesan":"semangat perkuliahannya bang, semangat"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "tegas, baik dan perhatian",  
                "pesan":"semangat terus kak, jaga kesehatan selalu btw kak info map robloks", 
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "kakaknya asik dan ramah",  
                "pesan":"bahagia selalu teman_teman"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "abangnya keliatan pinter banget, jago ngedit",  
                "pesan":"semoga bisa menjadi inspirasi buat adik-adik tingkat bang"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "kakaknya pinter banget, akrab dan seru",  
                "pesan":"tetap tersenyum kak"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "kerenn abangnya, PDD sejati",  
                "pesan":"semangat terus bang, jaga kesehatan yaa"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

# Tambahkan menu lainnya sesuai kebutuhan

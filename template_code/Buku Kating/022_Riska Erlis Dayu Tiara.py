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
            "https://drive.google.com/uc?export=view&id=14wXKui8Gw1LXY3vyzmfNzG4DU_RqEOBc",
            "https://drive.google.com/uc?export=view&id=14l1N_1vSxJXWceeMJw3apHz5Upp2O3sI",
            "https://drive.google.com/uc?export=view&id=14bNj8xOm6VFC3FZtNWMyU5qjDvb9WyWN",
            "https://drive.google.com/uc?export=view&id=14LLpC8yIepUsl9dVE8jA6C5gWPQL6bkc",
            "https://drive.google.com/uc?export=view&id=14mqEOiUvhhmhIgJ0C_GZ8RkJPv09o4u1",
            "https://drive.google.com/uc?export=view&id=14ox7sx2GJflj43kqnBjlamSpIPgMTh2L",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@endraa",
                "kesan": "abang keren dan berkarisma",  
                "pesan":"Semoga selalu diberi kemudahan dalam setiap urusan!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abangnya berwibawa dan bijak dalam bersikap",  
                "pesan":"Semoga makin sukses dan terus berkembang!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "24",
                "asal":"Baduy dalem",
                "alamat": "Airest Kost",
                "hobbi": "Makan kuaci",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya terlihat bersemangat dan positif",  
                "pesan":"Semoga terus sukses dan menginspirasi!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak punya aura positif",  
                "pesan":"Sukses terus dan semoga hal baik selalu menyertai!"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Wakatobi, Sulawesi Tenggara",
                "alamat": "Mutun, Pesawaran",
                "hobbi": "Ngomenin tiktok cewe cantik",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya keren dan berkarisma",  
                "pesan":"Semoga selalu diberi kemudahan dalam setiap urusan"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Gya Kost Kopri",
                "hobbi": "cute jenderal",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya ramah dan berwibawa",  
                "pesan":"Semoga terus semangat dan makin berprestasi!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11PxIbJfXtYyQugzcjF2FVFSeIkjVEo5e",
            "https://drive.google.com/uc?export=view&id=11dyqCgGi_KDumjRe0rCoTjVH1VBv8306",
            "https://drive.google.com/uc?export=view&id=111qoQ44QKt_suCxZlMze-fTIFldIey6J",
            "https://drive.google.com/uc?export=view&id=1JoFRUNfxvwQfmb1RySmJa0mvnAV2aMqW",
            "https://drive.google.com/uc?export=view&id=11EyeQosQ_WwMeiEymkjGqqxr00lFZ3Vh",
            "https://drive.google.com/uc?export=view&id=119voL39eO3w7fFBXsT6jjSpTHRD_TwOo",
            "https://drive.google.com/uc?export=view&id=11_FWhl6scCYUlbCOvHh7XLnPOvLbx5_4",
            "https://drive.google.com/uc?export=view&id=10VWLUyMfEPFjms4nn7uISpSBAme7aclB",
            "https://drive.google.com/uc?export=view&id=11Vhfd8YVDG3kOpbpuWrfQD32zmMeG-10",
            "https://drive.google.com/uc?export=view&id=115FrwaxAcgcZxvs_2BsyyeJBEyRgKl4C",
            "https://drive.google.com/uc?export=view&id=118LVG5k6-H85C4ln__JfG8MIq797Ov7t",
            "https://drive.google.com/uc?export=view&id=11ZmqG49ewJBaNRuU6uPN3kbQYg7KDEGA",
            "https://drive.google.com/uc?export=view&id=138VhwxVdRhYWxoqiWce7b2h2xOKX8b9B",
            "https://drive.google.com/uc?export=view&id=11ARZ3pQV3xO5m956ciF6cQhqQ4c0In6c",
            
             
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
                "kesan": "abangnya seru dan terarah",  
                "pesan":"Semoga selalu diberi kelancaran di tiap kegiatan"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "lomba ga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya santai tapi tetap berwibawa",  
                "pesan":"Semoga makin berkembang ke depannya"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Tidur",
                "sosmed": "@rnshism",
                "kesan": "Kakaknya punya aura positif",  
                "pesan":"Semoga semua urusan kakak berjalan lancar"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Ubud",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan baru",
                "sosmed": "@ansftynn",
                "kesan": "Kakaknya tenang dan menenangkan",  
                "pesan":"Semoga selalu dikelilingi hal-hal baik"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "lupa bales chat",
                "sosmed": "@dhruchyo",
                "kesan": "abangnya berwawasan dan bijak",  
                "pesan":"Semoga terus menginspirasi banyak orang"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak Sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya kalem dan sopan",  
                "pesan":"Semoga selalu sukses dan bahagia"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "Kakaknya tenang dan menenangkan",  
                "pesan":"Semoga selalu dikelilingi hal-hal baik!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerawat Kucing",
                "sosmed": "@myrrin",
                "kesan": "abang berwibawa dan disiplin",  
                "pesan":"Semoga makin sukses dan selalu diberkahi"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya positif dan menyenangkan",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya santun dan easy going",  
                "pesan":"Semoga selalu membawa energi positif"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "GH",
                "hobbi": "main paddle",
                "sosmed": "@iamridho",
                "kesan": "abangnya sederhana tapi berkesan",  
                "pesan":"Semoga selalu dimudahkan segala urusannya"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Bangka Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "koleksi batch google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya berkarisma dan tegas",  
                "pesan":"Semoga makin sukses ke depannya!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak terlihat tenang dan bijak",  
                "pesan":"Semoga selalu diberi kemudahan dalam setiap urusan"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Kota Farakan",
                "alamat": "Belwis",
                "hobbi": "nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya rendah hati dan menyenangkan",  
                "pesan":"Semoga selalu diberkahi di setiap langkahnya"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
    
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14-djonho4tkp3Lx_NbueIDWJV1KYqnCX",
            "https://drive.google.com/uc?export=view&id=14-YtZmQ_VedNsGq10sLZvbjjGwm6ryGD",
            "https://drive.google.com/uc?export=view&id=143aA6E_1El8r-KZpY0B1FT4knGFc7pZV,
            "https://drive.google.com/uc?export=view&id=146Ywf476AovBKEeD66ltbqLuh_34SIDF",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "lagu, nanyi, baca, game, rapat",
                "sosmed": "@bintangtwinkle",
                "kesan": "abangnya punya semangat yang tinggi",  
                "pesan":"Semoga semangat itu terus menyala"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakaknya tenang dan positif",  
                "pesan":"Semoga selalu sukses dan bahagia"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "main",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya rendah hati dan menyenangkan",  
                "pesan":"Semoga selalu diberkahi di setiap langkahnya"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450069",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya tenang dan positif",  
                "pesan":"Semoga selalu sukses dan bahagia"# 1
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15AlIoKzVznuqaJ8Shm8AI_p6evDZn5rQ",
            "https://drive.google.com/uc?export=view&id=11dyqCgGi_KDumjRe0rCoTjVH1VBv8306",
            "https://drive.google.com/uc?export=view&id=111qoQ44QKt_suCxZlMze-fTIFldIey6J",
            "https://drive.google.com/uc?export=view&id=1JoFRUNfxvwQfmb1RySmJa0mvnAV2aMqW",
            "https://drive.google.com/uc?export=view&id=11EyeQosQ_WwMeiEymkjGqqxr00lFZ3Vh",
            "https://drive.google.com/uc?export=view&id=119voL39eO3w7fFBXsT6jjSpTHRD_TwOo",
            "https://drive.google.com/uc?export=view&id=11_FWhl6scCYUlbCOvHh7XLnPOvLbx5_4",
            "https://drive.google.com/uc?export=view&id=10VWLUyMfEPFjms4nn7uISpSBAme7aclB",
            "https://drive.google.com/uc?export=view&id=11Vhfd8YVDG3kOpbpuWrfQD32zmMeG-10",
            "https://drive.google.com/uc?export=view&id=115FrwaxAcgcZxvs_2BsyyeJBEyRgKl4C",
            "https://drive.google.com/uc?export=view&id=118LVG5k6-H85C4ln__JfG8MIq797Ov7t",
            "https://drive.google.com/uc?export=view&id=11ZmqG49ewJBaNRuU6uPN3kbQYg7KDEGA",
            "https://drive.google.com/uc?export=view&id=138VhwxVdRhYWxoqiWce7b2h2xOKX8b9B",
            "https://drive.google.com/uc?export=view&id=11ARZ3pQV3xO5m956ciF6cQhqQ4c0In6c",
            
             
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berenang",
                "sosmed": "@randaandriana_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450079",
                "umur": "19,
                "asal":"Palembang",
                "alamat": "Jl. Permaddi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala mider",
                "hobbi": "lupa jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "21",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Pramuka,Bandar Lampung",
                "alamat": "Perum Bukit Alam permai 3, Blok c. No. 9",
                "hobbi": "dengerin musik",
                "sosmed": "@keyashafi_",
                "kesan": "_",  
                "pesan":"_"# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bumisari Kec. Natar",
                "hobbi": "dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "Main piano, nyanyi",
                "sosmed": "@",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "tidur",
                "sosmed": "@tvnty_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang(main game)",
                "sosmed": "@fifah.zy",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer), tidur, jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "main game",
                "sosmed": "@giofaniars_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya, Lampung Selatan",
                "hobbi": "main catur",
                "sosmed": "@_rhmaokktvia",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans sakum, Belwis",
                "hobbi": "futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    DepatemenMIKFES()







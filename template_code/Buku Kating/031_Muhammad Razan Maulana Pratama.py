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
            "nav-link-selected": {"background-color": "#FF6F00"},
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
            "https://drive.google.com/uc?export=view&id=1l59a1EhP_9kx7lJ74RAIwypZZcmLdk8c",
            "https://drive.google.com/uc?export=view&id=1e0r1Di1wCLHHrRQc5lUg1QsKRYipZHnY",
            "https://drive.google.com/uc?export=view&id=1-5KqZNlWnwNkNxeDJ4QEMbe8OB96YRlH",
            "https://drive.google.com/uc?export=view&id=1CAw-qWbsy5XrsegjtuS_5W1xJUUD-avi",
            "https://drive.google.com/uc?export=view&id=1YAPy0IIyxMOAUqVB0TxjZpzms5rpCJ81",
            "https://drive.google.com/uc?export=view&id=1vj3WEYec1A7yokmtNmzcH4cdsug6dr9G"
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
                "kesan": "Keren dan ramah, Bang Rendra kalo di ajak ngobrol juga santai jadi enak",  
                "pesan":"Semangat Bang kuliahnya dan sehat terus, semoga tercapai target nya"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanngerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "Bang Jo keliatan nya serem tapi kalo udah kenal jadi enak dan seru ngobrol bareng",  
                "pesan":"Semangat terus Bang kuliahnya sehat-sehat selalu bang, semoga apa yang diharapkan tercapai"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak Elisabeth ini seru, lucu, dan kocak. Apalagi pas ramah tamah sama Teknik Perkeretaapian",  
                "pesan":"Semangat terus kuliahnya kak, sehat terus dan apa yang di inginkan semoga tercapai"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini cantik, baik, dan ramah.",  
                "pesan":"Semangat dan sehat terus kak, semoga semua urusannya di permudah"# 1
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak Eksanty seru dan ramah banget pas ngomong",  
                "pesan":"Semangat dan sehat terus kuliahnya ka, Semoga hal apapun yang kakak hadapi di permudah"# 1
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak nya asik dan seru, keliatannya serem tapi baik kalo kenal",  
                "pesan":"Semangat terus kuliahnya ka, dan sehat-sehat selalu. Semoga tercapai apa yang diharapkan dan dipermudahkan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lUOdyiXq7lpp0Qo1bS6KiWYtwFbJQP6D",#1
            "https://drive.google.com/uc?export=view&id=11hVpINSF1hNPAPYxTDYlpz5xXQLUmQEb",#2
            "https://drive.google.com/uc?export=view&id=1DCwTwzBUvKOkAe-EAqLz0_B1vkicXGhP",#3
            "https://drive.google.com/uc?export=view&id=1YaZJniXXl1psNaQ9lB8xTFM4aaFKy91v",#4
            "https://drive.google.com/uc?export=view&id=13qQ_tBrdwff-TQiVY98DdFa2K0tfnya8",#5
            "https://drive.google.com/uc?export=view&id=1FYuFW2FtsxwVNYc-XC3XHNf8LCRpdHhV",#6
            "https://drive.google.com/uc?export=view&id=1mej2fYHssiDHRqbOQ8YGY2f_MAG8-9e7",#7
            "https://drive.google.com/uc?export=view&id=1AP85fair6XscZoLdzuNgGgCMAfg3BlgB",#8
            "https://drive.google.com/uc?export=view&id=1dLXT807PHnyFiAat4zkCvc-fmqgHn7xn",#9
            "https://drive.google.com/uc?export=view&id=1izjfETxv4gpms1jV7i6mVmVU-9LwoGeN",#10
            "https://drive.google.com/uc?export=view&id=1R99zp0Lb5a95ECHlkFIu28L5WGIOMXT1",#11
            "https://drive.google.com/uc?export=view&id=1FIigeFIWRrNy5_AKngfE2Bif3RHaW-IQ",#12
            "https://drive.google.com/uc?export=view&id=1L6YK0DsVX4nP6WjB2g1C4p47nVMZm9Oq",#13
            "https://drive.google.com/uc?export=view&id=1v7CWCM-dl5T2QETWC2w0Po9aqNF1n9_D" #14
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
                "kesan": "Bang Jer ini keren banget keliatannya, apalagi pas jadi pemandu sosok ganteng nya keliatan",  
                "pesan": "Semangat terus Bang kuliahnya dan tetep jaga kesehatan, Semoga apa yang diharapkan tercapai dan dimudahkan"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.deamalia",
                "kesan": "Kakak nya asik, seru dan baik banget, keliatan santai dan calm nya",  
                "pesan": "Sehat dan semangat terus ka, jaga kesehatan kakak dan semoga dilancarkan apapun urusannya"# 2
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakak nya cantik, seru, baik banget",  
                "pesan":"Sehat dan semangat terus ka, jaga kesehatan kakak dan semoga dipermudah urusannya"# 3
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@anisafitriani_01",
                "kesan": "Kakak Anisa sangat baik dan ramah, terus seru juga",
                "pesan": "Semangat terus kuliahnya kakak dan jangan lupa jaga kesehatannya. Semoga dipermudah urusannya"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nyuci baju",
                "sosmed": "dhruchyo",
                "kesan": "Bang Dharu orang nya lucu, imut, dan baik. Pokoknya kereng deh bang Dharu apalagi pas jadi MC FG SD 24",
                "pesan": "Sehat-sehat terus bang, dan jangan lupa sama tugas kuliahnya. Semoga dilancarkan urusannya baik di kuliah maupun di luar"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Ngulek cabe",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakak Feby baik, cantik, dan ramah. Warna rambutnya unik jadi keliatan berbeda dari yang lain",
                "pesan": "Semangat dan sehat terus ya kak, semoga dipermudah dan lancar urusannya."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin Ridho maen padel",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro itu baik dan ramah, awal liat Bang Givaro itu kayak abang-abang gym.",
                "pesan": "Semangat Bang kuliahnya, jaga kesehatan ya bang dan semoga diperlancar perkuliahannya"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "1234500118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan ini baik dan ramah, dari vibes nya keliatan orang cool dan pinter.",
                "pesan": "Semangat dan sehat terus yang Bang, Semoga diperlancarkan urusannya"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "123450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak Berliana itu baik dan ramah, kalo ngomong itu lembut banget",
                "pesan": "Sehat dan semangat terus ya kak kuliahnya, Semoga dipermudah urusannya"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengar Wave to Earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik, seru, dan suka banget ngobrol jadi seru banget pas wawancara.",
                "pesan": "Sehat dan semangat terus ya kak, semoga di permudah kuliahnya."
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho ini keliatan banget ganteng dan coolnya! punya aura cowo keren gitu.",
                "pesan": "semangat terus kuliahnya Bang dan jaga kesehatan nya, "
            },
            {
                "nama": "Feryadi Tulus",
                "nim": "123450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Bang Feryadi keliatannya kaya muka orang komdis, tapi dia baik, seru dan ramah.",
                "pesan": "semangat terus kuliahnya Bang, dan jaga kesehatnnya"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg",
                "kesan": "Ka Monica orangnya manis dan menyenangkan! Kakanya nya juga seru dan baik.",
                "pesan": "Sehat terus ya kak, semangat kuliahnya. Semoga dipermudah kuliahnya dan yang lain nya"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Fafa",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa ini orang nya baik, ramah, dan lucu. Muka nya tampak kayak lemes tapi asli nya penuh semangat",
                "pesan": "Semangat terus kuliahnya ka, jaga kesehatannya dan tetep jadi yang lucu ya ka "
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yxov3u4K7fnE_n10QNsO8DAx4Tk5Mspy",
            "https://drive.google.com/uc?export=view&id=1OJa01k8g6Slg-sTr3h-nWfYH-UxPu53f",
            "https://drive.google.com/uc?export=view&id=1Ghw-pCCY4SixrfMuFCJtqEshb2WRt_d4",
            "https://drive.google.com/uc?export=view&id=1CO7oTZOhh3gLvDxlQZ_T_4lyuI98KZKx",
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
                "kesan": "Baik banget Bang bintang, mengonspirasi banget dan seruu juga sama Bang Bintang",  
                "pesan": "Semangat terus kuliahnya Bang, jaga kesehatannya dan tetep jadi yang lucu ya Bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Maen Roblok",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak Nadya asik dan seru banget, kakak nya juga baik dan ramah",  
                "pesan":"Semangat dan sehat terus ya kak, semoga dipermudah dan dilancarkan urusannya."# 2
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Like Instagram",
                "sosmed": "@fatinahnazzh",
                "kesan": "Kakak nya kalem dan tenang banget jadi keliatan santainya, kakanya juga baik dan ramah",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 3
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "Semangat terus kuliahnya kakak dan jangan lupa jaga kesehatannya. Semoga dipermudah urusannya"# 4
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14ZLl6u4Kq--sqMNG8m5C3na6FMAHtv9H",#1
            "https://drive.google.com/uc?export=view&id=1yYjMWovA19R7UJbFGg5Bou2hlXbdc2XS",#2
            "https://drive.google.com/uc?export=view&id=11_tX-VhLC0OU8GT3kQcReAiToUQXzGcx",#3
            "https://drive.google.com/uc?export=view&id=1rGIchf8Cgkj_8bfA2WouL7_tK0-Tt0p9",#4
            "https://drive.google.com/uc?export=view&id=1IHloZLiAhWx98N1mgujAceRNa-ULqr9b",#5
            "https://drive.google.com/uc?export=view&id=1rjNC0SKbih7c4gr7SDy5UMJgYZp0mDoI",#6
            "https://drive.google.com/uc?export=view&id=1eJjli4XpRZRyQ3FNg-F9JEfWTHBpGhvC",#7
            "https://drive.google.com/uc?export=view&id=1jYtfROOqonrqHc9HJZb0q-e3ZsFsART8",#8
            "https://drive.google.com/uc?export=view&id=1kMNvpC5POciiVGMFTOLdpDiHTJCnU7JA",#9
            "https://drive.google.com/uc?export=view&id=1p36kOfhh7l22hZgPL7VQ90Eclc5arr5M",#10
            "https://drive.google.com/uc?export=view&id=1Gs37-asBOptZnPY2mZ7_LwW9CSu6uyy_",#11
            "https://drive.google.com/uc?export=view&id=14EMn9rNsFwlUD65TDAH-29n_nheW1B-d",#12
            "https://drive.google.com/uc?export=view&id=1G0zM-yXPZIohYETgO5peI77Yg8teVHuk",#13
            "https://drive.google.com/uc?export=view&id=11MRejHo3mLGdZXI6td8VNjjDZGzdQohW",#14
            "https://drive.google.com/uc?export=view&id=1cd5PeSl5WmWg4jC8ZddgpbezzMj6GSpd",#15
            "https://drive.google.com/uc?export=view&id=1mLR16OAWl5-GYBgJi_BiT0-3axgTzFF3",#16
            "https://drive.google.com/uc?export=view&id=15RIOjdFMOrwLVGBF8o2j8Aygt03p3iHE",#17
            "https://drive.google.com/uc?export=view&id=1X-Vd9giz8I-11GQRGbxdm7pN9oy3AU73",#18
            "https://drive.google.com/uc?export=view&id=1CIcfTe46kVa2VVPdhVNiP2vcQWpCE7_A",#19
            "https://drive.google.com/uc?export=view&id=1DVzji0SGKBG0Sq34oAlNz_ZoznmSCOOy",#20
            "https://drive.google.com/uc?export=view&id=1zZ9OSYrnRSZFJDI3AOfVA4L5Tqhuz04T",#21
            "https://drive.google.com/uc?export=view&id=1nfSRAAlSm7G3SkGD_8FNE3KtlGvXLblM",#22
            "https://drive.google.com/uc?export=view&id=1HTigz752TFLPBDm91nfYE997-PGh6tU6",#23
            "https://drive.google.com/uc?export=view&id=1a1PnQXDfID7SNRlWbXkiMTbbhMrjfzZb",#24
            "https://drive.google.com/uc?export=view&id=1_NikbOlDxssoNJY6kvhhTepD_fPU9uqO",#25
            "https://drive.google.com/uc?export=view&id=1GAU5xyWlaGwwuQw6osu3r6cUFvMUwrhL",#26
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

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WUdHRQJfypSpyXOkhCz5wLzzncJ5jogI",#1
            "https://drive.google.com/uc?export=view&id=1Bt5R8DDow6ahkExxcDsDSjCCZ-QdRkOu",#2
            "https://drive.google.com/uc?export=view&id=1AC0Jflbvkt-Fq-9lK02gMRYMADdZN74m",#3
            "https://drive.google.com/uc?export=view&id=1AVAnqCrLPLjHq5doEUtEX15H5AITYXrS",#4
            "https://drive.google.com/uc?export=view&id=1R-Zi8hVTAhKXwGRm6UDpdTxtycLdA39f",#5
            "https://drive.google.com/uc?export=view&id=1C4kEoDpYYZOKtpOYj5sUUlprGbi7iQUU",#6
            "https://drive.google.com/uc?export=view&id=1j7EgeYOlruuuOoZzHcpiJqBHfjXpkihV",#7
            "https://drive.google.com/uc?export=view&id=1IepOqYgAZwxvmDtCAdV3zahOdnPbAytR",#8
            "https://drive.google.com/uc?export=view&id=1hpGLK0wzIiF-Wi20LIibjReA5HlIQQJh",#9
            "https://drive.google.com/uc?export=view&id=1trq4lEtPHdevruH28lNj01bc6GlPC8pK",#10
            "https://drive.google.com/uc?export=view&id=1-xOmA_SGNaNG9j8Yytyyw3fCm4N3Sx2h",#11
            "https://drive.google.com/uc?export=view&id=1PAYzG0nPL0CJUA7Mrx7qqCeIqyXQT7EM",#12
            "https://drive.google.com/uc?export=view&id=1wAWwh5uHd3PTfIS5dDJnB9PnhV0WfaaG",#13
            "https://drive.google.com/uc?export=view&id=1pga-O6YaHHSnS-4iBAqr6mP0vzMfjZG3",#14
            "https://drive.google.com/uc?export=view&id=19IhE9cm4xcc_4VEpl9qNINiNH0OcLD3U",#15
            "https://drive.google.com/uc?export=view&id=1XqSQhIisGmhcDMxZbYq7RO2qxi2yAQJR",#16
            "https://drive.google.com/uc?export=view&id=1nUhK8gwDJxidlSpBOv6u39zem6K-BvM3",#17
            "https://drive.google.com/uc?export=view&id=1o6hGdauCPCeHFqu1jHFovs4jL70fUCtH",#18
            "https://drive.google.com/uc?export=view&id=1nV6PZ698DlJvCXBW3ZAm9jgBQFd9JWkF",#19
            "https://drive.google.com/uc?export=view&id=1w4szdmpczKKKns9mGqKbkjlLGan988MN",#20
            "https://drive.google.com/uc?export=view&id=1qsfqNwxX30SC-BydFERf1S1hPeWsDRL1",#21
            "https://drive.google.com/uc?export=view&id=1UASsKe2yaFJWJAVnXjFW-vWOPQ2tnMLL",#22
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
                "kesan": "Bang Randa tampak nya kaya orang yang jago coding, Abang nya juga ramah, baik dan soft spoken",
                "pesan": "Semangat terus yaa Bang kuliahnya dan jangan lupa jaga kesehatannya. Semoga dipermudah dan dilancarkan urusannya"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Nangka 3",
                "hobbi": "Membaca Abstrak",
                "sosmed": "@junitaa_0406",
                "kesan": "kakanya baik dan ramah, dari tampaknya keliatan pinter pas tau hobinya baca abstrak udah keliatan pinter nya",
                "pesan": "Sehat dan semangat terus ka, jaga kesehatan kakak dan semoga dilancarkan apapun urusannya"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "bang regi tampaknya keren banget, kaya terasa gitu vibes cool nya tapi dia baik dan ramah banget",
                "pesan": "Semangat terus Bang kuliahnya sehat-sehat selalu bang, semoga apa yang diharapkan tercapai"
            },
            {
                "nama": "Aisyah Musrifah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segair Midea",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiafarj",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka, Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, dengerin musik, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefiilidefi",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450024",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Gajah Mada, Tanjungkarang",
                "hobbi": "Bernyanyi dan denger musik",
                "sosmed": "@fabiollacharissa",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Main game dan makan",
                "sosmed": "@tvnty_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123440104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai no.27A, Kedaton",
                "hobbi": "Jalan-jalan, main game, tidur",
                "sosmed": "@biyokcb",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450039",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T_Qu0peMbovdAZRWCKOsjFaudcaJBI74",
            "https://drive.google.com/uc?export=view&id=1qZCnwq0-RgTvjYpFU4mocmH0bZXoHQnS",
            "https://drive.google.com/uc?export=view&id=1dlzi1LjtgzEpwcLlkvxt9SIr2CN1I603",
            "https://drive.google.com/uc?export=view&id=1M6sH4jKUfzEc7n468ACUSjZ3Gvk0-XZi",
            "https://drive.google.com/uc?export=view&id=11V269uWXXvDPBHiTFLm2AMMfuLfpIbl7",
            "https://drive.google.com/uc?export=view&id=1Pd1auS5q14M6sovSVAGBdEZtyQXVPoKp",
            "https://drive.google.com/uc?export=view&id=1muHybWF5QIKDoLiZZHle_5_QmIUJwisN",
            "https://drive.google.com/uc?export=view&id=1D0s0iSyeDj7E3KLTX6jR-o81u3l9OBe-",
            "https://drive.google.com/uc?export=view&id=1JhB9_427CRGT2FOSn1dSBR_yWNDizC3b",
            "https://drive.google.com/uc?export=view&id=1JT6hAw0W3GyXGEZGYqgLBIhGJKNpfHri",
            "https://drive.google.com/uc?export=view&id=1e6N4NNNNS5157E8-ESIUiTR1KlQ-u8MF",
            "https://drive.google.com/uc?export=view&id=1xRaGDKOZ_H8usz3FW4sqk4l6W63UXHn7",
            "https://drive.google.com/uc?export=view&id=155XU5yzpV5oBP_mcIhyvkYzbCmiEHMYc",
            "https://drive.google.com/uc?export=view&id=1PtCkKzc6kb8iRvPU03ziv6td69pUDH63",
            "https://drive.google.com/uc?export=view&id=1pU0hUqeH2Iv2PS7_T64wO1azr8osFMS6",
            "https://drive.google.com/uc?export=view&id=1GosLpAcXcienkgS4PR5bNkCNGGMNW5aO",
            "https://drive.google.com/uc?export=view&id=1LiM0icI3elXDoCck9rVm3S0V_tAlxEh9",
            "https://drive.google.com/uc?export=view&id=13TacR41rAeu39DL540e26I-STUnIPqk4",
            "https://drive.google.com/uc?export=view&id=1QnqP1ztbO39iwxLaH727s1GoNNTEZFe1",
            "https://drive.google.com/uc?export=view&id=1BQmpgDmfLVVZjuf4N3knNj2zWhaM4P9w",
            "https://drive.google.com/uc?export=view&id=14WW-iyxvE9avzlnUovS5gmF2hHsf9RIz",
            "https://drive.google.com/uc?export=view&id=1E_K0QOdJAkm5hSBgLjXsAa-s86ytV0Rt",
            "https://drive.google.com/uc?export=view&id=1vGn-P832S90JBhULlP5D3vjEalhSYqV5",
            "https://drive.google.com/uc?export=view&id=1wPsmGvRWyjXigo96E57UQ7Sk0omYP3tM",
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
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
           {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
           {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan jalan",
                "sosmed": "@bylaash",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsni",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylaaura",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450016",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpei",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3__",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like Crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonya",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitkin Ketang",
                "sosmed": "@luthfiaaramdhni",
                "kesan": "keren banget banggg bisa jadi",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziivan",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Khazanati Ilmi",
                "nim": "123440053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lamsel",
                "sosmed": "@tari_sya",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1C67hS2dk3kNMyjPq6to8laOmSr_-9alj",
            "https://drive.google.com/uc?export=view&id=1VEcVs4ii4hbkG7BPD1_cuB67L3zpeUvB",
            "https://drive.google.com/uc?export=view&id=1zoFM3rz2BfwRIBrgnoljJx2OFsC4achL",
            "https://drive.google.com/uc?export=view&id=1CJsiDFlu6TJZgdqNCRHepHXrJx9U-I8N",
            "https://drive.google.com/uc?export=view&id=1o-WmrDV3YzdOVghyWczUhJG56K8ujBmr",
            "https://drive.google.com/uc?export=view&id=1qlVUyk3_HQeaWPiPvUa5BuaWB3lFKTiZ",
            "https://drive.google.com/uc?export=view&id=1Af7MweMm_K7cEFuUYW-1J-GfupXSuc5_",
            "https://drive.google.com/uc?export=view&id=1eMZPeMdke0czjjZ2lJ9suwvfAgsE4py-",
            "https://drive.google.com/uc?export=view&id=1xIPBUsmrS0NhziWrZ1B-tCwD-WqLSmFK",
            "https://drive.google.com/uc?export=view&id=10DRo5E8d1HO9BG5Pd4M1n2RLNLatQluH",
            "https://drive.google.com/uc?export=view&id=1pT4dd1bR6wMmASYa9XJ0WM1B09g1gFd7",
            "https://drive.google.com/uc?export=view&id=1A744TQIPdogE5fexwJElNyLhiGSTrvcG",
            "https://drive.google.com/uc?export=view&id=1wiLJc61y2CDqS579A9BKFCcmQ9By2zjU",
            "https://drive.google.com/uc?export=view&id=11nhoy-2bD1qdOwotnyA9VgaCEYtHQix7",
            "https://drive.google.com/uc?export=view&id=1Pa0hrUNiCX0YXbVyrcUIrC0LnWe7U1YJ",
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
                "kesan": "keren banget banggg bisa jadi ",  
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
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 3
            },
            {
                "nama": "Rendy",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "may_dahlia12",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10wK2IRHVMNxs9CxNxe3lMfsctZWIhkgG",
            "https://drive.google.com/uc?export=view&id=1QYjLRnVtndCCN0IKZDSMjdgXhLG1WJR3",
            "https://drive.google.com/uc?export=view&id=1Ob_jTJJp8-pS0giXz0JiH2ASgF7BA2Ue",
            "https://drive.google.com/uc?export=view&id=1Dto2mzZRyPVVgrqVShV-clQSrrO4pFnJ",
            "https://drive.google.com/uc?export=view&id=1611k7LTKT0IAnxUUFwtEsiJaeC2TKyJ5",
            "https://drive.google.com/uc?export=view&id=1J9oZQNOyq38JoA4nPtge7LiEC2tt8DzL",
            "https://drive.google.com/uc?export=view&id=1qev_SL-LvCrlU9rwmtAbeBDhitXSfYpk",
            "https://drive.google.com/uc?export=view&id=1g7xRCmWIXtCMzvjBBAog8qnXRBHIFCda",
            "https://drive.google.com/uc?export=view&id=1o0FYjPOpV3IAzf00CrhhM-A2KUBKT9Ji",
            "https://drive.google.com/uc?export=view&id=1Eo1skAA-qDkT1mzf80KaF6LoVnUMVVgZ",
            "https://drive.google.com/uc?export=view&id=10Jr6ak_sGwY2C81NxqraYUYOcnvjFai-",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "keren banget banggg bisa jadi ",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NASFmw5J0L-5tcqUxDZGT2pPJbzxBzgW",
            "https://drive.google.com/uc?export=view&id=1u0X2_PKpxiapTNCn7EDZ5LXBewNZ2LhS",
            "https://drive.google.com/uc?export=view&id=1qHj75cpdoP7ViBfG2_ZuwipmUUUXi-3J",
            "https://drive.google.com/uc?export=view&id=1fOvKSxcqgC8Kb6Xu71R_mKXnKfPpkwak",
            "https://drive.google.com/uc?export=view&id=1KqSamg1Ag7YfKzMqjMYs16L5dXIH5jRD",
            "https://drive.google.com/uc?export=view&id=1MAyVuH2nCvyyzV3S-tpc-8lG8M4dG1tz",
            "https://drive.google.com/uc?export=view&id=1FhVi0m-PEvr_0lfZtBn_9i2mkGtqa3JQ",
            "https://drive.google.com/uc?export=view&id=18c6X-0geRoJcNeYMMMUpBAkTtEJ60c0c",
            "https://drive.google.com/uc?export=view&id=1StBny85arJDMp-pbt12dmiGM90cW5lPH",
            "https://drive.google.com/uc?export=view&id=1EkteDk7-O_nHItCo3G3E1Tb-_OfKGpJt",
            "https://drive.google.com/uc?export=view&id=1qDF5O3UnIcTghhkhmDSLvfBbcq7FFvJK",
            "https://drive.google.com/uc?export=view&id=1TR9usdMVwuzKewNmi6EFlvn6uLOKeT9f",
            "https://drive.google.com/uc?export=view&id=1STLNCW4EQrow7-YqQ8TFJgOqu6ecBIBd",
            "https://drive.google.com/uc?export=view&id=1d-Ce33hKC1XzW66d0ddJYq6fd-fsJl35",
            "https://drive.google.com/uc?export=view&id=1RfLvrXIdV4K69SDh0kfUHVpbAoc3Gu9K",
            "https://drive.google.com/uc?export=view&id=1y08VG1j1L8pMlko97c7n8v_Lzml4Hbqe",
            "https://drive.google.com/uc?export=view&id=1vzv1C6mFjONuqBQDwTKHpv_rKpIezQWB",
            "https://drive.google.com/uc?export=view&id=15OI43b4V9AvVXJCpeRxz_DPBHVZ8lq73",
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
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jl. Kresna, Korpri",
                "hobbi": "masak",
                "sosmed": "@rahmaneliyana",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 2
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "billiard dan volly",
                "sosmed": "@mananam__",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 3
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruu",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 4
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaengga_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 5
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 7
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati Raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 8
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 9
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 10
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsa.fazila",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 11
            },
            {
                "nama": "Nayla Salsabila Fathiansia",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumbar",
                "alamat": "Jl. Lapas, Kec. Jati Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 12
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main Roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 13
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450144",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 14
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, menulis, memasak",
                "sosmed": "@n1tg._",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 15
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450028",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastrn",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 16
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmw",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 17
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "keren banget banggg bisa jadi ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
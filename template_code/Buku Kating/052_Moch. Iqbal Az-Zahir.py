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
# sss
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1raJs9jl9lRH_uXDa-zvEahnIpVGmYQfD",
            "https://drive.google.com/uc?export=view&id=1nsw4dSdxhoYLYBHqLCCl7-itIb2UCwM9",
            "https://drive.google.com/uc?export=view&id=1Xpj686MS9YMA4h2Zh2hLYHP5MvdUeZaz",
            "https://drive.google.com/uc?export=view&id=1v61dGBOHfg7uBKsGAliC-kOOLr2VckDz",
            "https://drive.google.com/uc?export=view&id=1nSAbDLAvG3VYM8zadbrAVf_3NgQmaumR",
            "https://drive.google.com/uc?export=view&id=1COdHLghT9LQ1lcv_nT5zix_zuSdaDzkb",
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
                "kesan": "Walaupun dibilang baru kenal bang rendra, tapi saya liatnya abang keliatan ramah dan berwibawa",
                "pesan": "Semoga bisa sering sharing dan ngobrol santai lagi ke depannya ya, Bang.."
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Awalnya ngira abang bakal serius, ternyata lucu juga pas udah ngobrol",
                "pesan": "Semoga nanti bisa sharing pengalaman kuliah bareng bang"
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya ramah banget, langsung bikin suasana cair",
                "pesan": "Terus pertahankan sifat ramah itu ya kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Baru ketemu tapi langsung dapet kesan positif dari cara kakak bersikap",
                "pesan": "Sehat dan sukses selalu, Kak.."
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Walau pertemuan singkat, tapi kakaknya ninggalin kesan baik banget",
                "pesan": "Semoga silaturahmi ini bisa berlanjut terus, Kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak keren tapi tetap rendah hati",
                "pesan": "Semoga selalu dijaga sifat itu sampai kapan pun"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UCrPkKll25KftLtrxDqGrhPQd8fUY84r",
            "https://drive.google.com/uc?export=view&id=1dNocmy7U8KZOmPAwzCc-ffs23EVnTCGG",
            "https://drive.google.com/uc?export=view&id=1vfgXyD8Fahp893KefZnGV63X94lJnaQM",
            "https://drive.google.com/uc?export=view&id=1UDclbvlMenx5HNhZM0KT-rgbgGB1NWsg",
            "https://drive.google.com/uc?export=view&id=1zUwjHlPJ3H2JOPolWaNWIEFS4eWI0HbT",
            "https://drive.google.com/uc?export=view&id=1LJwMswvXWXzDf8Jly1Zua6HURSWTRUBH",
            "https://drive.google.com/uc?export=view&id=1Md0W4i0x-lqe3Iw72vNSYrrq92yjaauK",
            "https://drive.google.com/uc?export=view&id=1JrXmw0S7h0sykzH2YWvUteshArgZoLUq",
            "https://drive.google.com/uc?export=view&id=1mBg7JCOLyHb8f_Oeo2GGBwlEM6HlXwiQ",
            "https://drive.google.com/uc?export=view&id=1QTGYhv8pq1j-jv1lR16Get6fhzeXTaNj",
            "https://drive.google.com/uc?export=view&id=1YRnhYQm9vj8BSUihJnBCZbJPQXjfWa3L",
            "https://drive.google.com/uc?export=view&id=1VU3C2syGZivNabwQvYudPed3-Y7zkjLk",
            "https://drive.google.com/uc?export=view&id=1MqYbBVPSEcxJ1l1r9RUhQUhsf9kuYxAA",
            "https://drive.google.com/uc?export=view&id=1ft_nCaZhdOdPKae1bygxCza62jNJ76dr",
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
                "kesan": "Gaya bicara abang santai, tapi selalu ada makna di baliknya",
                "pesan": "Makasih udah mau berbagi pengalaman, semoga sehat selalu ya bang"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Awalnya agak sungkan, tapi ternyata kakak asik banget diajak ngobrol",
                "pesan": "Semoga selalu semangat dan gak lupa istirahat ya kak"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya keliatan tegas tapi tetap ramah",
                "pesan": "Semoga bisa terus jadi contoh buat kami ya kak"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Kakak keliatan tegas tapi tetap sopan dan santai",
                "pesan": "Semoga bisa jadi contoh yang baik buat kami yang baru mulai belajar"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Gaya abang yang sederhana justru bikin respect makin tinggi",
                "pesan": "Tetap rendah hati ya bang, itu yang bikin beda"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "Dari cara bicara aja udah keliatan kalau kakak orangnya bijak",
                "pesan": "Semoga bisa terus belajar banyak dari pengalaman kakak"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Baru kenal sebentar aja, tapi udah kerasa vibe positif dari abang",
                "pesan": "Jangan bosan kalo nanti kami sering minta arahan bang"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Gaya abang yang santai bikin suasana adem",
                "pesan": "emoga kita bisa sering ngobrol lagi bang"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak punya aura yang bikin nyaman semua orang di sekitarnya",
                "pesan": "Semoga kakak selalu dikelilingi hal-hal baik juga"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya punya pembawaan yang elegan banget",
                "pesan": "Semoga terus jadi sosok yang menginspirasi kak"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang kelihatan keren bukan cuma dari gaya, tapi juga dari sikap",
                "pesan": "Tetap rendah hati ya bang, sehat selalu.."
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Abang kayak punya banyak pengalaman menarik",
                "pesan": "Kapan-kapan cerita lebih banyak lagi ya bang"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya suka banget berbagi cerita yang bermanfaat",
                "pesan": "Makasih udah jadi sumber inspirasi kak"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya punya aura yang tenang tapi kuat",
                "pesan": "Semoga kakak selalu diberi kekuatan di tiap langkah"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ePFq5fup7onWqO9tZf5fk_4MVd-6RvxH",
            "https://drive.google.com/uc?export=view&id=17-Hsz1aTmVKqykKGinz5efcU7DiX7rlD",
            "https://drive.google.com/uc?export=view&id=16Gk7BVHbdzDWpuDSUfIH0iH8dT7qd6o7",
            "https://drive.google.com/uc?export=view&id=1EiNwt791MGe8uIJo7XBQXAXMfinFnc_6",  
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
                "kesan": "Baru ngobrol sebentar aja udah dapet banyak insight",
                "pesan": "Semoga abang gak bosan kalau nanti dimintain sudut pandang abang"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakak terlihat ceria, bikin semua semangat lagi",
                "pesan": "Jangan biarkan semangat itu padam walau sibuk kak"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "Salut sama cara kakak ngatur waktu antara organisasi dan kuliah",
                "pesan": "Terus semangat ngejar impian, semoga sukses terus kak"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak berkesan banget walau baru ngobrol sebentar",
                "pesan": "Semoga bisa terus berinteraksi di kegiatan berikutnya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Z5_l2QvdI0ug5bN1mg-Y9hVpVKfxlORa",
            "https://drive.google.com/uc?export=view&id=170m23jMQED19FZILe9ZoepS48qHWdz5t",
            "https://drive.google.com/uc?export=view&id=1IPeA5kERjobfF0KGjGYUoFAOua0AdBn4",
            "https://drive.google.com/uc?export=view&id=15gYXmfbeL4lEhwSQKTXB72ObjsqewCJe",
            "https://drive.google.com/uc?export=view&id=1LkQg9zh4BCKxT7go9ugt5DlK7m-SOEk_",
            "https://drive.google.com/uc?export=view&id=1VluSwxoAndt4gbPN-YVPrdhfGzn7hUrq",
            "https://drive.google.com/uc?export=view&id=1sutUasDmnn6SkWoDzAAP9urIeKbrYq9Z",
            "https://drive.google.com/uc?export=view&id=1uYpFXQhs9VE4AFHSgHUVHHAfWQqN5v6Q",
            "https://drive.google.com/uc?export=view&id=1krknt4JmTlKDf4ud29PRBvSC3tb9Fca-",
            "https://drive.google.com/uc?export=view&id=1gz62hyqOQsWwUOf2dxgN7JDuxAX01gsy",
            "https://drive.google.com/uc?export=view&id=1UwS6NIj20qsmO0pXGyln3bDlhpLKEMzU",
            "https://drive.google.com/uc?export=view&id=1kXlxt_oTaQhFHsoZYFwECUUrw7LVWs5P",
            "https://drive.google.com/uc?export=view&id=1X-birIJi5e4FjCvsNRXEPkSFq04uRY9H",
            "https://drive.google.com/uc?export=view&id=1WXY--2Vw7-hmK6ZZta-kbyPwu4Em_mLG",
            "https://drive.google.com/uc?export=view&id=1dyWYCL0CQ7pusST83RmvvCDS6di6G96X",
            "https://drive.google.com/uc?export=view&id=1R6kWi2TPRDPUE35iDOoLnHg0mbdb7H4j",
            "https://drive.google.com/uc?export=view&id=1gEPI4yN4QGvIKsZSKRS0GfBjnDRXjd7X",
            "https://drive.google.com/uc?export=view&id=1A_dUnwG_jULoy2lF7MDg5jtl6Rubf5pX",
            "https://drive.google.com/uc?export=view&id=1Ar-oCEimjnO5bYiz7gQd-daHSny4htFj",
            "https://drive.google.com/uc?export=view&id=1_yxqAztUN-rZESFoit8Fv1n1H59WPH5n",
            "https://drive.google.com/uc?export=view&id=11epxhmSe2YP06NrXaD6O_RRTQZYF8gbG",
            "https://drive.google.com/uc?export=view&id=1-mQcKL9KsBaPYAj8luxmSOdivER_nYbG",
            "https://drive.google.com/uc?export=view&id=1wA7smlcJ3zYGaZcLbs2ktHnCtShF7T8f",
            "https://drive.google.com/uc?export=view&id=1FBXbJ0OkzMGRHoUf9rgsti2yF94F4hEi",
            "https://drive.google.com/uc?export=view&id=13tS25htIWZbyJ6T5k7nM2cpUSZgDA1Q8",
            "https://drive.google.com/uc?export=view&id=15giKf_yoWk22K_k2r9s-HFMNyFe761fD",
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
                "kesan": "Abang keliatan sibuk tapi masih sempet nyapa kami",  
                "pesan": "Semoga kesibukannya selalu bawa hasil terbaik bang"
            },
           {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya keren, tapi gak sombong sama sekali",  
                "pesan": "Semoga tetap rendah hati dan makin sukses kak"
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Ngekader 24",
                "sosmed": "@Allyapasha_",
                "kesan": "Kakak tegas tapi care, kombinasi yang susah ditemuin",  
                "pesan": "Semoga nanti di dunia kerja pun tetap jadi sosok yang disegani kak"
            },
              {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Tangerang selatan",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Abang bener-bener cerdas, tiap ngomong selalu ada maknanya",  
                "pesan": "Jangan bosan ngajarin kami yang masih belajar ya bang"
            },
           {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "5 km dari pantai kedu",
                "alamat": "deket kost bang dapa",
                "hobbi": "cari kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakaknya ramah dan juga tegas",  
                "pesan": "Semoga kakak selalu dikuatkan dan selalu diberi kesehatan"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "rahim ibu",
                "alamat": "samping kost arienta",
                "hobbi": "jahilin yulia",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang kelihatan keren bukan cuma dari gaya, tapi juga dari sikap",  
                "pesan": "Tetap rendah hati ya bang"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Abang tegas tapi tetep asik",  
                "pesan": "Semoga abang selalu bahagia dan semangat juga"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "19",
                "asal": "lubuk linggau",
                "alamat": "kost putri gerbang barat",
                "hobbi": "ngitungin duit",
                "sosmed": "@natasyaamavisca",
                "kesan": "Kakaknya bisa ngatur waktu dengan keren banget",  
                "pesan": "Semoga selalu dijaga sama hal-hal baik ya kak"
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Samping kost kak alya",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abangnya pinter tapi gak pelit ilmu",  
                "pesan": "Semoga abang selalu sukses di tiap langkahnya"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma family",
                "hobbi": "ngasprak",
                "sosmed": "@j_gumel_17",
                "kesan": "Abang pintar tapi tetap menghargai pendapat orang lain",  
                "pesan": "Semoga abang selalu dikelilingi orang-orang baik juga"
            },
            {
                "nama": "Vany salsabila putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "airan raya",
                "hobbi": "ngoding di macbook",
                "sosmed": "@vany.salsabila",
                "kesan": "Kakaknya punya cara berpikir yang logis tapi tetap punya empati",  
                "pesan": "Semoga abang selalu sukses dan bahagia dalam setiap langkahnya"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "1224450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22_",
                "kesan": "Abangnya keren banget waktu jelasin sesuatu, jelas dan rapi",  
                "pesan": "Semoga aku bisa belajar ngomong sebaik abang juga nanti"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Sukarame",
                "hobbi": "Main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya kelihatan punya banyak pengalaman keren",  
                "pesan": "Semoga bisa sharing cerita hidupnya kapan-kapan bang"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@farazka",
                "kesan": "Kakaknya keren, tapi gak sombong sama sekali",
                "pesan": "Semoga tetap rendah hati dan makin sukses ya kak"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@risma.mustika_",
                "kesan": "Kakaknya humble banget, gak bikin kami sungkan",
                "pesan": "Tetap jadi kakak yang down to earth kayak gini ya kak"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "rosaliasiregar_",
                "kesan": "Kakak selalu terlihat bersemangat dan ceria",
                "pesan": "Jangan pernah kehilangan semangat itu, Kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi": "Main Video Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang bisa nyiptain suasana santai walau lagi sibuk",
                "pesan": "Jangan lupa jaga kesehatan bang"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "-",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerjain Tugas",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Abang punya cara ngomong yang sopan tapi tetap tegas",
                "pesan": "Terus jadi panutan buat kami semua ya bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi pita pink",
                "sosmed": "@d_aniar",
                "kesan": "Kakaknya sopan tapi tetap santai",
                "pesan": "Semoga makin sukses dan tetap rendah hati Kak"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Gangguin Kak Dea",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Gaya abang yang santai bikin suasana adem",
                "pesan": "Semoga kita bisa sering ngobrol lagi ya bang"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Ngomongin Kak Dea",
                "sosmed": "@kevinaja",
                "kesan": "Abang keliatan rajin banget belajar dan produktif",
                "pesan": "Semoga aku bisa ikut tertular semangat belajarnya ya bang"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dia_natzzyaa",
                "kesan": "Kakaknya keliatan selalu punya tujuan hidup yang jelas",
                "pesan": "Semoga semua langkah kakak dimudahkan kak"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nyuruh Kak Dea diam",
                "sosmed": "@m.ridwan_22",
                "kesan": "Abang punya energi positif yang bikin suasana jadi semangat",
                "pesan": "Semoga abang selalu bahagia dan semangat juga"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "jl. Raden saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Abangnya peka sama situasi, tahu kapan serius dan kapan santai",  
                "pesan": "Semoga bisa terus jadi panutan buat kita semua bang"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Abang selalu nyebarin vibes positif",
                "pesan": "Jangan pernah berubah, Bang, dunia butuh orang kayak abang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Ibu Kota Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Cari GPT",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakak punya aura positif yang bikin tenang",
                "pesan": "Terus sebarkan kebaikan di mana pun kakak berada"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MIKFES":
    def MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T2_7W9o0ibNMKyuG3g1Xx6fx-Mtv8peS",
            "https://drive.google.com/uc?export=view&id=1srTxXfXNoZ9Nxb_P61I-rcxWQC3xe5FD",
            "https://drive.google.com/uc?export=view&id=1JYgOiFwXSucSd4yktBb-K7WGH91oxHh8",
            "https://drive.google.com/uc?export=view&id=18aQZErSHQALSYPO169v4SP3Y48HJAZiP",
            "https://drive.google.com/uc?export=view&id=1netI0pYHLoyjvmMtV1zZartv7aUsx5VH",
            "https://drive.google.com/uc?export=view&id=19hSJ02l8q-lWOaWwM5N-RYpR_G58E9QM",
            "https://drive.google.com/uc?export=view&id=1yatJrlDW1mpa6IXfD62owLiAmf0SBhs7",
            "https://drive.google.com/uc?export=view&id=1HXYieJ-wWKYXfvi8o_k_KqXTEDD5A1u7",
            "https://drive.google.com/uc?export=view&id=1iBfVK9FDwgA6qdWKxDwggu9xqnvs3Eaw",
            "https://drive.google.com/uc?export=view&id=1y51-bSHl90Qvyv5apPj1H0GTBxVvAkeT",
            "https://drive.google.com/uc?export=view&id=1rGNNRGxDhY_zH3kKPq1eBd5eYKpvZKhO",
            "https://drive.google.com/uc?export=view&id=1TDta7gTq90DgLLURqZVEd6K7py7PgEYy",
            "https://drive.google.com/uc?export=view&id=1rqgwU8SzSZEBvlriLJFH7hDcb98_slPR",
            "https://drive.google.com/uc?export=view&id=1jYe3ZADVn6kxX_43QuVkH3eRP3pKfX3L",
            "https://drive.google.com/uc?export=view&id=1C1Q-1RBV7bhQcja3rNwzu1TI7Tgs5eeq",
            "https://drive.google.com/uc?export=view&id=1eO13kRh3J3ORG90iBbSqIrS2jlZz-eQg",
            "https://drive.google.com/uc?export=view&id=1OCVAeubucWuXsh4_iGdXjV0awfNCCxB0",
            "https://drive.google.com/uc?export=view&id=1lmOM0Z_Fyay-j3uurVsF0-sZAzwFSWut",
            "https://drive.google.com/uc?export=view&id=1ucv9HdHO3oPu6BKgkcYhbpPOWwq5iAg-",
            "https://drive.google.com/uc?export=view&id=1FfL0XOboJyMzD82LVIaQGuu1K4WUpriy",
            "https://drive.google.com/uc?export=view&id=1NnbXFc36cpIpNWubcM7JqhFbLDBwmP7p",
            "https://drive.google.com/uc?export=view&id=1rKxF4TgNdpoTXoNynes5NOlWZ0zWvn3o",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "",
                "pesan":""
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "124450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "124450081",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450022",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "-",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "-",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "",
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    MIKFES()
elif menu == "Departemen Eksternal":
    def EKSTERNAL():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WXgPB7M0IOmqkQ6rkRViAqeObIJb4BLa",
            "https://drive.google.com/uc?export=view&id=1dSuYE1h34bWTLzF9498XGtTMTPw6_Gqj",
            "https://drive.google.com/uc?export=view&id=1K_h4RCl_h1YmznFzetgIoudb3k5exTGG",
            "https://drive.google.com/uc?export=view&id=1YyBoW05kCOmS908SzXJ5sfUjh_8E09YP",
            "https://drive.google.com/uc?export=view&id=1bu0gGXoIN9qxuxyyE0mJlb8X2vkLvudG",
            "https://drive.google.com/uc?export=view&id=105HrSDhmMuMrycqgFwRxKTY0C7muM9fs",
            "https://drive.google.com/uc?export=view&id=1G4QrD6vHVamUfAcu8nCiD62pNdrpcEFv",
            "https://drive.google.com/uc?export=view&id=1JJVqNSTQQsH7uNPrb_b4ZnFm8ugqKdyY",
            "https://drive.google.com/uc?export=view&id=1lEda5P0T45z-h05VpAU78fR8Eh6xwdUr",
            "https://drive.google.com/uc?export=view&id=1EbbS8gVaDTCLeiFVK4Mx2xP4FqxbHBHS",
            "https://drive.google.com/uc?export=view&id=1Lbn4dEd24OJy2YmD7PKlnW8W3C0t_MCT",
            "https://drive.google.com/uc?export=view&id=16SxyEosmLKQKhXW52tlXuI4ZsEOB3CRM",
            "https://drive.google.com/uc?export=view&id=1uk-9xRmU7hV69w1NAT6EgJvDNy0UKyfU",
            "https://drive.google.com/uc?export=view&id=16dJrkFxAjJ7DwC2jc8ZxWAKLAmxQe5ve",
            "https://drive.google.com/uc?export=view&id=1eGLEIazm8nZ8hx4vyXblir7MKN0ssA6L",
            "https://drive.google.com/uc?export=view&id=1b50hSFmnfk58LGGUHzXJUy6ssE_RjkIM",
            "https://drive.google.com/uc?export=view&id=1AH08TLA0w53M-00vLmVIaJf8O0G8jlLi",
            "https://drive.google.com/uc?export=view&id=1ZvpkceJiKPyDrcwj-DzkSZXmN1EageJ9",
            "https://drive.google.com/uc?export=view&id=15QxnoV14Ti4OUrCElpriISes-E66Qr_r",
            "https://drive.google.com/uc?export=view&id=1d8r0TjXvBRi97a7ec4LEs0IH-GJQyIRO",
            "https://drive.google.com/uc?export=view&id=1DZCtmhQzF7eNuhUiatYBwnkK2H9co6Cw",
            "https://drive.google.com/uc?export=view&id=1TZQOvtM4yWU3N9f4FxLV4rPeVQIC8dSh",
            "https://drive.google.com/uc?export=view&id=1D4y-PWatBPmbNJqHWrMNeVDjtz79ziX0",
            "https://drive.google.com/uc?export=view&id=1H8ws4bKNriSGtPBB9KLEVCgqOqPd8pV-",
            
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
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva, follow @cerebral.id_",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main-main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam Naya",
                "sosmed": "@cindylauura",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton reels Agz",
                "sosmed": "@deaamnd3_",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "",
                "pesan": ""
              },
              {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajahi desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "",
                "pesan": ""
              },
        ]
        display_images_with_data(gambar_urls, data_list)
    EKSTERNAL()
    
elif menu == "Departemen Internal":
    def INTERNAL():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14ihH9e-VGZfBANPqeJyGJFt2oJurLDjx",
            "https://drive.google.com/uc?export=view&id=1iRDWwMlHQ6xuZu5oLMNi7caqbfW5khhh",
            "https://drive.google.com/uc?export=view&id=1LrL7SRv1KcyxXARVDmXE_9wOMNXvCOeQ",
            "https://drive.google.com/uc?export=view&id=113sCl7bBb2A6EOVE8NyJBe6ZtiLTLf36",
            "https://drive.google.com/uc?export=view&id=1YqAgR_DwbiK_HM1dciAblVkMCJHfApGk",
            "https://drive.google.com/uc?export=view&id=1ZVEYbMjty3dds_0t6Ad1Um0TRen1GtMy",
            "https://drive.google.com/uc?export=view&id=1N9omfiwYyJHd9YK-UzOxjoA-MWASfqHA",
            "https://drive.google.com/uc?export=view&id=19kjZKLkZ-oieWHqpl-VqWhn8Ua8xusph",
            "https://drive.google.com/uc?export=view&id=1Bqh-TKm1cCTrBrZJDitgWzjxmIGf9qGw",
            "https://drive.google.com/uc?export=view&id=1GulBmkMhwAq5a7DfajZ9s0Fu0K3SgwsR",
            "https://drive.google.com/uc?export=view&id=1lmeH4-3wxYNmkruyKKLvEaW9nkwm5ZF8",
            "https://drive.google.com/uc?export=view&id=1TUuLWOry637oXpLn_8x34Rf-1oBVT8AV",
            "https://drive.google.com/uc?export=view&id=1RCL3ANsSs97wE-m-3SksdmzkGRMJVqkO",
            "https://drive.google.com/uc?export=view&id=139IHk-DDHlM4guIKQMBasrmdOI4IQs0o",
            "https://drive.google.com/uc?export=view&id=1HadYpoI2_Pdh4AKG72TE6WR3vhAKogU9",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": 21,
                "asal": "Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@ranniku",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": 22,
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": 21,
                "asal": "Brebes, Jateng",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa.fhn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": 20,
                "asal": "Pekan Baru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azzah.raaa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450106",
                "umur": 18,
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Iqfinah Haula Halika",
                "nim": "123450076",
                "umur": 20,
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "iqfinanhalikaa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "May Thalita Dehlia",
                "nim": "123450009",
                "umur": 20,
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Naufal Algahni",
                "nim": "123450116",
                "umur": 20,
                "asal": "Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": 19,
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": 21,
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@reaxender",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": 20,
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": 19,
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Hanif Zaki",
                "nim": "123450004",
                "umur": 20,
                "asal": "Padang",
                "alamat": "Perumnas, Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Sarah Warti",
                "nim": "123450057",
                "umur": 20,
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwrti",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": 19,
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": "",
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    INTERNAL()
# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LNpAfkEnm9yCNMAyqcwjMUagZ0PCTSmJ",
            "https://drive.google.com/uc?export=view&id=1xrBNmLhTO8hHOVc7jCR9tnekgU_qD0ct",
            "https://drive.google.com/uc?export=view&id=1R-tBiGDl-N_i2LaqawFuuuYWJF56KkhX",
            "https://drive.google.com/uc?export=view&id=1KDhcBHtseeJZr79iljvVWNrVBBYLr-31",
            "https://drive.google.com/uc?export=view&id=10T7szQaNSMgpUH3-C0H03GSYzXdkQyvT",
            "https://drive.google.com/uc?export=view&id=1yHi4KZhJUfA2nrowmt40sTvhUnopHufC",
            "https://drive.google.com/uc?export=view&id=1M2NV8dF0OtCofBNr2bNYwOgDKeQqtVWE",
            "https://drive.google.com/uc?export=view&id=11hlww9zTlk-ZqvQ14EMMRVXvqbzvp3Ik",
            "https://drive.google.com/uc?export=view&id=1ZQWym4aMy_sjqn85tBzfp_K3ueWPbagb",
            "https://drive.google.com/uc?export=view&id=1p17-FLsbeiEy6dlmaOjnU7pV2ATNdiFq",
            "https://drive.google.com/uc?export=view&id=1QcjagUH_d9yfknsFj6VvfK2N3HEV3VKG",
        ]   
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Beli parfum",
                "sosmed": "@den_iki_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "",
                "pesan": ""
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
                "pesan": ""
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "nonton alur cerita",
                "sosmed": "@englirahmdhanii",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasari",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "",
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1swpxnCcUtYQ5T43JVIB3q2Y6ynix5kYl",
            "https://drive.google.com/uc?export=view&id=1IsdmzFyYOfRZVPDnzefwT49TlcBnwNYa",
            "https://drive.google.com/uc?export=view&id=14A3PWZl6j4Z0jF3WBIcnyKc5-nMWPr0q",
            "https://drive.google.com/uc?export=view&id=1DFXABB06P-L5AxeM1KEPvnkgxkefzi3Y",
            "https://drive.google.com/uc?export=view&id=13ajtUFy1DisgwgGwbqwjnArGWwayoLUU",
            "https://drive.google.com/uc?export=view&id=1nvZwmP5C6GpaKGSNrfb-84UUDt2ZbjNf",
            "https://drive.google.com/uc?export=view&id=1dYJJjXHS5jaaqvDPYHPCP7apIROXca-D",
            "https://drive.google.com/uc?export=view&id=1UGazos0U5VWmbw9mIqwz9e3BO6_6hjrO",
            "https://drive.google.com/uc?export=view&id=13_wjSpTH8pWa8YWB2kBCF0fCSc3_ez6I",
            "https://drive.google.com/uc?export=view&id=1ztuvsCh2mc68XpqlOOz3HxAYyM6nUFaY",
            "https://drive.google.com/uc?export=view&id=1-AhvZw8tPisSo_mNMLP9GQ4p_VQAg3HB",
            "https://drive.google.com/uc?export=view&id=1EIMYSLxzZTuLz5oAgUmpXQPLYE3fSro-",
            "https://drive.google.com/uc?export=view&id=1O1rOrLsyqPt88tkBHPtit2gHZpR9XxuM",
            "https://drive.google.com/uc?export=view&id=1TZi0SxtMV-n_YLIGRUAe0ShuXS7BnDNn",
            "https://drive.google.com/uc?export=view&id=1FLVynOZTz83k3svLL14hrPExEnKGwopz",
            "https://drive.google.com/uc?export=view&id=1zxJ0AIvnaL307WT9xe8Bj3MTY6gNgde6",
            "https://drive.google.com/uc?export=view&id=1flvQaesf05zOY1BY7j06tjDne-JCRHZp",
            "https://drive.google.com/uc?export=view&id=1DWvBxbizsqs1GsZKXIvCeLQAhDLWVLsM",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "jl.Kresna, korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "",
                "pesan": ""
            },
             {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "",
                "pesan": ""
            },
            {
            
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way huwi",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kota bumi, Lampung utara",
                "alamat": "jl.pangeran senopati raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaamara",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donamaya.p",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuan ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "",
                "pesan": ""
            },
             {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumatera barat",
                "alamat": "jl.Lapas, kec.Jati Agung",
                "hobbi": "mendengarkan musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "",
                "pesan": ""
            },
             {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main hp",
                "sosmed": "@i",
                "kesan": "",
                "pesan": ""
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan raya 1",
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
                "kesan": "",
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
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "",
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan

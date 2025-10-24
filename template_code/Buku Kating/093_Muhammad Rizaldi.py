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
            "https://drive.google.com/uc?export=view&id=1A5yYu6svP_hy2MeQOEouoZxXRzUqPXOI", #bang rendra   
            "https://drive.google.com/uc?export=view&id=1i-z2Ow7nNhU6XRTZkMBDjn9VPSBEA9DM", #bang johannes
            "https://drive.google.com/uc?export=view&id=1c1l48A9j4UKdyWe1y0Ojlb_8kNSvYyUU", #kak elisabeth
            "https://drive.google.com/uc?export=view&id=1W9EIsAk1CVPJJtjZbeDyQnxsYTEwyN22", #kak syadza
            "https://drive.google.com/uc?export=view&id=1Lwo49Rpaujy3tvmyB41Ys3TmR65kRJKa", #kak eksanti
            "https://drive.google.com/uc?export=view&id=1BeAglwl5IcIe-XTCX63qe2CvUJ2cxI8T", #kak farahanum
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
                "kesan": "Bang Rendra keren sama humble banget",
                "pesan": "Semangat kuliahnya nya bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang jo style nya kece abiez",
                "pesan": "Semangat kuliahnya ya bang"
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "kak Elisabet lucu banget seru deh pokoknya",
                "pesan": "Semangat kuliahnya kakak :) "
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza asik banget",
                "pesan": "Semangat terus ya kakak "
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanti lucu, kocak, heboh, seru puoll",
                "pesan": "Tetap jadi kocak yups kak's "
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak Farahanum juga lucu dan kocak banget, klop banget ama kak eksanty ",
                "pesan": "Semangat terus yupss kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BRQU-V3en4LMsAaYFfdDj2pvA9lK5Pft", #bang jeremia
            "https://drive.google.com/uc?export=view&id=1k3DePRd6Wilom-E_rPPw4KTQjcpEb6FK", #kak dhea
            "https://drive.google.com/uc?export=view&id=13tKd8aBZcRIHOQ64PJbnCa9qbNbpRl7o", #kak renisha
            "https://drive.google.com/uc?export=view&id=1EcbdLPtVx2A57L4fR-b0tjpUC8iTMmr2", #kak anisa
            "https://drive.google.com/uc?export=view&id=1Gk14II-WhDedJ6KMbeNo6-t-s3zZ7R_F", #bang dharu
            "https://drive.google.com/uc?export=view&id=1CT1yDpnGYWTPHRx1QZe3WVRpJ1cRKO4P", #kak feby
            "https://drive.google.com/uc?export=view&id=1MhAn-9P-g8zxwiASvgxDGUYrDJyNJlO8", #bang givaro
            "https://drive.google.com/uc?export=view&id=1IQ4jViojAvICwVqwDH5eiWd2QXiBliIu", #bang mirzan
            "https://drive.google.com/uc?export=view&id=1fC8oagWte4__d79EjFxGpQEZI6L4aPAz", #kak berliana
            "https://drive.google.com/uc?export=view&id=1csrbC1GrOdtBEeiGFcBMxldvJ8yP76OP", #kak juesi
            "https://drive.google.com/uc?export=view&id=1rP8Uu0CMKwPXUgjYtPmWdDRcWtJsuUf4", #bang ridho
            "https://drive.google.com/uc?export=view&id=1GdK0kqOkp6zUfRtDi4Ll4g_is-4ufYfZ", #bang feryadi
            "https://drive.google.com/uc?export=view&id=1yV000fYDYSFiIe41Ty6H7hKYwbef6aJf", #kak monica
            "https://drive.google.com/uc?export=view&id=1quOSpkOJGRhfCxV4L2ws1BdZaEJ3AWcf", #kak nashwa
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
                "kesan": "Bang Jeremia orang nya keren banget, seru diajak ngobrol suka becandaan juga",
                "pesan": "Semangat ya kuliah nya bang, semangat bikin TA nya bang !"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Kalo Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "kak dhea orangnya udah lucu, kocak lagi asik dah pokoknya ",
                "pesan": "jangan lupa liatin aku ya kak biar ga badmood wkwkw ☺️"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "kak renisha style nya keren, baik banget orangnya",
                "pesan": "kak jangan cuma nawarin alat pancing, sekali kali mancing bareng di embung yuks wkwkw 😁"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Kak anisa orangnya ramah banget",
                "pesan": "semangat ya kak kuliah nya, boleh lah diajarin main bowling hehe"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "bang dharu orang nya rada kalem, tapi keren dan pinter banget abang nya",
                "pesan": "tutorial mahamin ads ama lmd nya dong bnag 😭"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "kak feby imup banget orang nya, rambut merahnya jadi iconc banget keren pol",
                "pesan": "semangat tanding volly nya kakak"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "bang givaro asik cuy orang nya, suka becanda juga",
                "pesan": "pas iatin langit kalo ujan neduh dulu ya bang wkwkwk"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "bang mirzan seru orang nya",
                "pesan": "inpokan makanan bintang lima harga anak kostan wkwk"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "kak berli asik poll orang nya seru banget becandaan sama kakak nya",
                "pesan": "ngumpulin batu pantainya jangan nyampe satu truk ya kak hehehe 🤣"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "kak jue keren banget orang nya mana lucu lagi, aura aura duta nya terpancar banget",
                "pesan": "semangat kak juee jangan galau mulu yaa, mending liatin aku biar mood lagi wkwkwk 🤣🤣"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang ridho ornag nya asik diajak gobrol",
                "pesan": "semangat kuliah nya bang, semoga ITERA taun depan punya lapangan padle yaa bang wkwkwk"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "bang fryadi orang nya lucu, kocak suka becanda orangnya, aku kaget tiba tiba foto dibelakang tumbuhan orang wkwkwk",
                "pesan": "semangat ya bang kuliah nya jangan tiba-tiba sembunyi di belakang tumbuhan notiz lagi ya bang heheh🤣"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "kak monic asik bangettt orang nya, lucu juga",
                "pesan": "ajarin aku main ml dong kak wkwk"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "kak wawa orang nya lucyuu, imup suka becandaan juga,vibes nya kak wawa happy terus",
                "pesan": "teteap happy yaww kak bair orang-orang juga ikutan happy hehe"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1s1fsC_lGgCauWacVueYuHXpOg2aa61Yv", #bang bintang
            "https://drive.google.com/uc?export=view&id=1CKLOzg1aER2L-OA2EZOcW0E3LIfBca11", #kak nadya
            "https://drive.google.com/uc?export=view&id=1WiGhgBQCHAGOnkJSg2jC_-nxUyW5LrYP", #kak fathinah
            "https://drive.google.com/uc?export=view&id=1A0eSMMofpzduVXhmqs4Vb43F48q8gd_h", #kak lia
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
                "kesan": "Bang Bintang keren banget orang nya seru ngobrol sama bang bintang",
                "pesan": "bagi tips belajar nya dong bang"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "kak nadia seru orang nya imup kakak nya",
                "pesan": "inpokan rekomend lagu nya dong kak hehe"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "kak fatinah orang nya baik bangett, humble banget kakak nya",
                "pesan": "jangan suka bengngong sendirian kak takut kesambet, wkwkk canda kak"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "kak lia asik orang nya seru deh pokoknya",
                "pesan": "tutor tidur didalam gempuran tugas tugas yang masyaallah wkwkw"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c-4Pg78XT5uNlPAU7ETvax5j6WjM9ZNm", #bang frdy
            "https://drive.google.com/uc?export=view&id=1uLGUwGGomEyKRlvDndyknefM2RV6kmAf", #kak nisrina
            "https://drive.google.com/uc?export=view&id=1fd5NL1qE-4MXoazYbaLQ5SMsMO2Fa9NL", #kak allya
            "https://drive.google.com/uc?export=view&id=1dgY4Vsnk8BKROOS9XcNhBUcYFKazSuI7", #bang ahmad rizky
            "https://drive.google.com/uc?export=view&id=1lC3oxf5y1v6OfbIAvbGcfl8x965hUyvf", #kak arienta
            "https://drive.google.com/uc?export=view&id=16GyDxQwXwYyVJruCzxhMI-pBeeKHPzi6", #bang daffa hadyan
            "https://drive.google.com/uc?export=view&id=1RI69V_8saBjXpaGaFGVimtfQblWVxYIN", #bang fajar
            "https://drive.google.com/uc?export=view&id=1dS3n4XFYg0ic7Is0EM1F83kj0Vhvyj76", #kak natasya
            "https://drive.google.com/uc?export=view&id=15OGFRDdqYChd3ibWRBD-9Ju4YM43uMAO", #bang nobel
            "https://drive.google.com/uc?export=view&id=1dio0uM68JiQAnpZp302hepqwnN52C0LN", #bang aji
            "https://drive.google.com/uc?export=view&id=1jPASqRJFtu1rmeQfUy-0bcv7vWOZ6O3X", #kak vany
            "https://drive.google.com/uc?export=view&id=1-5o27PeE4gmAh5MZfrhIcJmMVe-kDKGT", #bang sahidin
            "https://drive.google.com/uc?export=view&id=1jtMWgugIQro4eXXGO6Hfq4_g6V5a5HN9", #bang aristo
            "https://drive.google.com/uc?export=view&id=1xUx6pcwDPbw5iNtSi1GFzKPY5uZPM_Fa", #kak raska
            "https://drive.google.com/uc?export=view&id=1ekdBbzNqSIUYkDGfpfYfjPR_MfBQM_iP", #kak kharisma
            "https://drive.google.com/uc?export=view&id=1RyRfRzrSb35_Gi_J0Zu957KDQKS35zLM", #kak rosalia
            "https://drive.google.com/uc?export=view&id=1joMsOOxncEM3gWnU0bCDmrCbVfAVGX-W", #bang sahid
            "https://drive.google.com/uc?export=view&id=1_djcg4oB6pqjwtIY4dlXQuPy9518fNsd ", #bang daffa ahmad
            "https://drive.google.com/uc?export=view&id=1EGXbF0muLmkYCPeQs6IU0zElvKxT4G4P", #kak erma
            "https://drive.google.com/uc?export=view&id=1qVxXTPOCu4-DcvPssaXylrXztvqezSww", #bang ihsan
            "https://drive.google.com/uc?export=view&id=1WXE8F8PvwpptYFcheSuiBScVz84EpwWQ", #bang kevin
            "https://drive.google.com/uc?export=view&id=1B2IHZ05p4q0Ck1GKiAnmQK54nLWIfv--", #kak lidia
            "https://drive.google.com/uc?export=view&id=1wrRS5D0MJs_uMsSRzAsDupqtsp_7IGIP", #bang ridwan
            "https://drive.google.com/uc?export=view&id=1hyLDc4aaEIS_n9ej0xK34dmZNyqqit8g", #bang ulliano
            "https://drive.google.com/uc?export=view&id=19_YCqgGDITHVUwsAdFbzv5ElB-r6fFiZ", #bang benget
            "https://drive.google.com/uc?export=view&id=15F9OAwAM557bEpaiD5nvFmVvZWg3kHOS", #bang rewina
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
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Ahmad Rizky",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Arienta Khusnul Ananda",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "vany salsabila putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang randa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak rut
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang regi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak aisyah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang fadhil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang aqil
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang naufal
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak nadia faraj
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak marleta
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang kea
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak anggi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak efi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak olla
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak fairuz
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak tanti
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang eggi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak afifah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang bio
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang gio
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak rahma
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak rahma gudtriana
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang razin
            
           
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
                "kesan": "Abangnya seru banget",
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak rut asik diajak ngobrol",
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "124450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya seru dan mudah diajak ngobrol.",
                "pesan": "Semoga Abang semakin sukses dan tetap rendah hati."
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya lembut dan sopan dalam berbicara.",
                "pesan": "Semoga Kak terus bersemangat dan selalu bahagia."
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Abangnya ramah dan mudah membuat suasana jadi menyenangkan.",
                "pesan": "Semoga Abang selalu diberi semangat dan rezeki yang lancar."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya aktif dan seru ketika ngobrol.",
                "pesan": "Semoga Abang selalu sehat dan sukses ke depannya."
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya tenang dan memiliki pemikiran yang matang.",
                "pesan": "Semoga Abang terus menjadi pribadi yang inspiratif."
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakaknya ceria dan membawa suasana positif.",
                "pesan": "Semoga Kak terus bahagia dan dikelilingi hal-hal baik."
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya sopan dan menyenangkan diajak berdiskusi.",
                "pesan": "Semoga Kak selalu diberi kemudahan dalam setiap urusan."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya seru dan mudah beradaptasi.",
                "pesan": "Semoga Abang selalu bersemangat dan percaya diri."
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya energik dan selalu bersemangat.",
                "pesan": "Semoga Kak terus menebarkan energi positif."
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya bijak dan suka membantu.",
                "pesan": "Semoga Kak selalu diberi kesehatan dan kebahagiaan."
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
                "kesan": "Kakaknya tenang dan menyenangkan.",
                "pesan": "Semoga Kak selalu semangat menjalani hari-hari."
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
                "kesan": "Abangnya tenang dan selalu terlihat santai.",
                "pesan": "Semoga Abang selalu sehat dan semangat menjalani kuliah."
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya ceria dan menyenangkan.",
                "pesan": "Semoga Kak selalu membawa keceriaan di mana pun berada."
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "Abangnya sopan dan mudah diajak bicara.",
                "pesan": "Semoga Abang selalu diberi kemudahan dalam segala urusan."
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya tenang dan berwawasan luas.",
                "pesan": "Semoga Abang terus berprestasi dan sukses selalu."
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakaknya lembut dan sopan berbicara.",
                "pesan": "Semoga Kak selalu sukses dan diberi kebahagiaan."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "-",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya humoris dan mudah akrab dengan teman.",
                "pesan": "Semoga Kak selalu ceria dan semangat terus."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya seru dan asik diajak ngobrol.",
                "pesan": "Semoga Abang selalu diberi kesehatan dan kesuksesan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    MIKFES()
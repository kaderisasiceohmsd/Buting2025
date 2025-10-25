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
            "https://drive.google.com/uc?export=view&id=1_djcg4oB6pqjwtIY4dlXQuPy9518fNsd", #bang daffa ahmad
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
            "https://drive.google.com/uc?export=view&id=1XiP67O29HtfcdAcrQYSlYNIW22OYoQKB", #bang randa
            "https://drive.google.com/uc?export=view&id=1rAd_x09PSjGlBXOgBqqUNZPm_B8NPkii", #kak rut
            "https://drive.google.com/uc?export=view&id=1XEWKWxDs7S6Jdk1Q3FdfHF4JCjEAsv7P", #bang regi
            "https://drive.google.com/uc?export=view&id=1aEINtzdUtAIHO_4KTb17wZ_aA27C4vZn", #kak aisyah
            "https://drive.google.com/uc?export=view&id=1rxshb8yZ04PI_cJbNSqCiyEAj9ojkkwN", #bang fadhil
            "https://drive.google.com/uc?export=view&id=1Qe1wxy6Y1OUPCOOq4Vg2_RbzsjdfjXgk", #bang aqil
            "https://drive.google.com/uc?export=view&id=14YHmG_U5GFgOafFVe-MQJXieVtpA6wsZ", #bang naufal
            "https://drive.google.com/uc?export=view&id=1dJIrOMq4NsDRHCrb034oAbTDrvQlf8xQ", #kak nadia faraj
            "https://drive.google.com/uc?export=view&id=1emK2J1YKedJyYqco9uaXCK-XUJnxl-eN", #kak marleta
            "https://drive.google.com/uc?export=view&id=1G7bbLCHFBRWX7qRlbOccxZefm7tIW5nv", #bang kea
            "https://drive.google.com/uc?export=view&id=1gBGaLFCCcqXxi2RIRHV-btNls2rWXd6q", #kak anggi
            "https://drive.google.com/uc?export=view&id=1Au8ka4VxmprSLJ8QH0cw3DoBnbQyUgM6", #kak efi
            "https://drive.google.com/uc?export=view&id=1emdLy9bz5QF3y0Utd6CPyEaEe_Y7E0KI", #kak olla
            "https://drive.google.com/uc?export=view&id=13-vgH9rn-WDj0FIvW3eH6ajUWSECjuiB", #kak fairuz
            "https://drive.google.com/uc?export=view&id=1ec8qiwgFpvQUHxlbI2X8Ha6uo63nUPst", #kak tanti
            "https://drive.google.com/uc?export=view&id=159Va0nC4AyWTAfkN34GcJdu8OE03efdw", #bang eggi
            "https://drive.google.com/uc?export=view&id=1ZLO8cofEekDfq5WO_T7xHD2e2uFQKTxR", #kak afifah
            "https://drive.google.com/uc?export=view&id=16m548vRepafWXjS485CGUycFgY_Br6nF", #bang bio
            "https://drive.google.com/uc?export=view&id=1H6dxfYhAB1aZq425MSPsPHyj6ZMnEiWB", #bang gio
            "https://drive.google.com/uc?export=view&id=15ekTAnNRCQHS4XhJ6H6YHXlVR5d7wb3f", #kak rahma
            "https://drive.google.com/uc?export=view&id=19aGFptfHPeUvY4YrVlI1-MNtVrUnvOAL", #kak rahma gudtriana
            "https://drive.google.com/uc?export=view&id=1EvGkSojZ_EKI3LpFwmbJ7FKLqJx-NohR", #bang razin
            
           
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

elif menu == "Departemen Eksternal":
    def EKSTERNAL():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14MQ0sqCgatBOo2VaLwhRBzw8Lt4yCO8Q", #bang arafi
            "https://drive.google.com/uc?export=view&id=1FoLpRNKZ9bkJTnt7a6E3UZhugObMRZY0", #kak yohana
            "https://drive.google.com/uc?export=view&id=19oeroEpzDOeJtjqAzTBfyumRbhDxAaty", #kak keisha
            "https://drive.google.com/uc?export=view&id=1KpCPQUz7ICA5UGDdpd6FqS2qDUY3VVw6", #kak arini
            "https://drive.google.com/uc?export=view&id=1hnyHRyPn9_kfWDISaMSuQ4uXHFuYEi8O", #bang arya
            "https://drive.google.com/uc?export=view&id=13efj_eGxzarfl306Sk5O8zAczusWmvlM", #kak mut
            "https://drive.google.com/uc?export=view&id=17nhNYLRE3sEWuuxXn5-xCSivmna3UHyV", #kak lutfi
            "https://drive.google.com/uc?export=view&id=133S6oqzzCIye68FbZWwZ9CyOWOYc1nrG", #kak nabila
            "https://drive.google.com/uc?export=view&id=1jQAbmoCC3nWqHGOIMUSt0Ow8pxcjUSpY", #bang aldi
            "https://drive.google.com/uc?export=view&id=14YRBtatfh5RW5ECYGke3M443cCDE5XPr", #kak dea
            "https://drive.google.com/uc?export=view&id=12CBXsTMdqkC4UhwN4dN_ufcoM0n36A-e", #kak cindy
            "https://drive.google.com/uc?export=view&id=19GVcpkHpkkzINoGcspNhZeFcsQ_xAmat", #kak dea amanda
            "https://drive.google.com/uc?export=view&id=1VcNHvp73DI70DRbXcFvNvEC5qzsEpdZu", #bang desman
            "https://drive.google.com/uc?export=view&id=17EzpfpI-Mdt9Iuir9FGeEn8ytXOCFDae", #kak sonya
            "https://drive.google.com/uc?export=view&id=1nf3dRzo4GVgZ-ehIE2WH6tnnBuznwKQ9", #kak lulu
            "https://drive.google.com/uc?export=view&id=1U_WJrBe3COei-r0KQa_0Id-u7y-RWjbk", #banf irfan
            "https://drive.google.com/uc?export=view&id=1K2LFdQGYG7Omtd52tY_T_PBTAh8GlQtG", #ban adit
            "https://drive.google.com/uc?export=view&id=1PWleANXb8qnAz9LWlLvkwajXWdJfMVPY", #kak fathya
            "https://drive.google.com/uc?export=view&id=1csBsCZHqq_YAFaJX3nOdsFKOSdMa8hoE", #kak nay
            "https://drive.google.com/uc?export=view&id=1s6ibjo0sitvQAEO98RDFvyOnWZAGrBdh", #kak melin
            "https://drive.google.com/uc?export=view&id=1Algft9wv3Ug334exUh8uEJnvJNGJ9IND", #kak ilmi
            "https://drive.google.com/uc?export=view&id=1C4Ho3YIV3xIrwz1mxcCtcnxqmV4wPdyX", #kak izzah
            "https://drive.google.com/uc?export=view&id=1q2Hr4Nc6eIe3dUl28BrPGfc_EXYm2-Rl", #bang qois
            "https://drive.google.com/uc?export=view&id=1EAnzJpeaV0k1TWV5sXDU7VQpmUcKGsAs", #kak tarisya
            
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
                "kesan": "Bang Arafi punya seru dan selalu bikin suasana cair!",
                "pesan": "Terus tebarkan semangat dan tawa di setiap kegiatan ya kak, tetap semangat bang!"
              },
              {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana seru banget!",
                "pesan": "Tetap semangat dan terus tingkatkan rasa ingin tahunya ya kak!"
              },
              {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva, follow @cerebral.id_",
                "kesan": "Kak Mine keren bangett!",
                "pesan": "Tetap semangat dan terus menginspirasi ya kak!"
              },
              {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini ramah dan seruu!",
                "pesan": "Semoga impian keliling dunia tercapai ya kak wkwkwkwk!"
              },
              {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Bang Arya kalem tapi seru!",
                "pesan": "Jangan kebanyakan ngelamun bang, dunia nyata nungguin wkwkwkw!"
              },
              {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main-main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kak Mut ceria dan seru bangett!",
                "pesan": "Terus tebarkan keceriaan ya kak Mut dan tetap semangatt!"
              },
              {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia pinter banget dan suka eksplor hal baru!",
                "pesan": "Semoga makin jago di dunia data ya kak!"
              },
              {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla ceria dan suka banget jalan-jalan bareng temen!",
                "pesan": "Tetap jadi sosok yang fun dan bersemangat ya kak!"
              },
              {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Bang aldi seru dan suka belajar hal baru!",
                "pesan": "Terus asah kemampuan dan semangat belajarnya bang!"
              },
              {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea chill banget!",
                "pesan": "Tetap semangat kakk!"
              },
              {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam Naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak Cindy seru dan selalu ceria!",
                "pesan": "Jangan lupa traktir risol ayamnya ya kak hehehe!"
              },
              {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton reels Agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea lucu banget dan punya vibes positif dan pastinya seru banget!",
                "pesan": "Tetap jadi moodbooster bagi sekelilingmu ya kak dan tetap semangat!"
              },
              {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman jago musik dan keren banget!",
                "pesan": "Terus berkarya dan jangan berhenti bermusik ya bang!"
              },
              {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya seru banget dan suka bercanda!",
                "pesan": "Tetap ceria dan terus tebarkan tawa ya kak!"
              },
              {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kak Lulu seru banget dan selalu bikin suasana hidup!",
                "pesan": "Tetap jadi pribadi yang penuh energi positif ya kak!"
              },
              {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Bang Irvan keren banget, seru dan inspiratif banget!",
                "pesan": "Terus semangat memimpin dan jadi contoh yang baik bang!"
              },
              {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Bang Adit itu orangnya seru banget, kocak parah, gokil banget juga, ketawanya seru banget nular juga, pokoknya seru bangett!",
                "pesan": "Ajak ajak bang kalo nemu tempat keren, tetap semangat bang!"
              },
              {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya aka kakak cantik orangnya lucu banget, ramah banget juga, kemana-mana selalu sama bang adit orangnya seru banget dan humble parahhh!",
                "pesan": "Tetep jadi moodboster kak Fathya eh kakak cantk dan tetap semangat kuliahnya!"
              },
              {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla keliatannya orangnya kalem, tapi ternyata seruu banget, ramaha banget juga, lucu juga orangnya, pokoknya orangnya seru bangettt!",
                "pesan": "Nikmati setiap waktu me timenya kak, tetap semangat kak!"
              },
              {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melin orangnya ramah banget, seru banget juga, cantik orangnya, easygoing dan suka banget film!",
                "pesan": "apa tuh film favoritnya kak? tetap semangat ya kak dan semoga menang Mister Miss Lampung 2025, aamiin!"
              },
              {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Ilmi orangnya asik banget diajak ngobrol, ramah banget, ceria banget orangnya, lucu banget orangnya, clingy juga orangnya dan ternyata orangnya aga penakut xixixi!",
                "pesan": "Terus jadi pribadi yang menyenangkan dan ceria ya kak, bahagia selalu kak semoga sifat takutnya bisa redam !"
              },
              {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak Izzah orangnya seru banget, ramah banget, asik juga orangnya, lucu banget orangnya dan imup wkwkwk!",
                "pesan": "Boleh bagi bagi ga kak hasil bakingnya wkwkw, semangat kuliahnya kakkk!"
              },
              {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois orangnya terlihat aga jaga image, paling jago kalo main undercover, baik juga orangnya, seru banaget orangnya dan suka jalan-jalan!",
                "pesan": "Tetap semangat bang, jangan lupa jaga kesehatann!"
              },
              {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajahi desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kak Tarisya baik banget, keren banget dan menjadi salah satu inspirator aku buat mengabdi di masyarakat, orangnya punya jiwa sosial tinggi, paling lucu kalo lagi main undercover 'bertangkai' pokoknya orangnya seru banget!",
                "pesan": "Terus semangat berkontribusi dan menjelajah desa ya kak,ajak ajak sabi kali wkwkwk!"
              },
        ]
        display_images_with_data(gambar_urls, data_list)
    EKSTERNAL()

elif menu == "Departemen Internal":
    def INTERNAL():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w5_WBq81MC4dgAk6ZQioJ3c5Is8tmbqb", #kak rani
            "https://drive.google.com/uc?export=view&id=16eSokSai2E-qucdo2QeOxKmVm2hDGO58", #kak renta
            "https://drive.google.com/uc?export=view&id=11I9V3up69BtjjPmdrv-2cdIVPlmb9GC0", #kak salwa
            "https://drive.google.com/uc?export=view&id=12QIR-MEi-ARxXgko1xRUA2XZncxiOwZQ", #kak azzahra
            "https://drive.google.com/uc?export=view&id=1c-i7N8Y8dy6VHP6f6hIYv6UKnxsiUh5P", #bang haikal
            "https://drive.google.com/uc?export=view&id=1w-uAnTLstenXgVH4W2c74D2O0FoxlKdW", #kak iqfinah
            "https://drive.google.com/uc?export=view&id=1TBksfW3Og_w9thz46vInclp7Sdilszn3", #kak may
            "https://drive.google.com/uc?export=view&id=1JOfanQ4WbC-sXenVyiVp7kG_7yAoeqmH", #bang naufal
            "https://drive.google.com/uc?export=view&id=1DgiKZH2fRNZ_Rgydhl4O5COHzcBBLsOk", #bang zailani
            "https://drive.google.com/uc?export=view&id=1nl20ngYWI7DrZaVaIyKJ6Ynp1_FTwTIv", #bang rendi
            "https://drive.google.com/uc?export=view&id=1PzORgI1NIdx2I3eRXJkmPrucUfT7GgUm", #kak hana
            "https://drive.google.com/uc?export=view&id=1C2g2Be3cZiKJKaPRuGShvLaKpseNHQlo", #kak keren
            "https://drive.google.com/uc?export=view&id=1Zc-ecnZDAqY0t1ZcMo4rwdzBwXmloG_t", #bang hanif
            "https://drive.google.com/uc?export=view&id=1-lBh0WxlBUWETOTM7u5axSQKXedOlO75", #kak sarah
            "https://drive.google.com/uc?export=view&id=12QIR-MEi-ARxXgko1xRUA2XZncxiOwZQ", #kak zahra
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
                "kesan": "Kak Rani orangnya lembut dan bijaksana.",
                "pesan": "Semoga selalu diberi kesehatan dan keberkahan dalam setiap langkah."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": 22,
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta orangnya tenang dan sopan.",
                "pesan": "Semoga selalu diberi kesabaran dan rezeki yang lancar."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": 21,
                "asal": "Brebes, Jateng",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa.fhn",
                "kesan": "Kak Salwa lembut dan ramah banget.",
                "pesan": "Semoga selalu bahagia dan sukses terus ya Kak!"
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": 20,
                "asal": "Pekan Baru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azzah.raaa_",
                "kesan": "Kak Azzahra punya aura positif banget.",
                "pesan": "Semoga selalu ceria dan makin sukses!"
            },
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450106",
                "umur": 18,
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang Haikal seru dan keren banget.",
                "pesan": "Semoga selalu membawa keceriaan di setiap suasana!"
            },
            {
                "nama": "Iqfinah Haula Halika",
                "nim": "123450076",
                "umur": 20,
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "iqfinanhalikaa_",
                "kesan": "Kak Iqfinah imut dan kreatif banget.",
                "pesan": "Semoga semua impian Kakak bisa terwujud!"
            },
            {
                "nama": "May Thalita Dehlia",
                "nim": "123450009",
                "umur": 20,
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak May selalu tampil cerah dan ramah.",
                "pesan": "Semoga terus jadi inspirasi bagi yang lain!"
            },
            {
                "nama": "M. Naufal Algahni",
                "nim": "123450116",
                "umur": 20,
                "asal": "Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": "Bang Naufal asik diajak ngobrol.",
                "pesan": "Semoga makin sukses dan tetap rendah hati!"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": 19,
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "bang Zai aktif dan seru banget.",
                "pesan": "Semoga tetap semangat bang!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": 21,
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@reaxender",
                "kesan": "Bang Rendi suaranya keren dan berkarisma.",
                "pesan": "Semoga terus semangat berkarya dan tetap rendah hati bang!"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": 20,
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna lucu dan supel.",
                "pesan": "Semoga terus membawa suasana ceria dan positif ke sekeliling!"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": 19,
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak Keren sesuai namanya, keren banget!",
                "pesan": "Semoga terus berprestasi dan menginspirasi banyak orang."
            },
            {
                "nama": "Muhammad Hanif Zaki",
                "nim": "123450004",
                "umur": 20,
                "asal": "Padang",
                "alamat": "Perumnas, Way Kandis",
                "hobi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Bang Hanif orangnya sopan dan kalem.",
                "pesan": "Semoga selalu diberkahi kesuksesan di setiap langkah!"
            },
            {
                "nama": "Sarah Warti",
                "nim": "123450057",
                "umur": 20,
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwrti",
                "kesan": "Kak Sarah anggun dan ramah.",
                "pesan": "Semoga selalu bahagia dan sukses di setiap perjalanan!"
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": 19,
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": "Kak Zahra orangnya lembut dan sopan.",
                "pesan": "Semoga selalu semangat dan penuh kebahagiaan!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    INTERNAL()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sFqkU1fFyFPCYrkfi5rWbv264mjVU6_S", #bang danang
            "https://drive.google.com/uc?export=view&id=1_8Sr9nZTDKnv79yfH33ZIGB8uwTHLJqK", #kak syalaisha
            "https://drive.google.com/uc?export=view&id=1pI563g7WQE_s_wvcWLYYMrA2ARrQCw8D", #bang rizqi
            "https://drive.google.com/uc?export=view&id=1T0hpGImlsQ1XK-bAK4P7Ytg2tf7Wmqw9", #kak anadia
            "https://drive.google.com/uc?export=view&id=1NBOmUV1IQmVi6Be--d6s6DgWcNwd1dKE", #kak aprilia
            "https://drive.google.com/uc?export=view&id=1HQa-Cs6QCtkUBmnRv9NgEES7ujSnpZMl", #kak nabila
            "https://drive.google.com/uc?export=view&id=1lxpv59Ux_hu_lnVmo9QcEu5Vpqytqva2", #bang dhafin
            "https://drive.google.com/uc?export=view&id=1csFJGAovA7u-VTAppfIEn1Ikja7AEMdg", #kak devi
            "https://drive.google.com/uc?export=view&id=1nncv1zAnn1uG3FSxa0-Qb1-ckTHcCT18", #kak enggli
            "https://drive.google.com/uc?export=view&id=1LsHUrLpm444y5ykQthemM0AWNGPZVH2U", #kak hanifah
            "https://drive.google.com/uc?export=view&id=14ROSaLX9-syUSg1lg3offQiBLRKuAGpt", #kak nydia
        ]   
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@dananghk_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@syalaishaa_31",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@den_iki_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@anadiacrn_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@aprhtp_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@nabila_zazahra",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@dhafinrzqa13",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@deviirhyu",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@englirahmdhanii",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@_inayasari",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@nydiaaptr_",
                "kesan": "-",
                "pesan": "-"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lfOpvZfy4soTWftmLZlbQShGPOHKthOo", #kak patricia
            "https://drive.google.com/uc?export=view&id=1DYTO3MRHBF4ErtsnhegoGch0p_XjSPE8", #kak nely
            "https://drive.google.com/uc?export=view&id=1N8NGHmRoy9XAUtV3fkou3sPyTnDKF0F0", #bang anam
            "https://drive.google.com/uc?export=view&id=1Jw24Kf05XTqkDd9xTywdodPekMfFvHSJ", #bang labo
            "https://drive.google.com/uc?export=view&id=1JKx9P0xQqOf-wi7vxLrNQyaaL1GRUoGN", #bang rafi
            "https://drive.google.com/uc?export=view&id=1KDyIEAeqpMBigaj344g6CbUu-94mnYDZ", #kak refa
            "https://drive.google.com/uc?export=view&id=1JgPIhqDDSiokqQ87uJVq6e-QwAEMqqEW", #kak try yani
            "https://drive.google.com/uc?export=view&id=1JPC-XnM-J2Iw9k1YfnSGzNQ2bccmb0b8", #kak aliya
            "https://drive.google.com/uc?export=view&id=1JM3CPdvsbZgX6ciqEdRNSxXlbrZ2RA4E", #kak dona
            "https://drive.google.com/uc?export=view&id=1J-nYZQt4bitbrN_NU3kVSReptSM0gejV", #kak feby
            "https://drive.google.com/uc?export=view&id=1KWS-34jJg32rLf539j8G8Oc9JxGyWvLX", #kak hafsah
            "https://drive.google.com/uc?export=view&id=1JMTDXgiNWOphZHlKGNCOJrhRTktxBpb0", #kak nayla
            "https://drive.google.com/uc?export=view&id=1KAHb0CdLu1Vx-P-SLk28NALDlkFJhacX", #kak sania
            "https://drive.google.com/uc?export=view&id=1Jt8cpS0Gb1XLMI4siEIqPv7SKtUyKL2v", #bang akmal
            "https://drive.google.com/uc?export=view&id=1JEWU-WLmPJzXl58e_wVigJ6HsbaIo3E4", #kak raihana
            "https://drive.google.com/uc?export=view&id=1IvxXGlr14CvfRsaC610aLgvD5knBRGCA", #kak Citra
            "https://drive.google.com/uc?export=view&id=1J9j8GmTLKZey1qwcV-8MkHFFXR7BeU4U", #kak eigi
            "https://drive.google.com/uc?export=view&id=1Jfcx2zj9t316QVTM9YK00cHoWXgg2t0T", #kak roma
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak ciaa asik banget dan seruu bangeett",
                "pesan": "sehaatt selaluu dan selalu ceria kakk!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@rahmanellyana",
                "kesan": "pinterr bangeett dan ramah banget",
                "pesan": "semangaatt kuliahnya kakk!"
            },
             {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@mananam_",
                "kesan": "baikk dan sabar bangett ngajarin nyaa",
                "pesan": "semangaatt truss bangg!"
            },
            {
            
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@noe_rruuu",
                "kesan": "keren banget dan seru banget juga",
                "pesan": "semangaaatt kuliahnya bangg!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@rafidivaefangga",
                "kesan": "Seru banget abangnya dan ramah banget juga",
                "pesan": "semangaatt kuliahnya bangg"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@refadp_",
                "kesan": "seruu banget kakaknya dan asik banget",
                "pesan": "semangatt kak kuliahnyaa, besok tepuk doa bareng ya kak wwkkwkw"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@tryyaniciaaa",
                "kesan": "seruu bangeet kak dan ramah juga",
                "pesan": "Tetap semangat kak kuliahnya!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@aliyaamara",
                "kesan": "kereenn kakaknya dan seru juga",
                "pesan": "Semangat kuliahnya kak!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@donamaya.p",
                "kesan": "Kakaknya seru banget dan ramah juga",
                "pesan": "Semoga sukses di masa depaann kaakk!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@writtenbyangel",
                "kesan": "baiikk bangeett kakaknya dan asik bangettt",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget suka bantuin kalau kesusahan ngerjain praktikum alpro",
                "pesan": "Sukses untuk ke depannya, kak dan selalu berbuat baik!"
            },
             {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@naylasalsabilaa",
                "kesan": "baiikk bangeett kakaknya dan seru juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
             {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@saniayyllstr",
                "kesan": "baiikk bangeett kakaknya dan seru",
                "pesan": "semangaatt kuliahnya kak dan bahagia selalu kak!"
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "baiikk bangeett abangnya dan ramah juga",
                "pesan": "semangaatt bang!"
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@nltg._",
                "kesan": "baiikk bangeett kakaknya dan ramah juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@citrastin",
                "kesan": "baiikk bangeett kak dan asik juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@eigirtmv",
                "kesan": "baiikk bangeett kakaknya dan ramah bangett",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@roms.slbn",
                "kesan": "baiikk bangeett kak, asik juga dan ramah bangett",
                "pesan": "sukses terus kedepannya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
    

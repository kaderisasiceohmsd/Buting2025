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
            "nav-link-selected": {"background-color": "#ffb6c1"},
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
            "https://drive.google.com/uc?export=view&id=1xeONq-4OIb4LcFNI6pmScWFAckPXBq8H",
            "https://drive.google.com/uc?export=view&id=1b1gpKZc603eHXCnjpbCm9UXTujTBMcHe",
            "https://drive.google.com/uc?export=view&id=1C9YFUwGZ112kIZ0Pi0KRfZiX08tqmfaM",
            "https://drive.google.com/uc?export=view&id=1rAnTLUrV64eisz25OsGweOg3DmE0Qxbc",
            "https://drive.google.com/uc?export=view&id=1_HdgTjPM7vcok5K8E2mYmuRjUTHcpPct",
            "https://drive.google.com/uc?export=view&id=1AHYV_HcMDQ3M_fFtD2TCfVJ06oLuQNAg",
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
                "kesan": "bang rendra seru bangett, suka ngelawak, jokesnya masuk bangett",  
                "pesan":"semangat kuliahnya abangg" # 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "baca buku dasar dasar sql",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "bang jo keren, perhatian banget sama kita kita",  
                "pesan":"semangat kuliahnya bangg"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabethh_",
                "kesan": "kak elisabeth lucuu, ramah bangett",  
                "pesan":"semangat terus kak, sering sering bahagia!!"
            },
            {
                "nama": "Syadza Puspandari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "lucuuu, baik banget kak puspa",  
                "pesan":"semangatt kuliahnya kak, jangan lupa bahagia!!"
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku saku pramuka",
                "sosmed": "@ekshantyfebriana",
                "kesan": "kak eksanty lucu, kocak banget,tapi inspiratifff",  
                "pesan":"jangan lupa mamam kak"
            } ,
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang, Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan": "kak farah asik banget, ramah, lucuu",  
                "pesan":"jangan lupa boboo"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HOz9QgOiiARM1ojIK1_Yzt1kUf7ApEPj",
            "https://drive.google.com/uc?export=view&id=1lKoBssPSgui-PAzcNWhHEYmaSl_3XjHH",
            "https://drive.google.com/uc?export=view&id=1sOIZ-N1UWsalxulx5RytdqLjB9Oftr_h",
            "https://drive.google.com/uc?export=view&id=1legUFBz2oO9MWOSA7oblrtb084TXCacR",
            "https://drive.google.com/uc?export=view&id=1xMUtRehkkRjZFwUe0JdzBGkf0-_vlRbG",
            "https://drive.google.com/uc?export=view&id=1u4geRP-rJFhkHQzrVCLHFm3KkhTll0oi",
            "https://drive.google.com/uc?export=view&id=1CZLWf_TLt3lptrl4e6uQ2SCzwlJnlRFS",
            "https://drive.google.com/uc?export=view&id=181E4lV2_bv5j96k14iT5Z0knXy793JHg",
            "https://drive.google.com/uc?export=view&id=1BX93yY_GX1w7ErHkhzvPPPtKmHWPzCqX",
            "https://drive.google.com/uc?export=view&id=1EIPz_g5doGYT8CpMuXaqwcwBZFrkiR1o",
            "https://drive.google.com/uc?export=view&id=11YaNaCsc9O9fZ9MRKuXCzvqLEfz22pIs",
            "https://drive.google.com/uc?export=view&id=1ZETDM96BJ2Xg_sXn2AcO5movbKY7Ojv9",
            "https://drive.google.com/uc?export=view&id=1b72xHipXSeBfxHziY6J8sp785AKpy3fl",
            "https://drive.google.com/uc?export=view&id=1hUQzGupRyX94UuDZHdhwRCyLA0G1KPoy",
        ]
        data_list = [
            {   
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"B2, NO 2",
                "alamat": "Pulau Damar",
                "hobbi": "Zumba di pln setiap jumat pagi",
                "sosmed": "@jeremia.s",
                "kesan": "Bang jer orangnya punya positif vibes, asik juga ngobrol sama bang jer",  
                "pesan":"Jangan pernah nyerah ya bang"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto, Jawa Timur",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak dhea orangnya ramah, nyambung banget kalo ngobrol",  
                "pesan":"Kalo cape mam es krim aja kakk"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha orangnya asik, ramah, dan humble banget",  
                "pesan": "Semoga sukses selalu kak!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Muara Enim, Sumatera Selatan",
                "alamat": "C2",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Kak Anisa orangnya baik dan perhatian.",  
                "pesan":"Semoga selalu bahagia."
            },
            {
                "nama": "Dharu Cahyo Aji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Bengong",
                "sosmed": "@dhruchyo",
                "kesan": "Bang dharu pinter, panutan banget.",  
                "pesan":"Selalu menginspirasi ya bangg, ditunggu gebrakan barunya."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Menggodai Abang Cimol",
                "sosmed": "@fby.wlndr",
                "kesan": "Kak Feby lucu bangett tauu, kayak loppyyy.",  
                "pesan":"Selalu bahagia kakk."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro berwibawa banget, ramah juga.",  
                "pesan":"Sehat dan bahagia selalu bang."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Abang Mirzan orangnya asik, humble, dan perhatian.",  
                "pesan":"Semangat terus bang, jangan lupa makann."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Mengukir sabun",
                "sosmed": "@berlyyyanda",
                "kesan": "Kak Berliana orangnya baik dan ramah banget.",  
                "pesan":"Tetep jadi orang baik ya kak."
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Kalimantan Utara",
                "alamat": "Belwis",
                "hobbi": "Sibuk",
                "sosmed": "@j__eesia",
                "kesan": "Kak Juesi lucu dan asik banget diajak ngobrol.",  
                "pesan":"Selalu bahagia kak, jangan lupa mamam."
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Gang Sakung",
                "hobbi": "Main  Padel",
                "sosmed": "@ianridhomanik",
                "kesan": "Abang Ridho orangnya asik, humble, dan perhatian.",  
                "pesan":"Semangat terus bang kuliahnya, jangan nyerah ya"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal": "Bangka Belitung",
                "alamat": "Kobam",
                "hobbi": "Nongkrong di gedung f",
                "sosmed": "@fer_yulius",
                "kesan": "Bang Feryadi orangnya asik dan ramah.",  
                "pesan":"Semoga selalu bahagiaa."
            },
            {
                "nama": "Monika Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Ketapang, Kalimantan Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monca_tjg",
                "kesan": "Kak monica ramah, lucu, dan seru banget",  
                "pesan":"Jangan pernah cape bimbing kita ya kak!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pekan Baru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak wawa lucuu,kalo iket rambut kanan kiri kayak bocill",  
                "pesan":"Semangat kuliahnya kak wawa cantii!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PNIGUM1H2zs1VjsG8a6Sf_YPV8wqIuMp",
            "https://drive.google.com/uc?export=view&id=1xeyVf_4beHhqjWfF2af74Us0ZSClX3sR",
            "https://drive.google.com/uc?export=view&id=1IJl95i50wS9nmniq3_tPviMnIO9mlomi",
            "https://drive.google.com/uc?export=view&id=1a9y-VdJDl3owV0Q7jJXtMVyJMQIP-TdT",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "-",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Bintang awalnya ku kira serem, tapi ternyata abangnya lucu juga, ketawanya bikin ikutan ngakakk",  
                "pesan":"Info mancing di roblox bang!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "kak nadya sayangkuuu, penyelamat gweedyyy, imupppp teruss",  
                "pesan":"Sayangg kak nadyaa, makasi yaa kakk, maaf selalu ngerepotin kakak"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah orangnya asik dan ramah banget, inspiratif pula",  
                "pesan":"Semangat terus kakk, jangan lupa jaga kesehatan yaa!"
            },
            {
                "nama": "Lia Hana Ichisassmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kak lia baik, ramah bangett",  
                "pesan":"Terima kasih banyak kak lia udah bimbing kita semua, semangat terus yaa kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA" :
    def departemen_psda():
        gambar_urls =  [
            "https://drive.google.com/uc?export=view&id=1xWIKI-qdgj3ZsXceOh4KYjTAR4oCF5Vf",
            "https://drive.google.com/uc?export=view&id=13YqZUSKXno5FPCiujDqBAJ71S9YuQA2e",
            "https://drive.google.com/uc?export=view&id=1ogkUoAUY5kgWsX2P3QcRZuZYrAts0DXq",
            "https://drive.google.com/uc?export=view&id=1Cg5JokVd-c1gH7cMi42j7xCC252T1c94",
            "https://drive.google.com/uc?export=view&id=1rW-Wx7bfjHgMIJUvzEHWVgPbLDXWGiPK",
            "https://drive.google.com/uc?export=view&id=1nCBn51NY_gsb6nCGr10NExfBl_eE1BHY",
            "https://drive.google.com/uc?export=view&id=14gIptnUzOxB5zyBkIbd51pn92rFseKRg",
            "https://drive.google.com/uc?export=view&id=18l1bE1_3Es72x1Y3AgT4jp3MJcdGk74X",
            "https://drive.google.com/uc?export=view&id=1y7Q0bUOoDGpkhTWruihsf6cfzd93Jstf",
            "https://drive.google.com/uc?export=view&id=1JAbWz2Kh05zGZ_mx6duynGfugGF_6zYB",
            "https://drive.google.com/uc?export=view&id=1CJ_J7EWFBFlbz_ryJrYef-AS7wgoaXn7",
            "https://drive.google.com/uc?export=view&id=1WfOdPxQugUFhL-Wx71VZ78v86Bqb2EyE",
            "https://drive.google.com/uc?export=view&id=1rsic0Dex7U7_6gUdEooKqqDn_MV3w4vf",
            "https://drive.google.com/uc?export=view&id=1ji5VO8yQ6XycDMzwb6chsJ1yVTdn_Qk6",
            "https://drive.google.com/uc?export=view&id=1QbrQMZhgmjQd2aTKD8fYtmpiMwPkNCys",
            "https://drive.google.com/uc?export=view&id=1zRVlPQnQK-rUj7JPOajqtaxec_DA6ueh",
            "https://drive.google.com/uc?export=view&id=1l4JtPYTACL1W9-Zi-QoJeha1I9Jaqi_7",
            "https://drive.google.com/uc?export=view&id=13gcEpp0xDRbS_-LFGjfr4bT0c4dPoUxc",
            "https://drive.google.com/uc?export=view&id=1quz4aT90ILvFI4FXroRha4W7LOrK0H2E",
            "https://drive.google.com/uc?export=view&id=1fYfT_WM-khVYrg4rC8k-VwybLq7DJD3j",
            "https://drive.google.com/uc?export=view&id=1ZOEHiYPnB6glkJxoRmpAeqn8Eolin5j7",
            "https://drive.google.com/uc?export=view&id=1W9PGjI1W2Q6_MqE-1g-AqMb1cnoP1bcO",
            "https://drive.google.com/uc?export=view&id=10ZpRitEaTFeyp2Y5TD0GvA-7t3Y0V74C",
            "https://drive.google.com/uc?export=view&id=12dNs9tyEoqhjwEadFllMXOqRpV2RoLLz",
            "https://drive.google.com/uc?export=view&id=133fMN0jDkJiRSCEsusk9R8Y8po6jml3m",
            "https://drive.google.com/uc?export=view&id=1ysmlhX999zaZzJv7t2EXkR_QgutyT8uZ",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Tanjung Senang",
                "hobbi": "Futsal",
                "sosmed": "@ferdy_kevin",
                "kesan": "Bang kevin orangnya asik, humble, dan perhatian.",  
                "pesan":"Semangat terus bang, jangan pernah cape bimbing kita"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "kak Nisrina cantik, lucu, dan baik.",
                "pesan": "Selalu bahagia ya kak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kak Allya profesional, tegas, dan inspiratif.",
                "pesan": "Sehat selalu kak, terimakasih sudah dibimbing."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Bang ahmad keren, selalu keren, inspiratif, imup waktu mampir ke sekre perpom.",
                "pesan": "Semangat terus bang, makasi uda selalu support kita."
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "sebelah  kos bang dapa",
                "hobbi": "Liatin Haikal",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak arienta orangnya tegas dan profesional",  
                "pesan":"semangat terus ya kak, terimakasih sudah dibimbing!!"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "sebelah kos kak arin",
                "hobbi": "Isengin Fislam",
                "sosmed": "@daffahdynn_",
                "kesan": "Bang daffa orangnya asik, humble, dan perhatian, punya kepemimpinan yang baik",  
                "pesan":"semangat terus bang, jangan pernah cape bimbing kita"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Bang fajar tegas dan berwibawa, keren!!",
                "pesan": "semangat bang, makasi sudah diberikan pengalaman yang ga bisa didapet dari mana mana."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Kak nataysa baik, ramah, pertama kali ketemu waktu latihan buat dramus pplk.",
                "pesan": "Sehat selalu kak nataysa, semangat kuliahnya."
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Gg. Perwira",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel orang yang tegas, disiplin dan baik",  
                "pesan":"Semangat kuliahnya bang nobel, terimakasih sudah dibimbing."
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450022",
                "umur": "-",
                "asal": "Sumatra Barat",
                "alamat": "-",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Bang aji punya jiwa leadership yang oke banget",  
                "pesan":"Terimakasih bang, jangan pernah cape bimbing kita"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany orangnya ceria dan juga disiplin.",
                "pesan": "Jangan lupa jaga kesehatan kak, semangatt!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@sahid22",
                "kesan": "Bang sahid orangnya ramah banget, sabar, mengayomi.",  
                "pesan":"semangatt kuliahnya abang!"# 1
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Bang Ali ramah banget, terus nyambung kalo lagingobroll, seruu!",  
                "pesan":"Jaga kesehatan bangg, semangat kuliahnya!"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Kak Ferazka orangnya asik, ramah, dan lucu banget",  
                "pesan":"Bahagia terus kak!!!"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kak risma baik dan ramah banget",  
                "pesan":"Semangat terus kak, jaga kesehatan!!"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kak ocaa baik banget banget bangettt, seruuuu, imupp jugaa!",  
                "pesan":"Makasi ya kak udah perhatiian ke aku, udah ditemenin kalo aku masuk medis, sayangg kak ocaa"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Bang sahid orangnya asik, humble, dan perhatian.",  
                "pesan":"Bahagia terus bang, semangat kuliahnya!"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Bang daffa orangnya asik, humble, dan perhatian.",
                "pesan":"Semangat kuliahnya bangg"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Ibookkk, sayang ibokkk, ibok baik bangett, kangen perpommm",  
                "pesan":"Makasi ya ibokk, langgeng sama ayahhhh, lov ibok"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Bang ihsan chill abiezz, seru ngobrol bareng bang ishannn",  
                "pesan":"Arigataoooouu udsh dijagain waktu sakit diembung b bangg, sehat selalu abangg"          
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "Bang Kevin orangnya asikk dan disiplin jugaa",  
                "pesan":"semangat kuliahnya bangg"
            },
            {

                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kak lidia seruu, baik, ramah, dan lucu bangetttt",  
                "pesan":"semangat terus kuliahnya kakak"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Ngehina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "Bang ridwan seru, da humble bangett",  
                "pesan":"semangat kuliahnya bang ridwan !!!"
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Berenang, ngoleksi figura & kartu anime",
                "sosmed": "@rewinanaaa",
                "kesan": "kak rewina keren, baik jugaa, ramahh",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Bang benget orangnya asik, humble, dan ramah.",  
                "pesan":"semangat kuliahnya bang!!!"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesann": "Bang ulliano orangnya tegas, asik, ramah, dan perhatian.",
                "pesan":"semangat bang, jaga kesehatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c-EqGsCp1fGUt0oFXk3o8FTVMbs5ZRvl",
            "https://drive.google.com/uc?export=view&id=1uUilgvoMK5kxT30c9Qr3qgJXSducP7jF",
            "https://drive.google.com/uc?export=view&id=1PM6w44nxnU7sneqRq5wytHtRA8WNeZZ5",
            "https://drive.google.com/uc?export=view&id=1HFTCBr8axlZiSw0ShttNlLwYkXV4wPXv",
            "https://drive.google.com/uc?export=view&id=1LAYBQl4bvggmSewgRGEWNnMeuwQOhKll",
            "https://drive.google.com/uc?export=view&id=1LbrCIhp2MJB6mr4rxDcW4shub_Cd4Tgp",
            "https://drive.google.com/uc?export=view&id=1q7QjRVHbzS5-S9TlnlE6aJm-Cinpqq6W",
            "https://drive.google.com/uc?export=view&id=1Ym2MWWScgy1V7gR-NqDfMvK2Makm0clE",
            "https://drive.google.com/uc?export=view&id=1ojMJRmO1lhzjXiM63oDpw_jwknYCdl5L",
            "https://drive.google.com/uc?export=view&id=1nLV_mCZTAcfMh7DWxuHK5D8gTv7D3KCB",
            "https://drive.google.com/uc?export=view&id=17OmrSC4miXDUc7lZgx9IHO3HCEK_19Gx",
            "https://drive.google.com/uc?export=view&id=1w6P79jHS91PZ55WI6MRWOPRlOvLLZTwe",
            "https://drive.google.com/uc?export=view&id=13d2ERb9tHisvxSZsFdVR8OYrZTjLyanD",
            "https://drive.google.com/uc?export=view&id=16Ov7kxojt25mG9OB_eWOLi8LXBTqFgXr",
            "https://drive.google.com/uc?export=view&id=16JdTtw23belqlcQvHI0tu5Cz5-1opbMj",
            "https://drive.google.com/uc?export=view&id=1gp_1zT1Y42xLC6iPL_3vbsbyBcvu5Nv-",
            "https://drive.google.com/uc?export=view&id=1jXohMmNFGphc8pJE6QjKptXhyTBsYNJS",
            "https://drive.google.com/uc?export=view&id=1jKpEogeH26WLpmxn4pf-R0p2ZLbTsA7Q",
            "https://drive.google.com/uc?export=view&id=1f8QesszrTC8dcsZkEAyZEjFeuwzLbrit",
            "https://drive.google.com/uc?export=view&id=1EUd6zWCSRuJqJhxAGaZFQ_FKlNyRvzQu",
            "https://drive.google.com/uc?export=view&id=1T7LBOI8pwDznQTW1Fz_WjAMVcvMfNofh",
            "https://drive.google.com/uc?export=view&id=1d2M7J6ni86eOJngjk-gogiZwy6j29FgD",
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
                "kesan": "Bang randa kerenn, salut banget sama bang randa",
                "pesan":"ditunggu gebrakan barunya bang!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Kak juwita pinterr bangett, aku jadi termotivasii, hobinya kerenn.",
                "pesan":"Semangat terus kak juwita, jangan lupa jaga kesehatan yaa!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Keren bangett kak, hobi nyaa woow bangett!",
                "pesan":"Jaga kesehatan kak!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "ramah bangett, baik, seruu",
                "pesan":"Semangat kuliahnyaa"
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kak anggi baik banget pls pls pls mau nangiss, makasi yaAllah udah ciptain kak anggi",
                "pesan":"Makasi kak anggi udah dijagain di mediss, sayang kak anggi "
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kak faraj asik, positif vibes, ramahh",
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Senang bisa kenal kak evi, kakak baik banget kayak ibu periii",
                "pesan":"Makasi kak udsh ditutorin LMD, jaga kesehatan kakk"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "bang regi orangnya asik, ramah, dan sabar banget ngajarnya",
                "pesan":"Jaga kesehatan bang!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Bang fadil kerenn, selalu keren.",
                "pesan":"Semangat kuliahnya bang."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Bang razin baik, ramah, dan seru.",
                "pesan":"Semangat kuliahnyaa bangg"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kagum sama bang gio dari awal pplk, bang gio keren",
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Bang fabio asik banget, chill gituu.",
                "pesan":"Sukses selalu bang"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kak rahma baik, ramah, dan perhatian.",
                "pesan":"semangat kuliahnya kak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kak rahmah humble banget, lucu.",
                "pesan":"Semangat kuliahnya kak."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Bang aqil selalu keren, selalu nyapa.",
                "pesan":"Semangat kuliahnya bang!"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kak aisyah asik dan seru.",
                "pesan":"Semangat kuliahnya kak!"
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Senang bisa kenal kak tanty, mc lucu fg.",
                "pesan":"Semangat kuliahnya kak!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kak afifah asik, ramah, dan lucu bangetttt",  
                "pesan":"semangat terus kakak jaga kesehatan!!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Bang naufal asik, ramah, dan lucu bangetttt",  
                "pesan":"semangat terus bang jaga kesehatan!!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main piano, nyanyi, ngehalu",
                "sosmed": "@bee_0115",
                "kesan": "Kak fabiolla asik, ramah, dan lucu bangetttt",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kak fairuz asik, ramah, seruu",  
                "pesan":"Jangan lupa mamam kak"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Bang eggi keren, pinter orangnyaa, kagumm banget",  
                "pesan":"Semangat terus bang jaga kesehatan!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def DepartemenEksternal(): 
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PKBLpwej1ukWNuZCv_2naQvJCC4b-iHT",
            "https://drive.google.com/uc?export=view&id=1W6RJZsjY6sZ7lxqsscvz1BUA41Ys9Hcd",
            "https://drive.google.com/uc?export=view&id=1P_oYsByE-HD6BjfiLq4jGurhyBinfh5u",
            "https://drive.google.com/uc?export=view&id=1UsKf-qT4paSeA5efezKK9ebkI2J3N171",
            "https://drive.google.com/uc?export=view&id=1Dr_bJtEOUs9pUIhbl4q4lxputKOJ_CMl",
            "https://drive.google.com/uc?export=view&id=1pmN72XRSvUjT09htg17n_L6Ebo83uP_r",
            "https://drive.google.com/uc?export=view&id=1wjl8NFUTbZSR1l9NdBzv2HB2F3SbPK3h",
            "https://drive.google.com/uc?export=view&id=1ucxCVXBkeu5cPs4JpYMZSsJ7X1wkEIuj",
            "https://drive.google.com/uc?export=view&id=1LU7aSIEJRl_j20-SiTV8J4fZHNjP-g3G",
            "https://drive.google.com/uc?export=view&id=1YS9DcGVVrWDQ5HBI8tey375yH_IWMDzR",
            "https://drive.google.com/uc?export=view&id=1VSE362VlZ1XpzFgY_phOIx18B05kPd4o",
            "https://drive.google.com/uc?export=view&id=1-xM2gavKEqocXDJuvy1Cvgr1ZJImtuIG",
            "https://drive.google.com/uc?export=view&id=1Avxv-7_J4Gxf3V7jfa6iHCc-mLBlhf3f",
            "https://drive.google.com/uc?export=view&id=1EB49kgxUjCWuVGj3D2duCSMY1x462Nz2",                                     
            "https://drive.google.com/uc?export=view&id=1g8k3_Bfq1OQi4fiZdtoQkoslIFiLJmNm",
            "https://drive.google.com/uc?export=view&id=1pqrSuL00DV0W0J_rkfA6JjLCaeIdhSje",
            "https://drive.google.com/uc?export=view&id=1CIfVHYFx1RVwwH6u_rlzBYrCk6GBJImR",
            "https://drive.google.com/uc?export=view&id=1na8qqWw3gGAzcTtKq-_-7R3W0wSp7odV",
            "https://drive.google.com/uc?export=view&id=1tWZ-QfDhYtQ5qrXte-g7rYb82ygsOPMv",
            "https://drive.google.com/uc?export=view&id=1n2VgGoLFt2coGqif0rVY3AbFTfuZc5wN",
            "https://drive.google.com/uc?export=view&id=1zVMh8XGSLSuFBXxSTpwkeTVWUZ2surRO",
            "https://drive.google.com/uc?export=view&id=1xqMIzytFiIyEo6XJ77wuI7ByQWKjayFv",
            "https://drive.google.com/uc?export=view&id=1YtVvAnePLGCkQ3ElevR7LcNntGEyfxcK",
            "https://drive.google.com/uc?export=view&id=1phLhtbyg8h51Q9jJSaMipgzP6DCUGooi",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Bang Arafi orangnya asik, ramah, dan humble banget",  
                "pesan":"Semangat terus bang jaga kesehatan!!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana orangnya asik, ramah, dan humble banget",  
                "pesan":"Semangat terus kak!!!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kak mine baikk, ngertiin banget, dan asik diajak ngobrol",  
                "pesan":"Makasi kak udah dibimbing sellama magang, Semangat terus kak jaga kesehatan!!"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini orangnya asik, ramah, dan humble banget",  
                "pesan":"Semangat terus kak jaga kesehatan!!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Bang Arya orangnya asik, ramah, dan humble banget",  
                "pesan":"Makasi bang aryaa!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak mutt orangnya asik, ramah, dan lucu banget",  
                "pesan":"semangat kuliahnya kak!"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia orangnya asik, ramah, dan aga jaill",  
                "pesan":"Semangat terus kak jaga kesehatan!!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla orangnya asik, ramah, dan sabar banget kalo ngajarin tutor",  
                "pesan":"Semangat terus kak nabb, makasii ilmunya"
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "bang aldi chill bangett, seruu, ga boseninn",  
                "pesan":"Semangat terus bang  alll, makasii"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea orangnya asik, ramah, dan humble banget",  
                "pesan":"Semakin positive vibes kak!"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "kak cindy lucuu dan baik bangetttt",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak dea lucuu, baik bangettt",  
                "pesan":"semangat dan jaga kesehatan kak"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "bang desman orangnya seru, tegas juga, dan sering usil kalo praktikum",  
                "pesan":"jangan ganti ganti nama orang bang kalo manggill"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Baik banget banget kak sonyaa, asprak paling imupp",  
                "pesan":"semangat terus kakak jaga kesehatan!!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Lucuu banget kak luthfia, baik, ramah, dan asik diajak ngobrol",  
                "pesan":"Semangat kuliahnyaa"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Bang irvan orangnya asik, ramah, dan seru",  
                "pesan":"Semangat terus bangg, tetap humble pokoknya"
            },
            {
                "nama": "Aditya Taufiqrrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@ty_tq90",
                "kesan": "Bang adit kocak bangett, humblee orangnya, asik diajak ngobrol.",  
                "pesan":"Tetap jadi bang adit yang kocak"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya orangnya asik, ramah, dan humble banget",  
                "pesan":"Semangat terus kuliahnyaa kakak fathyaa!"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "kak ilmi lucuu, murah senyumm",  
                "pesan":"semangat terus kak jaga kesehatan!!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakakk danuss pplk yang gemecc, cantikk bangett, ramahhhh",  
                "pesan":"Semangat terus kak melinnn!! lovv"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "lucuu, baik bangetttt",  
                "pesan":"semangat terus ya kakkk!!! jangan lupa makannn"
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kak izzah baik bangettt",
                "pesan":"Semangat terus kuliahnya ya kakk!!, jangan lupa makann tetap humble!!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepulauan Riau",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin Bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "bang qois cool tapi kocak",  
                "pesan":"tetep jadi bang qois"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "Kak Tarisya orangnya asik, ramah, dan humble banget",  
                "pesan":"Semangat terus kak, jaga kesehatan ya!"
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-JpExrC_Ew5MKI5guYjTIXS2R6_ilgZv", 
            "https://drive.google.com/uc?export=view&id=1oUWLNIJzIvxs23UWYKiAt0ezq-HhfUpP",
            "https://drive.google.com/uc?export=view&id=1wwpdo7esIa9s0MTfTpI7o-470uWbMDrF",
            "https://drive.google.com/uc?export=view&id=1syGSMpNfDao1aHsnJ0LVy1W9Y9lWOHWj",
            "https://drive.google.com/uc?export=view&id=1yuoNxX2RuceKnIZvMeKqR2kjqcXT-JZN",
            "https://drive.google.com/uc?export=view&id=1bva9nrh6sN0yqmtNYIcU3aiQv_2mdfYz",
            "https://drive.google.com/uc?export=view&id=1-Bjj5btq5Aq6a0htQGjOeqO5iR-dYJur",
            "https://drive.google.com/uc?export=view&id=1mAUVQZpCB1WerLhh7HgLc69_E-XemmZu",
            "https://drive.google.com/uc?export=view&id=1bDg710b4pE857aro3ScXwWGJ2Ddr7U9Z",
            "https://drive.google.com/uc?export=view&id=1Yx63uf6THXHT-nc7DZ7zMfRwfTl4Lzv6",
            "https://drive.google.com/uc?export=view&id=1GcWRbBgPI_lMdtdK6NocUrjr218Rmdkz",
            "https://drive.google.com/uc?export=view&id=1jZ_oygO4qOL4mR6MdLNZ9TBLVhfXhy8_",
            "https://drive.google.com/uc?export=view&id=1rYmmnHsgHb8lBso-AlNYhqYzfQbHjhx6",
            "https://drive.google.com/uc?export=view&id=1tWw-m2GZBEXLwA1MoDwWax_KM-_3JkGV",
            "https://drive.google.com/uc?export=view&id=1JGn35icSB2e5dVlFrPw5kLS-jbJ9exWA",
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
                "kesan": "kak rani suka kucingg, lusyuu ",  
                "pesan": "semangatt teruuss kak" # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta orangnya asik, sabar, dan imut. ",  
                "pesan": "semangat kuliahnya kak."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "kak salwa lucuu, baik bangetttt",  
                "pesan": "semangat kuliahnya kak,jaga kesehatan " 
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "bang rendi masyaallah ",  
                "pesan": "semangat terus bang" # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "kak azzahra santai orangnya, baik, asik",  
                "pesan": "semangat menjalani hari kak" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "bang haikal tegas, disiplin dan juga profesional",  
                "pesan": "semangat terus bang" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "kak iqfina lucu, baik, pehatian.",  
                "pesan": "semangat terus kak" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "seru banget, asik, baik hati.",  
                "pesan": "tetep jadi orang baik kak" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "bang naufal asik, ramah, dan humble banget",  
                "pesan": "semangat terus bang" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "seru, obrolannya jadi nyambung. ",  
                "pesan": "bahagia selalu bang." # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "lucu bangett, seru banget ngobrol sama kak hana, extrovert level maksimall.",  
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
                "kesan": "kak karen lucuu, baik, asik",  
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
                "kesan": "bang hanif selalu keren, asik, dan ramah",  
                "pesan": "semangat terus kuliahnya bang !!!" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "kak sarah lucuu, baik, asik",  
                "pesan": "jaga kesehatan kak, jagan lupa makan" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "kakel dari SMA, ga nyangka aku ikutin kakak wkwkwk.",  
                "pesan": "semangat kak zahraa kuliahnyaa" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XJodGWEKjT8u_v6Zwn6BdftinLRztFv-",
            "https://drive.google.com/uc?export=view&id=1S5FJlNC1gfTH1fGWEDt_KLzqE9a3mRPf",
            "https://drive.google.com/uc?export=view&id=1poJEvZnALRFr6fP573LgnvIGVMNP3XWH",
            "https://drive.google.com/uc?export=view&id=1hphhyLHyFbjs3l8KEtoqUjXuoXNQsJl8",
            "https://drive.google.com/uc?export=view&id=1dZD0nWQzYDGUzgidQ_HWdf5uurKtHLXL",
            "https://drive.google.com/uc?export=view&id=1OYX4zIMEgXtvYhkemEbt08AogJvSR9Sv",
            "https://drive.google.com/uc?export=view&id=10dQIUcL9Em-bBwuMRroB16pQt4Q8czCa",
            "https://drive.google.com/uc?export=view&id=1L8vVnNxSQprNKIr49v307DzUf6o3Mg50",
            "https://drive.google.com/uc?export=view&id=1JzodT0QrtqtQNPv_DmyjpTZOE4PMk-tV",
            "https://drive.google.com/uc?export=view&id=1rmXMJRfXUct7Ymt0syVUH2MhRHPPywYH",
            "https://drive.google.com/uc?export=view&id=1FaNf2vZcrs0Uh-evOb30zuq_2sJUXQ_b",
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
                "kesan": "Bang danang orangnya asik, selalu ngasih arahan kalo kita bingungg ",
                "pesan": "semangat kuliahnya bang, jangan lupa makan"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "kak syalaisha baik, ramah, dan asik diajak ngobrol ",
                "pesan": "semangat terus kuliahnya kakak, jangan lupa makan"   # 2
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "abang rizqi asik, seru, dan ramah ",
                "pesan": "semangat terus kuliahnya bangg!!!"   # 3
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn__",
                "kesan": "kak anadia asik, seru, dan baik bangettt ",
                "pesan": "semangat terus kuliahnya kak, jaga kesehatan"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "kak aprilia ramahh, murah senyum ",
                "pesan": "semangat kuliahnya kak"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "kak nabila baik bangetttt, ramah juga ",
                "pesan": "semangat terus kuliahnya kak, jaga kesehatan"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "bang dhafin seru, ramah juga",
                "pesan": "semangat kuliahnya bang, jangan lupa makan"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "lucuuu, ramah bangett",
                "pesan": "semangat kuliahnya kak"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "kakaknya baikk banget, ramah, dan asik diajak ngobrol ",
                "pesan": "semangat kuliahnya kak, jaga kesehatan"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "ramah banget kak, lucuuu",
                "pesan": "semangat kuliahnya kak, jaga kesehatan!"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "kak nydia lucuu, baik bangetttt",
                "pesan": "semangat terus kuliahnya kak, jangan lupa makannn!!!"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tFVUu0qjDCb9n6wQpqcEDvDzIK2UIOSM",
            "https://drive.google.com/uc?export=view&id=1S2AAntqOqQEB9snN8VKSnM-yTKpuHVH4",
            "https://drive.google.com/uc?export=view&id=1-deOMP-0K4mnVNSX15BCPAY-B_ajFcJz",
            "https://drive.google.com/uc?export=view&id=1UKbJGPzyBuQS90QV3azeY9xlTvNwpq3k",
            "https://drive.google.com/uc?export=view&id=1V_RJl3Nciz0aP1YTHs9hXz3wJfNJIg9b",
            "https://drive.google.com/uc?export=view&id=1G43C9To7hiKjQ-JoVrspUxpHM-iJezQY",
            "https://drive.google.com/uc?export=view&id=1lXQjxZolNyR5UM1V-7xg4LqFIeONCUsx",
            "https://drive.google.com/uc?export=view&id=1s-bQOJANsANTL2FGwk13ZgvF_N_myUf9",
            "https://drive.google.com/uc?export=view&id=1KwY36PawM0safJR0RBOF7P-InjpWoSFV",
            "https://drive.google.com/uc?export=view&id=1mpP_Eg6HFaOAoA-xkzZnFzVBtj3wVj0H",
            "https://drive.google.com/uc?export=view&id=1__UFCsPlpMStO3HIbDprDQ-u2scp_yLp",
            "https://drive.google.com/uc?export=view&id=11WoCgWazoM2p6JDaMzGbxEmwh1UQHCO-",
            "https://drive.google.com/uc?export=view&id=1_KxgqL-2lo6ghxXN3QGwCOzDrH6km2hd",
            "https://drive.google.com/uc?export=view&id=1bemmCJa5eV4H9BAZ5mnaF9SDN9EpRZpC",
            "https://drive.google.com/uc?export=view&id=1yJQYPshXVg8002-op2r9e0Q8l6jhCFyk",
            "https://drive.google.com/uc?export=view&id=1SZe0Juq-M5as18F5EGMCuGCWUml5qOuk",
            "https://drive.google.com/uc?export=view&id=1M_e87PUgk35DB_AtENQ-JcrqKxbyEVG6",
            "https://drive.google.com/uc?export=view&id=1KTYFDHeXdGgTWwNxZnl_DC5_p906T9xY",
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
                "kesan": "kak cia super duper lucu, gemes banget, extrovert finall, ramah banget banget",  
                "pesan":"semangat terus kuliahnya kak ciaa, jangan lupa mam sama beli eskwimm"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "kak rahma orangnya asik, ramah, dan humble banget",  
                "pesan":"semangat kuliahnya kak nelii imut!!!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "ramah banget, murah senyum",  
                "pesan":"semangat terus kuliahnya kakak, jangan lupa mamam"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "bang rafi baik bangett, seruu, asik diajak ngobrol",  
                "pesan":"semangat kuliahnya bang rafii jaga kesehatan!!!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "kak rom imut banget aaaaa, baik bangett, asikkk",  
                "pesan":"semangat terus kak romaa jaga kesehatan!!!"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "keren hobinya kak, kakak juga ramah bangett",  
                "pesan":"semangat kuliahnya kak eigi, jaga kesehatan!!!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "kak citra lucu, baik sangat lah",  
                "pesan":"tetap humble kak citra, semangat terus kuliahnya!!!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "kak aliyah ramah banget, asik diajak ngobrol",  
                "pesan":"jaga kesehatan kak, semangatt"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kakak cantik bangett, lucuu",  
                "pesan":"semangat terus kakak jaga kesehatan!!!"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "kak refa ramah banget, asik diajak ngobrol",  
                "pesan":"semangat terus kak refaa jaga kesehatan!!!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "kak feby lucu bangett, gemsinn",  
                "pesan":"semangat terus kak feby jaga kesehatan!!!"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "kak raihana ramah banget, asik diajak ngobrol",  
                "pesan":"semangat terus kak raihana jaga kesehatan!!!"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "ihhb seru bangett main roblokss",  
                "pesan":"infokan mabar kak"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "kak nayla ramah banget, asik diajak ngobrol",  
                "pesan":"semangat terus kakk, jangan lupa makan!!!"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@_akmal.faiz",
                "kesan": "abang akmal asik, ramah, dan humble banget",  
                "pesan":"semangat terus kuliahnya bangg!!!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "kak dona ramah banget, asik diajak ngobrol",  
                "pesan":"semangat terus kak dona jaga kesehatan!!!"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "bang labo kull, tapi asikk",  
                "pesan":"semngat kuiahnya abangg"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "bang anam, asik, seru, ramah bangett",  
                "pesan":"semangat kuliahnya bang, jaga kesehatan"       
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()





# Tambahkan menu lainnya sesuai kebutuhan

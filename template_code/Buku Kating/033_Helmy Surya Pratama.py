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
            "https://drive.google.com/uc?export=view&id=1w4RbjTCxazOeh9JF2onkLGvE6LPSW9lV",
            "https://drive.google.com/uc?export=view&id=1vfJ1SlDrvOj02uUEDG-p2ENXNTeVFFtM",
            "https://drive.google.com/uc?export=view&id=1XVn5LtpzKXn-yjB6Gtzj2f5h5ssb6jGQ",
            "https://drive.google.com/uc?export=view&id=1LCKBlDrFF9iKDAadWzjzWaC1jz_CzIlC",
            "https://drive.google.com/uc?export=view&id=1zOsbcdKrFn68GWDsYEIR_eYy1R6KHjI3",
            "https://drive.google.com/uc?export=view&id=1GQdFQdnCEdZwT3I2OOcJuQ6UxsH3IsTx",
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
                "kesan": "Kahim paling debestt, ramahh sekali",
                "pesan": "semangat terus ya Bang Rendraa !!!"  # 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar - dasar sql",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Jo asik sekalih orangnya",
                "pesan": "semangat terus Bang Joo !!!"  # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kos",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kak Abeth asikk bangett lucuu",  
                "pesan":"semangat terus kak Abeth!!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza dingin, kalemm",  
                "pesan":"semangat terus Kak Syadza !!!"# 1
            },
            {
                "nama": "Eksanty F Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku saku Pramukar",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty seru, asik waktu bawain materi",  
                "pesan":"semangat terus Kak Eksanty!!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang, Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kak Farahanum pendiem tapi seru ",  
                "pesan":"semangat terus Kak Farahanum!!!"# 1
            },
        ]

        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X0S7J1Gy4LOilPW7Ax2v7TTTeK1tv7XM",
            "https://drive.google.com/uc?export=view&id=1DvuCeGKP_CqMhXPOXFBFc-mH2uXQIQXZ",
            "https://drive.google.com/uc?export=view&id=11BOdrNaRZz8WWrAw6srgWJOO_EcxtmSY",
            "https://drive.google.com/uc?export=view&id=1qXuZIDQrxn-kNnSfkzRy1v8JKo2huMDU",
            "https://drive.google.com/uc?export=view&id=1mOu4daDKj7UxMGqcEmha_AY3Meb_tth7",
            "https://drive.google.com/uc?export=view&id=1sHKUihSctQ8VGlY2BciO2SzTcNF5hihL",
            "https://drive.google.com/uc?export=view&id=1zNurxZde1yHJ6GGDI3j4Vs8N98-jhhsk",
            "https://drive.google.com/uc?export=view&id=1b_i-UaA5GY9mGrjTQBDv_Ar5w7H1WzJI",
            "https://drive.google.com/uc?export=view&id=1_aFmPtGnluofFpFtNkWiAa0wmdVjeb4e",
            "https://drive.google.com/uc?export=view&id=1AQs3W2QFn2ub2iMk_DVw6v3gDXCJbSNz",
            "https://drive.google.com/uc?export=view&id=1cuL_moLAxnN_aj7EAs0diwqVeL6VhzTW",
            "https://drive.google.com/uc?export=view&id=178FHHP41wPZpPbyeTVqtOucX_zWzXvdY",
            "https://drive.google.com/uc?export=view&id=1c266T9AAyzSM7yK_u6WnUnwETW4Gxxn7",
            "https://drive.google.com/uc?export=view&id=1V-kC--03iZJUyOLi_2M_c4QHPdgBaych",

        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "12250022",
                "umur": "21",
                "asal":"Kutai Timur",
                "alamat": "Bilabong",
                "hobbi": "Nontonin orang kayang",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang Jere asik beutt orangnyaa",  
                "pesan":"semangat terus Bang Jere!!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "Lomba ga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak Dhea lucu banget orangnya",  
                "pesan":"semangat terus ya Kak Dhea!!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Tidur",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha seru, lucu beutt",  
                "pesan":"semangat terus Kak Renisha!!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi morse",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak Anisa baik bangett, ramahh",  
                "pesan":"semangat terus ya Kak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "Bang Dharu asikk betzz, no jaim - jaim",  
                "pesan":"semangat terus Bang Dharu!!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kak Feby ramah bengetzz orangnyaa",  
                "pesan":"semangat terus ya Kak Feby !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro cool abiezz orangnyaa",  
                "pesan":"semangat terusang Givaro !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan paling kece dahh di Baleg",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus Kak Berliana !!!"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Lupa bales chat",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue ramahh bangett, kalemm auranyaa",  
                "pesan":"semangat terus Kak Juee !!!"# 1
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Gh",
                "hobbi": "Main padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridhoo supakull beutt",  
                "pesan":"semangat terus Bang Ridho !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "Koleksi bath google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "Bang Feryadi diem - diem lucu orangnyah",  
                "pesan":"semangat terus Bang Feryadi !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monic baik sekalihh, seru orangnya",  
                "pesan":"semangat terus Kak Monicc !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Kota Tarakah",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nashwaalhasni",
                "kesan": "Kak Wawa seru orangnya",  
                "pesan":"semangat terus Kak Wawa !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lu47GJ16VxfjxdcM9YStLaP9ODGSoBNc",
            "https://drive.google.com/uc?export=view&id=1cohPAqSag7hshdQ-MmV9q-xtHzfYXk5m",
            "https://drive.google.com/uc?export=view&id=1tRZx_vWhBWhPgKrO9gpX5J1js2ahJ61r",
            "https://drive.google.com/uc?export=view&id=1jHxWFqm3rKABP56Ei-tdafLVdCYSwPAR",
        
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
                "kesan": "Bang Bintang enak banget pembawaannya, becanda muluu",
                "pesan": "semangat terus Bang Bintang !!!"  # 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kak Nadya kalem banget orangnya",
                "pesan": "semangat terus Kak Nadya !!!"  # 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main Ice Skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak Azizah kalem, supakull pokonya mahh",  
                "pesan":"semangat terus Kak Azizah!!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Ichi baik lucu beutt",  
                "pesan":"semangat terus Kak Ichi !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tGCaZUPWU32UDtIx3zGizhTsnshDfgJ9",#kevin
            "https://drive.google.com/uc?export=view&id=1zy3rgTLgtesEt8DUIszFB_x20O5aEw5K",#afifah
            "https://drive.google.com/uc?export=view&id=1TAILv3fh-2YuLJ_14hEkP-w0B7qQOF_v",#allya
            "https://drive.google.com/uc?export=view&id=1YN_z85Yx_B_5WppqDfhQCHIEGXMf-HxP",#ahmad
            "https://drive.google.com/uc?export=view&id=1CVlRzSOkeJNXuNj5v5JoTd6ht45t0Unw",#arienta
            "https://drive.google.com/uc?export=view&id=19VD7XsKDooCB3gqCPCpD7GkEWsjbbl0U",#daffa
            "https://drive.google.com/uc?export=view&id=1UGeq5tgsmg8bAj_2TH5EZdTl-4hLLBqB",#fajar
            "https://drive.google.com/uc?export=view&id=1I9cNrtLvr1zz47ilQ5wYP3AjMgV95Uwf",#natasya
            "https://drive.google.com/uc?export=view&id=1IB_Zz-YqFeifNrwXei_g9DMj9aVfoOGV",#nobel
            "https://drive.google.com/uc?export=view&id=1SYnAxiNCZBSu7DTNL3crKhbzQCmS_HHN",#aji
            "https://drive.google.com/uc?export=view&id=161-pl-joz978Mh04pf2NjV-Vs4huCYSC",#vany
            "https://drive.google.com/uc?export=view&id=1XD63eBdCD6GKAVMVjtJ6HmM1m5Xb2HAv",#sahid
            "https://drive.google.com/uc?export=view&id=1D-C3fjvKZIDH4IcExVsckGVjvPSdwwOB",#ali
            "https://drive.google.com/uc?export=view&id=1THlLwzKp2VOvu1nt0Fne0_VBxxkLC29t",#razka
            "https://drive.google.com/uc?export=view&id=1itW8BuBOJZDG3CBys9PGLQVT70JvFcC2",#kharisma
            "https://drive.google.com/uc?export=view&id=1LAnwrf4C49pGomZnZ5Uwara5ISBD4u3L",#rosalia
            "https://drive.google.com/uc?export=view&id=1GpovWlyDqH9Ka2bDPzetK5gYubiVrNAs",#maul
            "https://drive.google.com/uc?export=view&id=1bV4GANNo34CYfI0LEHfoLVya6jLDpwq-",#daffahmad
            "https://drive.google.com/uc?export=view&id=1aQa_d9pa01GDAqAKOgjcFMs4QV25lZnL",#daniar
            "https://drive.google.com/uc?export=view&id=1CjsU8eUYv8mjPCI996u5rnuFAFnmLcW_",#ihsan
            "https://drive.google.com/uc?export=view&id=1hgUw4iZ27YU7L9KsUE5qcJxc_ibG3x7S",#kevin
            "https://drive.google.com/uc?export=view&id=1nRflVxu6TRlCEaODJXOO7snS9iGbi9oL",#lidia
            "https://drive.google.com/uc?export=view&id=1tiKabMb4oN4RTLBGseq5FSdnr48aGGzk",#ridwan
            "https://drive.google.com/uc?export=view&id=1FbeUjzjbUHamo9ITO5QVYE8Kg8eUWY4X",#liano
            "https://drive.google.com/uc?export=view&id=1qxGzu-6aPPVdnh5Lt00E_Hx82AV1-dKe",#benget
            "https://drive.google.com/uc?export=view&id=1OCd8al5BkWua4n2xKkArp6RBAPOCDF9f",#rewina
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Bang Kevin ternyata orang lucu, ga nyangka psa stand up",  
                "pesan":"Semangat terus Bang Kevin"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20 ",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Afifah baik, melet mulu gayanya",  
                "pesan":"Semangat terus Kak Afifah"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kak Allya menginspirasi pendiriannya",  
                "pesan":"Semangat terus kak Allya"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "Kontrakan GH",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang Ahmad keren bangett pemikirannya",  
                "pesan":"Semnagat terus Bang Ahmad"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Kost Orange",
                "hobbi": "Ngekader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arien pembawaanya tenang",  
                "pesan":"Semangat terus Kak Arien"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Kak Arienta",
                "hobbi": "",
                "sosmed": "@daffahdynn_",
                "kesan": "Bang Daffa ternyata lucu juga orangnya",  
                "pesan":"Semangat terus Bang Daffa"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game",
                "sosmed": "@ginda_mrp",
                "kesan": "Bang Fajar orangnya baik sekali",  
                "pesan":"Semangat terus Bang Fajar"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kostan putri gerbang barat sebelah sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Kak Natasya baik orangnya",  
                "pesan":"Semangat terus Kak Natasya"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel paling jago ngoding",  
                "pesan":"Semangatr teruss yaa banggg"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma Fam",
                "hobbi": "Mancing keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Bang Aji bener bener berwibawa",  
                "pesan":"Semangat terus ya Bang Aji"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Dekat masjid",
                "hobbi": "Belajar",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany baikk orangnyaa ",  
                "pesan":"Semangatt teruss ya Kak Vanyy"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22__",
                "kesan": "Bang Sahid diem - diem, jago badminton",  
                "pesan":"Semangatt tersuss ya Bang Sahid"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Nangka 4",
                "hobbi": "Main Game, Kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya supakulll, kalemm betzz",  
                "pesan":"Semnagatt teruss Bang ALi"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Razka orangnya imuppp betss",  
                "pesan":"Semangat selaluu ya Kak Razka"# 1
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "122450079",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma kerenn betss",  
                "pesan":"Semangat selalu kak Kharisma"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kak Rosa caree banget waktu jadi medis",  
                "pesan":"Semangatt selalu kak Rosa"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jalan Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Ramahhh cekaliii waktu ketemu di studio",  
                "pesan":"Cemangattt celalu Bang Maull"# 1
            },
{
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Jl. Korpri Raya",
                "hobbi": "nontonin anak tari latihan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Keren bangett supakull dahh pokonyaa",  
                "pesan":" Semangat terus bang Daffa"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "Narinya jagooo bangetzz Kak Daniar",  
                "pesan":"Semnagatt terus ya Kak Daniar"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Belwis",
                "hobbi": "Joki Strava",
                "sosmed": "@ihsan.myusus",
                "kesan": "Bang Ihsann kocak beutt orangnyaa",  
                "pesan":"Semangatt empat lima Bang Ihsan"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat":"Panjang Selatan",
                "hobbi": "Terjun Payung",
                "sosmed": "@kevinaj__",
                "kesan": "Ga nyangka bang kevin tetanggaan sama temen SMA saya",  
                "pesan":"Semangattt selaluu bang kevin"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kak lidia jagooo beutzz narinyaa",  
                "pesan":"Cemangattt ya kakk"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton Anak Tari Perform",
                "sosmed": "@m.ridwan_22",
                "kesan": "Abangnnya pendiemm bangett dan baikkk bangett",  
                "pesan":"Semangattt alwayss bang Ridwann"# 1
            },
            {
                "nama": "Uliano Wilyam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Ngerjain Soal MTK",
                "sosmed": "@liano.wlm",
                "kesan": "Bang Lianoo supakulll no debastzz",  
                "pesan":"Semangattzz alwayss bangg"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "main bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Lucu bengetzzz bang benget ini",  
                "pesan":"Semangatt selaluh ya Bang Benget"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Ratu, Bandar Lampung",
                "hobbi": "Nonton Anime",
                "sosmed": "@rewinanaa",
                "kesan": "Kak Rewina baikk bangett dan lucu ngomongnya",  
                "pesan":"Ganbatte Kak Rewina"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan

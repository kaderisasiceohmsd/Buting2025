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

elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1t-0bC1uVv4nMuz7QREjg7OTE18I-oA5c",
            "https://drive.google.com/uc?export=view&id=178PL_Ckv9OSnA_QjUPCt8nWmETYTOJNO",
            "https://drive.google.com/uc?export=view&id=1LmtfLAAw3oM3YL1cY8Y6Uyb7V6oO7bGY",
            "https://drive.google.com/uc?export=view&id=1tIb56cslhQFfEH3X50VtHFkeJTztxydS",
            "https://drive.google.com/uc?export=view&id=1rDedPKq-JrMjS0egBr8zJSW7-UtXzpCa",
            "https://drive.google.com/uc?export=view&id=1cQUgkDHLVb_-S_txEjISxvL5ECtvg1EG",
            "https://drive.google.com/uc?export=view&id=1Gc1au-i7Y8ySrIakwaxUDow5I2Fgky6e",
            "https://drive.google.com/uc?export=view&id=1tVYcdGjXEJVOPFqsONGKvQW2u5ftMF9U",
            "https://drive.google.com/uc?export=view&id=1UUdLhTktQJxzahktdQgbQ7yIFFwGQtJ5",
            "https://drive.google.com/uc?export=view&id=1ljoGrOm7eFR_xZmaxU63_VqVGJglBG4R",
            "https://drive.google.com/uc?export=view&id=12iwAdVXvaL65eswj0ba4lYZID6y6AVC1",
            "https://drive.google.com/uc?export=view&id=1Y5FKsciNJbUYDqSZ9hMHIedto-6tvkKP",
            "https://drive.google.com/uc?export=view&id=14_70SQZlBHPb9Wq7XdyTgEFxsvqUXtPJ",
            "https://drive.google.com/uc?export=view&id=1AM3ULHP3gw0s_80N0dgi-Bc4NqyFcSob",
            "https://drive.google.com/uc?export=view&id=138yG0PVxf3b9VTqC2jVSBkhSruL04rah",
            "https://drive.google.com/uc?export=view&id=1LDuje89QVW5NFja-oGDIRaYXYjLB7UKk",
            "https://drive.google.com/uc?export=view&id=1fEwOi8CWpcZzvw3kkRm7EBpMyQUGsd8c",
            "https://drive.google.com/uc?export=view&id=1z8_vnfzGZmf6RCSs4CPE4EeXDcrO_WYl",
            "https://drive.google.com/uc?export=view&id=17BrBxvpGjMbU6-oWkTa_VxMXHOJCicra",
            "https://drive.google.com/uc?export=view&id=1eKKSqgMW2s77WgoCOGlkOS2ZgmZeJSpF",
            "https://drive.google.com/uc?export=view&id=1EW4KAwqS8XwDjfwIKhG7cWsJ08QiLAUz",
            "https://drive.google.com/uc?export=view&id=1j_1TgTjwpb4trnHqUF1P_mEsw0hVDkNm",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "1222450083",
                "umur": "22",
                "asal":"Serang,Baten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berenang",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa baik bangetzz soft spokenn",  
                "pesan":"Cemnagatzzz Bang Randa", # 1
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep.Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak Rut kalemm bangetzz",  
                "pesan":"Semangatt selalu Kak Rut", # 1
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@mregiiii_",
                "kesan": "Bang Regi diem diem lucu bangett",  
                "pesan":"Semangatzz alwayss Bang Regi", # 1
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kak Aisyah orangnyaa ademm bangett auranya",  
                "pesan":"Semangattt teruss ya kak. Aisyah", # 1
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Liat Jam",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Dutanya Itera Bang Fadil mahh",  
                "pesan":"Semangatt teruss Bang Fadil", # 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Jl. Kasuari Gg Salam",
                "hobbi": "Main basket",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya ramahh puoll",  
                "pesan":"Semangattt selalu Bang Aqil", # 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya pendiemm bangett, tapi saya penasaran kenapa abang dipanggil King sama Bang Bio",  
                "pesan":"Semangat selalu bang", # 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1 Way Huwi",
                "hobbi": "Nonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kak Nadia vibesnya positiff beutt",  
                "pesan":"Semangatt terusss ya Kak Nadia", # 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Kepo(baca codingan)",
                "sosmed": "@marletacornelia",
                "kesan": "Banggga sama sama orang depokk",  
                "pesan":"Cemunguttsss ya Kak Etaa", # 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234500119",
                "umur": "20",
                "asal":"Pramuka, Bandar Lampung",
                "alamat": "Perum Bukit Alam Permai 3, Blokk C, No.9",
                "hobbi": "Dengrin musik",
                "sosmed": "@keyashafi_",
                "kesan": "Lucu benarr loh Bang Akey, padahal mukanya kayak orang bener",  
                "pesan":"Cemungutt celalu Bang Akey", # 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jl. Seputih, Bummisari Kec.Natar",
                "hobbi": "Dance dan menyanyi",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kak Anggi seruu bingitsss asikkk orangnyaa",  
                "pesan":"Semangattt alwayss Kak Anggi", # 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Sale, Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi Baik puolll orangnyaa",  
                "pesan":"Tetap semangat menjakani hari kak", # 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kak Olla baikk bangettt lucuu ",  
                "pesan":"Semangattt selaluu Kak Olla" # 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang,Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kak Fairuz baikk betss orangnyaa",  
                "pesan":"Semangattt teruss ya kakk", # 1
            },
             {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Ngelihat Kak Tanty positive vibess bangett",  
                "pesan":"Be Happy Always kak semangat", # 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450004",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "tidur",
                "sosmed": "@_egistr",
                "kesan": "Bang eggi kalemm beuttt orangnyaa",  
                "pesan":"Semangatt teruss ya Bang Eggi", # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Airan,Hasan 4",
                "hobbi": "isengin orang (main game)",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah seruuu bingitss pembawaanya",  
                "pesan":"Cemangatts Celalu Kak Afifah", # 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No 27A, Kedaton",
                "hobbi": "game(proplayer),tidur,jalan-jalan",
                "sosmed": "@biyokcb",
                "kesan": "Bang Bio enak bangett kalau diajak ngobroll",  
                "pesan":"Cemunguttzzz yaaaa Bang Bio", # 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@giofaniars_",
                "kesan": "Bang Gio kalemm bangett euyy orangnyaa",  
                "pesan":"Semangatt teruss ya Bang Gio", # 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Laps Raya, Lampung Selatan",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakaknya asikkk bangett diajak ngobroll ",  
                "pesan":"Semangatt 45 Kak Rahma", # 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Airan 1",
                "hobbi": "Balap random",
                "sosmed": "@gustriana.d_",
                "kesan": "Kak Rahmah baikk sekaliii orangnyaa",  
                "pesan":"Semangatt teruzz yaa kakk", # 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450102",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Grans Sakum,Belwis",
                "hobbi": "futsal",
                "sosmed": "@razynhfd",
                "kesan": "Abangnya seruu bangett, kocakk",  
                "pesan":"Semangatt teruss ya Bang Razin", # 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ayv9espQ2CWf8MSPee3tCiCSxCic69nB",
            "https://drive.google.com/uc?export=view&id=1uXN0AoOSOg1h5nTW_1RiSCXeNVdv8Jve",
            "https://drive.google.com/uc?export=view&id=1aicnGjYnUv2XJgi8T-3abhcjL9Qqy0kL",
            "https://drive.google.com/uc?export=view&id=1sxC-X5X4LmvXkQl7FacQyk_aOnqlmDMx",
            "https://drive.google.com/uc?export=view&id=1TCKgKxRB718JNjEfO7k8veZIR1yxZ41O",
            "https://drive.google.com/uc?export=view&id=1H2yEyPjixTmVw1_8DbYjJlM2YT10VVzL",
            "https://drive.google.com/uc?export=view&id=11FGxBpGabgdf-yWBjri0K3I2nGq8onvq",
            "https://drive.google.com/uc?export=view&id=1KyTg6Sq3b_GXQMedIPEpIjXYzGvL4vnX",
            "https://drive.google.com/uc?export=view&id=1GLQ8EyJILFf_U2LMHFm7qjL-zrpAFPWf",
            "https://drive.google.com/uc?export=view&id=1JzaOX_vFU_K1xpUlalCy6VvWN6ZPIqSc",
            "https://drive.google.com/uc?export=view&id=1nDPlx16OBLe5t0GjjqXKRzDrJHmxSICY",
            "https://drive.google.com/uc?export=view&id=1CUG-2JBpmgSSw7M8pItqXjX3yYOjtVYK",
            "https://drive.google.com/uc?export=view&id=1RJEPy7tGNht5Wn43Wuro2EGw74QyyvO-",
            "https://drive.google.com/uc?export=view&id=1bog_X10wSg78MjAGG8UM1FEYAVdD_k6y",
            "https://drive.google.com/uc?export=view&id=1TvmxZ1gP-8srYPHz8dBBFgHfh-5HEYMU",
            "https://drive.google.com/uc?export=view&id=1rFcEtc7OFb92W20FCf1eOyZIzVhqSEia",
            "https://drive.google.com/uc?export=view&id=1wxcPZ4opDDFby31c-PrroHNxux886-ei",
            "https://drive.google.com/uc?export=view&id=1XMNDsIwclkC_skdj9jjIfC9Y-S7US_D2",
            "https://drive.google.com/uc?export=view&id=120yzmQMP89iY2FrRs0OfjQ9PMF8l9ATA",
            "https://drive.google.com/uc?export=view&id=1w2tgF6449DM9lDkDMNXfpGFFcuKi_089",
            "https://drive.google.com/uc?export=view&id=1ik9w6hUWQi-qIC2Eg8W8C4AV4khY-p4X",
            "https://drive.google.com/uc?export=view&id=1qFXNCHRNz3-yoeP13bgX5NZmIBpINOrI",
            "https://drive.google.com/uc?export=view&id=1VYmRuKfJUEjmVdpdMTzjappah0GxA0ZZ",
            "https://drive.google.com/uc?export=view&id=117Iirq6aq7INE60fH-fJWIctdyPa6z4E",
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
                "kesan": "Bang Arafi humblee bangetzzz",  
                "pesan":"Semangat truzzz Bangg Arafi"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gg. Sakum",
                "hobbi": "Menanam ubi",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana seru sekalii waktu ngobroll",  
                "pesan":"Cemangattt celalu kak Yohana"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Jalan-jalan",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya seruu abiesss",  
                "pesan":"Stayy Positive yaakk Kakk"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Jalan-jalan",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya Baikk dan ramahh",  
                "pesan":"Semngat terus Kak Arin"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Pahoman",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya supakulll",  
                "pesan":"Semangat selalu Bang Arya"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Mut baikkk bangett waktu ngasprak",  
                "pesan":"Sukses lancar selalu kak"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "20",
                "asal":"Amerika Serikat",
                "alamat": "Pemda",
                "hobbi": "Liatin Zayn Malik",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kak Lutfia lucuwww abizz",  
                "pesan":"Semangatt selalu kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla ramahh bangetzz",  
                "pesan":"Dilancarkan segala usahanya"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baca",
                "sosmed": "@",
                "kesan": "Abang Aldi baikk sekalehhhh",  
                "pesan":"Semoga sukses jaya selalu Bang"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Membaca",
                "sosmed": "@deaa.rsn",
                "kesan": "Kak Dea baikkk sekalihh",  
                "pesan":"Semangat kuliahnya kakak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak cindy palingg kece di Eksternal",  
                "pesan":"Sehat selalu kak"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea baikkk betzzz",  
                "pesan":"Semoga bahagia selalu kak"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermain musik",
                "sosmed": "@dsmannhal_",
                "kesan": "Bang Desman si pencair suasana",  
                "pesan":"Semangat terus Bang Desman"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Sukarame",
                "hobbi": "Bolak-balik gedung ITERA",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya ramah sekalehh",  
                "pesan":"Sehat dan Bahagia selalu Kak"# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "122450004",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Jalan Raden Saleh",
                "hobbi": "Menyenangkan waketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Lulu benar benar perangkul yang baikk",  
                "pesan":"Sehat Jaya Selalu Kak LULU"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Denger musik, badminton",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya keren banget",  
                "pesan":"Semangatt terus Abangkuhhh"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Samping Mie Aceh",
                "hobbi": "Baca Webtoon",
                "sosmed": "@ty_tq90",
                "kesan": "Abang Adit seruuu bangettt kalo dah ceritaa",  
                "pesan":"Be Yourself and Never Surrender ya Bang"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Nyuruh Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kak Fathya imoeppp kalehh",  
                "pesan":"Semoga makin sukses dan tetap ceria Kak"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "19",
                "asal":"Sumatera Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Ilmi Baikk sekalehhh",  
                "pesan":"Semangat always ya kak"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Nonton film",
                "sosmed": "@melynznb",
                "kesan": "Auranya emang cocok jadi Miss Indonesia",  
                "pesan":"Sukses Jaya Selalu Kak"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Cari info loker",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla seru banget diajak ngobrol",  
                "pesan":"Semangat 45 KAK"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya bikin happy banget",  
                "pesan":"Sukses dan bahagia selalu kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya bener bener asikk",  
                "pesan":"Semangat always ya Bang"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gerbang Barat",
                "hobbi": "Menjejak desa di Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakak Tutor terdebesttt",  
                "pesan":"Sukses bahagia selalu kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

elif menu == "Departemen Internal":
    def DepartemenInternal():
         gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1W3zwEYsLfrI_hVhUzrDT9exwcZ0Qx3Nf",#rani
            "https://drive.google.com/uc?export=view&id=1e2eqM_LMNKdSmDXwv9p98ywKv3awuM88",#renta
            "https://drive.google.com/uc?export=view&id=1bX_-RRxIKpS1OasVFg9YOPo_xMMyD-QJ",#salwa
            "https://drive.google.com/uc?export=view&id=15fQgonkyy_-NQgBe-oZv34xcLs4G-B28",#azzahra
            "https://drive.google.com/uc?export=view&id=1u038KkUf5_5wNPmUseYBOZY-vuAnaryw",#haikal
            "https://drive.google.com/uc?export=view&id=14Hb2oZfkdjysqWrwseXZpgq45NK3ZTyu",#iq
            "https://drive.google.com/uc?export=view&id=16a73rEIcQEq7ylY2jlyBpKeJg7v-y3zO",#may
            "https://drive.google.com/uc?export=view&id=1YCaHMTRZYLekLAmBwvNyPx1pO4MRXhet",#anufal
            "https://drive.google.com/uc?export=view&id=1Ni7GY7KpdmClV551Nc5AI07WXvNyAoIx",#zailani
            "https://drive.google.com/uc?export=view&id=1L-AyCeBUv-Kk8hI80VAdKPqFqm_AbDBc",#rendi
            "https://drive.google.com/uc?export=viem&id=18P13T9gAIEciKbxtUAm21fPkuWy-zpYN",#hanna
            "https://drive.google.com/uc?export=view&id=1cpTCIgjJLgabe-AtzrxkSRfVVNDkl7TY",#keren
            "https://drive.google.com/uc?export=view&id=1qoPvoA1fD7wR6Ew-ihfIe6i-URV8LYjv",#naufal
            "https://drive.google.com/uc?export=view&id=1UDCopkuYMi9dtCb_Ht3h1QtUQwQeny58",#sarah
            "https://drive.google.com/uc?export=view&id=1AUcu_7injd0d_1RK8ULVaLVEY00Tz_kd",#zahra
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
                "kesan": "Kak Rani skenaa abiezzz",  
                "pesan":"Semangatt teruss Kak Rani"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumut",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta baikk bangett ramahh",  
                "pesan":"Semoga sukses selalu ya kak!"# 1
            },
            {
                "nama": "Salwa Farhanatusaiidah",
                "nim": "12245055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa ademm banget vibesnya",  
                "pesan":"Semoga semangatt alwayss kak"# 1
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@azza.raaa_",
                "kesan": "Kak Azzahra mirip kek penyanyi dah",  
                "pesan":"Semangat terus ya Ka!"# 1
            },
            {
                "nama": "Haikal fransisko Simbolon",
                "nim": "122450106",
                "umur": "18",
                "asal":"Tulang Bawang",
                "alamat": "Sukabumi",
                "hobbi": "Membersihkan rumah",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang Haikal diem - diem nih asikkk beuttt orangnya",  
                "pesan":"Lancar terus kuliahnya bang"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "122450076",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak iqfina kalemmm bangett",  
                "pesan":"Semoga selalu bahagia dan lancar kuliahnya ya, Kak!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "122450009",
                "umur": "20",
                "asal":"Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak may keren abizzz",  
                "pesan":"Semangattt alwayss ya kak"# 1
            },
            {
                "nama": "Muhammad Naufal Afghani",
                "nim": "122450116",
                "umur": "20",
                "asal":"Sidorejo,Sidomulyo,Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@Muhammadnaufalafghani73",
                "kesan": "Pendiem tapi kocakk abangnya",  
                "pesan":"Semangat terus ya bang"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "122450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Bang Zailani panutann, the bestt",  
                "pesan":"Semangattt teruss ya Bangg"# 1
            },
             {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@lexanderr",
                "kesan": "Bang Rendi auranya ademm banget",  
                "pesan":"Sukses bahagia selalu bang"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna ramah dan ceria banget",  
                "pesan":"Sukses terus kedepannya ya kak"# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "122450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kak keren ramahh baikk sekalehh",  
                "pesan":"Always happy and semangat kaka"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "122450064",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hifzky",
                "kesan": "Abang Hanif auranya adem banget kayak abis wudhu",  
                "pesan":"Sukses bahagia sewlalu bang"# 1
            },
            {
                "nama": "Sarah wasti",
                "nim": "122450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kak Sarah asik ramahh bangett euyy",  
                "pesan":"Semoga Sukses terus kak"# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "122450096",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Pemda, Way Huwi",
                "hobbi": "Main Rubik mirror 3x3",
                "sosmed": "@zhrptrsl",
                "kesan": "Kak Zahra baikk bangett orangnyahh",  
                "pesan":"Semangat selalu ya kak"# 1
            },
        ]
         display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pl276lIZ4fXIZbYU9YoEsikpcBt_sV_M", 
            "https://drive.google.com/uc?export=view&id=1SPY19zfvN9X2VCDeLWdaHPDOyxN46vzF", 
            "https://drive.google.com/uc?export=view&id=1W0rvOZHV8iIpcoDe451_AZhSlc6jEMCQ",  
            "https://drive.google.com/uc?export=view&id=1HSlIrdFfjEO0HuXUvvu4tNq5ZafRVVnR", 
            "https://drive.google.com/uc?export=view&id=1Prixd78cshV_nbtDSJ-ZPUK22DvQwIAO",  
            "https://drive.google.com/uc?export=view&id=1N-U5_EPAEckpIujdyXr2rVNfzf3yiXHo",  
            "https://drive.google.com/uc?export=view&id=1Om4LRXUw550xu-hWc-AFXdj7NBbWyjp1",  
            "https://drive.google.com/uc?export=view&id=1VL1_UXVtUnbyZ5aw-v9cAUOm22TLD9aa",  
            "https://drive.google.com/uc?export=view&id=1p6ywdBeeClIPjLJaaUs5G8NmIa74fhuD",  
            "https://drive.google.com/uc?export=view&id=1MdtKOI1SmPa9EaWdaO0EiUglrwQ7JA7w", 
            "https://drive.google.com/uc?export=view&id=1Ay6JQRvAot0zjJgG2aoxUWvCtsT1JUfM",
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
                "kesan": "Bener bener asikk bangett diajak ngobroll gak berasa bisa sampe lama",  
                "pesan":"Semangat terus abangda !"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450012",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya vibesnya adem bangett",  
                "pesan":"Semangat teruss ya kak!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Airan",
                "hobbi": "Beli Parfum",
                "sosmed": "@den_iki_",
                "kesan": "Jujurr paling skena ini abangnya",  
                "pesan":"Semangatt alwayss ya bangg"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Joging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya asikk bangett",  
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
                "kesan": "Kak April jago beutt narinya",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_azazahra",
                "kesan": "Kakaknya baikk beut aslii",  
                "pesan":"Semoga makin sukses dan bahagia selalu kak!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Jogging",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Aura businessmann jujur kuat bangett",  
                "pesan":"Semangat alwayss bang!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Main",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya seru banget",  
                "pesan":"Sukses lancar selalu kak"# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "gang perwira 2",
                "hobbi": "Nontol alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "Kakaknya cantik banget mirip artis siapa gituu",  
                "pesan":"Semoga sukses selalu kak"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak naya seru bingitzzz",  
                "pesan":"Semangat 45 ya kak"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr",
                "kesan": "Kakaknya asikk bener loh yahh",  
                "pesan":"Semoga bahagia selalu kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yHfRvFt-CZGdh71WPyypM5j6SW_AQNyP",
            "https://drive.google.com/uc?export=view&id=1_YgqAM-7rQqHbFYsveXZFCjyjX7m8Tlj",
            "https://drive.google.com/uc?export=view&id=18iYurvwmuXgjFzouxmH8JcFvJoqyKnC1",
            "https://drive.google.com/uc?export=view&id=1PVUtF5hUbi8cyX6Ylf5ZEjI1m5u7tVKy",
            "https://drive.google.com/uc?export=view&id=1iPf0TWxQnNadwDAGLMX2XxXJ4nO2LGGr",
            "https://drive.google.com/uc?export=view&id=16wUWgw2wTbXVcB91keG1LYe4ZSTVF9bf",
            "https://drive.google.com/uc?export=view&id=1uiX6vaJtwABo7w4bZJHkVD16jgZZFyNK",
            "https://drive.google.com/uc?export=view&id=1YnXbLxPy-RCSy8F7r_Gu8JhlxFnlhhzG",
            "https://drive.google.com/uc?export=view&id=1s4cWDNFB6dcBHefwut8_bUpTbfgr_tZd",
            "https://drive.google.com/uc?export=view&id=1ckZZDeQ6yXIZExkHHIypoavo_6RImF99",
            "https://drive.google.com/uc?export=view&id=1aZpFBUBa1mJIggAJtswnvSBu1EgCwvAN",
            "https://drive.google.com/uc?export=view&id=1MFD0xKZ_gEGQqXyaw5USV0XWUfSMhSs9",
            "https://drive.google.com/uc?export=view&id=1rtRFG2kiTKtKQLuNbtgQYYQQ994iBlFJ",
            "https://drive.google.com/uc?export=view&id=1VUBxZqrTnPIxaoh-85zSl5PqkWeiVcet",
            "https://drive.google.com/uc?export=view&id=1F43sxnC8nDz63n9iiwPzjhrUZUe80BGB",
            "https://drive.google.com/uc?export=view&id=11Y1xkt_OFi8ENsiTNPOqHrwHKBXBPhru",
            "https://drive.google.com/uc?export=view&id=1wVC5NgGm_UWvFSNFxKWMjSkTO7dXm5E8",
            "https://drive.google.com/uc?export=view&id=1e0eKM3VnKRD2OZytoV1TIde0sxwCL_tw",
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
                "kesan": "Kak Cia asikk beutt baikk beutt kadiv terdebestt",  
                "pesan":"Sehat sukses selalu kak cia!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Nelly kocak bangett kalo ngomong pen ketawa dahh",  
                "pesan":"Semangatt alwayss kak!"# 1
            },
            {
                "nama": "Khoriul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan voli",
                "sosmed": "@mananam__",
                "kesan": "Abang Anam baikk sekali orangnya",  
                "pesan":"Semangat terus, Bang!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Way Hui",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Rajanya PDD takada lawann",  
                "pesan":"Semangattt alwayss Bang Labo!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Bang Rafi pdd gokilll",  
                "pesan":"Semangat selalu ya Bang"# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa baik betzzz",  
                "pesan":"Semangat 45 kaka"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122350020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaa",
                "kesan": "Kak Ciya baikk puolll debestt beutt kak ciya",  
                "pesan":"Cemungut celalu kak ciya"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal":"Kotabumi, Lampung Utara",
                "alamat": "Jl. Pangeran Senopati",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kak Allya vibesnya adem bangett",  
                "pesan":"Semangat n sukses selalu kak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna baikk bangett n rahmaa bangett",  
                "pesan":"Semangattt alwayss kak donna!"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@wriitenbyangel",
                "kesan": "Kak Feby baik ramah kocak",  
                "pesan":"Semangat terus kuliahnya ya kak!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Masak",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kak Hafsa baikk bangett apalagi pas ngasprakk",  
                "pesan":"Stay Positive ya kak!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas, Jati Agung",
                "hobbi": "Dengar musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla kalemm sekali pembawaanya",  
                "pesan":"Tetap semangat ya kak"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania baik bangett lembut ngomongnya",  
                "pesan":"Semoga bahagia selalu!"# 1
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan": "Bang Akmal visual design terdebest",  
                "pesan":"Semangat always bang!"# 1
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Membaca, Menulis, Memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kak Raihana baikk bangett adem banget vibesnya",  
                "pesan":"Semangat menjalani hari-harinya kak"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra ademm bangett vibesnya",  
                "pesan":"Cemangatt terus ya kak"# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Sabah balau residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kak eigi baik ramahh bangett",  
                "pesan":"cemangat celalu ya kak"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Romauli ketawa mulu dah wkwkw",  
                "pesan":"Semoga sukses terus ya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()



# Tambahkan menu lainnya sesuai kebutuhan

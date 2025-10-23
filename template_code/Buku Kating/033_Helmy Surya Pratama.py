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
                "kesan": "Kahim paling debest baik banget ramah",
                "pesan": "semangat terus kuliahnya Bang Rendra!!!"  # 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar - dasar sql",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Jo baikk betull dan ramah bangett",
                "pesan": "semangat terus kuliahnya Bang JO !!!"  # 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kos",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak Abeth seru banget, ceria orangnyaa,  
                "pesan":"semangat terus kuliahnya Kak Abeth!!!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya kalem banget",  
                "pesan":"semangat terus kuliahnya Kak Syadza !!!"# 1
            },
            {
                "nama": "Eksanty F Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku saku Pramukar",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty seru banget waktu bawain materi",  
                "pesan":"semangat terus kuliahnya Kak Eksanty !!!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang, Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kak Farahanum orangnya baik banget",  
                 "pesan":"semangat terus kuliahnya Kak Farahanum !!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan(

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
                "kesan": "Bang Jere seru banget waktu ngejelasin materi",  
                "pesan":"semangat terus kuliahnya Bang Jere !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto",
                "alamat": "Kemiling",
                "hobbi": "Lomba ga makan kerupuk",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak Dhea lucu banget orangnya",  
                "pesan":"semangat terus ya Kak Dhea !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Tidur",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha asik, seru, lucu",  
                "pesan":"semangat terus kuliahnya Kak Renisha !!!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi morse",
                "sosmed": "@ansftynn_",
                "kesan": "Kak Anisa baik banget",  
                "pesan":"semangat terus kuliahnya Kak Anisa !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "Bang Dharu pinter banget orangnyaa",  
                "pesan":"semangat terus kuliahnya Bang Dharu!!!"# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bajak sawah",
                "sosmed": "@fby.wlndr",
                "kesan": "Kak Feby baik banget dan ramah bangett",  
                "pesan":"semangat terus kuliahnya Kak Feby !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Dengerin spotify",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro cool banget orangnyaa",  
                "pesan":"semangat terus ya Bang Givaro!!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerawat kucing",
                "sosmed": "@myrrinn",
                "kesan": "Bang MIrzan paling kece dahh di Baleg",  
                "pesan":"semangat terus ya Bang Mirzan!!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini seru banget orangnya",  
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
                "kesan": "Kak Jue Baik bangetzzz dan ramahh bangetss",  
                "pesan":"semangat terus Kak Jue !!!"# 1
            },
            {}
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Gh",
                "hobbi": "Main padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho baik banget dan seru banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "25",
                "asal":"Belitung",
                "alamat": "Tanjung Karang",
                "hobbi": "Koleksi bath google cloud",
                "sosmed": "@fer_yulius",
                "kesan": "Bang Feryadi seru banget",  
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
                "kesan": "Kak Monic baik bangett dan ramah bangett",  
                "pesan":"semangat terus ya kak Monicc!!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Kota Tarakah",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nashwaalhasni",
                "kesan": "Kak Wawa baik dan ramah",  
                "pesan":"semangat terus ya Kak Wawa !!!"# 1
            },
            
        ]
        )
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
                "kesan": "Bang Bintang seru banget orangnya dan gak jaim",
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
                "kesan": "Kak Nadya baik banget dan ramah banget",
                "pesan": "semangat terus ya Kak Nadya !!!"  # 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Main Ice Skating",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Azizah Kalem bangett dan tenang banget orangnya",  
                "pesan":"semangat terus Kak Azizah !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Ichi seru bangettz orangnyaa",  
                "pesan":"semangat terus Kak Ichii!!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan

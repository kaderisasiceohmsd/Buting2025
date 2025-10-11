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
            "https://drive.google.com/uc?export=view&id=1hZbI0a_yhAqV1RdwIL4CJIGTtSBIPemI",
            "https://drive.google.com/uc?export=view&id=1grNZb11aTtYpOSPonOiUmQlcNTB09b0H",
             "https://drive.google.com/uc?export=view&id=1GXCNA6quUoo_vjS_L811AGxkFGClMnO3",
             "https://drive.google.com/uc?export=view&id=1nArmCr2GocuPpRPn2_MAv5rE3VeFnW_L",
            "https://drive.google.com/uc?export=view&id=16flvDqA6svuZU2m9exztomyQ125idHuN",
             "https://drive.google.com/uc?export=view&id=1lNhLE1H1NkTbbFi6N7hpPb7Wren3ulSj",
        ]
        data_list = [
            {
                "nama": "Kakak Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Makan Pisang",
                "sosmed": "@_erendraa",
                "kesan": "Kakak ini tegas dan ketawanya menular hahaha, asik banget!",  
                "pesan": "semoga selalu sukses dimana pun berada kakak !!!"# 1
            },
            {
                "nama": "Kakak Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kakak ini lucu banget parah!",  
                "pesan": "semoga lancar kuliahnya kakak!!!"# 1
            },
              {
                "nama": "Kakak Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak ini senyumnya manis, jadi suka deh!",  
                "pesan": "semoga sehat selalu kakak!!!"# 1
            },
              {
                "nama": "Kakak Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini pendiam tapi lucu, manis deh!",  
                "pesan": "Semoga sukses selalu kakak !!!"# 1
            },
            {
                "nama": "Kakak Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini tegas sekaligus lucu dalam satu waktu, sukaaa!",  
                "pesan":"Jangan lupa jaga kesehatan kakak !!!"# 1
            },
             {
                "nama": "Kakak Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini seru banget diajak ngobrol, suka deh",  
                "pesan": "Jaga kesehatan terus kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GssFMzoRbCwkWiQDvoT5E_IkjtR8uAJu",
            "https://drive.google.com/uc?export=view&id=1KV23gXma6AWwl7U8ZRjLdgTe_FWHoahO",
             "https://drive.google.com/uc?export=view&id=14w3iUtKO_YUypsET8QYnIvd13kHid53C",
             "https://drive.google.com/uc?export=view&id=151L2RoWLX0NHM4ga_oJayPcR3pmV_JZV",
            "https://drive.google.com/uc?export=view&id=15yOWLJSgO1GleNpPjQWJ38grdKQ7YOqa",
             "https://drive.google.com/uc?export=view&id=1VfZ-PSvsNHI03AsBgZvauo9_q8aH35P-",
            "https://drive.google.com/uc?export=view&id=1DVyXlMwFf4TNja5MZUCRVve7Z9uFzJlk",
            "https://drive.google.com/uc?export=view&id=1kXxgMLoBHNE2Qe9fJ58F8VHrNk7eY86E",
            "https://drive.google.com/uc?export=view&id=1S4cdEXqkmL73XmQZZANTi_hF0vTXVzmE",
            "https://drive.google.com/uc?export=view&id=1TpuYU3vt-9JFsE1076z5qjoK258VNocr",
            "https://drive.google.com/uc?export=view&id=1hDUdmPT1jS1sIAz2RtQaBGoHSs_nSh31",
            "https://drive.google.com/uc?export=view&id=1SdocdhBPqOJB-44b3P1w6S6K-t1Xb3Am",
            "https://drive.google.com/uc?export=view&id=1q8ezJRhP1GKjOdC02cWcRIlVs6Gv1QhA",
            "https://drive.google.com/uc?export=view&id=1m60QTcZLXNseW7awAieINFi1EgkD5PXc",
        ]
        data_list = [
            {
                "nama": "Kakak Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "Kakaknya manis, lucu ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya"# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "Kakak nya baik, seru ",  
                "pesan": "Sehat selalu kak, dilancakan semuanya "# 1
            },
              {
                "nama": "Kakak Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya keren dan asik ",  
                "pesan": "Semoga dilancarkan urusannya kak "# 1
            },
              {
                "nama": "Kakak Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kakaknya keren ",  
                "pesan": "Semoga urusannya diperlancar "# 1
            },
            {
                "nama": "Kakak Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Kakaknya keren banget ",  
                "pesan":"Semoga diperlancar semuanya  "# 1
            },
             {
                "nama": "Kakak Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya cantik dan lucu ",  
                "pesan": "Semangat kak, diperlancar semuanya "# 1
            },
              {
                "nama": "Kakak Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Kakaknya keren banget ",  
                "pesan": "Semoga dilancarkan semuanya kak "# 1
            },
              {
                "nama": "Kakak Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": " ",  
                "pesan": " "# 1
            },
              {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": " ",  
                "pesan": " "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bJiSw9OQ_B3IGAMnMYqkdUaFyXtl12ai",
            "https://drive.google.com/uc?export=view&id=1kQ_UKG693TchnUWBrQi43H3spdJ3dbo_",
             "https://drive.google.com/uc?export=view&id=1LzasgfP-hAMih41Y1hvI1ENm_yK8Ave2",
             "https://drive.google.com/uc?export=view&id=1nSNh-fkhR2vR8B40mIoRq4BKEFUVePWE",
        ]
        data_list = [
            {
                "nama": "Kakak Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Kakak ini suka suasana santai tapi sopan, sangat unik!",  
                "pesan": "semoga semuanya dipermudah kakak !!!"# 1
            },
            {
                "nama": "Kakak Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini cantik banget, pangling lihatnya!",  
                "pesan": "semoga akademik nya diperlancar kakak!!!"# 1
            },
              {
                "nama": "Kakak Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini independent women looks banget, jadi inspirasi aku!",  
                "pesan": "semoga sehat selalu ya kakak!!!"# 1
            },
              {
                "nama": "Kakak Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini pendiam tapi lucu, manis deh!",  
                "pesan": "Semoga kuliahnya lancar selalu ya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aBNjXyz3CHdNFzqpUP-kY_Tn3EuxwD8H", #1
            "https://drive.google.com/uc?export=view&id=1K7h4xOYdlSgJmCZOZKtH7SdV_WNRZMTh", #2
            "https://drive.google.com/uc?export=view&id=1AY7CGzLoD4RRswnoJqavoWuX7AFD-06H", #3
            "https://drive.google.com/uc?export=view&id=1TLLdzX6USsK9BKbHVlqV989gVTI6t8a0", #4
            "https://drive.google.com/uc?export=view&id=1_oOJkJo9O7q8Jq3AYQp1Sxb_uXA4OJ3", #5
            "https://drive.google.com/uc?export=view&id=1zaAAqd1wDtCVR6ya-5dh4TgVCZ53C040", #6
            "https://drive.google.com/uc?export=view&id=1TYdrADhjDlWFlpHNoAOoycRol_UMj-cB", #7
            "https://drive.google.com/uc?export=view&id=1Gwq-K7kFg6hARzerODJajwDFCK3a28Nv", #8
            "https://drive.google.com/uc?export=view&id=1qayfrg8hNzPqJFZQSwPTh8LlYvjC_dop", #9
            "https://drive.google.com/uc?export=view&id=1bTOyO0W4pCQ5HI3jfhBR_IoBRsY_VtIv", #10
            "https://drive.google.com/uc?export=view&id=1JQ-CspHT25aYYS6SG6lnPUxlxtxtm5IG", #11
            "https://drive.google.com/uc?export=view&id=1HvX9GpHwkVpMk_r0pRkYebCJ-B0TpeuI", #12
            "https://drive.google.com/uc?export=view&id=1XInjivN1YyQ7VtktdtFYvvaoT4r_Qm86", #13
            "https://drive.google.com/uc?export=view&id=1iuHKmXlbJBgupqS2UdAbdErJIJE5NRxe", #14
            "https://drive.google.com/uc?export=view&id=1TcIy6E0u-z6JcbpIJjPOTQM6y__aPT6P", #15
            "https://drive.google.com/uc?export=view&id=1lN2NuvwbNXYbKfMo0VvWfROrCpRFcKHm", #16
            "https://drive.google.com/uc?export=view&id=1fRAFfG3SPlh-APBP9D-cvlFHmN4D071W", #17
            "https://drive.google.com/uc?export=view&id=1WGo71HOoWpkCmkfx_3GwQ9KLaEp5uuSx", #18
            "https://drive.google.com/uc?export=view&id=1uf3jCnzI_YsGMBsSC9pSAopeAbnS_udW", #19
            "https://drive.google.com/uc?export=view&id=1SMFhxBJs_a6WN5k2CoDhA0PLuqLnn50x", #20
            "https://drive.google.com/uc?export=view&id=1beNTjXmHd1Wlsr1hSvNPlykiQ-lihKz5", #21
            "https://drive.google.com/uc?export=view&id=1WWeUVrsQkAkfGX6WH_F7xap1QEK5NePk", #22
        ] 
        data_list = [
            {
                "nama": "Kakak Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kak Randa sangat meginspirasi!",  
                "pesan":"Semoga kuliahnya lancar selalu, kakak!"# 1
            },
            {
                "nama": "Kakak Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak Rut cantik sekali!",  
                "pesan":"Sehat selalu kakak!"# 2
            },
            {
                "nama": "Kakak Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Pencapaian kak Regi bikin tercengang!",  
                "pesan":"Semoga kuliahnya lancar selalu kakak!"# 3
            },
            {
                "nama": "Kakak Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak Aisyah manis banget",  
                "pesan":"Sehat selalu ya kakak!"# 4
            },
            {
                "nama": "Kakak Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak ini sangat menginspirasi!",  
                "pesan":"Semoga terus menjadi inspirasi ya kakak!"# 5
            },
            {
                "nama": "Kakak Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak Aqil tinggi banget",  
                "pesan":"Jaga kesehatan terus ya kak"# 6
            },
            {
                "nama": "Kakak Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "Kakak ini mmanis banget deh",  
                "pesan":"Semoga terus manis kedepannya, kak!"# 7
            },
            {
                "nama": "Kakak Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kak Nadia cantik banget!",  
                "pesan":"Semoga semua urusan akademiknya diperlancar ya kakak!"# 8
            },
            {
                "nama": "Kakak Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini bikin kaget soal keturunannya! Cantik jugaa!",  
                "pesan":" Semoga terus cantik kedepannya kakak! Jaga kesehatan yaa!" # 9
            },
            {
                "nama": "Kakak Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Kakak Akeyla pendiam tapi ada lucunya!",  
                "pesan":"Semoga kuliahnya terus diperlancar ya kakak!"# 10
            },
            {
                "nama": "Kakak Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak Anggi cantik deh, sukaa!",  
                "pesan":"Jaga kesehatan terus ya kakak!"# 11
            },
            {
                "nama": "Kakak Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak Efi pinter banget!",  
                "pesan":"Makasih udah jadi tutor kami kakak! Semoga kuliahnya diperlancar!"# 12
            },
            {
                "nama": "Kakak Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kakak Fabiolla super baik baikk! Aku sukaa pakai bangett!",  
                "pesan":"Semoga diperkuat hingga tahap akhir studi ya kakak!"# 13
            },
            {
                "nama": "Kakak Fairus Ary Syifa",
                "nim": "123450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakak Fairuz maniss! Kaya gula merah, kebangetan manisnya!",  
                "pesan":"Semoga apapun itu, diberi jalan dan kemudahan ya kakak!"# 14
            },
            {
                "nama": "Kakak Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@i",
                "kesan": "Kakak Tanty hiperaktif banget, kayanya kita satu frekuensi deh kak,hehehe.",  
                "pesan":"Selalu jadi pribadi yang ceria ya kakak!"# 15
            },
            {
                "nama": "Kakak Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Kakak Eggi dengan kacamatanya adalah ikon mikfes ^^ ",  
                "pesan":"Semoga kuliahnya diperlancar ya kakak"# 16
            },
            { 
                "nama": "Kakak Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Aduh, kakak Afifah manis, tegas dan lucu! Paket Komplit di mikfes",  
                "pesan":"Semoga semua urusan diberi kemudahan ya kakak"# 17
            },
            {
                "nama": "Kakak Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Fabio! Lucu dan pinter dalam satu waktu! Suka deh!",  
                "pesan":"Terus jadi pribadi yang ceria ya kakak! Sehat selaluuu!"# 18
            },
          
            {
                "nama": "Kakak Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Manis sekali kakak, jadi suka dehh!",  
                "pesan":"Terus jadi orang manis ya kakak, ITERA butuh orang manis seperti kakak!"# 19
            },
            {
                "nama": "Kakak Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakak tutorkuu! Terima kasih udah jadi pribadi ya baik dan manis ya kakak!",  
                "pesan":"Terima kasih sudah lahir ke dunia ini, heheh!"# 20
            },
            {
                "nama": "Kakak Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakak Razin dan kacamatanya juga ikon Mikfes banget!",  
                "pesan":"Sehat dan kuat selalu di perkuliahan kakak!"# 21
            },
            {
                "nama": "Kakak Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@",
                "kesan": "Pasti kakak Giofani cerdas deh! Soalnya dari mukanya kelihatan banget! Kerennn!",  
                "pesan":"Semoga terus jadi orang pintar dan gajinya dua digit ya kakak!"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

# Tambahkan menu lainnya sesuai kebutuhan


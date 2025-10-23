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
                "nim": "122450043",
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
                "kesan": "Kakaknya tampan dan cerdas! ",  
                "pesan": "Semoga semuanya diperlancar ya kakak "# 1
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini manis dan humoris! ",  
                "pesan": "Jaga kesehatan selalu ya kakak! "# 1
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini cerdas, komunikatif dan ekspresif!",  
                "pesan": "Jaga kesehatan selalu kakak, kakak keren! "# 1
            },
              {
                "nama": "Kakak Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "Kakak ini cerdas dan wangi ",  
                "pesan": "Tetap wangi selalu ya kakak, jaga kesehatan! "# 1
            },
              {
                "nama": "Kakak Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini cerdas dan lugas ",  
                "pesan": "Jaga kepercayaan diri selalu kakak, kakak keren! "# 1
            },
              {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "Kakak ini ramah dan manis! ",  
                "pesan": "Terus menjadi pribadi yang ramah ya kakak, semoga Tuhan memperlancar semuanya "# 1
            },
              {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "Kakak ini manis dan seru ",  
                "pesan": "Sehat selalu kakak, banyak hal fantastis menanti kakak! "# 1
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
            "https://drive.google.com/uc?export=view&id=1_oOJkJo9O7q8Jq3AYQp1Sxb_uXA4OJ3-", #5
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

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gKYiETc7lFAWoYyQH3sHl7V-dNsPlmx1", #1
            "https://drive.google.com/uc?export=view&id=1kmvWgp2LDrHPXf_bmQGwVRsLxY-FuwIf", #2
            "https://drive.google.com/uc?export=view&id=150HxCxvjyUvoXYCb8GNzUJSYOhtJPzmT", #3
            "https://drive.google.com/uc?export=view&id=1isPM3GykmD2VOpp3N02CmlXvDWWtfAWt", #4
            "https://drive.google.com/uc?export=view&id=1591r4ueF3QXv0YZRQojA-3tHCUzHWjnJ", #5
            "https://drive.google.com/uc?export=view&id=1ytVqQqH77N7bH7xOI_rSCb-ILyqi8Dkk", #6
            "https://drive.google.com/uc?export=view&id=1KsRee8FkUtwxMAioCBOBpBg0FGkcAY5Z", #7
            "https://drive.google.com/uc?export=view&id=1_3l5lUlGk0IO63zN6isXfwPwkW6PJQtJ", #8
            "https://drive.google.com/uc?export=view&id=1fjvfITXQmbu9CqNLm7ogahK16cyoS1QR", #9
            "https://drive.google.com/uc?export=view&id=1wxda3i93MLaxBKdMTEsAdRBEwQ08RzV0", #10
            "https://drive.google.com/uc?export=view&id=1aX7zUTPggAswm7lRa1jHoDeCI8wQYzuh", #11
        ]
        data_list = [
            {
                "nama": "Kakak Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": "Kakaknya berjiwa ambisius dan keren! ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya ya kakak"# 1
            },
            {
                "nama": "Kakak Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakaknya cantik dan seru!",  
                "pesan": "Sehat selalu ya kakak!"# 2
            },
              {
                "nama": "Kakak Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "Kakaknya wangi dan seru!",  
                "pesan": "Semoga dilancarkan pendidikannya kak "# 3
            },
              {
                "nama": "Kakak Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya manis ",  
                "pesan": "Semoga studinya diperlancar ya kakak "# 4
                   },
              {
                "nama": "Kakak Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "Kakaknya pendiam tapi manis",  
                "pesan": "Sehat selalu ya kakak"# 5
            },
            {
                "nama": "Kakak Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": ".",
                "asal": ".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": ".",
                "kesan": "Kakaknya cantik dan wangi, suka! ",  
                "pesan":"Semoga diperlancar studi dan semuanya, kakak  "# 6
            },
             {
                "nama": "Kakak Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakaknya pendiam tapi seru! ",  
                "pesan": "Semangat kak, diperlancar studinya! "# 7
            },
              {
                "nama": "Kakak Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya keren banget ",  
                "pesan": "Semoga dilancarkan studinya ya kak "# 8
            },
              {
                "nama": "Kakak Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "Kakak ini manis banget!",  
                "pesan": "Sehat selalu ya kakak"# 9
            },
              {
                "nama": "Kakak Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini aura bussines women banget!",  
                "pesan": " Semoga rezekinya lancar terus, kakak"# 10
            },
              {
                "nama": "Kakak Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "Kakak ini cantik deh!",  
                "pesan": "Semoga semua diperlancar, kakak!"# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DXrbBcaqzGzwOG4dSnQBXgYes3yxbhIk", #1
            "https://drive.google.com/uc?export=view&id=1SSKZZMDqE6EXhXk9zAlT3JXkm8IQD6B8", #2
            "https://drive.google.com/uc?export=view&id=1EgppA53zNrKQ8uqGwSyyEb4LqRICvIJc", #3
            "https://drive.google.com/uc?export=view&id=1-dUquSDJZ63kbY_v8rb5KeGYb-0BfXF2", #4
            "https://drive.google.com/uc?export=view&id=15ljwZOv9sCfbLCebAZ8tOGG8xZ-jcisq", #5
            "https://drive.google.com/uc?export=view&id=14rZBigRdYm2BsqCUZzhWv6dQzpEMPMvZ", #6
            "https://drive.google.com/uc?export=view&id=1uO8NOR8hZyF77j77LHnC4SOgwGkpGDBv", #7
            "https://drive.google.com/uc?export=view&id=15rfkUdlsxvWD9HXSb5JZi8LJ1MNSV71i", #8
            "https://drive.google.com/uc?export=view&id=1APzE8lbZ3MAcFWnKcB5FDz1KMD5vKAvJ", #9
            "https://drive.google.com/uc?export=view&id=11KVx1eDQ3FUyvIl4FnxNp3rdcogN9onw", #10
            "https://drive.google.com/uc?export=view&id=1dORxg9Wg20JyfTUidGtWb6qqVrPnzsHd", #11
            "https://drive.google.com/uc?export=view&id=1JT1ErKg1Hfm3mys2xdeSyvUIohXKxV4I", #12
            "https://drive.google.com/uc?export=view&id=1091_ibgw_4HBtSIeZ34AZPZcG09TqTmX", #13
            "https://drive.google.com/uc?export=view&id=1ZTeW3rUPGqA5GiM3oiyUh6NNhD5bDVuM", #14
            "https://drive.google.com/uc?export=view&id=1UFBpevfmuy0H481MiK1NRvuW-P-SZTNd", #15
            "https://drive.google.com/uc?export=view&id=1Rj1-JRnUceE58oM7xt2fXvCwjoHriL1L", #16
            "https://drive.google.com/uc?export=view&id=1asLtG_FA5VNXEmAQeo5_hs-sqYbPd_X-", #17
            "https://drive.google.com/uc?export=view&id=1I5Y9ujxnvHkRp5N3jJmyhLZufco2Kpnc", #18
            "https://drive.google.com/uc?export=view&id=1lwbExCnGf-ymvsg-e5Aqf5SQ3mRuy9Uz", #19
            "https://drive.google.com/uc?export=view&id=11SK75_oOunPlh1TkyaFO8nE2rJLQTiWH", #20
            "https://drive.google.com/uc?export=view&id=1eUYPFUxH033fc9i_5e5lRe59GJ5S6X0V", #21
            "https://drive.google.com/uc?export=view&id=1CVGvj2sTw_9N-m2DRcsFID2pV20FyqGv", #22
            "https://drive.google.com/uc?export=view&id=1YDSJ600ShQ6Xi5hFTIE6r5UrgM69EV26", #23
            "https://drive.google.com/uc?export=view&id=1ZewuPTjTwaFSQcyUCrWdv-_7EPuDqT7G", #24
        ]
        data_list = [
            {
                "nama": "Kakak Arafi Putra Maulan",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Kakak ini wangi dan keren! ",  
                "pesan":"Semoga sehat selalu kak, dan segala studi nya dilancarkan! "# 1
            },
            {
                "nama": "Kakak Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana cantik dan baik! ",  
                "pesan":"Sehat selalu ya kakak, semoga diberikan kekuatan dalam segala hal! "# 2
            },
            {
                "nama": "Kakak Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini cantik dan wangi! ",  
                "pesan":"Jadi pribadi yang wangi terus ya kakak, semerbak banget wanginya seperti bunga "# 3
            },
            {
                "nama": "Kakak Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak sonyaa, paling baik dan paling pengertian, aku sukaaa! ",  
                "pesan":"Kakak udah hebat bangett dan mengayomi saya banget!Terima kasih ya kakak untuk semuanyaa! I love kak sonya! kak sonya di hati selamanya heheheh:) "# 4
            },
            {
                "nama": "Kakak Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kak Luthfia baik dan cantik, suka deh! ",  
                "pesan":"Sehat dan selalu dipermudah studinya kakak! "# 5
            },
            {
                "nama": "Kakak Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakak Cindy cantik dan wangi sekali ",  
                "pesan":"Sehat dan selalu mengandalkan Tuhan ya kakak!  "# 6
            },
            {
                "nama": "Kakak Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak ini lucu tapi agak seram tapi lucu ",  
                "pesan":"Semoga sehat selalu ya kakak, dan segala hal baik menghampiri kakak dengan lancar! "# 7
            },
            {
                "nama": "Kakak Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakak Dea suaranya khas banget, khas MC profesional hehehe ",  
                "pesan":"Kakak berpotensi jadi pembawa berita TV Nasional kak:) Semoga studinya selalu diperlancar ya kakak! "# 8
            },
            {
                "nama": "Kakak Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kakak ini ganteng dan wangi! ",  
                "pesan":"Sehat selalu ya kakak, jaga pola tidur karena sehat itu mahal kakak! "# 9
            },
            {
                "nama": "Kakak Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "Kakak Cantik! Manis banget dan ramah, aku suka hehehe ",  
                "pesan":"Selalu jadi pribadi yang ramah dan manis ya kakak! Itu ciri khas kakak banget soalnya:) "# 10
            },
            {
                "nama": "Kakak khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakak Ilmi, cantik wangi dan humble hehehe ",  
                "pesan":"Terima kasih sudah mau saya ajakin retake foto kakak! Semoga semua urusan kakak diperlancar dan diberikan keringanan "# 11
            },
            {
                "nama": "Kakak Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakak Izzah, baik dan pendiam, tapi tidak pelit berbagi ilmu! ",  
                "pesan":"Selalu semangat dalam berbagi ilmu ya kakak, semoga semua hal baik menghampiri kakak! "# 12
            },
            {
                "nama": "Kakak Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak Qois! Sangat baik dan sangat mengayomi! ",  
                "pesan":"Terima kasih sudah memberikan saya kesempatan jadi bagian dari SDM ya kakak! Semoga semua hal baik menghampiri kakak "# 13
            },
            {
                "nama": "Kakak Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak Melinza baik dan manis sekali! ",  
                "pesan":"Semoga sehat selalu ya kakak, diberkati dimanapun berada! "# 14
            },
            {
                "nama": "Kakak Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakak Nayla dengan kacamatanya adalah satu paket yang khas! Manis deh ",  
                "pesan":"Sehat selalu ya kakak, jangan lupa untuk makan:) "# 15
            },
            {
                "nama": "Kakak Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakak ini asik, humble dan ramah ",  
                "pesan":"Terima kasih sudah mengayomi saya selama di SDM kakak, semoga sehat selalu dan kuliahnya diperlancar "# 16
            },
            {
                "nama": "Kakak Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakak Tarisya! Baik banget, lembut banget suaranya! ",  
                "pesan":"Semoga semua hal baik menghampiri kakak ya kak! "# 17
            },
            {
                "nama": "Kakak Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakak Jasmine buat saya insecure hehehe, pintar sekali kakak!  ",  
                "pesan":"Terus menorehkan prestasi di kancah nasional dan internasional kakak, saya mendukung kakak selalu! "# 18
            },
            {
                "nama": "Kakak Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakak ini manis dengan baik! ",  
                "pesan":"Semoga semua studi nya diperlancar ya kakak, jangan lupa untuk tetap jaga kesehatan kakak "# 19
            },
            {
                "nama": "Kakak Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kakak ini baik dan humble banget! ",  
                "pesan":"Terima kasih ya kakak, semoga kakak mendapatkan semua hal baik di bumi! "# 20
            },
            {
                "nama": "Kakak Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak Arini manis banget! ",  
                "pesan":"Tetap jadi pribadi yang manis ya kakak "# 21
            },
            {
                "nama": "Kakak Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Kakak ini sangat mengayomi, baik, dan welcome sekali! ",  
                "pesan":"Terima kasih ya kakak, semoga semua hal baik menghampiri hidup kakak "# 22
            },
            {
                "nama": "Kakak Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak ini manis dan tegas, saya suka! ",  
                "pesan":"Semoga sehat selalu ya kakak, jangan sampai jatuh sakit. Amin "# 23
            },
            {
                "nama": "Kakak Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak Nabyla, manis dan cerdas! ",  
                "pesan":"Terima kasih sudah jadi kakak tutor ALE RC kakak! Saya paham OBE karena kakak, semoga rezeki kakak dilimpahkan selalu dan sehat-sehat terus! "# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EfYmWGN1eKluaJL1Hrp_7cjSaGn3bD4d", #1
            "https://drive.google.com/uc?export=view&id=1UA6fgSfr9yGpGs_MAVQWKhjYwcJk7NbL", #2
            "https://drive.google.com/uc?export=view&id=1161Eqoi_aK1Gol_2iebMg8dR97XiJfff", #3
            "https://drive.google.com/uc?export=view&id=1dTBuOxiLos_AQ7msVzdz_eGyEIHk5kpX", #4
            "https://drive.google.com/uc?export=view&id=1ih4C9Ae2igdTvBhk9x5-dRbfkubPUgKu", #5
            "https://drive.google.com/uc?export=view&id=1If-VO0k0k9x6lfDfdsXVZJVmlEnZnKVk", #6
            "https://drive.google.com/uc?export=view&id=1ZNNPBxl6coCiOzJXNJC68pLb6Mert_8M", #7
            "https://drive.google.com/uc?export=view&id=1pX6K3mWjyG8GpdsBb7NreVCl7gEnKOTd", #8
            "https://drive.google.com/uc?export=view&id=1mkyUSYnxUjQxclCO61o-iJoJGzhsXrI5", #9
            "https://drive.google.com/uc?export=view&id=1O3ZRF2h24yMy_zKJdqHhl9XCA__7Bwat", #10
            "https://drive.google.com/uc?export=view&id=1sXiBqt6zYxz5gWY_Kw8KYaggVLXuM5z9", #11
            "https://drive.google.com/uc?export=view&id=1cqJMMvVp1BW2ckHJ0KbK_72ArMqg0_U4", #12
            "https://drive.google.com/uc?export=view&id=19Zyzo1rYB3f7BqkHHTofO6B79om9VyOh", #13
            "https://drive.google.com/uc?export=view&id=1hYznI1fD680TCqsa3eCE29lRTuiZR5ys", #14
            "https://drive.google.com/uc?export=view&id=1co5-5luViaUiz1OKxIlnWDWWrEjRrYDL", #15
        ]
        data_list = [
            {
                "nama": "Kakak Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": "Kakak Rani manis sekaligus aura independent women nya menginspirasi saya! ",  
                "pesan":"Sehat selalu kakak, kakak cocok sekali menjadi pemimpin! "# 1
            },
            {
                "nama": "Kakak Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak Renta ber-karisma sekali! Saya suka! ",  
                "pesan":"Terus jadi inspirasi banyak orang ya kakak! "# 2
            },
            {
                "nama": "Kakak Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakak ini manis dan baik! ",  
                "pesan":"Semoga semua hal baik menghampiri hidup kakak yaa! "# 3
            },
            {
                "nama": "Kakak Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Kakak ini manis sekali! Seperti gula ",  
                "pesan":"Tetap jadi inspirasi semua orang ya kakak! "# 4
            },
            {
                "nama": "Kakak Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakak ini tegas dan baik dalam satu waktu ",  
                "pesan":"Sehat dan sukses selalu ya kakak, semoga Tuhan selalu memberkati langkah kakak "# 5
            },
            {
                "nama": "Kakak Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini manis sekali! ",  
                "pesan":"Terima kasih ya kakak, semoga kakak dipenuhi hal-hal yang bahagia "# 6
            },
            {
                "nama": "Kakak May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakak May manis dan tegas dalam satu waktu ",  
                "pesan":"Terima kasih ya kakak, semoga kakak selalu mencapai kesuksesan. Amin "# 7
            },
            {
                "nama": "Kakak Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Kakak Naufal baik sekali, juga welcome sekali! ",  
                "pesan":"Terus jadi pribadi yang menebar kebaikan ya kakak, suskes selaluu! "# 8
            },
            {
                "nama": "Kakak Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "Kakak ini jiwa sosialisasinya kukat banget! ",  
                "pesan":"Semoga apapun itu rencana kedepannya, diberi kemudahan ya kakak "# 9
            },
            {
                "nama": "Kakak Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Kakak ini suaranya bagus sekali, saya kalah loh! Sampai saya terpikat dengar suaranya ",  
                "pesan":"Semoga kakak selalu diberkati Tuhan dan diberikan kemudahan dalam semua pekerjaan! "# 10
            },
            {
                "nama": "Kakak Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak Hanna! Manis, cantik, baik, suara bagus! paket komplit! ",  
                "pesan":"Saya suka sekali dengan kakak, kakak asik dan seru. Semoga semua hal menghapiri kakak dengan bahagia "# 11
            },
            {
                "nama": "Kakak Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Kakak Keren, paling cantik se-ITERA! ",  
                "pesan":"Terima kasih sudah mengayomi saya dengan baik ya kakak, semoga semua hal baik menghampiri kakak! "# 12
            },
            {
                "nama": "Kakak Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Kakak Hanif jiwa introvertnya menguar banget, sama seperti saya ",  
                "pesan":"Sehat selalu ya kakak, semoga semua dipermudah!"# 13
            },
            {
                "nama": "Kakak Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Kakak Sarah jago main musik, tambah keren sekligus tambah cantik ",  
                "pesan":"Semoga sehat selalu ya kakak. Tuhan Yesus memberkati "# 14
            },
            {
                "nama": "Kakak Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak Zahra, manis sekali ",  
                "pesan":"Semoga selalu diberikan kebahagiaan ya kakak!"# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1x19gE0vFbgapt3lLBf3MI0_JoOXbA8QL",
            "https://drive.google.com/uc?export=view&id=1Pzw0fZiQV_ZnpLjpCj0jwaY_O2Hwyip_",
            "https://drive.google.com/uc?export=view&id=1-NNhj_MGe7rfLevTpPVC3zrLTBFuj7L9",
            "https://drive.google.com/uc?export=view&id=1IWZuvzpgw2-QbjDHO_OQ_C_E-Zg6EQxs",
            "https://drive.google.com/uc?export=view&id=1HfcPLi9h4bwXiqRBhocYy8otsypuAgQz",
            "https://drive.google.com/uc?export=view&id=1VM5Lh8s0guSZDG1Ncf_VXSr50awEm5Un",
            "https://drive.google.com/uc?export=view&id=1gtIMN48zZAj-_fKqUI8_fbIpCBQl_Q-Y",
            "https://drive.google.com/uc?export=view&id=1uRpwaqiidu5ZwZgK4UmP83GPWEYRnTxy",
            "https://drive.google.com/uc?export=view&id=1phXoSZmijn_g6L-uMKjhFuTrBixXNQ9m",
            "https://drive.google.com/uc?export=view&id=1jvONJKtR9_YJv_bluZm90SuCRULYbHlE",
            "https://drive.google.com/uc?export=view&id=1JD8FV662f449FHqToyWwRX_tUPwta0cI",
            "https://drive.google.com/uc?export=view&id=1GQgbAhG6o34FXwe3l1PLvRgiTgrIjy4S",
            "https://drive.google.com/uc?export=view&id=1mu6g37yhKhhehIqeP6d7MzM4yqYtb-Ms",
            "https://drive.google.com/uc?export=view&id=1pbRNcmjXkl2Eg4QTz04gTyO0nkviTHUC",
            "https://drive.google.com/uc?export=view&id=1ei2se_1_uqgpkmD_LQqBrVdTy-Ml8CsW",
            "https://drive.google.com/uc?export=view&id=1KDRWePTTzJ7tpl6Kj5sxS4yFn98hO2Yo",
            "https://drive.google.com/uc?export=view&id=1xvFF5JY8Gjuh8K6gxab5c0dxPM773JwS",
            "https://drive.google.com/uc?export=view&id=1LSaE8hIscrjwVToPLISHLs84SgTmfqsu",
        ]
        data_list = [
            {
                "nama": "Kakak Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakak Patricia sangat wangi dan cantik, suaranya juga lembut banget!",  
                "pesan": "Semoga sehat selalu ya kakak!"# 1
            },
            {
                "nama": "Kakak Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kakak ini manis sekali, pangling lihatny hehe",  
                "pesan": "Selalu menjadi pribadi yang manis ya kakak, semoga sehat selalu"# 1
            },
              {
                "nama": "Kakak Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Kakak ini welome banget, baik sekali!",  
                "pesan": "Terima kasih banyak ya kakak, semoga sehat selalu"# 1
            },
              {
                "nama": "Kakak Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Kakak ini wangi dan tinggi banget",  
                "pesan": "Semoga semua urusan dipermudah ya kakak!"# 1
            },
              {
                "nama": "Kakak Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Kakak Rafi baik dan welcome sekali!",  
                "pesan": "Semoga semuanya dipermudah ya kakak!"# 1
            },
              {
                "nama": "Kakak Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "Kakak Refa!! Manis, baik, asik dan seru!",  
                "pesan": "Semoga sehat selalu dan jadi inspirasi banyak orang terus ya kakak!"# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakak manis sekali dan baik sekali!",  
                "pesan": "Terus jadi panutan banyak orang ya kakak!"# 1
            },
              {
                "nama": "Kakak Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kakak ini baik sekali dan manis sekali",  
                "pesan": "Semoga semuanya dipermudah dan studinya diperlancar ya kakak"# 1
            },
              {
                "nama": "Kakak Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak Donna baik sekali, sangat welcome terhadap kami",  
                "pesan": "Terima kasih ya kakak, semoga hal baik menghampiri kakak"# 1
            },
              {
                "nama": "Kakak Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemmiling",
                "hobbi": "Scoll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakak Feby baik dan cantik sekali",  
                "pesan": "Sehat dan sukses selalu ya kakak, semoga semua hal baik terjadi kepada kakak!"# 1
            },
              {
                "nama": "Kakak Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakak Hafsa manis dan baik!",  
                "pesan": "Terima kasih banyak ya kakak, semoga semuanya dipermudah bagi kakak"# 1
            },
              {
                "nama": "Kakak Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "Kakak Nayla manis dan baik sekali",  
                "pesan": "Tetap jadi inspirasi saya dan banyak orang ya kakak"# 1
            },
              {
                "nama": "Kakak Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak Sania manis dan baik banget!",  
                "pesan": "Tetap jadi pribadi yang ceria ya kakak"# 1
            },
              {
                "nama": "Kakak Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Kakak Akmal ceria dan humble sekali",  
                "pesan": "Kakak mirip dengan seseorang yang aku kenal. Semoga sehat dan sukses selalu ya kakak"# 1
            },
              {
                "nama": "Kakak Raihan Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kakak baik dan manis",  
                "pesan": "Sehat dan sukses selalu ya kakak"# 1
            },
              {
                "nama": "Kakak Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakak Citra baik dan welcome banget",  
                "pesan": "Sehat dan sukses selalu ya kakak"# 1
            },
              {
                "nama": "Kakak Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "Kakak manis dan ceria banget! Sangat "cewe bumi" looks banget hehehe",  
                "pesan": "Semoga sehat selalu ya kakak, apapun itu diberikan kemudahan oleh Tuhan"# 1
            },
              {
                "nama": "Kakak Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "Kakak Roma manis sekali!",  
                "pesan": "Sehat dan ceria selalu ya kakak, semoga semua hal baik menghampiri kakak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()



# Tambahkan menu lainnya sesuai kebutuhan


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
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Makan Pisang",
                "sosmed": "@_erendraa",
                "kesan": " Kakak tegas sekali dan ketawanya menular hahaha, asik banget!",  
                "pesan": "Semoga selalu sukses dimana pun berada dan karirnya melonjak tinggi !!!"# 1
            },
            {
                "nama": " Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": " Kakak lucu banget parah berbakat menjadi komedian miliyuner!",  
                "pesan": "Semoga lancar kuliahnya dan sehat selalu diberikan Tuhan!!!"# 1
            },
              {
                "nama": " Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": " Kakak punya senyum manis, jadi suka deh!",  
                "pesan": "Semoga sehat selalu dan bantai semua semester dengan mantap,kak!!!"# 1
            },
              {
                "nama": " Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": " Kakak pendiam tapi lucu, manis deh!",  
                "pesan": "Semoga sukses selalu dan berkarir dengan tinggi di angkasa,kak  !!!"# 1
            },
            {
                "nama": " Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini tegas sekaligus lucu dalam satu waktu, sukaaa! Hobinya juga antimainstream!",  
                "pesan":"Jangan lupa jaga kesehatan dan berbahagia selalu, kak !!!"# 1
            },
             {
                "nama": " Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": " Kakak ini seru banget diajak ngobrol, suka deh",  
                "pesan": "Jaga kesehatan terus kak, jangan cute kahim terus kak, kasihan abangnya !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
elif menu == "Baleg":
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
                "nama": " Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "Kakaknya manis, lucu dan wangi bangett ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya, kakak!"# 1
            },
            {
                "nama": " Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": " Kakaknya baik, seru dan ada lesung pipinya gitu, manis kayak Afghan",  
                "pesan": "Sehat selalu kak, dilancarkan semuanya "# 1
            },
              {
                "nama": " Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya badass look banget, suka!",  
                "pesan": "Semoga dilancarkan urusannya kak dan teruslah menjadi keren! Kakak cocok jadi keren! "# 1
            },
              {
                "nama": " Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "Kakaknya keren dan manis!",  
                "pesan": "Semoga urusannya diperlancar dan ada gebrakan setiap harinya! "# 1
            },
            {
                "nama": " Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Kakaknya keren banget bisa ikut KKN Kebangsaan dan peraih OZT! Jadi inspirasi aku,kak!",  
                "pesan":"Semoga diperlancar semuanya dan semakin gemilang prestasinya "# 1
            },
             {
                "nama": " Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya cantik seperti cewe jepang dan lucu ",  
                "pesan": "Semangat kak, diperlancar semuanya! "# 1
            },
              {
                "nama": " Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "Kakaknya keren banget, wajahnya kayak pemain sinetron! ",  
                "pesan": "Semoga dilancarkan semuanya kak! "# 1
            },
              {
                "nama": " Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya tampan dan cerdas juga wangi ",  
                "pesan": "Semoga semuanya diperlancar ya,kakak "# 1
            },
              {
                "nama": " Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini manis dan humoris! Cantik banget! ",  
                "pesan": "Jaga kesehatan selalu ya kakak, sehat dahulu baru tuntaskan semua tugas! "# 1
            },
              {
                "nama": " Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini cerdas, komunikatif dan ekspresif! ",  
                "pesan": "Jaga kesehatan selalu , kakak keren, bisa menjadi Duta adalah kunci yang harus dijaga sampai kapanpun! "# 1
            },
              {
                "nama": " Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "Kakak ini cerdas dan wangi ",  
                "pesan": "Tetap wangi selalu ya , jaga kesehatan! "# 1
            },
              {
                "nama": " Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini cerdas dan lugas ",  
                "pesan": "Jaga kepercayaan diri selalu ,  keren! "# 1
            },
              {
                "nama": " Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "Kakak ini ramah dan manis! Suaranya khas banget ",  
                "pesan": "Terus menjadi pribadi yang ramah ya , semoga Tuhan memperlancar semuanya "# 1
            },
              {
                "nama": " Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "Kakak ini manis dan seru ",  
                "pesan": "Sehat selalu , banyak hal fantastis menanti ! "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bJiSw9OQ_B3IGAMnMYqkdUaFyXtl12ai",
            "https://drive.google.com/uc?export=view&id=1kQ_UKG693TchnUWBrQi43H3spdJ3dbo_",
             "https://drive.google.com/uc?export=view&id=1LzasgfP-hAMih41Y1hvI1ENm_yK8Ave2",
             "https://drive.google.com/uc?export=view&id=1nSNh-fkhR2vR8B40mIoRq4BKEFUVePWE",
        ]
        data_list = [
            {
                "nama": " Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": " Kakak ini suka suasana santai tapi sopan, sangat unik!",  
                "pesan": "semoga semuanya dipermudah, kakak!"# 1
            },
            {
                "nama": " Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini cantik banget, pangling lihatnya!",  
                "pesan": "semoga akademik nya diperlancar !!!"# 1
            },
              {
                "nama": " Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini independent women looks banget, jadi inspirasi aku!",  
                "pesan": "semoga sehat selalu ya, kakak !!!"# 1
            },
              {
                "nama": " Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini pendiam tapi lucu, manis deh!",  
                "pesan": "Semoga kuliahnya lancar selalu ya,kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen MIKFES":
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
                "nama": " Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kak Randa sangat meginspirasi!",  
                "pesan":"Semoga kuliahnya lancar selalu, Kakak !"# 1
            },
            {
                "nama": " Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak Rut cantik sekali!",  
                "pesan":"Sehat selalu, kakak!"# 2
            },
            {
                "nama": " Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Pencapaian kak Regi bikin tercengang!",  
                "pesan":"Semoga kuliahnya lancar selalu, kakak !"# 3
            },
            {
                "nama": " Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl.Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak Aisyah manis banget",  
                "pesan":"Sehat selalu ya,kakak !"# 4
            },
            {
                "nama": " Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": " Kakak sangat menginspirasi dan aktif di perkuliahan!",  
                "pesan":"Semoga terus menjadi inspirasi ya, kakak !"# 5
            },
            {
                "nama": " Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak Aqil tinggi banget",  
                "pesan":"Jaga kesehatan terus ya kak dan terima kasih telah membimbing saya!"# 6
            },
            {
                "nama": " Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "Kakak manis banget deh, walau pendiam sedikit",  
                "pesan":"Semoga terus manis kedepannya, kak!"# 7
            },
            {
                "nama": " Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kak Nadia cantik banget!",  
                "pesan":"Semoga semua urusan akademiknya diperlancar ya, kak !"# 8
            },
            {
                "nama": " Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": " Kakak bikin kaget saya soal keturunannya! Cantik jugaa!",  
                "pesan":" Semoga terus cantik kedepannya ! Jaga kesehatan yaa, kakak!" # 9
            },
            {
                "nama": " Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Kak Akeyla pendiam tapi ada lucunya!",  
                "pesan":"Semoga kuliahnya terus diperlancar ya,kak !"# 10
            },
            {
                "nama": " Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak Anggi cantik deh, sukaa!",  
                "pesan":"Jaga kesehatan terus dan pola makan ya kakak!"# 11
            },
            {
                "nama": " Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi pinter banget!",  
                "pesan":"Makasih udah jadi tutor kami, kak ! Semoga kuliahnya diperlancar!"# 12
            },
            {
                "nama": " Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kak Fabiolla super baik baikk! Aku sukaa pakai bangett!",  
                "pesan":"Semoga diperkuat hingga tahap akhir studi ya, kak! Pasti ada tujuan akhir dari semua itu!"# 13
            },
            {
                "nama": " Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur ",
                "sosmed": "@_fairuzary",
                "kesan": "Kak Fairuz maniss! Kaya gula merah, kebangetan manisnya!",  
                "pesan":"Semoga apapun itu, diberi jalan dan kemudahan ya !"# 14
            },
            {
                "nama": " Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "Kak Tanty hiperaktif banget, kayanya kita satu frekuensi deh kak,hehehe.",  
                "pesan":"Selalu jadi pribadi yang ceria ya, kakak !"# 15
            },
            {
                "nama": " Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Kak Eggi dengan kacamatanya adalah ikon mikfes ^^ ",  
                "pesan":"Semoga kuliahnya diperlancar ya, kak "# 16
            },
            { 
                "nama": " Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Aduh, Kak Afifah manis, tegas dan lucu! Paket Komplit di mikfes",  
                "pesan":"Semoga semua urusan diberi kemudahan ya, kak "# 17
            },
            {
                "nama": " Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Kak Fabio! Lucu dan pinter dalam satu waktu! Suka deh!",  
                "pesan":"Terus jadi pribadi yang ceria ya,kak ! Sehat selaluuu!"# 18
            },
          
            {
                "nama": " Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl.Lapas Raya",
                "hobbi": "Main catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakak manis sekali , jadi suka dehh!",  
                "pesan":"Terus jadi orang manis ya kak , ITERA butuh orang manis seperti kakak!"# 19
            },
            {
                "nama": " Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakak tutorkuu! Terima kasih udah jadi pribadi ya baik dan manis ya !",  
                "pesan":"Terima kasih sudah lahir ke dunia ini, heheh!"# 20
            },
            {
                "nama": " Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kak Razin dan kacamatanya juga ikon Mikfes banget!",  
                "pesan":"Sehat dan kuat selalu di perkuliahan, kak !"# 21
            },
            {
                "nama": " Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giovaniars_",
                "kesan": "Pasti Kakak Giofani cerdas deh! Soalnya dari mukanya kelihatan banget! Kerennn!",  
                "pesan":"Semoga terus jadi orang pintar dan semoga nanti gajinya dua digit ya,kak !"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen SSD":
    def ssd():
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
                "nama": " Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": "Kakaknya berjiwa ambisius dan keren! ",  
                "pesan": " Semoga dilancarkan semuanya dan dipermudah urusannya ya "# 1
            },
            {
                "nama": " Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakaknya cantik dan seru, pasti pintar dalam manajemen uang!",  
                "pesan": "Sehat selalu ya, kakak cantik !"# 2
            },
              {
                "nama": " Ahmad Rizqi",
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
                "nama": " Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya manis dan humoris serta humble",  
                "pesan": "Semoga studinya diperlancar ya, kakak "# 4
                   },
              {
                "nama": " Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "nya pendiam tapi manis",  
                "pesan": "Sehat selalu ya "# 5
            },
            {
                "nama": " Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya cantik dan wangi, suka! ",  
                "pesan":"Semoga diperlancar studi dan semuanya yang baik mendatangi kakak! "# 6
            },
             {
                "nama": " Dhafin Razaqa Luthfi",
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
                "nama": " Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakak humble banget ",  
                "pesan": "Semoga dilancarkan studinya ya kak "# 8
            },
              {
                "nama": " Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "Kakak ini manis banget!",  
                "pesan": "Sehat selalu ya,kak "# 9
            },
              {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini aura bussines women banget!",  
                "pesan": " Semoga rezekinya lancar terus, kak"# 10
            },
              {
                "nama": " Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": " Kakak cantik deh, gak bosan lihatnya!",  
                "pesan": "Semoga semua diperlancar,kak !"# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Eksternal":
    def eksternal():
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
                "nama": " Arafi Ramadhan Maulana",
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
                "nama": " Yohanna Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana cantik dan baik! ",  
                "pesan":"Sehat selalu ya , semoga diberikan kekuatan dalam segala hal! "# 2
            },
            {
                "nama": " Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": " Kak Dea cantik dan wangi! ",  
                "pesan":"Jadi pribadi yang wangi terus ya , semerbak banget wanginya seperti bunga "# 3
            },
            {
                "nama": " Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P (Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak sonyaa, paling baik dan paling pengertian, aku sukaaa! Terima kasih sudah lahir ke bumi kakk!",  
                "pesan":"Kakak udah hebat bangett dan mengayomi saya banget!Terima kasih ya  untuk semuanyaa! I love kak sonya! kak sonya di hati selamanya hehehe "# 4
            },
            {
                "nama": " Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kak Luthfia baik dan cantik, suka deh! ",  
                "pesan":"Sehat dan selalu dipermudah studinya ! "# 5
            },
            {
                "nama": " Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kak Cindy cantik dan wangi sekali ",  
                "pesan":"Sehat dan selalu mengandalkan Tuhan ya,kak !  "# 6
            },
            {
                "nama": " Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak lucu tapi agak seram tapi lucu ",  
                "pesan":"Semoga sehat selalu ya kak , dan segala hal baik menghampiri  dengan lancar! "# 7
            },
            {
                "nama": " Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak Dea suaranya khas banget, khas MC profesional hehehe ",  
                "pesan":"Kakak berpotensi jadi pembawa berita TV Nasional kak:) Semoga studinya selalu diperlancar ya ! "# 8
            },
            {
                "nama": " Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kakak ini ganteng dan wangi! ",  
                "pesan":"Sehat selalu ya , jaga pola tidur karena sehat itu mahal ! "# 9
            },
            {
                "nama": " Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": " Kakak cantik! Manis banget dan ramah, aku suka hehehe ",  
                "pesan":"Selalu jadi pribadi yang ramah dan manis ya ! Itu ciri khas  banget soalnya:) "# 10
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakak Ilmi, cantik wangi dan humble hehehe ",  
                "pesan":"Terima kasih sudah mau saya ajakin retake foto,kak ! Semoga semua urusan  diperlancar dan diberikan keringanan "# 11
            },
            {
                "nama": " Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kak Izzah, baik dan pendiam, tapi tidak pelit berbagi ilmu! ",  
                "pesan":"Selalu semangat dalam berbagi ilmu ya kak, semoga semua hal baik menghampiri ! "# 12
            },
            {
                "nama": " Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kak Qois! Sangat baik dan sangat mengayomi! ",  
                "pesan":"Terima kasih sudah memberikan saya kesempatan jadi bagian dari SDM ya ! Semoga semua hal baik menghampiri  "# 13
            },
            {
                "nama": " Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melinza baik dan manis sekali! ",  
                "pesan":"Semoga sehat selalu ya kak , diberkati dimanapun berada! "# 14
            },
            {
                "nama": " Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla dengan kacamatanya adalah satu paket yang khas! Manis deh ",  
                "pesan":"Sehat selalu ya , jangan lupa untuk makan:) "# 15
            },
            {
                "nama": " Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakak ini asik, humble dan ramah ",  
                "pesan":"Terima kasih sudah mengayomi saya selama di SDM kak , semoga sehat selalu dan kuliahnya diperlancar "# 16
            },
            {
                "nama": " Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakak Tarisya! Baik banget, lembut banget suaranya! Dan sabar dalam mengajari saya ",  
                "pesan":"Semoga semua hal baik menghampiri  ya kak! Saya doakan semoga semuanya berjalan lancar untuk kakak!"# 17
            },
            {
                "nama": " Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kak Jasmine buat saya insecure hehehe, pintar sekali !  ",  
                "pesan":"Terus menorehkan prestasi di kancah nasional dan internasional kak, saya mendukung  selalu! "# 18
            },
            {
                "nama": " Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakak ini manis dengan baik! ",  
                "pesan":"Semoga semua studi nya diperlancar ya kak , jangan lupa untuk tetap jaga kesehatan  "# 19
            },
            {
                "nama": " Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kakak ini baik dan humble banget! ",  
                "pesan":"Terima kasih ya kak , semoga  mendapatkan semua hal baik di bumi! "# 20
            },
            {
                "nama": " Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini manis banget! ",  
                "pesan":"Tetap jadi pribadi yang manis ya,kak  "# 21
            },
            {
                "nama": " Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": " ini sangat mengayomi, baik, dan welcome sekali! ",  
                "pesan":"Terima kasih ya , semoga semua hal baik menghampiri hidup  "# 22
            },
            {
                "nama": " Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak ini manis dan tegas, saya suka! ",  
                "pesan":"Semoga sehat selalu ya kak, jangan sampai jatuh sakit. Amin "# 23
            },
            {
                "nama": " Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak Nabyla, manis dan cerdas! ",  
                "pesan":"Terima kasih sudah jadi  tutor ALE RC,kak ! Saya paham OBE karena , semoga rezeki  dilimpahkan selalu dan sehat-sehat terus! "# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list) 
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EfYmWGN1eKluaJL1Hrp_7cjSaGn3bD4d", #1
            "https://drive.google.com/uc?export=view&id=1UA6fgSfr9yGpGs_MAVQWKhjYwcJk7NbL", #2
            "https://drive.google.com/uc?export=view&id=1161Eqoi_aK1Gol_2iebMg8dR97XiJfff", #3
            "https://drive.google.com/uc?export=view&id=1dTBuOxiLos_AQ7msVzdz_eGyEIHk5kpX", #4
            "https://drive.google.com/uc?export=view&id=1ih4C9Ae2igdTvBhk9x5-dRbfkubPUgKu", #5
            "https://drive.google.com/uc?export=view&id=12W_Qdj1yXsaeaybbi65CkN26eAOU8sJh", #6
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
                "nama": " Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": "Kakak Rani manis sekaligus aura independent women nya menginspirasi saya! ",  
                "pesan":"Sehat selalu kak, kakak cocok sekali menjadi pemimpin! "# 1
            },
            {
                "nama": " Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta ber-karisma sekali! Saya suka! ",  
                "pesan":"Terus jadi inspirasi banyak orang ya, kak ! "# 2
            },
            {
                "nama": " Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak ini manis dan baik! ",  
                "pesan":"Semoga semua hal baik menghampiri hidup  yaa, kak! "# 3
            },
            {
                "nama": " Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "Kakak ini manis sekali! Seperti gula ",  
                "pesan":"Tetap jadi inspirasi semua orang ya, kak ! "# 4
            },
            {
                "nama": " Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": " Kakak ini tegas dan baik dalam satu waktu ",  
                "pesan":"Sehat dan sukses selalu ya kak, semoga Tuhan selalu memberkati langkah  "# 5
            },
            {
                "nama": " Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak ini manis sekali! ",  
                "pesan":"Terima kasih ya kak , semoga  dipenuhi hal-hal yang bahagia "# 6
            },
            {
                "nama": " May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak May manis dan tegas dalam satu waktu ",  
                "pesan":"Terima kasih ya kak, semoga  selalu mencapai kesuksesan. Amin "# 7
            },
            {
                "nama": " Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Kak Naufal baik sekali, juga welcome sekali! ",  
                "pesan":"Terus jadi pribadi yang menebar kebaikan ya kak, suskes selaluu! "# 8
            },
            {
                "nama": " Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "Kakak ini jiwa sosialisasinya kuat banget! ",  
                "pesan":"Semoga apapun itu rencana kedepannya, diberi kemudahan ya kak "# 9
            },
            {
                "nama": " Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Kakak ini suaranya bagus sekali, saya kalah loh! Sampai saya terpikat dengar suaranya ",  
                "pesan":"Semoga  selalu diberkati Tuhan dan diberikan kemudahan dalam semua pekerjaan! "# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna! Manis, cantik, baik, suara bagus! paket komplit! ",  
                "pesan":"Saya suka sekali dengan ,  asik dan seru. Semoga semua hal menghapiri  dengan bahagia "# 11
            },
            {
                "nama": " Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": "Kak Keren, paling cantik se-ITERA! ",  
                "pesan":"Terima kasih sudah mengayomi saya dengan baik ya kak, semoga semua hal baik menghampiri ! "# 12
            },
            {
                "nama": " Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Kak Hanif jiwa introvertnya menguar banget, sama seperti saya ",  
                "pesan":"Sehat selalu ya kak, semoga semua dipermudah!"# 13
            },
            {
                "nama": " Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Kak Sarah jago main musik, tambah keren sekligus tambah cantik ",  
                "pesan":"Semoga sehat selalu ya kak, Tuhan Yesus memberkati "# 14
            },
            {
                "nama": " Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kak Zahra, manis sekali ",  
                "pesan":"Semoga selalu diberikan kebahagiaan ya, kak !"# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1x19gE0vFbgapt3lLBf3MI0_JoOXbA8QL", #1
            "https://drive.google.com/uc?export=view&id=1Pzw0fZiQV_ZnpLjpCj0jwaY_O2Hwyip_", #2
            "https://drive.google.com/uc?export=view&id=1-NNhj_MGe7rfLevTpPVC3zrLTBFuj7L9", #3
            "https://drive.google.com/uc?export=view&id=1IWZuvzpgw2-QbjDHO_OQ_C_E-Zg6EQxs", #4
            "https://drive.google.com/uc?export=view&id=1HfcPLi9h4bwXiqRBhocYy8otsypuAgQz", #5
            "https://drive.google.com/uc?export=view&id=1VM5Lh8s0guSZDG1Ncf_VXSr50awEm5Un", #6
            "https://drive.google.com/uc?export=view&id=1gtIMN48zZAj-_fKqUI8_fbIpCBQl_Q-Y", #7
            "https://drive.google.com/uc?export=view&id=1uRpwaqiidu5ZwZgK4UmP83GPWEYRnTxy", #8
            "https://drive.google.com/uc?export=view&id=1phXoSZmijn_g6L-uMKjhFuTrBixXNQ9m", #9
            "https://drive.google.com/uc?export=view&id=1jvONJKtR9_YJv_bluZm90SuCRULYbHlE", #10
            "https://drive.google.com/uc?export=view&id=1JD8FV662f449FHqToyWwRX_tUPwta0cI", #11
            "https://drive.google.com/uc?export=view&id=1GQgbAhG6o34FXwe3l1PLvRgiTgrIjy4S", #12
            "https://drive.google.com/uc?export=view&id=1mu6g37yhKhhehIqeP6d7MzM4yqYtb-Ms", #13
            "https://drive.google.com/uc?export=view&id=1pbRNcmjXkl2Eg4QTz04gTyO0nkviTHUC", #14
            "https://drive.google.com/uc?export=view&id=1ei2se_1_uqgpkmD_LQqBrVdTy-Ml8CsW", #15
            "https://drive.google.com/uc?export=view&id=1KDRWePTTzJ7tpl6Kj5sxS4yFn98hO2Yo", #16
            "https://drive.google.com/uc?export=view&id=1xvFF5JY8Gjuh8K6gxab5c0dxPM773JwS", #17
            "https://drive.google.com/uc?export=view&id=1LSaE8hIscrjwVToPLISHLs84SgTmfqsu", #18
        ]
        data_list = [
              {
                "nama": " Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak Patricia sangat wangi dan cantik, suaranya juga lembut banget!",  
                "pesan": "Semoga sehat selalu ya kak !"# 1
              },
              {
                "nama": " Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "Kak ini manis sekali, pangling lihatny hehe",  
                "pesan": "Selalu menjadi pribadi yang manis ya , semoga sehat selalu"# 1
              },
              {
                "nama": " Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "Kakak ini welome banget, baik sekali!",  
                "pesan": "Terima kasih banyak ya kak, semoga sehat selalu"# 1
              },
              {
                "nama": " Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Kakak ini wangi dan tinggi banget",  
                "pesan": "Semoga semua urusan dipermudah ya, kak !"# 1
              },
              {
                "nama": " Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "Kak Rafi baik dan welcome sekali!",  
                "pesan": "Semoga semuanya dipermudah ya,kak !"# 1
              },
              {
                "nama": " Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "Kak Refa!! Manis, baik, asik dan seru! Rekan SDM kuuu!",  
                "pesan": "Semoga sehat selalu dan jadi inspirasi banyak orang terus ya kak, kakak keren parah seabrek-abrek!"# 1
              },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450002",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyanitiaaa",
                "kesan": "Kakak manis sekali dan baik sekali!",  
                "pesan": "Terus jadi panutan banyak orang ya,kakak cantik !"# 1
              },
              {
                "nama": " Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "Kakak ini baik sekali dan manis sekali",  
                "pesan": "Semoga semuanya dipermudah dan studinya diperlancar ya,kak "# 1
              },
              {
                "nama": " Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak Donna baik sekali, sangat welcome terhadap kami",  
                "pesan": "Terima kasih ya kak telah ada di dunia, semoga hal baik menghampiri "# 1
              },
              {
                "nama": " Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemmiling",
                "hobbi": "Scoll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kak Feby baik dan cantik sekali",  
                "pesan": "Sehat dan sukses selalu ya , semoga semua hal baik terjadi kepada !"# 1
              },
              {
                "nama": " Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kak Hafsa manis dan baik! Banyak membantu saya di kelas praktikum Alpro!",  
                "pesan": "Terima kasih banyak ya kak, semoga semuanya dipermudah bagi kakak "# 1
              },
              {
                "nama": " Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": " Kak Nayla manis dan baik sekali",  
                "pesan": "Tetap jadi inspirasi saya dan banyak orang ya,kak "# 1
              },
              {
                "nama": " Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania manis dan baik banget!",  
                "pesan": "Tetap jadi pribadi yang ceria ya,kak "# 1
              },
              {
                "nama": " Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "Kak Akmal ceria dan humble sekali",  
                "pesan": "Kakak mirip dengan seseorang yang saya kenal. Semoga sehat dan sukses selalu ya "# 1
              },
              {
                "nama": " Raihan Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kakak baik dan manis",  
                "pesan": "Sehat dan sukses selalu ya kakak "# 1
              },
              {
                "nama": " Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kak Citra baik dan welcome banget",  
                "pesan": "Sehat dan sukses selalu ya kak "# 1
              },
              {
                "nama": " Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "Kakak manis dan ceria banget! Sangat 'cewe bumi' looks banget hehehe",  
                "pesan": "Semoga sehat selalu ya kak, apapun itu diberikan kemudahan oleh Tuhan"# 1
              },
              {
                "nama": " Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "Kak Roma manis sekali!",  
                "pesan": "Sehat dan ceria selalu ya kak, semoga semua hal baik menghampiri !"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-wWBQ5tYJ5CJJjAVYtEWpojuQmpScdzL",
            "https://drive.google.com/uc?export=view&id=1TXzHc0w4O5-RbYu-RG6spPdahrG9AxcU",
            "https://drive.google.com/uc?export=view&id=1RzzyH-yuMDyi1YELBwxrlsXoTMgL5fq-",
            "https://drive.google.com/uc?export=view&id=1g3FkIw-xgwbWig_PdEr38dvTW6Vk9L7o",
            "https://drive.google.com/uc?export=view&id=1VrSQXXSbb6dZSaf1k6NjvOHRkll0D9Ie",
            "https://drive.google.com/uc?export=view&id=1OmIJKwIuIP_rlU_doxM-mMfufRktI8VX",
            "https://drive.google.com/uc?export=view&id=1e1NwGuaoUdhx5GTCovxgon2-rFjGT6hQ",
            "https://drive.google.com/uc?export=view&id=1oCx0tTGbrBMzDLvKk2pGFyDekXJ-q3Ba",
            "https://drive.google.com/uc?export=view&id=1jHGKwvSeXr8jY-7eNcMXnko6ZjfdvcXL",
            "https://drive.google.com/uc?export=view&id=1_iACNTCfuzCd-U8yHlPEZWsf9fIqrwX2",
            "https://drive.google.com/uc?export=view&id=1BJYjeJLDGXTX3hKZNhRI66eu03Jk-zaw",
            "https://drive.google.com/uc?export=view&id=1svLBCmkeNuDaplvO-Q-kf2ToElDXIn_1",
            "https://drive.google.com/uc?export=view&id=1cNdmrflx2JsBAmwSwN3gTiiY4ITWIcNi",
            "https://drive.google.com/uc?export=view&id=1bBWo29aTqHDuC2J8pmzs0EyZA1fHG_51",
            "https://drive.google.com/uc?export=view&id=1r7RMPdlKgGrnPWT_kQGe92RTVepqJ7B_",
            "https://drive.google.com/uc?export=view&id=1Iz0_JtxQaWl1mjj-kBCKdWFfcmp9muRt",
            "https://drive.google.com/uc?export=view&id=1ILqj3ifAGkne0KL6yYqYJB9a0zn02j61",#
            "https://drive.google.com/uc?export=view&id=1ANtuOSwBkWaeM2P21eLTwEm4IlDLN0EB",
            "https://drive.google.com/uc?export=view&id=10TO2LJICNq3r6OWLODVNRmFm-Q6SA7lY",
            "https://drive.google.com/uc?export=view&id=14oqUlVdZ357sutmY1fUdJzqoVeuQuUtY",
            "https://drive.google.com/uc?export=view&id=1K4FXTX1I7SvIAdnVYTELFMFK3Z6v9eMl",
            "https://drive.google.com/uc?export=view&id=1srPaAdlK4ARaKfVgbqoW3HYaY4M0Ergd",
            "https://drive.google.com/uc?export=view&id=14H727lghf9-_P4azNzXTF-uTQU4SAaXf",
            "https://drive.google.com/uc?export=view&id=1u327tH8DN03bRreGsCeK-zzUN8iEHSUZ",
            "https://drive.google.com/uc?export=view&id=1ARceuAs69uJdGmSXdlbVDWzMIHmRcu9r",
            "https://drive.google.com/uc?export=view&id=1bZFedZPj9aN33RVhcmsnyVkUlzJCoTd0",

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
                "kesan": "Kakaknya super duper pendiam dan tertutup!",  
                "pesan":"Semangat ya kakak untuk semester ini pasti terlewati"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Jalan jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Afifah putih banget?!",  
                "pesan": "Saya doakan dilancarkan semua urusannya kak.."# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "Kak Allya manis kalau dilihat lama-lama tidak bosan! Senyumnya juga manis!",  
                "pesan": "Bantai semua semester itu kak, kasih paham mereka! Kakak keren sekali"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Kakaknya berwawasan luas banget apalagi soal debat!",  
                "pesan":"Semangat ya kak, pasti menang!"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kaak manis sekali, senyum dan fitur wajahnya kayak orang korea",  
                "pesan": "Semangat selalu kakak, semua hal baik menghampirimu"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Kakak sangat professional!",  
                "pesan":"Semangat ya kak, semua pasti berhasil dilalui"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Kakak keren dan tampil berani!",  
                "pesan": "Selalu andalkan Tuhan ya kak!"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "Kakak keren! Ikut lomba itu keren kak!",  
                "pesan": "Semangat kakak cantik, semua pasti mendatangi wanita pintar sepertimu"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "Kakak sangat profesional dan sangat pandai",  
                "pesan":"Semangat terus kakak, pasti semua yang baik mendatangi orang yang sabar seperti kakak"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "Kakaknya baik dan taat agama sekali!",  
                "pesan":"Semangat ya kakak, semua hal yang baik pasti menghampiri"# 1
            },
            {
                "nama": "Vany Salsabila Putri", 
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak manis sekali dan cocok sekali dengan warna merah!",  
                "pesan":"Tetap semangat kakak, jaga kesehatan dan jangn lupa tidur ya kak"# 1
            }, 
                {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "Kakaknya baik bannget selama wawancara",
                "pesan": "Semangat membantai semua semesternya kakak!" # 12
            },
            
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": " Kakak keren dan ganteng!",
                "pesan": "Semangat terus ya kakak! Semua hal baik pasti menghampiri!" # 13
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak cantik dan sangat cocok dengan kacamata",
                "pesan": "Tetap semangat ya kakak cantik!" # 16
            },
             {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Saya suka sekali lihat warna mata kakak! Cantik dan kelihatan berambisi",
                "pesan": "Semangat ya kak, kesehatannya juga harus tetap dijaga ya kak, jangan jatuh sakit" # 15
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakak cantik deh dan wajahnya ciri khas banget",
                "pesan": "SEMANGAT MEMBANTAI SEMESTER ITU KAKAK!" # 14
            },
            
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Kakak ganteng dan berwibawa banget",
                "pesan": "Semangat terus dan berambisi terus ya kakak!" # 17
            },
            
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Kakak keren dan wangi",
                "pesan": "Semoga selalu diberikan kemudahan oleh Tuhan ya kak " # 18
            },
             {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "Kakaknya mukanya dipandang kayak adem gitu",
                "pesan": "Semangat terus kakak, badai selalu berlalu lalang dan pasti terlewati!" # 24
            },
            
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "Kakaknya baik dan keren sekali",
                "pesan": "Kalau tanya soal PKM gitu boleh tidak ya kak?" # 19
            },
             {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "Kakak keren banget dan tinggi banget",
                "pesan": "Semangat ya kak basketnya, kakak berpotensi jadi atlet hehehe" # 23
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "Kakaknya lucu banget baik dan ramah. Cocok sekali dengan kacamatanya",
                "pesan": "Semangat selalu ya kakak cantik" # 20
            },
            
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "Awalnya kukira nya seram tapi ternyata lucu dan humoris",
                "pesan": "Semangat terus ya kak selalu bahagia" # 21
            },
            
            {
                "nama": "Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "Kakaknya berkarisma kalau main musik!",
                "pesan": "Semangat terus ya kak, kakak keren kalau main musik!" # 22
            },

            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak keren dan cantik sekali kakak!",
                "pesan": "Semangat ya kak, pengen diajari kepanitiaan sama kakak" # 25
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Kakak dan kacamatanya jadi ikon PSDA di mataku keren banget! ",
                "pesan": "Semangat terus ya kak, semua hal baik menghampiri!" # 26
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()



# Tambahkan menu lainnya sesuai kebutuhan


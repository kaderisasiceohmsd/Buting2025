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
if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zDyb2jWOrSIUjefaMx8Qjq2NqK1BAtqD", #1
            "https://drive.google.com/uc?export=view&id=1okA5q5l6knMfJqYkeG5BmW4ywpYvrd1N", #2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #3
            "https://drive.google.com/uc?export=view&id=1oplAcBSKO7YHI1CZwxx-BZJeoXCTXmiJ", #4
            "https://drive.google.com/uc?export=view&id=1rYBE8o6ocWkk1TukUdL-pgPV9JaTszne", #5
            "https://drive.google.com/uc?export=view&id=1exf_Gj41yxjWWf8daLBY_ggY-JvGw-SJ", #6
            "https://drive.google.com/uc?export=view&id=1G5S2q2WQ6DoQJ6I05s111vxPH7VXI75u", #7
            "https://drive.google.com/uc?export=view&id=14JpMF10-GAjGz_UpqQDg5E1iG5ziQwuM", #8
            "https://drive.google.com/uc?export=view&id=1ghrY9X9HsI1kXUTMU-aMD5mJ2BLCjx7X", #9
            "https://drive.google.com/uc?export=view&id=1iqPURv0FE8Q82UiH0VNS3fg74C5lQ5hT", #10
            "https://drive.google.com/uc?export=view&id=1w1SGEil3cSe4cBiwj1Kgfx8ycFsccyht", #11
            "https://drive.google.com/uc?export=view&id=1pIQMzYQXFljXHf39fYzk_03gjE-CYTGo", #12
            "https://drive.google.com/uc?export=view&id=1HLjJ11WiTejwxPSWZ7FUPxLB3oA5Cv41", #13
            "https://drive.google.com/uc?export=view&id=1TrAe8nBZwmytx5oroOou0rcgSKsJR-_u", #14
            "https://drive.google.com/uc?export=view&id=15sr1oF49UG60CfxeWzxbUhTs4ZJH6WhV", #15
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #16
            "https://drive.google.com/uc?export=view&id=1MmxJdkzyUTwe-0IzNJtshA0iysOUP7Z0", #17
            "https://drive.google.com/uc?export=view&id=1b_VjtsD-Fu7vUyiBa-o7vSUY8kUHkefk", #18
            "https://drive.google.com/uc?export=view&id=1PyqkcO5Vd7jAI2HLX_i0ldvD8ofM-8wH", #19
            "https://drive.google.com/uc?export=view&id=1ykVfNXmRGD1a99OsjtZ64CpRv1ptxPrE", #20
            "https://drive.google.com/uc?export=view&id=1HxfjKjMGGRJlDGpeSBAsOjDPZENFGMmO", #21
            "https://drive.google.com/uc?export=view&id=19FzoXx61BGZereezGqQZZEfnzWZ_7_Jv", #22
        ] 
        data_list = [
            {
                "nama": "Kakak Randra Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kak Randa asik, wawasannya luas",  
                "pesan":"Semangat kuliahnya kak"# 1
            },
            {
                "nama": "Kakak Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak Rut asyik dan keren",  
                "pesan":"Lancar-lancar kuliahnya kak Rut"# 2
            },
            {
                "nama": "Kakak Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak Regi kadiv PSD keren",  
                "pesan":"Semangat Kak Regi, terus menginspirasi"# 3
            },
            {
                "nama": "Kakak Aisyah Musfirah",
                "nim": "123450084",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@_aishsahi",
                "kesan": "Kakak Aisyah keren cara berbicaranya",  
                "pesan":"semangat menjalani semester 5 kakak"# 4
            },
            {
                "nama": "Kakak Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak Fadil keren banget jadi duta genre",  
                "pesan":"Semoga selalu kece ya kak fadil"# 5
            },
            {
                "nama": "Kakak Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak Aqil keren gacor",  
                "pesan":"Semoga hobinya bisa dikurangi ya kak, biar sehat hehe"# 6
            },
            {
                "nama": "Kakak Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "Kakak Naufal pendiam sekali",  
                "pesan":"Semoga sehat selalu dan bahagia"# 7
            },
            {
                "nama": "Kakak Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakak Nadia Keren banget",  
                "pesan":"Selalu keren ya kak"# 8
            },
            {
                "nama": "Kakak Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak marleta murah senyum",  
                "pesan":"semangat kak semester 7 nya semoga lulus tepat waktu" # 9
            },
            {
                "nama": "Kakak Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "Kakak Akeyla namanya bagus",  
                "pesan":"Sehat-sehat kak di pramuka"# 10
            },
            {
                "nama": "Kakak Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakak Anggi kita sam sama dari Natar",  
                "pesan":"Semangat kak pp Natar-Iteranya"# 11
            },
            {
                "nama": "Kakak Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak Efi keren banget",  
                "pesan":"Kakak Efi semangat ya"# 12
            },
            {
                "nama": "Kakak Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kakak Fabiolla kita sama NIM akhirnya",  
                "pesan":"Semangat selalu kak fabiolla"# 13
            },
            {
                "nama": "Kakak Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "kakaknya keren abis",  
                "pesan":"semangat kuliahnya kak"# 14
            },
            {
                "nama": "Kakak Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@i",
                "kesan": "kak tanty sangat menginspiratif",  
                "pesan":"semangat selalu menginspiratif kak"# 15
            },
            {
                "nama": "Kakak Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": "Kakak Eggi hebat",  
                "pesan":"Semangat kuliahnya kakak hebat!"# 16
            },
            { 
                "nama": "Kakak Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak Afifah asyik bangett",  
                "pesan":"Semangat kak ngobrolnyaa"# 17
            },
            {
                "nama": "Kakak Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Fabio keren abis",  
                "pesan":"semangat terus kak jadi pj bu Febri"# 18
            },
          
            {
                "nama": "Kakak Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "kakaknya ramah dan baik hati",  
                "pesan":"bagahia selalu kakk"# 19
            },
            {
                "nama": "Kakak Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "kakaknya sangat keren",  
                "pesan":"jaga kesehatan kak"# 20
            },
            {
                "nama": "Kakak Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kak razin keren",  
                "pesan":"semangat kuliahnya kak"# 21
            },
            {
                "nama": "Kakak Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "",
                "hobbi": "Catur",
                "sosmed": "@biyokcb",
                "kesan": "Kakak Gio keren banget",  
                "pesan":"semangat Caturnya kak"# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
    
elif menu == "Baleg":
    def baleg():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1ZqTYQywevzEUqNDXKtns_JnPXcEWSUBw", #1
            "https://drive.google.com/uc?export=view&id=1edUO6AL4gBaB6_LcW3YOtpzskqLnVQGe", #2
            "https://drive.google.com/uc?export=view&id=1F3DgW2b8AK1xdZt4DkR23n144AGzgxsJ", #3
            "https://drive.google.com/uc?export=view&id=1dfEhuBjXRS9MjjmcWlZ3RcMnwEA7QK5M", #4
            "https://drive.google.com/uc?export=view&id=1n_X6bKZrqCupQgk2IUC6Qg1Wx06mnKPL", #5
            "https://drive.google.com/uc?export=view&id=1FXu0FxkTadzYvhau9W4-5VvJmK4W-0sj", #6
            "https://drive.google.com/uc?export=view&id=1w7JBlhhWmnBWf9X06bZLkc1ZPsTqzS_9", #7
            "https://drive.google.com/uc?export=view&id=18KHe-RIRW5qQ-5wp5LymVNpD3UBARiak", #8
            "https://drive.google.com/uc?export=view&id=1bFvUaDDab2VbAkvkniAKdh4f3cbjglLi", #9
            "https://drive.google.com/uc?export=view&id=1JSvDxaj2dlUvfZS74B_gw4I4oi1y0_gS", #10
            "https://drive.google.com/uc?export=view&id=1NoW5rwZFhVZHwAH0Q98vfJz3kjRUCILn", #11
            "https://drive.google.com/uc?export=view&id=1HjeAmgt8T5s4DbRKi0MCljRXt9Kvcpyv", #12
            "https://drive.google.com/uc?export=view&id=1zNKgXBsTd0RDY8_cwDNyRsXaBBdSzp34", #13
            "https://drive.google.com/uc?export=view&id=1ctlqHF9hGPFJjTbcQ9bpYTcVK2UI5JUg", #14
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
                "kesan": "keren banget jadi kabaleg",  
                "pesan": "sehat selalu kak tetap keren"# 1
            },
            {
                "nama": "Kakak Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "kakaknya baik dan ramah",  
                "pesan": "selalu ramah ya kak"# 2
            },
              {
                "nama": "Kakak Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "kak renisha rambutnya bagus",  
                "pesan": "tetap keren kak, be your self"# 3
            },
              {
                "nama": "Kakak Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kak anisa ramah",  
                "pesan": "selalu baik dan ramah ya kak kepada semua orang"# 4
            },
            {
                "nama": "Kakak Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "kak dharu ini sangat keren dan baik wawasannya luas",  
                "pesan":"semoga wawasannya semakin luas ya"# 5
            },
             {
                "nama": "Kakak Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "kak feby lucu kayak orang jepang",  
                "pesan": "tetap menjadi baik kak"# 6
            },
              {
                "nama": "Kakak Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "kak givaro sangat baik dan keren",  
                "pesan": "semoga menjadi apa yang kakak inginkan yaa"# 7
            },
              {
                "nama": "Kakak Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "kak mirzan namanya unik",  
                "pesan": "semoga bahagia selalu ya kak"# 8
            },
              {
                "nama": "Kakak Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "kak berlin lucu",  
                "pesan": "semangat kuliahnya kak"# 9
            },
              {
                "nama": "Kakak Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "keren kak jue",  
                "pesan": "tetap menginspirasi ya kakk"# 10
            },
              {
                "nama": "Kakak Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": " kocak bgt kakak ridho",  
                "pesan": "semangat dan bahagia"# 11
            },
              {
                "nama": "Kakak Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "kak feryadi keren dan hebat",  
                "pesan": "semangat selalu"# 12
            },
              {
                "nama": "Kakak Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "kak monic auranya positif banget",  
                "pesan": "jaga kesehatan kakak"# 13
            },
              {
                "nama": "Kakak Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "Kak wawa lucuu banget",  
                "pesan": "semangat kuliahnya kak"# 14
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kakak Rendra asik",  
                "pesan": "Be happy kakak"# 1
            },
            {
                "nama": "Kakak Johannes Krisjon Silitonga",
                "nim": "122450000",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kak Jo Lucu",  
                "pesan": "Semoga jalannya selalu dipermudah"# 1
            },
              {
                "nama": "Kakak Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Elisabeth lucu dan senyumnya manis",  
                "pesan": "Lancar kuliahnya kak"# 1
            },
              {
                "nama": "Kakak Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "Kak Puspa ramah",  
                "pesan": "Semoga sehat selalu kak"# 1
            },
            {
                "nama": "Kakak Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty seruu",  
                "pesan":"Jangan lupa makan kak"# 1
            },
             {
                "nama": "Kakak Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "Kak Hanum lucu",  
                "pesan": "Semoga bahagia selalu kakak"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "kak bintang tegas dan bijaksana",  
                "pesan": "semangat menjalani semester akhirmya kak"# 1
            },
            {
                "nama": "Kakak Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": "kak nadya senyumnya lucu banget",  
                "pesan": "semangat selkalu kak kuliahnya"# 1
            },
            {
                "nama": "Kakak Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak azizahh keren parah",  
                "pesan": "jaga kesehatannya kak"# 1
            },
            {
                "nama": "Kakak Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "Kak lia tegas",  
                "pesan": "semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eAE-Snq10yghfJXjpM5SNPFLdx-5oJ2l", #1
            "https://drive.google.com/uc?export=view&id=1FrRJ5fCKdN7elTmS3rs5yX4pNpZ7V-lh", #2
            "https://drive.google.com/uc?export=view&id=1QYvfWaqv1SzJguQ_kSFfjRL-plJbPgEP", #3
            "https://drive.google.com/uc?export=view&id=1YdAUzL1wN2AOG8yknMjRpD5jWKLz90aY", #4
            "https://drive.google.com/uc?export=view&id=19QyjTDkA3aw1aG39KEsbvypI3her6Gna", #5
            "https://drive.google.com/uc?export=view&id=1K2BCiPgTADqF9HhlwA6N5Yan4c_xcw7-", #6
            "https://drive.google.com/uc?export=view&id=11mTc8FgTMNcUwbdZ7tgr_bJbfx1273DF", #7
            "https://drive.google.com/uc?export=view&id=1Di1qAYjqhlk2FX6C1ca_kGCWvJWuzCBf", #8
            "https://drive.google.com/uc?export=view&id=1lrjDstDKaCAKFRiX7Ofkq3ktk-dDC9FP", #9
            "https://drive.google.com/uc?export=view&id=1brUhv2cy056_LEOYDmpwzE2vSFNymzKs", #10
            "https://drive.google.com/uc?export=view&id=14GcZw9CUHRkjksyKcUMgri0ZAir-Cz1a", #11
            "https://drive.google.com/uc?export=view&id=1Z0LijJqo34hlP1mRpr19-_MhDjYlGITJ", #12
            "https://drive.google.com/uc?export=view&id=1nI2rypX1F5U8tgSeuaDFY93ohMy84yj_", #13
            "https://drive.google.com/uc?export=view&id=1tg1r5SvgFjICtxL_rwSWtET5gxJ80aOz", #14
            "https://drive.google.com/uc?export=view&id=1AAgwWw8MEypNa3F5a7B8R6Exeo0rA-C", #15
            "https://drive.google.com/uc?export=view&id=1AyFKn1ZDbGEOG6D7H_0FjtPmuLDOYLJ2", #16
            "https://drive.google.com/uc?export=view&id=1ldUXLAtaAQZHkR8Qa0MWK2FrrItJiw_9", #17
            "https://drive.google.com/uc?export=view&id=1no3mCqfX2qRDzc5PMzMeMMns0prZ62SW", #18
            "https://drive.google.com/uc?export=view&id=1sWUWbc4sKl4UOS2X9kFGuixxiTuoVfx-", #19
            "https://drive.google.com/uc?export=view&id=1mLyOKBqBLsNkSzpU-e6rblp0YX55a0yD", #20
            "https://drive.google.com/uc?export=view&id=17CQcLxXbrTh8IXH_7TAQTCZEsNWckrB5", #21
            "https://drive.google.com/uc?export=view&id=19ABETqn7Ed4lJLQwBouAScMJu_H_iKxL", #22
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #23
            "https://drive.google.com/uc?export=view&id=1oRxMs12cyUxG2LgKB6Y2pQORj-wp4LoK", #24
        ] 
        data_list = [
            {
                "nama": "Kakak Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Kak Arafi keren ya",  
                "pesan":"Semangat kuliahnya kak, tetap keren"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak Yohana cantik dan baik",  
                "pesan":"Lancar-lancar kuliahnya kak Yohana"# 2
            },
            {
                "nama": "Kakak Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika Baju",
                "sosmed": "@jasminednva",
                "kesan": "Kak Jamine bagus banget namanya",  
                "pesan":"Semangat Kuliahnya kak Jasmine, sehat selalu"# 3
            },
            {
                "nama": "Kakak Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kak Mut Lucu dan baik",  
                "pesan":"semangat kuliahnya kak mut"# 4
            },
            {
                "nama": "Kakak Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Kak Arya senyumnya keren",  
                "pesan":"Jangan ngelamun terus kak, semangat"# 5
            },
            {
                "nama": "Kakak Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak Arini tinggi",  
                "pesan":"Semoga hobinya bisa berkeliling dunia sampai jauh ya kak"# 6
            },
            {
                "nama": "Kakak Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@-",
                "kesan": "Kak Aldi keren bisa jadi ketuplak Sciencefest",  
                "pesan":"Semoga selalu sehat ya kak"# 7
            },
            {
                "nama": "Kakak Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakak Lutfia Keren banget",  
                "pesan":"Selalu keren ya kak"# 8
            },
            {
                "nama": "Kakak Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak Nabyla murah senyum",  
                "pesan":"semangat kak semester 5 nya, kalau jalan-jalan jangan sampai nyasar ya kak" # 9
            },
            {
                "nama": "Kakak Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak Dea keren jadi kadiv intra",  
                "pesan":"Sehat-sehat selalu kak dea"# 10
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "Like Crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "Kak Sonya keren jadi asprak",  
                "pesan":"Semangat kak scroll nya"# 11
            },
            {
                "nama": "Kakak Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak Luthfia keren banget",  
                "pesan":"Kakak Luthfia semangat kuliahnya ya"# 12
            },
            {
                "nama": "Kakak Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakak Cindy keren bangte bisa jadi finalis duta",  
                "pesan":"Semangat selalu kak semoga doa baiknya selalu terkabulkan"# 13
            },
            {
                "nama": "Kakak Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kak desman ketang keren",  
                "pesan":"Semangat kuliahnya kak desman"# 14
            },
            {
                "nama": "Kakak Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton reels AGZ",
                "sosmed": "@deaamnd3_",
                "kesan": "Kak dea heboh banget, yareuu",  
                "pesan":"Semangat kak dea berbagi vibes positifnya"# 15
            },
            {
                "nama": "Kakak Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "MAin BAdmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kak Irvan keren kadiv pengmas ",  
                "pesan":"Semangat kuliahnya kakak Irvan!"# 16
            },
            { 
                "nama": "Kakak Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak cantik(fathya) asyik bangett",  
                "pesan":"Semangat kak minta tolongnya" # 17
            },
            {
                "nama": "Kakak Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kak Ilmi keren abis",  
                "pesan":"semangat terus kak kuliahnya" # 18
            },
          
            {
                "nama": "Kakak Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Keren banget kak izzah hobinya baking",  
                "pesan":"Semangat selalu kak untuk apapun yang terjadi dalam hidup kak izzah"# 19
            },
            {
                "nama": "Kakak Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Kak Qois orangnya seru dan asik banget, selalu bikin suasana rame.",
                "pesan": "Tetap semangat di pengmas kak, jangan lupa hemat bensin ya!" # 20
            },
            {
                "nama": "Kakak Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kak Melinza lembut dan kalem banget",
                "pesan": "Terus semangat dan jangan lupa rehat nonton film favoritmu ya kak!" # 21
            },
            
            {
                "nama": "Kakak Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kak Nayla orangnya tenang tapi tetap punya aura semangat yang positif.",
                "pesan": "Semoga makin bahagia dan punya banyak waktu buat me time berkualitas kak!" # 22
            },
            
            {
                "nama": "Kakak Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kak Adit keren",
                "pesan": "Terus jelajahi dunia kak, tapi jangan lupa istirahat juga ya" # 23
            },
            
            {
                "nama": "Kakak Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajahi desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kak Tari energinya positif banget.",
                "pesan": "Semangat terus kak, semoga makin banyak desa yang bisa dijelajahi!" # 24
            }

            
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
elif menu == "Baleg":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1E7FEUk_KL894s6uUBj0adDHDnOohDF4Z", #1
            "https://drive.google.com/uc?export=view&id=1VMR7eIWKaaz1ospWzLTv-lGckTH15hls", #2
            "https://drive.google.com/uc?export=view&id=1STC8KjGvTXLYC45aeFL0_c9Zk8NOdKj7", #3
            "https://drive.google.com/uc?export=view&id=1vjihepUOlZXpD8vQIWOXa4SOiENlSBO8", #4
            "https://drive.google.com/uc?export=view&id=1OBc3fOJSFXbNNZo-GU75FQv0M2tyJzw8", #5
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #6
            "https://drive.google.com/uc?export=view&id=1fFGLOlRu5NDSXA_uqXH-45fmlNV272Xf", #7
            "https://drive.google.com/uc?export=view&id=1pU3zM-fZZIDUVWOvwTRA53U6o3mJB_iL", #8
            "https://drive.google.com/uc?export=view&id=1EE4kwBLCVYyd2UfwlLUDpUYGYHJRwlJX", #9
            "https://drive.google.com/uc?export=view&id=1CcmZGyAfBABIGkHD32ZnrpJhiNM8OYa_", #10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #11
            "https://drive.google.com/uc?export=view&id=1Ajz8KOxRWbBTxmS9sp617QM20yb1_jZh", #12
            "https://drive.google.com/uc?export=view&id=1xPTJKOn4r8pVAO1482ssq1U4i6ZDHXZr", #13
            "https://drive.google.com/uc?export=view&id=1DgZMWj2nCSwILvekY1olwg5SY7aXGJC_", #14
            "https://drive.google.com/uc?export=view&id=1W3xQIF69x-6kQLrHkbnt3IuqQv8KhMjc", #15
        ]
        data_list = [
            {
                "nama": "Kakak Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": "Kak Rani sosok yang inspiratif dan bijak",
                "pesan": "Semoga makin banyak ilmu dari setiap kajian yang diikuti!" # 1
            },
            
            {
                "nama": "Kakak Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta Bawa vibes positif.",
                "pesan": "Tetap enjoy dan semangat terus ya kak" # 2
            },
            
            {
                "nama": "Kakak Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kak Salwa keren",
                "pesan": "Semoga makin enak masakannya" # 3
            },
            
            {
                "nama": "Kakak Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Masak",
                "sosmed": "@azza.raaa_",
                "kesan": "Kak Azzahra sangat ramah",
                "pesan": "Semoga makin semangat kuliahnya kak azzahra" # 4
            },
            
            {
                "nama": "Kakak Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal": "Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "Kak Haikal keren abieez",
                "pesan": "Jangan lupa istirahat di sela-sela ngitung krikilnya ya kak!" # 5
            },
            
            {
                "nama": "Kakak Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kak Iqfina selalu ceria",
                "pesan": "Semangat terus kak Iqfina" # 6
            },
            
            {
                "nama": "Kakak May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kak May keren banget",
                "pesan": "Terus jadi versi terbaik dari diri sendiri ya kak!" # 7
            },
            
            {
                "nama": "Kakak Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@",
                "kesan": "Kak Naufal sosok yang kalem tapi kocak juga dalam waktu bersamaan",
                "pesan": "Semoga makin terus aktif di setiap kegiatan kak!" # 8
            },
            
            {
                "nama": "Kakak Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kak Zailani energinya luar biasa, selalu semangat di setiap kegiatan.",
                "pesan": "Terus jaga semangat dan kesehatan, biar makin kuat berolahraga kayak hobinya" # 9
            },
            
            {
                "nama": "Kakak Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "Kak Rendi keren banget kadiv kerohanian",
                "pesan": "Terus berkarya lewat lukisan dan semangat kerohaniaannya kak!" # 10
            },
            
            {
                "nama": "Kakak Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal": "Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna lucu, hobi melihat cicaknya unik",
                "pesan": "Tetap jadi pribadi yang ceria dan penuh semangat ya kak!" # 11
            },
            
            {
                "nama": "Kakak Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "Pemda",
                "hobbi": "Musik",
                "sosmed": "@kerennmrtl",
                "kesan": "Kak Keren kayak namanya, keren",
                "pesan": "Semoga selalu membawa semangat kebaikan kak!" # 12
            },
            
            {
                "nama": "Kakak Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Kak Hanif keren banget jago futsal",
                "pesan": "Tetap semangat dimana pun kakak berada yaa" # 13
            },
            
            {
                "nama": "Kakak Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main alat musik",
                "sosmed": "@ssarahwsti",
                "kesan": "Kak Sarah punya hobi yg keren bangett",
                "pesan": "Terus kembangkan bakat musiknya dan tetap semangat ya kak!" # 14
            },
            
            {
                "nama": "Kakak Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@",
                "kesan": "Kak Zahra lembut",
                "pesan": "Semoga makin aktif dan terus menebar kebaikan di setiap kegiatan!" # 15
            }

            
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1yglh7JpJrBAztxgZL7WxHCe-NTvEUfHC", #6
            "https://drive.google.com/uc?export=view&id=12mhSHo-eJiAlAyaxMww2KBvy31kw5OK2", #7
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        
            
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
                "kesan": "kakak cia lucu banget",  
                "pesan": "semangat kuliahnya kakak"# 1
            },
            {
                "nama": "Kakak Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "kak neli juga gak kalah lucu",  
                "pesan": "semoga kebahagiaan selalu menyertai kakak yaa"# 2
            },
              {
                "nama": "Bang Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "bang anam keren bgt",  
                "pesan": "keren selalu ya bang"# 3
            },
              {
                "nama": "Bang Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "bang labo juga gak kalah keren",  
                "pesan": "semangat kuliahnya bang labo"# 4
            },
              {
                "nama": "Bang Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "keren banget bang rafi nimnya 1",  
                "pesan": "semangat kuliahnya bang rafii"# 5
            },
              {
                "nama": "Kakak Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "kak refa lucuu bgtt",  
                "pesan": "semangat kuliah semester 5 kak refa"# 6
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "kakaknya canti dan imut",  
                "pesan": "sehat selalu kakak"# 7
            },
              {
                "nama": "Kakak Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "kakaknya cantik dan ramah",  
                "pesan": "semangat selalu kak dalam menjalani semester 5"# 8
            },
              {
                "nama": "Kakak Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "kak donna suaranya lembut",  
                "pesan": "sehat dan bahagia kak donna"# 9
            },
              {
                "nama": "Kakak Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemmiling",
                "hobbi": "Scoll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kak feby keren",  
                "pesan": "keren selalu kak feby"# 10
            },
              {
                "nama": "Kakak Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kak hafsa cantik",  
                "pesan": "semangat kuliahnya kakak"# 11
            },
              {
                "nama": "Kakak Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "kak nayla senyumnya lucu",  
                "pesan": "semangat selalu kak apapun yg terjadi"# 12
            },
              {
                "nama": "Kakak Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "kak sania keren isa jadi anak konten",  
                "pesan": "be happy kak sania"# 13
            },
              {
                "nama": "Bang Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "bang akmal keren jadi kadiv desain",  
                "pesan": "semangat bang ngerjar gelar S.Si.d nya"# 14
            },
              {
                "nama": "Kakak Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "kak raihana orangnya ramah",  
                "pesan": "hebat kak"# 15
            },
              {
                "nama": "Kakak Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "kita sama kak dari natar",  
                "pesan": "kak citra semangat selalu desainnya"# 16
            },
              {
                "nama": "Kakak Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtvm",
                "kesan": "kakak sangat ramah",  
                "pesan": "sehat selalu kak"# 17
            },
              {
                "nama": "Kakak Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "kak roma paling lucuu",  
                "pesan": "semangat kuliahnya kak jangan berhenti lucu"# 18
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1u_wPCTbS9l022dVQEUkLsTVh8QP79Ax9", #1
            "https://drive.google.com/uc?export=view&id=1qdJCKA8xrK6rKIU-giO0DO-9VQ8qlU9W", #2
            "https://drive.google.com/uc?export=view&id=1Giv8_wJlDseLUT9YmO5d6ABAWIgloQLw", #3
            "https://drive.google.com/uc?export=view&id=13k61uERNKVoPkuIrBZjkloFpE4CVD51f", #4
            "https://drive.google.com/uc?export=view&id=156NFN2fW0ybaCu_pCDO1Rz7jRMDQTv1O", #5
            "https://drive.google.com/uc?export=view&id=1Im4ElQIQkAypc_SpliFnbK5jaEUhNElY", #6
            "https://drive.google.com/uc?export=view&id=12d2fmmLErj9tXRPJf9v0T9rfiiMBViFx", #7
            "https://drive.google.com/uc?export=view&id=1ixo-_rNAtRRIvwTcK-6izHChPfQHAcy4", #8
            "https://drive.google.com/uc?export=view&id=1OX20Cl_R00UTgBP1f0EzFS5srftGdmmM", #9
            "https://drive.google.com/uc?export=view&id=1CuJ9BZyd4H50mmOdiiOrZTLqX1WR-IWj", #10
            "https://drive.google.com/uc?export=view&id=1QCTcXpfCCQKqP3blrqypyc7DprT2HhzK", #11
            "https://drive.google.com/uc?export=view&id=1GrVkYsXW370vB3j0KDuNEqrT4OSMrtZm", #12
            "https://drive.google.com/uc?export=view&id=1wkvAjgRZ4wi3d7y_5U-4LmV5d2cfqP2u", #13
            "https://drive.google.com/uc?export=view&id=170pnk_wEANdp7FFCY9qwT0NKapq-YeBv", #14
            "https://drive.google.com/uc?export=view&id=1o9455JkYa08LllBIQoC0MmhlaSug63ze", #15
            "https://drive.google.com/uc?export=view&id=1j_Na6ugSgWr48Y15t6LUcqWOkRsbT5hS", #16
            "https://drive.google.com/uc?export=view&id=1j4gN8AAHvQ_CxMKXAFK2rPLENISMcBx8", #17
            "https://drive.google.com/uc?export=view&id=1iHn5udusVyMsZxzKMjpRIfNmTMvBeIOV", #18
            "https://drive.google.com/uc?export=view&id=1VVttuVvQjHCRrPWPhvnqXTY3jHW0r-KS", #19
            "https://drive.google.com/uc?export=view&id=13764IarRE4jRHDY0N9OFtGkLzX7b_sg4", #20
            "https://drive.google.com/uc?export=view&id=1liZHEadrmOoRV1Zu975MAqO6Uq_cjDZ4", #21
            "https://drive.google.com/uc?export=view&id=1vxeC3VFOFXXuh0QnS4-PAoeeFMNGtQJB", #22
            "https://drive.google.com/uc?export=view&id=1j74N5HQi2aF0ad7DvhBJ8yDGtNyHDiR9", #23
            "https://drive.google.com/uc?export=view&id=18A_tuf9rokWfsx5QELP4kISjraqYrIls", #24
            "https://drive.google.com/uc?export=view&id=1ONSeWLHFVUXXLVlFWEZ9ge_06epwyRnc", #25
            "https://drive.google.com/uc?export=view&id=1_Rs9Q2-HmRevikaxr79ySIcVLFubyn5L", #26
            
        ]
        data_list = [
            {
                "nama": "Kakak Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ ",
                "kesan": "keren Kak Ferdy jadi kadep",  
                "pesan":"Semangat terus jadi kadepnya kak "# 1
            },
            {
                "nama": "Kakak Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "kak afifh cantik dan baik",  
                "pesan":"Semangat kuliahnya kakak sekdep"# 2
            },
            {
                "nama": "Kakak Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "Kak pasha tegas",  
                "pesan":"Semangat kak semester akhirnya"# 3
            },
            {
                "nama": "Kakak Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Kereen banget",  
                "pesan":"Semangat Kak Ahmad, tetap mengudara"# 4
            },
            {
                "nama": "Kakak Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "kak arienta keren",  
                "pesan":"semangat kak dan bahagia selalu"# 5
            },
            {
                "nama": "Kakak Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "Kak daffa keren",  
                "pesan":"keren terus ya kak"# 6
            },
            {
                "nama": "Kakak Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Hobinya banyak, keren deh",  
                "pesan":"Semangat terus untuk menekuni hobi"# 7
            },
            {
                "nama": "Kakak Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "kakaknya ramah",  
                "pesan":"semangat kuliahnya kak"# 8
            },
            {
                "nama": "Kakak Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "keren banet jago koding",  
                "pesan":"semoga jadi data engineer ya bang"# 9
            },
            {
                "nama": "Kakak Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": "tegas dan berwibawa",  
                "pesan":"sehat selalu ya kak"# 10
            },
            {
                "nama": "Kakak Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakaknya tegas namun kalau ketawa lucu",  
                "pesan":"jangan marah-marah terus ya kak, jaga kesehatan"# 11
            },
            {
                "nama": "Kakak Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": "Kak Sahid ramah dan bersemangat, selalu aktif di setiap kegiatan.",
                "pesan": "Terus jaga semangat dan tetap rajin latihan voli ya kak" # 12
            },
            
            {
                "nama": "Kakak Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Kak Ali keren",
                "pesan": "Semoga dompetnya sering tebal biar bisa kulineran terus ya kak" # 13
            },
            
            {
                "nama": "Kakak Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kak Rosalia lucu dan ceria banget",
                "pesan": "Tetap jadi pribadi ceria" # 14
            },
            
            {
                "nama": "Kakak Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "-",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma murah senyum",
                "pesan": "Semoga makin sukses dan tetap rendah hati ya kak" # 15
            },
            
            {
                "nama": "Kakak Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Ferazka chill banget",
                "pesan": "Tidurnya jangan kelamaan, tetap semangat ikut kegiatan ya kak" # 16
            },
            
            {
                "nama": "Kakak Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Kak Sahid keren",
                "pesan": "Semoga makin jago main game" # 17
            },
            
            {
                "nama": "Kakak Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Kak Daffa keren",
                "pesan": "Terus semangat kuliahnya" # 18
            },
            
            {
                "nama": "Kakak Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": "Kak Ihsan seru banget",
                "pesan": "Terus semangat kak, semoga lelenya makin banyak yang ketangkap!" # 19
            },
            
            {
                "nama": "Kakak Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "Kak Rewina calm tapi perhatian banget ke teman-teman.",
                "pesan": "Terus semangat dan jangan lupa isi hari dengan musik favoritmu!" # 20
            },
            
            {
                "nama": "Kakak Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": "Kak Benget jago banget main futsal",
                "pesan": "Terus latihan dan tetap rendah hati di setiap pertandingan kak!" # 21
            },
            
            {
                "nama": "Kakak Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "Kak Uliano multitalenta banget dan punya karakter unik.",
                "pesan": "Terus kembangkan bakatmu dan semoga makin produktif dalam hal positif!" # 22
            },
            
            {
                "nama": "Kakak Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": "Kak Kevin tinggi",
                "pesan": "Terus semangat nge-dribble kehidupan dan jangan lupa istirahat kak" # 23
            },
            
            {
                "nama": "Kakak Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "Kak Erma enerjik dan ceria banget",
                "pesan": "Terus menari dalam semangat dan jangan berhenti berkarya kak" # 24
            },
            
            {
                "nama": "Kakak Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kak Lidia lembut",
                "pesan": "Semoga makin aktif dan sukses di setiap langkahnya kak" # 25
            }
            {
                "nama": "Kakak Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "Kak Ridwan kece bgt",
                "pesan": "Semoga makin semangat main badminnya kak" # 26
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17bcYFXjB3LlnjedAgRW5R9WfFBtMTESf", #1
            "https://drive.google.com/uc?export=view&id=13_iSyUaTtJv8LVySmK_pFExCoBnbmkZZ", #2
            "https://drive.google.com/uc?export=view&id=1xKB6fao3y7eZe0_4bAUnkPm4GbAdAAJJ", #3
            "https://drive.google.com/uc?export=view&id=1s-Ie2veqsKxcNg_d9MmYedv60H2npD9r", #4
            "https://drive.google.com/uc?export=view&id=1biljBZ-a3PWkwG5717jHeVHIQCCTq9oP", #5
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #6
            "https://drive.google.com/uc?export=view&id=1KX0kd0GgPYARL9HSNn6xWDTFQGPdgz3Z", #7
            "https://drive.google.com/uc?export=view&id=1kCmowRnNbpXskwVROUbEcpUt9eEoNdfs", #8
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #9
            "https://drive.google.com/uc?export=view&id=1OruTJjsylxNIv5jld6fys0X_9MeRPAzs", #10
            "https://drive.google.com/uc?export=view&id=1hyQFr4Syqm87Wex35onnWWQr3uraClEn", #11
            
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
                "kesan": "Kakaknya lucu ",  
                "pesan": " Semoga dilancarkan kuliahnya" #1
            },
            {
                "nama": "Kakak Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": "Kakak dina asik ",  
                "pesan": "Sehat selalu kak"# 2
            },
              {
                "nama": "Kakak Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": "Kakaknya keren dan cakep ",  
                "pesan": "Semoga kuliahnya berjalan lancar kak "# 3
            },
              {
                "nama": "Kakak Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya keren sekali ",  
                "pesan": "Semoga bahagia kak "# 4
            },
            {
                "nama": "Kakak Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "kakaknya cantik dan baik",  
                "pesan": "semangat kak"# 5
            },
            {
                "nama": "Kakak Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": ".",
                "asal": ".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": ".",
                "kesan": "Kakaknya keren dan baik ",  
                "pesan":"Semoga diperlancar semua urusannya kakak"# 6
            },
             {
                "nama": "Kakak Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kakaknya keren pendiam",  
                "pesan": "Semangat kak kuliahna "# 7
            },
              {
                "nama": "Kakak Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya cantik banget ",  
                "pesan": "jaga kesehatan kak"# 8
            },
              {
                "nama": "Kakak Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "kakaknya senyumnya manis",  
                "pesan": "jaga kesehatan kak"# 9
            },
              {
                "nama": "Kakak Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "kakaknya jiwa usahanya keren bgt",  
                "pesan": "semangat danusannya kak naya"# 10
            },
              {
                "nama": "Kakak Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "kakaknya pendiam dan murah senyum",  
                "pesan": "semangat selalu kak"# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()



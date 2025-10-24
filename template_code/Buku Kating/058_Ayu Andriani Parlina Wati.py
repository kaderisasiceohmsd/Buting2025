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
            "https://drive.google.com/uc?export=view&id=1jqE0npXVVaWUlgDRPMGy67ftEd1iQQOs",
            "https://drive.google.com/uc?export=view&id=1_xrJ6pBwRQYhiTgReTXJNyEeYBTn2z6M",
            "https://drive.google.com/uc?export=view&id=19uh5w_-RDRla305Gt3jLbGIkvRYVThI3",
            "https://drive.google.com/uc?export=view&id=1_KYoQ0KCkLxP4h7gADb7UR8Nfv0CIRNQ",
            "https://drive.google.com/uc?export=view&id=1FZfkAPeJ3GTwg37vWrO5T0Vr_3BPb07q",
            "https://drive.google.com/uc?export=view&id=1uPbnjJiGl5InLCTQF_5jEOPQy_gAS1ww",
            

        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Cikarang",
                "alamat": "Pulau Damar",
                "hobbi": "Ikut lomba burung murai",
                "sosmed": "@_erendraa",
                "kesan": "Semangat terus bang, keren banget pokoknya!",  
                "pesan":"Jangan lupa istirahat bang"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca Buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Ngobrolnya keren,asik abangnya ngerangkul, jadi engga canggung buat nanya",  
                "pesan":"Semoga sukses di setiap langkahnya bang!"# 1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Ayres kost",
                "hobbi": "Jajan",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya Ceria terus, bikin suasana rame.",  
                "pesan":"Jangan pernah berubah ya, kak!"# 1
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya kalem tapi keren.",  
                "pesan":"Tetap jadi contoh baik buat kami!"# 1
            },
            {
                "nama": "Eksanty F Sugma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal":"Kelagian Kecil, Pahawang",
                "alamat": "Pesawaran",
                "hobbi": "Ngambilin Lanyard",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakaknya Ceria dan positif vibes banget.",  
                "pesan":"Terus sebarin energi baiknya ya, kak!"# 1
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Gya kost",
                "hobbi": "Cute",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya humble banget.",  
                "pesan":"Jangan berubah ya kak, tetap rendah hati."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()



if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ts9AHl7Z-3t7BMhTzhvahNe_S7wt_X0t",
            "https://drive.google.com/uc?export=view&id=1EdNNXUWfMFpb2hRflisg_jfKv0WshJ8S",
            "https://drive.google.com/uc?export=view&id=1U_FSzEh7X3Dus5YaKgolmrzUt7i3aTzF",
            "https://drive.google.com/uc?export=view&id=1NVgGPDeFFJXPYaoZPuSgT9GdrmA8q-by",
            "https://drive.google.com/uc?export=view&id=1M9w9HOlD1cCq8SWQdCL3oE85iJz2keeM",
            "https://drive.google.com/uc?export=view&id=1nhGX454mGruxoJRTqmDBqDM1Cei6eyOv",
            "https://drive.google.com/uc?export=view&id=1-yeHBeZ1KpWj7nUuYbMA5Dm-XdEYZKX2",
            "https://drive.google.com/uc?export=view&id=1UjMGvPiG0laonithBfNaUePgw6WMFOwK",
            "https://drive.google.com/uc?export=view&id=1jRAgbpo9yAuSM3ZA0voMEz3x9xMGyNFy",
            "https://drive.google.com/uc?export=view&id=18V3jPNiq2qzI6FJGVn7f_SYo8rNO675v",
            "https://drive.google.com/uc?export=view&id=1ps4W-7FJonCuWyR9D2lIHPHBjgJJ8DFV",
            "https://drive.google.com/uc?export=view&id=1rvThRTq593cVGoDJCHBDlB8svDnJ4jSw",
            "https://drive.google.com/uc?export=view&id=1rsluZDyRCRAAEsLCIZ7D-o1BZ8z3pzqC",
            "https://drive.google.com/uc?export=view&id=1__wpApG4hb7AznMqJru-Si2WF72tleDG",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Tanjung Morawa",
                "alamat": "B2 no 2",
                "hobbi": "main volly bareng feby",
                "sosmed": "@jeremia_s_",
                "kesan": "abangnya berwawasan luas banget.",  
                "pesan":"Semoga ilmunya makin berkembang bang!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "kalo badmood liat zaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya adem vibes-nya. ",  
                "pesan":"Jangan pernah hilang ketenangan itu kak."# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin Alat Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya penuh ide keren.",  
                "pesan":"Terus berinovasi ya kak!"# 1
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Wakatobi",
                "hobbi": "Bowling",
                "sosmed": "@ansftynn",
                "kesan": "Kakaknya murah senyum.",  
                "pesan":"Semoga senyumnya gak pernah pudar kak."# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "abangnya lucu dan pinter.",  
                "pesan":"Semoga semua impian abang tercapai."# 1
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Wai huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya bikin nyaman ngobrolnya.",  
                "pesan":"semangat kuliahnya kak"# 1
            },
             {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "abangnya keren, inspiratif dan asik di ajak ngobrol",  
                "pesan":"sehat terus ya bang"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain Makanan Baru",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya penuh semangat dan asik",  
                "pesan":"Semoga semangat abangnya nular ke semua!"# 1
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "ngumpulin batu unik dipantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya perhatian banget",  
                "pesan":"Terima kasih udah selalu peduli kak!"# 1
            },
             {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "20",
                "asal":"Teluk Mondawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya santai tapi bijak",  
                "pesan":"Semoga semua urusannya dimudahkan!"# 1
             },
             {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "keren bang, gokill pokoknya",  
                "pesan":"semoga lancar terus urusannya bang"# 1
            },
             {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin ka wawa ngomong",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya Orangnya asik banget, tiap ngobrol selalu bawa vibes positif",  
                "pesan":"Tetap jadi pribadi yang seru bang"# 1
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML hero semua franco",
                "sosmed": "@Monica_tjg",
                "kesan": "Orangnya asik parah! Selalu punya gaya sendiri yang bikin semua orang kagum",  
                "pesan":"Sukses dan makin kece tiap harinya kak!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya baik banget, gampang bikin orang lain nyaman",  
                "pesan":"Jangan lupa istirahat ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O36IPlait2QAkFa3X-8jB9MdnaSl81px",
            "https://drive.google.com/uc?export=view&id=1S1pr86KIIuOtP-3_hGn6wVbpyoznO-yM",
            "https://drive.google.com/uc?export=view&id=1n3S40MEVPn-3dIcNQTwLLPu5s2AXCbHc",
            "https://drive.google.com/uc?export=view&id=1bb59ASsNUT7TBQJstrNchk7dnvo9dmIZ",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Raden Saleh",
                "hobbi": "Mancing",
                "sosmed": "@bintangtwinkle",
                "kesan": "Keren banget, abangnya jago banget dalam ngatur waktu",  
                "pesan":"jangan lupa juga kasih waktu buat diri sendiri bang "# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjanani",
                "kesan": "kakaknya baik dan penyabar banget",  
                "pesan":"Tetap jadi sosok baik yang bisa nyebarin hal positif ke sekitar kak"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB1",
                "hobbi": "Denger musik sambil jalan",
                "sosmed": "@fathinahazzh",
                "kesan": "seru banget, Obrolannya jadi engga bosen",  
                "pesan":"Semangat terus kuliahnya kak jangan lupa makan"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main",
                "sosmed": "@lia.h_264",
                "kesan": "Baik dan murah senyum",  
                "pesan":"Tetap jadi pribadi keren yang rendah hati ya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZpozxPvdpgHz8RqonNLS_Fs1E98nrdsT",
            "https://drive.google.com/uc?export=view&id=12JEYn20zgmuavbJhQIBYtJKysbRjrXkf",
            "https://drive.google.com/uc?export=view&id=1OxrIq1TVa-4_ZTfUqx61w7h6I3GOFsWb",
            "https://drive.google.com/uc?export=view&id=1c6i6yBTrlV0PIaOVe65QJCB0R5QbBoGH",
            "https://drive.google.com/uc?export=view&id=13F222GAOCwtosu9fR4_FNb7azOwxqkZF",
            "https://drive.google.com/uc?export=view&id=1Tgg0erdpQh-sH9x-dqu6bqP76qCYtpLW",
            "https://drive.google.com/uc?export=view&id=15nOHEbQQusgabf28tPF0Luvw--r6vVmO",
            "https://drive.google.com/uc?export=view&id=12zvU4srzwqTKL2XHAcQPB9D68OCnqN7r",
            "https://drive.google.com/uc?export=view&id=1osh8PHiSr3Z-E_b4s0qReTnLHEMoSuF2",
            "https://drive.google.com/uc?export=view&id=1oS2pjP568jHeGv-SmoVVJ0FK64uKVop_",
            "https://drive.google.com/uc?export=view&id=1RyYNGGG0gX7p12JLb8_TplATWM4ByUBi",
            "https://drive.google.com/uc?export=view&id=1f8QC9irQ01CJj2nSLYvV0kU_ZCdFHkgh",
            "https://drive.google.com/uc?export=view&id=1sSwnpnWwRq31nDsNdk0NvE1fjYvUH4L5",
            "https://drive.google.com/uc?export=view&id=1k2G9ScRBtUUQbM3htOikIFM3a-_XFFjc",
            "https://drive.google.com/uc?export=view&id=1cRkuNESKYCfSz3vQEllZU7_L99aw1kc1",
            "https://drive.google.com/uc?export=view&id=1YXzgsvWANv_ryN8ohZyPAb8G55NISaiy",
            "https://drive.google.com/uc?export=view&id=1QP3GjW8_9gOIo3k60MR50B9ElRgmshmu",
            "https://drive.google.com/uc?export=view&id=1nN8TdFrIqT__S4B4bAw9iTt0u6nqV3oa",
            "https://drive.google.com/uc?export=view&id=1P0hNmsDR8_j-phCI2M_UIc5y6_9rusod",
            "https://drive.google.com/uc?export=view&id=1jd9Rpi4f2RSoQM-iwCFEhtcm32of63P-",
            "https://drive.google.com/uc?export=view&id=1D615nY6p5-V3NfmgQ6C6aA19TtdHVWNI",
            "https://drive.google.com/uc?export=view&id=1oIk9EzPCEivlClKi1M6Dcn2yIsxADTDB",
            "https://drive.google.com/uc?export=view&id=1l0J21ciG2TylBMPP3C_djU97HEK2p2k8",
            "https://drive.google.com/uc?export=view&id=1O4iuLppBtj4vDo_kRt4w74lVOruR9BUa",
            "https://drive.google.com/uc?export=view&id=1Al9EGIce2y6W_PCJTb0KU7RDvtDh_k8K",
            "https://drive.google.com/uc?export=view&id=1pXvt4cLmNN-cXG1gj8wCsZSj97sBPd11",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450000",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "Keren banget Bang! Selalu tampil percaya diri dan bisa ngarahin tim dengan tenang tapi tegas",  
                "pesan":"Tetap jadi keren dan inspiratif ya bang!"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Korpsu",
                "hobbi": "Jalan-jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Selalu asik, seru, dan vibes-nya tuh positif banget",  
                "pesan":"Jangan lupa bahagia, semangat terus ngejalanin harinya kak"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main apapun",
                "sosmed": "@allyapasha_",
                "kesan": "Kakaknya keren, tegas, profesional, asik!",  
                "pesan":"Tetap jadi panutan yang asik, jangan berubah ya kak"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang Selatan",
                "alamat": "kontrakan GH",
                "hobbi": "Mainn Bola",
                "sosmed": "@ahmad.rizky",
                "kesan": "Asik, berwawasan luas, dan selalu punya cerita seru",  
                "pesan":"Terus jadi sosok keren yang inspiratif ya bang"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "Samping kost daffa",
                "hobbi": "Main Sudoku",
                "sosmed": "@arientakhsnl",
                "kesan": "Kak yang selalu baik dan perhatian",  
                "pesan":"Tetap jadi kakak baik yang menginspirasi"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jailin putri",
                "sosmed": "@daffahdynn_",
                "kesan": "abang yang tegas dan selalu profesional, tapi tetap hangat ",  
                "pesan":"Semoga selalu sukses dan tetap menjadi inspirasi bagi kami semua. "# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_nrp",
                "kesan": "abang yang selalu tampil keren dan penuh percaya diri",
                "pesan": "Terus pertahankan semangat dan sikap profesionalnya,bang"  # 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"pasar muara beliti",
                "alamat": "kost putri, gerbang barat samping sawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakak yang selalu memberikan dukungan",  
                "pesan":"Semoga kakak selalu diberi kesehatan dan kebahagiaan"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Urip",
                "alamat": "Belwis",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "abang yang keren bukan hanya dari penampilan, tapi juga sikap, jago ngoding",  
                "pesan":"Semoga perjalanan abang selalu lancar dan penuh keberhasilan."# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sigma fam",
                "hobbi": "ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "baik, asik, dan selalu ramah ke semua orang",  
                "pesan":"Semangat terus, Terus jadi abang yang hangat dan seru ya"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "maju jaya kost",
                "hobbi": "yapping sampe bete",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya asik diajak ngobrol apa aja",  
                "pesan":"Tetap menyenangkan kayak gini terus ya kak!"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Lari",
                "sosmed": "@sahid22_",
                "kesan": "Ramah, baik, dan lucunya paket lengkap!",  
                "pesan":"Semoga makin banyak orang baik di sekitar abang!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "nangka 4, sukarame",
                "hobbi": "Main game + kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya kalem tapi vibes-nya adem banget",  
                "pesan":"Tetap jadi sosok yang tenang semangat kuliahnya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": "Selama jadi adik bimbingan kakak, aku benar-benar merasa beruntung punya sosok mentor sebaik dan sepeduli kakak. Kakak selalu sabar membimbing, gak pernah marah meski kami sering lambat paham, dan selalu bisa bikin suasana jadi ringan dengan candaan lucu. Sikap perhatian dan kepedulian kakak bikin kami ngerasa dihargai dan nyaman.",  
                "pesan":"Semoga semua kebaikan dan ketulusan kakak dibalas dengan kebahagiaan dan kesuksesan yang berlipat"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya Baik, lembut, dan cantik luar dalam",  
                "pesan":"Semoga selalu bahagia dan bersinar di mana pun kakak berada!"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Kakaknya gak pernah jutek, selalu nyapa dengan senyum.",  
                "pesan":"Semoga senyum ramah kakak selalu jadi penyemangat banyak orang!"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jawa Barat",
                "alamat": "Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul9",
                "kesan": "Abangnya baik banget, selalu bikin suasana jadi seru!",  
                "pesan":"Tetap jadi abang paling lucu dan asik ya!"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Ramah, sabar, dan penjelasannya selalu mudah dipahami",  
                "pesan":"Makasih udah gak pernah capek bantu kami, bang!"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl.lapas raya no 55",
                "hobbi": "ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "Baik hati dan selalu nyapa dengan senyum tulus",  
                "pesan":"semangat kuliahnya, Tetap jadi sosok yang ceria kak"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Bikin project, ngoleksi data",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Keren parah, asiknya kebangetan",  
                "pesan":"Semoga abang selalu sukses dan tetap rendah hati!"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Padang Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "Kakaknya keren banget, cool tapi tetap humble",
                "pesan": "Semoga makin sukses dan tetap jadi panutan!"  # 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakaknya asik banget, diajak ngobrol selalu nyambung",  
                "pesan":"Tetap jadi sosok yang santai tapi berkesan ya kak!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Lempar Batu",
                "sosmed": "@m.ridwan_22",
                "kesan": "abangnya baik banget dan jago main badminton",  
                "pesan":"Tetap rendah hati meski smash-nya udah profesional ya bang!"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Mainn Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Keren, asik, dan punya vibes yang bikin nyaman bange",  
                "pesan":"Terus jadi abang panutan yang seru dan inspiratif ya!"# 1
            },
            {
                "nama": "Uliano Wiliam Purba ",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jln. Raden Saleh",
                "hobbi": "Main musik, ngoding, menanam anggrek",
                "sosmed": "@nano.wlm",
                "kesan": "abangnya baik banget dan keren dalam segala hal",  
                "pesan":"Semoga selalu bahagia dan makin keren tiap harinya bang!"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Bengong",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakaknya santai banget tapi tetap perhatian dan baik",  
                "pesan":"Terus jadi kakak yang bikin suasana adem ya kak!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1i3NvJ-iysgRCMHCsmMDv7gKTZdN_iSDf",
            "https://drive.google.com/uc?export=view&id=1ItmtAIN95fKpC3rM0Q6Q_xK1OyaIkhvX",
            "https://drive.google.com/uc?export=view&id=1yerXy2s7WbHOM0FEcDwzaGupOmh_DlDj",
            "https://drive.google.com/uc?export=view&id=1gGgPD8n7__6ElvgrH_0koVG1fJgCVmnB",
            "https://drive.google.com/uc?export=view&id=18yQpv2cFOYI9BZyOmrqqFCrTZkzHnbEX",
            "https://drive.google.com/uc?export=view&id=1PrJW8XGEi8xphRFYibcGoy7AEmrWNFBd",
            "https://drive.google.com/uc?export=view&id=1_7XJXNDKpoK-h533CWFz5E99QSdd358T",
            "https://drive.google.com/uc?export=view&id=1XLxFTA1v4TvrVOQ93HWnDjsiMWefZ1_Q",
            "https://drive.google.com/uc?export=view&id=11_PWbwOuIey5h2UmoGMmFXopYb974Lzi",
            "https://drive.google.com/uc?export=view&id=1ois7OvL9Sz-_11DEOdXufa1fmJovmKwL",
            "https://drive.google.com/uc?export=view&id=1QDd9DLx1gQpRquoi63Lc3m2TFEwSgS91",
            "https://drive.google.com/uc?export=view&id=1OQNGoC32oIJaSjGhLCBNwwCLvclWD9wD",
            "https://drive.google.com/uc?export=view&id=16JMoyrf_PhrDfmyaxaj1PRO3-28M7jAC",
            "https://drive.google.com/uc?export=view&id=1XzzGN30AibohFekWaHwD1w09i4m8YkT3",
            "https://drive.google.com/uc?export=view&id=1oBHKOZq8bHKhITlieFKl158xhCLUuDt5",
            "https://drive.google.com/uc?export=view&id=1ci3yN1K9EETGJXMhjdGFx74zluh_82sP",
            "https://drive.google.com/uc?export=view&id=1A_tGuDP-Eujt8UWqVcDRZnXVQhU7TVzM",
            "https://drive.google.com/uc?export=view&id=1kvVuO8dGqgCaAzMCkW0apBpw8r1DtW4b",
            "https://drive.google.com/uc?export=view&id=10F-6hbzEwGN-6OFDj-5TZgxtP2mPnNhq",
            "https://drive.google.com/uc?export=view&id=1Tf2IOV6Nzc1UIe3HXCR3eabHVVkXbJzb",
            "https://drive.google.com/uc?export=view&id=1w2xV7cpoO5JA37s0cGUP6r_MNWxHz1EO",
            "https://drive.google.com/uc?export=view&id=1m8YmjCoR4vzf4q6VPOCpXugFOFCvarkv",
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
                "kesan": "abangnya baik banget dan selalu nyapa dengan senyum manis",
                "pesan":"Tetap jadi sosok yang nyenengin dan positif ya bang!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@junitaa.0406",
                "kesan": "Kakaknya lucu banget, tapi tetep baik dan perhatian!",  
                "pesan":"Terus tebarkan kebaikan dan keramahan itu ya kak!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya baik banget dan selalu ramah ke semua orang",  
                "pesan":"Semangat terus kuliahnya, jaga kesehatan ya bang"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya selalu ramah, bikin siapa pun nyaman buat ngobrol",
                "pesan":"Tetap jadi kakak yang humble dan bisa bikin orang nyaman ya!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Abangnya selalu jelasin dengan sabar dan gampang dipahami banget!",
                "pesan":"Tetap jadi kakak yang sabar dan inspiratif kayak gini bang!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Abangnya keren banget, kalau ngejelasin tuh detail tapi gak ngebosenin",
                "pesan":"Semoga ilmunya makin luas dan bisa terus berbagi dengan semangat!" 
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tj. Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Abangnya baik banget dan selalu punya aura tenang yang bikin nyaman",
                "pesan":"Semoga ketenangan dan kebaikan abang selalu nular ke sekitarnya!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "jl. Manggis 1",
                "hobbi": "Nonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "Kakaknya gampang banget akrab sama siapa aja, sikap baiknya tulus banget",  
                "pesan":"Tetap jadi sosok positif yang nyebarin semangat di mana pun ya kak!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "jl. Nangka 3",
                "hobbi": "Main Bass, Piano, Semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya asik banget, selalu bisa bikin suasana jadi rame dan seru!",
                "pesan":"Jangan pernah berubah ya kak, vibe lucunya tuh nyenengin banget!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keylashafi_",
                "kesan": "Abangnya kalem banget, tapi selalu perhatian dan baik ke semua orang",
                "pesan":"Tetap jadi abang yang tenang dan bisa diandalkan ya"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Denger musik, dance, Ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Kakaknya baik banget dan selalu kelihatan tenang dalam segala situasi",
                "pesan":"Tetap jadi sosok yang sabar dan menenangkan ya kak!"    
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jl. Raden Saleh",
                "hobbi": "jalan-jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya selalu bawa vibes seru tapi tetap sopan dan perhatian",
                "pesan":"Semoga kakak selalu bahagia dan tetap sebaik ini terus!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan Bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "Kalem tapi tetap perhatian, kebaikan kakak selalu kerasa dari sikapnya",  
                "pesan":"Terus jadi kakak yang menenangkan dan rendah hati ya!"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Kakaknya selalu nyambut siapa pun dengan senyum, ramah banget!",
                "pesan":"Tetap jadi pribadi yang hangat dan menyenangkan ya kak!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama ITERA TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Kakaknya gampang banget bikin suasana cair",
                "pesan":"Terus jadi kakak yang nyebarin semangat lewat tawa"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Coding udah kayak bahasa sehari-hari buat abang, hebat banget!",
                "pesan":"Terus berbagi ilmu dan tetap rendah hati ya bang, panutan banget!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin orang, dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Asik, seru, dan selalu bisa bikin suasana jadi hidup",
                "pesan":"Jangan berubah ya kak, dunia butuh orang se-humble ini!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "jalan-jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Abangnya keren banget, tiap nongol suasana langsung rame!",
                "pesan":"Tetap jadi pribadi yang seru dan nyebarin vibes positif terus ya bang!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur & main geometry dash",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya pinter banget tapi tetap rendah hati, senyumnya selalu bikin nyaman",
                "pesan":"Semoga abang selalu sukses dan tetap jadi panutan yang rendah hati!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakaknya sabar, baik, dan selalu siap bantu kalau ada yang belum paham",
                "pesan":"Jangan lupa istirahat kak!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya sopan, ramah, dan gak pernah ngebeda-bedain orang",  
                "pesan":"Terus pertahankan sikap rendah hatinya kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "abangnya Baiknya tulus, asiknya natural bener-bener paket lengkap",
                "pesan":"Terus tebarkan energi positif ya bang"
            }
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()
       

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Khjf8TiQgPXpxKV0UhKAT1IubruJBitE",
            "https://drive.google.com/uc?export=view&id=1ZXQxCaw1TNDyUJVZSd8c5lvBGCxNfnjx",
            "https://drive.google.com/uc?export=view&id=1hMprcznUPtGlIU4Yxn7MA9J4Qo5uU1Nl",
            "https://drive.google.com/uc?export=view&id=1GrwI6jWa6lLkfPNzTatUhSmXIgaysG6k",
            "https://drive.google.com/uc?export=view&id=12bKVaH0TqY92Qv9X7ub43fOY5keLvTwA",
            "https://drive.google.com/uc?export=view&id=1YqO9NjzGZetRuOIya7Jca1px0c2YyZzo",
            "https://drive.google.com/uc?export=view&id=1AAa84d-XXVKdkMsW7rMHo3NgpvXRnS65",
            "https://drive.google.com/uc?export=view&id=16WVKg4C6ajXyf-z6Y6tHvDmlr4Xqz4sW",
            "https://drive.google.com/uc?export=view&id=1cXyNsHWM-fdV0EFsEZfby4wGHh9FnPfq",
            "https://drive.google.com/uc?export=view&id=12vtuAclgNp6IDnzsVyreh8v2o_KZ-AFd",
            "https://drive.google.com/uc?export=view&id=1X_5EjTuOMQerONPdXK2u97GaIb51nYAt",
            "https://drive.google.com/uc?export=view&id=1TpqLvgEic7FJeE9yVUP_pqMgxaWwMtdD",
            "https://drive.google.com/uc?export=view&id=1uFf9UmtNdvBK5WCiVdBrskwQOnpmcR4j",
            "https://drive.google.com/uc?export=view&id=18bbut9Y9q3aux5DACqIZL2vtii9t-xTS",
            "https://drive.google.com/uc?export=view&id=11DLVZebGPq-t3SMklTWkEMk5RKtAm6kX",
            "https://drive.google.com/uc?export=view&id=1eUS1GOjQusFbATtM3K-KLkdWV2cfo5IH",
            "https://drive.google.com/uc?export=view&id=1hDnXYF4cQnOnurr5LqjVHgtnbMa4zLjv",
            "https://drive.google.com/uc?export=view&id=1zz0voOt8X2givRpccqNMvvNLmaf8Q56P",
            "https://drive.google.com/uc?export=view&id=1_ZUvG3vmvR1ix-A871MScyDVL-dnX1mC",
            "https://drive.google.com/uc?export=view&id=1ON_V0cJrkgqliGv6XDbFL-UAPuEHoYJa",
            "https://drive.google.com/uc?export=view&id=1F89fa3QRkStx7keYlbifLAUwS7cFUl8_",
            "https://drive.google.com/uc?export=view&id=1JZGp2MP4TBiQVWc0bNFGrkDd1LQhi52l",
            "https://drive.google.com/uc?export=view&id=1ITa3ZZ5or6MzjgjZ1bx-F-AydMg5MykQ",
            "https://drive.google.com/uc?export=view&id=13f4qFkW8sd8ND946x06ZqReE_seGyajN",
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "Abangnya baik banget, asiknya kebangetan, gampang bikin orang nyaman",
                "pesan":"Tetap jadi pribadi yang nyenengin dan bikin suasana selalu rame ya bang!"# 1
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Asik, baik, dan serunya gak ada obat",
                "pesan":"Terus jadi pribadi yang bikin suasana rame terus ya!"# 1
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Baik, seru, dan selalu bisa bikin suasana cair",
                "pesan":"Terus jadi kakak yang nyebarin tawa di mana pun berada!"# 1
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya asik, rame, tapi tetep perhatian",
                "pesan":"Terus nyebarin kehangatan dan keceriaanmu ya kak!"# 1
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya seru dan enak banget diajak ngobrol",
                "pesan":"Terus jadi abang yang asik dan gak pernah bosenin!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakaknya seru, kocak, tapi tetap sopan dan ngasih contoh baik",
                "pesan":"Jangan berubah ya kak, keasikanmu tuh berharga banget!r"# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Baik banget, serunya natural, dan gampang akrab sama siapa aja",
                "pesan":"Tetap jadi pribadi yang bikin orang lain nyaman kak!"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya ramah banget, tiap ngobrol selalu nyenengin!",
                "pesan":"Terus jadi pribadi yang hangat dan bikin orang lain nyaman ya kak"# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Abangnya asik, seru, dan gampang akrab sama siapa aja",
                "pesan":"Jangan pernah berubah ya bang, vibe-nya keren banget!"# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan mudah bergaul",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya kak"# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya seru tapi tetap sopan, kombinasi yang langka",
                "pesan":"Tetap jadi inspirasi dan panutan buat yang lain ya kak!"# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya baik banget dan selalu ngertiin orang lain",
                "pesan":"Terus jadi orang baik ya kak, dunia butuh lebih banyak orang kayak kak!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Abangnya gokil, seru, asik, penjelasannya mudah dimengerti",
                "pesan":"Semoga abang selalu bahagia dan terus nyebarin energi positif!"# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakaknya humble dan enak banget diajak cerita",
                "pesan":"Jangan pernah kehilangan sisi ramah dan rendah hatimu ya kak!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Asik, seru, dan selalu bikin suasana jadi hidup",
                "pesan":"Tetap jadi sumber tawa dan semangat buat semua orang ya!"# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya chill banget, tapi tetep perhatian",
                "pesan":"Terus jadi abang yang santai tapi selalu bisa diandalkan ya!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Abangnya baik banget, sabar, dan gampang akrab",
                "pesan":"Terus jadi orang yang nyenengin dan gak berubah ya bang!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya seru banget, tiap ketemu selalu bikin happy",
                "pesan":"Tetap asik dan ceria terus ya kak, biar suasana gak pernah sepi!"# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Baik, seru, dan selalu bisa bikin orang lain senyum",
                "pesan":"Semoga kebaikan kakak selalu dibalas yang lebih besar lagi!"# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya asik, ramah, dan gak pernah pelit senyum",
                "pesan":"Terus jadi pribadi yang ringan tangan dan ceria ya kak!"# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya kalem tapi asik, vibes-nya adem banget",
                "pesan":"Tetap rendah hati dan terus nyebarin ketenangan itu ya kak!"# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya baik, lucu, dan gampang bikin ketawa",
                "pesan":"Jangan pernah kehilangan sisi lucumu ya kak, itu yang bikin seru!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya seru dan punya cara sendiri buat bikin nyaman orang lain",
                "pesan":"Jangan berubah ya bang, tetap jadi abang yang keren dan nyenengin"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kakaknya penyabar banget, selalu ngasih contoh positif",
                "pesan":"Semoga kebaikan kakak selalu dibalas kebahagiaan yang besar!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K02BtC4YV9tPGrY5CSsJUcDIWExnks4v",
            "https://drive.google.com/uc?export=view&id=1JJKDIepMQYAyjObhJvZ--4KRYqvVX7li",
            "https://drive.google.com/uc?export=view&id=1njF2fS869UOtP6bEc648CFzqNxH1nF0n",
            "https://drive.google.com/uc?export=view&id=1h-pSmYdqrttFds_71EjsPLK41_JJPSC1",
            "https://drive.google.com/uc?export=view&id=10V3zFRwVmF_n1KErJ-JQtEAYBhqGfA7N",
            "https://drive.google.com/uc?export=view&id=14WPxyZhLNPUE-W9pR9lbGYSqfnIPCfPr",
            "https://drive.google.com/uc?export=view&id=1-7FaFnmt9wRhaSKPGO47keoO56Ix-H1o",
            "https://drive.google.com/uc?export=view&id=1AUtPoIHgHxBsesNesFap63Kv7wck4O70",
            "https://drive.google.com/uc?export=view&id=1pHUX9U5T3up1VCrdJMh74M2_tT16MDK9",
            "https://drive.google.com/uc?export=view&id=13e72huX0SHaar8wttZoYOami_0k0nvZ7",
            "https://drive.google.com/uc?export=view&id=1maMPtE2dHDUzODvcqi5o2fKmD7CVYqUa",
            "https://drive.google.com/uc?export=view&id=1riAbnLi-VsDedeyTS6QhVhoV97bY9kmz",
            "https://drive.google.com/uc?export=view&id=12PRo4yOp_AmruGquotXnBvgk8YTlAlr5",
            "https://drive.google.com/uc?export=view&id=1njF2fS869UOtP6bEc648CFzqNxH1nF0n",
            "https://drive.google.com/uc?export=view&id=1NJTa-g3kHqdemSoqLzxEWvMxqfHOOC8q",
            
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik dan perhatian, bikin suasana selalu hangat",
                "pesan": "Semoga kebaikan kakak selalu dibalas yang lebih besar lagi!"# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya murah senyum, bikin orang lain nyaman banget",
                "pesan": "Tetap ceria terus ya kak, senyum kakak tuh nular banget!"# 1
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya easy going banget, gampang nyatu sama siapa aja",
                "pesan": "Terus jadi pribadi yang terbuka dan nyenengin ya kak!"# 1
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya lembut tapi juga lucu, kombinasi yang pas banget",
                "pesan": "Jangan berubah ya kak, tetap jadi pribadi yang bikin nyaman!"# 1
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya asik banget, vibes-nya tuh selalu positi",
                "pesan": "Tetap semangat ya bang, aura serunya jangan pernah padam!"# 1
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya lembut tapi juga lucu, kombinasi yang pas banget",
                "pesan": "Jangan berubah ya kak, tetap jadi pribadi yang bikin nyaman!"# 1
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakaknya sabar banget, kalau ngejelasin tuh pelan tapi jelas",
                "pesan": "Makasih udah mau bantuin terus ya kak, semoga makin sukses!"# 1
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "124450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalghani73",
                "kesan": "Abangnya seru, lucu, dan selalu punya ide random tapi keren",  
                "pesan":"Terus jadi abang kreatif yang gak pernah kehabisan akal!!!!"# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kakaknya manis dan selalu bawa suasana adem",
                "pesan": ": Tetap jadi sosok yang lembut dan bikin tenang ya kak!"# 1
            },
             {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya tegas tapi asik, jadi kombinasi yang keren bangetAb",
                "pesan": "Tetap jadi sosok yang berwibawa tapi tetap ramah ya bang!"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya perhatian, baik, dan gampang bikin orang nyaman",  
                "pesan":"Jangan berubah ya kak, tetap jadi abang panutan!"# 1
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Abangnya lucu, asik, tapi juga bisa serius kalau dibutuhin.",
                "pesan": "Tetap jadi abang yang seimbang antara bercanda dan bijak ya!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Abangnya pinter, humble, dan asik banget diajak diskusi",
                "pesan": "Terus berbagi ilmu ya bang, gaya jelasin abang keren banget!"# 1
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya enerjik banget, gak pernah keliatan capek.",
                "pesan": "Semoga semangatnya gak pernah padam ya kak!."# 1
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Rubik Mirror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakaknya perhatian banget, selalu inget hal-hal kecil",  
                "pesan":"Terus jadi pribadi yang tulus dan penuh empati ya kak!"# 1
            },
           
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FGXdIhsyUKGXCMscZ9V0JrLHTJt43F44",
            "https://drive.google.com/uc?export=view&id=1WF2X2zgNXsIV0Ljdb-wE_taBSOb4I76x",
            "https://drive.google.com/uc?export=view&id=1kK6uj0Hui3gtx9uYxpFUvUcr3cYI0pxW",
            "https://drive.google.com/uc?export=view&id=10xVTp6OO-8LmxXV19ubN88JKN_RlnlxM",
            "https://drive.google.com/uc?export=view&id=1szhJgllzgrn5BjY_Jc45A58MA-K-r5uE",
            "https://drive.google.com/uc?export=view&id=1CgCnHwHc3eDjDg8VE-eisZ6WFgZwr3_N",
            "https://drive.google.com/uc?export=view&id=1n72U0ikcuBTejt9EA1hAVVGWmRn3Kly6",
            "https://drive.google.com/uc?export=view&id=1aLFmsINgZusggvdnxJac5eWpaPHBymdT",
            "https://drive.google.com/uc?export=view&id=1XF9eh_IxwNoiSTg7qrzWbzA7DA76tDmT",
            "https://drive.google.com/uc?export=view&id=1XdcbsvxyvvAVr8rv1LF24sGrhK-FEhXc",
            "https://drive.google.com/uc?export=view&id=1-uFJoOffSQ_3MTr10BI6xH0nWVMEJn1c",
            
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
                "kesan": "Abangnya asik banget, gak pernah ngebosenin kalau diajak ngobrol",
                "pesan": "Terus jadi abang yang seru dan selalu bikin suasana hidup ya!"# 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya baik, sabar, dan selalu bantu tanpa diminta",
                "pesan": "Semoga kebaikan kakak dibalas dengan kebahagiaan yang banyak!!"# 1
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "@den_iki__",
                "kesan": "Abangnya humble banget, gak jaim sama sekali",
                "pesan": "Tetap jadi abang yang santai tapi tetap keren ya bang!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya seru banget, selalu punya cara bikin orang lain ketawa",
                "pesan": "Terus nyebarin energi positifmu ya kak, bikin hari makin cerah!"# 1
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "Kakaknya lembut, sopan, tapi tetep rame pas bareng-bareng",
                "pesan": "Terus jadi kakak yang bisa bikin suasana tenang tapi hangat ya!."# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "Kakaknya selalu punya aura positif yang bikin nyaman",
                "pesan": "Semoga semangat baiknya gak pernah padam ya kak!!"# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya lucu tapi tetep sopan, kombinasi langka banget",
                "pesan": "Tetap jadi abang yang nyenengin dan berwibawa ya!"# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "Kakaknya peka banget sama sekitar, care parah",
                "pesan": "Terus jaga sifat perhatianmu ya kak, itu yang paling berharga!"# 1
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Kakaknya seru, suka ngajak ngobrol, dan gak pernah ngebosenin",
                "pesan": "Terus tebarkan energi positifmu ya kak"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya punya gaya ngomong yang tenang tapi ngena",
                "pesan": "Jangan berubah ya kak, auranya adem banget!"# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "Kakaknya murah senyum, bikin semua orang nyamann",
                "pesan": "Terus nyebarin senyum positifmu ke sekitar ya kak!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RWmIofXeprGQaMdil5JeC6r7rc0-afAB",
            "https://drive.google.com/uc?export=view&id=1raPfGIMK246uK4VamZaUD9ZeIkMr1AZA",
            "https://drive.google.com/uc?export=view&id=1y7Id-V0I1TnU5cj9EBAjIpgL0O34lNCc",
            "https://drive.google.com/uc?export=view&id=14fit6vz1SpjqpU1r1LXJOJi1wmx50a0w",
            "https://drive.google.com/uc?export=view&id=13y0XHEBOUqjUwsABb0LdJ7jRiHbPgEot",
            "https://drive.google.com/uc?export=view&id=1XGtvoxewLTb5tlfkSTrw3wdM1Vm-j9sf",
            "https://drive.google.com/uc?export=view&id=1Tetr5Eo4CD_tDHYGJC04jm1ixltoyX_l",
            "https://drive.google.com/uc?export=view&id=1Zb7U8kP4Dc5gDTIyEy2v4sWl4Ffe0NQ0",
            "https://drive.google.com/uc?export=view&id=1sNGm4ehkPkDvS5UWk7d63VXHEKGMkUgN",
            "https://drive.google.com/uc?export=view&id=1FsJQwIIDM5TIummMeR5nUPQv4O61EFim",
            "https://drive.google.com/uc?export=view&id=1s3eOrCAgJ8VCf5_WAVR-k34Y9f7beka7",
            "https://drive.google.com/uc?export=view&id=14q910ebnBJQ6C7eAGwTNN9w5rTPf_F1b",
            "https://drive.google.com/uc?export=view&id=1TqWd-LI8ifYWbJAm3yQWbGcDsgA6DWIo",
            "https://drive.google.com/uc?export=view&id=1SQ9MkuVH48vryeexm-g8dCAAMqjhAWku",
            "https://drive.google.com/uc?export=view&id=1EjLILvf-WgzvO1pROEgXQujtWHh-3_ec",
            "https://drive.google.com/uc?export=view&id=1E9ZeMuYTT-CD1hy-tfSDTzMyN76fKbbT",
            "https://drive.google.com/uc?export=view&id=1V8h-uQ7Bqe-I429b3BA0y56UE_9eu7Eb",
            "https://drive.google.com/uc?export=view&id=1HzP8R0M77X5WJQJqslRqd2FZc_rvbEuh",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya asik, seru, lucu, tapi juga perhatian",
                "pesan": "tetap jadi kakak yang ceria dan peduli kayak sekarang ya kak!"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Kakaknya lembut tapi tetap tegas kalau dibutuhkan",
                "pesan": "Semoga terus bisa jadi contoh yang baik buat semua!"# 1
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Abangnya enak diajak ngobrol, nyambung ke mana aja",
                "pesan": "Terus jadi abang yang easy going dan nyenengin ya!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Abangnya gokil tapi kalau serius juga keren banget",
                "pesan": "Tetap seimbang ya bang, biar tetap jadi panutan seru!"# 1
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Abangnya seru, suka bercanda tapi tetap sopan",
                "pesan": "Terus jaga vibe seru itu bang, semua jadi betah!"# 1
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Kakaknya sabar, baik, dan selalu ngajarin dengan telaten",
                "pesan": "Terima kasih udah mau bantuin tanpa ngeluh ya kak!"# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya tenang, santai, tapi selalu ngasih kesan hangat",
                "pesan": "Tetap jadi pribadi yang menenangkan dan positif ya kak!"# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Kakaknya baik, selalu nyapa duluan, super ramah",
                "pesan": "Terus tebarkan keramahanmu ya kak, itu keren banget!"# 1
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Kakaknya perhatian, gak segan bantu orang lain",
                "pesan": "Semoga semua kebaikan kakak dibalas yang lebih besar lagi"# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya punya aura ceria yang bikin suasana adem",
                "pesan": "Semoga kakak terus bahagia dan menebar kebaikan di mana pun!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya selalu bikin suasana jadi tenang tapi gak pernah ngebosenin",
                "pesan": "Terus pertahankan sisi kalemnya itu ya kak, nyaman banget!"# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya berwibawa tapi tetep gampang diajak becanda",
                "pesan": "Keren banget kak, semoga selalu rendah hati!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya suka bantu orang lain, engga sombom, dan ramah banget",
                "pesan": "Semoga kebaikan kakak dibalas berkali lipat ya"# 1
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Abangnya lucu tapi kalau ngomong selalu ada maknanya",
                "pesan": "Tetap jadi abang yang bijak tapi santai ya bang!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya ceria terus, vibes-nya tuh positif banget",
                "pesan": "Terus tebarkan energi ceria itu ke semua orang ya!"# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakaknya penyabar banget, bahkan di situasi ribet pun tetap tenang",
                "pesan": "Terima kasih udah selalu sabar dan jadi panutan ya kak!."# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya punya gaya ngomong yang lembut tapi berkesan",
                "pesan": "Semangat kuliahnya, jangn lupa istirahat ya kak"# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya selalu punya senyum tulus yang bikin tenang",
                "pesan": "Jangan lupa jaga diri dan tetap ceria ya kak!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
# Tambahkan menu lainnya sesuai kebutuhan


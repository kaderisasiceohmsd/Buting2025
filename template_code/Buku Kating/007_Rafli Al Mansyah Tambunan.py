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
            "https://drive.google.com/uc?export=view&id=1yZ9aYijqWMVbnI954FEQDWPcyiLw-ipd",
            "https://drive.google.com/uc?export=view&id=1eUy88M8d2fSIRR533GTFkugkfKpc2W6g",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "abangnya punya referensi yang banyak dan seru diajak ngobrol",  
                "pesan":"semangat terus bang" # 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "baca buku dasar dasar sql",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abangnya asik, banyak hal yang relate juga",  
                "pesan":"semangat terus bangg!!!"
            },
            {
                "nama": "Kakak CCc",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pDgvJzfBbScLJ2caJKuXnMVC-O6M-Bmw",
            "https://drive.google.com/uc?export=view&id=1f4F0mzAsHOpxueLXUU8DfS3rAsYotwdN",
            "https://drive.google.com/uc?export=view&id=14MVjnyAc238OfxAvaoAaSNSByljlrnLA",
            "https://drive.google.com/uc?export=view&id=1ActJPLQAEvsukaaDww03eQb8OaOjIuGs",
            "https://drive.google.com/uc?export=view&id=1BlKYDKZdQoY8ZJZQ-aPTKskvKmHi5SKJ",
            "https://drive.google.com/uc?export=view&id=1cpbpGkeexlhHugcrt8WBJj1e138t_Dkx",
            "https://drive.google.com/uc?export=view&id=1UFcr0rw47Pn-8jlVq8uybZhIq4DFUsQR",
            "https://drive.google.com/uc?export=view&id=1jEZb31lcDwPuFe-Z7NmaUxm_S9x4XkWH",
            "https://drive.google.com/uc?export=view&id=1XKvgTMzk8a3VzPNXnmzSqrqE8iiR0uFO",
            "https://drive.google.com/uc?export=view&id=1pzljJSFLgfioLHaepkdCZ1vJuRtv4Vm3",
            "https://drive.google.com/uc?export=view&id=1Fx-D-_OKBdZo7R-33AAUAAEchHy5pdK1",
            "https://drive.google.com/uc?export=view&id=1qVAkFlxbxCzkMl080wlcslrZUgQBfQ03",
            "https://drive.google.com/uc?export=view&id=17uazMsFhy4nzkev7E7_jsG-56uyKyLW-",
            "https://drive.google.com/uc?export=view&id=149KJ_6fXwYGXCdRjybnU8xWCe1JM5Cbs",
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
                "kesan": "Kakaknya keren dan humble banget",  
                "pesan":"Semoga makin sukses dan terus jadi inspirasi buat kami!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto, Jawa Timur",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "Ramah tapi juga tegas, panutan banget",  
                "pesan":"Jangan bosen ngasih arahan ke adek-adek ya kak!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakak tampak tenang dan bijak dalam bersikap.",  
                "pesan":"Semoga bisa mengenal kakak lebih dekat lagi ke depannya."
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Muara Enim, Sumatera Selatan",
                "alamat": "C2",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak orangnya santai tapi tetap terarah dalam bersikap.",  
                "pesan":"Semoga kakak selalu sukses dan terus menginspirasi."
            },
            {
                "nama": "Dharu Cahyo Aji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Bengong",
                "sosmed": "@dhruchyo",
                "kesan": "Kakak punya kepribadian yang menarik dan sopan.",  
                "pesan":"Semoga ke depannya bisa lebih banyak mengenal kakak."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Menggodai Abang Cimol",
                "sosmed": "@fby.wlndr",
                "kesan": "Walau baru kenal sebentar, kakak terlihat positif dan inspiratif.",  
                "pesan":"Terima kasih sudah memberi kesan baik sejak awal."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@givarooo",
                "kesan": "Dari pertemuan singkat saja sudah terlihat kalau kakak punya semangat positif.",  
                "pesan":"Semoga semangat itu bisa terus kakak jaga dan sebarkan"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Kaknya berwibawa tapi tetap asik",  
                "pesan":"Semoga sukses selalu dan tetap rendah hati!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Mengukir sabun",
                "sosmed": "@berlyyyanda",
                "kesan": "Kakaknya nggak banyak bicara tapi kerjanya nyata",  
                "pesan":"Teruslah jadi contoh buat kami yang baru belajar!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Kalimantan Utara",
                "alamat": "Belwis",
                "hobbi": "Sibuk",
                "sosmed": "@j__eesia",
                "kesan": "Kakaknya calm banget walau suasana chaos",  
                "pesan":"Semoga selalu tenang dan sabar hadapi dunia perkuliahan"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Gang Sakung",
                "hobbi": "Main  Padel",
                "sosmed": "@ianridhomanik",
                "kesan": "Kaknya produktif parah, panutan banget",  
                "pesan":"Semoga semua project-nya lancar terus kak!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal": "Bangka Belitung",
                "alamat": "Kobam",
                "hobbi": "Nongkrong di gedung f",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak tingkat adalah sosok yang berwibawa dan bisa diandalkan.",  
                "pesan":"Semoga setiap langkah kakak selalu dipenuhi keberhasilan dan kebahagiaan."
            },
            {
                "nama": "Monika Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Ketapang, Kalimantan Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monca_tjg",
                "kesan": "Ramah tapi juga tegas, panutan banget",  
                "pesan":"Jangan bosen ngasih arahan ke adek-adek ya kak!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pekan Baru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak pendiam tapi kalau ngomong dalem banget",  
                "pesan":"Terus jadi sosok inspiratif ya kak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FiQIR3pg96juNGlLZu8QZethb5MfYX5-",
            "https://drive.google.com/uc?export=view&id=16bh12DpL1Z-tg9i6Re5ow4o-zGXXVtFv",
            "https://drive.google.com/uc?export=view&id=1q8PZi78tXKOiSdw-n4X2UMPxF1fbqkgZ",
            "https://drive.google.com/uc?export=view&id=1jm7vy_UKK2h1p7DZyw-tHLCqmosXqPqA",
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
                "kesan": "abangnya asik,humble, suka perunggu juga yoai",  
                "pesan":"tetep humble bang!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "kakaknya baik, lucu, imup",  
                "pesan":"tetep humble kak!"# 1
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakaknya asik seru",  
                "pesan":"Semoga selalu tenang dan sabar hadapi dunia perkuliahan"
            },
            {
                "nama": "Lia Hana Ichisassmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Kaknya inspiratif banget, bikin pengen berkembang terus!",  
                "pesan":"Terima kasih udah jadi role model yang luar biasa kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA" :
    def departemen_psda():
        gambar_urls =  [
            "https://drive.google.com/uc?export=view&id=1mUyj1gVgF68qlX7ImVk4Qk0wucv6_8YK",
            "https://drive.google.com/uc?export=view&id=1lcniBmHA_72QEN_tpmafdAlIZN9OKIKj",
            "https://drive.google.com/uc?export=view&id=1XNB3SbimRcojHGrS-59MppeO8ni9BpIG",
            "https://drive.google.com/uc?export=view&id=1AYTq_RoGFIfaZ7P05h1D41Vkom11e02M",
            "https://drive.google.com/uc?export=view&id=114giUP8mdDqICr2IrQAJ6LkR-0CtUk33",
            "https://drive.google.com/uc?export=view&id=14loJ2LgYWD6TV1UOWqXYdhB5ioeG18d1",
            "https://drive.google.com/uc?export=view&id=1CsyxIUX10otErgdyC47ZnGP5P-RF_thS",
            "https://drive.google.com/uc?export=view&id=1vhL_HivFUAkVpxil1TkRTcY6XDAIch7y",
            "https://drive.google.com/uc?export=view&id=1zDwgUEhnWpBpQMw09MiNUOwP0BxQDuKi",
            "https://drive.google.com/uc?export=view&id=18XNpsKg5Tn3bE5mCbATHUmsHL6t19Wgi",
            "https://drive.google.com/uc?export=view&id=1zMu29e5gDORY2XbNOIk5TDv8CW0-fTJE",
            "https://drive.google.com/uc?export=view&id=1nyA-ijca5JU2ci_LfSEi6h31-0MdY0jM",
            "https://drive.google.com/uc?export=view&id=1BnKXAj2wICUcE5PRYWK2PiG2JTO4cAyF",
            "https://drive.google.com/uc?export=view&id=1hi1W-tZva2-TmstbwF_-7FgQnilMeoVd",
            "https://drive.google.com/uc?export=view&id=1rzAhPLMGVEqixJWbxNHxuO6Jm7xo_rAS",
            "https://drive.google.com/uc?export=view&id=1AtBS6GCPQOgd-0oAGoBMq0touc0948eF",
            "https://drive.google.com/uc?export=view&id=1S7id49lOfnxfDLzMiLt_dspMIsjaZUDk",
            "https://drive.google.com/uc?export=view&id=1OOxto08JLUc9MR8qkGO1AghVIk7_9_W-",
            "https://drive.google.com/uc?export=view&id=1M2jAAHZT--FlHTk6At4tRbBc8t084NXX",
            "https://drive.google.com/uc?export=view&id=1ay7ECqp6iLBT5y4jNB9T3x574pdj-xbi",
            "https://drive.google.com/uc?export=view&id=1mtHXvUe9tSTlprxaVF588RupzM5URRWE",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1QSgeT8O_faNqXdbwK7RFCC_xlK9DByjo",
            "https://drive.google.com/uc?export=view&id=1dkh6O2sYCpSPeqKdIG0DjAh14j0lvDYb",
            "https://drive.google.com/uc?export=view&id=11HEs-q_A5VtvlYtLPEcpo693u107Nlbk",
            "https://drive.google.com/uc?export=view&id=1Ltfl7aka3Y0KKXPPtoHQGXhwzzbPIdpG",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ferdy_kevin",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@afifahhnsrn",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "123450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira",
                "hobbi": "Main",
                "sosmed": "@alyapasha_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ahmad.rizky___",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "sebelah  kos bang dapa",
                "hobbi": "Liatin Haikal",
                "sosmed": "@arientakhsnl_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "sebelah kos kak arin",
                "hobbi": "Isengin Fislam",
                "sosmed": "@daffahdynn_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Cikarang",
                "alamat": "Sama kek bang ahmad",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Gg. Perwira",
                "hobbi": "Ngakader",
                "sosmed": "@berlyyyanda",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450022",
                "umur": "-",
                "asal": "Sumatra Barat",
                "alamat": "-",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@vany.salsabilaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@sahid22",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ali_parisi3",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Waydadi",
                "hobbi": "Tidur",
                "sosmed": "@verazkaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
                        {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@risma.mustika_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "-",
                "sosmed": "@ahmadnaufa_ll",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Makan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Makan Beling",
                "sosmed": "@kevinaj__",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450023",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Main Badminton",
                "sosmed": "@m.ridwan_22",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Berenang, ngoleksi figura & kartu anime",
                "sosmed": "@rewinanaaa",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Uliano Wiliam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Main piano, nanem anggrek, ngoding dan nyari kesalahan anak 24",
                "sosmed": "@ilano",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()



# Tambahkan menu lainnya sesuai kebutuhan

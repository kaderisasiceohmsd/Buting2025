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
            "https://drive.google.com/uc?export=view&id=1yZ9aYijqWMVbnI954FEQDWPcyiLw-ipd",
            "https://drive.google.com/uc?export=view&id=1eUy88M8d2fSIRR533GTFkugkfKpc2W6g",
            "https://drive.google.com/uc?export=view&id=1nOqU7LpQj2drVy-WP7n7p8dcHhHQ20TA",
            "https://drive.google.com/uc?export=view&id=1D4fNWSRCTFWmtKMeH2Owwd-muZx7oaCO",
            "https://drive.google.com/uc?export=view&id=1zUJjKF41iR5DZ7M11E1gsHnRIbeSxjUf",
            "https://drive.google.com/uc?export=view&id=1M0tA_VuVm1SQ9G1YW10e1Dioo9c4urOW",
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
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram Shopee",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya seru dan kelihatan attractive gampang senyum",  
                "pesan":"semangat terus kak, tetap humble!!"
            },
            {
                "nama": "Syadza Puspandari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "ramah dan mudah senyum",  
                "pesan":"semangatt kakk, jangan lupa makan!!"
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku saku pramuka",
                "sosmed": "@ekshantyfebriana",
                "kesan": "kakaknya menginspirasi pengen jadi pemandu",  
                "pesan":"semangat terus ya kakk!!"
            } ,
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Kota Padang, Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakaknya ramah dan kelihatan suka tidur",  
                "pesan":"semangat terus kak!!semoga punya banyak waktu buat tidur"
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
                "kesan": "Kakaknya produktif parah, panutan banget",  
                "pesan":"Semoga semua project-nya lancar terus kak!"
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
                "pesan":"Jangan bosen ngasih arahan ke adek-adek ya kak!"
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
                "pesan":"Terus jadi sosok inspiratif ya kak!"
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
                "pesan":"tetep humble bang!"
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
                "pesan":"tetep humble kak, jangan lupa sama gweedy!"
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
            "https://drive.google.com/uc?export=view&id=1wQ_uX77vUUhQgqVLOTYexlbl_HqnU9pV",
            "https://drive.google.com/uc?export=view&id=1QSgeT8O_faNqXdbwK7RFCC_xlK9DByjo",
            "https://drive.google.com/uc?export=view&id=1dkh6O2sYCpSPeqKdIG0DjAh14j0lvDYb",
            "https://drive.google.com/uc?export=view&id=11HEs-q_A5VtvlYtLPEcpo693u107Nlbk",
            "https://drive.google.com/uc?export=view&id=1Ltfl7aka3Y0KKXPPtoHQGXhwzzbPIdpG",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya kelihatan seru dan memang baik",  
                "pesan":"semangat terus bang jadi kadep, jangan capek sama kami angkatan 24"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya ramah baik ",
                "pesan": "Semoga kami bisa meneladani semangat kakak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Sikap kakaknya tegas dan professional, keren!.",
                "pesan": "Terima kasih atas bimbingannya, semoga kakak sehat selalu."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "abangnya punya wawasan dan punya rasa berkebangsaan yang tinggi, keren! ",
                "pesan": "Semangat terus capresma!"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "sebelah  kos bang dapa",
                "hobbi": "Liatin Haikal",
                "sosmed": "@arientakhsnl_",
                "kesan": "punya tingkat kepedulian yang tinggi dan attractive",  
                "pesan":"semangat terus ya kak!!"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "sebelah kos kak arin",
                "hobbi": "Isengin Fislam",
                "sosmed": "@daffahdynn_",
                "kesan": "terlihat punya semangat berorganisasi yang tinggi",  
                "pesan":"semangat terus bang!"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "abangnya baik dan perhatian kepada orang lain",
                "pesan": "semangat terus bang!!!"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Sikapnya tegas dan disiplin, menjadi panutan bagi kami.",
                "pesan": "Terima kasih atas ilmunya, semoga kakak sehat selalu."
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Gg. Perwira",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "abangnya tegas berwibawa, keren!!",  
                "pesan":"semangatt terus bang!!"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450022",
                "umur": "-",
                "asal": "Sumatra Barat",
                "alamat": "-",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "abangnya punya semangat berorganisasi",  
                "pesan":"semangatt terus bang!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak sangat berwibawa dan mengayomi.",
                "pesan": "Mohon bimbingannya selalu, Kak. Sehat dan sukses terus!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@sahid22",
                "kesan": "abangnya cool",  
                "pesan":"semangatt terus bang!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal":"Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "kakaknya ramah",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "kakaknya seru diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "abangnya punya ketertarikan lebih terhadap musik",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "kakaknya keren",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "kakaknya punya passion terhadap tari, keren",  
                "pesan":"semangat terus kakak"# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "abangnya sabar kalau ngajar asprak",  
                "pesan":"semangat terus bang !!!"          
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "abangnya tegas tapi nyantai",  
                "pesan":"semangat terus bang!!!"
            },
            {

                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakaknya baik",  
                "pesan":"semangat terus kuliahnya kakak jangan sering2 merajuk"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Ngehina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "abangnya baik dan ingat dengan orang yang ditemui",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Berenang, ngoleksi figura & kartu anime",
                "sosmed": "@rewinanaaa",
                "kesan": "kakaknya keren punya hobi koleksi",  
                "pesan":"semangat terus kak!!"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "abangnya terlihat menyeramkan tapi aslinya baik dan ramah, easy going",  
                "pesan":"semangat terus bang!!!"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal":"Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "abangnya tegas kalem",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Fs1RCJTHeqtqB4Z0BjAa8CDo2lxQw6Vc",
            "https://drive.google.com/uc?export=view&id=1slxVk9QsLG_JAC30LBf4poaoU_E8adF8",
            "https://drive.google.com/uc?export=view&id=1JN43-IhouU9ubhwX2Xdwuacn58fEd6C6",
            "https://drive.google.com/uc?export=view&id=1BTsB9RhEA90Ex6bihj2YxJsz1HpYwvxR",
            "https://drive.google.com/uc?export=view&id=1XLwJfWCmM2rkq-fKg3P4nJtDk_XLU3u4",
            "https://drive.google.com/uc?export=view&id=1tNm2pHdIIRtgFCJiHzbJFlPbPD4O6sOb",
            "https://drive.google.com/uc?export=view&id=1Mj8BiKyPREj7dot6ytNpfPjCBBGjgkGv",
            "https://drive.google.com/uc?export=view&id=1iBZTFRVgNVIBLJEqRBVvqssc92J-KCJn",
            "https://drive.google.com/uc?export=view&id=1bFaCCO07tlem7obvsG9W09EJGrvsHZDP",
            "https://drive.google.com/uc?export=view&id=1rXBQuTyBg1gYtx8MUH_1RQze7m4PkbFQ",
            "https://drive.google.com/uc?export=view&id=1RiDvOyx2i_RVxBMc2BZDdlgxVdGMOfrM",
            "https://drive.google.com/uc?export=view&id=1TXKQzsCdIkXgyToG2E-kyeYoJBCY7Pjr",
            "https://drive.google.com/uc?export=view&id=1HhFgNTrJfFSXkjZEhpoCxjc-XI0ma9Y8",
            "https://drive.google.com/uc?export=view&id=11S1dyyEkYDomYy4RQQ-bxSH3WrekcjdP",
            "https://drive.google.com/uc?export=view&id=1bh-mYQYm69-7Zezr6AhxG6ZTcWvkPKvE",
            "https://drive.google.com/uc?export=view&id=1AsnIOEAeSvsPPV7ufv_V5dVmT83TqPbJ",
            "https://drive.google.com/uc?export=view&id=1zvIP8IsYPNNAvb7MyRRGyCwwGCtYPhS3",
            "https://drive.google.com/uc?export=view&id=1tpB79qNJehFXbTh92ig3ELj5gwYJcN4v",
            "https://drive.google.com/uc?export=view&id=1DNramim-uMaJyN_oc_AzGSTdPq00-0Jb",
            "https://drive.google.com/uc?export=view&id=1sRaboy07GsUED7-7BePOmgWkix0_e1Kf",
            "https://drive.google.com/uc?export=view&id=1jqCjiFXaGKPHm1BCZc5CYRUF_UV1i04N",
            "https://drive.google.com/uc?export=view&id=1ULaw8_sZpYTcIOXznSEAvIzxFzRYoqod",
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
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan 1",
                "hobbi": "Main ke embung",
                "sosmed": "@gustriana.d_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Hh1kM1AGpREJ6Y4q-PF-DHa6LHxoQbTg",
            "https://drive.google.com/uc?export=view&id=1VTKaE-hWAShLFuRg0979nUsSb_jJmAZK",
            "https://drive.google.com/uc?export=view&id=1frLYpUwKs4yHs09vBp6Y_YtXjacOFO-t",
            "https://drive.google.com/uc?export=view&id=1KkgPSfavuHHnVlUj6YrSVeNeDOqc1KwU",
            "https://drive.google.com/uc?export=view&id=1_YzK8Vohvm26-xRfU5g2uxbeMVc_2Vg2",
            "https://drive.google.com/uc?export=view&id=1_pRPSc8j5Bmq2UDbU0nSeqKTBZveXeAj",
            "https://drive.google.com/uc?export=view&id=18CTM0VQUGwM3LCNq0520RRRTm_sKHS0s",
            "https://drive.google.com/uc?export=view&id=1nUizHAWrBmlOFFy3Tzj9AxALRnsAmy7T",
            "https://drive.google.com/uc?export=view&id=1pATerqlGQ_OHjIllTj7a-rnTNcWYGQZM",
            "https://drive.google.com/uc?export=view&id=1T6a1yCxvYqk9cFYoF6DgRcbXJw8u6d2b",
            "https://drive.google.com/uc?export=view&id=1t1YCkdzlnl4JpH_-HX1XCrd1f-VHSI05",
            "https://drive.google.com/uc?export=view&id=1eM5kqk3eHZr5uhwOsBAhkh860Ylp8VVF",
            "https://drive.google.com/uc?export=view&id=1BTJPI9LmiGhqnwV1doQGag4NHOOkcfHL",
            "https://drive.google.com/uc?export=view&id=1sC8W0GcVDnT7X8zjoUWzza5rnwshkORG",
            "https://drive.google.com/uc?export=view&id=1RbsZlqPWz0TLD6ARa3dsY5pamdDOD4Fm",
            "https://drive.google.com/uc?export=view&id=1T6ctfZK7NkNArxGb1202VCHl6zJL8mTf",
            "https://drive.google.com/uc?export=view&id=1-nn5mF_VzxiqOfjlGHLpkwQ_HaZXTnir",
            "https://drive.google.com/uc?export=view&id=1Id_VNqbQt5YgNSD7oK7LVmT9EAge4wmC",
            "https://drive.google.com/uc?export=view&id=11vAzEpR8vxn4WgzCy-2QCQCya1FlGBH7",
            "https://drive.google.com/uc?export=view&id=1U0fBv2ccLM0jWaAmzFh3y0cnmVM1tFeO",
            "https://drive.google.com/uc?export=view&id=1YUCEdC3TTAKDYPJaaaW2df9UL8j821lo",
            "https://drive.google.com/uc?export=view&id=1jJFZb_rtcUPWeuAKLI4tD6h1DuGJ_iGW",
            "https://drive.google.com/uc?export=view&id=1fggMez1dNIA_G7y72rouNFSOmRUj3vAM",
            "https://drive.google.com/uc?export=view&id=1_Dk-wbyivHK4ZNLiBUgcSThPgaPqJn42",
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
                "kesan": "Abangnya santuy kalem abis, kelihatan cool",  
                "pesan":"Tetap humble bang!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": "jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini seru banget",  
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
                "kesan": "Kakak lucu, seruu, dan ramah",  
                "pesan":"Semakin positif dan humble kak!"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakak baik, dan mudah senyum",  
                "pesan":"Semangat terus kak kuliahnya!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Abangnya seru dan memang positive vibes",  
                "pesan":"Tetap semangat bangg!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "main-main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak seru, baik, dan mudah senyum",  
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
                "kesan": "Kakak santai, kalem, dan ramah suka senyum",  
                "pesan":"Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya baik bangett",  
                "pesan":"Semoga tercapai cita-citanya kak!"
            },
            {
                "nama": "Syahrialdi Rachm Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bandar Lampung",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Abangnya santai, ramah, dan mudah senyum",  
                "pesan":"Semangat terus bang jadi asprak jangan galak galak, dan semangat kuliahnya!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya baik, seru, dan positive vibes",  
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
                "kesan": "Kakaknya cantik banget, keren banget dutanya!",  
                "pesan":"Semangat terus di segala kegiatannya kak"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya lucu dan easy going",  
                "pesan":"semangat terus kakkk!!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "Asrama TB3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "abangnya keren, cool, dan punya integritas, tegas juga bisa menjaga professinalitas dan kekeluargaan",  
                "pesan":"makasih banyak udah banyak ngasih ilmu secara ga langsung bang"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "like crowded",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak nim kuu, orangnya easy going dan kaget dikit pas di komen, ga nyangka se humble itu",  
                "pesan":"tetap semangat teruss jadi asprak dan kuliahnya uhuy!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakak baikk, dan stylish kerennn",  
                "pesan":"Semangat terus kak kuliahnya!!!"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main Badminton",
                "sosmed": "@alfartziirvan",
                "kesan": "Abangnya typical orang yang kalem dan kalau ada apa apa dipikirin dulu ada vibes gubernurnya wkwk",  
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
                "kesan": "Abangnya humble parah easy going gitu, perhatian juga sama orang lain, seru lah diajak ngobrol ga pelit ilmu, kocak juga",  
                "pesan":"Tetap humble ya bang, jangan cape sama kelakuan random gemash!!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya peka sama lingkungan, gampang senyum, ga jaim, lengket mulu ama bang adit, sering cie2 in ama ashila apalah kakak ini",  
                "pesan":"Semangat terus kuliahnyaa kakak cantik!"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazatil_ilmi05",
                "kesan": "kakaknya imup, baik bangett, gampang senyum juga. kelihatan excited banget orangnya",  
                "pesan":"Semangat terus kakakk kuliahnya, sehat selalu, jangan lupa makan ya kak!"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton Film",
                "sosmed": "@dsmannhal_",
                "kesan": "kakaknya kalemmmm banget, vibes orang baik gitu, kemaren minta di tag di igs diladenin, typical yang kalem tapi ramah banget pokoknya",  
                "pesan":"Semangat terus kak melinnn!! tetap humble yaa"
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me Time",
                "sosmed": "@n.shafiraz",
                "kesan": "kakaknya baikkk, walaupun kadang mukanya kadang agak judes gitu tapi aslinya baik pol,",  
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
                "kesan": "kak izzah ini enak diajak diskusii, typical goood listener banget orangnya, ramah juga",
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
                "kesan": "bang qois ini orangnya jaim banget, padahal aslinya receh tapi kadang sok cool gitu ada ada aja emang, tapi itu yang bikin lucu",  
                "pesan":"tetap humble banggg, semangat terus kuliahnya, jangan lupa makan"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajah desa Lampung Selatan",
                "sosmed": "@tari_sya",
                "kesan": "kakak pengmas 1, positive vibes banget, paling excited kalauu diajak main undercover biarpun ga jago, belajar lagi ya kak! btw ranting?",  
                "pesan":"Semangat terus kak pengmas 1, jangan capek tutorin kelas rb, tetap humble, jangan lupa makannn!!"#
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DJzyysWlQVb3vJUW_DaQ0Cz1vXZSHqHh",
            "https://drive.google.com/uc?export=view&id=1Ekj4lHbW0-LCn6Mf5UOEA1T_ILMTG6zy",
            "https://drive.google.com/uc?export=view&id=14P801cOFzLbJgZKhQnlB2XEpnwLM63-n",
            "https://drive.google.com/uc?export=view&id=1piScIs2IryYJy8O77Noybl9NA1SsFgA2",
            "https://drive.google.com/uc?export=view&id=1piScIs2IryYJy8O77Noybl9NA1SsFgA2",
            "https://drive.google.com/uc?export=view&id=1IlnqwWjFSFhsOgk4TT9mNHVDLNDZvOZG",
            "https://drive.google.com/uc?export=view&id=1CpxC4uMP8X0hZ1vE0ZsHTFwQRPBmuVPz",
            "https://drive.google.com/uc?export=view&id=1PmThy6KPd1k2qoGeCrMxbXWGwMpVMgU0",
            "https://drive.google.com/uc?export=view&id=1V9zJbGmSnaKJYfMeNpHy0B1Q41hXzzDW",
            "https://drive.google.com/uc?export=view&id=1XtEInIxiMSzoBIr4_qQlvmgFzy2R-5mI",
            "https://drive.google.com/uc?export=view&id=1yWi6d-B57pWQYNLbkRSlK07RuIHltjMp",
            "https://drive.google.com/uc?export=view&id=1J7O22uGHUToNCwJOwCPl6ku8TvWrxN1u",
            "https://drive.google.com/uc?export=view&id=1K0nAPt2wjAs1FXuv7qY5MSy2cEKEPiZU",
            "https://drive.google.com/uc?export=view&id=1EJsSdkrHUuKOw_CgScs7nvj4Rhb6tI09",
            "https://drive.google.com/uc?export=view&id=14g2zWIUkCxSVDM9wPgylpw6Mmk2CK7B8",
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
                "kesan": "Kak Rani orangnya perhatian dan selalu berusaha menjaga kekompakan di tim ",  
                "pesan": "Semoga Kak Rani selalu diberi semangat dan kebahagiaan dalam setiap kegiatan." # 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Ramah dan gampang akrab sama siapa aja, jadi suasana selalu hangat ",  
                "pesan": "Makasih udah selalu nyiptain vibe yang nyaman, semoga Kakak makin sukses ke depannya."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Jateng",
                "alamat": "Airan",
                "hobbi": "memasak",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya rajin banget dan selalu disiplin, jadi motivasi buat kami yang masih belajar ngatur waktu. ",  
                "pesan": "Semoga terus diberi semangat dan kesehatan biar bisa terus jadi inspirasi" 
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "melukis",
                "sosmed": "@exsander",
                "kesan": "Punya aura pemimpin yang tenang, tapi tetap santai dan gampang diajak becanda. ",  
                "pesan": "Semoga ke depannya makin sukses dan tetap jadi panutan yang rendah hati." # 4
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB 4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya lucu tapi bijak, selalu bisa ngasih masukan yang menenangkan tanpa menggurui.",  
                "pesan": "Teruslah jadi Kakak yang bisa diandalkan, semangat terus ngejalanin semua aktivitasnya!" # 5
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln",
                "kesan": "Kakaknya keren dan berwawasan luas, sering banget ngasih insight yang membuka pikiran. ",  
                "pesan": "Semoga terus jadi inspirasi buat kami yang masih belajar, Kak" # 6
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Ceria dan selalu bisa bikin suasana cair, gak pernah kelihatan bad mood.",  
                "pesan": "Semoga senyumnya tetap ada di setiap kegiatan, semangat selalu Kak!! !!!" # 7
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Surabaya",
                "alamat": "Teluk",
                "hobbi": "Travelling",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakaknya dewasa banget cara berpikirnya, bikin kita semua belajar tentang tanggung jawab.",  
                "pesan": "Terima kasih udah jadi contoh yang baik, semoga sukses selalu di setiap perjalanan Kak" # 8
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "123450116",
                "umur": "20",
                "asal": "Sidoarjo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "muhammadnaufalalghani73",
                "kesan": "Kakaknya punya aura positif, bikin orang lain semangat cuma dari cara Kakak ngomong ",  
                "pesan": "Jangan berhenti nyebarin semangat itu, himpunan butuh lebih banyak orang kayak Kakak!!!" # 9
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Humoris tapi tetap profesional, suasana jadi gak tegang kalau Kak udah ikut ngobrol. ",  
                "pesan": "tetap jadi sosok yang ringan tapi berpengaruh, semangat terus ya Kak!." # 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain alat musik",
                "sosmed": "@kerennmrti",
                "kesan": "Kaknya kalem tapi kalau udah ngobrol, banyak banget hal menarik yang bisa dipelajari.",  
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
                "kesan": "Kakak sangat peduli dengan keakraban dan kesejahteraan anggota ",  
                "pesan": "Teruslah berbagi pengalaman dan inspirasi ya Kak, bermanfaat banget buat kami." # 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Jawa Barat, Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahswti",
                "kesan": "Kakaknya dewasa banget, selalu bisa jadi penenang waktu tim lagi panik",  
                "pesan": "semangat terus kuliahnya kakak !!!" # 14
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "123450096",
                "umur": "19",
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Maen rubik mirror",
                "sosmed": "@zhrptsl",
                "kesan": "kakaknya sederhana tapi berpengaruh, setiap omongan Kakak selalu berkesan.",  
                "pesan": "Teruslah jadi inspirasi dalam kesederhanaan, semoga segala urusan Kakak dimudahkan!!!" # 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HrRkk6KYPnCtmHESgtI4hmE17tDv_cLS",
            "https://drive.google.com/uc?export=view&id=1yAXFjw12CLIGrFVKbn_B6e7mBuzhYQUi",
            "https://drive.google.com/uc?export=view&id=1qIRr_nP-PccxM1p2K2Y_m6796XDhBq91",
            "https://drive.google.com/uc?export=view&id=15qaoadoUTi-mMfPlcfWxG7YFemgbi2YP",
            "https://drive.google.com/uc?export=view&id=1NE84xc_VgGsRWjJELwzoYQpZwjIdCR-B",
            "https://drive.google.com/uc?export=view&id=1xhV7MoQVIKkNrVJ-XOR7HZFSvRcWN5Rq",
            "https://drive.google.com/uc?export=view&id=1utKZOrpn55mCV4R_8LJiqChhfM7xZFDK",
            "https://drive.google.com/uc?export=view&id=1OrSPelAGabonHtAUiJcFk4sOxAUaLnDU",
            "https://drive.google.com/uc?export=view&id=1iJVBLWfoCZxWw5B7rffrQlANQAmyBNjd",
            "https://drive.google.com/uc?export=view&id=18x3jK7XqbvdF5T8QKRH1-oG8UtS3XC8O",
            "https://drive.google.com/uc?export=view&id=1fUT4JfDkZ11o40JhwTAAajFeOtUd0svP",
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
                "kesan": "abangnya punya wawasan luas dan ga takut buat gagal, salut! ",
                "pesan": "semangat terus kuliahnya bang!!!"   # 1
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "Kakaknya punya semangat juang tinggi, gak gampang nyerah walau situasi lagi susah. ",
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
                "kesan": "abangnya keren banget, cool, ramah juga",
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
                "kesan": "Kakaknya sederhana tapi berpengaruh, setiap omongan Kakak selalu berkesan.",
                "pesan": "semangat terus kuliahnya kak, jangan lupa makann"   # 4
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aphrtjp__",
                "kesan": "kakaknya baik banget, ramah juga mudah senyum ",
                "pesan": "semangat terus kuliahnya kak, semoga dilancarkan segala urusannya, jangan lupa makan!"   # 5
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "kakaknya ramah baik hatiii ",
                "pesan": "semangat terus kuliahnya kakak !!!"   # 6
            },
            {
                "nama": "Dhafim Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "keren bangett hobinya belajarr, ramah orangnya ",
                "pesan": "semangat terus kuliahnya!!!"   # 7
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "sama sama suka nonton drakorr, lucuu.",
                "pesan": "semangat terus kuliahnya kakak !!"   # 8
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@engirahmdhnii",
                "kesan": "kakaknya baikk banget, ramah juga ",
                "pesan": "semangat terus kuliahnya, jangan lupa makan kak !!!"   # 9
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "keren banget hobinya masakkk, orangnya baik mudah senyum",
                "pesan": "semangat terus kuliahnya, jangan lupa makan kak!"   # 10
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "@nydiaputr_",
                "kesan": "kakaknya ramah dan emang baik ",
                "pesan": "semangat terus kuliahnya kak, jangan lupa makannn!!!"   # 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10MTRT9NETeoLZoD9M3J6nUD-LsqBnWGI",
            "https://drive.google.com/uc?export=view&id=1pi_Yzs4gADrN09BnkZ8twCge2XR8xxf1",
            "https://drive.google.com/uc?export=view&id=1J80ZoaNBLOO1NYhUCNcui0Z_zCEVSW3N",
            "https://drive.google.com/uc?export=view&id=1EmsXIl1djmFjIOZWagHAv9svww4T_rqt",
            "https://drive.google.com/uc?export=view&id=1iGWgIhQnILHxT_e-nUPHJeXYyDSAgPlx",
            "https://drive.google.com/uc?export=view&id=1S9vh6k7U1gDdBs_qX92W-doPsN9FwQbO",
            "https://drive.google.com/uc?export=view&id=1ZV0Olz6NuISd5-y93HlofSC9tkbpFcVV",
            "https://drive.google.com/uc?export=view&id=1qtBl5J0GaZfJ5uRSLHijbtDeISiBkcIu",
            "https://drive.google.com/uc?export=view&id=1Fvp2TFrcopHw3yUqzwycMCViTZydl2BS",
            "https://drive.google.com/uc?export=view&id=1rLQd1devd1mFRJ4FXOAxG30FhIAVV2Aa",
            "https://drive.google.com/uc?export=view&id=1zvdxngx99g7rdFJC_3dg46UO8Yc0XX1Z",
            "https://drive.google.com/uc?export=view&id=1T4DgFl0zuznDu62hZoxGpUhJe9o3iEde",
            "https://drive.google.com/uc?export=view&id=1m_C0nUWpaWn429qf1sMmkyiTItQat9j6",
            "https://drive.google.com/uc?export=view&id=1rgyHtzBhaPZOPt8Kt4H16Nq91IpRAXI6",
            "https://drive.google.com/uc?export=view&id=1jR0SVV-KsOIgFOeZq9x94TEk4S1BiOkD",
            "https://drive.google.com/uc?export=view&id=1XtknzGS6yhiuaOzoWb-Oy5Jig_lNR65i",
            "https://drive.google.com/uc?export=view&id=1wKu093GdKXz6QU9hz7V5ByhE0BrYUjPo",
            "https://drive.google.com/uc?export=view&id=1D0805IZYJlNDyIwvDD72CdnNGIAJFYP0",
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
                "kesan": "Kakaknya extrovert final boss, energinya ga habis-habis, ramah banget",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa makan, dan tetap humble yaa !!!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "kakaknya ramahh baikk bangett",  
                "pesan":"semangatt terus kuliahnya kak!!!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya baik bangetttt, mudah senyumm",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "abangnya ramah banget typical orang yang suka bantuin orang lain, salut!",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya seruuu, baik juga, keren punya hobi dance",  
                "pesan":"semangat terus kuliahnya kakak, jangan  lupa makan"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "hobinya melukiss, keren bangett, baik juga orangnya, ramah gitu",  
                "pesan":"semangat terus kuliahnya kak!!!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "kakaknya seruuu, humble banget",  
                "pesan":"tetap humble dan semangat selalu kak"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "sama sama suka nonton netflix, kirain kakaknya pendiem ternyata seru banget",  
                "pesan":"semangat terus kuliahnya kak, tetap humble, infokan rekomendasi series !!!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "kakaknya kirain pendiem ternyata seru banget orangnya ramah gitu",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa makannnn !!!"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "sama-sama suka gelang, hobi nya sama ,kakaknya baik dan ramah",  
                "pesan":"semangat terus kuliahnya kak, jangan lupa makann!!!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "username ig kakaknya keren banget, orangnya seru juga mudah senyum euy",  
                "pesan":"tetap humble kakk, jangan lupa makan!!"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "kakaknya kelihatan banget suka baca, literasinya tinggi, ramah dan baik",  
                "pesan":"ssemangat terus kuliahnya kak, jangan lupa makan !!!"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "sama sama suka main roblox, kakaknya juga asikk eak",  
                "pesan":"infokan mabar roblox kak, semangat terus kuliahnya !!!"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "kakaknya humble banget euy, gacorr",  
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
                "kesan": "abangnya positive vibes gitu, ramah banget, kelihatan suka nolong orang",  
                "pesan":"semangat terus ngedesignnya bangg!!!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "keren kakaknya hobi denger musikkk, orangnya humble banget cihuy",  
                "pesan":"semangat terus kuliahnya kak!!!"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "kerenn abangnya gacorrrr",  
                "pesan":"semangat terus kuliahnya bangg !!!"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "abangnya seruu bangett, ramah, mudah senyum",  
                "pesan":"semangat terus kuliahnya bangg!!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()





# Tambahkan menu lainnya sesuai kebutuhan

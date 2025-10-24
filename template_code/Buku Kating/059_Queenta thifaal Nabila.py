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
            "https://drive.google.com/uc?export=view&id=18NqhHgGVd5_fUeumoG88m7gzxaMb8AAD",
            "https://drive.google.com/uc?export=view&id=1ofplx9YOIMxaZsK53sRcOufZV_kQdUvP",
            "https://drive.google.com/uc?export=view&id=1Xqn254RgvF_bLtSWm2SBPih5F_WdlNMt",
            "https://drive.google.com/uc?export=view&id=15AvRWVpylYjfhSnIbrZJDepCehMjFJ5q",
            "https://drive.google.com/uc?export=view&id=1j4Cur6ir6KhxvXELfxJc7-dZbnfDrdRi",
            "https://drive.google.com/uc?export=view&id=1QOidBo8KiHfynYchxJOCZ-nwvxZaM51e",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "beli donat kentang",
                "sosmed": "@_erendraa",
                "kesan": "Abangnya ramah, sabar, dan selalu bisa mencairkan suasana. Sosok yang tenang tapi bisa jadi tempat cerita yang menyenangkan",  
                "pesan":"Terima kasih sudah menjadi contoh yang baik bagi kami. Semoga setiap langkah abang selalu diberi kemudahan dan kesuksesan"
            },
            {
                "nama": "Johannes Krisjon Sitilonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "baca buku (dasar-dasar sql)",
                "sosmed": "@johanneskrisjnnn",
                "kesan": ": Abang yang tegas tapi tetap rendah hati. Selalu hadir dengan sikap yang bijak dan tanggung jawab yang tinggi",  
                "pesan":"Terima kasih sudah banyak membantu dan memotivasi kami. Semoga abang terus diberi semangat dan kesuksesan di setiap perjalanan hidupnya"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tanggerang",
                "alamat": "Airest Kost",
                "hobbi": "siram shopee",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya lembut dan sabar banget waktu menjelaskan ke kami",  
                "pesan":"Terima kasih sudah jadi panutan, semoga karier kakak lancar selalu !!!"
            },
            {
                "nama": "Syadza Puspandari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya lembut dan penuh perhatian. Selalu bisa membuat suasana terasa nyaman dan menyenangkan.",  
                "pesan":"Terima kasih atas kebaikan dan bimbingannya. Semoga kakak selalu diberi kesehatan dan kebahagiaan di setiap langkah"
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "rajabasa",
                "hobbi": "baca buku , saku pramuka",
                "sosmed": "@ekshantyfebriana",
                "kesan": "Kakaknya ceria dan bersemangat, selalu menularkan energi positif kepada orang di sekitarnya",  
                "pesan":"Terima kasih sudah menjadi sosok yang menginspirasi. Semoga semangat kakak tidak pernah padam dalam mengejar cita-cita"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"kota Padang,Sumbar",
                "alamat": "sukarame",
                "hobbi": "tidur",
                "sosmed": "@farahanumafifahh",
                "kesan": ": Kakaknya bijak dan penyabar, selalu bisa memberikan solusi dengan tenang",  
                "pesan":"Terima kasih sudah banyak membantu dan membimbing dengan sabar. Semoga semua kebaikan kakak dibalas berlipat ganda"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WsHpeBZdvCzBIoRzfn_ut-2zcQg9tVWx",
            "https://drive.google.com/uc?export=view&id=1cqjmr5dy356sHoR-zU7gdThn6bNdyyxv",
            "https://drive.google.com/uc?export=view&id=1UengXToOnncgq_a7VL9Y0DKpp9NY6mop",
            "https://drive.google.com/uc?export=view&id=1TOJ9CMl1a7pTeaNj7VipiaMWX8QrxtuD",
            "https://drive.google.com/uc?export=view&id=1dz6U5OJKzNxQcy_N28QEHFJ-rxp0Xx7c",
            "https://drive.google.com/uc?export=view&id=15oTXcaK355m1pGKlpZxs1VcO8rbn6bG0",
            "https://drive.google.com/uc?export=view&id=1hwNUytpFR43k0cZm813b-l-KE9UvZVqO",
            "https://drive.google.com/uc?export=view&id=1xw6YjJCuiDDOLX7UWRGO4y7p4VQFs3AU",
            "https://drive.google.com/uc?export=view&id=1FTUZDHJi4RNbsC1a395b4anE1c8wCQ7N",
            "https://drive.google.com/uc?export=view&id=1qeNHZHlir0EsVqs5x5K35D6Vp44YFAvZ",
            "https://drive.google.com/uc?export=view&id=1nx0Qolaqqe_yy7zyIFprXYeIq68O5T85",
            "https://drive.google.com/uc?export=view&id=17ovsCP8sJE3barvjmELfQGN1xZnBTvve",
            "https://drive.google.com/uc?export=view&id=1fUW1UDbJQSG0GIVdpNVp0DnVxTBVT77J",
            "https://drive.google.com/uc?export=view&id=1htd20bCDyDMYv2bmJN2iabQGHdZinmQ9",
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
                "kesan": "Abangnya kalem tapi seru banget kalau udah diajak ngobrol",  
                "pesan":"Semoga selalu diberi kelancaran dan jangan lupa main bareng adik-adik lagi!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Mojokerto, Jawa Timur",
                "alamat": "Teluk",
                "hobbi": "Suka buat setan minder",
                "sosmed": "@_.dheamelia",
                "kesan": "Lembut tapi tegas, sosok kakak yang bijak banget",  
                "pesan":"Semoga selalu bahagia dan terus jadi panutan kami semua!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan pancing",
                "sosmed": "@renishapg",
                "kesan": "Ceria dan rame, selalu bawa suasana positif ke mana pun..",  
                "pesan":"Tetap jadi kakak yang penuh semangat dan nyebarin energi baik ya."
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Muara Enim, Sumatera Selatan",
                "alamat": "C2",
                "hobbi": "Belajar Mengaji",
                "sosmed": "@ansftynn_",
                "kesan": "Teliti dan tanggung jawabnya tinggi banget.",  
                "pesan":"Semoga semua kerja keras kakak dibalas dengan kesuksesan besar."
            },
            {
                "nama": "Dharu Cahyo Aji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Bengong",
                "sosmed": "@dhruchyo",
                "kesan": "Gampang akrab sama siapa pun, humble banget.",  
                "pesan":"Jangan pernah berubah, semoga sukses di semua hal yang abang kerjain."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Menggodai Abang Cimol",
                "sosmed": "@fby.wlndr",
                "kesan": "Perhatian dan penyayang, kayak kakak sendiri di rumah.",  
                "pesan":"Terima kasih udah selalu support dan kasih semangat ke kami."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@givarooo",
                "kesan": "Kocak dan santai, bikin suasana selalu cair.",  
                "pesan":"Tetap jadi abang yang rame dan gak berubah ya"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "Wibawanya kerasa banget, kayak pemimpin sejati.",  
                "pesan":"Semoga langkah abang selalu dimudahkan dan terus jadi inspirasi!"
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
                "kesan": "Kalem tapi lucu, selalu bikin suasana adem.",  
                "pesan":"Jangan berubah ya kak, tetap jadi sosok yang menenangkan"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Gang Sakung",
                "hobbi": "Main  Padel",
                "sosmed": "@ianridhomanik",
                "kesan": "Gampang akrab sama siapa pun, humble banget",  
                "pesan":"Jangan pernah berubah, semoga sukses di semua hal yang abang kerjain!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal": "Bangka Belitung",
                "alamat": "Kobam",
                "hobbi": "Nongkrong di gedung f",
                "sosmed": "@fer_yulius",
                "kesan": "Pendiam tapi perhatian, selalu ada saat dibutuhin.",  
                "pesan":"Terima kasih udah selalu dengerin dan kasih saran yang nenangin."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Ketapang, Kalimantan Barat",
                "alamat": "Belwis",
                "hobbi": "Memanah",
                "sosmed": "@monca_tjg",
                "kesan": "Disiplin dan tangguh, tapi tetap care sama adik-adiknya.",  
                "pesan":"Semoga kakak terus semangat dan jadi inspirasi banyak orang!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pekan Baru, Riau",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Baik hati dan selalu siap bantu tanpa banyak bicara.",  
                "pesan":"Makasih atas semua kebaikannya, semoga dibalas berkali lipat!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hI4CkDmB6mgGscesWl_MJoZMw9BpcJIn",
            "https://drive.google.com/uc?export=view&id=1FyKaA_10Ksx6a0PhN0aTQb2zTSJJLPR8",
            "https://drive.google.com/uc?export=view&id=1rETssavIX5E-vZIPGT1S7s_TozwO8Nd-",
            "https://drive.google.com/uc?export=view&id=1xBn_jEujnMxLQ9ok3jLq3LSdfqDFbmbV",
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
                "kesan": "Ramah dan asik diajak ngobrol, suasana langsung cair.",  
                "pesan":"Semoga selalu sukses dan terus menyebarkan energi positif"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjaani",
                "kesan": "kanad sangat perhatian sekali ke gweedy , imupppp ^^ ",  
                "pesan":"Semoga hal hal baik selalu menyertai!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kalem tapi lucu, selalu bikin suasana adem",  
                "pesan":"Jangan berubah ya kak, tetap jadi sosok yang menenangkan"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "Ceria dan rame, selalu bawa suasana positif ke mana pun.",  
                "pesan":"Tetap jadi kakak yang penuh semangat dan nyebarin energi baik ya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA" :
    def departemen_psda():
        gambar_urls =  [
            "https://drive.google.com/uc?export=view&id=1LbapYUsANnJRDjYAB3iuUngDOhRqTakN",
            "https://drive.google.com/uc?export=view&id=1Ln9T0DhW-D_zOTmAS4c6qYKUx9fQFbRV",
            "https://drive.google.com/uc?export=view&id=1FLGr8isu_oDH-IabVaZ_8SU6llQqJev-",
            "https://drive.google.com/uc?export=view&id=1etWTm-ZdP6Je4Yt-KXSzXYXCo-zkfPUw",
            "https://drive.google.com/uc?export=view&id=1oXgqB-ZbkTzRnHRgHuv_KjgLOhGRA5Zh",
            "https://drive.google.com/uc?export=view&id=1v4WN2spPL3gdtPujIh4Z4nC3uAwWO-gk",
            "https://drive.google.com/uc?export=view&id=10rENgVrOFC-YPZmsl1gsJNHOLUuLFMRR",
            "https://drive.google.com/uc?export=view&id=1D-LWqNGc-hFe93Z91trWrSv1aBCuUUj1",
            "https://drive.google.com/uc?export=view&id=1nVG7Gpvq7lMuUbwtrs-AKJMNUOd1nO56",
            "https://drive.google.com/uc?export=view&id=1XV0tnX2F9u-nX8K9Mx5sL76ajpWzO2FU",
            "https://drive.google.com/uc?export=view&id=1DC7GmMrbVfSrtd8PhyLbJFS4O1V6ipqn",
            "https://drive.google.com/uc?export=view&id=1eoDKLCGltnxJVV1EZ5zZJLzlt3m17Cie",
            "https://drive.google.com/uc?export=view&id=1BWPg2AoRgpqtLlaoDCKSn9B9DkipaUtP",
            "https://drive.google.com/uc?export=view&id=1JTOa43xWEBP8E-uOhRDbSLTuC_t8vUdp",
            "https://drive.google.com/uc?export=view&id=1CJm7BVnGpERM-UZCFPsMBGNIz8oD7Zsz",
            "https://drive.google.com/uc?export=view&id=1qkhAup9wSEmHbQlwGdDyNyxnaKQwHb4l",
            "https://drive.google.com/uc?export=view&id=1OEzLVeeUuUP_bLc-ov4DVc3_0hPUUhXq",
            "https://drive.google.com/uc?export=view&id=1Sie8F8EpI1RvVDBkvKN-DRZLIkooUXjR",
            "https://drive.google.com/uc?export=view&id=1MG9JzuUOYK3xssfk9Qtv5tba0-5dTjHk",
            "https://drive.google.com/uc?export=view&id=1eLnGOM0f356nNtsEUiMvFVxzBL_qcDLd",
            "https://drive.google.com/uc?export=view&id=1HC0YzPAoeAJhr6lHr2uq5kZQ02lSywGC",
            "https://drive.google.com/uc?export=view&id=1cChPcmWPVdUWPX8tDOx8B1XVXpbLLdi3",
            "https://drive.google.com/uc?export=view&id=1XZXOzK4GviQgZz3s-oeQiocYO24NAWCK",
            "https://drive.google.com/uc?export=view&id=1krHumDVgQfqWVQDPtuh0iWRqtEi4vpLq",
            "https://drive.google.com/uc?export=view&id=1P5sqzNvFneT3hfxxngKOw0KtboKnnqy4",
            "https://drive.google.com/uc?export=view&id=1JxcKNhoXi0rtpyDMpobfJhmnp01VQdIw",
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
                "kesan": "Selalu tampil tenang dan bijak dalam setiap situasi.",  
                "pesan":"Semoga terus jadi panutan yang inspiratif,  semangat bang"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri, sukarame",
                "hobbi": "Jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Tegas tapi tetap hangat, bikin suasana jadi terarah",  
                "pesan":"Terus pertahankan gaya kepemimpinan yang positif, kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "123450033",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira",
                "hobbi": "Main",
                "sosmed": "@alyapasha_",
                "kesan": "Disiplin dan bertanggung jawab, patut dicontoh, humoris",  
                "pesan":"Terima kasih sudah jadi pembimbing, kak semangattt"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tanggerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Punya pemikiran matang dan penuh pertimbangan.",  
                "pesan":"Semoga makin sukses dengan keputusan-keputusan bijak abang"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal":"Kalianda",
                "alamat": "sebelah  kos bang dapa",
                "hobbi": "Liatin Haikal",
                "sosmed": "@arientakhsnl_",
                "kesan": "Humoris tapi tetap profesional, enak diajak kerja bareng.",  
                "pesan":"Semoga semangat dan energinya nggak pernah padam."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "sebelah kos kak arin",
                "hobbi": "Isengin Fislam",
                "sosmed": "@daffahdynn_",
                "kesan": "Tegas tapi nggak menekan, cara bimbingnya keren.",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Cikarang",
                "alamat": "Sama kek bang ahmad",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Kalem tapi kalau bicara, selalu kena di inti.",  
                "pesan":"Semoga terus jadi pribadi yang bijak dan inspiratif"# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost putri Gerbang Barat",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Ceria dan selalu membawa suasana positif.",  
                "pesan":"Terus sebarkan semangat itu ke orang sekitar."
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Gg. Perwira",
                "hobbi": "Ngakader",
                "sosmed": "@nobelnizam",
                "kesan": "Selalu hadir dengan solusi, bukan sekadar kritik.",  
                "pesan":"Terus tebarkan energi positif di mana pun berada, bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450022",
                "umur": "21",
                "asal": "Sumatra Barat",
                "alamat": "Sigma family",
                "hobbi": "Mancing Keributan",
                "sosmed": "@ji_gumel17",
                "kesan": "Disiplin banget, tapi tetap bisa diajak bercanda",  
                "pesan":"Semoga tetap seimbang antara kerja keras dan santai, bang"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Pandai menempatkan diri di berbagai situasi",  
                "pesan":"Semoga makin sukses dan tetap rendah hati, kak"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@sahid22",
                "kesan": "Ramah, bijak, dan menyenangkan diajak kerja sama.",  
                "pesan":"Semoga sukses selalu dan terus menebar inspirasi."
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "1234450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gg nangka 4 Sukarame",
                "hobbi": "Main game, kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Punya rasa tanggung jawab yang besar.",  
                "pesan":"Terima kasih sudah jadi contoh kedisiplinan,bang"
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Waydadi",
                "hobbi": "Tidur",
                "sosmed": "@verazkaa",
                "kesan": "Pembawaan kakaknya menenangkan.",  
                "pesan":"Semoga terus jadi sosok penenang di tengah tekanan."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll TikTok",
                "sosmed": "@risma.mustika_",
                "kesan": "Teliti dan nggak asal-asalan",  
                "pesan":"Terus pertahankan detailnya kak, itu keren banget."
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "Enerjik dan selalu aktif dalam kegiatan",  
                "pesan":"Semoga semangat kakak tetap menyala di mana pun."
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal":"Depok, Jabar",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": "Selalu terbuka untuk berdiskusi",  
                "pesan":"Terima kasih sudah jadi tempat berbagi yang nyaman"
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "-",
                "sosmed": "@ahmadnaufa_ll",
                "kesan": "Punya komitmen tinggi terhadap tanggung jawab",  
                "pesan":"Semoga semangat itu terus terjaga, bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Jl. Lapas Raya no.55",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Tegas tapi tetap bisa bercanda.",  
                "pesan":"Semangatt kuliahnya ,kak"
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Belwis Pemda",
                "hobbi": "Makan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Visioner dan selalu punya ide baru",  
                "pesan":"Semoga ide abang makin besar pengaruhnya ke depan"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Makan Beling",
                "sosmed": "@kevinaj__",
                "kesan": "Wibawanya kuat tapi tetap friendly",  
                "pesan":"Semoga sukses di setiap langkah,  bang"
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Ramah dan penuh empati.",  
                "pesan":"Semangat menjalani hari harinya, kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450023",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Main Badminton",
                "sosmed": "@m.ridwan_22",
                "kesan": "Abangnya ini atlet badminton,rajin banget, nggak heran semua beres di tangan abang",  
                "pesan":"Jangan lupa rehat di sela kesibukan, bang"
            },
            {
                "nama": "Rewina Audrya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Berenang, ngoleksi figura & kartu anime",
                "sosmed": "@rewinanaaa",
                "kesan": "Lembut dalam berbicara, tapi kuat dalam tindakan",  
                "pesan":"Semoga terus konsisten dengan ketulusan , kakak"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "Selalu memotivasi tanpa menggurui.",  
                "pesan":"Terus jadi penyemangat bagi yang lain, bang"
            },
            {
                "nama": "Uliano Wiliam Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Main piano, nanem anggrek, ngoding dan nyari kesalahan anak 24",
                "sosmed": "@ilano",
                "kesan": "Teguh pada prinsip tapi tetap fleksibel",  
                "pesan":"Semoga prinsip baik abang terus menginspirasi"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SbUE83FT1dbJzlgDVbSwjdpvHMamMxkx",
            "https://drive.google.com/uc?export=view&id=1FntRYtFuDjClghtTCeJUhavH0z9BxVcZ",
            "https://drive.google.com/uc?export=view&id=1FpKYB2YZ0QuGwnEd1SJfQZdsvjamewWE",
            "https://drive.google.com/uc?export=view&id=1RHn2iH3djbUslgmJhkbFeMQVm8DN-FNv",
            "https://drive.google.com/uc?export=view&id=1MPf6OVbhzNr-HbvIeKw1w6Lbl4426fAj",
            "https://drive.google.com/uc?export=view&id=1kIdaaKYNV4gpt0IOsWITVZolPy3dFnx6",
            "https://drive.google.com/uc?export=view&id=1oq4zg1oAmymJ1Se_w8eG6fsKYc4tNHva",
            "https://drive.google.com/uc?export=view&id=1_gwzH691qihD37YY2CLSCQ_iEKQax7Sx",
            "https://drive.google.com/uc?export=view&id=1svS8C3qiI9Xf4V-BvDXMmzWAQOWhDINJ",
            "https://drive.google.com/uc?export=view&id=1qdRtm-26Aukt0Nl2jmWEPffkG1AKcL7A",
            "https://drive.google.com/uc?export=view&id=1j2jM0lEujYL8ecgPOXHn7FQAOIyoSEoR",
            "https://drive.google.com/uc?export=view&id=1zpKoG9HDCOYbN_HCYcJa7q1RUIT9V70M",
            "https://drive.google.com/uc?export=view&id=1LBXESrgu6e665ZzgoHIiPXdDocgzcfX2",
            "https://drive.google.com/uc?export=view&id=1b_OjX8hFwFlr-EZMqDIgZJpaq84aPkh7",
            "https://drive.google.com/uc?export=view&id=1ok8Kc587AVSCXnq3AToOeFJtTQunr_7z",
            "https://drive.google.com/uc?export=view&id=1rayB1f9sTAAelbQvTLwBJtLpx0FfuTzi",
            "https://drive.google.com/uc?export=view&id=1Y2PMBrLh_PSVD_LIcfDwgpQcrAvZwKQj",
            "https://drive.google.com/uc?export=view&id=1iB3FUbkZzBImDvWmCPvTo1piB6QGRtfq",
            "https://drive.google.com/uc?export=view&id=1LkRQ_LNoGaQIgblBVxHTz1ZwDcBNRw5C",
            "https://drive.google.com/uc?export=view&id=1Jg7IZB0mtUOSBxKhjlQ7Dq3AN6KgVDOg",
            "https://drive.google.com/uc?export=view&id=1tkRxaVC6BTUEWxdB8V8BLxhcp-95-kXf",
            "https://drive.google.com/uc?export=view&id=1LciGXzMtK5uGFpZJBRwaqjkENwP9ix-Q",
        ]
        data_list = [
            {
                "nama": "Randa Adriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur berkembang",
                "sosmed": "@randaadriana_",
                "kesan": "Selalu semangat dan enerjik, nular ke kita semua.",
                "pesan": "Jangan bosan ngajarin kita hal baru!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Membaca abstrak jurnal/paper/artikel, dan gangguin Randa",
                "sosmed": "@Junitaa.0406",
                "kesan": "Punya cara komunikasi yang enak dan mudah dimengerti.",
                "pesan": "Terima kasih sudah sering jadi jembatan antara kami dan pengurus atas."
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Sukarame",
                "hobbi": "dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Tegas tapi asik, selalu punya solusi di saat genting",
                "pesan": "Tetap jadi panutan ya, semangatt."
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas, Belwis",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Selalu semangat dan nggak pernah setengah-setengah kalau kerja.",
                "pesan": "Jangan pernah berubah, Kak. Energi Kakak luar biasa"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "fore",
                "hobbi": "Segala a100",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Selalu semangat dan enerjik, nular ke kita semua",
                "pesan": "Jangan bosan ngajarin kita hal baru, bang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal": "Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Sosok yang tegas, tapi tetap bisa diajak ngobrol santai",
                "pesan": "Terima kasih sudah banyak membimbing. Semoga makin sukses ke depannya."
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Tanjung Senang",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Punya jiwa kepemimpinan, tapi tetap membaur.",  
                "pesan": "Terus jaga cara memimpin yang santai tapi tegas itu, Bang."
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@adiaafrj",
                "kesan": "Terorganisir dan punya komitmen tinggi.",
                "pesan": "Terima kasih udah ngajarin pentingnya konsistensi dalam organisasi!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Bass, piano, semualah",
                "sosmed": "@marletacornelia",
                "kesan": "Ramah dan suka ngajak ngobrol duluan.",
                "pesan": "Terima kasih sudah banyak memberikan ruang untuk kami berkembang."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Kreatif dan punya gaya yang khas.",
                "pesan": "Semoga bisa terus berkarya dan berkembang di jalur yang Abang pilih."
            },
            {
                "nama": "Anggi puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar",
                "hobbi": "Dengerin Musik, Dance, ngedrakor",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Salah satu kakak yang paling aktif dan total kalau udah pegang program kerja.",
                "pesan": "Terus semangat berkarya ya, Kak. Kami banyak belajar dari etos kerja Kakak"
            },
            {
                "nama": "Efi Defiyah",
                "nim": "123450005",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Jalan jalan",
                "sosmed": "@eeffiidefi",
                "kesan": "Tegas, tapi tetap santai dan enak diajak diskusi.",
                "pesan": "Semoga tetap jadi panutan dan sukses ke depannya"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano, Nyanyi, Ngehalu",
                "sosmed": "@bee_0115",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fairuz  Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Teliti dan profesional dalam mengurus kegiatan.",  
                "pesan": "Terima kasih sudah menunjukkan standar kerja yang baik"
            },
            {
                "nama": "Tanty Widiyastut",
                "nim": "123450094",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "Punya wawasan luas dan selalu berbagi insight baru.",
                "pesan": "Semoga terus tumbuh jadi pribadi yang berdampak luas"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal": "Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Tenang, dewasa, dan selalu berpikir jernih.",  
                "pesan": "semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan IV, Airan",
                "hobbi": "Isengin Orang dan random chat bareng gpt",
                "sosmed": "@fifah.zy",
                "kesan": "Seru, dekat dengan semua kalangan, dan tetap profesional.",  
                "pesan": "Semoga tetap jadi sosok yang mengayomi dan adaptif."
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Jalan jalan, main game",
                "sosmed": "@biokcb",
                "kesan": "Disiplin dan konsisten, jadi contoh buat kami.",
                "pesan": "Terus pertahankan integritas itu, Bang. Kami banyak belajar dari Abang"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Main catur",
                "sosmed": "@giofaniars_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan": "Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas raya",
                "hobbi": "Main catur",
                "sosmed": "@rhmaoktvia",
                "kesan": "Aktif, kreatif, dan energik di setiap kegiatan.",
                "pesan": "Terus tebarkan semangat kepedulian itu ke mana pun melangkah."
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jalan airan 1",
                "hobbi": "Futsal",
                "sosmed": "@gustriana.d_",
                "kesan": "Tenang dan bisa ngontrol keadaan",
                "pesan": "Tetap semangat menginspirasi lewat karya-karya nyata, Kak"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan": "Terima kasih atas semua pelajarannya, bang semangat!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1034pgUGd6DUMEU-JhIG7PmJWT2eYdnqg",
            "https://drive.google.com/uc?export=view&id=1jcQds54xI6ZkTAkCt_uEqopYC0n8s7gw",
            "https://drive.google.com/uc?export=view&id=1WiXmNhPnJyBg59Duz-dW1_TPNnLkr0vU",
            "https://drive.google.com/uc?export=view&id=1r_C1nJPArkUh2YwbepWz-q6pmmXIqFwu",
            "https://drive.google.com/uc?export=view&id=1CDi-WmFRnuSqc4NmLySmOhg6ZKIMOdc3",
            "https://drive.google.com/uc?export=view&id=1cHRCuoTKVrCRZQ_E6dYXa_hlKw1NKOwB",
            "https://drive.google.com/uc?export=view&id=15a8lCdSpCho_qryn6omH8_9TFxhf1XTL",
            "https://drive.google.com/uc?export=view&id=1fWhJuFYc57W_CW6rJRAmmRu5Z_p8Vf4j",
            "https://drive.google.com/uc?export=view&id=1AvyCU2mNM1aIP-IhN0z3Rdjy2WH6k6uF",
            "https://drive.google.com/uc?export=view&id=1eicfvhTFHJGGJxqNL0h8doe_BNYLpmMB",
            "https://drive.google.com/uc?export=view&id=1hIZq0rhSsXt7Am_pmmv_0PbPSCT_mODi",
            "https://drive.google.com/uc?export=view&id=1Ir7RdNLlTHBkdBULkOxa9IGSwoRfqPVn",
            "https://drive.google.com/uc?export=view&id=1iArpXZxZMg0V7UDl0gWhYeRJtJQ3wUXb",
            "https://drive.google.com/uc?export=view&id=1MArWqsBAh2b5muzsglW4HK_AoMqePVsN",
            "https://drive.google.com/uc?export=view&id=1deEm5sMEAB9afTJZ_pLfl98-w8H6giRe",
            "https://drive.google.com/uc?export=view&id=1XbINrnvYdynGgfksl_zJ-eyw536bwaRY",
            "https://drive.google.com/uc?export=view&id=1A0996p54i9x75mqsyKgdChmZRLZ3GoAc",
            "https://drive.google.com/uc?export=view&id=1Rb4ORuRLHth0K3pFXaRUYllhErpF-AB1",
            "https://drive.google.com/uc?export=view&id=1XSPlxFiLDoAcIOhhZt7OaK8V_LbfY9ho",
            "https://drive.google.com/uc?export=view&id=1dfe8ORHRehVf6A7JfUgQX1cfMcvk51lk",
            "https://drive.google.com/uc?export=view&id=1apzenXiWJ59uZRZR8uCjK3H38-US2r2g",
            "https://drive.google.com/uc?export=view&id=143SuLvwRGRcJeG1ChJMUAzynmvyCjWRo",
            "https://drive.google.com/uc?export=view&id=1_tn9oP3iuEiFsZLsBcjxtoyZN_6FsYpJ",
            "https://drive.google.com/uc?export=view&id=1pZi5O_fj0Ynda-7YugFPYtZ-y7-Snimg",   
        ]
        data_list = [
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "berwibawa tapi tetap easy going",
                "pesan":"Semoga terus jadi panutan yang inspiratif buat kami"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya selalu ramah dan sabar banget",
                "pesan": "Terima kasih sudah banyak membimbing, semoga sukses terus, Kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Selalu memberi contoh baik dalam sikap dan tanggung jawab",
                "pesan":"Semoga ilmunya makin berkah dan langkahnya lancar, kak"
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Tegas tapi perhatian, benar-benar sosok pemimpin",
                "pesan":"Terus semangat berkarya dan tetap rendah hati ya, Kak"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Sederhana tapi bijak banget setiap ngomong",
                "pesan":"Semoga terus menginspirasi dengan cara khas abang"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kakaknya keren, tenang, tapi tetap peduli sama adik tingkat",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Kakaknya punya aura positif yang bikin suasana nyaman",
                "pesan":"Jangan berubah ya, tetap jadi pribadi yang menyenangkan"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak sangat baik disiplin tapi bisa diajak bercanda juga",
                "pesan":"Semoga makin sukses di jalan yang Kakak pilih"
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "asik, nggak jaim tapi tetap berwibawa",
                "pesan":"Semoga semua mimpi abang segera tercapai!"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Teladan banget dalam hal tanggung jawab",
                "pesan":"Semoga tetap konsisten dan terus menebar kebaikan"
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya punya semangat yang nular banget",
                "pesan":"Jangan pernah padamkan semangat itu ya, Kak"
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Kakaknya humble banget padahal udah keren",
                "pesan":"Tetap rendah hati dan terus berprestasi!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Baik, sopan, dan selalu menghargai siapa pun",
                "pesan":"Semoga kebaikan abang dibalas berlipat ganda"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakaknya selalu bikin suasana jadi adem",
                "pesan":"Terima kasih udah jadi sosok yang menenangkan"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Bijak banget kalau kasih masukan",
                "pesan":"Semoga makin bijak dalam setiap langkah"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya kalem tapi berkarakter kuat.",
                "pesan":"Semoga terus konsisten di setiap perjuangan"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Humoris, baik, dan punya gaya memimpin yang berkarakter. ",
                "pesan":"Semoga terus berkembang dan menginspirasi banyak orang"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya disiplin banget, tapi nggak kaku",
                "pesan":"Semoga terus konsisten di setiap perjuangan"
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakaknya nggak banyak bicara tapi berpengaruh besar",
                "pesan":"Terima kasih udah jadi sosok yang mengajarkan lewat tindakan"
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakaknya keren dalam cara berpikir dan bersikap",
                "pesan":"Semoga makin sukses dan bahagia di perjalanan hidup"
            },
            { 
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya punya cara sendiri buat memotivasi.",
                "pesan":"Semoga makin banyak yang terbantu karena Kakak"
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Pekerja keras dan tulus bantu orang lain",
                "pesan":"Teruslah menebar semangat dan inspirasi"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Disiplin tapi tetap fleksibel",
                "pesan":"Semoga bisa terus menyeimbangkan semuanya"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Penuh energi dan semangatnya nular",
                "pesan":"Semoga semangat itu terus bertahan"
             }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uolcZu1p_UgohP_7QGJbSjpPr58UzBUn",
            "https://drive.google.com/uc?export=view&id=1uhCfsxybYjuBnwnHPxmy9Bqiq3Bo93Y4",
            "https://drive.google.com/uc?export=view&id=1eYa7Z0tCrpNSbJigjZgBwL9wShdQXwAE",
            "https://drive.google.com/uc?export=view&id=1Pz1DlyNRuN4MUIAr8KIfy7N2G0oAuqik",
            "https://drive.google.com/uc?export=view&id=1LeQ0BaVW-p25u6uSkMOqH8D7rfCMDgcq",
            "https://drive.google.com/uc?export=view&id=1Kpo28uUnp8l1z270PUVaeA_t6hhMhtJt",
            "https://drive.google.com/uc?export=view&id=1gm_ByedKhJovuxxh1lnbs0pAnT40kB7m",
            "https://drive.google.com/uc?export=view&id=1GlzHDco2TB5otI1dsuorDA-ZoMoJngqh",
            "https://drive.google.com/uc?export=view&id=1RnixtHj1tCZQmweSXabg6-Yk1atvmEAN",
            "https://drive.google.com/uc?export=view&id=1jzj5YysMOEGlWnqctSoHZac8cnACG_D1", 
            "https://drive.google.com/uc?export=view&id=1F7w-QLldrjwJyvUtG3FtnydRaiCFiooX",
            "https://drive.google.com/uc?export=view&id=11_G17RVyftftwd-5cbvivFCTLe1qig7k",
            "https://drive.google.com/uc?export=view&id=1doG16qO588ZHyPd6smYCvMb6HTNjLumD",
            "https://drive.google.com/uc?export=view&id=1vZNR0QsYLCQs9UOJt0Ddncl7p_HdwEYS",
            "https://drive.google.com/uc?export=view&id=1ydZy1vjOfWBiuZEJ8OggaB7EoXtDZnPo",   
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Tegas tapi care, kombinasi yang susah ditemuin",
                "pesan":"Semoga terus konsisten dan menginspirasi, semanngat kak"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya kalem tapi karismatik banget",
                "pesan":"etap jadi panutan yang rendah hati ya, Kak"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Kakaknya kreatif banget, ide-idenya selalu fresh.",
                "pesan":"Terus berkarya dan jangan takut beda, Kak!"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Humoris tapi tanggung jawabnya tinggi banget.",
                "pesan":"Makasih udah bikin suasana nyaman, kak"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Pemikirannya selalu matang dan bijak.",
                "pesan":"Terus jadi inspirasi buat adik-adiknya, bang"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakak paling lucu dan nggak pernah bikin tegang suasana.",
                "pesan":"Tetap bawa vibes positif ke mana pun, Kak"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Selalu tenang dalam menghadapi situasi sulit.",
                "pesan":"Semoga terus menjadi sosok yang bijaksana."
            },
            {
                "nama": "Muhmmad Naufal Al Ghani",
                "nim": "1234500116",
                "umur": "20",
                "asal":"Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": "Tegas dan bertanggung jawab dalam setiap tugas.",
                "pesan":"Semoga selalu konsisten dalam setiap langkah,semangat bang"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kakak selalu memberi contoh yang baik.",
                "pesan":"Terima kasih atas bimbingan dan keteladanannya."
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Punya semangat tinggi dan mampu menularkan motivasi.",
                "pesan":"Semoga semangat itu tidak pernah padam"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak disiplin dan berkomitmen pada tanggung jawab.",
                "pesan":"Terus pertahankan integritas dan ketegasan itu, kak"
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakak memiliki kepedulian yang tulus terhadap junior.",
                "pesan":"Terima kasih atas perhatian dan arahannya."
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal":"Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Bijak dalam mengambil keputusan..",
                "pesan":"Semoga terus menjadi sosok yang menuntun dengan kebijaksanaan."
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakak memiliki wawasan luas dan mampu membimbing dengan baik.",
                "pesan":"Terima kasih atas ilmu dan arahannya selama ini."
            },
            {
                "nama": "Azzahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way huwi, pemda",
                "hobbi": "Rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "Kakak selalu memberi contoh kedewasaan dalam bersikap.",
                "pesan":"emoga terus menjadi panutan yang membangun generasi berikutnya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1j08nxmppEnJgkUTm2iRyRULbUqd_sBmT",
            "https://drive.google.com/uc?export=view&id=1UJuIfEbGRsTplgsbpDuzi6jpPtREmFV1",
            "https://drive.google.com/uc?export=view&id=1lsJODkWSuB1oyZ7LoDof6dO7hUNrZTm4",
            "https://drive.google.com/uc?export=view&id=1DcsWAj-DPL39dpv4V4Zp3NB9DRIiOmTU",
            "https://drive.google.com/uc?export=view&id=12dNcvUjG1v9qcppZaTtjLXTrXJWKx5PE",
            "https://drive.google.com/uc?export=view&id=1lmNXpKd_2B2wPZPHYn1o7PuX5Gyufa_f",
            "https://drive.google.com/uc?export=view&id=1kwbl2LJU3J1cExJKLyLtgnTah6PD0Sv2",
            "https://drive.google.com/uc?export=view&id=1jEaWs1XJOS9_iy5IteC8LhoU1UMjrenF",
            "https://drive.google.com/uc?export=view&id=15nMsqUlZi93wBAbS_fLjbx5XwCAr-0XI",
            "https://drive.google.com/uc?export=view&id=1mRGD8H9BBGH8DKof8ZtRiX-H8WIge_x8",
            "https://drive.google.com/uc?export=view&id=1d_Y4U71X5v5GZwYBrH0EMcP1exTQdkR3",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "jogging",
                "sosmed": "dananghk_",
                "kesan": "Selalu punya cara unik buat nyelesain masalah, kreatif banget.",
                "pesan": "Terus kembangin ide-ide kerennya, siapa tahu jadi inspirasi besar nanti."
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Bicaranya selalu sopan dan enak didengar.",
                "pesan": "Semoga sukses selalu kuliahnya kak!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Tampilannya cool, tapi hatinya lembut banget.",
                "pesan": "Sukses kedepannya ya bangg."
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Punya sense humor yang khas, gampang banget bikin orang ketawa.",
                "pesan": "Tetap ceria, jangan hilang di tengah kesibukan dunia kerja nanti."
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Punya aura positif yang bikin suasana adem tiap ngobrol.",
                "pesan": "Terus tebar energi baik itu ke mana pun kamu pergi."
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Ceria, supel, dan gampang akrab sama siapa aja.",
                "pesan": "Terus jadi penghubung yang nyatuin semua orang kayak sekarang"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Cara ngomongnya lembut tapi berisi, selalu bikin mikir.",
                "pesan": "Semoga terus bisa nyebarin hal-hal baik lewat kata-kata"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Orangnya lembut tapi berpendirian kuat.",
                "pesan": "Terus pegang nilai-nilai baik, Semangat terus ya, kak!"
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Setiap obrolan sama kamu selalu ada maknanya, nggak pernah sia-sia.",
                "pesan": "Semoga terus jadi pribadi yang berpengaruh baik di lingkungan mana pun."
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Selalu totalitas kalau dikasih tanggung jawab.",
                "pesan": "Jaga kesehatan selalu, kak!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "baikk, cantik,ramah,murah senyum.",
                "pesan": "Ssemngat menjalani kehidupan kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_iu0KM6TpZa-905Mg0Lc1e4RrV6HUYjC", 
            "https://drive.google.com/uc?export=view&id=1_gMIAeK9bdkJdjR3SzGne-ZvCoGq9Byk", 
            "https://drive.google.com/uc?export=view&id=1W_10AhuBTYJff3RtddFGAGxPB9wmUB8J", 
            "https://drive.google.com/uc?export=view&id=1AQy3kHv0z-E_LQtr-vTlMe0uSK_J8BIL", 
            "https://drive.google.com/uc?export=view&id=12PZU5Uf-AFK97b_FgGXR3hDZjkpKmTfA", 
            "https://drive.google.com/uc?export=view&id=1p1zIr1mExRrjFyCEY4OFi9VCM4uYY-7q", 
            "https://drive.google.com/uc?export=view&id=14gNsdJziUi92Y7oGLaY3gMuj3skRq2Os", 
            "https://drive.google.com/uc?export=view&id=1WY24blDZ4NhSUXoqcSneM9bfNPkUg3MN", 
            "https://drive.google.com/uc?export=view&id=1VFwWlEaDDlgjZKBIdV82wPsK-p7TKmMe", 
            "https://drive.google.com/uc?export=view&id=17CO_JZxOqJfG30TEKNzcWZR42rcdrFNt", 
            "https://drive.google.com/uc?export=view&id=1zEfmbDgdiFpmOX3HzjGImtEqfWrsPIwQ", 
            "https://drive.google.com/uc?export=view&id=1JAE8fN4gKO2cxUSku4nS6hS5lc8phv9H", 
            "https://drive.google.com/uc?export=view&id=1epCN2BblFPSbnofgAO3q7nOtkJU1gk_p", 
            "https://drive.google.com/uc?export=view&id=13Pjiu_SbQAu3B_JDbF48tjYpRcVubrCl", 
            "https://drive.google.com/uc?export=view&id=1gFdmUuNgr3YZEOxrpnSWFhmKUtJfIdp2", 
            "https://drive.google.com/uc?export=view&id=1AQMieeCgi42CUJbu6vkH3RdTdFUTYKrf", 
            "https://drive.google.com/uc?export=view&id=1aFhA1SFl2Q5hLaHwTzqdwnt6kpyBvoI8", 
            "https://drive.google.com/uc?export=view&id=1oxhjjaXtW9_qSYN-JLTuKFYekcWrnC83", 
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
                "kesan": "Suaranya lucu imupp, baik, cantik bbanggeetzz",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "Punya semangat tinggi dan selalu nyebarin energi positif",  
                "pesan":"Jangan pernah kehilangan semangat itu, dunia butuh orang kayak kakak!!!"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Serius pas kerja, tapi aslinya seru banget diajak ngobrol.",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Lucu tanpa usaha, gayanya tuh khas banget",  
                "pesan":"Tetap jadi diri sendiri, dunia butuh orang sejujur dan setulus itu."
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Punya gaya mimpin yang santai tapi efektif",  
                "pesan":"bisa jadi inspirasi buat banyak orang!!!"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Punya pemikiran matang dan selalu mikirin tim",  
                "pesan":"Terus jadi sosok yang bijak, semoga makin sukses di perjalanan berikutnya"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": ": Selalu punya ide menarik di setiap diskusi",  
                "pesan":"jangan berhenti berproses, ide-idenya keren banget buat dibawa lebih jauh"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Humornya ringan tapi bikin suasana cair banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Keliatan cuek, tapi ternyata peduli banget",  
                "pesan":"sTeruslah jadi versi terbaik dari diri sendiri, keren banget"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Energinya nggak pernah habis, selalu semangat dari awal sampai akhir",  
                "pesan":"Semoga semangatnya nular terus ke banyak orang"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Tegas tapi nggak galak, pas banget buat dijadiin panutan",  
                "pesan":"Semoga karier dan hidupnya lancar terus, kakak layak dapet yang terbaik"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Selalu datang dengan senyum, nular banget ke semua orang",  
                "pesan":"angan pernah berhenti nyebarin energi positif itu"
            },
            {
                "nama": "Akmal Faiz Abdilah ",
                "nim": "122450114",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Tenang, tapi kalau ngomong pasti nyentuh",  
                "pesan":"Jangan berubah, karena ketenanganmu bikin banyak orang nyaman"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Tipe orang yang susah dilupain, selalu ninggalin kesan baik di tiap momen",  
                "pesan":"Semoga langkahnya selalu ringan dan hatimu tetap hangat di mana pun berada"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Selalu rapi dan teratur, kayaknya hidupnya well-planned banget",  
                "pesan":"Tetap jadi inspirasi buat yang masih berantakan kak"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Disiplin tapi tetap bisa bercanda, kombinasi langka",  
                "pesan":"Terus jaga keseimbangan itu, bikin semua nyaman kerja bareng"
            },
            { 
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Asik banget diajak ngobrol apa aja, nyambung terus",  
                "pesan":"Semoga kita masih sering ketemu di luar kegiatan ini"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


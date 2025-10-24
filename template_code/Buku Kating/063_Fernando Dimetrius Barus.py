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
            "https://drive.google.com/uc?export=view&id=1yrvuhxnWwUrJ7-ES957SS8nnbdw4cWmS",
            "https://drive.google.com/uc?export=view&id=1QO96oZVftP9IGXeBEZszO-UilMjZNUmR",
            "https://drive.google.com/uc?export=view&id=1Bj-6IR1Kzrq_geA__sqYILijPE3meJFW",
            "https://drive.google.com/uc?export=view&id=19vDE4L_MAeMQgtalGkNnJ88QyIz4JVKp",
            "https://drive.google.com/uc?export=view&id=1O3aGC2VNpFYN4ACcR1ApyyE79u9mtzpn",
            "https://drive.google.com/uc?export=view&id=1fyc9Wk81fH0CAq0fG_cpzKsOUGTZWfVW",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Menyanyi",
                "sosmed": "@_erendraa",
                "kesan": "Bang rendra suaranya bagus baik penjelasan nya juga mudah di mengerti",  
                "pesan":"semangat terus bang, semoga cepet lulus!!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Jo orangnya agak serius tapi asik bercandanya",  
                "pesan":"semangat bang semoga cepet lulus yaa !!!"# 1
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                 "kesan": "kak elisabeth lucu orangnya heboh jugaa",  
                "pesan":"semoga lancar terus ya kak apapun yang dikerjain"# 1
           },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya pendiem tapi tetep asik kok pas foto",
                "pesan": "semangat kak sukses selalu"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty ramah keliatan kayak orang pinter juga hehe",
                "pesan": "Semangat kuliahnya ya kak"
            },
              {
                  "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya asik pas ngobrol juga nyambung",
                "pesan": "semoga kakak sehat selalu lancar urusannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1b1gMCHf_lAiZuv-qk25wfpRsDuNHSIUq",
            "https://drive.google.com/uc?export=view&id=1EdyeLKNjdORH5NFYNUG1tuBru1oc-Ots",
            "https://drive.google.com/uc?export=view&id=1YUOKa7RWwumjsG6DMNpxcqnk7zavaPSs",
            "https://drive.google.com/uc?export=view&id=1aI4pBGydKnyQnpE5DYM6YEG1PVANIBD3",
            "https://drive.google.com/uc?export=view&id=1jxcCe81yLe9jBNbGWQziXWLCg_1-vJSU",
            "https://drive.google.com/uc?export=view&id=1vNFTsdtvHNVlSBxZSrNkPQedDCvzQrQY",
            "https://drive.google.com/uc?export=view&id=1A8v8vAh4I_gRz5v2fRB6LINRZOFZ5UJ6",
            "https://drive.google.com/uc?export=view&id=1b-2hAJkewMKuA7aD_uwMeFtHAjglvYe5",
            "https://drive.google.com/uc?export=view&id=1vGN6HRNnRyhMl4-hNMDuxPAY7dTu_j0S",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1fu1A2yzKdiYXC1EEnLCB4j31MS2weCRE",
            "https://drive.google.com/uc?export=view&id=10SjyHSpmlNsAZYoUcsji8I32BO3NX2md",
            "https://drive.google.com/uc?export=view&id=18mIszVQDxbnsbTRNxNnnUMJ9lHG5ZOs3",
            "https://drive.google.com/uc?export=view&id=1xHf1DXPx0BOiDq2Vmo03m3IPoDDAxQqH",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Tanjung Merawa",
                "hobbi": "Suka main voli sama Feby",
                "sosmed": "@jeremia_s_",
                "kesan": "Lucu abangnya tapi tegas",
                "pesan": "semangat bang kuliahnya semoga urusannya lancar"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kaknya keren, penjelasannya selalu jelas",
                "pesan": "Semoga cepat lulus dan makin sukses!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Seru dan asik diajak ngobrol",
                "pesan": "Sukses terus kak, jangan lupa main bareng"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Baik dan lucu, gak pernah marah",
                "pesan": "Sukses selalu kak di setiap langkahnya!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Santai tapi serius di momen tertentu keren",
                "pesan": "Sehat selalu dan semoga kariernya lancar kak!"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "selalu bisa nyemangatin semua orang",
                "pesan": "tetap jadi pribadi seru kayak sekarang!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Kakaknya asik banget, selalu bikin suasana WWC jadi rame tapi tetap kondusif.",
                "pesan": "Semoga nanti bisa terus ngembangin diri dan tetep jadi kakak yang seru dan inspiratif buat adik-adik!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Kakaknya lembut, sabar, dan gak pernah marah meski kita kadang ribet sendiri.",
                "pesan": "Semoga terus dikelilingi orang-orang baik dan bisa terus berbagi hal positif ke banyak orang"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya selalu nyebarin energi positif, jadi suasana latihan gak pernah boring.",
                "pesan": "Semoga selalu bahagia dan tetap jadi sosok yang ceria dan bikin semangat!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "keren banget pas ngarahin kita, gayanya santai tapi tegas",
                "pesan": "Semoga ke depannya makin banyak acara yang bisa kak handle, dan tetep jadi mood maker tim!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Lucu banget orangnya, selalu bisa bikin semua ketawa walau lagi capek.",
                "pesan": "Semoga humornya gak pernah hilang dan terus bisa nyemangatin orang di sekitar kak!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Santai banget tapi selalu bisa diandelin di setiap situasi.",
                "pesan": "Semoga langkahnya selalu dimudahkan dan makin banyak hal baik yang datang ke kakak!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "Kocak banget tapi tetep fokus kalau udah kerja, seru banget bareng",
                "pesan": "Semoga terus jadi pribadi yang nyenengin dan makin banyak hal keren yang kak capai!"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lembut, perhatian, dan selalu nyemangatin kita tanpa bosan.",
                "pesan": "Semoga selalu bahagia, dikelilingi orang baik, dan cepat lulus dengan hasil terbaik!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
    # Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BItv1wKC0ueJnWjWC7Z-WjzmtaSkV9y_",
            "https://drive.google.com/uc?export=view&id=13quwp4kZJDWZfgI0983LVtIamApfu4Fx",
            "https://drive.google.com/uc?export=view&id=1MCIDZH_YU0MptOPFeFgEuytXsHZyu9Wc",
            "https://drive.google.com/uc?export=view&id=1UZXmd7lbyq2Y50TILmcW5T3-hRnPb-Lh",
             ]   
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Belajar",
                "sosmed": "@bintangtwinkle",
                "kesan": "Mantap bang penjelasannya keren abis lucu juga",
                "pesan": "Istirahat bang penting itu"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakaknya tenang tapi keren banget pas ngarahin kita",
                "pesan": "Semoga makin sukses dan tetep rendah hati ya kak!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "Seru banget diajak ngobrol, selalu nyebarin vibes positif",
                "pesan": "Semoga tetep semangat dan gak pernah kehilangan tawa kak!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "Asik banget pas bareng kak, selalu bisa cairin suasana",
                "pesan": "Semoga karier dan kuliahnya lancar terus kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
    # Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450122",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "korpri sukarame",
                "hobbi": "jajan",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "ngekader 24",
                "sosmed": "@allyapasha_",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "cari kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Yulia",
                "sosmed": "@daffahdynn_",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "ngitungin duit",
                "sosmed": "@natasyamavisca",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Nobel Nizam F",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Ngasprak",
                "sosmed": "@ji_gumel17",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "ngoding di macbook",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@shahid22_",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main video game",
                "sosmed": "@sahid_maul19",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerjain Tugas",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Koleksi Pita Pink",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngomongin Kak Dea",
                "sosmed": "@kevinaj_",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nyuruh Dea Diam",
                "sosmed": "@ridwan122",
                "kesan": "Kakaknya asik dan baik banget. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Liat Shoppe tapi ga beli",
                "sosmed": "@rewinanaaa",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main BOla",
                "sosmed": "@sidabutar.26",
                "kesan": "Senang bisa dibimbing sama Kakak. Keren!",
                "pesan": "Semoga studinya lancar dan sukses terus ya, Kak."
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Terima kasih banyak atas ilmunya, Kak.",
                "pesan": "Sukses selalu ya, Kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
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
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal": "Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "Kakaknya kalem tapi keren banget pas ngarahin kami",
                "pesan":"Semoga makin sukses dan tetep jadi panutan ya kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal": "Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Seru banget orangnya, bikin suasana WWC gak pernah sepi",
                "pesan":"Semoga tetep jadi kak yang asik dan berenergi positif!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "124450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "Kakaknya sabar dan penjelasannya selalu jelas banget",
                "pesan": "Semoga ilmunya makin luas dan bermanfaat terus!"
            },
            {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "Keren banget pas ngasih materi, gayanya santai tapi ngena",
                "pesan": "Semoga karier akademiknya makin lancar kak!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "Kocak tapi tetep fokus, bikin suasana jadi rileks.",
                "pesan": "Semoga tetep ceria dan sukses di jalan yang kak pilih!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal": "Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kalem tapi bisa banget ngatur suasana.",
                "pesan": "Semoga makin berprestasi dan selalu bahagia kak!"
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "Ramah banget dan gampang akrab sama siapa aja.",
                "pesan": "Semoga terus nyebarin semangat positif di mana pun kak berada!."
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "Santai tapi sigap, selalu bisa diandalkan.",
                "pesan": "Semoga makin sukses dan tetep jadi sosok keren yang rendah hati!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya aktif dan pinter banget, bener-bener inspiratif.",
                "pesan": "Semoga semua hal baik selalu ngikutin langkah kak!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Sabar banget ngadepin kami yang ribet, salut parah..",
                "pesan": "Semoga makin banyak hal keren yang bisa kak capai!"
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Bumi Sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "Gokil tapi peka, selalu bikin suasana enak",
                "pesan": "Semoga tetep seru dan gak pernah berubah jadi kak yang ngebosenin!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya lembut dan perhatian, bikin nyaman banget.",
                "pesan": "Semoga makin sukses dan terus jadi penyemangat!"
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "-",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "Tegas tapi baik banget, selalu kasih contoh yang bagus.",
                "pesan": "Semoga terus jadi sosok yang bijak dan disegani!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "124450081",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450022",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "-",
                "kesan": "gampang nyatu sama semua orang.",
                "pesan": "Semoga kebahagiaan selalu nyertai kakak di mana pun!"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya ceria dan menyenangkan.",
                "pesan": "Semoga Kak selalu membawa keceriaan di mana pun berada."
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "Abangnya kalem tapi punya aura positif yang kuat banget.",
                "pesan": "Semoga apa pun yang kak lakuin selalu lancar dan membawa kebaikan!"
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "Abangnya tenang dan berwawasan luas.",
                "pesan": "Semoga Abang terus berprestasi dan sukses selalu."
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "Kakaknya terkesan cool tapi sebenernya seru banget",
                "pesan": "Semoga makin sukses dan tetep jadi pribadi yang asik kayak sekarang!"
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "-",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "Kakaknya santai tapi selalu on point, gak pernah ribet.",
                "pesan": "Semoga semua hal yang kak impikan bisa tercapai satu-satu!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya chill tapi vibes-nya berwibawa banget, respect!",
                "pesan": "Semoga Abang selalu diberi kesehatan dan kesuksesan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
    
if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Gayanya chill tapi keren, kayaknya semua hal bisa di-handle dengan tenang.",
                "pesan": "Semoga makin sukses dan tetep santai dalam segala situasi, kak!"
            },
          {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya ceria banget, selalu bawa suasana jadi hidup.",
                "pesan": "Semoga semangatnya gak pernah padam dan terus nyebarin energi positif ke mana pun kak pergi!"
            },
          {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva, follow @cerebral.id_",
                "kesan": "Kakaknya elegan tapi friendly banget, gampang bikin orang nyaman.",
                "pesan": "Semoga makin banyak hal baik yang datang dan kariernya lancar terus!"
            },
          {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya vibes-nya positif banget, selalu nyemangatin tanpa banyak ngomong.",
                "pesan": "Semoga kakak selalu bahagia dan terus dikelilingi orang baik!"
            },
          {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Lucu banget, selalu punya cara buat bikin suasana cair.",
                "pesan": "Semoga tetap jadi sumber ketawa dan kebahagiaan di mana pun kak berada!"
            },
          {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main-main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Kalem tapi strong, kelihatan banget kalo kak Lala tuh punya aura pemimpin.",
                "pesan": "Semoga makin berani dan sukses di setiap langkahnya!"
           },
          {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Cool banget, tapi kalau udah ngomong langsung bikin suasana cair.",
                "pesan": "Semoga makin sukses dan tetep jadi sosok yang bisa diandalkan!"
            },
          {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya ramah banget, selalu bikin nyaman tiap kali ngobrol.",
                "pesan": "Semoga semua hal baik terus ngikutin kakak ke mana pun pergi!"
             },
          {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "Santai tapi fokus, kerjaannya selalu beres tanpa drama.",
                "pesan": "Semoga semua impian kak bisa terwujud satu per satu, semangat terus!"
              },
          {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya aktif banget dan selalu punya ide keren.",
                "pesan": "Semoga makin banyak kesempatan buat kakak nunjukin potensi terbaiknya!"
            },
          {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam Naya",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya tenang tapi lucunya kadang muncul tiba-tiba",
                "pesan": "Semoga sukses terus dan tetep jadi kak yang easy-going banget!"
              },
          {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton reels Agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Gokil banget, kayaknya gak ada momen yang gak seru kalo ada kakak.",
                "pesan": "Semoga terus jadi sosok yang nyebarin good vibes ke semua orang!"
             },
          {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Main musik bareng bang kita kapan kapan",
                "pesan": "Kakaknya lembut banget, auranya menenangkan."
             },
          {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Keliatan serius tapi ternyata asik banget pas udah kenal.",
                "pesan": "Semoga sukses terus dan tetep jadi kak yang bijak tapi santai!"
               },
          {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Ceria, humble, dan gampang akrab sama siapa aja.",
                "pesan": "Semoga semua yang kak impikan pelan-pelan jadi kenyataan!"
            },
          {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kakaknya pinter banget tapi gak pernah sombong.",
                "pesan": "Semoga makin sukses dan tetep rendah hati kayak sekarang, kak!"
              },
          {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakaknya kalem banget, tapi kalo udah ngomong langsung bikin suasana adem.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik dan orang-orang suportif!"
               },
          {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Punya ide-ide random tapi keren banget, selalu ngasih warna baru.",
                "pesan": "Semoga kreativitasnya gak pernah habis dan makin sukses di tiap jalan!"
              },
          {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya ceria dan gampang banget deket sama siapa aja.",
                "pesan": "Semoga hari-hari kak selalu penuh tawa dan kebahagiaan!"
              },
          {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "Santai tapi tangguh, selalu keliatan bisa handle apa aja.",
                "pesan": "Semoga makin sukses dan terus jadi inspirasi buat banyak orang!"
              },
          {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Kakaknya punya aura positif yang bikin nyaman.",
                "pesan": "Semoga terus bahagia dan makin percaya diri ngejar mimpi-mimpi kak!"
              },
          {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Kakaknya supel banget, gampang akrab sama siapa aja.",
                "pesan": "Semoga selalu semangat dan makin banyak hal keren yang kak capai!"
              },
          {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois orangnya terlihat aga jaga image, paling jago kalo main undercover, baik juga orangnya, seru banaget orangnya dan suka jalan-jalan!",
                "pesan": "Tetap semangat bang, jangan lupa jaga kesehatann!"
             },
          {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajahi desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Kaknya chill tapi punya vibe pemimpin banget, keren!",
                "pesan": "Semoga makin sukses dan tetep rendah hati kayak sekarang, kak!"
             },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": 21,
                "asal": "Metro",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengaji",
                "sosmed": "@ranniku",
                "kesan": "Kakaknya tenang tapi berwibawa banget, selalu keliatan siap di setiap situasi.",
                "pesan": "Semoga makin sukses dan tetep jadi sosok yang bisa diandelin di mana pun!"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": 22,
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta orangnya tenang dan sopan.",
                "pesan": "Semoga semangatnya gak pernah hilang dan makin banyak hal baik yang datang!."
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": 21,
                "asal": "Brebes, Jateng",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa.fhn",
                "kesan": "Kakaknya lembut tapi tegas, keliatan banget rasa tanggung jawabnya.",
                "pesan": "Semoga semua impian kak tercapai dan selalu bahagia di setiap langkah!"
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": 20,
                "asal": "Pekan Baru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azzah.raaa_",
                "kesan": "Kakaknya humoris banget, bikin suasana rapat jadi seru terus.",
                "pesan": "Semoga tetep jadi sumber tawa dan inspirasi buat semuanya, kak!"
            },
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450106",
                "umur": 18,
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakaknya kalem tapi kalau ngomong selalu ngena.",
                "pesan": "Semoga makin sukses dan tetep rendah hati kayak sekarang!"
            },
            {
                "nama": "Iqfinah Haula Halika",
                "nim": "123450076",
                "umur": 20,
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "iqfinanhalikaa_",
                "kesan": "Kakaknya berenergi banget, semangatnya bikin orang lain kebawa positif.",
                "pesan": "Semoga semangatnya gak pernah luntur dan makin banyak pencapaian kak dapet!"
            },
            {
                "nama": "May Thalita Dehlia",
                "nim": "123450009",
                "umur": 20,
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": "Kakaknya chill tapi selalu tahu kapan harus serius.",
                "pesan": "Semoga makin banyak hal baik yang datang dan tetep jadi kak yang asik!"
            },
            {
                "nama": "M. Naufal Algahni",
                "nim": "123450116",
                "umur": 20,
                "asal": "Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": "Kakaknya perhatian dan selalu nyebarin aura positif.",
                "pesan": "Semoga kak selalu dikelilingi kebahagiaan dan orang-orang baik!"
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": 19,
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kakaknya asik banget, suka bercanda tapi tetap fokus kalau udah kerja.",
                "pesan": "Semoga sukses selalu dan tetap jadi pribadi yang nyenengin!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": 21,
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@reaxender",
                "kesan": "Kakaknya kalem tapi berani, keren banget ngeliat caranya ngomong.",
                "pesan": "Semoga makin percaya diri dan terus bersinar ke depannya!"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": 20,
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya punya vibe positif, selalu bawa suasana adem.",
                "pesan": "Semoga karier dan kuliahnya lancar terus ya kak!"
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": 19,
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya manis banget, gampang bikin orang nyaman.",
                "pesan": "Semoga selalu bahagia dan makin banyak hal keren yang dicapai!"
            },
            {
                "nama": "Muhammad Hanif Zaki",
                "nim": "123450004",
                "umur": 20,
                "asal": "Padang",
                "alamat": "Perumnas, Way Kandis",
                "hobi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "Santai tapi niat, keren banget kalo udah turun langsung.",
                "pesan": "Semoga makin sukses dan tetep jadi pribadi yang solid!"
            },
            {
                "nama": "Sarah Warti",
                "nim": "123450057",
                "umur": 20,
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwrti",
                "kesan": "Kakaknya ceria banget, selalu nyebarin senyum ke semua orang.",
                "pesan": "Semoga selalu bahagia dan terus semangat ngejar mimpi-mimpi kak!"
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": 19,
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": "Kakaknya chill banget tapi tetep ngasih kesan berwibawa.",
                "pesan": "Semoga terus jadi kak yang keren dan makin sukses di mana pun berada!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
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
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@dananghk_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@syalaishaa_31",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@den_iki_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@anadiacrn_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@aprhtp_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@nabila_zazahra",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@dhafinrzqa13",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@deviirhyu",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@englirahmdhanii",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@_inayasari",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "-",
                "asal": "-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@nydiaaptr_",
                "kesan": "-",
                "pesan": "-"
             },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
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
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak ciaa asik banget dan seruu bangeett",
                "pesan": "sehaatt selaluu dan selalu ceria kakk!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@rahmanellyana",
                "kesan": "pinterr bangeett dan ramah banget",
                "pesan": "semangaatt kuliahnya kakk!"
            },
             {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@mananam_",
                "kesan": "baikk dan sabar bangett ngajarin nyaa",
                "pesan": "semangaatt truss bangg!"
            },
            {
            
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@noe_rruuu",
                "kesan": "keren banget dan seru banget juga",
                "pesan": "semangaaatt kuliahnya bangg!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@rafidivaefangga",
                "kesan": "Seru banget abangnya dan ramah banget juga",
                "pesan": "semangaatt kuliahnya bangg"
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": "  ",
                "sosmed": "@refadp_",
                "kesan": "seruu banget kakaknya dan asik banget",
                "pesan": "semangatt kak kuliahnyaa, besok tepuk doa bareng ya kak wwkkwkw"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@tryyaniciaaa",
                "kesan": "seruu bangeet kak dan ramah juga",
                "pesan": "Tetap semangat kak kuliahnya!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@aliyaamara",
                "kesan": "kereenn kakaknya dan seru juga",
                "pesan": "Semangat kuliahnya kak!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@donamaya.p",
                "kesan": "Kakaknya seru banget dan ramah juga",
                "pesan": "Semoga sukses di masa depaann kaakk!"
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@writtenbyangel",
                "kesan": "baiikk bangeett kakaknya dan asik bangettt",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget suka bantuin kalau kesusahan ngerjain praktikum alpro",
                "pesan": "Sukses untuk ke depannya, kak dan selalu berbuat baik!"
            },
             {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@naylasalsabilaa",
                "kesan": "baiikk bangeett kakaknya dan seru juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
             {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@saniayyllstr",
                "kesan": "baiikk bangeett kakaknya dan seru",
                "pesan": "semangaatt kuliahnya kak dan bahagia selalu kak!"
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@i",
                "kesan": "baiikk bangeett abangnya dan ramah juga",
                "pesan": "semangaatt bang!"
            },
             {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@nltg._",
                "kesan": "baiikk bangeett kakaknya dan ramah juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@citrastin",
                "kesan": "baiikk bangeett kak dan asik juga",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@eigirtmv",
                "kesan": "baiikk bangeett kakaknya dan ramah bangett",
                "pesan": "semangaatt kuliahnya kak!"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": " ",
                "asal": " ",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@roms.slbn",
                "kesan": "baiikk bangeett kak, asik juga dan ramah bangett",
                "pesan": "sukses terus kedepannya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

    



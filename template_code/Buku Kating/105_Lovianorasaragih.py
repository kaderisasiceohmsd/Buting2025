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
            "https://drive.google.com/uc?export=view&id=1rhyBIj-JSnlp5gSjNATcwSQZFVE4SztW",
            "https://drive.google.com/uc?export=view&id=1xSmY4gzXd-RTFyZq2BVkEzKMYf0uqefz",
            "https://drive.google.com/uc?export=view&id=1C9JwAErAf7O6pqzYJImsPIYlNWXBBtbE",
            "https://drive.google.com/uc?export=view&id=17vEujPlAXKfR2z17VwaAEuQ_Xn4kBbU8",
            "https://drive.google.com/uc?export=view&id=1mokkAuIQlIna_TRCS5KnC7iSBvLrHEx0",
            "https://drive.google.com/uc?export=view&id=1xEfMcNiDD45l1UZg6oagm2pc5ei3t_f5",
        ]

        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Beli donat kentang",
                "sosmed": "@erendraa",
                "kesan": "keren banget, bisa mengayomi dan memberi contoh yang baik sebagai pemimpin  ",  
                "pesan":"semangat kuliahnya, jangan banyak begadang bang!"
            },
            {
                 "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Baca buku dasar-dasar",
                "sosmed": "@johannneskrijnnn",
                "kesan": "abang nya asik, suka bercanda kalau ketemu jadi membuat suasana ga canggung ",  
                "pesan":"semoga langgeng ya bang!!"
            },
            {
               "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak ini asik, lucu, kalau ketemu kakanya pasti yang kaya ceria bgt gitu",  
                "pesan":"semangat kuliahnya kakkk, semoga langgeng ya!"
            },
            {
               "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "kakanya baik, dan juga pengertian waktu wawancara kakanya takut kami sakit",  
                "pesan":"jaga kesehatan ya kakk, jangan sampe sakit"
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Rote, NTT",
                "alamat": "Rajabasa",
                "hobbi": "Baca buku, suka pramuka",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kaka nya asik, asal ketemu di ged f pasti diteriakain saudara ester",  
                "pesan":"tetap jadi orang yang ceria ya kak"
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@farahanumafifah",
                "kesan": "Kaka nya cantik banget, kalau senyum matanya ilang jadi imut",  
                "pesan":"semnagat kuliah ya kak"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [

            "https://drive.google.com/uc?export=view&id=1fcEdOZIVHYnJQd6tLWyrwSLG9MJhnqJM",
            "https://drive.google.com/uc?export=view&id=1vJzSxrSK1pdKK26Zaut-xTqm9dmztd52",
            "https://drive.google.com/uc?export=view&id=1lwZ0WVAHnoC81fC9NCRAHX8KCtjVyP4z",
            "https://drive.google.com/uc?export=view&id=1VlXBbw6ybF3gM3BV7vNMca3-KrNER9nj",
            "https://drive.google.com/uc?export=view&id=1ETs8Sl6TO0TX_dDxOCNCutbvLprMZGyf",
            "https://drive.google.com/uc?export=view&id=1s7ytZFPg-CokLo-p_ZIHd8VLqjzk6m3W",
            "https://drive.google.com/uc?export=view&id=1FSicXBKv2bzGNS6VX7xVgkn_3pM0ry88",
            "https://drive.google.com/uc?export=view&id=1U43tK9CCB60E_oSXvp4AEuPKJ4C4OuTp",
            "https://drive.google.com/uc?export=view&id=1Kdxhau7BNIf8FIc4GarkOZ7fVPsOn19A",
            "https://drive.google.com/uc?export=view&id=11duh1A4-QD3CT5yVf6wVSr-R5vfYQ_Rk",
            "https://drive.google.com/uc?export=view&id=1aBDdeBbuFtAhyP3nrWJy5OnKbtn_q8MY",
            "https://drive.google.com/uc?export=view&id=1jPqoMANhzhlbUq8w0dAsx7MtWOqO4L6v",
            "https://drive.google.com/uc?export=view&id=1SCCzNJ31gX5ekUB_2md4biE_etf_S21O",
            "https://drive.google.com/uc?export=view&id=1RGpKA61B3-7mVvkag1WoAj6Z6NKRPKy1",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Yapping",
                "sosmed": "@Jeremia_s_",
                "kesan": "bang jere inspiratiff, pengen jadi pemandu lkmm jg karena liat bang jere.",
                "pesan":"sukses selalu bang kuliah nya, jangan lupa makan ya"
            },
             {
                "nama": "Dhea Amelia Putri",
                "nim": "",
                "umur": "20",
                "asal":"Chiwidew, Jawa Barat",
                "alamat": "Pesawaran",
                "hobbi": "Pawat Piwit",
                "sosmed": "@_.dheamelia",
                "kesan": "kaka nya seru, asik, suka sama cara ngomong buat suasana cair",
                "pesan":"stay heboh ya kak!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk, Bandar Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Tidur",
                "sosmed": "@Renishapg",
                "kesan": "suka sama style kaka nya, kalcer",
                "pesan":"stay kalcer kakk!!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Lubuk Linggau",
                "alamat": "Pringsewu",
                "hobbi": "Hafalin sandi Morse",
                "sosmed": "@ansftynn_",
                "kesan": "kaka nya cantik, imut, suka sama senyum nya lucu.",
                "pesan":"selalu jaga kesehatan ya kak"
            },
             {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Way halim, Bandar Lampung",
                "alamat": "Way halim, Bandar Lampung",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "abang nya inspiratif, punya banyak pengalaman, pengen kaya abang nya juga",
                "pesan":"tetap jadi panutan bang."
            },
             {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "17",
                "asal":"Bekasi",
                "alamat": "Way huwi, Bandar Lampung",
                "hobbi": "Main karambol",
                "sosmed": "@fby.wlndr",
                "kesan": "kaka nya lucu, suara nya imut bgt, ga nyangka orang seimut itu main voly",
                "pesan":"semangat kuliah nya kak"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Teluk Betung",
                "alamat": "Teluk Betung",
                "hobbi": "Dengerin Spotify",
                "sosmed": "@givarooo",
                "kesan": "vibes abang nya kaya tegas dan berwibawa",
                "pesan":"jaga kesehatan, jangan lupa tidur"
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@myrrinn",
                "kesan": "abang nya wangi bgt, vibes nya kaya seger terus gitu.",
                "pesan":"spill cara wangi tahan lama bang"
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "124450065",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@berlyyanda",
                "kesan": "orangnya cantik banget, lucu, senyum nya manis",
                "pesan":"tetap jaga kesehatan ya kak, jangan sampe sakit."
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Dengerin Lany",
                "sosmed": "@j_eesie",
                "kesan": "Ka juju cantik bgt, ramah, vibe nya kaya cewe kue.",
                "pesan":"SPILL SKINCARE NYAA KAKKKK!!!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Medan",
                "alamat": "gang sekuntum",
                "hobbi": "Main pedal",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang nya tipe orang yang tegas dan ga neko neko",
                "pesan":"semangat kuliah nya bang"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "orang nya baik, ramah juga",
                "pesan":"semangat kuliahnya bang, kuliah dibawa santai aja"
            },
             {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@monica_tjg",
                "kesan": "ka monicc, cantik bangettt, baik, ramah lagi, suka nolongin kalau aku butuh, sering kasih tips and trick kuliah ",
                "pesan":"semnagat kuliah nya kak, jangan sampe sakit dan telat makan ya kak"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "17",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Tiktokan bareng sahroni",
                "sosmed": "@nshaysk",
                "kesan": "Pembawaan kaka nya asik dan lucu",
                "pesan":"tetap jadi orang yang lucu ya kak"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1caD2ghFiCmmgf-8zwFzttqX34SwFnift",
            "https://drive.google.com/uc?export=view&id=1jlszDhveixiuVEK6-MCOvrQjm5MJjTh4",
            "https://drive.google.com/uc?export=view&id=1bWBtoGDU4WhTYsugWklLWWDm-aHU1YVv",
            "https://drive.google.com/uc?export=view&id=1ZSPLT6X2X-Ux_XgWTdLOTIn2O9txk2Kj",
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
                "kesan": "jokes abangnya lucu, waktu wawancara abangnya buat suasana ga canggung",  
                "pesan":"tetep lucu ya bang"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "kaka nya cantik bgt, vibesnya kaya cewe lemah lembutt gitu",  
                "pesan":"tetep baik hati ya kak!"
            },
             {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Mendengarkan musik sambil jalan",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakanya cantik, keliatannya baik banget dan alim gitu, dan kaya cewe tenang yang ga gampang panik",  
                "pesan":"tetap jadi orang baik ya kak"
            },
            {
              "nama": "Lia Hana Ichisassmita",
                "nim": "123450089",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Rebahan",
                "sosmed": "@lia.h_264",
                "kesan": "vibes kaka nya kaya independent women, keliatan wibawanya gitu",  
                "pesan":"Tetap jadi cewe yang mandiri ya kak"  
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1m8wqPuBXUQSpt9_boNuGKg8_dYmow1D8",
            "https://drive.google.com/uc?export=view&id=15Tpdg1SboT0jvVccoM56KxLNOeI-iMaq",
            "https://drive.google.com/uc?export=view&id=1waCdeivGxQg_oUvTvQvT8lW7doCI-bcQ",
            "https://drive.google.com/uc?export=view&id=1SUAWZ_bKotuTA5DbZoHVkbwHRdJUk3My",
            "https://drive.google.com/uc?export=view&id=1Ps6lZODw8-Ui_SkajO5h97sJPc94R5ga",
            "https://drive.google.com/uc?export=view&id=1SKoYnDzlfFNWXmNl-RW5WC1A8qJPA0xj",
            "https://drive.google.com/uc?export=view&id=1CdFrx_hwcDkGKfhsLil2y10SQ-z_fecf",
            "https://drive.google.com/uc?export=view&id=1T3Re_DGquJnbI2GQLtrKZOmegGhBfvRx",
            "https://drive.google.com/uc?export=view&id=1Bilh_tgjdGOSyDYOIu1Y9JXZzpwml9Ul",
            "https://drive.google.com/uc?export=view&id=1opQI4PUrOBGVJIcFsm1rSNiuF7RH2YW3",
            "https://drive.google.com/uc?export=view&id=1hZMJFbRX9xjTn-sL8JDqhVnYUJAtJYB7",
            "https://drive.google.com/uc?export=view&id=1UU6t74_coXcC5194IgCzucKxlhA9ncez",
            "https://drive.google.com/uc?export=view&id=1nl5PudtKS7o46kXRdTSYzuDRQZtUhsd4",
            "https://drive.google.com/uc?export=view&id=1yKClOH8VAR9ug0TLSSkJlCgKfmvxJeBE",
            "https://drive.google.com/uc?export=view&id=171oeQAygyBVNqXXLzK8eWv0t3UlOx7pv",
            "https://drive.google.com/uc?export=view&id=1PBOZqpzuK7uqKY27kV42WjI1STL74uKV",
            "https://drive.google.com/uc?export=view&id=1q3khtj0Lj-cy9e9VrSPWTDfu9h0kZC_5",
            "https://drive.google.com/uc?export=view&id=1SU88D6MsT8KXux7uAWP_8PylHoRDPfbe",
            "https://drive.google.com/uc?export=view&id=1t25Odfo7yDA6NJB9JsnWSQzkfAMIGPBv",
            "https://drive.google.com/uc?export=view&id=1y05Ly3Heq_-H_cEdJrpdQ15tx3bsypFg",
            "https://drive.google.com/uc?export=view&id=1Q1iafpHA5gv8C9cgQSVXls7bdFcT33WP",
            "https://drive.google.com/uc?export=view&id=1Ok7kCW6Q0Yov6fw-Ceiz-iHbxqxOeRRO",
            "https://drive.google.com/uc?export=view&id=1b8-D52AErLiCsOjEDWIeqDWBsy6YMiAC",
            "https://drive.google.com/uc?export=view&id=1xzqNNqhbod10XkQgTjJI_I_SgnKKcunn",
            "https://drive.google.com/uc?export=view&id=17FHXA0NTBtl48TbwFZDB3k6f07aT2BCG",
            "https://drive.google.com/uc?export=view&id=1QxzPrYamc3l_asSQnuqiL4vWfKEL6R9V",
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
                "kesan": "Kakaknya asik, cantik dan tegas terlihat seperti independen women",
                "pesan": "Sehat selalu, dan lancar segala urusannya kak."
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyapasha_",
                "kesan": "Kakaknya asik dan baik banget, dan juga tegas, terlihat seperti wanita dominan",
                "pesan": "tetap jaga kesehatan kak"
            },
             {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "saya senang mendapat arahan dan motivasi dari abangnya karena dapat saya gunakan dalam kehidupan perkuliahan.",
                "pesan": "Semangat terus kedepannya bang, walau banyak rintangan pasti bisa dihadapi."
            },
             {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Airan",
                "hobbi": "Main Blockblast",
                "sosmed": "@arientakhsnl_",
                "kesan": "Pembawaannya tenang dan keren gitu",
                "pesan": "Sukses selalu untuk kakak, jangan lupa istirahat."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Toraja",
                "alamat": "Airan",
                "hobbi": "Jahilin Miyor",
                "sosmed": "@daffahdynn_",
                "kesan": "abang nya aslinya baik walau terkadang agak galak",
                "pesan": "Sehat selalu bang, semoga segala urusannya lancar"
            },
             {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Main game, Baca, Badminton, Gitar",
                "sosmed": "@ginda_mrp",
                "kesan": "abangnya tegas, dan sedikit berbicara sehingga terlihat berwibawa",
                "pesan": "semoga studi nya lancar tanpa ada gangguan"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat",
                "hobbi": "",
                "sosmed": "@natasyamavisca",
                "kesan": "kaka nya cantik, tegas danb tidak suka menye menye, sehingga terlihat seperti wanita penuh wibawa",
                "pesan": "terimakasih selama ini udah ikut andil dalam membimbing kami"
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Wisma Emas Setengah",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "abang nya sering memberikan arahan, motivasi dan didikan untuk kami, beliau jg  bersifat tegas, jadi terlihat berwibawa",
                "pesan": "Semangat terus dalam menjalankan amanahnya, Kak!"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "abang nya memberikan bimbingan yang berharga, yang bisa dipakai kedepannya",
                "pesan": "Semangat kuliahnya bang, jangan lupa istirahat."
            },
             {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Senang berbicara",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kaka nya lucu dan cantik, kadang suka berperilaku random yang membuat nya jadi makin kelihatan lucu.",
                "pesan": "semangat kuliahnya kak, jangan sampai sakit."
            },
             {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Voli",
                "sosmed": "@shahid22_",
                "kesan": "abang nya asik, ramah dan suka tersenyum",
                "pesan": "semangat kuliahnya bang, jangan lupa tidur"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kuliner malam jika ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "Senang bisa kenal abang nya, abang asik",
                "pesan": "Semoga studinya lancar dan sukses terus ya, bang."
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@feraztaaa",
                "kesan": "kakanya baik, cantik, bisa menjadi sosok kaka yang membimbing adiknya, selalu nginetin buat makan, jaga kesehatan selalu nayain kabar, ramah lagi, KEREN BGT BUAT KAKA NYA.",
                "pesan": "SEMANGAT KULIAH NYA KAK, SEMOGA SEMUA URUSAN KAKA DIPERMUDAH."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya cantik, baik, dan asik",
                "pesan": "jangan lupa istirahat ya kak"
            },
             {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakak nya asik bgt, baik lagi ",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
              {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "abangnya terlihat cool dan jarang bicara, tapi kalau ketemu tetep ramah.",
                "pesan": "Sukses selalu bang, semangat kuliahnya"
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnoval_11",
                "kesan": "Kakaknya asik dan lucu, kadang kasih lelucon yang buat suasana ga canggung.",
                "pesan": "semoga lancar perkuliahannya."
            },
             {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya baik dan keren banget waktu jadi dancer",
                "pesan": "Sehat selalu kak, semangat nge dance nya."
            },
             {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Nangkap lele",
                "sosmed": "@ihsan.yusuf",
                "kesan": "abang nya asik, candaan nya lucu, dan abang nya bisa menyesuaikan mana keadaan serius dan bercanda",
                "pesan": "Sukses selalu ya, bang!"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Duduk",
                "sosmed": "@kevinaj_",
                "kesan": "abangnya baik banget, bertanggung jawab sama janji yang udah beliau buat",
                "pesan": "Semoga studinya lancar, dan sehat selalu bang."
            },
             {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kaka lidia baik banger, lucu aku suka sama rambut kakanyaa mirip moanaaa",  
                "pesan":"semangat terus kuliahnya kakakkkk"
            },
             {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nghina orang Bengkinang",
                "sosmed": "@ridwan122",
                "kesan": "abangnya lucu banget, kalau lagi ketawa, ketawanya nular.",
                "pesan": "sehat selalu bang, jangan lupa ketawa"
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "abang nya lucu, dan suka random tiba tiba senyum kaya mau ketawa gitu",
                "pesan": "Semoga studinya lancar dan sukses terus ya, bang"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "abang nya banyak ngajarin soal keyboard, keren beberapa kali ngasih tutorial belajar baik",
                "pesan": "Sukses selalu ya bang"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakak ini asik dan lucuu",
                "pesan": "semangat terus kuliahnya kakk, jangan lupa jaga kesehatan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15xhrzNCkgpbW1t4IHVVxRbpgPGlpvCJ4",
            "https://drive.google.com/uc?export=view&id=1ri9KYnY3eyfTUyLSaGe7tgyrmcA__dZw",
            "https://drive.google.com/uc?export=view&id=1KUaxAFH-qrytc_CptZtU2Lub6Zmcpaoj",
            "https://drive.google.com/uc?export=view&id=1fpuhaKwMkS0NLHQZDTz_XBP7K4TmgD-T",
            "https://drive.google.com/uc?export=view&id=1j9X0k_XhqB0Rxg3Ovmzmu3Dy9GwBkSw3",
            "https://drive.google.com/uc?export=view&id=14iA2HoCfaFfhmc4dnzkLMyuB3rmDlL58",
            "https://drive.google.com/uc?export=view&id=1ROmC6-hdUbujz-89klkGqERBgOxXAoc6",
            "https://drive.google.com/uc?export=view&id=12Sf7FQ1eQ0BJqCg3GOfCfj-auEuef-1z",
            "https://drive.google.com/uc?export=view&id=1HvdACmQOuUROEbo7J6s1Bua9yNuKGueK",
            "https://drive.google.com/uc?export=view&id=1NhYILheq_A4UG0MCOZfGVIA-UaletI0r",
            "https://drive.google.com/uc?export=view&id=1x9Q_c98WfZl-PqzovOxYWMXyhGEgTHxr",
            "https://drive.google.com/uc?export=view&id=1fxmZJgPnVBgfdECTrCqjhGbAPRjrePMB",
            "https://drive.google.com/uc?export=view&id=13jzU_i9J05yoGS5LkNSaeuRys3z-Cguu",
            "https://drive.google.com/uc?export=view&id=14yEM73VeJSF_SMVTb1_mIWjAI-TRJtaO",
            "https://drive.google.com/uc?export=view&id=1l7FGkvMHUy3zhLwRDAzqnjspVooW7mEy",
            "https://drive.google.com/uc?export=view&id=1Ky50zlRJ85v3ydpmu5Eq7P6IsRO6qRlp",
            "https://drive.google.com/uc?export=view&id=1rxsE8mSQr0xhdgO8Kder8AVAhvG3XzOO",
            "https://drive.google.com/uc?export=view&id=1ysHCHaG0dAKwnO0UUuJelmuJ_2QzkhfP",
            "https://drive.google.com/uc?export=view&id=1N7FOB7uAYUQpr98oRvgivUWlvh3KGjWx",
            "https://drive.google.com/uc?export=view&id=17AU4aIRMfGAvfc9nEx2W2ieHFy69rVDd",
            "https://drive.google.com/uc?export=view&id=1qIXP-PwnB0-z3O1_P_h7hphPyaPNX7pc",
            "https://drive.google.com/uc?export=view&id=1vxIXP-WvopBEs_5USWGnsJsv45qLjpKh",
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
                "nama": "Tanty Widiyastuti",
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
                "nama": "Anggi Puspita Ningrum",
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
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1m2oZGF4gy1-8hwII1GUCUN-zdghaqFq1",
            "https://drive.google.com/uc?export=view&id=1wnNFBdj5KdklWnLV6FPpnkQJjeu2Mfb3",
            "https://drive.google.com/uc?export=view&id=1LfTiDCBg7bVMXyzMAnjxTUCS2N0c2J4V",
            "https://drive.google.com/uc?export=view&id=12D6Lrndq_0zhV4y8a9wDg_PprBJ9jj85",
            "https://drive.google.com/uc?export=view&id=15DqCxNnjCGxEcW-IhNCaicfoYTFoPu9m",
            "https://drive.google.com/uc?export=view&id=1vEwV0wuj4WFfS9i--2me2Enj1LYifwTA",
            "https://drive.google.com/uc?export=view&id=1HbacwYTWIwvJK1pKf95RHe5rf5DQSMBI",
            "https://drive.google.com/uc?export=view&id=1LvXN1ae_Hcg1u69T_KgMb-B2qsxYjzxX",
            "https://drive.google.com/uc?export=view&id=1XTtaWyj9RDMBHt0rBvFAZgAdAu0w00Y4",
            "https://drive.google.com/uc?export=view&id=1IWQyfTmrUakLwtSwe1tsYjc4ghUAI6io",
            "https://drive.google.com/uc?export=view&id=1FR2holjt0V1JLT4vBSiw2jHVPp2H_6jQ",
            "https://drive.google.com/uc?export=view&id=14HTjd2WRWOgM9bZG1SPgRTBDWSwi5eKE",
            "https://drive.google.com/uc?export=view&id=134fyRSgzGCb_d74z7iFUbI43eHK7V4YR",
            "https://drive.google.com/uc?export=view&id=1WZy09-zIwGETQeu1l72pP5YE089qUhRV",
            "https://drive.google.com/uc?export=view&id=1wHlZ3Wz0-IRdgEgLWYO8dT5DI_h0sIs5",
            "https://drive.google.com/uc?export=view&id=1QFXaW88LIt97aBnqwW9y2d5PhITLG2v4",
            "https://drive.google.com/uc?export=view&id=1jhW6uNjg8poNLtKpYIzJIxsknPuT2gIZ",
            "https://drive.google.com/uc?export=view&id=1zEFJCEI9Qtrk4AMPbZrlp6YqqBnCRytM",
            "https://drive.google.com/uc?export=view&id=1WA00q3d64y6paeigamwEWIq-1DANH0SB",
            "https://drive.google.com/uc?export=view&id=1g2nzhtv6JB2kMZr56Z9lJOISrixSD-JL",
            "https://drive.google.com/uc?export=view&id=1EEicv3zp7DzYs5T5blnCkwCwHOrigdj1",
            "https://drive.google.com/uc?export=view&id=13-mXrBzRZAsUmIynbEyewD4fMNgCfss8",
            "https://drive.google.com/uc?export=view&id=1MZMO0xEZRAw9P8s6IUWHfB6QXikOQGGW",
            "https://drive.google.com/uc?export=view&id=1eemz8PNBWQu3_dR-OAe9WH6Vrr5Y6ioW",
        ]
        data_list = [
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Arafi Putra Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana:",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"usul",
                "alamat": " jl. hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gg.sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 Tahun",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya ",
                "sosmed": "@cindylauura",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                 "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 tahun",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Like crowded ",
                "hobbi": "gibah sama lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Syahrialdi Rachim Akbar ",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchmnim",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan ",
                "alamat": "Sukarame",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa_",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Kak!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17 tahun",
                "asal":"Swiss",
                "alamat": "Pemda ",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "Senang bisa kenal dengan kakak, orangnya ramah.",
                "pesan":"Sukses selalu untuk kakak ke depannya!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "Orangnya menyenangkan dan mudah bergaul.",
                "pesan":"Semoga apa yang dicita-citakan tercapai ya, Kak."
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 Tahun",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 Tahun",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "Kakak sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, Kak."
            },
            {
                "nama": "Nurul Izzah Istiqomah ",
                "nim": "123450054",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "Sangat berkesan, pembawaannya positif.",
                "pesan":"Terima kasih atas semua pelajarannya, Kak!"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BO6Q5TGBt6uHitFlq6iJn0RxM3gkRl-P",
            "https://drive.google.com/uc?export=view&id=1AAu5SSKS-Ehfgyby04gG08hsoaNgdMRL",
            "https://drive.google.com/uc?export=view&id=1CZ4xz0ycLUgSSoFqcWoE-HGors41jrjL",
            "https://drive.google.com/uc?export=view&id=1qLK7wjrf4I_Dm8pWAmcEAL5fGAKjHj4d",
            "https://drive.google.com/uc?export=view&id=1Da9keXsGnBl_Gge6MZ_Ua4tds_dFSPcY",
            "https://drive.google.com/uc?export=view&id=16fT__eOYTrRsyIirykRNV4xd3jC2l6Uy",
            "https://drive.google.com/uc?export=view&id=1ltiuXDJm49kgZZs7DDUNxxdXO2b7-EFP",
            "https://drive.google.com/uc?export=view&id=1ZCb0gkcdiAent9JiyK3W3B4G5I3oWLkg",
            "https://drive.google.com/uc?export=view&id=1b5hddOAd1hFhpkggGaK34--v0AU89D3f",
            "https://drive.google.com/uc?export=view&id=1T8HbfLmz7vVDuu7ryDsyLOAWv6kiV-sj",
            "https://drive.google.com/uc?export=view&id=1BnsFmkU4dC0Jd1h_2zA2h_x2_MYlqRCt",
            "https://drive.google.com/uc?export=view&id=1RvBpeOAUhIeq7ytyBh7oWpCSVOH444QT",
            "https://drive.google.com/uc?export=view&id=11GV77ZqIVPjqnoF0DPxNtAxHr8TssmCT",
            "https://drive.google.com/uc?export=view&id=1IAYYeTAdk5dJA5l9363ZPVn9GgVP2AdM",
            "https://drive.google.com/uc?export=view&id=11LOQp43VlkN-ajzEHXVwCMk8JGDcRfw-",
            
        ]
        data_list = [
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "Kakaknya baik dan supel.",
                "pesan": "Sukses selalu ya, Kak."   
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal": "Brebes, Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Memanah",
                "sosmed": "@salwa_fhn",
                "kesan": "Senang bisa kenal sama kakak.",
                "pesan": "Sukses terus buat ke depannya ya, Kak!"
            },
            {
                "nama": "Haikal Fransisqo Simbolon",
                "nim": "123450106",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Balapan",
                "sosmed": "@haikalsbln_",
                "kesan": "Kakaknya seru dan suka membantu.",
                "pesan": "Semangat terus kuliahnya, Kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalu",
                "nim": "122450057",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Airan",
                "hobbi": "Menyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Kakaknya humble dan mudah diajak ngobrol.",
                "pesan": "Semangat terus ya, Kak, jangan sungkan sapa kami."
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "123450064",
                "umur": "20",
                "asal": "Kota Padang",
                "alamat": "Prumnas Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hndzky_",
                "kesan": "Senang bisa satu himpunan sama kakak.",
                "pesan": "Semoga urusannya dipermudah selalu, Kak."
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya asik dan seru.",
                "pesan": "Semoga urusan kuliahnya lancar selalu, Kak."
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal": "Kota Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Bermain alat musik",
                "sosmed": "@sarahwsti",
                "kesan": "Kakaknya asik untuk diajak diskusi.",
                "pesan": "Lancar-lancar ya, Kak, kuliahnya."
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Melihat cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik dan friendly.",
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya baik banget dan ramah.",
                "pesan": "Sehat dan semangat terus ya, Kak!"
            },
            {
                "nama": "Keren Marito Lumba Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Way Hui Pemda",
                "hobbi": "Main musik",
                "sosmed": "@kerenmrtv",
                "kesan": "Kakaknya baik dan seru.",
                "pesan": "Semangat terus, Kak!"
            },
            {
                "nama": "Azzahra Putri Kamila",
                "nim": "123450013",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Asrama TB4",
                "hobbi": "Memasak",
                "sosmed": "@azza.rrr_",
                "kesan": "Kakaknya ramah banget.",
                "pesan": "Sehat dan bahagia selalu, Kak!"
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "Kakaknya asik banget.",
                "pesan": "Sehat selalu, Kak!"   
            },
            {
                "nama": "Zahra Putri Salsabilla",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Urip",
                "hobbi": "Berkuda",
                "sosmed": "@may_dahlia12",
                "kesan": "Kesan pertamanya positif banget, Kak.",
                "pesan": "Semoga kita bisa makin akrab ya, Kak."
            },
            {
                "nama": "Muhammad Naufal Alghani",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VMpTjAF2Uxcy3NJFvDxbc_taWPW_H8Lr",
            "https://drive.google.com/uc?export=view&id=1foPS-3AJznB2Q-vO5jaPqS7ND6SuEcw7",
            "https://drive.google.com/uc?export=view&id=1owTdMFjKC2wg9ilrWjndp7ITXCG4WAun",
            "https://drive.google.com/uc?export=view&id=1mG124ku9_kycVYx_MJ_NRMFVhseeIGUm",
            "https://drive.google.com/uc?export=view&id=1mG124ku9_kycVYx_MJ_NRMFVhseeIGUm",
            "https://drive.google.com/uc?export=view&id=1WSdAR_Sf8XohUUjYhQ5F7ZV7IRSz-MhE",
            "https://drive.google.com/uc?export=view&id=14O0I6VyeErdV858QeGe_wcwF-aSbU0xX",
            "https://drive.google.com/uc?export=view&id=1mG124ku9_kycVYx_MJ_NRMFVhseeIGUm",
            "https://drive.google.com/uc?export=view&id=1-Nhs6cnOkm0FBtpdTXM7NBtJI4vjoJOO",
            "https://drive.google.com/uc?export=view&id=1FEbnQtYCNFcr9SxH6MTKGtzVBVbMgKh_",
            "https://drive.google.com/uc?export=view&id=196L9hNn-U4sFVXK49W-s-BcX9ZAV84He",
            
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
                "kesan": "Kakaknya asik dan seru, pertama kali kami wawancara langsung ditawarin beli ganci",
                "pesan": "Semangat jualan ganci nya bang!!"
            },
              {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "kakanya lucu, cantik, lucu lagi",
                "pesan": "Semoga sukses selalu kuliahnya!"
            },
             {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "awalnya ngira abang nya pendiem gitu, ternyata ngga",
                "pesan": "Sehat selalu ya, bang"    
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya keren dan cantik, kalau senyum cantik bgt gitu",
                "pesan": "Semangat terus kuliahnya kak, jangan lupa istirahat ya" 
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "kaka nya manis bgt, kalau senyum makin manis",
                "pesan": "jangan lupa istirahat ya kak"
            },
             {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "kakanya seru bgt kalau ngobrol, topiknya asik gitu",
                "pesan": "Semangat terus ya kak kuliahnya"
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Kakaknya asik diajak diskusi soal cara menjadi wirausahawan yang baik.",
                "pesan": "Terimakasih atas sharing ilmunya bang"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik murah senyum, dan ramah kalau ketemu",
                "pesan": "jaga kesehatan ya kak"
            },
             {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "@englirahmdhnii",
                "kesan": "kakanya asik dan seru diajak ngobrol topiknya ga mati disebekah pihak dan mengalir aja",
                "pesan": "Semoga sukses selalu ya kak!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya sangat ramah, dan juga ceria, kakanya meyakinkan kami kalau ads ga susah",
                "pesan": "sehat selalu ya kak!"
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang",
                "hobbi": "Main",
                "sosmed": "nydiaaptr_",
                "kesan": "kakanya ramah, baik, cantik",
                "pesan": "Semangat dan sukses selalu!"
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gwTymYwQzjgUezyDQ9zO0CECJ8ReNIBz",
            "https://drive.google.com/uc?export=view&id=10A1dsOYuvXFBk7reEtG37bwIH-KRSYxX",
            "https://drive.google.com/uc?export=view&id=1q1HUnkaZ9_e4Hip_36Eo4bnxt6xFOX7N",
            "https://drive.google.com/uc?export=view&id=1qKa576aRVwfw4ud5OEIiNsB-j6n1kQPl",
            "https://drive.google.com/uc?export=view&id=1348u5gBZ41MHLWI435PS9j4pQFMbQKgG",
            "https://drive.google.com/uc?export=view&id=1F5iY7m4gNG-UZTl9MJ1UsfNdv3FnC8Id",
            "https://drive.google.com/uc?export=view&id=10pa2TCMEMWVCrP4sQF3RbccdrR6YH5QQ",
            "https://drive.google.com/uc?export=view&id=1r8004aIocwrpDszsGPW0srmxTpgRw_vB",
            "https://drive.google.com/uc?export=view&id=14_KhYmCKb4lwtf0ukaSQ-7qN1-sAjCoK",
            "https://drive.google.com/uc?export=view&id=1rYWjxvDaTeL2eoLDYl48aaxCP3ply7Yf",
            "https://drive.google.com/uc?export=view&id=1yOTtD1H-EM_C2ACev3uwCNZx2SbBOmbJ",
            "https://drive.google.com/uc?export=view&id=1000E4pEcgRevoSNX2h7VvlHmyoN-WRgM",
            "https://drive.google.com/uc?export=view&id=1FtvpsWVnx_gI3uJqsbre5xrEW5Fh1qcg",
            "https://drive.google.com/uc?export=view&id=1rCV0Ec3U1BZRCf_hpXa1dYGKr7LbNpDU",
            "https://drive.google.com/uc?export=view&id=195ikhN8V8pwVG9ZlvwR79I0uN6-ojqlt",
            "https://drive.google.com/uc?export=view&id=1oL6bdeCmZuVXOGXY_9Vrw-LbPJRk0U0F",
            "https://drive.google.com/uc?export=view&id=1BMfg9j9xXHSMMw3v14TyKiOWQXHVV9_t",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "Kakaknya asik diajak diskusi",
                "pesan": "Lancar terus ya kak kuliahnya!"
            },
            {
                "nama": "Dona Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mendengar musik",
                "sosmed": "@donamaya.p",
                "kesan": "Terima kasih sudah berbagi ilmu",
                "pesan": "Semoga sukses di masa depan!"
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Lapas Raya, Jati Agung",
                "hobbi": "Dengerin musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "Kakaknya seru dan pintar",
                "pesan": "Sukses terus untuk karirnya nanti."
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Korpri, Sukarame",
                "hobbi": "Gym, Masak",
                "sosmed": "@i",
                "kesan": "Belajar sama kakaknya jadi menyenangkan",
                "pesan": "Semoga lancar terus kuliahnya!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya sangat membantu dan baik",
                "pesan": "Tetap semangat, kak!"
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main Hp",
                "sosmed": "@i",
                "kesan": "Orangnya asik dan mudah bergaul",
                "pesan": "Semangat terus kak kuliahnya!"
            },
            {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "Pengalamannya keren dan menginspirasi",
                "pesan": "Teruslah berkarya, kak!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya baik banget",
                "pesan": "Sukses untuk ke depannya, kak!"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "Sangat berkesan bisa diajar kakak",
                "pesan": "Semoga sehat selalu, kak."
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Sabah Balau",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "Kakaknya keren dan inspiratif",
                "pesan": "Semoga apa yang dicita-citakan tercapai."
            },
            {
                "nama": "Refa Destini Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Mengoleksi Gelang",
                "sosmed": "@refadp_",
                "kesan": "Senang bisa belajar bareng kakak",
                "pesan": "Semoga sukses selalu menyertai."
            },
            {
                "nama": "Labo Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Gg.sakum",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "Kakaknya friendly dan baik hati",
                "pesan": "Sehat dan sukses selalu, kak!"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lamsel",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep Call",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kakaknya asik dan seru",
                "pesan": "Sukses selalu ya, kak!"
            },
            {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "Seru banget bisa kenal kakak ini",
                "pesan": "Semoga sehat dan sukses selalu"
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Kelengkeng 2",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "Kakaknya ramah dan humble",
                "pesan": "Terima kasih atas bimbingannya, kak."
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Suasananya jadi asik kalau ada kakak ini",
                "pesan": "Jangan lupa jaga kesehatan ya, kak."
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@nltg._",
                "kesan": "Kakaknya sangat welcome dan ramah",
                "pesan": "Semangat terus dan semoga sukses!"
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@aliyaamara",
                "kesan": "Penjelasannya mudah dimengerti",
                "pesan": "Semangat terus kak, jangan menyerah!"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()
# Tambahkan menu lainnya sesuai kebutuhan

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
            "https://drive.google.com/uc?export=view&id=17edwoyummfCXAZDwjjkLAp_3qZP_mlAM",
            "https://drive.google.com/uc?export=view&id=1N6wTdKDTN7ZzuEfUVhQxTg5eNZlgQxVl",
            "https://drive.google.com/uc?export=view&id=1qZ91ESydnPhMg_jmjNQ7tEo7Ct-IZCdB",
            "https://drive.google.com/uc?export=view&id=1VuOpx1q2MGvfRCaSaEDBRFanweZRnWcL",
            "https://drive.google.com/uc?export=view&id=1jjfKzH4z0HLuGcvLSeOQYqoJI2kTOuqr",
            "https://drive.google.com/uc?export=view&id=1JOxI0AGFNpXYoXFs5DDiiJlCb7M3crd0",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": " Ikut lomba burung murai",
                "sosmed": "@erendraa",
                "kesan": "keren banget banggg bisa jadi ",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                 "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johannneskrijnnn",
                "kesan": "Abang ini asik saya suka belajar dari dia",  
                "pesan":"semangat terus kuliahnya bang, semoga cepat lulus !!!"
            },
            {
                "nama": "Eksanty F. Sukma Islamiaty",
                "nim": "122450001",
                "umur": "19",
                "asal":"Kelagian kecil, Pahawang",
                "alamat": "Pesawaran",
                "hobbi": "Ngambilin lanyard",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini suka bercanda",  
                "pesan":"sehat selalu kak, semangat kuliahnya !!!"
            },
            {
                "nama": "Farhanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal":"Padang, Sumatera Barat",
                "alamat": "Gya Kost",
                "hobbi": "Cute",
                "sosmed": "@farahanumafifah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
               "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Airest Kost",
                "hobbi": "Siram shopee",
                "sosmed": "@celisabeth_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
               "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XQ8hX1v-VWKz9t2DL1K08qzlfcmrQKTJ",
            "https://drive.google.com/uc?export=view&id=1Jk26Z5d7uGbcwgdU9C_t4wn92AFP4MZz",
            "https://drive.google.com/uc?export=view&id=1rvgfxBuQYerPAFJjQNEmtJWTJZVb_KFB",
            "https://drive.google.com/uc?export=view&id=1JfL3QJTNhPNwTgdE9wu_HrTc9Ql1ZT8E",
            "https://drive.google.com/uc?export=view&id=1lw_U8jA5CKj4mXHloXTHsiK9TgB60iez",
            "https://drive.google.com/uc?export=view&id=1mZS6RmMBzSlIYND1MnlAz6DMBVpDvi1t",
            "https://drive.google.com/uc?export=view&id=1diFUDUUpC6pforqWOT3lRrNTx-g-SpXb",
            "https://drive.google.com/uc?export=view&id=18xN6uRaMSZcFZNUUwCaZ1cCepBUR8PFc",
            "https://drive.google.com/uc?export=view&id=1ZL8Z4Wf9WarfwW_V25Sm2DRJ_GiAKDHQ",
            "https://drive.google.com/uc?export=view&id=1GqHtei9Wegd0qTq4doDmx6aFSBusIdlS",
            "https://drive.google.com/uc?export=view&id=1RDczTNsGUPOMWrN3JUySnkR4N0p6u6mu",
            "https://drive.google.com/uc?export=view&id=1C-Op4jLP2uqipK9-9pW-soYTGt3Vc4eh",
            "https://drive.google.com/uc?export=view&id=1Wa-aDXIezYvGQCQXFz3C_HiOtv3MADvL",
            "https://drive.google.com/uc?export=view&id=1oV-kufHZajvxGb2paS7P_IQwC7EZnptp",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal":"Tanjung Morawa",
                "alamat": "B2 no 2",
                "hobbi": "Main volly bareng feby",
                "sosmed": "@Jeremia_s_",
                "kesan": "Abang ku ini keren kali.",
                "pesan":"Semoga bisa cepat lulus ya bang!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal":"Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Kalo badmood liat zaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya lucu, suka bercanda.",
                "pesan":"Jangan lupa jaga kesehatan, kak."
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal":"Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin Alat Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya style kalcer sekali.",
                "pesan":"Jangan lupa jaga kesehatannya kak!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Wakatobi",
                "hobbi": "Bowling",
                "sosmed": "@ansftynn",
                "kesan": "Kakaknya baik dan ramah.",
                "pesan":"Semoga sehat terus kak."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyobain makanan baru",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini keliatannya ramah dan juga baik hati.",
                "pesan":"Lancar-lancar kuliahnya ya bang."
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "21",
                "asal":"Bandung",
                "alamat": "Way kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Sangat berkesan, orangnya humble.",
                "pesan":"Tetap jadi pribadi yang menginspirasi!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main ML pake franco",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya keren suka ngegame.",
                "pesan":"Jangan ngegame terus kak, istirahat juga perlu!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal":"Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "Walaupun hobbi kakak ini aneh, tapi tetap keren.",
                "pesan":"Semangat terus kak kuliahnya, jangan keseringan nyapa angin!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal":"Melbourne",
                "alamat": "GH",
                "hobbi": "Main Padel",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangku satu ini kece abis.",
                "pesan":"Gas kita tanding padel bang!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Abang ini seru dan lucu.",
                "pesan":"Jangan keseringan liat langit bang, sakit leher nanti."
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya punya hobbi yang cukup unik.",
                "pesan":"Jangan lupa sama namaku ya kak hehe"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "20",
                "asal":"Teluk Mondawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya asik dan ramah positive vibes pula.",
                "pesan":"Jangan galau terus ya kak."
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal":"Bandar Lampung",
                "alamat": "Way halim",
                "hobbi": "Nonton live putri padang",
                "sosmed": "@dhruchyo",
                "kesan": "Abang paling keren ini, ikut KKN Kebangsaan",
                "pesan":"Semangat menggapai Cumlaude bang."
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Mancing keributan",
                "sosmed": "@fby.wlndr",
                "kesan": "Kakaknya punya banyak gebrakan yang lucu.",
                "pesan":"Semoga bisa jadi atlit pro volly ya kak."
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yJJyZBwjxNxdsP3cGq78W88FcKGE0US6",
            "https://drive.google.com/uc?export=view&id=1Pr8a_9-w2mQYD-H9ln8x_Ch9N7CCbb8U",
            "https://drive.google.com/uc?export=view&id=1W3wNh8Qh3csCXP8uRlAFTQ_9Fu3Q6Nkm",
            "https://drive.google.com/uc?export=view&id=1Zfk_FGga8Hu3gC_ApX_4xg21JbLE7O5N",
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
                "kesan": "abangnya asik,humble, suka perunggu lagi",  
                "pesan":"tetep humble bang!"
            },
            {
              "nama": "Lia Hana Ichisassmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Main",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya ramah sekali",  
                "pesan":"Semangat terus kak dalam perkuliahannya kak"  
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
                "pesan":"Semangat terus kak, share-kan playlist kpop kak"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@nadyaanjani",
                "kesan": "Kakaknya seru diajak berbincang",  
                "pesan": "Jaga kesehatan ya kak, jangan lupa makan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zphPIDt6_40edT6QEi90FZsBa_Vsr3Sy",
            "https://drive.google.com/uc?export=view&id=1OyTkM9e4Lr6GOL50j1WZd9B2FBaY5XZ1",
            "https://drive.google.com/uc?export=view&id=1_qS33XzLWFdQpuKsCFYEhnRE6Xx6txKw",
            "https://drive.google.com/uc?export=view&id=1qrfNzMfcBTa0EXQElhexq5UMX4NujM3u",
            "https://drive.google.com/uc?export=view&id=1-P3DQKx4X1uHNtzvTF3KrpjS8n3AD-1Q",
            "https://drive.google.com/uc?export=view&id=1vnF9g2XtzQcshVhZJtRpRgPCzqzE7bkJ",
            "https://drive.google.com/uc?export=view&id=1olRVG9xCUAD03Qea2MwACUnuycq_YeFv",
            "https://drive.google.com/uc?export=view&id=1Bt12iLz1KjywyPk5H_ni3bd_XHtVyS4M",
            "https://drive.google.com/uc?export=view&id=12jIiTbVGW-ZayEzLLTWv7SwEF2q0PpsB",
            "https://drive.google.com/uc?export=view&id=1s25Em3XBUBIGfC6LN34iXdYGHaAseBYL",
            "https://drive.google.com/uc?export=view&id=1Z0zOeoyenXnem0xq29w9gx8LiDtXlSID",
            "https://drive.google.com/uc?export=view&id=1sZ0aVa90jNVHbjJxOUbMCBxT09y0gA0P",
            "https://drive.google.com/uc?export=view&id=147eepAt8o6pFUOlM1JnCr0OwtObVpYIw",
            "https://drive.google.com/uc?export=view&id=16QW5xefRz5o8MnjT1l7svzqjTnI_m4-1",
            "https://drive.google.com/uc?export=view&id=1YZqf3qgqbJQ4o2U5vjyAdv8GnOedJzWi",
            "https://drive.google.com/uc?export=view&id=1nCHUnt9SODK0qbJgWl5NhkRUYgYKnk6n",
            "https://drive.google.com/uc?export=view&id=1uYUqTOKFSxvw5Ec6b77CEOfxVqN3hFW_",
            "https://drive.google.com/uc?export=view&id=1GZMUroek4u_OsPggt_d3kCehIXUS92fO",
            "https://drive.google.com/uc?export=view&id=1tKJX2KWmmxVy6HfqbhYSPXwptT5wLOaV",
            "https://drive.google.com/uc?export=view&id=1UKSfM1vKnYEJq46WGFwtEsBmU-aK6dLa",
            "https://drive.google.com/uc?export=view&id=1Xwsi8FKjxqWvPtrDwmLSiyUad9mK-nwl",
            "https://drive.google.com/uc?export=view&id=12HlHNZHPZlPA1bRbwDyQ2kykqc75fNZv",
            "https://drive.google.com/uc?export=view&id=1fKkAzzyc8SYCUrxCGUAE8Vo2pphBcWK5",
            "https://drive.google.com/uc?export=view&id=1rLi7fL_N4WTb8ALd7bBaxYvXn2abSPtN",
            "https://drive.google.com/uc?export=view&id=1rOYfh4ejIMPvOHR0jQukYVpECVhFnRr4",
            "https://drive.google.com/uc?export=view&id=1bBjH-7ZmS_1IvHOWeE9RhteZw-KQUoQ0",
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
                "kesan": "Abang ini berwibawa dan humoris.",
                "pesan": "Ayo coba jadi stand up comedian bang!"
            },
            {   "nama": "Nisrina Nur Afifah",
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
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Main apapun",
                "sosmed": "@allyapasha_",
                "kesan": "Kakaknya asik dan juga pengertian. Terima kasih, Kak.",
                "pesan": "Sehat selalu dan lancar terus urusannya, Kak."
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Lari",
                "sosmed": "@sahid22_",
                "kesan": "Abangnya keren sekali.",
                "pesan": "Semangat terus kedepannya bang."
            },
            {
                "nama": "Daffa Ahmad Noval",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Rebahan",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "Abangnya kalem banget.",
                "pesan": "Sehat selalu ya bang, jangan keseringan rebahan bang."
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kost kak arienta",
                "hobbi": "Jahilin Putri",
                "sosmed": "@daffahdynn_",
                "kesan": "Abang ini seru dan kocak.",
                "pesan": "Semangat terus bang, jangan lupa istirahat."
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@sidabutar.26",
                "kesan": "Abang ini asik dan juga humoris",
                "pesan": "Sukses terus untuk lomba futsalnya bang."
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Lempar Batu",
                "sosmed": "@m.ridwan_22",
                "kesan": "Abangnya baik dan juga kalem",
                "pesan": "Hati-hati pas ngelempar batu ya bang, awas kena orang."
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, pemda",
                "hobbi": "Bikin project, ngoleksi data",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abang ini kece dan lucu.",
                "pesan": "Semangat mengoleksi data dan bikin projectnya bang"
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 55",
                "hobbi": "Ngoleksi pita pink",
                "sosmed": "@d__aniar",
                "kesan": "Kakaknya ramah dan baik juga.",
                "pesan": "Semangat koleksi pita pinknya ya kak."
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450023",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dla_natzzyaa",
                "kesan": "Kakak ini keren suka merajut",  
                "pesan":"Sehat selalu kak, jangan lupa istirahat"
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "Abang ini kocak dan serius di waktu yang sama .",
                "pesan": "Sukses selalu ya, bang!"
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin musik",
                "sosmed": "@rewinanaaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Panjang Selamat",
                "alamat": "Bandar Lampung",
                "hobbi": "Masak",
                "sosmed": "@kevinaj_",
                "kesan": "Abang ini jago main PES",
                "pesan": "Semangat dan lancar terus kuliahnya bang"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jln. Airan",
                "hobbi": "Main game",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya ceria dan ramah",
                "pesan": "Semangat terus ya bang, jangan lupa istirahat"
            },
            {
                "nama": "Gusti Putu Ferazka D",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaaa",
                "kesan": "Mentoku yang paling asik, cantik, lucu dan juga banyak gebrakan",
                "pesan": "Terima kasih sudah membimbing saya kak, sukses selalu dalam segala hal kak"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, Kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya santai dan kalem!",
                "pesan": "Infokan lokasi kulineran yang sedap bang"
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Belwis",
                "hobbi": "Main roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": "Kakak ini fun dan lucu",  
                "pesan":"Semangat terus kak, jangan lupa istirahat ya kak"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya lucu dan keren",
                "pesan": "Jangan keseringan scroll tiktok kak, nanti jadi brain root"
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "Abang ini baik dan juga ga pelit ilmu",
                "pesan": "Jangan lupa istirahat kalau burnout karena banyak hobi bang"
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450122",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma Family",
                "hobbi": "Mancing Emosi",
                "sosmed": "@ji_gumel17",
                "kesan": "Abangnya keliatan bijaksana dan kalem",
                "pesan": "Semangat kuliah ya bang, kiranya bisa lulus tepat waktu"
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Urip",
                "alamat": "Belwis",
                "hobbi": "Ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "Abangnya jago ngoding dan juga ga pelit ilmu",
                "pesan": "Jangan lupa tidur bang, jaga kesehatan"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Abang ini orang pertama yang kutemui dengan ambisi yang sangat besar",
                "pesan": "Sukses terus ya bang kedepannya, semoga jadi pemimpin yang amanah"
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal": "Pasar Muara Beliti",
                "alamat": "Kost putri gerbang barat samping bawah",
                "hobbi": "Belajar",
                "sosmed": "@natasyamavisca",
                "kesan": "Kakaknya tegas dan baik",
                "pesan": "Semangat dan sehat selalu kak"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Maju jaya kost",
                "hobbi": "Yapping sampai bete",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakak ini baik dan juga asik",
                "pesan": "Sehat selalu ya kak, semoga ga sering bete ya kalau udah yapping kak"
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Samping kost daffa",
                "hobbi": "Main Sudoku",
                "sosmed": "@arientakhsnl_",
                "kesan": "Pembawaannya tenang dan bijaksana.",
                "pesan": "Sukses selalu untuk kakak, jangan lupa jaga kesehatan kak"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Neyw6n46Ef_DRqEdvJzMlMu_IDazU20D",
            "https://drive.google.com/uc?export=view&id=1EINYWXMg6dIfBOAd5V7Fhvid4jWbKnqv",
            "https://drive.google.com/uc?export=view&id=1TwhoPXKij-Y1jC_OAM_524uWds4rjjz0",
            "https://drive.google.com/uc?export=view&id=1MMmhvj_86sPh1wbzjCsbvjvqPgnfENwM",
            "https://drive.google.com/uc?export=view&id=1yWAHysgtiKlxb0JO_-VgnOcSgA7culn2",
            "https://drive.google.com/uc?export=view&id=1EJ4XZsmoWSGZZ9aWAb4rQfTS2-7QM5eI",
            "https://drive.google.com/uc?export=view&id=1iK4fYjjuJzTrLNPjsdvSXIXwKwu1bJlO",
            "https://drive.google.com/uc?export=view&id=1fUXYTiK_yDvErVLsj4aCiwtrdssoCDJd",
            "https://drive.google.com/uc?export=view&id=1IrLhQzoGsot_-oF5CQp12MYYToopW8O2",
            "https://drive.google.com/uc?export=view&id=1NhYILheq_A4UG0MCOZfGVIA-UaletI0r",
            "https://drive.google.com/uc?export=view&id=1X-u0iDOzFrGM11sklEYTA7i0-RIHgitX",
            "https://drive.google.com/uc?export=view&id=1Hb-G79Ddw0ZwROL9JHZsHa3c4toYrANF",
            "https://drive.google.com/uc?export=view&id=1Yo8YIdNLRJ3omyaxwFyUl7QGt9WyWymo",
            "https://drive.google.com/uc?export=view&id=14heo7dkNNeck-VZcRHxOLo4bATt1VYQc",
            "https://drive.google.com/uc?export=view&id=1E7l-EQWOu3BtC_qukvhJ_jTU_kDo5UsB",
            "https://drive.google.com/uc?export=view&id=1E7l-EQWOu3BtC_qukvhJ_jTU_kDo5UsB",
            "https://drive.google.com/uc?export=view&id=1SUd4tYMEnOSXRrgvqd2nAZ767HR-zM_Z",
            "https://drive.google.com/uc?export=view&id=1oU_xEyQvBE6JSNBXeVvFWarTujOKmQW5",
            "https://drive.google.com/uc?export=view&id=1XsMK3MW-Ajd9K8-6PFy6AQMxmHJEHCTH",
            "https://drive.google.com/uc?export=view&id=1occtyi2cUhETFIh3rwETgE_vAPSoK9R9",
            "https://drive.google.com/uc?export=view&id=12MbwU8w98NVSo8Z-plCOMwQvY38eyPg9",
            "https://drive.google.com/uc?export=view&id=",
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
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukarame",
                "alamat": "Sukabumi",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "Abangnya keren, pasti portonya bagus",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Sukarame",
                "hobbi": "Dengerin musik",
                "sosmed": "@mregiiii_",
                "kesan": "Abangnya asik dan seru untuk diajak diskusi.",
                "pesan":"Semangat terus untuk kuliahnya ya, Bang!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "123450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main bass, piano, semualah",
                "sosmed": "@marletacornelia",
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
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Riau",
                "alamat": "GH, Belwis",
                "hobbi": "Main Basket",
                "sosmed": "@muhammadqil1111",
                "kesan": "Abangnya baik dan juga ga pelit pengetahuan",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, bang."
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran, Lampung",
                "alamat": "Pesawaran, Lampung",
                "hobbi": "Main piano dan nyanyi",
                "sosmed": "@pebby_olla525",
                "kesan": "Kakaknya baik dan ramah",
                "pesan":"Sukses selalu untuk segala urusannya kak"    
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
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampura",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars",
                "kesan": "Abangnya sangat baik dan sabar dalam membimbing.",
                "pesan":"Jangan lupa jaga kesehatan di tengah kesibukannya ya, bang."
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O7uAi5IYQX0PWglruRyNcRQAfaXfwKHa",
            "https://drive.google.com/uc?export=view&id=121lVCX_o4uU8xvqgCzTpNnnjW5I7dB7B",
            "https://drive.google.com/uc?export=view&id=12WlUhCFmKnK-JGgnL0Omo4xRp143oowd",
            "https://drive.google.com/uc?export=view&id=1V3dWZf-4m1sBYTtfWXSiRz08z5nTY38L",
            "https://drive.google.com/uc?export=view&id=1st5EoyNc_-RzxXNCXvUo4cBkvsUB32hZ",
            "https://drive.google.com/uc?export=view&id=1WB9FcwaU-c8Kgz28k1koXLM0wRqRxmfh",
            "https://drive.google.com/uc?export=view&id=1yc3Q7ODEeHydr6rLP3r_e-1cHOtQETU9",
            "https://drive.google.com/uc?export=view&id=1h9CLtCORHL9376AFXrui3_c2rIemsI48",
            "https://drive.google.com/uc?export=view&id=1NviOe9Vp4JZSlrXwk3RQloKlJJa5xHSD",
            "https://drive.google.com/uc?export=view&id=17jqeqQLP3DS0-QCrPbg2QzsxWskX1ZqS",
            "https://drive.google.com/uc?export=view&id=1GOVOAf8HedsYlyIgZmdeiozZoi-sUHH7",
            "https://drive.google.com/uc?export=view&id=15DFsaIPA76QKq1OyqBCo4hxn5Utp4cvk",
            "https://drive.google.com/uc?export=view&id=1Mzzn8PPQHi7_AYGMzSFGx-Ht2cw1I7z9",
            "https://drive.google.com/uc?export=view&id=1VTzGlcziWn-Rtf6pX8NKP82uAEngx9VR",
            "https://drive.google.com/uc?export=view&id=18dFruNmt91enU-9SAXvsYhfX5rbn-3SK",
            "https://drive.google.com/uc?export=view&id=1VYZL26ATIP3162OYY0b1Uuxh2ZtvS5cC",
            "https://drive.google.com/uc?export=view&id=1la7l0hHyWLDgkTzOxYO0YTARLO1L4jQq",
            "https://drive.google.com/uc?export=view&id=1k792ToAyQfim33suAT0drKc7e-wrdQ9-",
            "https://drive.google.com/uc?export=view&id=1npE014IooIoXeI3jMkTMh4iBXXHiwall",
            "https://drive.google.com/uc?export=view&id=1Y2WrNplUTKvSblBOF5XHLqhV0VxzmR5X",
            "https://drive.google.com/uc?export=view&id=1BwG1S2GLMNeUsUAhUXnVHZOXjbdsxZHA",
            "https://drive.google.com/uc?export=view&id=1_OTsEObvuLTCvw645RFxU-dG3wq6eIIt",
            "https://drive.google.com/uc?export=view&id=1v86yMnlInZD_hkx7po1wNNQBFMG32LVy",
            "https://drive.google.com/uc?export=view&id=1dgwuFitnL9i_bljiDXGcGeV2NyBI4lVx",
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
            "https://drive.google.com/uc?export=view&id=1vTYKLoHVt43WF3X-hwDGNKdSG1gvpt-r",
            "https://drive.google.com/uc?export=view&id=1zj4usKVfVXOK16F5xVi3-Dp6tYsOcjX0",
            "https://drive.google.com/uc?export=view&id=1F8BXdxQcDQbL2kYDSIKj0dl_Lhg9rTYN",
            "https://drive.google.com/uc?export=view&id=1e1rApTgLa4OUpmtbXlfJlgdNvwlR2GQv",
            "https://drive.google.com/uc?export=view&id=1_-7eSoOg6zaiSkuGA3WXqEw4kBwfmZyU",
            "https://drive.google.com/uc?export=view&id=1wGm6WliM0KkWkz1pZ1YlypM0QbKyDQLe",
            "https://drive.google.com/uc?export=view&id=158P_VM136KL3CHVNUreleOXme6WfgyxP",
            "https://drive.google.com/uc?export=view&id=1vbBg22Wtd9L0p6Pqv9sHddSQ5bqCbmIc",
            "https://drive.google.com/uc?export=view&id=1OKAZI12Mj-jB_CYynVXBCg5M4gJUl9kC",
            "https://drive.google.com/uc?export=view&id=10e4hqL4IcSoPv1PEPaTWuYesUCAre8cM",
            "https://drive.google.com/uc?export=view&id=1XdonqwCl34iQYaUPbtK1smkrLoLoD4I2",
            
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
                "kesan": "Kakaknya asik dan seru.",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "_inayasani",
                "kesan": "Kakaknya sangat ramah.",
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
                "kesan": "Terima kasih kak atas bantuannya.",
                "pesan": "Semangat dan sukses selalu!"
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "nonton drakor",
                "sosmed": "deviirhyu",
                "kesan": "Kakaknya baik dan murah senyum.",
                "pesan": "Semangat terus ya, kak!"
            },
            {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "aprhtp_",
                "kesan": "Senang bisa bertemu dengan kakak.",
                "pesan": "Semoga semua urusannya dilancarkan."
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "jogging",
                "sosmed": "anadiacrn_",
                "kesan": "Kakaknya keren dan inspiratif.",
                "pesan": "Semangat terus kuliahnya, kak!"
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "jogging",
                "sosmed": "nabila_zazahra",
                "kesan": "Kakaknya sangat membantu.",
                "pesan": "Semangat terus ya, kak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "dhafinrzqa13",
                "kesan": "Kakaknya asik diajak diskusi.",
                "pesan": "Terima kasih atas bimbingannya, kak."
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "beli parfum",
                "sosmed": "den_iki__",
                "kesan": "Kakaknya ramah dan baik.",
                "pesan": "Sehat selalu ya, kak."    
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "syalaishaa_31",
                "kesan": "Senang bisa berkenalan dengan kakak.",
                "pesan": "Semoga sukses selalu kuliahnya!"
            },
            {
                "nama": "Engeli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "menonton alur cerita film",
                "sosmed": "englirahmdhnii",
                "kesan": "Seru bisa kenal dengan kakak.",
                "pesan": "Semoga sukses selalu, kak!"
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

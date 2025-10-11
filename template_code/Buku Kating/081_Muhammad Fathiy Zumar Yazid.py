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
            "https://drive.google.com/uc?export=view&id=1facqC5h5O0K4zmoXXsay0U-HlqWzqMb6",
            "https://drive.google.com/uc?export=view&id=1gGAQ6Wkw0I-XMBdPZ7GLIE0XQOJVPKAk",
            "https://drive.google.com/uc?export=view&id=1RLGL--fisT7O42uaF8-BicEvVtysL7UU",
            "https://drive.google.com/uc?export=view&id=119hABbvcr2QFIahM2KGPm88P8qw4pNRM",
            "https://drive.google.com/uc?export=view&id=1G7tT1YYHvWeZNXISvxnRc3hy3zjXc6Do",
            "https://drive.google.com/uc?export=view&id=1_M3yFRQWlTgGmdqhJ1Ih8RKt2AfJg1Fk",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Cikarang",
                "alamat": "Pulau damar",
                "hobbi": "Bikin lagu",
                "sosmed": "@_rendraa",
                "kesan": "Kak Rendra keren banget, jago bikin lagu!",
                "pesan": "Semangat terus kuliahnya Bang Rendra!!!"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Kak Johannes suka banget baca dan rajin belajar SQL!",
                "pesan": "Terus semangat eksplor data dan kodingnya kak Johannes!"
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Elisabeth lucu dan asik banget diajak ngobrol!",
                "pesan": "Jangan lupa istirahat dan tetap semangat ya kak Elisabeth!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza tenang tapi cerdas banget!",
                "pesan": "Tetap semangat dan terus berprestasi kak Syadza!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty ramah banget dan suka cerita hal lucu!",
                "pesan": "Tetap jadi kakak yang ceria dan positif ya!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak Farahanum seru banget dan inspiratif!",
                "pesan": "Semangat terus kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qhqxoUyqFCnmn5MjrOga9CWmrxlg2pa1",
            "https://drive.google.com/uc?export=view&id=1nhG44Yf9LG6VjhLDdbx_lIvF4a1AvVOB",
            "https://drive.google.com/uc?export=view&id=17kz08pPVu15mOGiivNKmfNjhcE8GmjN1",
            "https://drive.google.com/uc?export=view&id=1v5UrXOuduIvxBnl3c1vAVBxLQvcdKEuk",
            "https://drive.google.com/uc?export=view&id=1Kh0s6LTRqOtIi7CWI7gsrn6gcu4SD6EJ",
            "https://drive.google.com/uc?export=view&id=12jJeWep97P9yYbH8AyW1S_dAPMOt6DJx",
            "https://drive.google.com/uc?export=view&id=1nUm3APcMLftKwS6gX3IcALPoTHMbEXdS",
            "https://drive.google.com/uc?export=view&id=1H7Wqg0mx5oOjdSMmYcyzpp11FhegUyVX",
            "https://drive.google.com/uc?export=view&id=1wMaJ6_UZ705wPHCLJe6iVLhFccaWP7NH",
            "https://drive.google.com/uc?export=view&id=15OexmIE_UaVggDMXxUHUlYRv0L3Ekzl1",
            "https://drive.google.com/uc?export=view&id=13z9ggaL_OUgevBYYtwtAzULY6pJe53pj",
            "https://drive.google.com/uc?export=view&id=17xWlh1Knxhqpjk2LapYj_2lQ9esbZiAR",
            "https://drive.google.com/uc?export=view&id=1XszkR-kyXo8qHaCZP3gi04UkOmGqSVbZ",
            "https://drive.google.com/uc?export=view&id=1Tqd46sxxISB17qcpIbybUJwJaVQuJplA",
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
                "kesan": "Bang Jeremia orangnya seru banget!",
                "pesan": "Semangat terus kuliahnya Bang, sukses selalu!"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak Dhea punya vibe kalem tapi lucu banget!",
                "pesan": "Tetap semangat ya kak Dhea, jangan sering badmood hehe!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha selalu ceria dan kreatif banget!",
                "pesan": "Terus tebarkan semangat positifnya kak Renisha!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Kak Anisa asik banget dan aktif di setiap kegiatan!",
                "pesan": "Semangat terus kuliahnya kak Anisa, sukses selalu!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Way Halim, Balam",
                "alamat": "Way Halim, Balam",
                "hobbi": "Nyuci baju",
                "sosmed": "@dhruchyo",
                "kesan": "Bang Dharu santai tapi rajin banget!",
                "pesan": "Tetap semangat dan terus belajar hal baru ya Bang Dharu!"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "Kak Feby rame banget dan bikin suasana hidup!",
                "pesan": "Terus ceria dan semangat terus ya kak Feby!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro kalem dan suka merenung hal-hal dalam hidup!",
                "pesan": "Semoga selalu tenang semangat kuliahnya Bang Givaro!"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan pecinta kuliner sejati !",
                "pesan": "Jangan lupa traktir teman-teman kalo nemu makanan enak ya Bang!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Kak Berliana unik banget dan punya hobi yang keren!",
                "pesan": "Terus jadi pribadi yang berwarna dan inspiratif ya kak Berliana!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kak Juesi suka galau tapi tetap ceria di depan teman-teman!",
                "pesan": "Semangat terus ya kak Juesi, jangan galau terus hehe!"
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho keren banget dan punya aura positif!",
                "pesan": "Semangat terus ya Bang Ridho, sukses di setiap langkah!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Bang Feryadi lucu banget dan suka bercanda!",
                "pesan": "Jangan bosen dengerin Wawa ya Bang haha!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica pro banget kalau udah main ML!",
                "pesan": "Semangat terus push rank-nya kak Monica!"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa punya aura calm dan adem banget!",
                "pesan": "Tetap jadi pribadi yang menenangkan ya kak Nashwa!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def Senator():
        gambar_urls = [    
            "https://drive.google.com/uc?export=view&id=1n7-mkDuBFJXIDyq-ZX4FFbLOgj1CmM3n",
            "https://drive.google.com/uc?export=view&id=1xFIgU9ZvNb5qQJt3ebzjQWF14wyZFRAU",
            "https://drive.google.com/uc?export=view&id=1LN4Hvl-Mj5LetNQvMPgMhS1fpQtfYB4c",
            "https://drive.google.com/uc?export=view&id=1IK3Uelukq9rie1KAh4W4aueypgBdJvAe",   
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
                "kesan": "Bang Bintang rajin banget dan selalu semangat belajar!",
                "pesan": "Semangat belajarnya Bang Bintang!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kak Nadya santai banget dan punya selera musik yang bagus!",
                "pesan": "Semoga hari-hari kaka selalu penuh lagu yang menenangkan ya kak!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah suka bengong tapi tetep lucu banget!",
                "pesan": "Tetap santai tapi jangan kebanyakan bengong ya kak hehe!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Lia chill banget dan suka tidur di waktu yang pas!",
                "pesan": "Semangat terus kuliahnya kak Lia, tapi jangan kebanyakan tidur ya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

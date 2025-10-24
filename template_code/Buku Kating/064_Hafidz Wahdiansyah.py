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
            "https://drive.google.com/uc?export=view&id=1U5W5Bwj00-Syg5MJy1WEmOi1jj8Ngfe4",
            "https://drive.google.com/uc?export=view&id=16mSBzMpKEBwM5K3M6vhDVfWPLBYX2nQX",
            "https://drive.google.com/uc?export=view&id=1JokGJKkMS5f0lcaNyyJvhIRvFFcrZPpZ",
            "https://drive.google.com/uc?export=view&id=1THVF56NGKDiuLtWPVOe8tahIpsO7VSuy",
            "https://drive.google.com/uc?export=view&id=1kz9rXQse9VdVAvU9kQT6s7JfIlRiWeNK",
            "https://drive.google.com/uc?export=view&id=1e6UE-muoqApBppD41ncHkT22-XyWytbs",
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
                "kesan": "Bang rendra asik dan berwibawa",  
                "pesan":"semangat terus bang, dan semoga diberi kelancaran nyusun TA nya !!!"# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "jl.Lapas",
                "hobbi": "Baca buku SQL",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Johannes orangnya asik, seru diajak ngobrol, dan selalu punya semangat tinggi dalam belajar, terutama soal SQL",  
                "pesan":"semangat terus bang , semoga diberi kelancaran segala urusan!"# 1
            },
            {
                "nama": "Elisabeth Claudia",
                "nim": "122450123",
                "umur": "19",
                "asal": "Tangerang",
                "alamat": "airas kost",
                "hobbi": "nyemil",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Elisabeth orangnya ramah, ceria, dan gampang akrab sama siapa aja. Selalu bikin suasana jadi lebih santai dan seru",  
                "pesan":"Tetap jadi pribadi yang ceria dan positif ya! Semoga makin sukses di setiap hal yang kamu kerjakan, dan jangan lupa terus semangat ngejar impianmu kak"# 1
            },
             {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "belwis",
                "hobbi": "membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kak Syadza orangnya kalem, cerdas, dan terlihat sangat suka belajar",
                "pesan": "Terus pertahankan semangat belajarnya ya kak! Semoga apa pun yang kamu cita-citakan bisa tercapai. Jangan lupa juga untuk tetap menikmati waktu istirahat di tengah kesibukanmu!"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiati",
                "nim": "122450001",
                "umur": "21",
                "asal": "Borneo Kalimantan Barat",
                "alamat": "Gedung Tataan Pesawaran",
                "hobbi": "ngelas ngelus kucing",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty ramah banget, suka cerita dan bisa membaca zodiak seseorang",
                "pesan": "Terus menjadi kakak yang ramah, suka bercerita ya kak"
            },
              {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "kiya kost",
                "hobbi": "domino, qtek kahim",
                "sosmed": "@farahanumafifahh",
                "kesan": "Farahanum orangnya seru, aktif. Selalu terlihat semangat dalam setiap kegiatan",
                "pesan": "Terus jadi sosok yang inspiratif dan bersemangat ya! Semoga semua kesibukan dan tanggung jawabmu berjalan lancar, dan jangan lupa tetap jaga waktu buat istirahat serta bersenang-senang juga!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Dz6DGzty4rRAL8kFIqZlfaO1FDmsuQ1f",
            "https://drive.google.com/uc?export=view&id=1EGKdmyXv_dpP1jYYtHrirDTHeSDpsdWZ",
            "https://drive.google.com/uc?export=view&id=1IbLXbffiEcd1vP7pqvAFeuDVUCHgSGKJ",
            "https://drive.google.com/uc?export=view&id=1mlUvBJCyXqQ1q-scTRGlpKFr2-eFDZ6Q",
            "https://drive.google.com/uc?export=view&id=198FiOK2FsEQrnUl7CO552CV2shbTG9sb",
            "https://drive.google.com/uc?export=view&id=18Ce93uHTg1TpshF99G2NU8tE4w_kuj6W",
            "https://drive.google.com/uc?export=view&id=1fKSbGHgOe-mxbedK7MaxAlmFNnBMXRue",
            "https://drive.google.com/uc?export=view&id=1OWIgxbO-NJAEmUx7mQ7auBPUxFQFhX-L",
            "https://drive.google.com/uc?export=view&id=1PwTlTkhBJkWxOLSu48JyiR27nMRswqP4",
            "https://drive.google.com/uc?export=view&id=13b_MIc6QKHyX3sMVSX_ZmWHCbwPW73--",
            "https://drive.google.com/uc?export=view&id=1KOv_EoNjqYDxWlRfTsL3VHM-5NI-pYhb",
            "https://drive.google.com/uc?export=view&id=1y1fKHXA8zeOX_gJTXyOK7WE2N9lAwBXV",
            "https://drive.google.com/uc?export=view&id=1DM681DhzcFtT0_A3P3mAR-fJaCGXrFMS",
            "https://drive.google.com/uc?export=view&id=1INUnpsSJVkEfS9f_YhkL18tuhZ-jtDlK",
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
                "kesan": "Bang Jeremia adalah sosok kepala departemen yang bertanggung jawab, tegas, dan bisa jadi panutan. Cara dia memimpin menunjukkan kedewasaan dan ketegasan, tapi tetap bisa menjaga suasana agar nyaman dan kompak",
                "pesan": "Terus pertahankan jiwa kepemimpinanmu yang keren itu, ya bang! Semoga makin sukses dalam setiap langkah, baik di organisasi maupun di luar kampus."
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Bandar Lampung Ujung",
                "hobbi": "Badmood liatin Jaldi",
                "sosmed": "@_.dheamelia",
                "kesan": "Kak Dhea orangnya lucu, spontan, dan punya karakter yang unik banget",
                "pesan": "Tetap jadi diri sendiri ya, kak Dhea! Jangan terlalu dibawa perasaan kalau lagi badmood, hehehe. Semoga selalu bahagia, sukses di kuliah, dan makin banyak momen seru bareng teman-teman"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Nawarin alat pancing",
                "sosmed": "@renishapg",
                "kesan": "Kak Renisha orangnya asik, lucu dan selalu bisa bikin suasana jadi lebih santai",
                "pesan": "Terus jadi pribadi yang ceria dan menghibur ya,kak Renisha! Semoga semangatmu nggak pernah padam"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "20",
                "asal": "Wakatobi",
                "alamat": "Balam",
                "hobbi": "Main bowling",
                "sosmed": "@",
                "kesan": "Kak Anisa asik banget!",
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
                "kesan": "Bang Dharu orangnya pintar, rajin, dan punya aura tenang yang bikin nyaman diajak ngobrol. Selain cerdas, dia juga rendah hati",
                "pesan": "Terus pertahankan kepintaran dan kerendahan hatimu ya, Bang! Semoga selalu sukses di setiap langkah, dan jangan lupa juga tetap jaga semangat serta keseimbangan antara belajar dan istirahat"
            },
            {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Macing keributan",
                "sosmed": "@feby.wldr",
                "kesan": "Kak Feby orangnya rame, spontan, dan penuh energi!",
                "pesan": "Terus jadi sosok yang ceria dan berani nunjukin diri sendiri ya,kak Feby! Semoga semangatmu nggak pernah padam, dan tetap seimbang antara becanda dan seriusnya"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Liatin langit",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro orangnya kalem, santai, dan punya vibe yang tenang banget. Hobinya liatin langit kayaknya cocok sama kepribadiannya yang suka mikir dalam dan menikmati hal-hal kecil.",
                "pesan": "Terus jadi pribadi yang tenang dan penuh makna ya, Givaro! Semoga pandangan luasmu kayak langit itu bisa bantu kamu capai banyak hal besar ke depannya. Jangan lupa juga tetap semangat dan percaya diri dalam setiap langkah"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Nyoba makanan terbaru",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan orangnya seru, gampang akrab, dan selalu punya topik menarik",
                "pesan": "erus jadi pribadi yang ceria dan penuh semangat ya,bang Mirzan!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Ngumpulin batu unik di pantai",
                "sosmed": "@berlyyanda",
                "kesan": "Berliana orangnya lembut, tenang, dan punya kepribadian yang unik banget",
                "pesan": "Terus jadi pribadi yang tenang dan penuh warna ya,kak Berliana! Semoga kamu selalu menemukan “batu berharga” di setiap langkah hidupmu—baik itu pengalaman, teman, maupun kesempatan baru"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "18",
                "asal": "Teluk Pandawa",
                "alamat": "Belwis",
                "hobbi": "Galau",
                "sosmed": "@j_eesie",
                "kesan": "Kak Juesi orangnya imut, lucu, dan punya aura yang bikin suasana jadi adem tapi juga seru",
                "pesan": "Tetap jadi kakak yang imut dan menggemaskan ya, Kak Juesi! Jangan terlalu sering galau—ingat, banyak hal indah yang nunggu di depan."
            },
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Melbourne",
                "alamat": "Gh",
                "hobbi": "Main padle",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho orangnya keren, kalem, dan punya aura percaya diri yang kuat.",
                "pesan": "Terus jadi pribadi yang santai tapi tetap berprestasi ya,bang Ridho! Semoga sukses selalu dalam setiap hal yang kamu jalani, baik di kampus maupun di luar"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "17",
                "asal": "Tangerang",
                "alamat": "Belwis",
                "hobbi": "Dengerin Wawa ngomong",
                "sosmed": "@fer.yulius",
                "kesan": "Bang Feryadi orangnya lucu, santai dan hobinya unik",
                "pesan": "Terus jadi pribadi yang asik dan ringan hati ya bang! Semoga semangatmu selalu stabil, dan tetap jadi pendengar yang baik terutama buat kak Wawa, hehe"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450087",
                "umur": "19",
                "asal": "Sumut",
                "alamat": "Belwis",
                "hobbi": "Main ML, only Franco",
                "sosmed": "@monica_tjg",
                "kesan": "kak Monica orangnya seru, kompetitif, dan punya semangat tinggi",
                "pesan": "Terus jadi pribadi yang kuat dan bersemangat ya,kak Monica"
            },
            {
                "nama": "Wa Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Wawa orangnya lembut, lucu, dan punya keunikan tersendiri—apalagi dengan hobinya yang nyapa angin",
                "pesan": "Terus jadi pribadi yang manis dan positif ya, kak Wawa! Jangan pernah kehilangan keunikan dan keceriaanmu itu"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ev-tvt0SBAsyiadxrXYiX8vryxzO3uSU",
            "https://drive.google.com/uc?export=view&id=1urQ2fHrmLNkJiZCfzPTXl9mORUn-2UNw",
            "https://drive.google.com/uc?export=view&id=1nnWuYRXAi9_32g4JTrRBvxBeFpxYgDuT",
            "https://drive.google.com/uc?export=view&id=12iqlyuWL07Nzu6Fe-O0vSpmIwZRI1365",  
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
                "kesan": "Bang Bintang orangnya rajin, cerdas, dan tekun banget. Hobinya belajar nunjukin kalau dia serius dalam mengejar ilmu dan selalu ingin berkembang. Di balik keseriusannya, dia juga rendah hati dan gampang diajak ngobrol, bikin orang sekitar nyaman.",
                "pesan": "erus pertahankan semangat belajarmu, Bang Bintang! Semoga semua usaha dan kerja kerasmu membuahkan hasil yang membanggakan. Jangan lupa juga tetap jaga keseimbangan antara belajar dan istirahat biar selalu fresh"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjani",
                "kesan": "Kak Nadya orangnya ceria, ramah, dan selalu bisa bikin suasana jadi hidup. Hobinya dengerin lagu bikin dia terlihat santai dan mudah akrab sama siapa aja. Aura positifnya bikin orang di sekitarnya nyaman dan semangat.",
                "pesan": "Tetap pertahankan keceriaan dan energi positifmu, Kak Nadya!"
            },
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Bengong",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah orangnya sabar, tenang, dan perhatian. Hobinya bengong nggak mengurangi kesan profesionalnya—malah bikin dia terlihat reflektif dan bijaksana. Sebagai pengajar kelas tutorial ALE, dia sabar dalam membimbing dan selalu siap membantu teman-temannya memahami materi dengan jelas.",
                "pesan": "Terus jadi kakak yang sabar dan menginspirasi ya, Kak Fathinah! Semoga semua usaha dan dedikasimu dalam mengajar membuahkan hasil yang membanggakan"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang Indomaret Belwis",
                "hobbi": "Tidur",
                "sosmed": "@lia.h_264",
                "kesan": "KakLia orangnya santai dan gampang akrab sama siapa saja.",
                "pesan": "Tetap jadi pribadi yang santai tapi menyenangkan ya,kak Lia! Semoga selalu sehat, bahagia, dan tetap semangat menghadapi hari-hari"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MMIwtJAtaz6IQBvjL_l1N4Lf0FB9oq30",
            "https://drive.google.com/uc?export=view&id=1umQKOy_X_UPnoez8deGv8r3zozYDtDiG",
            "https://drive.google.com/uc?export=view&id=1kntexRBjiCkUM_ssUbmttDD_yEGBNIfm",
            "https://drive.google.com/uc?export=view&id=18VLtoRwO1LtCZFa7JHYLMa2dWuwNuKSP",
            "https://drive.google.com/uc?export=view&id=10xVFfLtCiZvetpWuDEVZ-Gc6_CR7Q5Cw",
            "https://drive.google.com/uc?export=view&id=1SNfIFzSC8P8xCI7X0QjvMWP_2zic_eQy",
            "https://drive.google.com/uc?export=view&id=1P9d6h6krJA5UoCcczU-wc873EgDE4ZQv",
            "https://drive.google.com/uc?export=view&id=1JF5AQJSjrhWYn-sw9HK0rG63z6oAm7b1",
            "https://drive.google.com/uc?export=view&id=1ngBnahLXyaFZp2oYmj9H6o1dn4ouyqSg",
            "https://drive.google.com/uc?export=view&id=1fnicnfhmqKWfm39M6Fht86RNwdOA3ybB",
            "https://drive.google.com/uc?export=view&id=1AVAXpCxIdxf-3UZAWwdv1uyHK0L6roaK",
            "https://drive.google.com/uc?export=view&id=1emoyRNU06Ivbw1O5HdA_ks_sUUylkEKr",
            "https://drive.google.com/uc?export=view&id=1MSHAImfVQXntkkgxHDxJcANdqYT3i_Qb",
            "https://drive.google.com/uc?export=view&id=1zZACqUJ-aH1mGvumflL8HiGAmdOqmdPQ",
            "https://drive.google.com/uc?export=view&id=1DGqtNxspYuvCEhdBsaIouq9ryjpCX_h4",
            "https://drive.google.com/uc?export=view&id=1QRMf69Io1JzHzdw-VrXvPD-Iy3IpfRe2",
            "https://drive.google.com/uc?export=view&id=14BwGAmKkdSJYgK0LcBgrrVVPmG-fim47",
            "https://drive.google.com/uc?export=view&id=1GaveRzp_eANVbpB51fxEVSLI206pdrSQ",
            "https://drive.google.com/uc?export=view&id=1RKx34eCEuEHVhoF-sWwyEn8dVt3gYEyu",
            "https://drive.google.com/uc?export=view&id=1K8SmNvD2BFF_JsySfYxBcZKfFBdvMhk_",
            "https://drive.google.com/uc?export=view&id=1LFwmNWGiTzdcpQNIazSfcrcy0Rd4bS6R",
            "https://drive.google.com/uc?export=view&id=1U5F7Vf8VXTPdk_2sCSIAOb0vXUjjlRZW",
            "https://drive.google.com/uc?export=view&id=1Wdz1Pz5MCM3D71QVjEgd15vMPGDm9nIq",
            "https://drive.google.com/uc?export=view&id=1IXsAquND-jQLTM82ymdMBhGJzBuHtpSO",
            "https://drive.google.com/uc?export=view&id=1gu3QoYnHT5NFQrp_wXCUuIMzFPJAI85X",
            "https://drive.google.com/uc?export=view&id=1MvSmYyPKrRHMvzDV9qDOYAVWorbA-T8R",
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@ferdy_kevin",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal": "Jawa barat",
                "alamat": "Korpri",
                "hobbi": "Mikir",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya asik banget",  
                "pesan": "semangat kuliahnya"
            },
             {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal": "Tulang Bawang Barat",
                "alamat": "Belwis",
                "hobbi": "Ngekader 24",
                "sosmed": "@Allyapasha_",
                "kesan": "Kak Allya orangnya energik, disiplin, dan penuh semangat.",  
                "pesan":"Semoga semua usaha dan energi positif kak allya bisa membawa banyak kebaikan"# 1
            },
              {
                "nama": "Ahmad Rizky",
                "nim": "123450027",
                "umur": "20",
                "asal": "Tangerang selatan",
                "alamat": "Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky__",
                "kesan": "Bang Ahmad orangnya aktif, sportif, dan gampang akrab sama teman-temannya.",  
                "pesan":"Terus pertahankan semangat dan energi positifmu,bang Ahmad! Semoga hobi dan kerja kerasmu selalu membuahkan hasil yang membanggakan"# 1
            },
           {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "20",
                "asal": "5 km dari pantai kedu",
                "alamat": "deket kost bang dapa",
                "hobbi": "cari kesibukan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta orangnya energik, kreatif, dan selalu aktif mencari hal-hal baru untuk dilakukan",  
                "pesan":"Semoga semua aktivitas dan kesibukanmu selalu membawa hal-hal positif dan pengalaman berharga"# 1
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal": "rahim ibu",
                "alamat": "samping kost arienta",
                "hobbi": "jahilin yulia",
                "sosmed": "@daffahdynn_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Natasya Amavisca",
                "nim": "123450024",
                "umur": "19",
                "asal": "lubuk linggau",
                "alamat": "kost putri gerbang barat",
                "hobbi": "ngitungin duit",
                "sosmed": "@natasyaamavisca",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Samping kost kak alya",
                "hobbi": "ngekader",
                "sosmed": "@nobelnizam",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sigma family",
                "hobbi": "ngasprak",
                "sosmed": "@j_gumel_17",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Vany salsabila putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "palembang",
                "alamat": "airan raya",
                "hobbi": "ngoding di macbook",
                "sosmed": "@vany.salsabila",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "1224450044",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Badminton",
                "sosmed": "@sahid22_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Jabung, Lampung Timur",
                "alamat": "Sukarame",
                "hobbi": "Main game, kulineran",
                "sosmed": "@ali_parisi3",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@farazka",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@risma.mustika_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi": "Main Video Game",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "-",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Ngerjain Tugas",
                "sosmed": "@ahmadnaufal_11",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No.55",
                "hobbi": "Koleksi pita pink",
                "sosmed": "@d_aniar",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Gangguin Kak Dea",
                "sosmed": "@ihsan.yusuf",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang Selatan",
                "hobbi": "Ngomongin Kak Dea",
                "sosmed": "@kevinaja",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajut",
                "sosmed": "@dia_natzzyaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nyuruh Kak Dea diam",
                "sosmed": "@m.ridwan_22",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Ulliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "jl. Raden saleh",
                "hobbi": "Main piano, ngoding, menanam anggrek, berantem",
                "sosmed": "@ullianowlm",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Benget Sidabutar",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Main Bola",
                "sosmed": "@sidabutar.26",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Ibu Kota Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Cari GPT",
                "sosmed": "@rewinanaaa",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1o8z8hutyViicPj-VnDPPstcF1X_Q2j-O",
            "https://drive.google.com/uc?export=view&id=1op7XUix3M3DLxwkVZRAwArPLgJYHdhxl",
            "https://drive.google.com/uc?export=view&id=1p1KN57riYl9_rYp4j_HkXct0Lk7-_P4C",
            "https://drive.google.com/uc?export=view&id=1oHmU0FYjyFv5BdcjQOQrwNtRxL1f5C6f",
            "https://drive.google.com/uc?export=view&id=1k966nWStMGziSz90PyuSVCXLkabDEWbJ",
            "https://drive.google.com/uc?export=view&id=1rkK5Gl3WPojkgUIhPGITp8XnNjcgDW0O",
            "https://drive.google.com/uc?export=view&id=1psVxrEW_ZzLk_Xx0y7kQIK02QDZU2w-y",
            "https://drive.google.com/uc?export=view&id=18d3SRYpRHvRVeF5LiYfN2fZsijrp0KGt",
            "https://drive.google.com/uc?export=view&id=14ZZou3yFXL7fGOfskLvpxkSXypLXohYX",
            "https://drive.google.com/uc?export=view&id=1IwT8DiPXVKFwEtnNknr2zTe7pnAGj3Mm",
            "https://drive.google.com/uc?export=view&id=1-SK7Y2vR5AQvdZySaiAKPoYrlLQ5_IUG",
            "https://drive.google.com/uc?export=view&id=1tW4cPbEI0vgE6XyESkQcY7iyYAcW346e",
            "https://drive.google.com/uc?export=view&id=1UcStdBDDp9jOvQz6dHbB4t3k0lx4yY3N",
            "https://drive.google.com/uc?export=view&id=1_4RiMKc9XwmRFUJBR-zCVo1E0YhLEUAs",
            "https://drive.google.com/uc?export=view&id=1LBM_YQQcfCJjtH15Ye8rdcP0xEm7B2Im",
            "https://drive.google.com/uc?export=view&id=1OpfRQLfbCjYHJLNHtpbHs1asyZhmLimS",
            "https://drive.google.com/uc?export=view&id=11WHiO5mp3P8rTDWsZKH1HClS5ss8ATkF",
            "https://drive.google.com/uc?export=view&id=1WE8dn_kakbRUjf5hNfWn5jztWM1MAze1",
            "https://drive.google.com/uc?export=view&id=1NJcoUaR9WQQRX8-aDqUWqrYyJVeYjkE9",
            "https://drive.google.com/uc?export=view&id=1B2qOUWtUXicC-ucxypm1IvzFUC-C2b7j",
            "https://drive.google.com/uc?export=view&id=1h0p7J8BCHcD39aQ3is4MsbxCN68kOHET",
            "https://drive.google.com/uc?export=view&id=1CKfbEM5NtCSNj38LigK4iOObA-nfa4Nt",
        ]
        data_list = [
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"Serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl. Permadani, Sukarame",
                "hobbi": "Dengerin Musik",
                "sosmed": "@mregiiii_",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishsahi",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segala Mider",
                "hobbi": "Fose",
                "sosmed": "@fadilalfarizzi",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450006",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "Belwis",
                "hobbi": "Main Basket/Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Dengerin Musik",
                "sosmed": "@notfall.s",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton film",
                "sosmed": "@nadiaafrj",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Bumi sari, Natar, Lampung Selatan",
                "hobbi": "Menari, Dengerin Musik, Ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh, Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": " 123450024",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "JL. Gajah Mada, Tanjungkarang",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama Itera TB 4",
                "hobbi": "Tidur",
                "sosmed": "@tunty_i",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450022",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Hasan VI, Airan",
                "hobbi": "Isengin orang/ngobrol random",
                "sosmed": "@fifah.zy",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jl. Teratai No.27, Kedaton",
                "hobbi": "Jalan-jalan, main game",
                "sosmed": "@biyokcb",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "",  
                "pesan":""# 1
            },

        
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
    
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1C26j5JQQsgihLQC6y_twwSUK_iQQ8JVA",
            "https://drive.google.com/uc?export=view&id=1b_M2SM9fX1wlBh0B6Z3ILCrJHzrl2snN",
            "https://drive.google.com/uc?export=view&id=1SpBTx2KSVJN2aLqVs-Feuh6vBG5150Za",
            "https://drive.google.com/uc?export=view&id=1MunHF0i0DBaRHxVeOgyYfkEQtG3e8LZ_",
            "https://drive.google.com/uc?export=view&id=1vofF80AGbJGKwdYBWlz09whdI1cb7mca",
            "https://drive.google.com/uc?export=view&id=1mpIcRh4CAfYhvHY-oM3gqAdPuIZVHJ8Y",
            "https://drive.google.com/uc?export=view&id=12G3itItbJz-wzCRf6OcvRrE_xljTbqbt",
            "https://drive.google.com/uc?export=view&id=1QWtL-zFYXcO0O0Ws2IONWWA60O3zQPBH",
            "https://drive.google.com/uc?export=view&id=1KRSHn9uRpv2VLmqDtDKfuG5dmsiZf21m",
            "https://drive.google.com/uc?export=view&id=1Ax6319f11K_PoVK6_K3fFVOeftsqLzEy",
            "https://drive.google.com/uc?export=view&id=1XUNDS7RquVZ3r4AYgthWPqJEdrCaqc8W",
            "https://drive.google.com/uc?export=view&id=1wW2B3ivWSI-LfldO09tN_tbciPaCrBAo",
            "https://drive.google.com/uc?export=view&id=1cgwMQU2b22S4OAs2PF-AHSd8YMuc3If0",
            "https://drive.google.com/uc?export=view&id=1aAC1PEBCYkjL0UxGX4flOiEmRVN7c00B",
            "https://drive.google.com/uc?export=view&id=1T3exMef4y9duY8lDCi8u99Zy1weAJIp-",
            "https://drive.google.com/uc?export=view&id=1m6myRe6NrhuUdUZ8ofDAwotKb6vQjT04",
            "https://drive.google.com/uc?export=view&id=1iokAPMnM6QobWuBRRi1MINDOWg_jlWof",
            "https://drive.google.com/uc?export=view&id=1qr2Yse63JQKV61uhLidn-2ju8hVWYK9z",
            "https://drive.google.com/uc?export=view&id=17wxAWgDMbQW2amYd2DajbtEmygVVpLQb",
            "https://drive.google.com/uc?export=view&id=1zWD4DC8citgoCJ8dqOBLtblenk0K6rmv",
            "https://drive.google.com/uc?export=view&id=1sOgluXXBmg5w_6lNXf8Ox8Egue2PPkVH",
            "https://drive.google.com/uc?export=view&id=1h6Z-64aM2riDLJraqKnm_jE3dU6jfJXz",
            "https://drive.google.com/uc?export=view&id=1RFJ-ZT1NoSrrr54GXA0VrfRj4JWDPzZX",
            "https://drive.google.com/uc?export=view&id=1NAXVSHb_bxaJGhMEvxsVTndFUa-6f33h",
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
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal": "Usul",
                "alamat": "Jl. Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva, follow @cerebral.id_",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "Jalan-jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "Ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Main-main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal": "Swiss",
                "alamat": "Pemda",
                "hobbi": "Nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "B. Lampung",
                "hobbi": "Baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Beli risol ayam Naya",
                "sosmed": "@cindylauura",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton reels Agz",
                "sosmed": "@deaamnd3_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Like crowded",
                "hobbi": "Gibah sama Lulu",
                "sosmed": "@devynasonyaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19",
                "asal": "Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal": "Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Minta tolong Adit",
                "sosmed": "@fatthyaa_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Khazanatil Ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Korpri Raya",
                "hobbi": "Nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Menonton film",
                "sosmed": "@melynznb",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Gang Nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal": "Batam, Kepri",
                "alamat": "Gang Sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Jelajahi desa Lamsel",
                "sosmed": "@tari_sya23",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dj9XjxQIr1oZpj7RXYnjxsmENZhz4rAS",
            "https://drive.google.com/uc?export=view&id=1JyAZxjpSkCTASzhZE9NrXqgO5Emcj1fl",
            "https://drive.google.com/uc?export=view&id=1XgKFBALP9VNhjGmWBQcVM4yhMHzpZSSi",
            "https://drive.google.com/uc?export=view&id=1rH-KSr1hl0qzM6rL2vJQQGliC4ZujJiT",
            "https://drive.google.com/uc?export=view&id=19WMow8zHlVutKBGORYCzJ8ul-ll-z5c8",
            "https://drive.google.com/uc?export=view&id=1odgVHLZzKZzcSlIx7RdQOZpQkF4NWqDc",
            "https://drive.google.com/uc?export=view&id=1UQTqFv6kpL8QiMGev_S5AYZnmVGIJxD2",
            "https://drive.google.com/uc?export=view&id=15H_YD2YtCH68BQfoueCXrej5LFOvfEyw",
            "https://drive.google.com/uc?export=view&id=1tu3nQjzOokkrSee88yUu_giM8qYr5A8X",
            "https://drive.google.com/uc?export=view&id=1iiH7eh2bdKpgH_0Twhky_S4YSPGSBWNc",
            "https://drive.google.com/uc?export=view&id=1awH8h-SlaIxKkzDDaFJbnLr3FwsCnLUm",
            "https://drive.google.com/uc?export=view&id=1CAAWrWwmUfXmAzLYpUwS0ze0R41kSN3g",
            "https://drive.google.com/uc?export=view&id=1Woz8-FaphOuFMr_N5XpSQdYMvibBKB1O",
            "https://drive.google.com/uc?export=view&id=1kX1v0AlKDjagyDTfSPsvhymtl3_wmXpF",
            "https://drive.google.com/uc?export=view&id=1gNr7Pbl3SolGlF6o8SYOxPUxs1cP9EyH",
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
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": 22,
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Memancing",
                "sosmed": "@renta.shn",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": 21,
                "asal": "Brebes, Jateng",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@salwa.fhn",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": 20,
                "asal": "Pekan Baru",
                "alamat": "Asrama TB4",
                "hobbi": "Main Palinfit",
                "sosmed": "@azzah.raaa_",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450106",
                "umur": 18,
                "asal": "Pekan Baru, Riau",
                "alamat": "Airan",
                "hobbi": "Mancing Ribut",
                "sosmed": "@haikalsbln_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Iqfinah Haula Halika",
                "nim": "123450076",
                "umur": 20,
                "asal": "Lampung Barat",
                "alamat": "Sukarame",
                "hobbi": "Berkhayal",
                "sosmed": "iqfinanhalikaa_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "May Thalita Dehlia",
                "nim": "123450009",
                "umur": 20,
                "asal": "Bandung",
                "alamat": "Kedaton",
                "hobbi": "Menyelam",
                "sosmed": "@may_dahlia12",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Naufal Algahni",
                "nim": "123450116",
                "umur": 20,
                "asal": "Sidorejo",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton Anime",
                "sosmed": "@muhammadnaufalalghani",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": 19,
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Olahraga",
                "sosmed": "@zailanisatria",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": 21,
                "asal": "Tanggerang",
                "alamat": "Belwis",
                "hobbi": "Nyanyi",
                "sosmed": "@reaxender",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": 20,
                "asal": "Jakarta Selatan",
                "alamat": "Belakang UIN",
                "hobbi": "Menggoreng Pisang",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": 19,
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobbi": "Bermain Musik",
                "sosmed": "@kerenmrtv",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450004",
                "umur": 20,
                "asal": "Padang",
                "alamat": "Perumnas, Way Kandis",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sarah Warti",
                "nim": "123450057",
                "umur": 20,
                "asal": "Jawa Barat",
                "alamat": "Tanjung Senang",
                "hobbi": "Berkebun",
                "sosmed": "@sarahwrti",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": 19,
                "asal": "Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "Mengetik",
                "sosmed": "@zhrptsr",
                "kesan": "",  
                "pesan":""# 1
            },
     
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AHVrBBTSUs2gtHfljAaJlj_1mRKemm9e",
            "https://drive.google.com/uc?export=view&id=1vUK-LzciuQ9-eWo-U0FpqExFnP-e7N-1",
            "https://drive.google.com/uc?export=view&id=1NHMorgZ7eJua3DFQZLr2A2h6gGrI0wwW",
            "https://drive.google.com/uc?export=view&id=1_5xvJ0HgOUXsKIXUndmtMGW0aHEJqLr_",
            "https://drive.google.com/uc?export=view&id=1jPRvnTLkwz6KU9Oc0YswTVr_q9nU9sCQ",
            "https://drive.google.com/uc?export=view&id=1sUW0sSNi_70TbV1vd5H2rTVSTMlqqEhT",
            "https://drive.google.com/uc?export=view&id=1iT-5xjjGAY0rlR2hAYrtLahpYWq2SYuD",
            "https://drive.google.com/uc?export=view&id=1aMlbtS3v93DdPckQpLtLG5KZmV1xJYnS",
            "https://drive.google.com/uc?export=view&id=1FjGuK_UOMOa8hLGCPvOHaRatfbBsJs2-",
            "https://drive.google.com/uc?export=view&id=1w8zmQtS0R59tR7o8reyjqm8RW7P3X0vT",
            "https://drive.google.com/uc?export=view&id=1I8CFhBc3f5j18wzL362kB8rkFg3BlxLc",
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca novel",
                "sosmed": "@syalaishaa_31",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Beli parfum",
                "sosmed": "@den_iki_",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "nonton dramashort di fb",
                "sosmed": "@aprhtp_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nabila Zakiyah Zahra",
                "nim": "122450139",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way halim",
                "hobbi": "jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way kandis",
                "hobbi": "nonton drakor",
                "sosmed": "@deviirhyu",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Enggli Rahmadhani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "gg.perwira 2",
                "hobbi": "nonton alur cerita",
                "sosmed": "@englirahmdhanii",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Masak",
                "sosmed": "@_inayasari",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung karang",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
    
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1o4WhENhwFGcGHq5YPkWnw7h9lHbleCwQ",
            "https://drive.google.com/uc?export=view&id=19nAEvpAcj1m_ftbE5NRbdYDLsbdas2Wl",
            "https://drive.google.com/uc?export=view&id=1R1_L5I7Of_kgu0EX-zoj-krs5YEjb_5_",
            "https://drive.google.com/uc?export=view&id=180Fa34qWaVUOC2EsapDQ2XkJKcxYWSps",
            "https://drive.google.com/uc?export=view&id=1mb8TCIvtrOoSfbQ2VAe6OAB_k0J95els",
            "https://drive.google.com/uc?export=view&id=1dgfEdLhEP700RT4uGFF-Xo1u16uOUVDa",
            "https://drive.google.com/uc?export=view&id=1FrgP_waXdp8TODp3sNFpJxRPm3dao8lp",
            "https://drive.google.com/uc?export=view&id=1n6vPm5f3ph181Dpoy4JIlbfbdLHmL57O",
            "https://drive.google.com/uc?export=view&id=170WsEA6uhgRXpUjzAS34RcfEloAOK_vc",
            "https://drive.google.com/uc?export=view&id=1jhOZFWWCiDoX5bRakMI4slLl6HARd8lO",
            "https://drive.google.com/uc?export=view&id=12OrnRQROSbavnskW7nvopDrUSJXhchPN",            
            "https://drive.google.com/uc?export=view&id=1VfvKjCtoM9kiz56X5InZjbPgX2Uj0p7Z",
            "https://drive.google.com/uc?export=view&id=1oKUBkzHc-JMmLsBBusve19vTYGBzJ62G",            
            "https://drive.google.com/uc?export=view&id=1b8hfOYjC-kAjNJT31XhMRWlzue1VQENT",
            "https://drive.google.com/uc?export=view&id=1a1jcHxlbC6IH2bu_jBpmEBbwnPbtk1x6",
            "https://drive.google.com/uc?export=view&id=1y9A_T1Zbibykxl_YKKABOskRCBtPPWTc",
            "https://drive.google.com/uc?export=view&id=1L6G_OUwoLJ02TaB4ts5CAI4Gwuw3m49C",
            "https://drive.google.com/uc?export=view&id=17Rc-NXsfQAv7Z5YwPSacIaZqBTo_jAo2",
        ]
        data_list = [
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Sleep call",
                "sosmed": "@patriciadiajeng",
                "kesan": "",  
                "pesan":""
            },
           {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "jl.Kresna, korpri",
                "hobbi": "Masak",
                "sosmed": "@rahmanellyana",
                "kesan": "",  
                "pesan":""# 1
            },
             {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "22",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Billiard dan volly",
                "sosmed": "@mananam_",
                "kesan": "",  
                "pesan":""# 1
            },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way huwi",
                "hobbi": "Motoran",
                "sosmed": "@noe_rruuu",
                "kesan": "",  
                "pesan":""# 1
            },
           {
                "nama": "Rafi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Ngoleksi gelang",
                "sosmed": "@refadp_",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@tryyaniciaaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "Kota bumi, Lampung utara",
                "alamat": "jl.pangeran senopati raya",
                "hobbi": "Main gitar",
                "sosmed": "@aliyaamara",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way huwi",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donamaya.p",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "",  
                "pesan":""# 1
            },
                        {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuan ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payakumbuh, Sumatera barat",
                "alamat": "jl.Lapas, kec.Jati Agung",
                "hobbi": "mendengarkan musik",
                "sosmed": "@naylasalsabilaa",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Akmal Faiz Abdilah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Main hp",
                "sosmed": "@i",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Airan raya 1",
                "hobbi": "membaca, menulis, memasak",
                "sosmed": "@nltg._",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Melukis",
                "sosmed": "@citrastin",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigirtmv",
                "kesan": "",  
                "pesan":""# 1
            },
            {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatera utara",
                "alamat": "Kelengkeng 2, Pemda",
                "hobbi": "Dance",
                "sosmed": "@roms.slbn",
                "kesan": "",  
                "pesan":""# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

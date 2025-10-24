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
            "https://drive.google.com/uc?export=view&id=14HGAyw0Kh44vLVH3b_uRypM6bpGzXV4L",
            "https://drive.google.com/uc?export=view&id=1_RHN-ZtRL6hB5YMPHcqAMHqboHO2aO6M",
            "https://drive.google.com/uc?export=view&id=14u7N_mKR8li-hPvzH9rIELEqveFq1ki6",
            "https://drive.google.com/uc?export=view&id=1jveA2Aj04qXbqyFF6DqlmQ9EADCseAQn",
            "https://drive.google.com/uc?export=view&id=1EOgxCCGUQe1CRcLbnUZqVju0uwFwsXfX",
            "https://drive.google.com/uc?export=view&id=12bKFwlul9tBO7MhaOtZTC0eRGQTYPGKO",
        ]
        data_list = [
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Pulau Damar",
                "hobbi": "Makan Pisang",
                "sosmed": "@_erendraa",
                "kesan": "aura kepemimpinan dan tugas abangnya keliatan banget, tapi ternyata bisa humble juga ",  
                "pesan": "semangat untuk tugas akhirnya bang, semoga lancar "# 1
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Baca buku sequel ",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya asik banget, enjoy ngedengar abangnya kalau bawain materi, ga bikin ngantuk sama sekali ",  
                "pesan": "semangat juga bang jo tugas akhirnya, jaga kesehatan jangan lupa bang "# 1
            },
              {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Ayres Kost",
                "hobbi": "Gangguin Orang",
                "sosmed": "@celisabethh_",
                "kesan": "kakaknya cantik dan imupp banget, bawaannya ceria terus ",  
                "pesan": " Sukses terus buat segala rencana dan mimpi kakak"# 1
            },
              {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya kalem banget, keren bisa ngimbangin energi kakak, abang yang lain hehe ",  
                "pesan": "Jangan lupa istirahat ya, kak! "# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "21",
                "asal": "Sammosir/Sumatera Utara",
                "alamat": "Natar (Raden Intan)",
                "hobbi": "Nemenin orang dari nol sampai jatuh ke jurang kemiskinan",
                "sosmed": "@eksantyfebriana",
                "kesan": " kakaknya jago cairin suasana ",  
                "pesan":"Semanagt untuk terus berkembang dan ngeraih cita-citanya kak "# 1
            },
             {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450001",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Cutek Kahim",
                "sosmed": "@farahanumafifah",
                "kesan": "kakaknya humble banget, bisa serius tapi bisa asik juga ",  
                "pesan": "semangat kuliahnya kakk "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SIZQWnW86RBFzAhlxZJDAFByUa_bLUAq",
            "https://drive.google.com/uc?export=view&id=1m3IZtgHB-S3CpWySSPv0VFWCQuAv9-cH",
            "https://drive.google.com/uc?export=view&id=1h1gZJbMJYe7RtIoYp0v2iZwaBzi1jhXT",
            "https://drive.google.com/uc?export=view&id=15gThKRX2Un1l0fvYByYvdEkghyCPKFkv",
            "https://drive.google.com/uc?export=view&id=13lZjoEC6SkZgDxWRhoznPBuGfjIdAvNM",
            "https://drive.google.com/uc?export=view&id=1NVLqSXpEkbSXYmzElvutJtkY3Menqf1Y",
            "https://drive.google.com/uc?export=view&id=1iW5WMrSU7x5Elx5SsNLCXnL4sqFFfnMB",
            "https://drive.google.com/uc?export=view&id=1hEya_NrIEo6l_5GcjcKhBu09BVBZ0K5c",
            "https://drive.google.com/uc?export=view&id=1XjEP9NNmwtUVfVmhJyWrIKWyagqq9KUi",
            "https://drive.google.com/uc?export=view&id=1zU5dayTnrumr3XY2pbfKQCSXCSMB4FFU",
            "https://drive.google.com/uc?export=view&id=1xMakceiyWW5P17-WPQF7wbSRSCImxm8u",
            "https://drive.google.com/uc?export=view&id=1jFjgSBCkgVNDvQQFLSvynmaFc5Do9TP4",
            "https://drive.google.com/uc?export=view&id=1RGrgaxHlaSgZTKNZ-YwU0ZMWguT0ibOb",
            "https://drive.google.com/uc?export=view&id=1Px-ZVwVlZuXCYqQJ-vRqgJajCymISTAc",
        ]
        data_list = [
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "21",
                "asal": "Nusa Kambangan",
                "alamat": "Lapas , Belwis",
                "hobbi": "Melarikan Diri",
                "sosmed": "@jeremia_s_ ",
                "kesan": "abangnya chill dan asik bangett,terus pintar juga ",  
                "pesan": "semangat ngeaspraknya bang, jangan lupa istirahat ya bang "# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "21",
                "asal": "Kendari",
                "alamat": "Metro",
                "hobbi": "Bertutur kata baik dan sopan",
                "sosmed": "@_.dheamelia ",
                "kesan": "kakaknya humble dan keliatan humoriss ",  
                "pesan": "semangatt terus ya Kak, terus jadi versi terbaik dari diri kakak sendiri "# 2
            },
              {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "22",
                "asal": "Teluk",
                "alamat": "Teluk",
                "hobbi": "Jualan Pancing",
                "sosmed": "@renishapg",
                "kesan": "Kakaknya keliatan kalem dan pendiam ",  
                "pesan": "Tetap jaga kesehatan ya kak. Jangan lupa makan kakk! "# 1
            },
              {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mencari kesibukan",
                "sosmed": "@ansftynn_",
                "kesan": "kakaknya juga kalem dan murah senyum banget ",  
                "pesan": "Walau sibuk, jangan lupa senyum ya kak "# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton AGZ",
                "sosmed": "@dhruchyo",
                "kesan": "Abangnya pintar banget, cara ngajarnya juga enak dan mudah dipahami ",  
                "pesan":" semangat kuliahnya bang, jangan lupa untuk jaga kesehatan juga bang "# 1
            },
             {
                "nama": "Feby Wulandari",
                "nim": "123450042",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Nguleg Cabai",
                "sosmed": "@fby.wlndr",
                "kesan": "kakakknya lucuu banget kaya anime, gemesh ",  
                "pesan": "Jangan lupa bahagia di tengah sibuknya kuliah dan tanggung jawab, kak "# 1
            },
              {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Nemenin ridho main pedel",
                "sosmed": "@givarooo",
                "kesan": "abangnya baik, humble dan murah senyum banget ",  
                "pesan": " Semangatt ngerjain tugas-tugas kuliahnya bang"# 1
            },
              {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Istirahat",
                "sosmed": "@myrrinn",
                "kesan": "abangnya keliatan cool dan kalem banget ",  
                "pesan": "tetap semangat ngejalanin kuliahnya bang"# 1
            },
              {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Belwis",
                "hobbi": "Ngukir Sabun",
                "sosmed": "@berlyyanda",
                "kesan": "kakaknya keren banget, vibesnya kaya tegas dan lembut di satu waktu",  
                "pesan": "Jangan lupa untuk istirahat setelah padatnya kegiatan ya kak "# 1
            },
              {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Teluk Kuandama",
                "alamat": "Belwis",
                "hobbi": "Mendengarkan wave to earth",
                "sosmed": "@j__eesie",
                "kesan": "senang banget liat kakaknya, bawaanya kaya happy terus ",  
                "pesan": "Tetap jadi pribadi yang positif ya kak, semangatnya selalu nular ke orang lain "# 1
            },
              {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "19",
                "asal": "Medan",
                "alamat": "GH",
                "hobbi": "Main Pedel",
                "sosmed": "@iamridhomanik ",
                "kesan": "lesung pipi abangnya manis banget ",  
                "pesan": "Tetap semangat ya kak, semoga setiap langkah kuliah kakak selalu dimudahkan "# 1
            },
              {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "22",
                "asal": "Sumatera Selatan",
                "alamat": "Kobang",
                "hobbi": "Ngeliatin warna baju orang",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya pintar dan dewasa banget ",  
                "pesan": "semangat terus ngeaspraknya bang, jangan lupa istirahat ya bang biar ga kecapean "# 1
            },
              {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Makan gula merah",
                "sosmed": "@monica_tjg ",
                "kesan": "senyum kakaknyaa manis banget ",  
                "pesan": "Jangan lupa istirahat, kak, tubuh juga butuh tenang di sela kesibukan "# 1
            },
              {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "19",
                "asal": "Tanjung Batu",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk ",
                "kesan": "kakaknya imut dan lucuu banget ",  
                "pesan": "Jangan lupa jaga kesehatan ya kak, semangat gak akan berarti kalau sakit "# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eFa-Jbmkvt0LC1BKs44SgJsD9GKP7RPM",
            "https://drive.google.com/uc?export=view&id=1B9EJfCS0m-w6GvJUUvPBD3jC1V0twn8d",
            "https://drive.google.com/uc?export=view&id=1F5KATtVQvtvXlkISpgsNEsLe-AFAs0as",
            "https://drive.google.com/uc?export=view&id=10PzSHPtiHTKMVtCVZDiv2meMZfQrM2ET",
        ]
        data_list = [
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Kobam",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya berwawasan dan keren bangett ",  
                "pesan": "semangat untuk terus berkembang ya bang,tetap jadi inspirasi buat banyak orang "# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450043",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengar Lagu ",
                "sosmed": "@nadyaanjaani",
                "kesan": " kakaknya cantik bangett, btw funfact sama nama ig kita sampir sama kak hehe ",  
                "pesan": "Jangan lupa jaga kesehatan ya kak, karena tubuh juga perlu perhatian "# 1
            },
              {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Asrama TB 1",
                "hobbi": "Melamun",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakaknya baikk banget, vibesnya adem banget ",  
                "pesan": "Tetap fokus tapi jangan lupa nikmatin prosesnya ya kak "# 1
            },
              {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Indomaret Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@lia.h_264",
                "kesan": "kakaknya ceria banget orangnya ",  
                "pesan": "Ceria dan Bahagia selalu ya kak "# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nbPQsbKmoCVgyXtjlfUd4uGHQdMq5-Qo", #1
            "https://drive.google.com/uc?export=view&id=1cgpxcNxXUtjDViwpKrXigz4eNxrs85_X", #2
            "https://drive.google.com/uc?export=view&id=1ormaBl5jtFD0kLIXDD2fOyXxKK6hIbPC", #3
            "https://drive.google.com/uc?export=view&id=1Y0SEf-AL8xZvhWnziMDFHUzhX4iWm53N", #4
            "https://drive.google.com/uc?export=view&id=1432_MkX0X5Jaza3Osy8IFNRfqWjYdTCf", #5
            "https://drive.google.com/uc?export=view&id=11JSfLS1fn0la8yJF9sb8Jh0j1lkNY4ks", #6
            "https://drive.google.com/uc?export=view&id=1dYtl3AU6cY34E_0qA65qed8Eo5SDA1mG", #7
            "https://drive.google.com/uc?export=view&id=16X-4PWgh7fJOvAAXwXUm0JbxbDhfpUyK", #8
            "https://drive.google.com/uc?export=view&id=18A_tuf9rokWfsx5QELP4kISjraqYrIls", #9
            "https://drive.google.com/uc?export=view&id=1ONSeWLHFVUXXLVlFWEZ9ge_06epwyRnc", #10
            "https://drive.google.com/uc?export=view&id=101MqkqKkoU6ao_guwYhp2TEA-FPDAtk8", #11
            "https://drive.google.com/uc?export=view&id=1yaNODg_rO48ot32vZcHJU901xazkemR2", #12
            "https://drive.google.com/uc?export=view&id=1M-bmSuBZubsQVX_qqjKMFiUSjXZh3TM5", #13
            "https://drive.google.com/uc?export=view&id=1fsD2YmhN9caBl-7xcMJi3NC3hRvlhE1d", #14
            "https://drive.google.com/uc?export=view&id=1QfOss-yt860ucnPHLYoarONeWn4_TJPM", #15
            "https://drive.google.com/uc?export=view&id=1lnPHc4LGeoR0Yw1BQPq7oUlAv03boVnh", #16
            "https://drive.google.com/uc?export=view&id=1fTltcesGV2O56VcuPjIwmG3WOUtVYV3u", #17
            "https://drive.google.com/uc?export=view&id=1w_tgTKEPpdij-0T3kCVM5DqDp24DC-53", #18
            "https://drive.google.com/uc?export=view&id=1CwkmC1bd29vOkUO8J6PkdGoAH-PaK44Z", #19
            "https://drive.google.com/uc?export=view&id=1qNkEj-v62lvRMCC-g5EywLjgaOZCt1tS", #20
            "https://drive.google.com/uc?export=view&id=1BO4OHeZTpVOt5cho8AYHlnJggoix2k2o", #21
            "https://drive.google.com/uc?export=view&id=1MM1QGGcbmmmrO1C63gyzdVRJ61Ewy0YQ", #22
            "https://drive.google.com/uc?export=view&id=1BhFYbY-kWlQ24hDzZBqBgyzd-NaZPzJH", #23
            "https://drive.google.com/uc?export=view&id=1zob7mi6TRPHsjzPbThPbVawOkdfH4Dqe", #24
            "https://drive.google.com/uc?export=view&id=1Jkzeixiwax3Eweh1EwaTf5I6Od7-jDcm", #25
            "https://drive.google.com/uc?export=view&id=13xm5P6q1P7AjLG5cTxjJ3w9Oo1_jzg0d", #26
        ]
        data_list = [
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": " ",
                "hobbi": " ",
                "sosmed": "@ferdy_kevin ",
                "kesan": "abangnya tegas dan keren banget,tapi pas FG abang lucuu banget",  
                "pesan":"Semangat terus ya bang ngejalanin semester -semester akhirnya "# 1
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpsu",
                "hobbi": "Jalan jalan",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya manis dan imut banget, tapi kadang galak",  
                "pesan":"pasti lagi masa-masa sibuk banget ya kak, jangan lupa makan  dan istirahat yang cukup ya kak. "# 2
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "21",
                "asal":"Solok",
                "alamat": "Belwis",
                "hobbi": "Healing",
                "sosmed": "@allyapsha_",
                "kesan": "kakak itu tegas, tapi vibesnya kayak kakak yang mengayomi banget ",  
                "pesan":"semangat terus ya kak untuk ngejalanin segala kesibukannya, jangan lupa untuk jaga kesehatan kakak "# 3
            },
            {
                "nama": " Ahmad Rizky",
                "nim": "123450050",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "GH Belwis",
                "hobbi": "Main bola",
                "sosmed": "@ahmad.rizky___",
                "kesan": "abang ini cerdas dan berwibawa bangett, kerenn dan inspiratif banget ",  
                "pesan":"semangat terus dalam menciptakan prestasi-prestasi yang membanggakannyaa bangg "# 4
            },
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "24",
                "asal":"Kalianda",
                "alamat": "Deket kost dapa",
                "hobbi": "Nyari Keributan",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakaknya cantik banget, tapi kadang keliatan judes dikit",  
                "pesan":"Semangat kuliahnya kak,jangan lupa banyakin senyum ya kak hehe "# 5
            },
            {
                "nama": "Daffa Hadyan Navista",
                "nim": "123450025",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sebelah kost Arienta",
                "hobbi": "Jailin orang sampe nangis",
                "sosmed": "@daffahdynn_",
                "kesan": "kadang serem kadang lucu abangnya ",  
                "pesan":"Semangat ngerjain tugas-tugas kuliahnya bang "# 6
            },
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Kontrakan GH",
                "hobbi": "Banyak",
                "sosmed": "@ginda_mrp",
                "kesan": "abangnya keren banget, tapi keliatan agak galak ",  
                "pesan":"semanagt kuliahnya bang, jangan galak galak ya bang "# 7
            },
            {
                "nama": " Natasya Amavisca",
                "nim": "123450024",
                "umur": "20",
                "asal":"Pasar Muara Beliti",
                "alamat": "Kost Putri Gerbang Barat ",
                "hobbi": "Belajar",
                "sosmed": "@natasyaamavisca",
                "kesan": "kakaknya cantik banget, keliatan agak jutek dikit, tapi aslinya baikk banget ",  
                "pesan":"semangat belajar dan kuliahnyaa kakk "# 8
            },
            {
                "nama": " Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "20",
                "asal":"Akamsi",
                "alamat": "Sebelah kost kak Allya",
                "hobbi": "Kader",
                "sosmed": "@nobelnizam",
                "kesan": "abang ini cool dan tinggi banget, agak galak dikit ",  
                "pesan":" semangat kuliahnya bang, sellalu bagiin ilmu yang bermanfaat ya bangg"# 9
            },
            {
                "nama": " Nurul Alfajar Gumel",
                "nim": "122450127",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Marah",
                "sosmed": "@ji_gumel17",
                "kesan": " abang ini pembawaannya tegas, tapi aslinya baik banget dan ga pelit ilmu",  
                "pesan":"semangat ngasprak dan kuliahnya bang, semoga TA nya cepat selesai "# 10
            },
            {
                "nama": " Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Airan",
                "hobbi": "Marah-marah",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakak ini cantik bangeet, keliatan judes dikit, tapi aslinya ramah ",  
                "pesan":" semangat terus ya kak kuliahnya, jangan lupa untuk isitirahat yang cukup"# 11
            },
             {
                "nama": " Ahmad Sahidin Akbar",
                "nim": "122450144",
                "umur": "21",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Main Voli",
                "sosmed": "@Syahidzz_",
                "kesan": " abangnya keren bangett",
                "pesan": " semangat untuk terus berprestasi bangg" # 12
            },
            
            {
                "nama": " Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gang Nangka 4 Sukarame",
                "hobbi": "Main game, kuliner kalau ada uang",
                "sosmed": "@ali_parisi3",
                "kesan": "muka abangnya babyface banget, terus abangnya juga kalem dan pendiem banget ",
                "pesan": "Jangan lupa kasih waktu buat istirahat dan main juga ya bang" # 13
            },
            
            {
                "nama": " Rosalia Siregar",
                "nim": "123450036",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@rosaliasiregar",
                "kesan": " kakak ini ramah banget, mukanya juga maniss bangett",
                "pesan": "Tetap jadi orang baik dan ramah kayak sekarang ya kak. " # 14
            },
            
            {
                "nama": " Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Untung",
                "hobbi": "Scroll Tiktok",
                "sosmed": "@rismaa.mustika_",
                "kesan": " kakaknyaa baik, ramah dan care banget sama sekitar",
                "pesan": " tetap berbuat baik ya kak, jangan lupa care sama diri sendiri juga" # 15
            },
            
            {
                "nama": " Gusti Putu Ferazka",
                "nim": "123450046",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Tidur",
                "sosmed": "@ferazkaa",
                "kesan": " kakaknya cantik dan lucu banget",
                "pesan": "Jangan lupa makan ya kak, nanti sakit " # 16
            },
            
            {
                "nama": " Sahid Maulana",
                "nim": "122450109",
                "umur": "22",
                "asal": "Depok",
                "alamat": "Jl. Airan Raya",
                "hobbi": "Main Game",
                "sosmed": "@sahid_maul19",
                "kesan": " abang ini keliatan berwibawa dan berwawasannya, pasti pintar banget",
                "pesan": " Tetap semangat ya, bang. Jangan lupa istirahat biar nggak kelelahan." # 17
            },
            
            {
                "nama": " Daffa Ahmad Naufal",
                "nim": "122450137",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Cari masalah anak 23",
                "sosmed": "@ahmadnaufal_11",
                "kesan": " abangnya keren",
                "pesan": " jangan lupa jaga kesehatan ya bang, btw masalah ga dicari juga datang sendiri bang" # 18
            },
            
            {
                "nama": " Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis, Pemda",
                "hobbi": "Nangkap Lele",
                "sosmed": "ihsan.yusuf",
                "kesan": " abang ini kadang keliatan ada tegasnya, tapi kadang juga humoris gitu",
                "pesan": "semangat terus ya bang organisasi dan akademik nyaa" # 19
            },
            
            {
                "nama": " Rewina Audriya Melva Sari",
                "nim": "123450049",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@rewinaaa",
                "kesan": "kakak ini keliatan kalem dan pendiem banget, tapi baik banget juga ",
                "pesan": " semangat terus ya kak belajarnyaa, pasti bisaa" # 20
            },
            
            {
                "nama": " Benget Sidabutar",
                "nim": "123450047",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "sidabutar.26",
                "kesan": " abang ini lucuu bangett, pasti orangnya humoris",
                "pesan": "semangatt belajar dan kuliahnya bangg, tugasnya jangan lupa bang " # 21
            },
            
            {
                "nama": " Uliano William Purba",
                "nim": "122450098",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Main piano, ngoding, nanem anggrek, berantem",
                "sosmed": "@ulianowlm",
                "kesan": "abang ini agak seram dan galak ",
                "pesan": "jangan marah-marah bang, nanti tensinya tinggi " # 22
            },
            
            {
                "nama": " Kevin Antoni Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Panjang",
                "hobbi": "Main Basket",
                "sosmed": "@kevinaj_",
                "kesan": " abangnya keliatan menyeramkan sedikit, sama tinggi banget",
                "pesan": "semangat kuliahnya bang, jangan lupa senyum bang " # 23
            },
            
            {
                "nama": " Erma Daniar Safitri",
                "nim": "123450061",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Jl. Lapas Raya No 50",
                "hobbi": "Dance",
                "sosmed": "@d_aniar",
                "kesan": "kakak ini positive vibes bangett, murah senyum ",
                "pesan": " selalu bagiin energi positive kakak ke banyak orang ya kak, semnagat narinya kakk" # 24
            },
            
            {
                "nama": " Lidia Natasyah Marpaung",
                "nim": "123450015",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Merajuk",
                "sosmed": "@dla_natzzyaa",
                "kesan": "kakak ini manis bangett, cantiknya beda gitu ",
                "pesan": "jangan lupa jaga kesehatan ya kak, jangan ngambek lagi ya kak hehe " # 25
            },
            {
                "nama": " Muhammad Ridwan",
                "nim": "123450091",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@ridwan122",
                "kesan": "abangnya keliatan kalem orangnyaa ",
                "pesan": "tetap semangat jalanin perkuliahannya ya bang " # 26
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EmEQBOfMwlv6h7MTA-vnuDXULkF1iYAG", #1
            "https://drive.google.com/uc?export=view&id=1-4PYAtGMiHagZ7huSd8OIreHKQFAQ6M4", #2
            "https://drive.google.com/uc?export=view&id=1l0DsounTZVmxpzSf0PHtOXCJIRy8XwLz", #3
            "https://drive.google.com/uc?export=view&id=1o15qz2DQEjOYtqDTYfLs6zTGBvLzFkVz", #4
            "https://drive.google.com/uc?export=view&id=1vz9dUtMs8-69dEw1qWeohrrssz68A_UT", #5
            "https://drive.google.com/uc?export=view&id=1hev_4OCeN1OUu2AQFo_jzZaJ_ceShjny", #6
            "https://drive.google.com/uc?export=view&id=1nIHd3-OkGOdpyx4c3cSBa6kB9LppNDJc", #7
            "https://drive.google.com/uc?export=view&id=1muSKRP1XZv_vjMgkIUtDvki0gqpi4TEt", #8
            "https://drive.google.com/uc?export=view&id=1bZmnFpbY7vc9w0lopEir8NKj4fQMcws-", #9
            "https://drive.google.com/uc?export=view&id=1V2FuvHFDzJtm4cbocR9HR_bsSSS6XK42", #10
            "https://drive.google.com/uc?export=view&id=1f-6vkVDPSyuy36yYMK97oRQ4UOIafhXU", #11
            "https://drive.google.com/uc?export=view&id=1NJFxEatsPN8sjDWDIb2_mmO4d5lbVXdh", #12
            "https://drive.google.com/uc?export=view&id=1o0RHXUm0BtKPE0g2nQAhrQUswMAntclG", #13
            "https://drive.google.com/uc?export=view&id=14ncieBvvIWMiTn_hqErwe-h5vCyIm10u", #14
            "https://drive.google.com/uc?export=view&id=1UNzq1tLuHa7PLrUR-Sfl-FWUcOxJMtrS", #15
            "https://drive.google.com/uc?export=view&id=1Pbid62m3uhGLpjlRmZKbL7Ge7CKtYb49", #16
            "https://drive.google.com/uc?export=view&id=1dN8HQAruIm8njDH17PnMvohnby7T_AsD", #17
            "https://drive.google.com/uc?export=view&id=1amaka-7yW9SVTGqd2xqn_IG3sGN7zU2f", #18
            "https://drive.google.com/uc?export=view&id=1Bt3QR1VBDj6y65q87gR-luTvgvFpjLki", #19
            "https://drive.google.com/uc?export=view&id=1bady_d6jvhBOJnPCRaNjOP5nuJUa0sw3", #20
            "https://drive.google.com/uc?export=view&id=1UTlNXMemmuWcfJVAsnf1kKAR2x4Y6TYM", #21
            "https://drive.google.com/uc?export=view&id=1QrrWqOuEeeTJH2bACKCAH3ep-wKWGA1l", #22
        ] 
        data_list = [
            {
                "nama": " Randra Andriana Putra",
                "nim": "122450083",
                "umur": "22",
                "asal":"serang, Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan": " abangnya baik, asik dan pinter bangett",  
                "pesan":"semangat terus ya bang ngejalanin semester semester inii "# 1
            },
            {
                "nama": " Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "21",
                "asal":"Kepulauan Riau",
                "alamat": "Jalan Nangka 3",
                "hobbi": "Membaca Buku",
                "sosmed": "@junitaa_0406",
                "kesan": " kakaknya lucuu dan gemesinn",  
                "pesan":"terus bagiin energi positif ke sekitar ya kak "# 2
            },
            {
                "nama": " Muhammad Regi Abdi Putra Ananta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jalan Permadi, Sukarame",
                "hobbi": "Mendengar Musik",
                "sosmed": "@mregiiii_",
                "kesan": " Kakaknya pinter parah, tiap ngomong selalu ada yang bisa diambil",  
                "pesan":"semangatt teruss bang, jangan lupa kasih waktu untuk istirahatin diri ya bang "# 3
            },
            {
               "nama": "Aisyah Musfirah",
                "nim": "123450084",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Jl. Lapas",
                "hobbi": "Maskeran",
                "sosmed": "@_aishahi",
                "kesan": "kakak ini adem banget vibesnya, tutur katanya juga sopan dan lembut banget ",  
                "pesan":"istiqomah selalu ya kak, semangat kuliahnya kakk "# 4
            },
            {
                "nama": "Kakak Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Segar Miden",
                "hobbi": "Fore",
                "sosmed": "@fadilalfarizzii",
                "kesan": " abang ini keren bangett, banyak prestasi, public speakingnya juga bagus",  
                "pesan":"terus jadi inspirasi dan motivasi untuk orang orang disekitar ya bangg "# 5
            },
            {
                "nama": " Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "20",
                "asal":"Kampar, Riau",
                "alamat": "GH Belwis",
                "hobbi": "Ngerokok",
                "sosmed": "@muhammadaqil1111",
                "kesan": "abang ini baikk banget, ga pelit ilmu, dan selalu mau ajarin hal-hal yang belum kami pahami ",  
                "pesan":"semangat terus ya bang untuk jalanin hari harinya "# 6
            },
            {
                "nama": " Muhammad Naufal Ramadhan",
                "nim": "123450113",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@_notfall.s",
                "kesan": "abang ini kalem dan pendiem banget, tapi aura orang pinternya keliatan si ",  
                "pesan":" semangat belajarnya bangg"# 7
            },
            {
                "nama": " Nadia Faraj Alyafaatin Simbolon",
                "nim": "123450092",
                "umur": "21",
                "asal":"Kalianda",
                "alamat": "Jl. Manggis 1",
                "hobbi": "Menonton Film",
                "sosmed": "@nadiaafrj",
                "kesan": "kakaknya baik dan ramah bangeet, vibesnya tenang banget gitu",  
                "pesan":" jangan lupa untuk bahagia ya kakk, semangat kuliahnya kak"# 8
            },
            {
                "nama": " Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Jl. Nangka 3",
                "hobbi": "Main Musik",
                "sosmed": "@marletacornelia",
                "kesan": " Kakaknya humble banget, gampang nyatu sama siapa aja, kalau ketemu selalu bahas ozt hehe",  
                "pesan":" tetap jadi pribadi yang ceria ya kak,semangat ngejar impian juga kak " # 9
            },
            {
                "nama": " Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pramuka, bandar Lampung",
                "hobbi": "Mendengar Musik",
                "sosmed": "@keyshafi_",
                "kesan": "abang ini keliatan kalem tapi asik dan kerenn juga ",  
                "pesan":" semangat untuk terus maju dan berkembangnya bangg"# 10
            },
            {
                "nama": " Anggi Puspita Ningrum",
                "nim": "123450012",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jln. Seputih, Bumisari, Natar",
                "hobbi": "Mendengarkan musik, nonton drakor, ngedance",
                "sosmed": "@anggi_yllow2318",
                "kesan": "kakak ini imutt dan lucu bangett ",  
                "pesan":"jangan lupa kasih jeda untuk istirahat ya kak, semnagat terus belajarnya kak "# 11
            },
            {
                "nama": " Efi Defiyati",
                "nim": "123450005",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": " kakak ini orangnya pendiam, tapi tetap ramah ",  
                "pesan":" semangat untuk mempelajari hal-hal baru kedepannya kak"# 12
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "nim": "123450035",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Main Piano dan bernyanyi",
                "sosmed": "@hey.olla",
                "kesan": "kakaknya keliatan kalem dan tenang banget orangnya ",  
                "pesan":"tetap semangat terus ya kak, jangan lupa untuk istirahat juga kakk "# 13
            },
            {
                "nama": "Fairuz Ary Syifa",
                "nim": "123450044",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_fairuzary",
                "kesan": "kakaknya syar'i dan kece di satu waktu",  
                "pesan":"jangan lupa jaga kesehatan ya kak, sama semoga istiqomah hehe"# 14
            },
            {
                "nama": "Tanty Widyiastuti",
                "nim": "123450094",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Asrama TB 4 ITERA",
                "hobbi": "Tidur",
                "sosmed": "@tvnty_",
                "kesan": "kakaknya ramah banget dan keliatan humoris orangnyaa",  
                "pesan":"Tetap semangat jalani hari ya kak"# 15
            },
            {
                "nama": " Eggi Satria",
                "nim": "122450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Jl. Permadi",
                "hobbi": "Bernafas",
                "sosmed": "@_egistr",
                "kesan": " abangnya keren, keliatan muka muka suka ngodingnya",  
                "pesan":"Jangan lupa istirahat ya, Bang. Capek juga butuh waktu buat pulih "# 16
            },
            { 
                "nama": " Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Padang, Sumbar",
                "hobbi": "Isengin orang dan ngobrol random with gpt",
                "sosmed": "@fifah.zy",
                "kesan": "kakaknya keren banget gayanya, ramah dan enak banget diajak ngobrol juga",  
                "pesan":"Terus semangat ya, kak. Jangan lupa bahagia juga di tengah kesibukan kakak "# 17
            },
            {
                "nama": " Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Jalan Teratai No 27A, Kedaton",
                "hobbi": "Jadi PJ Kelas bu Febri",
                "sosmed": "@biyokcb",
                "kesan": "abangnya keren dan asik bangettt, pasti jago banget ngodingnya ",  
                "pesan":" Terus semangat berkarya, Bang. Ilmu abang bener-bener inspiratif buat kami"# 18
            },
          
            {
                "nama": " Rahma Oktavia Albar",
                "nim": "123450003",
                "umur": "19",
                "asal":"Bengkulu Selatan",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Main Catur",
                "sosmed": "@_rhmaoktvia",
                "kesan": "kakakk lucu banget, babyface kaya anak SMP, ceria bangett juga",  
                "pesan":"Tetap sebarin energi baik itu ya kak"# 19
            },
            {
                "nama": " Rahmah Gustriana Deka",
                "nim": "123450102",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "ngerepotin Tanty",
                "sosmed": "@gustriana.d_",
                "kesan": "kakaknya ramah dan murah senyum bangett",  
                "pesan":"Tetap jadi pribadi yang hangat dan rendah hati ya kak"# 20
            },
            {
                "nama": " Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakaknya terlihat kalem, btw pasti abangnya udah pro banget ngodingnya",  
                "pesan":"Tetap jadi pribadi yang tenang tapi menyenangkan ya, kak."# 21
            },
            {
                "nama": "Giofani Aristyo",
                "nim": "123450065",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Pemda",
                "hobbi": "Catur",
                "sosmed": "@giofaniars_",
                "kesan": "abangnya pinter,cool dan keren bangettt ",  
                "pesan":"Terus sebarkan ilmunya ya, bang. "# 22
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1p4CK9kMKjrRcWpuAeo64XfnUpm2VmftB", #1
            "https://drive.google.com/uc?export=view&id=1ZW_x5oUWuj4QXgYJGT8dLvz28t4x4dew", #2
            "https://drive.google.com/uc?export=view&id=1gBgsMIExJ5uHOZmMl-Dd038pwZCB7uCF", #3
            "https://drive.google.com/uc?export=view&id=1WLA3AmqCs4X9TFnpTvDblJVkoxO_xlq3", #4
            "https://drive.google.com/uc?export=view&id=1-eoCaOY_94mKBcUVLNNusX5_sodU7S3F", #5
            "https://drive.google.com/uc?export=view&id=1qx3T2sErYefRZtn_RkJtLx3WeTByGG0n", #6
            "https://drive.google.com/uc?export=view&id=1DgH1wuui3sSrT2rweno9vfXlZxnPBxPB", #7
            "https://drive.google.com/uc?export=view&id=1Xka578kRqGugOJSAAzXHot5iac82Dw1r", #8
            "https://drive.google.com/uc?export=view&id=112UI8Kp4UtHpnwGU9LOgHBZxNFAu3yRO", #9
            "https://drive.google.com/uc?export=view&id=11ERhjQ7QJXcffabO-hvDR9Q2yW3I4wBQ", #10
            "https://drive.google.com/uc?export=view&id=1iBYM0Mme5Gleb13fI0gs5PtPw_zoSD1M", #11
            "https://drive.google.com/uc?export=view&id=1IX1MBRduubs5PbJcs30TXWCcvDSsX5W0", #12
            "https://drive.google.com/uc?export=view&id=1SG6XfhX8Tl8VCBZ5kfj0_pQhmsKPUarE", #13
            "https://drive.google.com/uc?export=view&id=180yRSFcTf9MFFuPIiCzYTAztg-_w5Isi", #14
            "https://drive.google.com/uc?export=view&id=1OUZ_reCbzW7q4qY94j2yY8NzBGjUpLeN", #15
            "https://drive.google.com/uc?export=view&id=1GlDHPrPGrkOlaBSOk_KmX76VaCfclHrb", #16
            "https://drive.google.com/uc?export=view&id=1bcr-fJ5Am_X85fjgbD1eMdRdU1mPtvyE", #17
            "https://drive.google.com/uc?export=view&id=1Vwg-h0NCdadnVU29XC8z1erEkDDmz0t0", #18
            "https://drive.google.com/uc?export=view&id=1Cg8zEd5eldwPwaMHPfr0Wzd5H2BJOE-u", #19
            "https://drive.google.com/uc?export=view&id=1H70f1A9Rg1uKI1ohtBxe2xgzQjmw6ZP6", #20
            "https://drive.google.com/uc?export=view&id=18JZguqhX2OCtmYivYmalygb8k32Xgx5H", #21
            "https://drive.google.com/uc?export=view&id=1M4wNDLKkikMaWr4_8lQsiKEEg32I6TL1", #22
            "https://drive.google.com/uc?export=view&id=1MKjWGG1yuzk7doYZoe51qWwFgejhxb7q", #23
            "https://drive.google.com/uc?export=view&id=1DThVLTB-3gPBY3pTPyFqEvnSpd6fLLuq", #24
        ]
        data_list = [
            {
                "nama": " Arafi Putra Maulan",
                "nim": "122450002",
                "umur": "20",
                "asal":"Spanyol",
                "alamat": "Asrama",
                "hobbi": "Bank BSI",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": " Abangnya pintar banget, keren",  
                "pesan":"jaga kesehatan ditengah kesibukan ya bang, semoga lancar sampai wis-udah"# 1
            },
            {
                "nama": " Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Usul",
                "alamat": "Jl Hidup",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kakaknya asik bangett ",  
                "pesan":" semangaatt kak, dikit lagi wis-udah"# 2
            },
            {
                "nama": " Dea Mutia Risani",
                "nim": "122450099",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@deaa.rsn",
                "kesan": "kakaknya humble dan baikk banget  ",  
                "pesan":"semangat terus sampai wis-udah nya kakk, jangan lupaa jaga kesehatan ya kak "# 3
            },
            {
                "nama": " Devyna Sonya Palupi Sanjaya",
                "nim": "123450007",
                "umur": "20",
                "asal":"Duo P(Palembang & Pringsewu)",
                "alamat": "like crowded",
                "hobbi": "Scroll template jj & ngasprak",
                "sosmed": "@devynasonyaa",
                "kesan": "kakakk kerenn bangett, bisa bagi waktu untuk semua kesibukannya ituu, baik bangettt jugaa ",  
                "pesan":" semangat ngaspraknya kakk, jangan lupa kasih waktu untuk istirahat ya kak, jaga kesehatann jugaa"# 4
            },
            {
                "nama": " Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "19 ",
                "asal":"Tambun",
                "alamat": "Jl. Raden Saleh",
                "hobbi": "Nyubitin Ketang",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "kakak ini baik, ramah dan tida sombong",  
                "pesan":"Tetap jadi orang baik dan murah senyumm ya kakk "# 5
            },
            {
                "nama": " Cindy Laura Manik",
                "nim": "123450112",
                "umur": "20",
                "asal":"Sumatera Utara ",
                "alamat": "Belwis ",
                "hobbi": "beli risol ayam naya",
                "sosmed": "@cindylauura",
                "kesan": " kakaknya cantik banget kaya blasteran",  
                "pesan":" jangan lupa untuk bahagiaa ya kak, semangat terus kakak"# 6
            },
            {
                "nama": " Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21 ",
                "asal":"Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Bermusik",
                "sosmed": "@dsmannhal_",
                "kesan": " abang ini asik dan lucu banget ",  
                "pesan":" semangat terus untuk berkembang dan menghasilkan prestasi-prestasinya bang"# 7
            },
            {
                "nama": " Dea Amanda",
                "nim": "123450006",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "korpri",
                "hobbi": "nonton reels agz",
                "sosmed": "@deaamnd3_",
                "kesan": " kakak humble dan asik banget, enak kalau diajak ngomong",  
                "pesan":"semangat terus kuliahnya kak, semangat untuk terus berkembangg ya kak "# 8
            },
            {
                "nama": " Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main badmin, denger lagu",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya keliatan kalem pendiem gitu ",  
                "pesan":"jangan lupa jaga sehatan ya bang, lagi musim sakit "# 9
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "19",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame ",
                "hobbi": "minta tolong adit",
                "sosmed": "@fatthyaa",
                "kesan": "kakak humble dan murah senyum banget ",  
                "pesan":"semangat dan bahagia selalu ya kakk "# 10
            },
            {
                "nama": "khazanatil ilmi",
                "nim": "123450053",
                "umur": "20",
                "asal":"padang",
                "alamat": "korpri raya",
                "hobbi": "nonton",
                "sosmed": "@khazanatil_ilmi05",
                "kesan": " kakak cantik dan humble banget, baik banget jugaa",  
                "pesan":" semangat terus ya kakk nugasnya, kuliahnya, organisasinya"# 11
            },
            {
                "nama": "Nurul Izzah Istiqomah",
                "nim": "123450054",
                "umur": "20 ",
                "asal":"Batam",
                "alamat": "Gang nalim",
                "hobbi": "Baking",
                "sosmed": "@izzah_tq",
                "kesan": "kakaknya lucuu  dan ramah banget ",  
                "pesan":"istiqomah terus ya kak hijabnya hehe "# 12
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "21",
                "asal":"Batam, Kepri",
                "alamat": "Gang sakum",
                "hobbi": "Ngabisin bensin",
                "sosmed": "@qoisolifio_",
                "kesan": "abangnya kerenn ",  
                "pesan":"jangan lupa jaga kesehatan bang, btw hemat duit bang "# 13
            },
            {
                "nama": "Melinza Nabila",
                "nim": "123450122",
                "umur": "20 ",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "menonton film",
                "sosmed": "@melynznb",
                "kesan": "kakaknya imupp bangett ",  
                "pesan":"jangan lupa makan dan istirahat ya kak "# 14
            },
            {
                "nama": "Nayla Shafira Roza",
                "nim": "123450017",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kedamaian",
                "hobbi": "Me time",
                "sosmed": "@n.shafirarz",
                "kesan": "Kakaknya ramah banget ",  
                "pesan":"semangat kuliahnya kak "# 15
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Sukabumi",
                "alamat": "Belwis",
                "hobbi": "Open the new map",
                "sosmed": "@Ty_Tq90",
                "kesan": "abangnya asik dan chill bangett ",  
                "pesan":" "# 16
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": " jelajahi desa lamsel",
                "sosmed": "@tari_sya23",
                "kesan": " kakaknya kalem dan adem banget",  
                "pesan":"istiqomah terus ya kak "# 17
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Nyetrika baju",
                "sosmed": "@jasminednva",
                "kesan": " nama kakak keren banget",  
                "pesan":"jangan lupa makan ditengah kesibukan kakak ya kakk "# 18
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "sukarame",
                "hobbi": "main main",
                "sosmed": "@khoirulmuttoharoh",
                "kesan": "kakaknya baik ternyata, btw senyum kakaknya manis bangett ",  
                "pesan":"jalanin hari-hari dengan penuh semangat ya kak "# 19
            },
            {
                "nama": "Arya Muda Siregar",
                "nim": "123450063",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rawa Laut",
                "hobbi": "ngelamun",
                "sosmed": "@aryamudasiregar",
                "kesan": "vibes abangnya kaya abdi negara gitu ",  
                "pesan":"ngelamunnya jangan magrib-magrib ya bang "# 20
            },
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "20 ",
                "asal":"Lampung",
                "alamat": "Teluk, Bandar Lampung",
                "hobbi": "jalan jalan berkeliling dunia",
                "sosmed": "@elandraa_",
                "kesan": "kakaknya keliatan jutek ternyata engga,kalau senyum cantik banget  ",  
                "pesan":"semangat kuliahnya kak, biar bisa keliling duni "# 21
            },
            {
                "nama": "Syahrialdi Rachim Akbar",
                "nim": "123450093",
                "umur": "20",
                "asal":"lampung",
                "alamat": "b.lampung",
                "hobbi": "baca",
                "sosmed": "@syahrialdi_rchm",
                "kesan": " abangnya kerenn bisa mimpin acara besar kaya science fest kemaren",  
                "pesan":" semangat untuk terus berkembang ya bang"# 22
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "nim": "123450074",
                "umur": "17",
                "asal":"Swiss",
                "alamat": "Pemda",
                "hobbi": "nyari dataset",
                "sosmed": "@lutfiaisyh",
                "kesan": "kakaknya manis bangett apalagi kalau senyum ",  
                "pesan":" semangat nyari data setnya kak"# 23
            },
            {
                "nama": " Nabyla Sharfina",
                "nim": "123450008",
                "umur": "19",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas Raya",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": " kakaknya babyface banget",  
                "pesan":"semangat ngastutnya kak "# 24
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1g1BRbT-_6_EcDjPSbES3E_VOoC0WzC5X", #1
            "https://drive.google.com/uc?export=view&id=1kuLRMKtIc0-da3p-PC8IHV7BMCpWrpS8", #2
            "https://drive.google.com/uc?export=view&id=1qHWIIsLCO3_svFvR05r6f6mrnl1h-IOM", #3
            "https://drive.google.com/uc?export=view&id=1n7PPuYOajJp9VVc52VDwEFM3O-dD4Xxo", #4
            "https://drive.google.com/uc?export=view&id=1whS_zP80UiJ-i0W6Hy1FEHmAf31-cHxw", #5
            "https://drive.google.com/uc?export=view&id=1If-VO0k0k9x6lfDfdsXVZJVmlEnZnKVk", #6
            "https://drive.google.com/uc?export=view&id=1UOpGcZx7xZ5u-WXhEqeArzUg3hyk3x97", #7
            "https://drive.google.com/uc?export=view&id=1GDQgLVZF2EPkZ91u5yf7VpotEdv0TUgW", #8
            "https://drive.google.com/uc?export=view&id=17vXuGpIX32NGdVXrG4Ky-mQankigRwjn", #9
            "https://drive.google.com/uc?export=view&id=1VaMzkxbPaZvbX5HO2AhNCfN1ZNyIznAb", #10
            "https://drive.google.com/uc?export=view&id=13MiYdXwUOfUmFCrRTnPP3vAPnEwNrRT6", #11
            "https://drive.google.com/uc?export=view&id=1tOAfXQEgM57w5yqmZs3A-Z5y9L8I5Dov", #12
            "https://drive.google.com/uc?export=view&id=1oxi1PUUe1HcXJYOe52vSfdX_6sJrxc8m", #13
            "https://drive.google.com/uc?export=view&id=1KmTz62O8y0YJCnJYLMqHTArzMWZMC68k", #14
            "https://drive.google.com/uc?export=view&id=1znGKL_9iSjZkQL8LjlA1YBfIzX0TXRa8", #15
        ]
        data_list = [
            {
                "nama": " Rani Puspita Sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Datang kajian",
                "sosmed": "@rannipu",
                "kesan": " kakaknya humble dan ramah banget ",  
                "pesan":" semangat ngejalanin semester-semester akhirnya kak, jangan sampai stress ya kak "# 1
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "22",
                "asal":"Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": " kakaknya kerenn banget",  
                "pesan":"semangat untuk  terus berkembang ya kak "# 2
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "21",
                "asal":"Jawa Tengah",
                "alamat": "Airan",
                "hobbi": "Masak",
                "sosmed": "@salwa_fhn",
                "kesan": " cie bentar lagi kakak wis-udah",  
                "pesan":"semangat TA nya kak "# 3
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "nim": "123450013",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Gerbang barat",
                "hobbi": "Zumba",
                "sosmed": "@azza.raaa",
                "kesan": "hobinya keren ",  
                "pesan":"jangan lupa ngerjain tugas kuliah ya kak, semnagatt terus kak "# 4
            },
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "22",
                "asal":"Medan sananya dikit",
                "alamat": "Way Kandis",
                "hobbi": "Menghitung Krikil",
                "sosmed": "@haikalsbln_",
                "kesan": "nama abangnya keren, agak mirip bastian coboy junior ",  
                "pesan":"semangat ngitung kerikilnya bang, kalau lupa harus ngulang dari 1 soalnya bang "# 5
            },
            {
                "nama": "Iqfina Haula Halika",
                "nim": "123450076",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Baking",
                "sosmed": "@iqfinahalikaa_",
                "kesan": "kakak ini lucuu dan imupp banget ",  
                "pesan":"semangat ngebakingnya kak, next buka toko roti di gedung f kak hehe "# 6
            },
            {
                "nama": "May Talitha Dahlia",
                "nim": "123450009",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Belakang PB",
                "hobbi": "Yoga",
                "sosmed": "@may_dahlia12",
                "kesan": "kakaknya keliatan serem dikit hehe ",  
                "pesan":"jangan lupa untuk senyum ya kak, kakak manis kalau senyum "# 7
            },
            {
                "nama": "Muhammad Naufal Al Ghani",
                "nim": "123450116",
                "umur": "20",
                "asal":"Sidorejo, Sidomulyo, Kalianda",
                "alamat": "Sabah Balau",
                "hobbi": "Nonton anime",
                "sosmed": "@muhammadnaufalalghani73",
                "kesan": " Abangnya kelihatan cuek, tapi ternyata peduli dan perhatian.",  
                "pesan":"tetap semangat terus ya bang ngejalanin segala kesibukannya"# 8
            },
            {
                "nama": "Zailani Satria",
                "nim": "123450111",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "olahraga ",
                "sosmed": "@zailanisatria",
                "kesan": "abang ini keliatan pendiem, tapi kalau ngobrol asik",  
                "pesan":"jangan lupa makan dan istirahat yang cukup ya bang "# 9
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Belwis",
                "hobbi": "Melukis",
                "sosmed": "@rexanderr",
                "kesan": "abangnya keren banget, suara abang bagus ",  
                "pesan":"semangat untuk terus menghasilkan prestasi-prestasinya bang "# 10
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "20",
                "asal":"Cikarang",
                "alamat": "Gerbang Barat",
                "hobbi": "Melihat Cicak",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakak ini lucuu, imup, asik, manis, receh bangeet, enak kalau diajak ngobrol, kayak ngomong sama kakak kandung sendiri ",  
                "pesan":" tetap jadi orang yang cerita dan nebarin happy virusnya ya kak"# 11
            },
            {
                "nama": "Keren Marito Lumban Gaol",
                "nim": "123450020",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Bermain musik",
                "sosmed": "@kerenmrtl",
                "kesan": " kakaknya asikk banget orangnya",  
                "pesan":"selalu jadi orang yang baik dan asik ya kak "# 12
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Way Kandid",
                "hobbi": "Futsal",
                "sosmed": "@hnfdzky_",
                "kesan": "abangnya kalem banget tapi baik ",  
                "pesan":"jangan lupa jaga kesehatan ya bangg "# 13
            },
            {
                "nama": "Sarah Wasti",
                "nim": "123450057",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Tanjung Senang",
                "hobbi": "Main Alat Musik",
                "sosmed": "@ssarahwsti",
                "kesan": " kakaknya mirip shella mantannya arhan dikit kak",  
                "pesan":"semangat terus kuliahnya kak, masih setengah jalan lagi hehe "# 14
            },
            {
                "nama": "Zahra Putri Salsabila",
                "nim": "123450026",
                "umur": "19",
                "asal":"Natar",
                "alamat": "Way Huwi, Pemda",
                "hobbi": "rubik miror",
                "sosmed": "@zhrptsl",
                "kesan": "kakaknya cantik banget, bole ajarin main rubik kak ",  
                "pesan":"semangat main rubiknya kak, hehe, semangat kuliahnya juga maksudnya kak "# 15
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1v5aSshnpQ52x2M9eiYbAiIHfXlAsi5xB", #1
            "https://drive.google.com/uc?export=view&id=14oVZ7BokIji1Nu78Y-vN3iJ7hwrpLlu_", #2
            "https://drive.google.com/uc?export=view&id=1wP2VPcZigocu-JBEBhZo6eVkP8tpA8GI", #3
            "https://drive.google.com/uc?export=view&id=1r6LICCp1HqR37NuHKcRLiPP2Uoo0oxdR", #4
            "https://drive.google.com/uc?export=view&id=1qAzhSMuM8WQVHkZsA1AGmmJQvxMSFOaF", #5
            "https://drive.google.com/uc?export=view&id=18dQnTi_1iaINAs3VjZzPO-txynWyGWQY", #6
            "https://drive.google.com/uc?export=view&id=1MmO9MhK5Vg04z0emBqmfP8dlCg0s6Bar", #7
            "https://drive.google.com/uc?export=view&id=1nsNXzhg1MsKf8DHuOLvtemp2LCyN5WTQ", #8
            "https://drive.google.com/uc?export=view&id=1Vw8x6QqjhkRCySixQeswHJ75rsONAAM1", #9
            "https://drive.google.com/uc?export=view&id=107m0rzE6blHXyTAA8ap9XtZHy0ZDR3SK", #10
            "https://drive.google.com/uc?export=view&id=1R87R9I8MCxlX3XkQvSdNW0BEsVJBDOyy", #11
        ]
        data_list = [
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "22",
                "asal": "Bandar Lampung",
                "alamat": "Belakang PB Swalayan",
                "hobbi": "Jogging",
                "sosmed": "@dananghk_ ",
                "kesan": " abangnya lucu suka fllexing, tapi beneran keren kok bang ",  
                "pesan": " selalu jadi inspirasi buat banyak orang ya bang "# 1
            },
            {
                "nama": "Kakak Syalaisha Andina Putriansyah",
                "nim": "122450021",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Suka Rame",
                "hobbi": "Baca Novel",
                "sosmed": "@syalaishaa_31 ",
                "kesan": " kakaknya keliatan kalem dan pendiam orangnya ",  
                "pesan": " semangat terus ya kak, dikit lagi wis-udah "# 2
            },
              {
                "nama": "Kakak Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobbi": "Pergi ke cafe tengah malam",
                "sosmed": "@den_iki__",
                "kesan": " abangnya keren banget ",  
                "pesan": " jangan terlalu sering keluar malem bang, nanti meriang "# 3
            },
              {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Lampung Selatan",
                "hobbi": "Jogging",
                "sosmed": "@anadiacrn_",
                "kesan": " kakaknya keren banget, kaya tomboy gitu vibesnya ",  
                "pesan": "jangan lupa istirahat juga ya kak setelah aktivitas yang melelahkan"# 4
                   },
              {
                "nama": " Aprilia Dewi Hutapea",
                "nim": "123450040",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Nonton di Facebook",
                "sosmed": "@aprhtp_ ",
                "kesan": "kakaknya pasti intropet ",  
                "pesan": "hati hati penipuan di facebook ya kak "# 5
            },
            {
                "nama": " Nabila Zakiyah Zahra",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Jogging",
                "sosmed": "@nabila_zazahra",
                "kesan": " kakak ini agak mirip sama kak nydia dimataku ",  
                "pesan": " jangan lupa makan dan istirahat yang cukup kak  "# 6
            },
             {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Belajar",
                "sosmed": "@dhafinrzqa13",
                "kesan": " abangnya keliatan kalem dan pendiam ",  
                "pesan": "semangat kuliah dan organisasinya bang "# 7
            },
              {
                "nama": "Devi Rahayu",
                "nim": "123450010",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@deviirhyu",
                "kesan": " kakaknya imut dan gemessin banget ",  
                "pesan": " jangan lupa jaga kesehatan ya kak, jangan sering-sering begadang untuk marathon drakor ya kakk "# 8
            },
              {
                "nama": "Enggli Rahmadhani",
                "nim": "122450043",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Gang Pawira 2",
                "hobbi": "Main Mobile Legend",
                "sosmed": "@engliramdhnii",
                "kesan": "kakaknya maniss banget, ga ekspek hobinya ml ",  
                "pesan": "semangat main mlnya kak, tapi tugasnya jangan lupa ya kak "# 9
            },
              {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "kakaknya keren, bisa ngehasilin duit sendiri ",  
                "pesan": "semnagat jual risolnya kak, semoga laku "# 10
            },
              {
                "nama": "Nydia Manda Putri",
                "nim": "123450018",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Tanjung Karang Timur",
                "hobbi": "Main",
                "sosmed": "@nydiaaptr_",
                "kesan": "kakak ini imup banget, tapi keliatan kalem orangnya ",  
                "pesan": "jangan sampai lupa waktu ya kak mainnya hehe "# 11
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bD47SFe_i1YUF5uYDV6YXNUVWofw-DD3",
            "https://drive.google.com/uc?export=view&id=1BuQb-31Mcy62fRWpWBKigiFdVkMcV4Nu",
            "https://drive.google.com/uc?export=view&id=1nZZXgoGGmERY8Wl_UaXmpzRuA76r861i",
            "https://drive.google.com/uc?export=view&id=1-4IYo_st4YBMX7mDaAUTgzuZ-FyKX59E",
            "https://drive.google.com/uc?export=view&id=1wzIj5owESXeQm9K4NT8POs0Mc0QvRdRQ",
            "https://drive.google.com/uc?export=view&id=18X0zMGj1Lg8fvI2-8Oi9aEH3b1BE0F6w",
            "https://drive.google.com/uc?export=view&id=1Arfq31V3PKzqNFCcpFFDVbJ68Qa2mthb",
            "https://drive.google.com/uc?export=view&id=1pLVcbebIthwDbP2xai964Dz7bJQxb4gk",
            "https://drive.google.com/uc?export=view&id=1GZ-ZzVL2yWrEZWw4G10M1TR8aGnaBuA2",
            "https://drive.google.com/uc?export=view&id=1pYEos4hyBsYAOA-SXDzTYupCVcgjycyw",
            "https://drive.google.com/uc?export=view&id=1ZyO5SB8WTTivJknwY0PpxuJJbmFnMUBu",
            "https://drive.google.com/uc?export=view&id=1x4x462BL4Ad8P4K9YXBmhPH7pbYdvTJR",
            "https://drive.google.com/uc?export=view&id=1cvhjdIrVheNMvl4-tZSDg3VfRzZ92Ga9",
            "https://drive.google.com/uc?export=view&id=114zIoIYOvJymlPg7EfgAYd1TgPjlYWEW",
            "https://drive.google.com/uc?export=view&id=1BVF5_NvfqUUQ1TnyvGnkmV-SlbG8e8nK",
            "https://drive.google.com/uc?export=view&id=1lagNrwBM3n5DCHYAmh1mImd72SOVgDyj",
            "https://drive.google.com/uc?export=view&id=1MHDOmpo14wXFQjUQLYqjYlmKg38aqFl0",
            "https://drive.google.com/uc?export=view&id=1-1_wW4DgnXFHMBsxycLzRuB7U32JZT1w",
        ]
        data_list = [
            {
                "nama": " Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@patriciadiajeng",
                "kesan": "kakaknya cantik, baik, ramah, lucuu jugaaa",  
                "pesan": "semangat ngeasprakk nya kak, semoga TA nya lancar"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "21",
                "asal": "Lampung",
                "alamat": "Jalan Kresna, Korpri",
                "hobbi": "Nge-gym",
                "sosmed": "@rahmaneliyana",
                "kesan": "kakaknya ceria dan positive vibes banget",  
                "pesan": "tetap nyebarin positive virus ke banyak orang ya kakk"# 1
            },
              {
                "nama": "Khoirul Anam",
                "nim": "122450039",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pesawaran",
                "hobbi": "Volly, billyard",
                "sosmed": "@mananam__",
                "kesan": "abangnya keliatan kalem dan intropet",  
                "pesan": "semangat teruss bang"# 1
              },
              {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Way Huwi",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "abangnya keren banget, kaya atlet basket",  
                "pesan": "semangat juga bang jadi pdd abadinya"# 1
            },
              {
                "nama": "Ravi Diva Efangga",
                "nim": "123450001",
                "umur": "21",
                "asal": "Lampung Tengah, Gunung Sugih",
                "alamat": "Airan Raya",
                "hobbi": "Olahraga",
                "sosmed": "@rafidivaefangga_",
                "kesan": "abangnya humble dan baik banget",  
                "pesan": "semangat jadi pdd abadinya bang"# 1
            },
              {
                "nama": " Refa Destiny Pranata",
                "nim": "123450016",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Nge-vlog",
                "sosmed": "@refadp_",
                "kesan": "kakaknya lucu dan murah senyum",  
                "pesan": "semangat nge vlognya kak, semoga jadi seleb"# 1
            },
              {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Belajar",
                "sosmed": "@",
                "kesan": "kakaknya cantik banget, outfitnya keren",  
                "pesan": "semangat terus untuk ngecapai impian kakak ya kak"# 1
            },
              {
                "nama": "Aliya Ammara Ananta",
                "nim": "123450075",
                "umur": "19",
                "asal": "KotaBumi",
                "alamat": "Gracia Kost 1",
                "hobbi": "Main Gitar",
                "sosmed": "@aliyaammara",
                "kesan": "kakakk nim akuu,manis banget kakaknyaa",  
                "pesan": "semogaa kita bisa lebih dekat ya kak hehe "# 1
            },
              {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi, Jawa Barat",
                "alamat": "Way Huwi, Gang Mangga",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@donnamaya.p",
                "kesan": "kakakk ini baik, ramah, murah senyumm banget, ngajarinnya juga enak",  
                "pesan": "semangat nge-astutnya kakk"# 1
                },
              {
                "nama": "Feby Angelina",
                "nim": "123450039",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "kemiling",
                "hobbi": "scroll pinterest",
                "sosmed": "@writtenbyangel",
                "kesan": "kakaknya lucuu dan keliatan pendiem orangnya",  
                "pesan": "semangat terus kakk, jangan menyerah hehe"# 1
            },
              {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Labuhan Ratu",
                "hobbi": "Memasak",
                "sosmed": "@hafsa.fazila",
                "kesan": "Kakaknya maniss banget senyumnya",  
                "pesan": "Tetap semangat dan full senyum ya kak ngejalanin hari-harinya"# 1
            },
              {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "19",
                "asal": "Payahkumbuh, Sumatera Selatan",
                "alamat": "Jalan Lapas, Kec. Kota Agung",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@naylasasabilaa_",
                "kesan": "Kakaknya cantik tapi nggak sombong, malah ramah banget.",  
                "pesan": "Selalu jadi orang yang ramah dan baik kesemua orang ya kak"# 1
            },
              {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Airan Raya",
                "hobbi": "Main roblox",
                "sosmed": "@saniayyllstr",
                "kesan": "kakak ini mukanya keliatan judes, tapi ternyata baikk",  
                "pesan": "Semangat terus ya kak, tapi jangan sampai stress juga ya kak"# 1
            },
              {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Griya Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@_akmal.faiz",
                "kesan": "abangnya keliatan pro dalam hal design, pengen ketularan jagonya",  
                "pesan": "Semangat terus belajar dan berkembang ya bangg"# 1
            },
              {
                "nama": "Raihana Addelia Putri",
                "nim": "123450041",
                "umur": "19",
                "asal": "Lampug Tengah, Terbanggi",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca, memasak",
                "sosmed": "@n1tg._",
                "kesan": "Kakaknya punya aura positif yang bikin orang nyaman.",  
                "pesan": "Semangat terus ya kakk kuliahnya"# 1
            },
              {
                "nama": "Citra Agustin",
                "nim": "123450108",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Scroll Pinterest",
                "sosmed": "@citrastin",
                "kesan": "Kakaknya terlihat kalem, tapi ternyata seru juga pas diajak ngobrol.",  
                "pesan": "Semangat ya kak ngejalanin hari-harinya, jangan lupa untuk bahagia sellalu kak"# 1
            },
              {
                "nama": "Eigi Artamevia",
                "nim": "123450011",
                "umur": "20",
                "asal": "Krui, Kec. Pesisir Selatan",
                "alamat": "Sabah Balau Residence",
                "hobbi": "Melukis",
                "sosmed": "@eigitvm",
                "kesan": "Imut banget, kak! outfitnya juga lucu-lucu bangett",  
                "pesan": "semangat terus dan Tetap jadi diri sendiri ya kak"# 1
            },
              {
                "nama": "Romauli Oktavia Silaban",
                "nim": "123450014",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Kelengkeng 2 Pemda",
                "hobbi": "Menanyi",
                "sosmed": "@roms.slbn",
                "kesan": "Kak itu cantik luar dan dalam, selalu bikin suasana jadi ceria!",  
                "pesan": "Jangan lupa makan ya, kak. Kesehatan tetap nomor satu di tengah kesibukan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


# Tambahkan menu lainnya sesuai kebutuhan

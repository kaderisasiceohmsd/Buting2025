import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

# Inline CSS code untuk interface
st.markdown("""
<style>
    /* Reset background colors */
    .stApp {
        background-color: transparent !important;
    }
    
    .main .block-container {
        background-color: transparent !important;
        padding-top: 0 !important;
    }

    /* Cloud Background Animation */
    @keyframes moveClouds {
        0% { transform: translateX(-100px); }
        100% { transform: translateX(calc(100vw + 100px)); }
    }

    @keyframes moveCloudsSlow {
        0% { transform: translateX(-200px); }
        100% { transform: translateX(calc(100vw + 200px)); }
    }

    @keyframes moveCloudsFast {
        0% { transform: translateX(-150px); }
        100% { transform: translateX(calc(100vw + 150px)); }
    }

    .cloud {
        position: fixed;
        background: white;
        border-radius: 1000px;
        opacity: 0.4;
        z-index: -1;
        pointer-events: none;
        filter: blur(2px);
    }

    .cloud::before {
        content: '';
        position: absolute;
        top: -80%;
        left: 10%;
        width: 50%;
        height: 150%;
        background: white;
        border-radius: 50%;
    }

    .cloud::after {
        content: '';
        position: absolute;
        top: -40%;
        right: 20%;
        width: 30%;
        height: 100%;
        background: white;
        border-radius: 50%;
    }

    .cloud1 {
        width: 200px;
        height: 60px;
        top: 15%;
        animation: moveClouds 60s linear infinite;
    }

    .cloud2 {
        width: 300px;
        height: 100px;
        top: 35%;
        animation: moveCloudsSlow 80s linear infinite;
        animation-delay: -20s;
    }

    .cloud3 {
        width: 250px;
        height: 80px;
        top: 55%;
        animation: moveCloudsFast 50s linear infinite;
        animation-delay: -10s;
    }

    .cloud4 {
        width: 180px;
        height: 70px;
        top: 75%;
        animation: moveClouds 70s linear infinite;
        animation-delay: -30s;
    }

    .cloud5 {
        width: 220px;
        height: 65px;
        top: 25%;
        animation: moveCloudsSlow 90s linear infinite;
        animation-delay: -40s;
    }

    /* Main content styling */
    .main-content {
        background-color: rgba(185, 215, 234, 0.95) !important;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, rgba(20, 108, 148, 0.9), rgba(25, 162, 174, 0.9)) !important;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        margin-bottom: 2rem;
    }

    /* Option menu styling */
    .st-emotion-cache-1avcm0n {
        background-color: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
        border-radius: 10px;
        margin: 1rem 0;
    }

    /* Background utama */
    body {
        background: linear-gradient(135deg, #B9D7EA 0%, #a0c8e0 50%, #8bb9d6 100%) !important;
        min-height: 100vh;
    }
    
    /* Image container - FIXED: hilangkan padding atas dan margin */
    .image-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        margin: 0 !important;
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }
    
    /* Fix untuk streamlit image spacing */
    .stImage {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Remove extra spacing around images */
    div[data-testid="stImage"] {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Fix column spacing */
    .stColumn {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Remove extra white space above images */
    .element-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Specific fix for the layout function */
    .layout-image-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 0.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        margin: 0.5rem 0 !important;
    }
</style>

<!-- Cloud Elements -->
<div class="cloud cloud1"></div>
<div class="cloud cloud2"></div>
<div class="cloud cloud3"></div>
<div class="cloud cloud4"></div>
<div class="cloud cloud5"></div>
""", unsafe_allow_html=True)

# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="layout-image-container">', unsafe_allow_html=True)
            st.image(img, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        if i < len(data_list):
            st.markdown(f"""
            <div class="main-content">
                <h3>👤 {data_list[i]['nama']}</h3>
                <p><strong>Sebagai:</strong> {data_list[i]['sebagai']}</p>
                <p><strong>NIM:</strong> {data_list[i]['nim']}</p>
                <p><strong>Fun Fact:</strong> {data_list[i]['fun_fact']}</p>
                <p><strong>Motto Hidup:</strong> <em>"{data_list[i]['motto_hidup']}"</em></p>
            </div>
            """, unsafe_allow_html=True)


# JANGAN DIUBAH

st.markdown(
    """
    <div class="main-header">
        <div style='text-align: center;'>
            <h1 style='font-size: 4.5em; color: white; margin-bottom: 0.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>WEBSITE KATING</h1>
            <p style='font-size: 1.8em; color: white; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);'>CEO HMSD Adyatama ITERA 2024</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("")
    with col2:
        # Gunakan container khusus dengan padding minimal
        st.markdown('<div class="layout-image-container">', unsafe_allow_html=True)
        st.image(load_image(url), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.write("")


# Panggil layout function tanpa extra spacing
layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "rgba(255, 255, 255, 0.9)", "backdrop-filter": "blur(10px)", "border-radius": "10px"},
            "icon": {"color": "#146c94", "font-size": "19px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "color": "#146c94",
                "--hover-color": "#e6f7ff",
            },
            "nav-link-selected": {
                "background-color": "#146c94",
                "color": "white",
                "font-weight": "bold"
            },
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center; color: #146c94; margin-bottom: 1rem;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div class="main-content">
                <div style="text-align: justify; line-height: 1.6;">
                    <h3 style="color: #146c94; text-align: center;">🎓 Kelompok Jordan</h3>
                    <p>Selamat datang di website buku kating kelompok <strong>Jordan</strong>! Kami adalah sekelompok mahasiswa yang bersemangat dari HMSD Adyatama ITERA 2024.</p>
                    <p>Kelompok kami terdiri dari 11 anggota yang berdedikasi untuk saling mendukung dan berkembang bersama. Dengan semangat kolaborasi dan inovasi, kami hadir untuk memberikan yang terbaik dalam setiap proyek yang kami kerjakan.</p>
                    <p><strong>Visi:</strong> Menjadi kelompok yang inspiratif dan berkontribusi positif untuk lingkungan sekitar.</p>
                    <p><strong>Misi:</strong> Belajar bersama, tumbuh bersama, dan mencapai kesuksesan bersama.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1ERUfITTPfR7SWanlCSTD_Q7LVF9EbRwn"
        
        # Layout untuk foto kelompok dengan container khusus
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="layout-image-container">', unsafe_allow_html=True)
            st.image(load_image(foto_kelompok), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown(
            """
            <div class="main-content">
                <div style="text-align: justify;">
                    <h4 style="color: #146c94; text-align: center;">🌟 Tentang Kami</h4>
                    <p>Kelompok Jordan terbentuk dengan dasar persahabatan dan komitmen untuk saling mendukung dalam perjalanan akademik maupun non-akademik. Setiap anggota membawa keunikan dan keahlian masing-masing, menciptakan sinergi yang harmonis dalam tim.</p>
                    <p>Kami percaya bahwa dengan kerja sama dan semangat pantang menyerah, tidak ada hal yang tidak mungkin untuk dicapai. Mari jelajahi lebih lanjut tentang setiap anggota kami di bagian <strong>About Us</strong>!</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center; color: #146c94; margin-bottom: 1rem;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="main-content">
                <h1 class='centered-title'>👥 About Us - Tim Jordan</h1>
                <p style="text-align: center; color: #666;">Meet our amazing team members!</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1aaGJOIdBMcJARcNFSqjJAiDcTAUPLhQK",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1TCAHTolhHAhrdpkk7eWzY5RIVhBvO-gP",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Alfaya Rafif Abiyyi",
                "sebagai": "Pak Lurah",
                "nim": "122450006",
                "fun_fact": "sering jatoh dari motor",
                "motto_hidup": "berjuang sampai titik akhir",
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "sebagai": "Bu Lurah",
                "nim": "122450029",
                "fun_fact": "hobby ngisengin dua princess",
                "motto_hidup": "apa yang sudah dimulai harus diselesaikan",
            },
            {
                "nama": "Kaleb Filbert Istel",
                "sebagai": "Anggota",
                "nim": "124450053",
                "fun_fact": "Username IG nya kelelep_comberan karena pernah kejebur di comberan",
                "motto_hidup": "Semper ad meliora.",
            },
            {
                "nama": "Nabila Nur Azizah",
                "sebagai": "Anggota",
                "nim": "124450048",
                "fun_fact": "makan roti tawar harus di kupas",
                "motto_hidup": "berjalan seperti air",
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "sebagai": "Anggota",
                "nim": "122450085",
                "fun_fact": "Eyangnya Sri Sultan Hamengkubuwana II",
                "motto_hidup": "Tetaplah merasa bodoh supaya terus belajar",
            },
            {
                "nama": "Selma Siti Aisyah",
                "sebagai": "Anggota",
                "nim": "124450044", 
                "fun_fact": "pernah ilang di kebun binatang", 
                "motto_hidup": "Doa dan Usaha adalah Kartu Kemenangan Mereka",
            },
            {
                "nama": "Hani Qurrota Aini",
                "sebagai": "Anggota",
                "nim": "122450020",
                "fun_fact": "suka buah stroberi tapi gasuka kalau stroberi nya diolah atau olahan stroberi",
                "motto_hidup": "breathe, evolve,shine",
            },
            {
                "nama": "Siti Sarifah", 
                "sebagai": "Anggota",
                "nim": "124450015", 
                "fun_fact": "ga suka alpukat", 
                "motto_hidup": "Jangan pernah menyerah",
            },
            {
                "nama": "Cika Adelia Br Marbun", 
                "sebagai": "Anggota",
                "nim": "124450107", 
                "fun_fact": "ga bisa makan pedas",  
                "motto_hidup": " Doakan apa yang kamu kerjakan, kerjakan apa yang kamu doakan",
            },
            {
                "nama": "Gustin H. Tampubolon", 
                "sebagai": "Anggota",
                "nim": "124450068",
                "fun_fact": "susah ingat nama orang, tapi hafal mukanya",
                "motto_hidup": "apapun yang kamu perbuat, perbuatlah dengan segenap hatimu",
            },
            {
                "nama": "Danil Nur Fadillah",
                "sebagai": "Anggota",
                "nim": "124450103",
                "fun_fact": "punya panggilan khusus di kelompok, nama panggilan nya Duta Gorengan",
                "motto_hidup": "dimana langit dipinjak, disitu langit dijunjung",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
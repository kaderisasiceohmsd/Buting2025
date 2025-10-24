import streamlit as st
import random
import time

def playlist_mood_poisson():
    st.markdown("<h2 style='text-align:center;'>🎧 Playlist Mood Poisson 🎶</h2>", unsafe_allow_html=True)
    st.write("Pilih suasana hatimu hari ini, biar Poisson kasih playlist yang cocok buat kamu~ 😎")

    # Pilihan mood
    mood = st.selectbox(
        "🌈 Pilih mood kamu:",
        ["😎 Santai", "😭 Lelah Kuliah", "💪 Semangat", "💤 Gabut", "💘 Baper", " 💔Galau Berat"]
    )

    # Tombol aksi
    if st.button("✨ Tampilkan Playlist ✨"):
        with st.spinner("🎲 Poisson lagi milihin lagu terbaik buat kamu..."):
            time.sleep(2)  # efek loading

        # Efek lucu saat hasil muncul
        st.balloons()

        # Data mood
        playlist_data = {
            "😎 Santai": {
                "pesan": "☀️ Chill aja, Poisson ngerti kamu butuh rebahan yang bermartabat 😎",
                "link": "[☕ Coffee & Lo-Fi Beats](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6)",
                "gif": "https://i.pinimg.com/originals/59/5e/79/595e79f0e5b9d4d62cf08413ad27b585.gif",
            },
            "😭 Lelah Kuliah": {
                "pesan": "📚 Istirahat dulu, tugas nggak akan kabur kok 😭",
                "link": "[😢 Lofi Sad Beats](https://open.spotify.com/playlist/37i9dQZF1DWSqBruwoIXkA)",
                "gif": "https://i.pinimg.com/originals/3d/5f/34/3d5f34a28226dd166b50e1b463d1c5d7.gif",
            },
            "💪 Semangat": {
                "pesan": "🔥 Gas terus! Deadline boleh banyak, tapi kamu lebih tangguh 💪",
                "link": "[💪 Motivation Boost](https://open.spotify.com/playlist/37i9dQZF1DX70RN3TfWWJh)",
                "gif": "https://i.pinimg.com/originals/fc/7b/08/fc7b08f891b5ac1b6d9a4fddcfcf3b75.gif",
            },
            "💤 Gabut": {
                "pesan": "😴 Gabut? Dengerin lagu biar bengongmu punya irama~",
                "link": "[🌙 Late Night Vibes](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6)",
                "gif": "https://i.pinimg.com/originals/83/a5/55/83a55504f796dd10a264e308f4c9d78b.gif",
            },
            "💘 Baper": {
                "pesan": "💔 Waduh... lagi mellow ya? Tenang, Poisson siap nemenin kamu 😢",
                "link": "[💘 Sad & Love Songs](https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1)",
                "gif": "https://i.pinimg.com/originals/7e/3d/d8/7e3dd82629a0998a027a79abac51e5b7.gif",
            },
            "💔Galau Berat": {
                "pesan": random.choice([
                "🌧️ Kadang bukan lagunya yang sedih, tapi kenangannya yang datang bareng intro musiknya 😢",
                "💔 Poisson ngerti... rasanya nahan air mata sambil pura-pura bilang ‘aku gapapa’.",
                "☕ Coba istirahat bentar. Kadang hati juga butuh jeda dari mikirin yang udah lewat.",
                "💫 Kamu nggak sendiri kok, bahkan Poisson juga pernah ditinggal (sama server Streamlit).",
                "🎶 Dengerin aja dulu, mungkin lagu ini bisa pelan-pelan ngobrol sama hatimu.",
                ]),
                "link": random.choice([
                    "[🎡 Indie Pop Mix](https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0)",
                    "[🌻 Feel Good Vibes](https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC)",
                    "[🍀 Chill Hits](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6)",
                ]),
                "gif": random.choice([
                    "https://i.pinimg.com/originals/1c/61/b1/1c61b1d5f0d4d1a3e3cbadfa8f71f0a7.gif",
                    "https://i.pinimg.com/originals/85/bf/33/85bf33d7cbf3858e1a93e7e2d118b32e.gif",
                    "https://i.pinimg.com/originals/9a/4d/89/9a4d89b72796d4e3b9ad1b4b70c99e67.gif"
                ]),
            }
        }

        data = playlist_data[mood]
        st.markdown(f"### {data['pesan']}")
        st.image(data["gif"], caption="🎶 Playlist by Poisson")
        st.markdown(f"**Klik di sini untuk dengar:** {data['link']}")
        
        # Pesan tambahan lucu
        st.toast(random.choice([
            "🎧 Poisson bilang: nikmati dulu musiknya, baru nugasnya~",
            "☕ Jangan lupa sambil ngopi, biar makin chill",
            "💫 Kadang musik lebih ngerti daripada dosen pembimbing 😌",
            "🌻 Semoga harimu secerah warna kuning Poisson~"
        ]))

# Jalankan fungsi
playlist_mood_poisson()

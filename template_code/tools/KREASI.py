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
                "link": "[☕ Coffee & Lo-Fi Beats](https://open.spotify.com/playlist/4hCUxSvL8L4b1JxvBhPuc4?si=253e46a494684918&pt=184e99381e4ab65249f9d6d56fb58f46)",
                "gif": "https://i.pinimg.com/originals/59/5e/79/595e79f0e5b9d4d62cf08413ad27b585.gif",
            },
            "😭 Lelah Kuliah": {
                "pesan": "📚 Istirahat dulu, tugas nggak akan kabur kok 😭",
                "link": "[😢 Lofi Sad Beats](https://open.spotify.com/playlist/3LorW9TD1kt0CNckq5UOJE?si=7f6287cebab04669&pt=a5d1bb93ac35487c11b976acdd668265)",
                "gif": "https://i.pinimg.com/originals/3d/5f/34/3d5f34a28226dd166b50e1b463d1c5d7.gif",
            },
            "💪 Semangat": {
                "pesan": "🔥 Gas terus! Deadline boleh banyak, tapi kamu lebih tangguh 💪",
                "link": "[💪 Motivation Boost](https://open.spotify.com/playlist/21NxkXhf6XP92GB44InWVg?si=9dc57eb2c59e4f95&pt=844b724122c4d502d3234a4c70d0394b)",
                "gif": "https://i.pinimg.com/originals/fc/7b/08/fc7b08f891b5ac1b6d9a4fddcfcf3b75.gif",
            },
            "💤 Gabut": {
                "pesan": "😴 Gabut? Dengerin lagu biar bengongmu punya irama~",
                "link": "[🌙 Late Night Vibes](https://open.spotify.com/playlist/4bznMJVf1AzP4G9KSPMTTF?si=ec0e843431ab4372&pt=f92f2a5cd473ea73a384eef0bcf297e5)",
                "gif": "https://i.pinimg.com/originals/83/a5/55/83a55504f796dd10a264e308f4c9d78b.gif",
            },
            "💘 Baper": {
                "pesan": "💔 Waduh... lagi mellow ya? Tenang, Poisson siap nemenin kamu 😢",
                "link": "[💘 Sad & Love Songs](https://open.spotify.com/playlist/4rvH1Dr19KyEk0LQ3fUSiT?si=dea23598cded47e8&pt=e74d40855eca1aa3a67dcba1b32dac3b)",
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
                    "[🎡 Indie Pop Mix](https://open.spotify.com/playlist/1zqoW3QYbVIxGRetCDp0lI?si=033e977222ab4576&pt=a96c0f1d1bde355051cf8f100e438c7d)",
                    "[🌻 Feel Good Vibes](https://open.spotify.com/playlist/1b1izbsaN6vWb1F0dD5zrU?si=0ace0f7435454b76&pt=54702f4c1fcfb8f9fb78a4b43e38127c)",
                    "[🍀 Chill Hits](https://open.spotify.com/playlist/0qecs1tv1ugkOrqApVjevN?si=8a440ee10b024d18&pt=cb0c360aa0fc06e12e468cd917c2abfe)",
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


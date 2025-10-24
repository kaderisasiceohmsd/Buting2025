import streamlit as st
import random

st.set_page_config(page_title="AI Lyric & Mood Music Generator", page_icon="🎶")

st.title("🎵 AI Lyric & Mood Music Generator")
st.write("Masukkan kata kunci — dan biarkan AI membuat lirik lagu sesuai suasana hatimu!")

keyword = st.text_input("Kata kunci atau tema lirik (contoh: cinta, rindu, hujan, bahagia)")

themes = {
    "cinta": {
        "lyrics": [
            "Cinta ini seperti laut — luas, tapi kadang menenggelamkan.",
            "Kau hadir di antara nada yang tak selesai kutulis.",
            "Ada rindu yang bernyanyi di antara setiap detak hatiku."
        ],
        "music": "music/love.mp3"
    },
    "rindu": {
        "lyrics": [
            "Rindu ini berjalan tanpa arah, tapi selalu menuju namamu.",
            "Aku bicara pada malam — tentang kamu yang tak pulang.",
            "Jika rindu punya suara, mungkin ia akan memanggil namamu terus."
        ],
        "music": "music/sad.mp3"
    },
    "bahagia": {
        "lyrics": [
            "Langit hari ini seperti senyum yang kamu titipkan kemarin.",
            "Kebahagiaan itu sederhana — ketika aku bisa melihatmu tertawa.",
            "Setiap detik bersamamu adalah melodi bahagia yang tak ingin berhenti."
        ],
        "music": "music/happy.mp3"
    },
    "hujan": {
        "lyrics": [
            "Hujan sore ini membawa aroma kenangan yang belum selesai.",
            "Payung tak cukup menahan derasnya kenangan tentangmu.",
            "Tetes hujan seperti nada — jatuh lembut tapi menggema lama."
        ],
        "music": "music/rain.mp3"
    }
}

if st.button("🎶 Buat Lirik!"):
    if keyword == "":
        st.warning("Masukkan dulu kata kunci ya!")
    else:
        if keyword.lower() in themes:
            theme_data = themes[keyword.lower()]
            lyric = random.choice(theme_data["lyrics"])
            music_path = theme_data["music"]

            st.subheader("✨ Lirikmu:")
            st.markdown(f"**{lyric}**")
            
            st.audio(music_path, format="audio/mp3")
        else:
            all_lyrics = [l for t in themes.values() for l in t["lyrics"]]
            lyric = random.choice(all_lyrics)
            st.subheader("✨ Lirikmu:")
            st.markdown(f"**{lyric}**")
            st.info("🔊 Musik tidak tersedia untuk tema ini.")

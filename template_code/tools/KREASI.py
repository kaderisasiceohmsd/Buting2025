
import streamlit as st

st.title("🎨 Tes Warna Kepribadian")
st.write("Pilih warna yang paling kamu suka, nanti aku tebak kepribadianmu 😎")

warna = st.selectbox(
    "Pilih warna favoritmu:",
    ["Merah", "Biru", "Hijau", "Kuning", "Hitam", "Ungu", "Putih"]
)

kepribadian = {
    "Merah": "Berani, penuh semangat, tapi kadang keras kepala ❤️",
    "Biru": "Tenang, bijak, tapi suka overthinking 💙",
    "Hijau": "Penyayang, stabil, dan cinta damai 💚",
    "Kuning": "Optimis dan ceria, tapi mudah bosan 💛",
    "Hitam": "Kuat dan misterius, tapi hati lembut 🖤",
    "Ungu": "Kreatif, intuitif, dan sedikit dramatis 💜",
    "Putih": "Sederhana, tulus, dan jujur 🤍"
}

if warna:
    st.subheader("💬 Hasil Tebakan:")
    st.success(kepribadian[warna])

if st.button("Ganti warna 🎲"):
    st.balloons()

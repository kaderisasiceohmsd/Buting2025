import streamlit as st
import pandas as pd

st.set_page_config(page_title="Penjadwalan Aktivitas Greedy", layout="centered")

st.title("📅 Penjadwalan Aktivitas Optimal (Algoritma Greedy)")
st.write("Masukkan daftar aktivitas dengan waktu mulai dan selesai, lalu klik tombol **Jadwalkan Aktivitas** untuk melihat hasil terbaik tanpa bentrok waktu.")

# Input data aktivitas
st.subheader("Masukkan Data Aktivitas")
data = st.text_area("Format: Nama, Mulai, Selesai (pisahkan dengan koma, 1 aktivitas per baris)",
"""
A, 1, 3
B, 2, 5
C, 4, 6
D, 6, 7
E, 5, 9
F, 8, 9
""")

if st.button("Jadwalkan Aktivitas"):
    try:
        # Ubah input ke DataFrame
        lines = [x.strip() for x in data.strip().split("\n") if x.strip()]
        activities = []
        for line in lines:
            name, start, finish = line.split(",")
            activities.append([name.strip(), int(start.strip()), int(finish.strip())])
        df = pd.DataFrame(activities, columns=["Aktivitas", "Mulai", "Selesai"])

        # Urutkan berdasarkan waktu selesai
        df = df.sort_values(by="Selesai").reset_index(drop=True)

        # Algoritma Greedy
        selected = []
        last_finish = -1
        for _, row in df.iterrows():
            if row["Mulai"] >= last_finish:
                selected.append(row)
                last_finish = row["Selesai"]

        selected_df = pd.DataFrame(selected)

        st.success("✅ Aktivitas terpilih tanpa bentrok waktu:")
        st.dataframe(selected_df)

        # Visualisasi sederhana
        st.subheader("Visualisasi Jadwal")
        import plotly.express as px
        fig = px.timeline(selected_df, x_start="Mulai", x_end="Selesai", y="Aktivitas", color="Aktivitas",
                          title="Aktivitas Terpilih", text="Aktivitas")
        fig.update_yaxes(autorange="reversed")  # supaya urutan dari atas ke bawah
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Terjadi kesalahan dalam input data: {e}")

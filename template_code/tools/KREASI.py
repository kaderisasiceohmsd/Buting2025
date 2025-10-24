import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

st.set_page_config(page_title="Penjadwalan Aktivitas Greedy (Jam)", layout="centered")

st.title("⏰ Penjadwalan Aktivitas Optimal (Algoritma Greedy dengan Jam)")
st.write(
    "Masukkan aktivitas harianmu dengan waktu mulai dan selesai (format **HH:MM**, 24 jam). "
    "Aplikasi ini akan memilih aktivitas paling optimal **tanpa bentrok waktu** menggunakan algoritma greedy."
)

# Contoh input
st.subheader("Masukkan Data Aktivitas")
data = st.text_area(
    "Format: Nama, Mulai, Selesai (pisahkan dengan koma, 1 aktivitas per baris)",
    """
Belajar, 08:00, 10:00
Main HP, 09:00, 11:00
Tidur Siang, 11:30, 13:00
Nonton, 12:00, 14:00
Makan, 14:30, 15:00
Olahraga, 16:00, 17:30
    """,
    height=180
)

if st.button("🧠 Jadwalkan Aktivitas"):
    try:
        # Parsing data input
        lines = [x.strip() for x in data.strip().split("\n") if x.strip()]
        activities = []
        for line in lines:
            name, start, finish = line.split(",")
            start_time = datetime.strptime(start.strip(), "%H:%M")
            end_time = datetime.strptime(finish.strip(), "%H:%M")
            activities.append([name.strip(), start_time, end_time])

        df = pd.DataFrame(activities, columns=["Aktivitas", "Mulai", "Selesai"])

        # Urutkan berdasarkan waktu selesai
        df = df.sort_values(by="Selesai").reset_index(drop=True)

        # Algoritma Greedy
        selected = []
        last_finish = datetime.strptime("00:00", "%H:%M")
        for _, row in df.iterrows():
            if row["Mulai"] >= last_finish:
                selected.append(row)
                last_finish = row["Selesai"]

        selected_df = pd.DataFrame(selected)

        st.success("✅ Aktivitas terpilih tanpa bentrok waktu:")
        selected_df["Mulai"] = selected_df["Mulai"].dt.strftime("%H:%M")
        selected_df["Selesai"] = selected_df["Selesai"].dt.strftime("%H:%M")
        st.dataframe(selected_df, hide_index=True, use_container_width=True)

        # Visualisasi Timeline
        st.subheader("🕗 Visualisasi Jadwal (Timeline)")
        timeline_df = pd.DataFrame(selected)
        fig = px.timeline(
            timeline_df,
            x_start="Mulai",
            x_end="Selesai",
            y="Aktivitas",
            color="Aktivitas",
            title="Jadwal Aktivitas Optimal",
            text="Aktivitas",
        )
        fig.update_yaxes(autorange="reversed")
        fig.update_layout(xaxis_title="Waktu", yaxis_title="Aktivitas")
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"⚠️ Terjadi kesalahan dalam input data: {e}")

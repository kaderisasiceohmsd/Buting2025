import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Prediksi Pemenang Berdasarkan Stats Historis ⚽", layout="centered")

st.title("⚽ Prediksi Pemenang: Tim A vs Tim B (Berdasarkan Stats Historis musim)")
st.write("Masukkan nama dan statistik historis dua tim, lalu lihat prediksi siapa yang lebih mungkin menang berdasarkan data historis")
st.write("untuk stats boleh di cek di fcstats.com ya!")
# --- Input Data Tim ---

st.subheader("📋 Input Data Tim")
col1, col2 = st.columns(2)

with col1:
    team_a_name = st.text_input("Nama Tim A", value="Barcelona", max_chars=20)
    
    st.write("**Stats Historis Tim A**")
    team_a_wins = st.number_input("Jumlah Kemenangan Historis", min_value=0, value=10, step=1)
    team_a_draws = st.number_input("Jumlah Seri Historis", min_value=0, value=5, step=1)
    team_a_losses = st.number_input("Jumlah Kekalahan Historis", min_value=0, value=5, step=1)
    team_a_goals_for = st.number_input("Gol Dicetak Historis", min_value=0, value=50, step=1)
    team_a_goals_against = st.number_input("Gol Kemasukan Historis", min_value=0, value=30, step=1)

with col2:
    team_b_name = st.text_input("Nama Tim B", value="Real Madrid", max_chars=20)
    
    st.write("**Stats Historis Tim B**")
    team_b_wins = st.number_input("Jumlah Kemenangan Historis", min_value=0, value=8, step=1)
    team_b_draws = st.number_input("Jumlah Seri Historis", min_value=0, value=6, step=1)
    team_b_losses = st.number_input("Jumlah Kekalahan Historis", min_value=0, value=6, step=1)
    team_b_goals_for = st.number_input("Gol Dicetak Historis", min_value=0, value=45, step=1)
    team_b_goals_against = st.number_input("Gol Kemasukan Historis", min_value=0, value=35, step=1)

st.write("---")

# --- Prediksi Pemenang ---

if st.button("Prediksi Pemenang ⚡"):
    # Hitung stats historis
    total_matches_a = team_a_wins + team_a_draws + team_a_losses
    total_matches_b = team_b_wins + team_b_draws + team_b_losses
    
    win_rate_a = (team_a_wins / total_matches_a * 100) if total_matches_a > 0 else 0
    win_rate_b = (team_b_wins / total_matches_b * 100) if total_matches_b > 0 else 0
    
    goal_diff_a = team_a_goals_for - team_a_goals_against
    goal_diff_b = team_b_goals_for - team_b_goals_against
    
    # Logika prediksi: Hanya berdasarkan stats historis
    # Bobot: 50% win rate, 30% goal difference, 20% total matches (untuk stabilitas)
    win_rate_score_a = win_rate_a
    win_rate_score_b = win_rate_b
    
    goal_diff_score_a = max(0, goal_diff_a + 50)  # Normalisasi agar positif
    goal_diff_score_b = max(0, goal_diff_b + 50)
    
    matches_score_a = total_matches_a  # Lebih banyak pertandingan = lebih stabil
    matches_score_b = total_matches_b
    
    total_score_a = (0.5 * win_rate_score_a) + (0.3 * goal_diff_score_a) + (0.2 * matches_score_a)
    total_score_b = (0.5 * win_rate_score_b) + (0.3 * goal_diff_score_b) + (0.2 * matches_score_b)
    
    total_combined = total_score_a + total_score_b
    if total_combined == 0:
        prob_a_win = 50.0
        prob_b_win = 50.0
        prob_draw = 0.0
    else:
        prob_a_win = (total_score_a / total_combined) * 100
        prob_b_win = (total_score_b / total_combined) * 100
        prob_draw = 10.0  # Probabilitas seri tetap
    
    # Sesuaikan probabilitas agar total 100%
    total_prob = prob_a_win + prob_b_win + prob_draw
    prob_a_win = (prob_a_win / total_prob) * 100
    prob_b_win = (prob_b_win / total_prob) * 100
    prob_draw = (prob_draw / total_prob) * 100
    
    # Tentukan pemenang berdasarkan probabilitas tertinggi
    if prob_a_win > prob_b_win and prob_a_win > prob_draw:
        predicted_winner = team_a_name
        winner_text = f"🏆 Prediksi: {team_a_name} lebih mungkin menang!"
        winner_color = "success"
    elif prob_b_win > prob_a_win and prob_b_win > prob_draw:
        predicted_winner = team_b_name
        winner_text = f"🏆 Prediksi: {team_b_name} lebih mungkin menang!"
        winner_color = "success"
    else:
        predicted_winner = "Seri"
        winner_text = "🤝 Prediksi: Pertandingan kemungkinan seri!"
        winner_color = "warning"
    
    # Tampilkan hasil
    st.subheader("📊 Hasil Prediksi")
    st.metric(label="Probabilitas Menang", value=f"{team_a_name}: {prob_a_win:.1f}% | {team_b_name}: {prob_b_win:.1f}% | Seri: {prob_draw:.1f}%")
    
    if winner_color == "success":
        st.success(winner_text)
    else:
        st.warning(winner_text)
    
    # Tampilkan stats historis
    st.write("### 📈 Ringkasan Stats Historis")
    historical_stats = pd.DataFrame({
        "Tim": [team_a_name, team_b_name],
        "Total Pertandingan": [total_matches_a, total_matches_b],
        "Kemenangan": [team_a_wins, team_b_wins],
        "Seri": [team_a_draws, team_b_draws],
        "Kekalahan": [team_a_losses, team_b_losses],
        "Win Rate (%)": [win_rate_a, win_rate_b],
        "Gol Dicetak": [team_a_goals_for, team_b_goals_for],
        "Gol Kemasukan": [team_a_goals_against, team_b_goals_against],
        "Selisih Gol": [goal_diff_a, goal_diff_b]
    })
    st.table(historical_stats)
    
    # Visualisasi sederhana
    st.write("### 📊 Visualisasi Win Rate dan Selisih Gol")
    chart_data = pd.DataFrame({
        "Win Rate (%)": [win_rate_a, win_rate_b],
        "Selisih Gol": [goal_diff_a, goal_diff_b]
    }, index=[team_a_name, team_b_name])
    st.bar_chart(chart_data)

st.markdown("<hr><center><p style='font-size:12px;'>© 2025 Kelompok Greedy | Mini Project Prediksi Berdasarkan Stats Historis</p></center>", unsafe_allow_html=True)

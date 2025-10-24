import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime, timedelta
import math

# CSS untuk background awan dan styling
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
        opacity: 0.3;
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

    /* Background utama */
    body {
        background: linear-gradient(135deg, #B9D7EA 0%, #a0c8e0 50%, #8bb9d6 100%) !important;
        min-height: 100vh;
    }

    /* Animated Title */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .animated-title {
        font-size: 2.8em;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(270deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3);
        background-size: 1200% 1200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 30s ease infinite;
        margin-bottom: 0.3em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        font-size: 1.3em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2em;
        background: linear-gradient(135deg, #146c94, #19a2ae);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* Content Cards */
    .content-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
    }

    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #146c94, #19a2ae);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
</style>

<!-- Cloud Elements -->
<div class="cloud cloud1"></div>
<div class="cloud cloud2"></div>
<div class="cloud cloud3"></div>
<div class="cloud cloud4"></div>
<div class="cloud cloud5"></div>
""", unsafe_allow_html=True)

def create_animated_title():
    """Membuat judul dengan efek warna bergerak"""
    st.markdown('<div class="animated-title">📊 Data Visualization Lab</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Visualisasi Data Interaktif dengan Altair</div>', unsafe_allow_html=True)

def generate_sample_data(option):
    """Generate sample dataset berdasarkan pilihan"""
    np.random.seed(42)
    
    if option == "E-Commerce Data":
        dates = pd.date_range('2024-01-01', periods=180, freq='D')
        revenue = np.random.normal(5000, 1500, 180) + np.sin(np.arange(180) * 0.1) * 1000
        orders = np.random.poisson(50, 180) + (np.sin(np.arange(180) * 0.05) * 20).astype(int)
        
        df = pd.DataFrame({
            'date': dates,
            'revenue': np.abs(revenue),
            'orders': orders,
            'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home'], 180),
            'region': np.random.choice(['North', 'South', 'East', 'West'], 180),
            'customer_rating': np.random.uniform(3.5, 5.0, 180)
        })
        return df
    
    elif option == "Student Performance":
        math_scores = np.random.normal(70, 12, 200)
        science_scores = math_scores * 0.8 + np.random.normal(20, 8, 200)
        english_scores = np.random.normal(65, 10, 200)
        
        df = pd.DataFrame({
            'student_id': range(1, 201),
            'math_score': np.clip(math_scores, 0, 100),
            'science_score': np.clip(science_scores, 0, 100),
            'english_score': np.clip(english_scores, 0, 100),
            'attendance': np.random.uniform(75, 100, 200),
            'extracurricular': np.random.choice(['Sports', 'Arts', 'Music', 'None'], 200),
            'parent_education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 200)
        })
        return df
    
    elif option == "Health & Fitness":
        age = np.random.randint(18, 65, 150)
        weight = np.random.normal(70, 15, 150)
        height = np.random.normal(170, 10, 150)
        bmi = weight / ((height / 100) ** 2)
        
        df = pd.DataFrame({
            'age': age,
            'weight_kg': weight,
            'height_cm': height,
            'bmi': bmi,
            'blood_pressure_sys': np.random.randint(110, 140, 150),
            'blood_pressure_dia': np.random.randint(70, 90, 150),
            'activity_level': np.random.choice(['Sedentary', 'Light', 'Moderate', 'Active'], 150),
            'smoker': np.random.choice(['Yes', 'No'], 150, p=[0.2, 0.8])
        })
        return df

def create_correlation_heatmap(df):
    """Buat heatmap korelasi dengan Altair"""
    numeric_df = df.select_dtypes(include=[np.number])
    if len(numeric_df.columns) < 2:
        return None
    
    corr_matrix = numeric_df.corr().reset_index().melt(id_vars='index')
    corr_matrix.columns = ['var1', 'var2', 'correlation']
    
    heatmap = alt.Chart(corr_matrix).mark_rect().encode(
        x='var2:O',
        y='var1:O',
        color=alt.Color('correlation:Q', scale=alt.Scale(scheme='redblue', domain=[-1, 1])),
        tooltip=['var1', 'var2', 'correlation']
    ).properties(
        width=400,
        height=400,
        title='Correlation Heatmap'
    )
    
    return heatmap

def create_scatter_plot(df, x_col, y_col, color_col=None):
    """Buat scatter plot interaktif"""
    if color_col:
        chart = alt.Chart(df).mark_circle(size=60).encode(
            x=alt.X(x_col, title=x_col),
            y=alt.Y(y_col, title=y_col),
            color=alt.Color(color_col, legend=alt.Legend(title=color_col)),
            tooltip=[x_col, y_col, color_col]
        )
    else:
        chart = alt.Chart(df).mark_circle(size=60).encode(
            x=alt.X(x_col, title=x_col),
            y=alt.Y(y_col, title=y_col),
            tooltip=[x_col, y_col]
        )
    
    return chart.properties(
        width=600,
        height=400,
        title=f'{y_col} vs {x_col}'
    ).interactive()

def create_time_series(df, date_col, value_col):
    """Buat time series chart"""
    chart = alt.Chart(df).mark_line().encode(
        x=alt.X(f'{date_col}:T', title='Date'),
        y=alt.Y(f'{value_col}:Q', title=value_col),
        tooltip=[date_col, value_col]
    ).properties(
        width=700,
        height=400,
        title=f'{value_col} Over Time'
    ).interactive()
    
    return chart

def create_bar_chart(df, x_col, y_col):
    """Buat bar chart"""
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(x_col, title=x_col),
        y=alt.Y(y_col, title=y_col),
        color=alt.Color(x_col, legend=None),
        tooltip=[x_col, y_col]
    ).properties(
        width=600,
        height=400,
        title=f'{y_col} by {x_col}'
    )
    
    return chart

def create_histogram(df, column, bins=30):
    """Buat histogram"""
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(f'{column}:Q', bin=alt.Bin(maxbins=bins), title=column),
        y=alt.Y('count()', title='Frequency'),
        tooltip=[alt.Tooltip(f'{column}:Q', bin=True), 'count()']
    ).properties(
        width=600,
        height=400,
        title=f'Distribution of {column}'
    )
    
    return chart

def create_box_plot(df, column, group_col=None):
    """Buat box plot"""
    if group_col:
        chart = alt.Chart(df).mark_boxplot().encode(
            x=alt.X(f'{group_col}:N', title=group_col),
            y=alt.Y(f'{column}:Q', title=column),
            color=alt.Color(f'{group_col}:N', legend=None)
        )
    else:
        chart = alt.Chart(df).mark_boxplot().encode(
            y=alt.Y(f'{column}:Q', title=column)
        )
    
    return chart.properties(
        width=600,
        height=400,
        title=f'Box Plot of {column}'
    )

def main():
    # Judul dengan animasi
    create_animated_title()
    
    st.sidebar.header("⚙️ Dataset Configuration")
    
    # Pilihan dataset
    dataset_option = st.sidebar.selectbox(
        "Choose Dataset:",
        ["E-Commerce Data", "Student Performance", "Health & Fitness"]
    )
    
    # Generate data
    df = generate_sample_data(dataset_option)
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.header("📈 Data Overview")
    
    # Tampilkan dataset
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Data Preview")
        st.dataframe(df.head(8), use_container_width=True)
    
    with col2:
        st.subheader("Dataset Info")
        st.metric("Total Records", len(df))
        st.metric("Total Columns", len(df.columns))
        st.metric("Numeric Columns", len(df.select_dtypes(include=[np.number]).columns))
        st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Statistical Summary
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.header("📊 Statistical Summary")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        st.dataframe(df[numeric_cols].describe(), use_container_width=True)
    else:
        st.info("No numeric columns for statistical analysis")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Correlation Analysis
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.header("🔗 Correlation Analysis")
    
    heatmap = create_correlation_heatmap(df)
    if heatmap:
        st.altair_chart(heatmap, use_container_width=True)
        
        # Highlight strong correlations
        numeric_df = df.select_dtypes(include=[np.number])
        corr_matrix = numeric_df.corr()
        strong_corrs = []
        
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                corr_val = corr_matrix.iloc[i, j]
                if abs(corr_val) > 0.6:
                    strong_corrs.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_val))
        
        if strong_corrs:
            st.subheader("Strong Correlations (|r| > 0.6)")
            for col1, col2, corr in strong_corrs:
                st.write(f"**{col1}** ↔ **{col2}**: {corr:.3f}")
    else:
        st.info("Need at least 2 numeric columns for correlation analysis")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Visualizations
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.header("🎨 Interactive Visualizations")
    
    viz_type = st.selectbox(
        "Choose Visualization Type:",
        ["Scatter Plot", "Time Series", "Bar Chart", "Histogram", "Box Plot"]
    )
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    date_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    
    if viz_type == "Scatter Plot" and len(numeric_cols) >= 2:
        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("X-Axis", numeric_cols, index=0)
        with col2:
            y_axis = st.selectbox("Y-Axis", numeric_cols, index=min(1, len(numeric_cols)-1))
        
        color_by = st.selectbox("Color By (Optional)", [None] + categorical_cols)
        
        scatter_chart = create_scatter_plot(df, x_axis, y_axis, color_by)
        st.altair_chart(scatter_chart, use_container_width=True)
    
    elif viz_type == "Time Series" and date_cols:
        date_col = st.selectbox("Date Column", date_cols)
        value_col = st.selectbox("Value Column", numeric_cols)
        
        time_chart = create_time_series(df, date_col, value_col)
        st.altair_chart(time_chart, use_container_width=True)
    
    elif viz_type == "Bar Chart":
        col1, col2 = st.columns(2)
        with col1:
            category_col = st.selectbox("Category Column", categorical_cols + numeric_cols[:1])
        with col2:
            value_col = st.selectbox("Value Column", numeric_cols)
        
        # Aggregate data for bar chart
        if category_col in numeric_cols:
            # Bin numeric data for grouping
            bar_data = df.groupby(pd.cut(df[category_col], bins=10))[value_col].mean().reset_index()
            bar_data[category_col] = bar_data[category_col].astype(str)
        else:
            bar_data = df.groupby(category_col)[value_col].mean().reset_index()
        
        bar_chart = create_bar_chart(bar_data, category_col, value_col)
        st.altair_chart(bar_chart, use_container_width=True)
    
    elif viz_type == "Histogram" and numeric_cols:
        hist_col = st.selectbox("Select Column", numeric_cols)
        bins = st.slider("Number of Bins", 5, 50, 20)
        
        hist_chart = create_histogram(df, hist_col, bins)
        st.altair_chart(hist_chart, use_container_width=True)
    
    elif viz_type == "Box Plot" and numeric_cols:
        box_col = st.selectbox("Numeric Column", numeric_cols)
        group_col = st.selectbox("Group By (Optional)", [None] + categorical_cols)
        
        box_chart = create_box_plot(df, box_col, group_col)
        st.altair_chart(box_chart, use_container_width=True)
    
    else:
        st.info(f"Not enough data for {viz_type} visualization")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Advanced Analysis
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.header("🔬 Advanced Analysis")
    
    analysis_type = st.selectbox(
        "Choose Analysis:",
        ["Data Distribution", "Outlier Detection", "Trend Analysis"]
    )
    
    if analysis_type == "Data Distribution" and numeric_cols:
        selected_cols = st.multiselect("Select columns to compare:", numeric_cols, default=numeric_cols[:2])
        
        if len(selected_cols) >= 2:
            # Create distribution comparison
            melted_df = df[selected_cols].melt(var_name='variable', value_name='value')
            
            chart = alt.Chart(melted_df).mark_bar(opacity=0.7).encode(
                x=alt.X('value:Q', bin=alt.Bin(maxbins=30)),
                y=alt.Y('count()', stack=None),
                color='variable:N'
            ).properties(
                width=600,
                height=400,
                title='Distribution Comparison'
            ).facet(
                column='variable:N'
            )
            
            st.altair_chart(chart, use_container_width=True)
    
    elif analysis_type == "Outlier Detection" and numeric_cols:
        outlier_col = st.selectbox("Select column for outlier detection:", numeric_cols)
        
        Q1 = df[outlier_col].quantile(0.25)
        Q3 = df[outlier_col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[outlier_col] < lower_bound) | (df[outlier_col] > upper_bound)]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Outliers Found", len(outliers))
        with col2:
            st.metric("Outlier Percentage", f"{(len(outliers)/len(df))*100:.1f}%")
        with col3:
            st.metric("IQR Range", f"[{lower_bound:.1f}, {upper_bound:.1f}]")
        
        if len(outliers) > 0:
            # Create visualization showing outliers
            base = alt.Chart(df).mark_circle(opacity=0.6).encode(
                x=alt.X('index:Q', title='Data Point'),
                y=alt.Y(f'{outlier_col}:Q', title=outlier_col),
                color=alt.condition(
                    alt.datum[outlier_col] < lower_bound | alt.datum[outlier_col] > upper_bound,
                    alt.value('red'),
                    alt.value('blue')
                ),
                tooltip=[outlier_col]
            )
            
            st.altair_chart(base.properties(width=700, height=400), use_container_width=True)
    
    elif analysis_type == "Trend Analysis" and date_cols and numeric_cols:
        trend_date_col = st.selectbox("Date Column", date_cols)
        trend_value_col = st.selectbox("Value Column", numeric_cols)
        
        # Add rolling average
        df_sorted = df.sort_values(trend_date_col)
        df_sorted['rolling_avg'] = df_sorted[trend_value_col].rolling(window=7).mean()
        
        line = alt.Chart(df_sorted).mark_line(color='blue').encode(
            x=f'{trend_date_col}:T',
            y=f'{trend_value_col}:Q'
        )
        
        rolling_line = alt.Chart(df_sorted).mark_line(color='red', strokeDash=[5,5]).encode(
            x=f'{trend_date_col}:T',
            y='rolling_avg:Q'
        )
        
        trend_chart = (line + rolling_line).properties(
            width=700,
            height=400,
            title=f'{trend_value_col} Trend with 7-day Moving Average'
        ).interactive()
        
        st.altair_chart(trend_chart, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Data Export
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.header("💾 Export & Share")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"{dataset_option.replace(' ', '_').lower()}.csv",
            mime="text/csv"
        )
    
    with col2:
        # Summary statistics
        summary = df.describe().to_string()
        st.download_button(
            label="📊 Download Summary",
            data=summary,
            file_name=f"{dataset_option.replace(' ', '_').lower()}_summary.txt",
            mime="text/plain"
        )
    
    with col3:
        st.info("✨ All visualizations are interactive! Hover for details.")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
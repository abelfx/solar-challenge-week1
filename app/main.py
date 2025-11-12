import streamlit as st
from utils import load_data, get_summary_stats, plot_boxplots, plot_avg_bar, generate_heatmap

st.set_page_config(
    page_title="Solar Data Comparison Dashboard",
    layout="wide",
    page_icon="🌞"
)

st.title("Cross-Country Solar Energy Comparison Dashboard")
st.markdown("""
Upload cleaned datasets (e.g., `benin_clean.csv`, `sierra_leone_clean.csv`, `togo_clean.csv`) 
to compare solar metrics across countries. Use the sidebar to select metrics and toggle heatmaps or summary stats.
""")

# --- File Upload ---
uploaded_files = st.file_uploader(
    "📂 Upload Cleaned CSV Files (at least 2–3 countries)",
    type=["csv"],
    accept_multiple_files=True
)

if not uploaded_files:
    st.info("Please upload your cleaned country CSV files to start analysis.")
    st.stop()

# --- Load Data ---
data_dict = load_data(uploaded_files)
countries = list(data_dict.keys())

# --- Sidebar Controls ---
st.sidebar.header("Dashboard Controls")
metric = st.sidebar.selectbox("Select metric to analyze", ["GHI", "DNI", "DHI"])
show_heatmap = st.sidebar.checkbox("Show correlation heatmaps", value=False)
show_summary = st.sidebar.checkbox("Show summary statistics", value=True)

# --- Boxplot ---
st.subheader(f"Comparing {metric} Across {', '.join(countries)}")
box_fig = plot_boxplots(data_dict, metric)
st.plotly_chart(box_fig, use_container_width=True)

# --- Average Bar Chart ---
avg_fig = plot_avg_bar(data_dict, metric)
st.plotly_chart(avg_fig, use_container_width=True)

# --- Summary Statistics ---
if show_summary:
    st.subheader("Summary Statistics (Mean, Median, Std)")
    summary_df = get_summary_stats(data_dict, [metric])
    st.dataframe(summary_df.style.format(precision=2))

# --- Optional: Correlation Heatmaps (on-demand) ---
if show_heatmap:
    st.subheader("Correlation Heatmaps per Country")
    for country, df in data_dict.items():
        with st.expander(country):
            st.plotly_chart(generate_heatmap(df, country), use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
**Features implemented:**
- Multi-country CSV upload & automatic recognition  
- Metric selection (GHI, DNI, DHI)  
- Boxplots + average ranking bars  
- Optional heatmaps for internal variable correlation  
- Summary statistics per country  
""")

import pandas as pd
import plotly.express as px

# --- Load and cache data ---
import streamlit as st

@st.cache_data
def load_data(uploaded_files):
    """Load multiple uploaded CSVs into a dictionary of DataFrames (cached)."""
    data = {}
    for uploaded_file in uploaded_files:
        name = uploaded_file.name.replace("_clean.csv", "").replace(".csv", "").capitalize()
        df = pd.read_csv(uploaded_file, parse_dates=True)
        df["Country"] = name
        data[name] = df
    return data

# --- Summary stats ---
@st.cache_data
def get_summary_stats(data_dict, metrics=["GHI", "DNI", "DHI"]):
    """Return summary statistics (mean, median, std) for given metrics."""
    summary = []
    for country, df in data_dict.items():
        stats = {"Country": country}
        for metric in metrics:
            if metric in df.columns:
                stats[f"{metric}_mean"] = df[metric].mean()
                stats[f"{metric}_median"] = df[metric].median()
                stats[f"{metric}_std"] = df[metric].std()
        summary.append(stats)
    return pd.DataFrame(summary)

# --- Boxplot ---
def plot_boxplots(data_dict, metric="GHI", sample_size=5000):
    """Create a boxplot comparing a metric across countries with optional downsampling."""
    combined = pd.concat(data_dict.values(), ignore_index=True)
    if len(combined) > sample_size:
        combined = combined.sample(sample_size, random_state=42)
    fig = px.box(
        combined,
        x="Country",
        y=metric,
        color="Country",
        title=f"{metric} Comparison Across Countries",
        points="all",
    )
    fig.update_layout(template="plotly_white", height=500)
    return fig

# --- Average bar chart ---
def plot_avg_bar(data_dict, metric="GHI"):
    """Bar chart showing average metric per country."""
    summary = get_summary_stats(data_dict, [metric])
    fig = px.bar(
        summary,
        x="Country",
        y=f"{metric}_mean",
        title=f"Average {metric} by Country",
        color="Country",
        text_auto=".2f"
    )
    fig.update_layout(template="plotly_white", height=400)
    return fig

# --- Correlation heatmap ---
def generate_heatmap(df, country_name):
    """Generate a correlation heatmap for main solar metrics."""
    metrics = ["GHI", "DNI", "DHI", "TModA", "TModB"]
    existing = [m for m in metrics if m in df.columns]
    corr = df[existing].corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title=f"Correlation Heatmap — {country_name}",
    )
    return fig

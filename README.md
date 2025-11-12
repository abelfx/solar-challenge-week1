# ☀️ Solar Data Discovery — Week 1 Challenge  
### Kickstart Your AI Mastery with Cross-Country Solar Farm Analysis  

---

## 🌍 Overview  
This repository contains my submission for **10 Academy’s Week 1 Challenge** — *Solar Data Discovery*.  
The challenge focuses on understanding, exploring, and analyzing solar radiation data across **Benin**, **Sierra Leone**, and **Togo**, to identify regions with the highest solar potential for future investments.  

---

## 🏢 Business Context  
**MoonLight Energy Solutions** aims to enhance its operational efficiency and sustainability through data-driven solar investments.  
As an **Analytics Engineer**, my objective was to:  

- Analyze environmental and solar measurement data.  
- Perform exploratory data analysis (EDA) for each country.  
- Identify key trends and insights supporting solar installation strategies.  
- Provide actionable insights toward the company’s long-term sustainability goals.  

---

## 📊 Dataset Overview  

| Column | Description |
|--------|--------------|
| **Timestamp** | Date and time of each observation |
| **GHI (W/m²)** | Global Horizontal Irradiance |
| **DNI (W/m²)** | Direct Normal Irradiance |
| **DHI (W/m²)** | Diffuse Horizontal Irradiance |
| **ModA / ModB (W/m²)** | Sensor/module irradiance measurements |
| **Tamb (°C)** | Ambient Temperature |
| **RH (%)** | Relative Humidity |
| **WS (m/s)** | Wind Speed |
| **WSgust (m/s)** | Maximum Wind Gust Speed |
| **WD (°N)** | Wind Direction |
| **BP (hPa)** | Barometric Pressure |
| **Cleaning (1/0)** | Cleaning event indicator |
| **Precipitation (mm/min)** | Rainfall rate |
| **TModA / TModB (°C)** | Module temperatures |
| **Comments** | Additional notes |

---

## 📁 Project Structure

```bash
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI pipeline
│
│
├── data/                         # (ignored in .gitignore)
│   ├── benin_clean.csv
│   ├── togo_clean.csv
│   └── sierraleone_clean.csv
│
├── notebooks/
│   ├── benin_eda.ipynb           # EDA notebook for Benin
│   ├── togo_eda.ipynb            # EDA notebook for Togo
│   ├── sierraleone_eda.ipynb     # EDA notebook for Sierra Leone
│   └── compare_countries.ipynb   # Cross-country analysis
│
├── scripts/
│   ├── __init__.py
│   └── README.md                 # Documentation for helper scripts
│
├── tests/
│   └── __init__.py               # Unit tests placeholder
│
├── app/                          # Streamlit dashboard
│   ├── main.py                   # Streamlit main app
│   └── utils.py                  # Utility functions for data/visuals
│
├── requirements.txt              # Python dependencies
├── .gitignore                    # Ignored files & folders
├── README.md                     # Project documentation
```

## 🧠 Task Summary  

### 🧩 **Task 1 — Git & Environment Setup**
**Branch:** `setup-task`  
**Objective:** Establish proper version control and environment configuration.

**Steps Completed:**  
- ✅ Created GitHub repo `solar-challenge-week1`  
- ✅ Initialized virtual environment (`venv`)  
- ✅ Added `.gitignore` (ignored data/, CSVs, and notebooks checkpoints)  
- ✅ Added `requirements.txt` and minimal `ci.yml` for CI/CD  
- ✅ Merged setup branch into `main` via Pull Request  

**Key Files:**  
- `.github/workflows/ci.yml` → runs basic Python CI  
- `requirements.txt` → includes pandas, numpy, matplotlib, seaborn, scipy  

---

### 📈 **Task 2 — Data Profiling, Cleaning & EDA**

**Branches:**  
- `eda-benin`  
- `eda-togo`  
- `eda-sierraleone`  

Each country had a dedicated notebook:  
- 📘 `notebooks/benin_eda.ipynb`  
- 📗 `notebooks/togo_eda.ipynb`  
- 📙 `notebooks/sierraleone_eda.ipynb`

**Key EDA Activities:**  

#### 1️⃣ Summary Statistics & Missing Values
- Generated `df.describe()` for all numeric columns.  
- Identified columns with >5% missing values using `df.isna().sum()`.  
- Handled missing values via **median imputation** for key metrics (GHI, DNI, DHI).  

#### 2️⃣ Outlier Detection & Cleaning
- Used **Z-score method** (|Z| > 3) to detect anomalies in:
  - GHI, DNI, DHI  
  - ModA, ModB  
  - WS, WSgust  
- Outliers visualized using boxplots and histograms.  

#### 3️⃣ Time Series Analysis
- Created time-based visualizations:
  - GHI, DNI, DHI, and Tamb vs. Timestamp  
  - Monthly and daily patterns of solar irradiance  
- Observed diurnal patterns (peak radiation at mid-day, low at night).  

#### 4️⃣ Cleaning Impact
- Grouped by `Cleaning` flag and compared average `ModA` & `ModB`.  
- Found post-cleaning improvements in irradiance readings.  

#### 5️⃣ Correlation & Relationship Analysis
- Heatmaps showing strong correlations between:
  - GHI ↔ DNI ↔ DHI  
  - TModA ↔ TModB ↔ Tamb  
- Scatter plots: RH vs Tamb, WS vs GHI  

#### 6️⃣ Wind & Distribution Analysis
- Wind direction visualized using **polar plots** (wind rose).  
- Distribution plots for GHI and WS showing normal-like spread with seasonal variations.  

#### 7️⃣ Temperature Analysis
- RH inversely correlated with Tamb — higher humidity = lower temperature.  
- GHI and Tamb show direct proportionality.  

#### 8️⃣ Bubble Chart
- Visualized `GHI vs Tamb` with bubble size = `RH` to represent atmospheric moisture influence.  

---

## 🌞 Insights Summary (per Country)

| Country | Key Insight | Observation |
|----------|--------------|-------------|
| **Benin** | High GHI mean | Consistent daily solar exposure; minimal variation |
| **Togo** | Slightly lower GHI but stable DNI | Moderate humidity impact |
| **Sierra Leone** | Highest RH and variable GHI | Cloud cover reduces overall solar efficiency |

---

## 🚧 Task 3 (In Progress): Cross-Country Comparison  
Planned next:
- Combine cleaned datasets (`data/*.csv`)  
- Compare GHI, DNI, DHI distributions  
- Conduct **ANOVA** for statistical significance  
- Visual ranking of solar potential across countries  

---

## 💡 Key Learnings
- Practical experience in **EDA**, **data cleaning**, and **visual storytelling**.  
- Enhanced understanding of environmental data variability.  
- Hands-on application of **Z-score**, **correlation analysis**, and **EDA workflows**.  
- Strengthened Git/GitHub and CI/CD workflow setup.  

---

## 🧮 Tech Stack
| Tool / Library | Purpose |
|----------------|----------|
| **Python 3.11** | Core programming |
| **Pandas / NumPy** | Data manipulation |
| **Matplotlib / Seaborn** | Data visualization |
| **Scipy** | Statistical testing |
| **GitHub Actions** | CI/CD automation |
| **Streamlit (Upcoming)** | Interactive dashboard development |

---

## 💻 How to Reproduce Environment  

```bash
# 1️⃣ Clone repository
git clone https://github.com/abelfx/solar-challenge-week0
cd solar-challenge-week1

# 2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Explore notebooks
jupyter notebook notebooks/



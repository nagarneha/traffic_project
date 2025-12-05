import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Traffic Accident Dashboard", layout="wide")

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("traffic_accidents.csv")

# Clean numeric columns (Vehicles, Casualties)
df["Vehicles_Involved"] = (
    df["Vehicles_Involved"]
    .astype(str)
    .str.extract(r"(\d+)", expand=False)
    .fillna("0")
    .astype(int)
)

df["Casualties"] = (
    df["Casualties"]
    .astype(str)
    .str.extract(r"(\d+)", expand=False)
    .fillna("0")
    .astype(int)
)

# Clean Severity (Low/Medium/High -> numeric 1/2/3)
severity_map = {"Low": 1, "Medium": 2, "High": 3}
df["Severity_Level"] = df["Severity"].map(severity_map)

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("Filters")

cities = st.sidebar.multiselect("Select City:", options=df["City"].unique(), default=df["City"].unique())

weather = st.sidebar.multiselect("Select Weather:", options=df["Weather"].unique(), default=df["Weather"].unique())

severity = st.sidebar.multiselect("Select Severity:", options=df["Severity"].unique(), default=df["Severity"].unique())


filtered_df = df[
    (df["City"].isin(cities)) &
    (df["Weather"].isin(weather)) &
    (df["Severity"].isin(severity))
]

"""# -------------------------------
# MAIN TITLE
# -------------------------------
st.title("🚦 Traffic Accident Analysis Dashboard")

st.write("Filtered dataset based on your selection:")

st.dataframe(filtered_df, use_container_width=True)

# -------------------------------
# KPI CARDS (TOP METRICS)
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Accidents", len(filtered_df))
col2.metric("Avg. Vehicles Involved", round(filtered_df["Vehicles_Involved"].mean(), 2))
col3.metric("Avg. Severity (1–Low, 3–High)", round(filtered_df["Severity_Level"].mean(), 2))

# -------------------------------
# CHART 1 — CITY WISE ACCIDENT COUNT
# -------------------------------
st.subheader("📊 Accidents by City")
fig1 = px.bar(filtered_df.groupby("City")["Accident_ID"].count().reset_index(),
              x="City", y="Accident_ID", title="City-wise Accident Count")
st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# CHART 2 — WEATHER IMPACT
# -------------------------------
st.subheader("🌦️ Accidents by Weather Condition")
fig2 = px.pie(filtered_df, names="Weather", title="Weather Impact on Accidents")
st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# CHART 3 — ROAD TYPE ANALYSIS
# -------------------------------
st.subheader("🛣️ Road Type Distribution")
fig3 = px.bar(filtered_df.groupby("Road_Type")["Accident_ID"].count().reset_index(),
              x="Road_Type", y="Accident_ID", title="Accidents per Road Type")
st.plotly_chart(fig3, use_container_width=True)

# -------------------------------
# CHART 4 — VEHICLES INVOLVED TREND
# -------------------------------
st.subheader("🚗 Vehicles Involved Trend")
fig4 = px.line(filtered_df, x="Date", y="Vehicles_Involved", markers=True, title="Vehicles Involved Over Time")
st.plotly_chart(fig4, use_container_width=True)"""



# app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Store Sales Forecasting",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Store Sales Forecasting Dashboard")
st.markdown("Forecast future store sales using **SARIMAX with promotion impact**.")

# -------------------- Load Data --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/daily_sales.csv", parse_dates=["date"])
    df.set_index("date", inplace=True)
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0)
    df["onpromotion"] = pd.to_numeric(df["onpromotion"], errors="coerce").fillna(0)
    return df

df = load_data()

# -------------------- Load Model --------------------
def load_model():
    return joblib.load("sarimax_sales_model.pkl")

model = load_model()

# -------------------- Sidebar --------------------
st.sidebar.header("⚙️ Forecast Settings")

n_days = st.sidebar.slider(
    "Forecast Horizon (Days)",
    min_value=7,
    max_value=90,
    value=30
)

promo_type = st.sidebar.selectbox(
    "Promotion Scenario",
    ["No Promotion", "Full Promotion", "Custom"]
)

# -------------------- Promotion logic --------------------
if promo_type == "No Promotion":
    future_promo = [0] * n_days
elif promo_type == "Full Promotion":
    future_promo = [1] * n_days
else:
    st.sidebar.markdown("#### Custom Promotion Plan")
    future_promo = [
        st.sidebar.number_input(
            f"Day {i+1}",
            min_value=0,
            max_value=1,
            value=0,
            key=f"promo_{i}"
        )
        for i in range(n_days)
    ]

future_exog = np.array(future_promo).reshape(-1, 1)

# -------------------- KPI Section --------------------
st.subheader("📊 Key Performance Indicators")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Last Recorded Sales", f"{df['sales'].iloc[-1]:,.0f}")

with col2:
    st.metric("Average Daily Sales", f"{df['sales'].mean():,.0f}")

with col3:
    st.metric("Promotion Days (Forecast)", sum(future_promo))

# -------------------- Historical Chart --------------------
st.subheader("📉 Historical Sales Trend")
st.line_chart(df["sales"].tail(90))

# -------------------- Forecast --------------------
if st.button("🚀 Generate Forecast"):

    # Forecast with selected promotion
    forecast = model.forecast(
        steps=n_days,
        exog=future_exog
    )

    forecast_df = pd.DataFrame(
        {"Forecasted Sales": forecast},
        index=pd.date_range(
            start=df.index[-1] + pd.Timedelta(days=1),
            periods=n_days
        )
    )

    # -------------------- Forecast KPIs --------------------
    st.subheader("📈 Forecast Summary")
    col1, col2, col3 = st.columns(3)

    # Forecast with No Promotion to calculate boost
    forecast_no_promo = model.forecast(
        steps=n_days,
        exog=np.zeros((n_days, 1))
    )
    forecast_no_df = pd.DataFrame(forecast_no_promo, index=forecast_df.index)

    promotion_boost = forecast_df["Forecasted Sales"] - forecast_no_df[0]

    with col1:
        st.metric("Total Forecasted Sales", f"{forecast_df['Forecasted Sales'].sum():,.0f}")
    with col2:
        st.metric("Average Forecasted Sales", f"{forecast_df['Forecasted Sales'].mean():,.0f}")
    with col3:
        st.metric("Total Promotion Boost", f"{promotion_boost.sum():,.0f}")

    # -------------------- Forecast Chart --------------------
    st.subheader("📊 Forecast Visualization")

    combined_df = pd.concat(
        [df["sales"].tail(60), forecast_df["Forecasted Sales"]],
        axis=0
    )

    st.line_chart(combined_df)

    # -------------------- Promotion Impact Chart --------------------
    st.subheader("💡 Promotion Impact (Sales Difference)")
    st.line_chart(promotion_boost)

    # -------------------- Forecast Table --------------------
    with st.expander("📄 View Forecast Data"):
        st.dataframe(forecast_df, use_container_width=True)

# -------------------- Footer --------------------
st.markdown("---")
st.markdown("💡 **Built using SARIMAX & Streamlit** | Time Series Forecasting Project")

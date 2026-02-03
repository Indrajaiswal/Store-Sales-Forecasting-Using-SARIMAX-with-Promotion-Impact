# 📈 Store Sales – Time Series Forecasting (SARIMAX with Promotion Impact)

## 💡 Project Overview
The **Store Sales Forecasting Dashboard** is an end-to-end time series forecasting system designed to predict daily store sales using historical data and promotion information. 

This project evaluates multiple forecasting models (**ARIMA, SARIMAX, and Prophet**) and deploys an interactive **Streamlit** dashboard to analyze future sales under different promotion scenarios.

## 🎯 Primary Goal
Enable businesses to accurately forecast short-term sales while understanding the effect of promotions on demand, supporting:
* **Inventory planning** & **Revenue forecasting**
* **Promotion strategy analysis**
* **Data-driven decision making**

## 🔗 Live App
[![Streamlit App](https://static.streamlit.io)](https://store-sales-forecasting-using-sarimax-with-promotion-impactgit.streamlit.app/)

## 🚀 Key Features
* **Interactive Dashboard:** Visualize historical trends vs. future forecasts.
* **Scenario Simulation:** Compare sales outcomes for **No Promotion**, **Full Promotion**, or **Custom Promotion** strategies.
* **KPI Metrics:** Track latest sales, average volume, and promotion density.
* **Data Export:** Download generated forecasts as CSV for external use.

## 🛠️ Tech Stack & Installation
* **Language:** Python 3.12 (Required for compatibility)
* **Libraries:** Streamlit, Statsmodels, Prophet, Scikit-learn, Pandas, Altair.

## 📊 Dataset Overview

source: https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data

| Column      | Description                              |
| ----------- | ---------------------------------------- |
| id          | Unique identifier for each record        |
| date        | Date of the sales record                 |
| store_nbr   | Store number                             |
| family      | Product family/category                  |
| sales       | Daily sales amount (**target variable**) |
| onpromotion | Promotion indicator (0 = No, 1 = Yes)    |

Frequency: Daily
Target Variable: sales

## 🧼 Data Preprocessing

Converted date column to datetime index

Checked and handled missing values

Aggregated data at daily level

Optional log transformation for stability

Prepared exogenous variables for SARIMAX

Holiday features processed for Prophet

## 🤖 Model Development:
Models Used

ARIMA

Captures historical trends and autocorrelation

Does not support seasonality or promotions

Used as a baseline model

SARIMAX

Extends ARIMA with:

Weekly seasonality (7 days)

Exogenous variable (onpromotion)

Learns how promotions historically affect sales

Enables promotion-based scenario forecasting

Prophet

Automatically models trend and seasonality

Tested with and without holiday effects

Evaluation Metrics

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

AIC (Akaike Information Criterion)

Time Series Cross-Validation

Hyperparameter Tuning

ARIMA

Grid search for (p, d, q)

SARIMAX

Grid search for (p, d, q) and seasonal (P, D, Q, s)

Prophet

changepoint_prior_scale

seasonality_prior_scale

holidays_prior_scale

### Local Setup
1. **Clone the repo:**
   ```bash
   git clone https://github.com
   cd store-sales-forecasting

  2. **Create a Python 3.12 environment:**
     ```bash
     py -3.12 -m venv venv
     .\venv\Scripts\activate

  3. **Install fixed dependencies:**
     ```bash
    pip install -r requirements.txt
     
  4. **Run the app:**
     ```bash
     streamlit run app.py


### 📊 Dataset Overview
## Source: Kaggle Store Sales - Time Series Forecasting
* Target Variable: sales
* Exogenous Regressor: onpromotion (0 = No, 1 = Yes)
* Frequency: Daily

## 🔍 Model Performance
| Model              | MAE       | RMSE      | Notes                        |
| ------------------ | --------- | --------- | ---------------------------- |
| ARIMA              | 26,505.89 | 43,422.49 | Strong baseline performance  |
| SARIMAX            | 69,032.02 | 87,154.60 | Promotion impact was limited |
| Prophet            | 37,628.94 | 50,568.55 | Good trend modeling          |
| Prophet + Holidays | 37,628.94 | 50,568.55 | Holiday impact insignificant |


## ✅ Conclusion
While ARIMA showed lower error, SARIMAX was selected for production because it allows business users to simulate "What-If" scenarios regarding promotions. The analysis revealed that while promotions influence sales, historical seasonality remains the dominant driver of demand.


## 🚀 Deployment:
The trained SARIMAX model is saved using Joblib and deployed with Streamlit.

Dashboard Capabilities:

Visualize historical sales trends

Forecast future sales for 7–90 days

Simulate promotion scenarios:

No Promotion

Full Promotion

Custom Promotion

Display KPIs:

Latest sales

Average sales

Number of promotion days

Download forecast results as CSV

## 🧪 Run Locally:
git clone  https://github.com/Indrajaiswal/Store-Sales-Forecasting-Using-SARIMAX-with-Promotion-Impact.git

## 👤 Author

**Indra Jaiswal**
📅 February 2026

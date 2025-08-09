# From Reviews to Reservations: How Machine Learning is Transforming Tourism

## Overview

This project demonstrates how machine learning can be applied to transform tourism management by combining:

- **Tourist demand forecasting** using multiple time series forecasting models (Linear Regression, Polynomial Regression, ARIMA, Exponential Smoothing, Prophet) on Rajasthan tourist arrival data.
- **Tourist sentiment analysis** using BERT-based NLP models on visitor reviews from Rajasthan cities to understand visitor satisfaction.
- **Integration of forecasts and sentiment** to help stakeholders prioritize destinations for development and marketing.

By leveraging both quantitative visitor forecasts and qualitative sentiment insights, this project aims to empower tourism planners, businesses, and policymakers to make smarter, data-driven decisions.

---

## Contents

- `forecasting/` — Jupyter notebooks and scripts for forecasting tourist arrivals using various ML/statistical models.
- `sentiment_analysis/` — Scripts and notebooks for sentiment analysis on tourist reviews using BERT.
- `data/` — Raw and processed datasets (tourism statistics, reviews).
- `requirements.txt` — Python dependencies.
- `README.md` — This documentation.

---

## Tourist Demand Forecasting

The forecasting component uses historical tourist arrival data from 2010 to 2023 for Rajasthan, India, split into training (2010-2021) and testing (2022-2023) sets. Five forecasting techniques are applied and compared based on RMSE:

1. Linear Regression  
2. Polynomial Regression (degree 2)  
3. ARIMA (1,1,1)  
4. Exponential Smoothing  
5. Prophet  

Prophet shows the best accuracy in predicting domestic tourist arrivals.

---

## Tourist Sentiment Analysis

Using a dataset of thousands of online tourist reviews filtered for Rajasthan cities, the project applies a pre-trained BERT-based sentiment model to score reviews from positive to negative.

This analysis reveals visitor satisfaction levels by city and specific places, helping to identify areas for improvement or growth.

---

## Integration & Insights

By combining forecasted visitor numbers with sentiment scores, the project proposes a priority matrix for tourism management:

- High forecast & high sentiment: Maintain/expand resources  
- High forecast & low sentiment: Improve services urgently  
- Low forecast & high sentiment: Growth opportunities  
- Low forecast & low sentiment: Low immediate priority  

This approach supports proactive tourism planning beyond raw visitor counts.

---

## Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/tourism-ml-forecast-sentiment-analysis.git
   cd tourism-ml-forecast-sentiment-analysis
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

Run forecasting scripts/notebooks in forecasting/ for time series models.

Run sentiment analysis in sentiment_analysis/.

Check combined analysis notebooks for integration and visualization.

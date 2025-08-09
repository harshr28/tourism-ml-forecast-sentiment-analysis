# Tourism Sentiment Analysis for Rajasthan

This project analyzes tourist reviews from various places in Rajasthan using sentiment analysis powered by a BERT multilingual model. It loads data from Kaggle via Kagglehub, filters for Rajasthan cities, and computes average sentiment scores.

## Setup

1. Clone the repo

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
   
3. Install dependencies:

```bash
pip install -r requirements.txt
```

Usage
Run the main analysis script:

Edit
```bash
python run_analysis.py
```

This will:

Load the review data from Kagglehub

Filter for Rajasthan cities

Sample reviews and perform sentiment analysis

Print sample sentiment scores

Notes

You may need to authenticate Kagglehub with your Kaggle API credentials.

The sentiment model used is nlptown/bert-base-multilingual-uncased-sentiment.
You may need to authenticate Kagglehub with your Kaggle API credentials.

The sentiment model used is nlptown/bert-base-multilingual-uncased-sentiment.

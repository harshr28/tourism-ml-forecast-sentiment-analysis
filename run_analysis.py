```python

from src.data_loader import load_reviews
from src.filtering import filter_rajasthan
from src.sentiment import create_sentiment_analyzer, analyze_sentiment

def main():
    print("Loading data...")
    df = load_reviews()

    print("Filtering Rajasthan cities...")
    df_raj = filter_rajasthan(df)

    print(f"Total reviews in Rajasthan: {len(df_raj)}")

    # Sample 500 reviews to analyze
    sample_reviews = df_raj["Review"].dropna().sample(n=500, random_state=42).tolist()

    print("Creating sentiment analyzer...")
    sentiment_analyzer = create_sentiment_analyzer()

    print("Analyzing sentiment...")
    scores = analyze_sentiment(sentiment_analyzer, sample_reviews)

    print("Sample sentiment scores:", scores[:10])

if __name__ == "__main__":
    main()

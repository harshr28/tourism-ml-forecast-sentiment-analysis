import kagglehub
from kagglehub import KaggleDatasetAdapter

def load_reviews():
    filename = "Review_db.csv"
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "ritvik1909/indian-places-to-visit-reviews-data",
        filename
    )
    return df

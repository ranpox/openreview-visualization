from openreview_visualization.data.fetcher import OpenReviewFetcher
from openreview_visualization.utils import save_jsonl
import pandas as pd

if __name__ == "__main__":
    papers = pd.read_csv("paperlist.csv")
    fetcher = OpenReviewFetcher("ICLR", "2024")
    reviews = fetcher.fetch_reviews(papers["id"].tolist())
    save_jsonl(reviews, "raw_paper_reviews.jsonl")

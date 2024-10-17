from openreview_visualization.data.processor import OpenReviewProcessor
import orjson

if __name__ == "__main__":
    processor = OpenReviewProcessor()

    with open("raw_paper_reviews.jsonl", "r") as f:
        reviews = [orjson.loads(line) for line in f]

    df = processor.process_reviews(reviews)
    df.sort_values(by=["avg_rating", "std_dev"], ascending=[False, True], inplace=True)
    df.to_csv("paper_reviews.csv", index=False)

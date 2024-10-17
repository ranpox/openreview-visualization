from openreview_visualization.data.fetcher import OpenReviewFetcher
from openreview_visualization.data.processor import OpenReviewProcessor
from openreview_visualization.utils import save_json

if __name__ == "__main__":
    fetcher = OpenReviewFetcher("ICLR", "2025", batch_limit=1000, limit=-1)
    papers, count = fetcher.fetch_papers()
    save_json({"notes": papers, "count": count}, "data/raw/iclr2025/raw_paperlist.json")

    processor = OpenReviewProcessor()
    df = processor.process_papers(papers)
    df.to_csv("data/processed/iclr2025/paperlist.csv", index=False)

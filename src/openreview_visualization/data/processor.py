import pandas as pd
import statistics


class OpenReviewProcessor:
    @staticmethod
    def process_papers(papers):
        df = pd.json_normalize(papers)
        filtered_df = df[
            [
                "id",
                "content.title.value",
                "content.abstract.value",
                "content.primary_area.value",
                "content.keywords.value",
                "content.TLDR.value",
            ]
        ]
        filtered_df.columns = ["id", "title", "abstract", "primary_area", "keywords", "tldr"]
        return filtered_df

    @staticmethod
    def process_reviews(reviews):
        processed_data = []
        for review in reviews:
            paper_id = None
            title = ""
            paper_ratings = []

            for note in review["notes"]:
                if "title" in note["content"]:
                    title = note["content"]["title"]["value"]
                    paper_id = note["id"]
                elif "rating" in note["content"]:
                    rating = int(note["content"]["rating"]["value"].split(":")[0])
                    paper_ratings.append(rating)

            if paper_ratings:
                avg_rating = sum(paper_ratings) / len(paper_ratings)
                std_dev = statistics.stdev(paper_ratings) if len(paper_ratings) > 1 else 0
            else:
                avg_rating = None
                std_dev = None

            processed_data.append(
                {"id": paper_id, "title": title, "avg_rating": avg_rating, "std_dev": std_dev, "ratings": paper_ratings}
            )

        return pd.DataFrame(processed_data)

import requests
from tqdm import tqdm
import concurrent.futures


class OpenReviewFetcher:
    BASE_URL = "https://api2.openreview.net/notes"
    HEADERS = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }

    def __init__(self, venue, year, batch_limit=1000, limit=-1):
        self.venue = venue
        self.year = year
        self.batch_limit = batch_limit
        self.limit = limit

    def fetch_papers(self):
        url = f"{self.BASE_URL}?content.venueid={self.venue}.cc%2F{self.year}%2FConference%2FSubmission&details=replyCount%2Cinvitation%2Coriginal&domain={self.venue}.cc%2F{self.year}%2FConference"
        initial_data = self._fetch_data(url)
        count = initial_data["count"]
        print(url)
        print(f"Total number of papers: {count}")
        print(f"Batch limit: {self.batch_limit}")
        print(f"Limit: {self.limit}")
        all_papers = []
        for offset in tqdm(range(0, count, self.batch_limit)):
            data = self._fetch_data(f"{url}&limit={self.batch_limit}&offset={offset}")
            all_papers.extend(data["notes"])
            if self.limit != -1 and len(all_papers) >= self.limit:
                break

        return all_papers, count

    def fetch_reviews(self, paper_ids):
        base_url = f"{self.BASE_URL}?details=replyCount%2Cwritable%2Csignatures%2Cinvitation%2Cpresentation&domain={self.venue}.cc%2F{self.year}%2FConference&forum="

        with requests.Session() as session:
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                futures = [
                    executor.submit(self._fetch_data, f"{base_url}{paper_id}", session) for paper_id in paper_ids
                ]
                return [
                    future.result() for future in tqdm(concurrent.futures.as_completed(futures), total=len(paper_ids))
                ]

    def _fetch_data(self, url, session=None):
        if session:
            response = session.get(url, headers=self.HEADERS)
        else:
            response = requests.get(url, headers=self.HEADERS)
        return response.json()

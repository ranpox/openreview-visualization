# OpenReview Visualization

This repository contains tools for downloading, parsing, and visualizing OpenReview submission data for various academic conferences, including ICLR 2024 and ICLR 2025. The data is downloaded using the [OpenReview API](https://docs.openreview.net/reference/api-v2/).

## Supported Conferences

| Conference | Nomic Visualization | Gradio Review Table | Word Cloud |
| ---------- | ------------------ | ------------------ | ---------- |
| ICLR 2025 | [Link](https://atlas.nomic.ai/data/ranpox/iclr2025/map) |  |  |
| ICLR 2024 | [Link](https://atlas.nomic.ai/data/ranpox/iclr-2024-submission/map) | [Link](https://huggingface.co/spaces/ranpox/iclr2024-submissions) | [Link](assets/wordcloud.png) |

## Data

For each supported conference, we provide the following data:

- Raw paper list data (JSON format)
- Raw paper reviews data (JSONL format)
- Parsed paper data (CSV format) containing:
  - ID
  - Title
  - Abstract
  - Primary area
  - Keywords
  - TLDR
- Parsed review data (CSV format) containing:
  - ID
  - Title
  - Average Score
  - Standard Deviation
  - Individual Scores

## Visualizations

### Interactive Visualization
Explore submissions using an interactive visualization powered by [Nomic Atlas](https://atlas.nomic.ai/):

[ICLR 2024 Visualization](https://atlas.nomic.ai/data/ranpox/iclr-2024-submission/map)
[ICLR 2025 Visualization](https://atlas.nomic.ai/data/ranpox/iclr2025/map)

![ICLR 2024 Submissions](assets/nomic_atlas.png)

### Rating Table
We provide a Gradio demo for exploring the rating table of submissions:

[ICLR 2024 Rating Table](https://huggingface.co/spaces/ranpox/iclr2024-submissions)

![Gradio Demo](assets/gradio.png)

### Statistical Visualizations
For each conference, we generate:

- Average Score Distribution
- Average Score Cumulative Distribution
- Top 50 Keywords Bar Chart
- Top 50 Keywords Word Cloud

Example visualizations:

![Average Score Distribution](assets/avg_dist.png)
![Top 50 Keywords Word Cloud](assets/top_keywords_wordcloud.png)

## Usage

### Download Data

```
python scripts/download_papers.py
```

### Generate Word Cloud

```
python scripts/visualize_wordcloud.py
```

### Generate Nomic Atlas Visualization

```
python scripts/visualize_nomic.py
```

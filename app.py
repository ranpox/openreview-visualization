from openreview_visualization.visualizers import OpenReviewVisualizer

if __name__ == "__main__":
    visualizer = OpenReviewVisualizer("paper_reviews.csv")
    visualizer.launch_app()

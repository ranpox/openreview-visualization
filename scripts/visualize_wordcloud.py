from openreview_visualization.visualizers.wordcloud import WordCloudVisualizer

if __name__ == "__main__":
    visualizer = WordCloudVisualizer("data/processed/iclr2025/paperlist.csv")
    visualizer.generate()
    visualizer.display()

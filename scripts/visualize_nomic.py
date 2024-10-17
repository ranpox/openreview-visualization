from openreview_visualization.visualizers.nomic import NomicVisualizer

if __name__ == "__main__":
    visualizer = NomicVisualizer("data/processed/iclr2025/paperlist.csv", project_name="iclr2025")
    visualizer.generate()
    visualizer.display()

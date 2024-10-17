from nomic import atlas
import pandas as pd
from .base import VisualizerBase


class NomicVisualizer(VisualizerBase):
    def __init__(self, data_file, project_name):
        super().__init__()
        self.data = pd.read_csv(data_file)
        self.project_name = project_name
        self.project = None

        self.data["title_abstract"] = "Title: " + self.data["title"] + "\n\nAbstract: " + self.data["abstract"]

    def generate(self):
        df = self.data.drop(columns=["tldr"])  # drop the tldr column since it's not compatible with atlas
        self.project = atlas.map_data(
            data=df.to_dict("records"),
            indexed_field="title_abstract",
            identifier=self.project_name,
        )

    def display(self):
        if self.project:
            print(f"Nomic Atlas project '{self.project_name}' has been generated.")
            print("You can view it in the Nomic Atlas web interface.")
        else:
            print("Project has not been generated yet. Call generate() first.")

    def save(self, filename):
        # Nomic Atlas projects are saved automatically, so we'll just log a message
        print(f"Nomic Atlas project '{self.project_name}' is automatically saved in the Nomic cloud.")

from .base import VisualizerBase
import gradio as gr


class GradioVisualizer(VisualizerBase):
    def __init__(self, data):
        super().__init__(data)
        self.app = None

    def generate(self):
        def search_papers(query=""):
            if query:
                return self.data[
                    self.data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)
                ]
            return self.data

        with gr.Blocks() as self.app:
            gr.Markdown("# ICLR 2024 Paper Review Explorer")
            gr.Markdown("Explore and search through the paper reviews for ICLR 2024.")
            search_bar = gr.Textbox(placeholder="Enter search terms here...", label="Search Reviews")
            reviews_table = gr.Dataframe(self.data)

            search_bar.change(fn=search_papers, inputs=search_bar, outputs=reviews_table)

    def display(self):
        if self.app:
            self.app.launch()
        else:
            print("Gradio app has not been generated yet. Call generate() first.")

    def save(self, filename):
        print("Gradio apps are not typically saved to files. Use display() to launch the app.")

from .base import VisualizerBase
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import ast
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download required resources
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("wordnet")
nltk.download("punkt_tab")

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()


# Function to convert nltk tag to first character used by WordNetLemmatizer
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith("J"):
        return wordnet.ADJ
    elif nltk_tag.startswith("V"):
        return wordnet.VERB
    elif nltk_tag.startswith("N"):
        return wordnet.NOUN
    elif nltk_tag.startswith("R"):
        return wordnet.ADV
    else:
        return None


def lemmatize_sentence(sentence):
    # Tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    # Tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            # If no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            # Else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)


class WordCloudVisualizer(VisualizerBase):
    def __init__(self, data_file, top_k=50):
        super().__init__()
        self.data = pd.read_csv(data_file)
        self.top_k = top_k
        self.wordcloud = None
        self.top_keywords = None

    def generate(self):
        keywords_list = self.data["keywords"].dropna().apply(ast.literal_eval).tolist()
        all_keywords = [keyword.lower() for sublist in keywords_list for keyword in sublist]
        all_keywords_lemmatized = [lemmatize_sentence(keyword) for keyword in all_keywords]
        keyword_counts_lemmatized = Counter(all_keywords_lemmatized)

        self.top_keywords = keyword_counts_lemmatized.most_common(self.top_k)
        self.wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(
            dict(self.top_keywords)
        )

    def display(self):
        if self.wordcloud:
            plt.figure(figsize=(10, 5))
            plt.imshow(self.wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title(f"Top {self.top_k} Keywords Word Cloud after Lemmatization")
            plt.show()
        else:
            print("WordCloud has not been generated yet. Call generate() first.")

    def save(self, filename):
        if self.wordcloud:
            plt.figure(figsize=(10, 5))
            plt.imshow(self.wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title(f"Top {self.top_k} Keywords Word Cloud after Lemmatization")
            plt.savefig(filename, bbox_inches="tight", dpi=300)
            plt.close()
        else:
            print("WordCloud has not been generated yet. Call generate() first.")

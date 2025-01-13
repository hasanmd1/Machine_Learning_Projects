import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


class Recommender(object):
    def __init__(self):
        pass

    def recommend_movies(self, mood, search, trained_model):
        pass

    def train_recommender_model(self):

        with open("../notebooks/Movies_Recommender_System.ipynb", "r") as file:
            nb = nbformat.read(file, as_version=4)

        ep = ExecutePreprocessor(timeout=600, kernel_name="python3.12")
        ep.preprocess(nb, {"metadata": {"path": "../notebooks"}})

        # replace the original notebook with the executed notebook
        with open("../notebooks/Movies_Recommender_System.ipynb", "w", encoding="utf-8") as f:
            nbformat.write(nb, f)


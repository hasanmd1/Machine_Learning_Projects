import os

import pandas as pd


def load_data():
    project_path = os.path.abspath('..')

    try:
        ratings = pd.read_csv(project_path + '/dataset/raw/ratings.csv')
        tags = pd.read_csv(project_path + '/dataset/raw/tags.csv')
        movies = pd.read_csv(project_path + '/dataset/raw/movies.csv')
        links = pd.read_csv(project_path + '/dataset/raw/links.csv')
    except FileNotFoundError or IOError:
        print('Dataset not found. Download it from https://grouplens.org/datasets/movielens/32m/')
        return None, None, None, None

    return ratings, tags, movies, links
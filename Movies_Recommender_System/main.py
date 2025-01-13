import argparse
import os
import pickle
import sys
from recommender import Recommender


def main():

    if len(sys.argv) > 1:
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description="Movie Recommendation System")
        parser.add_argument("--mood", type=str, help="User's mood", required=True)
        parser.add_argument("--search", type=str, help="Search query", required=True)
        parser.add_argument("--train-model", type=str, help="Train model", required=False)
        args = parser.parse_args()

        mood: list = args.mood.replace(" ", "").lower().split(",")
        search: list = args.search.replace(" ", "").lower().split(",")
        train_model: bool = args.train_model.replace(" ", "").lower() == "y"
    else:
        print("Welcome to the Movie Recommendation System!")
        print("Please enter your mood and search query:")
        mood: list = input("Mood: ").replace(" ", "").lower().split(",")
        search: list = input("Search query: ").replace(" ", "").lower().split(",")
        print("Should we train the model? (y/n)")
        train_model: bool = input("Train model: ").strip().lower() == "y"

        print("Searching for movies that match your mood and search query...")

        print(mood + search)

    if not os.path.exists("./models/recommender_model.pkl") or train_model:
        print("Training model...")
        Recommender().train_recommender_model()
        print("Successfully trained model!")

    # load the model and use it to make predictions for the user
    print("Loading model...")
    with open("./models/recommender_model.pkl", "rb") as f:
        model = pickle.load(f)

    print("Making predictions...")
    recommendations = Recommender().recommend_movies(mood, search, model)

    print("Successfully made predictions!")
    print("Recommendations:")
    print(recommendations)
    print("Thanks for using the Movie Recommendation System!")


if __name__ == "__main__":
    main()

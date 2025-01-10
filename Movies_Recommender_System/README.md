# Movies Recommender System  

This project focuses on building a robust movie recommendation system that suggests movies based on user preferences and historical data. The system employs collaborative filtering, content-based filtering, and hybrid recommendation models to deliver personalized recommendations.  

You can run this project as a standalone Jupyter Notebook or interact with it using a Flask web application that enables dataset uploads, model training, and recommendation testing.  

## Features  

### 1. Collaborative Filtering  

Recommends movies by analyzing user-item interactions and identifying patterns across similar users or items.  

### 2. Content-Based Filtering  

Suggests movies based on the similarity of movie attributes such as genre, actors, and directors to a user's preferences.  

### 3. Hybrid Recommendation Models  

Combines collaborative and content-based approaches for enhanced recommendation accuracy.  

### 4. Flask Integration  

Interact with the recommender system via a web application where you can upload data and test movie recommendations.  

## How Features Are Used  

### **Notebook Structure Summary**  

1. **Data Exploration and Preprocessing**:  
   - Load and clean the MovieLens dataset to ensure data integrity.  
   - Perform Exploratory Data Analysis (EDA) to understand user and item interactions.  

2. **Feature Engineering**:  
   - Generate user-item interaction matrices for collaborative filtering (Feature 1).  
   - Extract movie attributes such as genres and metadata for content-based filtering (Feature 2).  

3. **Model Implementation**:  
   - **Collaborative Filtering**: Implement matrix factorization techniques using Surprise library to generate user-based or item-based recommendations.  
   - **Content-Based Filtering**: Use cosine similarity and other similarity measures to recommend movies based on their attributes.  
   - **Hybrid Models**: Blend collaborative and content-based filtering to optimize recommendations (Feature 3).  

4. **Model Evaluation**:  
   - Evaluate recommendation models using metrics like RMSE, Precision, Recall, and Mean Average Precision (MAP).  
   - Compare the performance of different models to identify the best approach.  

5. **Visualization**:  
   - Visualize user-item interactions, similarity matrices, and top recommendations to gain insights into model performance.  

## Installation  

### Prerequisites  

- Python 3.12+  
- pip environment  
- Virtual environment for isolated dependencies  

### Running the Notebook  

1. **Clone the repository**:  

   ```bash  
   git clone https://github.com/hasanmd1/Machine_Learning_Projects.git  
   cd Movies_Recommender_System  
   ```  

2. **Create and activate a virtual environment**:  

   ```bash  
   python -m venv venv  
   source venv/bin/activate       (for macOS)  
   venv/Scripts/activate          (for Windows)  
   ```  

3. **Install the required dependencies**:  

   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Run the Notebook**:  
   Open the Jupyter Notebook `Movies_Recommender_System.ipynb` to explore the project.  

### Running the Flask Application  

Alternatively, you can explore this project using a Flask web application. The app allows you to upload datasets, configure recommendation models, and test recommendations interactively.  

1. **Navigate to the Flask project**:  

   ```bash  
   cd flask-app  
   ```  

2. **Install dependencies**:  
   Follow the setup instructions in `flask-app/README.md`.  

3. **Run the Flask app**:  

   ```bash  
   python app.py  
   ```  

4. **Access the app**:  
   Open your browser and navigate to `http://127.0.0.1:5000/`.  

## Data  

The dataset used for this project is the **MovieLens Dataset**, a widely used dataset for recommendation systems research and implementation. Access the dataset here:  
[MovieLens Dataset](https://grouplens.org/datasets/movielens/)  

## Usage  

### Recommender System Models  

Use the notebook to implement and evaluate collaborative, content-based, and hybrid recommendation models.  

### Flask Integration  

Upload custom datasets and test recommendation performance via the web interface.  

### Visualization  

Understand user preferences and model behavior through interactive visualizations and similarity graphs.  

## Contributing  

Contributions are not allowed for this project. However, you may open an issue to suggest improvements or new features.  

## License  

This project is licensed under the MIT License. See the LICENSE file for more details.  

## Acknowledgements  

Thanks to the creators of the MovieLens Dataset and the Surprise library for enabling the development of this project.  

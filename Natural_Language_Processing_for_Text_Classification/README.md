# Natural Language Processing for Text Classification  

This project focuses on classifying text documents into predefined categories using various Natural Language Processing (NLP) techniques. The system utilizes text preprocessing, TF-IDF vectorization, and word embeddings to process and classify text efficiently. The project incorporates popular libraries such as NLTK and SpaCy for text processing and Scikit-learn for implementing machine learning algorithms.  

You can run this project as a standalone Jupyter Notebook or interact with it via a Flask web application for dataset uploads, model training, and evaluation.  

## Features  

### 1. TF-IDF and Word Embeddings  

Use Term Frequency-Inverse Document Frequency (TF-IDF) for feature extraction and experiment with word embeddings (Word2Vec, GloVe) for better text representation.  

### 2. Text Preprocessing with NLTK and SpaCy  

Preprocess text using tokenization, stopword removal, lemmatization, and part-of-speech tagging using NLTK and SpaCy.  

### 3. Text Classification Models  

Implement machine learning models such as Naive Bayes, SVM, and Logistic Regression to classify text into categories.  

### 4. Flask Integration  

Interact with the text classification model via a web interface that allows users to upload datasets, train models, and test classifications.  

## How Features Are Used  

### **Notebook Structure Summary**  

1. **Text Preprocessing**:  
   - Tokenize, clean, and preprocess raw text using NLTK and SpaCy (Feature 2).  
   - Remove stopwords, perform lemmatization, and prepare data for feature extraction.  

2. **Feature Extraction**:  
   - Use **TF-IDF** to convert text data into numerical format (Feature 1).  
   - Optionally, use pre-trained word embeddings (Word2Vec, GloVe) to represent words in dense vector spaces.  

3. **Model Building**:  
   - Train various machine learning classifiers (e.g., Naive Bayes, SVM, Logistic Regression) using Scikit-learn.  
   - Evaluate the classifiers' performance based on accuracy, precision, recall, and F1 score.  

4. **Model Evaluation and Optimization**:  
   - Evaluate model performance using cross-validation.  
   - Fine-tune model hyperparameters and preprocessing techniques for better classification accuracy.  

5. **Visualization**:  
   - Visualize the performance of models using confusion matrices and other metrics.  
   - Generate word clouds or frequency plots to gain insights from the text data.  

## Installation  

### Prerequisites  

- Python 3.12+  
- pip environment  
- Virtual environment for isolated dependencies  

### Running the Notebook  

1. **Clone the repository**:  

   ```bash  
   git clone https://github.com/hasanmd1/Machine_Learning_Projects.git  
   cd NLP_Text_Classification  
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
   Open the Jupyter Notebook `NLP_Text_Classification.ipynb` to explore the project.  

### Running the Flask Application  

You can also interact with this project through a Flask web application, which enables users to upload datasets, train models, and view classification results interactively.  

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

The dataset used for this project is the **20 Newsgroups Dataset**, a collection of approximately 20,000 newsgroup documents, organized into 20 categories. This dataset is widely used for text classification research.  

Access the dataset here:  
[20 Newsgroups Dataset](http://qwone.com/~jason/20Newsgroups/)  

## Usage  

### Text Classification  

Use the notebook to preprocess text, extract features using TF-IDF, and train machine learning models for text classification.  

### Data Preprocessing  

Experiment with different preprocessing techniques (tokenization, stopword removal, lemmatization) to observe their impact on model performance.  

### Flask Integration  

Upload custom datasets, train models, and test the classification performance through the Flask web application.  

## Contributing  

Contributions are not allowed for this project. However, you may open an issue to suggest improvements or new features.  

## License  

This project is licensed under the MIT License. See the LICENSE file for more details.  

## Acknowledgements  

Thanks to the creators of the 20 Newsgroups Dataset and the NLTK and SpaCy libraries for providing the necessary tools to process and classify text effectively.  

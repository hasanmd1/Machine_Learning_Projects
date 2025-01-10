# Chat-Bot Modeling and Training  

This project focuses on building and training a conversational chatbot using modern Natural Language Processing (NLP) techniques. The chatbot is designed to provide dynamic and context-aware responses, leveraging state-of-the-art transformer models such as BERT and GPT. The project also includes sentiment classification to enhance the chatbot's ability to handle user interactions effectively.  

You can run this project as a standalone Jupyter Notebook or explore it interactively through a Flask web application for uploading datasets and evaluating chatbot performance.  

## Features  

### 1. Sentiment Classification  

Analyze user input to identify sentiment and tailor chatbot responses accordingly.  

### 2. Pretrained Transformer Models  

Use cutting-edge transformer architectures like BERT and GPT to generate accurate, context-aware responses.  

### 3. Dynamic Chatbot Training  

Train the chatbot on conversational datasets for improved fluency and relevance in responses.  

### 4. Flask Integration  

Interact with the chatbot through a web application by uploading custom datasets or chatting directly.  

## How Features Are Used  

### **Notebook Structure Summary**  

1. **Data Preprocessing**:  
   - Load and clean the dataset to prepare it for model training.  
   - Tokenize conversations using tools like Hugging Face's tokenizer.  

2. **Sentiment Analysis**:  
   - Train a sentiment classification model to identify positive, negative, or neutral sentiments in user inputs (Feature 1).  
   - Use the sentiment results to adjust the chatbot's tone dynamically.  

3. **Chatbot Training**:  
   - Fine-tune pretrained transformer models (BERT, GPT) on the conversational dataset to generate human-like responses (Feature 2).  

4. **Chatbot Interaction**:  
   - Simulate real-time conversations using the trained chatbot.  
   - Integrate Flask for a web-based interface to interact with the chatbot.  

5. **Evaluation**:  
   - Assess model performance using perplexity, BLEU scores, and other metrics.  
   - Visualize results and chatbot behavior for various conversation scenarios.  

## Installation  

### Prerequisites  

- Python 3.12+  
- pip environment  
- Virtual environment for isolated dependencies  

### Running the Notebook  

1. **Clone the repository**:  

   ```bash  
   git clone https://github.com/hasanmd1/Machine_Learning_Projects.git  
   cd Chat_Bot_Modeling_and_Training  
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
   Open the Jupyter Notebook `Chat_Bot_Modeling_and_Training.ipynb` to explore the project.  

### Running the Flask Application  

Alternatively, you can explore this project using a Flask web application. The app allows you to interact with the chatbot or upload custom datasets to retrain the model.  

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

The dataset used for this project is the **Cornell Movie-Dialogs Corpus**, a rich source of conversational data for training the chatbot. Access the dataset here:  
[Cornell Movie-Dialogs Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)  

## Usage  

### Chatbot Training  

Train the chatbot on the Cornell Movie-Dialogs Corpus or upload your own dataset for custom chatbot responses.  

### Sentiment Analysis  

Enable sentiment classification to provide more empathetic and appropriate responses based on user sentiment.  

### Flask Integration  

Use the web interface to interact with the chatbot, test different conversation scenarios, or retrain the chatbot with uploaded datasets.  

## Contributing  

Contributions are not allowed for this project. However, you may open an issue to suggest improvements or new features.  

## License  

This project is licensed under the MIT License. See the LICENSE file for more details.  

## Acknowledgements  

Thanks to the creators of the Cornell Movie-Dialogs Corpus for providing the dataset and Hugging Face for their powerful NLP tools.  

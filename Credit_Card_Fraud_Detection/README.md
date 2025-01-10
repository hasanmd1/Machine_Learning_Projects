# Credit Card Fraud Detection and Risk Management System  

## Overview  

This project is an advanced fraud detection and risk management system designed to identify fraudulent activities in financial transactions. The system leverages various machine learning techniques, including anomaly detection, time-series analysis, and transfer learning, to provide a robust solution for detecting and mitigating fraud. Additionally, it offers insights into customer behavior, risk scoring, and the potential impact of fraud on customer lifetime value.  

You can run this project independently as a Jupyter Notebook or use the integrated Flask web application for a more interactive experience.  

## Features  

### 1. Anomaly Detection  

The system utilizes advanced anomaly detection algorithms to identify unusual patterns in transaction data, flagging them as potential fraud cases.  

### 2. Transaction Risk Scoring  

Each transaction is assessed and assigned a risk score based on its likelihood of being fraudulent.  

### 3. Time-Series Fraud Detection  

By analyzing transaction data over time, the system can detect fraud that may be hidden within temporal patterns.  

### 4. Customer Segmentation for Fraud Risk  

The system segments customers based on their transaction behaviors and associated fraud risks.  

### 5. Feature Importance and Explainability  

Utilizing machine learning models, the system provides insights into which features (e.g., transaction amount, time, location) are most indicative of fraud.  

### 6. Real-Time Fraud Detection System  

The system is designed to operate in real-time, allowing for immediate detection and response to fraudulent activities.  

### 7. Multi-Label Classification  

In cases where transactions may display multiple types of fraudulent behavior, the system uses multi-label classification techniques to assign multiple fraud categories to a single transaction.  

### 8. Predicting Customer Lifetime Value (CLTV) and Fraud Impact  

The project includes a model for predicting Customer Lifetime Value (CLTV) while assessing the potential impact of fraud on a customer's value to the business.  

### 9. Transfer Learning for Fraud Detection  

To enhance fraud detection performance, the system incorporates transfer learning techniques, leveraging pre-trained models from related tasks.  

## How Features Are Used  

### **Notebook Structure Summary**  

1. **EDA Section**:  
   - Time-Series Fraud Detection (Feature 3)  
   - Customer Segmentation for Fraud Risk (Feature 4)  

2. **Feature Engineering Section**:  
   - Scaling & Transformation  
   - PCA for Dimensionality Reduction  
   - Feature Importance and Explainability (Feature 5)  
   - Transaction Risk Scoring (Feature 2)  

3. **Model Building Section**:  
   - Train-Test Split  
   - Anomaly Detection (Feature 1)  
   - Model Training (RandomForest, etc.)  
   - Multi-Label Classification (Feature 7)  
   - Predicting CLTV and Fraud Impact (Feature 8)  
   - Transfer Learning for Fraud Detection (Feature 9)  

4. **Model Evaluation Section**:  
   - Confusion Matrix & Evaluation Metrics  
   - Real-Time Fraud Detection System (Feature 6)  

## Installation  

### Prerequisites  

- Python 3.12+  
- pip environment  
- Virtual environment to run the project  

### Running the Notebook  

1. **Clone the repository**:  

   ```bash  
   git clone https://github.com/hasanmd1/Machine_Learning_Projects.git  
   cd Credit_Card_Fraud_Detection  
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
   Open the Jupyter Notebook `Credit_Card_Fraud_Detection.ipynb` to explore the project.  

### Running the Flask Application  

Alternatively, you can use the Flask web application for an interactive experience. The Flask app allows you to upload a dataset, train the model, evaluate performance, and use a chatbot for project guidance.  

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

The dataset used for this project consists of anonymous transaction records, including features such as transaction amount, time, customer ID, and more. Refer to the data source documentation for obtaining the dataset:  
[Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)  

## Contributing  

Contributions are not allowed for this project. However, you can open an issue to suggest improvements or new features.  

## License  

This project is licensed under the MIT License. See the `LICENSE.md` file for more details.  

## Acknowledgements  

Special thanks to Kaggle for providing the dataset that informed the development of this system.  

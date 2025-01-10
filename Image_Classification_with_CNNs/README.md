# Image Classification with CNNs  

This project focuses on image classification using deep learning models, specifically Convolutional Neural Networks (CNNs). The system is designed to classify images into various categories using techniques such as transfer learning and data augmentation. By leveraging pre-trained models like ResNet and VGG, the project ensures high accuracy while reducing training time.  

You can run this project as a standalone Jupyter Notebook or interact with it through a Flask web application for dataset uploads, model training, and evaluation.  

## Features  

### 1. Transfer Learning  

Use pre-trained models like ResNet and VGG to enhance classification accuracy and reduce computational costs.  

### 2. Data Augmentation  

Apply techniques such as rotation, flipping, and scaling to increase dataset diversity and improve model robustness.  

### 3. Model Optimization  

Incorporate fine-tuning and hyperparameter optimization to achieve the best classification results.  

### 4. Flask Integration  

Interact with the system via a web application that allows dataset uploads, model training, and testing.  

## How Features Are Used  

### **Notebook Structure Summary**  

1. **Data Preprocessing**:  
   - Load the CIFAR-10 dataset or a custom dataset.  
   - Normalize pixel values and preprocess images for model training.  

2. **Data Augmentation**:  
   - Increase dataset diversity by applying transformations such as rotations, flips, and zooms (Feature 2).  

3. **Model Building**:  
   - **Transfer Learning**: Load pre-trained models like ResNet and VGG with their weights.  
   - Modify the final layers for CIFAR-10 classification tasks (Feature 1).  
   - Implement custom CNN architectures for comparison.  

4. **Training and Fine-Tuning**:  
   - Train the model on augmented datasets.  
   - Fine-tune hyperparameters like learning rate, batch size, and epochs to optimize performance.  

5. **Evaluation and Visualization**:  
   - Evaluate the model using metrics like accuracy, precision, and recall.  
   - Visualize training progress and predictions using confusion matrices and performance graphs.  

## Installation  

### Prerequisites  

- Python 3.12+  
- pip environment  
- Virtual environment for isolated dependencies  

### Running the Notebook  

1. **Clone the repository**:  

   ```bash  
   git clone https://github.com/hasanmd1/Machine_Learning_Projects.git  
   cd Image_Classification_with_CNNs  
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
   Open the Jupyter Notebook `Image_Classification_with_CNNs.ipynb` to explore the project.  

### Running the Flask Application  

Alternatively, you can explore this project using a Flask web application. The app enables dataset uploads, model training, and prediction testing interactively.  

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

The dataset used for this project is the **CIFAR-10 Dataset**, a well-known benchmark dataset for image classification tasks. It contains 60,000 32x32 color images across 10 classes. Access the dataset here:  
[CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)  

## Usage  

### Model Training  

Train custom CNN architectures or fine-tune pre-trained models on the CIFAR-10 dataset.  

### Data Augmentation  

Experiment with various augmentation techniques to observe their impact on model performance.  

### Flask Integration  

Upload custom datasets and test classification performance via the web interface.  

## Contributing  

Contributions are not allowed for this project. However, you may open an issue to suggest improvements or new features.  

## License  

This project is licensed under the MIT License. See the `LICENSE.md` file for more details.  

## Acknowledgements  

Thanks to the creators of the CIFAR-10 dataset and the TensorFlow/Keras community for providing tools to implement deep learning models effectively.  

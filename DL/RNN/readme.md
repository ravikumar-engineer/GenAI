🎬 IMDB Movie Review Sentiment Analysis using Artificial Neural Network (ANN / RNN)
📖 Project Overview

Sentiment analysis plays a crucial role in understanding public opinion from textual data such as movie reviews, social media posts, and product feedback.

This project focuses on predicting whether a movie review is positive or negative using an Artificial Neural Network (Simple RNN) trained on the IMDB Movie Reviews dataset.

The project demonstrates how deep learning models can be used for Natural Language Processing (NLP) tasks.

The project is divided into three major parts:
1.⁠ ⁠Data Preparation & Preprocessing
2.⁠ ⁠Sentiment Classification using Neural Network
3.⁠ ⁠Model Evaluation & Prediction

This solution helps analyze customer opinions and automate sentiment classification effectively.

🧠 Problem Statement

To build a deep learning model that classifies movie reviews as Positive or Negative based on the textual content of the review.

The model learns from:

Word sequences

Review length

Vocabulary frequency

Contextual word order

🏗️ Project Structure
IMDB-Sentiment-Analysis/
│
├── data/
│   └── imdb_dataset (loaded via Keras)
│
├── model/
│   └── simple_rnn_imdb.h5
│
├── notebooks/
│   └── imdb_sentiment_training.ipynb
│
├── imdb_rnn.py
├── requirements.txt
└── README.md

⚙️ Part 1: Data Preparation & Preprocessing

•⁠ ⁠Loading IMDB dataset from Keras
•⁠ ⁠Limiting vocabulary size to top 1000 frequent words
•⁠ ⁠Padding review sequences to fixed length (200 words)
•⁠ ⁠Splitting data into training and testing sets

🧠 Part 2: Sentiment Classification using Neural Network

•⁠ ⁠Building a Simple RNN-based Neural Network
•⁠ ⁠Model Architecture:

Embedding Layer

Simple RNN Layer

Dense Output Layer (Binary Classification)
•⁠ ⁠Activation Functions:

tanh for RNN

sigmoid for output
•⁠ ⁠Loss Function: Binary Crossentropy
•⁠ ⁠Optimizer: Adam
•⁠ ⁠Early Stopping to prevent overfitting

📊 Part 3: Model Evaluation & Prediction

•⁠ ⁠Evaluation on unseen test data
•⁠ ⁠Visualization of:

Training vs Validation Accuracy

Training vs Validation Loss
•⁠ ⁠Saving trained model for reuse
•⁠ ⁠Predicting sentiment for new movie reviews

Prediction Output:

Positive → Review sentiment is positive

Negative → Review sentiment is negative

🛠️ Tech Stack

•⁠ ⁠Programming Language: Python
•⁠ ⁠Libraries & Frameworks:

NumPy

Matplotlib

TensorFlow / Keras
•⁠ ⁠Model Type: Artificial Neural Network (Simple RNN)
•⁠ ⁠IDE & Tools: VS Code, Jupyter Notebook
•⁠ ⁠Version Control: Git & GitHub

📊 Dataset

•⁠ ⁠IMDB Movie Review Dataset (Keras Built-in)
•⁠ ⁠50,000 total reviews
•⁠ ⁠Binary sentiment labels:

1 → Positive Review

0 → Negative Review

▶️ How to Run the Project
Step 1: Clone the Repository
git clone https://github.com/ravikumar-engineer/imdb-sentiment-rnn.git

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Run the Script
python imdb_rnn.py

📌 Future Enhancements

•⁠ ⁠Replace SimpleRNN with LSTM / GRU for better performance
•⁠ ⁠Increase vocabulary size
•⁠ ⁠Add Dropout layers
•⁠ ⁠Deploy model using Streamlit
•⁠ ⁠Compare ANN with traditional ML models

👤 Author

Ravi Kumar
Tech Enthusiast | Love Coding in JavaScript & Python |
Web Developer | Graphic Designer | Data Structures & Algorithms

⭐ Acknowledgement

Thanks to Keras, TensorFlow, and the IMDB open dataset for making this project possible.

🤝 Connect With Me

👤 Ravi Kumar
📞 Contact: +91-9199992833
🔗 LinkedIn: https://www.linkedin.com/in/ravi-kumar-b82815258

📧 Email: ravi10kumar0803@gmail.com
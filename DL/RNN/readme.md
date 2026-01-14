🎬 IMDB Movie Review Sentiment Analysis using Simple RNN

This project demonstrates binary sentiment classification (Positive / Negative) on the IMDB movie reviews dataset using a Simple Recurrent Neural Network (RNN) built with TensorFlow & Keras.

📌 Project Overview

Dataset: IMDB Movie Reviews (built-in Keras dataset)

Task: Sentiment Analysis (Positive / Negative)

Model Used: Simple RNN

Framework: TensorFlow (Keras API)

Evaluation Metric: Accuracy

Output: Trained model + sentiment prediction

📂 Dataset Details

Total reviews: 50,000

Training samples: 40,000

Testing samples: 10,000

Each review is encoded as a sequence of integers

Vocabulary size limited to 1,000 most frequent words

Reviews are padded to a maximum length of 200 words

🧠 Model Architecture
Embedding Layer (1000 → 128)
        ↓
SimpleRNN (128 units, tanh activation)
        ↓
Dense Layer (1 unit, sigmoid activation)

Why Simple RNN?

Suitable for sequential data

Learns word order and temporal dependencies

Simple to understand for beginners

⚙️ Installation & Requirements

Make sure you have Python 3.8+ installed.

pip install tensorflow numpy matplotlib

▶️ How to Run the Project

Clone or download the project

Open the Python file in Jupyter Notebook or VS Code

Run the script:

python simple_rnn_imdb.py

📊 Training Details

Optimizer: Adam

Loss Function: Binary Crossentropy

Batch Size: 32

Epochs: 15

Early Stopping used to prevent overfitting

Validation Split: 20%

📈 Performance Visualization

The project plots:

Training vs Validation Accuracy

Training vs Validation Loss

These plots help identify overfitting or underfitting.

🧪 Model Evaluation

After training:

Model is saved as simple_rnn_imdb.h5

Loaded again for evaluation

Tested on unseen test data

Displays test accuracy and loss

🔮 Sample Prediction

The model predicts sentiment for a sample movie review:

Output > 0.5 → Positive

Output ≤ 0.5 → Negative

Example:

Predicted Sentiment: Positive
Actual Label: Positive

📁 Saved Model
simple_rnn_imdb.h5


This file contains the trained Simple RNN model and can be reused without retraining.

🚀 Future Improvements

Replace SimpleRNN with LSTM or GRU

Increase vocabulary size

Add Dropout for better generalization

Use pre-trained word embeddings (GloVe)

🧑‍🎓 Author

Ravi bhaiya
Student – Deep Learning & NLP Enthusiast

📜 License

This project is for educational purposes only.
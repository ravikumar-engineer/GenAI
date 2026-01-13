import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle
import pandas as pd
import numpy as np

# Load model
model = load_model('model.h5')

# Load encoders & scaler
with open('onehot_encoder_geo.pkl', 'rb') as file:
    label_encoder_geo = pickle.load(file)

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Input data
input_data = {
    'CreditScore': 700,
    'Geography': 'France',
    'Gender': 'Female',
    'Age': 28,
    'Tenure': 4,
    'Balance': 80000,
    'NumOfProducts': 2,
    'HasCrCard': 1,
    'IsActiveMember': 1,
    'EstimatedSalary': 50000
}

input_df = pd.DataFrame([input_data])

# Encode Gender
input_df['Gender'] = label_encoder_gender.transform(input_df['Gender'])

# One-hot encode Geography
geo_encoded = label_encoder_geo.transform(
    pd.DataFrame(input_df[['Geography']])
)

geo_encoded_df = pd.DataFrame(
    geo_encoded.toarray(),
    columns=label_encoder_geo.get_feature_names_out(['Geography'])
)

# Combine data
input_df = pd.concat(
    [input_df.drop('Geography', axis=1), geo_encoded_df],
    axis=1
)

# Scale input
input_scaled = scaler.transform(input_df)

# Prediction
prediction = model.predict(input_scaled)
prediction_proba = prediction[0][0]

if prediction_proba > 0.5:
    print('The customer is likely to churn')
else:
    print('The customer is not likely to churn')

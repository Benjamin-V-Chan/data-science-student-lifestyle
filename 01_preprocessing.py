import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def preprocess_data(input_path, output_path):
    # Load dataset
    data = pd.read_csv(input_path)

    # Check for missing values
    if data.isnull().sum().any():
        print("Handling missing values...")
        data.fillna(data.mean(), inplace=True)

    # Normalize numeric features
    numeric_features = data.select_dtypes(include=['float64']).columns
    scaler = StandardScaler()
    data[numeric_features] = scaler.fit_transform(data[numeric_features])

    # Encode categorical features
    if 'Stress_Level' in data.columns:
        encoder = LabelEncoder()
        data['Stress_Level'] = encoder.fit_transform(data['Stress_Level'])

    # Save processed data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data('data/student_lifestyle_dataset.csv', 'data/processed/preprocessed_data.csv')
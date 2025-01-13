import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

def feature_modeling(input_path, output_folder):
    # Load preprocessed data
    data = pd.read_csv(input_path)

    # Features and target
    X = data.drop(columns=['GPA', 'Student_ID'])
    y = data['GPA']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Model Performance:\nMSE: {mse:.4f}\nR^2: {r2:.4f}")

    # Save metrics
    os.makedirs(output_folder, exist_ok=True)
    with open(f"{output_folder}/model_metrics.txt", 'w') as f:
        f.write(f"MSE: {mse:.4f}\nR^2: {r2:.4f}\n")

if __name__ == "__main__":
    feature_modeling('data/processed/preprocessed_data.csv', 'outputs')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def exploratory_analysis(input_path, output_folder):
    # Load preprocessed data
    data = pd.read_csv(input_path)

    # Summary statistics
    print(data.describe())

    # Visualizations
    os.makedirs(output_folder, exist_ok=True)

    # Distribution of GPA
    plt.figure()
    sns.histplot(data['GPA'], kde=True)
    plt.title('Distribution of GPA')
    plt.savefig(f"{output_folder}/gpa_distribution.png")

    # Pairplot of numeric features
    plt.figure()
    sns.pairplot(data.select_dtypes(include=['float64']))
    plt.savefig(f"{output_folder}/pairplot.png")

    print(f"Visualizations saved to {output_folder}")

if __name__ == "__main__":
    exploratory_analysis('data/processed/preprocessed_data.csv', 'outputs')
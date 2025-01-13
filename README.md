# data-science-student-lifestyle

## Project Overview
This project analyzes the impact of various lifestyle factors on students' GPA and stress levels using the Student Lifestyle Dataset. The workflow includes data preprocessing, exploratory data analysis, and predictive modeling to uncover insights about the relationships between daily habits and academic performance.

---

## Project Structure
The project is organized as follows:

```
project-root/
├── data/
│   ├── student_lifestyle_dataset.csv      # Original dataset
│   ├── processed/
│       └── preprocessed_data.csv          # Preprocessed dataset
├── scripts/
│   ├── 01_preprocess_data.py             # Data preprocessing script
│   ├── 02_exploratory_analysis.py        # Exploratory analysis script
│   ├── 03_feature_modeling.py            # Modeling and prediction script
├── outputs/
│   ├── gpa_distribution.png              # GPA distribution visualization
│   ├── pairplot.png                      # Pairplot of features
│   ├── model_metrics.txt                 # Model performance metrics
└── README.md                              # Project documentation
```

---

## Setup and Usage
### Prerequisites
- Python 3.8 or higher
- Required libraries (listed in `requirements.txt`):
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn

### Steps to Run
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd project-root
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the original dataset in the `data/` directory.

4. Run the scripts in sequence:

   **Data Preprocessing:**
   ```bash
   python scripts/01_preprocess_data.py
   ```

   **Exploratory Analysis:**
   ```bash
   python scripts/02_exploratory_analysis.py
   ```

   **Feature Modeling:**
   ```bash
   python scripts/03_feature_modeling.py
   ```

5. Check the `outputs/` folder for visualizations and model evaluation results.

---

## Acknowledgments
**Dataset Author:** Sumit Kumar
**Source:** [Kaggle Dataset - Student Lifestyle Dataset](https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset)
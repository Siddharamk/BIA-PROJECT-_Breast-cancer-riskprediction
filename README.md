# Breast Cancer Prediction System

A machine learning-powered web application that predicts breast cancer malignancy based on diagnostic features. This project uses a pre-trained model to provide accurate predictions through an intuitive user interface.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [Dataset](#dataset)
- [Evaluation Metrics](#evaluation-metrics)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Overview

This web application is designed to assist in the early detection of breast cancer by analyzing various diagnostic features. Users can input key measurements, and the system will predict whether the cancer is malignant or benign using a pre-trained machine learning model.

## Features

- **User-Friendly Interface**: Intuitive sidebar navigation with a modern design
- **Real-Time Predictions**: Get instant results based on input parameters
- **Visual Design**: Professional background with consistent styling
- **Comprehensive Input Fields**: Supports all key diagnostic features
- **Responsive Layout**: Optimized for various screen sizes

## Installation

1. Clone this repository to your local machine
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:

```bash
streamlit run app.py
```

2. The application will open in your default web browser
3. Navigate to the "Breast Cancer Prediction" page from the sidebar
4. Fill in all the required input fields with the diagnostic measurements
5. The system will automatically calculate and display the prediction

## Model Information

The prediction model used in this application is a trained machine learning classifier. Key details:

- **Model Type**: Pre-trained scikit-learn model
- **Training Data**: Breast Cancer Wisconsin (Diagnostic) Dataset
- **Features Used**: 10 key diagnostic measurements (radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, fractal dimension)
- **Model File**: `brest_cancer.pkl`

## Dataset

The model is trained on the [Breast Cancer Wisconsin (Diagnostic) Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29) from the UCI Machine Learning Repository. This dataset contains 569 instances with 30 numeric features.

### Key Features:

- **Radius Mean**: Mean of distances from center to points on the perimeter
- **Texture Mean**: Standard deviation of gray-scale values
- **Perimeter Mean**: Mean size of the core tumor
- **Area Mean**: Mean area of the tumor
- **Smoothness Mean**: Mean of local variation in radius lengths
- **Compactness Mean**: Mean of perimeter² / area - 1.0
- **Concavity Mean**: Mean of severity of concave portions of the contour
- **Concave Points Mean**: Mean number of concave portions of the contour
- **Symmetry Mean**: Mean symmetry of the tumor
- **Fractal Dimension Mean**: Mean "coastline approximation" - 1

## Evaluation Metrics

The model's performance has been evaluated using standard classification metrics. Detailed evaluation results and visualizations can be found in the Jupyter Notebook.

## Project Structure

```
BIA.Project/
├── app.py                 # Main Streamlit application
├── requirement.txt        # Project dependencies
├── notebook.ipynb         # Data analysis and model training notebook
├── breast_cancer.pkl      # Trained model file
├── Breast_cancer_dataset.csv  # Original dataset
├── feature_names.pkl      # Feature names for the model
└── README.md              # This file
```

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Joblib**: Model serialization and deserialization
- **scikit-learn**: Machine learning library
- **streamlit-option-menu**: Custom sidebar menu
- **base64**: Image encoding for background

## Future Improvements

- Add more detailed feature explanations
- Implement model interpretability visualizations
- Add historical prediction tracking
- Improve mobile responsiveness
- Add support for file upload of diagnostic data

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The dataset is provided by the UCI Machine Learning Repository
- Special thanks to the contributors of the scikit-learn library

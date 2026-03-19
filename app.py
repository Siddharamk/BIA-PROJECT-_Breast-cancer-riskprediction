import streamlit as st
import pandas as pd
import joblib
import base64
from streamlit_option_menu import option_menu

def add_bg_from_local(image_file):
    with open('/Users/siddharamkothane/BIA.Project /logo.png', "rb") as f:   
        data = f.read()
    b64_encoded = base64.b64encode(data).decode()  
    background_style = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{b64_encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

add_bg_from_local("/Users/siddharamkothane/BIA.Project /logo.png")

def set_input_label_styles():
    """
    Sets consistent styling for input field labels in the Streamlit app.
    
    This function ensures all input labels are clearly visible with proper
    contrast against the background, following accessibility guidelines.
    The styling is optimized for maintainability and compatibility with
    Streamlit's dynamic class structure.
    """
    st.markdown("""
        <style>
        /* CSS variables for consistent theming and easy updates */
        :root {
            --input-label-color: #2d3748; /* Slate gray - improves readability on light backgrounds */
            --input-label-font-weight: 500;
        }
        
        /* Target all input labels with specific Streamlit selectors */
        /* Using data-testid and class selectors for better reliability */
        [data-testid="stNumberInput"] label,
        [data-testid="stSelectbox"] label,
        [data-testid="stTextInput"] label,
        [data-testid="stSlider"] label {
            color: var(--input-label-color) !important;
            font-weight: var(--input-label-font-weight);
        }
        
        /* Additional fallback for other input types */
        .stInput label {
            color: var(--input-label-color) !important;
            font-weight: var(--input-label-font-weight);
        }
        </style>
    """, unsafe_allow_html=True)

# Apply input label styles
set_input_label_styles()

## Load the pre-trained model
cancer_model = joblib.load("/Users/siddharamkothane/BIA.Project /brest_cancer.pkl")

# sidebar for navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Breast Cancer Prediction System",
        options=["Home", "Breast Cancer Prediction",],
        icons=["house", "activity", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# Cancer Prediction page
if selected == "Breast Cancer Prediction":
    st.markdown("<h1 style='color:black;'>Breast Cancer Prediction</h1>", unsafe_allow_html=True)

    st.write("Please enter the following details to predict whether the breast cancer is malignant or benign:")
     # Input fields
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        radius_mean = st.number_input("Radius Mean", 0.0, 100.0, 14.0)
    with col2:
        texture_mean = st.number_input("Texture Mean", 0.0, 100.0, 20.0)
    with col3:
        perimeter_mean = st.number_input("Perimeter Mean", 0.0, 200.0, 90.0)
    with col4:
        area_mean = st.number_input("Area Mean", 0.0, 2000.0, 600.0)
    with col1:
        smoothness_mean = st.number_input("Smoothness Mean", 0.0, 1.0, 0.1)
    with col2:
        compactness_mean = st.number_input("Compactness Mean", 0.0, 1.0, 0.1)
    with col3:
        concavity_mean = st.number_input("Concavity Mean", 0.0, 1.0, 0.1)
    with col4:
        concave_points_mean = st.number_input("Concave Points Mean", 0.0, 1.0, 0.05)
    with col1:
        symmetry_mean = st.number_input("Symmetry Mean", 0.0, 1.0, 0.2)
    with col2:
        fractal_dimension_mean = st.number_input("Fractal Dimension Mean", 0.0, 1.0, 0.06)
    with col3:
        radius_error = st.number_input("Radius Error", 0.0, 5.0, 0.5)
    with col4:
        texture_error = st.number_input("Texture Error", 0.0, 5.0, 1.0)
    with col1:
        perimeter_error = st.number_input("Perimeter Error", 0.0, 20.0, 3.0)
    with col2:
        area_error = st.number_input("Area Error", 0.0, 200.0, 40.0)
    with col3:
        smoothness_error = st.number_input("Smoothness Error", 0.0, 0.1, 0.005)
    with col4:
        compactness_error = st.number_input("Compactness Error", 0.0, 0.5, 0.02)
    with col1:
        concavity_error = st.number_input("Concavity Error", 0.0, 0.5, 0.01)
    with col2:
        concave_points_error = st.number_input("Concave Points Error", 0.0, 0.1, 0.005)
    with col3:
        symmetry_error = st.number_input("Symmetry Error", 0.0, 0.5, 0.02)
    with col4:
        fractal_dimension_error = st.number_input("Fractal Dimension Error", 0.0, 0.1, 0.003)
    with col1:
        worst_radius = st.number_input("Worst Radius", 0.0, 100.0, 16.0)
    with col2:
        worst_texture = st.number_input("Worst Texture", 0.0, 100.0, 25.0)

    # Prediction code
    cancer_diagnosis = ''

    if st.button("Predict"):
        prediction = cancer_model.predict([[
            radius_mean, texture_mean, perimeter_mean, area_mean,
            smoothness_mean, compactness_mean, concavity_mean,
            concave_points_mean, symmetry_mean, fractal_dimension_mean,
            radius_error, texture_error, perimeter_error, area_error,
            smoothness_error, compactness_error, concavity_error, concave_points_error,
            symmetry_error, fractal_dimension_error, worst_radius, worst_texture
        ]])

        if prediction[0] == 1:
            cancer_diagnosis = "The breast cancer is Malignant"
        else:
            cancer_diagnosis = "The breast cancer is Benign"

   

    if cancer_diagnosis:
        col1 = st.columns(1)
        with col1[0]:
            color = "red" if "Malignant" in cancer_diagnosis else "green"
            st.markdown(f"<h2 style='color:{color};'>{cancer_diagnosis}</h2>", unsafe_allow_html=True)
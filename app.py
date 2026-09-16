import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Alzheimer's Disease Prediction",
    page_icon="🧠",
    layout="wide"
)


# --------------------------------------------------
# Load Model and Features
# --------------------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load("model/random_forest_model.pkl")
    selected_features = joblib.load("model/selected_features.pkl")
    return model, selected_features


model, selected_features = load_model()


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🧠 Alzheimer's Disease Classification")

st.write(
    "This application uses a Machine Learning model to classify "
    "whether the provided patient data indicates a predicted "
    "diagnosis or no diagnosis."
)

st.warning(
    "⚠️ This application is for educational and research purposes only. "
    "It is not a medical diagnosis or a substitute for professional medical advice."
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Prediction",
        "Model Information",
        "About Project"
    ]
)


# --------------------------------------------------
# Prediction Page
# --------------------------------------------------

if page == "Prediction":

    st.header("🔍 Alzheimer's Disease Prediction")

    st.write(
        "Enter the required values below and click "
        "**Predict** to generate a model prediction."
    )

    col1, col2 = st.columns(2)

    with col1:

        functional_assessment = st.number_input(
            "Functional Assessment",
            min_value=0.0,
            max_value=10.0,
            value=5.0,
            step=0.1
        )

        adl = st.number_input(
            "ADL",
            min_value=0.0,
            max_value=10.0,
            value=6.0,
            step=0.1
        )

        mmse = st.number_input(
            "MMSE",
            min_value=0.0,
            max_value=30.0,
            value=20.0,
            step=0.1
        )

        memory_complaints = st.selectbox(
            "Memory Complaints",
            [0, 1]
        )

        behavioral_problems = st.selectbox(
            "Behavioral Problems",
            [0, 1]
        )

    with col2:

        diet_quality = st.number_input(
            "Diet Quality",
            min_value=0.0,
            max_value=10.0,
            value=7.0,
            step=0.1
        )

        cholesterol_triglycerides = st.number_input(
            "Cholesterol Triglycerides",
            min_value=0.0,
            max_value=500.0,
            value=150.0,
            step=0.1
        )

        cholesterol_hdl = st.number_input(
            "Cholesterol HDL",
            min_value=0.0,
            max_value=150.0,
            value=50.0,
            step=0.1
        )

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=100.0,
            value=24.0,
            step=0.1
        )

        cholesterol_ldl = st.number_input(
            "Cholesterol LDL",
            min_value=0.0,
            max_value=300.0,
            value=100.0,
            step=0.1
        )


    # --------------------------------------------------
    # Prediction Button
    # --------------------------------------------------

    if st.button("🔮 Predict", use_container_width=True):

        input_data = pd.DataFrame(
            [[
                functional_assessment,
                adl,
                mmse,
                memory_complaints,
                behavioral_problems,
                diet_quality,
                cholesterol_triglycerides,
                cholesterol_hdl,
                bmi,
                cholesterol_ldl
            ]],
            columns=selected_features
        )

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        st.divider()

        if prediction == 1:

            st.error("⚠️ Model Prediction: Diagnosis")

        else:

            st.success("✅ Model Prediction: No Diagnosis")

        st.metric(
            "Diagnosis Probability",
            f"{probability * 100:.2f}%"
        )

        st.info(
            "The probability shown is the Random Forest model's "
            "estimated probability for the Diagnosis class."
        )


# --------------------------------------------------
# Model Information
# --------------------------------------------------

elif page == "Model Information":

    st.header("🤖 Model Information")

    st.write(
        "The project evaluated five classification algorithms "
        "using the same training and testing dataset."
    )

    results = pd.DataFrame({
        "Model": [
            "Random Forest",
            "Decision Tree",
            "SVM",
            "KNN",
            "Logistic Regression"
        ],

        "Accuracy": [
            0.9512,
            0.9465,
            0.8698,
            0.8372,
            0.8163
        ],

        "Precision": [
            0.9456,
            0.9329,
            0.8243,
            0.7770,
            0.7386
        ],

        "Recall": [
            0.9145,
            0.9145,
            0.8026,
            0.7566,
            0.7434
        ],

        "F1-Score": [
            0.9298,
            0.9236,
            0.8133,
            0.7667,
            0.7410
        ],

        "ROC-AUC": [
            0.9415,
            0.9362,
            0.9249,
            0.8914,
            0.8894
        ]
    })

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Selected Features")

    for feature in selected_features:
        st.write(f"• {feature}")

    st.subheader("Final Model")

    st.write(
        "Random Forest Classifier was used as the final deployed model."
    )

    st.write(
        "Test-set accuracy: **95.12%**"
    )


# --------------------------------------------------
# About Project
# --------------------------------------------------

elif page == "About Project":

    st.header("📊 About the Project")

    st.write("""
    ### Alzheimer's Disease Classification

    This project applies machine learning techniques to classify
    Alzheimer's disease diagnosis using selected patient-related
    features.

    ### Project Workflow

    1. Data Collection
    2. Data Inspection
    3. Missing Value Analysis
    4. Data Cleaning
    5. Exploratory Data Analysis
    6. Correlation Analysis
    7. Feature Selection
    8. Train-Test Split
    9. Model Building
    10. Model Comparison
    11. Final Model Evaluation
    12. Model Saving
    13. Streamlit Deployment

    ### Models Evaluated

    • Logistic Regression  
    • Decision Tree  
    • Random Forest  
    • K-Nearest Neighbors  
    • Support Vector Machine
    """)

    st.info(
        "This project is intended for academic and educational purposes."
    )
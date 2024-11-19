import streamlit as st
import asyncio
import aiohttp
import nest_asyncio
import pandas as pd
import joblib
from bulk_url_processor import URLFeatureExtractor
from deployment_pipeline import MLModelPipeline
from sklearn.ensemble import RandomForestClassifier

# Apply nest_asyncio to allow for re-entrance in the event loop in Streamlit
nest_asyncio.apply()

# Load the trained pipeline
@st.cache(allow_output_mutation=True)
def load_model():
    # Load the trained Random Forest pipeline using the relative path
    deployment_model = MLModelPipeline(model=RandomForestClassifier())
    model_path = "data/models/Random Forest_deployment.joblib"
    deployment_model.load_pipeline(model_path)
    return deployment_model

# Helper function to extract features for a single URL
def extract_features(url, ref_urls):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    async def extract():
        async with aiohttp.ClientSession() as session:
            extractor = URLFeatureExtractor(
                url=url,
                ref_urls_csv=ref_urls,
                session=session,
                perform_live_check=False  # Disable live check for initial tests
            )
            return await extractor.extract_all_features()
    
    features = loop.run_until_complete(extract())
    return features

# Main Streamlit app
def main():
    st.title("Phishing URL Detection with Feature Extraction")
    st.write("Enter a URL to determine if it is likely to be benign or malicious.")

    # Single-line text input to accept one URL
    user_url = st.text_input("Enter a URL:")

    # Predict button
    if st.button("Predict"):
        if user_url.strip():
            # Extract features for the URL
            ref_urls = []  # Replace with the actual list or path to CSV containing reference URLs
            try:
                features = extract_features(user_url, ref_urls)

                if features:
                    # Convert the features dictionary to a DataFrame
                    features_df = pd.DataFrame([features])
                    
                    # Fill missing values after feature extraction
                    features_df.fillna(0, inplace=True)

                    # Load the model and predict
                    model_pipeline = load_model()
                    predictions = model_pipeline.predict(features_df)
                    # Map the predictions to 'benign' and 'malignant'
                    predictions_mapped = ['benign' if pred == 0 else 'malignant' for pred in predictions]

                    # Display result
                    st.write(f"Prediction for {user_url}: **{predictions_mapped[0]}**")
                    st.write(f"Model Prediction (Raw): {predictions[0]}")

                    # If probabilistic predictions are required
                    if hasattr(model_pipeline.best_pipeline.named_steps['classifier'], 'predict_proba'):
                        prob_predictions = model_pipeline.predict_proba(features_df)
                        st.write(f"Probabilities (Benign, Malignant): (Benign: {prob_predictions[0][0]:.2f}, Malignant: {prob_predictions[0][1]:.2f})")
                else:
                    st.error("Failed to extract features from the URL.")
            except Exception as e:
                st.error(f"Error occurred while making predictions: {e}")
        else:
            st.warning("Please enter a URL to predict.")

if __name__ == "__main__":
    main()

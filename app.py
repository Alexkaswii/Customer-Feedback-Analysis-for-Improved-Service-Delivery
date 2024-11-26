# app.py

import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd

def clean_review(text):
    return text.lower()

def predict_sentiment(text, vectorizer, model):
    try:
        processed_text = clean_review(text)
        vectorized_text = vectorizer.transform([processed_text])
        prediction = model.predict(vectorized_text)
        return prediction[0]
    except Exception as e:
        print(f"Error in predict_sentiment: {e}")
        return None

def main():
    """Creates a Streamlit app for sentiment analysis"""
    st.title("Sentiment Analysis App")
    
    user_input = st.text_input("Enter your comment here")

    if st.button("Analyze Sentiment"):
        if user_input:
            prediction = predict_sentiment(user_input, vectorizer, model)
            
            if prediction is None:
                st.error("Failed to make prediction. Please check your input.")
            else:
                sentiment_dict = {
                    0: "Negative",
                    1: "Neutral",
                    2: "Positive"
                }
                
                if prediction in sentiment_dict:
                    sentiment = sentiment_dict[prediction]
                    st.write(f"Predicted Sentiment: {sentiment}")
                else:
                    
                    st.warning(f"Unexpected prediction value: {prediction}. Please check your model output.")
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    try:
        with open('vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        
        with open('sentiment_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        main()
    except FileNotFoundError:
        st.error("Model files not found. Please ensure 'vectorizer.pkl' and 'sentiment_model.pkl' are in the same directory.")
        st.stop()
python -m streamlit run app.py
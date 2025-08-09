import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import streamlit as st

@st.cache_resource
def load_model():
    data = pd.read_csv('youtube_comments.csv')

    model = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', LogisticRegression())
    ])

    model.fit(data['comment'], data['label'])
    return model

model = load_model()
st.title("Youtube comment classifier")
st.write("Classify your comment as Toxic or supportive")

user_input = st.text_area("Enter a youtube comment")

if user_input:
    prediction = model.predict([user_input])[0]
    
    if prediction == "toxic":
        st.error("This comment is likely **Toxic**")
    else:
        st.success("This comment is **Supportive**")

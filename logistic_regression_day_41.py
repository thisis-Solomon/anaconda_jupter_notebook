import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv('youtube_comments.csv')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['comment'], data['label'], test_size=0.2, random_state=42)

# Create pipeline

model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

# Train model
model.fit(X_train, y_train)
acc = model.score(X_test, y_test)
print(f"Accuracy: {round(acc*100,2)}% for the model trained")

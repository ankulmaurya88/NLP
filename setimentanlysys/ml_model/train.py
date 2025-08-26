import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

def train_and_save():
    # Example training
    df = pd.read_csv("data/sample_data.csv")  # text, label
    X, y = df["text"], df["label"]

    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vec, y)

    joblib.dump((vectorizer, model), "ml_model/model.pkl")
    print("✅ Model saved at ml_model/model.pkl")

if __name__ == "__main__":
    train_and_save()

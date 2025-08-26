import joblib
from .preprocessing import clean_text

def load_model(path="ml_model/model.pkl"):
    try:
        return joblib.load(path)
    except:
        return None   # fallback for dummy

def predict(model, text: str):
    if model:
        return model.predict([clean_text(text)])[0]
    else:
        # Dummy sentiment (for backend wiring)
        if "good" in text.lower():
            return "positive"
        elif "bad" in text.lower():
            return "negative"
        return "neutral"

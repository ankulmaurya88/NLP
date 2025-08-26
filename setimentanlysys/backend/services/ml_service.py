from ml_model.predict import load_model, predict
# from backend.services import ml_service

# Load model once when service starts
model = load_model()

def predict_sentiment(text: str):
    return predict(model, text)

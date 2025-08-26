from fastapi import APIRouter
from backend.services.ml_service import predict_sentiment


router = APIRouter(prefix="/sentiment", tags=["Sentiment"])

@router.post("/predict")
def predict(text: str):
    result = predict_sentiment(text)
    return {"text": text, "sentiment": result}

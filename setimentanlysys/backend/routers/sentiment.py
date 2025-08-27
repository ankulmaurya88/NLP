from fastapi import APIRouter
from backend.services.ml_service import predict_sentiment


from pydantic import BaseModel

router = APIRouter(prefix="/sentiment", tags=["Sentiment"])

class SentimentRequest(BaseModel):
    text: str

@router.post("/predict")
def predict(data: SentimentRequest):
    result = predict_sentiment(data.text)
    return {"text":data.text, "sentiment": result}

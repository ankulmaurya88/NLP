from fastapi import FastAPI

from backend.routers import sentiment

app = FastAPI(title="Sentiment Analysis API")

app.include_router(sentiment.router)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

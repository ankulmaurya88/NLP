from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import sentiment

app = FastAPI(title="Sentiment Analysis API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # or list your frontend domains
    allow_credentials=True,
    allow_methods=["*"],       # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

app.include_router(sentiment.router)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

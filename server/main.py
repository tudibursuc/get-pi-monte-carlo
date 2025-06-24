from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# Optional CORS middleware for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PointsRequest(BaseModel):
    n: int
    
@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/generate-points")
def generate_points(data: PointsRequest):
    points = [[random.random(), random.random()] for _ in range(data.n)]
    return {"points": points}

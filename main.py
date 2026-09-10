
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def seed_collection():
    return {"Response": "Welcome!"}


@app.get("/seed/collection/{collectionName}")
def seed_collection(collectionName : str):
    with open(f"collections/{collectionName}.json", "r") as f:
        return json.loads(f.read())

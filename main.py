
import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def seed_collection():
    return {"Response": "Welcome!"}


@app.get("/seed/collection/{collectionName}")
def seed_collection(collectionName : str):
    with open(f"collections/{collectionName}.json", "r") as f:
        return json.loads(f.read())

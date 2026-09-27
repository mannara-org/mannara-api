
from pydantic import ValidationError

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from mannara_api.schema import SeedCollection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/seed/collection/{collectionName}")
def seed_collection(collectionName : str) -> SeedCollection :
    with open(f"collections/{collectionName}.json", "r") as f:
        try:
            return SeedCollection.model_validate_json(f.read())
        except ValidationError as e:
            print("Pydantic validation error!\n", e)
            raise HTTPException(status_code=500)


@app.get("/search/university_programs")
def search_uni_programs(_: str = "test"):
    pass


import json
from typing import Any
from pydantic import BaseModel

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


class Meta(BaseModel):
    collectionName: str
    aggregated: bool
    aggregatedBy: dict[str, object] | None


class SeedCollection(BaseModel):
    meta: Meta
    data: list[object] | dict[str, object]


@app.get("/seed/collection/{collectionName}")
def seed_collection(collectionName : str) -> SeedCollection :
    with open(f"collections/{collectionName}.json", "r") as f:
        return SeedCollection.model_validate_json(f.read())

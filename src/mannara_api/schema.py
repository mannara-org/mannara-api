

from pydantic import BaseModel

# from mannara_api.models import Model

class Aggregator(BaseModel):
    model: str
    field: str


class Meta(BaseModel):
    collectionName: str
    aggregated: bool
    aggregatedBy: Aggregator | None


class SeedCollection(BaseModel):
    meta: Meta
    # data: list[Model] | dict[str, list[Model]]

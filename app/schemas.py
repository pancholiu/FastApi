from random import randint
from pydantic import BaseModel, Field


def random_destination():
    return randint(11000, 12000)


class Shipment(BaseModel):
    content: str = Field(description="What's inside", max_length=30)
    weight: float = Field(description="Measured in kg", le=25, ge=1)
    destination: int | None = Field(
        description="Zip code", default_factory=random_destination)

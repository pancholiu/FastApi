from random import randint
from pydantic import BaseModel, Field
from app.database.models import ShipmentStatus


def random_destination():
    return randint(11000, 12000)


class BaseShipment(BaseModel):
    content: str | None = None
    weight: (float | None) = Field(le=25, default=None)
    destination: int | None = None


class ShipmentRead(BaseShipment):
    status: ShipmentStatus


class ShipmentCreate(BaseShipment):
    pass


class ShipmentUpdate(BaseModel):
    status: ShipmentStatus

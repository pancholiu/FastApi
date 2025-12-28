from datetime import datetime
from random import randint

from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from app.database.models import ShipmentStatus


def random_destination():
    return randint(11000, 12000)


class BaseShipment(SQLModel):
    content: str | None = None
    weight: (float | None) = Field(le=25, default=None)
    destination: int | None = None


class Shipment(BaseShipment, table=True):
    id: int = Field(default=None, primary_key=True)
    status: ShipmentStatus
    estimated_delivery: datetime


class ShipmentCreate(BaseShipment):
    pass


class ShipmentUpdate(BaseModel):
    status: ShipmentStatus | None = Field(default=None)
    estimated_delivery: datetime | None = Field(default=None)

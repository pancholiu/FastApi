from datetime import datetime, timedelta
from typing import Any

from app.api.schemas.shipment import ShipmentCreate, ShipmentUpdate
from app.services.shipment import ShipmentService
from app.database.models import Shipment, ShipmentStatus
from app.database.session import SessionDep
from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/shipment", response_model=Shipment)
async def get_shipment(id: int, session: SessionDep):
    shipment = ShipmentService(session).get(id)

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Given {id} doesn't exist"
        )

    return shipment


@router.post("/shipment")
async def submit_shipment(shipment: ShipmentCreate, session: SessionDep) -> Shipment:
    return await ShipmentService(session).add(shipment)


@router.patch("/shipment", response_model=Shipment)
async def update_shipment(id: int, shipment_update: ShipmentUpdate, session: SessionDep):
    update = shipment_update.model_dump(exclude_none=True)

    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data provided to update"
        )

    return await ShipmentService(session).update(shipment_update)


@router.delete("/shipment")
async def delete_shipment(id: int, session: SessionDep) -> dict[str, str]:
    await ShipmentService(session).delete(id)

    return {
        "detail": f"Shipment {id} has been deleted"
    }

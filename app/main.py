from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from sqlmodel import Session, Shipment
from typing import Any
from .database import Database
from .schemas import ShipmentRead, ShipmentCreate, ShipmentUpdate
from app.database.session import create_db_tables, get_session

db = Database()


# @app.get("/shipment", response_model=ShipmentRead)
# def get_shipment_field(field: str, id: int) -> Any:
#     shipment = db.get(id)

#     if shipment is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Given id doesn't exist"
#         )

#     return shipment


# @app.get("/shipment/latest")
# def get_latest_shipment() -> dict[str, Any]:
#     latest_id = max(shipments.keys())
#     return shipments[latest_id]

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    create_db_tables()
    yield


app = FastAPI(lifespan=lifespan_handler)


@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int, session: Session = Depends(get_session)):
    shipment = session.get(Shipment, id)

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Given {id} doesn't exist"
        )

    return shipment


@app.post("/shipment", response_model=None)
def submit_shipment(shipment: ShipmentCreate, session: Session = Depends(get_session)) -> dict[str, Any]:
    new_id = db.create(shipment)
    return {"id": new_id}


@app.put("/shipment", response_model=ShipmentRead)
def shipment_put(id: int, shipment: ShipmentUpdate):
    return db.update(id, shipment)


@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, shipment: ShipmentUpdate):
    return db.update(id, shipment)


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    db.delete(id)

    return {
        "detail": f"Shipment {id} has been deleted"
    }


@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )

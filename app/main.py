from .database import save, shipments
from .schemas import ShipmentRead, ShipmentCreate, ShipmentUpdate
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from typing import Any


app = FastAPI()


@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> Any:
    return shipments[id][field]


@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    latest_id = max(shipments.keys())
    return shipments[latest_id]


@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int | None = None):
    if not id:
        id = max(shipments.keys())
        return shipments[id]

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Given id {id} does not exist.'
        )

    return shipments[id]


@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate) -> dict[str, Any]:

    new_id = int(max(shipments.keys())) + 1
    shipments[new_id] = {
        **shipment.model_dump(),
        "id": new_id,
        "status": "placed"
    }
    save()
    return shipments[new_id]


@app.put("/shipment", response_model=ShipmentRead)
def shipment_put(id: int, content: str, weight: float, status: str):
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status
    }

    return shipments


@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, body: ShipmentUpdate):
    shipments[id].update(body.model_dump(exclude_none=True))
    save()
    return shipments[id]


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    shipments.pop(id)

    return {
        "detail": f"Shipment {id} has been deleted"
    }


@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )

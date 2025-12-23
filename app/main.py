from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .schemas import ShipmentRead, ShipmentCreate, ShipmentUpdate


app = FastAPI()

shipments = {
    12701: {
        "weight": 1.2,
        "content": "wooden table",
        "status": "in transit"
    },
    12702: {
        "weight": 0.8,
        "content": "glassware set",
        "status": "fragile - in transit"
    },
    12703: {
        "weight": 2.5,
        "content": "box of books",
        "status": "delivered"
    },
    12704: {
        "weight": 4.3,
        "content": "electronics - laptop",
        "status": "out for delivery"
    },
    12705: {
        "weight": 0.4,
        "content": "pair of shoes",
        "status": "pending"
    },
    12706: {
        "weight": 6.0,
        "content": "flat-pack furniture",
        "status": "delayed"
    },
    12707: {
        "weight": 1.1,
        "content": "children's toys",
        "status": "cancelled"
    }
}


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

    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
        "id": new_id,
        "content": shipment.content,
        "weight": shipment.weight,
        "destination": shipment.destination,
        "status": "placed"
    }

    return shipments[new_id]


@app.put("/shipment", response_model=ShipmentRead)
def shipment_put(id: int, content: str, weight: float, status: str):
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status
    }

    return shipments


@app.patch("/shipment", response_model=ShipmentUpdate)
def update_shipment(id: int, body: ShipmentUpdate):
    shipment = shipments[id]
    shipment.update(body)
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

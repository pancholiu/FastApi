import sqlite3
from .schemas import ShipmentCreate, ShipmentUpdate
from typing import Any


class Database:
    def __init__(self):
        # Make the connection
        self.connections = sqlite3.connect("sqlite.db")
        self.cursor = self.connections.cursor()
        self.create_table("shipment")

    def create_table(self, name: str):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ? (
                id INTEGER PRIMARY KEY, 
                content TEXT, 
                weight REAL, 
                status TEXT)
        """, (name,))

    def create(self, shipment: ShipmentCreate) -> int:
        # Find a new id
        self.cursor.execute("SELECT MAX(id) FROM shipment")
        result = self.cursor.fetchone()

        new_id = result[0] + 1

        self.cursor.execute("""
            INSERT INTO shipment
            VALUES (:id, :content, :weight, :status)
        """, {
            "id": new_id,
            **shipment.model_dump(),

            "status": "placed"
        })

        return new_id

    def get(self, id: int) -> dict[str, Any] | None:
        self.cursor.execute("""
            SELECT * FROM shipment
            WHERE id = ? 
        """, (id,))

        row = self.cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row[0],
            "content": row[1],
            "weight": row[2],
            "status": row[3]
        } if row else None

    def update(self, shipment: ShipmentUpdate) -> dict[str, Any]:
        self.cursor.execute("""
            UPDATE shipment SET status = :status
            WHERE id = :id        
        """, {
            "id": id,
            **shipment.model_dump()
        })
        self.connections.commit()

        return self.get(id)

    def delete(self, id: int):
        self.cursor.execute("""
            DELETE FROM shipment
            WHERE id = ?
        """, (id,))

        self.connections.commit()

    def close(self):
        self.connections.close()

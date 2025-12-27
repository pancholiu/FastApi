import sqlite3
from app.schemas import ShipmentCreate, ShipmentUpdate
from typing import Any
# Use as decorator to replace enter and exit methods
from contextlib import contextmanager


class Database:
    def connect_to_db(self):
        # Make the connection
        self.connections = sqlite3.connect(
            "sqlite.db", check_same_thread=False)
        self.cursor = self.connections.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS shipment (
                id INTEGER PRIMARY KEY, 
                content TEXT, 
                weight REAL, 
                destination TEXT,
                status TEXT)
        """)

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

        self.connections.commit()

        return new_id

    def get(self, id: int | None = None) -> dict[str, Any] | None:
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

    def update(self, id: int, shipment: ShipmentUpdate) -> dict[str, Any] | None:
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

    # # This method replaces __init__
    # def __enter__(self):
    #     print("entering")
    #     self.connect_to_db()
    #     self.create_table()
    #     return self  # Requiered to make accessible the methods of the class

    # def __exit__(self, *arg):
    #     print("existing")
    #     self.close()


@contextmanager
def managed_db():
    db = Database()
    db.connect_to_db()
    db.create_table()

    yield db

    db.close()


with managed_db() as db:
    print(db.get(12701))
    print(db.get(12702))

import sqlite3
# Make the connection
connections = sqlite3.connect("sqlite.db")
cursor = connections.cursor()

# 1. Create a table
create_table = """
    CREATE TABLE IF NOT EXISTS shipment (
        id INTEGER PRIMARY KEY, 
        content TEXT, 
        weight REAL, 
        status TEXT)
"""

# 2. Add shipment data
insert_values = """
    INSERT INTO SHIPMENT
               VALUES ('12701', 'TREES', 15, 'placed'),
               ('12702', 'Copper', 25, 'in_transit'),
               ('12703', 'Steel', 35, 'placed')
"""

# 3. Read shipment by id
read_shipment_by_id = """
    SELECT * FROM shipment WHERE id = 12702
"""

# 4 Update a shipment
id = 12701
status = "out_for_delivery"

update_statement = """
    UPDATE shipment SET status = :status WHERE id = :id
"""

cursor.execute(update_statement, {"status": status, "id": id})
connections.commit()

# results = cursor.fetchone()

# print(results)


# Close the connection
connections.close()

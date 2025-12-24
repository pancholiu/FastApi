import sqlite3
# Make the connection
connections = sqlite3.connect("sqlite.db")
cursor = connections.cursor()

# 1. Create a table
create_table = """
    CREATE TABLE IF NOT EXISTS shipment (
        id INTEGER, 
        content TEXT, 
        weight REAL, 
        status TEXT)
"""

# 2. Add shipment data
insert_values = """
    INSERT INTO SHIPMENT
               VALUES ('12703', 'metal', 15, 'placed')
"""

# 3. Read shipment by id
read_shipment_by_id = """
    SELECT * FROM shipment WHERE id = 12702
"""

cursor.execute(read_shipment_by_id)

results = cursor.fetchone()

print(results)


# Close the connection
connections.close()

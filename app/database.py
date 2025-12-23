import sqlite3
# Make the connection
connections = sqlite3.connect("sqlite.db")
cursor = connections.cursor()

# 1. Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment (
        id INTEGER, 
        content TEXT, 
        weight REAL, 
        status TEXT)
""")


# 2. Add shipment data
cursor.execute("""
    INSERT INTO SHIPMENT
               VALUES ('12702', 'basalt', 18.7, 'in_transit')
""")
connections.commit()

# Close the connection
connections.close()

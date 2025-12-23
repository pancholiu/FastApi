import json

shipments = {}

with open("shipments.json") as json_file:
    data = json.load(json_file)

    for record in data:
        shipments[record["id"]] = record


def save():
    with open("shipments.json", "w") as json_file:
        json.dump(
            list(shipments.values()),
            json_file
        )

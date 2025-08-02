import json
import os

FILE = "expenses.json"
data = {"entries": []}
if os.path.exists(FILE):
    with open(FILE) as f:
        data = json.load(f)

def add(amount, category):
    data["entries"].append({"amount": amount, "category": category})
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def summary():
    totals = {}
    for e in data["entries"]:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    print("Summary:", totals)

add(150, "food")
add(200, "transport")
summary()

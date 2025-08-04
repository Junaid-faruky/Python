import json

filename = input("Enter JSON file path: ")
try:
    with open(filename) as f:
        json.load(f)
    print("Valid JSON.")
except Exception as e:
    print("Invalid JSON:", e)

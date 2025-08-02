import json
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

data = {"name": "Alice", "age": 30}

try:
    validate(instance=data, schema=schema)
    print("Valid!")
except ValidationError as e:
    print("Invalid:", e.message)

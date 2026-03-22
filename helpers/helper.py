import json

def read_json(schema):
    f = open(schema)
    data = json.load(f)
    return data
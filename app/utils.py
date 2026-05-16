import json

def load_job(path):
    with open(path, "r") as f:
        return json.load(f)

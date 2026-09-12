import json

path = r"src\data\products.json"

def get_all_product():
    with open(path, 'r') as file:
        return json.load(file)
        
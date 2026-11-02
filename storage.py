import json

def load_customers():
    try:
        with open("data/customers.json", "r") as file:
            file_data = json.load(file)
            return file_data
    except FileNotFoundError:
            print("File not found!")
            return []



def save_customers(customers):
    with open("data/customers.json", "w") as file:
        json.dump(customers, file, indent=4)

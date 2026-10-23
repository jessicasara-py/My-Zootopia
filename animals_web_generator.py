import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

# Alle Tiere durchlaufen
for animal in animals_data:
    # Name
    if "name" in animal:
        print("Name:", animal["name"])

    # Ernährung (liegt unter characteristics)
    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        print("Ernährung:", characteristics["diet"])

    # Erster Ort
    locations = animal.get("locations", [])
    if locations:
        print("Ort:", locations[0])

    # Typ
    if "type" in characteristics:
        print("Typ:", characteristics["type"])


    print()

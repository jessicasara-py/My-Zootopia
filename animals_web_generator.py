import json


def load_animals():
    """Liest die Tierdaten aus der JSON-Datei."""
    with open("animals_data.json", "r", encoding="utf-8") as file:
        return json.load(file)


def create_animals_info(data):
    """Erstellt HTML-Karten mit den Informationen aller Tiere."""
    output = ""

    for animal_data in data:
        characteristics = animal_data.get("characteristics", {})

        output += '<li class="cards__item">\n'

        if "name" in animal_data:
            output += f"Name: {animal_data['name']}<br/>\n"

        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}<br/>\n"

        locations = animal_data.get("locations", [])
        if locations:
            output += f"Location: {locations[0]}<br/>\n"

        if "type" in characteristics:
            output += f"Type: {characteristics['type']}<br/>\n"

        output += "</li>\n"

    return output

def load_template():
    """Liest die HTML-Vorlage ein."""
    with open("animals_template.html", "r", encoding="utf-8") as file:
        return file.read()


def create_html(template, animals_info):
    """Ersetzt den Platzhalter in der HTML-Vorlage."""
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_info)


def save_html(html):
    """Schreibt den HTML-Inhalt in eine neue Datei."""
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html)


def main():
    try:
        data = load_animals()
        template = load_template()

        animals_info = create_animals_info(data)
        html = create_html(template, animals_info)

        save_html(html)

        print("Die Datei animals.html wurde erstellt.")

    except FileNotFoundError as error:
        print(f"Datei nicht gefunden: {error.filename}")

    except PermissionError:
        print("Fehler: Keine Berechtigung für den Dateizugriff.")

    except json.JSONDecodeError as error:
        print(f"Fehler in der JSON-Datei: {error}")

    except OSError as error:
        print(f"Dateifehler: {error}")


if __name__ == "__main__":
    main()

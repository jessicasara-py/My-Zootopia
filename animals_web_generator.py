import json


def load_animals():
    """Load animal data from the JSON file."""
    with open("animals_data.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_template():
    """Load the HTML template."""
    with open("animals_template.html", "r", encoding="utf-8") as file:
        return file.read()


def serialize_animal(animal_obj):
    """Convert one animal into an HTML card."""
    output = ['<li class="cards__item">\n']

    if "name" in animal_obj:
        output.append(
            f'  <div class="card__title">{animal_obj["name"]}</div>\n'
        )

    characteristics = animal_obj.get("characteristics", {})

    output.append('  <p class="card__text">\n')

    if "diet" in characteristics:
        output.append(
            f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
        )

    locations = animal_obj.get("locations", [])
    if locations:
        output.append(
            f'    <strong>Location:</strong> {locations[0]}<br/>\n'
        )

    if "type" in characteristics:
        output.append(
            f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'
        )

    output.append("  </p>\n")
    output.append("</li>\n")

    return "".join(output)


def create_animals_info(data):
    """Create HTML cards for all animals."""
    return "".join(serialize_animal(animal) for animal in data)


def create_html(template, animals_info):
    """Insert animal information into the HTML template."""
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_info)


def save_html(html):
    """Save the generated HTML to a file."""
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html)


def main():
    try:
        data = load_animals()
        template = load_template()

        animals_info = create_animals_info(data)
        html = create_html(template, animals_info)

        save_html(html)

        print("The file animals.html was created successfully.")

    except FileNotFoundError as error:
        print(f"File not found: {error.filename}")

    except json.JSONDecodeError as error:
        print(f"Invalid JSON: {error}")

    except PermissionError:
        print("Error: Permission denied.")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    main()

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
    locations = animal_obj.get("locations", [])

    output.append('  <div class="card__text">\n')
    output.append('    <ul class="animal__details">\n')

    if "diet" in characteristics:
        output.append(
            f'      <li class="animal__detail"><strong>Diet:</strong> '
            f'{characteristics["diet"]}</li>\n'
        )

    if locations:
        output.append(
            f'      <li class="animal__detail"><strong>Location:</strong> '
            f'{locations[0]}</li>\n'
        )

    if "type" in characteristics:
        output.append(
            f'      <li class="animal__detail"><strong>Type:</strong> '
            f'{characteristics["type"]}</li>\n'
        )

    output.append('    </ul>\n')
    output.append('  </div>\n')
    output.append('</li>\n')

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
        print(
            "Error: The file 'animals_data.json' contains invalid data. "
            "Please check that the file contains valid JSON."
        )

    except PermissionError:
        print("Error: Permission denied.")

    except IsADirectoryError:
        print(
            "Error: A directory was provided instead of a file. "
            "Please check the file path."
        )

    except OSError:
        print(
            "Error: A file operation failed. "
            "Please check the file path and access permissions."
        )


if __name__ == "__main__":
    main()

import json


def wrap_in_quotes_and_add_fields(obj):
    # If the object is a dictionary, loop through its key-value pairs
    if isinstance(obj, dict):
        # Delete the 'domesticHighSchool' field if it is present
        if 'domesticHighSchool' in obj:
            del obj['domesticHighSchool']
            
        # Add the new fields right below 'canadianRanking'
        new_fields = {
            'businessFacultyRanking': '',
            'computerScienceFacultyRanking': '',
            'educationFacultyRanking': '',
            'nursingFacultyRanking': '',
            'engineeringFacultyRanking': '',
            'mathFacultyRanking': '',
            'psychologyFacultyRanking': ''
        }
        new_obj = {}
        for k, v in obj.items():
            new_obj[k] = wrap_in_quotes_and_add_fields(v)
            if k == 'canadianRanking':
                for field_name, field_value in new_fields.items():
                    new_obj[field_name] = field_value

        # Wrap the values of the constant fields in quotes
        for field in ['tuition', 'applicationDeadline', 'requirements', 'langRequirement', 'additonalRequirements']:
            if field in obj:
                obj[field] = f'"{obj[field]}"'
        # Recursively call the `wrap_in_quotes_and_add_fields` function for each value in the dictionary
        return {k: wrap_in_quotes_and_add_fields(v) for k, v in new_obj.items()}

    # If the object is a list, recursively call the `wrap_in_quotes_and_add_fields` function for each element in the list
    elif isinstance(obj, list):
        return [wrap_in_quotes_and_add_fields(elem) for elem in obj]

    # If the object is neither a dict nor a list, return the object as-is
    else:
        return obj


# Load the JSON data from the file
with open('F:\\PythonProjects\\python-exercises\\out_with_tags(12).json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Wrap the values of the constant fields in quotes and delete the 'domesticHighSchool' field
data = wrap_in_quotes_and_add_fields(data)

# Save the modified JSON data back to the file
with open('F:\\PythonProjects\\python-exercises\\out_with_tags(12).json', 'w') as file:
    json.dump(data, file, indent=4)
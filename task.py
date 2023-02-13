import json
from jsonpath_rw import jsonpath, parse

with open('F:\\PythonProjects\\python-exercises\\converted.json', 'r') as file:
    data = json.load(file)


def wrap_in_quotes(field, obj):
    # If the object is a dictionary, loop through its key-value pairs
    if isinstance(obj, dict):
        # If the field name is in the dictionary, wrap its value in quotes
        if field in obj:
            obj[field] = f'"{obj[field]}"'
        # Recursively call the `wrap_in_quotes` function for each value in the dictionary
        return {k: wrap_in_quotes(field, v) for k, v in obj.items()}
    # If the object is a list, recursively call the `wrap_in_quotes` function for each element in the list
    elif isinstance(obj, list):
        return [wrap_in_quotes(field, elem) for elem in obj]
    # If the object is neither a dict nor a list, return the object as-is
    else:
        return obj


# Wrap the values of the field 'tuition' in quotes
data = wrap_in_quotes('tuition', data)

# Wrap the values of the field 'applicationDeadline' in quotes
data = wrap_in_quotes('applicationDeadline', data)

# Wrap the values of the field 'requirements' in quotes
data = wrap_in_quotes('requirements', data)


with open('F:\\PythonProjects\\python-exercises\\converted.json', 'w') as file:
    json.dump(data, file, indent=4)
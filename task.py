import json
from jsonpath_rw import jsonpath, parse

with open('F:\\PythonProjects\\python-exercises\\converted.json', 'r') as file:
    data = json.load(file)


def wrap_in_quotes(field, obj):
    if isinstance(obj, dict):
        if field in obj:
            obj[field] = f'"{obj[field]}"'
        return {k: wrap_in_quotes(field, v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [wrap_in_quotes(field, elem) for elem in obj]
    else:
        return obj


data = wrap_in_quotes('tuition', data)
data = wrap_in_quotes('applicationDeadline', data)
data = wrap_in_quotes('requirements', data)

with open('F:\\PythonProjects\\python-exercises\\converted.json', 'w') as file:
    json.dump(data, file, indent=4)
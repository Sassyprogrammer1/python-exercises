import json
from jsonpath_rw import jsonpath, parse

with open('\message.txt', 'r') as file:
    json_str = file.read()
    json_data = json.loads(json_str)


# parse the jsonpath expression to match all fields with the keyword 'university' in them
jsonpath_expr = parse('$.canadianUniversities.*[*].courses.major.minor[*]')

# find all matches in the json data
matches = jsonpath_expr.find(json_data)

# Iterate over each match
for match in matches:
     # Check if the match is a dictionary and contains requirement and importantTag fields
    if isinstance(match.value, dict) and 'requirement' in match.value and 'importantTag' in match.value:
        # Check if the requirement field is not already a list and wrap it in a list
        if not isinstance(match.value['requirement'], list):
            match.value['requirement'] = [match.value['requirement']]

        # Check if the importTag field is not already a list and wrap it in a list    
        if not isinstance(match.value['importantTag'], list):
            match.value['importantTag'] = [match.value['importantTag']]


with open('\message.txt','w') as file:
    json.dump(json_data, file, indent=4)
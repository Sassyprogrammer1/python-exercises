import os
import json
import boto3

table_name = 'table-name'

dynamodb = boto3.client('dynamodb')

count_file = 'count.txt'

with open(count_file) as f:
    count = int(f.read())

#interchange aus,can,nz
json_folder = 'uni-json/aus'

for file_name in os.listdir(json_folder):
    if file_name.endswith('.json'):
        json_file = os.path.join(json_folder, file_name)
        with open(json_file) as f:
            data = json.load(f)

        for item in data:
            response = dynamodb.put_item(
                TableName = table_name,
                Item = item
            )

        count += 1
        with open(count_file,'w') as f:
            f.write(str(count))

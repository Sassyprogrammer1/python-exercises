import requests

# Define the URL you want to send the POST request to
url = 'https://example.com/api/endpoint'

# Define the data you want to send in the POST request (if any)
data = {
  'key1': 'value1',
  'key2': 'value2'
}

# Make the POST request
response = requests.post(url, data=data)

# Print the response content
print(response.content)
import requests

# Set the request parameters
url = 'https://dev61695.service-now.com/api/now/table/incident/3D7382a322db63101038d00d53ca9619c1'
user = 'apiuser'
pwd = 'Hello@1234'

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Do the HTTP request
response = requests.patch(url, auth=(user, pwd), headers=headers, data='{"short_description":"Test update Patch"}')

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
print('Status:', response.status_code, 'Headers:', response.headers, 'Response:', response.json())
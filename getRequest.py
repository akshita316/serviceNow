import requests

# Set the request parameters
url = 'https://dev61695.service-now.com/api/now/table/incident'
user = 'apiuser'
pwd = 'Hello@1234'

# Set proper headers
headers = {"Accept": "application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
print('Status:', response.status_code, 'Headers:', response.headers, 'Response:', response.json())
# print('response', response.json())
print('Cookies', response.cookies)

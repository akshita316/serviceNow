import requests
import pandas as pd
import xlrd, openpyxl
import json

df = pd.read_excel("/Users/akshitaagarwal/Downloads/work_test/servicenow.xlsx")
# Set the request parameters
url = 'https://dev61695.service-now.com/api/now/table/incident'
user = 'apiuser'
pwd = 'Hello@1234'

for i, r in df.iterrows():
    # Set proper headers
    # short = json.dumps(str(r['short']))
    short = str(r['short'])
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    data = {"short_description": short}

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers, data=json.dumps(data))

    # Check for HTTP codes other than 200
    if response.status_code != 201:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data

    # print('Status:', response.status_code, 'Headers:', response.headers, 'Response:', response.json())
    incident = response.json()
    elevations = response.read()

    print('status', response.status_code, 'Incident:', incident, 'elevations:', elevations.splitlines())
    df = pd.json_normalize(incident['task_effective_number'])
    df.to_excel("test.xlsx", index=False)
    break
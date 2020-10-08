import requests
import pandas as pd
import xlrd, openpyxl
import json

df = pd.read_excel("/Users/akshitaagarwal/Downloads/work_test/servicenow.xlsx")
json_data = pd.DataFrame()

# Set the request parameters
url = 'https://dev61695.service-now.com/api/now/table/incident'
user = 'apiuser'
pwd = 'Hello@1234'

for i, r in df.iterrows():
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
    print('Status:', response.status_code, 'Error Response:', response.json())

    data = response.json()
    df_temp = pd.json_normalize(data['result'])
    json_data = json_data.append(df_temp, ignore_index=True, sort=False)
    break

json_data.to_excel("json_response.xlsx", index=False)

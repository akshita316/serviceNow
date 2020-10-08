from __future__ import print_function
import pickle
import os.path
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SPREADSHEET_ID = '1apXKKijUQ1zSVl4dg0rlqO3t6-cp7rBnSWpxzEMM9m8'
RANGE_NAME = 'Form Responses 1'


def get_google_sheet(spreadsheet_id, range_name):
    """ Retrieve sheet data using OAuth credentials and Google Python API. """
    scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    # scopes = ['https://www.googleapis.com/auth/calendar']
    # scopes = "https://googleapis.com/auth/drive"
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    gsheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return gsheet


def gsheet2df(gsheet):
    """ Converts Google sheet data to a Pandas DataFrame.
    Note: This script assumes that your data contains a header file on the first row!
    Also note that the Google API returns 'none' from empty cells - in order for the code
    below to work, you'll need to make sure your sheet doesn't contain empty cells,
    or update the code to account for such instances.
    """
    print('gsheet', gsheet)
    # values = gsheet.get('values', [])
    header = gsheet.get('values', [])[0]   # Assumes first line is header!
    print(header)
    values = gsheet.get('values', [])[1:]  # Everything else is data.
    print(values)
    if not values:
        print('No data found.')
    else:
        df = pd.DataFrame(values, columns=header)
    return df


gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
df = gsheet2df(gsheet)
df.to_excel("form response.xlsx", index=False)
print(df.head())

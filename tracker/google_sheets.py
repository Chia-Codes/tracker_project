import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scope for Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Path to google-credentials.json (downloaded credentials)
CREDENTIALS_PATH = 'credentials.json' 


def get_google_sheets_service():
    creds = None

    # Load credentials from token.pickle if it exists
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials, go through the OAuth flow
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)

        # Save credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service

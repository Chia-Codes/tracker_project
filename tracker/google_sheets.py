import os
import json
import base64
import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


# Only add if you DON'T already have a similar loader
def _sa_info_from_env():
    """Load Service Account JSON from one of three env vars:
    1) GOOGLE_SA_JSON_B64 (base64-encoded JSON)
    2) GOOGLE_SA_JSON (raw JSON string)
    3) GOOGLE_SA_PATH (absolute path to creds file on disk)
    """
    b64 = os.getenv("GOOGLE_SA_JSON_B64")
    raw = os.getenv("GOOGLE_SA_JSON")
    path = os.getenv("GOOGLE_SA_PATH")
    if b64:
        return json.loads(base64.b64decode(b64).decode("utf-8"))
    if raw:
        return json.loads(raw)
    if path and os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    raise RuntimeError("Google Service Account credentials not found in env.")


# Client Gspread
def get_gspread_client():
    info = _sa_info_from_env()
    creds = Credentials.from_service_account_info(info, scopes=SCOPES)
    return gspread.authorize(creds)


def fetch_sheet_rows(sheet_id: str, worksheet_title: str = "Resources"):
    """Return a list of dicts based on header row from the given sheet/tab."""
    gc = get_gspread_client()
    sh = gc.open_by_key(sheet_id)
    ws = sh.worksheet(worksheet_title) if worksheet_title else sh.sheet1
    return ws.get_all_records()
    
# Add these helpers to your existing module (KEEP your current code; do not delete anything)
# If you already have functions with the same names, keep your versions and only add what's missing.
import os, json, base64
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


# If you already have a client factory (e.g., get_gspread_client), keep yours and skip this
def get_gspread_client():
    info = _sa_info_from_env()
    creds = Credentials.from_service_account_info(info, scopes=SCOPES)
    return gspread.authorize(creds)

# New: unified fetcher your view will call. If you already have something like
# get_sheet_rows(sheet_id, worksheet), you can simply alias:
#   fetch_sheet_rows = get_sheet_rows


def fetch_sheet_rows(sheet_id: str, worksheet_title: str = "Resources"):
    """Return a list of dicts based on header row from the given sheet/tab."""
    gc = get_gspread_client()
    sh = gc.open_by_key(sheet_id)
    ws = sh.worksheet(worksheet_title) if worksheet_title else sh.sheet1
    return ws.get_all_records()  # [{'Title': '...', 'Description': '...', 'URL': '...'}, ...]
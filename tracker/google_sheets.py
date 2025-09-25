import gspread


# Initialize gspread client
def get_gspread_client():
    # Auth using credentials.json and authorized_user.json
    return gspread.oauth()


# Create a new Google Sheet for a user
def create_user_sheet(username):
    gc = get_gspread_client()
    spreadsheet = gc.create(f"{username}_Cycle_Log")
    
    # Move the sheet to a folder or tag it if needed
    print(f"Created sheet for {username}: https://docs.google.com/spreadsheets/d/{spreadsheet.id}")
    return spreadsheet.id

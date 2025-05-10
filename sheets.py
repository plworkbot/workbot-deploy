import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEET_NAME

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open(GOOGLE_SHEET_NAME).sheet1

def add_user(data: dict):
    row = [
        data.get("name", ""),
        data.get("phone", ""),
        data.get("citizenship", ""),
        data.get("experience", ""),
        data.get("city", "")
    ]
    sheet.append_row(row)

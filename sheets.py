import gspread
from google.oauth2.service_account import Credentials
import streamlit as st


def get_client():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=scope
    )

    return gspread.authorize(creds)


def get_sheet(spreadsheet_id):
    client = get_client()
    spreadsheet = client.open_by_key(spreadsheet_id)
    return spreadsheet.sheet1


# ✅ CACHE DATA FOR 60 SECONDS
@st.cache_data(ttl=60)
def get_all_records(spreadsheet_id):
    sheet = get_sheet(spreadsheet_id)
    return sheet.get_all_records()


def update_status(spreadsheet_id, row_number, status_column, new_status):
    sheet = get_sheet(spreadsheet_id)
    sheet.update_cell(row_number, status_column, new_status)

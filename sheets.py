import streamlit as st
import gspread
from google.oauth2.service_account import Credentials


def get_client():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scope
    )

    return gspread.authorize(creds)


def get_sheet(spreadsheet_id):
    client = get_client()
    return client.open_by_key(spreadsheet_id).sheet1


def get_all_records(spreadsheet_id):
    sheet = get_sheet(spreadsheet_id)
    return sheet.get_all_records()

import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
BASE_URL = "https://sdpondemand.manageengine.com"
API_VERSION = "v3"


def create_access_token():
    url = "https://accounts.zoho.com/oauth/v2/token"
    data = {
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
    }

    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


def list_tickets(access_token, limite=10):
    url = f"{BASE_URL}/api/{API_VERSION}/requests"
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/vnd.manageengine.v3+json",
    }

    seven_days_ago = datetime.now() - timedelta(days=30)
    timestamp_ms = int(seven_days_ago.timestamp() * 1000)

    filter = {
        "list_info": {
            "row_count": limite,
            "search_criteria": {
                "field": "created_time.value",
                "condition": "greater than",
                "value": str(timestamp_ms),
            },
        }
    }

    params = {"input_data": json.dumps(filter)}

    response = requests.get(url, headers=headers, params=params, verify=False)
    response.raise_for_status()
    return response.json().get("requests", [])


def export_tickets(tickets):
    export_data = [
        {
            "id": c.get("id"),
            "subject": c.get("subject"),
            "status": c.get("status", {}).get("name"),
            "created_time": c.get("created_time", {}).get("value"),
            "technician": (
                c.get("technician", {}).get("name")
                if c.get("technician")
                else ""
            ),
            "group": c.get("group", {}).get("name"),
            "template": c.get("template", {}).get("name"),
        }
        for c in tickets
    ]

    with open("tickets.json", "w", encoding="utf-8") as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)

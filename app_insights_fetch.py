import requests
import os

# Load values from environment variables
APP_INSIGHTS_ID = os.getenv("APP_INSIGHTS_ID")
APP_INSIGHTS_API_KEY = os.getenv("APP_INSIGHTS_API_KEY")

API_URL = f"https://api.applicationinsights.io/v1/apps/{APP_INSIGHTS_ID}/query"

def get_api_response_times():
    query = """
    requests
    | summarize avg(duration) by name
    | order by avg_duration desc
    """
    headers = {
        "x-api-key": APP_INSIGHTS_API_KEY
    }
    response = requests.get(API_URL, params={"query": query}, headers=headers)
    return response.json()

def get_db_query_performance():
    query = """
    dependencies
    | where type == "SQL"
    | project name, duration, resultCode
    | order by duration desc
    """
    headers = {
        "x-api-key": APP_INSIGHTS_API_KEY
    }
    response = requests.get(API_URL, params={"query": query}, headers=headers)
    return response.json()

import requests
import json

# Replace with your Application Insights details
APP_INSIGHTS_ID = "your_app_insights_id"
APP_INSIGHTS_API_KEY = "your_api_key"

# Application Insights REST API URL
API_URL = f"https://api.applicationinsights.io/v1/apps/{APP_INSIGHTS_ID}/query"

# Function to fetch API response times
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

# Function to fetch database performance metrics
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

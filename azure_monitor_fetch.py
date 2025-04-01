import os
from azure.monitor.query import MetricsQueryClient
from azure.identity import DefaultAzureCredential

# Load from environment
RESOURCE_ID = os.getenv("AZURE_MONITOR_RESOURCE_ID")

# Initialize Azure Monitor client
client = MetricsQueryClient(credential=DefaultAzureCredential())

def get_system_health():
    try:
        # Correct method to use
        response = client.query(
            resource_id=RESOURCE_ID,
            timespan="PT1H",  # 1 hour
            metric_names=["Percentage CPU", "Available Memory", "Uptime"]
        )
        return response.metrics
    except Exception as e:
        print(f"Error fetching system health: {e}")
        return None

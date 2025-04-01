from azure.monitor.query import MetricsQueryClient
from azure.identity import DefaultAzureCredential

# Azure Monitor resource ID
RESOURCE_ID = "your_azure_monitor_resource_id"

# Initialize the Azure Monitor client
client = MetricsQueryClient(credential=DefaultAzureCredential())

# Function to fetch system health metrics (CPU, memory, uptime)
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

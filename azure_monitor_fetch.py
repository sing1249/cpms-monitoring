from azure.monitor.query import MetricsQueryClient
from azure.identity import DefaultAzureCredential

# Azure Monitor resource ID
RESOURCE_ID = "your_azure_monitor_resource_id"

# Initialize the Azure Monitor client
client = MetricsQueryClient(credential=DefaultAzureCredential())

# Function to fetch system health metrics (CPU, memory, uptime)
def get_system_health():
    response = client.query(
        resource_id=RESOURCE_ID,
        timespan="PT1H",
        metric_names=["Percentage CPU", "Available Memory", "Uptime"]
    )
    return response.metrics

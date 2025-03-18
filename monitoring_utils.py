from azure.monitor.query import MetricsQueryClient
from azure.identity import DefaultAzureCredential

def get_usage_stats():
    try:
        client = MetricsQueryClient(credential=DefaultAzureCredential())
        response = client.query(
            resource_id="YOUR_APPLICATION_INSIGHTS_RESOURCE_ID",
            timespan="last 30 days",
            metric_names=["requests", "dependencies"]
        )
        return response.metrics
    except Exception as e:
        print(f"Error fetching usage stats: {e}")
        return {}

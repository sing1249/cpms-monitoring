from opencensus.metrics.export import Gauge
from opencensus.metrics.export import MetricDescriptor
from opencensus.ext.azure.metrics import AzureMonitorMetricsExporter
import psutil  # For CPU usage metric

def setup_metrics_exporter():
    exporter = AzureMonitorMetricsExporter(
        connection_string='InstrumentationKey=YOUR_INSTRUMENTATION_KEY'
    )
    # Track API response time and other metrics
    response_time_metric = Gauge("api_response_time", "API response time in milliseconds", ["endpoint"])
    
    # Example of adding CPU usage metric
    cpu_usage_metric = Gauge("cpu_usage", "CPU usage percentage")
    
    exporter.export([response_time_metric, cpu_usage_metric])

import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

# Initialize logger for Application Insights
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string="InstrumentationKey=YOUR_INSTRUMENTATION_KEY"))

def log_event(event_name, details, level="info"):
    if level == "info":
        logger.info(f"Event: {event_name}, Details: {details}")
    elif level == "warning":
        logger.warning(f"Event: {event_name}, Details: {details}")
    elif level == "error":
        logger.error(f"Event: {event_name}, Details: {details}")

from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

# Setting up Application Insights
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=YOUR_INSTRUMENTATION_KEY'))

# Example log for warning message
logger.warning("This is a warning message to be logged in Application Insights.")

# CPMS Monitoring Backend

This project is the **backend monitoring microservice** for the Centralized Patient Management System (CPMS). It provides RESTful API endpoints to expose telemetry and performance data using:

- **Azure Application Insights** (API response times, database performance)
- **Azure Monitor** (system-level metrics like CPU, memory, uptime)

Built with **Flask**, this service runs on **Gunicorn** in production and is containerized for deployment to **Azure Kubernetes Service (AKS)**.

---

## 📂 Project Structure

```text
.
├── app.py                  # Flask API exposing monitoring endpoints
├── app_insights_fetch.py  # Queries metrics from Application Insights
├── azure_monitor_fetch.py # Queries metrics from Azure Monitor
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image definition
└── README.md               # This documentation
```

## 🧠 File Breakdown

### `app.py`

This is the **Flask application entry point**. It sets up the REST API and exposes the following endpoints:

- `/`  
  Health check endpoint to confirm the service is running.

- `/monitor/api-performance`  
  Fetches average duration of API calls from Azure Application Insights.

- `/monitor/db-performance`  
  Fetches database query performance metrics from Azure Application Insights.

- `/monitor/system-health`  
  Fetches system health metrics such as CPU usage, available memory, and uptime from Azure Monitor.

Each route safely handles exceptions and returns structured JSON responses.

---

### `app_insights_fetch.py`

Handles **interactions with Azure Application Insights** using the REST API.

#### Functions:

- `get_api_response_times()`  
  Queries average response duration per API endpoint.

- `get_db_query_performance()`  
  Queries SQL database dependencies, including execution time and result codes.

#### Reads from environment variables:

- `APP_INSIGHTS_ID` – Application Insights App ID  
- `APP_INSIGHTS_API_KEY` – API Key for querying metrics

## 🐳 Docker Image

The service is containerized and available on Docker Hub:
sing1249/cpms-monitoring:latest




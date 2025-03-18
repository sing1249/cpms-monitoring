# Backend System for Monitoring and Logging

This project involves monitoring, logging, and reporting various system activities such as user logins, CRUD operations, and API performance metrics. The backend is designed to capture and export relevant data to Azure Monitor and Application Insights. Below is an explanation of each file in the project to help the frontend developer integrate these features into the frontend.

## Table of Contents
- [File Overview](#file-overview)
- [API Endpoints](#api-endpoints)
- [Azure Monitor & Logging](#azure-monitor-logging)
- [System Metrics](#system-metrics)

---

## File Overview

### 1. `azure_monitor.py`
This file is responsible for setting up logging to Azure Application Insights using the OpenCensus library. The logger sends event logs (like errors and custom events) directly to Azure Monitor for visibility.

#### Key Functionality:
- Configures a logger that sends log events to Azure Application Insights.
- You can use the `logger.warning()` or `logger.info()` methods to log custom events or messages.

### 2. `logging_utils.py`
This file provides utility functions for logging events to Azure Application Insights. The function `log_event()` is used throughout the app to log specific events.

#### Key Functionality:
- **`log_event(event_name, details)`**: Logs a custom event to Azure Application Insights. For example, it logs user login events or CRUD activities.

### 3. `monitoring_utils.py`
This file is used to fetch usage statistics from Azure Monitor. It provides a function `get_usage_stats()` that queries Azure Monitor for metrics such as user requests and dependency calls over the last 30 days.

#### Key Functionality:
- **`get_usage_stats()`**: Retrieves usage data (requests, dependencies) from Azure Monitor to display in the frontend dashboard.

### 4. `system_health.py`
This file defines the setup for monitoring system health metrics like API response time. It exports metrics like response time to Azure Monitor to provide insights into how well the system is performing.

#### Key Functionality:
- **`setup_metrics_exporter()`**: Sets up an exporter that sends system health metrics (e.g., response times) to Azure Monitor for tracking.

### 5. `usage_tracking.py`
This file contains functions to track user activity, including user logins and CRUD operations on entities in the system. It logs these actions to Azure Application Insights using the logger from `azure_monitor.py`.

#### Key Functionality:
- **`log_user_login(user_id)`**: Logs when a user logs in.
- **`log_crud_activity(action, user_id, entity)`**: Logs CRUD operations like Create, Read, Update, and Delete performed by a user on a specific entity.

### 6. `app.py` (Main Flask Application)
This file is the main entry point of the Flask application. It exposes two main routes:
- **`/event`**: A route that logs a custom event (e.g., user login).
- **`/dashboard/usage`**: A route that fetches usage statistics from Azure Monitor and returns them as JSON.

#### Key Functionality:
- **`/event`**: Logs a custom event using the `log_event()` function.
- **`/dashboard/usage`**: Returns usage statistics (like requests and dependencies) fetched from Azure Monitor.

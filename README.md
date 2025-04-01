# Backend System for Monitoring and Logging

This project involves monitoring, logging, and reporting various system activities such as user logins, CRUD operations, and API performance metrics. The backend is designed to capture and export relevant data to Azure Monitor and Application Insights. Below is an explanation of each file in the project to help the frontend developer integrate these features into the frontend.

# CPMS Monitoring Service

This repository contains the **backend monitoring service** for the Centralized Patient Management System (CPMS). It provides REST API endpoints to retrieve performance metrics from:

- **Azure Application Insights** (API response times, DB query performance)
- **Azure Monitor** (CPU usage, memory, uptime)

The service is written in Python using **Flask** and is production-ready with **Gunicorn** for WSGI hosting.

---

## 📦 Features

- `/monitor/api-performance` → Avg API response durations from Application Insights  
- `/monitor/db-performance` → SQL DB dependency performance  
- `/monitor/system-health` → CPU %, available memory, and uptime from Azure Monitor  

---



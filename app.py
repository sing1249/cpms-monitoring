from flask import Flask, jsonify
from app_insights_fetch import get_api_response_times, get_db_query_performance
from azure_monitor_fetch import get_system_health

app = Flask(__name__)

# Endpoint to get API response times
@app.route('/monitor/api-performance')
def api_performance():
    data = get_api_response_times()
    return jsonify(data)

# Endpoint to get DB performance
@app.route('/monitor/db-performance')
def db_performance():
    data = get_db_query_performance()
    return jsonify(data)

# Endpoint to get system health (CPU, memory, uptime)
@app.route('/monitor/system-health')
def system_health():
    data = get_system_health()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

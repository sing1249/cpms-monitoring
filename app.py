from flask import Flask, jsonify
from app_insights_fetch import get_api_response_times, get_db_query_performance
from azure_monitor_fetch import get_system_health

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Monitoring service is running."})

# Endpoint to get API response times
@app.route('/monitor/api-performance')
def api_performance():
    try:
        data = get_api_response_times()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get DB performance
@app.route('/monitor/db-performance')
def db_performance():
    try:
        data = get_db_query_performance()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get system health (CPU, memory, uptime)
@app.route('/monitor/system-health')
def system_health():
    try:
        metrics = get_system_health()
        if not metrics:
            return jsonify({"error": "No metrics received"}), 500
        
        # Convert to JSON-friendly format
        result = {}
        for metric in metrics:
            datapoints = []
            for time_series in metric.timeseries:
                for data in time_series.data:
                    datapoints.append({
                        "timestamp": data.time_stamp.isoformat(),
                        "value": data.total
                    })
            result[metric.name] = datapoints
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

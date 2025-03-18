from flask import Flask, jsonify
from logging_utils import log_event
from monitoring_utils import get_usage_stats

app = Flask(__name__)

# Example route that logs a custom event
@app.route('/event')
def log_custom_event():
    log_event('User Login', 'User logged in successfully.')
    return jsonify({"status": "Event logged"})

# Example route that fetches usage stats from Azure Monitor
@app.route('/dashboard/usage')
def dashboard_usage():
    usage_stats = get_usage_stats()
    return jsonify(usage_stats)

if __name__ == '__main__':
    app.run(debug=True)

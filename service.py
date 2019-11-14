from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, defaults_prefix='myservice')

@app.route('/')
def main():
    return "done"

@app.route('/status/<int:status>')
def echo_status(status):
    return 'Status: %s' % status, status

print(app.url_map)

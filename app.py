import random
import time

from flask import Flask, render_template_string, abort
from prometheus_client import generate_latest, REGISTRY, Counter, Gauge, Histogram

app = Flask(__name__)

# A counter to count the total number of HTTP requests
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests (count)', ['method', 'endpoint', 'status_code'])

# A gauge (i.e. goes up and down) to monitor the total number of in progress requests
IN_PROGRESS = Gauge('http_requests_inprogress', 'Number of in progress HTTP requests')

# A histogram to measure the latency of the HTTP requests
TIMINGS = Histogram('http_request_duration_seconds', 'HTTP request latency (seconds)')




@app.route('/bcfm')
@IN_PROGRESS.track_inprogress()
@TIMINGS.time()
def index():
    return "BCFM"


@app.route('/metrics')
@IN_PROGRESS.track_inprogress()
@TIMINGS.time()
def metrics():
    REQUESTS.labels(method='GET', endpoint="/metrics", status_code=200).inc()
    return generate_latest(REGISTRY)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

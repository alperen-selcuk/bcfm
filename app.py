from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics


app = Flask(__name__)
@app.route("/bcfm")
def index():
  return "BCFM"

register_metrics(app, app_version="v0.1.2", app_config="staging")
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

run_simple(hostname="0.0.0.0", application=dispatcher)

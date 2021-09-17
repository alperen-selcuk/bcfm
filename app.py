from flask import request, Flask
import json
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

app = Flask(__name__)
@app.route('/bcfm')

register_metrics(app, app_version="v0.1.2", app_config="staging")
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

def hello_world():
  
  return 'BCFM'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', application=dispatcher)

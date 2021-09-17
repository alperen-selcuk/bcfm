from flask import request, Flask
import json

app = Flask(__name__)
@app.route('/bcfm')

def hello_world():
  
  return 'BCFM GREEN'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

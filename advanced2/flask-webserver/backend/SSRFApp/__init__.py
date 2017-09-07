import urllib2
import urllib
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'

@app.route('/testhook/', methods=['POST'])
def hook():
    return 'My internal (ie: secured) Flask service!\nOnly accessible from 10.0.0.0/8!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

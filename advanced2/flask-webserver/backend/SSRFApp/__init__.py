import urllib2
import httplib
import requests
from flask import Flask

app = Flask(__name__)
url = 'http://1.1.1.1 &@2.2.2.2# @3.3.3.3/'

@app.route('/')
def hello():
    return 'My internal (ie: secured) Flask service!\nOnly accessible from 10.0.0.0/8!'

@app.route('/filter1/')
def filter1():
    from urlparse import urlparse
    return urlparse(url).netloc

@app.route('/filter2/')
def filter2():
    return '{}'

@app.route('/filter3/')
def filter3():
    return '{}'

@app.route('/filter4/')
def filter4():
    return '{}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

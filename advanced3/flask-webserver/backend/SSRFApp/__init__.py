import urllib
import urlparse
import httplib
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    url=request.form['handler']
    host = urlparse.urlparse(url).hostname
    if host == 'secret.corp':
        return 'Restricted Area!'
    else:
        return urllib.urlopen(url).read()

@app.route('/mail/', methods=['POST'])
def index():
    url=request.form['handler']
    host = urlparse.urlparse(url).hostname
    if host == 'secret.corp':
        return 'Restricted Area!'
    else:
        httplib.HTTPConnection("www.python.org")
        return urllib.urlopen(url).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

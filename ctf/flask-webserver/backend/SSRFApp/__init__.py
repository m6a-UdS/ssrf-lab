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
    #FLAG 2
    if '10.0.0.38' in url or 'secret2.corp' in url:
        return 'FLAG2 - Restricted Area!'
    #FLAG 3
    if host == 'secret3.corp':
        return 'FLAG3 - Restricted Area!'
    else:
        return urllib.urlopen(url).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

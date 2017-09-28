import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    This is secretserver2!
    Only accessible from 10.0.0.0/8!
    Here is your flag: {0}
    """.format(os.environ['FLAG1'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

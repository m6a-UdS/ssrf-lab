from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is secretserver1!\nOnly accessible from 10.0.0.0/8!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

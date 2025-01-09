from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "Hello, DevOps!"})


if __name__ == "__main__":
    app.run(host="192.168.0.1", port=5000)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/prediction", methods=['GET', 'POST'])
def prediction_route():
        return jsonify({"status": "success", "payload": "['apple', 'Orange', 'Lemon']"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

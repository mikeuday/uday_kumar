from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'welcome '


@app.route('/add', methods=["POST"])
def addition():
    a = int(request.json("num1"))
    b = int(request.json("num2"))
    c = a + b
    return jsonify(c)


if __name__ == '__main__':
    app.run(debug=True)

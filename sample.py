from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/hello")
def helloPage():
    return "hello page"

@app.route("/user_login",methods=['POST'])
def user_login():
    username=request.json['username']
    password=request.json['password']

    if username=='uday kumar' and password=='123':

        return'valid user'
    else:
        return 'invaid user'


if __name__=='__main__':
    app.run(debug=True)
from flask import Flask,jsonify
app=Flask(__name__)


@app.route('/')
def home():
    return 'welcome to python world'


@app.route('/fib/<int:n>')
def fib(n):
    result = []
    a,b = 0,1
    while(n>0):
        result.append(a)
        a,b=b,a+b
        n-=1
    return jsonify(result)


if __name__=='__main__':
    app.run(debug='True')
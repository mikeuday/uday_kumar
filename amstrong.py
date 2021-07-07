from flask import Flask, jsonify
app=Flask(__name__)
@app.route('/')
def home():
    return 'welcome to my world'

@app.route('/armstrong/<int:n>')




def armstrong(n):
    sum = 0
    order=len(str(n))
    copy_n= n
    while(n>0):
        digit = n%10
        sum+= digit**order
        n= n//10

    if (sum == copy_n):
        print(f"{copy_n} is an amstrong number")
        result = {
            "name":copy_n,
            "amstrong":True,
            "server ip":"127.0.0.154"

        }
    else:
        print(f"f{copy_n} is not an amstrong  number")
        result = {
            "name":copy_n,
            "amstrong": False,
            "server ip": '127.0.0.154.'


        }
    return jsonify(result)



if __name__=="__main__":
    app.run(debug=True)







# n=153
# sum = 0
# order=len(str(n))
# copy_n= n
# while(n>0):
#     digit = n%10
#     sum+= digit**order
#     n= n//10
#
# if (sum == copy_n):
#     print("n is an amstrong number")
# else:
#     print("n is not an amstrong  number")
#

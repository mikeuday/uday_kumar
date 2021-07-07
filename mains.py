from flask import Flask,render_template, request

app=Flask('__name__')


# @app.route('/home', methods=['GET','POST'])
# def res():


@app.route('/home', methods=['GET','POST'])
def home():
	a=request.form.get('firstvalue') 
	b=request.form.get('secondvalue') 
	if a and b and request.method=='POST':
		sum=int(a)+int(b)  
		print(sum)   
		return render_template('res.html', sum=sum)

	return render_template('home.html')



@app.route('/home/about')
def  about():
	return '<h2>About this new website<h2> '


if __name__=='__main__':
	app.run(debug=True)
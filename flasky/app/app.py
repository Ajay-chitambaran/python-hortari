from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__,template_folder="temp")
@app.route("/")
def hello():
	return "Hello-test-world!"
@app.route("/success")
def success(name,password):
	return user,passer
@app.route("/login",methods=['POST','GET'])
def input():
	if(request.method=='GET'):
		return render_template('login.html')
	if(request.method=='POST'):
		user=request.form['name']
		passer=request.form['pwd']	
		return redirect(url_for('success',name=user,pwd=passer))
#def web():
#	a=2
#	b=2	
#	sum=int(a)+int(b)
#	return render_template('hell.html',name=sum)
if __name__=="__main__":
	app.run()

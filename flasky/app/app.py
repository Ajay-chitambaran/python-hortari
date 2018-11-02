from flask import Flask,render_template
app = Flask(__name__,template_folder="temp")
@app.route("/")
def hello():
	return "Hello-test-world!"
@app.route("/hello")
def web():
	a=2
	b=2	
	sum=int(a)+int(b)
	return render_template('hell.html',name=sum)
if __name__=="__main__":
	app.run()

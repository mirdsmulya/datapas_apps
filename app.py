from flask import Flask,request,redirect, render_template, request, json


from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap =Bootstrap(app)


@app.route('/')
def home():
	return render_template('logging.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')


@app.route('/signUpreq',methods=['POST'])
def signUpreq():
 
    _username = request.form['inputUsername']
    _name = request.form['inputName']
    _password = request.form['inputPassword']	


    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})



if __name__ == '__main__':
	app.run()
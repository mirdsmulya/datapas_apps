from flask import Flask,request,redirect, render_template


from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap =Bootstrap(app)


@app.route('/')
def home():
	return render_template('logging.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')



if __name__ == '__main__':
	app.run()
from flask import Flask
from flask import render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html");

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template("signup.html")
    else:
	form = request.form
	s = str(form)
	s = s[20:-2].replace(", u'", ", '")
	fp = open('data','wb')
	fp.write(s + '\n')
	fp.close()
	if 'mail' in form.values():
	    print form['mail']
	return render_template("signup.html")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=80)


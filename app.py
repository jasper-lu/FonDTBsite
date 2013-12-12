from flask import Flask
from flask import render_template, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def sendemail(form):
    fp = open("text",'a+')
    msg = MIMEText(fp.read())
    fp.close()
    sub = ""
    if form['type'] == "Business":
	sub = sub + "Business | " + form['bname'] + " | "
    else:
	sub = sub + "Resident | " + form['name'] + " | "
    
    if 'mail' in form.values():
	sub = sub + "Mailing List"

    me = "jasper.lu@fon.com"
    to = "jasper.lu@fon.com"

    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to
    s = smtpbli.SMTP('localhost',1024)
    s.sendmail(me,[to],msg.as_string())
    s.quit()

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
	fp = open('data','a+')
	fp.write(s+"\n")
	fp.close()
	return redirect("/")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=80)


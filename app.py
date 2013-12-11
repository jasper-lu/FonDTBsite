from flask import Flask
from flask import render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def sendemail(form):
    fp = open(text,'rb')
    msg = MIMEText(fp.read())
    fp.close()
    sub = ""
    if form.type = "Business":
	sub = sub + "Business | " + form.bname + " | "
    else:
	sub = sub + "Resident | " + form.name + " | "
    
    if 'mail' in form.values():
	sub = sub + "Mailing List"

    me = "admin@dtb.fon.com"
    to = "jasper.lu@fon.com"

    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to
    s = smtplib.SMTP('localhost')
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
	fp = open('data','wb')
	fp.write(s + '\n')
	fp.close()
	sendemail(form)
	return render_template("signup.html")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=80)


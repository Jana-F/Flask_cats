from flask import Flask, render_template,request,redirect, url_for
from datetime import datetime

app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', datum=datum)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == '__main__':
    app.run()

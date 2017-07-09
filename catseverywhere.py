from flask import Flask, render_template,request,redirect, url_for
from datetime import datetime

app = Flask(__name__)

email_addresses = []
stranka = "/static/a.jpg"


@app.route('/')
def hello_world():
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', datum=datum)


@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')


@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)


@app.route('/static/b.jpg')
def link():
    if request.method == 'POST':
        return redirect(url_for('/static/b.jpg'))
    else:
        return render_template('/')


@app.route(stranka)
def test():
    if request.method == 'POST':
        return redirect(url_for(stranka))
    else:
        return render_template('/')


if __name__ == '__main__':
    app.run()

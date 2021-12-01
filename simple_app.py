# How to install FLASK in Windows 10
# https://www.osradar.com/how-to-install-flask-in-windows-10/

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    html = '<h1>G\'day mate!</h1>'
    html += '<p>How\'s the weather?</p>'
    html += '<p>It\'s sunny today!</p>' 
    return html 
#



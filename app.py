# Deploy Keras Neural Network To Flask Web Service | Part 3 - Send And Receive Data With Flask
# https://deeplizard.com/learn/video/RkmfXz304ck

from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello, ' + name + '!'
    }
    return jsonify(response)
# 


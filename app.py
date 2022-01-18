from flask import Flask, render_template, request, jsonify
import os, sys, requests, json
from random import randint

app = Flask(__name__)


@app.route('/')
def home():
    return "Page working"


@app.route('/parse', methods=['POST', 'GET'])
def extract():
    text = str(request.form.get('value1'))
    payload = json.dumps({"sender": "Rasa", "message": "i am sad"})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.request("POST", url="http://localhost:5005/webhooks/rest/webhook", headers=headers,
                                data=payload)
    response = response.json()
    print(response)
    resp = []
    for i in range(len(response)):
        try:
            resp.append(response[i]['text'])
        except:
            continue
    result = resp
    print(result)
    return "Successful"


if __name__ == "__main__":
    app.run(debug=True)

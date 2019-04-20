# handle post requests
import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != 'dubembot':
        # send message
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message(msg)

    return "ok", 200

def parse_message(msg):
    return

def send_message(command):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : command,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

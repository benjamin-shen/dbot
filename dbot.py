# http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/
# handle post requests
import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request
app = Flask(__name__)

# send message
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != 'dbot':
        send_message(create_message(parse_message(data['text'])))

    return "ok", 200

# helper functions
def send_message(to_send):
    url  = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : to_send,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
def parse_message(msg):
    return "hello"
def create_message(command):
    return "hello"
import time
import random

# handle post requests
import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request
app = Flask(__name__)

# dbot
import commands as dbot

# someone sends a message
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    time.sleep(1)
    name = data['name']
    text = data['text'].lower()
    
    if name != 'dbot':
        # call bot
        if text.startswith('dbot'):
            bot_action(text)
        # doesn't call bot
        else:
            for key,value in dbot.understandableDict.items():
                if key in text:
                    if key=='dick' or key=='penis':
                        length = random.randint(0,12)
                        if length==0:
                            send_message("vagina")
                        elif length==1:
                            send_message(str(length) + " inch")
                        else:
                            send_message(str(length) + " inches")
                    else:
                        text = value
                        while len(text) > 1000: # handle character limit
                            send_message(text[:1000])
                            text = text[1000:]
                        send_message(text);
    
    return "ok", 200

# main functions
def bot_action(received_text):
    if True: #
        create_message(parse_message(received_text))
def send_message(to_send):
    url  = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : to_send,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

# helper functions
def parse_message(msg):
    words = msg.split(" ")
    words.pop(0) # remove call to dbot
    responseArray = []
    for key in dbot.responseDict.keys():
        responseArray.append(key)
    commands = []
    for word in words:
        if word in responseArray:
            commands.append(word)
    return commands
def create_message(commands):
    if len(commands)==0:
        send_message("Try 'dbot help'.")
    else:
        for command in commands:
            if command=="help":
                send_message(dbot.help())
            elif command=="info":
                send_message(dbot.info())
            else:
                send_message("Error: incorrect parsing.")
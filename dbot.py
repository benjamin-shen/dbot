# http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/
# handle post requests
import os
import time
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request
app = Flask(__name__)

# dbot
responseDict = {
    'help': 'list commands dbot knows',
    'info': 'learn about dbot',
}
understandableDict = {
    'dbot': "I heard my name.",
    
}

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
            result = ""
            for key,value in understandableDict.items():
                if key in text:
                    result += value + "\n";
            if len(result) != 0:
                send_message(result)
    
    return "ok", 200

# main functions
def bot_action(received_text):
    if True: #
        send_message(create_message(parse_message(received_text)))
def send_message(to_send):
    url  = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : to_send,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
# do another action eg. tussle

# helper functions
def parse_message(msg):
    words = msg.split(" ")
    words.pop(0) # remove call to dbot
    responseArray = []
    for key in responseDict.keys():
        responseArray.append(key)
    commands = []
    for word in words:
        if word in responseArray:
            commands.append(word)
    return commands
def create_message(commands):
    if len(commands)==0:
        return "Try 'dbot help'."
    else:
        result = ""
        for command in commands:
            if command=="help":
                for key,value in responseDict.items():
                    result += key + " - " + value + "\n"
            elif command=="info":
                result += "dbot is a GroupMe bot created by Benjamin Shen '22. What does the d stand for? Go to https://github.com/benjamin-shen/dubembot to find out." + "\n"
            else:
                "Error: incorrect parsing."
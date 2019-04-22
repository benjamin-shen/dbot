import time
import random

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
        if text.startswith('dbot'): # bot is explicitly called
            bot_commanded(parse(received_text))
        else: # bot understands something
            bot_understood()
        if False: # bot is implicitly called
            return
    return "ok", 200

# functions
def parse(msg): # breaks down user message
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
def bot_commanded(commands):
    if len(commands)==0:
        dbot.send_message("Try 'dbot help'.")
    else:
        for command in commands:
            try:
                eval("dbot." + command + "()")
            except:
                dbot.send_message("Error: command not defined.")
def bot_understood():
    for key,value in dbot.understandableDict.items():
        if key in text:
            if key=='dick' or key=='penis':
                dbot.inches()
            else:
                text = value
                while len(text) > 1000: # handle character limit
                    dbot.send_message(text[:1000])
                    text = text[1000:]
                    time.sleep(0.1)
                dbot.send_message(text);

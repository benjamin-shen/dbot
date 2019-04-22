#flask
from flask import Flask, request
app = Flask(__name__)

# dbot
import commands as dbot
import time

# someone sends a message
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    time.sleep(1)
    name = data['name']
    text = data['text'].lower()

    if name != 'dbot':
        if text.startswith('dbot'): # bot is explicitly called
            bot_commanded(parse(text))
        else: # bot understands something
            bot_understood(text)
        if False: # bot is implicitly called
            return
    return "ok", 200

# bot functions
def parse(msg): # breaks down user message
    words = msg.split(" ")
    words.pop(0) # remove call to dbot
    commandArray = []
    for key in dbot.commandDict.keys():
        commandArray.append(key)
    commands = []
    for word in words:
        if word in commandArray:
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
def bot_understood(msg):
    for key,value in dbot.keywordDict.items():
        if key in msg:
            if key=='dick' or key=='penis':
                dbot.inches()
            else:
                result = value
                while len(result) > 1000: # handle character limit
                    i = result[:1000].rfind(" ") # don't split a character
                    if i != -1:
                        i += 1
                    else:
                        i = 1000
                    dbot.send_message(result[:i])
                    result = result[i:]
                    time.sleep(0.1)
                dbot.send_message(result);

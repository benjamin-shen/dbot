#flask
from flask import Flask, request
app = Flask(__name__)

# dbot
import commands as dbot
import time
dbot.send_message("Hello world! dbot is online.")

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
        if word in commandArray or word[:1]=='-' and commands[-1]+word in dbot.functions.keys():
            commands.append(word)
    return commands
def bot_commanded(commands):
    length = len(commands)
    if length==0:
        dbot.send_message("Try 'dbot help'.")
    else:
        i = 0
        while i<length:
            command = commands[i]
            j = 1
            if i+1==length or commands[i+1][:1]!='-': # no parameters
                dbot.send_message(dbot.functions[command])
            else:
                while i+j<length and commands[i+j][:1]=='-': # with parameters
                    dbot.send_message(dbot.functions[command+commands[i+j]])
                    j += 1
            i += j
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

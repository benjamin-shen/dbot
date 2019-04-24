# dbot
import commands as dbot
import time

#flask
from flask import Flask, request
app = Flask(__name__)

# someone sends a message and it directs to heroku,
# which hosts a server to interpret the data
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    text = data['text'].lower()

    time.sleep(1)
    if name != 'dbot':
        if text.startswith('dbot'): # bot is explicitly called
            bot_commanded(parse(text))
        else: # bot understands something
            bot_understood(text)
        if False: # bot is implicitly called
            return
    return "ok", 200

# text functions
def parse(msg): # breaks down user message
    words = msg.split()
    words.pop(0) # remove call to dbot
    commands = []
    i = 0
    while i<len(words):
        word = words[i]
        if word in dbot.commandDict.keys():
            commands.append(word)
        if len(commands)>0:
            # deal with parameters
            if word=='-' and i+1<len(words):
                param = word+words[i+1]
                if commands[-1]+param in dbot.functions.keys():
                    commands.append(param)
                    words.pop(i+1)
            elif word[:1]=='-' and commands[-1]+word in dbot.functions.keys():
                commands.append(word)
        i += 1
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
                dbot.send_message(dbot.functions[command]())
            else:
                param = commands[i+j]
                while i+j<length and param[:1]=='-': # with parameters
                    dbot.send_message(dbot.functions[command+param]())
                    j += 1
            i += j
def bot_understood(msg):
    for key,value in dbot.keywordDict.items():
        if key in msg:
            if key=='penis' or key=='dick' or key=='cock':
                dbot.send_message(dbot.inches())
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

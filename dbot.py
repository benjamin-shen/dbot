# dbot
import os
import commands as dbot
import time

#flask
from flask import Flask, request
app = Flask(__name__)

# someone sends a message and it directs to heroku,
# which hosts a server to interpret the data
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json() # equivalent to last_message
    text = data['text'].lower()

    if data['name'] != 'dbot':
        if text.startswith('dbot '): # bot is explicitly called
            bot_commanded(parse(text))
            return 'ok'
        for key in dbot.keywordDict.keys():
            msgdata = remove_mentions(text)
            if key in msgdata[0] and not key in msgdata[2]: # bot understands something
                bot_understood(key)
        return 'ok'
        # bot is implicitly called
        dbot.dclub()
    elif data['sender_id'] != os.getenv('GROUPME_DBOT'): # dbot imposter
        dbot.send_message("Who are you?!")
    return 'ok'

# text functions
def remove_mentions(msg):
    nicknames = dbot.get_memberids().keys()
    mentioned = []
    names = ""
    for nickname in nicknames:
        name = nickname.lower()
        if name!='dbot':
            mention = '@' + name.lower()
            if mention in msg:
                mentioned.append(nickname)
                msg = msg.replace(mention,'') # remove mention from text
            if name in msg:
                names += name + ","
    return msg, mentioned, names
def parse(text): # breaks down user message
    msg = remove_mentions(text)[0]
    mentioned = remove_mentions(text)[1]
    words = msg.split()
    words.pop(0) # remove call to dbot
    commands = []
    i = 0
    while i<len(words):
        word = words[i]
        if word=='tussle' and dbot.tussle(mentioned):
            commands.append(word)
        else:
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
        return 'ok'
    i = 0
    while i<length:
        j = 1
        command = commands[i]
        if i+1==length or commands[i+1][:1]!='-': # no parameters
            dbot.functions[command]()
        else:
            param = commands[i+j]
            while i+j<length and param[:1]=='-': # with parameters
                dbot.functions[command+param]()
                j += 1
        i += j
    return 'ok'
def bot_understood(keyword):
    if keyword=='penis' or keyword=='dick' or keyword=='cock':
        dbot.inches()
    else:
        result = dbot.keywordDict[keyword]
        while len(result) > 1000: # handle character limit
            i = result[:1000].rfind(" ") # don't split a character
            if i != -1:
                i += 1
            else:
                i = 1000
            dbot.send_message(result[:i])
            result = result[i:]
        dbot.send_message(result);
    return 'ok'

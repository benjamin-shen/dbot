# dbot
import commands as dbot
import os
import random
import time

#flask
from flask import Flask, request
app = Flask(__name__)

# someone sends a message and it directs to heroku,
# which hosts a server to interpret the data
@app.route('/', methods=['POST'])
def webhook():
    time.sleep(1)
    data = request.get_json() # equivalent to last_message
    text = data['text'].lower()
    result = []
    if data['sender_type'] == 'user':
        if text.startswith('dbot '): # bot is explicitly called
            result = [bot_commanded(parse(text))]
        else:
            msgdata = remove_mentions(text)
            msg = msgdata[0]
            mentioned = msgdata[1]
            if dbot.message_cooldown():
                for key in dbot.keywordDict.keys():
                    if key in msg and not (key in str(mentioned)): # bot understands something
                        result.append(bot_understood(key))
        # bot is implicitly called
        dclub = dbot.dclub()
        if dclub != "":
            result.append(dclub)
    elif data['name'] == 'dbot' and data['sender_id'] != os.getenv('GROUPME_DBOT'): # dbot imposter
        message = "Who are you?!"
        dbot.send_message(message)
        result = [message]
    return result

# text functions
def remove_mentions(text):
    nicknames = dbot.get_memberids().keys()
    msg = text
    mentioned = []
    for nickname in nicknames:
        if nickname.lower()!='dbot':
            mention = '@' + nickname.lower()
            if mention in text:
                mentioned.append(nickname)
                msg = msg.replace(mention,'') # remove mention from text
    return msg, mentioned
def parse(text): # breaks down user message
    msgdata = remove_mentions(text)
    msg = msgdata[0]
    mentioned = msgdata[1]
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
        message = "Try 'dbot help'."
        dbot.send_message(message)
        return [message]
    i = 0
    result = []
    while i<length:
        j = 1
        command = commands[i]
        if i+1==length or commands[i+1][:1]!='-': # no parameters
            result.append(dbot.functions[command]())
        else:
            param = commands[i+j]
            while i+j<length and param[:1]=='-': # with parameters
                result.append(dbot.functions[command+param]())
                j += 1
        i += j
    return result
def bot_understood(keyword):
    if keyword=='dick' and random.randint(1,10) <= 1:
        result = dbot.dick()
    elif keyword=='asshole' and random.randint(1,10) <= 1:
        result = dbot.asshole()
    else:
        result = dbot.keywordDict[keyword]
        dbot.send_message(result)
    return [result]

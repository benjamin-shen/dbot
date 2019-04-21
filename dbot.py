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
    'help': "list the commands I know",
    'info': "learn about me",
    '[name]': "glozz member isms"
}
understandableDict = {
    'dbot': "I heard my name.",
    'julia adolphe': "All hail the Skylord!",
    'steve': "Dr. Steeeeve!",
    'tour': "Yeah tour!",
    'general': "*salute*",
    'werewolf': "Werewolf?",
    
    
    'fuck': "Watch your fucking language. (Did you mean to say 'duck'?)",
    'bitch': "",
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
            for key,value in understandableDict.items():
                if key in text:
                    if key=='bitch':
                        send_message("What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. ")
                        send_message("Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.")
                    else:
                        send_message(value);
    
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
        send_message("Try 'dbot help'.")
    else:
        for command in commands:
            if command=="help":
                for key,value in responseDict.items():
                    send_message("dbot " + key + " - " + value)
            elif command=="info":
                send_message("dbot is a GroupMe bot created by Ben Shen '22. The d stands for Douglas.")
            else:
                send_message("Error: incorrect parsing.")
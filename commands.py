import random

import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# interpret text files
commandDict = {}
with open('dictionaries/commands.txt', 'r') as file:
    responseArray = file.readlines()
    for line in responseArray:
        colon = line.find(':')
        if colon != -1:
            keyword = line[:colon]
            response = line[colon+1:].strip() # remove white space
            commandDict[keyword] = response
keywordDict = {}
with open('dictionaries/keywords.txt', 'r') as file:
    keywordArray = file.readlines()
    for line in keywordArray:
        colon = line.find(':')
        if colon != -1:
            keyword = line[:colon]
            response = line[colon+1:].strip() # remove white space
            keywordDict[keyword] = response

# GroupMe functions
def send_message(to_send):
    url  = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : to_send,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

# commands
def help():
    result = ""
    for key,value in commandDict.items():
        result += "dbot " + key + ": " + value + "\n"
    send_message(result)
    return result
def info():
    result = "dbot is a GroupMe bot created by Ben Shen '22. The d stands for Douglas."
    send_message(result)
    return result
def glozz():
    glozz = []
    with open('members/glozzSA.txt', 'r') as file:
        glozzSA = file.readlines()
        for line in glozzSA:
            name = line.strip()
            if len(name) > 0: # verify name is valid
                #ignore post-comma text
                i = name.find(",")
                name = name[:i]
                members.push(name)
    with open('members/glozzTB.txt', 'r') as file:
        glozzTB = file.readlines()
        for line in glozzTB:
            name = line.strip()
            if len(name) > 0: # verify name is valid
                members.push(name)
    result = ""
    for member in glozz:
        result += member + "\n"
    send_message(result)

# special keywords
def inches():
    length = random.randint(0,12)
    result = ""
    if length==0:
        result = "vagina"
    elif length==1:
        result = str(length) + " inch"
    else:
        result = str(length) + " inches"
    send_message(result)
    return result

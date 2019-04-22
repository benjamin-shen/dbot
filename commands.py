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
        'text'   : to_send.strip(),
    }
    try:
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()
    except:
        print("Error: send failed.")

# commands
def d_help():
    result = ""
    for key,value in commandDict.items():
        result += "dbot " + key + ": " + value + "\n"
    return result
def info():
    result = "dbot is a GroupMe bot created by Ben Shen '22. The d stands for Douglas."
    return result
def glozz(p):
    glozz = []
    with open('members/glozzSA.txt', 'r') as file:
        glozzSA = file.readlines()
        for line in glozzSA:
            name = line.strip()
            if len(name) > 0: # verify name is valid
                i = name.find(",")
                if i != -1:
                    name = name[:i] # ignore post-comma text
                glozz.append(name)
    with open('members/glozzTB.txt', 'r') as file:
        glozzTB = file.readlines()
        for line in glozzTB:
            name = line.strip()
            if len(name) > 0: # verify name is valid
                i = name.find(",")
                if i != -1:
                    name = name[:i] # ignore post-comma text
                glozz.append(name)
    result = []
    if p<3:
        for member in glozz:
            i = member.find(":")
            if i != -1:
                result.append(member[:i])
            else:
                result.append(member)
        if p==1: # alphabetize
            result.sort()
        elif p==2: # randomize
            random.shuffle(result)
        return "\n".join(result)
    elif p==3: # ism
        for member in glozz:
            i = member.find('"')+1
            j = member.find('"', i)
            if i != -1 and j != -1:
                result.append(member[:j])
        return "No one:\n" + random.choice(result)
    else:
        return "Error: invalid parameter"

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
    return result

# function dictionary
functions = {
    "help": d_help(),
    "info": info(),
    "glozz": glozz(0),
    "glozz-alphabetize": glozz(1),
    "glozz-randomize": glozz(2),
    "glozz-ism": glozz(3),
}

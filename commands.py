# dbot
import random
from datetime import datetime
import pytz
import requests

# access GroupMe
import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# config vars
access_token = 0
bot_id = 0
group_id = 0
def vars(): # init config variables
    global access_token
    global bot_id
    global group_id
    access_token = os.getenv('GROUPME_TOKEN')
    bot_id = os.getenv('GROUPME_BOT_ID')
    group_id = os.getenv('GROUPME_GROUP_ID')

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
    vars()
    url  = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id' : bot_id,
        'text'   : to_send.strip(),
    }
    try:
        request = Request(url, urlencode(data).encode())
        json = urlopen(request).read().decode()
    except:
        print("Error: send failed.")
def get_messages():
    vars()
    sent = ""
    messages = requests.get('https://api.groupme.com/v3/groups/'+group_id+'/messages?token='+access_token).json()['response']['messages']
    return messages # list of dictionaries; last 20 messages
msg = get_messages()[0]
name = msg['name']
id = msg['sender_id']
text = msg['text']

# commands
def d_help():
    result = ""
    for key,value in commandDict.items():
        result += "dbot " + key + ": " + value + "\n\n"
    return result
def d_help_1():
    result = "'[command] -[parameter]' or '[command] - [parameter]' executes the command with a parameter. Invalid syntax is ignored. Invalid parameters are ignored.\n"
    result += "dbot can only recognize one parameter per command.\n"
    result += "Keywords, regardless of white space, will trigger dbot to respond. Try to discover them all! The list of understood keywords is updated frequently."
    return result
def d_help_2():
    result = "https://github.com/benjamin-shen/dbot"
    return result
def info():
    result = "dbot is a GroupMe bot that responds to commands and recognizes keywords. The d stands for Douglas."
    return result
def info_1():
    result = "dbot is created and managed by Benjamin Shen '22."
    return result
def hello():
    result = "Hello, " + name + "."
    return result
def time():
    result = ""
    now = datetime.now(pytz.timezone('US/Eastern'))
    day = now.strftime('%w')
    hour = now.strftime('%I')
    min = now.strftime('%M')
    ampm = now.strftime('%p')
    if day==2 and 4<int(hour) and int(hour)<8:
        result += "Come to RPCC!\n"
    elif day==3:
        result += "Happy Wednesday!\n"
    result += "It is currently " + hour + ":" + min + " " + ampm + "."
    return result
def time_1():
    result = ""
    now = datetime.now(pytz.timezone('US/Eastern'))
    day = now.strftime('%A')
    date = now.strftime('%x')
    result += "Today is " + day + ", " + date + "."
    return result
def dinner():
    result = ""
    halls = ['RPCC','Appel','Risley','Okenshields','Becker','Bethe','Cook','Keeton','Rose']
    result += random.choice(halls)
    return result
def dinner_1():
    result = ""
    halls = ['Becker','Bethe','Cook','Keeton','Rose']
    result += random.choice(halls)
    return result
from bus import stop1701
def bus():
    result = ""
    time = stop1701.next()
    if time==None:
        result += "https://realtimetcatbus.availtec.com/InfoPoint/Stops/Stop/1701 is down."
    elif time=='':
        result += "No 90 buses anytime soon. Try Google Maps."
    else:
        result += "The next 90 is at " + time + "."
    return result
def glozz():
    glozz = []
    with open('members/glozzSA.txt', 'r') as file:
        glozzSA = file.readlines()
        for line in glozzSA:
            name = line.strip()
            if len(name) > 0: # verify name is valid
                i = name.find("//")
                if i != -1:
                    name = name[:i] # ignore comment
                glozz.append(name)
    with open('members/glozzTB.txt', 'r') as file:
        glozzTB = file.readlines()
        for line in glozzTB:
            name = line.strip()
            if len(name) > 0: # verify name is valid
                i = name.find("//")
                if i != -1:
                    name = name[:i] # ignore comment
                glozz.append(name)
    return glozz
def glozz_0():
    result = []
    for member in glozz():
        i = member.find(":")
        if i != -1:
            result.append(member[:i])
        else:
            result.append(member)
    return "\n".join(result)
def glozz_1():
    result = []
    for member in glozz():
        i = member.find(":")
        if i != -1:
            result.append(member[:i])
        else:
            result.append(member)
    result.sort()
    return "\n".join(result)
def glozz_2():
    result = []
    for member in glozz():
        i = member.find(":")
        if i != -1:
            result.append(member[:i])
        else:
            result.append(member)
    random.shuffle(glozz)
    return "\n".join(result)
def glozz_3():
    result = []
    for member in glozz():
        if (member.find('"') != -1):
            result.append(member)
    return "No one:\n" + random.choice(result)

# special keywords
def inches():
    length = random.randint(0,12)
    result = "("
    if length==0:
        result += "so small it can't be detected by an electron microscope"
    elif length==12:
        result += "ever deepthroat a footlong?"
    elif length==1:
        result += str(length) + " inch"
    else:
        result += str(length) + " inches"
    result += ")"
    return result

# function dictionary
functions = {
    "help": d_help,
    "help-syntax": d_help_1,
    "help-github": d_help_2,
    "info": info,
    "info-creator": info_1,
    "hello": hello,
    "time": time,
    "time-day": time_1,
    "dinner": dinner,
    "dinner-west": dinner_1,
    "bus": bus,
    "glozz": glozz_0,
    "glozz-alphabetize": glozz_1,
    "glozz-randomize": glozz_2,
    "glozz-ism": glozz_3,
}

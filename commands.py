# dbot
import random
import time
from datetime import datetime
import pytz
import requests

# access GroupMe
import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# config vars
access_token = 'error'
bot_id = 'error'
group_id = 'error'
def vars(): # init config variables
    global access_token
    global bot_id
    global group_id
    access_token = os.getenv('GROUPME_TOKEN')
    bot_id = os.getenv('GROUPME_BOT_ID')
    group_id = os.getenv('GROUPME_GROUP_ID')
    if access_token=='error' or bot_id=='error' or group_id=='error':
        return 'error'
    return 'ok'

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
    time.sleep(1)
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
        return 'error'
def get_messages():
    vars()
    sent = ""
    messages = requests.get('https://api.groupme.com/v3/groups/'+group_id+'/messages?token='+access_token).json()['response']['messages']
    return messages # list of dictionaries; last 20 messages
def last_message(key):
    result = ""
    msg = get_messages()[0]
    try:
        result += msg[key]
    except:
        result += "Error: couldn't handle request"
    return result
def get_members():
    vars()
    sent = ""
    members = requests.get('https://api.groupme.com/v3/groups/'+group_id+'?token='+access_token).json()['response']['members']
    return members
def get_memberids():
    result = {}
    members = get_members()
    for member in members:
        nickname = member['nickname']
        id = member['id']
        user_id = member['user_id']
        result[nickname] = {'id':id,'user_id':user_id}
    return result
def kick_member(memberid):
    vars()
    data = {
        'membership_id': memberid,
    }
    requests.post('https://api.groupme.com/v3/groups/'+group_id+'/members/'+memberid+'/remove?token='+access_token, json=data)
def add_member(nickname,userid):
    vars()
    data = {
        'members': [{
            'nickname': nickname,
            'user_id':  userid,
        }]
    }
    requests.post('https://api.groupme.com/v3/groups/'+group_id+'/members/add?token='+access_token, json=data)

# basic commands
def d_help():
    result = ""
    for key,value in commandDict.items():
        result += "dbot " + key + ": " + value + "\n\n"
    send_message(result)
    return result
def d_help_1():
    result = "'[command] -[parameter]' or '[command] - [parameter]' executes the command with a parameter. Invalid syntax is ignored. Invalid parameters are ignored.\n"
    result += "dbot can only recognize one parameter per command.\n"
    result += "Keywords, regardless of white space, will trigger dbot to respond. Try to discover them all! The list of understood keywords is updated frequently."
    send_message(result)
    return result
def d_help_2():
    result = "https://github.com/benjamin-shen/dbot"
    send_message(result)
    return result
def info():
    result = "dbot is a GroupMe bot that responds to commands and recognizes keywords. The d stands for Douglas."
    send_message(result)
    return result
def info_1():
    result = "dbot is created and managed by Benjamin Shen '22."
    send_message(result)
    return result
def hello():
    result = "Hello, " + last_message('name') + "."
    send_message(result)
    return result
def time_0():
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
    send_message(result)
    return result
def time_1():
    result = ""
    now = datetime.now(pytz.timezone('US/Eastern'))
    day = now.strftime('%A')
    date = now.strftime('%x')
    result += "Today is " + day + ", " + date + "."
    send_message(result)
    return result
def dinner():
    result = ""
    halls = ['RPCC','Appel','Risley','Okenshields','Becker','Bethe','Cook','Keeton','Rose']
    result += random.choice(halls)
    send_message(result)
    return result
def dinner_1():
    result = ""
    halls = ['Becker','Bethe','Cook','Keeton','Rose']
    result += random.choice(halls)
    send_message(result)
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
    send_message(result)
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
    members = []
    for member in glozz():
        i = member.find(":")
        if i != -1:
            members.append(member[:i])
        else:
            members.append(member)
    result = "\n".join(members)
    send_message(result)
    return result
def glozz_1():
    members = []
    for member in glozz():
        i = member.find(":")
        if i != -1:
            members.append(member[:i])
        else:
            members.append(member)
    members.sort()
    result = "\n".join(members)
    send_message(result)
    return result
def glozz_2():
    members = []
    for member in glozz():
        i = member.find(":")
        if i != -1:
            members.append(member[:i])
        else:
            members.append(member)
    random.shuffle(members)
    result = "\n".join(members)
    send_message(result)
    return result
def glozz_3():
    members = []
    for member in glozz():
        i = member.find(":")
        if i != -1:
            members.append(member[:i])
        else:
            members.append(member)
    result = random.choice(members)
    send_message(result)
    return result
def glozz_4():
    isms = []
    for member in glozz():
        if (member.find('"') != -1):
            isms.append(member)
    result = "No one:\n" + random.choice(isms)
    send_message(result)
    return result
def tussle_0():
    result = ""
    return result

# function dictionary
functions = {
    "help": d_help,
    "help-syntax": d_help_1,
    "help-github": d_help_2,
    "info": info,
    "info-creator": info_1,
    "hello": hello,
    "time": time_0,
    "time-day": time_1,
    "dinner": dinner,
    "dinner-west": dinner_1,
    "bus": bus,
    "glozz": glozz_0,
    "glozz-alphabetize": glozz_1,
    "glozz-randomize": glozz_2,
    "glozz-single": glozz_3,
    "glozz-ism": glozz_4,
    "tussle": tussle_0,
}

# other commands
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
    send_message(result)
    return result
def tussle(participants):
    tusslers = participants
    tusslers.append(last_message('nickname'))
    random.shuffle(tusslers)
    for nickname in tusslers:
        if nickname in get_memberids().keys(): # verify valid mentions
            id = get_memberids()[nickname]['id']
            user_id = get_memberids()[nickname]['user_id']
            kick_member(id)
            time.sleep(5)
            add_member(nickname,user_id)
            return 'ok'
    return 'error'

# implicit commands
def dclub():
    result = ""
    chance = random.randint(1,100)
    if chance<=5:
        id = last_message('sender_id')
        if id=='43405903': # Dubem
            result += "We have " + str(random.randint(1,4)) + " out of 4 voice parts."
        elif id=='62752724': # Benjamin
            result += "Daddy made me say this."
        elif id=='49904547': # Lucas
            result += "Yoshi!"
        elif id=='26134002': # Nate
            result += "Careful, that's Natebot."
        elif id=='43418465': # Aidan
            result += "CORRECT."
    if result != "":
        # send_message(result)
        send_message(result)
    return result

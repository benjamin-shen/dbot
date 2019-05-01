# dbot
from bus import stop1701
import random
import time
from datetime import datetime
import pytz
import pyowm
from googletrans import Translator

# access GroupMe
import requests
import os
import json

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
    result = to_send
    while len(result) > 1000: # handle character limit
        i = result[:1000].rfind(" ") # don't split a character
        if i != -1:
            i += 1
        else:
            i = 1000
        send_shortmessage(result[:i])
        result = result[i:]
    send_shortmessage(result)
    return to_send
def send_shortmessage(to_send):
    url  = 'https://api.groupme.com/v3/bots/post?token=' + access_token
    data = {
        'bot_id' : bot_id,
        'text'   : to_send.strip(),
    }
    requests.post(url, json=data) # send message via post
def get_messages():
    vars()
    url = 'https://api.groupme.com/v3/groups/'+group_id+'/messages?token='+access_token
    messages = requests.get(url).json()['response']['messages']
    return messages # list of 20 dictionaries
def last_message(key):
    result = ""
    msg = get_messages()[0]
    try:
        result += msg[key]
    except:
        result += "Error: couldn't handle request"
    return result
def get_creator():
    vars()
    url = 'https://api.groupme.com/v3/groups/'+group_id+'?token='+access_token
    creatorid = requests.get(url).json()['response']['creator_user_id']
    return creatorid
def get_members():
    vars()
    url = 'https://api.groupme.com/v3/groups/'+group_id+'?token='+access_token
    members = requests.get(url).json()['response']['members']
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
    time.sleep(2)
    vars()
    url = 'https://api.groupme.com/v3/groups/'+group_id+'/members/'+memberid+'/remove?token='+access_token
    data = {
        'membership_id': memberid,
    }
    kicked = requests.post(url, json=data)
    return kicked
def add_member(nickname,userid):
    time.sleep(2)
    vars()
    url = 'https://api.groupme.com/v3/groups/'+group_id+'/members/add?token='+access_token
    data = {
        'members': [{
            'nickname': nickname,
            'user_id':  userid,
        }]
    }
    added = requests.post(url, json=data)
    return added

# basic commands
def d_help_0():
    result = ""
    for key,value in commandDict.items():
        result += "dbot " + key + ": " + value + "\n\n"
    send_message(result)
    return result
def d_help_1():
    result = "'dbot [command]' or \n'dbot [command] -[parameter]' or \n'dbot [command] - [parameter]' \nexecutes the command with a parameter. Invalid syntax is ignored. Invalid parameters are ignored.\n"
    result += "dbot can only recognize one parameter per command.\n"
    result += "Keywords, regardless of white space, will trigger dbot to respond. Try to discover them all! The list of understood keywords is updated frequently."
    send_message(result)
    return result
def info_0():
    result = "dbot is a GroupMe bot that responds to commands and recognizes keywords. The d stands for Douglas. The profile picture is GORT."
    send_message(result)
    return result
def info_1():
    result = "dbot is created and managed by Benjamin Shen '22."
    send_message(result)
    return result
def info_2():
    result = "https://github.com/benjamin-shen/dbot"
    send_message(result)
    return result
def hello():
    result = "Hello, " + last_message('name') + "."
    send_message(result)
    return result
def glozz():
    glozz = []
    with open('members/glozzSA.txt', 'r') as file:
        glozzSA = file.readlines()
        for line in glozzSA:
            name = line.strip()
            if len(name) > 0: # verify name is valid
                i = name.find("|")
                if i != -1:
                    name = name[:i] # ignore comment
                glozz.append(name)
    with open('members/glozzTB.txt', 'r') as file:
        glozzTB = file.readlines()
        for line in glozzTB:
            name = line.strip()
            if len(name) > 0: # verify name is valid
                i = name.find("|")
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
        if (member.find(':') != -1):
            isms.append(member)
    result = "No one:\n" + random.choice(isms)
    send_message(result)
    return result
def dinner_0():
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
def dinner_2():
    result = ""
    halls = ['RPCC','Appel','Risley']
    result += random.choice(halls)
    send_message(result)
    return result
def time_0():
    result = ""
    now = datetime.now()
    est = now.astimezone(pytz.timezone('US/Eastern'))
    day = est.strftime('%w')
    hour = est.strftime('%I')
    min = est.strftime('%M')
    ampm = est.strftime('%p')
    if day=='2':
        firstappearance = datetime(2019,3,5)
        delta = now-firstappearance
        if delta.days%14 == 1:
            result += "Say hi to Reginald!\n"
    elif day=='3':
        result += "Happy Wednesday!\n"
    result += "It is currently " + hour + ":" + min + " " + ampm + "."
    send_message(result)
    return result
def time_1():
    result = ""
    now = datetime.now()
    est = now.astimezone(pytz.timezone('US/Eastern'))
    day = est.strftime('%A')
    date = est.strftime('%x')
    result += "Today is " + day + ", " + date + "."
    send_message(result)
    return result
def weather():
    owm = pyowm.OWM(os.getenv('WEATHER_APIKEY'))
    return owm
def weather_0():
    result = ""
    data = weather().weather_at_coords(42.451309,-76.482068).get_weather()
    status = data.get_detailed_status()
    temperature = data.get_temperature('fahrenheit')
    temp = str(temperature['temp'])
    low = str(temperature['temp_min'])
    high = str(temperature['temp_max'])
    result += status + ", currently " + temp + "F\n"
    result += "high of " + high + ", low of " + low
    send_message(result)
    return result
def weather_1():
    result = ""
    data = requests.get('https://api.weather.gov/gridpoints/BGM/44,69/forecast').json()
    forecasts = data['properties']['periods']
    for weather in forecasts:
        result += weather['name'] + ": " + weather['shortForecast'] + ", " + str(weather['temperature']) + "F\n"
    send_message(result)
    return result
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
def translate(text):
    result = ""
    translator = Translator()
    lang = translator.detect(text).lang
    if lang != 'en':
        result += translator.translate(text).text
    return result, lang
def translate_0():
    result = ""
    message = get_messages()[1]
    name = message['name']
    text = message['text']
    translated_text = translate(text)[0]
    if translated_text != "":
        result += name + ": " + translated_text
    else:
        result += "This shit's in English, dude."
    send_message(result)
    return result
def translate_1():
    result = ""
    messages = get_messages()
    for message in messages[len(messages)-1:0:-1]:
        name = message['name']
        text = message['text']
        translated = translate(text)
        if translated[1] != 'en':
            result += name + ": " + translate(text)[0] + " (" + text + ")\n"
    if result != "":
        send_message(result)
    return result
def identify():
    result = ""
    message = get_messages()[1]
    if message['sender_id'] == os.getenv('GROUPME_DBOT'):
        result += "Hi, I'm dbot!"
    elif message['sender_type'] == 'bot':
        result += "It's another bot!"
    elif message['sender_type'] == 'user':
        nickname = message['name']
        text = message['text']
        members = get_members()
        for member in members:
            if member['nickname']==nickname:
                result += member['name']
                result += ": " + text
                break
    else:
        result += "Try 'dbot help'."
    send_message(result)
    return result
def tussle_0():
    result = "Tussle attempted."
    return result

# function dictionary
functions = {
    "help": d_help_0,
    "help-syntax": d_help_1,
    "info": info_0,
    "info-creator": info_1,
    "info-github": info_2,
    "hello": hello,
    "glozz": glozz_0,
    "glozz-alphabetize": glozz_1,
    "glozz-randomize": glozz_2,
    "glozz-single": glozz_3,
    "glozz-ism": glozz_4,
    "dinner": dinner_0,
    "dinner-west": dinner_1,
    "dinner-north": dinner_2,
    "time": time_0,
    "time-day": time_1,
    "weather": weather_0,
    "weather-forecast": weather_1,
    "bus": bus,
    "translate": translate_0,
    "translate-all": translate_1,
    "identify": identify,
    "tussle": tussle_0,
}

# other commands
def dick():
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
def asshole():
    name = last_message('name')
    result = name + " is a "
    chance = random.randint(1,2)
    if chance==1:
        result += "real nice guy."
    else:
        result += "horse's ass."
    send_message(result)
    return result
def tussle(participants):
    tusslers = participants
    memberids = get_memberids()
    initiatorid = last_message('user_id')
    initiator = 'a ghost'
    for nickname,ids in memberids.items():
        user_id = ids['user_id']
        if user_id=='62752724' or user_id==get_creator(): # bot owner, group creator can't be kicked!
            i = 0
            while i<len(tusslers):
                if tusslers[i]==nickname:
                    tusslers.pop(i)
                else:
                    i += 1
            if user_id==initiatorid:
                initiator = nickname
        elif user_id==initiatorid:
            initiator = nickname
            tusslers.append(nickname)
    random.shuffle(tusslers)
    for nickname in tusslers:
        if nickname in memberids.keys(): # verify valid mentions
            member = memberids[nickname]
            id = member['id']
            user_id = member['user_id']
            if user_id==initiatorid:
                send_message(nickname + " tripped and punched himself in the face.")
            else:
                send_message(nickname + " was bested by " + initiator + "!")
            if kick_member(id):
                add_member(nickname,user_id)
            return True
    send_message("Try 'dbot help'.")
    return False

# implicit commands
def dclub():
    result = ""
    chance = random.randint(1,50)
    if chance<=1:
        id = last_message('sender_id')
        if id=='43405903': # Dubem
            result = "We have " + str(random.randint(1,4)) + " out of 4 voice parts."
        elif id=='62752724': # Benjamin
            result = "Daddy made me say this."
        elif id=='49904547': # Lucas
            result = "Yoshi!"
        elif id=='26134002': # Nate
            result = "Careful, that's Natebot."
        elif id=='43418465': # Aidan
            result = "CORRECT."
        if result!="":
            send_message(result)
    return result

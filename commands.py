import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# interpret text files
responseDict = {}
with open('dictionaries/response.txt', 'r') as file:
    responseArray = file.readlines()
    for line in responseArray:
        colon = line.find(':')
        if colon != -1:
            keyword = line[:colon]
            response = line[colon+1:].strip() # remove white space
            responseDict[keyword] = response
understandableDict = {}
with open('dictionaries/understandable.txt', 'r') as file:
    understandableArray = file.readlines()
    for line in understandableArray:
        colon = line.find(':')
        if colon != -1:
            keyword = line[:colon]
            response = line[colon+1:].strip() # remove white space
            understandableDict[keyword] = response

# GroupMe functions
def send_message(to_send):
    url  = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : to_send,
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

# response
def help():
    result = ""
    for key,value in responseDict.items():
        result += "dbot " + key + " - " + value + "\n"
    send_message(result)
    return result
def info():
    result = "dbot is a GroupMe bot created by Ben Shen '22. The d stands for Douglas."
    send_message(result)
    return result
# understandable
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

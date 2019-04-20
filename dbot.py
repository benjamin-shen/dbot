import requests
import time

# get port
from flask import Flask
port = int(os.environ.get('PORT', 5000))

# groupme variables
request_params = {'token': 'Y9KfQe7ICjWtWFZjmFc5RL78yB4F2X4AeWWbEpfS'}
group_id = '48976167'
bot_id = '021293724be9d5473e3a2dec3a'

while True:
    response = requests.get('https://api.groupme.com/v3/groups/' + group_id + '/messages', params = request_params)
    if (response.status_code == 200):
        response_messages = response.json()['response']['messages']
    
    for message in response_messages:
        if (message['text'] == 'dbot'):
            
            # message
            to_send = 'I hear my name'
            
            # send to bot
            post_params = { 'bot_id' : bot_id, 'text': to_send }
            requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
            request_params['since_id'] = message['id']
            break
            
    time.sleep(3)
# dbot
Written by Benjamin Shen

## Functionality
All possible commands can be found in [response.txt](dictionaries/response.txt).  
All recognized keywords can be found in [understandable.txt](dictionaries/understandable.txt).  

### Bugs
There is an occasional delay in the bot's response.  
The GroupMe on PC sometimes displays messages in the wrong order.  

### Warnings
If you are modifying the code, keep in mind that  
- I use `eval()` in [dbot.py](dbot.py).  
- there are `print()` statements in [commands.py](commands.py) for debugging.
- some keywords/responses are inappropriate for the general public. Please keep in mind your target group.  

#### Inspiration
- Dubem Ogwulumba for the name inspiration and helpful input on bot commands
- The rest of D Club and GLOZZ for participating in this project
- Collin Montag for creating mbot (MasterBot) and encouraging the creation of dbot

#### Credit
1. [This article by Joshua B](http://sweb.uky.edu/~jtba252/index.php/2017/09/13/how-to-write-a-groupme-bot-using-python/) helped me get accustomed to python and writing a locally hosted bot.  
2. [This article by apnorton](http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/) helped me get started with the code I wanted to deploy.  
3. [This tutorial by Michael K](https://github.com/michaelkrukov/heroku-python-script) helped me deploy the python app to heroku (a cloud platform).  

#### Links
[GroupMe for developers](https://dev.groupme.com)  
[GroupMe Public API](https://dev.groupme.com/docs/v3)  
[heroku](https://www.heroku.com)  

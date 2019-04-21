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
            
# responseDict = {
    # 'help': "list the commands I know",
    # 'info': "learn about me",
    # '[name]': "glozz member isms"
# }

# understandableDict = {
    # 'dbot': "I heard my name.",
    # 'julia adolphe': "All hail the Skylord!",
    # 'steve': "Dr. Steeeeve!",
    # 'tour': "Yeah tour!",
    # 'general': "*salute*",
    # 'werewolf': "Werewolf?",
    
    
    # 'fuck': "Watch your fucking language. (Did you mean to say 'duck'?)",
    # 'bitch': "",
    # 'dick': "",
    # 'penis': "",
# }

def help():
    result = ""
    for key,value in responseDict.items():
        result += "dbot " + key + " - " + value + "\n"
    return result
def info():
    return "dbot is a GroupMe bot created by Ben Shen '22. The d stands for Douglas."
    
    
# testing
print(understandableDict)
print(help())
print(info())
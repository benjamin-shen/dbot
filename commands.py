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
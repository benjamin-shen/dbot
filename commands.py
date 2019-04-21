responseDict = {
    'help': "list the commands I know",
    'info': "learn about me",
    '[name]': "glozz member isms"
}

def help():
    result = ""
    for key,value in responseDict.items():
        result += "dbot " + key + " - " + value + "\n"
    return result
def info():
    return "dbot is a GroupMe bot created by Ben Shen '22. The d stands for Douglas."
    
    
# testing
print(help())
print(info())
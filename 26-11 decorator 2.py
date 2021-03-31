def makeBold(printMsg):       #Decorator
    def boldLogic():
        return "<b>"+printMsg()+"</b>"
    return boldLogic

def makeItalic(printMsg):       #Decorator
    def italicLogic():
        return "<i>"+printMsg()+"</i>"
    return italicLogic

@makeBold
@makeItalic
def printMsg():
    return "Hello world"

print(printMsg())

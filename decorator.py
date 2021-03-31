""" decorator """

"""def outer():
    print("Outer function invoked")
    def inner():
        print("Inner function invoked")
    return inner

res=outer()
print(res())"""




"""def printMsg():
    print("Hello")
    
printMsg()


def parent(msg):
    return msg()

test=parent(printMsg)
test()                   """


def printMsg():
    return "Hello world"


def makeBold(printMsg):       #Decorator
    def boldLogic():
        return "<b>"+printMsg()+"</b>"
    return boldLogic

res=makeBold(printMsg)

print(res())
print(printMsg())








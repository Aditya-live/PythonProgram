"""FProgram for infinite fobonacci series"""


def myfibo():
    a,b=0,1
    while(True):
        yield(a)
        a,b=b,a+b


print(myfibo())


#For limiting the res

def myfibo():
    a,b=0,1
    while(a<10):
        yield(a)
        a,b=b,a+b


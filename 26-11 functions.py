
"""def testarg(a,b,c=30,*d):
    print(a,b,c)
    for i in d:
        print(i)


testarg(10,20,30,40,50,60,70) """


"""def testarg(a,b,c=30,*d,e,f):
    print(a,b,c)
    for i in d:
        print(i)


testarg(10,20,30,40,50,60,70,e=80,f=90) """


def testarg(a,b,c=30,*d,e,f,**kva):
    print("a={},b={},c={}".format(a,b,c))
    for i in d:
        print(i)
        
    for k,v in kva.items():
        print("{}={}".format(k,v))
        


testarg(10,20,30,40,50,60,70,e=80,f=90,g=100,h=101,i=102)

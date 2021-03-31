class Test:
    def fun(self,a,b):
        print("{}".format(a+b))

    def fun(self,a,b,c):
        print("{}".format(a+b+c))

ob=Test()
ob.fun(12,13)
            
#Solution to above problem 

class Test:

    def fun(self,a,b,c=0):
        print("{}".format(a+b+c))

ob=Test()
ob.fun(12,13)

def fibodec(myfibo):            #decorator to increase processing speed
    d={}
    def fiboLogic(n):
        if n not in d:
            d[n]=myfibo(n)
        return d[n]
    return fiboLogic



@fibodec          #Can also use myfibo=fibodec(myfibo)
def myfibo(num):          #Fib using recursion
    if num==0 or num==1:
        return num
    else:
        return myfibo(num-1)+myfibo(num-2)

num=int(input("Enter your limit"))
for i in range(num):
    print(myfibo(i),end=" ")



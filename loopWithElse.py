no= int(input("Enter number of lines"))
for i in range(2,no/ /2+1):
    if no%i==0:
        print("Not prime")
        break
else:
    print("Prime")

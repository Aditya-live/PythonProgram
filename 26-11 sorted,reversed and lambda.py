"""Sorted, reveresed and lamba function"""

lst=['james','smith','blake','king','meena']

for i in sorted(lst):   #Sorted
    print(i,end=" ")

print()

for i in reversed(lst):   #reversed
    print(i,end=" ")


def mys(lst):
    return lst[-1]

lst.sort(key=mys)


lst.sort(Key=lambda name:name[-1])  #to sort the list based on last letter
                                    #using lamba function

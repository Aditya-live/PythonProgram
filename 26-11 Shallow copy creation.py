lst=['james','paul','meenu','john']

for i in lst[:]:        #lst[:] is the shallow copy of the list 
    if len(i)==4:
        lst.append(i)

print(lst)

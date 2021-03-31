def getKey(val):
    for key,value in Dict.items():
        if val==value:
            return key
    return -1

Dict={'Tim': 10, 'Charlie': 22, 'tiffany': 23, 'Sarah': 20}
values=Dict.values()
values=sorted(list(values))

for i in values:
    print(getKey(i),":",i)

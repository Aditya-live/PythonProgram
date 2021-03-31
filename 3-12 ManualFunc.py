class Team:
    def __init__(self,member):
        self.__member=member

    def __len__(self):
        return len(self.__member) 

    def __contains__(self,member):
        return member in (self.__member)

    def __iter__(self):
        for i in self.__member:
            yield i


ob=Team(["James","Smith","Blake"])

#print(len(ob))

print("James" in ob)  #for call 
print("Neena" in ob)

for i in ob:
    print(i)

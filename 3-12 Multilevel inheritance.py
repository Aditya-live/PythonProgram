#Multilevel Inheritance
"""
class BaseClass:
    def msg(self):
        print("Base class")


class ChildClass(BaseClass):
    def msg(self):
        print("Child class")


class GrandChild(ChildClass):
    def msg(self):
        print("Grand child")

    

var=GrandChild()
var.msg()
"""
"""
#Using constructor works same

class BaseClass:
    def __init__(self):
        print("Base class const")


class ChildClass(BaseClass):
    def __init__(self):
        print("Child class const")


class GrandChild(ChildClass):
    def __init__(self):
        print("Grand child const")

ChildClass()
GrandChild()
"""
#Using Super
"""
class BaseClass:
    def __init__(self):
        print("Base class const")


class ChildClass(BaseClass):
    def __init__(self):
        super(ChildClass,self).__init__()
        print("Child class const")
        


class GrandChild(ChildClass):
    def __init__(self):
        print("Grand child const")
        BaseClass.__init__(self)  #To call a parent class
        super(GrandChild,self).__init__()

GrandChild()
"""
# Muliple inheritance
"""
class Base1:
    def msg(self):
        print("Message from base1")


class Base2:
    def msg(self):
        print("Message from base2")

class Child(Base2, Base1):
    pass


ob=Child()
ob.msg()
"""
#Abstract demo
"""
class MediaPlayer:
    def playAudio(self):
        print("Can play audio")

    def playVideo(self):
        pass


class Sr(MediaPlayer):
    def playVideo(self):
        print("Can't play video")

class Vlc(MediaPlayer):
    def playVideo(self):
        print("Can play video")



MediaPlayer().playAudio()
obsr=Sr()
obsr=playAudio()
obsr=playVideo()

obsr=Vlc()
obsr=playAudio()
obsr=playVideo()
"""

#Abstract class implemention

from abc import ABC,abstractmethod

class MediaPlayer(ABC):
    def playAudio(self):
        print("Can play audio")
        
    @abstractmethod
    def playVideo(self):
        pass


class Sr(MediaPlayer):
    def playVideo(self):
        print("Can't play video")

class Vlc(MediaPlayer):
    def playVideo(self):
        print("Can play video")


# ob=MediaPlayer()
ob=Vlc()

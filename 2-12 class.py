"""
This is a python
class basic structure
"""

"""
class Student:
    rollno=100
    name="james"
    per=66.66

print(Student.rollno, Student.name, Student.per)
"""
#
"""
class Student:
    rollno=100
    name="james"
    per=66.66

Ob1=Student()
Ob2=Student()

print(Ob1.rollno,Ob1.name,Ob1.per)    


Ob2.desig="CR"
print(Ob2.rollno,Ob2.name,Ob2.per,Ob2.desig)
"""
#
"""
class Student:
    def msg(self):
        print("Hello world")
        
Ob1=Student()
Ob2=Student()

Ob1.msg()
Ob2.msg()
"""
#
"""
class Student:
    def msg(self):
        print("Hello world")
        self.__stmt()
    def __stmt(self):    # Private method
        print("Bye world")

Ob1=Student()
Ob2=Student()

Ob1.msg()
"""
# Used for testing. In case you
"""
class Student:
    def msg(self):
        print("Hello world")
        self.__stmt()
    def __stmt(self):    # Private method
        print("Bye world")

Ob1=Student()
Ob2=Student()
Ob2._Student__stmt()
"""
# 
"""
class Student:
    def setData(self):
        self.rollno=12
        self.name="James"
        self.per=55.5

    def getData(self):
        print("rollno:{}\nname:{}\nper{}".format(self.rollno,self.name,self.per))


stu1=Student()
stu2=Student()

stu1.setData()
stu1.getData()

stu2.setData()
stu2.getData()
"""
#
"""
class Student:
    def setData(self,rollno,name,per):
        self.rollno=rollno
        self.name=name
        self.per=per

    def getData(self):
        print("rollno:{}\nname:{}\nper{}".format(self.rollno,self.name,self.per))


stu1=Student()
stu2=Student()

#stu1.setData(10,"Smith",89)
stu1.getData()

stu2.setData(20,"james",90)
stu2.getData()
"""
# Using constructor
"""
class Student:
    def __init__(self):
        self.rollno="NA"
        self.name="NA"
        self.per="NA"

    def setData(self,rollno,name,per):
        self.rollno=rollno
        self.name=name
        self.per=per

    def getData(self):
        print("rollno:{}\nname:{}\nper{}".format(self.rollno,self.name,self.per))


stu1=Student()
stu2=Student()

#stu1.setData(10,"Smith",89)
stu1.getData()

stu2.setData(20,"james",90)
stu2.getData()

stu2.setData(20,"james",90)  #Calling setData to initialize stu2
stu2.getData()
"""
# Passing different number of arguments( Only want to pass rollno and name not per)

class Student:
    def __init__(self,rollno="NA",name="NA",per="NA"):
        self.rollno=rollno
        self.name=name
        self.per=per

    def setData(self,rollno,name,per):
        self.rollno=rollno
        self.name=name
        self.per=per

    def getData(self):
        print("rollno:{}\nname:{}\nper{}".format(self.rollno,self.name,self.per))


stu1=Student(10,"James")
stu2=Student(20)

stu1.getData()
stu2.getData()


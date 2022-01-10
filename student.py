from person_v2 import Person

class Student(Person):
    def __init__(self,fname,lname,stNumber):
        super().__init__(fname,lname)
        self.__stNumber=stNumber
    
    def stNumber(self,value):
        self.__stNumber=value

    def studentInfo(self):
        print("the student number is "+str(self.__stNumber))
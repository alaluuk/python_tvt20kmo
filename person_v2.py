class Person:
    def __init__(self, fname, lname):
        self.__fname=fname
        self.__lname=lname

    def setFname(self,value):
        self.__fname=value

    def setLname(self,value):
        self.__lname=value
    
    def personInfo(self):
        print("The name of the person is : "+self.__fname, self.__lname)
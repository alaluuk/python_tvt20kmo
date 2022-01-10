class Person:
    def __init__(self,fn,ln,pn):
        self.__fname=fn
        self.__lname=ln
        self.publicName=pn

    def getPublicName(self):
        return self.publicName

    def setFname(self,value):
        self.__fname=value

    def getFname(self):
        return self.__fname

    def setLname(self,value):
        self.__lname=value

    def getLname(self):
        return self.__lname
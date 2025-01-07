import random
import csv

class Person:
    def __init__(self,firstName, surName,YOB,town):
        self.firstName=firstName;self.surName=surName
        self.YOB=YOB;self.town=town
    def printOutDetails(self):
        return "First Name {0}, surname {1},  I was born in {2}, I live in {3}"\
               .format(self.firstName, self.surName,self.YOB, self.town)
    def createuser(self):
        last2digits=str(self.YOB)
        fn=self.firstName[0:2]
        self.user=last2digits[-2:]+fn+self.surName
        return self.user
 
class Pupil(Person):
    def __init__(self, firstName, surName, YOB, town, school):
        Person.__init__(self,firstName,surName,YOB,town)
        self.school=school
    def printOutDetails(self):
        return Person.printOutDetails(self)+" i go to {0}".format(self.school) 
    def createuser2(self):
        last2digits=str(self.YOB)
        fn=self.firstName[0:2]
        self.user2=last2digits[-2:]+fn+self.surName+"@rgshw.com"
        return self.user2

class Sixthform(Pupil):
    def __init__(self, firstName, surName, YOB, town, school, subject1, subject2, subject3):
        Pupil.__init__(self, firstName, surName, YOB, town, school)
        self.subject1=subject1
        self.subject2=subject2
        self.subject3=subject3
    def printOutDetails(self):
        return Pupil.printOutDetails(self)+" i take {0}, and {1}, and {2}"\
            .format(self.subject1, self.subject2, self.subject3)

class Robot:
    def __init__(self,name, phrase,habit):
        self.name=name;self.phrase=phrase
        self.habit=habit
    def printOutDetails(self):
        return "Ho ho ho i am {0}, Have a {1},  I like {2}"\
               .format(self.name, self.phrase,self.habit)

class UberRobot(Robot):
    def __init__(self,name,phrase, habit, phrase1, phrase2, phrase3):
        Robot.__init__(self, name, phrase, habit)
        self.phrase1=phrase1
        self.phrase2=phrase2
        self.phrase3=phrase3
    def printOutrandDetails(self):
        return Robot.printOutDetails(self)+"{0}, {1}, {2}".format(self.phrase1, self.phrase2, self.phrase3)

def main():
    records = getClassRecordsfromCSV()
    showList(records)
    AlevelBoys=setUpDaBoys(records)
    showList(AlevelBoys)

def getClassRecordsfromCSV():
    Database=[]
    fileName="class/2025/wc_6_jan/BoysOptionsv4.csv"
    with open (fileName,"r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            Database.append(row)
    return Database

def showList(alist):
    for row in alist:
        print("\t".join([str(x) for x in row]))
        
def setUpDaBoys(alist):
    AlevelBoys=[]
    for i in range(len(alist)):
        tempList=[]
        temp=Person(alist[i][2], alist[i][1], alist[i][6], alist[i][9])
        tempList.append(temp); tempList.append(alist[i][2]); tempList.append(alist[i][1]); tempList.append(alist[i][6]); tempList.append(alist[i][9])
        AlevelBoys.append(tempList)
    return AlevelBoys

Person1=Person("DaGood","LookingOne",1995,"Norfolk")
print(Person1.printOutDetails())
print(Person1.createuser())
Pupil1=Pupil("DaGood","LookingOne",1995,"Norfolk","RGSHW")
print(Pupil1.printOutDetails())
print(Pupil1.createuser2())
Sixthform1=Sixthform("DaGood","LookingOne",1995,"Norfolk","RGSHW", "Maths", "computing", "geography")
print(Sixthform1.printOutDetails())
Robot1=Robot("Santa", "Merry Christmas", "Giving presents")
print(Robot1.printOutDetails())

if __name__ == '__main__':
    main()
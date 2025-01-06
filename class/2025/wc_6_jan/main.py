class Person:
    def __init__(self,fn, sn,yearofbirth,town):
        self.fn=fn;self.sn=sn
        self.yearofbirth=yearofbirth;self.town=town
    def outputDetails(self):
        return "First Name {0}, sn {1},  I was born in {2}, I live in {3}"\
               .format(self.fn, self.sn,self.yearofbirth, self.town)
    def createPupil(self):
        last2digits=str(self.yearofbirth)
        fn=self.fn[0:2]
        self.user=last2digits[-2:]+fn+self.sn
        return self.user

class Pupil(Person):
    def __init__(self, fn, sn, yearofbirth, town, school):
        Person.__init__(self,fn,sn,yearofbirth,town)
        self.school=school
    def outputDetails(self):
        return Person.outputDetails(self)+" I go to the school: {0}".format(self.school) 
    def createPupil2(self):
        last2digits=str(self.yearofbirth)
        fn=self.fn[0:2]
        self.user2=last2digits[-2:]+fn+self.sn+"@rgshw.com"
        return self.user2

class SixthForm(Pupil):
    def __init__(self, fn, sn, yearofbirth, town, school, subjectOne, subjectTwo, subjectThree):
        Pupil.__init__(self, fn, sn, yearofbirth, town, school)
        self.subjectOne = subjectOne
        self.subjectTwo = subjectTwo
        self.subjectThree = subjectThree
    def outputDetails(self):
        return Pupil.outputDetails(self)+" I do the following subjects: {0}, and {1}, and {2}"


Person1 = Person("DaGood","LookingOne",1995,"Norfolk")
print(Person1.outputDetails())
print(Person1.createPupil())
Pupil1 = Pupil("DaGood","LookingOne",1995,"Norfolk","RGSHW")
print(Pupil1.outputDetails())
print(Pupil1.createPupil2())
sixthFormStudent = SixthForm("DaGood","LookingOne",1995,"Norfolk","RGSHW", "Maths", "Physics","Computing")
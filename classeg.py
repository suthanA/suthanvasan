class Student:
    studCount = 0

    def __init__(self,rollnumber,name,mark1,mark2):
        self.rollnumber = rollnumber
        self.name = name
        self.mark1=mark1
        self.mark2=mark2
        Student.studCount += 1

    def totalCount(self):
        print "Total number of students", Student.studCount

    def student(self):
        print "Roll number: ", self.rollnumber, "Name: ", self.name,"mark:",self.mark1,self.mark2
    def sum(self):
        a=self.mark1+self.mark2
        print a
stud1= Student(2001435,"Rama",30,30)
stud2=Student(201234,"Krishna",20,50)

stud1.student()
stud1.sum()
stud2.student()
stud2.sum()
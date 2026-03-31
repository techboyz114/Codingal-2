class student:
    rno=10 #data member
    name="Rudransh" #data member
    grade=8 #data member
    def intp ro(self): #member function
        print("Hi this is", self.name, ", Roll number =", self.rno)
    def det(self): #member function
        print("I study in grade", self.grade)

o1=student() #create object
o1.intro()
o1.det()
o2=student()
o2.intro()
o2.det()

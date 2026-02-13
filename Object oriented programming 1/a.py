class student:
    rno=10 #data member
    name="Lohisree" #data member
    grade=7 #data member
    def intro(self): #member function
        print("Hi this is", self.name, ", Roll number =", self.rno)
    def det(self): #member function
        print("I study in grade", self.grade)

o1=student() #create object
o1.intro()
o1.det()
o2=student()
o2.intro()
o2.det()

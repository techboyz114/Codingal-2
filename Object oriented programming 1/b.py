class student:
    school="ABC"  # global variable : common for all objects
    def __init__(self,r,n,g):  # constructor
        self.rno=r        # data member, instance variable : diff for diff object
        self.name=n       # data member, instance variable : diff for diff object
        self.grade=g
    def intro(self):  # member function
        print("Hi this is",self.name,"from",self.school,"school, Roll number =",self.rno)
    def det(self):  # member function
        print("I study in grade",self.grade)

o1=student(16,"Arnold",11)  # object is created: call constructor automatically
o1.intro()
o1.det()
o2=student(14,"Lohisree",9)
o2.intro()
o2.det()

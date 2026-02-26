class parrot: #class
    species = "bird" # common / same for all objects / class variable
    def __init__(self, n, a):
        self.name = n #data
        self.age = a #data
        #instance variables

    def sing(self, song): #function
        print(self.name, "sings", song)

    def dance(self): #function
        print("I am a", self.species, "my name is", self.name, "I like to dance at the age", self.age)

o1 = parrot("Jojo", 6)
o2 = parrot("Mitu", 8)

o1.sing("Happy")
o1.dance()

o2.sing("Hurrey")
o2.dance()

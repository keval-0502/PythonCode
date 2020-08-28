class person():
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def printname(self):
        print(self.fname, self.lname, self.age)
    
class student(person):
    def __init__(self, fname, lname, age, year):
     person.__init__(self, fname, lname, age)
     self.year = year

    def welcome(self):
     print("Welcome",self.fname, self.lname, "to the class of",self.year,".","You are", self.age, "years old",".")

x = student("keval", "Bavisi", 20, 2020)
x.welcome()

    
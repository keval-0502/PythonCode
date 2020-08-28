class person:
 def __init__(self, fname, lname,age):
  self.fname = fname
  self.lname = lname
  self.age = age

 def printname(self):
  print(self.fname, self.lname)

 def print(self):
     print(self.age)

class student(person):
    def __init__(self,fname,lname, age):
     person.__init__(self,fname,lname, age)

x = student("KEVAL", "AYUSHI", 20)
x.printname()
x.print()


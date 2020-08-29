class person:
    def __init__(self, name, age):
     self.name = name 
     self.age = age
    
    def myfunction(self):
     print("HELLO MY NAME IS" + self.name)
p1 = person("KEVAL", 20)
print(p1.name)
print(p1.age)

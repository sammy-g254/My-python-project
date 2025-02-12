#Parent class
class animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return ("some sound")
    def parentmethod(self):
        print("calling from the parent method")
#Child class inherited from the parent class
class dog(animal):
    def childmethod(self):
        print("calling child method")
    def speak(self):
        return "bark"
#Creating 
mydog=dog("Bob")
print(mydog.name)
print(mydog.speak())
mydog.parentmethod()
mydog.childmethod()
#
class cat(animal):
    def speak(self):
        return "meow"
mycat=cat("xyz")
print(mycat.name)
#Calling method of a parent class
print(mycat.speak())
mycat.parentmethod()


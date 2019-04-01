#This is very important might come up in the panel interview
class Dog:  #has to be singular
    animal_variety="canine" # this is a class variable

    def bark(self):     #instance method # the self means referes the dog from the method
        return "woof"

#instance method means your making one of
print(Dog.animal_variety)

rolo= Dog() # by using the name of class and using brackets after it its called a constructor funtion
sandy= Dog() # class is a blue print of an object

print(sandy.animal_variety)
print(sandy.bark())
print(type(rolo))

sandy.animal_variety= "Feline Cat"
print(sandy.animal_variety)

#lab 2
#turning calculators into class

class Calculator:
    calc= "Calculator"

    #define class to simulate a simple calculator
    def __init__ (self):
        #start with zero
        self.current = 0
    def add(self, amount):
        #add number to current
        self.current += amount
    def getCurrent(self):
        return self.current

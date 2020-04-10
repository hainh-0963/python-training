##  Empty class
class person1:
    '''doc string: This is an empty person Class'''
    pass

class person2:
    count=0 #class attribute
    def __init__(self): #constructor
        self.name="unknown" #instance attribute
        self.age=0 #instance attribute
    def displayInfo(self): #method
        print(self.name, self.age)

class person:
    greet='Hello!'  # class attribute
    def __init__(self):
        self.name="Huu Hai" # instance attribute
        self.age=0 # instance attribute

p1 = person()
p1.name
p1.age
p1.greet
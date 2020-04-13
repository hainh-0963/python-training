class Parent:
    parentAttr = 100

    def __init__(self):
        print('This is parent constructor')

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('Parent attribute:', Parent.parentAttr)

    def myMethod(self):
        print('Calling parent method')


class Child(Parent):
    def __init__(self):
        print('Calling child constructor')

    def childMethod(self):
        print('Calling child method')

    def myMethod(self):
        print('Calling child method')


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMethod()


class Student:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello', name)
        else:
            print('Hello')


# Creating a class instance
std = Student()

# Call the method
std.sayHello()

# Call the method and pass a parameter
std.sayHello('Hai')

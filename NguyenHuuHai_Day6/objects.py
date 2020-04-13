class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello", self.name)

    def displayAge(self):
        print("You're", self.age, "years old!")


print("Person.__doc__:", Person.__doc__)
print("Person.__name__:", Person.__name__)
print("Person.__module__:", Person.__module__)
print("Person.__bases__:", Person.__bases__)
print("Person.__dict__:", Person.__dict__)
print("\n")
person1 = Person("Hai", 23)
person1.sayHello()
person1.displayAge()
print("\n")


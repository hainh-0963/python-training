##  Creating a function
print("\n")

def my_function():
    print("Hello from a function")

my_function()

print("\n")
def my_function(fname):
    print("Hello " + fname)

my_function("Hai")
my_function("Huu Hai")

##  Arbitrary Arguments, *args
print("\n")
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("John", "Smith", "Justin")

##  Arbitrary Keyword Arguments, **kwargs
print("\n")
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

##  Default Parameter Value
print("\n")
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

##  Passing a List as an Argument
print("\n")
def my_function(food):
    for x in food:
        print(x)
 
fruits = ["apple", "banana", "cherry"]

my_function(fruits)

##  Return Values
print("\n")
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

##  Recursion
print("\n")
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results")
tri_recursion(6)
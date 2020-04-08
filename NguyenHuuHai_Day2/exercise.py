#   Based on https://www.w3schools.com/python/exercise.asp
##  Syntax
print("\n-------- Syntax:")
### Exercise 1
print("Hello world");

### Exercise 2
if 5 > 2:
	print("Five is greater than two!")

##	Variables
print("\n-------- Variables:")
### Exercise 1

carname = "Volvo"
print(carname)

### Exercise 2
x = 50
print(x)

### Exercise 3
x = 5
y = 10
print(x + y)

### Exercise 4
z = x + y
print(z)

### Exercise 5
myfirst_name ="John"
print(myfirst_name)

### Exercise 6
x = y = z = "Orange"

### Exercise 7
def myfunc():
	global x
	x = "Fantastic"
myfunc()

print(x)

## 	Datatype
print("\n-------- Data Types:")
### Exercise 1
x = 5 
print(type(x))

### Exercise 2
x = "Hello World" 
print(type(x))

### Exercise 3
x = 20.5
print(type(x))

### Exercise 4
x = ["apple", "banana", "cherry"]
print(type(x))

### Exercise 5
x = ("apple", "banana", "cherry")
print(type(x))

### Exercise 6
x = {"name" : "John", "age" : 36}
print(type(x))

### Exercise 7
x = True
print(type(x))

##	Numbers
print("\n-------- Numbers")

###	Exercise 1
x = 5
x = float(x)
print(x)

### Exercise 2
x = 5.5
x = str(x)
print(x)

### Exercise 3
x = 5
x = complex(x)
print(x)

##	Strings
print("\n-------- Strings")

###	Exercise 1
txt = "Hello World"
print(txt)

### Exercise 2
print(txt[0])

### Exercise 3
print(txt[2:5])

### Exercise 4
txt = " Hello World "
print(txt.strip())

###	Exercise 5
txt = "Hello World"
print(txt.upper())

### Exercise 6
print(txt.lower())

### Exercose 7
print(txt.replace("H", "F"))

### Exercise 8
age = 23 
txt = "My name is Hai, and I am {}"
print(txt.format(age))

##	Booleans
print("\n-------- Booleans")

###	Exercise 1
print(10 > 9) 				# True

###	Exercise 2
print(10 == 9)				# False

###	Exercise 3
print(10 < 9)				# False

###	Exercise 4
print(bool("abc"))			# True

###	Exercise 5
print(bool(0))				# False

##	Operators
print("\n-------- Operators")

##Exercise 1
print(10 * 5)

##Exercise 2
print(10 / 2)

##Exercise 3
fruits = ["apple", "banana"]
if "apple" in fruits:
	print("Apple is a fruit!")

##Exercise 4
if 5 != 10:
	print("5 and 10 is not equal!")

##Exercise 5
if 5 == 10 or 4 == 4:
	print("At least one of the statements is true")

## 	Lists
print("\n-------- Lists")

###	Exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
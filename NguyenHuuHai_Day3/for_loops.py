##	For loops
print("\n")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)

##	Looping through a string
print("\n")
for x in "banana":
	print(x)

##	The break Statement
print("\n")
for x in fruits:
	print(x)
	if x == "banana":
		break

##	The continue Statement
print("\n")
for x in fruits:
	if x == "banana":
		continue
	print(x)

##	The range() function:
print("\n")
for x in range(6):
  print(x) 


## 	Else in for loop
print("\n")
for x in range(6):
	print(x)
else:
	print("Finally finished!")

##	Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
	for y in fruits:
		print(x, y)

##	The pass Statement
for x in [0, 1, 2]:
	pass
#	LIST 
##	Create a list
list1 = [1, 2, 3, 4, "A", "B", [5, 6, 7]]
print(list1)
print(type(list1))

##	Go to element has index 3
print(list1[3])

##	Assign new value for element
list1[3] = 10
print(list1)

##	Length
print(len(list1))

## Remove element
list1.remove('B')
print (list1)


## Sort
list1 = [4, 3, 5, 2, 1, 6, 2]
 
list1.sort()
print (list1)
list1.sort(reverse = True)
print (list1)

#	TUPLE 
## 	Create a tuple 
print("\n")
tuple1 = (1, 2, 3, 4, "A", 'B', (5, 6, 7))
print(tuple1)
print(type(tuple1))

print(tuple1.count('A'))
print(tuple1.index('A'))

#	SET
##	Create a set 
print("\n")
set1 = {4, 3, 5, 2, 1, 6, 2}
print(set1)

##	Add an element
set1.add(100)
print (set1)

##	Remove an element
set1.discard(100)
print (set1)

#	DICTIONARY
##	Create a dictionary
print("\n")
dictCar = {
    "brand": "Honda",
    "model": "Honda Civic",
    "year": 1972
}
print(dictCar)

## 	Get keys of dict 
print(dictCar.keys())

## 	Get values of dict 
print(dictCar.values())

## 	Get items of dict 
print(dictCar.items()) 

## 	Access by key
print(dictCar['brand'])

## 	Add an element
dictCar['madeIn'] = 'Japan'
print(dictCar)

## 	Remove an element
dictCar.pop("model")
print(dictCar)

try:
    a=5
    b=1
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")


try:
    a=5
    b=0
    print (a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print ('Division by zero not allowed')
print ('Out of try except blocks')


try:
    print("try block")
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x=0
    y=0
print ("Out of try, except, else and finally blocks." )
print("\n")

## Raise
try:
    x = input("Re-enter keyword Hai: ")
    if x != "Hai":
        raise Exception(x)
except:
    print(x, "is invalid!")
else:
    print("Your input is: ", x)

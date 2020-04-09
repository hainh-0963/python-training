##	In ket qua ra man hinh
print "Hello world\n"

##	Nhap data tu ban phim
###	input()
str = input("Enter something: ");
print "Your input are : ", str

###	raw_input()
print("\n")
str = raw_input("Enter something:  ");
print "Your input are : ", str

##	Example
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

import os
os.rename("foo.txt", "bar.txt")
os.remove("foo.txt")
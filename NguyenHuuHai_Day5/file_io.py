# Mo mot file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "Chuoi da doc la : ", str		# Kiem tra con tro hien tai
position = fo.tell();
print "Con tro file hien tai : ", position		# Dat lai vi tri con tro tai vi tri ban dau mot lan nua
position = fo.seek(0, 0);
str = fo.read(10);
print "Chuoi da doc la : ", str
# Dong file da mo
fo.close()

##	Thu muc 
import os		# Tao mot thu muc la "test"
os.mkdir("test")
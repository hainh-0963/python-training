#	FUNCTION 
##	Phan dinh nghia ham o day
def sum( arg1, arg2 ):
   total = arg1 + arg2
   print "Ben trong ham : ", total
   return total;
total = sum( 10, 20 );
print "Ben ngoai ham : ", total 

##	Truyen tham chieu va gia tri 
print("\n")
def changeme( mylist ):
   mylist.append([1,2,3,4]);
   print "Cac gia tri ben trong ham la: ", mylist
   return
mylist = [10,20,30];
changeme( mylist );
print "Cac gia tri ben ngoai ham la: ", mylist


##  Bien cuc bo va bien toan cuc
total = 0;
def sum( arg1, arg2 ):
    total = arg1 + arg2;
    print "Inside the function local total : ", total
    return total;
sum( 10, 20 );
print "Outside the function global total: ", total

square=lambda x1: x1*x1#Goi square nhu la mot ham
print "Binh phuong cua so la",square(10)
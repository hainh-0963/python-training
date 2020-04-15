import MySQLdb

# Open database connection
db = MySQLdb.connect('localhost', 'newuser', '@Hai123', 'testdb_python')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM employees \
      WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
       fname = row[0]
       lname = row[1]
       age = row[2]
       sex = row[3]
       income = row[4]
       # Now print fetched result
       print('First name: %s, Last name: %s, '
             'Age: %d, Gender: %c, Income: %d' % (fname, lname, age, sex, income))
except:
   print("Error: Unable to fecth data")

# Disconnect from server
db.close()

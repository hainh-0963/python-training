import MySQLdb

# Open database connection
db = MySQLdb.connect('localhost', 'newuser', '@Hai123', 'testdb_python')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database
sql = "insert into employees(first_name, \
      last_name, age, gender, income) \
      values ('%s', '%s', '%d', '%c', '%d' )" % \
      ('Nguyen Huu', 'Hai', 23, 'M', 2000)

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# Disconnect from server
db.close()

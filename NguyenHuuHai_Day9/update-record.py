import MySQLdb

# Open database connection
db = MySQLdb.connect('localhost', 'newuser', '@Hai123', 'testdb_python')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "UPDATE employees SET age = age + 1 \
        WHERE gender = '%c'" % ('M')
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

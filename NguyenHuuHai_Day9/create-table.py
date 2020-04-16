import MySQLdb

# Open database connection
db = MySQLdb.connect('localhost', 'newuser', '@Hai123', 'testdb_python')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute('DROP TABLE IF EXISTS employees')

# Create table as per requirement
sql = '''CREATE TABLE employees (
        first_name CHAR(20) NOT NULL,
        last_name  CHAR(20),
        age INT, 
        gender CHAR(1),
        income FLOAT )'''

cursor.execute(sql)

# Disconnect from server
db.close()

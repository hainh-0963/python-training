import MySQLdb

# Open database connection
db = MySQLdb.connect('localhost', 'newuser', '@Hai123', 'testdb_python')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Execute SQL query using execute() method
cursor.execute('SELECT VERSION()')

# Fetch a single row using fetchone() method
data = cursor.fetchone()
print('Database version: ', data)

# Disconnect from server
db.close()

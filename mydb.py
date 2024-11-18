import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'm8110m4951'
)

# prapare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE mahdico")

print("All Done!")
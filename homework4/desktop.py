import mysql.connector

cnx = mysql.connector.connect(user='root',
    password = 'Kiskakat1',
    host= 'localhost',
    database='bookbiz',
    auth_plugin='mysql_native_password')


cursor = cnx.cursor()
query = ("SELECT * FROM Books")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()

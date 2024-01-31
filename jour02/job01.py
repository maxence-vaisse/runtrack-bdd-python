import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="laplateforme"
)
cursor = mydb.cursor()
cursor.execute("SELECT * FROM etudiant")
result = cursor.fetchall()
print(result)
cursor.close()
mydb.close()
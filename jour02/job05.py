import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="laplateforme"
)
cursor = mydb.cursor()
cursor.execute("SELECT SUM(superficie) FROM etage")
result = cursor.fetchone()[0]
print("La superficie de La Plateforme est de", result, "m²")
cursor.close()
mydb.close()
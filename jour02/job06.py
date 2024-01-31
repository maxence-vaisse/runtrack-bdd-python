import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="laplateforme"
)
cursor = mydb.cursor()
cursor.execute("SELECT SUM(capacite) FROM salle")
result = cursor.fetchone()[0]
print("La capacité de toutes les salles est de", result, "personnes")
cursor.close()
mydb.close()
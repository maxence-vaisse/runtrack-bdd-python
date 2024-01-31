import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="entreprise"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM employe WHERE salaire >= 3000")
employes_riches = cursor.fetchall()
cursor.close()

# Convertir les valeurs décimales en chaînes de caractères
employes_riches = [(item[0], item[1], item[2], str(item[3]), item[4]) for item in employes_riches]

print(employes_riches)

cursor = mydb.cursor()
cursor.execute("SELECT employe.nom, prenom, service.nom FROM employe INNER JOIN service ON employe.id_service = service.id")
employes_et_services = cursor.fetchall()
cursor.close()

print(employes_et_services)


class salarie:
    def __init__(self, nom, prenom, salaire, id_service):        
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    def create(self):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)" , (self.nom, self.prenom, self.salaire, self.id_service))
        mydb.commit()
        cursor.close()

    def read(self,nom, prenom):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM employe WHERE nom = %s AND prenom = %s", (nom, prenom))
        employe = cursor.fetchall()
        cursor.close()
        print(employe)
    
    def update(self):
        cursor = mydb.cursor()
        cursor.execute("UPDATE employe SET salaire = %s WHERE nom = %s AND prenom = %s", (self.salaire, self.nom, self.prenom))
        mydb.commit()
        cursor.close()
    
    def delete(self):
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM employe WHERE nom = %s AND prenom = %s", (self.nom, self.prenom))
        mydb.commit()
        cursor.close()


employe = salarie("ROULIN", "Pauline", 25250.00, 2)
employe.create()
employe.read("ROULIN", "Pauline")
employe.salaire = 50000.00
employe.update()
employe.read("ROULIN", "Pauline")
employe.delete()
employe.read("ROULIN", "Pauline")
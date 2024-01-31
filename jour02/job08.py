import mysql.connector

# Se connecter à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="zoo"
)
cursor = conn.cursor()

# Fonction pour insérer une nouvelle cage
def inserer_cage(superficie, capacite_max):
    sql = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
    val = (superficie, capacite_max)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "cage insérée.")

# Fonction pour supprimer une cage
def supprimer_cage(cage_id):
    sql = "DELETE FROM cage WHERE cage_id = %s"
    val = (cage_id,)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "cage(s) supprimée(s).")

# Fonction pour modifier une cage
def modifier_cage(cage_id, superficie, capacite_max):
    sql = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE cage_id = %s"
    val = (superficie, capacite_max, cage_id)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "cage modifiée.")

# Fonction pour insérer un nouvel animal
def inserer_animal(nom, race, cage_id, date_naissance, pays_origine):
    sql = "INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    val = (nom, race, cage_id, date_naissance, pays_origine)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "animal inséré.")

# Fonction pour supprimer un animal
def supprimer_animal(animal_id):
    sql = "DELETE FROM animal WHERE animal_id = %s"
    val = (animal_id,)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "animal(s) supprimé(s).")

# Fonction pour modifier un animal
def modifier_animal(animal_id, nom, race, cage_id, date_naissance, pays_origine):
    sql = "UPDATE animal SET nom = %s, race = %s, cage_id = %s, date_naissance = %s, pays_origine = %s WHERE animal_id = %s"
    val = (nom, race, cage_id, date_naissance, pays_origine, animal_id)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "animal modifié.")

# Fonction pour récupérer tous les animaux du zoo
def afficher_animaux():
    sql = "SELECT * FROM animal"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\nAnimaux présents dans le zoo :")
    for row in result:
        print(row)

# Fonction pour récupérer les animaux présents dans les cages
def afficher_animaux_cages():
    sql = "SELECT c.cage_id, c.superficie, c.capacite_max, GROUP_CONCAT(a.nom SEPARATOR ', ') AS Animaux_dans_la_cage FROM cage c LEFT JOIN animal a ON c.cage_id = a.cage_id GROUP BY c.cage_id"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\nAnimaux présents dans les cages :")
    for row in result:
        print(row)

# Fonction pour calculer la superficie totale des cages
def calculer_superficie_totale_cages():
    sql = "SELECT SUM(superficie) FROM cage"
    cursor.execute(sql)
    total_superficie = cursor.fetchone()[0]
    print("La superficie totale de toutes les cages est :", total_superficie)

# Menu interactif
while True:
    print("\nMenu:")
    print("1. Ajouter une cage")
    print("2. Supprimer une cage")
    print("3. Modifier une cage")
    print("4. Ajouter un animal")
    print("5. Supprimer un animal")
    print("6. Modifier un animal")
    print("7. Afficher les animaux du zoo")
    print("8. Afficher les animaux dans les cages")
    print("9. Calculer la superficie totale des cages")
    print("10. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        superficie = float(input("Superficie de la cage : "))
        capacite_max = int(input("Capacité maximale de la cage : "))
        inserer_cage(superficie, capacite_max)

    elif choix == "2":
        cage_id = int(input("Entrez l'ID de la cage à supprimer : "))
        supprimer_cage(cage_id)

    elif choix == "3":
        cage_id = int(input("Entrez l'ID de la cage à modifier : "))
        superficie = float(input("Nouvelle superficie de la cage : "))
        capacite_max = int(input("Nouvelle capacité maximale de la cage : "))
        modifier_cage(cage_id, superficie, capacite_max)

    elif choix == "4":
        nom = input("Nom de l'animal : ")
        race = input("Race de l'animal : ")
        cage_id = int(input("ID de la cage : "))
        date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
        pays_origine = input("Pays d'origine : ")
        inserer_animal(nom, race, cage_id, date_naissance, pays_origine)

    elif choix == "5":
        animal_id = int(input("Entrez l'ID de l'animal à supprimer : "))
        supprimer_animal(animal_id)

    elif choix == "6":
        animal_id = int(input("Entrez l'ID de l'animal à modifier : "))
        nom = input("Nouveau nom de l'animal : ")
        race = input("Nouvelle race de l'animal : ")
        cage_id = int(input("Nouvel ID de la cage : "))
        date_naissance = input("Nouvelle date de naissance (YYYY-MM-DD) : ")
        pays_origine = input("Nouveau pays d'origine : ")
        modifier_animal(animal_id, nom, race, cage_id, date_naissance, pays_origine)

    elif choix == "7":
        afficher_animaux()

    elif choix == "8":
        afficher_animaux_cages()

    elif choix == "9":
        calculer_superficie_totale_cages()

    elif choix == "10":
        break

# Fermer la connexion à la base de données
cursor.close()
conn.close()
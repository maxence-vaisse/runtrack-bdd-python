INSERT INTO etudiant (prenom, nom, age, email) 
VALUES ('Martin', 'Dupuis', 18, 'martin.dupuis@laplateforme.io');

SELECT *
FROM etudiant
WHERE nom = 'Dupuis';
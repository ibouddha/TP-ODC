# Saisie des données de l'étudiant
nom = input("Entrez le nom de l'étudiant : ")
prenom = input("Entrez le prénom de l'étudiant : ")
date_naissance = input("Entrez la date de naissance (JJ/MM/AAAA) : ")

# Calcul de l'âge
annee_actuelle = 2024 # Supposez que nous sommes en 2024
_, _, annee_naissance = map(int, date_naissance.split('/'))
age = annee_actuelle - annee_naissance

# Affichage des informations de l'étudiant et de l'âge
print("Nom de l'étudiant : ", nom)
print("Prénom de l'étudiant : ", prenom)
print("Date de naissance : ", date_naissance)
print("Âge : ", age, "ans")

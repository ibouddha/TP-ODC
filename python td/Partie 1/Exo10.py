# Saisie du nombre de secondes
nb_secondes = int(input("Entrez le nombre de secondes : "))

# Conversion en heures, minutes et secondes
heures = nb_secondes // 3600
nb_secondes %= 3600
minutes = nb_secondes // 60
secondes = nb_secondes % 60

# Affichage du résultat
print("Durée : {} heures, {} minutes, {} secondes".format(heures, minutes, secondes))

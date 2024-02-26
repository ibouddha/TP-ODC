# Saisie de l'heure de départ
heure_depart = input("Entrez l'heure de départ (HH:MM) : ")
heure_dep, minute_dep = map(int, heure_depart.split(':'))

# Saisie de l'heure d'arrivée
heure_arrivee = input("Entrez l'heure d'arrivée (HH:MM) : ")
heure_arr, minute_arr = map(int, heure_arrivee.split(':'))

# Calcul de la durée de vol
if heure_arr < heure_dep:
    heure_arr += 24

duree_heures = heure_arr - heure_dep
duree_minutes = minute_arr - minute_dep

# Gestion du cas où les minutes sont négatives
if duree_minutes < 0:
    duree_heures -= 1
    duree_minutes += 60

# Affichage de la durée de vol
print("Durée de vol : {} heures et {} minutes".format(duree_heures, duree_minutes))

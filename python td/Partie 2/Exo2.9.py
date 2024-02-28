def date_suivante(jour, mois, annee):
    mois_31_jours = [1, 3, 5, 7, 8, 10]
    mois_30_jours = [4, 6, 9, 11]

    if mois == 2:
        if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
            nb_jours = 29
        else:
            nb_jours = 28
    elif mois in mois_31_jours:
        nb_jours = 31
    else:
        nb_jours = 30

    if jour < nb_jours:
        jour += 1
    else:
        jour = 1
        if mois < 12:
            mois += 1
        else:
            mois = 1
            annee += 1

    return jour, mois, annee

jour = int(input("Entrez le jour : "))
mois = int(input("Entrez le mois : "))
annee = int(input("Entrez l'année : "))

jour_suivant, mois_suivant, annee_suivante = date_suivante(jour, mois, annee)
print("La date suivante est : {}/{}/{}".format(jour_suivant, mois_suivant, annee_suivante))

def date_precedente(jour, mois, annee):
    mois_31_jours = [1, 3, 5, 7, 8, 10]
    mois_30_jours = [4, 6, 9, 11]

    if mois == 3:
        if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
            nb_jours_fevrier = 29
        else:
            nb_jours_fevrier = 28
        nb_jours_fevrier += 31
    elif mois == 1:
        nb_jours_fevrier = 0
    else:
        nb_jours_fevrier = 31

    if mois == 1:
        nb_jours_mois_precedent = 31
    elif mois in mois_31_jours:
        nb_jours_mois_precedent = 31
    else:
        nb_jours_mois_precedent = 30

    if jour > 1:
        jour -= 1
    else:
        if mois == 1:
            mois = 12
            annee -= 1
        else:
            mois -= 1
        jour = nb_jours_mois_precedent

    return jour, mois, annee

jour = int(input("Entrez le jour : "))
mois = int(input("Entrez le mois : "))
annee = int(input("Entrez l'année : "))

jour_precedent, mois_precedent, annee_precedente = date_precedente(jour, mois, annee)
print("La date précédente est : {}/{}/{}".format(jour_precedent, mois_precedent, annee_precedente))

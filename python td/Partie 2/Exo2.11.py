def date_dans_5_jours(jour, mois, annee):
    for _ in range(5):
        jour, mois, annee = date_suivante(jour, mois, annee)
    return jour, mois, annee

jour = int(input("Entrez le jour : "))
mois = int(input("Entrez le mois : "))
annee = int(input("Entrez l'année : "))

jour_futur, mois_futur, annee_futur = date_dans_5_jours(jour, mois, annee)
print("Dans 5 jours, la date sera : {}/{}/{}".format(jour_futur, mois_futur, annee_futur))

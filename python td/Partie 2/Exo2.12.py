def date_avant_N_jours(jour, mois, annee, N):
    for _ in range(N):
        jour, mois, annee = date_precedente(jour, mois, annee)
    return jour, mois, annee

N = int(input("Entrez le nombre de jours à reculer : "))
jour = int(input("Entrez le jour : "))
mois = int(input("Entrez le mois : "))
annee = int(input("Entrez l'année : "))

jour_avant, mois_avant, annee_avant = date_avant_N_jours(jour, mois, annee, N)
print("Il y a {} jours, la date était : {}/{}/{}".format(N, jour_avant, mois_avant, annee_avant))

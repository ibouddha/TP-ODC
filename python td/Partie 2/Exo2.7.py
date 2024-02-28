annee = int(input("Entrez une année : "))
mois = int(input("Entrez un mois (1-12) : "))

if mois in [1, 3, 5, 7, 8, 10, 12]:
    print("Nombre de jours :", 31)
elif mois in [4, 6, 9, 11]:
    print("Nombre de jours :", 30)
elif mois == 2:
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        print("Nombre de jours :", 29)
    else:
        print("Nombre de jours :", 28)
else:
    print("Mois invalide.")

jour = int(input("Entrez le jour : "))
mois = int(input("Entrez le mois : "))
annee = int(input("Entrez l'année : "))

if mois < 1 or mois > 12:
    print("Date invalide.")
elif mois in [1, 3, 5, 7, 8, 10, 12] and (jour < 1 or jour > 31):
    print("Date invalide.")
elif mois in [4, 6, 9, 11] and (jour < 1 or jour > 30):
    print("Date invalide.")
elif mois == 2:
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        if jour < 1 or jour > 29:
            print("Date invalide.")
    elif jour < 1 or jour > 28:
        print("Date invalide.")
else:
    print("Date valide.")

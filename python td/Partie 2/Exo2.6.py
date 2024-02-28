annee = int(input("Entrez une année : "))

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("L'année est bissextile.")
else:
    print("L'année n'est pas bissextile.")

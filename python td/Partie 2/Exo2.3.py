##
# Copyright (c) 2024-Petit Bouddha
# All rights reserved.
##

# Saisie des coefficients
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Calcul de Delta
Delta = b**2 - 4*a*c

# Vérification du Delta
if Delta > 0:
    # Deux solutions réelles distinctes
    x1 = (-b + (Delta ** 0.5)) / (2*a)
    x2 = (-b - (Delta ** 0.5)) / (2*a)
    print("Les xs sont :", x1, "et", x2)
elif Delta == 0:
    # Une solution réelle unique
    x = -b / (2*a)
    print("La x est unique :", x)
else:
    # Pas de soution réelle
    print("Pas de x réelle")

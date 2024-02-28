import math

# Saisie des coordonnées des points A et B
x1 = float(input("Entrez la coordonnée x du point A : "))
y1 = float(input("Entrez la coordonnée y du point A : "))
x2 = float(input("Entrez la coordonnée x du point B : "))
y2 = float(input("Entrez la coordonnée y du point B : "))

# Calcul de la distance entre les deux points en utilisant la formule
distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Affichage du résultat
print("La distance entre les points A et B est :", distance)

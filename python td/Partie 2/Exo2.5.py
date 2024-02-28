A = int(input("Entrez la valeur de A : "))
B = int(input("Entrez la valeur de B : "))
C = int(input("Entrez la valeur de C : "))

# Ordre croissant
croissant = sorted([A, B, C])
print("Valeurs dans l'ordre croissant :", croissant)

# Ordre décroissant
decroissant = sorted([A, B, C], reverse=True)
print("Valeurs dans l'ordre décroissant :", decroissant)

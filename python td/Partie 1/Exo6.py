#recuperer la longueur et la largeur

longueur =  float(input("Entrer la longueur de l'objet en cm : "))
largeur = float(input("Entrer la largeur de l'objet en cm : "))

#calculer le volume
volume = longueur * largeur

#calculer le perimetre
perimetre = 2*(longueur+largeur)

print(f"\nLe volume de l'objet est de {volume} cm³ et le périmètre est  de {perimetre} cm.")
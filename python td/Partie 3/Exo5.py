# Matrice carré à colorier la diagonale selon le choix de l'utilisateur
# Auteur : Bouddha
# since 04/03/2024

# fonction colorier partie diagonale

def colorier(n,position,color):
    endColor='\x1b[0m'
    blue = "\033[94m"
    vert = "\33[92m"
    red = "\033[31m"
    for i in range(n):
        for j in range(n):
            if position==1:
                if(color==2):
                    if i<j:
                        print(blue+"0 "+endColor,end="")
                    if i==j :
                        print(vert+"0 "+endColor,end="")
                    if i>j:
                        print("0 ",end="")
                else:
                    if i<j:
                        print(red+"0 "+endColor,end="")
                    if i==j :
                        print(vert+"0 "+endColor,end="")
                    if i>j :
                        print("0 ",end="")
            else:
                if(color==2):

                    if i>j:
                        print(blue+"0 "+endColor,end="")
                    if i<j:
                        print("0 ",end="")
                    if i==j :
                        print(vert+"0 "+endColor,end="")
                else:
                    if i>j:
                        print(red+"0 "+endColor,end="")
                    if i<j:
                        print("0 ",end="")
                    if i==j :
                        print(vert+"0 "+endColor,end="")

        print("")

# Demander à l'utilisateur de faire des choix obligatoires
print("Bienvenue dans le programme 5 !")
while(True):
    n = int(input("\nVeuillez saisir l'ordre de la matrice: "))
    couleur = int(input("Veuillez saisir votre couleur préférée\n 1. Rouge\n 2. bleu\n"))
    position = int(input("Quelle partie de la diagonale doit remplie par votre couleur\n 1. Haut\n 2. Bas\n"))

    if n >= 5 and couleur in (1,2) and position in (1,2):
        break
    
colorier(n, position, couleur)
print("")
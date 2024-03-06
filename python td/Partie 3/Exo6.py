#definition des couleurs
couleur = {
    "rouge" : "\033[91m",
    "vert" : "\033[92m",
    "bleu" : "\033[94m",
    "noir" : "\033[90m",
    "fin"  : "\x1b[0m"
}

#creation des fonctions de matrice
#colorier les symboles au dessus de la diagonale principale
def addp(n,color):
    #variable fin de coloration
    end = "\x1b[0m"
    #boucle dessin matrice
    for i in range(n):
        for j in range(n):
            if i<j:
                print(f"{color}0 {end}", end="")
            else:
                print("0 ", end="")
        print()
        
# colorier les symboles en dessous de la diagonale principale
def eddp(n, color):
    end = "\x1b[0m"
    for i in range(n):
        for j in range(n):
            if i>j:
                print(f"{color}0 {end}", end="")
            else:
                print("0 ", end="")
        print()
  
#colorier les symboles qui sont sur la diagonale principale
def sdp(n,color):
    end = "\x1b[0m"
    for i in range(n):
        for j in range(n):
            if i==j:
                print(f"{color}0 {end}", end="")
            else:
                print("0 ", end="")
        print()
        
#colorier les symboles qui sont au dessus de la diagonale secondaire
def adds(n, color):
    end = "\x1b[0m"
    for i in range(n):
        for j in range(n):
            if n-1-i > j:
                print(f"{color}0 {end}", end="")
            else:
                print("0 ", end="")
        print()
  
  
#colorier les symboles qui sont en dessous de la diagonale secondaire
def edds(n,color):
    end = "\x1b[0m"
    for i in range(n):
        for j in range(n):
            if n-1-i < j:
                print(f"{color}0 {end}", end="")
            else:
                print("0 ", end="")
        print()
        
        
#colorier les symboles qui sont sur la diagonale secondaire
def sds(n,color):
    end = "\x1b[0m"
    for i in range(n):
        for j in range(n):
            if n-1-i == j:
                print(f"{color}0 {end}", end="")
            else:
                print("0 ", end="")
        print()

def quitter():
    print("Fin et A la prochaine!!!!")
    return 0
  
def mainMenu(n,color):
    while(True):
        print(f"\n|{color}-----------------------------------------------\x1b[0m|",end= "\n")
        print(f"|{color}---------------|\t MENU SHAPE    |--------\x1b[0m|",end= "\n")
        print(f"|{color}-----------------------------------------------\x1b[0m|",end= "\n")
        
        print(f"|{color}\t\t1.\t ADDP   \t\t\x1b[0m|")
        print(f"|{color}\t\t2.\t EDDP   \t\t\x1b[0m|")
        print(f"|{color}\t\t3.\t SDP    \t\t\x1b[0m|")
        print(f"|{color}\t\t4.\t ADDS   \t\t\x1b[0m|")
        print(f"|{color}\t\t5.\t EDDS   \t\t\x1b[0m|")
        print(f"|{color}\t\t6.\t SDS    \t\t\x1b[0m|")
        print(f"|{color}\t\t7.\t QUITTER\t\t\x1b[0m|")
        print(f"|{color}-----------------------------------------------\x1b[0m|",end= "\n")
        
        choix = int(input("Enter your choice (1/2/3/4/5/6/7) : "))
        
        match(choix):
            case 1:
                addp(n,color)
                break
            case 2:
                eddp(n,color)
                break
            case 3:
                sdp(n,color)
                break
            case 4:
                adds(n,color)
                break
            case 5:
                edds(n,color)
                break
            case 6:
                sds(n,color)
                break
            case 7:
                quitter()
                break
            case _:
                print(f"{color}Invalid Choice! Please enter again.\n")
                break
            

def menuColor():
    while(True):
        print(f"\t\t\033[91m"+"0 : \tRouge"+"\x1b[0m")
        print(f"\t\t\033[92m"+"0 : \tVert"+"\x1b[0m")
        print(f"\t\t\033[94m"+"0 : \tBleu"+"\x1b[0m")
        print(f"\t\t\033[90m"+"0 : \tNoir"+"\x1b[0m")
        print(f"\t\t\033[93m"+"0 : \tJaune"+"\x1b[0m")
    
        choix = input("Make your choice : ")
        
        match(choix):
            case 'Rouge':
                color = "\033[91m"
                break
            case 'Vert' :
                color = "\033[92m"
                break
            case 'Bleu':
                color = "\033[94m"
                break
            case 'Noir':
                color = "\033[90m"
                break
            case "Jaune":
                color = "\033[93m"
                break
            case _:
                print(f"Invalid Choice! Please enter again.\n")
                break
    return color
    
    
n = int(input("Enter the number of rows : "))
#fonction d'affichage
# menuColor()
mainMenu(n,menuColor())
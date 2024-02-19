def dessiner_sapin(symbole, hauteur_feuilles, hauteur_tronc, largeur_racines):
    # Dessiner les feuilles
    for i in range(1, hauteur_feuilles + 1):
        print((symbole * (2 * i - 1)).center(hauteur_feuilles * 2 - 1))

    # Dessiner le tronc
    for _ in range(hauteur_tronc):
        print(symbole.center(hauteur_feuilles * 2 - 1))

    ## Dessiner les racines
    #for _ in range(largeur_racines):
    print((symbole * largeur_racines).center(hauteur_feuilles * 2 - 1))
    


# Demander les informations à l'utilisateur
symbole = input("Entrez le symbole à utiliser ($, *, +, ou 0) : ")
hauteur_feuilles = int(input("Entrez la hauteur des feuilles : "))
hauteur_tronc = int(input("Entrez la hauteur du tronc : "))
largeur_racines = int(input("Entrez la largeur des racines : "))

# Dessiner le sapin
dessiner_sapin(symbole, hauteur_feuilles, hauteur_tronc, largeur_racines)

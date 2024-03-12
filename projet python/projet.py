import csv
from tabulate import tabulate

#ouverture du fichier csv
with open("./projet python/Donnees_Projet_Python_Dev_Data.csv","r") as file:
    reader = csv.DictReader(file, delimiter = ",") 
    matrice = []
    for ligne in reader:
        if
        matrice.append(ligne.values())
    print(tabulate(matrice))
    
#lecture de la premiere ligne qui contient les titres des colonnes

    
#declaration des structures de données:
#parcourir les fichiers
#verifier les lignes valides et invalides
#récuperation de l'option de l'utilisateur
#faire le traitement en fonction du choix de l'utilisateur
    #afficher toutes les informations
    #afficher une informations par son numero
    #afficher les cinq premieres
    #ajouter une informations
    #modifier une informations invalides
    #quitter le programme
#repeter les etapes precedentes jusqu'a ce que l'utilisateur decide de quitter
#afficher les informations par pagination
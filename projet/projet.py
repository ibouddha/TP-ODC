import csv
from tabulate import tabulate
# import pandas as pd
import json

#convertir to json format
def convert_to_json(filename):
    #ouverture du fichier csv
    output_file = "./projet/data.json"
    prefix = "./projet/"
    data = []
    with open(prefix+filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
            
    # save the data in a json file
    with open(output_file, 'w') as f:
        json.dump(data, f,indent=4)

# convert_to_json("Data.csv")
#lire le fichier csv

def readfile(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    return data

print(readfile("projet\Data.csv"))

#lecture de la premiere ligne qui contient les titres des colonnes
#declaration des structures de données:
#parcourir les fichiers
#valider les lignes valides et invalides
def validateNom(nom):
    if nom[0].isalpha() and len(nom)>=2:
        valid = True
    else:
        valid = False
    return valid,nom
        
def validatePrenom(prenom):
    if prenom[0].isalpha() and len(prenom)>=3:
        valid = True
    else:
        valid = False
    return valid,prenom

def validateNumero(numero):
    valid = True
    print(numero.isalnum())
    if not numero.isalnum():
        for digit in numero:
            if digit.islower():
                valid = False
            
        if len (numero) != 7:
            valid = False
            
    return valid,numero

def ValidateClass(classe):
    valid = True
    if classe[0] not in ["6","5","4","3"] and classe[-1] not in ["A","B","C","D"]:
        print("iicccii")
        valid = False
        
    if classe[1:-2] != "em":
        print("icii")
        valid = False
    
    return valid, classe
    
#récuperation de l'option de l'utilisateur
def mainMenu():
    #faire le traitement en fonction du choix de l'utilisateur
    while(True):
        #afficher toutes les informations
        print(f"1. afficher les informations valides")
        #afficher les informations invalides
        print(f"2. afficher les informations invalides")
        #afficher une informations par son numero
        print(f"3. afficher les informations par numero")
        #afficher les cinq premieres
        print(f"4. afficher les cinq premiers informations")
        #ajouter une informations
        print(f"5. Ajouter une informations")
        #modifier une informations invalides
        print(f"6. Modifier une information invalide")
        #quitter le programme
        print(f"7. Quitter le programme")
        #repeter les etapes precedentes jusqu'a ce que l'utilisateur decide de quitter
        choice = input("Make a choice : ")
        
        match choice:
            case "1":
                #afficher informations valides
                afficher_valides()
                break
            case "2":
                #afficher informations invalides
                afficher_invalides()
                break
            case "3":
                #afficher une informations par son numero
                afficher_informations_par_numero()
                break
            case "4":
                #afficher les cinq premieres
                afficher_cinq_premiers_informations()
                break
            case "5":
                #ajouter une informations
                ajouter_une_informations()
                break
            case "6":
                #modifier une informations invalides
                modifier_invalide()
                break
            case "7":
                #quitter le programme
                quitter()
            case _:
                print("Veuillez saisir une valeur entre 1 et 6")
            

# mainMenu()

#afficher les informations par pagination
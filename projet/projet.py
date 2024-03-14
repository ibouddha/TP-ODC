import csv
from tabulate import tabulate
from calendar import month_abbr
import calendar
# import pandas as pd
import json
        
#convertir to json format
def convert_to_json(filename):
    #ouverture du fichier csv
    output_file = "./data.json"
    prefix = "./"
    data = []
    with open(prefix+filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
            
    # save the data in a json file
    with open(output_file, 'w') as f:
        json.dump(data, f,indent=4)

#lecture de la premiere ligne qui contient les titres des colonnes
#declaration des structures de données:
#parcourir les fichiers

#Methodes de validation des lignes valides et invalides
    
def convertLtoD(date):
    date = date.strip()
    month = date.split("/")[1]
    day = date.split("/")[0]
    annee = date.split("/")[2].strip()
    
    if(month>12 and (day<31 or month<31) and month.isnumeric()):
        day,month = month,day
    
    if(len(annee)==2):
        if(annee > 30):
            annee = "19" + annee
    
    for k, v in month_abbr:
        if v == month:
            month = k    


def verifier_date(date_str):
    """
    This function verifies if a date is correct in the format dd/mm/yyyy and handles months written in letters.

    Args:
        date_str (str): The date string to be verified.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # Months dictionary for conversion (key: month in letters, value: month number)
    mois_lettres = {
        "janv": 1, "fev": 2, "mar": 3, "avr": 4, "mai": 5, "jun": 6,
        "jul": 7, "aout": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    # Split the date string
    try:
        jour, mois, annee = date_str.split("/")
    except ValueError:
        return False  # Invalid format

    # Convert month from letters to number if necessary
    if mois.lower() in mois_lettres:
        mois = str(mois_lettres[mois.lower()]).zfill(2)  # Pad with leading zero

    # Validate day, month, and year
    try:
        # Check for valid integer values
        jour = int(jour)
        mois = int(mois)
        annee = int(annee)

        # Check for valid date range
        if not (1 <= jour <= 31 and 1 <= mois <= 12 and 1000 <= annee <= 9999):
            return False

        # Additional month validity check (considering leap years)
        if not calendar.isleap(annee) and mois == 2 and jour > 28:
            return False

    except ValueError:
        return False  # Invalid integer values

    return True

# print(verifier_date("21/01/2012"))

    
def validateNom(nom):    
    if nom[0].isalpha() and len(nom)>=2:
        valid = True
    else:
        valid = False
        
    #print(f"nom valide: {valid}")

    return valid


        
def validatePrenom(prenom):
    if prenom[0].isalpha() and len(prenom)>=3:
        valid = True
    else:
        valid = False
        
    #print(f"prenom valide: {valid}")
    
    return valid


def validateNumero(numero):
    valid = True
    if not numero.isalnum():
        valid = False
        
    for digit in numero:
        if digit.islower():
            valid = False
            
    if len (numero) != 7:
        valid = False
            
    #print(f"numero valide: {valid}")
    return valid

# print(validateNumero("JD7LO99"))

def validateNote(note):
    valid = True
    if note[0].isalpha() and len(note)>=3:
        valid = True
    else:
        valid = False
        
    
    return valid

def quitter():
    return 0
            
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
                case "2":
                    #afficher informations invalides
                    afficher_invalides()
                case "3":
                    #afficher une informations par son numero
                    afficher_informations_par_numero()
                case "4":
                    #afficher les cinq premieres
                    afficher_cinq_premiers_informations()
                case "5":
                    #ajouter une informations
                    ajouter_une_informations()
                case "6":
                    #modifier une informations invalides
                    modifier_invalide()
                case "7":
                    #quitter le programme
                    quitter()
                    break
                case _:
                    print("Veuillez saisir une valeur entre 1 et 6")
                

'''#fonction Afficher Valides
    def afficher_valides(self):
        """Affiche toutes les informations validées"""
        
        #vérification si il y a des informations dans la base de données
        # if validateNumero(self.code) and validateClass(self.classe) and validateNom(self.nom) and validatePrenom(self.prenom):
    
    # mainMenu()
    
    #testing
    #lire le fichier csv
'''
def validateClass(classe):
        valid = True
        if len(classe)>1:
            if classe[0] not in ["6","5","4","3"] and classe[-1] not in ["A","B","C","D"]:
                valid = False
                
            if classe[1:-1] != "em":
                valid = False
        else:
            valid = False
        
        #print(f"classe: {valid}")
        
        return valid

def readfile(filename):
    valideData = []
    invalideData = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            row[5] = row[5].replace(row[5][1:-1], "em").strip()
            row[6] = row[6].split("#")
            if(validateClass(row[5]) and validateNom(row[2]) and validatePrenom(row[3]) and validateNumero(row[1]) and row[1]!="" and row[2]!="" and row[3]!="" and row[4]!="" and row[5]!=""):
                valideData.append(row)
            else:
                invalideData.append(row)

    return valideData, invalideData

def afficher_valides():
    print(tabulate(readfile("Data.csv")[0]))
    
def afficher_invalides():
    print(tabulate(readfile("Data.csv")[1]))
    
mainMenu()
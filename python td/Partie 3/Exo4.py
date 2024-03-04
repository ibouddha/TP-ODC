#list d'indicatifs

def remove_space(numero:str):
    # Params: numero - string with spaces at the beginning and/or end.
    # Returns: string without leading or trailing space characters.
    
    #liste contenant les caractères speciaux à enlever. 
    number =""

    for i in range(0,len(numero)):
        if numero[i]!=" " :
            number += numero[i]
        else:
            if i==len(numero)-1 or numero[i+1]!=" ":
                number += ""

    return number

def isValid(number):
    indicatifs = {"77":"Orange","78":"Orange","70":"Expresso","75":"Promobile","76":"Free"}
    numero = remove_space(number)
    #recuperer le numero from l'utilisateur
    if numero[0:2] in indicatifs and len(numero) == 9 and numero.isnumeric() :
        return True
    else:
        return False 

#initialiser les listes de numeros
liste_valid = ["Numero Valide"]
liste_invalide=["Numero invalide"]

#recuperer le nombre maximal de numero
annuaire = int(input("combien de numero voulez vous entrer?"))

#recuperer les numeros depuis l'utilisateur et les verifier si ils sont valides ou non
for i in range(0,annuaire):
    numero = str(input("donner un numero de telephone: "))
    if numero == "":
        liste_valid.append("-----------")
        liste_invalide.append("-----------")
    if isValid(numero):
        liste_valid.append(numero)
        liste_invalide.append("-----------")
    else:
        liste_invalide.append(numero)
        liste_valid.append("-----------")

indicatifs = {"77":"Orange","78":"Orange","70":"Expresso","75":"Promobile","76":"Free"}
al = 0
fr = 0
ex = 0
pro = 0
#parcourir liste valide et chercher les operateurs
for numero in liste_valid:
    if numero != "-----------" :
        if numero[0:2] == "77" or numero[0:2] == "78":
            al += 1
        elif numero[0:2] == "76":
            fr += 1
        elif numero[0:2] == '70':
            ex += 1
        elif numero[0:2] == '75':
            pro += 1

for  i in range(0,annuaire+1):
    print (f"{liste_valid[i]}\t\t{liste_invalide[i]}")

print(f"Orange: {al} - Free: {fr} - Expresso: {ex} - Promobile: {pro}")
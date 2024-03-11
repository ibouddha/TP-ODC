#gestion student

#check if it's a number
def estUnNombre(numero):
    verif = bool
    digits = ['1','2','3','4','5','6','7','8','9','0']
    for digit in numero:
        if digit in digits:
            verif = True
        else:
            verif = False
    return verif

#function to remove spaces
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

#check if the number is valid
def isValid(number):
    indicatifs = {"77","78","70","75","76"}
    numero = remove_space(number)
    #recuperer le numero from l'utilisateur
    if numero[0:2] in indicatifs and len(numero) == 9 and estUnNombre(numero) :
        return True
    else:
        return False 

#valider numero telephone
def valideNumero(numero):
    while not isValid(numero):
        numero = input("Veuillez saisir un numero de téléphone valide : ")
    return numero

#creation of the student
def createStudent():
    print("Bienvenue à la création d'un étudiant")
    nom = input("Entrez le nom de l'étudiant : ")
    prenom = input("Entrez le prénom de l'étudiant : ")
    telephone = valideNumero(input("Entrez le numéro de téléphone de l'étudiant (format: 0612345678) : "))
    classe = input("Entrez le nom de la classe : ")
    note_Dev = validerNote(float(input("Entrez la note en Dev:")))
    note_Proj = validerNote(float(input("Entrez la note en Projet:")))
    note_Exam = validerNote(float(input("Entrez la note en Exam : ")))
    moy = (note_Dev + note_Proj + note_Exam) / 3
    return nom,prenom,telephone,classe,note_Dev,note_Proj,note_Exam,moy

#validation function
def validerNote(note):
    while note < 0 or note > 20:
        note = float(input("Veuillez saisir une note entre 0 et 20 : "))
    return note

#function to display a list of students in class
def displayAll(etudiant):
    space=""
    #print(f"Nom{space:10} Prenom{space:10} Telephone{space:10} Class{space:10} NoteDev{space:10} NoteProj{space:10} NoteExam{space:10} Moy{space:10}")
    print("----------------------------------------------------------------------------------------")
    for etu in etudiant:
        print(f"{etu[0]:10}",end= "|")
        print(f"{etu[1]:10}",end="|")
        print(f"{etu[2]:10}",end="|")
        print(f"{etu[3]:10}",end="|")
        print(f"{etu[4]:10}",end="|")
        print(f"{etu[5]:10}",end="|")
        print(f"{etu[6]:10}",end="|")
        print(f"{etu[7]:10.2f}",end="|")
        print("\n----------------------------------------------------------------------------------------")


#function to add the student in the list
def addStudent(etudiant):
    etudiant.append(createStudent())

#menu principal
def menu():
    print("|-------------------------------------------------------------------------------|")
    print("|-----------------------------------> Menu <------------------------------------|")
    print("|-------------------------------------------------------------------------------|")
    print("|\t\t\t\t-----> Afficher tout  <-----\t\t\t|")
    print("|\t\t\t\t---> trier et afficher  <---\t\t\t|")
    print("|\t\t\t\t----->   Rechercher   <-----\t\t\t|")
    print("|\t\t\t\t--> Modification de note <--\t\t\t|")
    
    
    
    
#function to run a test
def run():
    etudiant = []
    while(True):
        reponse = input("Voulez-vous ajouter un nouveau etudiant ? O/N : ")
        if reponse.upper() == 'O':
            addStudent(etudiant)
        elif reponse.upper() == 'N':
            break
        else:
            print("Veuillez saisir O ou N") 
    
    displayAll(etudiant)
        
# run()

menu()
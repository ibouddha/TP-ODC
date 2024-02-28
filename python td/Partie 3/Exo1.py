#create a python Matrice

def change_lang(lang):
    mois_in_french = [
    ["Janvier","Février","Mars"],
    ["Avril","Mai","Juin"],
    ["Juillet", "Août", "Septembre"],
    ["Octobre", "Novembre", "Decembre"]
    ]

    mois_in_English = [
        ["January", "February", "March"],
        ["April", "May", "June" ],
        ["July", "August", "September"], 
        ["October", "November", "December"]
    ]

    if lang == 'fr':
        lang = 'eng'
        mois = mois_in_English
    else:
        lang = "fr"
        mois = mois_in_french
    return mois

def display(mois):
    print("\n-----------------------------------------------------------",end= "\n")
    for i in range(3):
        print("|", end=" ")
        for j in range(4):
            print(f"{mois[j][i]:10}", end="|\t")
        print("\n-----------------------------------------------------------",end= "\n")

print("\t\t====>Affichage<====",end="\n")

display(change_lang("Eng"))
lang="fr"

while(True):
    while (True):
        choix = int(input("\n\n\n\n1. Changer de Langue\n2. Quitter"))
        if choix == 1:
            if lang == "fr":
                lang="Eng"
            else:
                lang = "fr"
            display(change_lang(lang))
        elif choix == 2:
            break
        else:
            print("\n\nVeuillez Saisir une Option Valide !!!!\n")
            display(change_lang(lang))
    break

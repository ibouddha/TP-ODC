#une phrase commence par une lettre majuscule et se termine par un point et ne contient pas de caractere special

def del_space(phrase):
    # Params: phrase - string with spaces at the beginning and/or end.
    # Returns: string without leading or trailing space characters.
    
    #liste contenant les caractères speciaux à enlever. 
    invalid_word = ["&", "$","£","%","#","{","]","[","}","@", "(", ")","<", ">","/"]
    valid_word = [",",";","'",".", "!", ":","?","-"] 
    modified_sentence =""

    for i in range(0,len(phrase)):
        if phrase[i]!=" " and phrase[i] not in invalid_word :
            modified_sentence += phrase[i]
        else:
            if i==len(phrase)-1 or phrase[i+1]!=" " and (phrase[i+1] not in valid_word and phrase[i+1]!=" "):
                modified_sentence += " "

    return modified_sentence

def estValide(phrase):
    valid = True
    if(len(phrase)<25): return False
    for i in range(0, len(phrase)):
        if (phrase[0].islower() or phrase[-1]!="."):
            valid = False
        else: 
            valid = True

    return valid


nombre_phrase = input("donnez le nombre de phrase: ")
paragraph = ""
for i in range(int(nombre_phrase)) :
    phrase=str(input("Donnez la phrase "+ str(i+1)+":"))
    
    while not estValide(phrase):
        print("La phrase doit commencer par une lettre majuscule et se terminer par un point et comporte au moins 25 caractères.")
        phrase=input("Reessayez la phrase "+ str(i+1)+":")
    
    paragraph += del_space(del_space(phrase)) + "\n"
print(f"{paragraph}")

#une phrase commence par une lettre majuscule et se termine par un point et ne contient pas de caractere special

def estEnMajuscule(letters):
    #list of capital letters
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

    if letters in capital_letters:
        return True
    else:
        return False

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

def extract(texte):
    paragraph = []
    phrase = ""
    text_correct = ""
    deb = True
    for i in range(0,len(texte)):
        if deb == False or texte[i] != " ":
            phrase += texte[i]
            deb = False
            if texte[i] == ".":
                paragraph.append(phrase)
                phrase = ""
                deb = True
    
    for text in paragraph:
        if estEnMajuscule(text[0]):
            text_correct += text

    return text_correct


phrase = input("text: ")

paragraphs = extract(del_space(phrase))            
    
print(f"le texte correct est: \n{paragraphs}")

# phrase1= "   je suis a dakar.  "
# prase2=""
# deb=True
# pour p dans phrase:
#     si p != " " ou deb =False :
#         prase2 += p
#         deb=false
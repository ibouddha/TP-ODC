#creating a script that delete all useless space in a given sentence
sentence = str(input("Enter a sentence: "))

valid_word = [",",";","'",".", "!", ":","?","-"] 
modified_sentence =""

for i in range(0,len(sentence)):
    if sentence[i]!=" ":
        modified_sentence += sentence[i]
    else:
        if i==len(sentence)-1 or sentence[i+1]!=" " and (sentence[i+1] not in valid_word and sentence[i+1]!=" "):
            modified_sentence += " "

print(modified_sentence)
# Creating a script that deletes all unnecessary spaces in a given sentence
sentence = str(input("Enter a sentence: "))

# List of valid punctuation marks and symbols that can appear between words
valid_word = [",", ";", "'", ".", "!", ":", "?", "-"]
modified_sentence = ""

# Iterating through each character in the sentence
for i in range(0, len(sentence)):
    # If the character is not a space
    if sentence[i] != " ":
        # Add the character to the modified sentence
        modified_sentence += sentence[i]
    else:
        # Check if it's the last character or the next character is not a space and not a valid punctuation mark
        if i == len(sentence) - 1 or sentence[i + 1] != " " and (sentence[i + 1] not in valid_word and sentence[i + 1] != " "):
            # Add a single space to the modified sentence
            modified_sentence += " "

# Print the modified sentence without unnecessary spaces
print(modified_sentence)
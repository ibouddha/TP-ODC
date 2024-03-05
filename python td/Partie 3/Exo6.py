#definition des couleurs
couleur = {
    "rouge" : "\033[91m",
    "vert" : "\033[92m",
    "bleu" : "\033[94m",
    "noir" : "\033[90m",
    "fin"  : "\x1b[0m"
}

#fonction saisie matrice
def matrice(n):
   # Loop through rows
   for i in range(n):
       # Loop through columns
       for j in range(n):
           # Print *
           print(f"*{' '}", end="")  # Print with space
       # Move to new line
       print()
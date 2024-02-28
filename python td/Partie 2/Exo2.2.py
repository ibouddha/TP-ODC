##
# Copyright (c) 2024-Petit Bouddha
# All rights reserved.
##

a = int(input("Donnez un entier: "))
ope = input("donnez l'operateur (+, -, * ou /): ")
b = int(input("Donnez l'entier qui va être utilisé en second operande :"))
if ope == "+":
    print(a + b)
elif ope == "-":
    print(a - b)
elif ope == "*":
    print(a * b)
elif ope == "/":
    if b != 0:
        print(a / b)
    else:
        print("Erreur division par zero")
else:
    print("Vous avez rentré un opérateur incorrect.")

#récupération de R1, R2, R3
##
# Copyright (c) 2024-Petit Bouddha
# All rights reserved.
##

R1 = int(input("Entrer la valeur de R1 : "))
R2 = int(input("Entrer la valeur de R2 : "))
R3 = int(input("entrer la valeur de R3 : "))

print('Menu:')
choix = input('1 - Calcule de la resistance en série \n 2 - Calcule de la resistance en parallele')

if choix == 1:
    print('\nCalcul de la résistance en série : ')
    resistance = R1 + R2 + R3
elif choix == 2:
    print('\nCalcule de la résistance en parallele')
    resistance = (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)
else:
    print('Vous n\'avez pas saisi une option valide')
    
print('La résistance est de ', resistance ,'ohms')
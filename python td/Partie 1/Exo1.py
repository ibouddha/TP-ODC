while(True):
    #recuperer les deux entiers
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    #verifier si l'un des deux est nul
    if (b!=0):
        result = a//b
        quotient = a%b
        ratio = a / b
        modulo = a % b
        break
#afficher le resultat
print(f"result:", result ,"\nquotient:", quotient ,"\nration:", ratio ,"\nmodulo: ", modulo)
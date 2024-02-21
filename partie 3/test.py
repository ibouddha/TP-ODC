n=input('entrer n')
#symbole = input('entrer un symbole')

for i in range(1, int(n)-1):
    for k in range(1,int(n)-i):
        print(' ', end= '*')  # On affiche des espaces pour ne pas avoir de saut de ligne
    
    for j in range(1,2*k+1):
        print('*')

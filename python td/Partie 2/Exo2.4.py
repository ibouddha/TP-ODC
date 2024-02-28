montant = int(input("Entrez le montant en euros : "))

billets_20 = montant // 20
reste = montant % 20

billets_10 = reste // 10
reste = reste % 10

billets_5 = reste // 5
reste = reste % 5

pieces_2 = reste // 2
pieces_1 = reste % 2

print("Billets de 20 euros :", billets_20)
print("Billets de 10 euros :", billets_10)
print("Billets de 5 euros :", billets_5)
print("Pièces de 2 euros :", pieces_2)
print("Pièces de 1 euro :", pieces_1)

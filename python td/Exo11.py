# Saisie des données du produit
libelle = input("Entrez le libellé du produit : ")
quantite_stock = float(input("Entrez la quantité en stock : "))
prix_unitaire = float(input("Entrez le prix unitaire : "))

# Calcul du montant en stock
montant_stock = prix_unitaire * quantite_stock

# Calcul du montant TTC
TVA = 0.18
montant_TTC = montant_stock + montant_stock * TVA

# Affichage des informations du produit et des montants
print("Produit : ", libelle)
print("Quantité en stock : ", quantite_stock)
print("Prix unitaire : ", prix_unitaire)
print("Montant en stock : ", montant_stock)
print("Montant TTC : ", montant_TTC)

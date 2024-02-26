#recuperer la temperature en degré celsius
a = input("donner la temperature en degre celsius: ")

resultat = int(a) * (9/5) + 32
formatted = "{:.2f}".format(resultat)
print(f"la temperature {a} degree Celsius est egale a {formatted} degree Fahrenheit")
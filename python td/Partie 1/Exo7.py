#recuperer les résistances R1, R2, R3
R1 = int(input("donner R1"))
R2 = int(input("donner R2"))
R3 = int(input("donner R3"))

serie = R1 + R2 + R3

parallele = (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)

print(f"la résistance en parallele est {parallele} et la résistance en série est {serie}")
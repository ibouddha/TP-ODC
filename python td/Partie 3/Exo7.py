#fonction permettant de convertir le caractere entré
def getEquiv(caractere):
    lib = {
        "a" : "2",
        "b" : "22",
        "c" : "222",
        "d" : "3",
        "e" : "33",
        "f" : "333",
        "g" : "4",
        "h" : "44",
        "i" : "444",
        "j" : "5",
        "k" : "55",
        "l" : "555",
        "m" : "6",
        "n" : "66",
        "o" : "666", 
        "p" : "7",
        "q" : "77",
        "r" : "777",
        "s" : "7777",
        "t" : "8",
        "u" : "88",
        "v" : "888",
        "w" : "9",
        "x" : "99",
        "y" : "999",
        "z" : "9999",
        " " : "00",
        "0" : "A",
        "1" : "B",
        "2" : "C",
        "3" : "D",
        "4" : "E",
        "5" : "F",
        "6" : "G",
        "7" : "H",
        "8" : "I",
        "9" : "J"
    }
    return lib.get(caractere)

text  = input("entrer un message:")
crypto = ""

for i in text.lower():
    if(i not in (",","'","’",";", ":", "!", "?", ".")):
        if len(crypto)>1 and getEquiv(i)[0] == crypto[-1] :
            crypto+="0"+getEquiv(i)
        else:
            crypto += getEquiv(i)
    else:
        crypto += i

print(crypto)
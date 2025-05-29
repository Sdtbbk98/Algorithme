#décomposation d'un nombre décimal en basse
nbr = int(input("Entrez un nombre pour convertir : "))
base = int(input("Entrez une base de conversion : "))
quotient = 1
while quotient != 0:
    quotient = (int) (nbr/base)
    reste = nbr - (quotient * base)
    nbr = quotient
    print(reste)


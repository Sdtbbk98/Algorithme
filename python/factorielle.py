mmo#Calcule de factorielle
# we can use  math library form math import factorial
def factorielle(nombre):
    res = 1
    if nombre < 2:
        return 1
    else:
        return nombre * factorielle(nombre -1)

# x = int (input("Entrez un nombre entier : "))
# resultat = factorielle(x)
# print('voici le factoriell de {0} = {1}'.format(x, resultat))
#un algorithmique améliorer pour trouver si un nombre est premier.
#la dificulter d'algotithmique est O*(racine de N)/2
#this function will stop whenever it find a nombre that it can be divided with so it wont go till the end of the numbre!
def nombre_premier_1(nbr):
    nbr_itération = 0
    trouve = False
    limite = (nbr ** 0.5) + 1 #on peut utiliser le sqrt de math library.
    if nbr != 2:
        reste = (int) (nbr%2)
        if reste == 0:
            trouve = True
            divisieur1 = 2
            divisieur2 = nbr/2
        else:
            i = 3 # on calcule les impaire maintenant
            while i<limite:
                nbr_itération += 1
                reste = (int) (nbr%i)
                if reste == 0:
                    trouve = True
                    divisieur1 = i
                    divisieur2 = (int) (nbr/i)
                i += 2
    else:
        print("le nbr doit supérieur que 2!")
    
    if trouve == True:
        print(nbr, "n'est pas un nombre premier!")
        print("il es divisible par", divisieur1, " et ", divisieur2, "voici les nombre de itération pour trouver ça", nbr_itération)
    else:
        print(nbr, "est un nombre premier!")

    

x = int(input("entrez un nombre pour trouver si c'est un nombre premier : "))
print("le résultat est: ", nombre_premier_1(x))

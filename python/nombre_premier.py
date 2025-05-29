#nombre premier qui divise par un et lui même example: 1,2,3,7,11,13...
#ici on a une chieffre 1000000001(un milliard un) on va voir si c'est un nombre premier ou pas.

#on va utiliser l'algorithmique linéaire 0(N) on va faire un milliard un calcule.
nbr_itérations = 0
nbr = int(input("Entrez un nombre : "))
if nbr < 2: print("nbr doit être supérieur à 1 car est un nombre premier.")
else:
    limite = nbr
    trouve = False
    for chiffre in range(2,limite):
        nbr_itérations += 1
        reste = (int) (nbr%chiffre)
        if reste == 0:
            trouve = True #donc c'est pas un nombre premier maintenat on va trouver les diviseurs.
            diviseur1 = chiffre #le chiffre sur lequel notre nbr est divisable.
            diviseur2 = (int) (nbr/chiffre) # le diviseur de notre chiffre est le diviseur.
        if trouve:
            print(nbr,"notre nombre n'est pas un nombre premier!")
            print("ils est divisible par ", diviseur1," et ", diviseur2)
        else:
            print(nbr, "est un nombre premier !")
        print("Résultat obtenu en ",nbr_itérations, " itérations")



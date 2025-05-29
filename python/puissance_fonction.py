#une fonction de la puissance avec troi variables.
#nome de la fonction: puissance()
#variables : nombre, exposant, res toutes en entier
def puissance(nombre, exposant, res):
    cmpt = 0
    resultat = 1
    while (cmpt < exposant):
        cmpt += 1
        resultat = resultat * nombre
    res.append(resultat)

n,exp = map(float, input("entre un nombre et son exposant : ").split())
exp = int(exp)
res_1 = []
puissance(n,exp,res_1)
print('{0:f} puissance {1:d} = {2:f}'.format(n,exp,res_1[0]))


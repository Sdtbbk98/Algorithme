#une code pour monter comment faire un puissance
num, puissance = map(float, input("entrez une nombre et sa puissance: ").split())
# .split() permet de séparer par un espace si on ne fait pas ca va causer une erreur.
puissance = int(puissance)
# on veut que la puissance soit un entier sinon on va compliquer les choses.
compteur = 0
res = 1
while compteur < puissance:
    compteur += 1
    res = res * num
# print(f"{num} puissance {puissance} est {res}")
print(num, "**", puissance, "=", res)

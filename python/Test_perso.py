# #une fonction qui montre si un nombre est premier ou pas.
# #et pour savoir le vittes et l'algorithmique on va compter les itérations aussi.
# def nombre_premier(nbr):
#     #nbr (int) le nombre que on va chercher trouver ses diviseurs

#     nbr_itération = 0
#     if nbr < 2: print("le nbr doit supérieur que un!")
#     #maintenat on va donner limiter notre recherche des diviseur
#     else:
#         limite = nbr
#         trouve = False
#         for diviseurs in range (2,limite):
#             nbr_itération += 1
#             reste = (int) (nbr%diviseurs)
#             if reste == 0:
#                 trouve = True
#                 diviseur1 = diviseurs
#                 diviseur2 = nbr/diviseurss
            
#             if trouve:
#                 print(nbr, "n'est pas un nombre premier!")
#                 print("il est divisible par ", diviseur1, " et ", diviseur2) 
#             else:
#                 print(nbr, "est un nombre premier!")
#         print("Résultat obtenu en ", nbr_itération, "itérations.")

"""
@author: animenosekai_
2020 ©Anime no Sekai - Maxence OSAWA
"""

print('') #juste pour espacer les résultats dans la console (ça ajoute une ligne qui ne contient rien)
print('')
print("#EXERCICE 49#") #j'annonce juste l'exercice
print('')

def puits(H): #je définis (démarre) la fonction/le programme
    M = 100 #je mets à 100 la variable M (le coût d'1 mètre supplémentaire) (je la réinitialise pour qu'elle est toujours la valeur 100 quand je lance le programme)
    S = 100 #je mets à 100 la variable S (le total) (je la réinitialise aussi)
    N = 1 #je mets à 1 la variable N (le nombre de mètres) (je la réinitialise aussi)
    while N<H: #tant que le nombre de mètres n'atteint pas celui choisi ( variable H ), continuer d'exécuter en boucle
        M = M + 40 #rajouter 40 à chaque mètre
        S = S + M #ajouter le coût du mètre au total
        N = N + 1 #rajouter 1 mètre au compteur de mètre
    return(S) #Donner le total

print("Voici le prix de 3 mètres creusés :", puits(3), '€') #j'annonce le résultat dans la console
print("Voici le prix de 8 mètres creusés :", puits(8), '€')
print("Voici le prix de 12 mètres creusés :", puits(12), '€')

print('')

def puitsOrganisation(H):
    M = 100
    S = 100
    N = 0
    while S<H: #tant que la somme totale n'atteint pas le budget, continuer d'exécuter en boucle
        M = M + 40
        S = S + M
        N = N + 1
    return(N) #Donner le nombre de mètres que le budget permet de creuser

print("Voici le nombre de mètres de profondeur du puits que l'organisation peut creuser avec son budget :", puitsOrganisation(4000)) #j'annonce le résultat dans la console

print('')

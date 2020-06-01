"""
@author: animenosekai_
2020 ©Anime no Sekai - Maxence OSAWA
"""

print('') #juste pour espacer les résultats dans la console (ça ajoute une ligne qui ne contient rien)
print('')
print("#EXERCICE 50#") #j'annonce juste l'exercice
print('')

def polluants(r,n): #je définis (démarre) la fonction/le programme
    while r>2000: #tant que la quantité de rejets polluants ne va pas en dessous de 2000 tonnes, continuer d'exécuter en boucle
        r = r * 0.92 #réduire de 8% (en multipliant par 0.92) la quantité de rejets polluants à chaque année
        n = n + 1 #rajouter 1 au compteur d'années
    return(n) #Donner le nombre d'années

print("Voici l'année à laquelle le groupe industrielle atteindra son objectif :", polluants(5000,0)) #Annoncer le résultat

print('')

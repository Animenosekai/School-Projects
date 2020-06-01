"""
@author: animenosekai_
2020 ©Anime no Sekai - Maxence OSAWA
"""
#'Importer' la racine carrée (square root) dans le programme pour pouvoir l'utiliser plus tard (dans l'exercice 3)
from math import sqrt

#Début du code
print(' ') #Cette ligne de code ne servira que pour sauter une ligne dans la console et ainsi avoir des résultats plus espacées
print(' ')
print(' ')

def exercice_1(): #Début d'un exercice (que j'effectue dans une fonction)
    print('#EXERCICE 10#') #Donne juste le numéro d'exercice dans la console
    print('1.') #Donne juste le numéro de question de l'exercice dans la console
    A = 'pa'
    B = A+A
    C = B+'maman'
    
    print("Voici ce qui s'affiche lorsque l'on demande B: ", B)
    print("Voici ce qui s'affiche lorsque l'on demande C: ", C)
    
    print(' ')
    
    print('2.')
    D = A+'radis'
    
    print("Voici ce qui s'affiche lorsque l'on demande len(D): ", len(D))
    print("Voici ce qui s'affiche lorsque l'on demande D[2]: ", D[2])
    
    print(' ')
    print(' ')
    print(' ')

def exercice_2():
    print('#EXERCICE 11#')
    x = 2;y = 3
    z = x+y+x*y
    z = z**2
    y = z/2
    
    print('1.')
    print("Voilà ce que l'on obtient en demandant x: ", x)
    print("Voilà ce que l'on obtient en demandant y: ", y)
    print("Voilà ce que l'on obtient en demandant z: ", z)
    
    print(' ')
    
    print('2.') 
    if z%2==0: #Si c'est pair (le reste de la division euclidienne est nul), mettre la variable 'checker' à True
        checker = True
    else: #Sinon la mettre à False
        checker = False

    if checker == True: #Si c'est True afficher que z est paire
        print("La variable 'z' est paire")
    else: #Sinon afficher que la variable est impaire
        print("La variable 'z' n'est pas pair (est impaire)")


    #Je ne fais que afficher dans la console ce que j'ai ajouter précédemment    
    print('')
    print('')
    print("Voici ce qui est ajouté au programme afin qu'une variable de type booléen teste si z est pair (la variable n'est pas réellement de type booléen mais renvoie True ou False): ")
    print('')
    print("if z%2==0:")
    print("    checker = True")
    print("else:")
    print("    checker = False")
    print('')
    print("if checker == True:")
    print("    print('La variable 'z' est paire')")
    print("else:")
    print("    print('La variable 'z' n'est pas pair (est impaire)')")

    print(' ')
    print(' ')
    print(' ')

def exercice_3():
    print('#EXERCICE 12#')
    print('1.')
    cote1 = 2
    cote2 = 5
    
    print('On considère que les côtés du triangle rectangle font respectivement ', cote1, 'et ', cote2) #Je donne juste les côtés
    
    aireTriangle = (cote1*cote2)/2 #Formule pour trouver l'aire d'un triangle
    print("L'aire de ce triangle est de ", aireTriangle)
    
    print(' ')
    
    print('2.')
    cote3 = sqrt(((cote1**2)+(cote2**2))) #J'utilise le théorème de Pythagore pour calculer le 3e côté (l'hypoténuse)
    perimetreTriangle = cote1 + cote2 + cote3 #J'additionne juste les différents côtés
    perimetreTriangle = round(perimetreTriangle, 2) #J'arrondis le résultat pour pas que ça fasse un chiffre interminable
    
    print("Le périmètre de ce triangle est de (environ) ", perimetreTriangle)
    
    print(' ')
    print(' ')
    print(' ')


def exercice_4():
    print('#EXERCICE 13#')
    #trouver la formule
    x = 12; y = 7
    u = x+y         #premier calcul
    v = x**2-y**2   #second calcul
    w = v%u #Rappel: '%' (modulo) donne le reste de la division euclidienne

    print('1.')
    print("La variable w a pour valeur: ", w)
    
    print(' ')
    
    print('2.')
    x = 3; y = 1
    u = x+y         #premier calcul
    v = x**2-y**2   #second calcul
    w = v%u
    
    print("La variable w a pour valeur: ", w)
    
    print(' ')

    print('3.')
    print('(x^2 - y^2) factorisé donne (x-y)*(x+y)')
    print("Donc V = u*(x-y)")
    print("Ainsi v % (modulo) u = 0")
    
    print(' ')
    print(' ')
    print(' ')

    
def exercice_5():
    print('#EXERCICE 14#')
    
    print('1.')
    def f(x):
        return(3*x-1)
    
    print('a.')
    print('Voici le résultat de f(1): ', f(1))
    print('Voici le résultat de f(-2): ', f(-2))

    print('b.')
    print("Cette fonction permet de faire le triple de x puis d'y soustraire 1")
    print('(Elle permet de calculer une fonction affine)') #de formule ax+b

    print(' ')

    print('2.')
    def affine(a,x,b):
        return(a*x+b)
    
    print('a.')
    print("Les arguments de cette fonction sont a, x et b") #Les arguments sont les valeurs qui vont pouvoir changer lorsqu'on va demander une fonction dans la console

    print('b.')
    print('Le résultat est: ', affine(1,2,3))

    print('c.')
    print("'affine(2,1,3) == 7' retourne dans la console: ", affine(2,1,3)==7) #Cela retournera False car '==' sert à vérifier si c'est égal (on double le signe = pour faire une vérification)
    
    print(' ')
    print(' ')
    print(' ')

print(exercice_1(), exercice_2(), exercice_3(), exercice_4(), exercice_5()) #J'affiche les résultats des exercices dans la console
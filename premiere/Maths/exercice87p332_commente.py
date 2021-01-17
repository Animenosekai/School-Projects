"""
Exercice 87 p.332
"""
from random import * # j'importe tout ce qui se trouve dans le module "random" (module qui permet de générer des choses pseudo-aléatoirement)

def sauts(n): # je définis la fonction (la fonction commence là)
    """
    Cette fonction retourne le nombre de fois où la puce est passé sur le point 0 en sautant n fois
    """
    p = 0 # je créer une variable p et je lui donne une valeur de 0
    k = 0 # je créer une variable k et je lui donne une valeur de 0
    for i in range(1, n + 1): # je vais exécuter tout ce qui se passe en dessous de moi "n" fois
        d = randint(0, 1) # je choisis un nombre au hasard entre 0 et 1
        if d == 0: # 0 ici correspond à "gauche" --> donc si  je vais à gauche
            p = p - 1 # alors j'enlève 1 à ma position
        else: # sinon
            p = p + 1 # j'augmente de 1 ma position
        if p == 0: # si je suis sur la position 0
            k = k + 1 # alors j'enregistre que je suis passé sur 0 une fois de plus
    return k # je retourne le nombre de fois où la puce est passé sur la position 0

"""
Explication des variables
p est la position de la puce
k est le nombre de fois où la puce est passée sur la position 0
d est une valeur, soit 0 (gauche), soit 1 (droite) qui détermine "aléatoirement" si la puce va à gauche ou à droite

Réponses:
a. p est la position de la puce tandis que k est le nombre de fois où la puce est passée sur la position 0
b. d est la valeur aléatoire, créé à chaque fois qu'on execute le code dans la boucle, qui est un entier entre 0 et 1 qui détermine si la puce va à gauche (0) soit à droite (1)
c. Pour simuler dix déplacements, il faut appeler la fonction "sauts" en lui donnant n=10:
J'execute le programme:
    python -i nom_du_programme.py
J'entre:
    sauts(10)
La machine me renvoie le résultat:
    1

c. et d.
Pour donner le parcours effectué, il faut changer un peu le programme en lui rajoutant des "print()" pour qu'il affiche la position à chaque fois que se lance le code dans la boucle et pour afficher à la fin où la puce s'arrête:
"""
def sauts(n):
    """
    Je reprends exactement le même programme
    """
    p = 0
    k = 0
    for i in range(1, n + 1):
        d = randint(0, 1)
        if d == 0:
            print("La puce va à gauche")
            p = p - 1
        else:
            print("La puce va à droite")
            p = p + 1
        if p == 0:
            k = k + 1
    print("La position de la puce lorsqu'elle s'arrête est: " + str(p)) # str() sert juste à convertir le nombre entier (int) en une chaîne de caractères (string) pour pouvoir rassembler le message de début et le nombre
    print("Elle est passée " + str(k) + " fois sur la position 0")
    return k

# je lance la fonction en simulant 10 déplacements
sauts(10)
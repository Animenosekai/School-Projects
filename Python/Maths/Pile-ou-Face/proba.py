### 						Proba
### by Anime no Sekai
### 2020

"""
Je pourrais améliorer la fonction avec par exemple des try-error pour ne plus avoir d'erreur d'entrée de la part de l'utilisateur mais j'ai essayé de garder un code relativement simple et facile à commenter.
"""

# Imports
import random # Pour ajouter de l'hasard/aléatoire
from time import sleep # Pour attendre et laisser respirer l'utilisateur
import os # Pour supprimer les messages de la console

# Fonction
def main():
	os.system('clear')
	print('Combien de fois voulez-vous faire lancer la pièce?')
	nombre = input('> ') # Demander le nombre de fois que l'on va "lancer" la pièce, input() demande à l'utilisateur d'écrire quelque chose.
	
	# int() est utilisé sur la variable nombre parce que input() sort une variable de type string (un mot, une phrase et pas un nombre entier)

	résultats = [] # La liste de résultats
	print('Please wait...')
	for i in range (int(nombre)): # On boucle un nombre de fois défini précédemment (le nombre que l'on a demandé à l'utilisateur)
		aléatoire = random.randint(0,1) # Un nombre aléatoire entre 0 et 1
		résultats.append(aléatoire) # Ajouter le résultat à la liste de résultats
		#print(aléatoire) # Montrer le nombre aléatoire
		#sleep(0.5) # Attendre une seconde pour l'utilisateur

	os.system('clear') # Supprimer les précédents messages, os.system() est utilisé pour entrer une commande système
	print('Voici les résultats:')
	#print(résultats) # Annoncer les résultats
	sleep(1) # Attendre une seconde
	nombre_de_pile = 0 # J'initialise les variables
	nombre_de_face = 0
	for i in range(int(nombre)): # Je boucle le nombre de fois prédéfini par l'utilisateur (comme avant)
		if résultats[i] == 0: # Si c'est pile
			nombre_de_pile += 1 # Ajouter 1 au nombre de fois qu'il y a eu pile, " += " c'est égal à nombre_de_pile =  nombre_de_pile + 1
		elif résultats[i] == 1: # Si c'est face
			nombre_de_face += 1 # Ajouter 1 au nombre de fois qu'il y a eu face

	print('')
	print('Voici le nombre de piles: ' + str(nombre_de_pile))
	print('Voici le nombre de faces: ' + str(nombre_de_face))
	print('')

	proba_de_pile = nombre_de_pile / int(nombre) # Je divise sur l'univers pour obtenir la proba
	proba_de_face = nombre_de_face / int(nombre)
	pourcentage_de_proba_de_pile = proba_de_pile * 100 # Je multiplie par 100 pour l'avoir en pourcentage
	pourcentage_de_proba_de_face = proba_de_face * 100

	print('')
	# str() est utilisé ici parce qu'on ne peut pas mélanger des variables de type string et des variables de nombres entiers.
	print('Il y a eu ' + str(pourcentage_de_proba_de_pile) + '% de résultats piles') # Annoncer les résultats
	print('Il y a eu ' + str(pourcentage_de_proba_de_face) + '% de résultats faces')
	sleep(2)
	print('')
	end = input('Appuyez sur entrée pour recommencer ou entrez quit pour quitter... ') # Demander si l'utilisateur veut recommencer
	if end.lower() == 'quit' or end.lower() == 'stop': # Si il dit stop ou quit, lower() désigne ici ce qu'a entré l'utilisateur sans majuscules.
		print("Merci d'avoir essayé ce programme!")
		quit() # Quitter
	else: # Sinon
		main() # Redémarrer la fonction

# Démarrer la fonction quand on lance le programme
main()

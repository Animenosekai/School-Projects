'''
Explication du programme:
- J'ai d'abord converti toutes les virgules des données en points dans les fichiers data-lambda-etoile-polaire.txt et data-intensite-etoile-polaire.txt
- Je vérifie que les installations des modules ont bien été faites (ce que vous voyez juste en bas avec # IMPORTS)
- J'ouvre chaque fichier (avec Python) pour pouvoir faire une boucle qui va lire chaque ligne des fichiers et ajouté chaque ligne à une liste. (le [:-1] est là pour enlever le saut de ligne qui est considéré comme un caractère dans python)
- A l'aide de matplotlib, je trace les données que j'ai obtenu (les listes de données)

lifeeasy est une librairie que j'ai codé moi-même et qui me sert pour raccourcir mes codes.

© Anime no Sekai - 2020
'''

from subprocess import check_output # Using this import just to install the dependencies if not.

# IMPORTS
try:
    import lifeeasy
    import matplotlib.pyplot as plt
except:
    print('It is the first time launching the program')
    print('Installing the dependencies...')
    command_output = check_output(["pip", "install", "lifeeasy", "matplotlib"], universal_newlines=True)
    import lifeeasy
    import matplotlib.pyplot as plt
    print('Successfully installed the dependencies!')
    lifeeasy.sleep(2)

lifeeasy.clear()
lifeeasy.display_action('Retrieving data from data-lambda-etoile-polaire.txt')
lambda_data = []

# Open file for reading
file = open(lifeeasy.working_dir() + "/data-lambda-etoile-polaire.txt")
# Read the first line from the file
line = file.readline()
# Initialize counter for line number
line_no = 1

# Loop until EOF (fin)
while line != '' :
    lambda_data.append(float(line[:-1]))
    line = file.readline()  
    line_no += 1
    
# Close the file
file.close()

lifeeasy.clear()
lifeeasy.display_action('Retrieving data from data-intensite-etoile-polaire.txt')
intensite_data = []

# Open file for reading
file = open(lifeeasy.working_dir() + "/data-intensite-etoile-polaire.txt")
# Read the first line from the file
line = file.readline()
# Initialize counter for line number
line_no = 1

# Loop until EOF (fin)
while line != '' :
    intensite_data.append(float(line[:-1]))
    line = file.readline()  
    line_no += 1
    
# Close the file
file.close()



#### JE TRACE

lifeeasy.clear() # JE NETTOIE LA CONSOLE
lifeeasy.display_action('Plotting') # J'ANNONCE QUE JE TRACE A L'UTILISATEUR AVEC MA LIBRAIRIE

plt.ylabel('Intensité')
plt.xlabel('Wavelength, in nm')
plt.title("Données de l'étoile polaire - Activité 3 p.274")
plt.plot(lambda_data, intensite_data, c=[101/255.0, 191/255.0, 247/255.0], linestyle='-', marker='o')
plt.show()
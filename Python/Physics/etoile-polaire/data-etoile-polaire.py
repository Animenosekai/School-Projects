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

# Loop until EOF
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

# Loop until EOF
while line != '' :
    intensite_data.append(float(line[:-1]))
    line = file.readline()  
    line_no += 1
    
# Close the file
file.close()

lifeeasy.clear()
lifeeasy.display_action('Plotting')
plt.ylabel('Intensité')
plt.xlabel('Wavelength, in nm')
plt.title("Données de l'étoile polaire - Activité 3 p.274")
plt.plot(lambda_data, intensite_data, c=[101/255.0, 191/255.0, 247/255.0], linestyle='-', marker='o')
plt.show()
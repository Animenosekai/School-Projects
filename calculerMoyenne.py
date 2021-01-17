from json import loads
from requests import post

## https://api.ecoledirecte.com/v3/eleves/483/notes.awp?verbe=get&
#token = "something"
#token = input("Enter your token >> ")
#request = post("https://api.ecoledirecte.com/v3/eleves/483/notes.awp?verbe=get&", {"token": token}, headers={"Content-Type": "application/x-www-form-urlencoded", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.ecoledirecte.com/Eleves/483/Notes", "Content-Length": "3030", "Origin": "https://www.ecoledirecte.com", "Accept": "application/json, text/plain, */*"})
#print(request)
#print(request.text)
#notes = loads(request.text)["data"]["notes"]
with open("resultat_api.json") as f:
    notes = loads(f.read())["data"]["notes"]
premierTrimestre = []
premierTrimestre_coef = 0
deuxiemeTrimestre = []
deuxiemeTrimestre_coef = 0
troisiemeTrimestre = []
troisiemeTrimestre_coef = 0

for devoir in notes:
    note = float(str(devoir["valeur"]).replace(",", "."))
    sur = float(str(devoir["noteSur"]).replace(",", "."))
    note = (note/sur) * 20
    coef = float(str(devoir["coef"]).replace(",", "."))
    if devoir["codePeriode"] == "A001":
        premierTrimestre.append(note)
        premierTrimestre_coef += coef
    elif devoir["codePeriode"] == "A002":
        deuxiemeTrimestre.append(note)
        deuxiemeTrimestre_coef += coef
    elif devoir["codePeriode"] == "A003":
        troisiemeTrimestre.append(note)
        troisiemeTrimestre_coef += coef
    
if premierTrimestre_coef != 0:
    moyennePremier = sum(premierTrimestre) / premierTrimestre_coef
else: moyennePremier = 0
if deuxiemeTrimestre_coef != 0:
    moyenneDeuxieme = sum(deuxiemeTrimestre) / deuxiemeTrimestre_coef
else: moyenneDeuxieme = 0
if troisiemeTrimestre_coef != 0:
    moyenneTroisieme = sum(troisiemeTrimestre) / troisiemeTrimestre_coef
else: moyenneTroisieme = 0
print("Votre moyenne pour le premier trimestre est de: " + str(round(moyennePremier, 2)))
print("Votre moyenne pour le deuxième trimestre est de: " + str(round(moyenneDeuxieme, 2)))
print("Votre moyenne pour le troisième trimestre est de: " + str(round(moyenneTroisieme, 2)))

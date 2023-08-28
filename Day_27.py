import random, os, time#importation de bibliothèque permettant de générer un nombre aléatoire, néttoyer le prompteur, gérer le temps d'appel
def rollSided(sides): #Fonction permet de générer un nombre aléatoire
  result= random.randint(1, sides)
  return result

def health():#fonction permettant de générer les point de santé par rapport au nombre aléatoire
  health_6 = rollSided(6)
  health_12 = rollSided(12)
  healthStat = (((health_6 * health_12)/2) +10)
  return healthStat

def strength():#permet de généré les point de force par rapport au nombre aléatoire
  strength_6 = rollSided(6)
  strength_8 = rollSided(8)
  strengthStat = (((strength_6 *strength_8)/2)+12)
  return strengthStat
  
while True:#Permet aux fonctions précédemment définies de s'exécuter
  print("⚔️ CHARACTER BUILDER ⚔️")
  print()
  name = input("Name your legend:\n ")
  character = input("Choose your character type from the list below: Human, Elf, Wizard, Orc:\n")
  print()
  print("HEALTH", health())
  time.sleep(3)
  print("STRENGTH", strength())
  print("May your name go down in Legend...")
  again =input("Try again? :")
  if again == "no" or again == "No":
    break
    time.sleep(5)
    os.system("clear")
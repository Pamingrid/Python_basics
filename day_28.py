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
#identifier les deux joueurs du jeux
player1 = input("Name your legend:\n ")
character1 = input("Character Type (Human, Elf, Wizard, Orc):\n")
health_1 = health()
strength_1 = strength()
print("Who are they battling?")
print()
player2 = input("Name your legend:\n ")
character2 = input("Character Type (Human, Elf, Wizard, Orc):\n")
health_2= health()
strength_2= strength()
round = 1
winner = None

while True:#Permet aux fonctions précédemment définies de s'exécuter et aux joueurs de compétir
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  player_1_Health = rollSided(6)
  player_2_Health = rollSided(6)

  difference = abs(strength_1 - strength_2) + 1

  if player_1_Health > player_2_Health:
    health_2 -= difference
    if round == 1: 
      print(player1, "wins the first blow")
    else:
      print(player1, "wins round", round)
  elif player_2_Health > player_1_Health:
    health_1 -= difference
    if round == 1:
      print(player2, "wins the first blow")
    else:
      print(player2, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)
  
  print()
  print(player1)
  print("HEALTH:", player_1_Health)
  print()
  print(player2)
  print("HEALTH:", player_2_Health)
  print()

  if player_1_Health <= 0:
    print(player1, "has died!")
    winner = player2
    break
  elif player_2_Health <= 0:
    print(player2, "has died!")
    winner = player1
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    

time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
    
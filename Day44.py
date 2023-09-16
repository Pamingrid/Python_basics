import random, os, time
bingo =[]

def ran():
  number = random.randint(0,90)
  return number
  
def printnumber():
  for row in bingo:#Afficher la ligne Bingo
    for item in row:#afficher séparemment chaque élément de la ligne
      print(item, end="\t |\t ") # veux dire je veux un nombre de 10 caractères d'espaces entre chaques items
    print()
  print()

def createCard():
  global bingo
  numbers=[]
  for i in range (8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())
  numbers.sort()
  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BINGO", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]
  
createCard()
while True:
  printnumber()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"

  exes = 0
  for row in bingo:
    for item in row:
      if item=="X":
        exes+=1

  if exes == 8:
    print("You have won")
    break

os.system = "Clear"
time.sleep = 1
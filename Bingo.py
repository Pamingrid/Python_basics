import random
bingo =[]

def ran():
  number = random.randint(0,90)
  return number
  
def printnumber():
  for row in bingo:
    print(row)

numbers=[]
for i in range (8):
  numbers.append(ran())

numbers.sort()

bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]
printnumber()
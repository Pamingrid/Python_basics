def coloring(color):
  if color== "r":
    print('\033[0;31m', end='') #red
  elif color == "":
    print('\033[0m', end='') #back to default
  elif color == "b":
    print('\033[0;34m', end='')#blue
  elif color == "g":
    print('\033[0;32m', end='') #green
  elif color == "p":
    print('\033[1;37m', end='') #white
  elif color == "y":
    print('\033[0;35m', end='') #purple

sentence = input("What sentence do you want rainbowizing?: ")
for letter in sentence:
  coloring(letter.lower())
  print(letter, end="")
print()
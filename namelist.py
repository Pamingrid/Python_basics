import os, time
listName = []

def printName():
  print()
  for name in listName:
    print(name)
  print ()

while True:
  firstName = input("What is your first name?\n").capitalize().strip()
  lastName = input("What is your last name?\n").capitalize().strip()
  name = f"{firstName} {lastName}"
  if name not in listName:
    listName.append(name)
  else:
    print("Error Duplication")
  printName()
  time.sleep(2)
  os.system("clear")
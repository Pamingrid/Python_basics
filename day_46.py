mokeBeast = {}

def prettyPrint():
  print()
  for key, value in mokeBeast.items():
    print (key, end = ":")
    for subKey, subValue, in value.items():
      print(subKey, subValue, end = " | ")
    print ()

while True: 
  print ("🌟MokeBeast Generator🌟\n")
  name = input ("Input the beast name >")
  element = input("Input the beast element >")
  specialMove= input("Input the beast special move >")
  startingHP= int(input("Input the beast starting HP"))
  startingMP= int(input("Input the beast starting MP"))
  
  mokeBeast[name]= {"Element": element,"Special Move": specialMove, "Starting HP": startingHP, "Starting MP": startingMP}
  
  prettyPrint()
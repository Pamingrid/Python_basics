exit = "no"
while exit == "no" or exit == "No":
  animal=input("What animal sound do you want to hear? ")
  if animal == "Cow" or animal == "cow":
    print(f"The {animal} goes moooooo.")
  elif animal == "Cat" or animal == "cat":
    print(f"The {animal} goes miaou.")
  elif animal == "pig" or animal == "Pig":
    print(f"The {animal} goes grouigroui")
  elif animal == "dog" or animal == "Dog":
    print(f"The {animal} goes Wouf wouf.")
  else:
    print(f"The {animal} sound is not recorded on my list.")
  exit=input("Do you want to exit? ")

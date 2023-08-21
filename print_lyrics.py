print("""
Fill in the blank lyrics!
Type in the blank lyrics and see if you are as cool as me.
""")
counter = 1
while True:
  print("Je prierai, je prierai, je prierai")
  lyrics = input("Missing word : ")
  if lyrics == "car si je ne prie pas le diable s'attachera à moi" or lyrics == "Car si je ne prie pas le diable s'attachera à moi":
    print("Le matin je prierai")
  else:
    print("It's not the word! Try again")
    counter +=1
    if lyrics == "Même la nuit je prierai":
      break
  print("Thanks for playing")
print("Well done! It only took you", counter, "attempts.")

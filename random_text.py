import random, os, time
print("🌟Hangman🌟")
listOfWord=["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
letterPicked = []
lives = 6

wordChosen = random.choice(listOfWord)

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Type in a letter: ").lower()
  
  if letter in letterPicked:
    print("You've tried that before")
    continue
    
  letterPicked.append(letter)
  
  if letter in wordChosen:
    print("You found a letter")
  else:
    print("Nope, not in there")
    lives -= 1

  allLetters = True
  print()
  for i in wordChosen:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print(f"You won with {lives} left!")
    break

  if lives<=0:
    print(f"You ran out of lives! The answer was {wordChosen}")
    break
  else:
    print(f"Only {lives} left")
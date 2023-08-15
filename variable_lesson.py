print("What is your Name")
myName=input("My name is ")
print("What is your favorite food ? ")
my_favorite_food=input("My favorite food is ")
print("What is your favorite music ")
my_favorite_music=input("My favorite music is ")
print(f"You have the same name as my brother, he also like {my_favorite_food} and {my_favorite_music} as you it's quite interesting")

import emoji
myScore=int(input("Your score:"))
if myScore >= 100000:
  print("Winner!")
else:
  print(emoji.emojize("Try aigain :crying_face:!!!"))
myPi=float(input("What is the value of Pi?"))
if myPi == 3.142:
  print(emoji.emojize("Good job:major_finger_up"))
else:
  print("Invalid proposal")


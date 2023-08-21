import random
print("Totally Random One-Million-to-One")
attempt = 0
myNumber = random.randint(1,1000001)
while True:
  answer=int(input("What is your guest? : "))
  if answer < myNumber:
    print("Too low")
    attempt+=1
  elif answer > myNumber:
    print("Too high")
    attempt+=1
    continue
  elif answer == myNumber:
    print("Correct")
    attempt+=1
    break
    exit()
  else:
    print("That number is not recognize !")
print("It took you", attempt, "attempt(s) to get the correct answer.")
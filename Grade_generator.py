testName=input("What is the name of the test?")
print("Welcome on {testName} grade Calculator !!!")
maxScore=int(input("What is the maximum score you could receive? "))
yourScore=int(input("What is the score you receive? "))
percentage = round((float(yourScore/maxScore)*100), 2)
if percentage > 90:
  print("Your grade is A+, you scored", percentage, "%")
elif percentage > 89:
  print("Your grade is A, you scored", percentage, "%")
elif percentage > 79:
  print("Your grade is B, you scored", percentage, "%")
elif percentage > 69:
  print("Your grade is C, you scored", percentage, "%")
elif percentage > 59:
  print("Your grade is D, you scored", percentage, "%")
else :print("Your grade is U, you scored", percentage, "%")
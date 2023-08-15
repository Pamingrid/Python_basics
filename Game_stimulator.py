print("""
      Welcome to rock, paper, scissors game!!!
      Rules of this rock, paper, scissors game are the following.
      Rock is represented by the letter R.
      Paper is represented by the letter P.
      Scissors by the letter S.
      """)
rock = "R"
scissors = "S"
paper = "P"
playerOne=input("What is your name?")
playerTwo=input("What is your name?")
print(f" This tournament will oppose {playerOne} to {playerTwo}, Goodluck !!!")
from getpass import getpass as input
answerPlayerOne=input("Make your choise:")
answerPlayerTwo=input("Make your choise")
print("The play is done")
if answerPlayerOne == "R" and answerPlayerTwo == "P":
    print(f"{playerOne} scored {answerPlayerOne} and {playerTwo} scored {answerPlayerTwo}. The paper rob the rock, {playerOne} won.")
elif answerPlayerOne == "S" and answerPlayerTwo == "P":
    print(f"{playerOne} scored {answerPlayerOne} and {playerTwo} scored {answerPlayerTwo}. The scissors cut the paper, {playerOne} won.")
elif answerPlayerOne == "P" and answerPlayerTwo == "S":
    print(f"{playerOne} scored {answerPlayerOne} and {playerTwo} scored {answerPlayerTwo}. The scissors cut the paper, {playerTwo} won.")
else:
    print(f"You are tied, you both played {answerPlayerOne}")
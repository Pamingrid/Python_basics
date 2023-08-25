from replit import audio#I use a library from replit.com
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_music=int(input("Press 2 to exit: "))
    if play == 2:
      source.paused=True
      return 
    else:
      continue
# Start taking user input and doing something with itinput(" Do you want to play music")

while True:
  os.system("clear")# clear the screen
  print("MyPOD Music Player")
  time.sleep(5)
  print("Press 1 to play")
  time.sleep(5)
  print("Press 2 to Exit ")
  time.sleep(5)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing music!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue


  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input

def color_to_print(color, word):
  if color == "red":
    print("\033[31m", word, sep="", end="")
  elif color == "green":
    print("\033[32m", word, sep="", end="") #green
  elif color == "yellow":
    print("\033[33m", word, sep="", end="") #yellow
  elif color == "cyan":
    print("\033[1;36m", word, sep="", end="")#cyan
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print()
print("Whith my",end=" ")
color_to_print("yellow", "new program ")
color_to_print("reset", "I can just call red ")
color_to_print("red", "('and') ")
color_to_print("reset","that wordk will appear in the color I set it to.")
print("\n")
color_to_print("reset", "With no ")
color_to_print("cyan", "weird gaps")
color_to_print("reset",".")
print("\n")
print("Epic")
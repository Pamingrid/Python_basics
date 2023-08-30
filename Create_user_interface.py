def coloring(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m") 

text = f"{coloring('red')}={coloring('white')}={coloring('blue')}= {coloring('yellow')}Music App {coloring('blue')}={coloring('white')}={coloring('red')}="

print(f"               {text:^35}")
print(f"🔥 ▶ \t{coloring('white')} Radio Gaga")
print(f"{coloring('yellow')} Queen")
print()

prev = "PREV"
next= "NEXT"
pause = "PAUSE"
print(f"{coloring('white')}{prev:<35}")
print(f"\t {coloring('green')}{next:^35}")
print(f"\t{coloring('purple')}{pause:>35}")
      
print()
print()

title =f"{coloring('white')} WELCOME TO \n {coloring('blue')} --\tARMBOOK\t-- \n {coloring('yellow')} Definitely not a rip off of a certain oter social networking site. \n {coloring('red')} Honest."
print(f"        {title :>35}")
print()
text = "Username: "
username = input(f"{coloring('white')}{text:^35}").capitalize
text = "Password: "
username = input(f"{coloring('white')}{text:^35}").capitalize

print("🌟 Website Rating 🌟")
website = {"name":None, "url": None, "content":None, "rate":None}
for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")

#day 42 challenge :This challenge is all about using dictionaries to create a game about small creatures that you have captured, enslaved, and forced to fight for your amusement. You monster.
#This game works in a completely non-copyright and totally lawyer friendly way. Pika-who? I have absolutely no idea what you mean..... officer.
print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()
gaming = {"Beast Name": None, "Beast Type":None, "Special move":None, "HP":None, "MP":None}
for name in gaming.keys():
  gaming[name]= input(f"{name}:\t").strip().title()

if gaming["Beast Type" ] == "Earth".split():
  print("\033[0;33m", end="")#brown
elif gaming["Beast Type"] == "Fire".split():
  print("\033[1;33m", end="")#yellow
elif gaming["Beast Type"] == "Water".split():
  print("\033[1;36m", end="")#cyan
elif gaming["Beast Type"] == "Air".split():
  print("\033[1;30m", end="")#dark gray
else:
  print("\033[33m", end="")

print()
for name, value in gaming.items():
  print(f"{name:<15}:{value}")
import os, time
print("🌟Life Organizer🌟")
to_do_list=[]

def add():
  time.sleep(1)
  os.system("clear")
  name =input("What is the task? >")
  priority= input("What is the priority? > ").capitalize()
  date= input("When is it due by? >")
  todo= [name, date, priority]
  to_do_list.append(todo)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  option = input("1: all\n2: By Priority\n>") 
  if option =="1":
    for todo in to_do_list:
      for item in todo:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? >")
    for todo in to_do_list:
      if priority in todo:
        for item in todo:
          print(item, end = " | ")
        print()
      print()
    time.sleep(1)
    
def edit():
  time.sleep(1)
  os.system("clear")
  new = input("What do you want to edit?\n")
  news = False
  for todo in to_do_list:
    if new in todo:
      news = True
    if not news:
      print(f"{new} does not exist in the list")
      return
  for todo in to_do_list:
    if new in todo:
      to_do_list.remove(todo)
  name =input("What is the task? >")
  priority= input("What is the priority? > ").capitalize()
  date= input("When is it due by? >")
  todo=[name, date, priority]
  to_do_list.append(todo)
  print ("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  new = input("What would you like to remove? ")
  for todo in to_do_list:
    if new in todo:
      to_do_list.remove(todo)
    else:
      print("It does not exist")
  

while True:
  menu = input("Welcome to the life organizer. Do you want to (1) add, (2) view, (3) edit or (4) remove a to do?\n")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()
    time.sleep(1)
    os.system("Clear")

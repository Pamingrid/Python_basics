import os, time
to_do_list=[]

def printList():
   print()
   for item in to_do_list:
     print(item)
     print()

while True:
  menu = input("Do you want to view, add, or edit your to do list ? : ")
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What should I add to the todo list? : ")
    to_do_list.append(item)
    print(f"Your actual todo list count :", {item})
  elif menu == "edit":
    item = input("What should I edit to the todo list? :")
    if item in to_do_list:
        to_do_list.remove(item)
    print(f"The remaining activities are: {printList()}")
    os.system("clear")
    time.sleep(3)
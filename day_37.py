import os, time
print("💥Star Wars Name Generator💥")
firstName = input("Input your first name : ")
lastName = input("Input your lastname : ")
maidenName= input("Input your mother's maiden name: ")
city = input("Input the city where you were born: ") 
name = f"{firstName[:3]}{lastName[:3]}"
id = f"{maidenName[:2]}{city[-3:]}"
print(f"your Star Wars name is {name.capitalize()} {id.capitalize()}")
time.sleep(1)
os.system("clear")
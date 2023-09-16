print("🌟Contact Card💥")
name= input("Input your name: ")
birthDate= input("Input your date of birth:")
phoneNumber=input("Input your telephone number: ")
email= input("Input your email:")
adress= input("Input your address: ")
myUser={"name":name, "birthDate":birthDate, "phoneNumber": phoneNumber, "email":email, "adress":adress}
print("Hi",myUser["name"], ". Our dictionary says that you were born on ", myUser["birthDate"], ",we can call you on", myUser["phoneNumber"], ", email", myUser["email"], "or write to The Cupboard Under The Stairs, Replit Towers, NY.")

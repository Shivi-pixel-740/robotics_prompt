#I learned the elif command and elif statement must go in between 'if' and 'else'. 

print("SECURE LOGIN")
Username = input ("Enter Username: ")
Password = input ("Enter Password: ")
if Username == "Crystal" and Password == "12345":
    print("Sucessful Login, I hope you have a nice day!")
elif Username == "Jake" and Password == "J234": 
    print("Sucessful Login, Thankyou for opening me!")
elif Username == "Mack" and Password == "M345":
    print("Sucessful Login, I am happy to see you!")
else: 
    print("Unsucessful Login, Try again")

#I learned how to print colors and understanding my mistakes. My mistake was that I forget to enter 3 quotation mark to a big text. 

print ("Welcome to my adventure game!")
print ("I am going to ask you a series of questions and you will have to answer them in order to survive.")
print ()
Name = input("What is your name?")
print ()
Hate = input("What is something you hate?")
print ()
Friend = input("What is the name of your best friend?")
print ()
Item = input("Do you have a red ruby in your house?")
print()
print("Hello", Name, """I understand why you hate it and I asked about it because I wanted to be a bit more personal""","\033[31m",  Hate, """I also understand that you have a best friend named""","\033[30m", Friend,"\033[34m","""and the red ruby was to test your honesty and I asked about it because, I wanted to know if you had a red ruby in your house""", Item,)

print("Thank you for you time and I hope you have a great life!")
